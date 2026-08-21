# AEO/SEO checklist - How Long Can a Facebook Reel Be?

Status against `AEOSEO_Checklist_1.xlsx`. `[x]` done in this repo, `[~]` done as
far as it can be without CMS or paid-tool access, `[ ]` genuinely outstanding
and owned by whoever publishes.

## 1. Before you write

- [~] **Confirm primary keyword and check search volume in Ahrefs / Semrush** -
  keyword confirmed as "how long can a facebook reel be". No Ahrefs or Semrush
  access in this environment, so volume is unverified. Run it before publishing.
- [x] **Research People Also Ask questions** - the six FAQ entries and four of
  the H2s are drawn from the questions surfacing for this query: max length in
  2026, 3-minute Reels, minimum length, why the 90-second cap persists, whether
  length affects reach, ads length.
- [x] **Check the top 3 ranking pages** - the query is dominated by spec pages
  running roughly 900-1,600 words in table format. They give a single number and
  mostly still quote the retired 90-second cap. This draft leads with the
  corrected answer and adds the upload/in-app distinction they miss.
- [x] **Confirm CTA destination** - SocialBee 14-day free trial.

## 2. On-page SEO

- [x] Title tag includes the primary keyword and the year, 44 characters.
- [x] Meta description is 153 characters with the keyword and a value prop.
- [x] H1 mirrors the title tag.
- [x] Primary keyword in the first 100 words (third word of the short answer)
  and in the H2 "What's the Maximum Length of a Facebook Reel in 2026?".
- [x] Slug `facebook-reel-length` - short, keyword-rich, no stop words.
- [x] Descriptive alt text specified for both image slots.

## 3. Content structure (AEO)

- [x] 40-60 word direct answer at the very top (50 words).
- [x] Key Takeaways box near the top, 5 bullets.
- [x] PAA questions used as H2 and H3 subheadings throughout.
- [x] FAQ section at the bottom with 6 Q&A pairs.

## 4. Schema markup (client reference)

- [x] FAQ schema drafted in `schema.json`, mirroring the visible FAQ exactly.
- [x] Article schema drafted with author, datePublished, dateModified
  placeholders.
- [ ] HowTo schema - not applicable, this is a reference article rather than a
  step-by-step procedure.
- [ ] SoftwareApplication schema - not applicable to a blog post.

## 5. E-E-A-T and trust signals

- [ ] **Author bio with name, role and LinkedIn** - CMS-side. Placeholders are
  in `schema.json`.
- [ ] **"Last updated" date shown and kept current** - CMS-side. This article
  dates specific to a rolling Meta change, so it needs a real review cadence.
- [x] **At least one external authoritative source cited** - two, TechCrunch and
  Social Media Today.
- [x] **Avoid generic AI-sounding sentences, be specific and product-grounded** -
  scored 0.0/100 by `humanizer-evolve`, with the exact specs SocialBee's Reels
  publishing enforces rather than generic advice. See `humanizer-pass.md`.

## 6. Internal linking

- [x] 4 internal links, above the 3 minimum.
- [x] Anchors are exact or partial keyword matches; no "click here".
- [ ] **Update older posts to link here** - post-publication. Targets listed in
  `meta.md`.

## 7. GEO

- [x] **Specific citable data point** - SocialBee's Facebook Page publishing
  requirements: 4 to 90 seconds, 9:16, 540 x 960 minimum, under 512 MB,
  .MP4/.MOV. Also the dated timeline of the cap moving 30s to 60s to 90s to no
  fixed cap, which is the fact most competing pages get wrong.
- [x] **Brand name used consistently** - "SocialBee", one word, capital S and B
  throughout. Verified by grep, zero variants.
- [ ] **Test the target query in ChatGPT, Perplexity and Gemini** -
  post-publication.

## Client checklist (task brief)

- [x] Every image has a hyperlinked `Image source` line directly below it.
- [x] H1 for the title, H2 for subheadings, H3 below that.
- [x] Title and subheadings in APA title case.
- [x] No plagiarism, no fluff, no unedited AI phrasing. Every factual claim
  traces to a cited source or is marked for verification in `meta.md`.
- [~] Images uploaded to their appropriate places - slots, alt text and source
  lines are specified; the screenshot files themselves have to be captured from
  a live account.
