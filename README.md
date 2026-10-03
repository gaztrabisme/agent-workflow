# agent-workflow

Reader: the owner, setting up or updating a machine. This private repo holds the whole working setup in one place: 28 skills, three tools the design skills run, and the settings that wire them in.

## Set up a new machine

Needed: `git`, `git-lfs`, `python3`, and credentials for the private repo (for example `gh auth login`). The tools also need Node 24 or later; see "The tools" below.

Run `git lfs install` before the clone. Without it the course images and PDFs arrive as 130-byte placeholders. The installer notices and fetches them, but it needs network access to do so.

```bash
git lfs install
git clone https://github.com/gaztrabisme/agent-workflow.git ~/Documents/Work/tools/agent-workflow
cd ~/Documents/Work/tools/agent-workflow
./install.sh
```

The clone downloads about 1.3 GB of course images and PDFs through Git LFS (GitHub's large-file storage). Each full clone counts against the 10 GiB monthly LFS download allowance of the GitHub account.

`install.sh` is safe to run again. It:
- links the 28 skills into `~/.claude/skills`, and into `~/.codex/skills` and `~/.agents/skills` when those folders exist;
- removes links with a retired skill's name in those folders (listed in `config/retired-skills.txt`);
- links `~/.claude/CLAUDE.md` to `config/claude/CLAUDE.md` (an existing different file is backed up first);
- creates `~/.agent-workflow`, a link to this repo that the skills' instructions use to find the tools;
- merges into `~/.claude/settings.json` (a dated backup is kept next to it): the command-guard hook (only if `~/.local/bin/dcg` exists), the code-quality hook, the seven plugins and their sources. It clones `gaztrabisme/pi-plan-goal` next to this folder for the `plan-goal` plugin; if that fails, the plugin is left out;
- with `--with-tools`, installs the dependencies of `tools/render-kit` and `tools/scene-engine`.

Restart Claude Code afterwards.

## Update a machine

```bash
cd ~/Documents/Work/tools/agent-workflow
git pull
./install.sh
```

After editing a skill on any machine, commit and push from this repo. The skills are linked into the agents, so an edit here is live at once. The same holds for `CLAUDE.md`: `~/.claude/CLAUDE.md` is a link to `config/claude/CLAUDE.md`, so changes to it show up here as uncommitted edits.

## The tools

`tools/render-kit` (chart and slide checks), `tools/scene-engine` (video and PowerPoint) and `tools/brand-profile` (style draft) are used by the design skills. `./install.sh --with-tools` runs `npm ci` in the first two and creates the Python environment `scene-engine` needs. It does not install the rest of what they use:

- Node 24 or later (both declare `>=24`).
- Chromium for Playwright. `scene-engine` looks for it only in the macOS cache folder (`~/Library/Caches/ms-playwright`), so it does not run on Linux as it stands.
- FFmpeg and `ffprobe`, and Python with NumPy and Pillow, for the video, photo and colour checks.

These tools were built and tested on macOS only.

## What is not in this repo

- **API keys.** Put them in `~/.config/agent-capabilities/subagent.env` on each machine.
- **MCP servers.** `subagent`, `knowledge-base`, `github-docs`, `markitdown` and `chrome-devtools` are registered per machine. The knowledge base is its own repo, `gaztrabisme/knowledge-base`, with its data in the `data-v10` release.
- **`dcg`, the destructive-command guard.** A compiled program expected at `~/.local/bin/dcg`. Without it the installer skips its hook and says so.
- **`ruff`.** The code-quality hook uses it on Python files and does nothing if it is not installed. The hook prints its findings to the terminal output; whether Claude Code passes that text back to the model has not been checked.
- **`~/.claude/reference/bppc.md`.** `CLAUDE.md` refers to this file for the GPU PC, and it is not in the package.
- **Anthropic's own skills** (`docx`, `xlsx`) and every third-party skill.

## Layout

```
skills/        28 skills, each with its commit history (tag <skill>/pre-stage-b is the state before the work-skill rebuild)
tools/         render-kit, scene-engine, brand-profile
config/        claude/CLAUDE.md, hooks/claude-quality-hook, retired-skills.txt
skills.txt     the skill names install.sh links
wiki/          goal file and the list of retired GitHub repos
```

To undo the rebuild of one work skill: `git checkout <skill>/pre-stage-b -- skills/<skill>`.

## Mac-only paths still in the files

Instructions in the skills reach the tools through `~/.agent-workflow`. Many files still name folders that exist only on the original Mac (`/Users/GaryT/...`, or `~/Documents/Work/lab/...`). They are records of how each skill was built, not instructions: every `EVOLUTION.md`, `DISTILL-REPORT.md`, `CLAIM-FIX-REPORT.md` and `TOOLS-REPORT.md`, the `audit/` folders, `skills/frontend/references/sources.md` and `tools/render-kit/SPEC.md`. Reference text with a Mac path: `skills/conductor/references/goal-file.md` and `lane-plan.md` (the `subagent` server's source, `~/Documents/Work/tools/mcp/subagent-mcp`) and `skills/photo/TOOLS.md` (this Mac's Python interpreter; any Python 3 with NumPy and Pillow works). To list them all: `grep -rIl '/Users/GaryT' .`
