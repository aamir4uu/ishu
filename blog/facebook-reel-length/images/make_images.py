#!/usr/bin/env python3
"""Generate every image the article uses.

SocialBee's brand guidelines rule out stock photography and ask for
screenshots, charts and original visuals. Product screenshots have to be
captured from a logged-in account, which cannot happen here, so all three
images are original graphics drawn from the article's own sourced figures.

Keeping the generator in the repo means the images are reproducible, their
provenance is checkable, and the "Image source" line can point at a real image
file rather than at a web page that happens to contain one.

    python3 make_images.py

Data sources are cited in ../image-manifest.md and in each figure's footer.
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


# --------------------------------------------------------------- figure two

def two_paths():
    """Upload versus record: the distinction the whole article turns on."""
    W, H = 1200, 620
    img, d = canvas(W, H)

    f_title = font("LiberationSans-Bold.ttf", 34)
    f_sub = font("LiberationSans-Regular.ttf", 19)
    f_head = font("LiberationSans-Bold.ttf", 23)
    f_body = font("LiberationSans-Regular.ttf", 17)
    f_big = font("LiberationSans-Bold.ttf", 40)
    f_cap = font("LiberationSans-Regular.ttf", 16)
    f_foot = font("LiberationSans-Regular.ttf", 15)

    d.text((px(60), px(48)), "Two Ways to Post a Reel, Two Different Limits",
           font=f_title, fill=INK)
    d.text((px(60), px(96)),
           "Mixing these up is what causes most of the confusion about Reel length.",
           font=f_sub, fill=MUTED)

    cards = [
        ("Upload a finished file", "You export the video from your editor "
         "and upload it to Facebook.", "No fixed\nmaximum",
         "Since June 2025, on updated accounts", GREEN),
        ("Record in the Facebook app", "You open the Reels composer and shoot "
         "straight into the timer.", "90 sec\nceiling",
         "The in-app timer still stops you", RED),
    ]

    cw, gap, top, ch = 500, 40, 160, 340
    for i, (head, body, verdict, foot, accent) in enumerate(cards):
        x = 60 + i * (cw + gap)
        d.rounded_rectangle([px(x), px(top), px(x + cw), px(top + ch)],
                            radius=px(14), fill=PANEL, outline=RULE,
                            width=SCALE)
        d.rounded_rectangle([px(x), px(top), px(x + 8), px(top + ch)],
                            radius=px(4), fill=accent)

        d.text((px(x + 34), px(top + 30)), head, font=f_head, fill=INK)
        # Wrap the body text by hand; two short lines beat one long one.
        words, line, lines = body.split(), "", []
        for w in words:
            trial = (line + " " + w).strip()
            if text_width(d, trial, f_body) > cw - 70:
                lines.append(line)
                line = w
            else:
                line = trial
        lines.append(line)
        for j, ln in enumerate(lines):
            d.text((px(x + 34), px(top + 74 + j * 26)), ln, font=f_body,
                   fill=MUTED)

        vy = top + 74 + len(lines) * 26 + 26
        for j, ln in enumerate(verdict.split("\n")):
            d.text((px(x + 34), px(vy + j * 46)), ln, font=f_big, fill=accent)
        d.text((px(x + 34), px(vy + len(verdict.split("\n")) * 46 + 8)),
               foot, font=f_cap, fill=MUTED)

    fy = top + ch + 34
    d.line([(px(60), px(fy)), (px(W - 60), px(fy))], fill=RULE, width=SCALE)
    d.text((px(60), px(fy + 20)),
           "Either way the minimum is 3 seconds, and SocialBee's direct "
           "publishing needs at least 4.", font=f_foot, fill=MUTED)
    d.text((px(60), px(fy + 44)),
           "Sources: Meta, June 2025 video consolidation; SocialBee help "
           "documentation.  Chart: SocialBee.", font=f_foot, fill=MUTED)

    save(img, W, H, "facebook-reel-upload-vs-in-app-limits.png")


# ------------------------------------------------------------- figure three

def length_by_content_type():
    """Recommended run time per kind of Reel, against the sweet spot."""
    W, H = 1200, 640
    img, d = canvas(W, H)

    f_title = font("LiberationSans-Bold.ttf", 34)
    f_sub = font("LiberationSans-Regular.ttf", 19)
    f_lab = font("LiberationSans-Bold.ttf", 20)
    f_small = font("LiberationSans-Regular.ttf", 15)
    f_val = font("LiberationSans-Bold.ttf", 20)
    f_foot = font("LiberationSans-Regular.ttf", 15)

    d.text((px(60), px(48)), "How Long Should a Facebook Reel Be?",
           font=f_title, fill=INK)
    d.text((px(60), px(96)),
           "Ranges that tend to hold attention, by what the Reel is doing.",
           font=f_sub, fill=MUTED)

    # Right margin has to hold the longest value label ("60 to 180 sec"),
    # otherwise the widest bar pushes its own label off the canvas.
    left, right, top, row_h, bar_h = 330, W - 250, 200, 96, 34
    axis_max = 180.0

    def x_of(sec):
        return left + (right - left) * (sec / axis_max)

    # Sweet-spot band behind everything else.
    d.rectangle([px(x_of(15)), px(top - 26), px(x_of(60)), px(top + 3 * row_h - 22)],
                fill=BAR_PALE)
    d.text((px(x_of(15) + 8), px(top - 48)), "15 to 60 sec: the range most "
           "business Reels do best in", font=f_small, fill=MUTED)

    rows = [
        ("Hooks and single tips", "One idea, no setup", 7, 15),
        ("Product demos and how-tos", "Long enough for a real workflow", 30, 60),
        ("Explainers and interviews", "Only once people know you", 60, 180),
    ]
    for i, (label, note, lo, hi) in enumerate(rows):
        y = top + i * row_h
        d.text((px(60), px(y - 4)), label, font=f_lab, fill=INK)
        d.text((px(60), px(y + 24)), note, font=f_small, fill=MUTED)
        d.rounded_rectangle([px(x_of(lo)), px(y), px(x_of(hi)), px(y + bar_h)],
                            radius=px(bar_h / 2), fill=BAR)
        d.text((px(x_of(hi) + 16), px(y + 6)), f"{lo} to {hi} sec",
               font=f_val, fill=INK)

    ay = top + 3 * row_h - 18
    d.line([(px(left), px(ay)), (px(right), px(ay))], fill=RULE, width=SCALE)
    for tick in (0, 30, 60, 90, 120, 150, 180):
        tx = x_of(tick)
        d.line([(px(tx), px(ay)), (px(tx), px(ay + 7))], fill=RULE, width=SCALE)
        d.text((px(tx - 8), px(ay + 14)), str(tick), font=f_small, fill=MUTED)
    d.text((px(right - 40), px(ay + 40)), "seconds", font=f_small, fill=MUTED)

    fy = ay + 74
    d.line([(px(60), px(fy)), (px(right), px(fy))], fill=RULE, width=SCALE)
    d.text((px(60), px(fy + 20)),
           "Facebook ranks on completion rather than duration, so the right "
           "length is the one people finish.", font=f_foot, fill=MUTED)
    d.text((px(60), px(fy + 44)),
           "Chart: SocialBee.", font=f_foot, fill=MUTED)

    save(img, W, H, "facebook-reel-length-by-content-type.png")


if __name__ == "__main__":
    length_limits_timeline()
    two_paths()
    length_by_content_type()
