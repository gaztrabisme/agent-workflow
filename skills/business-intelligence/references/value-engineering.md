# Value Engineering

Build defensible business cases. This file bridges the skill's existing claims verification (catching overclaims) with the constructive side (building real value propositions).

**The bridge:** Every rule that catches a bad claim inverts into a template for a good one. Verification is the immune system. Creation is the skeleton. They use the same knowledge of what "healthy" looks like.

---

## Value Quantification

### Three tiers of value (in order of CFO trust)

| Tier | Type | Example | CFO Trust | Test |
|------|------|---------|-----------|------|
| 1 | **Hard savings** | Eliminate 3 FTEs ($285K/yr), reduce licensing from $100K to $25K | HIGH — shows on P&L | "Would the process owner book this into their budget?" |
| 2 | **Soft savings** | 20% productivity gain, 4hr/week saved per person, cost avoidance | MEDIUM — requires conversion to dollars | Can you tie it to a headcount, budget line, or avoided spend? |
| 3 | **Strategic value** | Risk reduction, competitive advantage, speed-to-market, compliance | LOW unless quantified as risk exposure | Can you quantify the probability x impact of the risk? |

### The conversion trick

Soft savings become hard when they eliminate a budget line:
- "20% productivity gain" = soft
- "20% gain means we don't need to hire 5 planned FTEs = $475K avoided" = hard

Always attempt the conversion. If it can't convert, label it as soft and don't pretend it's hard.

### Quantified Pain Statement

Format: "[Customer] is currently experiencing [pain] which costs approximately [$X/period] due to [root cause]. Addressing this through [approach] would recover [$Y/period] with confidence level [high/medium/low]."

**Pain-to-Impact Chain:**
```
Surface symptom → Root cause → Business process affected → KPI impacted → Dollar value of KPI gap
```

Example: "Manual data entry errors" → "No validation at intake" → "Order fulfillment" → "Error rate 4.2% vs industry 0.8%" → "$340K/yr in rework + returns"

---

## Cost of Inaction (COI)

**Why COI often works better than ROI:** ROI requires faith in a future benefit. COI is already happening — fact, not projection. "You're already losing $25K/month" hits harder than "you could save $25K/month."

40-60% of B2B deals are lost to "no decision." In 75% of stalled deals, reps failed to establish a quantified COI. Loss aversion (Kahneman): people feel losses ~2x more intensely than equivalent gains.

**Quantification method:**
1. Map current-state costs: financial + time + risk + opportunity
2. Project over 2-3 years — what does doing nothing actually cost?
3. Use discovery questions to make the prospect discover the number themselves (SPIN Implication questions)

---

## ROI Calculation Methods

Use the right method for the right audience. Never present a single-point estimate — always ranges.

| Method | Best For | When to use | Audience |
|--------|----------|-------------|----------|
| **NPV** | Gold standard — accounts for time value of money | Every serious business case | CFO, Finance |
| **IRR** | Comparing against corporate hurdle rate (~12% typical) | When the client uses IRR internally | CFO, Board |
| **Payback Period** | Quick gut check — "when do we break even?" | Always include alongside NPV | Operations, BU leaders |
| **Break-Even** | Unit economics, volume-driven decisions | When the engagement has variable costs | Sales, Product |

**Sensitivity analysis:** Test 3-7 key drivers. Present base / downside / severe scenarios. If the downside scenario still clears the hurdle rate, the case is robust.

**Benchmark targets:** SaaS payback 6-12 months; enterprise platforms 12-24 months acceptable if NPV is strong; NPV should exceed 25% of project cost as margin of error.

---

## TCO (Total Cost of Ownership)

**Formula:** TCO = Upfront costs + (Operating costs × Years) − Residual value

### Mandatory cost categories (for completeness)

| Category | Include |
|----------|---------|
| **Upfront** | Purchase/licensing, implementation, data migration, integration, training, infrastructure |
| **Ongoing** | Subscription/maintenance, support, internal admin, updates/upgrades, energy/hosting |
| **Hidden** | Customization debt, shadow IT workarounds, productivity loss during transition, context-switching |
| **Exit** | Migration costs, data export, switching costs, contract termination |

### How competitors manipulate TCO

| Trick | Defense |
|-------|---------|
| Low initial license, high implementation buried in SOW | Always compare 3-5 year TCO, not Year 1 |
| Excluding training/migration from comparison | Use mandatory cost categories for ALL options |
| Comparing cloud subscription Year 1 vs on-prem amortized 5 years | Like-for-like time horizons |
| Ignoring "cost of doing nothing" baseline | Always include status quo as an option with its own TCO |

---

## Value by Role

Same project, different value story. Tailor to the audience.

| Role | What They Care About | Lead With | Avoid |
|------|---------------------|-----------|-------|
| **CEO** | Growth, market position, competitive advantage | "Accelerates [strategic priority] by [timeframe]" | Technical details, architecture |
| **CFO** | Financial discipline, ROI, risk mitigation | "Reduces [cost] by [$X/yr] with [N-month] payback" | Vague "productivity gains" without numbers |
| **CIO/CTO** | Architecture, integration, security, technical debt | "Consolidates [N] systems, reduces attack surface" | Business platitudes, ROI claims they can't verify |
| **COO/Operations** | Process efficiency, productivity, quality | "Cuts [process] from [X days] to [Y hours]" | Strategic vision without operational detail |
| **Procurement** | Risk, compliance, TCO, vendor viability | Certifications, references, contractual flexibility | Feature pitches, product demos |

**Gartner stat:** 94% of CIOs think they understand how tech impacts financials, but only 62% of CFOs agree. The translation between technical and financial value is your job.

---

## Business Case Skeleton

Produce this when the engagement warrants it (not every quick meeting). Use customer data from discovery where available; flag assumptions by confidence level.

```
BUSINESS CASE: [Project Name]
Prepared for: [Customer] | Date: [Date] | Confidence: [High/Medium/Low]

1. EXECUTIVE SUMMARY (1 page)
   Problem: [1-2 sentences, quantified]
   Solution: [1-2 sentences]
   Investment: [$X over Y months]
   Return: [NPV range, payback period]
   Recommendation: [Approve / Investigate / Reject]

2. COST OF INACTION
   Current process: [description]
   Annual cost of status quo: [$X]
     Direct: [$A] — [breakdown]
     Indirect: [$B] — [breakdown]
     Opportunity: [$C] — [breakdown]
   3-year projected COI: [$X]

3. PROPOSED FUTURE STATE
   KPI 1: [baseline] → [target] = [$value/yr] (source: [data])
   KPI 2: [baseline] → [target] = [$value/yr] (source: [data])
   Value breakdown:
     Hard savings: [$X] — [source]
     Soft savings (converted): [$X] — [conversion methodology]
     Strategic value: [described, not dollarized unless defensible]

4. INVESTMENT REQUIRED
   Implementation: [$X]
   Year 1 operating: [$X]
   3-year TCO: [$X]
   TCO vs status quo: [$delta]

5. FINANCIAL ANALYSIS
   NPV (3yr, [X]% discount): [$low — $high]
   IRR: [X-Y%] vs hurdle [Z%]
   Payback: [X-Y months]

6. SENSITIVITY
   | Scenario | Assumption change | NPV | IRR | Payback |
   |----------|------------------|-----|-----|---------|
   | Base     | As stated        |     |     |         |
   | Downside | [specific]       |     |     |         |
   | Severe   | [specific]       |     |     |         |

7. RISKS & MITIGATIONS (top 5)

8. ASSUMPTION LOG
   [Every number: customer data (H) / benchmark (M) / estimate (L)]
```

### Confidence grading for claims

| Grade | Source | Use |
|-------|--------|-----|
| **HIGH** | Customer's own data (from discovery, financial reports) | Present with confidence |
| **MEDIUM** | Industry benchmark, analyst data, comparable deployments | Present with source citation |
| **LOW** | Estimate, extrapolation, limited data | Label explicitly as estimate, include in sensitivity analysis |

**Rule:** No claim in the business case without a confidence grade and source. This is the same discipline as claims verification, applied constructively.

---

## When to produce a business case

- **Full business case:** Large engagement ($100K+), multiple stakeholders, CFO involvement expected
- **Value summary (abbreviated):** Mid-size engagement, business-unit-level approval
- **COI only:** When the main barrier is "no decision" / status quo — quantify the bleeding, skip the full ROI
- **Skip entirely:** Quick meeting prep, conference follow-up, relationship-building engagement
