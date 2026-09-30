# Goal File

The run's stop condition, persisted. Conductor always invokes `/goal` before dispatch, and `/goal` needs exact criteria to invoke with, so the file is written first and the slash command is fired with its criteria. Both happen, **file first**: `/goal <criteria text>` is the Claude Code slash command that sets the session's stop condition — or the harness's equivalent session-stop mechanism; failing that, the UAT column is the stop condition and Close runs it. The file is the durable audit record that survives the session. Close audits the artifacts against the file's UAT column and nothing else.

## Where it lives

`wiki/goals/<YYYY-MM-DD>-<slug>.md` in the project. When the project has no wiki, beside the primary artifact.

## Template

```
# Goal — <date> — <slug>

**Set by:** <who, via `/goal`>. **Audited by:** the coordinator at close, against this file only.

## Deliverable — <path or name>

| # | Success criterion | UAT (how to verify) |
|---|---|---|
| <n.n> | <criterion, exact> | <a concrete command or check> |

## Working pattern (binds this run)
<Which lane takes which shape of unit; any lane closed today.>

## Amendments
<Scope changes the owner asks for mid-run, each dated and in the owner's words; "(none)" if there are none.>
```

One row per criterion. Each UAT is a concrete command or check — a file that exists, a validator that exits 0, a grep that matches — never "looks right". A criterion you cannot write a UAT for is not yet a criterion.

## Writing rows

Three rules for the rows, learned from a run where two rows could never pass and blocked the stop hook for hours after the work was done:

- **No changeable counts.** No row states a count that the run can change. Counts come from the file that holds them.
- **Every branch passes.** A row that depends on a decision passes on each branch of that decision, and says so.
- **Owner amendments.** If the owner changes the scope mid-run, the change is appended under "Amendments" with the date and the owner's words. Existing rows are not re-worded.

## Who audits

The coordinator, at Close, against this file only: run each UAT command, report pass or fail per row. A criterion that fails is reported as failed, never re-worded to match what was produced — that is the kernel's first integrity constraint (`../../core/SKILL.md`). The file is written before dispatch, and the coordinator never re-words or deletes a row afterwards. A scope change the owner asks for mid-run is appended as a dated amendment in the owner's words. Criteria found to be wrong without an owner request are still a stop-and-escalate.

## Worked example

`~/Documents/Work/lab/ceric/GOAL-2026-09-15.md` — two deliverables, a numbered criteria table per deliverable with runnable UATs, and a working-pattern section naming the lanes for the run.
