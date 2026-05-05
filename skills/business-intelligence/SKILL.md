---
name: business-intelligence
description: "Build defensible intelligence on enterprise clients for presale engagements — presentations, proposals, negotiations. USE WHEN preparing for a high-stakes client conversation where what you claim will be tested. Keywords: research, client, executive, presentation, proposal, intel, profile, deep research, presale."
---

# Business Intelligence

Research foundation for enterprise presale. The output of this skill is intelligence you can **defend in the room** — not a literature review.

## Posture (read first, every time)

These five principles govern the skill. If a downstream pattern conflicts with them, the principle wins.

### 1. Scope research the same way you scope consulting: tightly.

**Why:** Overbroad research produces confident-sounding intel in areas you can't back. That's the same failure mode as overconfident consulting, one step upstream — the bad claim enters your materials before anyone pushes on it.

**How to apply:** This skill covers *presale-relevant* intel — strategy, pain points, tech landscape, executives, partnership history, competitive context. It does **not** cover M&A due diligence, market sizing for product strategy, or adjacent business questions you can't defend. If a research track starts drifting there, stop and refocus.

### 2. Demand evidence. Yours and theirs.

**Why:** Research output becomes the sales conversation. An unverified intel point surfaces as an unverified claim in the room, and that's where credibility dies. This applies symmetrically: every piece of client intel needs a source, and every claim in *your* materials needs verification before it reaches a slide.

**How to apply:** Every intel point cites source + date. Every claim you plan to make passes a Claims Verification check (see subagent-directives.md). Unsourced = unused until sourced.

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

---

## Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   SCOPE     │────▶│  RESEARCH   │────▶│  PROFILES   │────▶│  SYNTHESIZE │
│  (clarify)  │     │  (parallel) │     │  (execs)    │     │  (outputs)  │
└─────────────┘     └──────┬──────┘     └─────────────┘     └──────┬──────┘
                           │                   │                    │
                           └───────────────────┘                    │
                           (gap analysis loops back)                │
                                                                    │
                    On re-entry (multi-phase): read previous ◀──────┘
                    outputs first, update profiles, re-verify claims
```

### Multi-phase engagements

Real engagements iterate. Each invocation may be a new phase building on the last. On re-entry:

1. Read previous intelligence outputs before starting new research
2. Update executive profiles (new attendees, role changes, re-assessed risk including political layer)
3. Re-run Claims Verification against any positioning changes
4. Carry forward what worked, drop what didn't land

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

## Phase 3 — Executive profiles

**Posture reminder:** Principle 3. Risk scoring without a political layer is a half-answer. Principle 4 applies: know what each exec won't tolerate as much as what they'd lean into.

For each attendee, document:

| Element | Purpose |
|---------|---------|
| **Role & tenure** | Authority level, organizational context |
| **Background** | Career history, expertise areas, education |
| **Public positions** | Speeches, articles, LinkedIn activity |
| **Likely questions** | What they'll ask based on role |
| **Attack vectors** | Where they'll challenge your claims |
| **Interest signals** | What would make them lean in |
| **Risk level** | H/M/L with rationale |
| **Political layer** | Reports to whom / measured on what / loses what if we win |
| **Cultural notes** | Languages, background, personal interests |

See `references/executive-profiling.md` for the political-layer pattern, NEW-executive handling, attack vectors by role, cultural intelligence.

---

## Phase 4 — Synthesize outputs

**Posture reminder:** Principle 4. The outputs below aren't a checklist — they're the scaffolding that keeps landmines off the stage.

### Required outputs

| Output | Why it exists |
|--------|---------------|
| **Intelligence Report** | Baseline context — strategy, pain, tech, competitive, partnership |
| **Executive Profiles** | Risk map including political layer |
| **Capability Map** | Honest positioning tool — which capabilities lead, which stay off stage |
| **Honest Q&A Table** | Words you already have when you're under pressure |
| **Negative Space** | Landmine avoidance — what NOT to present or claim |
| **Claims Verification Summary** | Kills overclaim at the source, before it reaches a slide |
| **"What Competitor CANNOT Do"** | One defensible differentiator per named competitor |

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

## When to stop and hand off

This skill produces **intelligence**. It does not produce deliverables.

- **Stops at:** synthesis outputs (above)
- **Hands off to:** presentation / proposal / demo script authoring
- **Does not create:** slides, proposal text, demo scripts
- **Designed to minimize the handoff gap:** Honest Q&A Table and Negative Space are structured so the person writing the deliverable picks them up and uses them directly

### When NOT to use this skill

- Client is well-known to you (use existing knowledge; don't theater it)
- Simple transactional engagement (overkill)
- No time for research (skip to a Claims Verification pass + Honest Q&A only)

---

## Self-checks (tied to posture)

Before declaring the intel ready:

**Principle 1 — Scope**
- [ ] Every research track points back to positioning. No drift.

**Principle 2 — Evidence**
- [ ] All intel has source + date
- [ ] Claims Verification complete; Overclaims resolved (soften / remove / verify)

**Principle 3 — Score**
- [ ] Pain points ranked by offering-relevance
- [ ] Executives risk-scored with political layer
- [ ] Capabilities classified Gap / Overlap / Competition / Complement

**Principle 4 — Negative space**
- [ ] Negative Space output exists and is non-empty
- [ ] "What Competitor CANNOT Do" has one entry per named competitor

**Principle 5 — Loop-back**
- [ ] Loop-back triggers checked; any firing surfaced to user before synthesis

---

## Limitations

- **Public sources only** — never claim inside knowledge
- **Completeness varies** — some companies have thin public footprint; flag it
- **Question prediction is probabilistic** — attack vectors and interest signals are informed guesses, not certainty
- **No substitute for live room-reading** — prep covers what you can anticipate; the room handles the rest

---

## Cross-links

- **`ms-ai-discovery`** — for enterprise AI engagements specifically. That skill runs the Microsoft AI Discovery & Envisioning workshop and uses BXT scoring. Run BI skill as prework (executive profiles + competitive context) before Day 1.
- **`references/frameworks_vocabulary.md`** — named frameworks for query anchoring
- **`references/subagent-directives.md`** — parallel research orchestration
- **`references/deep-research-patterns.md`** — iterative research mechanics
- **`references/executive-profiling.md`** — political layer, NEW-executive handling
- **`references/defensive-positioning.md`** — Capability Map, Competitor CANNOT-Do, Honest Q&A, Negative Space
