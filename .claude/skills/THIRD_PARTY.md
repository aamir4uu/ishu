# Third-party skills in this kit

Each folder keeps its upstream LICENSE. Re-sync from upstream instead of forking
locally; `tools/install-skills.sh --upstream` pulls the latest copies.

| Skill folders | Upstream | Version / commit synced | License |
| --- | --- | --- | --- |
| `caveman` | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | v2.7.0, `4df4b03` (2026-09-14) | MIT (skill only; the proxy is BSL and not included) |
| `agent-reach` | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | v1.5.0, `da5044d` (2026-09-01). `SKILL.md` is the English file; `SKILL.zh.md` is the original | MIT |
| `hyperframes`, `hyperframes-core`, `hyperframes-animation`, `hyperframes-keyframes`, `hyperframes-creative`, `hyperframes-cli`, `hyperframes-audio`, `hyperframes-registry`, `media-use`, `product-launch-video`, `faceless-explainer`, `motion-graphics`, `slideshow`, `general-video` | [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | `e2d60cf` (2026-09-15). Core set plus five creation workflows; the rest install on demand via `npx hyperframes skills update <name>` | Apache 2.0 |
| `omniroute` | Authored here; `references/` are copied from [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) docs and generated CLI skills | v3.8.51, `aaf0777a` (2026-09-15) | MIT |
| `copywriting`, `copy-editing`, `content-strategy`, `ai-seo`, `seo-audit`, `schema`, `social`, `emails`, `cold-email`, `competitor-profiling`, `marketing-psychology`, `video`, `image`, `lead-magnets`, `launch`, `programmatic-seo`, `customer-research` | [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `5b2c000` (2026-09-04). `evals/` folders stripped | MIT |
| `brainstorming`, `writing-plans`, `executing-plans`, `verification-before-completion`, `systematic-debugging`, `dispatching-parallel-agents` | [obra/superpowers](https://github.com/obra/superpowers) | `b36e082` (2026-08-12). Some text refers to sibling skills with a `superpowers:` prefix; here they are plain names | MIT |
| Working principles in `CLAUDE.md` | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills) | `2c60614` (2026-04-20), paraphrased | No license file upstream; rewritten in our own words |
| `humanizer` | Authored here, v3.0.0 | | MIT |

## Considered and not installed

- `caveman-compress` and the Caveman proxy: need an API key and a running
  daemon; the `caveman` skill alone gives the output savings.
- HyperFrames `pr-to-video`, `music-to-video`, `embedded-captions`,
  `talking-head-recut`, `remotion-to-hyperframes`, `figma`: 12 MB of assets for
  workflows this repo has not needed. The router installs them on demand.
- OmniRoute's 40 generated REST/CLI skills: the seven CLI ones most useful for
  setup are folded into `omniroute/references/`.
- Aradotso/trending-skills: a feed of auto-generated skills. Browse it for new
  ones: `npx skills add Aradotso/trending-skills --skill <name>`.
