#!/usr/bin/env python3
"""Pre-flight AI-pattern scan. Run this before a draft ever reaches ZeroGPT.

Usage:
    python3 scan.py DRAFT.md
    python3 scan.py DRAFT.md --json
    python3 scan.py DRAFT.md --top 15      # worst N sentences only

Output is a document risk score (0-100, lower is better), the document-level
rhythm signals, and a per-sentence ranking so you know exactly which lines to
rewrite. The weights come from memory/state.json and shift every time learn.py
ingests a real ZeroGPT report, so this scan gets closer to the real detector
with each session.
"""

import argparse
import json
import sys

import detectors as D

# A sentence at or above this risk is one we expect a detector to highlight.
FLAG_RISK = 8.0


def scan(text):
    state = D.load_state()
    rules = D.load_rules()
    weights = state["weights"]

    doc_hits = D.document_hits(text, rules)
    sents = D.sentences(text)

    per_sentence = []
    for s in sents:
        hits = D.sentence_hits(s, rules)
        score = sum(weights.get(h.signal, 5.0) * h.magnitude for h in hits)
        per_sentence.append({
            "sentence": s,
            "risk": round(min(100.0, score), 1),
            "hits": [h.to_dict() for h in hits],
        })

    doc_penalty = sum(weights.get(h.signal, 5.0) * max(h.magnitude, 0.35)
                      for h in doc_hits)
    if per_sentence:
        mean_risk = sum(p["risk"] for p in per_sentence) / len(per_sentence)
        flag_share = (sum(1 for p in per_sentence if p["risk"] >= FLAG_RISK)
                      / len(per_sentence))
    else:
        mean_risk, flag_share = 0.0, 0.0

    # Three terms, because a detector reacts to all three:
    #   mean_risk   - how bad the average line is
    #   flag_share  - how much of the document is flaggable. A handful of very
    #                 bad sentences in a long article barely move a mean, but
    #                 they are exactly what gets highlighted.
    #   doc_penalty - how mechanical the rhythm is. A draft can be entirely
    #                 blacklist-clean and still read as generated because every
    #                 sentence is the same length.
    raw = 0.45 * mean_risk + 45.0 * flag_share + 1.15 * doc_penalty
    score = round(min(100.0, raw), 1)

    return {
        "score": score,
        "verdict": verdict(score),
        "sentence_count": len(sents),
        "document_signals": [h.to_dict() for h in doc_hits],
        "sentences": per_sentence,
        "weights_version": state.get("skill_version"),
        "learned_rules": {
            "phrases": len(rules.get("phrases", {})),
            "words": len(rules.get("words", {})),
        },
    }


def verdict(score):
    if score < 20:
        return "clean - reads human"
    if score < 35:
        return "mostly clean - fix the top sentences"
    if score < 55:
        return "at risk - expect ZeroGPT to flag passages"
    return "high risk - rewrite before submitting"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--top", type=int, default=12)
    ap.add_argument("--threshold", type=float, default=0.1)
    args = ap.parse_args()

    with open(args.draft, encoding="utf-8") as fh:
        text = fh.read()

    result = scan(text)

    if args.json:
        print(json.dumps(result, indent=2))
        return 0

    print(f"SCORE {result['score']}/100  ({result['verdict']})")
    print(f"{result['sentence_count']} sentences | learned rules: "
          f"{result['learned_rules']['phrases']} phrases, "
          f"{result['learned_rules']['words']} words")
    print()

    if result["document_signals"]:
        print("DOCUMENT-LEVEL SIGNALS (rhythm and structure)")
        for h in result["document_signals"]:
            note = f"  [{h['note']}]" if h["note"] else ""
            print(f"  - {h['signal']}: {h['span']}{note}")
        print()

    risky = [s for s in result["sentences"] if s["risk"] > args.threshold]
    risky.sort(key=lambda s: -s["risk"])
    if not risky:
        print("No sentence-level hits.")
        return 0

    print(f"TOP {min(args.top, len(risky))} SENTENCES TO REWRITE")
    for i, s in enumerate(risky[:args.top], 1):
        sig = ", ".join(sorted({h["signal"] for h in s["hits"]}))
        text_ = s["sentence"]
        if len(text_) > 190:
            text_ = text_[:187] + "..."
        print(f"\n{i}. risk {s['risk']}  [{sig}]")
        print(f"   {text_}")
        for h in s["hits"]:
            print(f"     -> {h['signal']}: \"{h['span']}\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
