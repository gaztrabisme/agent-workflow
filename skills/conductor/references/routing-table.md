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

Everything above routes on **work shape**. The table below routes on something else entirely.

## Carrier and capability skills — the second axis

A deck is not a kind of work. It is the **form an artifact takes**, and the skill that owns the form is chosen independently of the skill that decides the content. `dev` already names this split for its own execution-layer companions ("not pipeline stages — skills dev *calls into* mid-build"); conductor generalises it.

**Two rules:**

1. **Choose the carrier in the Plan Block, not at the end.** "We'll turn it into a deck later" is false — knowing the output is 12 slides changes what the producers write. Carrier chosen late means the content gets rewritten.
2. **A carrier skill never decides content.** `pptx` owns how the deck is built; `solution-architect` owns what it says. When a carrier skill starts making substantive calls, the routing was wrong.

| The artifact is… | Skill |
|---|---|
| a slide deck | `pptx` |
| a Word document | `docx` |
| a local spreadsheet (`.xlsx` / `.csv`) | `xlsx` |
| a Google Sheet (over the network, acts as you) | `gsheets` — **not** `xlsx` |
| a diagram as a file (`.drawio`, exported PNG/SVG) | `drawio` |
| **any** chart, plot, dashboard or stat tile, in any medium | `dataviz` — read **before** the first line of chart code |
| a published web page on claude.ai | `Artifact` + `artifact-design`; diagrams → `artifact-diagramming`; live/stateful → `artifact-capabilities` |
| generated stills, clips, or synthetic training data | `media-gen` |

**Frontend work has five overlapping skills. Pick on two axes, never one:**

| Axis | Choice |
|---|---|
| **Workflow** | new build → `frontend-design` (or `design-taste-frontend` for landing/portfolio) · existing UI → `redesign-existing-projects` (audit-first) |
| **Aesthetic direction** | `high-end-visual-design` (agency, expensive-feeling) · `minimalist-ui` (editorial, warm monochrome, flat) |

One workflow skill **plus** one direction. Loading two directions produces a hybrid that reads as neither. `color-expert` fires beneath any of them when the task is genuinely about colour — palettes, ramps, perceptual matching, accessibility.

**Capability skills, fired by substrate not by shape:**

| Trigger | Skill |
|---|---|
| the LLM call is **local** (MLX / oMLX / Apple Silicon) | `omlx` — owns the request contract, schema enforcement, thinking control |
| the LLM is **Anthropic**, or the task is LLM-shaped with the provider unstated | `claude-api` — read before opening the file. **Stands down** the moment another provider is named (OpenAI, Gemini, Deepseek, Llama, Mistral, Ollama) |
| Zalo OA / Mini App / ZNS / quota / pricing facts | `zalo-platform` — grounds the facts; `dev` builds against them |
| third-party API docs needed | `get-api-docs` |
| authoring or hardening a skill | `skill-builder` |

**Ambiguity rule, same as above:** name both candidates in the Plan Block and pick one with a reason. A carrier chosen silently is the cheapest routing error to make and the most annoying to undo.

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
