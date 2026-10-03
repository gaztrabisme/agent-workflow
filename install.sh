#!/usr/bin/env bash
# Link this package into the current user's agents. Safe to run again.
#
#   ./install.sh               skills, CLAUDE.md, hooks, plugin list
#   ./install.sh --with-tools  also install render-kit and scene-engine dependencies
#
# Never touches API keys, MCP servers, or files it did not put there.
set -euo pipefail

AW="$(cd "$(dirname "$0")" && pwd)"
WITH_TOOLS=0
if [ "${1:-}" = "--with-tools" ]; then WITH_TOOLS=1; fi
say() { printf '%s\n' "$*"; }
warn() { printf 'WARNING: %s\n' "$*" >&2; }

# --- needs ---
command -v git >/dev/null || { warn "git is required"; exit 1; }
git lfs version >/dev/null 2>&1 || { warn "git-lfs is required (course images and PDFs). Install it, then run: git lfs install && git -C '$AW' lfs pull"; exit 1; }
command -v python3 >/dev/null || { warn "python3 is required"; exit 1; }
if [ -n "$(git -C "$AW" lfs ls-files 2>/dev/null | head -1)" ] && git -C "$AW" lfs ls-files | grep -q ' - '; then
  say "Fetching course files from Git LFS (first run only)..."
  git -C "$AW" lfs pull
fi

# --- link one folder into an agent's skills folder ---
link_skills() { # $1 = skills folder
  local dir=$1 name target
  mkdir -p "$dir"
  while read -r name; do
    [ -n "$name" ] || continue
    target="$dir/$name"
    if [ -L "$target" ] || [ ! -e "$target" ]; then
      ln -sfn "$AW/skills/$name" "$target"
    else
      warn "$target is a real folder, left alone"
    fi
  done < "$AW/skills.txt"
  while read -r name; do
    [ -n "$name" ] || continue
    if [ -L "$dir/$name" ]; then rm "$dir/$name"; say "removed retired link $dir/$name"; fi
  done < "$AW/config/retired-skills.txt"
  return 0
}

link_skills "$HOME/.claude/skills"
for d in "$HOME/.codex" "$HOME/.agents"; do
  if [ -d "$d" ]; then link_skills "$d/skills"; fi
done
say "Linked $(wc -l < "$AW/skills.txt" | tr -d ' ') skills."

# --- stable path used by the skills' instructions ---
ln -sfn "$AW" "$HOME/.agent-workflow"

# --- CLAUDE.md ---
mkdir -p "$HOME/.claude"
CM="$HOME/.claude/CLAUDE.md"
if [ -e "$CM" ] && [ ! -L "$CM" ] && ! cmp -s "$CM" "$AW/config/claude/CLAUDE.md"; then
  cp "$CM" "$CM.bak-$(date +%Y%m%d-%H%M%S)"
  say "Existing CLAUDE.md backed up."
fi
ln -sfn "$AW/config/claude/CLAUDE.md" "$CM"

# --- hooks, plugins and plugin sources in settings.json (merged, never replaced) ---
PG="$(dirname "$AW")/pi-plan-goal"
if [ ! -d "$PG/claude-code" ]; then
  git clone -q https://github.com/gaztrabisme/pi-plan-goal.git "$PG" || warn "could not clone pi-plan-goal; the plan-goal plugin will not load"
fi
AW="$AW" PG="$PG" python3 - <<'PY'
import json, os, shutil, time
home = os.path.expanduser("~")
path = os.path.join(home, ".claude", "settings.json")
aw, pg = os.environ["AW"], os.environ["PG"]
s = json.load(open(path)) if os.path.exists(path) else {}
if os.path.exists(path):
    shutil.copy(path, f"{path}.bak-{time.strftime('%Y%m%d-%H%M%S')}")

def has(event, matcher, cmd):
    return any(m.get("matcher") == matcher and h.get("command") == cmd
               for m in s.get("hooks", {}).get(event, []) for h in m.get("hooks", []))

def add(event, matcher, cmd):
    if has(event, matcher, cmd):
        return
    s.setdefault("hooks", {}).setdefault(event, []).append(
        {"matcher": matcher, "hooks": [{"type": "command", "command": cmd}]})

dcg = os.path.join(home, ".local", "bin", "dcg")
if not os.path.exists(dcg):
    print("WARNING: dcg (destructive-command guard) not found at ~/.local/bin/dcg; install it, then re-run.")
add("PreToolUse", "Bash", dcg)
q = os.path.join(aw, "config", "hooks", "claude-quality-hook")
for m in ("Edit", "Write"):
    add("PostToolUse", m, q)

plugins = s.setdefault("enabledPlugins", {})
for p in ("pyright-lsp@claude-plugins-official", "rust-analyzer-lsp@claude-plugins-official",
          "swift-lsp@claude-plugins-official", "codex@openai-codex",
          "i-have-adhd@i-have-adhd", "plan-goal@pi-plan-goal", "warp@claude-code-warp"):
    plugins.setdefault(p, True)
mk = s.setdefault("extraKnownMarketplaces", {})
for name, repo in (("claude-code-warp", "warpdotdev/claude-code-warp"),
                   ("openai-codex", "openai/codex-plugin-cc"),
                   ("i-have-adhd", "ayghri/i-have-adhd")):
    mk.setdefault(name, {"source": {"source": "github", "repo": repo}})
mk["pi-plan-goal"] = {"source": {"source": "directory", "path": os.path.join(pg, "claude-code")}}
json.dump(s, open(path, "w"), indent=2)
PY
say "Settings merged (backup kept next to settings.json)."

# --- tools ---
if [ "$WITH_TOOLS" = 1 ]; then
  ( cd "$AW/tools/render-kit" && npm ci )
  ( cd "$AW/tools/scene-engine" && npm ci && python3 -m venv .venv && .venv/bin/pip install python-pptx==1.0.2 )
fi

say "Done. Restart Claude Code. API keys, MCP servers and the dcg program are not part of this package."
