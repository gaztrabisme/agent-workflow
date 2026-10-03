# Goal — 2026-10-03 — agent-workflow package

**Status:** APPROVED (owner "Go", 2026-10-03).

**Decision owner / author:** Huy, 2026-10-03. **Audited by:** the coordinator at Close, against this file only. **Contact:** Huy.

Shorthand: A = `~/Documents/Work/tools/agent-workflow`; the skill list is `A/skills.txt` (28 names); the retired-repo list is `A/wiki/retired-repos.txt` (26 names).

## Deliverable — private repo `gaztrabisme/agent-workflow`

| ID | Source | Success criterion | Artifact | UAT |
|---|---|---|---|---|
| G1 | owner: one private repo | The repo exists on GitHub and is private | GitHub repo | `gh repo view gaztrabisme/agent-workflow --json visibility -q .visibility` prints `PRIVATE` |
| G2 | owner: all skills in one repo | Every skill in `skills.txt` has `skills/<name>/SKILL.md` and passes the spec validator | `A/skills/` | for each name: `npx -y skills-ref@latest validate A/skills/<name>` exits 0 |
| G3 | default: keep history | Each skill that had a git repo keeps its commits, and its `pre-stage-b` tag where one existed | `A/.git` | for each such skill: commit count of `git log --oneline -- skills/<name>` ≥ commit count of its old repo's default branch; `git tag -l '<name>/pre-stage-b'` non-empty where the old repo had the tag |
| G4 | default: Git LFS | Course images, PDFs and video are stored in LFS, and a fresh clone holds real files, not LFS pointers | fresh clone | in a fresh clone: `git lfs ls-files` non-empty, and no tracked `*.jpg *.png *.pdf *.mp4` file starts with `version https://git-lfs` |
| G5 | owner: move to other machines | A fresh clone on the Linux PC installs cleanly into an empty home folder and links every skill for Claude, Codex and the shared agents folder | bppc temp home | `HOME=<tmp> ./install.sh` exits 0, and each of `<tmp>/.claude/skills`, `<tmp>/.codex/skills`, `<tmp>/.agents/skills` holds a resolving link for every name in `skills.txt` |
| G6 | owner: tools in the package | render-kit and scene-engine pass their test suites from their new place on this Mac | `A/tools/` | `npm test && ./bin/rk selftest` in `A/tools/render-kit`; `npm test` in `A/tools/scene-engine` |
| G7 | owner: hooks | Live settings on this Mac run the command guard and the code-quality hook from the package; read-once and the post-compaction reminder are no longer hooked | `~/.claude/settings.json` | grep finds `agent-workflow/config/hooks/claude-quality-hook` and `dcg`; grep finds no `read-once` and no `post-compact-reminder` |
| G8 | owner: one local place | On this Mac every skill link in `~/.claude/skills`, `~/.codex/skills` and `~/.agents/skills` for a name in `skills.txt` resolves into `A/skills/`; no link to a retired skill remains in those three folders; `~/.claude/CLAUDE.md` resolves to `A/config/claude/CLAUDE.md` | link folders | a script over the three folders prints 0 problems |
| G9 | owner: one local place | The old copies are gone from `tools/`: no `tools/skills/<name>` for a name in `skills.txt`, no `tools/render-kit`, `tools/scene-engine`, `tools/brand-profile`; the other folders that were in `tools/skills` are in `tools/_archive/`; github-docs is at `tools/mcp/github-docs` and both Claude's and Codex's config point there | `tools/` | `test ! -e` for each old path; `test -d tools/_archive`; `grep -c tools/mcp/github-docs ~/.claude.json ~/.codex/config.toml` ≥ 1 each |
| G10 | owner: KB on v10 | Release `data-v10` exists on `gaztrabisme/knowledge-base` and every asset's SHA-256 matches its manifest | GitHub release | download each asset and compare with `manifest.json` |
| G11 | owner: remove other skill repos | Every repo in `retired-repos.txt` is archived on GitHub (deletion is left to the owner) | GitHub | `gh repo view gaztrabisme/<r> --json isArchived -q .isArchived` prints `true` for each |
| G12 | default: README | The README says how to set up a new machine and how to update, and lists the remaining files with paths that only exist on this Mac | `A/README.md` | `grep -q 'install.sh' A/README.md && grep -q 'Mac-only paths' A/README.md` |

## Working pattern (binds this run)
Coordinator-direct: the work is git import, file moves, configuration and one installer script (wiring). No subagent lanes. One fresh-context Claude agent reviews the installer and README before the remote repos are archived.

## Amendments
(none)

## Branch resolutions (before dispatch)
- plan-goal plugin: stays in its own repo; the settings template enables it (recommendation accepted with "Go").
- Tools: inside the package. Course binaries: Git LFS with full history. Mac-only paths: listed, not fixed, except paths to folders this run moves, which are repointed so this Mac keeps working. Old local copies: Trash (packaged) or `tools/_archive/` (not packaged).
