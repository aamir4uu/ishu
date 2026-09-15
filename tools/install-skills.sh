#!/usr/bin/env bash
# Install the skill kit from this repo's .claude/skills/ into the user-level
# Claude Code skills directory so every repository on this machine can use it.
#
#   tools/install-skills.sh            copy skills into ~/.claude/skills (default)
#   tools/install-skills.sh --link     symlink instead of copy (edits here show up everywhere)
#   tools/install-skills.sh --upstream pull the latest versions straight from the upstream repos
#   tools/install-skills.sh --list     show what would be installed and exit
#
# Honors CLAUDE_CONFIG_DIR. Existing skills with the same name are replaced.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$HERE/.claude/skills"
DEST="${CLAUDE_CONFIG_DIR:-$HOME/.claude}/skills"
MODE="copy"

for arg in "$@"; do
  case "$arg" in
    --link) MODE="link" ;;
    --upstream) MODE="upstream" ;;
    --list) MODE="list" ;;
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "unknown flag: $arg" >&2; exit 2 ;;
  esac
done

skills=()
for d in "$SRC"/*/; do
  [ -f "$d/SKILL.md" ] && skills+=("$(basename "$d")")
done

if [ "$MODE" = "list" ]; then
  printf '%s\n' "${skills[@]}"
  exit 0
fi

if [ "$MODE" = "upstream" ]; then
  # Fresh copies from the source repos. Needs Node 22+ and network access.
  # Installs to the user level (-g) so they apply to every repo.
  command -v npx >/dev/null || { echo "npx not found; install Node.js 22+" >&2; exit 1; }
  npx -y skills add JuliusBrussee/caveman --skill caveman -a claude-code -g --yes
  npx -y skills add Panniantong/Agent-Reach --skill agent-reach -a claude-code -g --yes
  npx -y skills add heygen-com/hyperframes -a claude-code -g --yes \
    --skill hyperframes --skill hyperframes-core --skill hyperframes-animation \
    --skill hyperframes-keyframes --skill hyperframes-creative --skill hyperframes-cli \
    --skill hyperframes-audio --skill hyperframes-registry --skill media-use \
    --skill product-launch-video --skill faceless-explainer --skill motion-graphics \
    --skill slideshow --skill general-video
  npx -y skills add coreyhaines31/marketingskills -a claude-code -g --yes \
    --skill copywriting --skill copy-editing --skill content-strategy --skill ai-seo \
    --skill seo-audit --skill schema --skill social --skill emails --skill cold-email \
    --skill competitor-profiling --skill marketing-psychology --skill video --skill image \
    --skill lead-magnets --skill launch --skill programmatic-seo --skill customer-research
  npx -y skills add obra/superpowers -a claude-code -g --yes \
    --skill brainstorming --skill writing-plans --skill executing-plans \
    --skill verification-before-completion --skill systematic-debugging \
    --skill dispatching-parallel-agents
  # omniroute (setup guide) and humanizer are authored in this repo; copy them.
  mkdir -p "$DEST"
  for s in omniroute humanizer; do
    rm -rf "$DEST/$s"; cp -R "$SRC/$s" "$DEST/$s"
  done
  echo "Installed upstream skills into $DEST"
  exit 0
fi

mkdir -p "$DEST"
for s in "${skills[@]}"; do
  rm -rf "$DEST/$s"
  if [ "$MODE" = "link" ]; then
    ln -s "$SRC/$s" "$DEST/$s"
  else
    cp -R "$SRC/$s" "$DEST/$s"
  fi
done
echo "Installed ${#skills[@]} skills into $DEST ($MODE)"
echo "Restart Claude Code, then type /caveman, /hyperframes, /agent-reach or /omniroute to check."
