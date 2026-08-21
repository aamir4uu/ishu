# Sitejet Content Delivery

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

### Usage

```
python3 .claude/skills/humanizer/scripts/zerogpt_preflight.py FILE.md --verbose
```
