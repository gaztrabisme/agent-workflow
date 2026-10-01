# Running acceptance

Acceptance is an execution record tied to the signed criterion spine. Prepare each criterion so the parties can run the agreed demonstration, decide what it showed, and record the outcome without replacing the contract language.

## Prepare and demonstrate each criterion

Before testing a criterion, confirm its preconditions, which party supplies each precondition, who prepares the demonstration, the test or demonstration method, the pass condition and the client signatory. A pass condition such as “works adequately” is not testable; raise it as an annex defect before building against it. [book:user-story-mapping], 3. Confirmation

Run user acceptance testing against the signed criteria in the sequence that moves each criterion toward a recorded acceptance. Triage defects by their agreed severity while the test is being run. [book:scrum-masters-path], Waterfall vs. Agile

Demonstrate working software to stakeholders each iteration. Use the demonstration to show what has landed and to expose promised work that did not; it complements the signed acceptance record. [book:user-story-mapping], Use Your Story Map During Delivery

The acceptance tracker is the test and traceability index. Keep the signed criterion wording and ID, its business outcome, related deliverable, demonstration or test method, and the evidence reference together. Trace each criterion back to its business case and forward to deliverables and test evidence. [book:head-first-pmp], Scope management: Doing the right stuff

Before freezing the signed criterion set, check that each criterion is clear, concise, verifiable, consistent with the other criteria, complete as part of the set, and traceable by a unique ID. [book:pmbok-guide-7e], 2.6.2. Deliverables

## Record acceptance and deficiencies

Obtain written confirmation from the relevant stakeholders that the deliverables match the requirements and project plan. A confirmation may cover more than one criterion; link it from each affected tracker row and retain the evidence that supports the result. Do not require a separate detailed test record or extra named signatory for every criterion unless the contract calls for it. [book:head-first-pmp], The stakeholders give you criteria for deciding when you're done

In the tracker, mark a criterion Accepted only when its written acceptance is recorded and supporting evidence is linked. Keep the relevant stakeholder's acceptance tied to the criterion ID; do not treat a remembered verbal approval as the record. [book:swebok], 5.1. Determining Closure

Accept completed criteria in batches during delivery. For a rejection, capture each specific deficiency and the criterion it fails. A vague rejection is not actionable: ask which concrete harm or unmet condition the client means, and record the itemised answer. [book:holacracy], Chapter 6: Facilitating Governance (5907 · U3 · L19 · 02:31–03:25)

If a deficiency is a failure against the signed criterion, link it to the defect record. If it asks for behavior the signed set does not require, raise a change request immediately rather than treating the new requirement as a defect. [book:swebok], 3.1. Requesting, Evaluating, and Approving Software Changes; [book:head-first-pmp], Is the product ready to go?

Use the contract's severity definitions where it provides them.

## Exceptions and formal waivers

When the contract requires a deviation or waiver for work that departs from a specified requirement, obtain written authorization through the agreed approval process before relying on it. A waiver records that a submitted nonconforming item is accepted as-is or after an approved rework; it is not an undocumented substitute for acceptance. [book:swebok], 3.3. Deviations and Waivers

For critical software or where the governing contract requires formal configuration audits, record the functional audit against the specification and the physical audit against the as-built product and its reference documentation. Treat a required successful audit as a prerequisite to establishing the product baseline. [book:swebok], 5.1. Software Functional Configuration Audit
