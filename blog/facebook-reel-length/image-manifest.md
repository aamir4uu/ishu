# Image Manifest

Three images: one chart that exists, and two screenshots your team captures.

## Why the split is one chart and two screenshots

The brand guidelines mention charts exactly once, in a single word, inside a
Don't about stock photography:

> Use stock photos, use screenshots, charts, and original visuals only.

They ask for screenshots three separate times:

> Include real examples, case studies, and screenshots, especially of SocialBee
> in action.

> Follow with a relevant screenshot, caption, and CTA.

> [AI Post Generator] a feature worth referencing and screenshotting in
> relevant articles.

So charts are permitted, never requested. An earlier draft of this article
carried three charts and no screenshots, which inverted that emphasis. It now
carries one chart and two screenshots.

The chart that stayed plots dated figures from two cited sources, which is the
citable data point the GEO checklist asks for, and it shows a value that
changed four times over five years. No screenshot can show that. The two charts
that were cut restated things the body text and the specs table already said.

## The images

| # | File | Placement | Alt text | Image source | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | `facebook-reels-composer-timer.png` | End of "Reels Recorded in the App: 90 Seconds", after the text | The Facebook Reels composer with the 90-second recording timer visible above the record button | pending capture | **To capture** |
| 2 | `facebook-reel-length-limits-2021-2026.png` | After the TechCrunch and Social Media Today citations, in "Uploaded Reels: No Fixed Cap" | Bar chart of the maximum Facebook Reel length from 2021 to 2026, rising from 30 seconds to 90 seconds and then to no fixed cap | [.png file](https://raw.githubusercontent.com/aamir4uu/ishu/refs/heads/claude/facebook-reel-length-post-5fl797/blog/facebook-reel-length/images/facebook-reel-length-limits-2021-2026.png) | **Done**, 1200x700 |
| 3 | `socialbee-facebook-reel-scheduled.png` | In "How to Schedule Facebook Reels With SocialBee", before the walkthrough link | A 45-second Facebook Reel scheduled in the SocialBee post editor, with the preview panel and content category selector visible | pending capture | **To capture** |

Image 3 sits where the brand guidelines want it. Section 6 describes the
promotion pattern as context, then a natural transition, then "a relevant
screenshot, caption, and CTA". That is exactly the shape of that section.

Text always sits between a heading and an image. Alt text carries the keyword
where it reads naturally; image 3 describes the frame instead, because forcing
"Facebook Reel length" into a screenshot caption would read as stuffing.

## Capturing images 1 and 3

Neither could be captured here. Both need a logged-in account, and this
environment blocks facebook.com and socialbee.com outright.

For each one:

1. Reproduce the state described in the alt text. For image 1 that is the
   Reels composer with the timer showing. For image 3, a real Reel of about 45
   seconds queued in the post editor with the preview panel open and a content
   category selected, so the screenshot shows the feature the paragraph above
   it describes.
2. Capture at 1200px wide or better. Crop to the relevant panel. Do not
   screenshot a whole desktop.
3. Blur or replace any real account name, profile photo, or client data.
4. Save into `images/` under the exact filename in the table above, so the
   existing reference in the draft resolves with no edit.
5. Replace the pending line beneath it with a normal source line pointing at
   the uploaded image file:
   `*[Image source](https://socialbee.com/wp-content/uploads/.../file.webp)*`
6. Re-run the check below.

## The chart

Reproducible, so it can be corrected without a design tool:

```bash
python3 images/make_images.py
```

Requires Pillow. It plots the figures cited in the article body, and repeats
both sources in the figure's own footer so the credit survives if the image is
reshared on its own.

## Source links: the rule

Clicking `Image source` has to show you the image. Not a page containing it,
not the article, not a help centre entry, not a site's front page. Earlier
drafts got this wrong twice, first with bare domains and then with deep links
that were still web pages.

A slot awaiting a screenshot says so, rather than carrying a link that does not
lead to an image:

```
*Image source: pending capture, see image-manifest.md*
```

Check both rules at once:

```bash
python3 tools/check_image_sources.py blog/facebook-reel-length/facebook-reel-length.md
python3 tools/check_image_sources.py blog/facebook-reel-length/facebook-reel-length.md --strict
```

The plain run fails on a missing file, missing alt text, a malformed source
line, a bare domain, a link to the article's own page, a URL that is not an
image file, and a GitHub `/blob/` viewer URL. It reports pending slots without
failing. **Run it with `--strict` before handing the draft to a publisher**;
pending slots then fail, so an uncaptured screenshot cannot ship unnoticed.

**One caveat on the chart's link.** It points at `raw.githubusercontent.com`,
which serves the actual PNG bytes. This repository is private, so that URL
needs a GitHub token and will not open in a plain browser session. Replace it
with the uploaded asset's own URL at publish, the same as images 1 and 3.

## Before upload

- Convert to WebP and compress. Target under 150KB each at 1200px wide. The
  chart is 101KB as PNG.
- Set explicit width and height so images do not shift layout while the page
  loads. The chart is 1200x700.
- Re-run `check_image_sources.py --strict` after the CMS import. Source
  formatting is the thing most often lost in a paste.
