# ishu

Content work for SocialBee, plus the tooling used to produce it.

## Contents

| Path | What it is |
| --- | --- |
| `blog/trending-instagram-hashtags/` | Blog post: "Trending Instagram Hashtags (August 2026)", with its .docx, images, metadata, schema, filled checklist and humanizer log |
| `blog/facebook-reel-length/` | Blog post: "How Long Can a Facebook Reel Be? 2026 Limits and Best Run Times", with its .docx, images, metadata, schema, filled checklist and humanizer log |
| `.claude/skills/humanizer/` | The humanizer skill, v4.0. Gates drafts before a detector run, ranks sentences by risk, and learns from every filed ZeroGPT report |
| `tools/md_to_docx.py` | Converts an article markdown file to .docx |
| `tools/check_image_sources.py` | Checks every image has alt text and a source link resolving to an image file; `--strict` also fails on uncaptured slots |

## The articles

Each article folder holds the same set of files: the markdown draft as source
of truth, a .docx generated from it, `images/` with the script that draws them,
`image-manifest.md`, `meta.md`, `schema.json`, `aeo-seo-checklist.md` and
`humanizer-pass.md`.

**Trending Instagram Hashtags (August 2026)** leads on the five-hashtag cap
Instagram began enforcing in December 2025, which breaks the premise of every
list-of-thirty article ranking for the query. One flag for the editor: the
strongest statistic comes from Metricool, a competitor, so it is credited in
plain text with no hyperlink. See that article's `meta.md`.

**How Long Can a Facebook Reel Be?** corrects the widely repeated 90-second
figure. Alongside it:

- `How Long Can a Facebook Reel Be - 2026 Limits and Best Run Times.docx` - the
  Word version, generated from the markdown
- `image-manifest.md` and `images/` - three original visuals with the script
  that draws them, and why there are no screenshots
- `meta.md` - title tag, meta description, slug, image slots, link plan, and
  the facts that need re-verifying against a live account before publishing
- `schema.json` - Article and FAQPage JSON-LD
- `aeo-seo-checklist.md` - every item from the AEO/SEO checklist, marked done,
  partly done, or outstanding with an owner
- `humanizer-pass.md` - the scan-and-rewrite iterations, scores at each step,
  and the remaining honest tells

## The humanizer skill

```bash
cd .claude/skills/humanizer
python3 scripts/learn.py --status                    # what it knows so far
python3 scripts/zerogpt_preflight.py <draft.md> -v   # 11 pass/fail gates
python3 scripts/scan.py <draft.md>                   # ranked sentence risk
python3 scripts/learn.py reports/<report>.md         # ingest a ZeroGPT run
bash tests/run_tests.sh                              # verify the pipeline
```

The point of the skill is the feedback loop. The gates say whether a draft is
shippable and `scan.py` says which sentence to fix first; you run the draft
through ZeroGPT; `learn.py` compares the report against the prediction,
recalibrates the signal weights by what actually got flagged, and mines new
rules from the sentences it missed. All of that lives in `memory/` and is
committed, so it carries into the next session.

Read `.claude/skills/humanizer/SKILL.md` for the full workflow.
