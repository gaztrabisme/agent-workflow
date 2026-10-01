# Triage — evidence, eligibility and scope

Triage produces a decision record, not an automatic ranking. Use signals together, keep their meaning visible, and leave the selection to the accountable human. [book:site-reliability-engineering], Symptoms Versus Causes

## Eligibility and assessment

A skill with no evidence of use since its last entry is excluded from a real-use evolution run. A missing ledger is an integrity gap to repair, but it is not evidence that a used skill should be changed. A skill excluded for no trace may re-enter only on traces the evolution run itself creates; do not add it back on suspicion.

Before using an absence claim to shape scope or a hypothesis, verify that the inspected copy is complete against the run’s close record or the repository remote. If neither is available, label the claim `absent in this copy, unverified` and do not treat it as confirmed. (derived: dogfood 2026-10-01)

A periodic capability assessment names processes to improve, but first establish which work is in scope. Do not turn age or open-item volume into a standalone reason to select a skill. Prioritize by impact and effort while keeping settleable validation debt visible. [book:swebok], Software Process Improvement Models; [book:swebok], Prioritization; [book:site-reliability-engineering], Do One Thing Well; [book:continuous-delivery], Metrics

Match the response to the signal’s impact. A small reversible trim may need only a narrow evidence review; a broad or high-impact change warrants the full loop and a wider review. Set the severity threshold before choosing the work. [book:site-reliability-engineering], Triage

For a quiet but important skill, schedule a bounded exercise such as a game day where it is safe to do so. Apply the skill to a real exercise task and label the evidence as exercise-derived: it can reveal gaps and friction, but it does not establish that the guidance is naturally discoverable in ordinary work. [book:hands-on-site-reliability-engineering], 3. Introduction to SRE

Minimize context switches: group related evidence gathering into sustained, single-purpose blocks. Do not impose a fixed count cap where review capacity and value provide the real constraint. [book:site-reliability-engineering], Do One Thing Well; [book:swebok], Prioritization

## Signals and how to read them

Measure stages of the work to find the actual bottleneck; prioritize that globally constraining stage, rather than automatically ranking validation debt first or sorting by local open-item volume. Put the next unit of effort where expected impact outweighs cost. What you measure steers behavior, so scrutinize the signal and the behavior it rewards. [book:continuous-delivery], Metrics; [book:site-reliability-engineering], Creating a Test and Build Environment

Useful evidence includes post-entry uses, friction or corrections, undigested changes, open verdicts that can now be settled, linked references that have not been opened, and new patterns. For each pick, name the trace that supports it. For each skip, state one reason. A stable skill with no needed change is not neglected. Treat age only as a tie-breaker; give recently changed work room for real use before judging it, and deprioritize a skill changed in the previous run when its only evidence is age.

Use a common measurement window that fits the expected signal. A zero count means zero observed events only inside that window. State the coverage dates and preserve source provenance. [book:site-reliability-engineering], Choosing an Appropriate Resolution for Measurements

Keep unlike measures separate. Report skill invocations and reference reads in separate columns; do not add them into a synthetic total. Interpret them together against the underlying question. For invocations, count distinct parent sessions, not transcript files or child-agent sessions: a parent session and its child sessions are one use. If a prose or operations log has no session IDs, keep its documented task labels as a separate named-task proxy with `source: log`; do not call those values parent-session counts. (derived: dogfood 2026-10-01) If two measures of the same signal disagree, investigate the disagreement rather than averaging away the difference. [book:software-engineering-at-google], Chapter 7. Measuring Engineering Productivity

Assess trace quality before a trace can support a pattern: note whether it is direct or inferred, complete, task-independent, and captured by a reliable source. Do not let a weak source carry a strong conclusion. [book:critical-thinking-about-research], 10 Research Syntheses and Meta-Analysis

## Discoverability and instrument limits

A canonical, linked home makes references easier to find. Check whether `SKILL.md` links the reference before interpreting its read count. [book:software-engineering-at-google], Establishing Canonical Sources of Information

A linked but unread reference may be undiscoverable or too costly; it is not automatically wrong. An unlinked and unread reference is an orphan: remove it only if it no longer serves a purpose, or link it where it is useful. An unread but intentionally wired diagnostic artifact may still have a purpose. [book:site-reliability-engineering], Monitoring; [book:software-engineering-at-google], Chapter 10. Documentation

Disclose the discoverability measure’s limits whenever you use it, and validate its intended signal with qualitative feedback such as experience sampling or user surveys. Ask whether the reference helped, rather than assuming the count answers that question. [book:software-engineering-at-google], Chapter 7. Measuring Engineering Productivity

The older read-once instrument had three material blind spots: its window began only when collection was installed; child-agent reads were attributed to the parent, so event counts—not distinct sessions—answered whether a file opened; and skill injection could use a skill without recording a direct file read, so zero reads on a skill entry meant nothing. A local path mismatch also once hid most reads: 566 of 759 entries came through a linked path. Reconcile alternate paths before calling a reference unread. These are instrument limits, not findings about a skill.

A current session may not yet be present in a stored manifest. Check what you know was used this turn before treating an apparent zero as exclusion evidence.

## Pattern questions

Work through this fixed list of questions to identify recurring relationships and patterns:

1. How does information flow, and how is it transformed?
2. What events happen, and what follows them?
3. What boundaries exist, and why?
4. What building blocks are reused and how do they relate?
5. How does delivery work, and how are priorities and quality handled?
6. How are people organized and connected?
7. How is discourse structured, and are reasons shared across decision makers?

Use these seven questions as the fixed frame for pattern finding instead of a fixed taxonomy of finding categories. [book:learning-systems-thinking], Seven Pattern Thinking Questions

Keep key terms unambiguous across the owner, analyst and approver. Maintain a short shared glossary for verdicts, task independence, trace quality and measurement names. [book:learning-systems-thinking], Specialized language barriers

## Evidence table and prioritization

Keep signal columns separate, rank work against the current bottleneck, and explain the value and cost of each selection. A ranking is a prompt for judgment. Do not let an instrument choose the verdict or let an arbitrary numerical score override the trace.

A retained reference should carry an owner and last-reviewed date, with a reminder for its next review. This makes freshness visible between evolution runs. [book:software-engineering-at-google], Chapter 10. Documentation

### Portable trace manifest

The triage helper accepts a user-supplied JSONL manifest. Each record identifies `skill`, `task_id`, `date`, and `event` (`invoke`, `read`, `friction`, or `change`); `detail` is optional. Invocation records use `parent_session_id` when available. If the source is a prose or operations log with no session IDs, use `source: log` and a documented task label as described above; the output reports those separately from parent-session counts. An optional `reported: true` marks a value supplied by a source rather than measured directly; the helper carries these records into a separate output section instead of mixing them into measured counts. (derived: dogfood 2026-10-01) Keep the source path and its observed coverage window with the manifest. Do not scan a user’s home directory implicitly or assume one agent harness. The helper reports invocation and read evidence separately.
