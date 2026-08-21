#!/usr/bin/env python3
"""Draw the article's three original visuals.

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


# ------------------------------------------------------- shared text helpers

def wrap(d, text, f, max_w):
    """Greedy wrap measured against the real font, not a character count.

    Two earlier figures shipped with text running off the canvas because the
    wrapping was guessed. Everything that draws a run of text goes through here.
    """
    words, line, out = text.split(), "", []
    for w in words:
        trial = (line + " " + w).strip()
        if text_width(d, trial, f) > max_w and line:
            out.append(line)
            line = w
        else:
            line = trial
    if line:
        out.append(line)
    return out


def draw_wrapped(d, xy, text, f, fill, max_w, leading):
    x, y = xy
    lines = wrap(d, text, f, max_w)
    for i, ln in enumerate(lines):
        d.text((px(x), px(y + i * leading)), ln, font=f, fill=fill)
    return y + len(lines) * leading


def arrow_right(d, x, y, length, colour, thickness=4, head=13):
    if length <= head:
        return
    d.rectangle([px(x), px(y - thickness / 2), px(x + length - head),
                 px(y + thickness / 2)], fill=colour)
    d.polygon([(px(x + length - head), px(y - head / 2 - 2)),
               (px(x + length), px(y)),
               (px(x + length - head), px(y + head / 2 + 2))], fill=colour)


# ------------------------------------------------------------- figure two

def which_way_to_post():
    """A decision diagram, not a chart: length decides upload or record."""
    W, H = 1200, 740
    img, d = canvas(W, H)

    f_title = font("LiberationSans-Bold.ttf", 34)
    f_sub = font("LiberationSans-Regular.ttf", 19)
    f_q = font("LiberationSans-Bold.ttf", 22)
    f_branch = font("LiberationSans-Bold.ttf", 21)
    f_body = font("LiberationSans-Regular.ttf", 17)
    f_foot = font("LiberationSans-Regular.ttf", 15)

    d.text((px(60), px(48)), "Which Way Should You Post This Reel?",
           font=f_title, fill=INK)
    d.text((px(60), px(96)),
           "The run time decides it, because only one of the two routes has a "
           "ceiling.", font=f_sub, fill=MUTED)

    qx, qy, qw, qh = 60, 172, 320, 96
    d.rounded_rectangle([px(qx), px(qy), px(qx + qw), px(qy + qh)],
                        radius=px(12), fill=INK)
    for i, ln in enumerate(["How long is the", "finished video?"]):
        d.text((px(qx + 26), px(qy + 22 + i * 30)), ln, font=f_q, fill=BG)

    bx, bw, bh = 520, W - 520 - 60, 120
    rows = [
        (176, "3 to 90 seconds", GREEN,
         "Either route works. Record straight into the Reels composer, or "
         "upload a file you have already cut."),
        (336, "Over 90 seconds", BAR,
         "Upload only. The in-app timer stops at 90 seconds, so edit "
         "elsewhere and upload the finished file."),
        (496, "Under 3 seconds", RED,
         "Neither. Facebook will not publish it, and SocialBee's direct "
         "publishing needs at least 4 seconds."),
    ]
    for y, label, accent, body in rows:
        # Elbow connector from the question box out to this branch.
        midx = qx + qw + 60
        d.line([(px(qx + qw), px(qy + qh / 2)), (px(midx), px(qy + qh / 2))],
               fill=RULE, width=px(3))
        d.line([(px(midx), px(qy + qh / 2)), (px(midx), px(y + bh / 2))],
               fill=RULE, width=px(3))
        arrow_right(d, midx, y + bh / 2, bx - midx - 6, RULE)

        d.rounded_rectangle([px(bx), px(y), px(bx + bw), px(y + bh)],
                            radius=px(12), fill=PANEL, outline=RULE, width=SCALE)
        d.rounded_rectangle([px(bx), px(y), px(bx + 8), px(y + bh)],
                            radius=px(4), fill=accent)
        d.text((px(bx + 30), px(y + 20)), label, font=f_branch, fill=accent)
        draw_wrapped(d, (bx + 30, y + 54), body, f_body, MUTED, bw - 60, 25)

    # Footer sits below the last card, computed rather than guessed, so a
    # longer card can never run into it.
    fy = rows[-1][0] + bh + 34
    d.line([(px(60), px(fy)), (px(W - 60), px(fy))], fill=RULE, width=SCALE)
    d.text((px(60), px(fy + 18)),
           "Meta removed the 90-second cap on uploads in June 2025. The "
           "in-app recording timer was not changed.", font=f_foot, fill=MUTED)
    d.text((px(60), px(fy + 42)),
           "Sources: Social Media Today (June 2025); SocialBee help "
           "documentation.  Diagram: SocialBee.", font=f_foot, fill=MUTED)

    save(img, W, H, "facebook-reel-post-route-decision.png")


# ----------------------------------------------------------- figure three

def scheduling_workflow():
    """The batching workflow the SocialBee section describes, as a pipeline."""
    W, H = 1200, 560
    img, d = canvas(W, H)

    f_title = font("LiberationSans-Bold.ttf", 34)
    f_sub = font("LiberationSans-Regular.ttf", 19)
    f_num = font("LiberationSans-Bold.ttf", 21)
    f_step = font("LiberationSans-Bold.ttf", 19)
    f_body = font("LiberationSans-Regular.ttf", 16)
    f_foot = font("LiberationSans-Regular.ttf", 15)

    d.text((px(60), px(48)), "Scheduling a Batch of Facebook Reels",
           font=f_title, fill=INK)
    d.text((px(60), px(96)),
           "Batching is what lets you cut each Reel to the length it needs "
           "rather than the length you had time for.", font=f_sub, fill=MUTED)

    steps = [
        ("Plan the batch", "Decide what each Reel is for, and give it a run "
         "time to match. A hook is not a demo."),
        ("Add the files", "Direct publishing to a Facebook Page takes 4 to 90 "
         "seconds, 9:16, 540 x 960 or better, .MP4 or .MOV under 512 MB."),
        ("Sort by category", "Content categories hold the mix steady, so the "
         "queue is not five demos in a row."),
        ("Let it publish", "Pages publish automatically. Personal profiles get "
         "a mobile notification with the caption copied."),
    ]

    top, ch, gap = 170, 250, 18
    cw = (W - 120 - gap * 3) / 4
    for i, (head, body) in enumerate(steps):
        x = 60 + i * (cw + gap)
        d.rounded_rectangle([px(x), px(top), px(x + cw), px(top + ch)],
                            radius=px(12), fill=PANEL, outline=RULE, width=SCALE)
        d.ellipse([px(x + 24), px(top + 22), px(x + 24 + 40), px(top + 22 + 40)],
                  fill=BAR)
        d.text((px(x + 39), px(top + 30)), str(i + 1), font=f_num, fill=INK)
        d.text((px(x + 24), px(top + 82)), head, font=f_step, fill=INK)
        draw_wrapped(d, (x + 24, top + 114), body, f_body, MUTED, cw - 48, 23)

        if i < 3:
            arrow_right(d, x + cw + 3, top + 42, gap - 6, RULE, 3, 8)

    fy = top + ch + 34
    d.line([(px(60), px(fy)), (px(W - 60), px(fy))], fill=RULE, width=SCALE)
    d.text((px(60), px(fy + 18)),
           "Requirements shown are SocialBee's for direct publishing to a "
           "Facebook Page, and are checked at upload.", font=f_foot, fill=MUTED)
    d.text((px(60), px(fy + 42)),
           "Source: SocialBee help documentation.  Diagram: SocialBee.",
           font=f_foot, fill=MUTED)

    save(img, W, H, "facebook-reel-scheduling-workflow.png")


if __name__ == "__main__":
    length_limits_timeline()
    which_way_to_post()
    scheduling_workflow()
