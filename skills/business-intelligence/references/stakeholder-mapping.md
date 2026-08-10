# Stakeholder & Buying Committee Mapping

Move from "who's in the room" to "how does this deal get decided." The executive profiling file handles individual depth. This file handles the system — who influences whom, who decides, where the gaps are.

---

## The Buying Committee

Enterprise B2B purchases involve 8-13 stakeholders (Gartner 2023, Forrester 2024). Profiling only the 5 meeting attendees leaves half the decision-making unit invisible.

### Roles to identify

| Role | What they do | How to spot | Intelligence action |
|------|-------------|-------------|---------------------|
| **Economic Buyer** | Final budget authority | "Who approves spend at this level without escalation?" | See `deal-qualification.md` |
| **Technical Evaluator** | Gates on feasibility, security, compliance | Sends technical questionnaires, asks architecture questions | Satisfy, don't sell to. Give them what they need to say "no risk." |
| **User Buyer** | Lives with the solution daily | Asks workflow/integration questions | Multiple across teams — each needs a personal win |
| **Champion** | Actively sells internally on your behalf | Volunteers next steps, does homework between meetings | See Champion Development below |
| **Coach** | Provides inside intelligence on politics/process | Shares things about org dynamics, competing priorities | Protect them — never reveal what they told you |
| **Blocker** | Actively opposes the engagement | Goes silent, raises new objections after each resolved, cc's procurement early | Identify what they lose if you win (see `executive-profiling.md` Political Layer) |
| **Gatekeeper** | Controls access to Economic Buyer | EA, Chief of Staff, procurement lead | Build relationship — they decide who gets through |

### Invisible stakeholders (hunt for these)

| Stakeholder | Why invisible | Why dangerous |
|-------------|--------------|---------------|
| **Legal/Compliance** | Never in early meetings | Appears late, kills deals on contract terms |
| **Security/InfoSec** | Only surfaces during technical evaluation | Veto power, non-negotiable requirements |
| **CFO's office** | Involved in 79% of purchases but rarely in demos | Budget approval gatekeeper |
| **Board/Investment committee** | Above the org chart you can see | Threshold-based approval for large deals |
| **Predecessor's preferred vendor champion** | Left the company but their choice is still running | Institutional inertia favoring the incumbent |

---

## Stakeholder Map Format

For every deal above qualification threshold, produce a stakeholder map alongside executive profiles.

```
STAKEHOLDER MAP: [Client] — [Engagement]
Updated: [Date]

BUYING COMMITTEE:
| Name | Title | Buying Role | Attitude (-5 to +5) | Influence (H/M/L) | Our Relationship (R/Y/G) | Owner (our side) |
|------|-------|------------|---------------------|-------------------|--------------------------|-----------------|
|      |       |            |                     |                   |                          |                 |

COVERAGE GAPS:
- [ ] Economic Buyer identified and accessed? [Y/N]
- [ ] Technical Evaluator(s) identified? [Y/N]
- [ ] Champion identified and tested? [Y/N]
- [ ] Legal/Compliance contact known? [Y/N]
- [ ] Procurement contact known? [Y/N]
- [ ] Divisions/levels with ZERO relationship: [list]

MULTI-THREADING SCORE:
- Contacts engaged: [N]
- Roles covered: [N of 7]
- Risk: [Single-threaded (5% win rate) / Adequate (3-4 contacts) / Strong (5+ across roles)]

POLITICAL DYNAMICS:
- Faction 1: [who, what they want]
- Faction 2: [who, what they want]
- Conflict lines: [where factions disagree]
- Our position: [aligned with whom, neutral to whom]
```

---

## Champion Development

### Champion vs Supporter

A supporter likes you. A champion spends political capital pushing your deal forward internally.

| Signal | Supporter | Champion |
|--------|-----------|----------|
| In meetings | Nods, agrees, friendly | Drives agenda, proposes next steps |
| Between meetings | Responsive when you reach out | Proactively does homework, sends you intel |
| Internal advocacy | "They seem good" | "Here's why we should do this — I've built the case" |
| Risk tolerance | Won't stick neck out | Will argue for you in rooms you're not in |

### Champion identification (from Challenger Customer research)

Look for **Mobilizers** — Go-Getters, Teachers, Skeptics. These people drive internal change.

Avoid **Talkers** — Guides, Friends, Climbers. They feel like progress but won't drive action. The most common mistake: confusing friendliness with championship.

### Testing your champion

Assign a task. If they follow through, they're real.

| Test | What it proves |
|------|---------------|
| "Could you share your team's current process metrics so we can build the business case?" | Willing to invest effort |
| "Would you take a 15-minute call with a reference customer?" | Willing to invest time |
| "Could you draft a problem statement we could use in the internal proposal?" | Willing to invest reputation |
| "Who else should we talk to?" + they make the introduction | Willing to spend political capital |

If they don't follow through on any of these, they are a Supporter, not a Champion. Adjust strategy accordingly.

### Enabling champions (arming them to sell internally)

Champions sell when you're not in the room. Give them the tools:

1. **Business case in their language** — not your pitch deck, their internal memo
2. **Role-specific collateral** — exec summary for their boss, tech spec for IT, ROI for finance
3. **The internal email** — draft the recommendation email they'd send to their leadership
4. **Ammunition against objections** — the counterarguments for what the Blocker will say

**Gartner:** 3x more likely to close when champions armed with helpful information.

### Multi-champion strategy

Single champion = single point of failure. Build three:

| Champion type | Purpose | Risk if missing |
|--------------|---------|-----------------|
| **Executive Champion** | Air cover, budget authority alignment | No one to override blockers |
| **Technical Champion** | Feasibility validation, architecture buy-in | Technical evaluation fails |
| **User/Process Champion** | Workflow proof, adoption evidence | "But will our people actually use it?" |

---

## Multi-Threading

**The data:** Single-threaded deals have a 5% win rate. Multi-threaded (5+ contacts): 30%. 6x improvement. Yet 78% of reps are single-threaded.

### Target coverage by deal size

| Deal size | Minimum contacts | Minimum roles covered |
|-----------|-----------------|----------------------|
| < $50K | 2-3 | Economic Buyer + User |
| $50K-$200K | 5-7 across 3+ roles | EB + Technical + User + Champion |
| $200K+ | 7-10 across functions | All 7 roles mapped, 5+ engaged |

### How to expand from one contact

- Ask champion to introduce: "I want to make sure your team's concerns are addressed"
- Offer unique value to each new contact (not repeating your pitch)
- Use workshops/events as natural multi-threading vehicles
- Executive briefings create legitimate reason for cross-level access

### Multi-threading risk check

Run this at every deal review:
- If champion leaves tomorrow, do we still have access? [Y/N]
- Do we have relationships above and below our main contact? [Y/N]
- Do we have contacts in more than one department? [Y/N]
- Has someone on the buying committee NOT heard from us? [who]

---

## Consensus Building

### The "No Decision" Problem

40-60% of deals end in "no decision" despite buyer intent. Two types (critical distinction):

| Type | Cause | Fix | Wrong fix |
|------|-------|-----|-----------|
| **Status quo (44%)** | Buyer underestimates cost of doing nothing | Quantify cost of inaction | N/A |
| **Indecision (56%)** | Analysis paralysis, too many options, fear of wrong choice | Simplify choices, reduce fear, JOLT methodology | Pushing harder — makes them freeze more |

Using the status quo playbook (fear, urgency) on an indecisive buyer makes them *more* indecisive.

### How to build consensus across a committee

1. **Map each stakeholder's personal win** — organizational result + personal career gain
2. **Find the unifying frame** — the one story that gives every stakeholder something to care about
3. **Build a mutual action plan** — time-bound steps both sides commit to, with named owners
4. **Give the champion the internal selling tools** (see above)
5. **Address blockers individually** — understand what they lose if you win, route around or reframe

---

## Buying Process Intelligence

### How to gather without asking "how do you buy?"

| Question | What it reveals |
|----------|----------------|
| "What would need to happen between now and a decision?" | Decision process and timeline |
| "Who else would need to weigh in?" | Hidden stakeholders |
| "Have you done something like this before? What worked/didn't?" | Procurement scars and preferences |
| "Is there a budget cycle we should be aware of?" | Timing constraints |
| "What does your evaluation process typically look like at this investment level?" | Formal procurement stages |

### Pre-RFP influence

41% of buyers have a preferred vendor before formal evaluation. RFP scoring matrices (15-25 criteria, weighted) are locked before issuance. If you didn't influence the criteria, you're playing someone else's game.

**How to influence early:** Publish thought leadership in their space, get analyst coverage, engage during need-identification phase (before RFP), offer workshops that shape requirements.

---

## The Dark Funnel

73% of the B2B buying journey happens anonymously before vendor contact. Buyers consume 20-30 content pieces across review sites, peer communities, analyst reports, and AI tools.

**81% have already decided on their vendor by the time they talk to you.**

**Intelligence action:** Research what they found during anonymous research. What do G2/TrustRadius reviews say about you? What do analysts rate you? What are peers saying in communities? This is part of the intelligence picture — not just what you know about them, but what they already know about you.
