#!/usr/bin/env python3
"""Draw the article's two original visuals.

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



# ---------------------------------------------------------------- figure one

def hashtag_limit_change():
    """Thirty slots to five. The fact most trending-hashtag lists have missed."""
    W, H = 1200, 620
    img, d = canvas(W, H)

    f_title = font("LiberationSans-Bold.ttf", 34)
    f_sub = font("LiberationSans-Regular.ttf", 19)
    f_when = font("LiberationSans-Bold.ttf", 21)
    f_note = font("LiberationSans-Regular.ttf", 16)
    f_big = font("LiberationSans-Bold.ttf", 52)
    f_unit = font("LiberationSans-Regular.ttf", 18)
    f_foot = font("LiberationSans-Regular.ttf", 15)

    d.text((px(60), px(48)), "Instagram's Hashtag Limit Went From 30 to 5",
           font=f_title, fill=INK)
    d.text((px(60), px(96)),
           "Enforced from December 2025, on posts and Reels, for every account "
           "type.", font=f_sub, fill=MUTED)

    # Two columns of dots: thirty filled, five filled. Counting beats a bar here.
    def dot_grid(x, y, total, filled, cols, size, gap, colour):
        for i in range(total):
            r, c = divmod(i, cols)
            cx = x + c * (size + gap)
            cy = y + r * (size + gap)
            fill = colour if i < filled else RULE
            d.ellipse([px(cx), px(cy), px(cx + size), px(cy + size)], fill=fill)

    left_x, right_x, top = 60, 660, 190

    d.text((px(left_x), px(top - 32)), "Until December 2025", font=f_when,
           fill=MUTED)
    dot_grid(left_x, top + 8, 30, 30, 10, 22, 12, BAR_SOFT)
    d.text((px(left_x), px(top + 130)), "30", font=f_big, fill=MUTED)
    d.text((px(left_x + 74), px(top + 158)), "hashtags per post", font=f_unit,
           fill=MUTED)

    d.text((px(right_x), px(top - 32)), "From December 2025", font=f_when,
           fill=INK)
    dot_grid(right_x, top + 8, 30, 5, 10, 22, 12, BAR)
    d.text((px(right_x), px(top + 130)), "5", font=f_big, fill=INK)
    d.text((px(right_x + 42), px(top + 158)), "hashtags per post", font=f_unit,
           fill=INK)

    ny = top + 220
    d.rounded_rectangle([px(60), px(ny), px(W - 60), px(ny + 84)], radius=px(12),
                        fill=PANEL, outline=RULE, width=SCALE)
    d.rounded_rectangle([px(60), px(ny), px(68), px(ny + 84)], radius=px(4),
                        fill=RED)
    draw_wrapped(d, (94, ny + 22),
                 "The cap counts your caption and your comments together, so "
                 "moving tags into the first comment no longer buys you extra "
                 "slots.", f_note, INK, W - 200, 25)

    fy = ny + 116
    d.line([(px(60), px(fy)), (px(W - 60), px(fy))], fill=RULE, width=SCALE)
    d.text((px(60), px(fy + 18)),
           "Announced by Instagram's @Creators account on 19 December 2025.",
           font=f_foot, fill=MUTED)
    d.text((px(60), px(fy + 42)),
           "Source: Social Media Today (December 2025).  Chart: SocialBee.",
           font=f_foot, fill=MUTED)

    save(img, W, H, "instagram-hashtag-limit-change.png")


# ---------------------------------------------------------------- figure two

def five_slots():
    """A job for each of the five slots, instead of five big tags."""
    W, H = 1200, 600
    img, d = canvas(W, H)

    f_title = font("LiberationSans-Bold.ttf", 34)
    f_sub = font("LiberationSans-Regular.ttf", 19)
    f_num = font("LiberationSans-Bold.ttf", 20)
    f_role = font("LiberationSans-Bold.ttf", 19)
    f_body = font("LiberationSans-Regular.ttf", 16)
    f_eg = font("LiberationSans-Bold.ttf", 16)
    f_foot = font("LiberationSans-Regular.ttf", 15)

    d.text((px(60), px(48)), "How to Spend Your Five Hashtag Slots",
           font=f_title, fill=INK)
    d.text((px(60), px(96)),
           "Give every slot a job. Five big tags is five wasted slots.",
           font=f_sub, fill=MUTED)

    slots = [
        ("1", "Topic", "Names the subject the way a stranger would search it",
         "#sourdough", BAR),
        ("2", "Niche", "Small enough that your post stays visible in it",
         "#sourdoughstarter", BAR),
        ("3", "Niche", "A second angle on the same audience",
         "#homebaking", BAR),
        ("4", "Format", "Only when the format is the point",
         "#reels", BAR_SOFT),
        ("5", "Brand", "One you own and can track over time",
         "#yourbakeryname", GREEN),
    ]

    top, rh = 168, 66
    for i, (num, role, body, example, colour) in enumerate(slots):
        y = top + i * rh
        d.ellipse([px(60), px(y), px(60 + 36), px(y + 36)], fill=colour)
        d.text((px(72), px(y + 7)), num, font=f_num, fill=INK)
        d.text((px(116), px(y + 6)), role, font=f_role, fill=INK)
        d.text((px(230), px(y + 8)), body, font=f_body, fill=MUTED)
        d.text((px(880), px(y + 7)), example, font=f_eg, fill=INK)

    fy = top + len(slots) * rh + 18
    d.line([(px(60), px(fy)), (px(W - 60), px(fy))], fill=RULE, width=SCALE)
    d.text((px(60), px(fy + 18)),
           "Examples are illustrative. Then put the phrase someone would "
           "search into the caption itself, where Instagram indexes it.",
           font=f_foot, fill=MUTED)
    d.text((px(60), px(fy + 42)),
           "Diagram: SocialBee.", font=f_foot, fill=MUTED)

    save(img, W, H, "instagram-five-hashtag-slots.png")


if __name__ == "__main__":
    hashtag_limit_change()
    five_slots()
