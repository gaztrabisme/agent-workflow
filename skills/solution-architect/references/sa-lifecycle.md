# The SA Lifecycle — phases in depth

Scale each phase to the deal. A small RFI clarification may touch only Phases 1–2 and 5; a multi-week RFP runs the full set. Start light; add depth only where risk demands.

**Which machinery applies depends on the deal shape** — enterprise bid vs fixed-price delivery. Declare it in Phase 0 and read `deal-shapes.md` before reaching for a workbook or a pricing chain.

---

## Phase 0 — Intake (the front gate)

**Goal:** manufacture a formal input when there isn't one. Turn an informal dump — site-visit notes, a remembered conversation, a chat scroll — into a structured frame plus a short list of asks only the human can answer.

**Do:**
- **Take the whole dump before interrogating.** Interrupting for structure trains a filtered account, and the unfiltered one is where the negative space lives.
- **Tier every material claim** — Confirmed / Reported / Hearsay / Marketing / Inference / Speculation. Nothing changes tier silently; downstream artifacts inherit the tier.
- **Fill the frame slots** — outcome, baseline, economic buyer vs sponsor vs users vs blockers, trigger, decision process, hard constraints, relationship context, what winning looks like personally.
- **Name the negative space** — what would make us lose; what they *didn't* ask for; **who loses if this succeeds**.
- **Collapse opportunities into candidate projects.** A list of opportunities is zero projects. Promote only what has a named beneficiary, an observable outcome, an existing access path, and a definition of done; everything else is a parked lead with one named dependency.
- **Apply the sensitive-inference handling rule** to any inference that would damage the relationship if surfaced — internal-only, named holder, never in a shared artifact, never used as stated justification.
- **Declare the deal shape and the ID spine** (`deal-shapes.md`, `artifact-integrity.md`).
- **Declare the recipient** — `Recipient: <role> — decides <what> — therefore the primary artifact is <shape>` (`deal-shapes.md` §Axis 2). A correctly-shaped artifact aimed at the wrong reader still gets rejected.
- **Open the ask ledger** — the ask verbatim, the artifacts you will produce against it, and anything beyond it marked *proposed* with a named consumer and the decision it serves.

**Forcing questions:**
- What changes for the business, in their words, if this works — and what's the baseline?
- Why now? (No trigger usually means no budget.)
- Who releases the money, and who else can stop it?
- Who loses discretion if this succeeds?
- Which of these "opportunities" would I actually know how to finish?

**Hand back four things:** what you decided (and on what assumption) · ≤5 ranked asks only they can answer · proposed deliverables with dates · your pushback. Handing back a question list is a failure, not a deliverable.

**Artifact:** `docs/engagement-frame.md` (`templates/engagement-frame.md`). Method: `engagement-intake.md`.

**Skip when** the engagement genuinely starts from a formal document — but still run the tiering and negative-space steps on the surrounding context.

---

## Phase 1 — Frame (understand before architecting)

**Goal:** know the real problem, who decides, how they'll score, and what constrains the solution — before any box is drawn.

**Do:**
- Restate the problem in the client's business terms (outcome, not technology). If you can't, you don't understand it yet.
- Identify the **decision criteria**: how will the client actually evaluate responses? (cost, residency, domain experience, time-to-value, references, compliance). Win themes (Phase 5) map to these.
- Identify the **sponsor** and the political layer (pull from `business-intelligence` if available).
- Capture **hard constraints**: budget shape, residency, regulatory, existing stack, timeline, must-integrate systems.
- Classify the engagement: RFI (market scan — won't rank, may not reply) vs RFP (scored, binding-track) vs direct brief. This changes how aggressively you commit and how you use clarification questions.
- **If the RFI explicitly feeds a future RFP** (e.g. "we will issue an RFP based on refined requirements"), the highest-leverage goal is *shaping that RFP* — seeding requirements and criteria toward your differentiators. Treat the RFI response as influence, not just information. See `rfi-rfp-response.md` (RFI-feeds-RFP).
- **When the client publishes no decision criteria** (common in an RFI that "won't rank"), *infer* them from the problem statement, guiding principles, and domain — and state the inference. Win themes (Phase 5) then map to the *inferred* criteria (or the future RFP's), not to nothing. Don't claim to map to scoring that doesn't exist.
- **Source-integrity scan:** audit the client document itself. Real RFIs/RFPs are often copy-pasted from a prior solicitation — watch for duplicate requirement refs, contradictory figures, leaked out-of-scope sections, and a template that doesn't match the stated scope. Each is a clarification question or a stated convention, never a silent pass.

**Forcing questions:**
- What changes for the client's business if this works? What's the baseline today?
- Who signs, and what are they judged on? If no criteria are published, what *would* they be?
- What would make our response *lose*? (the negative space)
- What's genuinely fixed vs presented-as-fixed?
- Is the source document internally consistent (refs, figures, scope, template), or is it a copy-paste artefact I must flag?

**Artifact:** an engagement frame (problem · sponsor · evaluation criteria · constraints · engagement type).

---

## Phase 2 — Clarify (requirements + the unknowns)

**Goal:** turn a noisy requirement set into a structured one, with the gaps made explicit as questions or assumptions.

**Do:**
- Extract requirements into a working list; tag functional vs **non-functional** (run them against `nfr-checklist.md` — NFRs are usually under-stated in client docs).
- Separate **only-the-client-can-answer** (priorities, data, regulators, integration specifics, success metrics) from **we-can-decide / route internally** (logistics, document conventions).
- Draft clarification questions as a **positioning instrument** — business/domain first, logistics last or routed. See `rfi-rfp-response.md`.
- Open an **assumptions register** for everything unanswered, framed so you can proceed and the client can correct.
- On a multi-round engagement, host these in the **blueprint workbook** (`blueprint-workbook.md`) and run its **answer-folding loop** each time client answers arrive: fold each answer into every sheet it touches, move the question's status (TBC/Open → Partially Resolved → Resolved), rewrite its working assumption, and log the change with its source-answer reference.

**Artifact:** clarification questions (client-facing) + assumptions register — carried in the blueprint workbook on live engagements.

---

## Phase 3 — Architect (options → reference architecture)

**Goal:** a defensible reference architecture, chosen against alternatives, with NFRs and the hard cross-cuts (integration, security, residency) designed in.

**Do:**
- Run **options analysis** on the axes that matter to *this* client (see `tech-selection.md`). 2–3 viable options; recommend one; say why the rest lost.
- Draw the **reference architecture** in layers (channels/entry → app/orchestration → core capability → integration → data → security/governance). Written explanation is authoritative; diagrams illustrate. Recommended views: **context** (system in its environment), **component** (the layers), **data** (flow/lineage), **deployment** (regions/network/residency), and a **key-flow sequence** for the sensitive journeys. Use the `drawio` skill to produce them — diagrams are load-bearing when the client mandates an architecture demo.
- Design the **cross-cuts** explicitly using `nfr-checklist.md`: **integration** (its "Integration & API" section — patterns, gateway, resilience), identity & access, data residency, and the other NFRs. Integration is usually the bulk of the real work — don't hand-wave it.
- Ground domain decisions in the **KB** and record the line.
- Stay **vendor-neutral** until the positioning step; then map capabilities to a stack with tradeoffs.

**Artifact:** solution architecture doc + options/decision records (`wiki/decisions.md`).

---

## Phase 4 — Plan (phasing, sizing, risk)

**Goal:** a credible path from today to the outcome — de-risked, phased, and roughly sized.

**Do:**
- **Phase for value and risk:** lead with the lowest-risk, fastest-value slice (e.g. knowledge/FAQ before secure transactions). Each phase should stand on its own and de-risk the next.
- **Size honestly:** WBS, roles (on-site vs remote), rough effort. Don't precision-quote what you can't defend; give ranges and the assumptions behind them. Use the estimation chain in `estimation-and-costing.md`: WBS with a per-package **uncertainty-driver** column ("what narrows this to ±20%"), an explicit effort-distribution multiplier from build-MD to total-MD, a per-environment cloud-cost workbook with the dominant meter flagged, and AMS tiers with a retainer floor.
- **Reclassify what you can't commit or drop:** a demanded-but-risky capability (e.g. voice) can become a separately-priced *readiness-assessment track* with its own decision gate, and an unresolvable implementation choice can ship as *"in scope for design; approach TBC"* with the decision framed for the client. Full treatment vocabulary: `blueprint-workbook.md`.
- **Risk register:** technical, integration, data-availability, compliance, adoption risks — each with likelihood/impact, owner, mitigation.
- **Commercial inputs** — SA owns the *technical cost drivers and framing*; final pricing belongs to the deal's **commercial/bid owner** (a pricing/finance function, **not** the `business-intelligence` skill — that's client research). If the response document itself has pricing questions (itemised cost, lease/option terms, COTS vs bespoke, Year 1–5 maintenance, multi-year TCO), they *must* be answered or explicitly deferred to a labelled priced attachment — don't leave them blank. SA supplies: capex-vs-consumption shape, the cost levers (caching, tiering, model/quantization choices, license vs consumption), and what scales the bill.

**Artifact:** phased roadmap + risk register + sizing & commercial-driver inputs.

---

## Phase 5 — Respond (assemble the deliverable)

**Goal:** a response that proves coverage, tells a solution story, and answers the client's scoring criteria.

**Do:**
- Follow the client's required structure **exactly** (section order, numbering). If their template is wrong/mismatched, state your convention rather than asking permission.
- Lead with an **executive summary** that states the outcome and the win themes — not a feature dump.
- Include the **requirements-traceability matrix** (requirement → solution element → technology → phase) as proof of coverage.
- Weave **win themes** mapped to the Phase-1 decision criteria ("why us, in their terms").
- Fold in the **assumptions register** for anything unconfirmed — and note it can graduate to a *client-facing* "Project Dependencies" section in the deck (on a completed engagement the register was presented verbatim as two dependency slides; stating your assumptions openly reads as senior, not uncertain).
- Run the **Final QA pass** (`rfi-rfp-response.md`, full 6-item list) on every export — label/content alignment, internal-comment strip, totals/conversion recompute, numbering walk, date-coercion scan, version/date consistency — ideally by someone who didn't author the file.
- Run the **artifact-integrity checks** (`artifact-integrity.md`) *as well* — Final QA is within-document, integrity is across-artifact. Count reconciliation, dangling spine refs, orphans, version lineage, language parity, priced-vs-committed. Neither pass finds the other's defects.

**Artifact:** the response document + traceability matrix. See `rfi-rfp-response.md` for anatomy.

---

## Phase 6 — Contract & Acceptance (fixed-price shape, and any bid you win)

**Goal:** convert an accepted proposal into criteria that gate payment, obligations that bound your schedule risk, and contract terms you can live with for the whole delivery.

**Do:**
- **Author the acceptance criteria** as the engagement's ID spine — one per observable outcome, written in the observable and not the mechanism, each with its **preconditions to run the test** and the **preparing party**.
- **Open the client-obligation register** (`templates/client-obligations-register.md`): what the client must physically deliver, serving which criterion, by a *schedule-relative* deadline, with a **named** client focal point. Distinct from the assumptions register — an assumption you proceed on, an unmet obligation stops you.
- **Land the commercial risk-transfer terms before signature** — single authorized focal point, defect-severity definitions, the client's acceptance-response deadline, T0, numeric volume caps, change-request day rate, **standby rate for client-caused delay**, acceptance-council membership.
- **Run the loop until it converges:** criteria → preconditions → obligations → contract terms → back to what you can commit to. Every unclosed cycle is an argument scheduled for delivery.
- **Read the architecture-bearing clauses** against your own solution — acceptance & handover, change requests, IP, personal-data protection, limitation of liability.
- Re-run `artifact-integrity.md` before signature. Anything wrong here becomes contractual.

**Artifact:** acceptance annex + client-obligation register. Full treatment: `acceptance-and-contract.md`.

**Skip when** the engagement ends at submission (an enterprise bid you haven't won yet) — but revisit the moment it converts.

---

## Phase 7 — Handoff (to the build)

**Goal:** nothing learned in presale is lost when the build starts.

**Do:**
- Convert accepted decisions into a **build-ready brief** + `decisions.md` entries (what was chosen, what was rejected, what binds the build).
- Seed the project `AGENTS.md` / `wiki/` (per `../../core/references/wiki-protocol.md`) so `dev` starts with the architecture, constraints, NFRs, and open assumptions already captured.
- Flag the **highest-value first build step** and the open clarifications that gate it.

**Artifact:** decision records + build-ready brief (feeds `dev` Design mode).
