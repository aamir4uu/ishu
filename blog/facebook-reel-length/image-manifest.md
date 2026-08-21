# Image Manifest

Three images. Each sits in the draft with descriptive alt text and an "Image
source" line directly beneath it, hyperlinked, as the checklist requires. Text
always sits between a heading and an image, per the brand guidelines.

All assets and their sources live in one folder: `images/`.

## Why there is no stock photography here

The other article in this repo sourced its images from Pexels. This one does
not, deliberately. SocialBee's content guidelines say it plainly under Don't:

> Use stock photos, use screenshots, charts, and original visuals only.

So image 1 is an original chart drawn from the sourced figures, and images 2 and
3 are product screenshots that have to be captured from live accounts. A Pexels
photo of someone holding a phone would break the brand rule and add nothing.

## The images

| # | File | Placement | Alt text | Source | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | `images/facebook-reel-length-limits-2021-2026.png` | After the opening paragraph of "What's the Maximum Length of a Facebook Reel in 2026?" | Bar chart of the maximum Facebook Reel length from 2021 to 2026, rising from 30 seconds to 90 seconds and then to no fixed cap | Original SocialBee chart. Data from TechCrunch (March 2023) and Social Media Today (June 2025) | **Done.** 1200x700 PNG, in the repo |
| 2 | `images/facebook-reels-composer-timer.png` | End of "Reels Recorded in the App: 90 Seconds" | The Facebook Reels composer with the 90-second recording timer visible above the record button | https://www.facebook.com/ | **To capture** |
| 3 | `images/socialbee-facebook-reel-scheduled.png` | After the opening paragraph of "Facebook Reel Specs to Check Before You Post" | A Facebook Reel scheduled inside the SocialBee post editor with the preview panel open | https://socialbee.com/ | **To capture** |

Alt text carries the keyword where it reads naturally, per checklist item 2.6.
Images 1 and 2 name Facebook Reel length directly. Image 3 describes what is in
the frame instead, because forcing the keyword into a screenshot caption would
read as stuffing.

## Image 1: the chart

Original work, so there is no external licence to clear. It is reproducible:

```bash
python3 images/make_chart.py
```

`make_chart.py` is in the repo alongside the output. The figures it plots are
the ones cited in the article body, and both sources are named in the chart's
own footer so the credit survives if the image is reshared on its own.

The `Image source` link under it points at the article's own URL, which is the
convention for an original graphic. Update that URL if the published slug
differs from `facebook-reel-length`.

## Images 2 and 3: what still needs doing

Both are product screenshots. Neither could be captured here: this draft was
produced in a sandboxed environment where `facebook.com` and `socialbee.com`
are both blocked by the network egress policy, and neither product can be
screenshotted without a logged-in session anyway.

For each one:

1. Open the product and reproduce the state described in the alt text.
2. Capture at 1200px wide or better. Crop to the relevant panel; do not
   screenshot a whole desktop.
3. Blur or replace any real account name, profile photo, or client data.
4. Save into `images/` under the exact filename in the table above, so the
   `![...]()` reference in the draft resolves with no edit.
5. Leave the `Image source` line beneath it untouched.

## Before upload

- Convert to WebP and compress. Target under 150KB each at 1200px wide. The
  chart is currently 101KB as PNG, which is fine, but WebP will roughly halve it.
- Set explicit width and height attributes so images do not shift layout while
  the page loads.
- Re-check that every image still has its hyperlinked `Image source` line after
  the CMS import. That formatting is the item most often lost in a paste.
