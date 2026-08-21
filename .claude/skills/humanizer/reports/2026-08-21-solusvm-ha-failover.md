# ZeroGPT Report: SolusVM, What Happens When a Node Fails? A Look Inside SolusVM HA Failover

- Date scored: pending
- File scored: `blog/ha-failover/solusvm-ha-failover.md`
- Word count: 1,029 body words
- ZeroGPT result: **pending client run**
- Detector version or URL: https://www.zerogpt.com
- Pre-flight run before scoring: yes, output saved to `blog/ha-failover/zerogpt-preflight-result.txt`
- Gates failing at time of scoring: 0 of 11

Filed open, same as the three before it. No outbound access to zerogpt.com from
this environment, and pasting client copy into a third-party detector is the
client's call. Whoever runs it should fill the highlight table and work the
actions checklist. Until then this piece is not evidence and no threshold moves.

## Pre-flight metrics at final pass

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.571 | >= 0.45 | pass |
| sentences clustered at mean | 25.0% | <= 40% | pass |
| short sentences (< 9 words) | 20.3% | >= 12% | pass |
| long sentences (> 24 words) | 20.3% | >= 12% | pass |
| paragraph size variance (CV) | 0.506 | >= 0.35 | pass |
| top sentence opener | "a" x4 = 6.2% | <= 9% | pass |
| AI marker density | 0.0 per 1k | <= 2.2 | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.0 per 1k | <= 2.0 | pass |
| contraction rate | 5.83 per 1k | >= 4.0 | pass |

Mean sentence length 16.20 words, standard deviation 9.36, across 64 sentences
and 25 paragraphs.

## Drafting history for this piece

| Pass | Words | Gates failed | What changed |
| --- | --- | --- | --- |
| First draft | 1,046 | 1 of 11 (opener repetition, "the" x6 = 9.2%) | Written against the brand guide with the mechanism researched before drafting. |
| Opener repair | 1,041 | 0 of 11 | Reworded three sentence openers and split one 25-word chained sentence the script had flagged as riskiest. |
| Adversarial pass | 1,055 | 0 of 11 | Three structural fixes, below. Added words rather than cutting them. |
| Trim to spec | 1,029 | 0 of 11 | Tightened three passages. Contraction rate fell to 4.85, so one "it is" went back to "it isn't" for margin. |

## Adversarial pass, recorded

"What makes the text below so obviously AI generated?"

1. **Anaphora triple across three consecutive paragraphs.** "It is not live
   migration." / "It does not fail back." / "It does not protect the storage."
   The script counted the openers and passed them at 7.6%, under the 9% cap,
   because the gate measures the whole document. It cannot see three in a row.
   Two of the three were reworded.
2. **Enumerated preamble.** "Three things stay constant." followed by exactly
   three items. Announcing a count before a list is a model habit. The preamble
   was deleted and the list left to speak for itself.
3. **Every section landing on a two-beat aphorism.** Five sections, three of
   which closed on a short punchy line ("Started, not resumed.", "Configure
   both. They answer different failures."). One aphorism is voice. Three is a
   pattern. One was rewritten into a normal-length sentence carrying an actual
   recommendation.
4. **No admitted uncertainty**, which the brand guide's no-hedging rule makes
   hard. Compensated by refusing to invent a number: the FAQ on failover
   duration says to test it on your own hardware rather than quoting a figure
   that would have been fabricated. That is both honest and high-perplexity.

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| | _to be filled after scoring_ | | |

## Actions after scoring

- [ ] Paste the ZeroGPT percentage and every highlighted sentence above.
- [ ] Map each highlight to a signal in `references/zerogpt-signals.md`, or mark it NEW.
- [ ] Add any NEW pattern to the candidates table in `references/learning-log.md`.
- [ ] Check specifically whether the surviving "Started, not resumed." fragment was highlighted. If it was, the two-beat aphorism is a real signal and belongs in the candidates table with a second sighting.
- [ ] Update the piece history row in `references/learning-log.md` with the real score.
