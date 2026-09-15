# Operating Workflow — Goyal Lights on Meesho

One page per rhythm: the launch fortnight, the daily loop, the weekly review, and the
festive calendar. Print the daily loop and stick it near the packing table.

## A. Launch fortnight (do once)

| Day | Task | Owner | Output |
| --- | --- | --- | --- |
| 1 | Apply GSTIN (if not done). Register on Supplier Panel. | You | Supplier ID |
| 1 | Answer `01-questions-for-you.md`. | You | Costs, weights, SKU confirmation |
| 2 | Shoot 5 phone photos per SKU on white paper (front, angle, lit-up in a dark room, carton with BIS/MRP label, scale reference). | Shop boy | 90 raw photos |
| 2–3 | Run each raw photo through the ChatGPT prompts in `05-image-prompts.md`. Save as `SKU-1.jpg` … `SKU-5.jpg`, 1500×1500, under 5 MB. | You / me | Meesho-ready images |
| 3 | Download bulk templates per category from the panel; send to me. | You | Template files |
| 3 | I fill templates from `04-catalog-listings.xlsx` with prices from `03-pricing-calculator.xlsx`. | Me | Filled templates |
| 4 | Upload templates. Open each product and add images. Submit for QC. | You | Catalogs "Under QC" |
| 4–7 | QC takes 24–72 h. Fix rejections the same day (usual reasons: image not square, text on image, wrong category, description too long). | You + me | Catalogs live |
| 7 | Buy packaging: 3 box sizes, bubble wrap, tape, fragile stickers, thermal label printer or A4 labels. | You | Packing station |
| 8–14 | Turn on Meesho Ads on 3 hero SKUs at ₹300/day. Ask the first 10 buyers (via the order's chat is not possible, so via a printed thank-you card) to rate. | You | First reviews |

## B. Daily loop (every working day, 30–45 min)

**Morning (10:00)**
1. Open Supplier app → **Orders → Pending**. Accept everything in stock. Anything not in stock: cancel *now* (penalty is smaller than a late dispatch plus a cancel).
2. Print labels + invoices (**Orders → Download Label**). Meesho generates the invoice; you do not write one.
3. Pack: item → bubble wrap → box → invoice inside → label outside → fragile sticker on bulbs/chandeliers. **Weigh the packed box**; if it is over the slab you declared, fix the catalog weight tonight.
4. Mark **Ready to Ship** before the pickup cut-off (usually 1–2 pm for same-day pickup).

**Afternoon (pickup)**
5. Hand over to the courier, count parcels against the manifest, keep the signed manifest sheet for 30 days.

**Evening (18:00)**
6. **Returns → Pending**. For each returned parcel received: open it on video before cutting the tape (phone on a stand, label visible). Wrong or damaged item back → raise a **claim** within 7 days with the video. No video, no claim.
7. **Catalog → QC rejected** — fix and resubmit.
8. **Inventory** — set any SKU under 5 pieces to out-of-stock rather than risk a cancel.

## C. Weekly review (Monday, 1 hour)

| Check | Where | Action |
| --- | --- | --- |
| Orders per SKU, last 7 days | Panel → Reports | Top 3 sellers → add pack-of-2 / pack-of-4 variants; zero-order SKUs after 3 weeks → cut price 10% or improve image 1 |
| Return % per SKU | Reports → Returns | Above 12% → check listing promises vs product; usually wrong length/colour expectation in title |
| Ads: cost per order | Ads dashboard | Above 25% of price → pause that SKU's ad; below 12% → raise budget 30% |
| Ratings under 3 | Reviews | Reply is not possible, but read them: every 1-star for "not working" means a QC step in packing |
| Price vs. top 5 competitors for your hero keywords | Search Meesho as a buyer | Match within ₹10 or beat on pack size |
| Payout reconciliation | Payments → Reports | Match to bank; query missing settlements within 15 days |
| Stock reorder | Your notebook | Reorder anything under 2 weeks of sales |

## D. Festive calendar 2026–27

| Date | What | Listing deadline |
| --- | --- | --- |
| 20 Sep 2026 | Navratri starts; string-light searches begin rising | Jhalar/ladi/curtain live by **15 Sep** |
| 1 Oct | Meesho Diwali sale events open for enrolment | Enrol hero SKUs, keep 20% stock aside |
| 6 Nov 2026 | Dhanteras; peak week is 30 Oct–6 Nov | Ads at 2× budget from 25 Oct; holiday mode only on Diwali day itself |
| 15 Nov | Wedding season; chandeliers, pendants, warm-white curtains | Lifestyle images (living room, mandap) as image 2 |
| 10 Dec | Christmas / New Year; warm white and star strings | Relist the same jhalar with "Christmas" in title variant |
| Jan–Mar 2027 | Bulbs, panels, battens (housing hand-overs, offices) | Push pack-of-10 bulbs; ads on "9w led bulb" |
| Aug 2027 | Diwali 2027 import stock lands (from the sourcing pack) | New listings drafted in July |

## E. Packaging spec

| Box | Inside dims (cm) | For | Padding |
| --- | --- | --- | --- |
| S | 15 × 12 × 8 | Bulb packs, 10–20 m serial, strip reels | Bubble wrap 1 layer |
| M | 25 × 20 × 12 | 30–50 m serial, curtain lights, panels, battens (4 ft in tube) | Bubble wrap + paper fill |
| L | 40 × 30 × 25 | Chandeliers, pendants, flood lights | Bubble wrap 2 layers, corner blocks, "Fragile / This side up" |

Weigh each packed configuration once and enter that weight in the catalog. Meesho charges the higher of declared and measured weight.

## F. What "taking control of your PC" would look like

The parts that need a browser on your machine are: registering, uploading images, submitting catalogs, printing labels, running ads. If you want those automated end-to-end you need a local agent (Claude Code on your PC with a browser tool, or a computer-use agent) logged into the Supplier Panel. Steps:

1. Install Claude Code on the PC that stays at the shop.
2. Log in to supplier.meesho.com in Chrome once, and keep that Chrome profile.
3. Give the agent this repo folder; it has every listing, price and image prompt.
4. Start with "upload the 18 catalogs in `meesho/04-catalog-listings.xlsx`" and watch the first 3 before leaving it alone.

Until then, the split is: I prepare, you click.
