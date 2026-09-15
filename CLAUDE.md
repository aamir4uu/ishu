# CLAUDE.md

Working rules for this repo and the skill kit that ships with it. Read once per
session. Skills live in `.claude/skills/` and load on demand; the table below
says which one to reach for. Run `tools/install-skills.sh` to make the same kit
available in every other repo on this machine.

## What this repo is

A content and sourcing workspace, not an application. `blog/` holds published
articles with their SEO packs and Word deliverables, `sourcing/` holds supplier
research and purchase terms, `tools/` holds the docx builder and the skill
installer. Every piece of prose leaves through the humanizer gate before it is
called done.

## Working principles

Adapted from Andrej Karpathy's notes on LLM coding pitfalls, as packaged by
Forrest Chang in [andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills).

1. **Think before acting.** State assumptions. If two readings of a request
   exist, name both instead of picking one silently. If a simpler route exists,
   say so. If something is unclear, stop and ask.
2. **Simplicity first.** Do only what was asked. No speculative features, no
   abstractions for single-use code, no configurability nobody requested. If
   200 lines could be 50, rewrite.
3. **Surgical changes.** Touch only what the request needs. Match the existing
   style. Do not tidy neighbouring code or prose. Remove only the dead code your
   own change created.
4. **Goal-driven execution.** Turn every task into a check you can run: a test,
   a script, a diff, a word count. For multi-step work, list the steps with
   their check next to each, then loop until every check passes.

Use judgment on trivial tasks. These rules bias toward caution.

## Skill routing

Invoke the skill before answering, not after. Announce which one you are using
in one short line.

### Writing and content

| When the task is | Use |
| --- | --- |
| Any prose that will be published or sent: final pass, ZeroGPT gate | `humanizer` (run `scripts/zerogpt_preflight.py` before delivery) |
| Deciding what to write, topic clusters, editorial calendar | `content-strategy` |
| New page or landing copy, headlines, CTAs | `copywriting` |
| Improving copy that already exists | `copy-editing` |
| Getting cited by ChatGPT, Perplexity, AI Overviews | `ai-seo` |
| Diagnosing rankings, on-page and technical SEO | `seo-audit` |
| JSON-LD and rich results | `schema` |
| Many similar pages from data | `programmatic-seo` |
| LinkedIn, X, Instagram, short-form scripts | `social` |
| Drip, nurture, onboarding email flows | `emails` |
| Supplier or prospect outreach, follow-up sequences | `cold-email` |
| Profiling competitors from their URLs | `competitor-profiling` |
| Interviews, review mining, personas | `customer-research` |
| Persuasion principles, framing, social proof | `marketing-psychology` |
| Launch plans, Product Hunt, announcements | `launch` |
| Gated downloads, checklists, templates | `lead-magnets` |
| Blog heroes, OG images, social graphics | `image` |
| Choosing a video approach or tool | `video`, then `hyperframes` to build it |

### Research

| When the task is | Use |
| --- | --- |
| Look something up on the web, X, Reddit, YouTube, GitHub, LinkedIn, RSS | `agent-reach` (run `agent-reach doctor --json` first) |

### Video

| When the task is | Use |
| --- | --- |
| Any request to make, edit, or render a video, animation, deck or overlay | `hyperframes` first. It routes to `product-launch-video`, `faceless-explainer`, `motion-graphics`, `slideshow` or `general-video` |
| Composition HTML contract | `hyperframes-core` |
| Motion, transitions, runtime adapters | `hyperframes-animation`, `hyperframes-keyframes` |
| Palettes, typography, narration, beats | `hyperframes-creative` |
| Music, SFX, images, voice, captions | `media-use`, then `hyperframes-audio` to mix |
| Registry blocks and effects | `hyperframes-registry` |
| CLI: init, lint, preview, render, publish | `hyperframes-cli` |

Workflows not installed here (`pr-to-video`, `music-to-video`,
`embedded-captions`, `talking-head-recut`, `remotion-to-hyperframes`, `figma`)
can be pulled on demand with `npx hyperframes skills update <name>`.

### Process

| When the task is | Use |
| --- | --- |
| Building or changing anything non-trivial | `brainstorming` before design, `writing-plans` before code |
| Executing a written plan | `executing-plans` |
| Two or more independent tasks | `dispatching-parallel-agents` |
| A bug, failing check, or surprise | `systematic-debugging` before proposing a fix |
| About to say "done", "fixed", or "passing" | `verification-before-completion` |

### Tokens and models

| When the task is | Use |
| --- | --- |
| User asks for brevity, `/caveman`, "fewer tokens" | `caveman` (stays on for the session until "stop caveman") |
| Routing Claude Code or another agent through a local gateway, free model tiers, quota fallback | `omniroute` |

## Conventions

- Articles are written in second person for the audience named in their SEO
  pack. Do not reference product features that the pack excludes.
- Word deliverables are built with `node tools/build-docx.js <source.md> <out.docx>`,
  never by hand.
- The humanizer learns from filed reports. If a ZeroGPT run happens, file it in
  `.claude/skills/humanizer/reports/` using the template.
- Never commit an API key. OmniRoute keys go in env vars or `omniroute launch`.
- Third-party skills keep their upstream license file inside their folder. See
  `.claude/skills/THIRD_PARTY.md` for sources and versions before editing one;
  prefer re-syncing from upstream over local forks.

## Commit hygiene

Small commits, one concern each, imperative subject line. Push to the branch
you were given, never to another one.
