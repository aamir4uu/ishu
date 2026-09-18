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
| Aphoristic one-line opener on FAQ answers and sections ("Timing is the main benefit.", "Daily is the number that matters.", "Either.") | 2026-09-17, Hero FinCorp refresh drafts | 0 detector, 5 drafts | Self-observed in the adversarial pass, not yet highlighted by a detector. Appeared in all five drafts once the gates passed, which suggests the gates push writing toward it: short sentences satisfy the short-sentence floor and land at the top of paragraphs. Watch for it in highlights. |
| "X rather than Y" / "X, not Y" antithesis, about one sentence in eight | 2026-09-17, Hero FinCorp refresh drafts | 0 detector, 5 drafts | Self-observed. The negative-parallelism regex catches "not just X, it's Y" but not this plainer form. If a detector highlights it twice, add `\brather than\b` density to the hedging or negative_parallelism family with a per-1k cap rather than a ban. |
| Matched-pair paragraph closer ("Do that, and A. Ignore it, and B.") | 2026-09-17, Hero FinCorp refresh drafts | 0 detector, 3 drafts | Self-observed. Symmetrical two-sentence closers on conclusions and FAQ answers. Rewritten by hand; no regex proposed yet. |
| Uniform imperative procedure steps ("Start the application in the lender's app.", "Enter your Aadhaar, approve the OTP.") | 2026-09-18, Hero FinCorp e-KYC report | 1 detector sighting | Highlighted across a four-step numbered list while the surrounding prose stayed clean. Not gated yet. Promote if a second report highlights a numbered procedure. The working fix is to vary what each step opens on, and to let one step run long. |

## Threshold calibration history

| Date | Gate | Old | New | Report that forced it |
| --- | --- | --- | --- | --- |
| 2026-08-21 | all | n/a | initial values | Seeded from editorial prose baselines, not from a ZeroGPT report. Treat every number as provisional until the first three reports land. |
| 2026-08-21 | sentence opener repetition | `opener_repeat_max: 3` (raw count) | `opener_repeat_pct_max: 9.0` with `opener_repeat_floor: 3` | `reports/2026-08-21-sitejet-agency-delivery-sop.md`. A fixed raw cap cannot scale. On a 219-sentence article, "the" opened 16 sentences, which is 7.3% and entirely normal, and the gate failed a clean draft. Now proportional, with the raw floor kept so a 20-sentence piece is still checked. |
| 2026-09-17 | measurement, not a threshold: `strip_markdown()` | list markers (`- `, `1. `) left in the prose | list markers and HTML comments stripped before sentence splitting | Found while gating the Hero FinCorp refresh drafts, before any detector run. The sentence splitter needs a capital letter after the terminal period, and a bullet line starts with `-`, so every run of bullets was being measured as one sentence. Re-measured on the fix, the two Sitejet pieces each fall one sentence short of the long-sentence floor (11.4% and 11.6% against 12%). No threshold was moved; the earlier passes were partly an artefact and the pieces stay as delivered. |
| 2026-09-18 | four new gates added: `colon_header_bullets_max` 0, `colon_expansion_max_per_1k` 3.0, `semicolon_balance_max_per_1k` 4.0, `long_enumeration_max_per_1k` 1.5 | did not exist | as listed | The three Hero FinCorp reports of 2026-09-18. All eleven existing gates passed on drafts ZeroGPT then scored 41.6%, 37.9% and 23.1%. Under the protocol that means the gate set was too loose, so the shapes inside the highlight spans were measured and gated directly. Thresholds sit just below the best performer of the three, because even that one was above the 15% the client requires. |

## Piece history

| Date | Piece | Words | Pre-flight gates failed | ZeroGPT score | Notes |
| --- | --- | --- | --- | --- | --- |
| 2026-08-21 | Sitejet: agency delivery SOP | 1,072 (cut from 2,956) | 0 of 11 at final pass | pending client run |
| 2026-08-21 | Sitejet: website launch handover | 1,233 | 0 of 11 at final pass | pending client run | Second piece under v3.0. Failed three gates on first draft: paragraph variance, rule of three, and opener repetition. All three came from the same cause, a seven-item listicle structure that pushes every paragraph toward the same shape. Fixed without changing the structure. | First piece under v3.0. Forced one gate recalibration (sentence opener repetition). Client requires APA title case, which conflicts with pattern 17; resolved by excluding headings from the prose scan and compensating with a 22.7 per 1k contraction rate and 37% short sentences. Full report in `reports/2026-08-21-sitejet-agency-delivery-sop.md`. |
| 2026-09-17 | Hero FinCorp: upi-transaction-limit (refresh, 500 to 700 word brief) | 690 as counted / 525 prose | 0 of 11 at final pass | pending client run | Whole article gated as one run. Report in `reports/2026-09-17-herofincorp-upi-transaction-limit.md`. |
| 2026-09-17 | Hero FinCorp: working-capital-loan (refresh, 500 to 700 word brief) | 698 as counted / 592 prose | 0 of 11 at final pass | pending client run | Whole article gated as one run. Report in `reports/2026-09-17-herofincorp-working-capital-loan.md`. |
| 2026-09-17 | Hero FinCorp: what-is-ekyc (refresh, 500 to 700 word brief) | 698 as counted / 644 prose | 0 of 11 at final pass | pending client run | Whole article gated as one run. Report in `reports/2026-09-17-herofincorp-what-is-ekyc.md`. |
| 2026-09-17 | Hero FinCorp: suit-filed-cibil (refresh, 500 to 700 word brief) | 997 as counted / 730 prose | 0 of 11 at final pass | pending client run | Whole article gated as one run. Report in `reports/2026-09-17-herofincorp-suit-filed-cibil.md`. |
| 2026-09-17 | Hero FinCorp: msme-loan (refresh, 500 to 700 word brief) | 697 as counted / 545 prose | 0 of 11 at final pass | pending client run | Whole article gated as one run. Report in `reports/2026-09-17-herofincorp-msme-loan.md`. |
| 2026-09-17 | Hero FinCorp: reduce-loan-emi (refresh, 500 to 700 word brief) | 698 as counted / 579 prose | 0 of 11 at final pass | pending client run | Whole article gated as one run. Report in `reports/2026-09-17-herofincorp-reduce-loan-emi.md`. |
| 2026-09-17 | Hero FinCorp: personal-loan-default (refresh, 500 to 700 word brief) | 976 as counted / 834 prose | 0 of 11 at final pass | pending client run | Whole article gated as one run. Report in `reports/2026-09-17-herofincorp-personal-loan-default.md`. |
| 2026-09-18 | Hero FinCorp: msme-loan (rewrite) | 1000 words / 5645 chars | 0 of 15 at final pass | 41.6% before the rewrite, pending re-score | Rewritten 2026-09-18 after ZeroGPT scored the previous draft **41.6% AI**. Report in `reports/2026-09-18-herofincorp-msme-loan.md`. |
| 2026-09-18 | Hero FinCorp: what-is-ekyc (rewrite) | 999 words / 5682 chars | 0 of 15 at final pass | 37.9% before the rewrite, pending re-score | Rewritten 2026-09-18 after ZeroGPT scored the previous draft **37.9% AI**. Report in `reports/2026-09-18-herofincorp-what-is-ekyc.md`. |
| 2026-09-18 | Hero FinCorp: working-capital-loan (rewrite) | 1000 words / 5919 chars | 0 of 15 at final pass | 23.1% before the rewrite, pending re-score | Rewritten 2026-09-18 after ZeroGPT scored the previous draft **23.1% AI**. Report in `reports/2026-09-18-herofincorp-working-capital-loan.md`. |
| 2026-09-18 | Hero FinCorp: upi-transaction-limit (rewrite) | 1002 words / 5478 chars | 0 of 15 at final pass | pending client run | Not scored, but carried the same shapes as the three that were, so it was rewritten against the new gates on 2026-09-18 and grown past the client's 5,000-character floor. |
| 2026-09-18 | Hero FinCorp: suit-filed-cibil (rewrite) | 1028 words / 5863 chars | 0 of 15 at final pass | pending client run | Not scored, but carried the same shapes as the three that were, so it was rewritten against the new gates on 2026-09-18 and grown past the client's 5,000-character floor. |
| 2026-09-18 | Hero FinCorp: reduce-loan-emi (rewrite) | 987 words / 5511 chars | 0 of 15 at final pass | pending client run | Not scored, but carried the same shapes as the three that were, so it was rewritten against the new gates on 2026-09-18 and grown past the client's 5,000-character floor. |
| 2026-09-18 | Hero FinCorp: personal-loan-default (rewrite) | 1005 words / 5656 chars | 0 of 15 at final pass | pending client run | Not scored, but carried the same shapes as the three that were, so it was rewritten against the new gates on 2026-09-18 and grown past the client's 5,000-character floor. |

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

**Structure flags, vocabulary does not.** The first three drafts ever scored in
this skill came back 41.6%, 37.9% and 23.1% AI with an AI marker density of
0.0 per 1,000 words. Not one highlighted span contained a word from the
vocabulary list in `zerogpt-signals.md`. Every one of them was a sentence
shape: a colon-header bullet, a colon expansion, a semicolon welding two
balanced clauses, or a comma list of four or more items. When a draft passes
the vocabulary gates and still scores badly, stop looking at words and start
looking at punctuation.

**The colon is the most expensive character in this kind of copy.** A bullet
written as `- Label: expansion` was highlighted every single time it appeared,
while plain-sentence bullets in the same list came back clean. The same holds
in prose for a short declarative followed by a colon and an appositive. Both
gates exist now, the bullet one at zero tolerance.

**Eleven green gates are not a pass.** All three scored drafts cleared every
gate in v3.0.1. The script measures what it has been taught to measure and
nothing else, so a clean run means "no known tell", never "will score low".
Until a piece has been through a detector, the gates are a floor rather than
a verdict.

**A strict word cap turns every floor into a single sentence.** Seven pages
written to a 500 to 700 word brief (headings and tables counted) came out at
36 to 54 sentences each. At that size the short-sentence and long-sentence
floors are each four to six sentences, one merge or split flips a gate, and
the clustered-at-mean gate fails during trimming because cuts take the tails
off long sentences first. Run the script after every edit. Repair by merging
two mid-length sentences into one long one and adding a fragment elsewhere;
both cost nothing against the count. `tools/count-words.py` sits beside the
script so the length gate and the detector gates run together.

**Bullets were invisible to the sentence gates until 2026-09-17.** The splitter
only breaks after a period when the next character is a capital, a digit or a
quote. A bullet line starts with `-`, so a Key Takeaways box of five bullets
was one 60-word sentence to the script, which inflated the long-sentence share
and the CV on every listicle. `strip_markdown()` now removes list markers and
HTML comments first. Two consequences: end every bullet with a period, or
consecutive bullets still merge; and re-measure any piece gated before the fix
before quoting its numbers.

**Refresh briefs need two runs.** When the deliverable is an existing page with
new sections dropped in, gate the new copy on its own (that is what the writer
is answerable for) and the full page (that is what the client pastes into a
detector). `tools/extract-new-copy.py` pulls the marked sections out. The full
page usually fails on the client's existing copy, most often rule of three and
long-sentence share, and the cheapest repairs there are dropping Oxford commas
from plain lists and merging two medium sentences into one long one.

**The opener gate bites hardest on FAQ sections and numbered steps.** Answers
that start "The ..." and steps that start "You ..." or "For ..." cluster
fast in a 40-sentence block. Five pages in a row failed this gate on the first
pass and nothing else. Start FAQ answers with the subject of the question, a
number, or a conjunction, and vary the step openers on purpose.

**Gates that use raw counts do not survive contact with a long piece.** Any
threshold expressed as an absolute number needs checking against a 3,000-word
draft before it is trusted. The opener gate failed this test on the first real
article it saw. If you add a gate, express it per thousand words or as a
percentage of sentences.
