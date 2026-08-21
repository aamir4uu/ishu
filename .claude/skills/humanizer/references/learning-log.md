# Learning Log

This is the part of the skill that changes. Every piece that gets scored in
ZeroGPT produces a report, the report produces findings, and the findings edit
this file, `zerogpt-signals.md`, or the thresholds in
`scripts/zerogpt_preflight.py`. Nothing gets added here on a hunch. An entry
needs a report behind it.

## What changed in v4.0

The update protocol below used to be entirely manual: read the highlights, map
each to a signal, decide what to promote, hand-edit thresholds. That works, and
it is also the step people skip.

v4.0 automates the mechanical half. `scripts/learn.py` ingests a filed report,
matches the highlighted spans back to the draft, recalibrates each signal's
weight by its observed lift in flagged versus accepted sentences, mines
repeat-offender n-grams into `memory/learned_rules.json`, and prints the
scanner's recall against that report. Everything it learns lands in `memory/`,
which is committed.

The judgement half stays manual and stays below: deciding whether a gate in
`zerogpt_preflight.py` is too loose or too tight, and writing the piece-history
row. A script cannot tell the difference between a threshold that is wrong and
a draft that was bad.

## How to update the skill after a ZeroGPT run

0. Run `python3 scripts/learn.py <report>` first. It does steps 3 and 4 for you
   and prints its own recall. Then do the rest by hand.
1. Score the published or final draft at zerogpt.com. Save the full report to
   `reports/YYYY-MM-DD-slug.md` using `reports/TEMPLATE.md`.
2. Copy every highlighted sentence into the report verbatim. The highlights are
   the data. The percentage is just a headline.
3. For each highlighted sentence, name the signal that caused it. If it maps to
   an existing entry in `zerogpt-signals.md`, note the entry. If it does not,
   you have found something new.
4. New patterns go in the table below with the report that produced them. Once
   a pattern appears in two separate reports, promote it: add it to the
   relevant `MARKERS` family in `zerogpt_preflight.py` so it gets caught
   automatically next time.
5. If a gate in `zerogpt_preflight.py` passed but ZeroGPT still flagged the
   piece, the threshold is too loose. Tighten it, record the old and new value
   in the calibration table, and say which report forced the change.
6. If a gate failed but ZeroGPT scored clean, the threshold may be too tight.
   Do not loosen on a single sample. Wait for three.

## Pattern candidates

Patterns observed in ZeroGPT highlights that are not yet automated. Promote at
two independent sightings.

| Pattern | First seen | Sightings | Status |
| --- | --- | --- | --- |
| Tailing rhetorical triple used as a section opener, e.g. "You cap them, you channel them, and you price the overflow." | 2026-08-21, Sitejet SOP draft | 1 | Caught by the existing rule-of-three regex during drafting, before any detector run. Not yet a new pattern. Watch whether ZeroGPT highlights this shape specifically. |

## Threshold calibration history

| Date | Gate | Old | New | Report that forced it |
| --- | --- | --- | --- | --- |
| 2026-08-21 | all | n/a | initial values | Seeded from editorial prose baselines, not from a ZeroGPT report. Treat every number as provisional until the first three reports land. |
| 2026-08-21 | sentence opener repetition | `opener_repeat_max: 3` (raw count) | `opener_repeat_pct_max: 9.0` with `opener_repeat_floor: 3` | `reports/2026-08-21-sitejet-agency-delivery-sop.md`. A fixed raw cap cannot scale. On a 219-sentence article, "the" opened 16 sentences, which is 7.3% and entirely normal, and the gate failed a clean draft. Now proportional, with the raw floor kept so a 20-sentence piece is still checked. |

## Piece history

| Date | Piece | Words | Pre-flight gates failed | ZeroGPT score | Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-08-21 | SocialBee: Facebook Reel length | 1,017 | 0 of 11 at final pass | not yet run | Second piece. First run under v4.0. Two gates failed on the first pass and were fixed in the draft, not the thresholds: paragraph size variance at CV 0.349 against a 0.35 floor, and "the" opening 12.1% of sentences against a 9% cap. Both were real. The FAQ format produces a run of same-size paragraphs, which is what pushed paragraph variance to the floor. Client requires APA title case, same conflict as the previous piece, resolved the same way. `scan.py` scores 0.0 with no sentence-level or rhythm hits. Awaiting the client's ZeroGPT run before anything is ingested. |
| 2026-08-21 | Sitejet: agency delivery SOP | 1,072 (cut from 2,956) | 0 of 11 at final pass | pending client run | First piece under v3.0. Forced one gate recalibration (sentence opener repetition). Client requires APA title case, which conflicts with pattern 17; resolved by excluding headings from the prose scan and compensating with a 22.7 per 1k contraction rate and 37% short sentences. Full report in `reports/2026-08-21-sitejet-agency-delivery-sop.md`. |

## Defects found by building the v4.0 test suite

`tests/run_tests.sh` scores a deliberately AI-sounding fixture and asserts the
pipeline reacts. Writing it exposed four defects that had been silently making
the scanner look better than it was. Recorded because the failure modes will
recur.

**A splitter that chops hard-wrapped lines destroys the rhythm numbers.** The
first version treated every newline as a sentence boundary. Markdown wraps prose
across lines, so sentences were cut mid-clause and the length statistics were
meaningless. The scanner reported 9.2 on a draft that actually scored 32.6. It
now rebuilds blocks before splitting, and still treats list items and bolded FAQ
question lines as genuine boundaries.

**Averaging risk across a long document hides the sentences that get
highlighted.** ZeroGPT highlights individual sentences; a mean does the opposite
of that. The score now carries a separate term for the share of the document
that is flaggable, not just the average.

**Documented patterns are not implemented patterns.** "Despite these challenges,
the future looks bright." sailed through a scanner whose own reference file
described both halves of it. Recall on the fixture went from 0.86 to 1.0 once
`challenges_trope` and `generic_closer` were actually written.

**A statistical rule miner will learn the topic.** Given a flagged corpus about
remote work, it promoted "remote work" as an AI tell. Fixed with
`memory/never_promote.txt`, a minimum corpus size before anything is promoted, a
maximal-n-gram filter so one phrase does not become nine rules, and
`learn.py --unlearn` for correction.

## Standing findings

Things learned that are already baked into the skill, kept here so the reason
survives.

**Two measurements beat one.** The gate script and the ranking script disagree
usefully. On the Facebook Reel piece `scan.py` reported nothing while
`zerogpt_preflight.py` failed two gates, both real. Pass/fail gates catch
distribution problems that a per-sentence ranking averages away, and the ranking
catches sentence-level problems that a gate on the whole document never sees.
Run both.

**Headings are not prose.** ZeroGPT scores sentences. Markdown headings, table
rows, and image credit lines are not sentences a detector weighs the same way,
and including them in the burstiness calculation produced misleading CV numbers
in early testing. `strip_markdown()` removes them before analysis.

**Uniformity beats vocabulary.** A draft with three flagged AI vocabulary words
and high sentence variance scores better than a draft with clean vocabulary and
flat sentence lengths. When time is short, fix the rhythm first.

**Intros flag hardest.** Across drafts, the first two paragraphs get highlighted
more than any other part of the piece. They are the most formulaic thing a model
produces. Write them last and write them by hand.

**Specificity is a detector fix, not just an editorial one.** Named numbers,
dates, tools, and dollar figures raise perplexity. Client checklists that ask
for citable data points are asking for the same thing the detector rewards.

**Fixing one pattern can break another gate.** Rewriting bold-header bullet
lists (pattern 16) into flowing prose removed long sentences and dropped the
long-sentence share below its floor, failing a gate that had been passing.
Structural edits change the length distribution. Re-run the script after every
structural edit, not only at the end.

**Cutting a piece in half breaks the variance gates.** Trimming this article
from 2,956 words to a 1,000-word spec dropped it below both the long-sentence
floor and the paragraph-variance floor, because trimming attacks long sentences
first. The fix was to restore length in a few specific places rather than trim
evenly: one long sentence per section, plus two single-sentence paragraphs.
Re-run after any large cut, and expect to add words back.

**Gates that use raw counts do not survive contact with a long piece.** Any
threshold expressed as an absolute number needs checking against a 3,000-word
draft before it is trusted. The opener gate failed this test on the first real
article it saw. If you add a gate, express it per thousand words or as a
percentage of sentences.
