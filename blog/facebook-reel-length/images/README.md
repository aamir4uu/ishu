# Images

Every image the article uses, plus the script that draws them. All three are
original SocialBee graphics; there is no stock photography, per the brand
guidelines. Placement, alt text and source links are in `../image-manifest.md`.

| File | Size | What it shows |
| --- | --- | --- |
| `facebook-reel-upload-vs-in-app-limits.png` | 1200x620 | Uploaded file has no fixed maximum, in-app recording stops at 90 seconds |
| `facebook-reel-length-limits-2021-2026.png` | 1200x700 | The cap over time: 30s, 60s, 90s, then no fixed cap |
| `facebook-reel-length-by-content-type.png` | 1200x640 | Recommended run time by content type against the 15 to 60 second band |
| `make_images.py` | — | Regenerates all three |

Figures 1 and 2 are drawn from [TechCrunch, March 2023](https://techcrunch.com/2023/03/03/meta-rolls-out-new-facebook-reels-features-expands-max-video-length-to-90-seconds/),
[Social Media Today, June 2025](https://www.socialmediatoday.com/news/facebook-renames-all-videos-reels/750973/)
and SocialBee's own publishing requirements. Each figure repeats its sources in
its footer so the credit survives if the image is reshared on its own.

```bash
python3 make_images.py   # requires Pillow
```
