# Publishing Pack: Stop Writing Content AI Tools Can't Understand

Everything the CMS needs, plus the SEO + AEO/GEO checklist worked line by line.

## Metadata

| Field | Value | Check |
| --- | --- | --- |
| Title tag | AI Content Optimisation: Write for AI Tools in 2026 | 51 chars, under the 60 limit, primary keyword plus year |
| H1 | Stop Writing Content AI Tools Can't Understand | APA title case. See the note below on the H1/title-tag split |
| Meta description | AI content optimisation without the guesswork. Four fixes that make your pages legible to ChatGPT, Gemini and AI Overviews, plus how to check what they see. | 156 chars, inside 150-160 |
| URL slug | `/ai-content-optimisation` | Short, keyword-rich, no stop words |
| Primary keyword | AI content optimisation | |
| Secondary keywords | AI visibility, AI search optimisation, content for AI search, AI Overviews, GEO, answer engine optimisation | |
| Audience | XOVI primary: agencies, freelancers, in-house SEO and SaaS marketers | |
| Point of view | Second person | |
| CTA destination | XOVI AI product page (`/xovi-ai/`) | |
| Publish date | 21 August 2026 | |

## Decisions you should sanity-check

Task Info came back **N/A** for key points, personas and keywords, so three
things were inferred. Each one is cheap to change now and expensive later.

**1. The primary keyword.** `AI content optimisation` was derived from the
headline. It appears in the title tag, the meta description, the first sentence,
one H2 and one FAQ H3, so swapping it touches five places.

**2. British spelling.** The brand guide writes "optimisation" and
"customisable", so the article follows house style. That matters here because
the keyword itself carries the spelling. US "optimization" almost certainly has
the larger global volume. If the .com site targets US search, swap the spelling
in the five places above and in the slug. Schema.org type names
(`Organization`) keep the z regardless, and the existing xovi.com URL
`/ai-search-optimization-xovi/` already uses the US spelling, which is worth
resolving one way or the other across the site.

**3. Search volume and difficulty were not checked.** That is checklist item
1.1 and it is still open. Ahrefs and Semrush were not reachable from this
environment.

**On the H1 not matching the title tag.** Checklist 2.3 asks the H1 to mirror
the title tag. The article title was fixed by the brief, and it is a good
headline: it is a command, it names a real fear, and it earns the click. The
title tag carries the keyword and the year for the SERP instead. If you would
rather have them match exactly, use `Stop Writing Content AI Tools Can't
Understand (2026)` as the title tag and accept losing the keyword from it.

## Length

Target was 800-1000 words. The article is **1,154 words** including headings and
excluding the image credit lines, which is 15% over the top of the range. Two
things drove that: the brief asks for a Key Takeaways box, a PAA section and a
five-question FAQ, which together account for roughly 320 words before the
article argues anything; and the brand guide asks for specifics rather than
generalities, which costs words. Body prose alone, the number the humanizer
script measures, is 1,035 words.

Cut the FAQ to three questions if you need to land inside 1,000. Nothing else
comes out without losing a citation or a fix.

## Checklist status

### 1. Before You Write

| Item | Status |
| --- | --- |
| Confirm primary keyword, check volume in Ahrefs / Semrush | **Open.** Keyword proposed, volume not verified. |
| Research People Also Ask questions | Done. Two PAA-shaped H2s and all five FAQ H3s are written as questions a buyer would type. |
| Check top 3 ranking pages | **Open.** No competitor set supplied, and the brief said N/A for competitors. |
| Confirm CTA destination | Done. XOVI AI product page. |

### 2. On-Page SEO

| Item | Status |
| --- | --- |
| Title tag with keyword and year, under 60 chars | Done. 51 chars. |
| Meta description 150-160 chars with keyword and value prop | Done. 156 chars. |
| H1 mirrors title tag | **Partial by design.** See the note above. |
| Keyword in first 100 words and in at least one H2 | Done. First five words of the direct answer, plus the H2 "AI Content Optimisation Is a Different Job From Ranking" and the FAQ H3. |
| Slug short, keyword-rich, no stop words | Done. `/ai-content-optimisation`. |
| Descriptive alt text with keyword where natural | Done. Image 1 carries the keyword. Images 2 and 3 describe what is in the frame, because forcing the keyword into a photo of a laptop would read as stuffing. |

### 3. Content Structure (AEO)

| Item | Status |
| --- | --- |
| 40-60 word direct answer at the very top | Done. 51 words, immediately under the H1. |
| Key Takeaways box near the top, 4-5 bullets | Done. Five bullets, written at deliberately uneven lengths. |
| PAA questions as H2 or H3 | Done. One question H2 plus five FAQ H3s. |
| FAQ section at the bottom, 5-8 Q&A pairs | Done. Five pairs, which suits the word count. Answer lengths run from one line to four sentences on purpose. |

### 4. Schema Markup (client reference only)

Drafted in `schema-markup.json`: FAQPage, Article, HowTo and SoftwareApplication,
all generated from the live copy. The SoftwareApplication block describes XOVI AI
and should only ship if you want product markup on a blog URL. Update
`datePublished`, `author` and the `url` fields before it goes live.

### 5. E-E-A-T and Trust Signals

| Item | Status |
| --- | --- |
| Author bio with name, role and LinkedIn | **Open.** No named author was supplied. Add a real person with a personal LinkedIn URL before publishing. A named human author matters twice here: for E-E-A-T, and for the no-AI-content requirement. |
| Last updated date shown and current | Done. 21 August 2026. |
| At least one external authoritative source cited | Done. Two: Pew Research Center and Ahrefs. Both need the spot-check below. |
| Avoid generic AI-sounding sentences | Done. All eleven humanizer gates pass. See `zerogpt-preflight-result.txt` and the report under `.claude/skills/humanizer/reports/`. |

### 6. Internal Linking

Three internal links, all partial-match keyword anchors, none of them "click here":

| Anchor text | Destination |
| --- | --- |
| The approved XOVI AI positioning sentence | `https://www.xovi.com/xovi-ai/` |
| AI Visibility Score | `https://www.xovi.com/xovi-ai-launch-ai-visibility/` |
| AI search optimisation | `https://www.xovi.com/ai-search-optimization-xovi/` |

**Open item:** checklist 6.3 wants older posts updated to link here. That is a
CMS job after publication.

**Also worth checking:** xovi.com was unreachable from this environment, so the
three URLs above came from search results rather than from opening the pages.
Confirm each one resolves before publishing.

### 7. GEO

| Item | Status |
| --- | --- |
| At least one specific, citable data point | Done. Two. Pew Research Center: 8% of visits with an AI summary produced a result click, against 15% without, from 68,879 searches by 900 US adults in March 2025. Ahrefs: branded web mentions correlated with AI Overview visibility at 0.664 against 0.218 for referring domains, across 75,000 brands. |
| Brand name used consistently and exactly | Done. XOVI and XOVI AI throughout, always in caps. Lowercase "xovi" appears only inside URLs. |
| Test target query in ChatGPT, Perplexity and Gemini after publishing | **Open.** Post-publication task, and the article tells readers to do the same thing. |

## Brand guide compliance

- **Voice.** Direct, short sentences, opinions where they are earned. "One is a
  fact. The other is a mood." and "be sceptical of anyone who does" are the
  lightly-opinionated register the guide asks for.
- **No guarantees.** The piece says outright that nobody can promise a mention
  in an AI answer. That is section 10's hard rule and it is stated rather than
  implied.
- **Approved positioning anchor used verbatim.** The XOVI AI definition appears
  word for word as the opening of "Where XOVI AI Fits", used as the anchor text
  for the product link. It contains "AI-powered search", which is otherwise on
  the avoid list; it stays because the guide says use the anchor as-is.
- **Access → Understanding → Visibility → Improvement → Monitoring** is the
  spine of that section, in order.
- **Not positioned as an SEO replacement.** The first FAQ answers this
  explicitly, and the body frames the product as the upstream diagnostic layer.
- **White-label and client-ready exports** are called out for agency users
  specifically, per section 10.
- **Banned vocabulary avoided.** No streamline, leverage, robust, holistic,
  empower, revolutionize, game-changer, cutting-edge, seamless, next-generation,
  intelligent or smart. Checked by grep, not by eye.
- **No LLM mechanics explained.** The article talks about chunking and
  retrieval in terms of what it does to your page, never how a model works.

## Two sources to spot-check

Outbound access to pewresearch.org and ahrefs.com is blocked from this
environment, so both figures were confirmed through search results rather than
by opening the source. Open the two links and confirm the sentences before
publishing.

1. **Pew Research Center, 22 July 2025.** "Google users are less likely to click
   on links when an AI summary appears in the results." Reported figures: a
   result link was clicked on 8% of visits where an AI summary appeared and 15%
   where none did, from 68,879 Google searches by 900 US adults, March 2025.
2. **Ahrefs, August 2025.** "An Analysis of AI Overview Brand Visibility Factors
   (75K Brands Studied)." Reported figures: branded web mentions correlate with
   AI Overview brand visibility at 0.664; referring domains at 0.218.

If either figure has moved, the surrounding sentence still works with a new
number. Neither argument depends on the exact value.

## Deliverable formats

| File | Format |
| --- | --- |
| `Stop Writing Content AI Tools Can't Understand.docx` | Word, Heading 1/2/3 styles, live hyperlinks, image slots with hyperlinked "Image Source" captions |
| `ai-content-optimisation.md` | Markdown source of record |

Structure verified by parsing the packed XML: one H1, six H2, nine H3, five
bullets, three image slots, eight live hyperlinks. LibreOffice in this
environment cannot open any .docx, including the client's own brand guide file,
so a visual render was not possible.
