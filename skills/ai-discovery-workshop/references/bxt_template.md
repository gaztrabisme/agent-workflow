# BXT Template & Scoring Model

BXT = **B**usiness × e**X**perience × **T**echnology. The core prioritization framework. Every candidate use case must be scored.

## The 3 Pillars

### Business (Viability) — "Is it viable?"
- Clear, quantifiable revenue or cost reduction
- Efficiency gains, competitive advantage
- Durability of advantage; time-to-value prediction
- Strategic alignment with executive goals

### Experience (Desirability) — "Is it desirable?"
- Alignment with users' needs and preferences
- Impact on user experience and adoption likelihood
- Clear user persona (the "pilot" of the assistant)
- Change resistance assessment and mitigation

### Technology (Feasibility) — "Is it feasible?"
- Skill gaps and expertise requirements
- Integration challenges with legacy systems
- Model accuracy and reliability safeguards
- Natural extension of existing solutions

## Scoring Rubric (1–5 per pillar, 1 = Low, 5 = High)

Each candidate use case gets scored across:

| Dimension | Scored In |
|-----------|-----------|
| **Strategic Fit** | Business pillar |
| **Business Impact** | Business pillar |
| **User Desirability** | Experience pillar |
| **Technical Feasibility** | Technology pillar |

### Derived Scores

```
Business Viability Score  = (Strategic Fit + Business Impact)     / 2
Executional Fit Score     = (User Desirability + Technical Feasibility) / 2
```

## Prioritization Matrix (2×2)

Plot each use case on:
- **X-axis:** Degree of Executional Fit (1–5, low → high)
- **Y-axis:** Degree of Strategic Business Impact (1–5, low → high)

**Four quadrants:**

| | Low Executional Fit | High Executional Fit |
|---|---|---|
| **High Strategic Impact** | **Invest Long Term** | **Quick Wins** ← target these first |
| **Low Strategic Impact** | **Parked** (drop) | **Test & Learn** |

## BXT Use Case Template — Structure

**Page 1 of 2: General + Strategic Fit**

- Use case name
- Department
- Internal or external use
- Problem to solve (bullets)
- Use case description (bullets)
- Business objective
- Key results (KRs, measurable)
- Primary stakeholder accountable for OKRs (role, name, org/group)
- **Strategic Fit score** (1–5)

**Page 2 of 2: 3 impact assessments**

**Business viability — Strategic business impact assessment:**
- How does the use case align to the org's executive strategy?
- How does the use case generate business value?
- Business change management timeframe (1–3 mo / 4–6 mo / >6 mo)
- **Business Impact score** (1–5)

**Experience value — User desirability impact assessment:**
- Key personas
- How appealing is the overall value proposition for the user?
- Change resistance (Low / Medium / High, with mitigation)
- **User Desirability score** (1–5)

**Technical value — Feasibility impact assessment:**
- Implementation and operational risks
- Are sufficient safeguards available? (Responsible AI, RAG, model validation, etc.)
- AI/LLM fit (why generative, what value does it add)
- **Technical Feasibility score** (1–5)

## Illustrative Example — Factory AI Assistant (PDF pp 71–72)

### Page 1: General

**Use case name:** Factory AI assistant
**Department:** Product development
**Internal/external:** External

**Problem to solve:**
- New workers lack established knowledge held by others (inc. ability to program/configure machines to meet factory goals)
- Machinery breakdown and redirection costly, especially regarding time lost
- Less need to bring in specialists to solve equipment challenges
- Difficulty in quickly training new employees

**Use case description:**
- Provide frontline workers with a personal assistant for quickly identifying reasons for equipment malfunctions and path to resolution
- Frontline workers use natural language dialogue; always-on onboarding & upskilling
- The assistant can access training material, factory data, machine info

**Business objective:**
- Improve skillset of frontline workers
- Shorten time to diagnose and fix machinery
- Improve PLC code creation

**Key results:**
- Increase in worker productivity
- Decrease in downtime due to equipment malfunctions

**Primary stakeholder accountable:** Product and engineering leads / factory line managers
**Strategic Fit:** **4/5**

### Page 2: Assessments

**Business viability:**
- Aligns with corporate strategy of improving employee experience and digital transformation
- Higher quality, lower cost, faster time to resolution
- Faster time to value for frontline workers; increase production through quicker analysis and repair
- **Business change management timeframe:** >6 months
- **Business Impact:** **4/5**

**Experience value:**
- **Key personas:** Frontline factory workers
- **Value proposition appeal:** Medium — frontline workers continually look for areas to improve diagnostic and repair efforts
- **Change resistance:** Medium–high — workers need training on the assistant and are generally wary of tech changes
- **User Desirability:** **3/5**

**Technical value:**
- **Implementation risks:** Incorrect models/content (precision) could damage equipment or misdiagnose problems; data security and IP concerns
- **Safeguards:** Responsible use of AI (oversight, transparency, privacy); RAG
- **AI/LLM fit:** Faster & more accurate resolution; democratize domain-specific info through natural language
- **Technical Feasibility:** **4/5**

### Derived Scores for Factory AI Assistant

```
Business Viability Score = (4 + 4) / 2 = 4.0
Executional Fit Score    = (3 + 4) / 2 = 3.5
```

→ Plot: High Strategic Impact (4.0) × Moderate Executional Fit (3.5) → **Quick Win / edges into Invest Long Term**.

## Industry Scorecard Templates (PDF pp 73–76)

Appendix includes 4-pillar scorecards per industry showing:
- Column 1: **AI Transformation Offer Pillars** (Reinventing Customer Engagement / Enriching Employee Experiences / Reshaping Business Processes / Bending the Curve on Innovation)
- Column 2: **Metrics to track** per pillar
- Column 3: **3 Key Initiatives** per pillar with status (In Prod / On Track / At Risk / High Risk / Not started) and Core Pattern star
- Column 4: **Top-of-Mind Backlog Initiatives**

Industries included: Banking, Insurance, Retail and **Energy**. Pick the scorecard matching the client's sector and adapt the metrics — the pillars are stable across industries, the metrics are not.
