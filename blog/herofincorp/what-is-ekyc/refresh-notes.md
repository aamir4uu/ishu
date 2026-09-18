# Refresh Notes: What Is e-KYC

- Live URL: https://www.herofincorp.com/blog/what-is-ekyc
- Category: existing content (refresh)
- H1: unchanged, **E-KYC: Meaning, Full Form, Types, Process, and Eligibility**.
- Length: 999 words and 5,682 characters (see the 18 September update below) against the 500 to 700 brief (headings, body and tables counted; editor notes, captions and the disclaimer excluded).
- Deliverable: `E-KYC - Meaning, Full Form, Types, Process, and Eligibility.docx`, the whole article.

## How the brief was met

The live page runs to about 1,800 words; the brief asks for two new H3s, two new H2s and four new FAQs, which is roughly 420 words of mandated copy. The rest of the page was condensed to fit under 700.

| Brief item | Delivered | Where |
| --- | --- | --- |
| New H3 "Offline e-KYC" (about 50 words, keyword "ekyc meaning") | 53 words | Types section, third |
| New H3 "Video KYC" (about 50 words) | 59 words | Types section, fourth |
| New H2 "e-KYC Process Explained Step by Step" (numbered, about 100 words, keyword "ekyc process") | 84 words, keyword in the first sentence | After eligibility |
| New H2 "How to Apply for e-KYC Online" (steps, about 120 words, keyword "how to apply ekyc online") | 104 words, keyword in the first sentence | After the process section |
| Four new FAQs (full form; Aadhaar e-KYC vs Video KYC; why it fails; is it mandatory) | 30 to 45 words each | FAQ section |
| Keywords "e kyc online", "e kyc full form", "ekyc means", "what is ekyc" | H1, "What Is e-KYC?", the two new H2s | |

The brief's generic "e-KYC Process" H2 sat right above the existing "How to Complete e-KYC for a Personal Loan" list. Only the new one survives, written as the Aadhaar mechanics (consent, challenge, what UIDAI returns, CKYC), so the page doesn't carry two near-identical lists. The Axis reference for "How to Apply" describes the KRA route for mutual funds; the section leads with the lender route and gives the KRA route in one line.

Kept, condensed: Neha's opening, the definition, OTP and biometric e-KYC, eligibility. Cut: the traditional-vs-e-KYC table, the "core pillars" bullets, the advantages and security sections, the Hero FinCorp product bullets (the eligibility line now carries the loan range), the conclusion and the four existing FAQs.

## Corrections to the live copy

- **Personal loan ceiling**: the live copy says Rs 5 lakh; herofincorp.com/personal-loans says "Upto Rs. 7 Lakh". The draft says Rs 7 lakh. Confirm with the product team.
- "At its core", "leverages", "robust framework", "revolutionized", "empowers" and the "not just X, it's Y" shapes are gone with the cut.

## Fact-check log

| Claim | Source | Status |
| --- | --- | --- |
| Offline e-KYC: signed XML from myaadhaar.uidai.gov.in, four-digit share code, reference ID rather than the Aadhaar number, verified offline | UIDAI, "Aadhaar Paperless Offline e-KYC" | Confirmed |
| Video KYC: live, recorded, PAN on camera, face match, geotagging, under RBI's V-CIP rules | RBI KYC Master Direction; HyperVerge and IDfy summaries | Confirmed |
| OTP-only e-KYC accounts: term loans capped at Rs 60,000 a year | RBI KYC Master Direction, section 17 (OTP-based e-KYC in non-face-to-face mode) | Confirmed |
| UIDAI returns name, date of birth, gender, address and photo, never biometrics | UIDAI e-KYC API specification | Confirmed |
| CKYC identifier; KRAs (CVL KRA, CAMS KRA) | CERSAI CKYC rules; SEBI KRA regulations | Confirmed |
| Hero FinCorp personal loan: Rs 50,000 to Rs 7 lakh, 12 to 36 months, minimum age 21, minimum income Rs 15,000, CIBIL 725 | herofincorp.com/personal-loans (title and snippet); Paisabazaar; the client's live copy for 725 | Ceiling updated; the rest matches the live copy. **Confirm with the product team.** |

## Open items

1. Confirm the Rs 7 lakh ceiling and the 725 CIBIL figure.
2. Score the page in ZeroGPT and fill in `.claude/skills/humanizer/reports/2026-09-17-herofincorp-what-is-ekyc.md`.

## Update, 18 September 2026: rewritten against a ZeroGPT score

The client ran this page through ZeroGPT and it came back **37.9% AI**. The brief is 15% or lower, so the page was rewritten.

Two client constraints now apply on top of the earlier brief. The article must
run to at least 5,000 characters, and it must score 15% or below. This draft
measures **999 words and 5,682 characters**.

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
`.claude/skills/humanizer/reports/2026-09-18-herofincorp-what-is-ekyc.md`.
The gates are evidence-led but they are still a proxy, and only a real score
confirms the 15% target has been met.
