# ZeroGPT session log

Appended to by `scripts/learn.py` every time a real detector report is
ingested. Each entry records the score, how many flagged spans matched the
draft, the scanner's recall before that report, which sentences it missed, and
how the signal weights moved as a result.

Read the last two or three entries at the start of any session. The "missed by
the scanner" lists are the highest-value part: those are the sentence shapes
that got past the model last time.

---

## Session 0 - 2026-08-21 (seed, no detector report)

Note: this memory was built alongside the SocialBee Facebook Reel piece and then
merged into the established `humanizer` skill as its v4.0 automation layer. The
manual learning history that predates it is in `references/learning-log.md`.

Baseline only. No ZeroGPT report has been ingested yet, so every weight in
`state.json` is still the untrained prior and `learned_rules.json` contains only
the SocialBee banned lists, marked `source: client:socialbee`.

- Draft scanned: `content/facebook-reel-length/facebook-reel-length.md`
- Final scan score: 0.0/100, no sentence-level and no document-level signals
- Scanner fixes made this session: markdown line breaks are now hard sentence
  boundaries, and headings and table rows are excluded from the prose sample.
  Before the fix the scanner was reporting 9.2 on a draft that actually scored
  32.6.

The first real report will move the weights. Until then, treat the score as a
lint pass, not as a detector prediction.

## Session 1 - 2026-08-21

- Draft: `/home/user/ishu/blog/facebook-reel-length/facebook-reel-length.md`
- ZeroGPT score: 23.4
- Flagged spans matched: 21
- Scanner recall before this report: 0.24
- Rules promoted: 1

Missed by the scanner (now feeding rule mining):

  - **Short answer:** A Facebook Reel can now run past the old 90-second cap.
  - Meta retired that limit in June 2025 when every Facebook video became a Reel, so uploaded Reels have no fixed maximum on updated accounts.
  - Recording inside the Facebook app still stops at 90 seconds, and the minimum is 3 seconds.
  - The 90-second cap went away in June 2025.
  - Recording in the app still stops at 90 seconds, so anything longer has to be uploaded as a finished file.
  - The minimum is 3 seconds.
  - That answer changed recently, and a lot of the advice still circulating was written before it did.
  - Meta rolled this out gradually by region and account type, which is why two people on the same team can open the same composer on the same day and see different limits.
  - If yours still rejects anything over 90 seconds, you haven't been switched yet.
  - TechCrunch covered the earlier jump to 90 seconds back in March 2023, and Social Media Today reported the 2025 consolidation that removed the ceiling.
  - Facebook needs 3 seconds.
  - For most business content, aim for 15 to 60 seconds.
  - **Hooks and single tips:** 7 to 15 seconds, with no setup.
  - Length decisions get easier when you aren't posting in a rush.
  - SocialBee publishes Reels straight to your Facebook Pages, so you can queue a 12-second hook for Tuesday and a 60-second demo for Thursday without opening the app twice.

Weight moves:

  - `parallel_structure` 13.0 -> 16.6 (lift 1.79)
  - `parallel_opening` 13.0 -> 15.92 (lift 1.64)
