# ZeroGPT Report: Hero FinCorp: What Is Suit Filed and How to Remove It in CIBIL Report? (refresh)

- Date scored: pending
- File scored: `blog/herofincorp/suit-filed-cibil/suit-filed-cibil-new-copy.md` (new copy) and `blog/herofincorp/suit-filed-cibil/suit-filed-cibil.md` (full refreshed page)
- Word count: 587 new / 1491 full page (prose as measured; headings, tables and image lines excluded)
- ZeroGPT result: **pending client run**
- Detector version or URL: https://www.zerogpt.com
- Pre-flight run before scoring: yes, both runs saved to `blog/herofincorp/suit-filed-cibil/zerogpt-preflight-result.txt`
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
| sentence length variance (CV) | 0.478 | >= 0.45 | pass |
| sentences clustered at mean | 32.4% | <= 40% | pass |
| short sentences (< 9 words) | 14.7% | >= 12% | pass |
| long sentences (> 24 words) | 23.5% | >= 12% | pass |
| paragraph size variance (CV) | 0.377 | >= 0.35 | pass |
| top sentence opener | "a" x2 = 5.9% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.0 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 15.33 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 17.29 words, standard deviation 8.27, across 34 sentences and 11 paragraphs.

## Pre-flight metrics at final pass: full refreshed page

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.536 | >= 0.45 | pass |
| sentences clustered at mean | 39.6% | <= 40% | pass |
| short sentences (< 9 words) | 23.8% | >= 12% | pass |
| long sentences (> 24 words) | 13.9% | >= 12% | pass |
| paragraph size variance (CV) | 0.686 | >= 0.35 | pass |
| top sentence opener | "the" x5 = 5.0% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.0 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 20.12 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 14.75 words, standard deviation 7.91, across 101 sentences and 40 paragraphs.

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| | _to be filled after scoring_ | | |

## Findings from the drafting pass

Nothing here needed a detector run to establish.

**New copy.** Two of the four new sections are tables, which the script strips, so only 550 of roughly 810 new words are measured. A comparative section written as a table leaves the gates little to read; the lead-in and closing paragraphs around each table are what keep the section inside the measurement. The new copy failed opener repetition ("The" x8 of 37) on the first pass, then paragraph variance by 0.002 after the adversarial merges. Sub-40-sentence samples are fragile: one merged sentence moves a gate.

**Full page.** The client's copy came with 52 curly quotes and a signposting intro ("In this guide, we'll break down..."). Straightening quotes is mechanical; the intro was reworded. The 45-day dispute follow-up in the existing step 7 contradicted the 30-day RBI timeline stated elsewhere on the same page and was corrected.

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
