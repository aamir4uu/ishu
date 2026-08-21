---
name: humanizer
version: 4.0.0
description: |
  Remove signs of AI-generated writing and drive text past ZeroGPT-class
  detectors. Two layers: the Wikipedia "Signs of AI writing" catalogue for how
  text reads, and a ZeroGPT signal model for how text scores. Ships a
  measurement script that gates a draft on sentence burstiness, opener
  repetition, marker density, contraction rate, and punctuation tics before it
  is ever pasted into a detector. Learns mechanically: every filed ZeroGPT
  report is ingested by a calibration script that recalibrates signal weights
  against what the detector actually flagged, mines new rules from the
  sentences it missed, and reports its own recall so you can see whether the
  skill is improving.
license: MIT
compatibility: claude-code opencode
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# Humanizer

Two different problems wear the same name.

The first is that text *reads* like AI. A human editor sees "delve", "pivotal
moment", four bullets that all start with a gerund, and rejects it. The fix is
the Wikipedia pattern catalogue in `references/wikipedia-patterns.md`.

The second is that text *scores* as AI. ZeroGPT, GPTZero, and Copyleaks do not
read. They measure how predictable your word choices are and how much your
sentence lengths vary, then highlight the sentences that look machine-shaped.
A draft can be clean by every editorial standard and still come back 78% AI
because every sentence in it is nineteen words long. The fix is
`references/zerogpt-signals.md` and the script.

Do both. They are not the same job.

## Files

| File | What it is |
| --- | --- |
| `references/zerogpt-signals.md` | How ZeroGPT scores, the nine signals, and the repair order |
| `references/wikipedia-patterns.md` | The 29 editorial patterns, with before and after for each |
| `references/scan-signals.md` | What each signal name from `scan.py` means and how to fix it |
| `references/learning-log.md` | What the last reports taught, and the protocol for updating this skill |
| `scripts/zerogpt_preflight.py` | Pass/fail gates on rhythm and marker density. Run before every detector paste |
| `scripts/scan.py` | Weighted per-sentence risk ranking. Tells you *which* sentences to rewrite |
| `scripts/learn.py` | Ingests a filed report and evolves the model. This is what automates step 5 |
| `scripts/detectors.py` | The shared signal library both scripts read, so they can never drift apart |
| `memory/` | Signal weights, mined rules, flagged corpus, session log. Committed, so calibration survives the session |
| `reports/` | One filed report per ZeroGPT run. The evidence base for every threshold |
| `tests/run_tests.sh` | End-to-end pipeline test against a synthetic fixture |

The two scripts do different jobs and you want both. `zerogpt_preflight.py`
answers "is this draft shippable" with eleven pass/fail gates.
`scan.py` answers "which sentence do I fix first" with a ranked list. The gates
catch rhythm problems the ranking cannot see; the ranking catches sentence-level
problems the gates average away.

## Process

### 1. Establish the target voice

If the user supplied a writing sample or a brand guide, read it first and note
sentence length habits, contraction use, how paragraphs open, punctuation tics,
and any recurring phrases. Match those. If a client style guide mandates
something that trips a detector signal, the client wins and you compensate
elsewhere. Log the conflict in the known-conflicts table in
`references/zerogpt-signals.md`.

Without a sample, write with the voice described under Personality and Soul in
`references/wikipedia-patterns.md`: varied rhythm, real opinions, specific
detail, willing to admit uncertainty.

### 2. Editorial pass

Work `references/wikipedia-patterns.md` top to bottom. Significance inflation,
promotional language, hollow -ing analyses, vague attributions, copula
avoidance, negative parallelism, rule of three, elegant variation, false ranges,
filler, hedging, generic conclusions. Cut them.

### 3. Detector pass

Read the memory first. It is the accumulated result of every past report:

```
python3 scripts/learn.py --status      # version, score history, corpus size
cat memory/learned_rules.md            # what past reports taught it
```

Then run both scripts:

```
python3 scripts/zerogpt_preflight.py DRAFT.md --verbose
python3 scripts/scan.py DRAFT.md --top 15
```

It reports eleven gates and lists the highest-risk sentences in the draft. Work
the repair order from `references/zerogpt-signals.md`:

1. Clear every marker family the script names. Mechanical work, do it first.
2. Clear the punctuation gates. Em dashes to commas or periods. Curly quotes to
   straight.
3. Rewrite the sentences the script lists as riskiest.
4. Fix rhythm. Split long sentences into a long one plus a short one. Merge two
   mediums into one long. Add a fragment. This is what moves the CV gate, and
   the CV gate is the one that matters most.
5. Vary paragraph size. Some single sentences. One that runs long.
6. Check openers. No first word should start more than three sentences.
7. Rewrite the intro and the conclusion by hand, last. They flag hardest.

Re-run until every gate passes and `scan.py` reports no sentence-level hits.

`scan.py`'s weights are not fixed. They are whatever the last ingested report
calibrated them to, so its ranking reflects what ZeroGPT actually reacted to on
past pieces rather than a static blacklist.

### 4. Adversarial pass

The script cannot see meaning. Do this by hand, every time:

Ask yourself: "What makes the text below so obviously AI generated?" Answer in
three or four blunt bullets. Be harsh. Then revise against your own answer.

Then read the piece aloud, or as close as you can get. Anywhere you would not
say it that way, rewrite it.

### 5. Score and file

Paste into zerogpt.com. Copy the result and every highlighted sentence into a
new file under `reports/`, based on `reports/TEMPLATE.md`.

Then ingest it. This is no longer a manual protocol:

```
python3 scripts/learn.py reports/YYYY-MM-DD-slug.md --dry-run   # preview
python3 scripts/learn.py reports/YYYY-MM-DD-slug.md             # commit
```

`learn.py` reads both the template's highlighted-sentences table and a plain
`## flagged` list. On ingest it:

- Matches each reported span back to a draft sentence by token overlap, so
  ZeroGPT's segmentation does not have to match ours.
- Computes each signal's **lift**, meaning how much more often it appears in
  flagged sentences than in accepted ones, and moves that signal's weight
  toward the lift at a learning rate of 0.35, clamped to 1-30. One odd report
  cannot wreck the model.
- Promotes n-grams that keep appearing in flagged text and essentially never in
  accepted text into `memory/learned_rules.json`, with provenance and hit
  counts. Overlapping n-grams collapse to the longest form.
- Appends every flagged and accepted sentence to the corpus in `memory/*.jsonl`,
  which is the evidence base for future promotions.
- Prints `scan.py`'s **recall** against the report. That number is the honest
  measure of whether the skill is learning. It should climb across sessions.
- Bumps the version and writes a session entry to `memory/zerogpt-log.md`.

Two guards run automatically. Nothing is promoted until the flagged corpus holds
at least 8 spans, and anything in `memory/never_promote.txt` is skipped, which
is where the client's topic and brand vocabulary belongs. Seed it before the
first report. If a bad rule slips through:

```
python3 scripts/learn.py --unlearn "the phrase"
```

Then still do the judgement work the script cannot:

- A gate in `zerogpt_preflight.py` that passed on text ZeroGPT flagged is too
  loose. Tighten it, record old and new in the calibration table.
- A gate that failed on text ZeroGPT scored clean may be too tight. Do not
  loosen on one sample. Wait for three.
- Add a piece-history row to `references/learning-log.md`.

**Commit `memory/` afterwards.** Memory that is not committed does not survive
the session, and a skill that forgets is a static checklist again.

Skipping step 5 is what stops the skill improving. The reports are the only
thing separating this from a blacklist.

## Tests

```
bash tests/run_tests.sh
```

Runs the whole pipeline against a synthetic slop fixture in a throwaway copy of
`memory/`, so real calibration is never touched. Asserts that the fixture scores
as at-risk, that ingesting its report moves weights and mines rules, that the
topic-term guard holds, that the same text scores higher afterwards, and that
both report formats parse. Run it after any change to `detectors.py`.

## Output

1. Draft rewrite
2. "What makes the below so obviously AI generated?" with the remaining tells
3. Final rewrite
4. The pre-flight gate table for the final version
5. A short list of what changed and why

## The thing people get wrong

Detector-safe writing is not a filter you apply at the end. Low perplexity comes
from safe, general, unsurprising claims, so the draft that says "agencies should
document their processes to improve efficiency" is unfixable by editing. It has
to say something a model would not have predicted, which usually means a real
number, a named tool, a specific failure, or an actual opinion. Specificity is
the fix for the detector and for the reader at the same time.

## Reference

Editorial layer based on [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing),
maintained by WikiProject AI Cleanup. Detector layer built from ZeroGPT report
observations filed in `reports/`.
