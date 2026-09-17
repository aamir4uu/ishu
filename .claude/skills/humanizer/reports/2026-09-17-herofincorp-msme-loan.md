# ZeroGPT Report: Hero FinCorp: What Is an MSME Loan? Meaning, Types, Eligibility & How to Apply in 2026 (refresh)

- Date scored: pending
- File scored: `blog/herofincorp/msme-loan/msme-loan-new-copy.md` (new copy) and `blog/herofincorp/msme-loan/msme-loan.md` (full refreshed page)
- Word count: 374 new / 2800 full page (prose as measured; headings, tables and image lines excluded)
- ZeroGPT result: **pending client run**
- Detector version or URL: https://www.zerogpt.com
- Pre-flight run before scoring: yes, both runs saved to `blog/herofincorp/msme-loan/zerogpt-preflight-result.txt`
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
| sentence length variance (CV) | 0.615 | >= 0.45 | pass |
| sentences clustered at mean | 27.3% | <= 40% | pass |
| short sentences (< 9 words) | 22.7% | >= 12% | pass |
| long sentences (> 24 words) | 22.7% | >= 12% | pass |
| paragraph size variance (CV) | 0.369 | >= 0.35 | pass |
| top sentence opener | "for" x3 = 13.6% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.0 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 13.37 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 17.82 words, standard deviation 10.97, across 22 sentences and 5 paragraphs.

## Pre-flight metrics at final pass: full refreshed page

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.541 | >= 0.45 | pass |
| sentences clustered at mean | 34.6% | <= 40% | pass |
| short sentences (< 9 words) | 14.1% | >= 12% | pass |
| long sentences (> 24 words) | 19.9% | >= 12% | pass |
| paragraph size variance (CV) | 1.232 | >= 0.35 | pass |
| top sentence opener | "the" x11 = 7.1% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 1.43 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 5.0 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 18.17 words, standard deviation 9.83, across 156 sentences and 50 paragraphs.

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| | _to be filled after scoring_ | | |

## Findings from the drafting pass

Nothing here needed a detector run to establish.

**New copy.** Only 355 new words, because the brief asks for one 70-word section and four FAQs. A sample that small fails the variance gates on the first pass almost by default (52% clustered, 9.5% long, paragraph CV 0.28) because each sentence is 5% of the distribution. It passed after one 26-word bullet, one three-word bullet and a two-sentence FAQ were introduced deliberately. Below about 400 words, plan the length distribution before writing rather than repairing it afterwards.

**Full page.** The full page failed rule of three at 5.83 per 1k, sixteen serial-comma lists in the client's copy. Eleven had the Oxford comma removed and three were restructured. This page also carried the most stale facts of the five (2020 MSME thresholds, a discontinued subsidy scheme, a mislabelled CIBIL rank), all corrected and logged in refresh-notes.md.

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
