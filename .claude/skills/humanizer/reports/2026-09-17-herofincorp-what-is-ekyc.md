# ZeroGPT Report: Hero FinCorp: E-KYC, Meaning, Full Form, Types, Process, and Eligibility (refresh)

- Date scored: pending
- File scored: `blog/herofincorp/what-is-ekyc/what-is-ekyc-new-copy.md` (new copy) and `blog/herofincorp/what-is-ekyc/what-is-ekyc.md` (full refreshed page)
- Word count: 650 new / 1792 full page (prose as measured; headings, tables and image lines excluded)
- ZeroGPT result: **pending client run**
- Detector version or URL: https://www.zerogpt.com
- Pre-flight run before scoring: yes, both runs saved to `blog/herofincorp/what-is-ekyc/zerogpt-preflight-result.txt`
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
| sentence length variance (CV) | 0.474 | >= 0.45 | pass |
| sentences clustered at mean | 32.5% | <= 40% | pass |
| short sentences (< 9 words) | 17.5% | >= 12% | pass |
| long sentences (> 24 words) | 15.0% | >= 12% | pass |
| paragraph size variance (CV) | 0.371 | >= 0.35 | pass |
| top sentence opener | "you" x3 = 7.5% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.0 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 27.69 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 15.78 words, standard deviation 7.47, across 40 sentences and 10 paragraphs.

## Pre-flight metrics at final pass: full refreshed page

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.452 | >= 0.45 | pass |
| sentences clustered at mean | 39.6% | <= 40% | pass |
| short sentences (< 9 words) | 12.3% | >= 12% | pass |
| long sentences (> 24 words) | 16.0% | >= 12% | pass |
| paragraph size variance (CV) | 0.503 | >= 0.35 | pass |
| top sentence opener | "the" x4 = 3.8% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 1.12 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 13.39 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 16.58 words, standard deviation 7.5, across 106 sentences and 32 paragraphs.

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| | _to be filled after scoring_ | | |

## Findings from the drafting pass

Nothing here needed a detector run to establish.

**New copy.** Three passes on the opener gate alone: "The" x8 (numbered steps and FAQ answers), then "For" x5 (the how-to's two sub-lists both opened with "For a loan..." and "For mutual funds..."), then "You" x4 (the numbered steps). Numbered process sections drive opener repetition harder than prose does because every step naturally starts with the actor. The fix was to open steps with a time word, the object, or the system doing the work.

**Full page.** The existing copy carried the heaviest marker load of the five pages (6.9 per 1k: "at its core", "leverages", "robust framework", "revolutionized", "empowers", "furthermore", "ensuring"). Word-level swaps cleared it without changing a fact. The adversarial pass then removed three "X, not Y" contrasts that the script does not see.

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
