# Non-functional requirements (NFR) catalog

NFRs are where enterprise and regulated deals are won or lost. Client docs almost always under-state them. Run every solution against this list early (Phase 2–3); each gap is either a design decision, a clarification question, or an assumption.

Use the **forcing questions** to pull the real requirement out of a vague one ("must be secure" → *what* exactly).

## Security & identity
- Authentication & customer identity provider; SSO; step-up/MFA for sensitive actions.
- Authorization model: RBAC, row/record-level access, least privilege.
- Secrets/key management; encryption at rest and in transit.
- Data masking/redaction; PII handling; **credentials/identity never flow through an LLM** (for AI solutions).
- Audit trail: what's logged, immutability, retention.
- **Forcing:** Whose data can each user see? What's the blast radius of a compromised component? What must be auditable for a regulator?

## Integration & API
*Usually the bulk of an enterprise solution's real work and risk — design it explicitly, don't hand-wave "we integrate."*
- Per system: documented API available? protocol (REST/SOAP/file/queue)? authentication (OAuth2 / mTLS / API key)? rate limits & SLAs of the back-end itself?
- Pattern per interaction: **synchronous** (real-time enquiry — balances, profile) vs **asynchronous / event-driven** (broadcasts, campaigns, updates). Don't make everything synchronous.
- Gateway/middleware: single secured entry, throttling, schema validation, caching, telemetry; **back-ends never exposed directly** (esp. never to an LLM — deterministic actions are typed tools behind the gateway).
- Resilience: retries, idempotency, circuit breakers, timeouts, graceful degradation when a back-end is slow/down.
- Data contracts & versioning: payload schemas, canonical models, how breaking changes are absorbed.
- **Forcing:** Which integration is real-time-critical vs can be async? What happens to the customer experience when system X is unavailable? Is each back-end's own throughput/SLA enough for your peak?

## Data residency & sovereignty
- In-country hosting requirement; region availability of each proposed service.
- Cross-border transfer rules; data-localization law.
- Private/hybrid vs public cloud; network isolation (VNet, private endpoints).
- **Split-region residency posture** (the fallback pattern when a load-bearing PaaS isn't GA in-region): keep **data-at-rest, application, and identity in-region**; run only the non-resident service (e.g. LLM inference) cross-region over Private Link — encrypted in transit, **no data stored** there — and commit to migrating it in-region when it becomes available. State this as a single posture sentence and repeat it as a callout on the deployment diagram; it converts the deal's residency blocker into a governed, time-bounded exception. (Validated on a regulated-market engagement where the required managed inference service was not generally available in the mandated region.)
- **Owned-infrastructure posture** — the sibling pattern, and often the *reason a deal is winnable* rather than a concession. When the client buys and owns the compute, sovereignty comes from ownership rather than region selection: models run on client-owned hardware on the client's premises, nothing leaves the site, and there is no per-token meter to forecast. The tradeoffs to state honestly are a one-time CapEx and a lead time (see `estimation-and-costing.md` CapEx/BOM), the client inheriting hardware lifecycle and failure risk, capacity that is fixed rather than elastic, and a self-managed upgrade path for models and security patches. Name who replaces failed hardware and against whose warranty — that question decides whether this posture is an asset or a liability in year two.
- **Forcing:** Where must the data physically live? Which proposed services are *not* available in that region — and what's the fallback?

## Compliance & governance
- Applicable regulators and named guidelines (don't accept "be compliant" — list them).
- Sector rules (financial advice licensing, health, etc.); the line the product must not cross without a human.
- Data-protection law (consent, classification, retention, right-to-erasure).
- Data lineage, model/content governance, approval workflows (for AI/data solutions).
- **Forcing:** Which specific regulation, which clause? What requires human-in-the-loop by law, not preference?

## Scale & performance
- Volume today and projected; peak periods; concurrency.
- Latency/throughput targets per interaction type; cost-at-scale (the number that breaks naive designs).
- **Forcing:** What's the peak, not the average? What does it cost at 10×? Which operation is latency-critical vs can be async?

## Availability & resilience
- SLA/uptime target; RTO/RPO; multi-zone/region; DR.
- Failure modes: graceful degradation, retries, circuit breakers, fallback paths.
- **Forcing:** What happens when a back-end is down? What's the cost of an hour of downtime to the client?

## Observability & operations
- Monitoring, logging, tracing, alerting; health & quality dashboards.
- For AI: quality/eval monitoring, drift, groundedness/accuracy tracking in production.
- Support model: hours, tiers, response/restore targets, on-site vs remote.
- **Forcing:** How will the client know it's working *right now*? Who gets paged, and against what SLA?

## Cost & commercial (technical drivers)
- CapEx vs OpEx; licensing/consumption model; what scales the bill.
- TCO over the contract term; cost levers (caching, quantization, tiering).
- **Forcing:** What's the unit economics per interaction/user? Which design choice is the biggest cost lever?

## Maintainability, portability, extensibility
- Modularity, lock-in/portability, standards-based interfaces.
- Future channels/use cases; how the architecture absorbs them.
- Skills/transfer-of-technology; client maker/admin enablement.
- **Forcing:** What's the cost of switching a component later? Can the client's team run and extend this?

## Accessibility & UX-level NFRs
- Accessibility standards; multilingual/localization correctness; channel consistency.
- **Forcing:** Which languages/locales, validated how? (For multilingual AI: validate on the client's *own* data, not benchmarks.)

---

**Output:** fold the resolved NFRs into the solution architecture doc; turn the unresolved ones into clarification questions or assumptions. An RFP response that addresses NFRs head-on reads as senior; one that only lists features reads as junior.
