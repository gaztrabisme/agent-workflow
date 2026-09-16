# Evolution Log — conductor

The ledger. Every change: the trace that motivated it, the edit, and the verdict.
Verdicts are `PENDING` until **≥2 independent real uses** confirm `KEEP`.
Protocol: `../evolution/references/loop.md`.

---

## Evolution 1 — 2026-08-06 — Birth: the missing entry point

### Why it exists

The constellation composes correctly on paper — `core` is a real kernel, `harness-operator`
draws the SA/delivery/dev composition explicitly, every sibling disambiguates against its
neighbours on a stated axis. What it had no answer for was the **first move**: a raw intent,
unrouted, with no human deciding which skill owns it. Everything downstream of that decision
worked; the decision itself was made by hand, every time.

The trigger was a request to **merge** the constellation into one skill. That was declined —
`skill-builder`'s own rule ("compose, don't merge; a mega-skill triggers on everything and
disambiguates nothing"), plus three mechanical failures: merging destroys the description-level
disambiguation the siblings were built around, loads ~10,500 lines of markdown on every turn
instead of progressively disclosing it, and collapses seven independent `EVOLUTION.md` verdict
streams into one where nothing can be attributed. The repo's own history is the strongest
argument: root `SKILL.md` *was* one skill, and was deliberately decomposed into `core` +
siblings. A merge is a completed migration run backwards.

The real gap was a **driver**, not a merge — and `harness-operator` already demonstrated the
shape (80 lines, deliberately thin, *"all judgment content lives in the siblings; mine them,
never duplicate them here"*). Conductor is that shape one level up: it covers the whole
intent → product arc rather than the build spine alone.

### Traces it was built from

**T1 — the pattern already worked twice, and was written down nowhere.** A live engagement ran
an 8-agent market validation (2026-08-03) and a 10-agent cost validation (2026-08-06: 6 research
streams + 4 adversarial verifiers, 228 tool calls, bilingual sources) that line-audited a budget
inside a funding document, moved it under 2%, and sourced every line. Both were invented in the
moment from scratch. → `references/task-force-protocol.md` codifies the shape: domain-cut
streams, confidence grades, verdict-vs-assumption columns, refute-instructed verifiers that must
find *uncited* sources, a quote-required section for what research cannot settle, and
propose-don't-apply on anything client-facing.

**T2 — persona fan-out did not exist anywhere.** Grepped the full constellation: zero hits.
`dev/references/subagent-briefs.md` carries research / test / impl / verify / adversarial /
spec-adversarial / mechanical — every one of them *disinterested*. Nothing in the constellation
could surface an objection driven by a stakeholder's incentives rather than by correctness, which
is the class of objection that actually stops deals. → `references/persona-fanout.md`, with the
persona-vs-adversarial distinction made explicit so the briefs don't collapse into each other.

**T4 — the fan-out taxonomy had a hole where the most-wanted mode should be.** The user described
the pattern they actually wanted — *"each subagent gets a business-context ground truth file, each
assumes a role (solution architect, delivery manager, backend, frontend, intended user), each
researches and writes documents, then a mechanism for them to see each other's and cross-review into
a final coherent document"* — and it matched nothing built. `task-force-protocol` investigates;
`persona-fanout` reacts. Neither **produces**. The cast also mixed two agent types silently: four
producers and one *receiver*, where the receiver cannot author a design document because at T0 there
is no artifact to react to. → H6, and the user narrative reframed as a derivation over testimony.

**T5 — the routing table only covered skills that *decide*.** Asked whether `pptx`, `drawio` and the
frontend/taste skills were routed, the answer was half-no: doc and sheet carriers were listed, the
diagram, chart, artifact, colour and API-docs skills were not, and the five overlapping frontend
skills — three of them symlinks into one repo — had no disambiguation at all. The miss was
conceptual, not clerical: a deck is not a *kind of work*, it is the **form an artifact takes**, and
form is chosen on a different axis from shape. → H7.

**T3 — the checkpoint placement was set by the user, against the obvious design.** The intuitive
answer to "where should it stop?" is *between phases*. Rejected on a stated reason: *"if it stops
in the middle I don't have the context of what it had been doing so far to make a decision."* A
mid-run stop asks for a decision with hour-old context plus a paragraph — stripped of exactly what
would answer it. → the one-stop-at-T0 design, the `DECIDE NOW` row that front-loads every
foreseeable fork, and the *decide forward / escalate whole* rule.

### What shipped

| # | Trace | Edit |
|---|---|---|
| H1 | T3 | `SKILL.md` — single checkpoint at T0; the Plan Block with `DECIDE NOW` as its load-bearing row; the four legitimate mid-run stops enumerated as a closed list; escalation must be self-contained |
| H2 | T1 | `references/task-force-protocol.md` — stream/verifier briefs, confidence + verdict-vs-assumption contract, engine selection by agent count, propose-don't-apply |
| H3 | T2 | `references/persona-fanout.md` — casting rules, the cold-artifact brief, the five-section return, objection register with presentation/substance/fact typing |
| H4 | — | `references/convergence.md` — the three failure modes (staple / average / lose-the-tail), and the **interaction pass**: does finding A change what finding B means. Nothing in a single thread can see this by construction |
| H5 | — | `references/routing-table.md` — intent→skill map reusing the siblings' existing disambiguation axes (artifact+audience, tense, board) rather than inventing a fourth |
| H6 | T4 | `references/design-cell.md` — the third fan-out mode. Producers author under **exclusive** mandates and close with an interface contract (OWN / PROVIDE / NEED / ASSUME / OPEN); cross-review reads contracts only, from each reviewer's own stake; a **fresh** reconciler runs five mechanical checks. User narratives are a *derivation over testimony* with grounding tiers, not a role-play |
| H7 | T5 | `references/routing-table.md` — the **second axis**: work shape picks the skill that decides, artifact form picks the skill that renders. Carrier chosen in the Plan Block, never at the end; a carrier never decides content. Frontend's five overlapping skills split into one workflow choice **plus** one aesthetic direction |
| H8 | — | `routing-table.md` — "no board is a question, not an answer": substantial build work on a boardless project *proposes* onboarding instead of falling through to `dev` silently |

### Verdict: `PENDING` — nothing here has been fire-tested

Authored, not yet run. Two of the eight edits (H2, H3) are distilled from real traces and two more
(H6, H7) from a live design conversation; the rest are design. Per the evolution loop,
**distilled ≠ validated**.

**The dogfood gate has not been run.** `skill-builder` calls it non-negotiable: a skill is not done
until a *fresh-context* subagent has used it on a real task and the findings are folded back. That
gate is open, stated here rather than skipped silently — per `core` spine #3.

**Self-inflicted defect worth recording, because it is the class this skill is supposed to prevent.**
A consistency check after authoring found the skill contradicting itself in three places: SKILL.md
carried six work shapes while `routing-table.md` carried five, the two files stated *different*
compose orders, `design-cell.md` was orphaned (no routing row pointed at it), and this ledger
described five edits when eight had shipped. Cause: the shape vocabulary and the compose order were
each stated in **two** files. Fix: one canonical statement in `routing-table.md`, SKILL.md points at
it. This is `delivery`'s "two numbering systems" anti-pattern, committed by the skill whose own job
is convergence — which is the argument for running the dogfood gate rather than trusting a read.

### What to watch on the first real runs

- **Does conductor actually fire?** It competes for triggers with `dev` on build-shaped prompts.
  If it loses consistently, the fix is a routing line in the user's global `CLAUDE.md`, not a
  broader description — a broader description is the mega-skill failure arriving by the back door.
- **Is `DECIDE NOW` ever empty on non-trivial work?** That is the single measurable proxy for
  whether H1 works. An empty row followed by a mid-run stop falsifies the whole design.
- **Does the interaction pass (H4) find anything?** If three runs produce no cross-thread
  interaction, it is ceremony and should be cut to a line in the synthesis contract.
- **Does conductor stay out of the domain?** The predicted failure mode is conductor reasoning
  about the work instead of routing it. Watch for it doing research inline rather than dispatching.
- **Does the persona register's presentation/substance/fact split hold?** If most objections land
  in one bucket, the typing is not earning its column.

---

## Evolution 2 — 2026-09-15 — remake: lanes, goal file, CERIC gates

### Why it exists

Harvest scope: the 2026-09-15 session that built `ceric` and remade this skill. Two failures
from that session are the spine of this entry: the coordinator doing unit work itself, and a
Claude workflow burning the session budget. The skill that survived that session routed well
and then violated its own identity — which is the strongest kind of trace a skill can harvest.

### Traces it was built from

**T1 — the coordinator did unit work.** The run's orchestrator wrote analysis content instead
of briefing a lane. The existing anti-pattern ("Doing the work") was too vague to catch it: it
named the domain-reasoning case, not the drafting case. → H1.

**T2 — a Claude workflow burned the session.** A Workflow fan-out of 12 graders plus 2
verifiers per finding reached 154 agents and 1.8 M tokens before the session limit killed the
run with 7 agents done. The cost was unbudgeted because subagent lanes were unplanned. → H2, H3.

**T3 — lanes refused with no fallback discipline.** DeepSeek returned "Insufficient Balance";
Codex's quota turned out to be per account (all three models, one limit, reset reported for
20 Sep). Nothing written said what to do when a lane refuses. → H2.

**T4 — criteria were not the audit.** Success criteria existed (`GOAL-2026-09-15.md`, rows
1.x/2.x) but nothing bound Close to them; `/goal` sets a session stop condition and leaves no
durable record unless a file is written. → H4.

**T5 — inputs were skimmed and the synthesis carried unevidenced claims.** `ceric`, built in
the same session, is the instrument for both: hunt on read, claim audit on merge. → H5.

### What shipped

| # | Trace | Edit |
|---|---|---|
| H1 | T1 | `SKILL.md` — identity narrowed to orchestration + administrative paperwork (briefs, goal file, Plan Blocks, AGENTS.md/wiki entries, run ledger); anti-pattern renamed to the violation itself: "conductor wrote the report itself" |
| H2 | T2, T3 | `references/lane-plan.md` (new) + `LANE PLAN` row in the Plan Block — the machine's lanes with command shapes, models, quotas; the brief contract (Target · Change · Acceptance, acceptance run by the coordinator); lane-selection table; quota fallback (next model → next lane → record in ledger → stop and report) |
| H3 | T2 | `references/lane-plan.md` — Claude fan-outs ≤ 8 agents, never verifier layers at scale; the 154-agent run recorded as the reason |
| H4 | T4 | `references/goal-file.md` (new) + `GOAL FILE` row + the Goal step between Plan Block and Run — file first, then `/goal`; Close audits the goal file's UAT column and nothing else; failed criteria reported, never re-worded |
| H5 | T5 | `references/ceric-gates.md` (new) — CERIC wired as three gates: ground hunts every input (missing register → `DECIDE NOW`), converge audits the synthesis as a claim table, close runs the UAT; `ceric` added to Composition |

### Verdict: `PENDING`

Authored from one session's traces; nothing here has been fire-tested on a run that is not the
one that produced them.

**Validation list — what would move this to KEEP:**
- A multi-lane run fills the `LANE PLAN` per unit before dispatch, and the coordinator runs
  each acceptance command itself.
- A lane refusal produces a ledger line and a reroute; the coordinator absorbs no unit.
- Close reports a failed criterion as failed, at least once, without re-wording it.
- The converge claim table appears in a real synthesis and catches at least one claim.
- The ≤ 8 Claude cap and the per-account Codex quota are re-measured on the next run before
  the numbers are trusted; DeepSeek balance and Codex quota are live facts, not constants.

**What to watch:** whether the Goal step earns its place on small runs or degrades into
ceremony (core spine #9 — cut it if a small run's goal file never gets audited against);
whether `lane-plan.md`'s numbers survive first contact with live quotas.

### Dogfood findings and their disposition

The dogfood gate has now run: the critic was a fresh-context GLM agent that used the skill on a
real planning intent and stopped at the Plan Block as designed. Eleven findings, all applied,
each with the file it changed. This entry's verdict stays `PENDING`.

1. The one stop had no protocol for stopping — `SKILL.md` §4: end the turn after the Plan Block; the run fires only on an explicit go from the requester; silence is not go. Run opens with the same condition.
2. A structural insert silently breaks constellation-wide numbering — `references/lane-plan.md`: Target names the anchors other files cite, and a unit touching numbered structure carries the `grep -rn "spine #\|SKILL.md §"` sweep and the repointing, proven by its Acceptance command.
3. Deliverable content could be smuggled in through the brief — `references/lane-plan.md`: Change names its upstream source ("exactly as given in <file> §<n> row <m>") instead of containing it; `SKILL.md` gains the anti-pattern "Smuggling content through the brief".
4. The LANE PLAN row and `lane-plan.md` disagreed about where the table lives — `SKILL.md`: the row reads `<table per references/lane-plan.md, appended directly below this block>`.
5. The ceremony threshold had no counter-trigger — `SKILL.md`: more than two units, two units on one file, or any edit to numbered structure gets the Plan Block even when each unit is one file.
6. Lane selection routed onto lanes the file itself recorded dead — `references/lane-plan.md`: dead lanes struck from the selection table at run start with a status line for which lanes were open when last checked, and a unit whose primary lane is closed is planned with a primary and a fallback lane.
7. Gate 2 had no audited object on a build run — `references/ceric-gates.md`: research → the synthesis, personas → the objection register, build → the run report and the ledger's claims, never the code; this resolves `convergence.md`'s "conductor does not re-judge" build-unit rule.
8. Gate 1 mandated the hunt but gave the output no home — `references/ceric-gates.md`: the artifact is `grounded.md` beside the Plan Block, per input document Claim / Evidence / Reasoning / Context / Implications / MISSING plus the `Grounded:` line; `SKILL.md` §2 points at it.
9. The domain-reasoning anti-pattern overclaimed against Ground — `SKILL.md`: reading and auditing inputs is conductor's own work; producing deliverable content from them is not.
10. `/goal` is environment-bound — `references/goal-file.md`: or the harness's equivalent session-stop mechanism; failing that, the UAT column is the stop condition and Close runs it.
11. The flow diagram ended at "product" before Close — `SKILL.md`: the arrow ends at CLOSE, with product after it.

---

## Evolution 3 — 2026-09-16 — harness map and dynamic-workflow binding

### Why it exists

Harvest scope: the 2026-09-16 harness research (`~/Documents/Work/lab/ceric/harness-research.md` — six harnesses, every cell carrying an official-doc URL fetched live that day, gaps kept as MISSING) and Gary's statement that the skill runs across agents ("find equivalents for other agents; go"). The goal file for this run: `GOAL-2026-09-16-harness-map.md`.

The skill's machinery assumed Claude Code in two load-bearing places. The Compose engine table named "Workflow script" as if every harness had one, and the Goal step invoked `/goal` as if every harness had it. Both assumptions fail on five of the six harnesses the research covers, at the two steps that do the heavy lifting: the engine that fans out, and the mechanism that keeps the run going.

### Traces it was built from

**T1 — the scripted pipeline is Claude Code's alone.** The research found exactly one documented multi-stage workflow primitive across the six harnesses: Claude Code's dynamic workflows, a JavaScript script orchestrating subagents through the Workflow tool, opted in by the "Ultracode" keyword or a session toggle, scripts saved under `.claude/workflows/`. The other five: MISSING. A skill that offers the Workflow script as an engine breaks at compose time on every harness without one. → H1, H4.

**T2 — the goal loop is Claude Code's alone, with one bounded cousin.** `/goal` keeps starting turns until a small model judges the criteria met. Copilot CLI's autopilot stops at a continuation limit (default 5), not at a stated criterion. The other four: MISSING. The fallback was already half-built: Close audits the UAT column, and Evolution 2's dogfood finding 10 made goal-file.md name "the harness's equivalent session-stop mechanism". What was missing was the generic term itself and the map saying which harness has what. → H3, H5.

**T3 — the universal facts are the ones the skill already assumed silently.** Every harness loads a Markdown instruction file at session start (`CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `.github/copilot-instructions.md`), and five of six tie skill triggering to the `SKILL.md` frontmatter `description` (Copilot CLI: MISSING on fetched pages). The skill's Ground step and its description assume both; the map records them as established per harness, with sources. → H2.

**T4 — the subagent primitive exists everywhere; the caps mostly do not.** All six spawn subagents in some form (Agent tool, multi-agent tools, named tools, `@` mention, custom agents, child sessions), but only Claude Code documents a concurrency cap (1–256 for workflow fan-out) and Gemini CLI a per-subagent `maxTurns`; the rest MISSING. A verify layer sized without a known cap is sized blind, which is how the 154-agent run happened. → H1.

### What shipped

| # | Trace | Edit |
|---|---|---|
| H1 | T1, T4 | `references/workflow-patterns.md` (new) — "dynamic workflow" defined harness-neutral: units → lanes/subagents, pipeline vs barrier, a verify layer that refutes and is sized to stakes and to the documented cap, converge as the meeting point (`convergence.md`), resume from a run id where the harness offers it (run ledger as the resume state where it does not), caps and cost (`lane-plan.md`, the 154-agent lesson); the binding table per harness; the coordinator-as-pipeline rule declared in the Plan Block |
| H2 | T1, T3, T4 | `references/harness-map.md` (new) — the four things every run needs in harness-neutral prose (instruction file, skill folder and trigger, dynamic-workflow primitive, session stop); one table row per harness exactly as researched, every cell carrying its source, MISSING kept MISSING; shared ground; the three facts to establish before a first run on an unlisted harness |
| H3 | T2 | `SKILL.md` §5 — "session stop" is the generic term; `/goal` named as Claude Code's form, Copilot's autopilot the nearest elsewhere, the UAT column the stop where the harness has none |
| H4 | T1 | `SKILL.md` §3 — engine rows renamed inline · subagent fan-out · dynamic workflow · harness-operator, the dynamic-workflow row binding per harness via the two new references; the Workflow opt-in note kept and stated as Claude Code's binding |
| H5 | T2 | `SKILL.md` §2 — Ground's reading list gains the harness row you are running in; References list gains both new files with one-line purposes |

### Verdict: `PENDING`

Authored from one research pass; no run outside Claude Code has used the map yet.

**Validation list — what would move this to KEEP:**
- First real run in a non-Claude harness exercises the map without new friction.
- A coordinator-pipelined run states the fact in its Plan Block and the stages hold: dispatch, await, acceptance, next stage.
- Every harness fact used in a run comes from the map or from a fresh sourced fetch; no MISSING cell gets filled by guesswork.
- An unlisted harness gets its three facts established before the first run, and the run composes without editing this skill.
- A Copilot autopilot run ends at the UAT column rather than at the continuation limit, or the limit is raised knowingly in the Plan Block.

**What to watch:** the map's rows carry a fetch date of 2026-09-16 and harness docs move; re-fetch before trusting a MISSING verdict as still-MISSING. Whether "the coordinator is the pipeline" holds past three stages or degrades into the coordinator doing units inline (Evolution 2's H1 failure mode).
