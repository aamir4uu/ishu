---
name: humanizer-evolve
version: 1.0.0
description: |
  Self-improving humanizer. Removes signs of AI-generated writing, then learns
  from real ZeroGPT reports so it catches more on the next pass. Every ingested
  report recalibrates the scanner's signal weights and mines new rules from the
  sentences the detector actually flagged, which are stored in memory/ and
  carried into every future session. Use when drafting or editing prose that
  has to pass an AI detector, and after any ZeroGPT run.
license: MIT
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
---

# Humanizer (evolving)

A static blacklist stops working the moment a detector changes or a writer
learns to dodge it. This skill keeps a memory instead. It scores a draft, you
run the draft through ZeroGPT, you feed the report back, and the scoring model
moves toward what the detector actually reacted to.

The base pattern catalogue is the same one the plain `humanizer` skill uses
(Wikipedia's "Signs of AI writing"). What is added here is the loop around it.

## The loop

```
  draft ──▶ scan.py ──▶ rewrite worst sentences ──▶ scan.py ──▶ submit to ZeroGPT
                ▲                                                      │
                │                                                      ▼
          memory/state.json ◀── learn.py ◀────────────── ZeroGPT report
          memory/learned_rules.json
          memory/flagged.jsonl
```

## Start of every session

Read the memory before touching the draft. It is the whole point of the skill.

```bash
cd .claude/skills/humanizer-evolve/scripts
python3 learn.py --status          # version, score history, corpus size
cat ../memory/learned_rules.md     # what past reports taught it
```

If `memory/zerogpt-log.md` exists, skim the last two or three sessions. The
"missed by the scanner" lists are the highest-value part: those are the
sentence shapes that slipped past the model last time.

## Scanning a draft

```bash
python3 scan.py ../../../../content/post/post.md
python3 scan.py path/to/draft.md --json --top 25
```

The score is 0-100, lower is better. It blends two things:

- **Sentence load** - the average per-line risk from lexical and syntactic
  signals (AI vocabulary, participial tails, negative parallelism, copula
  dodging, rule of three, learned rules).
- **Document rhythm** - burstiness, mid-band sentence clustering, uniform
  paragraph lengths, repeated sentence openers, contraction rate.

The second half matters more than most writers expect. Perplexity-based
detectors respond to rhythm, so a draft can be completely blacklist-clean and
still read as machine-written because every sentence is 19 words long. If
`low_burstiness` or `mid_band_clustering` is firing, no amount of word swapping
will fix the score: you have to change sentence lengths.

Target before submitting: **under 20**, with no document-level rhythm signal
firing.

## Rewriting

Work the ranked list top down. For each flagged sentence, fix the named signal
rather than paraphrasing at random. The catalogue of patterns and their
rewrites lives in `reference/patterns.md`.

Two rules that override everything else:

1. **Preserve meaning and facts.** Never invent a statistic, a source, a date,
   or a quotation to make a sentence sound more human.
2. **Honour the client's style rules even when they conflict with the
   catalogue.** Recorded exceptions are in `memory/exceptions.md`. For example
   the SocialBee brief mandates APA title case in headings, which the generic
   catalogue treats as an AI tell. The client's brief wins; log the exception
   rather than silently overriding either one.

After rewriting, re-scan. If the score has not moved, you paraphrased instead
of restructuring.

## Feeding a ZeroGPT report back

This is the step that makes the skill improve. Write the report to a file:

```
draft: content/facebook-reel-length/facebook-reel-length.md
score: 18
date: 2026-08-21
note: second pass, after rhythm fixes

## flagged
Paste each sentence ZeroGPT highlighted, one per line.
Paste them exactly as shown so they can be matched to the draft.
```

Then:

```bash
python3 learn.py ../reports/2026-08-21-pass2.md --dry-run   # preview
python3 learn.py ../reports/2026-08-21-pass2.md             # commit
```

What happens on ingest:

- Reported spans are matched to draft sentences by token overlap, so ZeroGPT's
  segmentation does not have to match ours.
- Each signal's **lift** is computed: how much more often it appears in flagged
  sentences than in accepted ones. Weights move toward that lift at a learning
  rate of 0.35 and are clamped to 1-30, so one odd report cannot wreck the
  model.
- N-grams that appear in at least two flagged sentences and essentially never
  in accepted ones are **promoted into `learned_rules.json`** with provenance
  and hit counts.
- The flagged and accepted sentences are appended to the corpus in
  `memory/*.jsonl`, which is the evidence base for future promotions.
- `scan.py` recall against the report is printed. That number is the honest
  measure of whether the skill is actually learning: it should climb across
  sessions.
- The skill version bumps and `memory/zerogpt-log.md` gains a session entry.

Commit the `memory/` changes. Memory that is not committed does not survive
the session, and a skill that forgets is just a blacklist again.

## Correcting a bad rule

The miner is statistical, so it will occasionally promote a phrase that merely
happened to sit inside flagged sentences. Topic vocabulary is the usual
offender: an article about Facebook Reels says "Facebook Reels" in most of its
sentences, flagged or not.

```bash
python3 learn.py --unlearn "facebook reels"
```

That drops the rule and adds the term to `memory/never_promote.txt` so it is
never mined again. Seed that file with the client's topic and brand vocabulary
before the first report rather than cleaning up afterwards.

Two guards run automatically:

- Nothing is promoted until the flagged corpus holds at least 8 spans, so a
  single thin report cannot fill the rule set with topic nouns.
- Overlapping n-grams are collapsed to the longest form of each equal-count
  family, so one phrase produces one rule instead of nine fragments.

## Tests

```bash
bash tests/run_tests.sh
```

Runs the whole pipeline against a synthetic slop fixture in a throwaway copy of
`memory/`, so the real calibration is never touched. It asserts that the
fixture scores as at-risk, that ingesting its report moves weights and mines
rules, that the topic-term guard holds, and that the same text scores higher
afterwards than it did before. Run it after any change to `detectors.py`.

## Honest limits

- The scanner does not run a language model, so it cannot measure true
  perplexity. It approximates the detector with countable proxies and
  calibrates them against real reports. It will never be a perfect oracle,
  which is why the ZeroGPT step stays in the loop.
- ZeroGPT is not fetched automatically here; the environment has no API key
  and outbound access is restricted. Reports are pasted in. If a key is
  available later, `learn.py` accepts the same report format from any source,
  so only the fetching step needs adding.
- Detector scores are noisy. Treat a single report as one observation, not as
  proof. The weights are deliberately slow-moving for that reason.

## Output format when humanizing

1. The rewritten draft.
2. The scan score before and after.
3. "What still reads as AI here?" - a short honest list of remaining tells.
4. The final revision after acting on that list.
5. Anything worth recording in memory once a real report comes back.
