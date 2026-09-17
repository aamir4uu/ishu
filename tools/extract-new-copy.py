#!/usr/bin/env python3
"""Print only the copy between <!-- NEW SECTION START: ... --> and <!-- NEW SECTION END -->
markers in a refreshed page, so the humanizer pre-flight can gate the new words on
their own. Usage: python3 tools/extract-new-copy.py page.md > page-new-copy.md"""
import re, sys
text = open(sys.argv[1], encoding="utf-8").read()
blocks = re.findall(r"<!--\s*NEW SECTION START:(.*?)-->\n(.*?)<!--\s*NEW SECTION END\s*-->", text, flags=re.S)
for label, body in blocks:
    print(body.strip())
    print()
