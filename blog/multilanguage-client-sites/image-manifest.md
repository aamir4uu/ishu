# Image Manifest: Multi-Language Client Sites

Three images, each placed in the draft with descriptive alt text and an "Image
Source" line directly beneath it, hyperlinked to the image's own page.

## The files still need downloading and uploading

Outbound access to `pexels.com` is blocked in the environment that produced this
draft, so the image files could not be downloaded and re-hosted. Each URL below
was returned by search as a real Pexels photo page, but the `![...]()` markdown
currently points at the photo page rather than an uploaded asset, and the .docx
carries a sized placeholder frame in each slot.

For each image: open the source URL, download the file, upload it to the Sitejet
media library, then replace the URL inside the `![alt text](...)` markdown (or
the placeholder box in the .docx). Leave the "Image Source" link underneath
pointing at the original Pexels page.

All three are Pexels, free for commercial use with no attribution required. The
credit line is there because the brief asks for it.

## The images

| # | Placement | Alt text | Source URL |
| --- | --- | --- | --- |
| 1 | Below the opening answer, above Key Takeaways | Laptop on a desk showing a world map on screen, set up for a multi-language website build | https://www.pexels.com/photo/laptop-with-world-map-on-screen-on-table-7411970/ |
| 2 | End of "A Multi-Language Client Site Workflow That Holds" | Person working at a laptop and underlining words in a dictionary during translation review | https://www.pexels.com/photo/close-up-of-woman-sitting-at-the-desk-with-a-laptop-and-underlining-words-in-a-book-5238126/ |
| 3 | End of "Where Sitejet Studio Carries the Weight" | World map on a wall above a desk with a laptop, planning a website for several countries | https://www.pexels.com/photo/world-map-on-wall-and-laptop-near-cup-and-container-7411982/ |

Images 1 and 3 are by the same photographer and share a world-map motif. That
reads as a deliberate pair, but if it feels repetitive, swap image 3 for
https://www.pexels.com/photo/desk-globe-standing-on-books-7635155/ (alt: "Desk
globe standing on a stack of books beside a laptop").

## Before upload

Checklist item 2.6 wants the keyword in alt text where it reads naturally.
Image 1 carries "multi-language website". Images 2 and 3 describe what is in
the frame rather than repeating the phrase.

Two things to do at upload time:

- Compress and convert to WebP. Target under 150KB each at 1200px wide.
- Set explicit width and height attributes so the images do not shift layout
  while the page loads.
