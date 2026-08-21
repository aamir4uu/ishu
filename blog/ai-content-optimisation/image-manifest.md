# Image Manifest

Three images. Each one sits in the draft with descriptive alt text and an
"Image Source" line directly beneath it, hyperlinked to the image's own page,
as the brief requires.

## The files still need downloading and uploading

This draft was produced in a sandboxed environment with outbound access
restricted, so `pexels.com` and `images.pexels.com` could not be reached. The
image **files** could not be downloaded or re-hosted. Every URL below was
confirmed through search and points at a real Pexels photo page, but the
`![...]()` markdown currently points at the photo page rather than at an
uploaded asset, and the .docx carries a sized placeholder frame with the alt
text and the source link beside it.

For each image: open the source URL, download the file, upload it to the XOVI
media library, and replace the URL inside the `![alt text](...)` markdown with
the uploaded asset path. Leave the "Image Source" link underneath pointing at
the original Pexels page.

All three are Pexels, free for commercial use with no attribution required. The
credit line is there because the brief asks for it, not because the licence
demands it.

## The images

| # | Placement | Alt text | Source URL |
| --- | --- | --- | --- |
| 1 | Below the opening answer, above Key Takeaways | Monitor screen showing a ChatGPT landing page, the starting point for any AI content optimisation check | https://www.pexels.com/photo/monitor-screen-showing-chatgpt-plus-landing-page-15863103/ |
| 2 | End of "Four Fixes That Make a Page Legible to a Machine" | A person editing written content on a laptop while taking notes | https://www.pexels.com/photo/person-writing-on-notebook-while-using-a-laptop-5387268/ |
| 3 | Above "Frequently Asked Questions" | A laptop screen displaying an analytics graph used to track AI visibility over time | https://www.pexels.com/photo/graph-displayed-on-laptop-screen-7567486/ |

## Alt text and the keyword

Checklist item 2.6 asks for the keyword in alt text where it reads naturally.
Image 1 carries it. Images 2 and 3 describe what is actually in the frame,
because "AI content optimisation" welded onto a photo of a laptop is stuffing,
and a screen reader user gets nothing from it.

## Before upload

- Compress and convert to WebP. Target under 150KB each at 1200px wide.
- Set explicit width and height attributes so the images do not shift the layout
  while the page loads.
- Check that image 1 still shows a current ChatGPT interface. Screenshots of AI
  products date faster than any other stock category, and a visibly old UI
  undercuts an article about AI search.
