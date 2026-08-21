# Image Manifest

Two images, each placed in the draft with descriptive alt text and an "Image
Source" line directly beneath it, hyperlinked to the image's own page as the
brief requires.

## Important: the files still need downloading and uploading

Produced in a sandboxed environment where outbound access to `pexels.com` and
`images.pexels.com` was blocked by the network egress proxy, so the image
**files** could not be downloaded or re-hosted. Both URLs below were confirmed
through search and point at a real Pexels photo page, but the `![...]()`
markdown in the draft currently points at the photo page rather than at an
uploaded asset.

Before publishing, for each image: open the source URL, download the file,
upload it to the SolusVM CMS media library, and replace the URL inside the
`![alt text](...)` markdown with the uploaded asset path. Leave the "Image
Source" link underneath pointing at the original Pexels page.

Both are Pexels, free to use commercially with no attribution required. The
credit line is there because the client asked for it, not because the licence
demands it.

## The images

| # | Placement | Alt text | Source URL |
| --- | --- | --- | --- |
| 1 | Below the opening answer, above Key Takeaways | Rows of servers in a data center rack, the hardware a SolusVM HA failover domain protects | https://www.pexels.com/photo/server-racks-on-data-center-5480781/ |
| 2 | End of "What Happens to Your Virtual Servers During Failover?" | Network cables connected to a server rack, the fabric a failover domain runs across | https://www.pexels.com/photo/ethernet-cables-plugged-on-a-server-rack-1054397/ |

Alt text carries the primary keyword terms ("SolusVM HA failover", "failover
domain") without keyword stuffing, per checklist item 2.6.

## Note on reuse

Both images are the same two used in `blog/vps-storage-choice/`. If the two
SolusVM articles publish close together, swap at least one so the pair does not
look templated. This one fits and was shortlisted:

| Placement | Alt text | Source URL |
| --- | --- | --- |
| Either slot | Cables connected to a server in a data center rack | https://www.pexels.com/photo/cables-connected-on-server-2881229/ |

Alt text in the draft would need updating to match if you swap.
