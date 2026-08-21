# Image Manifest

Three images. All three are real files in `images/`, all three are original
graphics, and every `Image source` link points straight at an image file.

## Why all three are original

SocialBee's content guidelines say it plainly under Don't:

> Use stock photos, use screenshots, charts, and original visuals only.

That rules out Pexels, which is what the other article in this repo used. It
leaves screenshots and original graphics. Product screenshots have to be
captured from a logged-in Facebook and SocialBee account, which was not
possible here, and an earlier draft carried them as placeholders with source
links pointing at help articles. A help article is a web page, not an image, so
those slots were replaced with charts that carry the same information and
actually exist.

## The images

| # | File | Placement | Alt text | Image source link |
| --- | --- | --- | --- | --- |
| 1 | `facebook-reel-upload-vs-in-app-limits.png` | After the paragraph stating the two limits, in "What's the Maximum Length of a Facebook Reel in 2026?" | Diagram comparing the two Facebook Reel length limits: an uploaded file has no fixed maximum, while recording in the app stops at 90 seconds | [.png file](https://raw.githubusercontent.com/aamir4uu/ishu/refs/heads/claude/facebook-reel-length-post-5fl797/blog/facebook-reel-length/images/facebook-reel-upload-vs-in-app-limits.png) |
| 2 | `facebook-reel-length-limits-2021-2026.png` | After the TechCrunch and Social Media Today citations, in "Uploaded Reels: No Fixed Cap" | Bar chart of the maximum Facebook Reel length from 2021 to 2026, rising from 30 seconds to 90 seconds and then to no fixed cap | [.png file](https://raw.githubusercontent.com/aamir4uu/ishu/refs/heads/claude/facebook-reel-length-post-5fl797/blog/facebook-reel-length/images/facebook-reel-length-limits-2021-2026.png) |
| 3 | `facebook-reel-length-by-content-type.png` | After the padding paragraph, in "How Long Should a Facebook Reel Be?" | Chart of recommended Facebook Reel length by content type, with hooks at 7 to 15 seconds, demos at 30 to 60 seconds and explainers at 60 to 180 seconds | [.png file](https://raw.githubusercontent.com/aamir4uu/ishu/refs/heads/claude/facebook-reel-length-post-5fl797/blog/facebook-reel-length/images/facebook-reel-length-by-content-type.png) |

Each one sits in the section it explains rather than decorating a heading, and
text always comes between the heading and the image.

Alt text carries the keyword where it reads naturally, per checklist item 2.6.
All three name Facebook Reel length directly, because all three are about it.

## What each image shows

**1. Upload versus in-app recording.** Two cards, green and red, carrying the
distinction the whole article turns on: an uploaded file has no fixed maximum
since June 2025, while the in-app timer still stops at 90 seconds. Footer
carries the 3-second minimum and SocialBee's 4-second floor.

**2. The cap over time.** 30 seconds at launch, 60 in 2022, 90 in March 2023,
then no fixed cap from June 2025, drawn as a bar that fades out into an arrow
because there is no number to draw. Sources are named in the figure's own
footer so the credit survives if the image is reshared alone.

**3. Run time by content type.** Hooks at 7 to 15 seconds, demos at 30 to 60,
explainers at 60 to 180, against a shaded band marking the 15 to 60 second
range most business Reels do best in.

## Reproducing them

```bash
python3 images/make_images.py
```

Requires Pillow. The script draws all three from the figures cited in the
article, so the graphics can be regenerated or corrected without a design tool.

## Source links: the rule

Clicking `Image source` has to show you the image. Not a page containing the
image, not the article, not a help centre entry, not a site's front page.

Two earlier drafts got this wrong, first with bare domains
(`https://www.facebook.com/`) and then with deep links that were still web
pages (a Facebook help article, a GitHub blob viewer). Both now fail the check:

```bash
python3 tools/check_image_sources.py blog/facebook-reel-length/facebook-reel-length.md
```

It fails on a missing image file, missing alt text, a missing or malformed
`Image source` line, a bare domain, a link to the article's own page, a URL
that does not end in an image extension, and a GitHub `/blob/` viewer URL.

**One caveat, stated plainly.** The links currently point at
`raw.githubusercontent.com`, which serves the actual PNG bytes and satisfies
the rule. This repository is private, so those URLs need a GitHub token and
will not open in a plain browser session for anyone outside it. At publish
time, replace each one with the uploaded asset's own URL on socialbee.com, for
example `https://socialbee.com/wp-content/uploads/2026/08/facebook-reel-length-limits-2021-2026.webp`.
The rule does not change: the link ends in an image extension and shows the
photo.

## Before upload

- Convert to WebP and compress. Target under 150KB each at 1200px wide. The
  three PNGs are 101KB, 119KB and 99KB, so WebP will roughly halve them.
- Set explicit width and height attributes so the images do not shift layout
  while the page loads. All three are 1200px wide; heights are 700, 620 and 640.
- Re-run `check_image_sources.py` after the CMS import. That formatting is the
  thing most often lost in a paste.
