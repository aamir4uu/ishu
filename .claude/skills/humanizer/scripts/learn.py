#!/usr/bin/env python3
"""Ingest a real ZeroGPT report and evolve the skill from it.

This is the part that makes the skill get better instead of staying static.
A report tells us two things scan.py cannot know on its own:

  1. Which sentences a real detector actually flagged.
  2. Which sentences it let through.

From that we do three things:

  * Recalibrate signal weights. Signals that show up disproportionately in
    flagged sentences get heavier; signals that fire mostly on sentences
    ZeroGPT accepted get lighter. Over sessions the scanner converges on what
    the detector actually reacts to rather than on a fixed blacklist.
  * Mine new rules. Any n-gram that keeps appearing in flagged text and never
    in accepted text is promoted into memory/learned_rules.json, so the next
    scan catches it before submission.
  * Keep a corpus. Every flagged span and its rewrite is appended to
    memory/flagged.jsonl, which is the evidence base for future promotions.

Report format (plain text or markdown):

    draft: content/post/post.md
    score: 43
    date: 2026-08-21
    note: first pass

    ## flagged
    A sentence ZeroGPT highlighted.
    Another sentence it highlighted.

Usage:
    python3 learn.py report.md
    python3 learn.py report.md --dry-run
    python3 learn.py --status
"""

import argparse
import collections
import datetime as dt
import json
import os
import re
import sys

import detectors as D

MEMORY = D.MEMORY
FLAGGED = os.path.join(MEMORY, "flagged.jsonl")
ACCEPTED = os.path.join(MEMORY, "accepted.jsonl")
RULES = os.path.join(MEMORY, "learned_rules.json")
LOG = os.path.join(MEMORY, "zerogpt-log.md")

LEARNING_RATE = 0.35
MIN_WEIGHT = 1.0
MAX_WEIGHT = 30.0
STOPWORDS = set("""a an the and or but if of to in on for with at by from as is are was
were be been being it its this that these those you your yours we our they their he she
his her them us not no so than then there here what which who whom how when where why can
could should would will shall may might must do does did done have has had having i me my
more most much many very just also into over under about across per each other some any""".split())


# ------------------------------------------------------------------ parsing

def parse_report(path):
    """Read a filed ZeroGPT report.

    Two formats are accepted, because the skill has used both:

    * The table format in `reports/TEMPLATE.md`, where highlighted sentences sit
      in the second column of the "Highlighted sentences" table.
    * A plain list under a `## flagged` heading, one sentence per line.

    Metadata is read from `key: value` lines wherever they appear, including the
    template's bulleted front matter.
    """
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()

    meta = {}
    aliases = {
        "file scored": "draft",
        "zerogpt result": "score",
        "date scored": "date",
        "word count": "words",
    }
    for key in ("draft", "score", "date", "note", "tool", "file scored",
                "zerogpt result", "date scored", "word count"):
        m = re.search(rf"^[-*\s]*`?{key}`?\s*[:=]\s*(.+)$", raw, re.M | re.I)
        if m:
            val = m.group(1).strip().strip("`").strip()
            if val and not val.startswith("<"):
                meta[aliases.get(key, key)] = val

    if "score" in meta:
        m = re.search(r"(\d+(?:\.\d+)?)\s*%", meta["score"])
        if m:
            meta["score"] = m.group(1)

    spans = []

    # Format 1: the template's highlighted-sentences table.
    m = re.search(r"^#+\s*highlighted sentences.*$", raw, re.M | re.I)
    if m:
        body = re.split(r"^#+\s", raw[m.end():], flags=re.M)[0]
        for line in body.splitlines():
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 2:
                continue
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue
            if cells[1].lower() in ("", "highlighted sentence"):
                continue
            spans.append(cells[1])

    # Format 2: a plain list under "## flagged".
    if not spans:
        m = re.search(r"^#+\s*flagged.*$", raw, re.M | re.I)
        if not m:
            raise SystemExit(
                "Report needs either a 'Highlighted sentences' table (see "
                "reports/TEMPLATE.md) or a '## flagged' list of the "
                "highlighted sentences."
            )
        body = re.split(r"^#+\s", raw[m.end():], flags=re.M)[0]
        for line in body.splitlines():
            line = re.sub(r"^[-*+]\s+", "", line.strip())
            line = re.sub(r"^\d+[.)]\s+", "", line).strip('"').strip()
            if len(line) > 15:
                spans.append(line)

    spans = [x for x in spans if len(x) > 15 and not is_placeholder(x)]
    if not spans:
        raise SystemExit(
            "No highlighted sentences found in the report. If it is still a "
            "stub awaiting the detector run, fill it in before ingesting: an "
            "empty report teaches the skill nothing."
        )

    if "draft" not in meta:
        raise SystemExit(
            "Report needs a 'File scored:' or 'draft:' line pointing at the "
            "markdown file that was scored."
        )
    return meta, spans


PLACEHOLDER = re.compile(
    r"^\s*(?:_.*_|<.*>|n/?a|tbd|pending|none)\s*$|to be filled|paste (each|every)",
    re.I
)


def is_placeholder(text):
    """Template rows and stub reports must never enter the corpus."""
    return bool(PLACEHOLDER.search(text.strip()))


def scan_score_of(text):
    """The scanner's own score for this draft, recorded next to the detector's.

    The gap between the two is the honest measure of how much the model still
    cannot see.
    """
    try:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import scan
        return scan.scan(text)["score"]
    except Exception:
        return None


def resolve_draft(draft, report_path):
    """Find the scored file.

    Reports record a repo-relative path, but the scripts are usually run from
    the skill directory, so a bare open() fails. Try the obvious places in
    order rather than making the caller cd around.
    """
    report_dir = os.path.dirname(os.path.abspath(report_path))
    candidates = [
        draft,
        os.path.join(report_dir, draft),
        os.path.join(MEMORY, "..", draft),
    ]
    # Walk up looking for the repo root, then try from there.
    here = os.path.abspath(HERE if (HERE := os.path.dirname(MEMORY)) else ".")
    for _ in range(6):
        candidates.append(os.path.join(here, draft))
        if os.path.isdir(os.path.join(here, ".git")):
            break
        parent = os.path.dirname(here)
        if parent == here:
            break
        here = parent
    for c in candidates:
        c = os.path.normpath(c)
        if os.path.isfile(c):
            return c
    raise SystemExit(
        f"Draft not found: {draft}\nLooked in:\n  "
        + "\n  ".join(os.path.normpath(c) for c in candidates)
    )


def match_spans(draft_sentences, spans):
    """Map each reported span onto the draft sentences it covers.

    ZeroGPT reports its own segmentation, which rarely matches ours, so we
    match on normalised token overlap rather than exact strings.
    """
    flagged = set()
    unmatched = []
    norm_sents = [D.squash(s) for s in draft_sentences]

    for span in spans:
        key = D.squash(span)
        if not key:
            continue
        hit = False
        for i, ns in enumerate(norm_sents):
            if not ns:
                continue
            if key in ns or ns in key:
                flagged.add(i)
                hit = True
                continue
            a, b = set(key.split()), set(ns.split())
            if a and b:
                overlap = len(a & b) / min(len(a), len(b))
                if overlap >= 0.75:
                    flagged.add(i)
                    hit = True
        if not hit:
            unmatched.append(span)
    return flagged, unmatched


# -------------------------------------------------------------- calibration

def recalibrate(weights, flagged_feats, clean_feats, lr=LEARNING_RATE):
    """Move each weight toward the signal's observed lift in flagged text."""
    n_flag = max(1, len(flagged_feats))
    n_clean = max(1, len(clean_feats))
    flag_rate = collections.Counter()
    clean_rate = collections.Counter()
    for feats in flagged_feats:
        for sig in set(feats):
            flag_rate[sig] += 1
    for feats in clean_feats:
        for sig in set(feats):
            clean_rate[sig] += 1

    changes = []
    signals = set(flag_rate) | set(clean_rate)
    for sig in signals:
        p_flag = flag_rate[sig] / n_flag
        p_clean = clean_rate[sig] / n_clean
        # Laplace-smoothed lift: >1 means the signal predicts a flag.
        lift = (p_flag + 0.05) / (p_clean + 0.05)
        old = weights.get(sig, 5.0)
        target = old * lift
        new = old + lr * (target - old)
        new = round(max(MIN_WEIGHT, min(MAX_WEIGHT, new)), 2)
        if abs(new - old) >= 0.05:
            changes.append({
                "signal": sig, "old": old, "new": new,
                "lift": round(lift, 2),
                "flagged_hits": flag_rate[sig], "clean_hits": clean_rate[sig],
            })
            weights[sig] = new
    changes.sort(key=lambda c: -abs(c["new"] - c["old"]))
    return changes


# ------------------------------------------------------------- rule mining

def ngrams(sentence, lo=2, hi=5):
    # Numbers become "#" rather than vanishing. Dropping them turned
    # "15 to 60 seconds" into the gram "to seconds", which is meaningless and
    # promoted straight into the rule set on the first real report.
    text = re.sub(r"\b\d[\d,.:]*\b", " # ", sentence.lower())
    toks = [t for t in re.findall(r"#|[a-z']+", text)]
    out = set()
    for n in range(lo, hi + 1):
        for i in range(len(toks) - n + 1):
            gram = toks[i:i + n]
            if all(t in STOPWORDS or t == "#" for t in gram):
                continue
            if gram[0] in STOPWORDS and gram[-1] in STOPWORDS:
                continue
            # Needs at least two real content words. Without this, a report
            # about video lengths mines "to #" and "a #", which describe the
            # subject matter rather than the writing.
            if sum(1 for t in gram if t not in STOPWORDS and t != "#") < 2:
                continue
            out.add(" ".join(gram))
    return out


def mine_rules(rules, flagged_corpus, accepted_corpus, session, min_hits=2,
               min_corpus=8):
    """Promote n-grams that keep showing up in flagged text and never in
    accepted text. Requires evidence from more than one flagged sentence, so a
    single unlucky sentence cannot poison the rule set."""
    never = D.load_never_promote()
    if len(flagged_corpus) < min_corpus:
        print(f"\n(rule mining held back: {len(flagged_corpus)} flagged spans "
              f"in the corpus, need {min_corpus} before promoting anything)")
    flag_counts = collections.Counter()
    for rec in flagged_corpus:
        for g in ngrams(rec["text"]):
            flag_counts[g] += 1
    clean_counts = collections.Counter()
    for rec in accepted_corpus:
        for g in ngrams(rec["text"]):
            clean_counts[g] += 1

    # Promoting from a thin corpus mostly mines topic nouns. Wait for evidence.
    allow_promotion = len(flagged_corpus) >= min_corpus

    promoted = []
    for gram, n in flag_counts.items():
        if n < min_hits:
            continue
        if gram in never or any(t in never for t in gram.split()):
            continue
        c = clean_counts.get(gram, 0)
        if c and n / c < 3.0:
            continue
        bucket = "phrases" if " " in gram else "words"
        if gram in rules[bucket]:
            rules[bucket][gram]["hits"] = n
            rules[bucket][gram]["last_seen_session"] = session
            continue
        # Skip anything the base lexicon already covers.
        if gram in D.BASE_PHRASES or gram in D.BASE_WORDS:
            continue
        if not allow_promotion:
            continue
        rules[bucket][gram] = {
            "hits": n,
            "clean_hits": c,
            "first_seen_session": session,
            "last_seen_session": session,
            "source": "zerogpt",
        }
        promoted.append((bucket, gram, n, c))
    # Collapse overlapping n-grams. Mining "best practices in order to" also
    # yields "best practices", "in order to", "practices in" and so on at the
    # same count. Keep only the maximal gram of each equal-count family, or the
    # rule table fills with nine spellings of one phrase.
    promoted.sort(key=lambda p: (-len(p[1]), -p[2]))
    kept, kept_grams = [], []
    for entry in promoted:
        gram, n = entry[1], entry[2]
        if any(gram in g and flag_counts.get(g, 0) == n for g in kept_grams):
            rules[entry[0]].pop(gram, None)
            continue
        kept_grams.append(gram)
        kept.append(entry)
    kept.sort(key=lambda p: -p[2])
    return kept


# ------------------------------------------------------------------- corpus

def read_jsonl(path):
    if not os.path.exists(path):
        return []
    out = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                out.append(json.loads(line))
    return out


def append_jsonl(path, records):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as fh:
        for r in records:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")


def write_rules(rules):
    os.makedirs(MEMORY, exist_ok=True)
    with open(RULES, "w", encoding="utf-8") as fh:
        json.dump(rules, fh, indent=2, sort_keys=True, ensure_ascii=False)
        fh.write("\n")


def render_rules_markdown(rules, state):
    lines = [
        "# Learned rules",
        "",
        "Auto-generated by `scripts/learn.py`. Do not hand-edit; edit the",
        "report or `memory/learned_rules.json` and re-render.",
        "",
        f"Skill version: **{state['skill_version']}** | "
        f"reports ingested: **{state['reports_ingested']}** | "
        f"sessions: **{state['sessions']}**",
        "",
        "## Phrases ZeroGPT kept flagging",
        "",
    ]
    ph = sorted(rules["phrases"].items(), key=lambda kv: -kv[1]["hits"])
    if ph:
        lines += ["| phrase | flagged hits | clean hits | since | source |",
                  "| --- | --- | --- | --- | --- |"]
        for k, v in ph:
            lines.append(f"| {k} | {v['hits']} | {v.get('clean_hits', 0)} | "
                         f"s{v['first_seen_session']} | {v.get('source', '?')} |")
    else:
        lines.append("_None yet. Ingest a report to populate this._")
    lines += ["", "## Words ZeroGPT kept flagging", ""]
    wd = sorted(rules["words"].items(), key=lambda kv: -kv[1]["hits"])
    if wd:
        lines += ["| word | flagged hits | clean hits | since | source |",
                  "| --- | --- | --- | --- | --- |"]
        for k, v in wd:
            lines.append(f"| {k} | {v['hits']} | {v.get('clean_hits', 0)} | "
                         f"s{v['first_seen_session']} | {v.get('source', '?')} |")
    else:
        lines.append("_None yet._")
    lines += ["", "## Current signal weights", "",
              "| signal | weight |", "| --- | --- |"]
    for sig, w in sorted(state["weights"].items(), key=lambda kv: -kv[1]):
        lines.append(f"| {sig} | {w} |")
    lines.append("")
    with open(os.path.join(MEMORY, "learned_rules.md"), "w",
               encoding="utf-8") as fh:
        fh.write("\n".join(lines))


def bump(version):
    major, minor, patch = (list(map(int, version.split("."))) + [0, 0, 0])[:3]
    return f"{major}.{minor}.{patch + 1}"


# --------------------------------------------------------------------- main

def unlearn(term):
    """Remove a mined rule and blacklist it from future promotion.

    The miner works on statistics, so it will occasionally promote a topic
    phrase that merely happened to sit inside flagged sentences. This is the
    correction path; use it rather than hand-editing the JSON.
    """
    term = term.strip().lower()
    rules = D.load_rules()
    removed = []
    for bucket in ("phrases", "words"):
        if term in rules[bucket]:
            del rules[bucket][term]
            removed.append(bucket)
    write_rules(rules)

    path = os.path.join(MEMORY, "never_promote.txt")
    existing = D.load_never_promote()
    if term not in existing:
        os.makedirs(MEMORY, exist_ok=True)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(term + "\n")

    state = D.load_state()
    render_rules_markdown(rules, state)
    if removed:
        print(f"Removed \"{term}\" from {', '.join(removed)}.")
    else:
        print(f"\"{term}\" was not in the rule set.")
    print(f"Added to never_promote.txt; it will not be mined again.")
    return 0


def status():
    state = D.load_state()
    rules = D.load_rules()
    print(f"skill version   : {state['skill_version']}")
    print(f"sessions        : {state['sessions']}")
    print(f"reports ingested: {state['reports_ingested']}")
    print(f"learned phrases : {len(rules['phrases'])}")
    print(f"learned words   : {len(rules['words'])}")
    print(f"flagged corpus  : {len(read_jsonl(FLAGGED))} spans")
    print(f"accepted corpus : {len(read_jsonl(ACCEPTED))} spans")
    if state["history"]:
        print("\nZeroGPT score history (lower is better):")
        for h in state["history"]:
            def cell(key, width=6):
                v = h.get(key)
                return f"{'-' if v is None else v!s:>{width}}"
            print(f"  s{h.get('session', '?'):>3}  {str(h.get('date', '?')):>10}  "
                  f"zerogpt={cell('zerogpt_score')}  "
                  f"scan={cell('scan_score')}  "
                  f"recall={cell('recall', 4)}  {h.get('draft', '')}")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report", nargs="?")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--min-hits", type=int, default=2)
    ap.add_argument("--min-corpus", type=int, default=8,
                    help="flagged spans needed before any rule is promoted")
    ap.add_argument("--unlearn", metavar="TERM",
                    help="drop a mined rule and never promote it again")
    args = ap.parse_args()

    if args.unlearn:
        return unlearn(args.unlearn)

    if args.status or not args.report:
        return status()

    meta, spans = parse_report(args.report)
    if not re.fullmatch(r"\d+(?:\.\d+)?", str(meta.get("score", ""))):
        print(f"Warning: no numeric ZeroGPT score in the report "
              f"(found {meta.get('score', 'nothing')!r}). Ingesting anyway, "
              f"but the score history will have a gap.")
    draft_path = resolve_draft(meta["draft"], args.report)
    with open(draft_path, encoding="utf-8") as fh:
        text = fh.read()

    draft_sents = D.sentences(text)
    flagged_idx, unmatched = match_spans(draft_sents, spans)

    state = D.load_state()
    rules = D.load_rules()
    session = state["sessions"] + 1

    # Parallelism is a document-level measurement attributed back to the
    # sentences it matched. scan.py does the same thing, and if learn.py did
    # not, every cross-sentence signal would show zero lift forever and could
    # never earn a weight.
    parallel_by_sentence = {}
    for h in D.document_hits(text, rules):
        if h.signal.startswith("parallel_"):
            for idx in h.members:
                parallel_by_sentence.setdefault(idx, []).append(h)

    flagged_feats, clean_feats = [], []
    missed, caught = [], []
    for i, s in enumerate(draft_sents):
        hits = D.sentence_hits(s, rules) + parallel_by_sentence.get(i, [])
        sigs = [h.signal for h in hits]
        risk = sum(state["weights"].get(h.signal, 5.0) * h.magnitude
                   for h in hits)
        if i in flagged_idx:
            flagged_feats.append(sigs)
            (caught if risk >= 5.0 else missed).append(s)
        else:
            clean_feats.append(sigs)

    recall = round(len(caught) / max(1, len(flagged_idx)), 2)

    new_flagged = [{"session": session, "draft": draft_path, "text": s,
                    "date": meta.get("date", str(dt.date.today()))}
                   for s in (caught + missed)]
    new_accepted = [{"session": session, "draft": draft_path, "text": s,
                     "date": meta.get("date", str(dt.date.today()))}
                    for i, s in enumerate(draft_sents) if i not in flagged_idx]

    flagged_corpus = read_jsonl(FLAGGED) + new_flagged
    accepted_corpus = read_jsonl(ACCEPTED) + new_accepted

    changes = recalibrate(state["weights"], flagged_feats, clean_feats)
    promoted = mine_rules(rules, flagged_corpus, accepted_corpus, session,
                          args.min_hits, args.min_corpus)

    print(f"Report      : {args.report}")
    print(f"Draft       : {draft_path}")
    print(f"ZeroGPT     : {meta.get('score', 'n/a')}")
    print(f"Spans       : {len(spans)} reported, "
          f"{len(flagged_idx)} matched to draft sentences, "
          f"{len(unmatched)} unmatched")
    print(f"Scan recall : {recall} "
          f"({len(caught)} predicted, {len(missed)} missed)")
    if unmatched:
        print("\nUnmatched spans (check the draft path and paste exact text):")
        for u in unmatched:
            print(f"  ? {u[:110]}")
    if missed:
        print("\nSentences ZeroGPT flagged that the scanner missed:")
        for s in missed[:12]:
            print(f"  ! {s[:150]}")

    print(f"\nWeight changes ({len(changes)}):")
    for c in changes[:14]:
        arrow = "up  " if c["new"] > c["old"] else "down"
        print(f"  {arrow} {c['signal']:<22} {c['old']:>5} -> {c['new']:<6}"
              f" lift={c['lift']}  (flagged {c['flagged_hits']}, "
              f"clean {c['clean_hits']})")

    print(f"\nNew rules promoted ({len(promoted)}):")
    for bucket, gram, n, c in promoted[:20]:
        print(f"  + [{bucket[:-1]}] \"{gram}\"  flagged x{n}, clean x{c}")
    if not promoted:
        print("  (nothing crossed the evidence threshold this round)")

    if args.dry_run:
        print("\n--dry-run: nothing written.")
        return 0

    state["sessions"] = session
    state["reports_ingested"] += 1
    state["skill_version"] = bump(state["skill_version"])
    state["history"].append({
        "session": session,
        "date": meta.get("date", str(dt.date.today())),
        "draft": draft_path,
        "zerogpt_score": meta.get("score"),
        "scan_score": scan_score_of(text),
        "recall": recall,
        "flagged_spans": len(flagged_idx),
        "promoted_rules": len(promoted),
        "note": meta.get("note", ""),
    })

    append_jsonl(FLAGGED, new_flagged)
    append_jsonl(ACCEPTED, new_accepted)
    write_rules(rules)
    D.save_state(state)
    render_rules_markdown(rules, state)

    os.makedirs(MEMORY, exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(f"\n## Session {session} - {meta.get('date', dt.date.today())}\n\n")
        fh.write(f"- Draft: `{draft_path}`\n")
        fh.write(f"- ZeroGPT score: {meta.get('score', 'n/a')}\n")
        fh.write(f"- Flagged spans matched: {len(flagged_idx)}\n")
        fh.write(f"- Scanner recall before this report: {recall}\n")
        fh.write(f"- Rules promoted: {len(promoted)}\n")
        if meta.get("note"):
            fh.write(f"- Note: {meta['note']}\n")
        if missed:
            fh.write("\nMissed by the scanner (now feeding rule mining):\n\n")
            for s in missed[:15]:
                fh.write(f"  - {s}\n")
        if changes:
            fh.write("\nWeight moves:\n\n")
            for c in changes[:12]:
                fh.write(f"  - `{c['signal']}` {c['old']} -> {c['new']} "
                         f"(lift {c['lift']})\n")

    print(f"\nSkill evolved to version {state['skill_version']}. "
          f"Memory updated in {MEMORY}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
