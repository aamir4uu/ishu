# ZeroGPT Report: Hero FinCorp: Working Capital Loan, Meaning, Eligibility and 2026 Application Guide (refresh)

- Date scored: pending
- File scored: `blog/herofincorp/working-capital-loan/working-capital-loan-new-copy.md` (new copy) and `blog/herofincorp/working-capital-loan/working-capital-loan.md` (full refreshed page)
- Word count: 656 new / 1662 full page (prose as measured; headings, tables and image lines excluded)
- ZeroGPT result: **pending client run**
- Detector version or URL: https://www.zerogpt.com
- Pre-flight run before scoring: yes, both runs saved to `blog/herofincorp/working-capital-loan/zerogpt-preflight-result.txt`
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
| sentence length variance (CV) | 0.548 | >= 0.45 | pass |
| sentences clustered at mean | 30.2% | <= 40% | pass |
| short sentences (< 9 words) | 23.3% | >= 12% | pass |
| long sentences (> 24 words) | 16.3% | >= 12% | pass |
| paragraph size variance (CV) | 0.724 | >= 0.35 | pass |
| top sentence opener | "a" x3 = 7.0% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.0 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 16.77 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 15.4 words, standard deviation 8.44, across 43 sentences and 9 paragraphs.

## Pre-flight metrics at final pass: full refreshed page

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.482 | >= 0.45 | pass |
| sentences clustered at mean | 37.4% | <= 40% | pass |
| short sentences (< 9 words) | 18.2% | >= 12% | pass |
| long sentences (> 24 words) | 16.2% | >= 12% | pass |
| paragraph size variance (CV) | 0.707 | >= 0.35 | pass |
| top sentence opener | "a" x8 = 8.1% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.6 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 10.23 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 16.8 words, standard deviation 8.1, across 99 sentences and 24 paragraphs.

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| | _to be filled after scoring_ | | |

## Findings from the drafting pass

Nothing here needed a detector run to establish.

**New copy.** The reference competitor (Ujjivan SFB) presents the features section as a bold-label-colon list, which is Wikipedia pattern 16 and the surest structural tell in the catalogue. The section was written as a numbered list of plain sentences instead, and the trade-off is recorded in the known-conflicts table. New copy failed long-sentence share (11.6%) and rule of three (two forced triples) on the first pass; both were fixed by merging a pair of sentences and breaking the triples into a pair plus a trailing clause.

**Full page.** The full page is where the work was. The existing copy measured CV 0.40, 47% of sentences clustered at the mean and 9% long: a page written entirely in 14-to-20-word sentences. Seven existing sentences were split or merged, with the wording otherwise untouched, and that alone moved the page to CV 0.46 and 39% clustered. The fix for uniform client copy is length surgery, not rewriting.

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
