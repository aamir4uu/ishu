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

Every `Image source` link is a deep link to the exact page or file the image
comes from. A link to a site's front page is not a source; it satisfies the
wording of the checklist and none of its point.

| # | File | Placement | Alt text | Exact source link | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | `images/facebook-reel-length-limits-2021-2026.png` | After the opening paragraph of "What's the Maximum Length of a Facebook Reel in 2026?" | Bar chart of the maximum Facebook Reel length from 2021 to 2026, rising from 30 seconds to 90 seconds and then to no fixed cap | [the image file itself](https://github.com/aamir4uu/ishu/blob/claude/facebook-reel-length-post-5fl797/blog/facebook-reel-length/images/facebook-reel-length-limits-2021-2026.png) | **Done.** 1200x700 PNG, in the repo |
| 2 | `images/facebook-reels-composer-timer.png` | End of "Reels Recorded in the App: 90 Seconds" | The Facebook Reels composer with the 90-second recording timer visible above the record button | [Create a reel on Facebook, Facebook Help Center](https://www.facebook.com/help/2862139500770200) | **To capture** |
| 3 | `images/socialbee-facebook-reel-scheduled.png` | After the opening paragraph of "Facebook Reel Specs to Check Before You Post" | A Facebook Reel scheduled inside the SocialBee post editor with the preview panel open | [How to schedule and post Reels on Facebook, SocialBee Help](https://help.socialbee.com/hc/en-us/articles/29979081550487-How-to-schedule-and-post-Reels-on-Facebook) | **To capture** |

Alt text carries the keyword where it reads naturally, per checklist item 2.6.
Images 1 and 2 name Facebook Reel length directly. Image 3 describes what is in
the frame instead, because forcing the keyword into a screenshot caption would
read as stuffing.

### What each source link has to become at publish time

The rule is that clicking `Image source` lands you on the image, or failing
that, on the exact screen the image was taken from. Never on a front page.

| # | Now | At publish |
| --- | --- | --- |
| 1 | The PNG in this repo | The direct file URL of the uploaded asset, e.g. `https://socialbee.com/wp-content/uploads/.../facebook-reel-length-limits-2021-2026.webp` |
| 2 | The Facebook help article that documents that exact screen | Unchanged. It is a screenshot of Facebook's own UI, so the help article is the correct attribution |
| 3 | The SocialBee help article that documents that exact screen | Unchanged, for the same reason |

Image 1 is the only one that has to change, because it is the only one whose
"source" is a file rather than a product screen. Once the chart is uploaded,
swap the link for the asset's own URL.

### Checking this automatically

```bash
python3 tools/check_image_sources.py blog/facebook-reel-length/facebook-reel-length.md
```

Fails the build if any image is missing alt text, missing its `Image source`
line, sitting directly under a heading, or pointing at a bare domain or at the
article's own page. It was written after exactly those last two mistakes
shipped in an earlier draft.

## Image 1: the chart

Original work, so there is no external licence to clear. It is reproducible:

```bash
python3 images/make_chart.py
```

`make_chart.py` is in the repo alongside the output. The figures it plots are
the ones cited in the article body, and both sources are named in the chart's
own footer so the credit survives if the image is reshared on its own.

Its `Image source` link points at the image file, not at the article that
contains it. That is the whole point of the line: it should take you to the
photo. Replace it with the uploaded asset's direct URL once the chart is in the
media library.

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
