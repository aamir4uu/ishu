# Publishing Pack: SolusVM HA Failover

Everything the CMS needs, plus the AEO/SEO checklist worked line by line.

## Metadata

| Field | Value | Check |
| --- | --- | --- |
| Title tag | SolusVM HA Failover: What Happens When a Node Fails (2026) | 58 chars, under the 60 limit, primary keyword plus year |
| H1 | What Happens When a Node Fails? A Look Inside SolusVM HA Failover | Client-supplied headline, kept verbatim. APA title case, and "A" is capitalised because it follows end punctuation |
| Meta description | Inside SolusVM HA failover: how the storage lock detects a dead node, what happens to your virtual servers, and what HA will not do for you. Updated 2026. | 154 chars, inside 150-160 |
| URL slug | `/solusvm-ha-failover` | Short, keyword-rich, no stop words |
| Primary keyword | SolusVM HA failover | |
| Secondary keywords | failover domain, compute resource failure, high availability VPS, storage lock, watchdog, disaster recovery, virtual server evacuation | |
| Audience | Small to mid-sized hosting providers and VPS resellers | |
| Point of view | Second person | |
| CTA destination | SolusVM features page (`/features/`) | |

## Assumptions flagged for the client

Task Info was **N/A** again, so key points, personas and target keywords had no
source document. These were inferred from the headline and the SolusVM brand
guide:

- Primary keyword set to **SolusVM HA failover**. It appears in the H1, the
  title tag, the first sentence, one H2 and one FAQ H3, so a change touches five
  places plus the slug.
- Audience read as the brand guide's stated primary audience: small to
  mid-sized hosting providers and VPS resellers. KVM, iSCSI, NFS, watchdog and
  split brain are used without definition, per the tone rules.
- Search volume and difficulty were not checked in Ahrefs or Semrush. That is
  checklist item 1.1 and still needs doing.

## Length

Target was 800-1000 words with up to 25% over accepted. The article is
**1,029 words** of body copy, or roughly 1,120 including headings and excluding
image credit lines. That sits inside the accepted range.

## Checklist status

### 1. Before you write

| Item | Status |
| --- | --- |
| Confirm primary keyword, check volume in Ahrefs / Semrush | **Open.** Keyword proposed, volume not verified. No keyword tool access in this environment. |
| Research People Also Ask questions | Done. Two question H2s and all five FAQ H3s are PAA-shaped. |
| Check top 3 ranking pages | **Open.** Competitor set was N/A in the brief, and `solusvm.com` plus `docs.solusvm.com` were both blocked by the network egress proxy here. |
| Confirm CTA destination | Done. SolusVM features page. |

### 2. On-page SEO

| Item | Status |
| --- | --- |
| Title tag with keyword and year, under 60 chars | Done. 58 chars, includes 2026. |
| Meta description 150-160 chars with keyword and value prop | Done. 154 chars. |
| H1 mirrors title tag | Done. Client headline kept; title tag reorders it keyword-first. |
| Keyword in first 100 words and in at least one H2 | Done. First sentence, plus "How Does SolusVM Know a Compute Resource Has Failed?" and "What HA Failover Does Not Do". |
| Slug short, keyword-rich, no stop words | Done. `/solusvm-ha-failover`. |
| Descriptive alt text with keyword where natural | Done. See `image-manifest.md`. |

### 3. Content structure (AEO)

| Item | Status |
| --- | --- |
| 40-60 word direct answer at the very top | Done. 50 words, directly under the H1, and it answers the title question literally. |
| Key Takeaways box near the top, 4-5 bullets | Done. Five bullets, deliberately uneven lengths. |
| PAA questions as H2 or H3 | Done. Two question H2s and five FAQ H3s. |
| FAQ section at the bottom, 5-8 Q&A pairs | Done. Five pairs. |

### 4. Schema markup (client reference only)

| Item | Status |
| --- | --- |
| FAQ schema | Done. All five Q&A pairs, generated from the live copy. |
| HowTo schema | Done. Six prerequisite steps for standing up a failover domain. |
| Article schema with author, datePublished, dateModified | Structure done, plus a `citation` node for the Backblaze source. Author name, LinkedIn URL and both dates are `REPLACE WITH` placeholders. |
| SoftwareApplication schema | Done. SolusVM, with the HA and DR feature list. |

All in `schema-markup.json` as a single `@graph`.

### 5. E-E-A-T and trust signals

| Item | Status |
| --- | --- |
| Author bio with name, role, LinkedIn | **Open.** No author was supplied. The schema carries placeholders. |
| 'Last updated' date shown and kept current | **Open.** CMS-side. |
| At least one external authoritative source cited | Done. Backblaze 2025 Drive Stats, linked in Key Takeaways. |
| Avoid generic AI-sounding sentences | Done. Drafted and gated with the repo's humanizer skill v3.0.0. See `zerogpt-preflight-result.txt`. |

### 6. Internal linking

| Item | Status |
| --- | --- |
| Minimum 3 internal links | Done. Five: the High Availability doc, the Shared LVM storage doc, the Disaster Recovery doc, the storage article, and the features page in the CTA. |
| Anchor text uses exact or partial-match keywords | Done. "failover domain", "Shared LVM over iSCSI or NFS", "Disaster Recovery", "storage design behind the failover domain", "See how High Availability and Disaster Recovery fit together in SolusVM". No "click here". |
| Update older blog posts to link to this new article | **Done in repo.** A link to this article was added to the FAQ answer "Can I Use Local Storage and Still Offer High Availability?" in `blog/vps-storage-choice/`. That article was re-gated after the edit and still passes 11/11. Both articles reference each other, so publish order matters: whichever goes second, fix the first one's URL. |

### 7. GEO

| Item | Status |
| --- | --- |
| At least one specific, citable data point | Done. Backblaze 2025 annualised drive failure rate of 1.36% across 344,196 drives, the 2,000 compute resource domain limit, the two-node minimum, and the storage-lock detection mechanism. |
| Brand name used consistently and exactly | Done. "SolusVM" throughout, capital S, capital V, capital M, one word. |
| After publishing, test target query in ChatGPT, Perplexity, Gemini | **Open.** Post-publish task. |

## Brand guide compliance

| Guideline | How the draft handles it |
| --- | --- |
| Documentation-like, not brochure-like | The piece explains a mechanism, in order, and names its limits. |
| Clear, honest communication, no vague promises | The core argument is that HA is a restart, not a continuation, and that "no downtime" is not a promise a provider can keep. Section "What HA Failover Does Not Do" exists for this reason. |
| No vague language | "powerful", "cutting-edge", "next-level" and "seamless" appear nowhere. |
| Don't define basics | KVM, iSCSI, NFS, watchdog, split brain and journal replay are used unexplained. |
| Claims tie to operational outcomes | Ticket volume, restore hours, capacity headroom left idle, what you can promise a customer. |
| Differentiators referenced where relevant | Operational simplicity (HA handles placement automatically) and reliability without surprises (the false-failover protection). |
| No performance or uptime claims without specifics | No timing figure is invented. The FAQ on failover duration explicitly refuses to give an estimate and tells you to test on your own hardware. |

## Note on the contraction rate

The humanizer gate for contractions passed at 5.83 per 1k against a 4.0 floor,
against 12.58 on the storage article and 22.67 on an earlier piece for a
different client. The SolusVM register is close to technical documentation and
does not carry contractions well. This is a known conflict between the brand
guide and the detector signal, logged in the skill. Compensated on rhythm
instead: sentence length CV 0.571, paragraph variance 0.506, both comfortably
above their floors.

## Open items before publishing

1. Confirm the primary keyword (`SolusVM HA failover`) and check its volume.
2. Upload the two images and repoint the `![]()` URLs. Pexels was blocked by the
   network egress proxy here. Both images are shared with the storage article,
   so swap one if the two publish together. See `image-manifest.md`.
3. Replace the placeholder author with a named person, role and personal
   LinkedIn URL, in the post and in `schema-markup.json`.
4. Verify the three SolusVM documentation URLs resolve. `docs.solusvm.com` was
   blocked here, so they came from search results. Every mechanism they support
   (storage lock and watchdog detection, the network-partition behaviour, the
   two-node minimum, the 2,000 resource limit, KVM plus Shared LVM or NFS only,
   no Virtuozzo, dedicated storage per domain, the global toggle, manual
   failback, and Disaster Recovery restoring from backups one by one) was
   confirmed in more than one search result.
5. Fix the cross-links once both SolusVM articles have real URLs.
6. Confirm the grace period wording matches your own configuration UI. The
   article treats it as an administrator-set value rather than quoting a
   default, because no default could be verified from here.
7. After publishing, test the target query in ChatGPT, Perplexity and Gemini.
