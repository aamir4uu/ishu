#!/usr/bin/env python3
"""
zerogpt_preflight.py - measure the signals ZeroGPT-class detectors key on.

ZeroGPT's DeepAnalyse engine scores text sentence by sentence and leans on two
statistical properties plus a bag of surface markers:

  perplexity  - how predictable the next word is. Low = machine-like.
  burstiness  - how much sentence length and structure varies. Low = machine-like.

We cannot compute true perplexity without a language model, so this script
measures the proxies that correlate with it and that we can actually control
while writing: length variance, opener repetition, contraction rate, marker
vocabulary, and punctuation tics.

Usage:
    python3 zerogpt_preflight.py FILE.md [--json] [--verbose]

Exit codes:
    0  all gates pass
    1  one or more gates fail (see report)
"""

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

# ---------------------------------------------------------------- thresholds
# Calibrated against human editorial prose. Tighten as reports come in;
# record every change in references/learning-log.md with the report that
# justified it.
GATES = {
    "sentence_cv_min": 0.45,        # stdev/mean of sentence word counts
    "clustered_max_pct": 40.0,      # % of sentences within +/-4 words of mean
    "short_sentence_min_pct": 12.0, # % of sentences under 9 words
    "long_sentence_min_pct": 12.0,  # % of sentences over 24 words
    "opener_repeat_pct_max": 9.0,   # % of sentences sharing one first word
    "opener_repeat_floor": 3,       # never fail below this raw count (short texts)
    # Sentence endings. Verb-final languages cluster here the way English
    # clusters at the opener, and the two need different ceilings. Both values
    # are PROVISIONAL: forced by one report, with no human-written baseline
    # behind them yet. See references/learning-log.md.
    "closer_repeat_pct_max": 12.0,          # non-Devanagari drafts
    "closer_repeat_pct_max_devanagari": 30.0,
    "closer_repeat_floor": 3,
    "para_cv_min": 0.35,            # stdev/mean of paragraph sentence counts
    "marker_density_max": 2.2,      # AI marker hits per 1000 words
    "em_dash_max": 0,
    "curly_quote_max": 0,
    "rule_of_three_max_per_1k": 2.0,
    "contraction_min_per_1k": 4.0,
    "devanagari_majority": 0.5,     # above this share, English-only gates skip
}

# Markers that ZeroGPT-flagged spans repeatedly contain. Grouped so the report
# tells you which family to attack, not just that you tripped a counter.
MARKERS = {
    "connective_scaffolding": [
        r"\bmoreover\b", r"\bfurthermore\b", r"\badditionally\b",
        r"\bin conclusion\b", r"\bin summary\b", r"\bto summari[sz]e\b",
        r"\boverall,", r"\bultimately,", r"\bconsequently\b",
        r"\bas a result,", r"\bthat said,", r"\bthat being said\b",
        r"\bin today'?s\b", r"\bin the world of\b", r"\bwhen it comes to\b",
    ],
    "significance_inflation": [
        r"\bplays? a (?:crucial|vital|key|pivotal|significant) role\b",
        r"\bis a testament\b", r"\bunderscor(?:e|es|ing)\b",
        r"\bhighlight(?:s|ing) the importance\b", r"\bserves? as\b",
        r"\bstands? as\b", r"\bmarks? a\b", r"\brepresents? a shift\b",
        r"\bevolving landscape\b", r"\bin the realm of\b",
    ],
    "ai_vocabulary": [
        r"\bdelve\b", r"\bintricate\b", r"\btapestry\b", r"\bnavigat(?:e|ing)\b",
        r"\bleverag(?:e|es|ing)\b", r"\brobust\b", r"\bseamless(?:ly)?\b",
        r"\bstreamlin(?:e|es|ed|ing)\b", r"\bfoster(?:s|ing)?\b",
        r"\bharness(?:es|ing)?\b", r"\bempower(?:s|ing)?\b", r"\bunlock\b",
        r"\bcrucial\b", r"\bpivotal\b", r"\bvital\b", r"\bholistic\b",
        r"\bcutting-edge\b", r"\bgame-chang(?:er|ing)\b", r"\bseismic\b",
        r"\bever-(?:evolving|changing|growing)\b", r"\bmyriad\b",
        r"\brealm\b", r"\bparadigm\b", r"\bsynerg(?:y|ies|istic)\b",
    ],
    "hollow_analysis": [
        r"\bhighlighting\b", r"\bemphasi[sz]ing\b", r"\bensuring\b",
        r"\breflecting\b", r"\bshowcasing\b", r"\bcontributing to\b",
        r"\bcultivating\b", r"\bencompassing\b", r"\ballowing (?:you|them|it) to\b",
    ],
    "signposting": [
        r"\blet'?s (?:dive|explore|break|take a look|get into)\b",
        r"\bhere'?s what you need to know\b", r"\bwithout further ado\b",
        r"\bin this (?:article|post|guide), (?:we|I|you)\b",
        r"\bnow, let'?s\b", r"\bfirst and foremost\b",
    ],
    "persuasive_authority": [
        r"\bthe real question is\b", r"\bat its core\b", r"\bthe heart of\b",
        r"\bwhat (?:really|truly) matters\b", r"\bfundamentally,",
        r"\bthe bottom line is\b", r"\bthe truth is\b",
    ],
    "negative_parallelism": [
        r"\bit'?s not (?:just|merely|only) about\b",
        r"\bnot only\b[^.]{0,80}\bbut also\b",
        r"\bisn'?t (?:just|merely|only)\b[^.]{0,60}\bit'?s\b",
    ],
    "hedging": [
        r"\bcould potentially\b", r"\bmight possibly\b",
        r"\bit is (?:important|worth) (?:to note|noting)\b",
        r"\bit'?s (?:important|worth) (?:to note|noting)\b",
        r"\bgenerally speaking\b", r"\bin many cases,",
    ],
    # Hindi/Hinglish equivalents. AI-written Hindi reaches for the same
    # scaffolding as AI-written English, just translated, and ZeroGPT scores
    # Devanagari through the same perplexity model.
    "hindi_connective_scaffolding": [
        r"इसके अलावा", r"इसके अतिरिक्त", r"साथ ही साथ",
        r"निष्कर्ष के (?:रूप में|तौर पर)", r"निष्कर्षतः", r"अंततः",
        r"संक्षेप में", r"दूसरी ओर", r"इसलिए यह कहा जा सकता है",
        r"जैसा कि हम (?:सभी )?जानते ह", r"आज के (?:इस )?(?:समय|दौर|युग) में",
        r"वर्तमान समय में", r"आजकल के दौर में",
    ],
    "hindi_signposting": [
        r"आइए (?:जानते|समझते|देखते|विस्तार से)", r"चलिए (?:जानते|समझते|देखते)",
        r"इस (?:लेख|ब्लॉग|आर्टिकल) में हम", r"इस (?:लेख|ब्लॉग|आर्टिकल) में आपको",
        r"तो चलिए", r"सबसे पहले (?:तो )?बात करते ह",
    ],
    "hindi_significance_inflation": [
        r"महत्वपूर्ण भूमिका निभात", r"अहम भूमिका निभात",
        r"बेहद महत्वपूर्ण ह", r"अत्यंत आवश्यक ह",
        r"ध्यान देने योग्य बात यह है कि", r"यह ध्यान रखना (?:महत्वपूर्ण|जरूरी) है",
        r"एक बेहतरीन विकल्प (?:है|साबित)", r"वरदान साबित",
    ],
    "promotional": [
        r"\bstunning\b", r"\bbreathtaking\b", r"\bworld-class\b",
        r"\bstate-of-the-art\b", r"\bunparalleled\b", r"\bboasts?\b",
        r"\bnestled\b", r"\bvibrant\b", r"\bmust-(?:visit|have|read)\b",
    ],
}

CONTRACTIONS = re.compile(
    r"\b\w+(?:'|’)(?:s|t|re|ve|ll|d|m)\b", re.IGNORECASE
)
RULE_OF_THREE = re.compile(
    r"\b\w+(?:\s+\w+){0,2},\s+\w+(?:\s+\w+){0,2},\s+and\s+\w+(?:\s+\w+){0,2}\b"
)
# Same tic in Hindi: "X, Y और Z" used as a habit.
RULE_OF_THREE_HI = re.compile(
    r"[\u0900-\u097F\w]+(?:\s+[\u0900-\u097F\w]+){0,2},\s*"
    r"[\u0900-\u097F\w]+(?:\s+[\u0900-\u097F\w]+){0,2},\s*"
    r"और\s+[\u0900-\u097F\w]+"
)

DEVANAGARI = r"\u0900-\u097F"
WORD_RE = re.compile(f"[A-Za-z'{DEVANAGARI}‍]+")
# Hindi ends sentences on the danda as often as on a full stop.
SENT_END = f"[.!?।]"
NEXT_START = f"[\"'(\\[]?[A-Z0-9{DEVANAGARI}]"


def devanagari_share(text: str) -> float:
    """Fraction of word tokens written in Devanagari. Decides which gates apply."""
    words = WORD_RE.findall(text)
    if not words:
        return 0.0
    hi = sum(1 for w in words if re.search(f"[{DEVANAGARI}]", w))
    return hi / len(words)


def _terminate_list_item(m: "re.Match") -> str:
    """A list item is a sentence. Give it a full stop so the splitter sees one."""
    body = m.group(1).strip()
    if body and body[-1] not in ".!?।:":
        body += "."
    return body


def strip_markdown(text: str) -> str:
    """Remove structure that is not prose so counts reflect what a reader sees."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"^\s*\|.*\|\s*$", " ", text, flags=re.M)   # tables
    text = re.sub(r"^\s{0,3}#{1,6}\s.*$", " ", text, flags=re.M)  # headings
    # Meta title and description lines are CMS fields carried in the draft for
    # the client's convenience. They are not body copy and must not be scored.
    text = re.sub(r"^\s*\*\*Meta (?:Title|Description):\*\*.*$", " ", text,
                  flags=re.M | re.I)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)          # images
    # Image credit lines are a caption, not prose. Drop them before links are
    # unwrapped, or every one becomes a two-word "sentence".
    text = re.sub(r"^\s*\[Image Source\]\([^)]*\)\s*$", " ", text,
                  flags=re.M | re.I)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)       # links -> label
    # A reader takes each bullet as its own sentence. Without a terminator the
    # splitter swallowed an entire list into one enormous "sentence", which
    # inflated the long-sentence share and flattened the variance figures.
    text = re.sub(r"^\s{0,4}(?:[-*+]|\d+[.)])\s+(.*?)\s*$",
                  _terminate_list_item, text, flags=re.M)
    text = re.sub(r"^\s*>\s?", "", text, flags=re.M)
    text = re.sub(r"<[^>]+>", " ", text)
    return text


def split_sentences(text: str):
    protected = re.sub(
        r"\b(Mr|Mrs|Ms|Dr|Prof|Sr|Jr|vs|etc|e\.g|i\.e|No|Inc|Ltd|St)\.",
        r"\1<DOT>", text,
    )
    protected = re.sub(r"(\d)\.(\d)", r"\1<DOT>\2", protected)
    parts = re.split(f"(?<={SENT_END})\\s+(?={NEXT_START})", protected)
    out = []
    for p in parts:
        p = p.replace("<DOT>", ".").strip()
        if len(p.split()) >= 2:
            out.append(p)
    return out


def analyse(raw: str) -> dict:
    prose = strip_markdown(raw)
    sentences = split_sentences(prose)
    words = WORD_RE.findall(prose)
    n_words = len(words) or 1
    per_1k = 1000.0 / n_words

    lengths = [len(s.split()) for s in sentences]
    mean_len = statistics.mean(lengths) if lengths else 0.0
    stdev_len = statistics.pstdev(lengths) if len(lengths) > 1 else 0.0
    cv = (stdev_len / mean_len) if mean_len else 0.0

    clustered = sum(1 for L in lengths if abs(L - mean_len) <= 4)
    shorts = sum(1 for L in lengths if L < 9)
    longs = sum(1 for L in lengths if L > 24)
    n_s = len(lengths) or 1

    paras = [p for p in re.split(r"\n\s*\n", prose) if len(p.split()) > 12]
    para_sent_counts = [max(1, len(split_sentences(p))) for p in paras]
    p_mean = statistics.mean(para_sent_counts) if para_sent_counts else 0.0
    p_cv = (
        statistics.pstdev(para_sent_counts) / p_mean
        if len(para_sent_counts) > 1 and p_mean
        else 0.0
    )

    openers = {}
    for s in sentences:
        w = re.sub(f"[^A-Za-z'{DEVANAGARI}]", "", s.split()[0]).lower() if s.split() else ""
        if w:
            openers[w] = openers.get(w, 0) + 1
    worst_opener = max(openers.items(), key=lambda kv: kv[1]) if openers else ("", 0)
    opener_pct = 100.0 * worst_opener[1] / (len(sentences) or 1)

    # Hindi puts the verb last, so its predictability sits at the end of the
    # sentence rather than the start. A draft where half the sentences close on
    # the same copula has the same flat cadence an English draft has when every
    # sentence opens with "The", and the opener gate cannot see it.
    closers = {}
    for s in sentences:
        w = re.sub(f"[^A-Za-z'{DEVANAGARI}]", "", s.split()[-1]).lower() if s.split() else ""
        if w:
            closers[w] = closers.get(w, 0) + 1
    worst_closer = max(closers.items(), key=lambda kv: kv[1]) if closers else ("", 0)
    closer_pct = 100.0 * worst_closer[1] / (len(sentences) or 1)

    marker_hits, marker_total = {}, 0
    for family, pats in MARKERS.items():
        hits = []
        for pat in pats:
            for m in re.finditer(pat, prose, re.IGNORECASE):
                hits.append(m.group(0).strip())
        if hits:
            marker_hits[family] = sorted(set(hits))
        marker_total += len(hits)

    flagged = []
    for s in sentences:
        score = 0
        wc = len(s.split())
        if abs(wc - mean_len) <= 3:
            score += 1
        for pats in MARKERS.values():
            if any(re.search(p, s, re.IGNORECASE) for p in pats):
                score += 2
                break
        if not CONTRACTIONS.search(s) and wc > 18:
            score += 1
        if RULE_OF_THREE.search(s) or RULE_OF_THREE_HI.search(s):
            score += 2
        if score >= 3:
            flagged.append({"score": score, "words": wc, "text": s[:180]})
    flagged.sort(key=lambda d: -d["score"])

    return {
        "devanagari_share": round(devanagari_share(prose), 3),
        "words": n_words,
        "sentences": n_s,
        "mean_sentence_len": round(mean_len, 2),
        "stdev_sentence_len": round(stdev_len, 2),
        "sentence_cv": round(cv, 3),
        "clustered_pct": round(100.0 * clustered / n_s, 1),
        "short_sentence_pct": round(100.0 * shorts / n_s, 1),
        "long_sentence_pct": round(100.0 * longs / n_s, 1),
        "paragraphs": len(paras),
        "para_cv": round(p_cv, 3),
        "top_opener": {
            "word": worst_opener[0],
            "count": worst_opener[1],
            "pct": round(opener_pct, 1),
        },
        "top_closer": {
            "word": worst_closer[0],
            "count": worst_closer[1],
            "pct": round(closer_pct, 1),
        },
        "contractions_per_1k": round(len(CONTRACTIONS.findall(prose)) * per_1k, 2),
        "rule_of_three_per_1k": round(
            (len(RULE_OF_THREE.findall(prose)) + len(RULE_OF_THREE_HI.findall(prose)))
            * per_1k, 2),
        "em_dashes": prose.count("—"),
        "curly_quotes": sum(prose.count(c) for c in "“”‘’"),
        "marker_density_per_1k": round(marker_total * per_1k, 2),
        "marker_hits": marker_hits,
        "riskiest_sentences": flagged[:12],
    }


def gate(r: dict):
    checks = [
        ("sentence length variance (CV)", r["sentence_cv"] >= GATES["sentence_cv_min"],
         f"{r['sentence_cv']} (need >= {GATES['sentence_cv_min']})"),
        ("sentences clustered at mean", r["clustered_pct"] <= GATES["clustered_max_pct"],
         f"{r['clustered_pct']}% (need <= {GATES['clustered_max_pct']}%)"),
        ("short sentences present", r["short_sentence_pct"] >= GATES["short_sentence_min_pct"],
         f"{r['short_sentence_pct']}% (need >= {GATES['short_sentence_min_pct']}%)"),
        ("long sentences present", r["long_sentence_pct"] >= GATES["long_sentence_min_pct"],
         f"{r['long_sentence_pct']}% (need >= {GATES['long_sentence_min_pct']}%)"),
        ("paragraph size variance (CV)", r["para_cv"] >= GATES["para_cv_min"],
         f"{r['para_cv']} (need >= {GATES['para_cv_min']})"),
        ("sentence opener repetition",
         r["top_opener"]["count"] <= GATES["opener_repeat_floor"]
         or r["top_opener"]["pct"] <= GATES["opener_repeat_pct_max"],
         f"'{r['top_opener']['word']}' x{r['top_opener']['count']} = "
         f"{r['top_opener']['pct']}% of sentences "
         f"(max {GATES['opener_repeat_pct_max']}%, floor {GATES['opener_repeat_floor']})"),
        ("sentence closer repetition",
         r["top_closer"]["count"] <= GATES["closer_repeat_floor"]
         or r["top_closer"]["pct"] <= (
             GATES["closer_repeat_pct_max_devanagari"]
             if r["devanagari_share"] >= GATES["devanagari_majority"]
             else GATES["closer_repeat_pct_max"]),
         f"'{r['top_closer']['word']}' x{r['top_closer']['count']} = "
         f"{r['top_closer']['pct']}% of sentences (max "
         f"{GATES['closer_repeat_pct_max_devanagari'] if r['devanagari_share'] >= GATES['devanagari_majority'] else GATES['closer_repeat_pct_max']}%)"),
        ("AI marker density", r["marker_density_per_1k"] <= GATES["marker_density_max"],
         f"{r['marker_density_per_1k']}/1k (max {GATES['marker_density_max']})"),
        ("em dashes", r["em_dashes"] <= GATES["em_dash_max"], str(r["em_dashes"])),
        ("curly quotes", r["curly_quotes"] <= GATES["curly_quote_max"], str(r["curly_quotes"])),
        ("rule of three", r["rule_of_three_per_1k"] <= GATES["rule_of_three_max_per_1k"],
         f"{r['rule_of_three_per_1k']}/1k (max {GATES['rule_of_three_max_per_1k']})"),
    ]
    # Apostrophe contractions do not exist in Devanagari, so the gate measures
    # nothing on a Hindi draft. It is reported as not applicable rather than
    # failed. Nothing replaces it yet; see the limitation note in
    # references/learning-log.md.
    if r["devanagari_share"] >= GATES["devanagari_majority"]:
        checks.append(("contraction rate", None,
                       "n/a on a Devanagari-majority draft "
                       f"(script share {int(r['devanagari_share'] * 100)}%)"))
    else:
        checks.append(("contraction rate",
                       r["contractions_per_1k"] >= GATES["contraction_min_per_1k"],
                       f"{r['contractions_per_1k']}/1k "
                       f"(need >= {GATES['contraction_min_per_1k']})"))
    return checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    raw = Path(a.file).read_text(encoding="utf-8")
    r = analyse(raw)
    checks = gate(r)
    failed = [c for c in checks if c[1] is False]

    if a.json:
        print(json.dumps(
            {"metrics": r, "failed": [c[0] for c in checks if c[1] is False]}, indent=2))
        return 1 if failed else 0

    print(f"ZeroGPT pre-flight: {a.file}")
    print(f"{r['words']} words / {r['sentences']} sentences / {r['paragraphs']} paragraphs")
    if r["devanagari_share"] > 0.05:
        print(f"Devanagari share: {int(r['devanagari_share'] * 100)}% of word tokens")
    print(f"mean sentence {r['mean_sentence_len']} words, stdev {r['stdev_sentence_len']}\n")
    for name, ok, detail in checks:
        mark = "N/A " if ok is None else ("PASS" if ok else "FAIL")
        print(f"  [{mark}] {name}: {detail}")

    if r["marker_hits"]:
        print("\nMarker families present:")
        for fam, hits in sorted(r["marker_hits"].items()):
            print(f"  {fam}: {', '.join(hits[:10])}")

    if a.verbose and r["riskiest_sentences"]:
        print("\nHighest-risk sentences (rewrite these first):")
        for f in r["riskiest_sentences"]:
            print(f"  ({f['score']}) [{f['words']}w] {f['text']}")

    if failed:
        print(f"\n{len(failed)} gate(s) failed.")
    elif r["devanagari_share"] >= GATES["devanagari_majority"]:
        # Do not let a Hindi run read as a clean bill of health. One Hindi draft
        # has been scored so far: it passed every applicable gate here and came
        # back 89.4% AI. See references/learning-log.md.
        print("\nAll applicable gates passed (10 of 11; contraction is N/A on "
              "Devanagari).")
        print("These gates are proxies, not a score. The Hindi thresholds rest "
              "on one report.")
    else:
        print("\nAll gates passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
