# ZeroGPT session log

Appended to by `scripts/learn.py` every time a real detector report is
ingested. Each entry records the score, how many flagged spans matched the
draft, the scanner's recall before that report, which sentences it missed, and
how the signal weights moved as a result.

Read the last two or three entries at the start of any session. The "missed by
the scanner" lists are the highest-value part: those are the sentence shapes
that got past the model last time.

---

## Session 0 - 2026-08-21 (seed, no detector report)

Baseline only. No ZeroGPT report has been ingested yet, so every weight in
`state.json` is still the untrained prior and `learned_rules.json` contains only
the SocialBee banned lists, marked `source: client:socialbee`.

- Draft scanned: `content/facebook-reel-length/facebook-reel-length.md`
- Final scan score: 0.0/100, no sentence-level and no document-level signals
- Scanner fixes made this session: markdown line breaks are now hard sentence
  boundaries, and headings and table rows are excluded from the prose sample.
  Before the fix the scanner was reporting 9.2 on a draft that actually scored
  32.6.

The first real report will move the weights. Until then, treat the score as a
lint pass, not as a detector prediction.
