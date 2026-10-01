# Triage — evidence, eligibility and scope

Triage produces a decision record, not an automatic ranking. Use signals together, keep their meaning visible, and leave the selection to the accountable human. [R081] [R082] [book:site-reliability-engineering], Symptoms Versus Causes

## Eligibility and assessment

A skill with no evidence of use since its last entry is excluded from a real-use evolution run. A missing ledger is an integrity gap to repair, but it is not evidence that a used skill should be changed. A skill excluded for no trace can re-enter only on evidence created after the exclusion; do not add it back because it seems stale. [R154] [R107]

A periodic capability assessment names processes to improve, but first establish which work is in scope. Do not turn age or open-item volume into a standalone reason to select a skill. Prioritize by impact and effort while keeping settleable validation debt visible. [R008] [R014] [R018] [R101] [R104] [R106] [R107] [book:swebok], Software Process Improvement Models; [book:swebok], Prioritization; [book:site-reliability-engineering], Do One Thing Well; [book:continuous-delivery], Metrics

Match the response to the signal’s impact. A small reversible trim may need only a narrow evidence review; a broad or high-impact change warrants the full loop and a wider review. Set the severity threshold before choosing the work. [evolution-C15] [book:site-reliability-engineering], Triage

For a quiet but important skill, schedule a bounded exercise such as a game day where it is safe to do so. Apply the skill to a real exercise task and label the evidence as exercise-derived: it can reveal gaps and friction, but it does not establish that the guidance is naturally discoverable in ordinary work. [evolution-C35] [book:hands-on-site-reliability-engineering], 3. Introduction to SRE

Minimize context switches: group related evidence gathering into sustained, single-purpose blocks. Do not impose a fixed count cap where review capacity and value provide the real constraint. [R104] [book:site-reliability-engineering], Do One Thing Well; [book:swebok], Prioritization

## Signals and how to read them

Measure stages of the work to find the actual bottleneck; prioritize that globally constraining stage, rather than automatically ranking validation debt first or sorting by local open-item volume. Put the next unit of effort where expected impact outweighs cost. What you measure steers behavior, so scrutinize the signal and the behavior it rewards. [R081] [R083] [R101] [R107] [book:continuous-delivery], Metrics; [book:site-reliability-engineering], Creating a Test and Build Environment

Useful evidence includes post-entry uses, friction or corrections, undigested changes, open verdicts that can now be settled, linked references that have not been opened, and new patterns. For each pick, name the trace that supports it. For each skip, state one reason. A stable skill with no needed change is not neglected. Treat age only as a tie-breaker; give recently changed work room for real use before judging it, and deprioritize a skill changed in the previous run when its only evidence is age. [R086] [R089] [R102] [R103] [R106]

Use a common measurement window that fits the expected signal. A zero count means zero observed events only inside that window. State the coverage dates and preserve source provenance. [R094] [book:site-reliability-engineering], Choosing an Appropriate Resolution for Measurements

Keep unlike measures separate. Report skill invocations and reference reads in separate columns; do not add them into a synthetic total. Interpret them together against the underlying question. For real-use independence, count distinct task identities, not transcript files or agent sessions: a parent task and its child sessions are one use, and multiple sessions on the same task are also one use. If two measures of the same signal disagree, investigate the disagreement rather than averaging away the difference. [R095] [R096] [R100] [book:software-engineering-at-google], Chapter 7. Measuring Engineering Productivity

Assess trace quality before a trace can support a pattern: note whether it is direct or inferred, complete, task-independent, and captured by a reliable source. Do not let a weak source carry a strong conclusion. [evolution-C25] [book:critical-thinking-about-research], 10 Research Syntheses and Meta-Analysis

## Discoverability and instrument limits

A canonical, linked home makes references easier to find. Check whether `SKILL.md` links the reference before interpreting its read count. [R057] [R087] [book:software-engineering-at-google], Establishing Canonical Sources of Information

A linked but unread reference may be undiscoverable or too costly; it is not automatically wrong. An unlinked and unread reference is an orphan: remove it only if it no longer serves a purpose, or link it where it is useful. An unread but intentionally wired diagnostic artifact may still have a purpose. [R090] [R091] [book:site-reliability-engineering], Monitoring; [book:software-engineering-at-google], Chapter 10. Documentation

Disclose the discoverability measure’s limits whenever you use it, and validate its intended signal with qualitative feedback such as experience sampling or user surveys. Ask whether the reference helped, rather than assuming the count answers that question. [R093] [evolution-C32] [book:software-engineering-at-google], Chapter 7. Measuring Engineering Productivity

The older read-once instrument had three material blind spots: its window began only when collection was installed; child-agent reads were attributed to the parent, so event counts—not distinct sessions—answered whether a file opened; and skill injection could use a skill without recording a direct file read, so zero reads on a skill entry meant nothing. A local path mismatch also once hid most reads: 566 of 759 entries came through a linked path. Reconcile alternate paths before calling a reference unread. These are instrument limits, not findings about a skill. [R093] [R095]

A current session may not yet be present in a stored manifest. Check what you know was used this turn before treating an apparent zero as exclusion evidence.

## Pattern questions

Use these questions to look for relationships before classifying a finding:

1. How does information flow, and how is it transformed?
2. What events happen, and what follows them?
3. What boundaries exist, and why?
4. What building blocks are reused and how do they relate?
5. How does delivery work, and how are priorities and quality handled?
6. How are people organized and connected?
7. How is discourse structured, and are reasons shared across decision makers?

The questions guide inquiry; they do not replace evidence categories. [R134] [evolution-C23] [book:learning-systems-thinking], Seven Pattern Thinking Questions

Keep key terms unambiguous across the owner, analyst and approver. Maintain a short shared glossary for verdicts, task independence, trace quality and measurement names. [evolution-C24] [book:learning-systems-thinking], Specialized language barriers

## Evidence table and prioritization

Keep signal columns separate, rank work against the current bottleneck, and explain the value and cost of each selection. A ranking is a prompt for judgment. Do not let an instrument choose the verdict or let an arbitrary numerical score override the trace. [R018] [R081] [R082] [R083] [R100] [R101] [R107]

A retained reference should carry an owner and last-reviewed date, with a reminder for its next review. This makes freshness visible between evolution runs. [evolution-C33] [book:software-engineering-at-google], Chapter 10. Documentation

### Portable trace manifest

The triage helper accepts a user-supplied JSONL manifest. Each record should identify `skill`, `task_id`, `date`, `event` (`invoke`, `read`, `friction`, or `change`) and a short `detail`. Keep the source path and its observed coverage window with the manifest. Do not scan a user’s home directory implicitly or assume one agent harness. Distinct `task_id` values determine real-use independence; invocation and read totals remain separate.
