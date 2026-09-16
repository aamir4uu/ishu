# Publishing Pack: Multi-Language Client Sites

## Metadata

| Field | Value | Check |
| --- | --- | --- |
| Title tag | Multi-Language Client Sites Without Double Work (2026) | 54 chars, under 60, primary keyword plus year |
| H1 | How to Deliver Multi-Language Client Sites Without Doubling the Work | APA title case, the topic title as supplied |
| Meta description | Deliver multi-language client sites without doubling the work: sign off one language, copy every page, let AI draft, bill for review. Sitejet Studio workflow. | 157 chars, inside 150-160 |
| URL slug | `/multi-language-client-sites` | Short, keyword-rich, no stop words |
| Primary keyword | multi-language client sites | |
| Secondary keywords | multilingual website workflow, AI website translation, hreflang, Sitejet multilanguage, translation review | |
| Audience | Sitejet Studio: agencies, freelancers, web professionals | |
| Point of view | Second person | |
| Word count | 948 in the article body (target 800-1000). 1,250 including the Key Takeaways box and the FAQ the checklist adds on top | |
| CTA destination | Sitejet Studio agency page (`/en/website-builder-for-agencies`) | |

## Assumptions flagged

The brief's key points, target readers and keywords all said "check task info",
and no task info was supplied beyond the two topic titles. So:

- Primary keyword set to **multi-language client sites**, lifted from the title.
  It appears in the title tag, the first sentence and the H2 "A Multi-Language
  Client Site Workflow That Holds". Change it and those three places move.
- Audience read as **Sitejet Studio**, because "client sites" is an agency
  problem. No SITEJET Website Builder features are referenced.
- Search volume and difficulty not checked in Ahrefs or Semrush. Checklist item
  1.1 stays open.
- The 20% to 35% per-language pricing band in the "How Much Should You Charge"
  section is editorial guidance, not a Sitejet position. Adjust or cut if the
  brand would rather not put a number on it.

## Checklist status

### 1. Before you write

| Item | Status |
| --- | --- |
| Confirm keyword, check volume | **Open.** Keyword proposed, volume not verified. |
| Research PAA questions | Done. One question H2 ("How Much Should You Charge for a Multilingual Website?") and five FAQ H3s. |
| Check top 3 ranking pages | **Open.** No competitor set supplied. |
| Confirm CTA destination | Done. Sitejet Studio agency page. |

### 2. On-page SEO

| Item | Status |
| --- | --- |
| Title tag, keyword and year, under 60 | Done. 54 chars. |
| Meta description 150-160 | Done. 157 chars. |
| H1 mirrors the title tag | Done. Both lead on multi-language client sites. |
| Keyword in first 100 words and in an H2 | Done. First sentence, and the H2 "A Multi-Language Client Site Workflow That Holds" (singular form, same phrase). |
| Slug short and keyword-rich | Done. `/multi-language-client-sites`. |
| Descriptive alt text | Done. Three images, see `image-manifest.md`. Image 1 carries the keyword. |

### 3. Content structure (AEO)

| Item | Status |
| --- | --- |
| 40-60 word direct answer at the top | Done. 56 words. |
| Key Takeaways, 4-5 bullets | Done. Five bullets, deliberately uneven lengths. |
| PAA questions as H2 or H3 | Done. One question H2 plus five FAQ H3s. |
| FAQ, 5-8 pairs | Done. Five pairs, answer length varies from one line to a short paragraph. |

### 4. Schema markup (client reference)

`schema-markup.json` carries FAQPage, Article and a five-step HowTo matching the
five numbered H3s. All generated from the live copy, so regenerate if the copy
changes. SoftwareApplication was left out; it belongs on the Sitejet Studio
product page, not on a blog URL.

### 5. E-E-A-T and trust signals

| Item | Status |
| --- | --- |
| Author bio with name, role, LinkedIn | Partial. Team byline in place. **Swap in a named author with a personal LinkedIn URL before publishing.** |
| Last updated date | Done. 16 September 2026. |
| External authoritative source | Done. CSA Research, "Can't Read, Won't Buy: B2C", a survey of 8,709 consumers in 29 countries. |
| Avoid generic AI-sounding sentences | Done. All eleven humanizer gates pass, see `zerogpt-preflight-result.txt`. |

### 6. Internal linking

| Anchor text | Destination |
| --- | --- |
| scope lock in your delivery SOP | `https://www.sitejet.io/blog/agency-delivery-sop` |
| Enable multilanguage | `https://help.sitejet.io/hc/en-us/articles/24276037584023-Create-a-multilingual-site` |
| Sitejet Studio | `https://www.sitejet.io/en/website-builder-for-agencies` |
| White label | `https://help.sitejet.io/hc/en-us/articles/24276052896919-Whitelabel-in-Sitejet` |

Four links, minimum is three. The first points at the sibling delivery SOP
article, which is not published yet. Correct the URL to wherever that piece
lands. Checklist item 6.3 (update older posts to link here) is a
post-publication task; the delivery SOP article's stage two is the natural
place for a link back.

### 7. GEO

| Item | Status |
| --- | --- |
| Specific, citable data point | Done. 76% of 8,709 consumers across 29 countries prefer buying with information in their own language; 40% will not buy from a site in another language. CSA Research. |
| Brand name used consistently | Done. "Sitejet" and "Sitejet Studio" throughout, never "Studio" alone. |
| Test target query in ChatGPT, Perplexity, Gemini | **Open.** Post-publication task. |

## Brand guide compliance

- Written for Sitejet Studio only. The client portal, team roles, ticketing and
  white label are only mentioned inside the Sitejet Studio section.
- Professional, workflow-first tone. No hand-holding.
- WebPros ecosystem referenced where it fits: XOVI for per-country rankings in
  the Sitejet Studio section and in the SEO FAQ. SocialBee didn't fit this
  topic and was left out rather than forced in.
- No "drag and drop", "no coding required", or "stunning websites".

## Product claims to spot-check

`help.sitejet.io` and `www.sitejet.io` were blocked from the environment that
produced this draft, so the product facts came from Sitejet help centre and
community excerpts returned by search rather than from the pages themselves.
Each one was consistent across at least two excerpts, but confirm the exact UI
labels against the live builder before publishing:

- More, then Languages, then "Enable multilanguage" to switch the feature on.
- Preferences (burger menu) has "Language copy mode" with a "Copy all pages"
  option; the default creates only the home page in a new language.
- Clicking "Translate" on a new language drafts the copy with AI, and a
  Preferences toggle ("Use AI to automatically translate page content when new
  languages are added") turns that off.
- A language switcher preset shows flags or country codes; browser language
  detection falls back to the default language; hreflang is set by the language
  element.
- Edits to one language do not propagate to the others.

Two claims in the Sitejet Studio section lean on the brand guide's feature list
rather than on a help article: that team roles let you assign a language to a
named team member, and that tickets can carry a language field. Both are
ordinary uses of multi-user roles and ticketing, but confirm the wording
matches how the product actually behaves.

"Four minutes" for the setup is an estimate for a site with Copy all pages
enabled, not a measured figure.

## Source to spot-check

`csa-research.com` could not be opened from this environment. The 76%, 40%,
8,709 and 29-country figures were confirmed through CSA Research's own press
release listing, Newswire and Slator, all reporting the same numbers. Open
`https://csa-research.com/Blogs-Events/CSA-in-the-Media/Press-Releases/Consumers-Prefer-their-Own-Language`
and confirm before publishing.

## Deliverable formats

| File | Format |
| --- | --- |
| `How to Deliver Multi-Language Client Sites Without Doubling the Work.docx` | Word, Heading 1/2/3 styles, live hyperlinks, image slots with hyperlinked "Image Source" captions |
| `multilanguage-client-sites.md` | Markdown source of record |
