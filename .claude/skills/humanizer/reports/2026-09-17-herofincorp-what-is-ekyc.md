# ZeroGPT Report: Hero FinCorp: E-KYC, Meaning, Full Form, Types, Process, and Eligibility (refresh)

> **SUPERSEDED on 2026-09-18.** The draft described here was scored in
> ZeroGPT and came back above the client bar. See
> `2026-09-18-herofincorp-what-is-ekyc.md` for the score, the highlighted sentences
> and the rewrite. The metrics below describe a draft that no longer exists.


- Date scored: pending
- File scored: `blog/herofincorp/what-is-ekyc/what-is-ekyc.md`
- Word count: 698 as the client counts it (headings, body, tables and captions; `tools/count-words.py`); 644 words of prose as the pre-flight measures it
- Length brief: 500 to 700 words, up to 700 for this page
- ZeroGPT result: **pending client run**
- Detector version or URL: https://www.zerogpt.com
- Pre-flight run before scoring: yes, saved to `blog/herofincorp/what-is-ekyc/zerogpt-preflight-result.txt`
- Gates failing at time of scoring: 0 of 11

This report is filed open. The environment that produced the draft has no
outbound access to zerogpt.com, so the piece has not been scored yet. Whoever
runs it should paste the result and the highlighted sentences into the table
below, then work the actions checklist. Until that happens this skill has no
new evidence from this piece and no threshold should be moved because of it.

## Pre-flight metrics at final pass

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.525 | >= 0.45 | pass |
| sentences clustered at mean | 35.1% | <= 40% | pass |
| short sentences (< 9 words) | 13.5% | >= 12% | pass |
| long sentences (> 24 words) | 21.6% | >= 12% | pass |
| paragraph size variance (CV) | 0.608 | >= 0.35 | pass |
| top sentence opener | "you" x3 = 8.1% | <= 9% (floor 3) | pass |
| AI marker density | 0.0 per 1k | <= 2.2 per 1k | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.0 per 1k | <= 2.0 per 1k | pass |
| contraction rate | 20.19 per 1k | >= 4.0 per 1k | pass |

Mean sentence length 16.89 words, standard deviation 8.87, across 37 sentences and 15 paragraphs.

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| | _to be filled after scoring_ | | |

## Findings from the drafting pass

Nothing here needed a detector run to establish.

**This page.** Four new sections and four FAQs inside 700 words. The clustered-at-mean gate failed twice while trimming, because cutting words from long sentences pulls them into the middle band; the fix was a deliberate pair of very short sentences and one merged 30-word one. The final trim also caught a rule-of-three hit that the earlier draft did not have ("gender, address and photo, and nothing else"), which is the regex reading a four-item list as a triple.

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
