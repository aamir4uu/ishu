---
name: humanizer
version: 3.0.0
description: |
  Remove signs of AI-generated writing and drive text past ZeroGPT-class
  detectors. Two layers: the Wikipedia "Signs of AI writing" catalogue for how
  text reads, and a ZeroGPT signal model for how text scores. Ships a
  measurement script that gates a draft on sentence burstiness, opener
  repetition, marker density, contraction rate, and punctuation tics before it
  is ever pasted into a detector. Learns: every ZeroGPT report gets filed and
  edits the thresholds and marker lists.
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
| `references/learning-log.md` | What the last reports taught, and the protocol for updating this skill |
| `scripts/zerogpt_preflight.py` | Measures the gates. Run it before every detector paste |
| `reports/` | One filed report per ZeroGPT run. The evidence base for every threshold |

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

Run the script:

```
python3 scripts/zerogpt_preflight.py DRAFT.md --verbose
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

Re-run until every gate passes.

### 4. Adversarial pass

The script cannot see meaning. Do this by hand, every time:

Ask yourself: "What makes the text below so obviously AI generated?" Answer in
three or four blunt bullets. Be harsh. Then revise against your own answer.

Then read the piece aloud, or as close as you can get. Anywhere you would not
say it that way, rewrite it.

### 5. Score and file

Paste into zerogpt.com. Copy the result and every highlighted sentence into a
new file under `reports/`, based on `reports/TEMPLATE.md`. Then work the update
protocol at the top of `references/learning-log.md`:

- Each highlighted sentence maps to a known signal, or it is new.
- New patterns go to the candidates table with the report that found them.
- Two independent sightings promotes a pattern into the `MARKERS` dict in
  `scripts/zerogpt_preflight.py`.
- A gate that passed on text ZeroGPT then flagged is too loose. Tighten it and
  record the change in the calibration table.
- A gate that failed on text ZeroGPT scored clean may be too tight. Do not
  loosen on one sample. Wait for three.

Skipping step 5 is what stops the skill improving. The reports are the only
thing separating this from a static checklist.

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
