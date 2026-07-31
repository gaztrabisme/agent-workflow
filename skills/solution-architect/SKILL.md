---
name: solution-architect
description: "Vendor-neutral Solution Architect lifecycle for presale — turn client requirements (an RFI/RFP, a discovery output, a brief) into a defensible solution architecture and a winning response. USE WHEN scoping or architecting a client solution, writing/reviewing an RFI/RFP/proposal/tender response, doing tech-stack options analysis and tradeoffs, defining non-functional requirements, building a requirements-traceability matrix, or phasing/sizing/risk-assessing a deal. Composes with business-intelligence (client intel), ms-ai-discovery (MS workshop scoping), and dev (the build). Keywords: solution architect, SA, RFI, RFP, proposal, tender, bid, solution architecture, reference architecture, tech stack selection, options analysis, tradeoff, NFR, non-functional, traceability matrix, presale, phasing, roadmap, sizing, estimation, win theme."
license: MIT
---

# Solution Architect

Turn a client's stated need — an RFI, an RFP, a workshop output, a one-line brief — into a **solution the client can buy and a team can build**. The output of this skill is an architecture and a response you can **defend in the evaluation room**: every requirement traced, every major choice justified against alternatives, every assumption stated, every non-functional risk named before the client finds it.

This is the connective tissue of the presale lifecycle. It sits *after* you know the client and *before* anyone writes code:

```
business-intelligence → ms-ai-discovery → [ SOLUTION-ARCHITECT ] ──signed──┬─→ delivery (run the engagement)
 (know the client)      (scope use cases,   (architect the solution        └─→ dev      (build it)
                         Microsoft-specific) + write the response)
```

It **consumes** client intel (from `business-intelligence`) and scoped use cases (from `ms-ai-discovery`, or directly from an RFI/RFP when there is no workshop), and **hands off** decisions to `dev` for the build.

## When this fires — and when a sibling owns it

- **This skill:** client-facing presale. RFI/RFP/proposal/tender response, solution & reference architecture, tech-stack options analysis, NFRs, traceability, phasing, sizing, risk, win themes. **Vendor-neutral by default.**
- **`business-intelligence` instead:** you need to *research* the client, competitors, stakeholders, or build the business case — the *inputs* to architecture, not the architecture.
- **`ms-ai-discovery` instead:** you're running a *Microsoft discovery/envisioning workshop* (BXT, Five Golden Questions, Discovery Cards) to scope use cases. SA consumes its output; when the deal positions Microsoft, SA *invokes* it for the MS lens rather than duplicating it.
- **`dev` (Design mode) instead:** the audience is the *engineering team*, not the client — implementation specs, data models, contracts, success criteria for code. SA stops at the architecture and the response; dev takes it into the build.
- **`delivery` instead:** the deal is **signed** and the work is now being run — baselining the estimate, tracking acceptance criteria to sign-off, chasing client obligations, pricing change requests, reporting status. SA *produces* the acceptance annex, obligations register, estimate, and ID spine; `delivery` baselines and tracks them. Decide on **tense**: criteria being *negotiated* → SA; criteria being *tracked to sign-off* → delivery.

> **Disambiguation rule:** both SA and dev/Design trigger on "design/architect." Decide on **artifact + audience**. Client solution / proposal / tech selection → **SA**. Internal spec / data model / feature implementation → **dev/Design**.

## Anchoring principles

1. **Problem before solution — always.** The dominant failure mode (Microsoft's own data: ~80% of AI projects) is architecting the wrong thing well. Nail the business outcome, the decision criteria, and the constraints *before* drawing a box. A diagram produced before the problem is understood is a liability.
2. **Vendor-neutral first; positioning is a separate, explicit step.** Architect to the requirement, then position a stack against it with tradeoffs shown. Never let the preferred vendor pick the architecture. (When Microsoft is being positioned, pull the MS lens from `ms-ai-discovery`.)
3. **Show the tradeoff, then recommend.** Single-option architecture is not architecture — it's a guess with confidence. Present 2–3 viable options on the axes that matter to *this* client, then recommend one and say why the others lost.
4. **NFRs kill more deals than features.** Security, scale, data residency, compliance, availability, cost-at-scale — these are where credibility is won or lost in regulated/enterprise deals. Treat them as first-class, early.
5. **Trace everything.** Every client requirement maps to a solution element and a delivery phase. A requirements-traceability matrix is the proof of coverage; gaps you find are clarification questions, not silent omissions.
6. **State assumptions; don't fabricate certainty.** Anything you can't confirm becomes an explicit assumption in a register, framed so you can proceed and the client can correct. Don't overconfident-consult — build escape hatches, flag uncertainty, and know the negative space.
7. **Clarification questions are a positioning instrument, not just intake.** A sharp domain question signals mastery; a pile of logistics questions signals juniority. Ask what only the client can answer; decide or route the rest. (See `references/rfi-rfp-response.md`.)
8. **Win themes map to *their* evaluation criteria, not your feature list.** "Why us" must answer how the client will actually score the bid.

## The SA lifecycle (at a glance)

| Phase | Goal | Primary artifact |
|-------|------|------------------|
| **0. Intake** | Turn an informal dump (site visit, conversation, chat scroll) into a structured frame + ranked asks. Tier fact vs inference; name the negative space; collapse "opportunities" into candidate projects. | Engagement frame + ≤5 asks + proposed deliverables |
| **1. Frame** | Understand the real problem, decision criteria, constraints, and what "winning" means. Challenge the brief. | Engagement frame (problem, sponsor, eval criteria, constraints) |
| **2. Clarify** | Extract & disambiguate requirements; produce clarification questions + assumptions register. | Clarification questions + assumptions register |
| **3. Architect** | Options analysis → reference architecture; integration, security, residency, NFRs. | Solution architecture doc + options/decision records |
| **4. Plan** | Phasing/roadmap, sizing/estimation inputs, risk register, commercial framing inputs. | Phased roadmap + risk register + sizing inputs |
| **5. Respond** | Assemble the RFI/RFP/proposal: exec summary, solution narrative, traceability matrix, win themes. | The response document + traceability matrix |
| **6. Contract & Acceptance** | Convert an accepted proposal into criteria that gate payment and obligations that bound schedule risk. *(Fixed-price shape, and any bid you win.)* | Acceptance annex + client-obligation register |
| **7. Handoff** | Convert accepted decisions into build inputs for `dev`; record what binds the build. | Decision records + build-ready brief |

Full method, checklists, and templates per phase: `references/sa-lifecycle.md`. Don't run every phase heavyweight — scale to the deal (a one-pager RFI clarification ≠ a multi-week RFP). Start light; add depth only where the deal's risk demands it.

**Pick the deal shape before reaching for machinery.** An *enterprise bid* (scored RFI/RFP, requirement refs, blueprint workbook, blended-rate pricing) and a *fixed-price delivery* engagement (acceptance-criteria spine, obligation register, lump sum + CapEx) need different instruments. Declare it in Phase 0: `references/deal-shapes.md`. Applying one shape's machinery to the other is how this skill generates ceremony instead of leverage.

**Then declare the recipient — it is a second axis, not a detail.** Shape says what the deal is; it does not say who picks the artifact up next or what they decide with it. One line, beside the shape: `Recipient: <role> — decides <what> — therefore the primary artifact is <shape>`. A correctly-shaped artifact aimed at the wrong reader still gets rejected. See `references/deal-shapes.md` §Axis 2.

## Gates (declared, not skipped)

These are inherited from the `core` kernel so the discipline is consistent across every role. On entry, read the referenced files.

- **Pushback gate.** If the brief is vague, business-level, or hand-waves a tradeoff, *challenge before architecting* and surface the decision. Narrate the WHY in the final response. See `../core/references/pushback-and-teach.md`.
- **KB Grounding gate.** When a decision touches a KB-covered domain (ML/RAG, RAG-evaluation, multilingual NLU, databases, security, distributed systems, cryptography), search the Knowledge Base first and record one line: `KB: searched "<q>" → applied <finding>` or `→ nothing relevant`. A silent skip on a covered domain is a gate violation. (The general gate — and its substrate-by-role table and honesty corollary — is in `../core/references/grounding-gate.md`; for SA the tech-layer substrate is the KB.)
- **Approach declaration.** Before substantive work, state in one line how you'll run it: `Approach: <single-architect | options-panel | research-first | fan-out over requirements> — <reason>`. For wide solution spaces, generate independent options and compare; for unknowns, research first; for big multi-requirement RFPs, fan out coverage and merge. *Skippable for a single-actor engagement (one architect, a small RFI clarification) — declare only when the work fans out or forks.*
- **Output Contract.** A phase is not done until its artifact exists on disk and is captured in the project wiki. See "Artifacts & Output Contract" below and `../core/references/wiki-protocol.md`.
- **Ask ledger.** Restate the ask verbatim, then list the artifacts you will produce against it. **Anything beyond the ask is *proposed*, not produced** — with a named consumer and the decision it serves. Research that changes the build is a *findings list*, not a paper. The failure this closes is real: an engagement asked for a scope list and an estimate, and received eleven documents totalling 22,400 words; the owner's report was *"I'm lost in the middle — I thought we just need to make a WBS?"* Volume also defeats `artifact-integrity.md`, whose reconciliation cost grows with the square of the artifact count.

## Anti-patterns (hard no-list)

- **Tech-first framing** — an architecture diagram before the problem, criteria, and constraints are nailed.
- **Single-option architecture** — no alternatives, no tradeoff, no defensible "why this."
- **NFRs as an afterthought** — security/residency/compliance/scale bolted on at the end of the response.
- **Line-by-line feature matching** — answering each RFI clause with no overarching solution narrative or win theme.
- **Asking the client what you can decide** — burning clarification goodwill on logistics or convention questions. Route or decide them.
- **Promising maturity you don't have** — claiming capability/experience that won't survive due diligence. Score feasibility honestly.
- **Untraced coverage** — claiming "full coverage" without a matrix that proves it.
- **Vendor-led design** — picking the architecture to suit the stack you want to sell.

## Composition with sibling skills

- **From `business-intelligence`:** client profile, decision-makers & political layer, competitor context, capability map, verified claims → feed Phase 1 (Frame) and Phase 5 win themes. Full handoff in `references/composition.md`.
- **From `ms-ai-discovery`:** BXT-scored use cases, agentic journey map, ROI baseline → feed Phase 2–3. When positioning Microsoft, use its stack/commercial-framing references instead of re-deriving them.
- **To `dev`:** accepted architecture + decision records + NFRs + traceability → become the Design-mode input and the project `AGENTS.md`/`wiki/` for the build.
- **To `delivery` (on signature):** the estimate, phased roadmap, acceptance annex, client-obligation register, risk register, and the declared **ID spine** → become the delivery baseline and its trackers. `delivery` runs for the whole engagement with `dev` cycling inside it.
- **Back from `delivery` (at close-out):** estimate vs actual per phase, which criteria were contested and why, which client obligations slipped. This is the highest-value correction signal `references/estimation-and-costing.md` and `references/acceptance-and-contract.md` will ever receive — a criterion that caused a dispute was written ambiguously here.

## Artifacts & Output Contract

Every SA engagement, at minimum, writes its result to the project wiki (`wiki/` per `../core/references/wiki-protocol.md`) — append a dated `log.md` entry and keep `active-work.md` current. Beyond that floor, the **primary artifacts** are:

| Artifact | Consumer | Lives in | Purpose |
|----------|----------|----------|---------|
| Engagement frame | **SA (internal)** — never shipped | `docs/` | Phase 0 output: the problem, buyer, trigger, constraints, negative space, candidate projects — tiered fact vs inference. The thing every later choice is checked against. |
| Clarification questions + assumptions register | Client | `docs/` | What only the client can answer; what we assume in the meantime. |
| Client-obligation register | Client · `delivery` | `docs/` | What the *client* must deliver, by when, to whom — the schedule risk the assumptions register doesn't hold. *(Delivery shape.)* |
| Acceptance annex | Client · `delivery` | `docs/` | The criteria that gate payment, with per-criterion preconditions and preparing party. *(Delivery shape.)* |
| Solution architecture doc | Client · `dev` | `docs/` | Reference architecture, integration, security, residency, NFRs. |
| Options/decision records | SA · `dev` | `wiki/decisions.md` | Each major choice: alternatives, why the rest lost, what it binds. **Record rejected approaches.** |
| Requirements-traceability matrix | Client | `docs/` | Every requirement → solution element → phase. Proof of coverage. |
| The response (RFI/RFP/proposal) | Client evaluator | `docs/` | The client-facing deliverable. |
| **Delivery WBS (instrument)** | **PM / delivery planner** | `docs/` | **The task inventory they price and staff from — enumerate the work, ship the effort column empty.** Its absence from this table is why an eight-sheet scope-defence workbook got handed to a PM who needed a task list. Spec: `references/templates/delivery-wbs-workbook.md`. |

**Close-out before "done":** artifact on disk · `wiki/log.md` entry · `decisions.md` updated with choices *and* rejected options · assumptions register reflects open items · traceability matrix has no silent gaps · **Final QA pass run on every client-bound export** (label/content alignment, internal-comment strip, totals/conversion recompute, numbering walk — full 6-item list in `references/rfi-rfp-response.md`) · **artifact-integrity checks run across the artifact set** (count reconciliation, dangling spine refs, orphans, version lineage, language parity, priced-vs-committed — `references/artifact-integrity.md`). The two passes catch different defects; running one is not running the other.

> On a live multi-round engagement, the matrix, register, questions, risks, WBS and roadmap converge into a single **blueprint workbook** with a cell-level change log — see `references/blueprint-workbook.md`.

## References

- `references/sa-lifecycle.md` — the 8 phases in depth: methods, checklists, per-phase templates.
- `references/deal-shapes.md` — enterprise bid vs fixed-price delivery: which spine, carrier, and pricing chain apply. Read before reaching for a workbook or a multiplier.
- `references/engagement-intake.md` — Phase 0, the front gate: statement tiering, the frame slots, the negative space, opportunity→project promotion, the sensitive-inference handling rule.
- `references/artifact-integrity.md` — the cross-artifact consistency checks: one ID spine, count reconciliation, dangling refs, orphans, version lineage, language parity, priced-vs-committed.
- `references/acceptance-and-contract.md` — Phase 6: acceptance criteria as the spine, the client-obligation register, and the commercial risk-transfer terms that must land before signature.
- `references/blueprint-workbook.md` — the living spreadsheet that carries a multi-round engagement: sheet inventory, the answer-folding loop (client answers → every touched sheet + change log), scope-treatment vocabulary, phase naming in the client's outcome language.
- `references/estimation-and-costing.md` — WBS→price chain: uncertainty-driver column, effort-distribution multiplier, per-environment cloud-cost workbook (dominant meter flagged, BYOL exclusions), AMS tiers + retainer floor, pre-ship sanity checks.
- `references/tech-selection.md` — options-analysis method, tradeoff-table template, decision records, neutral-then-position.
- `references/nfr-checklist.md` — the non-functional requirements catalog with forcing questions (security, scale, performance, residency, compliance, availability, observability, cost).
- `references/rfi-rfp-response.md` — response anatomy, clarification-question discipline, assumptions register, win themes, traceability.
- `references/composition.md` — exact hand-offs to/from `business-intelligence`, `ms-ai-discovery`, `dev`, and the SA-vs-dev/Design disambiguation.
- `references/templates/rfi-rfp-response-template.md` — fill-in skeleton for a full RFI/RFP/proposal response (generalised from a real enterprise AI RFI), with traceability matrix, options table, and assumptions register built in.
- `references/templates/engagement-frame.md` — the Phase-0 fill-in: frame slots with tiers, negative space, candidate-project promotion test, sensitive-inference handling, and the four-part handback.
- `references/templates/clarification-questions.md` — two-bucket question template (ask-the-client vs resolve-internally) with paired working-assumption, **impact-if-wrong**, and **serves-criterion** columns.
- `references/templates/assumptions-register.md` — standalone assumptions-register (a primary artifact); pairs 1:1 with the clarification questions.
- `references/templates/client-obligations-register.md` — what the client must deliver, by a schedule-relative deadline, with a named focal point; pre-seeded with the contract terms that cost money to fix after signature.
- `references/templates/delivery-wbs-workbook.md` — the WBS as a **collection instrument** for a delivery planner: column spec, the effort column shipped **empty**, formula-driven summary, capacity sheet, two-direction traceability.
