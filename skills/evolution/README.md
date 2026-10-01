# evolution

Evolution turns real-use evidence into reviewable skill changes and later verdicts. Use it when a skill has repeated-use evidence, a recurring correction, or an open verdict that needs review.

## The loop

1. Triage eligible evidence and set scope.
2. Settle prior open verdicts for each selected skill.
3. Harvest real traces and assess their quality.
4. Explain and rank patterns.
5. Write falsifiable hypotheses and stop for whole-set approval.
6. Apply approved, small, reversible changes.
7. Record the result with `PENDING` status and future checks.

Validation happens during Phase 2 of a later run. Select work by impact, effort, evidence quality and review capacity; there is no fixed skill-count cap.

## Triage helper

`scripts/triage.py` summarizes an explicitly supplied JSONL manifest. It supports a decision; it does not select skills or settle verdicts. It does not scan home-directory telemetry or assume an agent harness.

```bash
python3 scripts/triage.py --root /path/to/skills --traces /path/to/traces.jsonl
```

Each record needs `skill`, `task_id`, `date` (`YYYY-MM-DD`) and `event` (`invoke`, `read`, `friction`, or `change`). For invocations, use `parent_session_id` when available. A prose or operations log without session IDs may use a documented task label with `source: "log"`; define the label in the manifest provenance note. The helper shows log task labels separately from parent-session counts. `reported: true` marks a source-reported value, which the helper lists separately from measured counts.

## Shared core

This skill links to the current `core` package for shared gates: result integrity, grounding and evidence provenance, durable completion records, and pushback and teaching. The evolution loop and its verdict gate are owned here.

## License

MIT
