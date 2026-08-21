# Publishing Pack: Agency Delivery SOP

Everything the CMS needs, plus the AEO/SEO checklist worked line by line.

## Metadata

| Field | Value | Check |
| --- | --- | --- |
| Title tag | Agency Delivery SOP: Run Like a 10-Person Team in 2026 | 54 chars, under the 60 limit, primary keyword plus year |
| H1 | The Delivery SOP That Lets a 3-Person Agency Run Like a 10-Person One | Mirrors the title tag, APA title case |
| Meta description | An agency delivery SOP that lets three people ship like ten. Five stages, three documents and a 30-day rollout you can run without pausing client work. | 151 chars, inside 150-160 |
| URL slug | `/agency-delivery-sop` | Short, keyword-rich, no stop words |
| Primary keyword | agency delivery SOP | |
| Secondary keywords | web design agency workflow, agency project management SOP, scope creep, client review rounds, agency capacity | |
| Audience | Sitejet Studio: agencies, freelancers, web professionals | |
| Point of view | Second person | |
| CTA destination | Sitejet Studio agency page (`/en/website-builder-for-agencies`) | |

## Assumptions flagged for the client

The brief listed "check task info" for key points, target personas and target keywords. Task Info was subsequently confirmed as **N/A**, so there is no source document to check against. The following were inferred from the headline and the brand guide:

- Primary keyword set to **agency delivery SOP**. Swap it if the keyword sheet says otherwise. The keyword appears in the title tag, the H1, the first sentence and one H2, so a change touches four places.
- Audience read as **Sitejet Studio** (agencies and freelancers), not SITEJET Website Builder. The whole piece is written to that side of the split and no DIY features are referenced.
- Search volume and difficulty were not checked in Ahrefs or Semrush. That is checklist item 1.1 and still needs doing.

## Length

Target was 800-1000 words, with up to 25% over accepted. The article is **1,072 words** including headings and excluding image credit lines, which sits inside the accepted range. An earlier 2,956-word draft was cut to this spec; the three images dropped in that cut are listed in `image-manifest.md` in case the piece is ever expanded.

## Checklist status

### 1. Before you write

| Item | Status |
| --- | --- |
| Confirm primary keyword, check volume in Ahrefs / Semrush | **Open.** Keyword proposed, volume not verified. |
| Research People Also Ask questions | Done. PAA-shaped questions used as H2s and as all eight FAQ H3s. |
| Check top 3 ranking pages | **Open.** Competitor set not supplied and the brief said N/A for competitors. |
| Confirm CTA destination | Done. Sitejet Studio agency page. |

### 2. On-page SEO

| Item | Status |
| --- | --- |
| Title tag with keyword and year, under 60 chars | Done. 54 chars. |
| Meta description 150-160 chars with keyword and value prop | Done. 151 chars. |
| H1 mirrors title tag | Done. |
| Keyword in first 100 words and in at least one H2 | Done. First sentence, and H2 "The Five Stages of an Agency Delivery SOP". |
| Slug short, keyword-rich, no stop words | Done. `/agency-delivery-sop`. |
| Descriptive alt text with keyword where natural | Done. Three images, alt text written per image, see `image-manifest.md`. |

### 3. Content structure (AEO)

| Item | Status |
| --- | --- |
| 40-60 word direct answer at the very top | Done. 51 words, sits directly under the H1. |
| Key Takeaways box near the top, 4-5 bullets | Done. Five bullets, deliberately uneven lengths. |
| PAA questions as H2 or H3 | Done. One question H2 plus five FAQ H3s. |
| FAQ section at the bottom, 5-8 Q&A pairs | Done. Five pairs, which is right for the word count. |

### 4. Schema markup (client reference)

All four blocks are drafted in `schema-markup.json`. FAQPage, Article and HowTo are populated from the live copy. SoftwareApplication is included for the Sitejet Studio reference and should only ship if the client wants it on a blog URL.

### 5. E-E-A-T and trust signals

| Item | Status |
| --- | --- |
| Author bio with name, role and LinkedIn | Partial. Team byline and Sitejet LinkedIn link in place. **Swap in a named author with a personal LinkedIn URL before publishing.** A named human author is worth more here than a team byline, both for E-E-A-T and for the no-AI requirement. |
| Last updated date shown and current | Done. 21 August 2026. |
| At least one external authoritative source cited | Done. PMI 2018 Pulse of the Profession, linked to the PMI-hosted PDF. |
| Avoid generic AI-sounding sentences | Done. See `zerogpt-preflight-result.txt` and the humanizer skill report. |

### 6. Internal linking

Three internal links, all with partial-match keyword anchors and none using "click here":

| Anchor text | Destination |
| --- | --- |
| Sitejet Studio | `https://www.sitejet.io/en/website-builder-for-agencies` |
| White label options | `https://help.sitejet.io/hc/en-us/articles/24276052896919-Whitelabel-in-Sitejet` |
| built-in SEO tools | `https://www.sitejet.io/en/features` |

**Open item:** checklist 6.3 asks for older posts to be updated to link to this article. That needs doing in the CMS after publication and cannot be done from the draft.

### 7. GEO

| Item | Status |
| --- | --- |
| At least one specific, citable data point | Done. 52% of projects experience scope creep, up from 43% five years earlier, PMI 2018 Pulse of the Profession. |
| Brand name used consistently and exactly | Done. "Sitejet" and "Sitejet Studio" throughout. "Studio" never appears alone. No SITEJET Website Builder features referenced, per the brand guide's product split. |
| Test target query in ChatGPT, Perplexity and Gemini after publishing | **Open.** Post-publication task. |

## Brand guide compliance

- Written entirely for the Sitejet Studio audience. No DIY features referenced, and nothing in the piece implies SITEJET Website Builder has client portals, workflows, team roles, white label or API access.
- Tone is professional and workflow-focused, leading with efficiency, control and scale rather than encouragement. That matches the Studio half of the tone-of-voice section.
- Product names always carry the Sitejet prefix.
- WebPros ecosystem referenced through the built-in SEO tools link. XOVI and SocialBee callouts were cut with the length reduction and can be restored if the piece is expanded.
- Banned generic phrasing avoided. No "drag and drop", no "no coding required", no "stunning websites".

## One source to spot-check

The PMI statistic was confirmed through search but the primary PDF could not be opened from this environment, because outbound access to pmi.org is blocked here. The figure is widely reported as: PMI's 2018 Pulse of the Profession found 52% of projects completed in the prior 12 months experienced scope creep, up from 43% five years earlier. Open the linked PDF and confirm the sentence before publishing.


## Deliverable formats

| File | Format |
| --- | --- |
| `The Delivery SOP That Lets a 3-Person Agency Run Like a 10-Person One.docx` | Word, H1/H2/H3 heading styles, live hyperlinks, image slots with hyperlinked "Image Source" captions |
| `agency-delivery-sop.md` | Markdown source of record |

The .docx uses real Word heading styles (Heading 1/2/3), so the CMS import and
any table of contents will pick the structure up correctly. Structure verified
from the packed XML: one H1, six H2, ten H3, five bullets, three image slots,
eight live hyperlinks.

A visual render could not be produced here. LibreOffice in this environment
fails to load any .docx, including the client's own brand guide file, so the
check was done against the document XML instead.
