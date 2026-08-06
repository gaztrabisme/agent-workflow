# Routing Table

Intent → skill → mode. Conductor's only original judgment. Everything downstream belongs to the skill named in the third column.

## The table

| The user says (roughly) | Shape | Route |
|---|---|---|
| "build X", "add feature", "fix", "implement", "refactor" | Build | `dev` → Build mode. Board project → `harness-operator` instead. |
| a list of features / a backlog | Build | `dev` → Design → Sprint. >6 items on a board project → `harness-operator`. |
| "assess", "audit", "code health", "why is this slow" | Build | `dev` → Assess / Analyze |
| "train", "finetune", "run the experiment", "evaluate the model" | Build | `dev` → Train |
| "I have an idea", "how would we", "spec this" — **for engineers** | Frame | `dev` → Design |
| "proposal", "RFP", "what do we pitch", "architecture for the client" | Frame | `solution-architect` |
| "scope the AI use cases with them" (Microsoft-shaped) | Frame | `ms-ai-discovery` → hands to `solution-architect` |
| "who is this client", "competitors", "will they buy", "build the case" | Ground | `business-intelligence` |
| "validate", "is this true", "what does it actually cost", "check my numbers" | Ground | task-force fan-out — `task-force-protocol.md` |
| "pressure-test", "what breaks", "red team", "will this survive the room" | Contest | persona fan-out — `persona-fanout.md` |
| "status", "are we on track", "they want a change", "get it accepted" | Run | `delivery` |
| local LLM call, schema enforcement, thinking control | — | `omlx` |
| generated stills/clips/synthetic data | — | `media-gen` |
| Zalo OA / Mini App / ZNS / quotas / pricing | — | `zalo-platform` |
| deck / doc / spreadsheet as the deliverable | — | `pptx` / `docx` / `xlsx` / `gsheets` |

## Disambiguation — the three collisions that actually happen

These are already resolved by the siblings. Conductor applies their rule; it does not invent a fourth.

1. **`dev`/Design vs `solution-architect`** — decide on **artifact + audience**. Internal spec, data model, success criteria for code → `dev`. Client-facing solution, proposal, tech selection to win a deal → `solution-architect`.
2. **`solution-architect` vs `delivery`** — decide on **tense**. Criteria being *negotiated* → SA. Criteria being *tracked to sign-off* → delivery. Estimate being *derived* → SA. Estimate being *measured against* → delivery. (One exception, SA's own: pre-signature effort numbers are authored by delivery, because whoever will be held to an estimate owns writing it.)
3. **`dev` vs `harness-operator`** — decide on **board**. If the project's `CLAUDE.md` declares `HARNESS_DB`, multi-ticket build work runs through the harness and `dev` is the judgment *inside* each ticket. Never run both spines over the same work.

   **No board is not an answer — it is a question.** Substantial build work (multi-ticket, or a spec heading into a build phase) on a boardless project → **propose onboarding in the Plan Block**, don't fall through to `dev` and never mention it again. Falling through silently is how a project runs its whole build outside the spine by default. The onboarding is three steps (`harness-operator` → Project onboarding) and the qualifying question is whether the mutation gate will be real: a Python/Rust project with a test runner gets a genuine gate; a JS/TS-only diff gets an honest skip, so the oracle carries the whole load and onboarding buys less. One-off fixes and single-file work stay on `dev` — the board is for work that has tickets.

**When genuinely ambiguous, name both in the Plan Block and pick one with a reason.** Silent choice between two siblings is how the wrong artifact gets built well.

## Compose-order for multi-shape requests

Most real intents carry several shapes. Order them by what constrains what — a later stage should never be re-run because an earlier one changed the premise.

```
Ground ──▶ Frame ──▶ Contest ──▶ Build ──▶ Run
 facts     decision   stress      code    engagement
```

- **Ground before Frame.** Deciding on unverified numbers means re-deciding. If the frame rests on a cost, a quota, a regulation, or a competitor claim, ground it first.
- **Contest after Frame, before Build.** A persona pass over a *decision* is cheap; over shipped code it is a rewrite. Contest the frame while it is still prose.
- **Build last, and only what Contest survived.**
- **Run wraps everything** on a signed engagement — `delivery` is concurrent, not sequential.

Two legitimate reorderings:
- **Probe-first.** An irreversible or expensive fork (hardware spend, schema lock-in, a long training run) gets the cheapest experiment that resolves it *before* the frame is finished. This is `dev`'s sim/probe-first pattern; conductor honours it.
- **Contest the brief itself.** When the ask is vague or hand-waves a tradeoff, the pushback gate fires *before* any stage — challenge, surface the fork, put it in `DECIDE NOW`. See `../../core/references/pushback-and-teach.md`.

## What conductor never routes

- **A one-line fix, a question, a lookup.** No Plan Block, no fan-out. Answer it.
- **Work the user routed themselves.** `/dev`, `/solution-architect` typed explicitly → stay out of the way.
- **Anything a sibling's gate reserves for a human.** `harness-operator`'s align / land / close are keystones; conductor announces them in the Plan Block and returns for them. That is not a mid-run stop — it was on the plan.
