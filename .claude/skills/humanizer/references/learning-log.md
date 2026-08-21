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
| Anaphora across consecutive paragraphs, e.g. three paragraphs opening "It is not X." / "It does not Y." | 2026-08-21, SolusVM HA failover draft | 1 | Caught by hand in the adversarial pass, not by the script. The opener gate measures the whole document and passed this at 7.6%. A positional check (same opener in N consecutive paragraphs) would catch it. Not automated yet. |
| Enumerated preamble, e.g. "Three things stay constant." immediately before exactly three items | 2026-08-21, SolusVM HA failover draft | 1 | Announcing a count before a list. Distinct from the rule-of-three regex, which looks at "X, Y and Z" inside one sentence. Watch for it. |
| Two-beat aphorism closing every section, e.g. "Started, not resumed." | 2026-08-21, SolusVM HA failover draft | 1 | One is voice. Three in a five-section piece is a shape. Also seen as the paragraph-variance culprit on the SolusVM storage piece, though that was a drafting observation rather than a detector highlight, so it does not count as a second sighting yet. |

## Threshold calibration history

| Date | Gate | Old | New | Report that forced it |
| --- | --- | --- | --- | --- |
| 2026-08-21 | all | n/a | initial values | Seeded from editorial prose baselines, not from a ZeroGPT report. Treat every number as provisional until the first three reports land. |
| 2026-08-21 | sentence opener repetition | `opener_repeat_max: 3` (raw count) | `opener_repeat_pct_max: 9.0` with `opener_repeat_floor: 3` | `reports/2026-08-21-sitejet-agency-delivery-sop.md`. A fixed raw cap cannot scale. On a 219-sentence article, "the" opened 16 sentences, which is 7.3% and entirely normal, and the gate failed a clean draft. Now proportional, with the raw floor kept so a 20-sentence piece is still checked. |

## Piece history

| Date | Piece | Words | Pre-flight gates failed | ZeroGPT score | Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-08-21 | Sitejet: agency delivery SOP | 1,072 (cut from 2,956) | 0 of 11 at final pass | pending client run |
| 2026-08-21 | Sitejet: website launch handover | 1,233 | 0 of 11 at final pass | pending client run | Second piece under v3.0. Failed three gates on first draft: paragraph variance, rule of three, and opener repetition. All three came from the same cause, a seven-item listicle structure that pushes every paragraph toward the same shape. Fixed without changing the structure. | First piece under v3.0. Forced one gate recalibration (sentence opener repetition). Client requires APA title case, which conflicts with pattern 17; resolved by excluding headings from the prose scan and compensating with a 22.7 per 1k contraction rate and 37% short sentences. Full report in `reports/2026-08-21-sitejet-agency-delivery-sop.md`. |
| 2026-08-21 | SolusVM: shared vs local storage for VPS | 1,033 | 0 of 11 at final pass | pending client run | Third piece under v3.0, first for a different client and a different voice. Brand guide mandates a formal, documentation-like register, which pushes the contraction rate down; landed at 12.58 per 1k against 22.67 on the Sitejet piece and still passed. The adversarial pass broke the paragraph-variance gate: removing parallel two-beat constructions is a sentence-level edit that flattens paragraph shapes as a side effect. Full report in `reports/2026-08-21-solusvm-shared-vs-local-storage.md`. |
| 2026-08-21 | SolusVM: HA failover | 1,029 | 0 of 11 at final pass | pending client run | Fourth piece under v3.0, second for SolusVM. Failed one gate on first draft (opener repetition, "the" x6 = 9.2%). Lowest contraction rate recorded so far at 5.83 per 1k, and it dipped to 4.85 mid-edit, which is the closest anything has come to that floor. Full report in `reports/2026-08-21-solusvm-ha-failover.md`. |

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

**The adversarial pass can break a gate the trim pass left clean.** Removing
symmetric two-beat constructions ("X wins on A. Y wins on B.") is the single most
useful editorial fix in the catalogue, and it is also a paragraph-shape edit in
disguise: those pairs were carrying the short paragraphs. Paragraph variance fell
from 0.373 to 0.307 on a draft where nothing else changed. Run the script after
the adversarial pass, not only before it.

**Paragraph variance moves at the extremes.** Two failed repairs nudged
mid-sized paragraphs around and gained 0.023. The third merged a 2-sentence and
a 3-sentence paragraph into one 5-sentence paragraph and cut an FAQ answer to a
single sentence, and the gate went from 0.330 to 0.400 in one edit. This gate is
stdev over mean of paragraph sentence counts, so add a very long paragraph and a
very short one. Do not redistribute the middle.

**Document-wide gates cannot see local clusters.** Three consecutive paragraphs
opened "It is not X." on the SolusVM HA draft. The opener gate passed it at 7.6%
of sentences, comfortably under the 9% cap, because four other paragraphs
started differently and the average absorbed the run. Adjacency is what a reader
and a detector both notice. Until a positional check exists, the adversarial
pass is the only thing that catches this, which is another reason step 4 is not
optional.

**Refusing to invent a number is a detector fix.** The obvious move in an FAQ
asking "how long does failover take" is to give a range. No figure could be
verified, so the answer says to test it on your own hardware instead. That
sentence is less predictable than any plausible range would have been, and it is
also the only honest version. The brand guide's rule against unspecific
performance claims and the perplexity signal want the same thing here.

**A formal brand voice costs you contractions, and that is survivable.** The
SolusVM guide asks for a register close to technical documentation. That halved
the contraction rate against the previous client (12.58 per 1k against 22.67)
while still clearing the 4.0 floor. The floor is low for exactly this reason.
Compensate on rhythm and specificity, not by forcing contractions into copy the
brand would reject.

**Gates that use raw counts do not survive contact with a long piece.** Any
threshold expressed as an absolute number needs checking against a 3,000-word
draft before it is trusted. The opener gate failed this test on the first real
article it saw. If you add a gate, express it per thousand words or as a
percentage of sentences.
