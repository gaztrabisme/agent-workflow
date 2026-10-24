# Running the work with agents

How this skill runs multi-step work: one person directs agents, each agent works to a brief, and the person (the coordinator) checks every result before it counts. The run produces a Plan Block, briefs, a run ledger and a convergence record for the accountable lead. Domain work belongs to the routed skill or to a briefed agent; the coordinator does not write the deliverable or reason through its domain. [book:facilitating-software-architecture], If You Have Experience, Facilitate Decisions Rather than Deciding Yourself.

This method was the former `conductor` skill, merged into `project` on 14 Oct 2026; its history is in `../../history/conductor-EVOLUTION.md`.

## PRINCE2 terms

| PRINCE2 term | In an agent run |
|---|---|
| Work package | An agent's brief: the product it must produce, its quality criteria (the acceptance command), its tolerances, and how to report back. Shape and fields: [lane-plan.md](lane-plan.md). Work packages are defined together with the team that will do the work. [book:prince2-agile], Chapter 20: Managing product delivery |
| Checkpoint report | The agent's report, written before it runs out of steps even when the verdict is FAIL |
| Quality review | The acceptance check the coordinator runs, plus a review by an agent that did not produce the work and has no prior context, briefed with the product's quality criteria |
| Exception | A forecast that a tolerance (time, cost, scope, quality, benefits, risk) will be broken; it stops the run and goes to the owner (see [Mid-run stops](#mid-run-stops)) |
| Highlight report | The report to the owner at a milestone and at Close |
| Stage boundary | The Plan Block go, and the Close audit |

## Principles

1. **Coordinate; do not take the unit.** Every unit belongs to a routed skill or an agent with a brief. The coordinator runs its acceptance check and records the result; it does not become the producer. The coordinator writes coordination records: briefs, the goal file, Plan Blocks, the CERIC ground hunt (`grounded.md`), the run ledger, the convergence record, and AGENTS/wiki entries. Routed skills and agents own the domain deliverable. [book:site-reliability-engineering], Trust but Verify.
2. **Facilitate decisions and keep their record.** Put foreseeable forks in the Plan Block; decide small unplanned forks against the stated intent and record them in the run ledger. Use a separate durable decision record when the choice affects later work. [book:facilitating-software-architecture], Introducing Architectural Decision Records.
3. **Scale the ceremony to its value.** Use enough process, artifacts, and checks to manage the task's stakes and dependencies. A one-line fix or lookup needs no fan-out; use a Plan Block when coordination materially clarifies the work. [book:pmbok-guide-7e], 3.3.2. Processes.
4. **Make the evidence trail visible.** Read the project and source material before planning; carry missing information as an owned follow-up instead of turning it into an unsupported assumption. [book:pmbok-guide-7e], 4.6.2. Logs and Registers.
5. **Name the meeting point before dispatch.** Reconcile the threads, preserve contradictions, and report what changed so the run ends in one usable artifact set. [book:learning-systems-thinking], Systems Thinking Is Sociotechnical.

## Scope

- **This method:** a substantive multi-step request that needs coordinated stages, whether a project stage or multi-step work that is not a project.
- **The owning skill:** the user names a skill directly, or one skill already owns the requested artifact and audience. This method stays out of the way. Decide on artifact and audience; implementation, presale architecture and signed-engagement delivery stay with their owners. Full rules: [../routing.md](../routing.md).

## Flow at a glance

| Phase | Goal | Primary artifact |
|---|---|---|
| Classify | Name every work shape and route it | Route sequence |
| Ground | Read project state and source inputs | `grounded.md` |
| Compose | Select agents (lanes), engine, and meeting point | Lane plan |
| Declare | Stop once at the Plan Block for approval, with any intent-interview questions at its top | Plan Block |
| Goal | Write testable success criteria and bind the session stop | Goal file |
| Run | Dispatch work packages and record checkpoint reports | Briefs and run ledger |
| Converge | Resolve interactions and surface unresolved forks | Convergence record |
| Close | Audit the goal file and update project state | UAT results and close report |

## 1. Classify

Use [../routing.md](../routing.md) for the route table, carrier and capability skills, disambiguations, and the canonical compose order. Name every work shape present. Do not collapse shapes unless the compose rules say to. A single request can need fact-finding, framing, cross-discipline design, stakeholder challenge, implementation, and delivery in sequence. [book:agentic-mesh], Routing.

## 2. Ground

Before composing, read project rules, the wiki index and live state, existing decisions, the declared agent board if present, the relevant skill substrate, and the current harness row. A plan that ignores existing decisions reopens settled questions. [book:agentic-mesh], Agents as Plan Steps; [book:facilitating-software-architecture], Framing the Context.

Read every input document as a CERIC hunt: what it claims, its evidence and reasoning, relevant context, implications, and what is missing. For a shared Office file, its comments, speaker notes and tracked changes are part of the input; say in the report what they ask for. (derived: LSP 2026-10-09) Write `grounded.md` with one section per input and a closing `Grounded:` line. Missing items become `Decisions for you` questions and specific questions in the briefs of agents tasked with resolving them; while open, they also become owned issue-log entries with a responsible person and follow-up. See [ceric-gates.md](ceric-gates.md). [book:learning-systems-thinking], Identify Your Reasons; [book:pmbok-guide-7e], 4.6.2. Logs and Registers.

At Ground, carry forward every fork the prior run left open: restate it in `Decisions for you`, or record the evidence and owner decision that resolved or retired it. Close records the resulting state. (derived: dogfood 2026-10-01)

### Intent interview

Prepared after Ground, sent at Declare. When, after Ground, the request still has an open outcome that would cost a redone stage if guessed wrong, an undecided edge case or two conflicting requirements, prepare 2 to 5 concrete scenario questions about the outcome ("what should happen when…"). Ask about what, not how; ask nothing the record already settles. Each question states the scenario and why it matters, then a default if skipped, or `No default: needed before go` for a fact only the requester holds. Send them at the top of the Plan Block message, with the plan drafted on the defaults, so one reply can answer and give go. Skip the interview when the request is already specific or the requester says to skip. Answers go to `grounded.md` and `Goal`. Full rules: [intent-interview.md](intent-interview.md). [book:swebok], 3. Requirements Elicitation.

## 3. Compose

Select an agent (lane) and execution engine for each unit, then declare the choice and why. The task shape and risk determine whether work is inline, parallel, or multi-stage; use the definitions and limits in [workflow-patterns.md](workflow-patterns.md). [book:agentic-mesh], Explainable and Traceable; [book:agentic-mesh], Task Planning; [book:agentic-mesh], Parallelization; [book:agentic-mesh], Orchestration.

Before finalizing unit assignments or dispatch, run the system check in [lane-plan.md](lane-plan.md) and plan only onto lanes it reports open. If the Plan Block is prepared before a same-turn check is available, use the provisional form in [lane-plan.md](lane-plan.md); it is not dispatch authorization. That file remains the single home for local lane rules. Select the convergence point before dispatch; a fan-out without a named merger and artifact leaves good work uncombined. [book:agentic-mesh], Parallelization.

When the owner says "dynamic workflow", the engine is the provider-lane dynamic workflow in [workflow-patterns.md](workflow-patterns.md): every unit on a `subagent` provider lane, the coordinator as the pipeline, and no Claude Workflow or Agent fan-out (a hook blocks both for that session). Claude Code's own Workflow tool is used only when the owner says "ultracode"; that word is the opt-in, shown in the Plan Block. For other harness-specific primitives and limits, read [harness-map.md](harness-map.md).

## 4. Declare: the Plan Block

The Plan Block is the single scheduled checkpoint, before any agent starts. Surface every foreseeable fork with two or three options, brief consequences, and a recommendation. Put to the requester only the forks that need something only they hold: the goal, money, taste, accounts and approvals, and facts about their own situation. Decide technical forks (thresholds, methods, models, structure) yourself and list each under `Decided by coordinator` with its one-line reason, so the requester can overrule it (Huy, 2026-10-20: "I just set the goal you decide these technical details"). A recommendation is for the requester; when seeking advice from others on a decision you own, do not disclose a preferred option if your authority could anchor their response. [book:facilitating-software-architecture], Should You Provisionally Select an Option or Not?

Print it as a two-column Markdown table, never as an aligned text block: a long value in a text block wraps under the next label, and the reader loses which label it belongs to (Huy, 2026-10-18). Use the row names below as written; each cell says the thing in plain words, with any file name or ID explained in the same cell. Leave out a row that does not apply to the run rather than filling it with "none", except `Decisions for you`, which always comes first.

| Item | Plan |
|---|---|
| Decisions for you | each fork only the requester can settle, with its recommendation; when detail would make the table hard to scan, put the full register below it |
| Decided by coordinator | each technical fork, the option chosen and why in one line |
| Goal | the request restated in one line |
| Kind of work | the shapes present, in canonical order [book:agentic-mesh], Creating the Task Plan |
| What was read | files read and what constrains this plan |
| Skills used | skills invoked, in order, with the mode [book:agentic-mesh], Identifying Collaborators and Tools |
| Approach | chosen approach from the alternatives and why, in one line |
| How it runs | inline, fan-out, or dynamic workflow, and why |
| Lanes open | checked status, or provisional status with check time and required recheck |
| Who does what | table per lane-plan.md; mark provisional until the required check is complete |
| Schedule | waves, loops, batch cap and acceptance, schedule record path |
| Success criteria | goal file path; written before dispatch; session stop set from its criteria [book:agentic-mesh], Shared Workspaces for Agents |
| Run ID | identifier shared by every unit and run record |
| Agents | unit or agent count and what each lane covers [book:agentic-mesh], Simulation Agents |
| Reviewers | who reacts and what each is asked to test |
| Merge point | where the threads meet, and the artifacts on disk |
| Assumptions | assumptions and constraints to track through the run |
| Checks | core gates applied; any skipped gate and why; human keystone owner, timing, and record if applicable |
| Out of scope | what this run will not do [book:head-first-pmp], Scope Answers |
| Cost | agent count, expected time, and any material risk budget [book:pmbok-guide-7e], 4.4.2. Estimating |

**Native plan mode.** When a person will approve the plan in this session's window, enter plan mode (`EnterPlanMode`) at the start of Classify, so Classify and Ground run read-only, and present the Plan Block table with `ExitPlanMode`; the approval there is the go. Plan mode cannot write files, so `grounded.md` goes into the plan itself or is written right after approval. Skip plan mode when no person is there to approve: `claude -p` runs, runs launched by another session, and scheduled turns. There, end the turn at the Plan Block as text and wait for the go. In a bypass-mode session the approval prompt's first option ("Yes, and switch to BYPASS PERMISSIONS") returns the session to bypass, so messages to and from the other sessions keep flowing; "manually approve edits" drops it to a mode where they are held (tested 2026-10-18).

If the full fork details would make the Plan Block hard to scan, list every fork and its recommendation in `Decisions for you`, then put this register directly below the table:

| ID | Fork | Options and consequences | Recommendation | Decision owner |
|---|---|---|---|---|

(derived: dogfood 2026-10-01)

If the `Goal` restatement is wrong, stop here and correct it before any planning continues.

The Plan Block is the only scheduled stop; the intent interview's questions travel in the same message. When an answer changes the plan's stages, lanes, cost, goal criteria or a client-facing `Goal`, the revised plan gets one more go; an answer that contradicts another answer or a recorded decision allows one follow-up round, sent with that revised plan where both are needed. End the planning turn at the Plan Block; dispatch starts only after an explicit go. Silence is not approval. [book:project-planning-scheduling-control], CHAPTER 17 Using Stagegate® to Select, Evaluate, and Control Projects. After go, decide forward only on choices delegated to you and log the choice. Technical choices (thresholds, methods, models, structure, a small fix inside the plan) count as delegated unless the requester said otherwise: make the choice, log it with its reason, and report it rather than asking first (Huy, 2026-10-23: "dont stop to ask, just decide yourself"). Pause for material scope, commitment, or risk changes that exceed your authority; investigate alternatives and impacts, then give the accountable decision owner a concise recommendation. Stop mid-run when continuing would break one of core's gates, for an irreversible and unrecoverable action, or for a falsified plan premise. [book:facilitating-software-architecture], Fast and Wrong Is Better Than Slow and Correct; [book:pmbok-guide-7e], 2.2.4. Leadership Skills.

## Approach declaration

Required for substantive work: choose an approach from the available alternatives and state it in one line, in the Plan Block's `Approach` row; trivial and conversational turns are exempt. [book:facilitating-software-architecture], Stage 2: The Act of Deciding; [book:facilitating-software-architecture], Step 2c (optional): Sharing your decision.

## 5. Goal: the stop condition on disk

Before any agent fires, write the goal file, then set the harness's session-stop mechanism from its criteria. The file lives at `wiki/goals/<YYYY-MM-DD>-<slug>.md`, or beside the primary artifact when there is no wiki. Give every criterion a unique ID, source or stakeholder, target artifact, and a concrete UAT command or check. Automate acceptance checks where it is practical; a passing check must demonstrate the criterion. [book:swebok], 6.4. Acceptance Tests. For service work, express reliability targets as measurable SLOs and record the corresponding error budget in the Plan Block. [book:continuous-delivery], Why Is Automated Acceptance Testing Essential?; [book:pmbok-guide-7e], 4.6.6. Visual Data and Information; [book:site-reliability-engineering], SLOs Set Expectations; [book:site-reliability-engineering], Forming Your Error Budget.

On Claude Code, the goal file's `## Goal block` is the session stop: the plan-goal plugin arms from it when the file is marked APPROVED, so `/goal` is not typed.

Do not use changeable counts as criteria; ensure every decision branch has a passing condition. Record scope changes as dated owner amendments without rewriting earlier criteria. The goal file is written first and is not edited after dispatch except to append an owner amendment when the tested assumption or functionality has genuinely changed. A failed criterion remains a failure; never alter its wording to conceal the result. Details and examples: [goal-file.md](goal-file.md). [book:continuous-delivery], Essential Practices.

## 6. Run

Dispatch each work package under its brief and keep the run ledger in-session, then in `wiki/log.md`. Give every unit the run ID and a stable unit ID. Record its lane, status, verdict, acceptance result, forward-decided forks with reasons, and each refusal/error/reroute using the six-column row shape in [lane-plan.md](lane-plan.md). Report to the owner (highlight report) at meaningful milestones, such as a completed wave or a contradiction, not after each edit.

For repeated item loops, batches, or queued work, maintain the run schedule described in [run-schedule.md](run-schedule.md); record acceptance at each batch boundary and resume from its durable state.

The coordinator runs each acceptance command against the output and reads a sample of that output before recording PASS. An agent's claim of completion (its checkpoint report) is not proof. Reroute a refusal using the lane plan; when no lane accepts a unit, record it as blocked and report it instead of absorbing it into the coordinator. Keep sibling gates and project review policy intact. [book:agentic-mesh], Layer 4: Task Planning and Explainability; [book:site-reliability-engineering], Trust but Verify; [book:site-reliability-engineering], Enforcement of Policies and Procedures.

### Mid-run stops

A question raised mid-run arrives after findings the owner has not read, so it cannot be answered well. Put every foreseeable fork in the Plan Block at go. A fork that was not planned is decided forward and logged in the ledger. When a stop is unavoidable (the cases in step 4, including a forecast tolerance breach), state what ran, what it found, the fork, each option with its consequences, and your recommendation. The owner should be able to answer without opening anything else. Never send "I hit a problem, advise."

## 7. Converge

Threads must reconcile explicitly. Surface contradictions, test how load-bearing findings and decisions interact, and create one artifact set with a summary of what moved. Keep the evidence, reasoning, and hedges visible; a claim that fails the CERIC audit stays open with a named owner and the information needed to settle it. See [convergence.md](convergence.md) and [ceric-gates.md](ceric-gates.md). [book:learning-systems-thinking], Systems Thinking Is Sociotechnical; [book:facilitating-software-architecture], Examining the Interconnectedness of Decisions.

## 8. Close: the UAT audit

Audit the artifacts against the goal file's UAT column and nothing else: run each check and report pass or fail per row. For client-, investor-, or contract-facing changes, route the proposed change through the accountable change authority or project's change control board for approval, delay, or rejection. For internal reversible work, apply it and say so. Update `wiki/decisions.md`, `wiki/log.md`, and `wiki/active-work.md`; leave open issues with an owner and next step. Finish with what exists, what changed, what remains open, and every fork decided forward. [book:head-first-pmp], Is the product ready to go?; [book:continuous-delivery], Essential Practices; [book:pmbok-guide-7e], 4.4.3. Meetings and Events; [book:swebok], 4. Software Configuration Status Accounting.

## Gates as applied

The core spine names eight gates. A run applies them as follows and records any gate it skips, with the reason, in the Plan Block's `Checks` row:

1. **Result integrity** — report observed outcomes faithfully; a failed UAT remains failed. `../../../core/references/output-contract.md`.
2. **Grounding and evidence provenance** — Ground reads project state and source inputs; CERIC Gate 1 records claims, evidence, reasoning, context, implications, and missing information. `../../../core/references/grounding-gate.md`; [ceric-gates.md](ceric-gates.md).
3. **Durable completion records** — Close updates the run log, decisions, active work, and open issues. `../../../core/references/wiki-protocol.md`.
4. **Confidentiality and external claims** — check data and lane authorization before dispatch; support external claims with appropriate sources. `../../../core/references/grounding-gate.md`; [lane-plan.md](lane-plan.md).
5. **Decision records and shared memory** — preserve run, unit, fork, assumption, and decision state in the ledger and project wiki. `../../../core/references/wiki-protocol.md`; [convergence.md](convergence.md).
6. **Reader-focused writing** — make the Plan Block, briefs, and records usable by their accountable reader. `../../../core/references/artifact-writing.md`.
7. **Pushback and teaching** — frame unresolved choices as recommended forks with consequences. `../../../core/references/pushback-and-teach.md`.
8. **Checks and independent review** — run UAT yourself, read an output sample, and audit the synthesis at CERIC Gate 2 when required by the work's risk. `../../../core/references/output-contract.md`; [ceric-gates.md](ceric-gates.md).

The approach declaration is also required; see [Approach declaration](#approach-declaration).

## Ownership

- **Inherits:** `core` — result integrity, grounding, output contract, pushback and teach, and wiki protocol.
- **Coordinates:** CERIC, the routed domain skills, and agent work according to [../routing.md](../routing.md).
- **Owns:** routing, Plan Block, task-force protocol, persona fan-out, design-cell coordination, lane plan, goal-file convention, run ledger, and convergence contract.
- **Defers to:** a sibling the user invoked directly.

## Anti-patterns

The hard no-list for running agents is in [../anti-patterns.md](../anti-patterns.md#running-agents); one copy, kept there.
