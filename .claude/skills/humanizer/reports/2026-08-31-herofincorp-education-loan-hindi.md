# ZeroGPT Report: Hero FinCorp, education loan (Hindi)

- Date scored: 2026-08-31 14:15
- File scored: the full .docx text, pasted whole. **Not** the article alone. See "What was actually scored".
- Word count: 1,188 words / 6,321 characters as counted by ZeroGPT
- ZeroGPT result: **89.4% AI GPT**
- Detector version or URL: zerogpt.com, DeepAnalyse
- Pre-flight run before scoring: all 10 applicable gates passed
- Gates failing at time of scoring: none

This is the first report in the series that measures a failure, and the first
on non-English text. It is also the first time the pre-flight passed a draft the
detector then rejected outright, which is the condition the update protocol says
must tighten something.

## Highlighted sentences

**Not recoverable from this report.** ZeroGPT marks flagged sentences with a
background colour, and the PDF was exported through a browser print that had
background graphics turned off. Every rectangle in the file is white and every
character is black or a font-fallback grey. The per-sentence data, which the
protocol calls "the data", is simply not in the artefact.

| # | Highlighted sentence | Signal | Already in skill? |
| --- | --- | --- | --- |
| - | not recoverable, see above | - | - |

To recover it next time: in the browser print dialog tick "Background graphics"
before saving to PDF, or screenshot the result panel, or copy the highlighted
spans out by hand. Without it a report can only be read at the whole-document
level, which is what this one is.

## What was actually scored

ZeroGPT counted 1,188 words. The article body is 860. The difference is document
scaffolding that was pasted along with the copy and will never appear on the
published page:

- `[IMAGE 1 PLACEHOLDER - download from the Image Source link below, then replace this box]`, twice, verbatim
- `Alt text: ...`, twice
- `Image Source`, twice
- `**Meta Title:** ...` and `**Meta Description:** ...`

Three things are wrong with that, beyond it not being the article:

1. It is **English boilerplate sitting inside Hindi prose**.
2. The placeholder line **repeats verbatim**. Exact repetition is about the
   strongest low-perplexity signal there is.
3. The placeholder string contained an **em dash**, a marker the gates ban at
   zero tolerance. The pre-flight never saw it because `strip_markdown` removes
   image lines before scanning, so the tool that builds the deliverable was
   injecting a banned marker into the text a human would paste.

None of this explains 89.4% on its own. All of it had to go before the number
meant anything.

## Findings

**1. The gates were blind to the end of the sentence.** Opener repetition has
been gated since the first report. Hindi is verb-final, so its predictability
lives at the *other* end, and nothing was looking there. Measured after the
fact:

| Piece | Commonest sentence ending | Share |
| --- | --- | --- |
| CIBIL score (Hindi) | `है।` | 45.5% |
| Education loan (Hindi) | `है।` | 33.3% |
| What is collateral (English) | `it` | 3.0% |

Nearly half of one draft closing on the same token is the exact flat cadence the
opener gate exists to catch, one clause later. Both Hindi drafts passed every
gate while doing it.

**2. Passing ten of eleven gates is not the same as passing eleven.** The
contraction gate is N/A on Devanagari, and the marker families for Hindi were
translated predictions with no report behind them. The pre-flight reported "all
gates passed" on a draft that scored 89.4%. That phrasing oversells what was
actually measured on a Hindi draft, and the run output now says so.

**3. Unknown, and it matters more than anything above: whether ZeroGPT is
reliable on Hindi at all.** No control was run. The site claims support for all
languages; detectors are widely observed to over-flag non-English text. Until
known-human Hindi is scored on the same tool, it is not possible to say how much
of the 89.4% is the writing and how much is the detector. That control has been
specified for the client to run and is the single highest-value next step.

## Actions taken

- [x] Pattern added to `references/learning-log.md` candidates table
- [ ] Pattern promoted to `MARKERS` (not applicable, this is a gate not a marker)
- [x] Threshold changed in `GATES`: new `closer_repeat_pct_max` (12%) and
      `closer_repeat_pct_max_devanagari` (30%). Both **provisional**, forced by
      this report, with no human-written baseline behind them.
- [x] `references/zerogpt-signals.md` updated with signal 10, closer repetition
- [x] Piece history rows added to `references/learning-log.md`
- [x] Both Hindi drafts rewritten: commonest ending down from 45.5% and 33.3%
      to 6.1% each, by varying tense, mood and clause shape rather than swapping
      words
- [x] `tools/detector-paste.py` added, so what gets pasted is the published
      article and nothing else
- [x] Em dash removed from the placeholder string in `tools/build-docx.js`

## Still open

The rescore. Everything above is a hypothesis about why the number was 89.4%
until the revised text is put back through the same tool, together with the
human-Hindi control. Neither can be run from this environment.
