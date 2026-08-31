#!/usr/bin/env python3
"""
detector-paste.py - emit exactly the text to paste into a detector.

A .docx deliverable carries scaffolding that never reaches the published page:
meta title and description fields, image placeholder frames, alt-text lines and
"Image Source" captions. Pasting the whole document into ZeroGPT tests that
scaffolding too. It is English boilerplate, it repeats verbatim once per image,
and in the placeholder frame it even carries an em dash, which is a marker the
pre-flight gates ban outright.

This writes the published article and nothing else: headings and body copy,
tables flattened to plain lines, links reduced to their anchor text.

Usage:
    python3 tools/detector-paste.py ARTICLE.md [-o OUT.txt]
"""

import argparse
import re
import sys
from pathlib import Path


def to_paste(md: str) -> str:
    md = re.sub(r"^\s*\*\*Meta (?:Title|Description):\*\*.*$", "", md,
                flags=re.M | re.I)
    md = re.sub(r"^\s*!\[[^\]]*\]\([^)]*\)\s*$", "", md, flags=re.M)
    md = re.sub(r"^\s*\[Image Source\]\([^)]*\)\s*$", "", md, flags=re.M | re.I)
    md = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", md)          # links -> anchor
    md = re.sub(r"^\s*\|[\s:|-]+\|\s*$", "", md, flags=re.M)  # table rules
    md = re.sub(r"^\s*\|(.*)\|\s*$",
                lambda m: " ".join(c.strip() for c in m.group(1).split("|") if c.strip()),
                md, flags=re.M)
    md = re.sub(r"^\s{0,3}#{1,6}\s+", "", md, flags=re.M)     # heading markers
    md = re.sub(r"^\s{0,4}[-*+]\s+", "", md, flags=re.M)      # bullet markers
    md = md.replace("**", "")
    return re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("-o", "--out")
    a = ap.parse_args()
    text = to_paste(Path(a.file).read_text(encoding="utf-8"))
    out = Path(a.out) if a.out else Path(a.file).with_name("detector-paste.txt")
    out.write_text(text, encoding="utf-8")
    words = len(re.findall(r"[A-Za-z'ऀ-ॿ0-9]+", text))
    print(f"wrote: {out}  ({words} words, {len(text)} chars)")
    for bad, label in [("—", "em dash"), ("PLACEHOLDER", "image placeholder"),
                       ("Meta Title", "meta field"), ("Image Source", "image credit")]:
        if bad in text:
            print(f"  WARNING: {label} still present", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
