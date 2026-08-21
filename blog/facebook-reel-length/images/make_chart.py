#!/usr/bin/env python3
"""Generate the article's original chart.

Kept in the repo so the graphic is reproducible and so nobody has to wonder
where it came from. SocialBee's brand guidelines rule out stock photography and
ask for screenshots, charts and original visuals, so this is drawn from the
sourced figures rather than licensed from a photo library.

    python3 make_chart.py

Data sources are cited in ../image-manifest.md.
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = "/usr/share/fonts/truetype/liberation"

W, H = 1200, 700
SCALE = 2  # draw at 2x, downsample for clean edges

INK = (26, 32, 44)
MUTED = (113, 128, 150)
RULE = (226, 232, 240)
BG = (255, 255, 255)
BAR = (247, 183, 49)
BAR_OPEN = (250, 217, 141)
ACCENT = (26, 32, 44)

# (label, sublabel, seconds, is_uncapped)
ROWS = [
    ("2021", "Reels launch", 30, False),
    ("2022", "Cap doubles", 60, False),
    ("March 2023", "Meta expands Reels", 90, False),
    ("June 2025", "All videos become Reels", None, True),
]

AXIS_MAX = 120.0  # seconds represented by a full-width bar


def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size * SCALE)


def main():
    img = Image.new("RGB", (W * SCALE, H * SCALE), BG)
    d = ImageDraw.Draw(img)

    f_title = font("LiberationSans-Bold.ttf", 34)
    f_sub = font("LiberationSans-Regular.ttf", 19)
    f_year = font("LiberationSans-Bold.ttf", 22)
    f_note = font("LiberationSans-Regular.ttf", 16)
    f_val = font("LiberationSans-Bold.ttf", 26)
    f_foot = font("LiberationSans-Regular.ttf", 15)

    def px(v):
        return int(v * SCALE)

    d.text((px(60), px(52)), "Maximum Facebook Reel Length, 2021 to 2026",
           font=f_title, fill=INK)
    d.text((px(60), px(100)),
           "The 90-second cap most guides still quote was retired in June 2025.",
           font=f_sub, fill=MUTED)

    left = 300
    right = W - 90
    top = 170
    row_h = 108
    bar_h = 42

    for i, (year, note, secs, uncapped) in enumerate(ROWS):
        y = top + i * row_h

        d.text((px(60), px(y + 4)), year, font=f_year, fill=INK)
        d.text((px(60), px(y + 34)), note, font=f_note, fill=MUTED)

        d.line([(px(left), px(y - 18)), (px(right), px(y - 18))],
               fill=RULE, width=SCALE)

        if uncapped:
            # An open-ended bar: fades out and ends in an arrow, because there
            # is no number to draw here.
            # Reserve room on the right for the arrow and its label.
            bw = right - left - 230
            steps = 90
            for s in range(steps):
                x0 = left + bw * s / steps
                x1 = left + bw * (s + 1) / steps + 1
                t = s / steps
                col = tuple(int(BAR[c] + (255 - BAR[c]) * (t ** 1.6))
                            for c in range(3))
                d.rectangle([px(x0), px(y), px(x1), px(y + bar_h)], fill=col)
            ax = left + bw + 6
            d.polygon([(px(ax), px(y + 4)), (px(ax + 26), px(y + bar_h / 2)),
                       (px(ax), px(y + bar_h - 4))], fill=BAR_OPEN)
            d.text((px(ax + 40), px(y + 8)), "No fixed cap",
                   font=f_val, fill=ACCENT)
        else:
            bw = (right - left) * (secs / AXIS_MAX)
            d.rectangle([px(left), px(y), px(left + bw), px(y + bar_h)],
                        fill=BAR)
            d.text((px(left + bw + 18), px(y + 8)), f"{secs} sec",
                   font=f_val, fill=ACCENT)

    fy = top + len(ROWS) * row_h + 4
    d.line([(px(60), px(fy)), (px(right), px(fy))], fill=RULE, width=SCALE)
    d.text((px(60), px(fy + 22)),
           "Recording inside the Facebook app still stops at 90 seconds. "
           "The minimum length is 3 seconds.",
           font=f_foot, fill=MUTED)
    d.text((px(60), px(fy + 48)),
           "Sources: TechCrunch (March 2023); Social Media Today (June 2025).  "
           "Chart: SocialBee.",
           font=f_foot, fill=MUTED)

    img = img.resize((W, H), Image.LANCZOS)
    out = os.path.join(HERE, "facebook-reel-length-limits-2021-2026.png")
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out} ({os.path.getsize(out) // 1024} KB)")


if __name__ == "__main__":
    main()
