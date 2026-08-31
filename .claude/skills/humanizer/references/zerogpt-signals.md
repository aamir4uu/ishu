# What ZeroGPT Actually Flags

Reference layer for the humanizer skill. Everything here is about one detector
family: ZeroGPT and the other perplexity/burstiness scorers that behave like it
(GPTZero, Copyleaks, Originality.ai in "AI" mode). The Wikipedia pattern
catalogue in SKILL.md is about *reading* like AI. This file is about *scoring*
as AI. They overlap, but not completely, and the gap is where most rejected
drafts live.

## The scoring model

ZeroGPT markets its engine as DeepAnalyse. Whatever the internals, the output
behaves like a classifier over two statistical properties plus a marker bag:

**Perplexity.** How surprised a language model is by your next word. Text that
picks the highest-probability continuation at every step scores low perplexity
and reads as machine-written. This is why polished, safe, unsurprising prose
gets flagged harder than sloppy prose with an odd word choice in it.

**Burstiness.** How much sentence length and structure vary across the piece.
Humans write a 6-word sentence, then a 31-word one, then two mediums. Models
regress toward a comfortable 17 to 22 words and stay there. Uniformity is the
single most reliable tell, and it is the one you can measure without a model.

**Marker bag.** Surface features that correlate with model output: connective
scaffolding, a specific vocabulary, punctuation habits, structural tics.

## The reporting behaviour that matters

ZeroGPT returns a percentage and highlights *individual sentences*. It does not
average your good writing against your bad writing evenly. A run of three
uniform, marker-dense sentences will get highlighted and drag the score even
inside an otherwise varied piece.

Two consequences for how you edit:

1. **Fix sentences, not paragraphs.** The unit of detection is the sentence, so
   the unit of repair is the sentence.
2. **Watch the openers and the closers.** Intros and conclusions are the most
   formulaic parts of any generated draft, and they are where the highlighting
   almost always starts. Rewrite them last, hardest, and by hand.

## Signal 1: length uniformity

The failure looks like this, and it is invisible until you count:

    18, 21, 19, 22, 20, 17, 23, 19  -> CV 0.09, flagged
    6, 31, 14, 9, 27, 4, 22, 16     -> CV 0.55, clean

Targets enforced by `scripts/zerogpt_preflight.py`:

- coefficient of variation on sentence length at or above 0.45
- no more than 40% of sentences sitting within four words of the mean
- at least 12% of sentences under nine words
- at least 12% of sentences over twenty-four words

Sentence fragments count and help. So does a one-word sentence, used once.

## Signal 2: paragraph uniformity

The same problem one level up. Generated drafts produce paragraph after
paragraph of three or four sentences. Break the pattern with single-sentence
paragraphs and with one paragraph that runs long enough to feel like someone
got going and did not stop.

## Signal 3: opener repetition

Count the first word of every sentence. When "This", "The", "It", or "You"
opens more than three sentences in a piece, a detector picks up the rhythm even
if a reader would not. Start sentences with a subordinate clause, a number, a
quoted phrase, a conjunction, a prepositional phrase.

## Signal 3b: closer repetition

The mirror of signal 3, and the one that got missed for three articles. Count
the *last* word of every sentence, not just the first.

Which end matters depends on the language. English front-loads the subject, so
repetition shows up at the opener. Hindi is verb-final and its present copula is
`है`, so a Hindi draft can vary its openers beautifully and still close half its
sentences on the same two characters. Measured on real drafts:

    Hindi, before revision:   है। x30 of 66 sentences = 45.5%
    Hindi, after revision:    हैं। x4 of 66 = 6.1%
    English, same author:     it x2 of 66 = 3.0%

Ceilings enforced by the script: 12% normally, 30% on a Devanagari-majority
draft, where the copula is structurally common enough that an English-style
ceiling is not reachable. Both numbers are provisional, set from one report with
no human-written baseline behind them.

The fix is not synonym-swapping. Vary the grammar: switch tense, drop into an
imperative, end on a noun instead of a verb, let one sentence be verbless. In
Hindi, `होता है` to `होता`, `जाता है` to `जाएगा`, `करती है` to `करेगी`, and a
plain nominal close where the copula is doing no work.

## Signal 4: connective scaffolding

The highest-value single fix. Models glue clauses together with explicit
logical connectors because that is what maximises coherence scores:

    Moreover, Furthermore, Additionally, Consequently, As a result,
    In conclusion, Ultimately, That said, It is important to note that,
    When it comes to, In today's, In the world of, First and foremost

Humans imply the relationship and move on. Cut the connector and let the two
sentences sit next to each other. Where you genuinely need one, use the plain
version: "so", "but", "and then", "which is why".

## Signal 5: contraction absence

Formal registers suppress contractions, and models over-suppress them. A piece
of business prose with zero contractions across 1,500 words reads as generated
even when nothing else is wrong. Four or more per thousand words is a
reasonable floor for anything short of legal drafting.

## Signal 6: the vocabulary

Beyond the Wikipedia list, these are the words that show up inside ZeroGPT
highlight spans most often in practice:

    leverage, streamline, seamless, robust, foster, harness, empower,
    unlock, navigate, crucial, pivotal, vital, holistic, myriad, realm,
    paradigm, synergy, delve, intricate, tapestry, cutting-edge,
    game-changer, ever-evolving

Two of these in a paragraph is usually enough to get it highlighted.

## Signal 7: structural tics

- **Rule of three.** "X, Y, and Z" as a habit rather than because there are
  exactly three things. Cut to two or expand to four.
- **Colon-header bullets.** `**Speed:** the system is faster` is a generated
  list shape. Write the bullet as a sentence.
- **Em dashes.** Straight replacement with commas, periods, or parentheses.
- **Curly quotes and ellipsis characters.** Straight quotes, three periods.
- **Perfectly parallel bullets.** When every bullet starts with a verb in the
  same tense and runs the same length, vary two of them.
- **Symmetrical negation.** "It's not just X, it's Y" and its cousins.

## Signal 8: specificity starvation

Low perplexity comes from safe, general claims. Every concrete detail you add
raises perplexity because a model would not have predicted it: a real number, a
named tool, a date, a dollar figure, a thing that went wrong on a Tuesday.
Generic competence is what gets flagged. This is also why the checklist item
about citable data points and the AI-detection problem have the same fix.

## Signal 9: emotional flatness

Models produce balanced, non-committal prose. An opinion, an admission, a mild
complaint, or a sentence that takes a side raises perplexity and reads human.
You do not need much. One per section is plenty in professional copy.

## Known conflicts with client style guides

Some client requirements push *toward* detector signals. Follow the client and
compensate elsewhere. Log every conflict here.

| Client requirement | Detector signal it triggers | Compensation |
| --- | --- | --- |
| APA title case on all headings | SKILL.md pattern 17 treats title case as a tell | Headings are excluded from the prose scan. Buy the variance back in body copy: more short sentences, higher contraction rate. |
| "Key Takeaways" box with 4-5 bullets | Bullet parallelism, rule of three | Write bullets at deliberately different lengths. Never four bullets of identical shape. |
| FAQ section with 5-8 Q&A pairs | Highly templated block, uniform answer length | Vary answer length by 3x across the set. Let one answer be a single line and one run to a short paragraph. |
| Formal or serious tone | Contraction suppression | Keep contractions in the explanatory sentences even where the register is formal. Second person helps carry them. |
| Keyword in first 100 words and in an H2 | Repetitive keyword placement reads templated | Place the keyword inside a sentence doing real work, not in an announcement sentence. |
| A word count fixed per H2 section | Trimming to a cap attacks long sentences first and drops the long-sentence share | Merge two mediums into one long instead of deleting clauses. A merge is word-neutral, removes a sentence and adds a long one. |
| Hindi or Hinglish body copy | The contraction gate does not apply and is reported N/A, leaving register informality unmeasured | Ten gates instead of eleven. Compensate by hand: read for stiffness, and keep the short-sentence share well above its floor. |
| Meta title and description carried inside the draft | Two long, contraction-free pseudo-sentences skew the distribution | Stripped by `strip_markdown`. Keep them on their own lines with the `**Meta Title:**` label so the pattern matches. |

## Writing in a script other than English

The two statistical signals are script-independent. Burstiness, paragraph
variance and opener repetition mean the same thing in Devanagari as in Latin,
and `zerogpt_preflight.py` measures all three once its tokeniser and sentence
splitter know about the Devanagari block and the danda. The marker bag is not
script-independent, and neither is the contraction gate.

What carries over:

- Length variance, clustering, short and long sentence shares, paragraph
  variance, opener repetition. All measured normally.
- Specificity. A real date or a named circular raises perplexity in any
  language.
- Em dashes and curly quotes. Both appear in Hindi typesetting.

What does not:

- **Contractions.** No Devanagari equivalent. The gate reports N/A above a 50%
  Devanagari word share.
- **The English marker list.** Hindi has its own scaffolding, and three
  families are now in `MARKERS`. They are translated predictions rather than
  observed highlights, so do not trust a 0.0 marker density on a Hindi draft
  the way you would on an English one.
- **The rule-of-three regex.** The Hindi shape is "X, Y और Z" and needs its own
  pattern, which `RULE_OF_THREE_HI` supplies.

Mixed Hinglish is the normal case in Indian finance copy, and the script share
is reported at the top of every run so you can see which regime you are in.

## What the gates do not measure

Worth keeping in front of you, because a clean run is easy to over-read.

The gates measure proxies for perplexity. They do not measure perplexity, and
they cannot: that needs a language model. Every threshold is a bet that the
proxy tracks the thing. On English, four scored pieces support that bet. On
Hindi there is one data point and it is a draft that passed all ten applicable
gates and came back **89.4% AI**.

So: a clean pre-flight means nothing obvious is wrong. It does not mean the
piece will pass. On Hindi in particular, treat it as the floor and do the
adversarial pass properly.

Two practical rules follow.

**Paste the article, not the document.** Meta fields, image placeholders,
alt-text lines and credit captions are scaffolding a published page never shows.
Pasting them scores boilerplate that repeats verbatim and is often in a
different language from the body. `tools/detector-paste.py` emits the right
text.

**Insist on the highlights.** A ZeroGPT PDF printed with background graphics
off loses every highlight, and the highlights are the data. A bare percentage
tells you a piece failed; only the highlights tell you why.

## Repair order

Work top down. Each step is cheaper than the one below it and often removes the
need for it.

1. Run `scripts/zerogpt_preflight.py FILE --verbose`.
2. Fix every marker family hit. This is find-and-replace work.
3. Fix punctuation gates: em dashes, curly quotes.
4. Rewrite the riskiest sentences the script lists.
5. Re-split and re-merge sentences until the CV gate passes. Splitting a long
   sentence into a long one plus a short one raises variance twice.
6. Rewrite the intro and the conclusion by hand, last.
7. Re-run. Repeat until clean.
8. Score the result in ZeroGPT, save the report, update `learning-log.md`.
