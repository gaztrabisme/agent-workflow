# agent-workflow

Reader: the owner, or an AI agent the owner asks to set up or update a machine. This private repo holds the whole working setup in one place: 28 skills, three tools the design skills run, and the settings that wire them in.

The repo is private. A machine needs no GitHub login to install or update it: a fine-grained access token, created once by the owner and handed to the machine or agent, is enough.

## Create the access token (owner, once)

1. In GitHub, go to **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. Set:
   - **Token name:** something that names the machine, for example `aw-bppc`.
   - **Resource owner:** `gaztrabisme`.
   - **Expiration:** 1 year.
   - **Repository access:** **Only select repositories**, then `agent-workflow`. Add `knowledge-base` too if the same machine installs the knowledge base; one token then serves both installers.
   - **Permissions → Repository permissions → Contents:** **Read-only**. (`Metadata: Read-only` is added by GitHub.) Leave everything else unset.
3. Generate it, copy it, and keep it somewhere safe. Give it to the machine's agent in the conversation or type it at the installer's prompt.
4. When a machine is retired, or a token was shown somewhere it should not have been, revoke it on the same GitHub page. Machines keep their copy of the skills but can no longer update.

## Install or update on any machine (an agent can do this)

Needed: `git`, `git-lfs`, `python3` and `curl`. The tools also need Node 24 or later; see "The tools" below.

Rules for an agent:
- The owner creates the token and gives it to you. You never create a token, print it, or write it to a file.
- Put it in the environment as `AW_GH_TOKEN`. `bootstrap.sh` then runs without any prompt; it passes the token to git only through environment variables, so nothing is saved in the repo, in git's configuration or in a credential store.
- Do not use plain `git clone` or `git pull` on a machine without a GitHub login; they will fail. `bootstrap.sh` does both jobs.

First install, on macOS or Linux:

```bash
export AW_GH_TOKEN="<the token the owner gave you>"
curl -fsSL -H "Authorization: Bearer $AW_GH_TOKEN" -H "Accept: application/vnd.github.raw" \
  "https://api.github.com/repos/gaztrabisme/agent-workflow/contents/bootstrap.sh" -o /tmp/aw-bootstrap.sh
bash /tmp/aw-bootstrap.sh              # add --with-tools for render-kit and scene-engine; --dir <path> to change the folder
unset AW_GH_TOKEN
```

It clones into `~/Documents/Work/tools/agent-workflow` (or `--dir`), downloads the course images and PDFs (about 1.3 GB), and runs `install.sh`. The last lines say `Linked 28 skills.` and `Done.`

Update later, from the installed copy:

```bash
export AW_GH_TOKEN="<the token>"
~/Documents/Work/tools/agent-workflow/bootstrap.sh
unset AW_GH_TOKEN
```

It pulls the latest commit, fetches any new course files and re-runs `install.sh`.

Check that it worked: `test -e ~/.claude/skills/project/SKILL.md && readlink ~/.agent-workflow` prints the install folder. Then restart the agent so it reads the new skill list.

If the script stops with "GitHub refused the token": the token has expired, was revoked, or does not include `agent-workflow` with Contents: Read-only. Ask the owner for a token that does.

Each fresh install downloads about 1.3 GB of course files, which counts against the GitHub account's 10 GiB monthly Git LFS (large-file storage) allowance. Updates download only changed files.

### A machine that cannot reach GitHub

Copy the whole folder, including the hidden `.git` folder, from a machine that has it (for example `rsync -a ~/Documents/Work/tools/agent-workflow/ <host>:~/Documents/Work/tools/agent-workflow/`), then run `./install.sh` in it. To update, copy again.

### What install.sh does

`install.sh` is safe to run again. It:
- links the 28 skills into `~/.claude/skills`, and into `~/.codex/skills`, `~/.agents/skills`, `~/.gemini/skills` (Gemini CLI) and `~/.gemini/config/skills` (Antigravity) when those agents are installed. pi reads `~/.agents/skills`; omp, grok and opencode read `~/.claude/skills`, so they need no links of their own;
- removes links with a retired skill's name in those folders (listed in `config/retired-skills.txt`);
- links `~/.claude/CLAUDE.md` to `config/claude/CLAUDE.md` (an existing different file is backed up first);
- creates `~/.agent-workflow`, a link to this repo that the skills' instructions use to find the tools;
- merges into `~/.claude/settings.json` (a dated backup is kept next to it): the command-guard hook (only if `~/.local/bin/dcg` exists), the code-quality hook, the seven plugins and their sources. It clones `gaztrabisme/pi-plan-goal` next to this folder for the `plan-goal` plugin; if that fails, the plugin is left out;
- with `--with-tools`, installs the dependencies of `tools/render-kit` and `tools/scene-engine`.

Restart Claude Code afterwards.

## Editing skills

After editing a skill, commit and push from this repo on a machine with write access to GitHub; the read-only token cannot push. The skills are linked into the agents, so an edit here is live at once. The same holds for `CLAUDE.md`: `~/.claude/CLAUDE.md` is a link to `config/claude/CLAUDE.md`, so changes to it show up here as uncommitted edits.

## The tools

`tools/render-kit` (chart and slide checks), `tools/scene-engine` (video and PowerPoint) and `tools/brand-profile` (style draft) are used by the design skills. `./install.sh --with-tools` runs `npm ci` in the first two and creates the Python environment `scene-engine` needs. It does not install the rest of what they use:

- Node 24 or later (both declare `>=24`).
- Chromium for Playwright. `scene-engine` looks for it only in the macOS cache folder (`~/Library/Caches/ms-playwright`), so it does not run on Linux as it stands.
- FFmpeg and `ffprobe`, and Python with NumPy and Pillow, for the video, photo and colour checks.

These tools were built and tested on macOS only.

## Keep claude.ai in step

`./scripts/make-cloud-zips.sh` builds one upload zip per skill (course images and PDFs left out, which keeps the six design skills under 2 MB each). Upload them in claude.ai under Settings, Customize, Skills; replace a skill's older copy when its text changed. The account's copies are separate from the package, so they change only when you re-upload. claude.ai accepts at most 200 files per zip, so `color-theory` (304 files), `photo` (233) and `zalo-platform` (2,063) go through `scripts/cloud_merge.py`, which merges their reference libraries into 130, 55 and 71 larger files (each section starts with `=== FILE: <original path> ===`; `photo` also leaves out its `audit/` and `tests/` folders). The script builds the zips; no manual step.

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

Instructions in the skills reach the tools through `~/.agent-workflow`. Many files still name folders that exist only on the original Mac (`/Users/GaryT/...`, or `~/Documents/Work/lab/...`). They are records of how each skill was built, not instructions: every `EVOLUTION.md`, `DISTILL-REPORT.md`, `CLAIM-FIX-REPORT.md` and `TOOLS-REPORT.md`, the `audit/` folders, `skills/frontend/references/sources.md` and `tools/render-kit/SPEC.md`. Reference text with a Mac path: `skills/project/references/run/goal-file.md` and `lane-plan.md` (the `subagent` server's source, `~/Documents/Work/tools/mcp/subagent-mcp`) and `skills/photo/TOOLS.md` (this Mac's Python interpreter; any Python 3 with NumPy and Pillow works). To list them all: `grep -rIl '/Users/GaryT' .`
