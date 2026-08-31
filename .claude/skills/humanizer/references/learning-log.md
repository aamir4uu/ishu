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
| Sentence-closer repetition in verb-final languages. Hindi drafts closing 45.5% and 33.3% of sentences on `है।` | 2026-08-31, Hero FinCorp education loan | 1 | **Promoted to a gate, not a marker.** `closer_repeat_pct_max` added. Thresholds provisional pending a human-Hindi baseline. |
| Document scaffolding pasted into the detector along with the copy: image placeholders, alt-text lines, meta fields. Verbatim-repeated English boilerplate inside Hindi prose | 2026-08-31, Hero FinCorp education loan | 1 | Fixed at source with `tools/detector-paste.py`. Watch whether removing it alone moves a score. |
| Tailing rhetorical triple used as a section opener, e.g. "You cap them, you channel them, and you price the overflow." | 2026-08-21, Sitejet SOP draft | 1 | Caught by the existing rule-of-three regex during drafting, before any detector run. Not yet a new pattern. Watch whether ZeroGPT highlights this shape specifically. |

## Threshold calibration history

| Date | Gate | Old | New | Report that forced it |
| --- | --- | --- | --- | --- |
| 2026-08-21 | all | n/a | initial values | Seeded from editorial prose baselines, not from a ZeroGPT report. Treat every number as provisional until the first three reports land. |
| 2026-08-31 | sentence closer repetition | gate did not exist | `closer_repeat_pct_max: 12.0`, `closer_repeat_pct_max_devanagari: 30.0`, floor 3 | `reports/2026-08-31-herofincorp-education-loan-hindi.md`. First report where the pre-flight passed a draft ZeroGPT then scored 89.4%. The protocol says that condition tightens something. Openers were gated from the first report; nothing looked at closers, and Hindi is verb-final. Both numbers are **provisional guesses at a natural rate**, not measurements: no human-written Hindi has been scored yet. The English figure of 12% is a loose safety net, well above the 3.0% the English draft actually showed. |
| 2026-08-29 | strip_markdown (measurement, not a threshold) | list items and `[Image Source]` lines fed into the sentence splitter as-is | list items terminated so each counts as one sentence; image credit lines dropped; `**Meta Title:**` / `**Meta Description:**` lines dropped | No report. Found while writing the Hero FinCorp set. A markdown list has no sentence terminators, so the splitter was swallowing an entire bullet block into one "sentence" of 40 or 80 words. That single fake sentence was carrying the long-sentence gate on any bullet-heavy draft. Re-measuring the two Sitejet articles with the fix drops them to 11.4% and 11.6% against a 12% floor, so **both were passing that gate on an artefact**. Their filed results are stale; the copy was not changed. |
| 2026-08-21 | sentence opener repetition | `opener_repeat_max: 3` (raw count) | `opener_repeat_pct_max: 9.0` with `opener_repeat_floor: 3` | `reports/2026-08-21-sitejet-agency-delivery-sop.md`. A fixed raw cap cannot scale. On a 219-sentence article, "the" opened 16 sentences, which is 7.3% and entirely normal, and the gate failed a clean draft. Now proportional, with the raw floor kept so a 20-sentence piece is still checked. |

## Piece history

| Date | Piece | Words | Pre-flight gates failed | ZeroGPT score | Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-08-21 | Sitejet: agency delivery SOP | 1,072 (cut from 2,956) | 0 of 11 at final pass | pending client run |
| 2026-08-21 | Sitejet: website launch handover | 1,233 | 0 of 11 at final pass | pending client run |
| 2026-08-29 | Hero FinCorp: what is collateral | 961 | 0 of 11 at final pass | pending client run | English, UK spelling. Failed opener repetition on the first draft ("the" x6 = 9.2%), fixed by rewording five sentence openings. Trimming to the brief's per-section word caps then cost the long-sentence gate, recovered by merging pairs rather than restoring words. |
| 2026-08-29 | Hero FinCorp: CIBIL score (Hindi) | 935 | 0 of 10 applicable at final pass | pending client run | First Devanagari piece. Contraction gate is N/A. Needed three separate rounds on the long-sentence gate: it broke on the first draft, again after the section trim, and again after the meta-field fix changed the sentence count. |
| 2026-08-29 | Hero FinCorp: education loan (Hindi) | 860 | 0 of 10 applicable at final pass | pending client run | Three bullet lists in nine sections. Long-sentence share read 13.0% before the strip_markdown fix and 4.6% after, which is the clearest single measurement of how badly the bullet bug distorted things. | Second piece under v3.0. Failed three gates on first draft: paragraph variance, rule of three, and opener repetition. All three came from the same cause, a seven-item listicle structure that pushes every paragraph toward the same shape. Fixed without changing the structure. | First piece under v3.0. Forced one gate recalibration (sentence opener repetition). Client requires APA title case, which conflicts with pattern 17; resolved by excluding headings from the prose scan and compensating with a 22.7 per 1k contraction rate and 37% short sentences. Full report in `reports/2026-08-21-sitejet-agency-delivery-sop.md`. |
| 2026-08-31 | Hero FinCorp: education loan (Hindi), **scored** | 1,188 as pasted | 0 of 10 applicable | **89.4% AI** | The whole .docx was pasted, scaffolding included. Commonest sentence ending was 33.3%. See the report. |
| 2026-08-31 | Hero FinCorp: education loan (Hindi), revised | 856 | 0 of 10 applicable | pending rescore | Commonest ending cut to 6.1%. |
| 2026-08-31 | Hero FinCorp: CIBIL score (Hindi), revised | 933 | 0 of 10 applicable | pending rescore | Commonest ending cut from 45.5% to 6.1%. Never scored in its original form. |

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

**Gates that use raw counts do not survive contact with a long piece.** Any
threshold expressed as an absolute number needs checking against a 3,000-word
draft before it is trusted. The opener gate failed this test on the first real
article it saw. If you add a gate, express it per thousand words or as a
percentage of sentences.

**Devanagari drafts measure on ten gates, not eleven.** Apostrophe contractions
do not exist in Hindi, so the contraction gate measures nothing and is reported
as N/A above a 50% Devanagari word share. Nothing replaces it yet. That is a
real hole: contraction rate was the proxy for register informality, and a Hindi
draft can now be stiff and formal without any gate objecting. The Hindi
equivalent would be a floor on colloquial particles, but there is no report
behind such a list yet, so none was invented. Watch for it in the first Hindi
ZeroGPT report.

**AI-written Hindi reaches for translated scaffolding.** Three Hindi marker
families were added to `MARKERS` on the same reasoning as their English
counterparts: connective scaffolding (इसके अलावा, निष्कर्ष के रूप में, अंततः),
signposting (आइए जानते हैं, इस लेख में हम) and significance inflation
(महत्वपूर्ण भूमिका निभाता है, ध्यान देने योग्य बात यह है कि). These are
predictions from the English patterns, not observations from a Hindi report.
Treat them as provisional until a Hindi ZeroGPT report either confirms or
clears them.

**A per-section word cap fights the long-sentence gate.** The Hero FinCorp
briefs specify a word count for every H2, and trimming to a cap attacks long
sentences first, exactly as the earlier bulk-cut finding predicted. The fix
that works inside a cap is merging: turning two 14-word sentences into one
27-word sentence removes a sentence, adds a long one, and costs no words at
all. Deleting clauses does the opposite on both counts. Reach for the merge
before the delete whenever a word ceiling is binding.

**Metadata carried in a draft is not prose.** The Hero FinCorp sample puts the
meta title and meta description in the body of the .docx, under the H1. Left
unstripped they read as two ~20-word sentences with no contractions, which
pushed one draft below the long-sentence floor purely by changing the
denominator. They are now stripped alongside headings.

**A passing pre-flight is not a passing score, and the gap is widest in Hindi.**
The education loan draft passed every applicable gate and came back 89.4% AI.
The gates measure proxies for perplexity; they do not measure perplexity. On
English there are now four pieces of evidence that the proxies track something
real. On Hindi there is one piece of evidence and it is a failure. Treat a clean
Hindi pre-flight as "nothing obvious is wrong", not as "this will pass".

**Gate the sentence ending, not just the opening.** Which end of a sentence
carries the predictable part depends on the language. English front-loads the
subject, so "The" opening sixteen sentences is the tell. Hindi puts the verb
last, so `है।` closing half of them is the same tell at the other end. Any
future language needs the same question asked: where does this language put the
part a model would predict?

**Paste the article, not the document.** A deliverable carries scaffolding a
published page never shows. Pasting it into a detector scores boilerplate that
repeats verbatim, often in a different language from the body, and in this case
smuggled in an em dash the gates ban. `tools/detector-paste.py` now emits
exactly what should be pasted. Generate it and hand it over with the draft.

**Get the highlights out of the report.** A ZeroGPT PDF exported through a
browser print with background graphics off loses every highlight, and the
highlights are the data the protocol runs on. Ask for them explicitly: tick
"Background graphics" in the print dialog, or send a screenshot of the result
panel. A percentage alone supports one report; it cannot support a pattern.
