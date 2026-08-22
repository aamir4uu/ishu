# Website Build & Connector Guide

The site is built on **Lovable** (React + Tailwind + shadcn/ui).

- **Editor:** https://lovable.dev/projects/8deba5b4-3083-4bb7-92b2-ea1ac69339c5
- **Preview:** https://id-preview--8deba5b4-3083-4bb7-92b2-ea1ac69339c5.lovable.app

---

## 1. The map — why there is no API key

The site uses Google's **keyless embed iframe**:

```
https://www.google.com/maps?q=Bhagirath+Palace,+Chandni+Chowk,+New+Delhi,+Delhi+110006&output=embed
```

No API key, no Google Cloud account, no billing card, no usage cap. For a shop
that needs to show one pin and an "Open in Google Maps" link, this is the right
call — and it is what most well-built local business sites actually use.

**Upgrade to the Google Maps Platform connector only if you want:**

- a custom-styled dark map that matches the site instead of a filtered iframe
- a "Directions from your location" widget
- your live Google Business Profile rating and review count pulled onto the page
- multiple pins, once you have a second shop or a godown

That path needs a Google Cloud project with billing enabled. Google gives a
recurring free monthly credit that a single shop site will not exhaust, but a
card still has to be on file. **Not worth doing before your Google Business
Profile is verified** — once it is, swap the iframe for your real `place_id`
embed, which is a one-line change. The code has a comment marking the spot.

---

## 2. Connectors — what to actually turn on, and when

Lovable has 80+ connectors. Almost all of them are wrong for a shop of this
size. Ranked by whether they earn their setup time:

### Turn on now — nothing

The site captures leads by **composing a WhatsApp message and deep-linking to
`wa.me`**. No database, no email service, no backend, nothing to maintain, and
it lands the enquiry in the one inbox you actually check all day. For a shop
doing wholesale over WhatsApp, that beats a contact form that emails you.

### Turn on within the first month

| Connector | Why | Setup |
| --- | --- | --- |
| **Google Analytics** | You need to know whether the site produces enquiries before you spend anything on ads. Track clicks on the WhatsApp buttons as events — that is your real conversion, not pageviews. | Free, 20 min |
| **Google Search Console** | Tells you which queries you actually appear for. Pairs with `03-marketing-plan.md` — this is how you find out if "bhagirath palace light market" is sending you traffic. | Free, 15 min |

### Consider after Diwali, if the season proves the site works

| Connector | Why | Cost |
| --- | --- | --- |
| **Lovable Cloud** | Adds a real database. Worth it only when you want the enquiry form to store leads so nothing gets lost in a busy WhatsApp inbox, or when you want a rate list that you can update without a code change. | Free tier, then paid |
| **Resend** or **Brevo** | Emails you a copy of every enquiry as a backup. Only needed once someone other than you is handling WhatsApp. | Free tier |
| **Twilio** or **GatewayAPI** | SMS for order-dispatch alerts to out-of-Delhi buyers. Real value for wholesale, but only once order volume justifies it. | Pay per SMS |
| **PostHog** | Session recordings — watch where buyers drop off on mobile. Genuinely useful, but only when you have enough traffic for patterns to appear. | Free tier |

### Do not turn on

| Connector | Why not |
| --- | --- |
| **Stripe / Paddle** | Both are built for card payments in USD/EUR. Your buyers pay by UPI, cash and bank transfer. If you ever take online payments, use Razorpay or a UPI link — not these. |
| **Shopify / WooCommerce / PrestaShop** | Adds a full storefront, inventory sync, returns and shipping. That is a second business. Revisit only if retail D2C ever passes 30% of turnover. |
| **Salesforce / HubSpot / Pipedrive / Zoho CRM** | Enterprise CRMs. WhatsApp labels are your CRM and they cost nothing. |
| **Mapbox** | The map is already solved for free. |
| **Semrush** | Useful data, priced far above a ₹10,000/month total budget. |
| **Supabase (external)** | Lovable Cloud already covers this if you ever need a database. Don't run two. |

**The pattern:** every connector adds a thing that can break, an account to
maintain, and usually a bill. At your stage, the site's job is to be found and
to open WhatsApp. Two analytics connectors support that. The rest do not.

---

## 3. Before you launch

Everything you need to change lives in **one file**: `src/config/shop.ts`.

| Constant | Replace with |
| --- | --- |
| WhatsApp number | Country code, no `+`, no spaces — e.g. `919876543210` |
| Display phone | `+91 98765 43210` |
| Shop number | Your exact shop and building number |
| GSTIN | Once registered |
| Warranty window | Your real replacement period |
| Maps embed | Your Google Business Profile `place_id` embed, once verified |

Then:

1. **Publish** from the Lovable editor.
2. **Connect `goyallights.com`** in Lovable's domain settings (custom domains need a paid Lovable plan; alternatively export the code to GitHub and host free on Netlify or Cloudflare Pages).
3. **Submit the site to Google Search Console** and request indexing.
4. **Add the site URL to your Google Business Profile**, IndiaMART, JustDial and every WhatsApp/Instagram bio. Same URL everywhere — see the NAP consistency rule in `03-marketing-plan.md`.

---

## 4. What the site deliberately does not do

- **No online cart.** Wholesale buyers negotiate; they will not check out. The enquiry builder that composes a WhatsApp message converts better than a checkout ever would at this stage.
- **No prices.** Rates in this market move and get bargained. Publishing them fixes your ceiling and hands your card to 200 competitors in the same lane. "Rate list on WhatsApp" is both truer and a better lead capture.
- **No stock photos.** The design is type, colour and light. Once you have real photographs of your own lit shelves, they will beat any stock image — and photographing your own stock is on the week-1 checklist in `03-marketing-plan.md`.

---

## 5. What was built

Stack: TanStack Start + React + Tailwind v4 + shadcn/ui. One route, ten section
components.

| File | Section |
| --- | --- |
| `src/config/shop.ts` | **Every placeholder lives here.** Phone, WhatsApp, shop number, GSTIN, warranty window, both map URLs, Dhanteras date |
| `src/styles.css` | The whole design system — colour tokens, fonts, bulb flicker, ticker, scroll reveal, map dark filter, reduced-motion guards |
| `src/routes/index.tsx` | Page assembly, meta tags, LocalBusiness + FAQPage JSON-LD |
| `src/components/site/Hero.tsx` | Dark hero, 7 hanging bulbs, colour-temperature switcher, Dhanteras countdown |
| `src/components/site/Ticker.tsx` | Bilingual marquee |
| `src/components/site/TrustRow.tsx` | GST billing / transport / replacement / reply speed |
| `src/components/site/Stock.tsx` | Nine categories with filter pills |
| `src/components/site/BuyWays.tsx` | Wholesale vs retail terms |
| `src/components/site/Enquiry.tsx` | Form that composes a WhatsApp message — no backend |
| `src/components/site/Visit.tsx` | Address, metro directions, hours, Google map |
| `src/components/site/Faq.tsx` | Eight questions, feeds the FAQPage schema |
| `src/components/site/data.ts` | Category and FAQ content |

### Verified in the code

- Colour tokens resolve in all three theme states, including the unstamped system-preference case — the bug that makes most generated sites render one theme's text on the other theme's background
- Every animation is disabled under `prefers-reduced-motion: reduce`
- Two JSON-LD blocks: `LightingStore` with address and Mon–Sat hours, and `FAQPage` generated from the live FAQ content. The FAQ schema is what gets the shop quoted in AI Overviews and ChatGPT search
- Map uses the keyless embed with a dark-mode CSS filter

### Fixed after review

1. A circular `--bulb: var(--bulb)` declaration in `styles.css` — invalid CSS, now removed
2. The countdown number was hidden from screen readers while animating — now carries a visually-hidden readable string
3. `telephone` in the JSON-LD used the spaced display format — now uses a separate E.164 field

### Not verified

The preview domain is blocked by this environment's network policy, so the
rendered page has not been viewed. Everything above was confirmed by reading the
source. Open the preview and judge the visual result yourself.

---

## 6. Revision of 22 Aug 2026 — final details applied

Verified line-by-line in the commit diff:

- **Rebrand to "Goyal Lights"** — H1 (with "Lights" as the retintable accent
  word), header, footer, page title, meta, both JSON-LD blocks, root fallback meta
- **Real contacts wired in** — WhatsApp and hero call CTA use Gaurav Goyal
  +91 83758 28408; Visit section and footer list both Gaurav and Mahender Goyal
  by name; JSON-LD telephone in E.164
- **Exact map** — embed now uses the door coordinates 28.656861, 77.233972;
  "Open in Google Maps" uses the shop's own share link
  (maps.app.goo.gl/guznh4czrvjFCCDR8)
- **Warranty erased** — trust item replaced with "Budget and branded, side by
  side"; FAQ question replaced with stock-photos-on-WhatsApp; the config field
  deleted so it cannot leak back
- **GSTIN gated** — the field stays in config but renders nowhere until the
  placeholder is replaced
- **Hindi as accent** — Devanagari survives in exactly three places (hero name
  line, three ticker words, footer name); all card subtitles, ledes and section
  Hindi removed
- **Polish** — bulb sway layered on the flicker with per-bulb delays, colour
  swatch dots in the CCT chips, tinted hover glow on the primary CTA, consistent
  eyebrow labels on every section, fade-rise on stock-filter changes, hover
  accent on card titles, hairline on the scrolled header, amber rule on the
  footer; every new animation covered by prefers-reduced-motion

