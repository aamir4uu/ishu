#!/usr/bin/env python3
"""Convert an article markdown file to .docx.

Deliberately narrow: it handles exactly the markdown this repo's articles use
(ATX headings, paragraphs, bold and italic runs, inline links, ordered and
unordered lists, pipe tables, images with a hyperlinked source line beneath).
It is not a general markdown engine, and it fails loudly on anything it does
not recognise rather than silently dropping content.

    python3 tools/md_to_docx.py blog/slug/article.md "Document Title.docx"

Missing image files are not an error. The converter drops a visible placeholder
box carrying the alt text and the filename, so the gap is obvious in Word and
whoever captures the screenshot knows what belongs there.
"""

import os
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
IMAGE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$")
INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]+\))")

LINK_BLUE = RGBColor(0x0B, 0x5C, 0xAB)
MUTED = RGBColor(0x71, 0x80, 0x96)


def add_hyperlink(paragraph, url, text, bold=False, italic=False):
    part = paragraph.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "0B5CAB")
    rpr.append(color)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    if bold:
        rpr.append(OxmlElement("w:b"))
    if italic:
        rpr.append(OxmlElement("w:i"))
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    run.append(t)
    link.append(run)
    paragraph._p.append(link)


def add_runs(paragraph, text, bold=False, italic=False):
    """Render inline bold, italic and links into an existing paragraph."""
    for piece in INLINE.split(text):
        if not piece:
            continue
        if piece.startswith("**") and piece.endswith("**") and len(piece) > 4:
            r = paragraph.add_run(piece[2:-2])
            r.bold = True
            r.italic = italic
        elif (piece.startswith("*") and piece.endswith("*")
              and len(piece) > 2 and not piece.startswith("**")):
            r = paragraph.add_run(piece[1:-1])
            r.italic = True
            r.bold = bold
        else:
            m = LINK.fullmatch(piece)
            if m:
                add_hyperlink(paragraph, m.group(2), m.group(1), bold, italic)
            else:
                r = paragraph.add_run(piece)
                r.bold = bold
                r.italic = italic


def shade(cell, hex_fill):
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear")
    el.set(qn("w:fill"), hex_fill)
    cell._tc.get_or_add_tcPr().append(el)


def add_image(doc, base_dir, alt, path):
    full = os.path.normpath(os.path.join(base_dir, path))
    if os.path.exists(full):
        doc.add_picture(full, width=Inches(6.0))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        return True
    # Visible placeholder, so a missing screenshot cannot be overlooked.
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(f"[ IMAGE TO BE PLACED: {path} ]")
    r.bold = True
    r.font.color.rgb = MUTED
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r2 = p2.add_run(f"Alt text: {alt}")
    r2.italic = True
    r2.font.size = Pt(9)
    r2.font.color.rgb = MUTED
    return False


def parse_table(lines, i):
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
            rows.append(cells)
        i += 1
    return rows, i


def convert(md_path, out_path):
    base_dir = os.path.dirname(os.path.abspath(md_path))
    with open(md_path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    doc = Document()
    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    normal.paragraph_format.space_after = Pt(10)

    missing = []
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()

        if not line:
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            doc.add_heading(m.group(2).strip(), level=len(m.group(1)))
            i += 1
            continue

        m = IMAGE.match(line)
        if m:
            if not add_image(doc, base_dir, m.group(1), m.group(2)):
                missing.append(m.group(2))
            i += 1
            # The source line directly beneath is part of the image block.
            while i < len(lines) and not lines[i].strip():
                i += 1
            if i < len(lines) and lines[i].strip().startswith("*["):
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                add_runs(p, lines[i].strip())
                for r in p.runs:
                    r.font.size = Pt(9)
                p.paragraph_format.space_after = Pt(16)
                i += 1
            continue

        if line.startswith("|"):
            rows, i = parse_table(lines, i)
            if not rows:
                continue
            t = doc.add_table(rows=len(rows), cols=len(rows[0]))
            t.style = "Table Grid"
            t.alignment = WD_TABLE_ALIGNMENT.CENTER
            for ri, row in enumerate(rows):
                for ci, cell in enumerate(row):
                    if ci >= len(rows[0]):
                        continue
                    c = t.cell(ri, ci)
                    c.text = ""
                    add_runs(c.paragraphs[0], cell, bold=(ri == 0))
                    c.paragraphs[0].paragraph_format.space_after = Pt(2)
                    if ri == 0:
                        shade(c, "F2F2F2")
            doc.add_paragraph()
            continue

        m = re.match(r"^[-*+]\s+(.*)$", line)
        if m:
            p = doc.add_paragraph(style="List Bullet")
            add_runs(p, m.group(1))
            i += 1
            continue

        m = re.match(r"^\d+[.)]\s+(.*)$", line)
        if m:
            p = doc.add_paragraph(style="List Number")
            add_runs(p, m.group(1))
            i += 1
            continue

        if line.startswith("---"):
            i += 1
            continue

        # A line that is entirely bold is a standalone heading-ish line, such as
        # an FAQ question. Keep it as its own paragraph instead of letting the
        # answer beneath get swept into it.
        if re.fullmatch(r"\*\*[^*]+\*\*", line):
            p = doc.add_paragraph()
            p.paragraph_format.space_after = Pt(2)
            add_runs(p, line)
            i += 1
            continue

        # Paragraph: gather the wrapped continuation lines.
        buf = [line]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if (not nxt or nxt.startswith(("#", "|", ">", "!["))
                    or re.match(r"^([-*+]|\d+[.)])\s", nxt)
                    or re.fullmatch(r"\*\*[^*]+\*\*", nxt)):
                break
            buf.append(nxt)
            i += 1
        p = doc.add_paragraph()
        add_runs(p, " ".join(buf))

    doc.save(out_path)
    return missing


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    missing = convert(sys.argv[1], sys.argv[2])
    size = os.path.getsize(sys.argv[2]) // 1024
    print(f"wrote {sys.argv[2]} ({size} KB)")
    if missing:
        print(f"{len(missing)} image(s) not on disk, placeholders inserted:")
        for m in missing:
            print(f"  - {m}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
