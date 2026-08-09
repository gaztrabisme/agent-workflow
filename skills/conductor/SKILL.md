---
name: conductor
description: "Turn a raw intent into a finished product by composing the skills that already exist — classify the work, route it, fan out research and persona threads, converge them, write the artifacts. USE WHEN a request is substantive and multi-step and nobody has said which skill to use: a feature list to build, a business idea to pressure-test, a document that must survive scrutiny, an engagement spanning research → decision → build. Fires FIRST on unrouted intent and delegates — it never does the work itself. Not `dev` / `solution-architect` / `delivery` / `harness-operator`: those are what it invokes; go direct when you already know which one you want. Keywords: orchestrate, route, workflow, fan out, task force, persona, red team, converge, end to end, just do it, run this, build me, pressure test, swarm, multi-agent, driver, intent to product."
license: MIT
---

# Conductor

The entry point. It takes an unrouted intent — *"build these features"*, *"pressure-test this deal"*, *"is this plan sound"* — and turns it into a **finished product** by composing the constellation: `dev`, `solution-architect`, `delivery`, `business-intelligence`, `ms-ai-discovery`, `harness-operator`, and the execution-layer skills.

> Inherits the `core` kernel — `../core/SKILL.md`. Obey its Integrity Constraints; declare its gates; reference its files, never copy them.

**Conductor does not do the work.** It classifies, composes, declares, dispatches, converges, and closes. Every unit of judgment belongs to a sibling skill or a subagent briefed by one. The moment conductor starts *reasoning about the domain instead of the routing*, it has failed — hand that reasoning to the skill that owns it.

```
intent ──▶ [ CLASSIFY ] ──▶ [ GROUND ] ──▶ [ COMPOSE ] ──▶ ⟨ PLAN BLOCK ⟩ ──▶ [ RUN ] ──▶ [ CONVERGE ] ──▶ product
                                                            the only stop      to completion
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

Record one line: `Grounded: <files read> → <what constrains this plan>`. See `../core/references/grounding-gate.md`.

### 3. Compose — build the workflow

Pick the engine per unit of work. **Declare which and why in one line** — this is `dev`'s Pattern Gate, elevated.

| Engine | When |
|---|---|
| **inline** | ≤2 units, mechanical or unambiguous. The default that must be *chosen*, not fallen into. |
| **Agent fan-out** | 3–8 independent units you want to watch live; personas; research streams. Single message, parallel calls. |
| **Workflow script** | >8 units, or genuinely multi-stage (streams → adversarial verify → synthesis). Deterministic, schema-validated, resumable, pipelines without barriers. |
| **harness-operator** | Build work on a board project. Tickets, worktrees, mutation gate — and align/land stay human keystones. |

> **Workflow opt-in:** the Workflow tool requires explicit user opt-in, and *"the user invoked a skill whose instructions tell you to call Workflow"* is one of the valid forms. **This skill is that instruction** — when composition selects the Workflow engine, calling it is authorized. Say so in the Plan Block so the choice is visible.

Then decide **convergence** before dispatch, not after: where threads land, who reconciles them, what the artifact is. See `references/convergence.md`. A fan-out without a declared meeting point produces six files nobody merges.

### 4. Declare — the Plan Block

One block. Scannable. It is the checkpoint.

```
INTENT      <restated in one line — if this is wrong, stop here>
SHAPE       <shapes present, in order>
GROUNDED    <files read → what constrains this>
ROUTE       <skills invoked, in order, with the mode>
FAN-OUT     <engine> · <N agents> · <what each covers>
PERSONAS    <who> — <what each is asked to break>
CONVERGE    <meeting point> → <artifacts on disk>
DECIDE NOW  <every fork the run would otherwise return for, each with a recommendation>
NOT DOING   <explicit out-of-scope>
COST        <agent count · rough wall-clock>
```

`DECIDE NOW` is the load-bearing row. If it is empty on non-trivial work, you have not thought hard enough about where the run will fork — go back and find them. Defaults are stated as recommendations so the answer can be *"go"*.

### 5. Run — to completion

Dispatch. Maintain a **run ledger** (in-session, then into `wiki/log.md`): each unit, its verdict, and every fork you decided forward with the one-line reason. Report at real milestones — a wave completing, a thread contradicting another — not per edit.

The sibling skill's gates are **not** yours to waive. If `dev` says adversarial review fires on this trigger, it fires. If `harness-operator` says land is human, it comes back — that is a keystone, not a mid-run stop, and it was announced in the Plan Block.

### 6. Converge — the meeting point

The step that makes fan-out worth doing. Threads reconcile, contradictions surface **explicitly** (never silently resolved by the synthesizer), and the result becomes one artifact set with a *what moved* summary. Full protocol: `references/convergence.md`.

### 7. Close — output contract

Not done until: artifacts on disk · `wiki/log.md` entry with the run ledger · `wiki/decisions.md` updated with choices **and** rejected options · `active-work.md` reconciles every unit (done / deferred / blocked) · open forks named. Per `../core/references/wiki-protocol.md`.

**Report the product, not the process.** Close with what exists now, what moved, what is still open — and every fork you decided forward, so a decision made without you is still a decision you can see and reverse.

## Anti-patterns (hard no-list)

- **Doing the work.** Conductor reasoning about the domain instead of routing to the skill that owns it.
- **Empty `DECIDE NOW`** on substantive work — guarantees the mid-run stop this skill exists to prevent.
- **Mid-run "should I continue?"** — that is not a fork, it is a lack of nerve. Decide forward.
- **Context-free escalation** — *"I hit a problem, what do you want?"* An escalation that isn't self-contained is a failure of this skill.
- **Fan-out with no declared meeting point** — N files, no synthesis, no reconciled contradiction.
- **Skipping ground** — planning against the prompt instead of against the wiki; re-deciding what `decisions.md` already locked.
- **Waiving a sibling's gate** to hit the plan. The plan bends; the gate doesn't.
- **Ceremony on a small ask.** A one-file fix does not get a Plan Block. Wu Wei — see `core` spine #9.

## Composition

- **Invokes:** `dev` (build/design/sprint/assess/train) · `solution-architect` (client-facing architecture, proposals) · `delivery` (signed engagements) · `business-intelligence` (client/market intel) · `ms-ai-discovery` (MS workshop scoping) · `harness-operator` (board-driven build) · `evolution` (meta: evolve the skills from their traces) · `skill-builder` (meta: author/shape a skill) · execution-layer (`omlx`, `media-gen`, `zalo-platform`, `gsheets`, doc skills).
- **Inherits:** `core` — integrity constraints, gate-by-artifact, wiki protocol, grounding gate, pushback-and-teach, the evolution loop.
- **Defers to:** any sibling invoked directly by name. If the user says `/dev`, conductor stays out of the way.
- **Owns, because nothing else did:** the routing decision, the task-force protocol, persona fan-out, and the convergence contract.

## References

- `references/routing-table.md` — intent → skill/mode, the disambiguation rules that resolve trigger collisions, and the compose-order for multi-shape requests.
- `references/task-force-protocol.md` — fan-out that finds **facts**: N streams + M adversarial verifiers → VERIFY → synthesis. Codified from two runs that worked.
- `references/design-cell.md` — fan-out that produces **decisions**: N roles author under exclusive mandates, reconcile on interface contracts, converge to one coherent spec. Carries the user-narrative brief and its grounding tiers.
- `references/persona-fanout.md` — fan-out that collects **reactions**: stakeholders react cold to a finished artifact → ranked objection register. Why a persona is not a research agent.
- `references/convergence.md` — the meeting point: contradiction handling, the interaction pass, and what lands in the wiki.
