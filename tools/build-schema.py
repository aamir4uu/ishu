#!/usr/bin/env python3
"""
build-schema.py - regenerate an article's JSON-LD from its live copy.

The FAQPage block is pulled out of the article's own FAQ section rather than
maintained by hand, so editing an answer and forgetting to update the schema
cannot happen. Article and HowTo metadata live in schema-config.json beside the
article, because they are not derivable from the prose.

Usage:
    python3 tools/build-schema.py blog/<slug>/
"""

import json
import re
import sys
from pathlib import Path

PUBLISHER = {
    "@type": "Organization", "name": "Hero FinCorp Limited",
    "url": "https://www.herofincorp.com/",
    "logo": {"@type": "ImageObject", "url": "https://www.herofincorp.com/logo.png"},
}


def faq_pairs(md: str, faq_heading: str):
    out, inblock, q, buf = [], False, None, []
    for line in md.split("\n"):
        if line.startswith("## "):
            if inblock and q:
                out.append((q, " ".join(buf).strip()))
            inblock = faq_heading in line
            q, buf = None, []
            continue
        if not inblock:
            continue
        if line.startswith("### "):
            if q:
                out.append((q, " ".join(buf).strip()))
            q, buf = line[4:].strip(), []
        elif line.strip() and q:
            buf.append(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line.strip()))
    if inblock and q:
        out.append((q, " ".join(buf).strip()))
    return [p for p in out if p[1]]


def main() -> int:
    folder = Path(sys.argv[1])
    cfg = json.loads((folder / "schema-config.json").read_text(encoding="utf-8"))
    md = (folder / f"{folder.name}.md").read_text(encoding="utf-8")
    url = cfg["url"]
    pairs = faq_pairs(md, cfg["faq_heading"])
    if not pairs:
        print(f"error: no FAQ pairs found under {cfg['faq_heading']!r}", file=sys.stderr)
        return 1
    doc = {"@context": "https://schema.org", "@graph": [
        {"@type": "FAQPage", "@id": f"{url}#faq", "inLanguage": cfg["lang"],
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}}
                        for q, a in pairs]},
        {"@type": "Article", "@id": f"{url}#article", "headline": cfg["headline"],
         "description": cfg["description"], "inLanguage": cfg["lang"],
         "keywords": cfg["keywords"], "image": cfg["image"],
         "mainEntityOfPage": {"@type": "WebPage", "@id": url},
         "publisher": PUBLISHER,
         "author": {"@type": "Person", "name": "REPLACE WITH NAMED AUTHOR",
                    "url": "REPLACE WITH AUTHOR LINKEDIN URL"},
         "datePublished": "REPLACE ON PUBLISH", "dateModified": "REPLACE ON PUBLISH"},
        {"@type": "HowTo", "@id": f"{url}#howto", "name": cfg["howto"]["name"],
         "inLanguage": cfg["lang"],
         "step": [{"@type": "HowToStep", "position": i, "name": n, "text": t}
                  for i, (n, t) in enumerate(cfg["howto"]["steps"], 1)]},
    ]}
    (folder / "schema-markup.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{folder.name}: {len(pairs)} FAQ pairs, "
          f"{len(cfg['howto']['steps'])} HowTo steps")
    return 0


if __name__ == "__main__":
    sys.exit(main())
