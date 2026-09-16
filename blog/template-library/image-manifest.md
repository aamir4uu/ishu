# Image Manifest: Agency Template Library

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
| 1 | Below the opening answer, above Key Takeaways | Designer sketching a website layout on paper at a desk | https://www.pexels.com/photo/faceless-designer-drawing-on-paper-while-working-on-project-7147490/ |
| 2 | End of "What Goes in an Agency Template Library" | A spread of colour swatches on a desk, the raw material of a reusable design system | https://www.pexels.com/photo/pantone-color-chart-9421350/ |
| 3 | End of "Where Sitejet Studio Fits" | Layout sketches and drawing tools spread across a designer's desk | https://www.pexels.com/photo/person-people-building-desk-6615235/ |

Image 3's Pexels title calls them architectural sketches. Check the frame reads
as layout work rather than a building plan once you see it; if not, use
https://www.pexels.com/photo/hand-of-a-person-fanning-color-swatches-6583363/
(alt: "Hand fanning out a set of colour swatches") and drop image 2 for
https://www.pexels.com/photo/colorful-sticky-notes-taped-to-schedule-on-whiteboard-15505432/
(alt: "Colour-coded sticky notes on a project schedule whiteboard"), which was
shortlisted for the delivery SOP piece and never used.

## Before upload

Checklist item 2.6 wants the keyword in alt text where it reads naturally.
"Template library" doesn't describe anything a photo can show, so the alt text
describes the frames instead: layouts, swatches, sketches. Image 1 carries
"website layout", the closest natural phrase.

Two things to do at upload time:

- Compress and convert to WebP. Target under 150KB each at 1200px wide.
- Set explicit width and height attributes so the images do not shift layout
  while the page loads.
