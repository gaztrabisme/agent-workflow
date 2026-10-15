# Lane Plan

The part of the Plan Block that says who does each unit and how we will know they did. Every unit of work is planned onto a **lane** before any agent fires: the lane, the brief, the acceptance command the coordinator will run, and the cost consequence. Fan out without one and the work lands back in the coordinator's hands by accident. [book:head-first-pmp], Inside the work package.

Per unit of work, one row:

| Unit | Lane | Brief (Load · Target · Change · Acceptance) | Acceptance command | Cost consequence |
|---|---|---|---|---|

- **Brief** — four sections, always the same four: **Load** (what the agent reads before working), **Target** (what exists, what is wrong with it), **Change** (what the unit must produce), **Acceptance** (a command that proves the work is done). Every brief ends with: *"write the report before running out of steps even if the verdict is FAIL."*
  - **Load takes one of three forms**, copied from the unit's row in the skill-and-book map ([lifecycle.md](../lifecycle.md#planning-flow)): *References* (the routed skill's reference files, and book chapters a second agent has verified, each with the practice to apply); *None found* (the knowledge-base searches that were run and returned nothing, listed so the claim can be checked); *Not applicable* (a reason, for mechanical work). An agent cannot see skills or the knowledge base unless the brief names them. The agent's report states, for each Load item, whether it was used, not used or disagreed with, and what it changed; a report without that is not accepted. (derived: adapt-os 2026-10-15 — about 25 briefs named no skill or book; a later review backed by the knowledge base found 33 defects in the built code, 11 of them high.)
  - When a unit is tasked with resolving an open grounding gap, state that gap as a specific question in the brief's Target or Change section. This carries the grounding question to the lane that can settle it.
  - **Every brief names its paths and forbids searching outside them.** The brief names the paths the child may read and write, and forbids listing or searching outside them — no `find`, `grep`, `ls` or `mdfind` on the home folder or `/`. A search of the home folder crosses the owner's cloud drives and triggers macOS privacy prompts.
  - **Target names the anchors.** Where other files cite the numbering of what the unit touches (a spine item, a section number), Target names each anchor at its current number.
  - **Numbered structure carries a sweep.** A unit that edits numbered structure includes the sweep `grep -rn "spine #\|SKILL.md §"` across the constellation and the repointing it finds, and its Acceptance command proves the repointing. [book:swebok], 7.4. Requirements Tracing.
  - **Change names its upstream.** Where upstream content exists, Change points at it — "exactly as given in <file> §<n> row <m>" — rather than containing the content. A brief that authors new deliverable content is coordinator work by another name. [book:software-engineering-at-google], Establishing Canonical Sources of Information; [book:facilitating-software-architecture], Step 3: Make Options and Gather Their Consequences.
  - **Output sample.** Acceptance includes a sample of the real output (for example headings, chunk text, rendered rows) that the unit writes into its report and the coordinator reads before recording PASS; an exit code alone is not a pass (KB v9 run, 2026-09-30).
  - **Wiki untouched.** When a brief forbids editing wiki/ (or any path), the acceptance script compares that path's `git status --porcelain` with a baseline recorded before dispatch (KB v9 run, 2026-09-30). [book:continuous-delivery], Compliance and Auditing.
  - **Facts checked on the machine.** Every fact about the environment that a brief states (a host, alias, port, path, service or version) is checked on the machine by the coordinator before dispatch, not recalled (KB v9 run, 2026-09-30).
- **Acceptance** — the coordinator runs this command itself against the unit's output. A lane grading its own homework is not a gate, and the coordinator never does the unit work.
- **Cost consequence** — roughly what the unit costs on this lane, and what the run loses if the lane dies mid-unit.

## Run ledger row template

Use this six-column row shape for the run ledger. Record one row per unit result; add a row for any run-level fork, contradiction, refusal, or reroute not already represented by a unit row. Use `—` when a field does not apply, and link to the fuller convergence or decision record when the explanation needs more room. (derived: dogfood 2026-10-01)

| Run ID | Unit / fork / thread ID | Lane | Status / verdict | Acceptance command, outcome, and output sample | Forward decision, contradiction, refusal, or reroute (reason and destination) |
|---|---|---|---|---|---|
| `<run>` | `<stable ID>` | `<lane or —>` | `<state and verdict>` | `<command + result + sample path, or —>` | `<decision/refusal and why, or —>` |

## Lane check — before composing, every run

Any lane can be down on a given day: a spent quota, an empty balance, a revoked key, a local server that is off. A lane plan written from memory routes units onto dead lanes, and the run then stops mid-flight for a reroute that could have been decided at T0. So **final lane assignments are checked on the system before the lane plan is finalized**, never assumed from a past run or from this file.

1. Run `set -a; . ~/.config/agent-capabilities/subagent.env; set +a; subagent doctor --prompt --json`. The key file has to be loaded first: the `subagent` MCP server loads it itself, but a plain shell does not. Without it, the check reports the keyed lanes (glm, deepseek, omlx) as unavailable when they are fine (found 2026-09-29). For each provider it checks the driver's binary, the API-key variables, the health gate for local servers, and with `--prompt` one cheap real turn. A provider is **open** only when its row passes, including the prompt turn. A binary and a key prove nothing about quota.
2. Read the lane memory at `~/.subagent-mcp/sessions/lane_state.json`. A lane closed there with an unexpired `closed_until` is closed, even if the doctor turn passed.
3. Compose only on open lanes. A unit whose preferred lane is closed goes to the next open lane of the right shape (the Lane selection table below). When no open lane fits a unit, that is a `DECIDE NOW` item, not a run-time surprise. Assess the cause and choose a response before dispatch. [book:head-first-pmp], How do you respond to a risk?
4. Record the result in the Plan Block's `LANES` row: each provider, open or closed, with the doctor's reason for each closure. The Plan Block is where the owner sees it.

## Provisional LANES before approval

When the Plan Block must be prepared before a same-turn check is available, it may show a **provisional** LANES row from the latest recorded check. Include that check's date/time and source, and state that it must be rerun before the lane plan is finalized or any unit is dispatched. Mark the attached lane table provisional too. Provisional status is a planning aid, not proof that a lane is open or permission to dispatch.

After approval and before dispatch, run the full lane check, update the Plan Block and lane table to the observed state, then assign units only to currently open lanes. If the check changes the available lanes, revise the assignments and acceptance plan before dispatch. If no open lane fits a unit, surface it in `DECIDE NOW`. (derived: dogfood 2026-10-01)

## Data handling before dispatch

Before sending a unit to a lane, confirm that the lane and model are authorized for the material, then provide only the data needed for that unit. If access or handling is uncertain, keep the material with the coordinator while the accountable owner resolves it. [book:llm-security-playbook], Zero Trust Decoded.

The Claude Agent and Workflow tools need no check, because they run on the coordinator's own session. Their limit is the session budget, below.

## The lanes on this machine

All external lanes go through the `subagent` MCP server (`mcp__subagent__*`; source `~/Documents/Work/tools/mcp/subagent-mcp`). `delegate` takes `provider=` one of the providers below.

| `provider=` | Model | Use for |
|---|---|---|
| `codex` (the default) | `gpt-6.1-sol`, effort `xhigh` (owner, 2026-10-07; needs Codex CLI 0.160+) | Critical-path multi-file code, long build-and-fix loops, adversarial code review |
| `deepseek` | `deepseek-v4-pro` | Measurement, analysis, research that must end in a verdict. Peer strength |
| `glm` | `glm-5.3-flash` | Mechanical leaves: one file, a clear port, a report from already-gathered data, a git commit |
| `gemini` | `gemini-3.8-flash-high`, effort `high` (Antigravity CLI `agy`) | **Disabled** (owner, 2026-10-07): it looped twice in one run. Its provider block is commented out in `~/.config/subagent/config.toml`; second reviews go to a fresh Codex session |
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

**Codex directly, when the MCP server is down.** Use `codex exec -m gpt-6.1-sol -c model_reasoning_effort=xhigh`. Do not switch among Codex models to look for quota when the quota is per account. The other installed models (`gpt-6-luna`, `gpt-5.3-codex-spark`, `gpt-6-astra`, `gpt-5.6-luna`) are not used unless the owner asks. Codex CLI 0.156 refuses `gpt-6.1-sol` ("not supported when using Codex with a ChatGPT account"); `codex update` fixes it.
- Pass `-s workspace-write -C <dir>`. `~/.codex/config.toml` sets no sandbox mode, so without the flag the run is read-only and every edit fails. Add `--add-dir` for any other folder it must write, such as `/tmp` for verify scripts.
- The brief goes on stdin, with a trailing `-` as the positional prompt, or it hangs.
- Add `--skip-git-repo-check` outside a git repository.
- Add `-c 'sandbox_workspace_write.network_access=true'` when the unit must fetch anything.
- `codex exec resume <id>` takes neither `-C` nor the session's model: it runs in the process's current directory (start it from the unit's worktree, or the session's writable root becomes wherever you are) and on `~/.codex/config.toml`'s default model unless you pass `-m gpt-6.1-sol` again (2026-10-07: six resumed rounds ran on `gpt-6-sol`, one failed on an unsupported default).
- Bound every run with `perl -e 'alarm shift; exec @ARGV' N`, because macOS has no `timeout`.
- Never share one `CARGO_TARGET_DIR` across worktrees on different code: Cargo reuses path-crate artifacts across them, so a unit can compile or pass against another branch (2026-10-08: S17 failed to compile in the shared folder; earlier passes were unprovable). Each unit builds in its own folder, cleaned after acceptance; a release is built from scratch on the merged tree. Run `disk-guard check` before builds.
- Run it in the background with an events log.
- The sandbox keeps `.git` read-only, so a direct Codex unit cannot commit, and it cannot bind sockets, so a test suite that opens loopback or Unix sockets fails inside it. The coordinator reruns such suites outside the sandbox, and the commit goes to another lane (2026-09-30).
- The session scratchpad under `/private/tmp/claude-*` is not visible inside the sandbox, even with `--add-dir /tmp`. Put acceptance scripts inside the workspace (2026-09-30).

**The `subagent` server refuses its own repo** (`~/Documents/Work/tools/mcp/subagent-mcp`) as a `delegate` workspace; the call fails with a bare "Error executing tool delegate" (2026-09-30). Work in that repo goes through direct `codex exec`, and its commits through a Claude Agent.

**Codex multi-edit units through the MCP server.** Until 2026-09-30 the server's loop detector killed Codex units that edited one file 8 times, because Codex reports edits without their content. subagent-mcp commit `6ae599a` gives each Codex edit its own signature. It takes effect when the `subagent` server next starts; until then, send such units through direct `codex exec`.

**Codex quota.** Check the lane state before dispatch. When the quota is per account, switching Codex models does not find a fresh quota; do not model-hop to seek one. The lane check records the observed status for the day.

### `epi` (efficient-pi serve mode): work in progress, fix what you find

`epi` is the owner's own agent harness (`~/Documents/Work/tools/efficient-pi`, branch `core`, Rust workspace `core/`; installed as `~/.local/bin/epi`). It is not a `subagent` MCP provider: drive it directly with `epi call list|delegate|await|continue|transcript`, as the subagent-mcp v2 contract describes. A new project needs a board (`epi show`), `wiki/index.md`, `wiki/active-work.md`, `wiki/log.md`, and `epi prefix schema accept <hash>` before serve accepts work.

**It is still work in progress (owner, 2026-10-07).** Expect defects. Any session that uses it and finds a problem fixes it and commits the fix along the way, without asking first, in that repo under its own `AGENTS.md` rules:
- Check `git worktree list` and `wiki/active-work.md` there first. If another session has a fix in flight on the same files, message that session (ListAgents, SendMessage) instead of editing.
- Fix on a branch or worktree, add a test that fails before the fix, pass `cargo test --workspace` and `cargo clippy --workspace --all-targets -- -D warnings` outside the Codex sandbox, then commit with explicit paths and `git commit -F`.
- Record the defect and the fix in that repo's `wiki/log.md`. Reinstall `epi` only with the release installer (`core/release/install.sh`, which keeps the previous version for `--rollback`).
- Never push; publishing stays with the owner.

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
