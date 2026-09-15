---
name: omniroute
description: >
  Set up and operate OmniRoute, the free MIT AI gateway (one local endpoint,
  350+ providers, 150+ free tiers, quota-aware fallback, RTK + Caveman
  compression) and point Claude Code, Codex, Cursor, Cline or OpenCode at it.
  Use when the user says "omniroute", "omni route", "AI gateway", "free
  models for Claude Code", "route Claude Code through", "fallback when quota
  runs out", "ANTHROPIC_BASE_URL", "cut my token bill", or wants Claude Code
  to run on Kimi / GLM / DeepSeek / Gemini / a local model. Covers install,
  provider connection, API keys, combos (fallback chains), Claude Code
  profiles, compression, quota tracking and troubleshooting.
metadata:
  upstream: https://github.com/diegosouzapw/OmniRoute
  docs: https://omniroute.dev
  version-tracked: 3.8.50
---

# OmniRoute setup guide

OmniRoute runs on the user's machine as a single OpenAI- and Anthropic-compatible
endpoint (`http://localhost:20128`). Coding agents talk to it; it picks a provider,
falls back when a quota runs out, and compresses what the agent reads.

Everything below is the short path. The long form lives in `references/`:

| Need | Read |
| --- | --- |
| Every install method, ports, split-port, MCP/A2A, uninstall | `references/SETUP_GUIDE.md` |
| Claude Code env vars, profiles, model tiers, discovery aliases | `references/CLAUDE-CODE-CONFIGURATION.md` |
| Every `omniroute setup-<tool>` command and what it writes | `references/CLI-INTEGRATIONS.md` |
| Which free providers are worth connecting first | `references/FREE_PROVIDER_RANKINGS.md` |
| Quota and usage tracking | `references/USAGE_QUOTA_GUIDE.md` |
| Something broke | `references/TROUBLESHOOTING.md` |
| CLI verbs: providers, keys, models, routing combos, server, compression | `references/cli-*.md`, `references/omni-combos-routing.md` |

## Step 0: decide local or remote

- **Local** (default): OmniRoute and the coding tool run on the same machine.
- **Remote**: OmniRoute runs on a VPS or home server. Run `omniroute connect <host>`
  once on the client machine; every later `setup-*` and `launch` command targets it.

## Step 1: install and start

Needs Node.js 20+.

```bash
npm install -g omniroute
omniroute                    # server + dashboard on http://localhost:20128
```

Alternatives (details in `references/SETUP_GUIDE.md`):

```bash
pnpm add -g omniroute@latest --allow-build=better-sqlite3 --allow-build=@swc/core
yay -S omniroute-bin && systemctl --user enable --now omniroute.service   # Arch
docker compose up -d                                                      # from the repo
omniroute setup --non-interactive --password "$OMNIROUTE_PASSWORD"        # headless
```

Peer-dependency warnings from npm are harmless. Check health with:

```bash
omniroute doctor
omniroute status
```

## Step 2: connect a provider

Dashboard → **Providers** → connect. Zero-signup options that work immediately:

- **OpenCode Free** (no auth)
- **Kiro AI** (free Claude credits per account)
- Any provider where the user already has an API key or OAuth login
  (OpenAI, Anthropic, Google, DeepSeek, Kimi, GLM, OpenRouter, Ollama, LM Studio…)

From a shell instead:

```bash
omniroute providers available --search kimi
omniroute setup --non-interactive --add-provider --provider openai --api-key "$OPENAI_API_KEY" --test-provider
omniroute providers test-all
```

Read `references/FREE_PROVIDER_RANKINGS.md` before recommending free tiers; rankings
change and some tiers need a phone number or a region.

## Step 3: create an API key

Dashboard → **Endpoints** → create key. It looks like `oma_live_…`. This is the
gateway key your tools present. (`omniroute keys add <provider>` is different: it
stores an upstream provider's key, see `references/cli-keys.md`.)

## Step 4: point the coding tool at OmniRoute

### Claude Code (the common case)

Fastest path, no config written:

```bash
omniroute launch                          # picks the active context, execs `claude`
omniroute launch --profile auto-coding-free
```

Persistent profiles, one per model, stored under `~/.claude/profiles/<name>/`:

```bash
omniroute setup-claude                    # writes profiles from the live model catalog
omniroute setup-claude --only glm,kimi    # subset
omniroute setup-claude --dry-run          # preview
omniroute launch --profile kimi-k27       # run one
```

Manual, if the user wants to see the wiring:

```bash
export ANTHROPIC_BASE_URL="http://localhost:20128"      # NO /v1 suffix
export ANTHROPIC_AUTH_TOKEN="oma_live_xxx"
export ANTHROPIC_MODEL="auto"                           # or glm/glm-5.2, kmc/kimi-k2.6 ...
export CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1     # /model picker lists gateway models
claude
```

Or in `~/.claude/settings.json`:

```jsonc
{
  "env": {
    "ANTHROPIC_BASE_URL": "http://localhost:20128",
    "ANTHROPIC_AUTH_TOKEN": "oma_live_xxx",
    "CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY": "1",
    "CLAUDE_CODE_AUTO_COMPACT_WINDOW": "190000"
  }
}
```

Rules that bite:

- Env vars are read once at startup. Restart `claude` after changing them.
- `ANTHROPIC_BASE_URL` has no `/v1` and no trailing slash.
- The `/model` picker only shows ids starting with `claude` or `anthropic`. Force any
  other model with `ANTHROPIC_MODEL=<id>` or turn on discovery aliases
  (Settings → Feature Flags → `EXPOSE_CC_DISCOVERY_ALIASES`).
- Non-Claude models with a window larger than 200K need
  `CLAUDE_CODE_AUTO_COMPACT_WINDOW` set below the real window.
- Per-tier mapping is optional: `ANTHROPIC_DEFAULT_OPUS_MODEL`,
  `ANTHROPIC_DEFAULT_SONNET_MODEL`, `ANTHROPIC_DEFAULT_HAIKU_MODEL`.

### Other tools

```bash
omniroute setup-codex        # Codex CLI profiles
omniroute setup-opencode     # OpenCode
omniroute setup-cline        # Cline CLI + VS Code
omniroute setup-cursor       # prints Cursor's in-app steps
omniroute setup-continue     # Continue
omniroute setup-aider        # Aider
omniroute setup-goose        # Goose
omniroute setup-qwen         # Qwen Code
omniroute run <claude|codex|aider|goose|opencode|qwen|gemini>   # generic launcher
```

Any OpenAI-compatible SDK:

```txt
Base URL: http://localhost:20128/v1
API key:  oma_live_xxx
Model:    auto   (or provider/model, e.g. deepseek/deepseek-chat)
```

Clients that cannot send an Authorization header use the tokenized alias
`http://localhost:20128/api/v1/vscode/YOUR_KEY/`.

## Step 5: verify

```bash
curl http://localhost:20128/v1/models -H "Authorization: Bearer oma_live_xxx"
omniroute logs --follow
```

Models listed and a request in the log means it works.

## Step 6 (optional): combos, compression, quotas

**Combos** are named fallback chains. Dashboard → **Combos**, or:

```bash
omniroute combo list
omniroute combo create cheap-first     # interactive: pick models, order, strategy
omniroute combo switch cheap-first     # make it the default
omniroute suggest                      # let OmniRoute propose a combo from connected providers
```

Use the combo name as the model id (`ANTHROPIC_MODEL=combo/cheap-first`).
Seventeen strategies exist; `fallback`, `round-robin`, `cost-optimized` and
`quota-aware` cover most cases. See `references/omni-combos-routing.md`.

**Compression** (RTK for command output, Caveman for prose) is on the dashboard
under Compression, or `omniroute compression …` (`references/cli-compression.md`).
It stacks with the `caveman` skill in this repo: the skill shrinks what the
agent writes, OmniRoute shrinks what the agent reads.

**Quotas**: Dashboard → Usage, or `omniroute logs`. Quota-aware routing moves to
the next provider automatically when one is exhausted
(`references/USAGE_QUOTA_GUIDE.md`).

## Troubleshooting quick table

| Symptom | Fix |
| --- | --- |
| Claude Code ignores the gateway | `ANTHROPIC_BASE_URL` must have no `/v1`; restart `claude` |
| `/model` picker empty | Claude Code 2.1.219+ and `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` |
| `400 Ambiguous model 'claude-…'` | Both `cc/` and `claude/` providers connected; pin `ANTHROPIC_MODEL=cc/claude-…` or enable "Prefer Claude Code for unprefixed Claude models" |
| Auth errors with a profile | Profiles hold no token; use `omniroute launch --profile` or export `ANTHROPIC_AUTH_TOKEN` |
| Port 20128 busy | `omniroute --port 3000` and update the base URL |
| Native build errors on pnpm | add `--allow-build=better-sqlite3 --allow-build=@swc/core` |

Everything else: `references/TROUBLESHOOTING.md`.

## How to run this skill

1. Ask which tool the user wants routed (default Claude Code) and local vs remote.
2. Run Steps 1 to 5 with the user, one command at a time, and show the output.
3. Never paste a real `oma_live_` key into a file that gets committed. Use env vars
   or `omniroute launch`, which injects the token.
4. Finish with the verify curl and one line saying which model id is active.
