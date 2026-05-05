# Positioning

Frameworks for honest positioning — defense, opportunity reading, and swagger calibration.

---

## Philosophy

> **Aggressive where defensible, soft where provably false. Alert where interested.**

The goal is confidence backed by evidence, not bravado backed by hope. But confidence is only half the job — reading what the room wants is the other half.

- If you can defend it under cross-examination → **say it with confidence**
- If you can't defend it → **don't claim it**
- If it's uncertain → **build an escape hatch**
- If they're interested → **feed it, don't deflect it**

Over-preparing for defense without preparing for opportunity creates a defensive posture. The room reads this as insecurity.

---

## Trap Analysis

### What Is a Trap?

A trap is any claim that:
1. Sounds impressive but can't be defended
2. Invites follow-up questions you can't answer
3. References specifics that aren't in your demo/materials
4. Names standards, protocols, or integrations you can't explain

### Trap Categories

| Category | Example | Risk |
|----------|---------|------|
| **Specific Metrics** | "99.7% accuracy" | Will be asked how measured, what dataset |
| **Named Integrations** | "Integrates with SAP, Workday, Snowflake" | Will be asked to show it |
| **Standards/Protocols** | "Compliant with IEC 62443" | Technical expert will drill |
| **Client References** | "Deployed for [Company]" | May be asked for contact |
| **Capability Claims** | "Handles millions of transactions" | Will be asked for evidence |
| **Timeline Claims** | "Implemented in 6 weeks" | Context matters enormously |

### Trap Analysis Process

1. **List every claim** in your materials
2. **Categorize** by drillability risk
3. **Cross-reference** against what you can actually show
4. **Simulate hostile questions** from each executive
5. **Decide**: Keep (defensible), Soften (partial), Remove (indefensible)

### Decision Matrix

| Can You Show It? | Can You Explain It? | Decision |
|------------------|---------------------|----------|
| Yes | Yes | Keep with confidence |
| Yes | Partially | Keep with escape hatch |
| No | Yes | Soften or remove |
| No | No | Remove immediately |

---

## Escape Hatches

Pre-built deflections for uncertain territory.

### Universal Escape Hatches

| Situation | Escape Hatch |
|-----------|--------------|
| **Metric question** | "The specific numbers depend on your data environment. We'd scope targets during discovery." |
| **Integration question** | "The platform supports standard enterprise integrations. Specific configuration depends on your existing systems." |
| **Accuracy question** | "Accuracy depends on data quality and use case. We'd establish baselines with your data during pilot." |
| **Timeline question** | "Timeline depends on scope and environment complexity. That's a scoping conversation." |
| **Comparison question** | "Different tools solve different problems. We'd want to understand your requirements before comparing." |
| **Cost question** | "Pricing depends on scope and configuration. Happy to discuss in commercial phase." |

### Pattern: Acknowledge → Deflect → Redirect

```
"That's an important consideration. [ACKNOWLEDGE]
The specific answer depends on your environment. [DEFLECT]
We'd want to understand your requirements before committing to specifics." [REDIRECT]
```

### When to Use vs. When NOT to Use

- **Use when**: You don't know, it legitimately depends, question is premature, you're being tested
- **Don't use when**: You know the answer (just answer it), overusing makes you evasive, question is fair and central

---

## Q&A Defense Frameworks

### Technical Lead (HIGH RISK)

**Defense Approach**: Be honest about unknowns, use precise terminology, acknowledge complexity, offer deeper technical session.

| Question | Defense |
|----------|---------|
| "What protocols do you support?" | "The platform supports standard industrial protocols. The specific implementation depends on your OT environment and security posture." |
| "How do you handle [edge case]?" | "That's environment-specific. We'd want to understand your architecture before proposing how we'd handle it." |
| "Show me [specific feature]" | "Happy to do a deep-dive session focused on that. Today's overview is higher-level." |

### CIO/CTO (HIGH RISK if NEW)

**Defense Approach**: Focus on business outcomes, acknowledge strategic context, don't oversell. If new: earn trust, don't assume it.

| Question | Defense |
|----------|---------|
| "What have you delivered for us?" | "Today we're showing platform capabilities. The specific delivery history is better discussed with your team who manages the engagement." |
| "How does this fit our architecture?" | "We'd want to understand your current architecture before proposing integration patterns. The platform is designed for flexibility." |
| "Why you vs [competitor]?" | "Different solutions have different strengths. We're here to show what we can do; the comparison is yours to make." |

### Procurement/Finance

**Defense Approach**: Ready with value evidence (not ROI promises), acknowledge commercial discussions are separate, don't commit to indefensible numbers.

| Question | Defense |
|----------|---------|
| "What's the actual ROI?" | "ROI depends on your baseline and how it's configured. We can help you build a business case during scoping." |
| "What guarantees do you offer?" | "Performance commitments are scoped to the specific engagement. That's a commercial conversation." |
| "How does pricing work?" | "Pricing depends on scope and configuration. Happy to discuss in the next phase." |

### Operations/Business

**Defense Approach**: Focus on how it works (not architecture), acknowledge change management, show you understand their reality.

| Question | Defense |
|----------|---------|
| "How long until we see value?" | "Time to value depends on scope and data readiness. We typically see initial results in [range], but we'd scope specifically for your situation." |
| "Will our team be able to use this?" | "The platform is designed for business users. Training and adoption support is part of implementation planning." |
| "What happens when it breaks?" | "Support model is scoped to the engagement. We can discuss SLAs and escalation paths in commercial phase." |

---

## Swagger Calibration

### The Problem

Too defensive = weak, uncertain, doesn't inspire confidence
Too aggressive = arrogant, unbelievable, invites attacks

### Calibration Guide

| Situation | Swagger Level | Example |
|-----------|---------------|---------|
| Proven capability, can demo | HIGH | "The platform handles this. Let me show you." |
| Capability exists, can't demo | MEDIUM | "We've done this for similar clients. Happy to discuss specifics." |
| Capability is configurable | MEDIUM | "The platform supports this. Configuration depends on your environment." |
| Capability is roadmap | LOW | "That's on our roadmap. We can discuss timing if it's a priority." |
| Capability doesn't exist | HONEST | "That's not our focus. We'd want to understand why it matters to you." |

### Swagger Phrases (Calibrated)

**High Confidence** (use when defensible):
- "The platform handles this."
- "Let me show you."
- "This is what we do."

**Medium Confidence** (use when mostly defensible):
- "We've done this for clients in similar situations."
- "The question is not whether it works, it's how we configure it for you."

**Low Confidence** (use when uncertain):
- "That depends on your specific requirements."
- "That's a scoping conversation."

**Honest Limitation** (use when can't do it):
- "That's not our core focus."
- "We'd partner with [X] for that."

---

## Demo-Specific Defenses

### When Demo Data Is Dummy/Illustrative

> "What you're seeing is the dashboard structure. The specific values are illustrative — in production, these populate from your operational data."

If called out:
> "Correct, these are placeholder values in the demo environment. Production shows meaningful percentages based on actual data quality."

### When Feature Isn't Shown

> "That's available in the platform — today's demo is focused on [X]. Happy to do a deep-dive on [Y] in a follow-up session."

### When Demo Breaks

> "As you can see, the demo environment is [light acknowledgment]. The architecture you're seeing is production-grade — this is just demo infrastructure being temperamental."

---

## Closing Swagger

### Weak Closings (Avoid)

- "We hope we can be useful."
- "Let us know if you're interested."
- "Features are properly covered."

### Strong Closings (Use When Earned)

- "The question is not whether this works — you've seen it running. The question is how we configure it for your environment."
- "We can accelerate what you're already building."
- "If what you've seen today is worth a closer look, we're ready for a deeper conversation whenever you are."

### Calibration Check

Before using a strong closing:
- Did the demo actually work?
- Did you handle questions well?
- Is the audience engaged?
- Have you earned the right to be confident?

---

## Capability Map

The positioning tool that forces honesty before it forces cleverness. A capability map states — side by side — what the client needs, what you can credibly address, and what you cannot. The Gap column is the load-bearing column.

### Format

| Client Need | Our Fit | Gap |
|-------------|---------|-----|
| [Specific need, evidence-backed — not invented] | [What we have that credibly addresses it] | [What we don't cover, honestly stated] |

### Why the Gap column is the point

A capability map without gaps is a pitch deck. A capability map with gaps is a positioning document. The difference matters because:

1. **Gaps you acknowledge before the room acknowledges them are repositioned as scope, not weakness.** "Not in this phase" is a different conversation than "we can't do that." You only get the first framing if you raised it first.
2. **Gaps flag partnership or phasing opportunities.** If the Gap column is empty, you're either lying or you're the only vendor they need — and if you're the only vendor they need, the sale shouldn't require this much intel work.
3. **Gap honesty earns trust on the rest of the map.** A client who reads a credible Gap column trusts the Our Fit column. A client who reads a Gap column full of euphemisms treats everything as spin.

### Building the map

1. Start from **Client Need**, not from your feature list. Pull needs from the Pain Points research track — each should have evidence attached.
2. For each need, write **Our Fit** as what you can actually demo or defend today, not what's on the roadmap.
3. For each need, write **Gap** as the honest negative space — what you can't cover, what needs phasing, what requires a partner, what's unverified.
4. **No need should map to "100% fit."** If it does, either the need is too coarse (decompose it) or the Fit is overclaim (soften it).

### How the map feeds other outputs

| Column | Feeds |
|--------|-------|
| **Client Need** | Pain point prioritization in the Intelligence Report |
| **Our Fit** | Core pitch content — what to lead with on stage |
| **Gap** | Negative Space (what not to claim) + Honest Q&A Table (how to frame when asked) + phased scoping conversation (what's in a later phase) |

---

## What Competitor CANNOT Do

A disciplined framing tool for competitive positioning. For every named competitor likely to come up in the room, produce **one defensible sentence** describing a structural limitation they can't resolve without changing what they are.

### Why this is the discipline, not the slogan

It's tempting to write "we're better than Competitor X at Y." That's useless — every vendor deck says that. What's defensible is a *structural* limitation: something the competitor cannot do *without becoming a different company*.

Structural limitations look like:

| Structural pattern | Example shape |
|--------------------|---------------|
| **Architectural** | Their product is X-type; they cannot deliver Y-type outcomes without a ground-up rewrite |
| **Business model** | Their pricing model monetizes per-seat; they cannot deliver outcome-based pricing without cannibalizing their core |
| **Scope** | They're a platform provider; they don't deliver engineering services, so the last-mile is on the client |
| **Maturity** | They're a point solution; they don't integrate across the data layer |
| **Partnership posture** | They compete with the client's other vendors; they can't play the ecosystem role the client needs |

### Format

| Competitor | What They Cannot Do | Why (Structural Reason) |
|------------|---------------------|-------------------------|
| [Named competitor in the room] | [One defensible sentence] | [The structural reason — architecture, business model, scope, maturity, ecosystem] |

### Rules

1. **One entry per competitor.** If you have five, you're grasping. Pick the one that matters.
2. **Structural, not circumstantial.** "They haven't won a deal in energy" is circumstantial — they could win one tomorrow. "Their platform doesn't run on-premise" is structural.
3. **Defensible under technical cross-examination.** If a technical lead from the client presses, you must be able to explain the mechanism behind the limitation.
4. **Never volunteered unprompted on stage.** This is ammunition for Q&A and scoping conversations. Leading with competitor attacks makes you look insecure.

### Using it in the room

- **When a client asks "why you vs. [competitor]?"** — answer with your own differentiators first, then name one thing the competitor structurally can't do. Don't chain multiple.
- **When a competitor just won an adjacent deal** — acknowledge, then pivot to the structural limitation that applies to *this* client's context.
- **When a technical lead is benchmarking** — the structural limitation is what they'll remember after the meeting, when the vendor shortlist discussion happens internally.

### How this output feeds Negative Space

If a competitor structurally cannot do X, you **can** talk about X confidently. If a competitor structurally *can* do X and does it well, X belongs in the Negative Space — don't raise it for them.

---

## Honest Q&A Table

The most actionable output format for live prep. Replaces narrative defensive briefs.

### Format

| Topic | Reality | Honest Response |
|-------|---------|-----------------|
| [Claim area] | [What's actually true — internal, not for sharing] | [Verbatim words to say in the room] |

### Why This Format Works

- **Reality column forces honesty during prep** — you can't write a good response without first admitting what's true
- **Response column gives you words under pressure** — when your brain freezes in the room, you have a sentence ready
- **Table format is scannable** — find the topic, read the response, deliver it

### Building the Table

1. List every topic the audience might raise
2. For each: write the reality (be brutal — this is internal)
3. For each: write what you'd actually say (honest but positioned)
4. Test: would a technical expert accept this response? If not, soften the claim, not the honesty

### Example (from real engagement)

| Topic | Reality | Honest Response |
|-------|---------|-----------------|
| SCADA connectivity | MQTT gateway, not direct SCADA | "We connect through MQTT. For your specific SCADA setup, that's something we'd scope together." |
| Deployment status | Staging for energy client, can't share name | "This is deployed in staging for an energy client. We can't share the name, but the system is built and running." |
| Runs on their platform? | Never tested | "We haven't run it on [platform] specifically. Integration validation would be the first step of a pilot." |

---

## Negative Space

What NOT to present is as strategic as what to present. Getting this wrong (showing a capability they already have, showing to the wrong audience) costs credibility.

### Format

| Don't Present | Why |
|---------------|-----|
| [Capability/topic] | [Specific reason — they have it, wrong audience, overclaim, irrelevant] |

### How to Build

1. Run Product-Environment Fit analysis — anything classified as Overlap or Competition goes here
2. Run Claims Verification — anything classified as Overclaim without resolution goes here
3. Check audience — capabilities irrelevant to attendees' roles go here
4. Check competitor landscape — capabilities where a competitor is entrenched go here (unless you have a clear differentiator)

### The Rule

If you're not sure whether to show something, the default is don't. You can always bring it up later if the conversation opens to it. You can't un-show something that damaged your positioning.
