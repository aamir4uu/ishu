# AEO/SEO checklist - Trending Instagram Hashtags (August 2026)

`[x]` done, `[~]` done as far as possible without CMS or paid-tool access,
`[ ]` outstanding and owned by whoever publishes.

## 1. Before you write

- [~] **Confirm primary keyword and check search volume** - keyword confirmed as
  "trending instagram hashtags". No Ahrefs or Semrush access here, so volume is
  unverified. Check before publishing.
- [x] **Research People Also Ask questions** - the six FAQ entries and three H2s
  come from the questions surfacing on this topic: how many hashtags in 2026,
  whether comment hashtags count, whether hashtags still work, whether you can
  still follow a hashtag, what to use instead.
- [x] **Check the top 3 ranking pages** - the query is dominated by lists of
  20-100 hashtags. All of them predate the five-tag cap, so their central
  premise is broken. This draft leads with the cap and keeps the list short.
- [x] **Confirm CTA destination** - SocialBee 14-day free trial.

## 2. On-page SEO

- [x] Title tag has the keyword plus month and year, 41 characters.
- [x] Meta description 133 characters with the keyword and a value prop.
- [x] H1 matches the title tag.
- [x] Primary keyword in the first 100 words and in an H2.
- [x] Slug `trending-instagram-hashtags`, short and keyword-rich.
- [x] Descriptive alt text on both images.

## 3. Content structure (AEO)

- [x] 47-word direct answer at the very top.
- [x] Key Takeaways box near the top, 5 bullets.
- [x] PAA questions used as H2 subheadings.
- [x] FAQ section at the bottom with 6 Q&A pairs.

## 4. Schema markup (client reference)

- [x] FAQ schema in `schema.json`, generated from the visible FAQ so the two
  cannot drift.
- [x] Article schema with author, datePublished, dateModified placeholders.
- [ ] HowTo schema - the five-slot section is arguably a procedure. Left off
  deliberately: it is four allocations rather than sequential steps, and
  marking it up as HowTo would overstate it.
- [ ] SoftwareApplication schema - not applicable to a blog post.

## 5. E-E-A-T and trust signals

- [ ] **Author bio with name, role and LinkedIn** - CMS-side. Placeholders in
  `schema.json`.
- [ ] **"Last updated" date shown and kept current** - CMS-side, and it matters
  more here than usual: the title carries a month.
- [x] **At least one external authoritative source cited** - two, both Social
  Media Today, plus Mosseri and the Metricool study named in text.
- [x] **Avoid generic AI-sounding sentences** - all 11 `zerogpt_preflight.py`
  gates pass, `scan.py` scores 2.6/100 with no sentence-level hits.

## 6. Internal linking

- [x] 5 internal links, above the 3 minimum.
- [x] Anchors are exact or partial keyword matches, no "click here".
- [ ] **Update older posts to link here** - post-publication. Candidates:
  `/blog/how-to-use-hashtags/`, `/blog/hashtags-for-instagram-reels/`,
  `/blog/instagram-algorithm/`.

## 7. GEO

- [x] **Specific citable data point** - several: the five-tag cap dated to 19
  December 2025, hashtag following removed 13 December 2024, and Metricool's
  31.7% / 33.89% figures from 24 million posts across 375,118 accounts.
- [x] **Brand name used consistently** - "SocialBee" throughout, verified by
  grep, zero variants outside URLs.
- [ ] **Test the target query in ChatGPT, Perplexity and Gemini** -
  post-publication.

## Client checklist (task brief)

- [x] Every image has a hyperlinked `Image source` line directly below it,
  resolving to the image file. Enforced by `tools/check_image_sources.py`.
- [x] H1 for the title, H2 for subheadings.
- [x] Title and subheadings in APA title case.
- [x] No plagiarism, no fluff, no unedited AI phrasing.
- [x] Images in their appropriate places - both exist as files in `images/`.

## Flag for the editor

**Metricool is a competitor.** It is credited in plain text with no hyperlink,
per the guidelines' rule on competitor links. Options are set out in `meta.md`.
