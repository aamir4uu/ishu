# ZeroGPT Report: Hero FinCorp: What Is the UPI Transaction Limit per Day & Month? Complete Guide (refresh)

- Date scored: pending
- File scored: `blog/herofincorp/upi-transaction-limit/upi-transaction-limit-new-copy.md` (new copy) and `blog/herofincorp/upi-transaction-limit/upi-transaction-limit.md` (full refreshed page)
- Word count: 530 new / 2198 full page (prose as measured; headings, tables and image lines excluded)
- ZeroGPT result: **pending client run**
- Detector version or URL: https://www.zerogpt.com
- Pre-flight run before scoring: yes, both runs saved to `blog/herofincorp/upi-transaction-limit/zerogpt-preflight-result.txt`
- Gates failing at time of scoring: 0 of 11 on the new copy, 0 of 11 on the full page

This report is filed open. The environment that produced the draft has no
outbound access to zerogpt.com, so the piece has not been scored yet. Whoever
runs it should paste the result and the highlighted sentences into the table
below, then work the actions checklist. Until that happens this skill has no
new evidence from this piece and no threshold should be moved because of it.

Score the new copy and the full page separately. The new copy is what the
writer is answerable for; the full page is what the client will paste in.

## Pre-flight metrics at final pass: new copy

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.629 | >= 0.45 | pass |
| sentences clustered at mean | 10.7% | <= 40% | pass |
| short sentences (< 9 words) | 25.0% | >= 12% | pass |
| long sentences (> 24 words) | 35.7% | >= 12% | pass |
| paragraph size variance (CV) | 0.404 | >= 0.35 | pass |
| top sentence opener | "npci" x3 = 10.7% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.0 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 32.08 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 19.39 words, standard deviation 12.21, across 28 sentences and 8 paragraphs.

## Pre-flight metrics at final pass: full refreshed page

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.496 | >= 0.45 | pass |
| sentences clustered at mean | 35.1% | <= 40% | pass |
| short sentences (< 9 words) | 13.7% | >= 12% | pass |
| long sentences (> 24 words) | 19.1% | >= 12% | pass |
| paragraph size variance (CV) | 0.771 | >= 0.35 | pass |
| top sentence opener | "the" x7 = 5.3% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.45 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 15.47 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 17.04 words, standard deviation 8.46, across 131 sentences and 39 paragraphs.

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| | _to be filled after scoring_ | | |

## Findings from the drafting pass

Nothing here needed a detector run to establish.

**New copy.** The new copy failed two gates on the first pass, paragraph variance (0.25) and opener repetition ("The" x4 of 28), and nothing else. Every FAQ answer had come out at three or four sentences. The repair was to make one answer a single 45-word sentence and another six sentences, and to move "NPCI's" and "Above that" to the front of two sentences. One false positive worth knowing: "face unlock", the name of a phone feature, trips the `unlock` marker. It was reworded to "face recognition" rather than argued with, since the client runs a detector that will not know the difference either.

**Full page.** The full page fails rule of three on the client's own copy (2.78 per 1k) before any new words are added; five Oxford-comma lists supply most of the hits. Dropping the serial comma from plain lists is enough to pass and matches Indian usage on the rest of the site.

**Adversarial pass, all five pages.** After every gate passed, a hand read
found three tells the script cannot see, each present in most of the five
drafts: FAQ answers opening on a one-line aphorism ("Timing is the main
benefit", "Daily is the number that matters", "Either."), an "X rather than Y"
or "X, not Y" contrast in roughly one sentence in eight, and paragraph closers
built as a matched pair ("Do that, and A. Ignore it, and B."). About half of
each were rewritten. All three are logged as candidates in
`references/learning-log.md`, marked as self-observed rather than
detector-observed.

## Actions taken

- [x] Three candidate patterns added to the `references/learning-log.md`
      candidates table (self-observed during the adversarial pass; sightings
      count starts at 0 until a detector highlights one)
- [ ] Pattern promoted to `MARKERS` (needs two detector sightings)
- [ ] Threshold changed in `GATES` (none; the 2026-09-17 change to
      `strip_markdown()` is a measurement fix, recorded in the calibration
      history)
- [x] `references/zerogpt-signals.md` known-conflicts table gained a row for
      competitor reference layouts built on bold-label lists
- [x] Piece history row added to `references/learning-log.md`
