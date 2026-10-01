# Run Schedule

Use a run-specific schedule when work repeats over items, runs in batches or waves, or depends on an external queue/watch process. The Plan Block's `SCHEDULE` row names the schedule record and summarizes its shape. A single-stage run can state `none`.

This record owns execution order, batching, queue state, and resume position. Provider status, lane selection, invocation, and fallback rules stay in `lane-plan.md`, the owner's single home for lane rules. (derived: dogfood 2026-10-01)

## Schedule record

Record the following for any repeated or queued workflow:

- **Items and units:** name the source that determines the work items and give each item a stable ID. Read the count from that source rather than freezing a count in the goal file.
- **Order and barriers:** show the waves, loops, rounds, and dependencies. Name which result must be accepted before the next stage or batch can start.
- **Batch cap:** state the selected maximum batch size and why it fits the open lane capacity, task risk, and review effort. There is no universal batch size.
- **Queue and watch operations:** record each queue/watch script's workspace path, command, owner, status signal, stop signal, and the action to take on failure. Keep the scripts in the project workspace so their state and acceptance are reviewable.
- **Per-batch acceptance:** state the acceptance check and required output sample for every batch boundary. A final aggregate check does not replace checks that prevent a bad batch from feeding the next stage.
- **Resume state:** record the last completed stage and stable item or batch ID, the partial work to reconcile, and the next safe action. Reconcile side effects before retrying; make repeated steps safe.

## Schedule table

| Stage / wave | Items or batch IDs | Depends on | Lane-plan reference | Acceptance before next stage | Queue/watch state and resume cursor |
|---|---|---|---|---|---|
| `<stage>` | `<stable IDs or source>` | `<prior accepted result>` | `<unit IDs in lane plan>` | `<command and sample>` | `<script/state/cursor, or —>` |

For per-item loops, include each repeating audit/fix round in the schedule logic without inventing one lane-plan row per iteration. The lane plan assigns lanes and acceptance ownership to the work shapes; this record makes the loop, batch boundaries, and restart point visible. (derived: dogfood 2026-10-01)
