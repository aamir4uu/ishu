# Publishing metadata

## Core fields

| Field | Value | Check |
| --- | --- | --- |
| Primary keyword | how long can a facebook reel be | — |
| Secondary keywords | facebook reel length, facebook reel length limit, facebook reels max length, facebook reel specs | — |
| Title tag | How Long Can a Facebook Reel Be? 2026 Limits | 44 chars, under 60, keyword + year |
| Meta description | Facebook Reels no longer stop at 90 seconds. Get the 2026 length limits, the specs to check before you post, and the run times that actually get watched. | 153 chars, in the 150-160 band |
| URL slug | `facebook-reel-length` | Short, keyword-rich, no stop words |
| H1 | How Long Can a Facebook Reel Be? 2026 Limits and Best Run Times | Mirrors the title tag |
| Word count | 1,285 total / 1,017 prose (preflight count) | Brief: 800-1,000, +25% tolerance approved |
| Point of view | Second person | Per brief |
| Structure | Subheads, APA title case | Per brief and checklist |

Primary keyword placement: appears in the H1, in the first sentence of the
short answer (word 3), in the H2 "What's the Maximum Length of a Facebook Reel
in 2026?", and in the FAQ heading.

## Images

Three images. Full detail, sources and capture instructions are in
`image-manifest.md`; the assets themselves are in `images/`.

| Slot | File | Alt text | Source | Status |
| --- | --- | --- | --- | --- |
| 1 | `images/facebook-reel-length-limits-2021-2026.png` | Bar chart of the maximum Facebook Reel length from 2021 to 2026, rising from 30 seconds to 90 seconds and then to no fixed cap | Original SocialBee chart; data from TechCrunch and Social Media Today | In the repo |
| 2 | `images/facebook-reels-composer-timer.png` | The Facebook Reels composer with the 90-second recording timer visible above the record button | https://www.facebook.com/ | To capture |
| 3 | `images/socialbee-facebook-reel-scheduled.png` | A Facebook Reel scheduled inside the SocialBee post editor with the preview panel open | https://socialbee.com/ | To capture |

Every image carries a hyperlinked `Image source` line directly beneath it, and
text always sits between a heading and an image. No stock photography, per the
brand guidelines.

## Deliverables

| File | What it is |
| --- | --- |
| `facebook-reel-length.md` | The draft, source of truth |
| `How Long Can a Facebook Reel Be - 2026 Limits and Best Run Times.docx` | Word version, generated from the markdown by `tools/md_to_docx.py` |
| `image-manifest.md` | Every image, its source, and what still needs capturing |
| `images/` | The image assets and the script that generates the chart |
| `schema.json` | Article and FAQPage JSON-LD |
| `aeo-seo-checklist.md` | The checklist, marked up |
| `humanizer-pass.md` | Detector passes and scores |

Regenerate the .docx after any edit to the markdown:

```bash
python3 tools/md_to_docx.py blog/facebook-reel-length/facebook-reel-length.md \
  "blog/facebook-reel-length/How Long Can a Facebook Reel Be - 2026 Limits and Best Run Times.docx"
```

## Links

Internal (4, exceeds the 3 minimum), all partial or exact match anchors:

| Anchor | Target | Placement |
| --- | --- | --- |
| free social media resources | https://socialbee.com/resources/ | Early touchpoint, downloadable resource |
| Facebook algorithm | https://socialbee.com/blog/facebook-algorithm/ | Reach section |
| social media video sizes | https://socialbee.com/blog/social-media-video-sizes/ | Specs section |
| how to schedule Reels on Facebook | https://socialbee.com/blog/can-you-schedule-reels-on-facebook/ | Feature section |

External authoritative sources (both DA 65+, no competitors linked):

- TechCrunch, March 2023, on the expansion to 90 seconds
- Social Media Today, June 2025, on all Facebook videos becoming Reels

Older posts to update with a link to this article once live:
`/blog/facebook-reels/`, `/blog/can-you-schedule-reels-on-facebook/`,
`/blog/social-media-video-sizes/`.

## SocialBee touchpoints

1. **Early** - free social media resources link in the minimum-length section.
2. **Middle** - "How to Schedule Facebook Reels With SocialBee", tied to Reels
   direct publishing and content categories.
3. **End** - 14-day free trial CTA in the conclusion.

## Schema markup (client reference)

Article and FAQPage JSON-LD are in `schema.json`. The FAQ entities mirror the
six on-page Q&A pairs exactly; do not publish the schema without the visible
FAQ section.

## Facts to re-verify before publishing

Meta ships changes to this quietly and the rollout is staggered by account, so
confirm against a live account rather than against this draft:

1. Whether the in-app Reels camera still caps at 90 seconds on the account you
   are publishing from. The article states 90 seconds "on most accounts".
2. That the no-fixed-maximum upload behaviour has reached the publishing
   account.
3. SocialBee's current direct-publishing floor and ceiling (stated as 4-90
   seconds, 9:16, 540 x 960 minimum, 512 MB, .MP4/.MOV) against the live help
   documentation.
