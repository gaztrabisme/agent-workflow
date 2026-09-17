# Workflow Patterns

Written for the coordinator composing a run: what "dynamic workflow" means here, independent of any harness, and how each harness binds the abstract. Per-harness facts (paths, caps, what stays MISSING) live in `harness-map.md`; read the row for the harness this run is in before selecting an engine.

## The abstract

A dynamic workflow takes the units of work from the lane plan and hands each to a lane or subagent, then moves results between stages.

- **Units to lanes.** Every unit already has a lane, a brief, and an acceptance command (`lane-plan.md`). The workflow is the schedule that connects them: which units start immediately, which wait on which.
- **Pipeline.** Each item flows through the stages with no barrier: a unit's research output goes to verify as soon as it exists, and to synthesis as soon as it passes. Pipelining is the default because it removes the idle wait between stages.
- **Barrier.** Insert one only when a stage genuinely needs every prior result: convergence (all threads must be present to reconcile), a cost total, a verdict that must see all findings. A barrier on a stage that could have streamed is idle time billed to the run.
- **Verify layer.** A stage whose brief instructs it to refute, not confirm (the task-force rule: `task-force-protocol.md`). Size it to the stakes: load-bearing claims get a verifier each; the tail gets sampling. Also size it to the harness's documented cap, and where no cap is documented, to what you can watch (the 154-agent lesson: `lane-plan.md` — a Claude workflow reached 154 agents before the session limit killed it with 7 agents done).
- **Converge.** The meeting point where the stages end and the threads reconcile into one artifact set: `convergence.md`. Declare it before dispatch, never after.
- **Resume.** Where the harness offers a run id or a re-runnable workflow list, plan on resuming a failed or interrupted run from its last completed stage instead of re-running completed work. Claude Code re-runs workflows from `/workflows`; Grok resumes sessions with `-r/--resume` and `-c/--continue` (`harness-map.md`). Where the harness offers nothing, the run ledger is the resume state: every completed unit with its verdict is a stage that does not run twice.
- **Caps and cost.** The only documented workflow concurrency cap in the research is Claude Code's `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` (1–256); Gemini CLI documents a per-subagent `maxTurns`. The rest: MISSING. An unknown cap is a cost risk, so a fan-out sized past the known caps needs a stated reason in the Plan Block's COST row.

## The coordinator is the pipeline

Only Claude Code documents a scripted multi-stage pipeline (the Workflow tool). Everywhere else the coordinator IS the pipeline: dispatch, await, acceptance, next stage, in its own turn, holding the run ledger as the pipeline state. Say so in the Plan Block's FAN-OUT row ("dynamic workflow · coordinator-pipelined · N stages") so the choice is visible, and keep each stage's dispatch, acceptance, and ledger write in separate turns so a failed stage is visible before the next one fires.

## Binding per harness

| Harness | Dynamic-workflow binding |
|---|---|
| Claude Code | The Workflow tool: a JavaScript script Claude writes that orchestrates many subagents; opt in by the word "ultracode" or "dynamic workflow" in the prompt or the config toggle; saved scripts in `.claude/workflows/` (project) or `~/.claude/workflows/` (personal), re-runnable from `/workflows`; concurrency cap 1–256 via `CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS` [map S6, S10]. For 3–8 independent units worth watching live, use the Agent tool fan-out instead: billed to the session, so kept small (`lane-plan.md`). |
| Codex CLI | `features.multi_agent` (default on) with custom role declarations, plus `codex exec` invoked in bash from the coordinator as the dispatch mechanism [map S14, S16, S17]. No documented pipeline: coordinator-pipelined. |
| Gemini CLI | Each subagent is exposed to the main agent as a tool of the same name; delegate by naming the tool or force it with `@<subagent>` at prompt start; per-subagent `maxTurns` under `agents.overrides` [map S22]. No documented pipeline: coordinator-pipelined. |
| opencode | Primary agents and subagents; subagents invoked by the primary agent or manually by `@` mention; the built-in general subagent runs multiple units of work in parallel [map S30]. No documented pipeline: coordinator-pipelined. |
| Copilot CLI | Custom agents configured under `.copilot/agents/`, invoked through the "Invoke custom agents" flow [map S41]. Spawn tool and caps MISSING: coordinator-pipelined, sized conservatively. |
| Grok Build | Subagents are child sessions with their own context that return a summary; add or override them under `.grok/agents/` or `~/.grok/agents/`, manage with `/config-agents` [map S47]. No documented pipeline: coordinator-pipelined. |

The map citation [map S#] resolves in `harness-map.md`'s Sources section, all fetched 2026-09-16.
