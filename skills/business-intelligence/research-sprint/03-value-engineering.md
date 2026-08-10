# Value Engineering & Business Case Research

## 1. Value Selling Fundamentals

**The spectrum:** Feature selling ("32GB RAM, M2 chip") -> Solution selling ("we diagnose your problem and prescribe a fix") -> Value selling ("this saves you 5 hours/week of rendering, worth $X/year to your operation").

Buyers now complete ~60% of their purchasing decision before talking to a rep. 35% of lost deals are due to "perceived poor value" -- not product fit, not price.

**The Value Hypothesis:** "We believe [solution] will deliver [quantified outcome] for [customer segment] by addressing [specific pain]." This gets validated or killed during discovery. The seed of every defensible business case.

---

## 2. Business Case Construction (CFO-Grade)

**Structure (3-7 pages):**

1. **Executive Summary** -- one page, "what, why, how much, when"
2. **Problem Statement + Cost of Inaction** -- the bleeding, quantified
3. **Strategic Alignment** -- maps to stated corporate priorities
4. **Financial Analysis** (make-or-break): NPV, IRR, payback period, break-even
5. **Sensitivity/Scenario Analysis** -- base, downside, severe. If downside still shows positive NPV, the case is robust
6. **Risk Assessment + Mitigation** -- top 5 risks with one-line mitigations
7. **Recommendation** -- approve / reject / investigate further

**Credible vs laughable:**
- Credible: Assumptions grounded in customer data or industry benchmarks, sensitivity analysis, conservative base case, risks acknowledged
- Laughable: Single-point estimates, benefits without methodology, no mention of what could go wrong, "projected 10x ROI" with no backing

---

## 3. TCO (Total Cost of Ownership)

**Formula:** TCO = Upfront costs + (Operating costs x Years) - Residual value

**Three buckets:** (1) Initial cost & installation, (2) Ongoing operation & maintenance, (3) Retirement/migration costs

**Hidden costs (where competitors cheat):** Data migration, integration rework, customization debt, shadow IT workarounds, switching costs at end-of-life

**How competitors manipulate TCO:** Low initial license but high implementation; excluding training/migration; comparing cloud Year 1 vs on-prem amortized 5 years; ignoring "cost of doing nothing" baseline

**Defense:** Always compare like-for-like time horizons (3-5 year TCO), include ALL cost categories for ALL options including status quo.

---

## 4. Value Quantification Framework

**Three tiers (in order of CFO trust):**

| Tier | Type | Example | CFO Trust |
|------|------|---------|-----------|
| 1 | **Hard savings** | Eliminate 3 FTEs ($285K/yr), reduce licensing $100K to $25K | HIGH -- shows on P&L |
| 2 | **Soft savings** | 20% productivity gain, 4hr/week per person, cost avoidance | MEDIUM -- requires conversion |
| 3 | **Strategic value** | Risk reduction, competitive advantage, speed-to-market | LOW unless quantified as risk exposure |

**The conversion trick:** Soft savings become hard when they eliminate a budget line. "20% productivity gain" is soft. "20% gain means we don't need to hire 5 planned FTEs = $475K avoided" is hard.

**The test:** "If a process owner is willing to book something into their budget, that's hard savings."

---

## 5. ROI Calculation Methods

| Method | Best For | Limitation | Audience |
|--------|----------|------------|----------|
| **NPV** | Gold standard, time value of money | Discount rate choice subjective | CFO, Finance |
| **IRR** | Comparing against hurdle rate (~12%) | Misleading for low-upfront | CFO, Board |
| **Payback** | Quick gut check -- "when break even?" | Ignores post-payback flows | Operations, BU |
| **Break-Even** | Unit economics, volume decisions | Doesn't capture full value | Sales, Product |

**Critical rule:** Never present "ROI = 340%." Present "ROI range: 180-340% depending on adoption speed (base case: 250%)." Sensitivity analysis should test 3-7 key drivers.

---

## 6. Value Engineering in Presale

**Discovery-to-value pipeline:**
```
Discovery Questions -> Pain Points -> Quantified Pain Statement -> Value Hypothesis -> Business Case
```

**Pain-to-Impact Chain:**
```
Surface symptom -> Root cause -> Business process affected -> KPI impacted -> Dollar value of KPI gap
```

**Quantified Pain Statement format:** "[Customer] is currently experiencing [pain] which costs approximately [$X/period] due to [root cause]. Addressing this through [approach] would recover [$Y/period] with confidence level [high/medium/low]."

**Key insight:** VE does NOT add to sales cycles -- it replaces weeks of customer self-assessment.

---

## 7. Outcome-Based Selling

**The chain:** Business goals -> KPIs -> Baseline measurement -> Target outcome -> Solution mapping -> Value realization tracking

**TSIA outcome framework:**
1. Customer states desired business outcome
2. Link outcome to financial results
3. Identify KPIs the customer monitors
4. Map business processes that must improve to move those KPIs
5. Then (and only then) present which capabilities drive those process improvements

---

## 8. The "Cost of Inaction" Framework

**Why it works:** ROI requires faith in future benefit. COI is already happening -- fact, not projection. "You're already losing $25K/month" hits harder than "you could save $25K/month."

40-60% of B2B deals are lost to "no decision." In 75% of stalled deals, reps failed to establish a quantified COI.

**The psychology (Kahneman):** Loss aversion means people feel losses ~2x more intensely than equivalent gains. COI leverages this directly.

---

## 9. Value Frameworks by Role

| Role | What They Care About | Value Message | Metric Language |
|------|---------------------|---------------|-----------------|
| **CEO** | Growth, market position, competitive advantage | "Accelerates entry into [market] by 6 months" | Revenue, market share, strategic alignment |
| **CFO** | Financial discipline, ROI, risk mitigation | "Reduces OpEx by $1.2M/yr with 14-month payback" | NPV, IRR, payback, risk-adjusted returns |
| **CIO** | Modernization, integration, security | "Consolidates 4 systems into 1, reducing attack surface" | Operational efficiency, uptime, complexity |
| **COO** | Process efficiency, productivity, quality | "Cuts order processing from 4 days to same-day" | Throughput, error rates, cycle times |

**Key insight (Gartner):** 94% of CIOs think they understand how tech impacts financials, but only 62% of CFOs agree.

---

## 10. Business Case Skeleton

```
BUSINESS CASE: [Project Name]
Prepared for: [Customer] | Date: [Date] | Confidence Level: [H/M/L]

1. EXECUTIVE SUMMARY
   Problem: [1-2 sentences, quantified]
   Proposed solution: [1-2 sentences]
   Investment required: [$X over Y months]
   Expected return: [NPV range, payback period]
   Recommendation: [Approve/Investigate/Reject]

2. CURRENT STATE (Cost of Inaction)
   Current process: [description]
   Annual cost of status quo: [$X] (direct $A + indirect $B + opportunity $C)
   Projected 3-year COI: [$X]
   Key pain points: [quantified pain statements]

3. FUTURE STATE (Proposed)
   Expected outcomes mapped to KPIs:
     KPI 1: [baseline] -> [target] = [$value]
     KPI 2: [baseline] -> [target] = [$value]
   Value breakdown:
     Hard savings: [$X] (source: [data])
     Soft savings (converted): [$X] (methodology: [how])
     Strategic value: [described, not dollarized unless defensible]

4. INVESTMENT REQUIRED
   Implementation: [$X]
   Year 1 operating: [$X]
   3-year TCO: [$X]
   TCO comparison: [proposed vs status quo vs alternative]

5. FINANCIAL ANALYSIS
   NPV (3yr, discount rate X%): [$range]
   IRR: [X-Y%] vs hurdle rate [Z%]
   Payback period: [X-Y months]

6. SENSITIVITY ANALYSIS
   | Scenario | Key Assumption Change | NPV | IRR | Payback |
   | Base     | As stated             |     |     |         |
   | Downside | [specific changes]    |     |     |         |
   | Severe   | [specific changes]    |     |     |         |

7. RISKS & MITIGATIONS

8. ASSUMPTION LOG
   [Every number traced to: customer data / benchmark / estimate]

9. RECOMMENDATION
```

---

## The Bridge: Verification to Creation

**Same rigor, constructive direction.** Every rule that catches a bad claim inverts into a template for a good one:
- "ROI claim needs a source" becomes "ROI template: [benefit] based on [source] with [confidence level]"
- The Assumption Log is the bridge -- verification asks "where did this come from?", creation asks "what source would make this defensible?"
- Confidence-graded claims: HIGH (customer data), MEDIUM (industry benchmark), LOW (estimate)

**Verification is the immune system. Creation is the skeleton.** They use the same knowledge of what "healthy" looks like.

---

## Essential Reading

| Resource | Why |
|----------|-----|
| *The Strategy and Tactics of Pricing* (Nagle, Muller, Gruyaert) | Gold standard on value-based pricing |
| *B2B Elements of Value* (HBR/Bain, 2018) | 40-element pyramid for B2B value |
| Value Proposition Canvas (Osterwalder) | Customer jobs/pains/gains mapping |
| PreSales Collective (presalescollective.com) | Best practitioner-level VE content for SEs |
