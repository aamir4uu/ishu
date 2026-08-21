# Image Manifest

Three images. All three exist, all three are original SocialBee visuals, and
every `Image source` link resolves to the image file itself. Nothing is
outstanding.

## Why there are no screenshots

The brand guidelines ask for screenshots, and screenshots would have been the
better choice. They were not possible, and the reason is worth recording so
nobody retries it:

This environment has no general web egress. Every external host is refused at
the proxy with a 403 to CONNECT, verified with both curl and headless Chromium:

```
curl     socialbee.com   -> CONNECT tunnel failed, 403
Chromium socialbee.com   -> net::ERR_TUNNEL_CONNECTION_FAILED
Chromium facebook.com    -> net::ERR_TUNNEL_CONNECTION_FAILED
```

It is not specific to those two sites. example.com, wikipedia.org and
techcrunch.com are refused the same way. Only GitHub and package registries are
reachable. There is no page to load and no product UI to capture, and the two
uploaded reference files contain no product imagery either.

Building a mock-up of the Facebook or SocialBee interface and photographing it
was rejected on purpose. A fabricated screenshot of a real product, published
in a client article, misrepresents that product.

So the two screenshot slots became original diagrams that carry the same
information. The guidelines permit exactly this: "screenshots, charts, and
original visuals only".

## The images

| # | File | Type | Placement | Alt text | Image source |
| --- | --- | --- | --- | --- | --- |
| 1 | `facebook-reel-post-route-decision.png` | Decision diagram | End of "Reels Recorded in the App: 90 Seconds" | Decision diagram showing which way to post a Facebook Reel by length: 3 to 90 seconds can be recorded or uploaded, over 90 seconds must be uploaded, under 3 seconds will not publish | [.png file](https://raw.githubusercontent.com/aamir4uu/ishu/refs/heads/claude/facebook-reel-length-post-5fl797/blog/facebook-reel-length/images/facebook-reel-post-route-decision.png) |
| 2 | `facebook-reel-length-limits-2021-2026.png` | Chart | After the TechCrunch and Social Media Today citations | Bar chart of the maximum Facebook Reel length from 2021 to 2026, rising from 30 seconds to 90 seconds and then to no fixed cap | [.png file](https://raw.githubusercontent.com/aamir4uu/ishu/refs/heads/claude/facebook-reel-length-post-5fl797/blog/facebook-reel-length/images/facebook-reel-length-limits-2021-2026.png) |
| 3 | `facebook-reel-scheduling-workflow.png` | Process diagram | In "How to Schedule Facebook Reels With SocialBee" | Four-step diagram of scheduling a batch of Facebook Reels in SocialBee: plan the batch, add the files, sort by content category, let it publish | [.png file](https://raw.githubusercontent.com/aamir4uu/ishu/refs/heads/claude/facebook-reel-length-post-5fl797/blog/facebook-reel-length/images/facebook-reel-scheduling-workflow.png) |

One chart and two diagrams, not three charts. The earlier draft ran charts
throughout, which over-read the single word "charts" in the guidelines and
ignored that screenshots are what they actually ask for. Diagrams are the
closest honest substitute: they explain a process, which is what a screenshot
would have done here.

Each sits in the section it explains. Text always comes between a heading and
an image. Alt text carries the keyword where it reads naturally.

## What each one shows

**1. Which way to post.** A decision diagram driven by run time. 3 to 90
seconds takes either route; over 90 seconds must be uploaded because the in-app
timer stops; under 3 seconds will not publish at all, and SocialBee's direct
publishing needs 4. This is the distinction the whole article turns on, and it
is what the composer screenshot was meant to convey.

**2. The cap over time.** 30 seconds at launch, 60 in 2022, 90 in March 2023,
then no fixed cap from June 2025, drawn as a bar that fades into an arrow
because there is no number to draw. The dated, sourced data point the GEO
checklist asks for.

**3. The scheduling workflow.** Plan the batch, add the files, sort by content
category, let it publish. The requirements shown in step 2 are SocialBee's real
direct-publishing constraints: 4 to 90 seconds, 9:16, 540 x 960 or better,
.MP4 or .MOV under 512 MB. This replaces the product screenshot in the
promotion section, where section 6 of the guidelines asks for a visual,
caption and CTA.

## Reproducing them

```bash
python3 images/make_images.py
```

Requires Pillow. Draws all three. Every figure repeats its sources in its own
footer so the credit survives if the image is reshared alone.

## Source links: the rule

Clicking `Image source` has to show you the image. Not a page containing it,
not the article, not a help centre entry, not a front page. Earlier drafts got
this wrong twice, first with bare domains and then with deep links that were
still web pages.

```bash
python3 tools/check_image_sources.py blog/facebook-reel-length/facebook-reel-length.md --strict
```

Fails on a missing file, missing alt text, a malformed source line, a bare
domain, a link to the article's own page, a URL that is not an image file, a
GitHub `/blob/` viewer URL, and any slot still awaiting capture. Currently
passes with 3 of 3 final.

**One caveat.** The links point at `raw.githubusercontent.com`, which serves
the actual PNG bytes. This repository is private, so those URLs need a GitHub
token and will not open in a plain browser session. Replace each with the
uploaded asset's own URL at publish. The rule does not change: the link ends in
an image extension and shows the photo.

## Before upload

- Convert to WebP and compress. Target under 150KB each at 1200px wide. The
  PNGs are 101KB, 136KB and 123KB.
- Set explicit width and height so images do not shift layout while loading.
  All are 1200px wide; heights are 740, 700 and 560.
- Re-run `check_image_sources.py --strict` after the CMS import.
