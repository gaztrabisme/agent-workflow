# Composition with sibling skills

The four presale/build skills form a pipeline. Each is narrow and well-triggered on purpose; they compose by hand-off, not by merger.

```
business-intelligence → ms-ai-discovery → solution-architect → dev
 (know the client)      (scope use cases)   (architect + respond)  (build)
```

`solution-architect` is the connective tissue: it turns *intel* and *scoped use cases* into a *buildable, sellable solution*, then feeds the *build*.

## ← From `business-intelligence` (inputs)
What it produces that SA consumes:
- Client profile, decision-makers, **political layer** → SA Phase 1 (Frame): sponsor, evaluation criteria.
- Competitor context, capability map, verified claims → SA Phase 5: **win themes** and honest positioning.

When to switch *to* BI mid-SA: you hit a research gap — you need to *know* something about the client/market/competitor you can't answer. Get the intel there, return to architect with it.

## ← From `ms-ai-discovery` (inputs, Microsoft-specific)
What it produces that SA consumes:
- BXT-scored use cases, agentic journey map, ROI baseline → SA Phase 2–3.
- When the deal **positions Microsoft**: use its `references/commercial_framing.md` (Azure Accelerate tiers, partner path) and stack guidance instead of re-deriving in SA.

Boundary: ms-ai-discovery is *Microsoft-flavored and workshop-scoped*. SA is *vendor-neutral and covers the no-workshop path* (straight from an RFI/RFP). If there's no workshop, SA does its own framing/clarify (Phases 1–2) without it.

## → Downstream: four consumers, not one

SA has never had a single downstream. Naming only `dev` is how an artifact built for engineers gets handed
to someone who needed a different shape entirely.

| Consumer | Consumes | Shape it needs | Strip before handing over |
|---|---|---|---|
| **`dev`** (build) | architecture, decision records, NFRs, traceability | spec + contracts + success criteria | commercial framing, win themes |
| **PM / delivery planner** *(pre-signature)* | the WBS as a **collection instrument** — task rows, disciplines, release buckets | spreadsheet; **effort column empty** for them to fill | cut order, risk narrative, scope defence |
| **Commercial / bid owner** | cost drivers, envelope, exclusions | priced attachment | architecture detail |
| **Client evaluator** | the response | narrative, tight | everything internal |
| **`delivery`** *(on signature)* | estimate, roadmap, acceptance annex, obligation register, risk register, **the ID spine** | the baseline it will track against | nothing — this is the full handover |

**The pre-signature PM is the one the skill kept missing.** They own the release split and the staffing
plan, and both are *their* decisions. An architect who arrives with the effort column already filled has
answered a question that wasn't his and silently allocated work to a team nobody has named. Enumerate the
work; let the disciplines price it. Full spec: `templates/delivery-wbs-workbook.md`.

Distinguish by **tense**, per `delivery`'s own rule: an estimate being *derived* → SA. An estimate being
*measured against* → `delivery`.

### To `dev` specifically
- Accepted reference architecture + **decision records** (with rejected options) → dev Design-mode input.
- NFRs + constraints + residency → dev's non-functional design and gates.
- Requirements-traceability matrix → dev's coverage check / backlog seed.
- Seed the project `AGENTS.md` and `wiki/` (per `../../core/references/wiki-protocol.md`) so the build starts with everything presale learned.

## SA vs dev/Design — the disambiguation

Both trigger on "design/architect." Decide on **artifact + audience**:

| | solution-architect | dev / Design mode |
|---|---|---|
| Audience | the **client** (evaluator, buyer) | the **engineering team** |
| Artifact | solution architecture, options analysis, **RFI/RFP/proposal**, traceability, win themes | implementation **spec**, data models, contracts, success criteria, test plan |
| Stance | vendor-neutral, then positioned; commercial-aware | implementation-committed; code-bound |
| Output of | a *winnable response* | a *buildable spec* |
| Lifecycle stage | presale | build |

Rule of thumb: if the work product goes **to the client to win the deal**, it's SA. If it goes **to engineers to build the thing**, it's dev/Design. The hand-off point is "we won / it's approved — now build it."

### Name collision: the `business-intelligence` *skill* vs "BI" as a *capability*
A client requirement may ask for "Business Intelligence / data visualisation" (e.g. Power BI dashboards). That is a **solution element** you architect and `dev` builds — it has nothing to do with the `business-intelligence` *skill*, which is client/market *research*. Don't invoke the research skill because the word "BI" appears in a requirement; treat the BI/reporting capability as part of the solution.

## Reuse, don't duplicate
SA deliberately **reuses the `core` kernel by reference** rather than copying it:
- `../../core/references/wiki-protocol.md` — project memory & Output Contract.
- `../../core/references/pushback-and-teach.md` — the challenge-before-execute gate.
- `../../core/references/grounding-gate.md` — the grounding gate (KB is SA's tech-layer substrate).
- `../../core/references/evolution-loop.md` — the harvest→apply→validate loop behind SA's `EVOLUTION.md`.

If a piece of guidance belongs to *all* skills, it lives in `core` and the others point at it. Keep SA focused on what's unique: client-facing solution architecture and the winning response. (`dev` is the *build* stage SA hands off to — a peer consumer of `core`, not SA's kernel.)
