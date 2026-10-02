# Routing Table

Intent → skill → mode. Conductor's only original judgment. Everything downstream belongs to the skill named in the third column.

## The table

| The user says (roughly) | Shape | Route |
|---|---|---|
| "plan the next programme run", "coordinate these stages", or an unrouted multi-step task needing coordinated stages | Coordination | `conductor` → classify, ground, compose, plan, and coordinate. If the request is specifically to improve an existing skill from its traces, route to `evolution`; if it is to create, split, or publish a skill, route to `skill-builder`. |
| "build X", "add feature", "fix", "implement", "refactor" | Build | `dev` → Build mode. Board project → `harness-operator` instead. |
| a list of features / a backlog | Build | `dev` → Design → Sprint. >6 items on a board project → `harness-operator`. |
| "assess", "audit", "code health", "why is this slow" | Build | `dev` → Assess / Analyze |
| "train", "finetune", "run the experiment", "evaluate the model", "which model", "what metric", "design the eval", "why does it score well but behave badly" | **Model** | `applied-ml-problem-solver` (see § ML / model work below — `dev` has no Train mode; it moved here 2026-09-17) |
| "I have an idea", "how would we", "spec this" — **for engineers** | Frame | `dev` → Design |
| "proposal", "RFP", "what do we pitch", "architecture for the client" | Frame | `solution-architect` |
| "scope the AI use cases with them", "run a discovery workshop" | Frame | `ai-discovery-workshop` → hands to `solution-architect` |
| a solution spanning disciplines — architecture *and* delivery shape *and* backend *and* UI | Design | design cell — `design-cell.md` |
| the same, but one discipline could hold the whole design | Design | `dev` → Design directly. **No cell** — see `design-cell.md` §When it fires |
| "who is this client", "competitors", "will they buy", "build the case" | Ground | `business-intelligence` |
| "validate", "is this true", "what does it actually cost", "check my numbers" | Ground | task-force fan-out — `task-force-protocol.md` |
| "pressure-test", "what breaks", "red team", "will this survive the room" | Contest | persona fan-out — `persona-fanout.md` |
| "status", "are we on track", "they want a change", "get it accepted" | Run | `delivery` |
| "evolve my skills", "meta session", "improve the skill", "what have we learned" | Meta | `evolution` — triages the whole constellation and runs the loop on what has traces. Target-less by design; don't pre-pick the skill for it. |
| "build me a skill", "split this skill", "publish it" | Meta | `skill-builder` — birth and shape. Evidence-driven change to a working skill is `evolution` instead. |

Everything above routes on **work shape**. The table below routes on something else entirely.

## Carrier and capability skills — the second axis

A deck is not a kind of work. It is the **form an artifact takes**, and the skill that owns the form is chosen independently of the skill that decides the content. `dev` already names this split for its own execution-layer companions ("not pipeline stages — skills dev *calls into* mid-build"); conductor generalises it.

**Two rules:**

1. **Choose the carrier in the Plan Block, not at the end.** "We'll turn it into a deck later" is false — knowing the output is 12 slides changes what the producers write. Carrier chosen late means the content gets rewritten.
2. **A carrier skill never decides content.** `pptx` owns how the deck is built; `solution-architect` owns what it says. When a carrier skill starts making substantive calls, the routing was wrong.

**Project route override.** If a current project decision retires or replaces a carrier or capability skill, follow that decision for this project and name the override and decision in the Plan Block's `ROUTE` row. Keep the default route intact for other projects. (derived: dogfood 2026-10-01)

| The artifact is… | Skill |
|---|---|
| a slide deck | `pptx` |
| a Word document | `docx` |
| a local spreadsheet (`.xlsx` / `.csv`) | `xlsx` |
| a Google Sheet (over the network, acts as you) | `gsheets` — **not** `xlsx` |
| a diagram as a file (`.drawio`, exported PNG/SVG) | `drawio` |
| **any** chart, plot, dashboard or stat tile, in any medium | `visualize` — consult it **before** the first line of chart code |
| a published web page on claude.ai | `Artifact` + `artifact-design`; diagrams → `artifact-diagramming`; live/stateful → `artifact-capabilities` |
| generated stills, clips, or synthetic training data | `media-gen` |

**Frontend work** (web pages and apps: semantic HTML, CSS, TypeScript, the project's framework, accessibility, performance, agent-ready affordances, render-and-check) → `frontend`. It covers both a new interface (its greenfield path) and an audit-first redesign of an existing one; the owner's `brand-profile` supplies the visual direction when the work is the owner's own. `color-theory` fires beneath it when the task is genuinely about colour: planning or critiquing an image's colour with the course method, palettes, ramps, perceptual matching, accessibility. It carries the old `color-expert` library inside it as its science layer.

`visual-design` fires the same way for form: planning, making or critiquing a graphic, poster, editorial page, presentation, package, campaign or visual identity — composition, visual hierarchy, negative space, Gestalt, balance, grids, typography, identity systems, visual weight.

| The decision is about… | Route |
|---|---|
| colour | `color-theory` |
| composition and form | `visual-design` |
| charts, infographics, dashboards and data stories: reader, chart choice, encoding, annotation, narrative | `information-design` |
| product UX and interface words: research, scope, flows, wireframes, microcopy, empty/error/status states | `ux` |
| motion: animated explainers, animated infographics, storyboards and animatics, easing and choreography (rendered by `scene-engine`) | `motion` |

**Boundary by artifact:** colour choices → `color-theory`; composition and form → `visual-design`; what a chart or dashboard shows and how it reads → `information-design`; what a screen asks of its user and what it says → `ux`.

**Capability skills, fired by substrate not by shape:**

| Trigger | Skill |
|---|---|
| the LLM call is **local** (MLX / oMLX / Apple Silicon) | `omlx` — owns the request contract, schema enforcement, thinking control |
| the LLM is **Anthropic**, or the task is LLM-shaped with the provider unstated | `claude-api` — read before opening the file. **Stands down** the moment another provider is named (OpenAI, Gemini, Deepseek, Llama, Mistral, Ollama) |
| Zalo OA / Mini App / ZNS / quota / pricing facts | `zalo-platform` — grounds the facts; `dev` builds against them |
| the artifact is **in Vietnamese**, at any level of formality | `vietnamese-copywriter` — owns register, calques and the cold-read gate; the carrier skill still owns the file |
| third-party API docs needed | `get-api-docs` |
| authoring or hardening a skill | `skill-builder` |

**Ambiguity rule, same as above:** name both candidates in the Plan Block and pick one with a reason. A carrier chosen silently is the cheapest routing error to make and the most annoying to undo. [book:software-engineering-at-google], Identify the Key Trade-Offs.

## Disambiguation — the three collisions that actually happen

These are already resolved by the siblings. Conductor applies their rule; it does not invent a fifth.

1. **`dev`/Design vs `solution-architect`** — decide on **artifact + audience**. Internal spec, data model, success criteria for code → `dev`. Client-facing solution, proposal, tech selection to win a deal → `solution-architect`.
2. **`solution-architect` vs `delivery`** — decide on **tense**. Criteria being *negotiated* → SA. Criteria being *tracked to sign-off* → delivery. Estimate being *derived* → SA. Estimate being *measured against* → delivery. (One exception, SA's own: pre-signature effort numbers are authored by delivery, because whoever will be held to an estimate owns writing it.)
3. **`dev` vs `harness-operator`** — decide on **board**. If the project's `CLAUDE.md` declares `HARNESS_DB`, multi-ticket build work runs through the harness and `dev` is the judgment *inside* each ticket. Never run both spines over the same work.

   **No board is not an answer — it is a question.** Substantial build work (multi-ticket, or a spec heading into a build phase) on a boardless project → **propose onboarding in the Plan Block**, don't fall through to `dev` and never mention it again. Falling through silently is how a project runs its whole build outside the spine by default. The onboarding is three steps (`harness-operator` → Project onboarding) and the qualifying question is whether the mutation gate will be real: a Python/Rust project with a test runner gets a genuine gate; a JS/TS-only diff gets an honest skip, so the oracle carries the whole load and onboarding buys less. One-off fixes and single-file work stay on `dev` — the board is for work that has tickets.

**When genuinely ambiguous, name both in the Plan Block and pick one with a reason.** Silent choice between two siblings is how the wrong artifact gets built well. [book:software-engineering-at-google], Identify the Key Trade-Offs.

## Compose-order for multi-shape requests

Most real intents carry several shapes. Order them by what constrains what — a later stage should never be re-run because an earlier one changed the premise.

**This is the canonical shape order. It is stated here and nowhere else** — a second copy is how the two files drift apart, which is the anti-pattern this skill inherits from `delivery` ("two numbering systems") turned on itself.

```
Ground ──▶ Frame ──▶ Design ──▶ Contest ──▶ Build ──▶ Run
 facts     what/      how, across   stress      code    engagement
           whether    disciplines
```

Most requests carry three or four of these, not six. Name the ones present; skip the rest out loud.

- **Ground before Frame.** Deciding on unverified numbers means re-deciding. If the frame rests on a cost, a quota, a regulation, or a competitor claim, ground it first. [book:facilitating-software-architecture], Questions That Improve Judgment Around Framing.
- **Frame before Design.** Frame settles *what and whether*; Design works out *how*. A cell that starts before the frame is settled designs a solution to a moving problem. [book:swebok], 5.3. Software Requirements Specification.
- **Design collapses to `dev`/Design when one discipline could hold it.** The cell is for work that would produce incompatible halves. Single-discipline work that runs a cell gets ceremony, not coverage.
- **Contest after Design, before Build.** A persona pass over a *spec* is cheap; over shipped code it is a rewrite. Contest it while it is still prose. [book:facilitating-software-architecture], When and How to Seek Advice.
- **Build last, and only what Contest survived.** Validate the requirements document before committing build resources. [book:swebok], 6. Requirements Validation.
- **Run wraps everything** on a signed engagement — `delivery` is concurrent, not sequential. [book:continuous-delivery], Principles of Software Delivery.

Two legitimate reorderings:
- **Probe-first.** An irreversible or expensive fork (hardware spend, schema lock-in, a long training run) gets the cheapest experiment that resolves it *before* the frame is finished. This is `dev`'s sim/probe-first pattern; conductor honours it. [book:facilitating-software-architecture], Spikes Can Tackle Architectural Variability More Cheaply.
- **Contest the brief itself.** When the ask is vague or hand-waves a tradeoff, surface the assumptions and fork before any stage, then put it in `DECIDE NOW`. See `../../core/references/pushback-and-teach.md`. [book:learning-systems-thinking], Modeling as a Core Practice.

## What conductor never routes

- **A one-line fix, a question, a lookup.** No Plan Block, no fan-out. Answer it. [book:pmbok-guide-7e], 3.7. Tailor Based on Context.
- **Work the user routed themselves.** `/dev`, `/solution-architect` typed explicitly → stay out of the way.
- **Anything a sibling's gate reserves for a human.** Announce the decision owner and reserved step in the Plan Block. Before escalating a decision beyond your authority, investigate alternatives and their impacts, then send the owner a recommendation. [book:pmbok-guide-7e], 2.2.4. Leadership Skills.


## ML / model work — the fourth collision

| Intent | Route |
|---|---|
| ML metric, problem framing, architecture, evaluation, retrieval, or inference-budget question | Consult the available skill and lane inventory and assign each plan step to the resource specialized for that work. When the request needs an ML problem or evaluation decision, route that decision to `applied-ml-problem-solver`. |
| Dataset, training script, API, or test implementation | Route the code unit to its implementation owner after the required model and evaluation decisions are framed. |

When implementation depends on a model or evaluation decision, settle that step first. Give the implementation owner the framed problem and its pre-registered evaluation gate; do not ask that owner to reframe the problem. [book:agentic-mesh], Specialization.

## When a route absorbs an existing collection

When a distilled skill absorbs a standalone knowledge collection, install the skill as the single entry point, unlink the old route by the transition date, update this routing table, and give the prior route owner the new skill name. A warning beside the old entry is not a migration plan; remove the competing entry point rather than relying on advisory deprecation. [book:software-engineering-at-google], Advisory Deprecation.
