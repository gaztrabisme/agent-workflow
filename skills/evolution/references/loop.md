# The Evolution Loop

Evolution converts a used skill’s traces into a durable decision about changing that skill. The skill’s own history and future use form a feedback loop: experience informs the next thinking, and a later run checks whether the change helped. [book:learning-systems-thinking], Feedback Loops Include Learning

## Phase sequence

1. **Triage** — establish that there is evidence to examine and size the run.
2. **Settle** — for each selected skill, answer its eligible open verdicts before searching for new patterns.
3. **Harvest** — collect actual traces, not imagined use.
4. **Patterns** — explain repeated events and weigh their causes.
5. **Hypotheses** — write a specific change that could be shown wrong.
6. **Apply** — make approved changes in small reversible steps.
7. **Record** — write what happened, the new status and the next checks.

This is one numbered sequence. Validation is Phase 2 of a later run, not an eighth phase. [R039] A later use feeds experience back into the next evolution pass. [R045] [book:learning-systems-thinking], Feedback Loops Include Learning

## Triage and scope

A periodic capability assessment should name which parts of the process need improvement; settling yesterday’s edits alone is not a complete assessment. [book:swebok], Software Process Improvement Models

Scale the run to the request, severity and review capacity. A targeted, reversible one-skill trim can use the trace already supplied and proceed to a concise hypothesis and approval. A request to evolve every eligible skill needs the full loop. Prioritize by client value within schedule and resource constraints, then stage the work by review capacity; there is no fixed three-to-five skill limit. [R014] [book:swebok], Prioritization

Rank candidates against common value criteria. Impact divided by effort is a useful comparison, not the only legitimate one. [R018] A scope adaptation may omit activities that do not apply to the request. [R024] [book:swebok], Software Process Adaptation

For each negotiable change limit, agree an objective measure and use its evidence to govern negotiation reproducibly. A quantified error budget can expose the cost of risk and keep the choice from turning on politics, fear or hope. This does not authorize relaxing an integrity constraint. [R012] [R037] [book:site-reliability-engineering], Forming Your Error Budget

When a request would weaken a shared gate, record the conflict with the constraint, take it to the decision advisers, and explain the mechanism before acting. A proposed change that makes the evidence easier to fake weakens the loop even if it shortens the work. [R027] [book:facilitating-software-architecture], A single decision conflicts with a single principle

## Settle open records before new patterns

After triage selects a skill, read its most recent entry that still has open verdicts. Settle each eligible unchecked item and each `PENDING` verdict before harvesting new patterns. State the trace that exercised the change, or state that no eligible trace exists. [R015] [R031] [R041] [R061] [R062]

A run that only settles old verdicts is complete work. Do not create a new hypothesis just to make the run look productive. The first evolution dogfood found that 13 of 15 ledgers had never settled a verdict; that is why this phase runs before new pattern work. [R141]

## Harvest real use and find causes

Judge a change by what real user traffic does, not by imagined or simulated use. [R042] [book:site-reliability-engineering], Feature Flag Frameworks

A signal may trigger review, but the human decision maker retains judgment over whether it matters. [R082] [book:site-reliability-engineering], Symptoms Versus Causes

Look for the pattern behind repeated events, not just the event that was easiest to notice. Compare what recurs and what common feature links it; rank the forces that matter most. [R043] [R069] [R086] [book:learning-systems-thinking], Patterns Produce Events; [book:learning-systems-thinking], How Relationships Produce Effect

For commercial skills, analyze closed-lost deals to reverse-engineer missed qualification checks and promote recurring findings into the qualification checklist. [business-intelligence-R138] [book:meddicc], MEDDICC CHECKLIST

Keep role-specific evidence connected to the skill it can improve:

- For skills used in presales account work, review deal outcomes and debriefs; turn recurring lessons into changes to the method, positioning or gates, not only into deal notes. Capture lessons continuously as work proceeds, then consolidate recurring findings into the method. [R071] [business-intelligence-R003] [book:selling-to-big-companies], HOLD YOURSELF ACCOUNTABLE; [book:head-first-pmp], Exam Answers; [book:meddicc], MEDDICC CHECKLIST
- For skills used in signed engagements, compare estimates with actual effort by phase, contested criteria and obligation slippage. Feed ambiguous upstream guidance back to the skill that owns that guidance; record engagement-level learning in its own evolution entry. [R073] [delivery-R075] [book:swebok], 5.2. Closure Activities
- For skills distilled from workshops or other source methods, let real outcomes update the method and verify claims in the source artifact. Repeated conflicts between decisions and a stated principle signal that the principle may need revision. For authoring practice, use recurring conflicts between advice and later decisions to update reusable conventions and checklists. [R074] [R075] [book:facilitating-software-architecture], Keeping Principles Useful; [book:facilitating-software-architecture], Repeated conflicts between multiple decisions and a principle are a signal to change

For coordination methods, use run records and routing decisions to improve the protocol. Ways of working can change as learning accumulates. [R076] [book:pmbok-guide-7e], 2.5.8. Learning throughout the Project
- For a significant failure, turn the outcome into a preventive action that reduces recurrence; do not respond to one incident by merely changing triage weights. [R078] [book:site-reliability-engineering], Google’s Postmortem Philosophy

## Hypotheses and change size

Prioritize improvements by importance, discuss the priorities with the affected owners, and agree a plan. Smaller independent changes reduce overhead and give feedback sooner, so each change can be judged on its own. [R019] [book:site-reliability-engineering], Improvements and Refactoring; [R033] [book:facilitating-software-architecture], Benefits of reducing decision size

A hypothesis names one target file and one change. Do not bundle unrelated edits. Give the applied change a defined real-use incubation before judgment; validation belongs to a later run, never the day of application. [R033] [R034] [book:site-reliability-engineering], Production Tests

## Apply and preserve history

Use small, frequent check-ins that preserve behavior and can be reversed. A hypothesis is the review and traceability unit; it need not be exactly one commit. Keep the hypothesis identifier in the change record and check in small pieces to the skill’s mainline as they are ready. [R020] [R112] [R123] [R124] [book:continuous-delivery], Continuous Integration; [book:continuous-delivery], Essential Practices; [book:continuous-delivery], Prerequisites for Continuous Integration

Before applying a change, know the path back to the last known-good revision. [R115] [book:continuous-delivery], Rolling Back Deployments and Zero-Downtime Releases; [book:continuous-delivery], Essential Practices

Treat configuration and workflow changes as auditable state: record what changed, when, why, and how to roll it back, however small. [R128] [book:continuous-delivery], Managing Software Configuration

## EVOLUTION entry and verdicts

Do not finish a run until each touched skill has an on-disk `## Evolution N` entry with an honest status. [R026] [book:site-reliability-engineering], Keep a History of Outages

Every skill needs an `EVOLUTION.md` with a consistent section convention for new entries. Use the canonical shape for new entries, but leave older entries in their historical form; the triage reader handles both established forms. This common entry convention is provisional until a later dogfood validates it. [R046] [R047] [book:pmbok-guide-7e], 4.6.2. Logs and Registers

The initial ledger entry is part of authoring; later entries record trace-based evolution. A new or distilled skill stays `PENDING` until later real use validates it. [core-R036]

Use only these verdicts:

| Verdict | Meaning and evidence floor |
|---|---|
| `PENDING` | Applied or distilled, not yet proven; state why it remains open, name an owner and set a revisit date. |
| `KEEP` | At least two independent real tasks used the change without new friction. |
| `REVISED` | The mechanism is useful, but a selector must name the narrower context. The selector is itself `PENDING`. |
| `REVERT` | Evidence shows the change is wrong after scope, access and cost have been checked; record the failure mechanism and preventive action. |

Each record’s status must tell its reader where the decision stands. [R048] [R126] [book:facilitating-software-architecture], The ADR Lifecycle; [book:facilitating-software-architecture], Meta-Elements

Keep new changes `PENDING` until evidence settles them; never assign `KEEP` on application day. Independently verify critical results against an out-of-band source before trusting the change. [R049] [R034] [book:site-reliability-engineering], Trust but Verify

Before harvesting, set the evidence floor for each verdict class. Do not move it after seeing results. [evolution-C26] [book:critical-thinking-about-research], 4 The Sample

## Validation and non-adoption

Check non-adoption in this order:

1. **Scope:** was the result generalized beyond the context that produced it? If so, retain the useful mechanism and add a selector. For a sound but risky change, gate exposure to a limited context rather than discard it. [R056] [book:site-reliability-engineering], Feature Flag Frameworks
2. **Discoverability:** was the reference linked and findable? A path problem is not evidence that the practice is wrong. [R057] [R087] [R090] [R091]
3. **Weight:** did the process cost more than the case justified? State a lighter floor if cost caused the skip. [R058]
4. **Validity:** only now decide the mechanism was wrong. Revert it and write a postmortem that records the failure mechanism and the preventive action. [R059] [R052] [R054]

Use `REVISED` for the first three causes, with the selector still `PENDING`; reserve `REVERT` for the last. Preserve the old record and layer a new, linked decision on top of it. [R032] [R051] [book:facilitating-software-architecture], The ADR Lifecycle; [book:site-reliability-engineering], Google’s Postmortem Philosophy

A second engagement is especially useful for finding which earlier conclusions were context rather than general principle. Treat earlier conclusions as time-bound agreements that current circumstances may challenge. [R060] [book:facilitating-software-architecture], Repeated conflicts between multiple decisions and a principle are a signal to change

Use replay to test whether a specific change plausibly caused an outcome, while recognizing that production systems often cannot be reproduced exactly. Replay cannot establish discoverability because it already knows where the change is. A canary applies risky or structural changes to one skill or project before expanding them. [R067] [R068] [book:site-reliability-engineering], Effective Troubleshooting; [book:site-reliability-engineering], Production Tests

Assess changes against recurrence, user friction, whether the changed reference was actually opened, and whether the change introduced a new problem. [R069] [book:site-reliability-engineering], Production Tests

## Retrospective and maintenance

Define objective triggers before a run for a formal postmortem; write one for a significant undesirable event, and keep it blameless. The run review focuses on conditions, causes and preventive action, never on fault. Keep one formal retrospective per engagement. A short closing reflection may accompany every run. [R079] [evolution-C01] [evolution-C02] [evolution-C16] [book:site-reliability-engineering], Google’s Postmortem Philosophy

A significant failure should produce specific preventive actions, with an owner, and the follow-up should remain accessible until completed. [R021] [book:software-engineering-at-google], Blameless Postmortem Culture

Review and share completed learning records; an unreviewed postmortem does not complete the learning loop. Curate useful, settled records so later skill owners can learn from them. [R031] [R062] [evolution-C05] [book:site-reliability-engineering], Introducing a Postmortem Culture; [book:site-reliability-engineering], Disaster Role Playing; [book:facilitating-software-architecture], Introducing Architectural Decision Records

Keep periodic resweeps of prior guidance. Set an owner and revisit date on every open item; adjust the review frequency to how quickly the surrounding practice changes and how often the guidance is used. [evolution-C06] [book:facilitating-software-architecture], Updating Your Blips

Classify recurring, manual, automatable, tactical work with little lasting value as toil; separate it from overhead and work that creates durable improvements. Use the label to identify automation opportunities, not to dismiss necessary judgment. [evolution-C07] [book:site-reliability-engineering], Toil Defined

Removing a skill component that no longer adds value is useful maintenance; measure the value it provides rather than rewarding line or section count. [book:site-reliability-engineering], The “Negative Lines of Code” Metric

When a skill component no longer serves a purpose, name the replacement, provide a transition path, then remove or mark the obsolete component. Age alone is not a reason to deprecate it. [R089] [R106] [evolution-C34] [book:software-engineering-at-google], Chapter 15. Deprecation
