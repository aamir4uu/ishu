# WebPros Content Delivery

Blog content for two WebPros brands, written in second person against each
brand's own content guidelines. Every piece is worked line by line against the
client's AEO/SEO checklist and gated by the humanizer skill before delivery.

| Article | Client | Words | Gates | Folder |
| --- | --- | --- | --- | --- |
| The Delivery SOP That Lets a 3-Person Agency Run Like a 10-Person One | sitejet.io | 1,072 | 11/11 | `blog/delivery-sop/` |
| What to Send a Client on Launch Day so They Never Email You Again | sitejet.io | 1,233 | 11/11 | `blog/launch-day-handover/` |
| Stop Writing Content AI Tools Can't Understand | xovi.com | 1,154 | 11/11 | `blog/ai-content-optimisation/` |

Every folder has the same six files: the .docx deliverable, the markdown source
of record, a publishing pack with the checklist worked item by item, schema
JSON-LD, an image manifest, and the humanizer gate results.

The two Sitejet pieces cross-link: the handover article points back at the
delivery SOP as its stage five. Publish the SOP piece first, or fix that URL.

## Blog: The Delivery SOP That Lets a 3-Person Agency Run Like a 10-Person One

`blog/delivery-sop/`

| File | What it is |
| --- | --- |
| `The Delivery SOP...10-Person One.docx` | **Word deliverable.** Real Heading 1/2/3 styles, live hyperlinks, image slots with hyperlinked "Image Source" captions |
| `agency-delivery-sop.md` | Markdown source of record. H1/H2/H3, APA title case, three images each with a hyperlinked "Image Source" line beneath |
| `seo-publishing-pack.md` | Title tag, meta description, slug, internal links, and the AEO/SEO checklist worked item by item with open items called out |
| `schema-markup.json` | FAQPage, Article, HowTo and SoftwareApplication JSON-LD, generated from the live copy. Client reference only, per checklist section 4 |
| `image-manifest.md` | The six images, their alt text, source URLs, and what still needs doing before upload |
| `zerogpt-preflight-result.txt` | Detector gate results for the final draft |

**Written for the Sitejet Studio audience** (agencies, freelancers, web
professionals), second person, per the brand content guidelines. No SITEJET
Website Builder features are referenced and "Studio" never appears without the
Sitejet prefix.

**Length:** 1,072 words against a 800-1000 target with 25% headroom accepted.

### Open items before publishing

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

## Blog: What to Send a Client on Launch Day so They Never Email You Again

`blog/launch-day-handover/`

| File | What it is |
| --- | --- |
| `What to Send a Client on Launch Day so They Never Email You Again.docx` | **Word deliverable.** Heading 1/2/3 styles, live hyperlinks, image slots with hyperlinked "Image Source" captions |
| `website-launch-handover.md` | Markdown source of record |
| `seo-publishing-pack.md` | Metadata, checklist worked item by item, open items flagged |
| `schema-markup.json` | FAQPage, Article and a seven-step HowTo, generated from the live copy |
| `image-manifest.md` | Three images, alt text, source URLs, upload steps |
| `zerogpt-preflight-result.txt` | Detector gate results |

**Length:** 1,233 words against a 800-1000 target with 25% headroom accepted.

### Open items before publishing

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

## Blog: Stop Writing Content AI Tools Can't Understand

`blog/ai-content-optimisation/`

| File | What it is |
| --- | --- |
| `Stop Writing Content AI Tools Can't Understand.docx` | **Word deliverable.** Heading 1/2/3 styles, live hyperlinks, image slots with hyperlinked "Image Source" captions |
| `ai-content-optimisation.md` | Markdown source of record |
| `seo-publishing-pack.md` | Metadata, the checklist worked item by item, and the three inferred decisions called out |
| `schema-markup.json` | FAQPage, Article, a five-step HowTo, and a SoftwareApplication block for XOVI AI |
| `image-manifest.md` | Three images, alt text, source URLs, upload steps |
| `zerogpt-preflight-result.txt` | Detector gate results |

**Written for XOVI**, the all-in-one SEO platform, and specifically for
**XOVI AI**, its AI visibility module. Audience is agencies, freelancers and
in-house marketers. Voice per the XOVI guide: direct, short sentences, specifics
over adjectives, opinions where they are earned, and no guarantees about
rankings or AI mentions.

The approved XOVI AI positioning sentence appears verbatim, used as the anchor
text for the product link, and the Access → Understanding → Visibility →
Improvement → Monitoring framework is the spine of that section.

**Length:** 1,154 words including headings against a 800-1000 target. The
publishing pack explains what drove the overrun and what to cut if you need to
land inside the range.

### Open items before publishing

1. Confirm the primary keyword (`AI content optimisation`) and check its volume.
   Task Info was N/A, so it was inferred from the headline.
2. **Decide the spelling.** The brand guide writes "optimisation"; the article
   follows it. US "optimization" almost certainly has more volume, and
   xovi.com's own `/ai-search-optimization-xovi/` URL already uses the z. Pick
   one and make the site consistent.
3. Drop the three images in. Pexels was unreachable from this environment, so
   the .docx carries sized placeholder frames. See `image-manifest.md`.
4. Replace the byline with a named author and a personal LinkedIn URL. Checklist
   item 5.1, and it matters for the no-AI requirement too.
5. Spot-check both statistics. Pew and Ahrefs were both blocked here, so the
   figures were confirmed through search rather than from the source.
6. Confirm the three xovi.com URLs resolve. They came from search results,
   because xovi.com is also blocked from this environment.
7. After publishing, link older posts to this one and test the target query in
   ChatGPT, Perplexity and Gemini.

## Tooling

`tools/build-docx.js` converts any of these markdown articles to a formatted
Word file:

```
node tools/build-docx.js <source.md> <output.docx>
```

It maps H1/H2/H3 to real Word heading styles, keeps hyperlinks live, renders
bullets through a proper numbering config, and drops a sized placeholder frame
into each image slot with the alt text and the hyperlinked "Image Source"
caption beneath it.

The placeholder frames are generated at build time rather than read from disk,
and the `docx` package is resolved by searching the obvious locations instead of
one hardcoded path. Both were session-specific paths that broke as soon as the
script ran anywhere else.

Note: LibreOffice in this environment cannot open any .docx, including the
client's own brand guide file, so output is verified by parsing the packed XML
rather than by rendering.

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
| `scripts/zerogpt_preflight.py` | Measures eleven gates and names the riskiest sentences. Run before every detector paste |
| `reports/` | One filed report per ZeroGPT run. The evidence base behind every threshold |

Three reports are filed. None of them carries a real ZeroGPT score yet: this
environment's egress proxy blocks zerogpt.com, so the paste has to happen
client-side. Every report records the pre-flight gate table and the tells found
by hand, which is what the thresholds are actually calibrated from so far.

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

The XOVI piece added a third finding, from the other direction. It is the first
article under 1,100 words, and it failed the paragraph-variance gate on
structure rather than on prose: a short spec that also demands a takeaways box,
a PAA section and an FAQ leaves no room for a paragraph longer than four
sentences. The repair costs nothing, which is the useful part. Split two
existing paragraphs so a single sentence stands alone. It also produced three
new pattern candidates, all found by hand after the gates were already green.

### Usage

```
python3 .claude/skills/humanizer/scripts/zerogpt_preflight.py FILE.md --verbose
```
