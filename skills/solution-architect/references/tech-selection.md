# Technology and Architecture Decisions

Compare options against the client’s problem, constraints, quality priorities, and change horizon before naming products. Keep decisions reviewable and ready for the response and engineering handoff.

## Reference architecture

- Use a documented pattern blueprint for the reference architecture; add decision options and only the integration, security, residency, and NFR views this engagement needs [book:fundamentals-enterprise-architecture], Architecture Pattern Deliverable.
- Show context, component, and deployment views, with the resilience, security, residency, and NFR details relevant to the proposal [book:fundamentals-enterprise-architecture], Application Target Architecture Deliverable.
- Identify dimensions entangled in this architecture instead of requiring a fixed five-to-eight axes [book:software-architecture-hard-parts], Chapter 15. Build Your Own Trade-Off Analysis.
- Build the shortlist from actual constraints and keep criteria neutral; avoid comparison charts fitted to a preselected result [book:software-architect-elevator], Chapter 6. Making Decisions.
- Use qualitative measures and compare their context-specific effects instead of treating numeric ratings as conclusive [book:software-architecture-hard-parts], Chapter 15. Build Your Own Trade-Off Analysis.

## Decision records

- Record major decisions with alternatives, rationale, consequences, and what the selected option binds [book:fundamentals-enterprise-architecture], Architecture Decision Deliverable.
- Use a factor-by-option matrix with pros and cons and a recommendation; the template does not prescribe separate design-time checks [book:fundamentals-enterprise-architecture], Sample Template.

## Decision methods

- Record each major decision with its context, choice, tradeoff, and rejected alternatives in wiki/decisions.md [book:software-architecture-hard-parts], Architectural Decision Records.
- Record the rejected option and why it lost so later sessions do not reopen a settled decision [book:fundamentals-enterprise-architecture], Overview.
- Preserve options by minimizing early decisions that are difficult to reverse when project knowledge is limited [book:software-architect-elevator], Reversing Irreversible Decision Making.
- Use bounded contexts and context maps to make business boundaries and integration relationships explicit [book:learning-domain-driven-design], Chapter 3. Managing Domain Complexity.
- Use a consistent architecture decision record with an identifier, description, stakeholders, status, date, problem, alternatives, rationale, and implications [book:fundamentals-enterprise-architecture], Overview.
- Codify proven architecture patterns as reusable, technology-agnostic designs or technology-specific implementation recommendations [book:fundamentals-enterprise-architecture], Architecture Pattern Deliverable.
- Use an architecture advice process that separates option making, decision taking, and decision sharing [book:facilitating-software-architecture], Chapter 3. Decisions at Scale.
- Record decision implications, including technical debt and risk [book:fundamentals-enterprise-architecture], Architecture Decision Deliverable.
- Choose architecture sketch viewpoints from the perspective being examined and indicate uncertainty [book:software-architect-elevator], Sketching Architectures.
- Classify subdomains as core, generic, or supporting before choosing where to invest bespoke design effort [book:learning-domain-driven-design], Chapter 1. Analyzing Business Domains.
- Manage each decision through draft, in-progress research and feedback, review, approval, and deprecation [book:fundamentals-enterprise-architecture], Managing the Architecture Decision Lifecycle.
- Give each architecture decision forum a clear charter, purpose, and chair [book:fundamentals-enterprise-architecture], Defining the Architecture Decision Workflow.
- Model only feasible combinations in a context-specific trade-off analysis, then compare their effects in a matrix [book:software-architecture-hard-parts], Analyze Coupling Points.
- Offer architecture options at different up-front costs and switching costs, accounting for uncertainty and vendor lock-in [book:software-architect-elevator], Strike Prices.
- Invite likely dissenters into decision review and record unresolved concerns as risks [book:fundamentals-enterprise-architecture], Managing the Architecture Decision Lifecycle.
- Keep an accessible, searchable and immutable ADR registry, linking deprecated records to replacements [book:fundamentals-enterprise-architecture], Providing an Architecture Decision Registry.
- Use MECE criteria to compare like-for-like alternatives and check that the decision space has no obvious gaps [book:software-architecture-hard-parts], MECE Lists.
- Use domain model language consistently in diagrams, writing, and speech [book:domain-driven-design-evans], Ubiquitous Language.
- Frame decision context around the circumstances, scope boundaries, and time horizon that make the decision necessary now [book:facilitating-software-architecture], Framing the Context.
- Record raw advice on an ADR with the advice giver’s name, role, and date alongside the decision analysis [book:facilitating-software-architecture], Advice.

## SaaS architecture choices

- The book directs architects toward options and trade-offs beyond product lists; this rule makes the Phase 3 design explicitly vendor-neutral [book:software-architect-elevator], Measuring an Architect’s Value.
- For workshop-originated deals, reuse the discovery skill's stack and commercial framing while keeping a neutral comparison visible.
- Start with business drivers and analyze the problem’s trade-offs before naming products [book:software-architecture-hard-parts], Chapter 15. Build Your Own Trade-Off Analysis.
- Compare alternatives against the real problem instead of shaping a score chart to justify a preferred option [book:software-architect-elevator], Chapter 6. Making Decisions.
- Do not use ratings without stating their reasons [book:fundamentals-enterprise-architecture], Overview.
- For SaaS proposals, compare silo, pool, or hybrid deployment models against current and emerging needs [book:building-multi-tenant-saas], Chapter 3. Multi-Tenant Deployment Models.
- Establish tenant identities, authentication, and tenant context in the SaaS control-plane foundation on day one [book:building-multi-tenant-saas], Build Your Multi-Tenant Foundation on Day One.
