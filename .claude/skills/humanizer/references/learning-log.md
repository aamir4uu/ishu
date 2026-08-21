# Learning Log

This is the part of the skill that changes. Every piece that gets scored in
ZeroGPT produces a report, the report produces findings, and the findings edit
this file, `zerogpt-signals.md`, or the thresholds in
`scripts/zerogpt_preflight.py`. Nothing gets added here on a hunch. An entry
needs a report behind it.

## How to update the skill after a ZeroGPT run

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
| Counted rule of three: an announcement like "read each answer for three things" followed by exactly three items. | 2026-08-21, XOVI AI content piece | 1 | Invisible to the `X, Y and Z` regex because the three items are separate sentences. Found by hand in the adversarial pass. If it shows up again, the check is a regex for `\b(three|four) (things|reasons|questions|steps)\b` followed by a matching count. |
| A run of verb-first imperative headings, four or more, all roughly the same length. | 2026-08-21, XOVI AI content piece | 1 | Headings are excluded from the prose scan on purpose, so no gate can see this. It is an editorial tell rather than a detector one, but it is the first thing a human reviewer names. A heading-shape check would be a new gate, not a new marker. |
| A feature list rewritten as consecutive subject-verb-object sentences, one per feature. | 2026-08-21, XOVI AI content piece | 1 | Passes every variance gate because the sentences differ in length. Still reads as a bullet list with the bullets deleted. Watch for it in any section that has to cover a fixed set of product capabilities. |

## Threshold calibration history

| Date | Gate | Old | New | Report that forced it |
| --- | --- | --- | --- | --- |
| 2026-08-21 | all | n/a | initial values | Seeded from editorial prose baselines, not from a ZeroGPT report. Treat every number as provisional until the first three reports land. |
| 2026-08-21 | sentence opener repetition | `opener_repeat_max: 3` (raw count) | `opener_repeat_pct_max: 9.0` with `opener_repeat_floor: 3` | `reports/2026-08-21-sitejet-agency-delivery-sop.md`. A fixed raw cap cannot scale. On a 219-sentence article, "the" opened 16 sentences, which is 7.3% and entirely normal, and the gate failed a clean draft. Now proportional, with the raw floor kept so a 20-sentence piece is still checked. |

## Piece history

| Date | Piece | Words | Pre-flight gates failed | ZeroGPT score | Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-08-21 | Sitejet: agency delivery SOP | 1,072 (cut from 2,956) | 0 of 11 at final pass | pending client run |
| 2026-08-21 | XOVI: stop writing content AI tools can't understand | 1,035 prose / 1,154 with headings | 1 of 11 on first draft, 0 at final pass | pending client run | Third piece under v3.0, and the first under 1,100 words. Only failure was paragraph variance at 0.324, caused by the spec rather than the prose: a 1,000-word article carrying Key Takeaways, four H3 fixes, a PAA section and a five-question FAQ has no room for a long paragraph. Fixed with two single-sentence paragraphs split out of existing ones, at zero word cost. Three further tells were found by hand after the gates were clean. Full report in `reports/2026-08-21-xovi-ai-content-optimisation.md`. |
| 2026-08-21 | Sitejet: website launch handover | 1,233 | 0 of 11 at final pass | pending client run | Second piece under v3.0. Failed three gates on first draft: paragraph variance, rule of three, and opener repetition. All three came from the same cause, a seven-item listicle structure that pushes every paragraph toward the same shape. Fixed without changing the structure. | First piece under v3.0. Forced one gate recalibration (sentence opener repetition). Client requires APA title case, which conflicts with pattern 17; resolved by excluding headings from the prose scan and compensating with a 22.7 per 1k contraction rate and 37% short sentences. Full report in `reports/2026-08-21-sitejet-agency-delivery-sop.md`. |

## Standing findings

Things learned that are already baked into the skill, kept here so the reason
survives.

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

**Listicle structures flatten everything at once.** A seven-item numbered
section drove three separate gate failures in one draft: every item became a
three-sentence paragraph (paragraph variance), each item body reached for an
"X, Y and Z" list (rule of three), and nine sentences opened with "A" because
each item began by naming a thing. The structure was correct for the topic and
was kept. The fix was per-item: vary the sentence count deliberately, convert
two triples into pairs plus a trailing clause, and reword four openers. Expect
this cluster whenever a piece is built from parallel numbered items.

**Short specs break paragraph variance, and the repair is free.** Below roughly
1,100 words, a brief that mandates a takeaways box, a PAA section and an FAQ
forces almost every paragraph into the two-to-four sentence band, and the
paragraph CV gate fails on structure rather than on writing. Do not fix it by
writing a long paragraph; a short spec has no words to spare. Split two existing
paragraphs so a single sentence stands alone. That moved the XOVI piece from
0.324 to 0.368 without adding a word.

**A clean gate run is not the end of the adversarial pass.** Every tell found in
the XOVI piece after the gates went green was invisible to the script by
design: parallel headings (headings are stripped before scanning), a counted
rule of three spread across sentences (the regex looks for `X, Y and Z`), and a
feature list rewritten as prose (the sentence lengths varied, so the variance
gates were happy). The script measures rhythm and vocabulary. Shape is still a
human job.

**Gates that use raw counts do not survive contact with a long piece.** Any
threshold expressed as an absolute number needs checking against a 3,000-word
draft before it is trusted. The opener gate failed this test on the first real
article it saw. If you add a gate, express it per thousand words or as a
percentage of sentences.
