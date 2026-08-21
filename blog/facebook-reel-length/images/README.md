# Images

Every image used by the article, plus the script that generates the one
original asset. Sources for all three are documented in `../image-manifest.md`.

| File | What it is | Source |
| --- | --- | --- |
| `facebook-reel-length-limits-2021-2026.png` | Original chart of the Reel length cap over time | SocialBee original. Data: TechCrunch (March 2023), Social Media Today (June 2025) |
| `make_chart.py` | Regenerates the chart above | — |
| `facebook-reels-composer-timer.png` | **Not yet captured.** Facebook Reels composer showing the 90-second timer | https://www.facebook.com/ |
| `socialbee-facebook-reel-scheduled.png` | **Not yet captured.** SocialBee post editor with a Reel scheduled | https://socialbee.com/ |

No stock photography: SocialBee's guidelines allow screenshots, charts and
original visuals only.

```bash
python3 make_chart.py   # requires Pillow
```
