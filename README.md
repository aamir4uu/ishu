# ishu

Content work for SocialBee, plus the tooling used to produce it.

## Contents

| Path | What it is |
| --- | --- |
| `content/facebook-reel-length/` | Blog post: "How Long Can a Facebook Reel Be? 2026 Limits and Best Run Times", with its metadata, schema, filled checklist and humanizer log |
| `.claude/skills/humanizer-evolve/` | Self-improving humanizer skill. Scores drafts for AI-writing patterns and learns from real ZeroGPT reports |

## The article

`content/facebook-reel-length/facebook-reel-length.md` is the draft. Alongside
it:

- `meta.md` - title tag, meta description, slug, image slots, link plan, and
  the facts that need re-verifying against a live account before publishing
- `schema.json` - Article and FAQPage JSON-LD
- `aeo-seo-checklist.md` - every item from the AEO/SEO checklist, marked done,
  partly done, or outstanding with an owner
- `humanizer-pass.md` - the scan-and-rewrite iterations, scores at each step,
  and the remaining honest tells

## The humanizer skill

```bash
cd .claude/skills/humanizer-evolve/scripts
python3 learn.py --status                                        # what it knows
python3 scan.py ../../../../content/facebook-reel-length/facebook-reel-length.md
python3 learn.py ../reports/2026-08-21-pass1.md                  # feed it a report
bash ../tests/run_tests.sh                                       # verify the pipeline
```

The point of the skill is the feedback loop. `scan.py` predicts what a detector
will flag; you run the draft through ZeroGPT; `learn.py` compares the two,
recalibrates the signal weights against what actually got flagged, and mines
new rules from the sentences it missed. All of that lives in `memory/` and is
committed, so it carries into the next session.

Read `.claude/skills/humanizer-evolve/README.md` for the full design.
