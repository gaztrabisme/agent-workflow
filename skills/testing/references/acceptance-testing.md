# Acceptance testing with the client

How to prepare and run the tests the client accepts against, and assemble the evidence. Recording the signed outcome, waivers and change requests belongs to `delivery`: [acceptance execution](../../delivery/references/acceptance-execution.md).

## Acceptance criteria as test cases

Discuss the acceptance criteria with the customer, write them down in an executable form, and implement each as a test that uses the domain's language. [book:continuous-delivery], Creating Acceptance Tests (part 2). Acceptance testing is validation (are we building the right product), where the levels below it are verification against the specification. [book:hands-on-selenium-webdriver], Types of Testing

Decide acceptance by test cases passing against a list agreed in advance, plus a defect gate by severity. Do not make an aggregate accuracy percentage the pass condition while the measurement has not been run; report it beside acceptance with its sample size. (derived: EVOLUTION.md case 5)

For each acceptance case record: the criterion ID and wording as agreed, preconditions and who supplies each, the script steps, the pass condition, the evidence it produces, and the signatory. The structure and tracker belong to `delivery`; this module fills the script and evidence columns.

## Kinds of acceptance item

| Kind | Pass condition | Example |
|---|---|---|
| Demonstrated step | Binary: the step runs end to end on the agreed set, or it does not | A scanned document is detected, routed and shown in the review screen |
| Defect gate | Open defects by severity at or below agreed counts | No open critical or major defects |
| Reported figure | No pass or fail; published with method and sample size | Accuracy per class on the frozen set |
| Delivered artifact | Exists, versioned, matches its description | Runbook, measurement method, interface contract |

State on the page that no accuracy figure is claimed for a demonstrated step that has no answer key. (derived: EVOLUTION.md case 5)

## Entry conditions

List what must be true before acceptance opens, and record any condition not met against its owner. Typical entries: classes declared and set stratified; field list frozen; reference set complete, adjudicated and signed; configuration frozen; every script agreed step by step; findings from earlier sessions dispositioned; no open critical defect. (derived: EVOLUTION.md case 5)

When an input the client owes has not arrived, the step that depends on it is deferred with its reason recorded; it neither fails nor silently passes. List deferred steps at acceptance. (derived: EVOLUTION.md case 5)

## Dry run and binding run

1. **Dry run** — run every script and the full scoring on the frozen set, log findings, disposition each within the agreed window. Nothing is accepted or rejected here.
2. **Remediation** — one cycle for steps that failed.
3. **Binding run** — the same scripts and scoring on the same set and configuration. This run alone decides.

Configuration changes between the dry run and the binding run re-base the measurement; if any change is planned, name it in advance and say the binding run is scored on it. (derived: EVOLUTION.md case 12)

## Missed targets

Decide in advance what happens when a reported or committed figure is missed, and put each miss in exactly one bucket. If the system underperforms, it is reported as missed with its cause, beside any re-run, never silently replaced. If the client-supplied reference set was not delivered, the figure is reported as not measurable, not failed. If the field list, rules or suite changed after the run, the figure is re-based and both baselines are kept; no old run is re-scored against new rules. (derived: EVOLUTION.md case 1)

## Evidence pack

Every item in the evidence pack must name the task in the plan that produces it, and the check runs whenever scope is cut. When a producing task is removed, remove or re-home each promise that cites its output (in the plan, the deck and the contract) in the same change. The link lives in task descriptions, not in the dependency graph, so scheduling tools do not catch it. (derived: EVOLUTION.md case 7)

| Evidence item | Produced by (task ID) | Format | Where it is stored |
|---|---|---|---|

Typical items: the scorecard per class, the run log reconciling to the document list, the flag or finding log, the defect register, the deferral register, a recording of the scripted run.

## Ownership

The whole team owns the acceptance tests; acceptance tests written without developer involvement tend to be brittle, and a separate team owning them leads developers to ignore their failures. Developers must be able to run them in their own environment. [book:continuous-delivery], The Automated Acceptance Test Gate (part 2). Ownership is shared; judging the result is not: see [agents-and-independence](agents-and-independence.md).

## Rejections

A rejection must name the criterion it fails and the specific deficiency. A deficiency against an agreed criterion is a defect; a request for behaviour the criteria do not require is a change request. Both are recorded through `delivery`.
