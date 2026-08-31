# Content Delivery

Blog content written to client brief, worked against the client's own SEO and
compliance checklist and gated by the humanizer skill before delivery.

Two clients live here.

## Hero FinCorp

Three blogs, written from per-section content briefs against the Hero FinCorp
master guidelines. Audience is the "Young Climber" ICP, second person, UK
English, with the UTM-tagged personal loan CTA in every piece.

| Article | Language | Words | Gates | ZeroGPT | Folder |
| --- | --- | --- | --- | --- | --- |
| What Is Collateral? Meaning, Types and How It Works | English | 961 | 11/11 | not yet scored | `blog/what-is-collateral/` |
| CIBIL Score क्या होता है? इसे कैसे Check करें | Hindi | 933 | 10/10 applicable | not yet scored | `blog/cibil-score-kya-hota-hai/` |
| एजुकेशन लोन कैसे मिलता है? | Hindi | 856 | 10/10 applicable | 89.4% on the pre-revision draft, rescore pending | `blog/education-loan-kaise-milta-hai/` |

Each folder carries the same eight files:

| File | What it is |
| --- | --- |
| `<Title>.docx` | **Word deliverable.** Real Heading 1/2/3 styles, live hyperlinks, real Word tables, image slots with hyperlinked "Image Source" captions. Devanagari drafts are set in Nirmala UI |
| `<slug>.md` | Markdown source of record, with the meta title and description at the top as the client's sample has them |
| `seo-publishing-pack.md` | Metadata, per-section word count against the brief, the master guidelines checklist, the compliance checklist, sources, and open items |
| `schema-markup.json` | FAQPage, Article and HowTo JSON-LD, generated from the live copy |
| `image-manifest.md` | The two images, alt text, source URLs, and what still needs doing before upload |
| `detector-paste.txt` | **Paste this into ZeroGPT**, not the .docx. The published article with no meta fields, image placeholders or credit lines |
| `schema-config.json` | The Article and HowTo metadata `tools/build-schema.py` needs; FAQ content comes from the article itself |
| `zerogpt-preflight-result.txt` | Detector gate results for the final draft |

### The ZeroGPT result, 31 August

The education loan piece was scored and came back **89.4% AI**, against a brief
that asks for under 15%. Full report in
`.claude/skills/humanizer/reports/2026-08-31-herofincorp-education-loan-hindi.md`.

Three things came out of it.

**The whole .docx was pasted, not the article.** ZeroGPT counted 1,188 words
against an 860-word article. The rest was scaffolding that never reaches a
published page: meta fields, image placeholder frames, alt-text lines, credit
captions. One English boilerplate sentence appeared verbatim twice inside Hindi
prose, and it carried an em dash, a marker the gates ban outright. Each folder
now has a `detector-paste.txt` holding the published article and nothing else.

**The gates were blind to the end of the sentence.** Opener repetition has been
gated since the first article. Hindi is verb-final, so its predictable part sits
at the other end, and nothing was looking there. The two Hindi drafts were
closing 45.5% and 33.3% of their sentences on `है।`; the English draft's
commonest ending was 3.0%. Both have been rewritten to 6.1% by varying tense,
mood and clause shape. A closer-repetition gate now exists.

**What is still unknown is the important part.** Nobody has yet scored
known-human Hindi on this tool, so there is no way to tell how much of 89.4% is
the writing and how much is the detector's handling of Hindi. Before any further
rewriting, paste an already-published Hero FinCorp Hindi post into ZeroGPT as a
control. If the client's own live Hindi scores 80%+, the under-15% criterion is
not achievable in Hindi and that is a conversation, not an editing problem.

The English piece has not been scored yet.

### Read these three things before publishing

1. **Word count.** Task Info says 500-700 words. The master guidelines say
   roughly 700. The per-section counts inside each brief add up to 790-1,050.
   The per-section brief was followed as the more specific instruction, so all
   three run past the Task Info figure. Each publishing pack says exactly how to
   cut back to 700 if that is the number that matters.
2. **A closing CTA section was added to each piece.** None of the three briefs
   has a slot after the FAQ block, and the master guidelines require a
   conclusion with a UTM-tagged CTA. Delete it and move the link if you prefer.
3. **The education loan piece needs a compliance read.** Hero FinCorp sells an
   unsecured personal loan for education, not a classic education loan with a
   moratorium. The article explains education loans generally and names the Hero
   FinCorp product accurately in the final FAQ. The reasoning is written out in
   `blog/education-loan-kaise-milta-hai/seo-publishing-pack.md`.

Open items common to all three: confirm keyword volumes, re-host the images,
add a named author byline, verify the RBI and government sources, and run
ZeroGPT for the report the brief asks for. The pre-flight gates are not a
detector score.

## Sitejet

Blog content for sitejet.io, written for the **Sitejet Studio** audience
(agencies, freelancers, web professionals) in second person, per the brand
content guidelines.

| Article | Words | Gates | Folder |
| --- | --- | --- | --- |
| The Delivery SOP That Lets a 3-Person Agency Run Like a 10-Person One | 953 | 10/11 | `blog/delivery-sop/` |
| What to Send a Client on Launch Day so They Never Email You Again | 1,086 | 10/11 | `blog/launch-day-handover/` |

Both pieces were re-measured on 2026-08-29 after a correction to
`strip_markdown` in the pre-flight script: a markdown list used to collapse into
a single pseudo-sentence, which was carrying the long-sentence gate on any
bullet-heavy draft. Both now read marginally short on that one gate, 11.4% and
11.6% against a 12% floor. The copy has not been changed. Merging one sentence
pair in each would clear it if either piece is ever revised.

The two pieces cross-link: the handover article points back at the delivery SOP
as its stage five. Publish the SOP piece first, or fix that URL.

### The Delivery SOP That Lets a 3-Person Agency Run Like a 10-Person One

`blog/delivery-sop/`

| File | What it is |
| --- | --- |
| `The Delivery SOP...10-Person One.docx` | **Word deliverable.** Real Heading 1/2/3 styles, live hyperlinks, image slots with hyperlinked "Image Source" captions |
| `agency-delivery-sop.md` | Markdown source of record. H1/H2/H3, APA title case, three images each with a hyperlinked "Image Source" line beneath |
| `seo-publishing-pack.md` | Title tag, meta description, slug, internal links, and the AEO/SEO checklist worked item by item with open items called out |
| `schema-markup.json` | FAQPage, Article, HowTo and SoftwareApplication JSON-LD, generated from the live copy. Client reference only, per checklist section 4 |
| `image-manifest.md` | The six images, their alt text, source URLs, and what still needs doing before upload |
| `detector-paste.txt` | **Paste this into ZeroGPT**, not the .docx. The published article with no meta fields, image placeholders or credit lines |
| `schema-config.json` | The Article and HowTo metadata `tools/build-schema.py` needs; FAQ content comes from the article itself |
| `zerogpt-preflight-result.txt` | Detector gate results for the final draft |

**Written for the Sitejet Studio audience** (agencies, freelancers, web
professionals), second person, per the brand content guidelines. No SITEJET
Website Builder features are referenced and "Studio" never appears without the
Sitejet prefix.

**Length:** 1,072 words against a 800-1000 target with 25% headroom accepted. Re-measured at 953 body words after the strip_markdown correction.

#### Open items before publishing

1. Confirm the primary keyword and check its volume. Task Info was confirmed
   N/A, so `agency delivery SOP` was inferred from the headline.
2. Drop the three images in. Outbound access to Pexels was blocked in this
   environment, so the .docx carries sized placeholder frames with the source
   link and alt text beside each, and the markdown `![]()` tags point at the
   photo pages. See `image-manifest.md`.
3. Replace the team byline with a named author and a personal LinkedIn URL.
   Checklist item 5.1 asks for a person, and a named human author matters for
   the no-AI requirement too.
4. Spot-check the PMI statistic against the linked PDF. Confirmed through search
   but pmi.org could not be opened from here.
5. After publishing, update older posts to link to this one, and test the target
   query in ChatGPT, Perplexity and Gemini.

### What to Send a Client on Launch Day so They Never Email You Again

`blog/launch-day-handover/`

| File | What it is |
| --- | --- |
| `What to Send a Client on Launch Day so They Never Email You Again.docx` | **Word deliverable.** Heading 1/2/3 styles, live hyperlinks, image slots with hyperlinked "Image Source" captions |
| `website-launch-handover.md` | Markdown source of record |
| `seo-publishing-pack.md` | Metadata, checklist worked item by item, open items flagged |
| `schema-markup.json` | FAQPage, Article and a seven-step HowTo, generated from the live copy |
| `image-manifest.md` | Three images, alt text, source URLs, upload steps |
| `zerogpt-preflight-result.txt` | Detector gate results |

**Length:** 1,233 words against a 800-1000 target with 25% headroom accepted. Re-measured at 1,086 body words after the strip_markdown correction.

#### Open items before publishing

1. Confirm the primary keyword (`website launch handover`) and check its volume.
   Task Info is N/A, so it was inferred from the headline.
2. Drop the three images in. See `image-manifest.md`. Image 3 is shared with the
   delivery SOP shortlist, so swap it if both pieces publish together.
3. Replace the team byline with a named author and a personal LinkedIn URL.
4. Spot-check the Ignition figures against the linked report.
5. Fix the internal link to the delivery SOP article once that piece has a real
   URL, and add a link back from that article to this one.
6. **Title capitalisation:** APA lowercases "so" as a short conjunction, so the
   headline reads "...Launch Day so They Never Email You Again". That is
   correct, not a typo. Capitalise it if the client prefers the look.

## Tooling

Three tools, all driven off the markdown source of record.

`tools/build-docx.js` converts any of these markdown articles to a formatted
Word file:

```
DOCX_MODULES=/path/to/node_modules node tools/build-docx.js <source.md> <output.docx> ["Creator Name"]
```

It maps H1/H2/H3 to real Word heading styles, keeps hyperlinks live, renders
bullets through a proper numbering config, converts markdown tables to real
Word tables with a shaded header row, and drops a sized placeholder frame into
each image slot with the alt text and the hyperlinked "Image Source" caption
beneath it. A draft containing Devanagari is set in Nirmala UI, which covers
both scripts; everything else stays in Calibri.

`docx` is not vendored here. Install it anywhere and point `DOCX_MODULES` at
that `node_modules`, or install it next to the script. The placeholder frame is
generated in-process, so there is no asset directory to carry around.

Note: LibreOffice in this environment cannot open any .docx, including the
client's own brand guide file, so output is verified by parsing the packed XML
rather than by rendering.

`tools/detector-paste.py` emits the text to paste into a detector: the published
article with the meta fields, image placeholders and credit captions stripped
out. Run it after every edit.

```
python3 tools/detector-paste.py blog/<slug>/<slug>.md
```

`tools/build-schema.py` regenerates an article's JSON-LD. The FAQ block is read
out of the article's own FAQ section rather than maintained by hand, so an
edited answer cannot drift out of sync with the schema. Everything not
derivable from the prose lives in `schema-config.json` beside the article.

```
python3 tools/build-schema.py blog/<slug>/
```

## Skill: humanizer v3.0.0

`.claude/skills/humanizer/`

Upgraded from v2.5.1. The old version covered how text *reads*. This version
adds a layer for how text *scores* in ZeroGPT and the other perplexity and
burstiness detectors, and a protocol that makes the skill improve every time a
piece gets scored.

| File | What it is |
| --- | --- |
| `SKILL.md` | The five-step process: voice, editorial pass, detector pass, adversarial pass, score and file |
| `references/zerogpt-signals.md` | How ZeroGPT scores, the nine signals it keys on, the repair order, and a table of client requirements that fight the detector |
| `references/wikipedia-patterns.md` | The 29 editorial patterns from v2.5.1, preserved in full |
| `references/learning-log.md` | Threshold calibration history, pattern candidates, and the protocol for updating the skill from a report |
| `scripts/zerogpt_preflight.py` | Measures eleven gates and names the riskiest sentences. Run before every detector paste. Handles Devanagari and Hinglish |
| `reports/` | One filed report per ZeroGPT run. The evidence base behind every threshold |

### How it evolves

A report goes in `reports/` using `TEMPLATE.md`. Every highlighted sentence gets
mapped to a known signal or marked NEW. New patterns land in the candidates
table; two independent sightings promotes one into the `MARKERS` dict in the
script so it is caught automatically from then on. A gate that passed on text
ZeroGPT then flagged is too loose and gets tightened, with the old and new
values recorded. Nothing changes without a report behind it.

The first article already forced one recalibration: the sentence-opener gate
used a raw count of 3, which failed a clean 219-sentence draft where "the"
opened 16 sentences (7.3%, normal for English). It is now proportional with a
raw floor. Cutting that draft to 1,072 words then produced a second finding,
that large cuts break the variance gates because trimming attacks long sentences
first. Both are recorded in the learning log.

### What changed on 2026-08-29

The Hero FinCorp set is the first Hindi work through the skill, and it forced
three changes.

**Devanagari support.** The tokeniser and sentence splitter now know the
Devanagari block and the danda, three Hindi marker families were added, and the
Hindi "X, Y और Z" shape is caught. The script reports the Devanagari word share
at the top of every run. The contraction gate is reported N/A above a 50% share,
because apostrophe contractions do not exist in Hindi, so a Hindi draft is gated
on ten of the eleven measures.

**A measurement bug, and it mattered.** A markdown list has no sentence
terminators, so the splitter was swallowing an entire bullet block into one
"sentence" of 40 or 80 words. On any bullet-heavy draft that single fake
sentence was quietly carrying the long-sentence gate. List items now terminate
individually. Image credit lines and meta title/description lines are stripped
for the same reason: they are not prose. Both Sitejet articles were passing that
gate on the artefact and now read marginally short.

**A new client conflict.** A brief that fixes a word count per H2 section fights
the long-sentence gate, because trimming to a cap attacks long sentences first.
The fix that works inside a cap is merging two mediums into one long, which is
word-neutral, removes a sentence and adds a long one. Logged in the
known-conflicts table.

### Usage

```
python3 .claude/skills/humanizer/scripts/zerogpt_preflight.py FILE.md --verbose
```
