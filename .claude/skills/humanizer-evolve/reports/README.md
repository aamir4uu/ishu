# ZeroGPT reports

One file per detector run. Format:

```
draft: content/facebook-reel-length/facebook-reel-length.md
score: 18
date: 2026-08-21
tool: zerogpt
note: pass 2, after rhythm fixes

## flagged
Paste each highlighted sentence on its own line, exactly as ZeroGPT shows it.
Leading bullets or numbers are stripped automatically.
```

Then `python3 ../scripts/learn.py <this file>`.

Keeping the raw reports in the repo means the calibration can be rebuilt from
scratch if the weights ever need resetting.
