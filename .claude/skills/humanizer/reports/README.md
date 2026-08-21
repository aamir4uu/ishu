# Reports

One file per ZeroGPT run, named `YYYY-MM-DD-slug.md`, based on `TEMPLATE.md`.

These are the evidence base for every threshold and pattern in the skill. Do not
change a gate value or add a marker without a report in this folder that
justifies it. When a report is filed, work through the actions checklist at the
bottom of it and then add a row to the piece history table in
`../references/learning-log.md`.

## Ingesting a report

Since v4.0 the mechanical half of the update protocol is automated:

```bash
python3 ../scripts/learn.py 2026-08-21-slug.md --dry-run   # preview
python3 ../scripts/learn.py 2026-08-21-slug.md             # commit
```

Two formats parse. Prefer `TEMPLATE.md`, which keeps the signal attribution
alongside each sentence. The short form is there for a quick paste:

```
draft: blog/slug/article.md
score: 21
date: 2026-08-21
note: pass 1

## flagged
One highlighted sentence per line, exactly as ZeroGPT shows it.
```

Either way, paste the sentences **verbatim**. `learn.py` matches them back to
the draft by token overlap, and a paraphrase will not match.

A stub report is refused rather than ingested. An empty highlights table teaches
the skill nothing and would only pollute the accepted corpus with sentences the
detector never actually cleared.

After ingesting, commit `../memory/`. That is where the calibration lives.
