# BXT Template and Scoring

## AI suitability screen

Before BXT scoring, record `AI needed?` as `yes`, `uncertain`, or `no`, with a short reason and evidence. If the answer is `no`, describe the conventional option, remove it from the AI matrix, and hand it to solution-architect only if the client wants further design. Keep `uncertain` visible as an open question; any related scores stay provisional. (derived: dogfood 2026-10-01)

## BXT dimensions and their evidence

BXT is Business, Experience, and Technology. Strategic Fit and Business Impact belong in the Business view. [book:semantic-software-design], Business Design

Business Impact captures the value of the opportunity. [book:art-of-ai-product-development], Business impact

User Desirability captures whether the experience is wanted. [book:art-of-ai-product-development], Desirability

Technical Feasibility captures whether it can be implemented and operated. [book:art-of-ai-product-development], Technical feasibility

Use these four criteria for each candidate with a plausible AI role or an open AI-suitability question:

| Criterion | Dimension | Questions to record |
|---|---|---|
| Strategic Fit | Business | Which objective and executive strategy does it advance? What measurable result matters? Who is accountable? |
| Business Impact | Business | What value could change, for whom, and on what time horizon? What is the evidence? |
| User Desirability | Experience | Which users benefit? How appealing is the value proposition? What adoption concerns or resistance need to be understood? |
| Technical Feasibility | Technology | What data, systems, expertise, safeguards, and operational conditions are needed? What is still unknown? |

The source's prioritization criteria include user impact, business value, and technical feasibility. In this workshop, those ideas are captured in the four criteria above; keep the criteria coarse when the team lacks detail. [book:art-of-ai-product-development], 2.2.1 Defining your prioritization criteria

## Use-case assessment template and criteria

For each candidate that passes the AI suitability screen or remains uncertain, record:

- Name, business unit, internal or external use, and concise description.
- Problem in the client's words, affected workflow, and desired business outcome.
- Measurable key results and accountable stakeholder.
- Strategic Fit score and evidence.
- Business Impact: strategy alignment, expected value, change timeframe, score, and evidence. Discuss organizational benefit, return, and strategic alignment in general terms before filling the workshop's additional fields. [book:user-story-mapping], Have Conversations About Opportunities
- User Desirability: primary and secondary personas, user value, appeal, change resistance, mitigation, score, and evidence. Include affected workers and their role in a pilot, such as validating examples, reviewing outputs, or giving feedback; mark the role open if unknown. User trust and control concerns belong in the assessment. (derived: dogfood 2026-10-01) [book:art-of-ai-product-development], 10.1.1 Identifying the best opportunities for automation and augmentation
- Technical Feasibility: implementation and operational risks, available safeguards, fit for AI or an LLM, score, and evidence. Tasks vary in AI suitability; account for expertise, payoff, and risk. [book:art-of-ai-product-development], 10.1.1 Identifying the best opportunities for automation and augmentation

The business-and-data review starts by stating the business problem. The remaining fields here are the workshop's assessment structure. [book:data-science-for-business], Business and Data Understanding

## Scoring and prioritization

Rate each criterion from 1 (low) to 5 (high). [book:art-of-ai-product-development], 2.2.2 Deciding on the next opportunity.

Keep each rating distinct and attach a short evidence note, confidence mark, or open question. Do not average Strategic Fit with Business Impact to create a Business Viability score, and do not average User Desirability with Technical Feasibility into an Executional Fit score. Sum the individual criterion scores for a rough total if useful; the source aggregates by summing criteria. [book:art-of-ai-product-development], 2.2.2 Deciding on the next opportunity.

Use the 2×2 as a conversation aid. The workshop plots Executional Fit on the X-axis and Strategic Business Impact on the Y-axis. Place cases with the group using the agreed underlying evidence; do not present an averaged score as a formula-backed coordinate. [book:art-of-ai-product-development], 2.2.2 Deciding on the next opportunity

| | Lower Executional Fit | Higher Executional Fit |
|---|---|---|
| Higher Strategic Business Impact | Invest Long Term | Quick Wins |
| Lower Strategic Business Impact | Parked | Test and Learn |

The book's quick-win idea is high value, desirable, and reasonable effort; the four quadrant labels and this matrix are the workshop's field method. Investigate Quick Wins first when the evidence and client priorities support it, while treating each plotted location as provisional rather than a verdict. [book:art-of-ai-product-development], 10.1.1 Identifying the best opportunities for automation and augmentation

After scoring, use the matrix to surface the two or three candidates worth discussing next; it does not impose a hard cutoff. [book:art-of-ai-product-development], 2.2.2 Deciding on the next opportunity

If Business and Experience look strong while Technology remains weak or unknown, keep the case as a later option when payoff and evidence justify it instead of discarding it solely for uncertainty. Keep long-term opportunities visible for later. [book:art-of-ai-product-development], 2.2.3 Balancing quick wins vs. long-term investments

Only park or drop candidates with little hope of the desired outcome; record why. [book:user-story-mapping], Be Picky

## Worked example: Factory AI Assistant

The source example describes a frontline assistant for diagnosing equipment problems. It gives Strategic Fit 4, Business Impact 4, User Desirability 3, and Technical Feasibility 4. Record the four ratings separately and the total of 15/20; do not turn them into averaged pillar scores. The desirability score reflects medium appeal and medium-high change resistance, while technical notes include misdiagnosis, security, and IP risks. The numbers alone do not settle the choice: verify user adoption, safeguards, and the baseline for downtime before recommending a PoV. [book:art-of-ai-product-development], 2.2.2 Deciding on the next opportunity

## Industry scorecards

Use an authorized, current scorecard closest to the client's sector when one is available. Otherwise, use this compact pattern note (derived: dogfood 2026-10-01) and fill it only from client evidence:

| Industry pattern or client workflow | AI capability | Evidence or source | Measure | Status or open question |
|---|---|---|---|---|
| [client-described pattern] | [capability to assess] | [observation, data, or assumption] | [client-valued measure] | [current, consider, unknown] |

The book says prioritization criteria vary by company and context; derive them from the client's objectives rather than pretending this note is a sector-specific scorecard. [book:art-of-ai-product-development], 2.2.1 Defining your prioritization criteria

## Added practices for value and confidence

For a value discussion, compare plausible outcomes and their probabilities and values rather than presenting one unsupported point estimate. Expected value is an organizing frame; ask the client to supply or validate the ranges and assumptions. [book:data-science-for-business], A Key Analytical Framework: Expected Value

Ask what the current pain costs, including time, rework, delay, or missed outcome, and carry the client's estimate into the business case. [book:meddicc], Implicate the Pain

Add a separate confidence mark to each criterion so a high score based on assumption is visible. Define the confidence scale with the group and write down what evidence would raise confidence; confidence describes evidence quality, not the opportunity's value. [book:meddicc], MEDDICC SCORING
