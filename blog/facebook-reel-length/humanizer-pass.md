# Humanizer pass log

Tool: `.claude/skills/humanizer` v4.0.
Run from `.claude/skills/humanizer`:

```bash
python3 scripts/zerogpt_preflight.py ../../../blog/facebook-reel-length/facebook-reel-length.md --verbose
python3 scripts/scan.py ../../../blog/facebook-reel-length/facebook-reel-length.md
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


---

## Addendum 2: running the skill's own gate script

The calibration engine above was built as a separate skill before I found that
this repo already had a `humanizer` skill on the other branch, with a gate
script and a manual learning protocol. The two are now merged into
`.claude/skills/humanizer` v4.0.

Running the established `zerogpt_preflight.py` against this draft immediately
failed two gates that the new scanner had reported clean:

| Gate | Result | Verdict |
| --- | --- | --- |
| paragraph size variance (CV) | 0.349, floor is 0.35 | Real. The FAQ format produces a run of identically sized two-sentence paragraphs, which flattens the distribution. |
| sentence opener repetition | "the" opened 12.1% of sentences, cap is 9% | Real. Seven sentences began with "The". |

Both were fixed in the draft rather than by moving the thresholds: four "The"
openers rewritten, one paragraph merged into a longer one, one split into a
single-sentence paragraph.

That disagreement is the useful part. Pass/fail gates on the whole document
catch distribution problems a per-sentence ranking averages away, and the
ranking catches sentence-level problems the gates never see. The finding is
recorded in `references/learning-log.md` under standing findings.

Fixing the merge also caught one more scanner defect: image credit lines were
being counted as prose sentences, producing a phantom "three sentences open with
'image source'" hit. The older skill's own notes already said credit lines are
not prose. The detector now excludes them.

## Final state

| Check | Result |
| --- | --- |
| `zerogpt_preflight.py` | **11 of 11 gates pass.** CV 0.555, paragraph CV 0.385, marker density 0.0/1k, contraction rate 21.6/1k |
| `scan.py` | **0.1/100**, no sentence-level hits |
| Real ZeroGPT run | **Not done.** Needs a human to paste the article in |


---

## Addendum 3: the real ZeroGPT run, 23.4%

The client ran the .docx through ZeroGPT. Result: **23.4% AI**, verdict "Most
Likely Human written, may include parts generated by AI", 1,232 words counted.

The highlights were read out of the exported PDF by span colour rather than by
eye. Flagged body text is `#000000`, clean body text is `#60657b`, both Segoe UI
12pt, which is very easy to mistake in a screenshot. Full report and the
verbatim highlighted sentences are filed at
`.claude/skills/humanizer/reports/2026-08-21-socialbee-facebook-reel-length.md`.

### What the pre-flight had said

All 11 gates passed. `scan.py` scored 0.1/100. Ingesting the report put the
scanner's recall against it at **0.0**: of 21 flagged sentences, it had
predicted none.

That is the useful part of the whole exercise. Both tools were measuring real
things and neither was measuring the thing that mattered.

### The one pattern behind almost all of it

Every substantial highlight was one half of a matched pair or triad. Not the
rule of three inside a sentence, which the skill already caught, but
neighbouring sentences built to the same grammatical template:

| What was flagged | The template |
| --- | --- |
| Three numbered list items | `<noun phrase>: <N> to <M> seconds, <qualifier>` three times. The items were flagged; the numerals "1." "2." "3." between them came back clean |
| Two sentences three paragraphs apart | Both opened `A <N>-second Reel that/stretched ...` |
| Two consecutive Key Takeaways bullets | Same shape |
| One citation sentence | `X covered A, and Y reported B` |
| The SocialBee paragraph | `a 12-second hook for Tuesday and a 60-second demo for Thursday`, then `Preview each one ..., then drop it into ...` |

All of it was written that way deliberately, because parallel structure reads
well. It is also the most predictable thing a writer can do, which is exactly
what a perplexity model rewards with a highlight.

Two secondary findings: the flags concentrated in the intro and the product
pitch, the two places writing gets smoothed into a template; and three cells of
the specs table came back highlighted, so the detector flattens tables and
reads them as prose.

### What changed

A new signal, `parallel_construction`, in two parts:

- `parallel_opening` compares sentences on a shape signature where numbers
  become `#` and content words become `*`, so "A 45-second Reel stretched..."
  and "A 25-second Reel that most..." match despite sharing almost no
  vocabulary. The existing `repeated_openers` check, which compares raw first
  words, cannot see this.
- `parallel_structure` compares near neighbours by longest common subsequence
  over the full skeleton, gated on matching punctuation and numeral count, and
  requires a shared anchor so two unrelated sentences cannot match on shape
  alone.

Both are regression-tested in `tests/run_tests.sh` against the exact text
ZeroGPT flagged.

Then all 17 highlighted spans were rewritten. The short answer, the takeaway
bullets, the three list items, both "A N-second Reel" sentences, the citation
sentence and the whole SocialBee paragraph.

Two of the pairs the detector caught afterwards were ones the rewrite itself
had created, including a takeaway bullet that had become a near-duplicate of a
sentence in the intro. Those were fixed too.

### Where it stands

| Check | Before | After |
| --- | --- | --- |
| ZeroGPT | 23.4% AI | **not yet re-run** |
| `zerogpt_preflight.py` | 11 of 11 pass | 11 of 11 pass |
| `scan.py` | 0.1/100, recall 0.0 against the report | 0.6/100, no sentence-level hits, parallelism cleared |
| Words | 1,017 prose | 1,036 prose |

The skill now knows something it did not know this morning, and the memory
holds it: 21 flagged spans and 52 clean ones in the corpus, weights for both
parallelism signals calibrated by their measured lift, and the session logged.

**This needs a second ZeroGPT run to confirm.** The rewrite targets exactly what
the detector highlighted and the new signal is clean, but nothing here proves
the 23.4% actually moved. Run it again and file the result the same way; the
score history will then show whether the fix worked.
