---
name: conductor
license: MIT
description: "Coordinates an unrouted substantive multi-step task into a Plan Block, lane briefs, run ledger, and convergence record for its accountable lead. USE WHEN a request needs coordinated stages and no domain skill already owns it. Disambiguation: use the owning implementation skill for code, the presales architect for a client proposal, and delivery for signed work; conductor coordinates across them. Keywords: orchestrate, multi-step task, Plan Block, lane plan, fan-out, task force, persona review, convergence, run ledger, UAT."
---

# Conductor

Conductor gives the accountable lead a coordinated plan and a durable record of the run: a Plan Block, lane briefs, run ledger, and convergence record. It owns routing, coordination, and administrative artifacts. Domain work belongs to the relevant skill or to a briefed lane; conductor does not write the deliverable or reason through its domain. [book:facilitating-software-architecture], If You Have Experience, Facilitate Decisions Rather than Deciding Yourself.

> Inherits the `core` kernel — see `../core/SKILL.md`. Obey its Integrity Constraints; declare its gates; reference its files, never copy them.

## When it fires — and when a sibling owns it

- **Conductor:** a substantive multi-step request is still unrouted and needs coordinated stages.
- **The owning skill:** the user names a skill directly, or one skill already owns the requested artifact and audience. Conductor stays out of the way.
- **Disambiguation:** decide on artifact and audience. Conductor coordinates across stages; implementation, presales architecture, and signed-engagement delivery stay with their respective owners.

## Principles / anchoring rules

1. **Coordinate; do not take the unit.** Every unit belongs to a routed skill or a lane with a brief. The coordinator runs its acceptance check and records the result; it does not become the producer. Conductor writes coordination records: briefs, the goal file, Plan Blocks, the CERIC ground hunt (`grounded.md`), the run ledger, the convergence record, and AGENTS/wiki entries. Routed skills and lanes own the domain deliverable. [book:site-reliability-engineering], Trust but Verify.
2. **Facilitate decisions and keep their record.** Put foreseeable forks in the Plan Block; decide small unplanned forks against the stated intent and record them in the run ledger. Use a separate durable decision record when the choice affects later work. [book:facilitating-software-architecture], Introducing Architectural Decision Records.
3. **Scale the ceremony to its value.** Use enough process, artifacts, and checks to manage the task's stakes and dependencies. A one-line fix or lookup needs no fan-out; use a Plan Block when coordination materially clarifies the work. [book:pmbok-guide-7e], 3.3.2. Processes.
4. **Make the evidence trail visible.** Read the project and source material before planning; carry missing information as an owned follow-up instead of turning it into an unsupported assumption. [book:pmbok-guide-7e], 4.6.2. Logs and Registers.
5. **Name the meeting point before dispatch.** Reconcile the threads, preserve contradictions, and report what changed so the run ends in one usable artifact set. [book:learning-systems-thinking], Systems Thinking Is Sociotechnical.

## The flow (at a glance)

| Phase | Goal | Primary artifact |
|---|---|---|
| Classify | Name every work shape and route it | Route sequence |
| Ground | Read project state and source inputs | `grounded.md` |
| Compose | Select lanes, engine, and meeting point | Lane plan |
| Declare | Stop once at the Plan Block for approval, with any intent-interview questions at its top | Plan Block |
| Goal | Write testable success criteria and bind the session stop | Goal file |
| Run | Dispatch units and record results | Lane briefs and run ledger |
| Converge | Resolve interactions and surface unresolved forks | Convergence record |
| Close | Audit the goal file and update project state | UAT results and close report |

## Gates (declared, inherited from core)

The core spine names eight gates. Conductor applies them as follows and records any gate it skips, with the reason, in the Plan Block's `GATES` row:

1. **Result integrity** — report observed outcomes faithfully; a failed UAT remains failed. `../core/references/output-contract.md`.
2. **Grounding and evidence provenance** — Ground reads project state and source inputs; CERIC Gate 1 records claims, evidence, reasoning, context, implications, and missing information. `../core/references/grounding-gate.md`; `references/ceric-gates.md`.
3. **Durable completion records** — Close updates the run log, decisions, active work, and open issues. `../core/references/wiki-protocol.md`.
4. **Confidentiality and external claims** — check data and lane authorization before dispatch; support external claims with appropriate sources. `../core/references/grounding-gate.md`; `references/lane-plan.md`.
5. **Decision records and shared memory** — preserve run, unit, fork, assumption, and decision state in the ledger and project wiki. `../core/references/wiki-protocol.md`; `references/convergence.md`.
6. **Reader-focused writing** — make the Plan Block, briefs, and records usable by their accountable reader. `../core/references/artifact-writing.md`.
7. **Pushback and teaching** — frame unresolved choices as recommended forks with consequences. `../core/references/pushback-and-teach.md`.
8. **Checks and independent review** — run UAT yourself, read an output sample, and audit the synthesis at CERIC Gate 2 when required by the work's risk. `../core/references/output-contract.md`; `references/ceric-gates.md`.

**Approach declaration** is also required for substantive work: choose an approach from the available alternatives and state it in one line; trivial and conversational turns are exempt. [book:facilitating-software-architecture], Stage 2: The Act of Deciding; [book:facilitating-software-architecture], Step 2c (optional): Sharing your decision.

## Flow

### 1. Classify — what shape is this?

Use `references/routing-table.md` for the complete route table, carrier/capability axis, disambiguations, and canonical compose order. Name every work shape present. Do not collapse shapes unless the compose rules say to. A single request can need fact-finding, framing, cross-discipline design, stakeholder challenge, implementation, and delivery in sequence. [book:agentic-mesh], Routing.

### 2. Ground — read the project before planning it

Before composing, read project rules, the wiki index and live state, existing decisions, the declared agent board if present, the relevant skill substrate, and the current harness row. A plan that ignores existing decisions reopens settled questions. [book:agentic-mesh], Agents as Plan Steps; [book:facilitating-software-architecture], Framing the Context.

Read every input document as a CERIC hunt: what it claims, its evidence and reasoning, relevant context, implications, and what is missing. Write `grounded.md` with one section per input and a closing `Grounded:` line. Missing items become `DECIDE NOW` questions and specific questions in the briefs of lanes tasked with resolving them; while open, they also become owned issue-log entries with a responsible person and follow-up. See `references/ceric-gates.md`. [book:learning-systems-thinking], Identify Your Reasons; [book:pmbok-guide-7e], 4.6.2. Logs and Registers.

At Ground, carry forward every fork the prior run left open: restate it in `DECIDE NOW`, or record the evidence and owner decision that resolved or retired it. Close records the resulting state. (derived: dogfood 2026-10-01)

### 2a. Interview — find out what the requester actually wants

Prepared after Ground, sent at Declare. When, after Ground, the request still has an open outcome that would cost a redone stage if guessed wrong, an undecided edge case or two conflicting requirements, prepare 2 to 5 concrete scenario questions about the outcome ("what should happen when…"). Ask about what, not how; ask nothing the record already settles. Each question states the scenario and why it matters, then a default if skipped, or `No default: needed before go` for a fact only the requester holds. Send them at the top of the Plan Block message, with the plan drafted on the defaults, so one reply can answer and give go. Skip the interview when the request is already specific or the requester says to skip. Answers go to `grounded.md` and `INTENT`. Full rules: `references/intent-interview.md`. [book:swebok], 3. Requirements Elicitation.

### 3. Compose — build the workflow

Select a lane and execution engine for each unit, then declare the choice and why. The task shape and risk determine whether work is inline, parallel, or multi-stage; use the definitions and limits in `references/workflow-patterns.md`. [book:agentic-mesh], Explainable and Traceable; [book:agentic-mesh], Task Planning; [book:agentic-mesh], Parallelization; [book:agentic-mesh], Orchestration.

Before finalizing unit assignments or dispatch, run the system check in `references/lane-plan.md` and plan only onto lanes it reports open. If the Plan Block is prepared before a same-turn check is available, use the provisional form in `references/lane-plan.md`; it is not dispatch authorization. That file remains the single home for local lane rules. Select the convergence point before dispatch; a fan-out without a named merger and artifact leaves good work uncombined. [book:agentic-mesh], Parallelization.

On Claude Code, when the dynamic-workflow engine is selected, this skill's instruction to use that workflow is the opt-in; show that authorization in the Plan Block. For other harness-specific primitives and limits, read `references/harness-map.md`.

### 4. Declare — the Plan Block

The Plan Block is the single scheduled checkpoint, before any agent starts. It is one scannable block. Surface every foreseeable fork with two or three options, brief consequences, and a recommendation. A recommendation is for the requester; when seeking advice from others on a decision you own, do not disclose a preferred option if your authority could anchor their response. [book:facilitating-software-architecture], Should You Provisionally Select an Option or Not?

```
INTENT       <restated in one line>
SHAPE        <shapes present, in canonical order> [book:agentic-mesh], Creating the Task Plan
GROUNDED     <files read and what constrains this plan>
ROUTE        <skills invoked, in order, with the mode> [book:agentic-mesh], Identifying Collaborators and Tools
APPROACH     <chosen approach from the alternatives and why, in one line>
ENGINE       <inline, fan-out, or dynamic workflow, and why>
LANES        <checked status, or provisional status with check time and required recheck>
LANE PLAN    <table per references/lane-plan.md; mark provisional until the required check is complete>
SCHEDULE     <waves, loops, batch cap and acceptance, schedule record path; "none" for a single-stage run>
GOAL FILE    <path; written before dispatch; session stop set from its criteria> [book:agentic-mesh], Shared Workspaces for Agents
RUN ID       <identifier shared by every unit and run record>
FAN-OUT      <unit or agent count and what each lane covers> [book:agentic-mesh], Simulation Agents
PERSONAS     <who reacts and what each is asked to test>
CONVERGE     <meeting point and artifacts on disk>
ASSUMPTIONS  <assumptions and constraints to track through the run>
GATES        <core gates applied; any skipped gate and why; human keystone owner, timing, and record if applicable>
DECIDE NOW   <every fork ID and recommendation; when detail would make this block hard to scan, put the full options/consequences register below>
NOT DOING    <explicit out of scope> [book:head-first-pmp], Scope Answers
COST         <agent count, expected time, and any material risk budget> [book:pmbok-guide-7e], 4.4.2. Estimating
```

If the full fork details would make the Plan Block hard to scan, list every fork ID and recommendation in `DECIDE NOW`, then put this register directly below the block:

| ID | Fork | Options and consequences | Recommendation | Decision owner |
|---|---|---|---|---|

(derived: dogfood 2026-10-01)

If the INTENT restatement is wrong, stop here and correct it before any planning continues.

The Plan Block is the only scheduled stop; the intent interview's questions travel in the same message. When an answer changes the plan's stages, lanes, cost, goal criteria or a client-facing `INTENT`, the revised plan gets one more go; an answer that contradicts another answer or a recorded decision allows one follow-up round, sent with that revised plan where both are needed. End the planning turn at the Plan Block; dispatch starts only after an explicit go. Silence is not approval. [book:project-planning-scheduling-control], CHAPTER 17 Using Stagegate® to Select, Evaluate, and Control Projects. After go, decide forward only on choices delegated to you and log the choice. Pause for material scope, commitment, or risk changes that exceed your authority; investigate alternatives and impacts, then give the accountable decision owner a concise recommendation. Stop mid-run for an Integrity Constraint, an irreversible and unrecoverable action, or a falsified plan premise. [book:facilitating-software-architecture], Fast and Wrong Is Better Than Slow and Correct; [book:pmbok-guide-7e], 2.2.4. Leadership Skills.

### 5. Goal — the stop condition, on disk

Before any agent fires, write the goal file, then set the harness's session-stop mechanism from its criteria. The file lives at `wiki/goals/<YYYY-MM-DD>-<slug>.md`, or beside the primary artifact when there is no wiki. Give every criterion a unique ID, source or stakeholder, target artifact, and a concrete UAT command or check. Automate acceptance checks where it is practical; a passing check must demonstrate the criterion. [book:swebok], 6.4. Acceptance Tests. For service work, express reliability targets as measurable SLOs and record the corresponding error budget in the Plan Block. [book:continuous-delivery], Why Is Automated Acceptance Testing Essential?; [book:pmbok-guide-7e], 4.6.6. Visual Data and Information; [book:site-reliability-engineering], SLOs Set Expectations; [book:site-reliability-engineering], Forming Your Error Budget.

Do not use changeable counts as criteria; ensure every decision branch has a passing condition. Record scope changes as dated owner amendments without rewriting earlier criteria. The goal file is written first and is not edited after dispatch except to append an owner amendment when the tested assumption or functionality has genuinely changed. A failed criterion remains a failure; never alter its wording to conceal the result. Details and examples: `references/goal-file.md`. [book:continuous-delivery], Essential Practices.

### 6. Run — to completion

Dispatch each unit under its brief and keep the run ledger in-session, then in `wiki/log.md`. Give every unit the run ID and a stable unit ID. Record its lane, status, verdict, acceptance result, forward-decided forks with reasons, and each refusal/error/reroute using the six-column row shape in `references/lane-plan.md`. Report at meaningful milestones, such as a completed wave or a contradiction, not after each edit.

For repeated item loops, batches, or queued work, maintain the run schedule described in `references/run-schedule.md`; record acceptance at each batch boundary and resume from its durable state.

The coordinator runs each acceptance command against the output and reads a sample of that output before recording PASS. A lane's claim of completion is not proof. Reroute a refusal using the lane plan; when no lane accepts a unit, record it as blocked and report it instead of absorbing it into conductor. Keep sibling gates and project review policy intact. [book:agentic-mesh], Layer 4: Task Planning and Explainability; [book:site-reliability-engineering], Trust but Verify; [book:site-reliability-engineering], Enforcement of Policies and Procedures.

### 7. Converge — the meeting point

Threads must reconcile explicitly. Surface contradictions, test how load-bearing findings and decisions interact, and create one artifact set with a summary of what moved. Keep the evidence, reasoning, and hedges visible; a claim that fails the CERIC audit stays open with a named owner and the information needed to settle it. See `references/convergence.md` and `references/ceric-gates.md`. [book:learning-systems-thinking], Systems Thinking Is Sociotechnical; [book:facilitating-software-architecture], Examining the Interconnectedness of Decisions.

### 8. Close — the UAT audit

Audit the artifacts against the goal file's UAT column and nothing else: run each check and report pass or fail per row. For client-, investor-, or contract-facing changes, route the proposed change through the accountable change authority or project's change control board for approval, delay, or rejection. For internal reversible work, apply it and say so. Update `wiki/decisions.md`, `wiki/log.md`, and `wiki/active-work.md`; leave open issues with an owner and next step. Finish with what exists, what changed, what remains open, and every fork decided forward. [book:head-first-pmp], Is the product ready to go?; [book:continuous-delivery], Essential Practices; [book:pmbok-guide-7e], 4.4.3. Meetings and Events; [book:swebok], 4. Software Configuration Status Accounting.

## Anti-patterns (hard no-list)

- Doing the unit in the coordinator: writing the deliverable, reasoning about the domain, or absorbing work refused by every lane.
- Smuggling upstream content into a brief instead of naming its exact file, section, and row.
- Treating a lane's completion claim as acceptance, or recording PASS without reading an output sample.
- Rewording a failed criterion to fit what was produced.
- Leaving a foreseeable fork out of `DECIDE NOW`, or returning mid-run with a context-free question.
- Launching fan-out without a declared meeting point, or silently smoothing away contradictory evidence.
- Skipping the project and source read before planning.
- Planning on a guessed intent when the outcome is open, or interviewing about what the record already settles or about how to build it.
- Waiving a sibling's gate to meet the plan.
- Adding process elements that do not earn their cost, or omitting checks that matter to the task's risk. Scale the Plan Block and artifacts to the work rather than using a fixed unit-count trigger. [book:pmbok-guide-7e], 3.3.2. Processes.

## Composition

- **Inherits:** `core` — integrity constraints, grounding, output contract, pushback and teach, and wiki protocol.
- **Coordinates:** CERIC, the routed domain skills, and lane work according to `references/routing-table.md`.
- **Owns:** routing, Plan Block, task-force protocol, persona fan-out, design-cell coordination, lane plan, goal-file convention, run ledger, and convergence contract.
- **Defers to:** a sibling the user invoked directly; conductor stays out of the way.

## References

- `references/routing-table.md` — work-shape and carrier routing, disambiguation, composition order, and absorbed-route migration.
- `references/task-force-protocol.md` — sourced fact-finding, adversarial verification, and synthesis.
- `references/design-cell.md` — cross-discipline producers, interface contracts, and one coherent spec.
- `references/persona-fanout.md` — stakeholder reactions and the objection register.
- `references/convergence.md` — contradiction and interaction passes, decision records, and durable landing.
- `references/lane-plan.md` — local lane check, providers, invocation, brief contract, selection, and fallback.
- `references/run-schedule.md` — waves, per-item loops, batch boundaries, queue/watch operations, per-batch acceptance, and resume state.
- `references/intent-interview.md` — when to ask scenario questions about the outcome before planning, how to ask them, and where the answers go.
- `references/goal-file.md` — goal-file template, UAT criteria, amendments, and close audit.
- `references/harness-map.md` — harness-specific instruction files and orchestration/session-stop facts.
- `references/workflow-patterns.md` — engine choice, pipelines, barriers, resume safety, and coordination topologies.
- `references/ceric-gates.md` — CERIC at Ground, Converge, and Close.
