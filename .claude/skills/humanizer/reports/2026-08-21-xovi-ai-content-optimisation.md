# ZeroGPT Report: Stop Writing Content AI Tools Can't Understand (XOVI)

- Date scored: 2026-08-21 (pre-flight only)
- File scored: `blog/ai-content-optimisation/ai-content-optimisation.md`
- Word count: 1,035 prose words / 1,154 including headings
- ZeroGPT result: **not run.** Outbound access to zerogpt.com is blocked by the
  network egress proxy in this environment, along with pexels.com,
  pewresearch.org, ahrefs.com and xovi.com. The detector paste has to happen
  client-side.
- Detector version or URL: n/a
- Pre-flight run before scoring: `python3 scripts/zerogpt_preflight.py blog/ai-content-optimisation/ai-content-optimisation.md --verbose`
- Gates failing at time of scoring: **0 of 11**

## Pre-flight, final pass

```
1035 words / 72 sentences / 24 paragraphs
mean sentence 14.51 words, stdev 10.01

  [PASS] sentence length variance (CV): 0.69 (need >= 0.45)
  [PASS] sentences clustered at mean: 26.4% (need <= 40.0%)
  [PASS] short sentences present: 30.6% (need >= 12.0%)
  [PASS] long sentences present: 16.7% (need >= 12.0%)
  [PASS] paragraph size variance (CV): 0.366 (need >= 0.35)
  [PASS] sentence opener repetition: 'it' x5 = 6.9% of sentences (max 9.0%, floor 3)
  [PASS] AI marker density: 0.0/1k (max 2.2)
  [PASS] em dashes: 0
  [PASS] curly quotes: 0
  [PASS] rule of three: 0.0/1k (max 2.0)
  [PASS] contraction rate: 14.49/1k (need >= 4.0)
```

## Highlighted sentences

None to record. The piece has not been through the detector. This section stays
empty until somebody runs the paste and comes back with the result.

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| - | (pending client-side run) | | |

## Findings

**The paragraph-variance gate is the one that fails first on short pieces.** It
was the only gate to fail on the first draft here, at 0.324 against a 0.35
floor, and it failed for a structural reason rather than a prose one. An
800-1000 word article that carries a Key Takeaways box, four H3 fixes, a PAA
section and a five-question FAQ has almost no room for a paragraph longer than
four sentences, so every paragraph lands in the 2-4 band and the coefficient of
variation collapses. Both of the previous two pieces were over 1,000 words and
neither hit this.

The fix was two single-sentence paragraphs, both made by splitting an existing
paragraph rather than by adding text: "That is the gap." and "Front-load
instead." That moved the gate from 0.324 to 0.368 and cost nothing. Worth
knowing that the repair is free, because the instinct is to write a long
paragraph, which costs words a short spec does not have.

**Three tells the script cannot see, found in the adversarial pass.** All three
survived a clean gate run:

1. Four H3 headings in a row, all verb-first imperatives of similar length
   ("Answer the...", "Name What...", "Attach a...", "Keep One..."). Headings are
   excluded from the prose scan by design, so nothing flagged it. Fixed by
   rewriting the fourth as a noun phrase, "One Set of Facts, Used Everywhere".
2. A product section built from four consecutive subject-verb-object sentences,
   one per feature. That is a feature list with the bullets removed, and it
   reads like one. Fixed by opening with a question, then a "then" clause, then
   an if-clause, then the long sentence.
3. "Read each answer for three things," followed by exactly three questions. A
   counted rule of three, which the `X, Y and Z` regex does not match. Fixed by
   dropping the count.

**A brand guide can pull toward the detector.** The XOVI guide mandates the
approved positioning sentence verbatim, and that sentence contains "AI-powered",
a phrase the same guide bans elsewhere and one that sits close to the marker
vocabulary. The client wins, as SKILL.md says. Compensated with a 14.49/1k
contraction rate, the highest of the three pieces so far, and 30.6% short
sentences.

## Actions taken

- [x] Pattern added to `references/learning-log.md` candidates table
- [ ] Pattern promoted to `MARKERS` in `scripts/zerogpt_preflight.py` (2+ sightings)
- [ ] Threshold changed in `GATES` (record old and new in calibration history)
- [x] `references/zerogpt-signals.md` updated (known-conflicts table)
- [x] Piece history row added to `references/learning-log.md`
