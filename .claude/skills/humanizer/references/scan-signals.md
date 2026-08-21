# Pattern catalogue

Each entry names a signal emitted by `scripts/detectors.py`, what it means, and
how to fix it. When `scan.py` flags a sentence it names the signal, so look it
up here rather than paraphrasing blindly.

Base catalogue adapted from [Wikipedia: Signs of AI
writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

## Rhythm signals (document level)

### low_burstiness
Human sentence lengths scatter. Machine sentence lengths cluster. If the
standard deviation of your sentence lengths is under 8 words, the draft reads
as generated no matter how clean the vocabulary is.

Fix by breaking one long sentence into a 4-word one and a 30-word one. Add a
fragment. Let one sentence run long because the thought is genuinely long.

### mid_band_clustering
More than 55% of sentences landing in the 14-26 word band. Same cause, same
fix. Count the short sentences: you probably have none under 8 words.

### uniform_paragraphs
Every paragraph is the same number of sentences. Real writing has one-line
paragraphs next to five-line ones.

### repeated_openers
Three or more sentences starting with the same two words. Usually "This is",
"You can", "It's important". Vary the entry point, or merge the sentences.

### no_contractions
Under 0.18 contractions per sentence in a conversational register. Machines
write "it is" where people write "it's".

## Content signals

### ai_phrase / learned_phrase
A phrase from the base blacklist, or one promoted from a real ZeroGPT report.
Learned ones carry the session they came from. Cut and rewrite in plain
English. The test: could this phrase appear in an article on any topic? Then
it says nothing.

### ai_word / learned_word
Single words that spiked in text after 2023: delve, robust, leverage, pivotal,
seamless, comprehensive, foster, elevate. Use the ordinary word instead.

### participial_tail
A trailing `-ing` clause bolted on to fake depth: "..., highlighting its
importance", "..., ensuring consistency". Either delete it or promote it into
a real sentence with a subject.

### negative_parallelism
"Not just X, but Y" and "It isn't about X, it's about Y". Also clipped tail
negations: "no guessing", "no wasted motion". State the positive claim.

### copula_dodge
"serves as", "stands as", "represents a", "boasts". Use "is" or "has".

### rule_of_three
Forced triads: "faster, simpler, and more reliable". Cut to the one or two that
are actually true, or make the list four items long.

### false_range
"From X to Y" where X and Y are not on any scale. Name the things instead.

### transition_density
Stacked connectives: however, moreover, furthermore, additionally, ultimately.
Most can be deleted with no loss.

### hedging
"potentially", "arguably", "tends to", "in many cases". Either you know it or
you don't. Say which.

### em_dash
Machines reach for the em dash. Commas, periods and parentheses usually read
better. Not banned, but keep them rare.

### bold_header_item
`- **Thing:** explanation` repeated down a list. Rewrite as prose or as plain
bullets.

### chatbot_artifact
"I hope this helps", "Certainly!", "Let me know if". Conversation residue that
should never reach a published draft.

### challenges_trope
"Despite these challenges...", "faces several challenges", a "Challenges and
Future Prospects" heading. A formulaic section that says nothing specific.
Replace with the actual problem and what was done about it.

### generic_closer
"The future looks bright", "exciting times lie ahead", "continues to thrive",
"only time will tell". Vague upbeat endings. End on a concrete fact or a
specific next step instead.

### curly_quote / emoji
Smart quotes from a chat window; decorative emoji in headings.

### long_sentence
Over 34 words. Usually two ideas wearing one sentence. The brand brief for
SocialBee asks for one idea per sentence.

## Adding soul, not just removing tells

Clean prose with no point of view still reads as generated. After the signals
are gone, check that the draft:

- takes a position somewhere, rather than reporting neutrally throughout
- says something specific enough that it could not have been written about a
  different product
- varies its rhythm because the ideas vary, not because a scanner asked
- admits a limit or a tradeoff where one honestly exists
