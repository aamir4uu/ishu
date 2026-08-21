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

## Session 2 - 2026-08-21

- Draft: `/home/user/ishu/blog/trending-instagram-hashtags/trending-instagram-hashtags.md`
- ZeroGPT score: 25.6
- Flagged spans matched: 18
- Scanner recall before this report: 0.33
- Rules promoted: 2

Missed by the scanner (now feeding rule mining):

  - Read the section after it before you use any of them, though, because the rules have changed twice in the past eighteen months.
  - These are the tags carrying the most volume this month, grouped by what they are for.
  - The head of Instagram has put it about as bluntly as he can.
  - Hashtags aren't a primary way to increase reach, and whatever effect they once had was marginal.
  - What hashtags still do is tell Instagram what your post is about, which feeds search and Explore.
  - Our guide to the Instagram algorithm covers the signals that actually rank you.
  - That sounds manageable until you're scheduling twenty posts across four content categories.
  - SocialBee generates relevant hashtags from your post, then saves them as Hashtag Collections you can drop into any future post.
  - Build one set per content pillar and you'll stop rebuilding the same five tags every Tuesday.
  - Here is how hashtag generation works in SocialBee.
  - Use one only when your content genuinely belongs to that moment.
  - Mosseri has said they never meaningfully did, and Metricool's 2026 study found posts with hashtags underperforming the average by roughly a third on views.

Weight moves:

  - `stat_dense` 11.0 -> 23.83 (lift 4.33)
  - `clause_triad` 8.0 -> 11.11 (lift 2.11)
  - `parallel_structure` 16.6 -> 14.25 (lift 0.6)
  - `intro_position` 12.0 -> 13.54 (lift 1.37)
