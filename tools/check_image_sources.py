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

A slot awaiting a screenshot is not a failure, as long as it says so. Mark it:

    *Image source: pending capture, see image-manifest.md*

Those are reported as PENDING rather than passed off as done. Run with
``--strict`` before handing the draft over and pending slots become failures,
so an uncaptured screenshot cannot reach a publisher unnoticed.

    python3 tools/check_image_sources.py blog/slug/article.md

Exit status is non-zero if anything fails, so it can gate a build.
"""

import os
import re
import sys
from urllib.parse import urlparse

IMAGE = re.compile(r"^!\[([^\]]*)\]\(([^)]+)\)\s*$")
SOURCE = re.compile(r"^\*\[Image source\]\(([^)]+)\)\*\s*$", re.I)
PENDING = re.compile(
    r"^\*Image source: pending capture, see image-manifest\.md\*\s*$", re.I)
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
    pending = []
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

        # Find the source line first: a slot marked pending is allowed to be
        # missing its file, because that is precisely what pending means.
        k = i + 1
        while k < len(lines) and not lines[k].strip():
            k += 1
        is_pending = k < len(lines) and PENDING.match(lines[k].strip())

        if is_pending:
            pending.append(f"{where}: awaiting capture, {src}")

        if not is_pending and not urlparse(src).scheme:
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

        if is_pending:
            continue

        j = k
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

    return images, problems, pending


def main():
    if len([a for a in sys.argv[1:] if not a.startswith("--")]) < 1:
        print(__doc__)
        return 2
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    failed = False
    for path in args:
        images, problems, pending = check(path)
        if problems:
            failed = True
            print(f"{path}: {len(problems)} problem(s) across {images} image(s)")
            for p in problems:
                print(f"  - {p}")
        else:
            done = images - len(pending)
            print(f"{path}: OK, {done} of {images} image(s) final, every "
                  f"source links straight to an image file")
        if pending:
            if strict:
                failed = True
            label = "FAILED (--strict)" if strict else "pending"
            print(f"  {len(pending)} slot(s) {label}:")
            for p in pending:
                print(f"  - {p}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
