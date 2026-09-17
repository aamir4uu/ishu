#!/usr/bin/env python3
"""Count the words a client would count in the published article.

Counts headings, body text, list items, table cells and the two-word
"Image Source" captions, which is what Word counts once the placeholder frames
are replaced by pictures. Skips HTML comments (editor notes), image lines,
table separator rows and any paragraph that starts with "Disclaimer:".
Markdown link labels count, URLs do not.

Usage: python3 tools/count-words.py page.md [more.md ...] [--min 500 --max 700]
Exit 1 if any file is outside the range.
"""
import re, sys, argparse
ap = argparse.ArgumentParser()
ap.add_argument('files', nargs='+'); ap.add_argument('--min', type=int, default=500); ap.add_argument('--max', type=int, default=700)
a = ap.parse_args()
bad = 0
for fn in a.files:
    t = open(fn, encoding='utf-8').read()
    t = re.sub(r'<!--.*?-->', ' ', t, flags=re.S)
    out = []
    for line in t.split('\n'):
        s = line.strip()
        if not s: continue
        if re.match(r'^!\[', s): continue
        if re.match(r'^\[Image Source\]', s, re.I): out.append('Image Source'); continue   # the caption is visible text
        if re.match(r'^\|\s*-{2,}', s): continue
        if s.lower().startswith('disclaimer:'): continue
        s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)   # links -> label
        if re.match(r'^\s{0,3}#{1,6}\s+', s):
            s = re.sub(r'^\s{0,3}#{1,6}\s+', '', s)          # heading marks; a "1." inside a heading is visible text
        else:
            s = re.sub(r'^\s*(?:[-*+]|\d+\.)\s+', '', s)     # list marks
        s = s.replace('|', ' ').replace('**', '')
        out.append(s)
    n = len(re.findall(r"\S+", ' '.join(out)))
    ok = a.min <= n <= a.max
    print(f"{n:5d} words  {'ok ' if ok else 'OUT'}  {fn}")
    bad += (not ok)
sys.exit(1 if bad else 0)
