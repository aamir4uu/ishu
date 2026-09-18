# Refresh Notes: Working Capital Loan

- Live URL: https://www.herofincorp.com/blog/guide-understanding-working-capital-loans
- Category: existing content (refresh)
- H1: unchanged, **Working Capital Loan: Meaning, Eligibility and 2026 Application Guide**.
- Length: 1,000 words and 5,919 characters (see the 18 September update below) against the 500 to 700 brief (headings, body and tables counted; editor notes, captions and the disclaimer excluded).
- Deliverable: `Working Capital Loan - Meaning, Eligibility and 2026 Application Guide.docx`, the whole article.

## How the brief was met

The live page runs to about 1,650 words and the brief asks for two new sections and seven new FAQs. At a 700-word ceiling the mandated copy alone is close to 450 words, so the existing sections were compressed hard and the three existing FAQs dropped.

| Brief item | Delivered | Where |
| --- | --- | --- |
| New H2 "Advantages of Working Capital Loans" (100 to 120 words, keyword "benefit of working capital loan", reference Axis Bank) | 96 words, keyword in the first sentence | After "What Is a Working Capital Loan?" |
| New H2 "Key Features of a Working Capital Loan" (about 100 words, keyword "features of working capital loan", reference Ujjivan SFB) | 88 words, keyword in the first sentence | After "Advantages" |
| Seven new FAQs (calculate requirement; documents; interest rate; secured or unsecured; vs term loan; without collateral; how fast) | 22 to 45 words each | FAQ section |
| Keywords "working capital loan", "working capital loan meaning", "what is working capital loan", "working capital loan eligibility" | H1, first H2, "Eligibility and How to Apply" | |

The Ujjivan reference lays the features out as bold-label bullets. The section is a numbered list of plain sentences instead, because the bold-label-colon list is one of the surest AI tells and the no-AI requirement outranks matching a competitor's layout.

Kept, condensed: the definition, the five facility types (now one sentence), eligibility and the application steps (now one paragraph). Cut: the "Why Should You Take" bullets, the standalone types section, the long conclusion and the three existing FAQs (tenure, prepayment charges, drawing power). The prepayment answer is worth restoring if the page ever gets room, since RBI's 2025 directions changed the rule.

## Fact-check log

| Claim | Source | Status |
| --- | --- | --- |
| Hero FinCorp unsecured business loans start at 14% p.a. | herofincorp.com/business-loan-interest-rates (title in search results); Paisabazaar, Wishfin, Urban Money | **Confirm with the product team**; the site could not be opened from the drafting environment. No loan ceiling is quoted because sources disagree (Rs 40 lakh on herofincorp.com/business-loan, Rs 45 to 50 lakh on aggregators). |
| Eligibility: five years in business, three in the current one, clean credit record, industry-standard profitability | The client's live copy | Kept as given; herofincorp.com/unsecured-business-loans mentions five years, so confirm the three-year clause |
| NBFC disbursal within about two working days of complete paperwork | CreditMantri and Paisabazaar on Hero FinCorp ("48 working hours"); worded as typical | Confirmed as typical |
| CGTMSE-backed loans to micro and small enterprises need no collateral | CGTMSE scheme document CGS-I, updated 1 April 2025 | Confirmed |
| Operating cycle method and the worked example (45 + 60 − 30 = 75 days × Rs 40,000 = Rs 30 lakh) | Standard working-capital assessment; arithmetic checked | Confirmed |
| Interest on business borrowing is deductible | Income-tax Act, section 36(1)(iii) | Confirmed |

## Open items

1. Confirm the 14% starting rate.
2. Choose a banner (see `image-manifest.md`); the brief carries none.
3. The brief's "Also Read: What is Credit Purchase?" link pointed back at this same page; it was not carried over. Add the correct URL if the link is wanted.
4. Score the page in ZeroGPT and fill in `.claude/skills/humanizer/reports/2026-09-17-herofincorp-working-capital-loan.md`.

## Update, 18 September 2026: rewritten against a ZeroGPT score

The client ran this page through ZeroGPT and it came back **23.1% AI**. The brief is 15% or lower, so the page was rewritten.

Two client constraints now apply on top of the earlier brief. The article must
run to at least 5,000 characters, and it must score 15% or below. This draft
measures **1,000 words and 5,919 characters**.

The character floor and the earlier 500 to 700 word guidance cannot both hold,
since 5,000 characters is roughly 870 words of English. The floor is the newer
and more specific instruction, so the page sits near the 1,000-word ceiling the
brief allows in extreme cases.

### What changed and why

Nothing factual. Every figure, source and link survives from the previous
draft. What changed is sentence shape, because that is what the detector
highlighted. Reading the fill colour of each text run in the three report PDFs
separates flagged spans from clean ones exactly, and four shapes accounted for
almost all of them:

1. **Colon-header bullets** such as `- Term loans: a lump sum repaid in EMIs`.
   Every bullet of this shape was highlighted. Plain-sentence bullets in the
   same list were not. All bullets are now full sentences.
2. **Colon expansion in prose**, a short claim followed by a colon and a
   restatement. Rewritten as separate sentences.
3. **Semicolons welding two balanced clauses**. Replaced with full stops or
   plain conjunctions.
4. **Comma lists of four or more items**, which slipped past the existing
   rule-of-three check. Broken into shorter sentences.

Marker vocabulary was not the problem. AI marker density measured 0.0 per
1,000 words on the drafts that scored 41.6% and 37.9%.

The humanizer skill was upgraded to v3.1.0 with a gate for each of the four
shapes, so they cannot return unnoticed. This page passes all fifteen.

### Still to do

Re-score the rewritten page in ZeroGPT and record the result in
`.claude/skills/humanizer/reports/2026-09-18-herofincorp-working-capital-loan.md`.
The gates are evidence-led but they are still a proxy, and only a real score
confirms the 15% target has been met.
