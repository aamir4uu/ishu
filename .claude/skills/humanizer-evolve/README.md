# humanizer-evolve

A humanizer that keeps a memory.

Static AI-detection blacklists go stale. This skill scores a draft with a
weighted signal model, and every time a real ZeroGPT report is fed back it
recalibrates those weights against what the detector actually flagged and mines
new rules from the flagged sentences. The memory lives in `memory/` and is
committed, so it carries across sessions.

## Layout

```
SKILL.md                  the workflow Claude follows
reference/patterns.md     what each signal means and how to fix it
scripts/detectors.py      shared signal library (scanner and learner agree)
scripts/scan.py           score a draft, rank sentences by risk
scripts/learn.py          ingest a ZeroGPT report, evolve the model
memory/state.json         version, session history, signal weights
memory/learned_rules.json rules mined from reports + client bans
memory/learned_rules.md   human-readable render of the above
memory/flagged.jsonl      corpus of every span a detector flagged
memory/accepted.jsonl     corpus of spans it accepted
memory/zerogpt-log.md     per-session narrative log
memory/exceptions.md      client rules that override the catalogue
memory/never_promote.txt  topic and brand terms the miner must never promote
reports/                  raw ZeroGPT reports, one file per pass
tests/run_tests.sh        end-to-end pipeline test against a synthetic fixture
```

## Quick start

```bash
cd scripts
python3 learn.py --status
python3 scan.py ../../../../content/my-post/draft.md
# rewrite, re-scan, then run the draft through ZeroGPT
python3 learn.py ../reports/2026-08-21-pass1.md
```

Run the tests after changing any detector:

```bash
bash tests/run_tests.sh
```

No third-party dependencies. Python 3.8+.

## Why the score is not just a word blacklist

Roughly two thirds of the score comes from per-sentence lexical and syntactic
signals, one third from document rhythm: sentence-length burstiness, mid-band
clustering, paragraph uniformity, repeated openers, contraction rate.

That split matters. A draft can contain none of the banned words and still be
flagged, because perplexity-based detectors respond to how evenly the text is
paced. If `low_burstiness` is firing, swapping synonyms will not help. Change
the sentence lengths.
