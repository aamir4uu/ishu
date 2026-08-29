# Publishing Pack: What Is Collateral?

Everything the CMS needs, plus the Hero FinCorp brief and master guidelines
worked line by line.

## Metadata

| Field | Value | Check |
| --- | --- | --- |
| Meta title | What Is Collateral? Meaning, Types and How It Works | 51 chars, inside the 55 limit, primary keyword first |
| H1 | What Is Collateral? Meaning, Types and How It Works | Mirrors the meta title, APA title case |
| Meta description | Collateral is an asset you pledge to secure a loan. Learn the types, how secured and unsecured loans differ, and when a personal loan needs none. | 145 chars, inside the 155 limit, carries the primary keyword |
| URL slug | `/blog/what-is-collateral` | Short, keyword-rich, no stop words |
| Primary keyword | what is collateral (SV 5,400) | In the meta title, H1, the first sentence and one H2 |
| Secondary keywords | collateral loan meaning (480), collateral loans (2,400) | Worked into the body, not forced |
| Linking keywords | loan against property (22,200), loan against property eligibility (1,000), documents required for loan against property (720) | All three used as anchor text |
| Point of view | Second person | |
| Language | UK English | |
| CTA destination | `https://loans.apps.herofincorp.com/en/personal-loan?utm_source=website&utm_medium=organic&utm_campaign=Blogsorganic` | The UTM link the client wants in every blog |

## Word count against the brief

The brief sets a word count per section. Measured on body copy, with the H1,
image credit lines and the meta fields excluded.

| Section | Brief | Draft | |
| --- | --- | --- | --- |
| Intro | 40-50 | 43 | OK |
| What Is Collateral? | 180-200 | 212 | 6% over |
| Types of Collateral | 150-170 | 160 | OK |
| Secured Loan vs Unsecured Loan | 130-150 | 149 | OK |
| Why Do Lenders Ask for Collateral? | 90-110 | 104 | OK |
| What Happens to Collateral After Loan Repayment? | 70-90 | 97 | 8% over |
| Do Personal Loans Require Collateral? | 90-110 | 114 | 4% over |
| Frequently Asked Questions About Collateral | 150-170 | 166 | OK |
| Borrowing Without Pledging an Asset (added) | not in brief | 78 | see below |

Total body copy is roughly 1,120 words. Three sections sit 4-8% above their
ceiling. Cutting further started costing the detector gates, so they were left
as they are; each can be trimmed by a sentence if you want the numbers exact.

**Note on the totals.** Task Info gives a target length of 500-700 words, and
the master guidelines say roughly 700. The per-section counts in the brief add
up to 900-1,050 before the mandatory final CTA. The per-section brief was
treated as the governing instruction because it is the more specific one. Say
the word and the piece can be cut to 700 by dropping the FAQ block to four
questions and shortening the two explainer sections.

## The section the brief does not list

The brief ends at the FAQ block. The master guidelines require a
"Conclusion + CTA" and a "strong final CTA with UTM-tagged link", so a short
closing H2, **Borrowing Without Pledging an Asset**, was added after the FAQs to
carry it. Delete it if the client would rather end on the FAQ; the UTM link then
needs moving into the last FAQ answer.

## Master guidelines checklist

| Requirement | Status |
| --- | --- |
| Intro of 2-3 lines with a relatable problem or data point | Done. 43 words, defines the term and lands the secured/unsecured split immediately. |
| Benefit-driven H2/H3 subheadings | Done. Every H2 is a question a reader would type. |
| Bullets and short paragraphs, max 3-4 lines | Done. |
| Use cases, but not a character opener every time | Done. The ₹40 lakh example is a situation, not a named character. |
| 2-4 FAQs with crisp answers | Eight, as the brief's FAQ list specifies. Answer lengths run from 6 to 30 words. |
| Conclusion plus CTA | Done, in the added closing section. |
| Meta title under 55 chars | Done. 51. |
| Meta description under 155 chars | Done. 145. |
| Keyword in title, meta description, H1, H2, first 100 words | Done. |
| At least two internal links | Done. Six: personal loans, loan against property, LAP eligibility, LAP documents, personal loan eligibility, personal loan interest rates. |
| Final CTA with the UTM-tagged link | Done. |
| Banner image plus 1-2 in-line images | Done. Two, with hyperlinked "Image Source" captions. See `image-manifest.md`. |
| UK English, active voice, second person | Done. |
| Financial terms explained simply | Done. Valuation, charge, hypothecation and KFS are each explained in place. |
| No judgemental language about financial stress | Done. |

## Compliance check

| Rule | Status |
| --- | --- |
| No loan denial exploitation | Clean. Default is described factually, with the notice period stated. |
| No "guaranteed", "sure-shot", "zero risk" | Clean. The piece says the opposite: "None of that makes approval automatic, and you should be wary of anyone who implies it does." |
| No exaggerated promises | Clean. Every claim about terms is qualified with "subject to the lender's policy". |
| Data backed by RBI, SEBI or government sources, 2024 onwards | Two facts, both RBI. See below. |
| No internal quotes | Clean. None used. |

### The two sourced facts

1. **Original property documents must be returned within 30 days of full
   repayment or settlement, with ₹5,000 per day of compensation for delay,**
   for cases falling due from 1 December 2023. RBI directions of 13 September
   2023 on the release of movable and immovable property documents, issued to
   banks, NBFCs, HFCs, ARCs and co-operative banks. This is the one fact that
   predates the 2024 cut-off in the guidelines. It is still the rule in force
   and it is directly on the topic of the H2 it sits under, so it was kept.
   Flagging it so the desk can make the call.
2. **Key Facts Statement mandatory on all retail loans from 1 October 2024,**
   carrying the annual percentage rate and every charge. RBI circular
   RBI/2024-25/18 dated 15 April 2024.

Both should be spot-checked against rbi.org.in before publishing. Outbound
access to that domain was blocked in the environment this was written in.

## Open items before publishing

1. Confirm the primary keyword and its volume against your own keyword sheet.
   The brief gives 5,400 for "what is collateral"; that figure was taken as
   given and not independently verified.
2. Drop the two images in and re-host them. See `image-manifest.md`.
3. Add the author byline. The master guidelines want a trusted-friend voice, and
   a named human author matters for the no-AI requirement.
4. Verify both RBI facts against rbi.org.in.
5. Run the ZeroGPT check and attach the report. The brief asks for a score below
   15%. `zerogpt-preflight-result.txt` records the pre-flight gate results, which
   is not the same thing as a detector score.
6. Decide whether the added closing CTA section stays.
