# Lane Plan

The part of the Plan Block that says who does each unit and how we will know they did. Every unit of work is planned onto a **lane** before any agent fires: the lane, the brief, the acceptance command the coordinator will run, and the cost consequence. Fan out without one and the work lands back in the coordinator's hands by accident. [book:head-first-pmp], Inside the work package.

Per unit of work, one row:

| Unit | Lane | Brief (Target · Change · Acceptance) | Acceptance command | Cost consequence |
|---|---|---|---|---|

- **Brief** — three sections, always the same three: **Target** (what exists, what is wrong with it), **Change** (what the unit must produce), **Acceptance** (a command that proves the work is done). Every brief ends with: *"write the report before running out of steps even if the verdict is FAIL."*
  - **Every brief names its paths and forbids searching outside them.** The brief names the paths the child may read and write, and forbids listing or searching outside them — no `find`, `grep`, `ls` or `mdfind` on the home folder or `/`. A search of the home folder crosses the owner's cloud drives and triggers macOS privacy prompts.
  - **Target names the anchors.** Where other files cite the numbering of what the unit touches (a spine item, a section number), Target names each anchor at its current number.
  - **Numbered structure carries a sweep.** A unit that edits numbered structure includes the sweep `grep -rn "spine #\|SKILL.md §"` across the constellation and the repointing it finds, and its Acceptance command proves the repointing. [book:swebok], 7.4. Requirements Tracing.
  - **Change names its upstream.** Where upstream content exists, Change points at it — "exactly as given in <file> §<n> row <m>" — rather than containing the content. A brief that authors new deliverable content is coordinator work by another name. [book:software-engineering-at-google], Establishing Canonical Sources of Information; [book:facilitating-software-architecture], Step 3: Make Options and Gather Their Consequences.
  - **Output sample.** Acceptance includes a sample of the real output (for example headings, chunk text, rendered rows) that the unit writes into its report and the coordinator reads before recording PASS; an exit code alone is not a pass (KB v9 run, 2026-09-30).
  - **Wiki untouched.** When a brief forbids editing wiki/ (or any path), the acceptance script compares that path's `git status --porcelain` with a baseline recorded before dispatch (KB v9 run, 2026-09-30). [book:continuous-delivery], Compliance and Auditing.
  - **Facts checked on the machine.** Every fact about the environment that a brief states (a host, alias, port, path, service or version) is checked on the machine by the coordinator before dispatch, not recalled (KB v9 run, 2026-09-30).
- **Acceptance** — the coordinator runs this command itself against the unit's output. A lane grading its own homework is not a gate, and the coordinator never does the unit work.
- **Cost consequence** — roughly what the unit costs on this lane, and what the run loses if the lane dies mid-unit.

## Lane check — before composing, every run

Any lane can be down on a given day: a spent quota, an empty balance, a revoked key, a local server that is off. A lane plan written from memory routes units onto dead lanes, and the run then stops mid-flight for a reroute that could have been decided at T0. So **the lanes are checked on the system before the lane plan is written**, never assumed from a past run or from this file.

1. Run `set -a; . ~/.config/agent-capabilities/subagent.env; set +a; subagent doctor --prompt --json`. The key file has to be loaded first: the `subagent` MCP server loads it itself, but a plain shell does not. Without it, the check reports the keyed lanes (glm, deepseek, omlx) as unavailable when they are fine (found 2026-09-29). For each provider it checks the driver's binary, the API-key variables, the health gate for local servers, and with `--prompt` one cheap real turn. A provider is **open** only when its row passes, including the prompt turn. A binary and a key prove nothing about quota.
2. Read the lane memory at `~/.subagent-mcp/sessions/lane_state.json`. A lane closed there with an unexpired `closed_until` is closed, even if the doctor turn passed.
3. Compose only on open lanes. A unit whose preferred lane is closed goes to the next open lane of the right shape (the Lane selection table below). When no open lane fits a unit, that is a `DECIDE NOW` item, not a run-time surprise. Assess the cause and choose a response before dispatch. [book:head-first-pmp], How do you respond to a risk?
4. Record the result in the Plan Block's `LANES` row: each provider, open or closed, with the doctor's reason for each closure. The Plan Block is where the owner sees it.

## Data handling before dispatch

Before sending a unit to a lane, confirm that the lane and model are authorized for the material, then provide only the data needed for that unit. If access or handling is uncertain, keep the material with the coordinator while the accountable owner resolves it. [book:llm-security-playbook], Zero Trust Decoded.

The Claude Agent and Workflow tools need no check, because they run on the coordinator's own session. Their limit is the session budget, below.

## The lanes on this machine

All external lanes go through the `subagent` MCP server (`mcp__subagent__*`; source `~/Documents/Work/tools/mcp/subagent-mcp`). `delegate` takes `provider=` one of the providers below.

| `provider=` | Model | Use for |
|---|---|---|
| `codex` (the default) | `gpt-6-luna`, effort `xhigh` | Critical-path multi-file code, long build-and-fix loops, adversarial code review |
| `deepseek` | `deepseek-v4-pro` | Measurement, analysis, research that must end in a verdict. Peer strength |
| `glm` | `glm-5.3-flash` | Mechanical leaves: one file, a clear port, a report from already-gathered data, a git commit |
| `gemini` | `gemini-3.8-flash-high`, effort `high` (Antigravity CLI `agy`) | Experimental. It runs without the tool-call guard, so its workspace is a worktree or scratch folder, never a tree you cannot lose |
| `bppc` | `qwen3.8-27b` on the GPU workstation | Offline or private work. Needs its server up (`start-llm`) |
| `omlx` | `Qwen3.6-35B-A3B-OptiQ-4bit-REAP-19B` on this Mac | Offline or private work. It loads onto the Mac's GPU, so check no other session holds it |

**Invocation rules, all providers:**
- Call `await` immediately after `delegate`, with `wait_seconds` ≥ 1800.
- For DeepSeek, use the documented run defaults: 120 steps, four agents, and 5,400 seconds.
- Every `delegate` carries a `verification` command. It must not contain `cd`, so use paths relative to the workspace root, or absolute paths. It must also be one simple command: the guard blocks compound lines (`&&`, pipes, `$(…)`) before they run ("blocked before execution: compound command line", 2026-09-29). Put a multi-step check in a script and pass `bash path/to/verify.sh`.
- The script in a `verification` command must be a file inside the workspace; the guard blocks a script outside it ("not a file in the workspace", 2026-09-30).
- Standing rules go in `instructions`, not in the task text, so they survive `continue`.
- Two children never share a workspace. [book:agentic-mesh], Shared Workspaces for Agents.
- `cancel` ends a session permanently. It is not a pause, so cancel early when the lane was the wrong weight, not late.
- GLM's guard refuses paths under `~/.claude` (the skills symlinks, settings). The coordinator does installs there.

**Tuning.** Model, `effort`, `max_steps`, timeouts, `max_agents`, the default provider and the fallback chain live in `~/.config/subagent/config.toml`, a copy of the subagent-mcp repo's `wiki/data/config-mcbob-2026-09-28.toml`. Keys live in the 0600 file `~/.config/agent-capabilities/subagent.env`. Both take effect when the `subagent` server next starts. Size each knob from the work. An uncapped child finds the provider's rate limit instead of the answer. Tune a lane rather than working around it.

**Codex directly, when the MCP server is down.** Use `codex exec -m gpt-6-luna -c model_reasoning_effort=xhigh`. Do not switch among Codex models to look for quota when the quota is per account. The other installed models (`gpt-5.3-codex-spark`, `gpt-6-astra`, `gpt-5.6-luna`) are not used unless the owner asks.
- Pass `-s workspace-write -C <dir>`. `~/.codex/config.toml` sets no sandbox mode, so without the flag the run is read-only and every edit fails. Add `--add-dir` for any other folder it must write, such as `/tmp` for verify scripts.
- The brief goes on stdin, with a trailing `-` as the positional prompt, or it hangs.
- Add `--skip-git-repo-check` outside a git repository.
- Add `-c 'sandbox_workspace_write.network_access=true'` when the unit must fetch anything.
- Bound every run with `perl -e 'alarm shift; exec @ARGV' N`, because macOS has no `timeout`.
- Run it in the background with an events log.
- The sandbox keeps `.git` read-only, so a direct Codex unit cannot commit, and it cannot bind sockets, so a test suite that opens loopback or Unix sockets fails inside it. The coordinator reruns such suites outside the sandbox, and the commit goes to another lane (2026-09-30).
- The session scratchpad under `/private/tmp/claude-*` is not visible inside the sandbox, even with `--add-dir /tmp`. Put acceptance scripts inside the workspace (2026-09-30).

**The `subagent` server refuses its own repo** (`~/Documents/Work/tools/mcp/subagent-mcp`) as a `delegate` workspace; the call fails with a bare "Error executing tool delegate" (2026-09-30). Work in that repo goes through direct `codex exec`, and its commits through a Claude Agent.

**Codex multi-edit units through the MCP server.** Until 2026-09-30 the server's loop detector killed Codex units that edited one file 8 times, because Codex reports edits without their content. subagent-mcp commit `6ae599a` gives each Codex edit its own signature. It takes effect when the `subagent` server next starts; until then, send such units through direct `codex exec`.

**Codex quota.** Check the lane state before dispatch. When the quota is per account, switching Codex models does not find a fresh quota; do not model-hop to seek one. The lane check records the observed status for the day.

### Claude Agent tool / Workflow tool — small and watchable only

Same model as the coordinator, billed to the coordinator's session: a Claude fan-out spends the session's own budget. Measured on 2026-09-15: a Workflow fan-out of 12 graders plus 2 verifiers per finding reached 154 agents and 1.8 M tokens before the session limit killed the run with 7 agents done. The cap counts every Claude agent a run starts, not only those alive at once: on 2026-09-28 a per-lesson audit loop ran ≤ 4 Claude agents at a time but about 140 fix jobs in total, and hit the 5-hour usage limit mid-run. Rule: Claude fan-outs only for small, watchable sets (≤ 8 agents), or when no other lane can do the job; never for verifier layers at scale.

## Lane selection

| Unit shape | Lane | Why |
|---|---|---|
| Critical-path multi-file code, build-and-fix loop, adversarial code review | Codex | strongest at sustained code work; background + alarm keeps it bounded |
| Measurement, analysis, research that must end in a verdict | DeepSeek | peer strength; its verdicts feed convergence |
| One file, a clear port, a report from gathered data, a git commit | GLM | mechanical leaves; cheap and sufficient |
| Personas, graders, anything ≤ 8 agents worth watching live | Claude Agent tool | watchable in-session; billed to the session, so kept small |
| > 8 mechanical units | GLM / Codex, batched | a Claude Workflow at that scale burns the session (the 154-agent run) |
| Verifier layer over many findings | DeepSeek or Codex | never Claude at scale |
| Per-item loops (audit and fix per lesson or claim, many rounds) | Codex / GLM; Claude only when the whole loop stays ≤ 8 agents | the loop multiplies items by rounds; count it at Compose |
| Translating long transcripts | a lane checked on one sample first | a Codex writer once condensed a unit instead of translating it (32 High findings); a length floor does not catch it |

**The table applies to open lanes only.** Before using it, strike every lane the lane check (above) found closed. This file records no lane status: status is whatever `subagent doctor` said today.

## Quota fallback

At Compose, every unit gets a **primary and a fallback lane** in its row, both taken from the open lanes, so a mid-run refusal has its reroute decided before any agent fires.

Lanes that passed the check can still refuse mid-run: a quota runs out, a balance hits zero, a model goes down. In order:

1. Try the **next model in the same lane**, knowing the quota may be shared across models.
2. Try the **next lane** that fits the unit shape.
3. **Record the refusal and the reroute in the run ledger**: which lane refused, with what error, where the unit went. [book:site-reliability-engineering], Keep a History of Outages.
4. When every lane is closed, **stop and report**. The coordinator picking up the unit itself is the failure this skill exists to prevent; a closed lane is a blocked unit, and blocked is a reportable state.
