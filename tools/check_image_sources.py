#!/usr/bin/env python3
"""Check that every image in a draft has a usable "Image source" link.

The client checklist says each image needs an "Image source" line beneath it,
hyperlinked so it takes the reader to the image. A link to a site's front page
satisfies the letter of that and none of the intent, which is exactly the
mistake this catches: it lands you on facebook.com, not on the photo.

Rules enforced:

  1. Every ``![alt](path)`` is followed by an italic "Image source" line.
  2. Every image has non-empty alt text.
  3. The source URL is a deep link, not a bare domain or a lone trailing slash.
  4. The source URL points at an image file, not at a web page that happens to
     contain one. Clicking it has to show you the photo.
  5. Every referenced image file actually exists on disk.
  6. Text sits between a heading and an image, per the brand guidelines.

    python3 tools/check_image_sources.py blog/slug/article.md

Exit status is non-zero if anything fails, so it can gate a build.
"""

import os
import re
import sys
from urllib.parse import urlparse

IMAGE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$")
SOURCE = re.compile(r"^\*\[Image source\]\(([^)]+)\)\*\s*$", re.I)
HEADING = re.compile(r"^#{1,6}\s")

# Paths that mean "the front page" and nothing more.
EMPTY_PATHS = {"", "/", "/index.html", "/home"}

IMAGE_EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".svg")

# GitHub serves a viewer page at /blob/ and the file itself at raw.
# The blob URL renders the image inside a page, which is not the same thing.
PAGE_NOT_FILE = ("/blob/",)


def check(path):
    base = os.path.dirname(os.path.abspath(path))
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    problems = []
    images = 0
    last_meaningful = None

    for i, raw in enumerate(lines):
        line = raw.strip()
        if not line:
            continue

        m = IMAGE.match(line)
        if not m:
            if not SOURCE.match(line):
                last_meaningful = line
            continue

        images += 1
        alt, src = m.group(1).strip(), m.group(2).strip()
        where = f"{path}:{i + 1}"

        if not alt:
            problems.append(f"{where}: image has no alt text ({src})")

        if not urlparse(src).scheme:
            on_disk = os.path.normpath(os.path.join(base, src))
            if not os.path.isfile(on_disk):
                problems.append(
                    f"{where}: image file does not exist: {src}\n"
                    f"    Either generate it or take the image out of the "
                    f"draft. A reference to a file nobody has captured is not "
                    f"an image."
                )

        if last_meaningful is not None and HEADING.match(last_meaningful):
            problems.append(
                f"{where}: image sits directly under a heading. The brand "
                f"guidelines want text between a heading and an image."
            )

        # Find the source line: the next non-blank line.
        j = i + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if j >= len(lines):
            problems.append(f"{where}: no 'Image source' line beneath the image")
            continue
        sm = SOURCE.match(lines[j].strip())
        if not sm:
            problems.append(
                f"{where}: next line is not an 'Image source' link, it is "
                f"{lines[j].strip()[:60]!r}"
            )
            continue

        url = sm.group(1).strip()
        parsed = urlparse(url)
        sloc = f"{path}:{j + 1}"

        if parsed.scheme not in ("http", "https"):
            problems.append(f"{sloc}: source link is not an http(s) URL: {url}")
            continue
        if parsed.path in EMPTY_PATHS and not parsed.query:
            problems.append(
                f"{sloc}: source link is a bare domain, {url}\n"
                f"    It has to be the exact page or file the image comes "
                f"from, not the site's front page."
            )
        if re.search(r"/blog/[a-z0-9-]+/?$", parsed.path) and "image" not in url:
            problems.append(
                f"{sloc}: source link points at an article page, {url}\n"
                f"    For an original graphic, link the image file itself."
            )
        elif not parsed.path.lower().endswith(IMAGE_EXT):
            problems.append(
                f"{sloc}: source link is a web page, not an image file: {url}\n"
                f"    It has to end in one of {', '.join(IMAGE_EXT)} so that "
                f"clicking it shows the photo itself."
            )
        elif any(marker in parsed.path for marker in PAGE_NOT_FILE):
            problems.append(
                f"{sloc}: source link is a file viewer page, not the file: "
                f"{url}\n    Use the raw file URL instead."
            )

    return images, problems


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    failed = False
    for path in sys.argv[1:]:
        images, problems = check(path)
        if problems:
            failed = True
            print(f"{path}: {len(problems)} problem(s) across {images} image(s)")
            for p in problems:
                print(f"  - {p}")
        else:
            print(f"{path}: OK, {images} image(s), all present on disk, "
                  f"every source links straight to an image file")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
