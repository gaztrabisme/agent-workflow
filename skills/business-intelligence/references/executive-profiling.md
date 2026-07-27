# Executive Profiling

Methodology for building actionable executive profiles with attack vectors.

---

## Why Profile Executives

- **Personalization** — Tailor message to their priorities
- **Anticipation** — Prepare for likely questions
- **Defense** — Know where you'll be challenged
- **Opportunity** — Know what would make them lean in
- **Connection** — Find cultural or personal touchpoints
- **Risk Management** — Identify who could derail AND who could champion the engagement
- **Deal Strategy** — Map buying influences and identify the real decision architecture

---

## Buying Influence Role

For each profiled executive, assign a buying influence role (Miller Heiman). These are roles, not titles — one person may hold multiple.

| Role | What they do | Profile implication |
|------|-------------|-------------------|
| **Economic Buyer** | Final budget authority — can say yes when everyone says no | Highest priority profile. Prepare win-result (personal + organizational). |
| **User Buyer** | Lives with the solution daily | Prepare workflow-level value story, not strategic. |
| **Technical Buyer** | Gates on feasibility, security, compliance — cannot say yes but CAN say no | Satisfy, don't sell to. Prepare honest technical depth. |
| **Coach** | Internal advocate with organizational influence who supports you | Protect — never reveal what they told you. Enable — give them tools to sell internally. |

Add this to every profile:

```
Buying Influence: [Economic Buyer / User Buyer / Technical Buyer / Coach / Unknown]
Win-Result: [Organizational result they need] + [Personal win they'd get]
```

---

## Champion Identification

A champion is not a friendly contact. A champion spends political capital pushing your deal forward.

### Champion signals (add to profile when observed)

| Signal | Champion | Supporter (not champion) |
|--------|----------|------------------------|
| In meetings | Drives agenda, proposes next steps | Nods, agrees, friendly |
| Between meetings | Does homework, sends intel proactively | Responsive when you reach out |
| Internal advocacy | "Here's why we should do this — I built the case" | "They seem good" |
| Risk tolerance | Will argue for you in rooms you're not in | Won't stick neck out |

### Champion testing

When you suspect someone is a champion, assign a task:
- "Could you share your team's process metrics for the business case?"
- "Would you take a 15-minute call with a reference customer?"
- "Could you draft a problem statement for the internal proposal?"

Follow-through = real champion. No follow-through = supporter. Adjust strategy.

### Multi-threading assessment (add to profile set)

After profiling all attendees + known stakeholders:

```
Multi-Threading Score:
  Contacts engaged: [N]
  Roles covered: [list]
  Coverage gaps: [missing roles or levels]
  Single-thread risk: [Y/N — if champion is only contact]
```

See `stakeholder-mapping.md` for the full buying committee map that wraps around individual profiles.

---

## Risk Assessment

### Risk Level Criteria

| Level | Criteria | Preparation Priority |
|-------|----------|---------------------|
| **HIGH** | New to role, technical expert in your domain, known skeptic, key decision authority, external hire | Maximum preparation, anticipate deep grilling |
| **MEDIUM** | Experienced in role, tangential expertise, neutral disposition, influencer but not decider | Standard preparation, know their domain |
| **LOW** | Long tenure, non-technical, supportive of existing relationship, limited decision authority | Basic awareness, don't ignore |

### Red Flags (Auto-Elevate to HIGH)

| Flag | Why It's Dangerous |
|------|-------------------|
| **New to company (< 1 year)** | No loyalty to existing partnerships, may reassess vendors |
| **External hire from competitor** | May have preferred vendors, different expectations |
| **Technical expert in your domain** | Will test depth, catches bullshit immediately |
| **Known for tough questions** | Reputation precedes them |
| **Recently promoted** | Proving themselves, may be aggressive |
| **Procurement/Finance background** | Will scrutinize TCO, ROI, value evidence |

---

## The Political Layer

Risk (H/M/L) tells you how hard they'll push back. The political layer tells you *why* — and what's actually at stake for them if your engagement succeeds or fails. Without this, risk scoring is a surface read.

### Three Questions

For every HIGH and MEDIUM risk executive, answer:

| Question | What It Tells You |
|----------|-------------------|
| **Who do they report to?** | Whose agenda they're executing. A CIO reporting to a transformation-focused CEO behaves differently than one reporting to a cost-focused CFO. |
| **What are they measured on?** | Their actual incentive. "Reduce OpEx 15%," "ship digital platform by Q4," "pass the regulator audit." Maps directly to which of your capabilities they'll care about. |
| **What do they lose if you win?** | The hidden blocker. If your engagement threatens their in-flight initiative, internal team, preferred vendor, or political capital, they will quietly work against you even when they nod in the room. |

### Why "lose if you win" is load-bearing

This is the question most presale skips — and it's the one that explains surprise losses. A few common shapes:

| Pattern | Example |
|---------|---------|
| **In-flight build** | They have a team building what you're proposing. Your win = their project canceled. |
| **Preferred vendor** | They championed a competitor's contract last year. Your win = they were wrong. |
| **Empire shrinkage** | Your solution reduces their team's scope. Your win = smaller org, smaller influence. |
| **Attribution conflict** | A peer exec is on record claiming this problem is solved. Your win = they contradicted that peer. |
| **Political debt** | They owe a favor to someone who backs a competitor. Your win = they couldn't pay the favor. |

If you identify this pattern, flag it in the profile and route around it — find a sponsor whose incentives align, or acknowledge the conflict directly. Pretending it isn't there is how engagements die quietly.

### Capture format

Add to every H/M profile:

```
Political Layer:
  Reports to: [name, role] — [what that person is pushing for]
  Measured on: [the 1-3 metrics or objectives they own]
  Loses if we win: [in-flight build / preferred vendor / empire / attribution / debt / none identified]
  Sponsor alignment: [who on their side actually wants this to succeed, and why]
```

If "Loses if we win" is non-empty, the engagement strategy must account for it — not the Q&A table.

---

## Attack Vector Analysis

### By Role Type

| Role | Typical Attack Vectors |
|------|----------------------|
| **CIO/CTO** | Architecture fit, security, scalability, vendor lock-in |
| **CFO/Finance** | TCO, ROI, hidden costs, value quantification |
| **Procurement** | Contract terms, SLAs, competitive alternatives |
| **Operations** | Reliability, support model, implementation risk |
| **Security** | Compliance, data handling, access controls |
| **IT/OT** | Integration complexity, protocol support, existing systems |
| **HR/CHO** | Change management, user adoption, training |
| **Business Unit** | Time to value, business outcomes, use case fit |

### Preparing Defenses

For each attack vector:

1. **Anticipate the question** — What exactly will they ask?
2. **Prepare honest answer** — What can you actually defend?
3. **Build escape hatch** — How to deflect gracefully if uncertain?
4. **Know the boundary** — Where to stop and say "that's a scoping discussion"?

---

## Interest Signal Analysis

Attack vectors tell you where you'll be challenged. Interest signals tell you where you'll be *wanted*. Both matter. Preparing only for defense creates a defensive posture that reads as insecurity.

### Interest Signals by Role

| Role | What Would Make Them Lean In |
|------|------------------------------|
| **CIO/CTO** | Capability that fills a known gap, accelerates their roadmap, reduces vendor dependency |
| **CFO/Finance** | Clear cost avoidance, consolidation of existing tools, measurable baseline |
| **Operations** | Reduces manual work they're doing today, unifies fragmented tools |
| **IT/OT** | Solves a problem their current stack can't, integrates without replacing |
| **Business Unit** | Faster time to value than building internally, visible to their leadership |
| **HR/CHO** | Enables workforce without heavy change management |

### Reading Live Signals

These happen in the room. You can't fully prepare for them, but you can recognize them:

| Signal | What It Means | Response |
|--------|---------------|----------|
| "What else can this do?" | They want breadth, not more depth | **Zoom out.** Show other use cases, platform capabilities. Don't drill deeper into current topic. |
| "How would this work with our [X]?" | They're mentally fitting you into their stack | Answer directly. This is buying behavior, not testing. |
| "Can you show that again?" | Feature landed. They want to understand it. | Slow down, explain the mechanics, let them ask follow-ups. |
| "Who else uses this?" | Social proof seeking — they're interested but need validation | Reference similar deployments (honestly). If limited, say "early but deployed for [X]." |
| Leaning forward, taking notes | Engaged. Don't interrupt with more slides. | Let the moment land. Pause. Let them ask. |
| Silence after your point | Could be processing OR disengaged — read body language | Brief pause, then: "Does that connect to how your team handles this today?" |
| "That's interesting but..." | Partial interest, specific objection | Address the objection directly. Don't deflect — they're close. |

### The Zoom-Out Card

Prepare a 2-3 sentence breadth summary for each engagement. When someone signals expansion, you need words ready — not a new slide deck, just a sentence.

**Format**: "Beyond [what we just showed], [breadth of capabilities]. [Concrete second example]."

**Example (composite)**: "Beyond asset management, we've built forecasting pipelines, data enrichment workflows, and low-code model deployment. For example, a renewable-generation forecasting pipeline uses the same platform to go from raw sensor data to operational dashboards."

If you don't have the breadth to zoom out, hand up to management: "Let me bring [senior person] in — they can speak to how this connects across the broader architecture." This is not failure. This is the hierarchy working correctly.

### When to Hand Up

| Situation | Action |
|-----------|--------|
| Audience wants strategic context you don't own | Hand to management |
| Question is about the commercial relationship | Hand to management |
| You're stuck and pushing through isn't working | Hand up immediately — delay costs more than the handoff |
| Audience wants breadth you can't credibly speak to | Hand to whoever can |

**The rule**: Handing up is a professional move, not an admission of weakness. Pushing through when stuck reads as evasion.

---

## Cultural Intelligence

### Why It Matters

- **Greetings** — "Merhaba" to a Turkish executive creates instant rapport
- **References** — Acknowledging their background shows you did homework
- **Sensitivity** — Avoiding cultural missteps prevents awkwardness

### What to Capture

| Element | How to Use |
|---------|-----------|
| **Languages** | Greeting in their language (if confident in pronunciation) |
| **Education background** | Reference their university or field |
| **Cultural background** | Awareness of customs, communication style |
| **Career highlights** | Acknowledge notable achievements |
| **Personal interests** | Connect if natural, don't force |

### Cautions

- **Don't overdo it** — One cultural touch is charming, five is creepy
- **Get it right** — Mispronounced greetings are worse than none
- **Keep it professional** — Personal info is for connection, not leverage
- **Respect privacy** — Only use publicly available information

---

## Handling NEW Executives

### The distinction that matters

Existing partnership equity transfers to **some** executives and not others. Knowing which is which is the single biggest presale calibration when the account is long-running.

| Carries partnership forward | Does NOT carry partnership forward |
|-----------------------------|------------------------------------|
| Long-tenured exec (> 2 years) whose remit overlaps your engagement | NEW to company (< 1 year) |
| Promoted from within (knows the relationship history) | External hire, especially from a competitor |
| Was personally involved in your prior wins | Inherited the vendor list but didn't choose it |
| Public track record of continuity ("build on what works") | Public track record of vendor rationalization or "fresh starts" |

The right column requires **demonstrate-from-scratch** posture. Relationship references land as "why should I care?"

### Why NEW executives are dangerous

1. **No relationship equity** — Your existing partnership means nothing to them
2. **Proving themselves** — May be aggressive, looking for quick wins to validate the hire
3. **Different preferences** — May prefer vendors from previous company
4. **Fresh perspective** — Will question "the way we've always done it"

### Adjustments

| Standard Approach | Adjustment for NEW Executive |
|-------------------|------------------------------|
| Reference partnership history | Focus on future value, not past |
| Assume goodwill | Earn trust from scratch |
| Lean on relationships | Demonstrate capability |
| "We know your business" | "We're here to understand your priorities" |

### What to Research

- Where did they come from?
- What vendors did they use there? (Read this with the political layer — it predicts preferences.)
- What did they accomplish in previous role?
- What are they trying to prove in new role? (This is the real interest signal.)

---

## Profile Maintenance

### Before Engagement

- [ ] Verify current role (check LinkedIn)
- [ ] Check recent news (last 30 days)
- [ ] Review recent LinkedIn activity
- [ ] Confirm attendance

### Red Flags to Watch

- Role changed since research
- Recent negative news
- Announced departure
- New to company since last contact
