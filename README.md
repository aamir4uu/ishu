# Blog Content Delivery

Client blog content, written in second person against each client's brand
guide. Every piece is worked through the AEO/SEO checklist and gated by the
humanizer skill before delivery.

| Client | Article | Words | Gates | Folder |
| --- | --- | --- | --- | --- |
| Sitejet | The Delivery SOP That Lets a 3-Person Agency Run Like a 10-Person One | 1,072 | 11/11 | `blog/delivery-sop/` |
| Sitejet | What to Send a Client on Launch Day so They Never Email You Again | 1,233 | 11/11 | `blog/launch-day-handover/` |
| SolusVM | Choosing Between Shared Storage and Local Storage for VPS Infrastructure | 1,033 | 11/11 | `blog/vps-storage-choice/` |

The two Sitejet pieces cross-link: the handover article points back at the
delivery SOP as its stage five. Publish the SOP piece first, or fix that URL.
The SolusVM piece is standalone.

Each folder holds the same six things: the .docx deliverable, the markdown
source of record, a publishing pack with the checklist worked item by item,
JSON-LD schema, an image manifest, and the humanizer gate results.

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

## Blog: Choosing Between Shared Storage and Local Storage for VPS Infrastructure

`blog/vps-storage-choice/`, client: **SolusVM**

| File | What it is |
| --- | --- |
| `Choosing Between Shared Storage...VPS Infrastructure.docx` | **Word deliverable.** Heading 1/2/3 styles, seven live hyperlinks, two image slots with hyperlinked "Image Source" captions |
| `shared-vs-local-storage-vps.md` | Markdown source of record |
| `seo-publishing-pack.md` | Metadata, the checklist worked item by item, brand guide compliance table, open items flagged |
| `schema-markup.json` | Article, FAQPage, a five-step HowTo and SoftwareApplication JSON-LD as one `@graph` |
| `image-manifest.md` | Two images plus one optional, alt text, source URLs, upload steps |
| `zerogpt-preflight-result.txt` | Detector gate results, 11/11 |

**Written for the SolusVM audience** (small to mid-sized hosting providers and
VPS resellers) in second person, per the SolusVM content writing guidelines. The
register is documentation-like rather than promotional, VPS and iSCSI and thin
provisioning are used without definition, and every performance claim carries a
figure. "SolusVM" appears in the correct casing throughout.

**Length:** 1,033 body words against a 800-1000 target with 25% headroom
accepted, or roughly 1,130 including headings.

**The angle:** the piece is built on a real product constraint rather than a
generic pros-and-cons list. High Availability in SolusVM requires Shared LVM
over iSCSI or NFS, and the Shared LVM implementation supports neither Thin LVM
nor snapshots. So the decision is not "which is faster", it is whether you want
to sell failover or sell oversubscription.

### Open items before publishing

1. Confirm the primary keyword (`shared storage vs local storage`) and check its
   volume. Task Info was N/A, so it was inferred from the headline.
2. Drop the two images in. `pexels.com` was blocked by the network egress proxy
   in this environment. See `image-manifest.md`.
3. Replace the placeholder author with a named person, role and personal
   LinkedIn URL, in the post and in `schema-markup.json`.
4. Verify the four SolusVM documentation URLs resolve. `docs.solusvm.com` and
   `solusvm.com` were both blocked here, so those URLs came from search results.
   Each supporting fact was confirmed in more than one result.
5. Spot-check the NVMe latency ranges and the SPDK iSCSI IOPS figures against
   the linked source.
6. After publishing, link older SolusVM posts to this one and test the target
   query in ChatGPT, Perplexity and Gemini.

## Tooling

`tools/build-docx.js` converts any of these markdown articles to a formatted
Word file:

```
npm install docx
node tools/build-docx.js <source.md> <output.docx>
```

It resolves the `docx` package from `DOCX_PATH`, then `NODE_PATH`, then the
usual `node_modules` lookup, so it runs from any checkout. Image placeholders
are generated in memory, so there is no external asset to stage; set
`PLACEHOLDER_DIR` to a folder of `placeholder-1.png`, `placeholder-2.png` and so
on if you want real comps in the frames instead.

It maps H1/H2/H3 to real Word heading styles, keeps hyperlinks live, renders
bullets through a proper numbering config, and drops a sized placeholder frame
into each image slot with the alt text and the hyperlinked "Image Source"
caption beneath it.

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

### How it evolves

A report goes in `reports/` using `TEMPLATE.md`. Every highlighted sentence gets
mapped to a known signal or marked NEW. New patterns land in the candidates
table; two independent sightings promotes one into the `MARKERS` dict in the
script so it is caught automatically from then on. A gate that passed on text
ZeroGPT then flagged is too loose and gets tightened, with the old and new
values recorded. Nothing changes without a report behind it.

Three pieces have been through it so far, all filed open pending a client-side
ZeroGPT run. Nothing is scored yet, so no threshold has moved on detector
evidence.

The first article already forced one recalibration: the sentence-opener gate
used a raw count of 3, which failed a clean 219-sentence draft where "the"
opened 16 sentences (7.3%, normal for English). It is now proportional with a
raw floor. Cutting that draft to 1,072 words then produced a second finding,
that large cuts break the variance gates because trimming attacks long sentences
first. Both are recorded in the learning log. The SolusVM piece added a third finding:
the adversarial pass itself breaks the paragraph-variance gate, because the
symmetric two-beat constructions you remove are the ones carrying the short
paragraphs. Run the script after that pass, not only before it.

### Usage

```
python3 .claude/skills/humanizer/scripts/zerogpt_preflight.py FILE.md --verbose
```
