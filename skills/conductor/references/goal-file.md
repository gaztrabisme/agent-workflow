# Goal File

The goal file is the run's persisted stop condition. Write it before dispatch, then set the active harness's session-stop mechanism from its criteria. Where the harness has no such mechanism, the UAT column is the stop condition and Close runs it. The file is the durable audit record; Close audits the artifacts against its UAT column.

## Where it lives

`wiki/goals/<YYYY-MM-DD>-<slug>.md` in the project. When the project has no wiki, beside the primary artifact.

## Template

The decision record names the accountable author and a contact so responsibility for its contents is visible in the artifact. [book:facilitating-software-architecture], The Structure of an ADR.

```
# Goal — <date> — <slug>

**Decision owner / author:** <name and date>. **Audited by:** <coordinator or named reviewer at Close>. **Contact:** <who answers questions about this record>.

## Deliverable — <path or name>

| ID | Source / stakeholder | Success criterion | Artifact / evidence | UAT (how to verify) |
|---|---|---|---|---|
| <unique ID> | <origin or owner> | <measurable outcome> | <path or evidence> | <concrete command or check> |

## Working pattern (binds this run)
<Which lane takes which shape of unit; any lane closed today.>

## Amendments
<Scope changes the owner asks for mid-run, each dated and in the owner's words; "(none)" if there are none.>
```

## Service objectives and error budget

For service or reliability work, state a user-facing SLO as a measurable goal-file criterion. Record the corresponding error budget in the Plan Block so the allowed reliability risk is explicit. Use this only when the service context makes an SLO meaningful. [book:site-reliability-engineering], SLOs Set Expectations; [book:site-reliability-engineering], Forming Your Error Budget.

One row per criterion. Trace it from its source or stakeholder to the artifact that satisfies it and the UAT that proves it. Each UAT is a concrete command or check — a file that exists, a validator that exits 0, a grep that matches — never "looks right". Where practical, make acceptance checks automated and run them against the delivered artifact. A criterion you cannot verify is not yet a criterion. [book:pmbok-guide-7e], 4.6.6. Visual Data and Information; [book:continuous-delivery], Why Is Automated Acceptance Testing Essential?

## Writing rows

Bind each work shape to its lane and record lanes that are closed at planning time; this makes the working pattern checkable against the work package. [book:pmbok-guide-7e], 4.6.6. Visual Data and Information.

For each criterion about user-visible value, make an automated acceptance test prove that the value is delivered where practical. [book:continuous-delivery], Real-Life Situations and Strategies.

Three rules for the rows, learned from a run where two rows could never pass and blocked the stop hook for hours after the work was done:

- **No changeable counts.** No row states a count that the run can change. Counts come from the file that holds them.
- **Every branch passes.** A row that depends on a decision passes on each branch of that decision, and says so.
- **Owner amendments.** If the owner changes the scope mid-run, append the dated change in the owner's words. Preserve the original row and its UAT result. A failing criterion may be revised only when its underlying assumption or the tested functionality has genuinely changed; record that change and keep the original failure visible. Never change wording just to hide a failure. [book:continuous-delivery], Essential Practices.

## Who audits

The coordinator, at Close, against this file only: run each UAT command, report pass or fail per row. A criterion that fails is reported as failed, never re-worded to match what was produced — that is the kernel's first integrity constraint (`../../core/SKILL.md`). The file is written before dispatch. The coordinator never deletes or silently rewrites a row. A scope change, or a demonstrated change to the tested assumption or functionality, is recorded as a dated amendment that preserves the original criterion and verdict. A criterion found to be wrong without such a change remains a stop-and-escalate.

## Worked example

`~/Documents/Work/lab/ceric/GOAL-2026-09-15.md` — two deliverables, a numbered criteria table per deliverable with runnable UATs, and a working-pattern section naming the lanes for the run.
