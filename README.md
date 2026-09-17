# Content Delivery

Two client workstreams. Every piece is gated by the humanizer skill before
delivery, and every Word file is built from a markdown source of record with
`tools/build-docx.js`.

1. **Sitejet** (sitejet.io): two new blog articles for the Sitejet Studio
   audience, second person, per the brand content guidelines and the AEO/SEO
   checklist.
2. **Hero FinCorp** (herofincorp.com): seven existing SEO landing pages
   refreshed against the client's content-gap briefs at a strict 500 to 700
   words each. See [Hero FinCorp refreshes](#hero-fincorp-seven-seo-landing-page-refreshes).

| Article | Words | Gates | Folder |
| --- | --- | --- | --- |
| The Delivery SOP That Lets a 3-Person Agency Run Like a 10-Person One | 1,072 | 11/11 at delivery; 10/11 re-measured on 2026-09-17, see note | `blog/delivery-sop/` |
| What to Send a Client on Launch Day so They Never Email You Again | 1,233 | 11/11 at delivery; 10/11 re-measured on 2026-09-17, see note | `blog/launch-day-handover/` |
| What Is the UPI Transaction Limit per Day & Month? Complete Guide | 690 | 11/11 | `blog/herofincorp/upi-transaction-limit/` |
| Working Capital Loan: Meaning, Eligibility and 2026 Application Guide | 698 | 11/11 | `blog/herofincorp/working-capital-loan/` |
| E-KYC: Meaning, Full Form, Types, Process, and Eligibility | 698 | 11/11 | `blog/herofincorp/what-is-ekyc/` |
| What Is Suit Filed and How to Remove It in CIBIL Report? | 997 | 11/11 | `blog/herofincorp/suit-filed-cibil/` |
| What Is an MSME Loan? Meaning, Types, Eligibility & How to Apply in 2026 | 697 | 11/11 | `blog/herofincorp/msme-loan/` |
| Simple Ways to Reduce Your Loan EMI | 698 | 11/11 | `blog/herofincorp/reduce-loan-emi/` |
| Personal Loan Default Consequences in India & Legal Impact | 976 | 11/11 | `blog/herofincorp/personal-loan-default/` |

Note on the two Sitejet rows: a measurement bug fixed on 2026-09-17 (bullets
were being counted as one sentence) means both now sit one sentence short of
the long-sentence floor (11.4% and 11.6% against 12%). Nothing else changed.
They were delivered as gated at the time and have not been edited since.

The two pieces cross-link: the handover article points back at the delivery SOP
as its stage five. Publish the SOP piece first, or fix that URL.

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

## Hero FinCorp: Seven SEO Landing Page Refreshes

`blog/herofincorp/`

Seven "Existing Content" briefs from the client's SEO team, each an annotated
copy of a live herofincorp.com article with "New Suggested H2/H3" blocks
(content nature, word count, target keyword, competitor reference screenshot)
and a list of new FAQs. The project brief fixes the article length at 500 to
700 words, with up to 1,000 allowed in extreme cases. So each deliverable is
the whole article rewritten at that length: every section the brief asks for,
the suggested H1, the corrected facts, the new FAQs, and the existing copy
condensed to what fits around them.

| Page | Live URL | Brief mandates | Words | Folder |
| --- | --- | --- | --- | --- |
| What Is the UPI Transaction Limit per Day & Month? Complete Guide | herofincorp.com/blog/upi-transaction-limit | 3 sections + 5 FAQs | 690 | `upi-transaction-limit/` |
| Working Capital Loan: Meaning, Eligibility and 2026 Application Guide | herofincorp.com/blog/guide-understanding-working-capital-loans | 2 sections + 7 FAQs | 698 | `working-capital-loan/` |
| E-KYC: Meaning, Full Form, Types, Process, and Eligibility | herofincorp.com/blog/what-is-ekyc | 4 sections + 4 FAQs | 698 | `what-is-ekyc/` |
| What Is Suit Filed and How to Remove It in CIBIL Report? | herofincorp.com/blog/how-to-remove-suit-filed-in-cibil-report | 4 sections + 6 FAQs | 997 | `suit-filed-cibil/` |
| What Is an MSME Loan? Meaning, Types, Eligibility & How to Apply in 2026 | herofincorp.com/blog/msme-loan | 1 section + 4 FAQs | 697 | `msme-loan/` |
| Simple Ways to Reduce Your Loan EMI | herofincorp.com/blog/simple-ways-reduce-your-loan-emi | 1 section + 6 FAQs | 698 | `reduce-loan-emi/` |
| Personal Loan Default Consequences in India & Legal Impact | herofincorp.com/blog/what-are-the-consequences-of-defaulting-on-a-personal-loan | 5 sections + 6 FAQs | 976 | `personal-loan-default/` |

Words are counted the way a client counts them: headings, body copy, list
items and table cells, with editor notes, image captions and the standard
disclaimer excluded (`tools/count-words.py`). Suit filed and personal loan
default are the two extreme cases: their briefs mandate 600 to 800 words of
new sections and FAQs on their own, so they run above 700 and under 1,000.

Each folder holds the same six things:

| File | What it is |
| --- | --- |
| `<Title>.docx` | **Word deliverable.** The whole article. Heading 1/2/3 styles, live hyperlinks, banner embedded (or a placeholder frame where the brief carried none) with a hyperlinked "Image Source" caption, tables, numbered lists. No editor notes; alt text lives in each image's alt attribute |
| `<slug>.md` | Markdown source of record, with HTML-comment notes on the H1, the banner, the corrections and the length |
| `refresh-notes.md` | How the brief was met section by section, what was kept and cut, corrections to the live copy, the fact-check log with sources, open items |
| `image-manifest.md` | Banner and infographic placement, alt text, source links, and what still needs doing |
| `zerogpt-preflight-result.txt` | The length gate and the eleven detector gates on the final draft |
| `images/` | The client's own banners and infographics, carried over from the briefs |

### Facts corrected in the client's existing copy

Each is marked and sourced in the page's `refresh-notes.md`:

- **MSME classification thresholds** were the 2020 values. Revised from
  1 April 2025 (Notification S.O. 1364(E)).
- **CLCSS** was described as a live 15% subsidy. Its general component closed
  on 31 March 2020; only the Special CLCSS for SC/ST enterprises operates.
- **"CIBIL Commercial Rank (CCR)"** is the CIBIL MSME Rank (CMR).
- **MSME sector statistics** updated to Ministry of MSME figures (7.83 crore
  Udyam registrations, 45.8% of exports).
- **UPI sector table**: the education and healthcare row had its Rs 5 lakh
  figure in the wrong column.
- **Personal loan ceiling** on the e-KYC page read Rs 5 lakh; Hero FinCorp's
  own product page now says Rs 7 lakh. Flagged for the product team.
- **CIBIL dispute follow-up** said 45 days; RBI's timeline is 30.
- **Loan default page**: "defaults drop off the credit report after seven
  years" (no such rule in India), "IBC insolvency for Rs 1 crore personal loan
  defaults" (a corporate threshold), and "IPC 420" (replaced by BNS section
  318 on 1 July 2024) were all removed or updated.
- **EMI page**: "seven ways" above a list of six; a prepayment section that
  contradicted its own heading; and a disclaimer about travel and itineraries
  pasted in from another site.

### Open items before publishing

1. Hero FinCorp's site, NPCI, CIBIL, UIDAI and every stock-photo host were
   blocked by the egress policy in the drafting environment. Product figures
   (14% business loan rate, Rs 7 lakh personal loan ceiling) and the August
   2026 NPCI biometric change were confirmed through search results only.
   Each `refresh-notes.md` lists what to re-check on the live pages.
2. Banners: four pages keep their existing banner, embedded from the brief,
   with the Image Source line pointing at the live article. Working capital,
   EMI and loan default briefs carry none, so those drafts hold a placeholder
   frame and a proposed Pexels photo. The UPI banner still shows the old title
   and needs re-titling.
3. Score each page in ZeroGPT and fill in the seven open reports under
   `.claude/skills/humanizer/reports/`.

## Tooling

`tools/build-docx.js` converts any of these markdown articles to a formatted
Word file:

```
cd tools && npm install && cd ..      # once; installs the docx package
node tools/build-docx.js <source.md> <output.docx> [--creator "Team name"]
```

It maps H1/H2/H3 to real Word heading styles, keeps hyperlinks live, renders
bullets and numbered lists through proper numbering configs, converts pipe
tables to Word tables, and handles image slots two ways: a local path
(relative to the markdown file) is embedded as the real picture; a remote URL
gets a sized placeholder frame from `tools/placeholders/` plus an instruction
line. Either way the caption beneath is the words "Image Source", hyperlinked
to the URL on the following `[Image Source](url)` line. HTML comments in the
markdown render as italic editor notes so a refresh draft can mark what is
new and what was changed.

`tools/extract-new-copy.py <page.md>` prints only the copy between
`<!-- NEW SECTION START -->` and `<!-- NEW SECTION END -->` markers, for the
case where new sections are delivered into an unchanged page and need gating
on their own.

`tools/count-words.py <page.md> [--min 500 --max 700]` counts the words a
client counts (headings, body, list items, table cells) and skips editor
notes, image lines, "Image Source" captions and the disclaimer. Exit code 1
when a file is outside the range, so it runs beside the detector gates.

`--no-notes` leaves the HTML-comment editor notes out of the Word file and
`--no-alt` keeps alt text in the image attribute instead of printing it, which
is how the Hero FinCorp files were built so nothing in them counts against the
client's length rule.

Note: LibreOffice in this environment cannot open any .docx, including the
client's own brand guide file, so output is verified by parsing the packed XML
rather than by rendering.

## Skill: humanizer v3.0.1

`.claude/skills/humanizer/`

3.0.1 (2026-09-17) is a measurement fix plus findings, no threshold changes:
`strip_markdown()` now removes list markers and HTML comments before sentence
splitting, because consecutive bullets were being measured as one sentence.
Five open reports for the Hero FinCorp pages sit in `reports/`, three
self-observed candidate patterns are logged, and the known-conflicts table
gained a row for competitor reference layouts. Details in
`references/learning-log.md`.

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
