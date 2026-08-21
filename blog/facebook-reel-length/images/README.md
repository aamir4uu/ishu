# Images

Three original SocialBee visuals. No stock photography and no screenshots: this
environment has no web egress, so no product UI could be captured. The full
reasoning, with the evidence, is in `../image-manifest.md`.

| File | Size | Type | What it shows |
| --- | --- | --- | --- |
| `facebook-reel-post-route-decision.png` | 1200x740 | Decision diagram | Which way to post, by run time: record, upload, or not at all |
| `facebook-reel-length-limits-2021-2026.png` | 1200x700 | Chart | The maximum over time: 30s, 60s, 90s, then no fixed cap |
| `facebook-reel-scheduling-workflow.png` | 1200x560 | Process diagram | Batching Reels in SocialBee: plan, add, categorise, publish |
| `make_images.py` | — | — | Regenerates all three |

Figures draw on [TechCrunch, March 2023](https://techcrunch.com/2023/03/03/meta-rolls-out-new-facebook-reels-features-expands-max-video-length-to-90-seconds/),
[Social Media Today, June 2025](https://www.socialmediatoday.com/news/facebook-renames-all-videos-reels/750973/)
and SocialBee's published direct-publishing requirements. Each repeats its
sources in its own footer.

```bash
python3 make_images.py   # requires Pillow
```
