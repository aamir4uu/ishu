# Image Workflow — Real Photo In, Meesho-Ready Image Out

Meesho rejects AI-invented product shots when the delivered item does not match, and
buyers return them. So the rule is: **image 1 is always your real product, cleaned up**;
AI is for the background, the lifestyle scene and the spec graphic. Every prompt below
assumes you upload a phone photo first.

## Meesho image rules (2026)

| Rule | Value |
| --- | --- |
| Shape / size | Square 1:1, minimum 1000 × 1000 px, aim for 1500 × 1500 |
| Format | JPG or PNG, under 5 MB |
| Image 1 | Product only on pure white (RGB 255,255,255). No text, logo, watermark, price, "sale", hands, props, multiple products |
| Images 2–5 | Lifestyle and detail shots allowed. Keep text minimal; a single spec line ("30 Meter · 8 Modes") is tolerated, promotional words are not |
| Product fill | 70–80% of the frame, centred |
| Lit shots | Allowed and they convert; shoot in a dark room, phone on a stand, night mode off |
| Never | Stock photos of a different model, competitor screenshots, images with another brand's logo |

## Step 1 — Shoot (shop boy, 20 min per SKU)

1. White chart paper on the counter, phone above at 45°, daylight from the shop door, flash off.
2. Front · angle · close-up of the LED/holder · carton back label (BIS R-number, MRP) · the item lit up in the store-room with the lights off.
3. Name files `SKU_raw1.jpg` … `SKU_raw5.jpg`. Do not crop or filter.

## Step 2 — ChatGPT prompts (paste with the photo attached)

Use ChatGPT with image generation (GPT-4o / Images). Attach the raw photo, paste the prompt.
Save the result as `SKU-1.jpg` etc. Check the output against the real item before uploading.

### Master prompt — image 1 (white-background clean-up)

```
This is a photo of a product I sell. Recreate it as an e-commerce catalog image:
- Keep the product EXACTLY as it is: same shape, colour, wire, plug, holder, number of parts. Do not add, remove, or restyle anything.
- Remove the background and replace with pure white (#FFFFFF), no shadow except a very soft contact shadow under the product.
- Centre the product; it should fill about 75% of a square 1:1 frame, 1500 x 1500 px.
- Even, soft studio lighting. No text, no logo, no watermark, no props, no hands.
Output the image only.
```

### Image 2 — lifestyle scene (product stays real)

Serial / jhalar / pixel:
```
Using the attached photo of my LED string light, place this exact string, switched on and glowing [multicolour / warm white], along the railing of an Indian home balcony at night during Diwali. Realistic, slightly wide shot, the string is the main subject and clearly the same product (same LED size and spacing). Warm festive mood, a few clay diyas on the ledge, no people, no text. Square 1:1, 1500 x 1500.
```
Curtain:
```
Place this exact LED curtain light, lit warm white, hanging flat on the wall behind a bed in a modern Indian bedroom at night. Same strand count and drop length as the photo. Cosy, realistic, no text, no people. Square 1:1, 1500 x 1500.
```
Rope / strip:
```
Show this exact LED rope/strip installed inside a false-ceiling cove in an Indian living room, lit warm white, glow visible along the ceiling edge. Realistic interior photo, no text. Square 1:1.
```
Diya string:
```
Drape this exact diya-shaped LED string around a small home mandir / pooja shelf, lit warm white, a rangoli on the floor below. Indian home, evening, realistic, no text, no people. Square 1:1.
```
Battery fairy:
```
Put this exact copper-wire fairy light inside a clear glass bottle on a bedside table, lit warm white, soft bokeh, cosy bedroom. Product unchanged. No text. Square 1:1.
```
Bulb:
```
Show this exact LED bulb screwed into a ceiling holder in a bright Indian living room, switched on, cool white light. Bulb shape and size unchanged. No text. Square 1:1.
```
Panel / COB / batten:
```
Show this exact [panel / COB spot / batten] installed in a false ceiling of a modern Indian [bedroom / showroom / kitchen], switched on, [cool white / warm white]. Product unchanged, realistic interior photo, no text. Square 1:1.
```
Flood:
```
Mount this exact LED flood light on the pillar of a house gate at night, switched on, lighting the driveway, cool white. Product unchanged. No text. Square 1:1.
```
Chandelier:
```
Hang this exact chandelier from the ceiling of an elegant Indian living room, lit warm, sofa below, evening. Product unchanged: same arms, drops, finish. No text. Square 1:1.
```

### Image 3 — detail / close-up

```
From the attached photo, produce a clean close-up of the [LEDs and controller box / bulb base and holder pins / driver and clips / crystal drops] on a white background, sharp focus, product unchanged, no text. Square 1:1, 1500 x 1500.
```

### Image 4 — spec graphic (the only image with text)

```
Make a simple e-commerce infographic on a white background using the attached product image, unchanged, on the left. On the right, three short labelled lines in a clean sans-serif, dark grey text, no icons of other brands:
"[30 Meter length]"
"[8 lighting modes]"
"[220–240 V plug-in]"
No other words, no prices, no discounts, no logos. Square 1:1, 1500 x 1500.
```
Replace the three lines per SKU with the values from `04-catalog-listings.xlsx` (Length /
Wattage, modes or lumens, voltage or waterproof rating).

### Image 5 — carton label (no AI)

Upload the straight phone photo of the carton back showing BIS R-number, MRP, importer
details. Crop to square only. Do not run it through AI; a regenerated label is a fake label.

## Step 3 — Checks before upload

- [ ] Same product as the carton (LED count, colour, plug type)
- [ ] Image 1: pure white corners — open it and look at the corners; off-white gets rejected
- [ ] 1:1 square, ≥1000 px, <5 MB
- [ ] No text on images 1–3 and 5; only the three spec lines on image 4
- [ ] Lit shots show the real light colour (warm vs cool) that the attribute says

## If you want me to generate instead of ChatGPT

This session has a Higgsfield image connector but the account shows **0 credits on a free
plan**, so I cannot render images from here today. Top it up (or connect Canva) and send me
the raw photos; I run the same prompts and return the five images per SKU named and sized.

## Prompt for ChatGPT to write more listings (when you add SKUs)

```
You write Meesho product listings for an Indian lighting shop. Given: product, length or wattage, light colour, pack size, what is in the box. Return: (1) product name under 150 characters, head keyword first, Hinglish search terms (jhalar, ladi, rice light, jhoomar) where buyers use them, no promotional words, no caps; (2) description under 600 characters with voltage, package contents and one care line; (3) attribute values for Colour, Light Colour, Power Source, Length/Wattage, Waterproof, Material, Pack of; (4) 8 search keywords. Product: ___
```
