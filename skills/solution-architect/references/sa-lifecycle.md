# Solution-Architect Lifecycle

Follow the presale work from intake through signed handoff. Scale depth to the deal and keep general project planning, signed-client execution, and implementation in their owning workflows.

## Presale scope and outputs

- For presale work, produce phasing, roadmap, sizing inputs, a risk register, and commercial framing inputs.
- Declare the deal shape in Phase 0 and read deal-shapes.md before using a workbook or pricing chain.

## Presale flow

- PMBOK supports scaling rigor to project criticality; applying the adjustment phase by phase and the start-light sequence are the rule’s operational detail [book:pmbok-guide-7e], 3.2. Why Tailor?.
- Let the human finish the full informal dump before asking structured questions [book:articulating-design-decisions], Chapter 4. Listen to Understand.
- Fill the engagement frame slots for outcome, baseline, stakeholders, trigger, decision process, constraints, relationship, and personal success.
- Name the negative space, including what could cause a loss, what was not requested, and who loses if the work succeeds.
- Promote an opportunity only when it has a named beneficiary, observable outcome, access path, and definition of done; park the rest with one named dependency. For factory or OT opportunities, start with instrumentation already available; phase work that needs client-built hardware after a pilot on what exists. (derived: dogfood 2026-10-01)
- Keep damaging sensitive inferences internal with a named holder; never share them or use them as stated justification.
- Declare the deal shape and ID spine during intake.
- The book says to define the specific audience, the action they should take, and the communication medium before creating the message [book:storytelling-with-data], Chapter 1: the importance of context.
- Open an ask ledger that quotes the ask, lists matching artifacts, and marks extras as proposed with a named consumer and decision.
- Ask what business outcome changes and establish its baseline [book:fundamentals-enterprise-architecture], Align on the Why.
- Identify the trigger for acting now [book:fundamentals-enterprise-architecture], Align on the Why.
- The book says to map affected people, decision authorities, and subject experts, then prioritize them by influence and importance [book:fundamentals-enterprise-architecture], Align on Who.
- Identify who loses discretion if the project succeeds.
- Test which candidate opportunities are finishable before treating them as projects.

## Phase 0 — Intake

- Produce an engagement frame with the problem, sponsor, evaluation criteria, constraints, and engagement type.
- Hand back what was decided with assumptions, no more than five ranked asks, dated proposed deliverables, and pushback; a question list alone is not a deliverable.
- Skip intake only when work starts from a formal document, while still tiering claims and naming negative space in surrounding context.

## Phase 2 — Clarify

- Restate the problem in the client's business outcome terms before architecting; if unable, continue framing [book:fundamentals-enterprise-architecture], Align on the Why.
- Extract requirements and distinguish functional from non-functional requirements using the NFR checklist. Requirement discovery must also uncover unstated context, assumptions, and dependencies beyond an explicit checklist [book:software-architect-elevator], Architects Deal with Nonrequirements. Inventory fields on client-supplied forms and mockups, then trace each to the requirements matrix or the exclusions. (derived: dogfood 2026-10-01)
- Separate questions only the client can answer from decisions that can be resolved or routed internally.
- Order clarification questions with business and domain matters first; put logistics last or route them internally.
- Surface and verify outside-in assumptions on the first call. Record an unanswered matter as a correctable assumption when needed to proceed, rather than turning every unresolved matter into a working assumption by default [book:meddicc], DISCOVERY.
- On multi-round engagements, carry questions and assumptions in the blueprint workbook and fold each answer into every affected sheet, status, assumption, and source-linked change log.
- Deliver client-facing clarification questions and an assumptions register, carried in the workbook on live engagements.

## Phase 3 — Architect

- Identify how the client evaluates responses and map later win themes to those criteria [book:meddicc], QUALIFICATION.
- The book says to map impacted groups, approvers, and experts by influence and importance because some stakeholders can block the outcome [book:fundamentals-enterprise-architecture], Align on Who.
- Capture budget shape, residency, regulation, existing stack, timeline, and required integrations as hard constraints. The book calls for decision context, goals, constraints, and alternative analysis; these named categories elaborate the constraint set [book:fundamentals-enterprise-architecture], Architecture Decision Deliverable.
- Compare two or three viable options on client-relevant axes, recommend one, and explain why the alternatives lost. The book sets two as the minimum and recommends aiming for three to five, so this workflow's range is narrower [book:facilitating-software-architecture], Chapter 6. Architectural Decision Records.
- Describe the reference architecture in layers and treat its written explanation as authoritative. The book sets context, component, and deployment views as minimum content; add data and sensitive key-flow views when needed [book:fundamentals-enterprise-architecture], Application Target Architecture Deliverable.
- Use drawio for architecture diagrams when the client mandates an architecture demo.
- Design integration, identity/access, residency, and other NFR cross-cuts explicitly; do not hand-wave integration. For multi-tenant SaaS, establish tenant and admin identities, authentication, and tenant context in the foundation from day one [book:building-multi-tenant-saas], Build Your Multi-Tenant Foundation on Day One.
- Ground domain decisions in the Knowledge Base and record the grounding line.
- Keep architecture vendor-neutral until a separate positioning step maps capabilities to a stack with trade-offs. Compare options beyond vendor names and feature lists before selecting a stack [book:software-architect-elevator], Measuring an Architect’s Value.
- Produce the solution architecture document and options/decision records [book:fundamentals-enterprise-architecture], Application Target Architecture Deliverable.
- Classify the engagement as RFI, RFP, or direct brief because the class changes commitment and clarification strategy.

## Phase 4 — Plan and estimate

- Phase delivery for value and risk, leading with the lowest-risk, fastest-value slice and ensuring each phase stands alone and de-risks the next. Head First PMP frames adaptive increments around stakeholder value; it does not make this ordering a universal rule for every phase [book:head-first-pmp], Adaptive.
- Size work with a WBS, roles, effort ranges, and assumptions; state uncertainty drivers and a declared distribution multiplier. The architect supplies scope and technical cost drivers; the delivery planner owns and returns effort ranges. Include per-environment cloud costs for proposed environments, and AMS tiers with a retainer floor when recurring support is in scope.
- Before Phase 5, send the WBS with effort blank to the delivery planner and wait for the estimate when the client asks for price or payment terms. If one person serves in both roles, run the planner's presignature estimate as the delivery planner, label that role, and name the estimate owner. Do not mark the response ready while an explicit client pricing ask is unanswered. (derived: dogfood 2026-10-01)
- Maintain a risk register covering technical, integration, data, compliance, and adoption risks, with likelihood, impact, owner, and mitigation. Score failure criticality from probability and impact [book:fundamentals-enterprise-architecture], Chapter 5. Enable and Enforce.
- Reclassify risky demanded capabilities into separately priced readiness tracks or defer an unresolved implementation approach with the decision framed for the client.

## Phase 5 — Respond

- Challenger Sale recommends using customer-relevant insight to define the need before the RFP, then showing how the solution fits, rather than simply steering criteria toward supplier differentiators [book:challenger-sale], Step 2: The Reframe.
- MEDDICC advises defining absent criteria with the customer's Champion before using them as the basis for evaluation, rather than relying on inference alone [book:meddicc], CHAMPION.
- Audit source documents for duplicate references, contradictory figures, leaked scope, and template mismatch; raise findings as questions or stated conventions.
- Follow the client's required response structure and numbering exactly; if its template is mismatched, state a convention and proceed.
- Lead with an executive summary of the outcome and win themes, then tell a focused, audience-specific story with only the takeaways the evaluator needs [book:storytelling-with-data], Chapter 1: the importance of context.
- Include a traceability matrix mapping each requirement to its solution element, technology, and phase. The book requires forward traceability to satisfying design entities; technology and phase columns extend that matrix [book:swebok], Requirements Tracing.
- Map each win theme to customer pain and its supporting metric before connecting it to Phase 1 decision criteria [book:meddicc], COMPETITION.
- Fold every unconfirmed item into the assumptions register and expose important assumptions in a correctable, client-facing dependencies section when useful.
- Do not mark the response ready while an explicit client pricing or payment ask is unanswered; include a supported amount or a clearly labelled priced attachment with its owner and delivery date. (derived: dogfood 2026-10-01)
- Run the complete Final QA pass on every client-bound deliverable and export, using a reviewer who did not author it when possible.
- Run artifact-integrity checks as well as Final QA because they detect different defect classes.

## Phase 6 — Agree terms before signature

- Getting to Yes treats a stated constraint as a position whose underlying interests should be tested before accepting it as fixed [book:getting-to-yes], 3 Focus on Interests, Not Positions.
- Leave final pricing to the commercial or bid owner while the SA supplies technical cost drivers and commercial framing.
- Answer every pricing question in the response or explicitly defer it to a labelled priced attachment.
- The book requires user-valued outcomes in acceptance criteria; the per-outcome format, preconditions, and preparing-party fields are additions [book:continuous-delivery], Chapter 4: Implementing a Testing Strategy.
- Flawless Consulting treats client support and involvement as contract content, so record access, time, and participation alongside physical client deliverables [book:flawless-consulting], Elements of a Contract.
- Land the focal point, defect severities, acceptance deadline, T0, numeric volume caps, change-request rate, standby rate, and council membership before signature.
- Iterate criteria, preconditions, obligations, and contract terms until they converge before signature.
- Read acceptance/handover, change-request, IP, personal-data, and liability clauses against the solution architecture.
- Re-run artifact-integrity checks before signature.
- Skip contract and acceptance work while an enterprise bid remains unawarded, then revisit it when the bid converts.
