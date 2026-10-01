# Non-functional Requirements

Select and prioritize quality requirements from the client’s business context. Define measurable targets and the architecture decisions, evidence, and operational implications that follow.

## Select client-relevant quality attributes

- The book starts with system quality goals and develops measurable fitness functions iteratively, rather than prescribing this exact NFR catalog workflow [book:software-architecture-metrics], Fitness Functions and Metrics.
- The book says to make broad quality goals measurable with an objective value, which sharpens a forcing question into a testable target [book:software-architecture-hard-parts], Using Fitness Functions.
- The book centralizes MFA support in a shared authorization framework; the rule also calls for naming the customer identity provider and SSO model [book:building-secure-reliable-systems], Using Advanced Authorization Controls.
- Specify authorization including role or record-level controls and least privilege [book:building-secure-reliable-systems], Least Privilege.
- The book covers encryption at rest and in transit, then warns that data can remain exposed during computation [book:zero-trust-networks-2e], When You Host Applications in a Public Cloud, How Can You Trust It?.
- The book requires sanitizing sensitive inputs before model processing; the rule adds a stricter prohibition on routing credentials or identity through an LLM [book:llm-security-playbook], The Role of Guardrails in an LLM Security Strategy.
- The book makes logs hard to alter and preserves an immutable trail of changes; the retention period still needs its own policy [book:building-secure-reliable-systems], Design Your Logging to Be Immutable.
- The book supports limiting each user to needed data and services; the blast-radius and regulator-audit prompts extend that security inquiry [book:building-secure-reliable-systems], Chapter 5. Design for Least Privilege.

## Quality attribute catalog

- The book tests third-party API latency and unavailability explicitly, adding failure behavior to the integration design [book:software-architecture-metrics], Fitness Functions: Integration Tests with Network Latency.
- The book calls out authentication, rate limits, and timeouts/retries at the gateway; the rule also asks for protocol and backend SLA details [book:mastering-api-architecture], What Functionality Does an API Gateway Provide?.
- The book favors asynchronous communication where fault tolerance matters, so select the communication pattern per interaction instead of making every call synchronous [book:software-architecture-hard-parts], Availability/Fault Tolerance.
- The book gives gateways authentication, rate limits, and telemetry responsibilities; validation, caching, and backend exposure still need explicit treatment [book:mastering-api-architecture], What Functionality Does an API Gateway Provide?.
- The book lists those resilience patterns for service communication; add idempotency as a separate requirement [book:mastering-api-architecture], Reliability.
- The book versions APIs and treats incompatible changes as a major release; the rule additionally asks for canonical payload schemas [book:mastering-api-architecture], Semantic Versioning.
- Ask which integrations must be real time, what happens to the customer when a back end is unavailable, and whether its capacity meets peak demand.

## Security and identity

- The book checks model availability by region; apply that check to every proposed service whose regional presence is load-bearing [book:azureai-102certificationessentials], Deploying Azure OpenAI.
- The book includes residency and locality in data policy; the rule also requires identifying applicable cross-border transfer and localization laws [book:data-governance-definitive-guide], The Enterprise Dictionary.
- When a required PaaS service is not available in-region, state the split-region posture, keep data, app, and identity in-region, restrict cross-region use to an encrypted unstored service over private connectivity, plan migration, and repeat the posture on the deployment diagram.
- For owned infrastructure, state that data stays on client premises and disclose CapEx, lead time, lifecycle/failure risk, fixed capacity, upgrade responsibility, and hardware replacement/warranty owner.
- The book records residency and locality requirements by data class; it does not specify the regional fallback architecture [book:data-governance-definitive-guide], The Enterprise Dictionary.
- The book calls for identifying applicable regulations and defining compliance; naming the regulator and guideline in this checklist makes that concrete [book:data-governance-definitive-guide], Chapter 8. Monitoring.

## Integration and API

- The book identifies legal demands for human oversight in AI systems; the sector-specific rules and exact legally required human steps are additions [book:building-reliable-ai-systems], 1.6 Why reliable AI systems matter now.
- The book calls for per-class access, retention, residency, and processing policies; consent and erasure obligations need separate detail [book:data-governance-definitive-guide], The Enterprise Dictionary.
- The book grounds data governance in lineage, quality, and classification during processing; it does not specify AI model or content approval workflows [book:data-governance-definitive-guide], Data Processing.
- The book requires identifying applicable regulations and their compliance meaning; asking for the clause and legally required human step adds precision [book:data-governance-definitive-guide], Chapter 8. Monitoring.
- The book makes concurrency and responsiveness explicit and distinguishes gradual growth from spike-driven elasticity [book:software-architecture-hard-parts], Scalability.
- The book relates response-time targets to active user load; define comparable targets for each interaction type and cost threshold [book:software-architecture-metrics], Is the fitness function static or dynamic?.
- The book separates spike capacity from ordinary growth; the ten-times cost and latency-critical questions remain client-specific [book:software-architecture-hard-parts], Scalability.

## Data residency and sovereignty

- The book turns user priorities into measurable service objectives; the rule adds recovery times, recovery points, site choices, and fallback requirements [book:site-reliability-engineering], Chapter 4. Service Level Objectives.
- The book ties availability to dependency failures, so capture what an unavailable backend does to the service and its users [book:building-secure-reliable-systems], Access Controls.
- An SLO quantitatively measures outage impact; asking the client for the financial cost of one hour adds a commercial input [book:site-reliability-engineering], Chapter 30. Embedding an SRE to Recover from Operational Overload.
- The book identifies gateway telemetry for observability; define alerts and health or quality dashboards for the client’s operating model [book:mastering-api-architecture], What Functionality Does an API Gateway Provide?.
- The book tracks semantic quality and system drift in production; the rule adds groundedness and accuracy measures [book:building-reliable-ai-systems], Principle 3: Monitor systems continuously.

## Compliance and governance

- The book uses metrics for alerts and historical views; it does not specify the client-facing health dashboard or pager owner [book:site-reliability-engineering], Monitoring and Alerting.
- The book distinguishes capital from operating expenditure within TCO; licensing, consumption models, and their cost drivers are added prompts [book:fundamentals-data-engineering], Total Cost of Ownership.
- The book uses workload-aware inference techniques such as quantization to manage cost and latency; contract-term TCO and tiering remain additional views [book:ai-engineering-huyen], Chapter 9. Inference Optimization.

## Scale and performance

- The book monitors cost per interaction in production; use client-specific unit economics and identify the design lever that moves them [book:building-reliable-ai-systems], Principle 3: Monitor systems continuously.
- The book warns that portability stops at cloud-native integrations, so name the switching boundary rather than promise blanket portability [book:fundamentals-enterprise-architecture], Example Architecture Decision.
- The book treats extensibility as adding functionality as a service context grows; it does not require committing every future channel or use case now [book:software-architecture-hard-parts], Extensibility.
- The book says enablement needs tools and training for its users; translate that into client administrator and maker coaching [book:fundamentals-enterprise-architecture], Enterprise Architecture Enablement.
- The book raises replaceability and vendor lock-in; estimating switching cost and the client team’s ability to run and extend are additions [book:software-architect-elevator], Planned Obsolescence.

## Availability and resilience

- The book uses WCAG success criteria as the accessibility baseline; locale correctness and cross-channel consistency need their own checks [book:practical-web-accessibility], 1. The Accessibility Problem.
- The book distinguishes benchmark scores from production reliability, supporting evaluation on representative client data [book:building-reliable-ai-systems], 1.1 From benchmarks to the real world.
- The book includes audience language fluency among localization inputs; define how each required locale will be validated [book:strategic-writing-for-ux], 6: Measuring UX Content Effectiveness.
- The book surfaces unstated context, assumptions, and dependencies; carry each NFR into the design or make its uncertainty explicit [book:software-architect-elevator], Architects Deal with Nonrequirements.

## Architecture assurance

- Define NFRs as measurable targets, then prioritize trade-offs among them [book:fundamentals-enterprise-architecture], Summarizing NFRs.
- Add architecture fitness functions to check that implementation preserves selected architecture characteristics [book:software-architecture-hard-parts], Architecture Fitness Functions.
- Define architecture fitness functions with acceptable quality values and a way to check them, automating the check where practical [book:software-architecture-metrics], Fitness Functions.
- Use FMEA to score failure likelihood and impact, calculate criticality, and record mitigations [book:fundamentals-enterprise-architecture], Chapter 5. Enable and Enforce.
- Run a proof of concept or pilot in the client environment to validate consequential architecture recommendations [book:fundamentals-enterprise-architecture], The Importance of Experimentation.
- Use consumer-driven contract tests for service integrations [book:software-architecture-hard-parts], Consumer-driven contracts.
- Version public APIs semantically and gate breaking changes with specification diffs [book:mastering-api-architecture], Semantic Versioning.
- Define service indicators, objectives, and agreements around user-visible behavior [book:site-reliability-engineering], Chapter 4. Service Level Objectives.
- Add data lifecycle policies for retention and verified destruction [book:data-governance-definitive-guide], Chapter 4. Data Governance over a Data Life Cycle.
- Design audit logging to resist alteration and retain an immutable change trail [book:building-secure-reliable-systems], Design Your Logging to Be Immutable.
- Require production AI evaluation with both automated metrics and human review [book:building-reliable-ai-systems], Principle 6: Build in evaluation from day one.
