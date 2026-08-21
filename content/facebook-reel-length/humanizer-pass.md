# Humanizer pass log

Tool: `.claude/skills/humanizer-evolve`, scanner version 1.0.0.
Run from `.claude/skills/humanizer-evolve/scripts`:

```bash
python3 scan.py ../../../../content/facebook-reel-length/facebook-reel-length.md
```

## Iterations

| # | Score | Verdict | What the scan caught | What changed |
| --- | --- | --- | --- | --- |
| 1 | 9.2 | clean | 7 forced triads, 1 false range, 3 phantom long sentences | Nothing yet. The phantom hits exposed a bug in the scanner, not the draft. |
| — | — | — | — | **Scanner fix:** the sentence splitter was collapsing markdown line breaks, gluing FAQ question lines onto the answers after them. Headings and table rows were also being counted as prose sentences and faking the rhythm numbers. Both fixed in `detectors.py`. |
| 2 | 32.6 | mostly clean | `low_burstiness` (sd 6.5), `repeated_openers` ("if you" x5), 7 triads | The real score, once the splitter stopped hiding it. Article rewritten from 1,556 to ~1,050 prose words to hit the brief. |
| 3 | 15.0 | clean | `low_burstiness` (sd 6.2), `repeated_openers` ("the in" x3), 3 triads | Tightened, cut the standalone history section into the main answer, folded the ads section into the FAQ. |
| 4 | 6.1 | clean | `low_burstiness` (sd 6.3) only | Triads rewritten as pairs; repeated openers varied. |
| 5 | 6.2 | clean | `low_burstiness` (sd 7.9), 1 long sentence | Deliberately varied sentence lengths: merged some short pairs into longer sentences, cut others to fragments. |
| 6 | **0.0** | clean | nothing | Split the 36-word sentence, final trim. No sentence-level hits and no document-level rhythm signals. |

## What the scanner cannot tell us

Score 0.0 means the draft contains none of the patterns this model knows about.
It does not mean ZeroGPT will pass it. The scanner has no language model behind
it, so it approximates perplexity with countable proxies: sentence-length
burstiness, mid-band clustering, paragraph uniformity, repeated openers,
contraction rate, plus the lexical and syntactic catalogue.

That gap is the whole reason `learn.py` exists.

## Remaining honest tells

Read aloud, two things still feel a little engineered:

1. The Key Takeaways bullets are close to parallel in construction. The
   checklist mandates that box, so the format is fixed, but a human writer
   would probably let one bullet run long and one run short. Partially done;
   worth another look at edit stage.
2. The article has no first-person perspective and no anecdote, because the
   brief calls for second person and a serious register. That is correct for
   the client and slightly flattening for detection purposes. It is a real
   tradeoff, not an oversight.

## Next step, and it needs you

The memory has no real detector data in it yet, only the SocialBee banned lists
seeded with `source: client:socialbee`. The skill starts learning at the first
real report.

1. Paste the article into ZeroGPT.
2. Copy the percentage and every highlighted sentence into a file:

```
draft: content/facebook-reel-length/facebook-reel-length.md
score: <the percentage ZeroGPT gives>
date: 2026-08-21
note: pass 1

## flagged
<one highlighted sentence per line, exactly as shown>
```

3. Save it as `.claude/skills/humanizer-evolve/reports/2026-08-21-pass1.md` and
   run:

```bash
cd .claude/skills/humanizer-evolve/scripts
python3 learn.py ../reports/2026-08-21-pass1.md
```

That recalibrates the signal weights against what ZeroGPT actually reacted to,
promotes any repeat offender phrases into `memory/learned_rules.json`, prints
the scanner's recall against the report, and logs the session. Commit the
`memory/` changes so the next session starts from what this one learned.

---

## Addendum: what building the skill's test suite changed

Writing `tests/run_tests.sh` against a deliberately AI-sounding fixture exposed
four defects in the scanner, all fixed and all re-verified against this article:

1. **The splitter chopped hard-wrapped lines mid-sentence.** Markdown wraps
   prose across lines; the splitter treated every newline as a boundary, which
   destroyed the sentence-length statistics that the rhythm signals depend on.
   It now rebuilds blocks before splitting.
2. **The score diluted bad sentences.** Averaging risk across a long document
   let a handful of very bad sentences disappear into the mean, which is the
   opposite of how a detector behaves. The score now carries a separate term
   for the share of the document that is flaggable.
3. **Two documented patterns were never implemented.** The fixture's "Despite
   these challenges, the future looks bright." sailed through. `challenges_trope`
   and `generic_closer` were added, and the scanner's recall on the fixture went
   from 0.86 to 1.0.
4. **The rule miner promoted topic vocabulary.** It learned "remote work" as an
   AI tell purely because the fixture was about remote work. Added a
   `never_promote.txt` guard seeded with brand and topic terms, a minimum
   corpus size before anything gets promoted, a maximal-n-gram filter, and a
   `--unlearn` command for human correction.

Final scan of this article after all four fixes: **0.0/100, no sentence-level
hits, no document-level rhythm signals.**
