---
name: business-intelligence
description: "Build defensible intelligence on enterprise clients for presale engagements — presentations, proposals, negotiations. USE WHEN preparing for a high-stakes client conversation where what you claim will be tested. Keywords: research, client, executive, presentation, proposal, intel, profile, deep research, presale, discovery, account, qualify, business case, win loss."
license: MIT
---

# Business Intelligence

Full presale intelligence lifecycle — from deal qualification through post-engagement learning. The output of this skill is intelligence you can **defend in the room** — not a literature review.

## Posture (read first, every time)

These five principles govern the skill. If a downstream pattern conflicts with them, the principle wins.

### 1. Scope research the same way you scope consulting: tightly.

**Why:** Overbroad research produces confident-sounding intel in areas you can't back. That's the same failure mode as overconfident consulting, one step upstream — the bad claim enters your materials before anyone pushes on it.

**How to apply:** This skill covers *presale-relevant* intel — strategy, pain points, tech landscape, executives, partnership history, competitive context. It does **not** cover M&A due diligence, market sizing for product strategy, or adjacent business questions you can't defend. If a research track starts drifting there, stop and refocus.

### 2. Demand evidence. Yours and theirs.

**Why:** Research output becomes the sales conversation. An unverified intel point surfaces as an unverified claim in the room, and that's where credibility dies. This applies symmetrically: every piece of client intel needs a source, and every claim in *your* materials needs verification before it reaches a slide.

**How to apply (this is the Grounding Gate — inherited from `core`):** Every intel point cites source + date and carries an Admiralty grade; every claim you plan to make passes a Claims Verification check (see subagent-directives.md). Record it: `Grounded: <claim> → <source>, grade <A–F/1–6>` or flag it as an assumption/unknown. **Unsourced = unused until sourced. A claim you cannot ground, you do not make** — or you state it as negative space. Silent skip = integrity violation. Canonical gate + honesty corollary: `../core/references/grounding-gate.md`.

### 3. Score before recommending.

**Why:** Ranking by vibe gives tangential and load-bearing problems equal weight. The output is noise dressed as insight. Structured scoring also forces you to defend *why* something matters, which surfaces weak intel.

**How to apply:**
- **Pain points** ranked by relevance to your offering, with evidence.
- **Executives** risk-scored H/M/L with rationale, including the political layer (see executive-profiling.md).
- **Capabilities** classified Gap / Overlap / Competition / Complement (see defensive-positioning.md — Capability Map).
- For enterprise AI engagements specifically, use the **BXT framework** (Business viability / Experience desirability / Technology feasibility) as the scoring lens — see the `ms-ai-discovery` skill.

### 4. Know the negative space.

**Why:** The thing that kills presale isn't missing a point — it's stepping on a landmine. Showing a capability they already have. Overclaiming something a technical lead drills into. Raising a competitor's differentiator for them. Negative space is the discipline of knowing what *not* to do.

**How to apply:** Every engagement produces an explicit Negative Space output (defensive-positioning.md). Capability Map Overlap/Competition rows feed it. Claims Verification Overclaims feed it. Capabilities irrelevant to the attendee roster feed it.

### 5. Loop back when reality shifts.

**Why:** Research only has value if it can change what you do. If findings arrive and get ignored because "we're already committed to the approach," you did expensive theater.

**How to apply:** Named triggers pause current work and surface to the user before proceeding. See the Loop-Back Rule section below.

---

## Quick start

```
Research [Company] for [presentation/proposal/meeting]
```

```
Build intel on [Company] — I'm meeting with [executives]
```

```
Prep for discovery call with [Company] tomorrow
```

```
Should we pursue the [Company] deal?
```

```
Debrief on the [Company] meeting — what worked, what didn't
```

```
What's our position with [Company]? Review the account.
```

```
Build a business case for [Company]
```

---

## Workflow

```
┌──────────┐  ┌─────────┐  ┌───────────┐  ┌─────────────┐  ┌───────────┐  ┌───────────┐
│ QUALIFY   │─▶│  SCOPE  │─▶│ RESEARCH  │─▶│ STAKEHOLDER │─▶│ SYNTHESIZE│─▶│ DISCOVERY │
│ (score)   │  │(clarify)│  │ (parallel)│  │    MAP      │  │ (outputs) │  │   PREP    │
└──────────┘  └─────────┘  └─────┬─────┘  └─────────────┘  └─────┬─────┘  └───────────┘
                                 │               │                │
                                 └───────────────┘                │
                                 (gap analysis loops back)        │
                                                                  │
┌───────────────────────────────────────────────────────────────── │ ───────────────┐
│ ACCOUNT STRATEGY — persists across engagements, updated after each              │
│ (account plan, relationship map, white space, competitive position)              │
└─────────────────────────────────────────────────────────────────────────────────┘
                                                                  │
                          POST-ENGAGEMENT (debrief, win/loss)  ◀──┘
```

### Phase activation (not all phases fire every time)

| Trigger | Phases that fire |
|---------|-----------------|
| "Research [Company] for [meeting]" | Qualify → Scope → Research → Stakeholders → Synthesize → Discovery Prep |
| "Prep for call with [Company]" | Discovery Prep (pulls existing intel if available) |
| "Should we pursue [Company]?" | Qualify only |
| "[Company] meeting went well/badly" | Post-Engagement debrief |
| "What's our position with [Company]?" | Account Strategy review |
| "Build a business case for [Company]" | Value Engineering (Phase 4 output) |
| Quick meeting / conference follow-up | Scope → lightweight Research → Profiles only |

### Multi-phase engagements

Real engagements iterate. Each invocation may be a new phase building on the last. On re-entry:

1. Read previous intelligence outputs before starting new research
2. Update executive profiles and stakeholder map (new attendees, role changes, champion status)
3. Re-run Claims Verification against any positioning changes
4. Update MEDDPICC score with new intelligence
5. Carry forward what worked, drop what didn't land

---

## Phase 0 — Qualify

**Posture reminder:** Principle 1. Not every deal deserves full research. Score before committing.

Run MEDDPICC scoring at entry. Each element: **Strong** (evidence) / **Weak** (partial) / **Missing** (unknown). See `references/deal-qualification.md` for the full scoring template, go/no-go matrix, and buying influence mapping.

| Condition | Decision |
|-----------|----------|
| No identified pain | Walk away |
| No access to Economic Buyer after 2 attempts | High risk — escalate or walk |
| No Champion identified | Stall likely — invest in champion development or walk |
| 5+ elements Strong | Pursue — high-quality opportunity |
| 2+ elements Missing | Pause — gather intelligence before committing |

**Output:** Deal Qualification Score with go/no-go recommendation and intelligence targets (what to resolve during research).

**When to skip:** Client is well-known, deal is low-risk, or engagement is already contracted.

---

## Phase 1 — Scope

**Posture reminder:** Principle 1. If the engagement objective is fuzzy, research will drift. Scope before spawning subagents.

### Clarify before researching

| Category | Questions |
|----------|-----------|
| **Context** | Presentation, proposal, negotiation, meeting? |
| **Audience** | Who's attending? Names, titles if known |
| **Objective** | What outcome are you seeking? |
| **Your offering** | Which solutions/capabilities are you presenting? |
| **History** | Existing relationship? Past engagements? |
| **Timeline** | When is the engagement? |

**Output of Phase 1:** A mental model of what intel is needed. No documents yet.

---

## Phase 2 — Deep research (parallel tracks)

**Posture reminder:** Principles 2 + 4. Every track cites sources. Every track feeds Negative Space as much as it feeds the positive pitch.

### Deploy research team

YOU are the coordinator. Spawn subagents for independent tracks. Do NOT do all research yourself — parallel subagents save context and time.

See `references/subagent-directives.md` for deployment instructions per researcher type.

**Parallel** when topics are independent. **Sequential** when findings would redirect later research.

### Research tracks

**Always run:**

| Track | What to find |
|-------|--------------|
| **Company Strategy** | Current priorities, multi-year plans, public commitments, CEO messaging |
| **Pain Points** | Stated challenges, analyst concerns, public admissions |
| **Technology Landscape** | Current stack, vendors, recent implementations, gaps |
| **Competitive Position** | Market standing, benchmarks, pressures — and **what each competitor CANNOT do** (defensive-positioning.md) |
| **Claims Verification** | Cross-reference YOUR materials against product reality. Verified / Overclaim / Unknown |
| **Product-Environment Fit** | Capability Map: Gap / Overlap / Competition / Complement |

**Run when relevant:**

| Track | When | What to find |
|-------|------|--------------|
| **Financial Context** | Unfamiliar client, pricing discussion expected | Investment capacity, budget cycles, cost pressures |
| **Partnership History** | Existing relationship matters to positioning | Past engagements, key contacts, relationship health |

### Research methodology

See `references/deep-research-patterns.md` for Plan-Act-Observe-Reflect, broad-to-narrow queries, gap analysis, source prioritization, context compression.

See `references/frameworks_vocabulary.md` for named frameworks to anchor queries — Sandler pain funnel for pain-point research, MEDDIC qualifiers for decision-making intel, Forrester/Gartner for analyst landscape, Porter 5 forces for competitive context.

---

## Phase 3 — Stakeholder map & executive profiles

**Posture reminder:** Principle 3. Risk scoring without a political layer is a half-answer. Principle 4 applies: know what each exec won't tolerate as much as what they'd lean into.

### 3a. Executive profiles (per attendee + known stakeholders)

| Element | Purpose |
|---------|---------|
| **Role & tenure** | Authority level, organizational context |
| **Buying influence** | Economic Buyer / User Buyer / Technical Buyer / Coach |
| **Background** | Career history, expertise areas, education |
| **Public positions** | Speeches, articles, LinkedIn activity |
| **Likely questions** | What they'll ask based on role |
| **Attack vectors** | Where they'll challenge your claims |
| **Interest signals** | What would make them lean in |
| **Risk level** | H/M/L with rationale |
| **Political layer** | Reports to whom / measured on what / loses what if we win |
| **Win-result** | Organizational result + personal win they'd get |
| **Cultural notes** | Languages, background, personal interests |

See `references/executive-profiling.md` for political-layer pattern, NEW-executive handling, buying influence roles, champion identification, attack vectors by role, cultural intelligence.

### 3b. Buying committee map (beyond attendees)

Profile the attendees, then map the broader buying committee. Enterprise purchases involve 8-13 stakeholders — profiling only attendees leaves half the decision-making unit invisible.

**Produce a stakeholder map** covering: buying influence roles, attitude scores, relationship strength, coverage gaps, multi-threading score, political dynamics.

**Hunt for invisible stakeholders:** Legal/Compliance, Security/InfoSec, CFO's office, Board/Investment committee, predecessor's preferred vendor champion.

**Champion assessment:** Identify, test (assign a task — do they follow through?), and enable (give them the internal selling tools).

See `references/stakeholder-mapping.md` for the full stakeholder map template, champion development, multi-threading assessment, consensus building, and buying process intelligence.

---

## Phase 4 — Synthesize outputs

**Posture reminder:** Principle 4. The outputs below aren't a checklist — they're the scaffolding that keeps landmines off the stage.

### Required outputs

| Output | Why it exists |
|--------|---------------|
| **Intelligence Report** | Baseline context — strategy, pain, tech, competitive, partnership |
| **Executive Profiles** | Risk map including political layer and buying influence roles |
| **Stakeholder Map** | Buying committee, multi-threading assessment, champion status, coverage gaps |
| **Capability Map** | Honest positioning tool — which capabilities lead, which stay off stage |
| **Honest Q&A Table** | Words you already have when you're under pressure |
| **Negative Space** | Landmine avoidance — what NOT to present or claim |
| **Claims Verification Summary** | Kills overclaim at the source, before it reaches a slide |
| **"What Competitor CANNOT Do"** | One defensible differentiator per named competitor |

### Conditional outputs (when the engagement warrants it)

| Output | When to produce | Reference |
|--------|----------------|-----------|
| **Deal Qualification Score** | New client or large deal | `deal-qualification.md` |
| **Business Case Skeleton** | $100K+ deal, CFO involvement, "no decision" risk | `value-engineering.md` |
| **Battle Card** | Named competitor in the evaluation | `battle-cards.md` |
| **Discovery Playbook** | Live meeting coming up | `discovery-methodology.md` |
| **Account Plan** | Strategic account, multi-phase engagement | `account-strategy.md` |

### Output structure

**Intelligence Report** — executive summary (3–5 bullets), business context, pain points ranked by offering-relevance with evidence, technology landscape, competitive pressure, partnership context, sources with dates.

**Executive Profiles** — per attendee: risk + rationale, role/authority, political layer, background, public positions, likely questions, attack vectors AND interest signals, cultural notes, engagement strategy.

**Capability Map** (see defensive-positioning.md):

| Client Need | Our Fit | Gap |
|-------------|---------|-----|
| [Specific need, evidence-backed] | [What we have that addresses it] | [Honest gap — what we don't cover] |

The Gap column is not weakness to hide. It's honest positioning. A client who sees a credible Gap column trusts the rest of the map.

**Honest Q&A Table** (see defensive-positioning.md):

| Topic | Reality | Honest Response |
|-------|---------|-----------------|
| [Claim area] | [What's actually true — internal] | [Verbatim words for the room] |

**Negative Space** (see defensive-positioning.md):

| Don't Present | Why |
|---------------|-----|
| [Capability/topic] | [They have it / wrong audience / overclaim / irrelevant] |

**Claims Verification Summary**:

| Claim | Status | Action |
|-------|--------|--------|
| [What you plan to say] | Verified / Overclaim / Unknown | Keep / Soften / Remove / Verify before presenting |

**What Competitor CANNOT Do** (see defensive-positioning.md): for each named competitor in the room, one sentence on what they structurally can't deliver that you can. Not a hit piece — a defensible differentiator.

---

## The Loop-Back Rule

Research that changes the picture isn't a distraction. It's the whole point.

### Named triggers — pause and surface to user

| Trigger | What changed |
|---------|--------------|
| **NEW executive (< 1 year)** | Existing relationship goodwill may not transfer. Re-assess engagement strategy. |
| **Competitive shift** | Competitor won a relevant deal, launched a competing capability, or changed positioning. Defensive work needed. |
| **Pain misalignment** | Their stated pain points don't align with your offering. Rescope or reconsider. |
| **Stack change** | They adopted (or dropped) a platform that changes the Capability Map. Re-run product-environment fit. |
| **Political shift** | Exec reorg, sponsor change, budget reassignment. Political layer changed. |
| **Claim collapse** | Claims Verification surfaces an Overclaim you didn't know about. Fix the claim, not the messaging. |

### What "surface to user" looks like

1. **STOP** current track
2. **STATE** what you found and why it changes things
3. **DISCUSS** implications
4. **DECIDE** together whether to adjust approach

Do not silently adjust. The user is the one who has to defend the work in the room — they need to know what shifted.

---

## Phase 5 — Discovery preparation

**When:** A live meeting is coming up. Fires after synthesis (full cycle) or standalone ("prep for call with [Company] tomorrow").

### Pre-call playbook

Produce a concise discovery playbook using intelligence from earlier phases:

1. **Objective:** "As a result of this call, the buyer will [specific action]"
2. **Minimum acceptable outcome:** The floor if the call goes sideways
3. **Top 3 questions:** Must-answer for this call (use SPIN — lead with Problem and Implication, not Situation)
4. **Likely objections (top 2):** With prepared responses (LAER framework)
5. **Role assignment:** Who leads, who handles technical, who takes notes
6. **Relevant evidence:** Which case study or data point matches
7. **Landmines:** What could go wrong (from Negative Space and competitive intel)
8. **Meeting type playbook:** Initial discovery / Technical deep-dive / Demo / Executive briefing / POC scoping / Negotiation (each has a different approach)

See `references/discovery-methodology.md` for SPIN in practice, Sandler pain funnel, active listening techniques, meeting type playbooks, objection handling (LAER), and handling difficult moments.

---

## Phase 6 — Post-engagement learning

**When:** After a meeting, after a deal decision (win or loss), or when the user says "debrief."

### Post-meeting debrief

Capture within 1 hour:
- Pain points heard (in their exact words)
- Business impact (quantified where possible)
- Decision process intelligence (who, when, how)
- Political dynamics (who championed, who resisted, who was silent)
- MEDDPICC updates (any elements moved from Missing/Weak to Strong?)
- Stakeholder map updates (attitudes shifted? new stakeholders?)

### Win/Loss debrief

After a deal decision, run a structured debrief. See `references/win-loss.md` for:
- Win/loss interview questions (IT services-specific)
- Win/loss debrief template
- Deal health scoring
- Pattern tracking across deals

**Close the loop — deal-learning → skill-learning.** A debrief that ends in `win-loss.md` teaches you about *that deal*. After each one, ask "does this contradict or extend the skill?" — and when a pattern recurs, promote it into `EVOLUTION.md` so it changes BI's frameworks, positioning, or gates. That is the difference between a skill that learns about deals and one that learns about itself. See `EVOLUTION.md` (loop: `../core/references/evolution-loop.md`).

### Intelligence handoff (presale → delivery)

When a deal is won, transfer: stakeholder map, decision criteria, competitive context, business drivers, risk factors, champion identity, Honest Q&A Table. See `references/win-loss.md` for the full handoff checklist.

---

## Account Strategy (overarching layer)

For strategic accounts with multi-phase engagements, maintain a persistent account plan. This is not per-engagement — it compounds across engagements.

See `references/account-strategy.md` for:
- Account plan template (snapshot, relationship map, engagement history, white space, competitive landscape, growth strategy, 90-day actions)
- Land-and-expand vectors
- Multi-year arc (Year 1: credibility → Year 2: expansion → Year 3: strategic partnership)
- Relationship mapping and gap analysis
- Competitive displacement framework
- Reference selling

**Trigger:** "What's our position with [Company]?" or any multi-phase engagement.

---

## When to stop and hand off

This skill produces **intelligence and preparation**. It does not produce deliverables.

- **Stops at:** synthesis outputs + discovery playbook
- **Hands off to:** presentation / proposal / demo script authoring
- **Does not create:** slides, proposal text, demo scripts
- **Designed to minimize the handoff gap:** Honest Q&A Table, Negative Space, Discovery Playbook, and Business Case Skeleton are structured so the person writing the deliverable picks them up directly
- **Loops back via:** Post-engagement debriefs that feed into the next engagement's intelligence

### When NOT to use this skill

- Client is well-known to you (use existing knowledge; don't theater it)
- Simple transactional engagement (overkill)
- No time for research (skip to a Claims Verification pass + Honest Q&A only)

---

## Self-checks (tied to posture)

Before declaring the intel ready:

**Principle 1 — Scope**
- [ ] Every research track points back to positioning. No drift.
- [ ] Deal qualification score completed (if new client/large deal)

**Principle 2 — Evidence**
- [ ] All intel has source + date + confidence grade
- [ ] Claims Verification complete; Overclaims resolved (soften / remove / verify)
- [ ] Business case assumptions graded H/M/L with sources

**Principle 3 — Score**
- [ ] Pain points ranked by offering-relevance
- [ ] Executives risk-scored with political layer AND buying influence role
- [ ] Capabilities classified Gap / Overlap / Competition / Complement
- [ ] MEDDPICC score current (if qualifying)

**Principle 4 — Negative space**
- [ ] Negative Space output exists and is non-empty
- [ ] "What Competitor CANNOT Do" has one entry per named competitor

**Principle 5 — Loop-back**
- [ ] Loop-back triggers checked; any firing surfaced to user before synthesis

**Stakeholder coverage**
- [ ] Buying committee mapped beyond attendees (if known)
- [ ] Champion identified and tested (or flagged as gap)
- [ ] Multi-threading score assessed
- [ ] Coverage gaps flagged

**Discovery readiness** (if meeting coming up)
- [ ] Pre-call playbook produced with objective + minimum outcome
- [ ] Top questions prepared (SPIN — Implication-heavy, not Situation-heavy)
- [ ] Objection responses prepared (LAER)
- [ ] Role assignment clear

---

## Limitations

- **Public sources only** — never claim inside knowledge
- **Completeness varies** — some companies have thin public footprint; flag it
- **Question prediction is probabilistic** — attack vectors and interest signals are informed guesses, not certainty
- **No substitute for live room-reading** — prep covers what you can anticipate; the room handles the rest

---

## Cross-links

**Kernel:**
- **`core`** — the shared spine BI inherits: integrity constraints, gate-by-artifact, the Grounding Gate (posture #2), the Output Contract, and the evolution loop behind `EVOLUTION.md`. Reference `../core/references/…`, don't re-derive. See `../core/SKILL.md`.

**Other skills:**
- **`ms-ai-discovery`** — for enterprise AI engagements specifically. That skill runs the Microsoft AI Discovery & Envisioning workshop and uses BXT scoring. Run BI skill as prework (executive profiles + competitive context) before Day 1.
- **`solution-architect`** — the next step after intel. BI tells you *what you know about the client*; `solution-architect` turns that (plus any scoped use cases) into a defensible solution architecture and a winning RFI/RFP/proposal response. Feed BI's profiles, competitor context, and capability map into its Frame phase and win themes.

**Core references (existing):**
- **`references/frameworks_vocabulary.md`** — named frameworks for query anchoring (MEDDPICC, SPIN, Challenger, Miller Heiman, Sandler, Admiralty Code, TCO, LAER, and more)
- **`references/subagent-directives.md`** — parallel research orchestration
- **`references/deep-research-patterns.md`** — CI discipline, source grading, iterative research mechanics
- **`references/executive-profiling.md`** — political layer, buying influences, champion identification, NEW-executive handling
- **`references/defensive-positioning.md`** — Capability Map, Competitor CANNOT-Do, Honest Q&A, Negative Space

**New references (from research sprint):**
- **`references/deal-qualification.md`** — MEDDPICC scoring, go/no-go, buying influence mapping
- **`references/value-engineering.md`** — business case skeleton, TCO, ROI, cost of inaction, value by role
- **`references/stakeholder-mapping.md`** — buying committee, champion development, multi-threading, consensus building
- **`references/discovery-methodology.md`** — SPIN practice, Sandler pain funnel, meeting types, objection handling, pre-call planning
- **`references/account-strategy.md`** — account planning, land-and-expand, relationship mapping, multi-year arc
- **`references/win-loss.md`** — win/loss practice, deal health scoring, post-engagement debrief, intelligence handoff
- **`references/battle-cards.md`** — battle card structure, war gaming, competitive displacement, CI source grading

**Raw research (for reference):**
- **`research-sprint/`** — full research outputs from the 6-track discipline survey (enterprise sales methodology, competitive intelligence, value engineering, stakeholder/buying process, discovery/needs analysis, account strategy/win-loss)
