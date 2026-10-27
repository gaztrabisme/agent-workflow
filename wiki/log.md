# Log

## 2026-10-03 — package built and this Mac switched over

Reader: whoever resumes work on this repo. Goal file: `goals/2026-10-03-agent-workflow.md`.

**What was done**
- Created the private repo `gaztrabisme/agent-workflow` from 27 skill repos (with their commit history and the 11 `pre-stage-b` tags), `physical-product-design` (no earlier git history), and the three tools `render-kit`, `scene-engine` and `brand-profile`.
- Converted 7,038 images, PDFs and audio files to Git LFS across all history (git objects 9.8 MB, LFS 1.2 GB).
- Wrote `install.sh`, `README.md`, the settings merge, and `config/` (CLAUDE.md, the code-quality hook, the retired-skill list).
- Removed the oMLX key from `CLAUDE.md` and from the history of two old `dev` commits before the first push.
- Published knowledge-base release `data-v10` (330,778 points; gate PASS 2026-10-02) and moved the knowledge-base release tooling and installer default to it.
- Switched this Mac: links for Claude, Codex and the shared agents folder now resolve into the package; `~/.claude/CLAUDE.md` links to `config/claude/CLAUDE.md`; read-once and the post-compaction reminder hooks removed; github-docs moved to `tools/mcp/github-docs` and its three config files repointed; old copies moved to the Trash (31) or `tools/_archive/skills-leftovers` (30); the 26 old GitHub skill repos archived.

**Forks decided forward** (owner approved the plan with "Go"; these were not separately asked)
- Course images and PDFs: Git LFS with full history, not release downloads.
- `tools/skills` keeps `docx`, `xlsx` (Anthropic's, not packaged) and `.claude` (session goal state).
- plan-goal plugin stays its own public repo; the installer clones it next to the package.
- The code-quality hook is packaged unchanged.
- Old repos archived rather than deleted; deletion is the owner's.

**Found while doing it, fixed**
- render-kit's `value` check looked for color-theory one level too shallow after the move and silently skipped; fixed and re-tested (48/48).
- The first installer skipped the Write hook (duplicate check ignored the matcher), mis-detected LFS placeholders, and aborted on a malformed `settings.json`; fixed after an independent review.
- 60 skill-doc links to the tools broke with the move; repaired and checked.
- A copied `.venv` pointed at the old folder; rebuilt in place.

**UAT**

| Row | Result | Evidence |
|---|---|---|
| G1 private repo | PASS | `gh repo view` prints PRIVATE |
| G2 28 skills valid | PASS | `skills-ref validate` on all 28, run twice (fresh clone, then final) |
| G3 history and tags | PASS, with one note | Subjects of all 25 archived repos compared with the package: all present except one color-theory subtree-merge commit whose message embeds an old commit hash that the import rewrote; the merge exists. ceric, domestika-course-archive and physical-product-design have no GitHub copy to compare; their counts were checked before the push. |
| G4 LFS | PASS | Fresh clone from GitHub before the last commits: 7,038 files present, 0 placeholders; no LFS-tracked path changed since |
| G5 Linux install | PASS | Copy of the fresh clone on the GPU PC, empty home: 28 links each for the three agents, second run clean, 0 placeholders. The clone itself was made on this Mac (the PC has no GitHub login). |
| G6 tools | PASS | render-kit 48/48 and selftest with nothing skipped; scene-engine 52 pass, 0 fail, 1 skipped (the Keynote check, which waits on an owner permission) |
| G7 hooks | PASS | settings.json: quality hook for Edit and Write from the package, dcg present, no read-once, no reminder |
| G8 links | PASS | 0 problems across the three agent folders and CLAUDE.md |
| G9 old copies | PASS | no old skill or tool folder; `_archive` exists; github-docs path in 3 configs |
| G10 data-v10 | PASS | all three parts downloaded and matched to the manifest's SHA-256 |
| G11 archived | PASS | 26 of 26 archived |
| G12 README | PASS | grep |

**Open**
- The folder `~/aw-test` on the GPU PC (2.6 GB, my test copy of this repo) is still there and can be deleted.
- The code-quality hook's output may not reach the model; unchecked in a live session.
- scene-engine cannot find Chromium on Linux (macOS cache path only).
- `~/.claude/reference/bppc.md` and the `dcg` program are not in the package.
- Deleting the 26 archived GitHub repos is the owner's call; `retired-repos.txt` has the names.
- The `dev` skill's old public history may contain the oMLX key (a local-server key); the new repo is clean.

## 2026-10-11 — reward-design skill (run 2026-10-10-reward-skill)

Owner asked for a skill on "hitting the dopamine release" in presentations, videos, UI and infographics, sourced from research, books and industry practice. Owner at go: "You orchestrate Codex only." Goal file: `wiki/goals/2026-10-10-reward-design-skill.md`. Run folder: `~/Documents/Work/lab/reward-skill-run/`.

| Run ID | Unit | Lane | Verdict | Acceptance | Note |
|---|---|---|---|---|---|
| 2026-10-10-reward-skill | A brain science | codex | PASS | check_findings: 25 entries; A9 read | — |
| 2026-10-10-reward-skill | B visual | codex | PASS | 25 entries | — |
| 2026-10-10-reward-skill | C sound | codex | PASS | 25 entries | — |
| 2026-10-10-reward-skill | D industry | codex | PASS | 25 entries; D3 read | — |
| 2026-10-10-reward-skill | E books | codex | PASS | 29 entries | — |
| 2026-10-10-reward-skill | V claim check | codex (fresh session) | PASS | 129 rows: 122 supported, 7 weakened, 0 unsupported; A21, B6, D24 read | First launch carried the research rules by a launcher bug; stopped and relaunched clean |
| 2026-10-10-reward-skill | S build | codex | PASS | verify.sh PASS; scope diff clean; SKILL.md read | — |
| 2026-10-10-reward-skill | T dogfood | codex | done; skill verdict FAIL | 27/27 checks on deck and on explainer | Skill not self-sufficient for critique: 19 findings |
| 2026-10-10-reward-skill | F fix round | codex | PASS | verify.sh PASS; all 11 ffmpeg/ffprobe commands run on the explainer | F01–F20 resolved, incl. coordinator F20 quick start |

**UAT:** G1 PASS, G2 PASS, G3–G7 PASS (`check-skill.sh`), G8 PASS (5/5 pointers).

**Open**
- Skill verdict PENDING: one real use (critique). Needs a second, independent real use, ideally planning a new piece, before KEEP.
- The fixed critique workflow has not been re-run end to end; next real use is that test.
- claude.ai copy not made: run `./scripts/make-cloud-zips.sh` and upload `reward-design` if wanted there.
- Not committed (owner commits).

## 2026-10-15 — Work-laptop setup merged on branch `merge-2026-10-15`

- Source: the work laptop's package `claude-setup-2026-10-15.zip` (forked from `0621c7e` on 2026-10-08). Branches: `mac-wip-2026-10-15` (the Mac's uncommitted work plus GitHub's per-machine split), `work-laptop-2026-10-15` (the package, line endings fixed), `merge-2026-10-15` (both).
- Owner decisions (Huy, 15 Oct): `project` replaces `conductor` and `project-management`; the work laptop's `xlsx` replaces the Mac's copy of Anthropic's (which stays in `~/Documents/Work/tools/skills/xlsx`); the `require_load.py` brief hook is installed on the Mac.
- Mac conductor edits carried into `project`: the provider-lane dynamic workflow, the plan-goal goal block, and the `epi` lane in `references/run/lane-plan.md`.
- `CLAUDE.md`: the laptop's Voice, question, don't-invent and Character sections, plus the Mac's Documents, routing (now `project`), lanes and machine import. The laptop's LSP "two hats" paragraph moved to `config/claude/machines/huytl10.md`.
- Left out of the package: `dev/AGENTS.md` (a symlink flattened to text by Windows), `skills/.gitignore`, the 2026-08-11 `skills-patches`, the laptop's project memory notes, and its three scene-engine Windows fixes (not in the package).
- Not merged to `main`, not pushed, not installed; waits for Huy's review.

## 2026-10-23 · Improver · `machines/mcbob.md`: no `timeout` command on this Mac
- Evidence: a freelancing session (2026-10-18) failed with `command not found: timeout`; the bob session's review (2026-10-20) records the same failure in its daily-look script. The perl workaround was written only in `skills/project/references/run/lane-plan.md`.
- Change: one bullet under "Working on this Mac". Disproved if the failure recurs. Verdict PENDING, revisit 2026-11-06. Revert: `git revert <sha>`.

## [2026-10-27] run | wiki tool, autoresearch MCP server and wiki search built and checked (goal 2026-10-27-wiki-autoresearch-tools, all rows pass; see its amendments). Commits: agent-workflow main; subagent-mcp branch autoresearch-aware (worktree subagent-mcp-wt/autoresearch-aware); autoresearch-mcp main (new local repo); knowledge-base branch wiki-corpus (worktree knowledge-base-wt/wiki-corpus). Nothing pushed or merged.
