# Workflow Patterns

Written for the coordinator composing a run: what a dynamic workflow means independent of any harness, and how to bind the abstract to documented capabilities. Harness-specific primitives and limits live in harness-map.md; read the current row before selecting an engine.

## The abstract

A dynamic workflow takes the units in the lane plan, assigns each to a lane, and moves results between stages.

- **Units to lanes.** Every unit already has a lane, a brief, and an acceptance command in lane-plan.md. The workflow is the schedule that connects them: which units start immediately and which depend on earlier results.
- **Pipeline.** Independent work can run in parallel; later stages can begin as soon as their required inputs are ready. Deployment and test stages can be sequential, parallel, or optional depending on their dependency. [book:continuous-delivery], Subsequent Test Stages.
- **Barrier.** Wait for all results only when the next stage needs them together, such as the final contradiction and interaction pass or a complete cost total. Gather the required parallel results before their combined outcome.
- **Verify layer.** A stage whose brief instructs it to refute, not confirm. Size it to the stakes: verify load-bearing claims individually and sample the tail. Respect documented harness caps; where no cap is documented, size the work to what can be watched and accepted. [book:site-reliability-engineering], Testing at Scale.
- **Converge.** Declare the meeting point and final artifact before dispatch; see convergence.md.
- **Resume.** Resume from the last completed stage when the harness supports it; otherwise use the run ledger as the resume state. Make each workflow step idempotent so a retry is safe. If a step has a partial or non-repeatable side effect, reconcile its actual state before retrying and guard against applying it twice. [book:site-reliability-engineering], Resolving Inconsistencies Idempotently.
- **Caps and cost.** Use only the cap documented for the current harness row. Treat an unknown cap as a cost risk; state why a fan-out beyond known capacity is justified in the Plan Block's `COST` row.

### Coordination topology

Name the topology in the Plan Block when a run has several interacting lanes: **hierarchical** when a coordinator directs dependent work, **peer-to-peer** when lanes coordinate as equals, or **hybrid** when both patterns are needed. Record the trade-off: hierarchy gives control but can bottleneck; peer coordination shares the work but needs clear interfaces. Choose from a tested pattern rather than inventing the coordination style during the run. [book:agentic-mesh], Create Fleet Factory.

### Choose the execution mode by risk

Small, low-risk requests can use a flexible agent-governed workflow. Use explicit, repeatable stages when the cost of an error exceeds the requestor's tolerance. The Plan Block names the mode and why. For work on Codex, use the documented available delegation and execution path in harness-map.md; this section stays at the decision level. [book:agentic-mesh], Executing the Task Plan.

Use task size as an engine-fit cue: inline suits up to two clear, mechanical units; on Claude Code, use the Agent tool to fan out three to eight independent units that benefit from watching, subject to the current harness cap; use the provider-lane dynamic workflow (below) for more than eight units or genuine multi-stage dependencies, and the Workflow tool only when the owner says "ultracode". These are starting points, not automatic ceremony thresholds: scale the process to the task's value, risk, independence, and the current harness cap. [book:agentic-mesh], Task Planning; [book:agentic-mesh], Parallelization; [book:agentic-mesh], Orchestration.

## The coordinator is the pipeline

Claude Code is the only harness in the current map with a documented scripted multi-stage pipeline. Everywhere else, the coordinator pipelines the run: dispatch, await, acceptance, next stage, with each stage recorded separately so a failure is visible before the next stage starts. State that choice in the Plan Block. Visibility makes the process easier to coordinate and problems easier to catch. [book:agentic-mesh], Comparing AI Workflows and Agents; [book:continuous-delivery], Chapter 1: The Problem of Delivering Software.

## Provider-lane dynamic workflow

What the owner means by "dynamic workflow": the coordinator-pipelined run above, with every unit on a `subagent` provider lane instead of a Claude agent. On Claude Code a `UserPromptSubmit` hook (`config/hooks/claude-lane-workflow-hook` in the agent-workflow repo) marks the session when the phrase appears, and a `PreToolUse` hook then denies the Workflow and Agent tools for that session; saying "ultracode" clears the mark.

1. **Plan every lane first.** Run the lane check in lane-plan.md, then put the whole run in the Plan Block before anything fires: each unit with its stage or wave, primary and fallback lane, brief, and acceptance command. `ENGINE` reads `provider-lane dynamic workflow`; `SCHEDULE` lists the waves and which results each wave needs.
2. **Dispatch a wave.** One `delegate` per unit, all units of the wave sent together, each in its own workspace; one `await` per run straight after, with `wait_seconds` ≥ 1800.
3. **Gate the wave.** Run each acceptance command and read its output sample; record the run ledger rows. A failed unit gets `continue` on the same lane or its fallback lane before the next wave that depends on it starts.
4. **Next wave, then converge.** Later waves start when their inputs pass. The merger named in `CONVERGE` is also a lane unit.

A unit no open lane accepts is blocked and reported; the coordinator does not take it and does not fall back to a Claude agent.

## Binding per harness

| Harness | Dynamic-workflow binding |
|---|---|
| Claude Code | Provider-lane dynamic workflow (above). The documented scripted Workflow tool only when the owner says "ultracode"; read harness-map.md for its caps and resume behavior. |
| Codex CLI | Coordinator-pipelined unless the current harness map documents a suitable multi-stage primitive. |
| Gemini CLI | Coordinator-pipelined unless the current harness map documents a suitable multi-stage primitive. |
| opencode | Coordinator-pipelined unless the current harness map documents a suitable multi-stage primitive. |
| Copilot CLI | Coordinator-pipelined unless the current harness map documents a suitable multi-stage primitive. |
| Grok Build | Coordinator-pipelined unless the current harness map documents a suitable multi-stage primitive. |

The harness map is the source for per-harness details; do not infer an undocumented capability from another harness.
