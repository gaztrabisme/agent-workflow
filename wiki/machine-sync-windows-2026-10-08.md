# Machine sync: knowledge base, skills, scene-engine

How to bring a second Windows work machine to the same setup as this one. This was set up on 2026-10-08 on the first machine (`HuyTL10`, Windows 11). Written for Huy and for an agent he asks to do the work.

**Stop before Part 5.** The other machine has its own `CLAUDE.md` and possibly its own skill edits. Nothing in Part 4 or Part 5 overwrites them without Huy reviewing first.

## End state

| Piece | Where | State after sync |
|---|---|---|
| Knowledge base (MCP server) | `~/knowledge-base` | Release `data-v10`, **full** edition: technical books (`developer_knowledge_v10`) + philosophy collection. Old v9 data removed. |
| Owner's skills repo | `~/Documents/Work/tools/agent-workflow` | Clone of `gaztrabisme/agent-workflow` at `0621c7e`, plus 3 local Windows fixes for scene-engine. Never pushed. |
| `~/.agent-workflow` | junction → the repo above | Skills use this path to find the owner's tools. |
| Skills | `~/.claude/skills` (a local git repo) | Owner's skills merged with Huy's local rules. One commit per step, starting from a snapshot. |
| Video tool | `agent-workflow/tools/scene-engine` | Renders MP4 on Windows with a portable Node 24. Replaces the old `screencast` skill. |
| `~/.claude/CLAUDE.md` | per machine | Character section changed (Part 5). Human-reviewed merge only. |

## What to carry from this machine

The other machine cannot rebuild these from GitHub alone. The owner's release has core-only code without the Windows fixes, and the skill merge and scene-engine fixes exist only here. Run these on **this** machine and copy the `machine-sync` folder over:

```bash
OUT=~/machine-sync; mkdir -p $OUT
# 1. skills: whole history, including the pre-merge snapshot
git -C ~/.claude/skills bundle create $OUT/claude-skills.bundle --all
# 2. scene-engine Windows fixes as patches on top of the owner's 0621c7e
git -C ~/Documents/Work/tools/agent-workflow format-patch 0621c7e..HEAD -o $OUT/scene-engine-patches
# 3. knowledge-base code (philosophy-capable, v10, Windows fixes); no data
tar -czf $OUT/knowledge-base-code.tar.gz -C ~ knowledge-base/knowledge_base knowledge-base/scripts knowledge-base/pyproject.toml knowledge-base/uv.lock knowledge-base/data/catalog.json
cp ~/.claude/skills/README.md $OUT/
```

## Tokens

Two fine-grained GitHub tokens, both **Contents: Read-only**, both created by the repo owner (`gaztrabisme`):
- one for `knowledge-base` (release download)
- one for `agent-workflow` (clone + Git LFS course files)

The owner can make one token that covers both. Test a token before using it: HTTP `200` means access, `404` means the token does not cover that repo.

```bash
curl -s -o /dev/null -w '%{http_code}\n' -H "Authorization: Bearer $T" https://api.github.com/repos/gaztrabisme/<repo>
```

Never write a token to a file, a git config, or a credential store. Pass it only through environment variables for one command.

## Part 0: Prerequisites

| Need | Check | Note |
|---|---|---|
| git, git-lfs | `git lfs version` | |
| Python ≥ 3.11.4 and `uv` | `python --version`, `uv --version` | `python3` on Windows is a Store stub; use `python`/`uv`. |
| curl | | Used instead of `gh`, which is not needed. |
| FFmpeg + ffprobe with libx264, aac, libass | `ffmpeg -encoders \| findstr x264` | For scene-engine. |
| Disk | | ~3.4 GB KB books + 1.1 GB philosophy + ~2.4 GB temporary download; ~1.3 GB course files; ~1 GB skills repo. |

Make a dated backup first: `~/.claude/CLAUDE.md`, `~/.claude/settings.json`, the whole `~/.claude/skills` folder, and the `~/knowledge-base` code (if it exists).

## Part 1: Knowledge base → data-v10 full edition

**Do not** unpack the release's `core-source.tar.gz` over the install, as the owner's `README-core.md` says to. That code is core-only: it has no philosophy tools and lacks the Windows snapshot-restore fix, which makes the restore fail with "Access is denied". Use the code carried from this machine instead.

1. Put the code in place: `tar -xzf knowledge-base-code.tar.gz -C ~`. On a fresh machine also run `uv sync --project ~/knowledge-base`.
2. Download the release files with curl. Asset IDs can change, so resolve them by name. You need `manifest.json` (the **full** one, not `core-manifest.json`), `kb-core.part00`, `kb-core.part01` and `kb-philosophy.part00` (~2.35 GB total).
   ```bash
   export T='<knowledge-base token>'; D=~/kb-transfer/release; mkdir -p $D; cd $D
   API=https://api.github.com/repos/gaztrabisme/knowledge-base/releases
   curl -s -H "Authorization: Bearer $T" $API/tags/data-v10 | python -c "import json,sys;[print(a['id'],a['name']) for a in json.load(sys.stdin)['assets']]" |
   while read id name; do case $name in manifest.json|kb-core.part*|kb-philosophy.part*)
     curl -sSL --retry 5 -C - -H "Authorization: Bearer $T" -H "Accept: application/octet-stream" $API/assets/$id -o $name;; esac; done
   unset T; sha256sum kb-*.part*   # compare with manifest.json
   ```
3. Run the installer with UTF-8 output. Without it, its last step crashes printing a Vietnamese character from the philosophy test result.
   ```bash
   PYTHONUTF8=1 PYTHONIOENCODING=utf-8 uv run --project ~/knowledge-base python ~/knowledge-base/scripts/install.py \
     --dir "$(cygpath -w ~/knowledge-base)" --edition full --release-tag data-v10 --local-release "$(cygpath -w ~/kb-transfer/release)"
   ```
   It must end with `Installed full edition, release data-v10`. Re-running is safe; it skips collections that are already restored.
4. Remove the old data, only after confirming the alias points to v10:
   ```bash
   curl -s localhost:6333/aliases          # developer_knowledge -> developer_knowledge_v10
   curl -s -X DELETE localhost:6333/collections/developer_knowledge_v9
   rm -rf ~/kb-transfer; rm -f ~/knowledge-base/.kb-download/kb-*
   ```

What the carried code changes compared with the owner's code, so you can redo it by hand if needed:
- `scripts/install.py`: `developer_knowledge_v9` → `_v10` (4 places), default `--release-tag data-v10`.
- `scripts/install.py` `_pid_is_running`: on Windows, check with `tasklist /FI "PID eq <pid>"`. `os.kill(pid, 0)` on Windows **terminates** the process instead of probing it, and raises WinError 87 when it doesn't exist.
- `knowledge_base/server.py`: adds the release's "read in steps" search guidance to the server instructions: search, read in context, search again with the passage's terms, find a second book, name book and chapter.

## Part 2: Owner's repo on Windows

Plain `git clone` fails on Windows:
- 4 course PDFs have `:` in their names.
- Some `zalo-platform` paths exceed 260 characters.
- `core.autocrlf=true` adds CRLF line endings, which break scene-engine's shell scripts.

```bash
export T='<agent-workflow token>'
H="AUTHORIZATION: basic $(printf 'x-access-token:%s' "$T" | base64 -w0)"
R=~/Documents/Work/tools/agent-workflow; mkdir -p ~/Documents/Work/tools
GIT_LFS_SKIP_SMUDGE=1 GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=http.https://github.com/.extraheader GIT_CONFIG_VALUE_0="$H" \
  git -c core.longpaths=true -c core.protectNTFS=false -c core.autocrlf=false clone --no-checkout https://github.com/gaztrabisme/agent-workflow.git $R
cd $R
git config core.longpaths true; git config core.protectNTFS false; git config core.autocrlf false
git sparse-checkout init --no-cone; printf '/*\n!*:*\n' > .git/info/sparse-checkout
GIT_LFS_SKIP_SMUDGE=1 git checkout 0621c7e -B main
git ls-files -z | grep -z ':' | xargs -0 git update-index --skip-worktree
GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=http.https://github.com/.extraheader GIT_CONFIG_VALUE_0="$H" git lfs pull
unset T H
git am ~/machine-sync/scene-engine-patches/*.patch     # the 3 Windows fixes
git status --short | wc -l                             # expect 0
```

Then create the junction (PowerShell, no admin needed):
```powershell
New-Item -ItemType Junction -Path "$env:USERPROFILE\.agent-workflow" -Target "$env:USERPROFILE\Documents\Work\tools\agent-workflow"
```

**Do not run the owner's `install.sh` or `bootstrap.sh`:**
- It replaces `~/.claude/CLAUDE.md` with a link to the owner's copy.
- It merges hooks and plugins into `settings.json`.
- It expects macOS (`python3`, symlinks).

## Part 3: scene-engine (video)

Follow `tools/scene-engine/WINDOWS.md` (included in the patches). In short:
- Unzip the portable Node 24 (`node-v24.21.0-win-x64.zip` from nodejs.org) to `~/Documents/Work/tools/node24`. Put it first on PATH only in the shell that runs the tool. **Leave the system Node alone**; other projects use it.
- Install the dependencies: `npm ci` in `scene-engine` and `render-kit`, then `uv venv .venv --python 3.11` and `uv pip install --python .venv/Scripts/python.exe python-pptx==1.0.2`.
- Chromium 1243 is needed in `%LOCALAPPDATA%\ms-playwright` (`npx playwright install chromium` if missing).
- Check: `npm run samples` (~4 min) produces `out/explainer.mp4`. ffprobe should show 1920×1080, h264, 30 fps, 32 s. Extract one frame and look at it.
- Known gaps on Windows:
  - `check --pptx` needs poppler's `pdftoppm`.
  - The symlink test needs Developer Mode.
  - Keynote checks are macOS-only.
  - On this machine: 50/53 tests pass, 2 skipped, 1 fail (`pdftoppm`).

## Part 4: Skills (human review where the other machine has its own edits)

The merged result lives in the bundle. Do not copy it over blindly: the other machine's skills may carry edits this machine never saw.

1. On the other machine, commit everything in its `~/.claude/skills` first ("snapshot before sync"). If it is not a git repo, `git init` it and commit. Then run `git config core.longpaths true`.
2. Fetch this machine's result next to it: `git fetch ~/machine-sync/claude-skills.bundle master:from-machine-1`.
3. For each skill, compare the other machine's folder with `from-machine-1` (`git diff HEAD from-machine-1 -- <skill>`):
   - **Identical to this machine's pre-merge snapshot** (`a3303f4` in the bundle) → take `from-machine-1`'s version.
   - **Different from that snapshot** → that machine has its own edits. Show Huy the diff and let him decide before anything is replaced.
4. Apply the decisions below, one commit per step.

**Decisions taken on machine 1** (apply the same unless Huy says otherwise):

| Action | Skills | Why |
|---|---|---|
| Add from the owner's repo | applied-ml-problem-solver, ceric, color-theory, communication, domestika-course-archive, frontend, information-design, motion, photo, physical-product-design, presentation, product-management, project-management, reddit-corpus, skill-builder, ux, visual-design, zalo-platform | New. `omlx` skipped: Apple Silicon only. |
| Owner's version as is | core, dev | Nothing local was missing (dev's ML guidance moved to applied-ml-problem-solver). |
| Owner's version + re-added local rules | business-intelligence (stop-and-ask "loop-back" triggers), solution-architect (close-out checklist), delivery (pre-signature exception, client-register gate, 3 anti-patterns), ai-discovery-workshop (20-minute form), drawio (editing an existing diagram; **keep** the `.drawio` source after export), conductor (mid-run stop must carry its own context and a recommendation), evolution (standing-corrections inbox, `harvest.py`; old runs archived out of the skill) | Owner's are newer rewrites; these rules came from Huy's own corrections. |
| Dropped | business-intelligence `research-sprint/` | conductor now plans research steps. |
| Removed | pptx (→ presentation), redesign-existing-projects (→ frontend), color-expert (→ color-theory), design-taste-frontend, design-taste-frontend-v1, gpt-taste, stitch-design-taste, minimalist-ui, high-end-visual-design, industrial-brutalist-ui, orchestration, screencast (→ scene-engine via presentation + motion) | Replaced, or retired by Huy. |
| Kept | brandkit, fpt-infographics, full-output-enforcement, image-to-code, imagegen-frontend-mobile, imagegen-frontend-web, xlsx | No equivalent in the owner's package. |

Commits on machine 1, in order: `a3303f4` snapshot → `04fbea5` removals → `5ec072a`…`e23aa8f` five merges → `126665f` 18 new skills → `465ce3c` core+dev → `4d692d0` conductor → `36a3601` evolution → `1f97d50` remove screencast.

Known loose end: the owner's conductor routing mentions a `harness-operator` skill that is not in his package.

## Part 5: CLAUDE.md (human review required)

The other machine's `CLAUDE.md` is different. **Do not copy this machine's file over it, and do not edit it without Huy approving the exact text.** Show him the proposal below and wait.

Changes made on machine 1, all inside `## Character`:

1. **"Look within first"**: appended "When you catch yourself explaining why a rule doesn't apply this time, follow it or ask; don't act on the exception." (From the owner's version, with his internal tag removed.)
2. **"Refinement"** replaced with:
   > **Refinement:** when a mistake recurs, search the philosophy collection (`search_philosophy`) for the passage that speaks to it, and propose one edit here with Huy. Start from the Original Library, but treat it as the entry point of a multi-step search, not the answer: follow the terms and ideas it surfaces into the other books in the philosophy collection, and compare what they say before proposing. The section stays under 15 lines: an added line replaces or merges an existing one.

Item 2 needs Part 1's full edition; without it, `search_philosophy` doesn't exist.

Kept from machine 1's own version, not taken from the owner's: second-person voice ("you", not "I"); the Tao Te Ching 64 line under Non-forcing; the pointer from Truthfulness to Global Context. The rest of the owner's `CLAUDE.md` (his GPU workstation, the Mac-only local model server) was not taken.

If the other machine has no Character section, show Huy machine 1's whole section and ask whether to add it.

## Verification

- `claude mcp list` → `knowledge-base … ✔ Connected`. `curl localhost:6333/collections` → only `developer_knowledge_v10` and `philosophy`.
- `cat ~/knowledge-base/.kb-install.json` → `"edition": "full", "tag": "data-v10"`.
- `git -C ~/Documents/Work/tools/agent-workflow status --short` → empty. `~/.agent-workflow` resolves to that repo.
- `git -C ~/.claude/skills status --short` → empty. The skill folder list matches Part 4. Every `SKILL.md` has `name:` and `description:`.
- Grep confirms the re-added rules: `loop-back` (business-intelligence), `Pre-signature exception` (delivery), `20-minute form` (ai-discovery-workshop), `Close-out checklist` (solution-architect), `Mid-run stops` (conductor), `standing-corrections` (evolution). `grep -i delete drawio/SKILL.md` shows no instruction to delete the `.drawio` source.
- scene-engine sample renders and plays.
- Restart Claude Code; the new skills appear in the skill list.

## How the work was run (for an agent repeating it)

- **Who does what:** the orchestrator handles anything that touches a token, every git commit, every deletion and every final check. Haiku agents compare files, copy folders and re-add rules. Each agent owns separate folders, and none of them runs git write commands. A Sonnet agent does the Windows port, which is too fiddly for Haiku.
- **Check agent claims against the files** before acting on them (grep for the rule, run ffprobe on the video, look at the frame).
- **One git process per repo at a time.** A background `git lfs pull` held `index.lock` while another agent tried to check out files, and that left 166 files deleted until the lock cleared.
- **Before deleting anything, commit it**, so every step can be reverted.
