# Image Manifest: AI Visibility Audit

Three images, each placed in the draft with descriptive alt text and an "Image
Source" line directly beneath it, hyperlinked to the image's own Pexels page.

## The files still need downloading and uploading

Outbound access to `pexels.com` is blocked in the environment that produced this
draft, so the image files could not be downloaded or re-hosted. Each URL below
was confirmed through search and points at a real Pexels photo page, but the
`![...]()` markdown currently points at the photo page rather than an uploaded
asset, and the .docx carries a sized placeholder frame in each slot.

For each image: open the source URL, download the file, upload it to the XOVI
media library, then replace the URL inside the `![alt text](...)` markdown (or
the placeholder box in the .docx). Leave the "Image Source" link underneath
pointing at the original Pexels page.

All three are Pexels, free for commercial use with no attribution required. The
credit line is there because the brief asks for it, not because the licence
demands it.

## The images

| # | Placement | Alt text | Source URL |
| --- | --- | --- | --- |
| 1 | Below the opening answer, above Key Takeaways | A marketer typing a question into ChatGPT on a laptop during an AI visibility audit | https://www.pexels.com/photo/man-using-laptop-wit-chat-gpt-16094045/ |
| 2 | End of "What Does an AI Visibility Audit Actually Check?" | A laptop on a desk showing graphs from a monthly AI visibility report | https://www.pexels.com/photo/a-laptop-showing-graphs-7109316/ |
| 3 | End of "How Do You Turn the Audit Into a Client Deliverable?" | An AI chat interface open on a computer screen during a client audit | https://www.pexels.com/photo/ai-chat-interface-on-computer-screen-30530407/ |

Note that the Pexels slug for image 1 really does read "wit" rather than
"with". That is the photographer's typo in the page URL, not ours. Do not
correct it or the link breaks.

## Before upload

Checklist item 2.6 wants the keyword in alt text where it reads naturally.
Images 1 and 2 carry "AI visibility". Image 3 describes what is in the frame
rather than forcing the phrase in a third time.

Two things to do at upload time:

- Compress and convert to WebP. Target under 150KB each at 1200px wide.
- Set explicit width and height attributes so the images do not shift layout
  while the page loads.
