# Standing corrections

The buffer between evolution runs. A correction the owner gives once is a line here, and the next
session pays for it in a read instead of in his time. Drained by `evolution` Phase 0, so it is an
inbox, not an archive.

**Where.** `wiki/standing-corrections.md` in a project with a `wiki/`; `.claude/standing-corrections.md`
otherwise. One per project. Never in `docs/` or `deliverables/` — it is working state, and those
folders get exported.

## The line

Four fields, one line, pipe-free, no prose field:

`DATE · SURFACE · THE INSTANCE, both sides · THE RULE`

```
2026-08-26 · slide heading · "What we will hold ourselves to" -> "Acceptance criteria" · a label is a noun phrase, four words or fewer, never a sentence
2026-08-26 · WBS workbook · README and GAPS sheets -> deleted · ship the items that were asked for and nothing else
2026-08-26 · options sheet · empty "Confirm today" column -> removed · a blank beats a filler
2026-08-24 · note for a colleague · "as [he] instructed..." -> cut · never quote a colleague's own instruction back to him in a file he opens
2026-08-18 · deck for the funder · "352.5 MD" -> cut · no man-day or cost figure in anything a client sees
```

**The verbatim before-and-after is the load-bearing field.** "Be plain" is an adjective and nobody
can check a draft against it. `"What we will hold ourselves to" -> "Acceptance criteria"` is
checkable by anyone, against anything, in one pass.

## What writes it

Any session, in the same turn as the fix — not at the end, not at the next evolution run. The
trigger is a test, not a judgement:

> **The user corrected an output, and the correction would apply to a different artifact next week.**

That is a line. A one-off factual fix ("the total is 422, not 416") is not — that belongs in the
project's own record.

## What reads it

Two points, and the second is the one that catches things:

1. **Session start.** Whole file. It is capped, so this is free.
2. **Before any file goes to a named human** — deck, workbook, note, email. The reply says which
   lines were checked against the draft. Session start alone does not work: the global instructions
   are already read at session start and the same defects recur, because every failure in the record
   happens at send time.

## Why it does not become a dumping ground

- **Hard cap: 25 lines.** At 26 nothing may be appended until a line is removed. The cap forces the
  triage that a growing file always postpones.
- **`evolution` Phase 0 drains it, every run.** A line whose rule has now been corrected on two
  different surfaces is **promoted** into the owning skill as a real rule and struck from the file
  with the commit that promoted it. A line older than 60 days that never recurred is deleted as a
  one-off, with that word written next to it. Draining has an owner and a trigger, which is what
  `loop.md` says every validation step that never fires was missing.
- **No prose field.** Four fields on one line. There is nowhere to write a paragraph, so nobody does.

## Why the two files that already exist are not doing this job

- **`wiki/decisions.md`** records what was decided about the *engagement* — scope, price, what to tell
  the funder. Nothing in it is about how the owner wants the work done, and nothing appends to it when
  he says a heading is cringe.
- **The project `CLAUDE.md`** is read at session start and nowhere else, while every instance in the
  record happens at *send* time, hours later: the cringe heading, the man-days on the slide, a
  colleague's own instruction quoted back to him. It is also hand-edited on explicit order — measured
  once in six weeks — so nothing accumulates in it between those orders.

⚠ **The weak link is the install step.** This file describes a mechanism; a project only gets it when
its own `CLAUDE.md` carries the pointer, and that pointer is a documented instruction in the same file
whose existing rules are already being skipped. If a later harvest shows lines being appended only by
evolution runs, the read trigger belongs in a `SessionStart` hook, not in prose.
