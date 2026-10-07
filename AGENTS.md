# AGENTS.md

Reader: a coding agent (Claude Code, Codex, Gemini CLI, Antigravity, pi, omp, opencode, grok) working inside this repo. For installing the package on a machine, read `README.md` instead.

## What this repo is

The single source of the owner's agent skills. Each folder in `skills/` is one skill: a `SKILL.md` (instructions plus the frontmatter that tells an agent when to load it), with optional `references/`, `scripts/`, `modes/` and `tests/`. `install.sh` symlinks every skill named in `skills.txt` into each agent's skills folder, so **an edit here is live in every agent at once**. Nothing is copied, except for claude.ai (see "claude.ai copies").

| Path | What it holds |
|---|---|
| `skills/<name>/` | One skill. `SKILL.md` is the entry point. |
| `skills.txt` | The skill names `install.sh` links. One per line. |
| `config/retired-skills.txt` | Names whose old links `install.sh` removes from every agent folder. |
| `config/claude/CLAUDE.md` | The owner's global instructions. `~/.claude/CLAUDE.md` is a symlink to it. |
| `config/hooks/claude-quality-hook` | Post-edit hook that runs `ruff` on Python files. |
| `tools/` | `render-kit`, `scene-engine`, `brand-profile`: programs the design skills run. Skills reach them through `~/.agent-workflow/tools/...`, never through a Mac path. |
| `scripts/make-cloud-zips.sh`, `scripts/cloud_merge.py` | Build the claude.ai upload zips. |
| `wiki/` | Decisions, log, goal files. Internal notes, not instructions. |

## Where each agent reads skills

`install.sh` links into these folders (the last three only when `~/.codex`, `~/.agents` or `~/.gemini` exists):

| Folder | Read by |
|---|---|
| `~/.claude/skills` | Claude Code, omp, grok, opencode |
| `~/.codex/skills` | Codex |
| `~/.agents/skills` | pi, and other agents following the `.agents` convention |
| `~/.gemini/skills` | Gemini CLI |
| `~/.gemini/config/skills` | Antigravity |

Do not add links to `~/.config/opencode/skills`, `~/.omp/agent/skills`, `~/.pi/agent/skills`, `~/.grok/skills` or `~/.copilot/skills`: those agents already read one of the folders above, and a second copy of a name makes opencode warn about duplicates. `install.sh` only removes retired links there.

## Rules for changes

- **Add a skill:** create `skills/<name>/SKILL.md`, add `<name>` to `skills.txt`, run `./install.sh`. The folder name, the `name:` in the frontmatter and the line in `skills.txt` must match.
- **Retire a skill:** remove its line from `skills.txt`, add it to `config/retired-skills.txt`, delete or keep the folder as the owner decides, run `./install.sh`.
- **Rename a skill:** both of the above. Then search the other skills for the old name (`grep -rn '<old>' skills/`), since skills route to each other by name.
- **Never put a real folder** with a skill's name in an agent's skills folder. `install.sh` leaves real folders alone and warns, so that agent would keep a stale copy.
- **Paths in instructions:** reach tools and other skills through `~/.agent-workflow/...` or a relative path (`../core/references/...`). `/Users/GaryT/...` appears only in build records (`EVOLUTION.md`, `DISTILL-REPORT.md`, `audit/` and the files the README lists); do not add it to instructions.
- **Large binaries** (images, PDFs, audio, video, zips) go through Git LFS; `.gitattributes` already routes them. Check with `git lfs ls-files` before committing a new type.
- **`EVOLUTION.md`** in each skill records real-use lessons. Use the `evolution` skill to add entries; use `skill-builder` to change a skill's structure or trigger.
- **`skills/dev/AGENTS.md`** is a symlink to `skills/dev/CLAUDE.md` and covers only that skill.
- Run `./install.sh` after any change to `skills.txt`, `config/retired-skills.txt` or `install.sh`. Editing a file inside an existing skill needs no re-run. Restart the agent so it reloads the skill list.
- Commit and push only when the owner asks. The machines' read-only tokens cannot push.

## claude.ai copies

claude.ai keeps its own uploaded copies; they do not follow this repo. Claude Code's desktop app syncs them into `~/.claude/skills/synced/<account-id>/`, where they appear as `anthropic-skills:<name>` next to the linked `<name>`. After changing a skill's text, run `./scripts/make-cloud-zips.sh` and re-upload that skill's zip in claude.ai under Settings → Customize → Skills. A zip may hold at most 200 files; `color-theory`, `photo` and `zalo-platform` are merged by `cloud_merge.py` to fit.

## Check that every agent sources from here

```bash
REPO=$(cd ~/.agent-workflow && pwd -P)
for d in ~/.claude/skills ~/.codex/skills ~/.agents/skills ~/.gemini/skills ~/.gemini/config/skills; do
  [ -d "$d" ] || continue
  while read -r n; do
    r=$(cd "$d/$n" 2>/dev/null && pwd -P)
    [ "$r" = "$REPO/skills/$n" ] || echo "$d/$n -> ${r:-missing}"
  done < "$REPO/skills.txt"
done
```

No output means every listed skill in every agent folder resolves to this repo.
