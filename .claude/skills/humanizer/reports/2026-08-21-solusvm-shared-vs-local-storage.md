# ZeroGPT Report: SolusVM, Choosing Between Shared Storage and Local Storage for VPS Infrastructure

- Date scored: pending
- File scored: `blog/vps-storage-choice/shared-vs-local-storage-vps.md`
- Word count: 1,033 body words
- ZeroGPT result: **pending client run**
- Detector version or URL: https://www.zerogpt.com
- Pre-flight run before scoring: yes, output saved to `blog/vps-storage-choice/zerogpt-preflight-result.txt`
- Gates failing at time of scoring: 0 of 11

Filed open, same as the two Sitejet reports. This environment has no outbound
access to zerogpt.com, and pasting client copy into a third-party detector is
the client's call to make, not ours. Whoever runs it should paste the result and
every highlighted sentence into the table below, then work the actions
checklist. Until that happens this piece is not evidence and no threshold should
move because of it.

## Pre-flight metrics at final pass

| Gate | Value | Threshold | Result |
| --- | --- | --- | --- |
| sentence length variance (CV) | 0.624 | >= 0.45 | pass |
| sentences clustered at mean | 27.9% | <= 40% | pass |
| short sentences (< 9 words) | 29.4% | >= 12% | pass |
| long sentences (> 24 words) | 17.6% | >= 12% | pass |
| paragraph size variance (CV) | 0.400 | >= 0.35 | pass |
| top sentence opener | "local" x6 = 8.8% | <= 9% | pass |
| AI marker density | 0.0 per 1k | <= 2.2 | pass |
| em dashes | 0 | 0 | pass |
| curly quotes | 0 | 0 | pass |
| rule of three | 0.0 per 1k | <= 2.0 | pass |
| contraction rate | 12.58 per 1k | >= 4.0 | pass |

Mean sentence length 15.31 words, standard deviation 9.56, across 68 sentences
and 20 paragraphs.

## Drafting history for this piece

| Pass | Words | Gates failed | What changed |
| --- | --- | --- | --- |
| First draft | 1,184 | 0 of 11 | Written against the brand guide voice, with figures sourced before drafting rather than after. |
| Trim to spec, pass 1 | 1,107 | 0 of 11 | Cut whole clauses, kept the sentence count roughly flat. |
| Trim to spec, pass 2 | 1,029 | 0 of 11 | Removed one FAQ pair and tightened bullets. |
| Adversarial pass | 1,036 | 1 of 11 (paragraph variance, CV 0.307) | Broke up three parallel two-beat constructions and cut four "rather than" clauses. Removing those flattened the paragraph shapes. |
| Repair 1 | 1,032 | 1 of 11 (CV 0.330) | Split one paragraph, merged two others. Not enough. |
| Repair 2 | 1,033 | 0 of 11 (CV 0.400) | Merged a 2-sentence and a 3-sentence paragraph into one 5-sentence paragraph, and collapsed one FAQ answer to a single sentence. Extremes at both ends is what moves this gate, not nudging the middle. |

## Adversarial pass, recorded

The question the skill asks: "What makes the text below so obviously AI
generated?" The answers at the pre-adversarial draft, and what was done:

1. **Symmetric two-beat constructions stacked.** "Local storage wins on latency.
   Shared storage wins on recovery time. There is no configuration that wins
   both." Then "Less than the folklore says... Considerably more if you don't."
   Then "As a ratio... As an absolute number..." Three antithesis pairs inside
   400 words. Two were rewritten, one was kept because the section needs it.
2. **"X rather than Y" as a tic.** Five instances. Cut to one.
3. **Every H2 section opened with a declarative topic sentence followed by
   support.** Uniform enough to feel generated. Two sections were reopened with
   a fragment or a scene ("A host dies at 03:00.").
4. **No admitted uncertainty and no first-hand detail.** Partly unfixable inside
   a brand-voice piece that must not hedge. Compensated with specificity: eight
   named figures, three named storage mechanisms, one named product constraint.

## Highlighted sentences

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| | _to be filled after scoring_ | | |

## Actions after scoring

- [ ] Paste the ZeroGPT percentage and every highlighted sentence above.
- [ ] Map each highlight to a signal in `references/zerogpt-signals.md`, or mark it NEW.
- [ ] Add any NEW pattern to the candidates table in `references/learning-log.md`.
- [ ] If a gate passed here but ZeroGPT flagged the piece, tighten it and record the change.
- [ ] Update the piece history row in `references/learning-log.md` with the real score.
