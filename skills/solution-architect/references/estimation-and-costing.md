# Estimation and Costing

Use this reference for presignature estimation inputs and commercial cost views. Effort is collected through `project`'s WBS from the leads who will be held to it; the solution architect supplies technical drivers, scenarios, and cost consequences for the response.

## Effort estimate ownership

- Have the leads who will be accountable for pre-signature effort author or confirm it; a draft made by the plan's drafter becomes an estimate only when its lead confirms it [book:head-first-pmp], Estimation tools and techniques. Do not author effort figures in the architect's role.
- On an RFI, stop at ranged effort with uncertainty drivers unless pricing structure was requested; leave price and detailed cost work to the commercial owner.

## Close-out feedback

- Use implementation feedback to revisit architecture; return estimate-versus-actuals, contested criteria, and slipped obligations to the presale references [book:software-architect-elevator], Measuring an Architect’s Value.

## Pricing model and scenarios

- Choose the pricing chain by deal shape: enterprise bid uses the blended-rate chain; fixed-price delivery uses per-phase lump sums plus applicable CapEx/BOM.

## WBS and uncertainty drivers

- The book describes scheduling WBS tasks with assigned resources; the requirement-reference and uncertainty-driver columns are additions [book:swebok], Software Engineering Management Tools.
- The book recommends range estimates grounded in calibrated historical data, expert judgment, or analogy rather than a fixed ±20% condition [book:swebok], 2. Software Project Planning.

## Effort distribution and uncertainty

- Treat bottom-up WBS effort as build effort and convert it to total delivery effort with an explicit distribution.
- Separate reclassified capability tracks and AMS/hypercare setup so they can be priced and dropped without disturbing the base.

## Cloud cost by environment

- Tie every cloud-cost row to a sizing driver and its corresponding volume assumption. The book ties resource scaling to tenant consumption activity and spikes; it does not prescribe a per-row cloud-cost worksheet [book:building-multi-tenant-saas], Chapter 3. Multi-Tenant Deployment Models.

## Estimate and pricing quality checks

- Include each multiplier’s rates and reasoning in a traceable estimate basis alongside its inclusions and exclusions [book:head-first-pmp], Basis of estimates.
- Present excluded effort as a named risk, not as savings to book.
- The book describes probability distributions for effort, schedule, and risk; this rule applies that guidance to estimation rather than a single multiplier [book:swebok], Software Engineering Management Tools.
- Do not assume a universal effort multiplier. The book recommends calibrated models grounded in historical data but does not prescribe a universal multiplier [book:swebok], 2. Software Project Planning.
- Apply the multiplier only to base build phases and state whether separately priced tracks are build-only or all-in.
- Convert total effort to man-months, multiply by the blended rate, then add out-of-pocket costs as a separate percentage line. The book translates resource requirements into cost estimates; it does not prescribe this blended-rate chain or separate out-of-pocket line [book:swebok], 2. Software Project Planning.
- When pricing scenarios, hold engineering scope fixed and vary only provisioning around it.
- Offer optimized, recommended, and full-spec provisioning scenarios where useful, and describe the physical difference in each row.
- Keep labor identical across provisioning scenarios and put any engineering-scope change in the WBS instead.
- The book calls for documenting positive and negative consequences of each option, rather than stating only the cheaper scenario’s saving [book:facilitating-software-architecture], Consequences.
- Estimate cloud costs with one worksheet per environment and one service per row.
- For each cloud service row, record layer, component, purpose, region, SKU, sizing driver, billing note, and monthly min–max.
- Use min–max ranges for usage-based cloud costs and report monthly and yearly ranges.
- Mark cloud lines that depend on client licenses or unconfirmed plans for verification.
- State BYOL or client-provided exclusions on each applicable line and repeat them as commercial assumptions.

For a delivery-shaped proposal, send the planner a task inventory with effort blank. The planner returns the effort model; the solution architect contributes technical drivers such as data volume, environments, regions, usage meters, and uncertainty. Keep the assumptions and cost scenarios visible beside any quoted option.

## Cost drivers and measurement

- Flag the dominant billing meter so the client can see what drives the bill. The book recommends correlating infrastructure consumption with tenant activity to reveal cost drivers, but does not prescribe a single dominant meter [book:building-multi-tenant-saas], The SaaS Mindset.
- Keep non-production rows aligned with production rows by zeroing inapplicable costs with a reason instead of deleting them.
- Offer Bronze, Silver, and Gold support tiers with their listed service levels, and recommend Silver content operations for AI quality sustainability.
- Define the actual included work and service additions for each support tier offered.
- Price discrete project work separately from retainer access, and state the access boundaries and expectations in the retainer terms [book:value-based-fees], ORGANIZING THE SCOPE AND MANAGING PROJECTS CONCURRENT WITH THE RETAINER.
- State a minimum monthly retainer floor and how effort above it is billed.
- Name the on-site escalation trigger and mark its commercial treatment TBC rather than silently absorbing it.
- State whether L1 support is in scope and attach a severity and SLA matrix.
- For on-premise, edge, and manufacturing work, include hardware in the price as a bill of materials.
- For each hardware item, record group, specification, quantity, unit price, tax, totals, source, and notes.
- Cite a procurement-verifiable source for every hardware price line.
- If no supplier quote is available, show a separate line labelled **Indicative range**, with its range, source, and date; identify the quote that will replace it before signature. (derived: dogfood 2026-10-01)
- Show pre-tax and tax-inclusive amounts separately.
- Add a numeric hardware contingency line and state whether subgroups also carry contingency.
- Price installation and mechanical work as explicit line items.
- State who funds or procures hardware, the ownership and warranty path, and who replaces failed units.
- State the residency consequence of client-owned on-premise hardware.
- PMBOK requires physical-resource lead-time planning; excluding hardware from the effort multiplier and recording it in the obligation register are rule-specific additions [book:pmbok-guide-7e], 2.4.5. Physical Resources.
- The book separates capital and operating expense types and describes their timing; the client still supplies the commercial comparison lens [book:fundamentals-data-engineering], Cost Optimization and Business Value.
- Present implementation and hardware as CapEx and cloud/AMS as OpEx, then use the client's preferred subscription or usage comparison lens. Compare the split with total ownership cost, including labor and resources [book:fundamentals-enterprise-architecture], Example Architecture Decision.
- Never choose an input assumption because it makes the estimate fit available capacity.
- When changing an assumption makes an estimate fit, state the assumption alongside the client's figure and re-derive the estimate.
- Do not calibrate productivity factors to close a capacity gap.
- Record the pre-adjustment number beside the changed input so readers can see when an estimate was targeted to capacity.
- When a total is cut to meet a price, the cut is shown as a price decision on the bridge, not as productivity; the per-feature margin view, tolerances and AI-assisted adjustment rules are in `project`'s [business case](../../project/references/business-case-and-tolerances.md) and [estimating](../../project/references/estimating.md) references.
- Recompute every total and currency conversion from raw cells before shipping.
- Scan numeric cost columns for range entries coerced into date-typed cells.
- Reconcile WBS effort, distribution, and priced man-months through one calculation chain.
- Verify effort units agree across summary and detail sheets.
- Read each summary label against the content and arithmetic it describes.
- Use one formula per concept across sheets rather than duplicate definitions.
- Investigate zero-priced rows with non-zero effort notes and remove the inconsistency before shipping.
- Reconcile every priced function with the current acceptance annex in both directions.
- Proofread client-facing feature names in the cost model before they propagate to other deliverables.
- Use Goal-Question-Metric to connect an architecture goal to questions and the metrics that answer them [book:software-architecture-metrics], The Goal-Question-Metric Approach.
- Attribute SaaS infrastructure costs to tenant consumption and activity [book:building-multi-tenant-saas], Chapter 3. Multi-Tenant Deployment Models.
- Compare technology choices with total opportunity cost of ownership [book:fundamentals-data-engineering], Total Opportunity Cost of Ownership.
- Prioritize architecture metrics by signal strength and collection cost [book:software-architecture-metrics], Prioritize Metrics and Devise a Data Collection Strategy.
- Build early predictive models from prior experience, comparable systems, benchmarks, or test results, and validate whether they are useful [book:software-architecture-metrics], Estimates and Models.
- Add a basis-of-estimates note listing the rates and reasoning behind quoted activity and project costs [book:head-first-pmp], Basis of estimates.
