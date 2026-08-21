#!/usr/bin/env python3
"""Draw the article's one chart.

The brand guidelines permit charts but ask for screenshots: "Include real
examples, case studies, and screenshots, especially of SocialBee in action",
and the promotion pattern in section 6 wants a screenshot, caption and CTA.
Charts appear once, in a single word, in the list of things that are not stock
photography. So the article carries one chart and two screenshots, not three
charts.

This is the chart. It earns its place because it plots dated figures from two
cited sources, which is the citable data point the GEO checklist asks for, and
no screenshot can show a value that changed four times over five years.

    python3 make_images.py

Sources are cited in ../image-manifest.md and in the figure's own footer.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = "/usr/share/fonts/truetype/liberation"

SCALE = 2  # draw at 2x, downsample for clean edges

INK = (26, 32, 44)
MUTED = (113, 128, 150)
RULE = (226, 232, 240)
BG = (255, 255, 255)
PANEL = (248, 250, 252)
BAR = (247, 183, 49)
BAR_SOFT = (250, 217, 141)
BAR_PALE = (253, 240, 213)
GREEN = (56, 161, 105)
RED = (197, 48, 48)


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size * SCALE)


def px(v):
    return int(v * SCALE)


def canvas(w, h):
    img = Image.new("RGB", (w * SCALE, h * SCALE), BG)
    return img, ImageDraw.Draw(img)


def save(img, w, h, name):
    img = img.resize((w, h), Image.LANCZOS)
    out = os.path.join(HERE, name)
    img.save(out, "PNG", optimize=True)
    print(f"wrote {name} ({os.path.getsize(out) // 1024} KB)")


def text_width(d, s, f):
    return (d.textbbox((0, 0), s, font=f)[2]) / SCALE


# --------------------------------------------------------------- figure one

def length_limits_timeline():
    """How the maximum has moved, 2021 to 2026."""
    W, H = 1200, 700
    img, d = canvas(W, H)

    f_title = font("LiberationSans-Bold.ttf", 34)
    f_sub = font("LiberationSans-Regular.ttf", 19)
    f_year = font("LiberationSans-Bold.ttf", 22)
    f_note = font("LiberationSans-Regular.ttf", 16)
    f_val = font("LiberationSans-Bold.ttf", 26)
    f_foot = font("LiberationSans-Regular.ttf", 15)

    d.text((px(60), px(52)), "Maximum Facebook Reel Length, 2021 to 2026",
           font=f_title, fill=INK)
    d.text((px(60), px(100)),
           "The 90-second cap most guides still quote was retired in June 2025.",
           font=f_sub, fill=MUTED)

    rows = [
        ("2021", "Reels launch", 30, False),
        ("2022", "Cap doubles", 60, False),
        ("March 2023", "Meta expands Reels", 90, False),
        ("June 2025", "All videos become Reels", None, True),
    ]
    left, right, top, row_h, bar_h = 300, W - 90, 170, 108, 42

    for i, (year, note, secs, uncapped) in enumerate(rows):
        y = top + i * row_h
        d.text((px(60), px(y + 4)), year, font=f_year, fill=INK)
        d.text((px(60), px(y + 34)), note, font=f_note, fill=MUTED)
        d.line([(px(left), px(y - 18)), (px(right), px(y - 18))],
               fill=RULE, width=SCALE)

        if uncapped:
            bw = right - left - 230
            for s in range(90):
                x0 = left + bw * s / 90
                x1 = left + bw * (s + 1) / 90 + 1
                t = s / 90
                col = tuple(int(BAR[c] + (255 - BAR[c]) * (t ** 1.6))
                            for c in range(3))
                d.rectangle([px(x0), px(y), px(x1), px(y + bar_h)], fill=col)
            ax = left + bw + 6
            d.polygon([(px(ax), px(y + 4)), (px(ax + 26), px(y + bar_h / 2)),
                       (px(ax), px(y + bar_h - 4))], fill=BAR_SOFT)
            d.text((px(ax + 40), px(y + 8)), "No fixed cap", font=f_val, fill=INK)
        else:
            bw = (right - left) * (secs / 120.0)
            d.rectangle([px(left), px(y), px(left + bw), px(y + bar_h)], fill=BAR)
            d.text((px(left + bw + 18), px(y + 8)), f"{secs} sec",
                   font=f_val, fill=INK)

    fy = top + len(rows) * row_h + 4
    d.line([(px(60), px(fy)), (px(right), px(fy))], fill=RULE, width=SCALE)
    d.text((px(60), px(fy + 22)),
           "Recording inside the Facebook app still stops at 90 seconds. "
           "The minimum length is 3 seconds.", font=f_foot, fill=MUTED)
    d.text((px(60), px(fy + 48)),
           "Sources: TechCrunch (March 2023); Social Media Today (June 2025).  "
           "Chart: SocialBee.", font=f_foot, fill=MUTED)

    save(img, W, H, "facebook-reel-length-limits-2021-2026.png")


if __name__ == "__main__":
    length_limits_timeline()
