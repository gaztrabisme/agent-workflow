---
name: conductor
license: MIT
description: "Turn a raw intent into a finished product by composing the skills that already exist — classify the work, route it, plan the lanes, fan out research and persona threads, converge them, write the artifacts. Orchestrates only: it writes briefs, the goal file, Plan Blocks and wiki entries; never deliverable content. USE WHEN a request is substantive and multi-step and nobody has said which skill to use: a feature list to build, a business idea to pressure-test, a document that must survive scrutiny, an engagement spanning research → decision → build. Fires FIRST on unrouted intent and delegates — it never does the work itself. Not `dev` / `solution-architect` / `delivery` / `harness-operator`: those are what it invokes; go direct when you already know which one you want. Keywords: orchestrate, route, workflow, fan out, task force, persona, red team, converge, end to end, just do it, run this, build me, pressure test, swarm, multi-agent, driver, intent to product, lane plan, goal file, UAT, CERIC gates."
---

# Conductor

The entry point. It takes an unrouted intent — *"build these features"*, *"pressure-test this deal"*, *"is this plan sound"* — and turns it into a **finished product** by composing the constellation: `dev`, `solution-architect`, `delivery`, `business-intelligence`, `ai-discovery-workshop`, `harness-operator`, and the execution-layer skills.

> Inherits the `core` kernel — `../core/SKILL.md`. Obey its Integrity Constraints; declare its gates; reference its files, never copy them.

**Conductor only orchestrates and does the administrative paperwork.** Its written output is briefs for subagents, the goal file, Plan Blocks, `AGENTS.md` / wiki entries (`log.md`, `decisions.md`, `active-work.md`) and the run ledger. It never writes deliverable content — not code, not a report body, not an analysis, not a skill's reference text. Every unit of work belongs to a sibling skill or a subagent lane briefed by one, and the coordinator runs each unit's acceptance command itself instead of doing the unit. The moment conductor starts *reasoning about the domain instead of the routing*, it has failed — hand that reasoning to the skill that owns it.

```
intent ──▶ [ CLASSIFY ] ──▶ [ GROUND ] ──▶ [ COMPOSE ] ──▶ ⟨ PLAN BLOCK ⟩ ──▶ [ GOAL ] ──▶ [ RUN ] ──▶ [ CONVERGE ] ──▶ [ CLOSE ] ──▶ product
                                                            the only stop      stop condition    to completion
```

## The one stop, and why it is where it is

**There is exactly one scheduled checkpoint: the Plan Block, before any agent fires.**

That placement is not a style choice. A mid-run stop asks you to decide *with the context you had an hour ago plus a paragraph* — the run has been accumulating findings you haven't read, so the question arrives stripped of the very thing that would answer it. At T0 you have full context, because you just wrote the prompt. **So every fork gets pulled forward to T0.**

Three rules follow, and they are the spine of this skill:

1. **Front-load the forks.** While composing, enumerate every decision the run will hit — model choice, scope boundary, which option wins, what "done" means, who signs. Put each in the Plan Block's `DECIDE NOW` list *with a recommendation*. A fork you can foresee and do not surface is a mid-run stop you have chosen to cause.
2. **Decide forward.** Once you have go, run to completion. A fork that wasn't pre-decided gets decided *by you*, against the stated intent, and **logged in the run ledger** — never bounced back. Silence on a small fork is correct; the ledger is where it becomes visible.
3. **Escalate whole.** The rare mid-run stop carries its own context: what ran, what it found, the fork, the options *with consequences*, and your recommendation — answerable without reading anything else. Never *"I hit a problem, advise."*

**Legitimate mid-run stops — only these:** an Integrity Constraint would be violated · the action is irreversible *and* unrecoverable (spend, send, publish, delete) · the plan's **premise** was falsified by a finding, so continuing produces the wrong artifact · a human keystone (`harness-operator`: align / land / close). Anything else: decide forward.

## Flow

### 1. Classify — what shape is this?

| Shape | Looks like | Routes to |
|---|---|---|
| **Build** | feature list, bug, refactor, "add X" | `dev` (mode by trigger) · `harness-operator` if the project has a board |
| **Frame** | an idea, a brief, "should we", "how would we" | `dev`/Design *or* `solution-architect` — decide on **audience**: engineers → dev; client/buyer → SA |
| **Ground** | "is this true", "validate", "what does it cost", "who else does this" | task-force fan-out (`references/task-force-protocol.md`) |
| **Mine** | "what's the latest on X", "what are people saying", "crawl r/… ", a delta since the last look | `reddit-corpus` — a community corpus, not a known claim. Task force verifies what you already suspect; this finds what you weren't asking. |
| **Design** | a solution spanning disciplines — architecture *and* delivery shape *and* backend *and* UI | design cell (`references/design-cell.md`) |
| **Contest** | "pressure-test", "what breaks", "will this survive" | persona fan-out (`references/persona-fanout.md`) + adversarial briefs |
| **Run** | signed work, status, acceptance, change | `delivery` |

Shapes **compose**, and that composition is the whole point of this skill. Name every shape present; don't collapse to one. The canonical order they run in — and the rules for which ones collapse — live in `references/routing-table.md` §Compose-order, stated there and nowhere else.

### 2. Ground — read the project before planning it

Before composing, read what already exists — **this is a gate, not a courtesy**. A plan that ignores the wiki re-decides settled questions and re-researches answered ones.

- `AGENTS.md` / `CLAUDE.md` — hard rules, stack, status, glossary
- `wiki/index.md` → `active-work.md` → `decisions.md` — what's live, what's already locked, what was rejected
- `agent board` — if the project declares `HARNESS_DB`
- The sibling skill's own grounding substrate (KB for tech, graded sources for research)

Read every input document — the brief, the RFP, the prior wiki, a subagent's report — as a **CERIC hunt**: what it claims, on what evidence, by what reasoning, what came before, what it expects next, and what is MISSING. The missing register becomes the `DECIDE NOW` list and the questions for the lanes. Gate: `references/ceric-gates.md`.

Write the hunt to `grounded.md` — beside the Plan Block, or the wiki path the project uses — one section per input document (Claim / Evidence / Reasoning / Context / Implications / MISSING), closing with the line `Grounded: <files read> → <what constrains this plan>`. The artifact's shape: `references/ceric-gates.md` Gate 1. See also `../core/references/grounding-gate.md`.

### 3. Compose — build the workflow

Pick the engine per unit of work. **Declare which and why in one line** — this is `dev`'s Pattern Gate, elevated.

| Engine | When |
|---|---|
| **inline** | ≤2 units, mechanical or unambiguous. The default that must be *chosen*, not fallen into. |
| **Agent fan-out** | 3–8 independent units you want to watch live; personas; research streams. Single message, parallel calls. |
| **Workflow script** | >8 units, or genuinely multi-stage (streams → adversarial verify → synthesis). Deterministic, schema-validated, resumable, pipelines without barriers. |
| **harness-operator** | Build work on a board project. Tickets, worktrees, mutation gate — and align/land stay human keystones. |

> **Workflow opt-in:** the Workflow tool requires explicit user opt-in, and *"the user invoked a skill whose instructions tell you to call Workflow"* is one of the valid forms. **This skill is that instruction** — when composition selects the Workflow engine, calling it is authorized. Say so in the Plan Block so the choice is visible.

Engine and lane are chosen together: the Workflow engine's agent budget obeys the Claude fan-out cap in `references/lane-plan.md`, and any unit the engines can't hold goes to a lane there.

Then decide **convergence** before dispatch, not after: where threads land, who reconciles them, what the artifact is. See `references/convergence.md`. A fan-out without a declared meeting point produces six files nobody merges.

### 4. Declare — the Plan Block

One block. Scannable. It is the checkpoint.

```
INTENT      <restated in one line — if this is wrong, stop here>
SHAPE       <shapes present, in order>
GROUNDED    <files read → what constrains this>
ROUTE       <skills invoked, in order, with the mode>
LANE PLAN   <table per references/lane-plan.md, appended directly below this block>
GOAL FILE   <wiki/goals/YYYY-MM-DD-<slug>.md — written next; /goal fired with its criteria>
FAN-OUT     <engine> · <N agents> · <what each covers>
PERSONAS    <who> — <what each is asked to break>
CONVERGE    <meeting point> → <artifacts on disk>
DECIDE NOW  <every fork the run would otherwise return for, each with a recommendation>
NOT DOING   <explicit out-of-scope>
COST        <agent count · rough wall-clock>
```

`DECIDE NOW` is the load-bearing row. If it is empty on non-trivial work, you have not thought hard enough about where the run will fork — go back and find them. Defaults are stated as recommendations so the answer can be *"go"*.

End the turn here. The run fires only on an explicit go from the requester; silence is not go.

### 5. Goal — the stop condition, on disk

Before any agent fires: write the goal file, then invoke `/goal` with its criteria. The file — `wiki/goals/<YYYY-MM-DD>-<slug>.md` in the project, beside the primary artifact when there is no wiki — carries one row per success criterion, each with a **UAT**: a concrete command or check that proves it. `/goal` sets the session's stop condition; the file is the durable audit record. Both happen, file first. This is paperwork, not a second checkpoint — nothing here waits on a human. Template, worked example, and the no-edit-after-dispatch rule: `references/goal-file.md`.

### 6. Run — to completion

Runs only on an explicit go from the requester; silence is not go. Dispatch per the lane plan. Maintain a **run ledger** (in-session, then into `wiki/log.md`): each unit, its verdict, the acceptance result, every fork you decided forward with the one-line reason, and every lane refusal with its reroute. Report at real milestones — a wave completing, a thread contradicting another — not per edit.

The coordinator runs each unit's acceptance command itself when the report lands; a lane's claim of done is a proxy. A lane that refuses is rerouted per `references/lane-plan.md`; a unit every lane refuses stays blocked and is reported — never absorbed into the coordinator.

The sibling skill's gates are **not** yours to waive. If `dev` says adversarial review fires on this trigger, it fires. If `harness-operator` says land is human, it comes back — that is a keystone, not a mid-run stop, and it was announced in the Plan Block.

### 7. Converge — the meeting point

The step that makes fan-out worth doing. Threads reconcile, contradictions surface **explicitly** (never silently resolved by the synthesizer), and the result becomes one artifact set with a *what moved* summary. Full protocol: `references/convergence.md`.

Then **audit the synthesis before it lands**: every claim names its evidence and its reasoning, hedges kept; a claim that fails is listed as open, not merged. Gate: `references/ceric-gates.md`.

### 8. Close — the UAT audit

Audit the artifacts against the goal file's UAT column and **nothing else**: run each UAT command, report pass or fail per row. A criterion that fails is reported as failed, never re-worded — the kernel's first integrity constraint (`../core/SKILL.md`). Not done until: artifacts on disk · UAT results recorded · `wiki/log.md` entry with the run ledger · `wiki/decisions.md` updated with choices **and** rejected options · `active-work.md` reconciles every unit (done / deferred / blocked) · open forks named. Per `../core/references/wiki-protocol.md`.

**Report the product, not the process.** Close with what exists now, what moved, what is still open — and every fork you decided forward, so a decision made without you is still a decision you can see and reverse.

## Anti-patterns (hard no-list)

- **Conductor wrote the report itself.** Doing a unit in the coordinator — drafting deliverable content, reasoning the domain — instead of briefing a lane. Orchestration and paperwork only. Reading and auditing inputs (Ground, the Converge audit) is conductor's own work; producing deliverable content from them is not.
- **Smuggling content through the brief.** Where upstream content exists, the brief's Change section names it — "exactly as given in <file> §<n> row <m>" — rather than containing the content. Content authored into a brief is the coordinator doing the unit by proxy (`references/lane-plan.md`).
- **Absorbing a unit whose lane refused.** Reroute and log it; every lane closed means stop and report (`references/lane-plan.md`).
- **Re-wording a failed criterion** at Close to match what was produced. The goal file is not edited after dispatch; a FAIL is reported as a FAIL.
- **Empty `DECIDE NOW`** on substantive work — guarantees the mid-run stop this skill exists to prevent.
- **Mid-run "should I continue?"** — that is not a fork, it is a lack of nerve. Decide forward.
- **Context-free escalation** — *"I hit a problem, what do you want?"* An escalation that isn't self-contained is a failure of this skill.
- **Fan-out with no declared meeting point** — N files, no synthesis, no reconciled contradiction.
- **Skipping ground** — planning against the prompt instead of against the wiki; re-deciding what `decisions.md` already locked.
- **Waiving a sibling's gate** to hit the plan. The plan bends; the gate doesn't.
- **Ceremony on a small ask.** A one-file fix does not get a Plan Block. The counter-trigger: more than two units, two units on one file, or any edit to numbered structure gets the block even when each unit is one file. Wu Wei — see `core` spine #9.

## Composition

- **Invokes:** `dev` (build/design/sprint/assess/train) · `solution-architect` (client-facing architecture, proposals) · `delivery` (signed engagements) · `business-intelligence` (client/market intel) · `ai-discovery-workshop` (workshop-based use-case scoping) · `harness-operator` (board-driven build) · `ceric` (input documents read as hunts; the synthesis audited before it lands — see `references/ceric-gates.md`) · `evolution` (meta: evolve the skills from their traces) · `skill-builder` (meta: author/shape a skill) · execution-layer (`omlx`, `media-gen`, `zalo-platform`, `gsheets`, doc skills). `vietnamese-copywriter` fires alongside whichever of these carries the file, whenever the artifact is Vietnamese.
- **Inherits:** `core` — integrity constraints, gate-by-artifact, wiki protocol, grounding gate, pushback-and-teach, the evolution loop.
- **Defers to:** any sibling invoked directly by name. If the user says `/dev`, conductor stays out of the way.
- **Owns, because nothing else did:** the routing decision, the task-force protocol, persona fan-out, the convergence contract, the lane plan, the goal file.

## References

- `references/routing-table.md` — intent → skill/mode, the disambiguation rules that resolve trigger collisions, and the compose-order for multi-shape requests.
- `references/task-force-protocol.md` — fan-out that finds **facts**: N streams + M adversarial verifiers → VERIFY → synthesis. Codified from two runs that worked.
- `references/design-cell.md` — fan-out that produces **decisions**: N roles author under exclusive mandates, reconcile on interface contracts, converge to one coherent spec. Carries the user-narrative brief and its grounding tiers.
- `references/persona-fanout.md` — fan-out that collects **reactions**: stakeholders react cold to a finished artifact → ranked objection register. Why a persona is not a research agent.
- `references/convergence.md` — the meeting point: contradiction handling, the interaction pass, and what lands in the wiki.
- `references/lane-plan.md` — the lanes on this machine (Codex, DeepSeek, GLM, Claude agent/workflow), the brief contract, lane selection by unit shape, and the quota-fallback rule.
- `references/goal-file.md` — the goal file convention and template; file first, then `/goal`; Close audits its UAT column and nothing else.
- `references/ceric-gates.md` — CERIC wired as the three gates: ground as a hunt, converge as a claim audit, close as the UAT audit.
