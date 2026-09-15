# Publishing Pack: AI Visibility Audit

## Metadata

| Field | Value | Check |
| --- | --- | --- |
| Title tag | AI Visibility Audit: How to Run One for Clients (2026) | 54 chars, under 60, primary keyword plus year |
| H1 | How to Run an AI Visibility Audit Before a Client Asks Why ChatGPT Ignores Them | APA title case |
| Meta description | An AI visibility audit checks whether AI crawlers can read a site, how ChatGPT describes the business and who gets recommended instead. Five steps, in order. | 156 chars, inside 150-160 |
| URL slug | `/ai-visibility-audit` | Short, keyword-rich, no stop words |
| Primary keyword | AI visibility audit | |
| Secondary keywords | AI visibility, AI Visibility Score, ChatGPT recommendations, AI search visibility, AI crawlers, competitor benchmarking | |
| Audience | XOVI: agencies and freelancers on retainer work, plus in-house SEO pros | |
| Point of view | Second person | |
| Word count | 1,001 body words (target 800-1000). 1,052 including the author bio. | |
| CTA destination | XOVI AI product page (`/xovi-ai/`) | |

## Assumptions flagged

Task Info was N/A, so there was no headline, keyword list or key-points brief.
The topic, angle and keyword were chosen from the brand guide and the AEO/SEO
checklist:

- **Topic: an AI visibility audit for agency clients.** Part Two of the brand
  guide says XOVI AI is a new category and "content needs to educate readers on
  why AI visibility matters before it can sell the solution." The checklist's
  GEO section points the same way. If the client wanted a core-XOVI topic
  (white-label reporting, rank tracking, audits), this piece does not cover it.
- **Primary keyword: AI visibility audit.** It appears in the first sentence,
  the title tag, one H2 and two alt texts. Search volume was not checked in
  Ahrefs or Semrush (checklist 1.1 still open).
- **Structure follows the Access, Understanding, Visibility, Improvement,
  Monitoring framework** the brand guide mandates for XOVI AI explanations.
- The approved positioning anchor is used verbatim and unchanged.

## Checklist status

### 1. Before you write

| Item | Status |
| --- | --- |
| Confirm keyword, check volume | **Open.** Keyword proposed, volume not verified. |
| Research PAA questions | Done. Three question H2s plus five FAQ H3s, all phrased as searches people run. |
| Check top 3 ranking pages | **Open.** Search-result titles for "AI visibility audit" were reviewed, but the pages themselves could not be opened from this environment. |
| Confirm CTA destination | Done. XOVI AI product page. |

### 2. On-page SEO

| Item | Status |
| --- | --- |
| Title tag, keyword and year, under 60 | Done. 54 chars. |
| Meta description 150-160 | Done. 156 chars. |
| H1 mirrors the title tag | Done. Both lead on the AI visibility audit. |
| Keyword in first 100 words and in an H2 | Done. First four words, and H2 "What Does an AI Visibility Audit Actually Check?" |
| Slug short and keyword-rich | Done. `/ai-visibility-audit`. |
| Descriptive alt text | Done. Three images, see `image-manifest.md`. |

### 3. Content structure (AEO)

| Item | Status |
| --- | --- |
| 40-60 word direct answer at the top | Done. 56 words. |
| Key Takeaways, 4-5 bullets | Done. Five bullets at deliberately different lengths. |
| PAA questions as H2 or H3 | Done. "What Does an AI Visibility Audit Actually Check?", "Can You Do This by Hand?", "How Do You Turn the Audit Into a Client Deliverable?" plus the FAQ. |
| FAQ, 5-8 pairs | Done. Five pairs, answer length varies from one line to a short paragraph. |

### 4. Schema markup (client reference)

`schema-markup.json` carries FAQPage, Article and a five-step HowTo, generated
from the live copy. The Article block nests a SoftwareApplication reference to
XOVI AI under `about` rather than shipping a separate SoftwareApplication
schema, which belongs on the product page, not on a blog URL.

### 5. E-E-A-T and trust signals

| Item | Status |
| --- | --- |
| Author bio with name, role, LinkedIn | Partial. Team byline in place, pointing at the XOVI GmbH company page. **Swap in a named author with a personal LinkedIn URL before publishing.** |
| Last updated date | Done. 15 September 2026. |
| External authoritative source | Done. Ahrefs, 300,000-keyword study of AI Overview click-through. |
| Avoid generic AI-sounding sentences | Done. All eleven humanizer gates pass, see `zerogpt-preflight-result.txt`. |

### 6. Internal linking

| Anchor text | Destination |
| --- | --- |
| XOVI AI | `https://www.xovi.com/xovi-ai/` |
| XOVI | `https://www.xovi.com/` |
| white-label report | `https://www.xovi.com/xovi-tool/reporting/` |
| eight ways to get cited by AI tools | `https://www.xovi.com/how-to-get-your-brand-cited-by-ai-tools/` |

Four internal links against a minimum of three. All four URLs were confirmed
through search results, but xovi.com could not be opened from this environment,
so check each resolves before publishing. Checklist item 6.3 (update older posts
to link here) is a post-publication task; the natural candidates are the XOVI AI
launch post and "AI Search and SEO: The Future Is Now".

### 7. GEO

| Item | Status |
| --- | --- |
| Specific, citable data point | Done. Top organic result CTR fell from 7.3% to 2.6%, a 34.5% drop, across 300,000 keywords. Ahrefs, 2025. |
| Brand name used consistently | Done. "XOVI" and "XOVI AI" only, all caps, never "Xovi". |
| Test target query in ChatGPT, Perplexity, Gemini | **Open.** Post-publication task. |

## Brand guide compliance

- Voice: leads with the takeaway, short sentences, lightly opinionated. "Let's
  be real" is lifted from the guide's own example phrases.
- Framework: Access, Understanding, Visibility, Improvement, Monitoring, in that
  order, as the five numbered H3s.
- Approved positioning anchor used verbatim in the deliverable section.
- Named capabilities referenced: access check, understanding analysis,
  competitor benchmarking, Improvement Centre, scheduled monitoring, AI
  Visibility Score, white-label reporting.
- No guarantees of mentions or placement. The caveat paragraph says so outright.
- No banned vocabulary (streamline, leverage, robust, holistic, empower,
  revolutionize, game-changer, cutting-edge, AI-powered outside the approved
  anchor, next-generation, intelligent, smart).
- XOVI AI positioned as the upstream complement to SEO, never a replacement.
  "SEO measures rankings. An AI visibility audit diagnoses understanding."
- No technical explanation of how language models work.
- Competitors never named or mocked.

## Source to spot-check

The Ahrefs figures (7.3% to 2.6%, 34.5%, 300,000 keywords) were consistent
across several independent write-ups, but `ahrefs.com` could not be opened from
this environment. Open `https://ahrefs.com/blog/ai-overviews-reduce-clicks/`
and confirm the three numbers before publishing. Ahrefs published a follow-up
in December 2025 putting the drop at 58%; the piece cites the original
34.5% figure because it is the one with the published methodology, but the
follow-up URL is `https://ahrefs.com/blog/ai-overviews-reduce-clicks-update`
if the client prefers the newer number.

## Deliverable formats

| File | Format |
| --- | --- |
| `How to Run an AI Visibility Audit Before a Client Asks Why ChatGPT Ignores Them.docx` | Word, Heading 1/2/3 styles, live hyperlinks, image slots with hyperlinked "Image Source" captions |
| `ai-visibility-audit.md` | Markdown source of record |

## Google Doc and tracker

The brief asks for the blog to be moved to a Google Doc with edit access for
all and added to the internal tracker. The Google Drive connector was not
authorised in this session, so that step could not be done here. Upload the
.docx to Drive, open it as a Google Doc, set sharing to "Anyone with the link
can edit", and paste the link into the tracker next to the topic.
