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
```

One row per criterion. Each UAT is a concrete command or check — a file that exists, a validator that exits 0, a grep that matches — never "looks right". A criterion you cannot write a UAT for is not yet a criterion.

## Who audits

The coordinator, at Close, against this file only: run each UAT command, report pass or fail per row. A criterion that fails is reported as failed, never re-worded to match what was produced — that is the kernel's first integrity constraint (`../../core/SKILL.md`). The file is written before dispatch and is not edited afterwards; if the criteria themselves turn out to be wrong, that is a stop-and-escalate, not a quiet edit.

## Worked example

`~/Documents/Work/lab/ceric/GOAL-2026-09-15.md` — two deliverables, a numbered criteria table per deliverable with runnable UATs, and a working-pattern section naming the lanes for the run.
