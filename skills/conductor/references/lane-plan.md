# Lane Plan

The part of the Plan Block that says who does each unit and how we will know they did. Every unit of work is planned onto a **lane** before any agent fires: the lane, the brief, the acceptance command the coordinator will run, and the cost consequence. Fan out without one and the work lands back in the coordinator's hands by accident.

Per unit of work, one row:

| Unit | Lane | Brief (Target · Change · Acceptance) | Acceptance command | Cost consequence |
|---|---|---|---|---|

- **Brief** — three sections, always the same three: **Target** (what exists, what is wrong with it), **Change** (what the unit must produce), **Acceptance** (a command that proves the work is done). Every brief ends with: *"write the report before running out of steps even if the verdict is FAIL."*
  - **Target names the anchors.** Where other files cite the numbering of what the unit touches (a spine item, a section number), Target names each anchor at its current number.
  - **Numbered structure carries a sweep.** A unit that edits numbered structure includes the sweep `grep -rn "spine #\|SKILL.md §"` across the constellation and the repointing it finds, and its Acceptance command proves the repointing.
  - **Change names its upstream.** Where upstream content exists, Change points at it — "exactly as given in <file> §<n> row <m>" — rather than containing the content. A brief that authors new deliverable content is coordinator work by another name.
- **Acceptance** — the coordinator runs this command itself against the unit's output. A lane grading its own homework is not a gate, and the coordinator never does the unit work.
- **Cost consequence** — roughly what the unit costs on this lane, and what the run loses if the lane dies mid-unit.

## The lanes on this machine

### Codex — code and adversarial review

`codex exec` in a bash call. Models: `gpt-5.3-codex-spark`, `gpt-6-astra`, `gpt-5.6-luna`. For critical-path multi-file code, long build-and-fix loops, adversarial review.

- The brief goes on stdin with a trailing `-` as the positional prompt.
- `--skip-git-repo-check` when the working directory is not a git repo.
- `-c 'sandbox_workspace_write.network_access=true'` when the unit must fetch anything.
- Bound every run with `perl -e 'alarm shift; exec @ARGV' N codex exec …` — macOS has no `timeout`.
- Always run in the background with an events log.
- Quotas turned out to be per account, not per model: on 2026-09-15 all three models returned the same credit limit. Model-hopping inside the lane does not find a fresh wallet.

### DeepSeek harness — analysis with a verdict

MCP tools `dsh_delegate` → `dsh_await` (wait_seconds ≥ 1800) → `dsh_continue` → `dsh_cancel`. Model `deepseek-v4-pro`, high effort, 120 steps, 4 agents, 5400 s run timeout. Peer strength. For measurement, analysis, research that must end in a verdict.

- The `verification` command must not contain `cd` — use paths relative to the workspace root, or absolute paths.
- Standing rules go in `instructions`, not in the task text.
- Two children never share a workspace.
- `dsh_cancel` ends a session permanently; it is not a pause button.
- On 2026-09-15 it returned "Insufficient Balance".

### GLM — mechanical leaves

MCP tools `glm_delegate` → `glm_await` → `glm_continue` → `glm_cancel`. Model `glm-5.3-flash`. For mechanical leaves: one file, a clear port, a report from already-gathered data, a git commit. Same `verification` and workspace rules as DeepSeek.

### Claude Agent tool / Workflow tool — small and watchable only

Same model as the coordinator, billed to the coordinator's session: a Claude fan-out spends the session's own budget. Measured on 2026-09-15: a Workflow fan-out of 12 graders plus 2 verifiers per finding reached 154 agents and 1.8 M tokens before the session limit killed the run with 7 agents done. Rule: Claude fan-outs only for small, watchable sets (≤ 8 agents), or when no other lane can do the job; never for verifier layers at scale.

## Lane selection

| Unit shape | Lane | Why |
|---|---|---|
| Critical-path multi-file code, build-and-fix loop, adversarial code review | Codex | strongest at sustained code work; background + alarm keeps it bounded |
| Measurement, analysis, research that must end in a verdict | DeepSeek | peer strength; its verdicts feed convergence |
| One file, a clear port, a report from gathered data, a git commit | GLM | mechanical leaves; cheap and sufficient |
| Personas, graders, anything ≤ 8 agents worth watching live | Claude Agent tool | watchable in-session; billed to the session, so kept small |
| > 8 mechanical units | GLM / Codex, batched | a Claude Workflow at that scale burns the session (the 154-agent run) |
| Verifier layer over many findings | DeepSeek or Codex | never Claude at scale |

**Dead lanes are struck at run start.** A lane recorded closed that day comes off this table before composing; the closure notes in the lane sections above stay as history. The table carries a status line saying which lanes were open when last checked — 2026-09-15: DeepSeek closed ("Insufficient Balance"); Codex closed (quota turned out to be per account, all three models at the same limit); GLM and the Claude Agent tool — no closure recorded.

## Quota fallback

Plan around the refusals already known: at Compose, a unit whose primary lane is recorded closed that day is planned with a **primary and a fallback lane** in its row, so the reroute is decided before any agent fires.

Lanes refuse: a quota runs out, a balance hits zero, a model is down. In order:

1. Try the **next model in the same lane** — knowing the quota may be per account and shared across them.
2. Try the **next lane** that fits the unit shape.
3. **Record the refusal and the reroute in the run ledger**: which lane refused, with what error, where the unit went.
4. When every lane is closed, **stop and report**. The coordinator picking up the unit itself is the failure this skill exists to prevent; a closed lane is a blocked unit, and blocked is a reportable state.
