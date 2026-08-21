# Humanizer pass log

Tool: `.claude/skills/humanizer` v4.0, now calibrated against the real ZeroGPT
report filed for the Facebook Reel article.

```bash
cd .claude/skills/humanizer
python3 scripts/zerogpt_preflight.py <draft> --verbose
python3 scripts/scan.py <draft> --top 6
```

## Iterations

| # | Gates | scan.py | What was caught | What changed |
| --- | --- | --- | --- | --- |
| 1 | 10 of 11 | 5.2 | `sentence opener repetition`: "instagram" opened 6 sentences (10.2%). `no_contractions`: 6 across 74 sentences. Two `parallel_opening` pairs. | — |
| 2 | 10 of 11 | 6.1 | Fixed the pairs and the contraction rate (5.51 to 21.86 per 1k), but "the" then opened 7 sentences (10.9%) and a new "Five ... per ..." pair appeared | 25 edits |
| 3 | **11 of 11** | 4.0 | One weak `parallel_structure` pair left in a takeaway bullet | 7 edits |
| 4 | **11 of 11** | **2.6** | Nothing | Merged the bullet, lengthened three sentences |

## What the new detector caught

The `parallel_construction` signal was added after the Facebook Reel article
came back 23.4% from ZeroGPT, where every highlight turned out to be one half
of a matched pair. It earned its place immediately here, on a draft I had
written without noticing either problem:

| Pair it found | Why it matters |
| --- | --- |
| "Instagram began enforcing that cap in December 2025" / "Instagram started enforcing that limit in December 2025" | Near-duplicate sentences in two different sections. A reader would have noticed; I had not. |
| "Adam Mosseri has said plainly that..." / "Adam Mosseri has said it about as directly as..." | Same construction, same subject, twelve paragraphs apart. |

Neither would have been caught by the opener-repetition gate, which compares
raw first words and sees "Instagram began" and "Instagram started" as
different. That is precisely the gap the report exposed.

## Contraction rate

Worth calling out because it nearly shipped. The first draft ran 5.51
contractions per 1,000 words, which **passes** the gate's floor of 4.0 and is
still wrong for this client: SocialBee's guidelines ask for contractions
throughout, and the Facebook Reel article runs at 22 per 1,000. A passing gate
is not the same as a correct draft. Final version: 22.05 per 1,000.

## Remaining honest tells

`scan.py` still reports `low_burstiness` at a sentence-length standard
deviation of 6.7. The authoritative gate disagrees: `zerogpt_preflight.py`
measures coefficient of variation at 0.572 against a 0.45 floor, comfortably
passing. The two use different measures and the gate script is the calibrated
one, so this is noted rather than chased.

The article also has no first-person voice and no anecdote, because the brief
specifies second person and a serious register. Correct for the client,
slightly flattening for a detector. A real tradeoff, not an oversight.

## Next step

**Run it through ZeroGPT and file the report**, the same way as last time:

```bash
cd .claude/skills/humanizer
python3 scripts/learn.py reports/2026-08-21-socialbee-instagram-hashtags.md
```

Use `reports/TEMPLATE.md`. Two reports is when the skill starts being able to
tell a real pattern from a one-off, and the score history will show whether the
parallelism work moved the number.
