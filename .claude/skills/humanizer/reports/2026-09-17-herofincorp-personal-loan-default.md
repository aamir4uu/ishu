# ZeroGPT Report: Hero FinCorp: Personal Loan Default Consequences in India & Legal Impact (refresh)

> **SUPERSEDED on 2026-09-18.** The draft described here was scored in
> ZeroGPT and its siblings came back above the client bar. See
> `2026-09-18-herofincorp-personal-loan-default.md` for the score, the highlighted sentences
> and the rewrite. The metrics below describe a draft that no longer exists.


- Date scored: pending
- File scored: `blog/herofincorp/personal-loan-default/personal-loan-default.md`
- Word count: 976 as the client counts it (headings, body, tables and captions; `tools/count-words.py`); 834 words of prose as the pre-flight measures it
- Length brief: 500 to 700 words, up to 1000 for this page
- ZeroGPT result: **pending client run**
- Detector version or URL: https://www.zerogpt.com
- Pre-flight run before scoring: yes, saved to `blog/herofincorp/personal-loan-default/zerogpt-preflight-result.txt`
- Gates failing at time of scoring: 0 of 11

This report is filed open. The environment that produced the draft has no
outbound access to zerogpt.com, so the piece has not been scored yet. Whoever
runs it should paste the result and the highlighted sentences into the table
below, then work the actions checklist. Until that happens this skill has no
new evidence from this piece and no threshold should be moved because of it.

## Pre-flight metrics at final pass

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.527 | >= 0.45 | pass |
| sentences clustered at mean | 31.8% | <= 40% | pass |
| short sentences (< 9 words) | 15.9% | >= 12% | pass |
| long sentences (> 24 words) | 31.8% | >= 12% | pass |
| paragraph size variance (CV) | 0.652 | >= 0.35 | pass |
| top sentence opener | "what" x3 = 6.8% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 1.2 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 14.39 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 19.43 words, standard deviation 10.25, across 44 sentences and 12 paragraphs.

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| | _to be filled after scoring_ | | |

## Findings from the drafting pass

Nothing here needed a detector run to establish.

**This page.** The second page allowed up to 1,000 words. Five mandated sections plus six FAQs run past 700 on their own, so the live page's consequences, handling and alternatives sections were cut to a conclusion. First draft failed the short-sentence floor (7%) and the opener gate ("A" x9, from list items and bullets that each named a thing); fixed with two fragments and by opening list items on the noun without an article. This page carried the most legal claims and each is sourced in refresh-notes.md.

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
