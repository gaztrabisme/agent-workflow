# agent-workflow

Reader: the owner, setting up or updating a machine. This private repo holds the whole working setup in one place: 28 skills, three tools the design skills run, and the settings that wire them in.

## Set up a new machine

You need `git`, `git-lfs`, `python3` and `node` (version 18 or later).

```bash
git clone https://github.com/gaztrabisme/agent-workflow.git ~/Documents/Work/tools/agent-workflow
cd ~/Documents/Work/tools/agent-workflow
git lfs install
./install.sh --with-tools
```

The first clone downloads about 1.2 GB of course images and PDFs through Git LFS (GitHub's large-file storage). Each full clone counts against the 10 GiB monthly LFS download allowance of the GitHub account.

`install.sh` is safe to run again. It:
- links the 28 skills into `~/.claude/skills`, and into `~/.codex/skills` and `~/.agents/skills` when those folders exist;
- removes links to retired skills in those folders (listed in `config/retired-skills.txt`);
- links `~/.claude/CLAUDE.md` to `config/claude/CLAUDE.md` (an existing different file is backed up first);
- creates `~/.agent-workflow`, a link to this repo that the skills' instructions use to find the tools;
- merges into `~/.claude/settings.json` (a backup is kept next to it): the command guard hook, the code-quality hook, the seven plugins and their sources, including the `plan-goal` plugin, which it clones from `gaztrabisme/pi-plan-goal` next to this folder;
- with `--with-tools`, installs the dependencies of `tools/render-kit` and `tools/scene-engine`.

Restart Claude Code afterwards.

## Update a machine

```bash
cd ~/Documents/Work/tools/agent-workflow
git pull
./install.sh
```

After editing a skill on any machine, commit and push from this repo. The skills are linked into the agents, so an edit here is live at once.

## What is not in this repo

- **API keys.** Put them in `~/.config/agent-capabilities/subagent.env` on each machine.
- **MCP servers.** `subagent`, `knowledge-base`, `github-docs`, `markitdown` and `chrome-devtools` are registered per machine. The knowledge base is its own repo, `gaztrabisme/knowledge-base`, with its data in the `data-v10` release.
- **`dcg`, the destructive-command guard.** A compiled program expected at `~/.local/bin/dcg`; the installer warns when it is missing.
- **`ruff`.** The code-quality hook uses it on Python files and does nothing if it is not installed.
- **Anthropic's own skills** (`docx`, `xlsx`) and every third-party skill.

## Layout

```
skills/        28 skills, each with its commit history (tags: <skill>/pre-stage-b is the state before the work-skill rebuild)
tools/         render-kit (chart and slide checks), scene-engine (video and PowerPoint), brand-profile (style draft)
config/        claude/CLAUDE.md, hooks/claude-quality-hook, retired-skills.txt
skills.txt     the skill names install.sh links
wiki/          goal file and record of how this package was built
```

To undo the rebuild of one work skill: `git checkout <skill>/pre-stage-b -- skills/<skill>`.

## Mac-only paths still in the files

Instructions in the skills now reach the tools through `~/.agent-workflow`. These files still name folders that exist only on the original Mac (`/Users/GaryT/...`, or `~/Documents/Work/lab/...`) and will point nowhere elsewhere. All are records of past runs or notes, except where marked:

- `skills/*/DISTILL-REPORT.md`, `skills/photo/TOOLS-REPORT.md` and the `audit/` folders: logs of how each skill was built.
- `skills/frontend/references/sources.md`: links to research reports under `lab/`.
- `skills/conductor/references/goal-file.md` (example goal file) and `lane-plan.md` (the location of the `subagent` server's source, `~/Documents/Work/tools/mcp/subagent-mcp`): both are reference text, not scripts.
- `skills/photo/TOOLS.md`: names this Mac's Python interpreter (`/Users/GaryT/miniconda3/bin/python3`) as the one verified; any Python 3 with NumPy and Pillow works.
- `tools/render-kit/SPEC.md`: cites the research folder under `lab/`.
