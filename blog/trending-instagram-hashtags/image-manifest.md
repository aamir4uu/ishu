# Image Manifest

Two images. Both exist, both are original SocialBee visuals, and both
`Image source` links resolve to the image file itself. Nothing is outstanding.

## Why there are no screenshots

The brand guidelines ask for screenshots and they would have been the better
choice. This environment has no general web egress: every external host is
refused at the proxy with a 403 to CONNECT, verified with curl and headless
Chromium. Only GitHub and package registries are reachable, so no product UI
could be captured. Mocking up an interface and photographing it was rejected
on purpose, because a fabricated screenshot of a real product misrepresents it.

The guidelines permit the alternative used here: "screenshots, charts, and
original visuals only".

## The images

| # | File | Type | Placement | Alt text | Image source |
| --- | --- | --- | --- | --- | --- |
| 1 | `instagram-hashtag-limit-change.png` | Chart | After the paragraph describing the cap, in "Instagram Now Caps You at Five Hashtags" | Chart showing Instagram's hashtag limit dropping from thirty per post to five in December 2025 | [.png file](https://raw.githubusercontent.com/aamir4uu/ishu/refs/heads/claude/facebook-reel-length-post-5fl797/blog/trending-instagram-hashtags/images/instagram-hashtag-limit-change.png) |
| 2 | `instagram-five-hashtag-slots.png` | Diagram | After the opening line of "How to Spend Your Five Hashtags" | Diagram allocating five Instagram hashtag slots: one topic tag, two niche tags, one format tag and one brand or campaign tag | [.png file](https://raw.githubusercontent.com/aamir4uu/ishu/refs/heads/claude/facebook-reel-length-post-5fl797/blog/trending-instagram-hashtags/images/instagram-five-hashtag-slots.png) |

Text always sits between a heading and an image. Alt text carries the keyword
where it reads naturally.

## What each one shows

**1. Thirty to five.** Two dot grids of thirty, one filled and one with five
filled, so the size of the cut is countable rather than asserted. Carries the
detail most coverage omits: the cap counts caption and comments as one pool.
Sourced in its own footer to Social Media Today's December 2025 report.

**2. Five slots, five jobs.** One topic tag, two niche tags, one format tag,
one brand tag, each with an illustrative example. This is the practical core of
the article, and the section it sits in is the reason the piece is worth
reading over a list of thirty tags.

The examples in figure 2 are labelled illustrative in the figure itself, so
nobody reads #sourdough as a recommendation.

## Reproducing them

```bash
python3 images/make_images.py
```

Requires Pillow. The drawing kit is shared with the Facebook Reel article, so
both sets of figures use one visual language.

## Source links: the rule

Clicking `Image source` has to show you the image, not a page containing it.

```bash
python3 tools/check_image_sources.py blog/trending-instagram-hashtags/trending-instagram-hashtags.md --strict
```

Passes with 2 of 2 final.

**One caveat.** The links point at `raw.githubusercontent.com`, which serves
the actual PNG bytes. This repository is private, so those URLs need a GitHub
token and will not open in a plain browser session. Replace each with the
uploaded asset's own URL at publish; the rule does not change.

## Before upload

- Convert to WebP and compress. Target under 150KB at 1200px wide. The PNGs are
  94KB and 108KB.
- Set explicit width and height. Both are 1200px wide, 620 and 600 tall.
- Re-run `check_image_sources.py --strict` after the CMS import.
