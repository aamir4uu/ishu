# Publishing Pack: CIBIL Score Kya Hota Hai

Everything the CMS needs, plus the Hero FinCorp brief and master guidelines
worked line by line.

## Metadata

| Field | Value | Check |
| --- | --- | --- |
| Meta title | CIBIL Score क्या होता है? Check करने का तरीका | 45 chars, inside the 55 limit |
| H1 | CIBIL Score क्या होता है? इसे कैसे Check करें | Matches the brief's H1 exactly |
| Meta description | CIBIL Score 300 से 900 के बीच का नंबर है। जानिए अच्छा score कितना होता है, उसे प्रभावित करने वाले factors और उसे मुफ्त में check करने का तरीका। | 143 chars, inside the 155 limit |
| URL slug | `/blog/cibil-score-kya-hota-hai` | Matches the primary keyword transliteration |
| Primary keyword | cibil score kya hota hai (SV 5,400) | In the H1, the meta title and the first sentence |
| Secondary keywords | cibil score kya hai (880), cibil ka matlab (170) | "Cibil ka matlab" opens the second paragraph of the first H2 |
| Linking keywords | CIBIL score check kaise kare (590), CIBIL score range (9,900) | Both used as anchor text on Hero FinCorp pages |
| Point of view | Second person | |
| Language | Hindi in Devanagari with English financial terms in Latin, matching the brief's own register and the H1 | |
| CTA destination | `https://loans.apps.herofincorp.com/en/personal-loan?utm_source=website&utm_medium=organic&utm_campaign=Blogsorganic` | |

## Keyword transliteration

The keyword sheet is in Roman script and the article is in Devanagari. Both
forms are carried: the Devanagari rendering in the H1 and headings for readers,
and the Roman form once in the body ("Cibil ka matlab") and in the slug for the
transliterated query. That covers the search both ways without stuffing.

## Word count against the brief

Measured on body copy, with the H1, image credit lines and meta fields excluded.

| Section | Brief | Draft | |
| --- | --- | --- | --- |
| Intro | 40-50 | 53 | 6% over |
| CIBIL Score क्या होता है और अच्छा Score कितना माना जाता है? | 180-200 | 190 | OK |
| Personal Loan के लिए CIBIL Score क्यों जरूरी है? | 100-120 | 124 | 3% over |
| CIBIL Score को प्रभावित करने वाले कारक | 110-130 | 134 | 3% over |
| CIBIL Score कैसे सुधारें और कैसे Check करें? | 160-180 | 185 | 3% over |
| CIBIL Score और CIBIL Report में क्या अंतर है? | 80-100 | 96 | OK |
| क्या CIBIL Score Personal Loan की Eligibility को प्रभावित करता है? | 90-110 | 110 | OK |
| अक्सर पूछे जाने वाले सवाल | 130-150 | 162 | 8% over |
| अगला कदम (added) | not in brief | 40 | see below |

Total body copy is roughly 1,090 words. Everything sits within 8% of its
ceiling.

**Note on the totals.** Task Info gives 500-700 words and the master guidelines
say roughly 700, while the brief's own per-section counts add up to 890-1,040.
The per-section brief was followed because it is the more specific instruction.
The piece can be cut to 700 by halving the FAQ block and shortening the factors
section.

## The section the brief does not list

**अगला कदम** was added after the FAQs to carry the mandatory final CTA with the
UTM link, which the master guidelines require and the brief's outline has no
slot for. Remove it if you would rather end on the FAQ block.

## Structural requirements from the brief

| Requirement | Status |
| --- | --- |
| 300-900 range in a table with the four bands | Done. Poor, Fair, Good, Excellent, exactly as briefed. |
| State that score alone is not an approval guarantee | Done, twice. Income, employment and existing EMIs are named both times. |
| Higher score may mean better terms, subject to lender policy | Done, with the qualifier attached. |
| Five H3 factors under the factors H2 | Done. Repayment history, credit utilisation, credit mix, multiple applications, length of history. |
| Improve tips plus check process in one H2 | Done. Bullet list for the tips, prose for the check and dispute steps. |
| Advice to raise a dispute on wrong information | Done, naming both the lender and the bureau route. |
| Score vs Report comparison table | Done. Three rows. |
| Internal links to पर्सनल लोन पात्रता कैलकुलेटर and पर्सनल लोन | Done, in the eligibility H2 as the brief specifies. |
| Seven FAQs | Done, all seven from the brief, in order. |

## Master guidelines checklist

| Requirement | Status |
| --- | --- |
| Intro of 2-3 lines | Done. 53 words. |
| Short paragraphs, bullets, scannable | Done. |
| Friendly, conversational, credible tone | Done. |
| Financial terms explained simply | Done. Soft and hard enquiry, credit utilisation and moratorium-free unsecured lending are each explained in place. |
| No judgemental language about financial stress | Done. A low score is described as recoverable, never as a failing. |
| Meta title under 55 chars | Done. 45. |
| Meta description under 155 chars | Done. 143. |
| At least two internal links | Done. Five. |
| Final CTA with the UTM link | Done. |
| Banner plus in-line image | Done. Two, with hyperlinked "Image Source" captions. |

## Compliance check

| Rule | Status |
| --- | --- |
| No loan denial exploitation | Clean. |
| No "guaranteed", "sure-shot", "zero risk" | Clean. The article states plainly that a high score is not an approval guarantee. |
| No exaggerated promises | Clean. Every terms claim is tied to lender policy. |
| Data backed by RBI or government sources, 2024 onwards | Two RBI facts, both 2024. See below. |
| No internal quotes | Clean. |

### The two sourced facts

1. **Fortnightly credit reporting from 1 January 2025.** Lenders must report on
   the 15th and the last day of each month. RBI circular
   DoR.FIN.REC.No.32/2024-25 dated 8 August 2024.
2. **Key Facts Statement mandatory on retail loans from 1 October 2024.** RBI
   circular RBI/2024-25/18 dated 15 April 2024.

The article also states that every RBI-registered bureau owes you one free full
report a year, and that four bureaus operate in India. Both are long-standing
positions rather than 2024 rulings, so they are stated without a date.

Spot-check all of it against rbi.org.in before publishing. Outbound access to
that domain was blocked in the environment this was written in.

## Detector status

**Run ZeroGPT on `detector-paste.txt`, not on the .docx.** The Word file carries
scaffolding a published page never shows: the meta title and description lines,
image placeholder frames, alt-text lines and "Image Source" captions. When the
education loan piece was tested, all of that went into the detector along with
the copy, roughly 330 words of it, including one English boilerplate sentence
repeated verbatim. `detector-paste.txt` is the published article and nothing
else. Regenerate it after any edit:

```
python3 tools/detector-paste.py blog/<slug>/<slug>.md
```

**If the result comes back high, send the highlights, not just the number.** The
report we received was printed with background graphics turned off, which
silently drops every highlight ZeroGPT draws. That leaves a percentage and no
way to tell which sentences caused it. Tick "Background graphics" in the browser
print dialog, or send a screenshot of the result panel.

**Before rewriting anything on a bad Hindi score, run the control.** Paste a
Hero FinCorp Hindi blog post that is already live and was written by a person,
for example `https://www.herofincorp.com/blog/herofincorp-loan-status-check-karen`,
into the same tool. If your own published Hindi scores 80% or more, the problem
is the detector's handling of Hindi rather than this draft, and the under-15%
acceptance criterion needs discussing before more time goes into rewrites. This
takes about a minute and it decides whether any further editing is worth doing.

## Open items before publishing

1. Confirm the keyword volumes against your own sheet.
2. Drop the two images in and re-host them. See `image-manifest.md`.
3. Add a named author byline.
4. Verify both RBI circulars.
5. Run ZeroGPT on `detector-paste.txt` and attach the report, target under 15%.
6. Decide whether the added closing section stays.
7. **Detector note for the Hindi pieces:** the pre-flight contraction gate does
   not apply to Devanagari and is reported as N/A. Ten of the eleven gates were
   measured and passed. See `zerogpt-preflight-result.txt`.
