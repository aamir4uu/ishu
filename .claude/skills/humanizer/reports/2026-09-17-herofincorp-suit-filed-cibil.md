# ZeroGPT Report: Hero FinCorp: What Is Suit Filed and How to Remove It in CIBIL Report? (refresh)

> **SUPERSEDED on 2026-09-18.** The draft described here was scored in
> ZeroGPT and its siblings came back above the client bar. See
> `2026-09-18-herofincorp-suit-filed-cibil.md` for the score, the highlighted sentences
> and the rewrite. The metrics below describe a draft that no longer exists.


- Date scored: pending
- File scored: `blog/herofincorp/suit-filed-cibil/suit-filed-cibil.md`
- Word count: 997 as the client counts it (headings, body, tables and captions; `tools/count-words.py`); 730 words of prose as the pre-flight measures it
- Length brief: 500 to 700 words, up to 1000 for this page
- ZeroGPT result: **pending client run**
- Detector version or URL: https://www.zerogpt.com
- Pre-flight run before scoring: yes, saved to `blog/herofincorp/suit-filed-cibil/zerogpt-preflight-result.txt`
- Gates failing at time of scoring: 0 of 11

This report is filed open. The environment that produced the draft has no
outbound access to zerogpt.com, so the piece has not been scored yet. Whoever
runs it should paste the result and the highlighted sentences into the table
below, then work the actions checklist. Until that happens this skill has no
new evidence from this piece and no threshold should be moved because of it.

## Pre-flight metrics at final pass

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.627 | >= 0.45 | pass |
| sentences clustered at mean | 28.0% | <= 40% | pass |
| short sentences (< 9 words) | 26.0% | >= 12% | pass |
| long sentences (> 24 words) | 14.0% | >= 12% | pass |
| paragraph size variance (CV) | 0.517 | >= 0.35 | pass |
| top sentence opener | "it" x3 = 6.0% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 1.37 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 20.55 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 14.64 words, standard deviation 9.18, across 50 sentences and 16 paragraphs.

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| | _to be filled after scoring_ | | |

## Findings from the drafting pass

Nothing here needed a detector run to establish.

**This page.** One of two pages allowed up to 1,000 words because the brief mandates four sections and six FAQs. Tables carry about 120 of the words and the script ignores them, so the measured prose is roughly 730. The clustered gate and the long-sentence floor both tripped after the cut; four in-band sentences were split into short pairs and one bullet pair was merged into a 30-word sentence.

**All seven pages, the length constraint.** The client's brief caps the whole
article at 500 to 700 words with headings and tables counted, which is 550 to
600 words of prose. Two effects on the gates. First, every floor is a single
sentence: at 40 sentences, the short-sentence and long-sentence floors are both
five sentences, so one merge or split flips a gate, and the script has to run
after every edit rather than at the end. Second, trimming pulls sentences
toward the mean, because the words that go first are the tails of long
sentences, so the clustered-at-mean gate is the one that fails during a cut
even when it passed before. The repair that costs no words is the merge (two
mid-length sentences into one long one) paired with a fragment somewhere
else. `tools/count-words.py` was added so the length gate runs beside the
detector gates.

**Adversarial pass.** After the gates passed, a hand read looked for the three
tells logged as candidates in `references/learning-log.md` (aphoristic
one-line openers, "X rather than Y" contrasts, matched-pair closers). The
condensed pages carry fewer of them than the full-length drafts did, because
there is no room for flourishes; the ones that remained were rewritten.

## Actions taken

- [x] Piece history row added to `references/learning-log.md`
- [x] Standing finding on length-capped pages added to `references/learning-log.md`
- [ ] Pattern added to the candidates table (nothing new observed; the three from the full-length drafts stand)
- [ ] Pattern promoted to `MARKERS` (needs two detector sightings)
- [ ] Threshold changed in `GATES` (none)
