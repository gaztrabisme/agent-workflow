# Convergence — the meeting point

Where parallel threads stop being parallel. This is the step that makes fan-out worth its cost, and the step most likely to be done badly, because it *looks* finished the moment every thread has reported.

**Declare the meeting point before dispatch, never after.** A fan-out launched without a named merger, a named artifact, and a rule for handling disagreement produces N good files and no answer. [book:agentic-mesh], Parallelization.

## The three ways it fails

1. **Stapling.** The threads are concatenated. Every finding survives; no finding *interacts*. The reader is handed the merge job you were supposed to do.
2. **Averaging.** Two threads disagreed and the merger smoothed it into a middle value nobody sourced. The disagreement was the most valuable thing the run produced and it is now gone.
3. **Losing the tail.** Headlines survive, the tail evaporates — the ⚠ traps, quote-required questions, unresolved uncertainties and how to monitor them, and a persona's unspoken objection. The tail is where the next failure is already written down. [book:critical-thinking-about-research], 10 Research Syntheses and Meta-Analysis.

## Who merges

**Not a thread author.** A stream agent merging its own findings against a rival's protects its own; a persona merging the register argues its own objection. Use the coordinator holding all threads, or a fresh agent given every thread and none of the reasoning. [book:agentic-mesh], Coordination and Operation.

Give the merger the thread *files*, not thread summaries. A summary of a summary loses exactly the tail described above. [book:facilitating-software-architecture], Gathering Advice.

## The merge, in order

### 1. Inventory
Every thread, what it covered, whether it completed. **A thread that died or was dropped is named here, not omitted** — silent truncation reads as full coverage.

### 2. Contradiction pass
Find every place two threads disagree. For each, do not pick quietly:

- State both claims and both sources.
- Compare source credibility and recency; use primary, official, and dated sources as useful signals, especially when a rule changes over time. For empirical claims, note the evidence design and use the field's evidence hierarchy as guidance, not as a mechanical verdict. [book:langchain-life-sciences-healthcare], Chapter 6. LangChain for Chemistry; [book:how-to-read-a-paper], The traditional hierarchy of evidence.
- **Name the winner and the reason** — one line, in the artifact. State opposing claims and test the reasons behind each one. [book:learning-systems-thinking], Strengthen the Reasons.
- If it is load-bearing and genuinely unresolvable from sources, it becomes a **quote-required** item with a named person to ask, not a guess.

A contradiction resolved silently is indistinguishable from one that was never noticed.

### 3. Interaction pass — the part that earns the fan-out

Findings that are individually true can change each other's meaning. Nothing in a single thread can see this, because each thread was scoped precisely so it couldn't.

For each pair of **load-bearing** findings and decisions across threads, ask how they relate to what came before and what may follow: *does A change what B means?* If an important coupling is unclear, use a small spike to test it. [book:learning-systems-thinking], Relationships Produce Effect; [book:facilitating-software-architecture], Examining the Interconnectedness of Decisions.

Two real ones from the cost-validation run:

- Hardware stream: *"the 4090 is EOL, last-stock only."* Budget: *"$4k box, month-3 purchase."* → Neither is wrong. Together they say the hardware line is a **timing** decision, not a price decision — buy inside the window or the number breaks. Neither stream could have said that.
- Channel stream: *"screening conversations are free in-window."* Business model: *"15k đ per screening."* → Together: the gross-margin claim in the investor document gets **stronger**, and the sentence hedging it should be rewritten.

This is O(n²) in principle and trivial in practice, because you only run it over the findings a decision rests on — usually five to ten. **Skipping it is the difference between a research dump and an answer.**

### 4. Diff against the assumption

The reader does not want to know what is true. They want to know **what changed.** Group by direction — *confirmed / cheaper / more expensive / newly discovered / now blocked / now unblocked* — against whatever the prior belief was. A synthesis that reads as a description of reality rather than a diff has failed its reader.

### 5. Carry the tail forward

Consolidate, do not drop: open quote-required questions with who to call · ⚠ traps for the downstream conversation · what remains uncertain and how it will be monitored · unspoken persona objections, verbatim. Keep risks visible and managed through the run. [book:continuous-delivery], A Risk Management Process.

### 6. Propose, don't apply — on anything that leaves the building

When the merge feeds a document that is client-, investor-, or contract-facing, produce a `was → proposed → why` table and route it to the accountable change authority or project change control board to approve, delay, or reject. Do not stop merely to have the client apply the proposed changes. [book:pmbok-guide-7e], 4.4.3. Meetings and Events.

Internal and reversible → apply, and say you applied.

## Artifact shapes by thread type

| Threads | Meeting point | Merge rule |
|---|---|---|
| Research streams | `VERIFY.md` + synthesis `README.md` beside the stream files | `task-force-protocol.md` |
| Personas | one ranked **objection register** | `persona-fanout.md` — never average |
| Options / approaches | one decision record: chosen, alternatives, **why each lost** | `wiki/decisions.md` [book:facilitating-software-architecture], Options |
| Build units | the branch, the passing suite, the gate rows | each unit's own gates; the coordinator does not re-judge them |
| Mixed | the artifact the *intent* named, with the others as inputs to it | the intent decides — say which in the Plan Block |

**Mixed is the common case**, and the failure is producing one artifact per thread type and no single thing the user asked for. If the intent was "a plan I can send the investor", the meeting point is that document — the register and the synthesis are inputs, not deliverables.

## Landing it

Convergence is not done when the merged artifact exists. It is done when the durable memory reflects it:

- `wiki/decisions.md` — what was chosen, what was rejected, **and which objections were consciously accepted**. An objection you decided to live with is a decision; one you forgot is a defect.
- `wiki/log.md` — the run ledger: threads dispatched, contradictions found and how resolved, every fork decided forward with its reason.
- `wiki/active-work.md` — every unit reconciled: done / deferred / blocked, and what is still open. Report and update status through the life cycle. [book:swebok], 4. Software Configuration Status Accounting.
- Artifacts on disk, at the paths named in the Plan Block.

### Decision and assumption records

For a consequential choice, keep a reader-facing decision record: status and date, accountable author and contact, context, options considered, why each unselected option lost, consequences, and advice. [book:facilitating-software-architecture], The Structure of an ADR; [book:facilitating-software-architecture], Consequences.

Maintain an assumption log for the whole run. Record assumptions and constraints, assign an owner to each unresolved item, and update it as evidence confirms, contradicts, or changes the premise. [book:pmbok-guide-7e], 4.6.2. Logs and Registers.

Carry the same run ID and stable unit IDs from the Plan Block into lane briefs, the goal file, verification, convergence, and the project log. This lets a reader reconstruct which dispatch, decision, and result belong together. [book:agentic-mesh], Explainable and Traceable.

### Failure learning

When a run has a material failure or recovery, link a blameless postmortem from the run ledger. Record impact, contributing conditions, recovery, and a named follow-up owner; use the history to prevent recurrence, not to indict a person or team. [book:site-reliability-engineering], Keep a History of Outages; [book:site-reliability-engineering], Chapter 15. Postmortem Culture: Learning from Failure.

Per `../../../core/references/wiki-protocol.md`. The rule that governs all of it: **the work not written down didn't happen** — and after a ten-agent fan-out, the amount of work that can silently not-have-happened is considerable.
