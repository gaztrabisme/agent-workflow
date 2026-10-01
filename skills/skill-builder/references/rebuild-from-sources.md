Derived from this programme's Stage B method, checkers, work log, and the core rebuild; not from a book or course reading copy.

# Rebuild a skill from its sources

Use this method when a skill must be rewritten against an approved rule proposal, its historical ledger, book crosswalk, and course reading copies. It makes the source boundaries visible before writing and keeps coverage, claim review, dogfood, and the live swap independently checkable.

## Programme checkers and local fallback

`check_rebuild.py`, `check_rebuild_audit.py`, `check_dogfood.py`, and `check_swap.py` are Stage B programme checkers in the programme's external `checks/` directory; they are supplied by the coordinator and are not files in this skill package. When that programme environment is unavailable, do not imply that these checks ran. Use the in-repo `scripts/check_refs.py` for package paths, shipped-file inventory, links, and optional skeleton headings, and compare proposal routing, coverage locations, and claim rows manually. For example, from the skill-builder checkout:

```sh
python3 scripts/check_refs.py <target-skill-path> --no-anchor-check --format --skeleton <absolute-path-to-SKILL.md.skeleton>
```

For a distilled skill, replace `--no-anchor-check` with explicit `--sources` and `--anchor` arguments. The local command does not replace the Stage B coverage, audit, dogfood, or swap checkers. The in-repo `Worked example: core rebuild, run 1` below is the fallback example for how their results fit together.

## Inputs and scope

Gather these inputs before drafting:

- The approved proposal: the skill's artifact, audience, trigger, dependencies, named sources, and every row routed to it. The destination table sets the boundary. A dropped rule or a rule routed to another skill is outside the rebuild, even if it appears in the old skill.
- The rule ledgers: each routed rule's wording, old location, quote, provenance type, and evidence.
- The book crosswalk: each rule's verdict, book, cited chapter, source passage, and any correction. Apply a `refines` correction to the rule. State `disputed` material as a field rule and preserve the disagreement only in the audit record.
- The candidate sections: decide which practices fit the proposed artifact and audience. Do not adopt a candidate merely because it is available.
- The source material: read each cited book chapter and relevant course reading copy before writing the claim. Use the checked text, figure, page, or lesson anchor; do not rely on the crosswalk excerpt alone.
- The current skill, its practitioner review, the shared kernel, and the canonical skill-authoring skeleton and checklist.

Record what you read and what it changed. The top-level skill remains the operating index; place longer procedures in linked references.

## Coverage map

Keep one separate Markdown coverage file for the rebuilt skill. Use this shape:

```markdown
# Coverage: <skill>
Writer: <lane>

## Rules
| Rule ID | Location | Basis | Note |
|---|---|---|---|
| <rule id> | SKILL.md§<heading> | book:<slug> | correction applied: <short correction> |

## Added
| ID | Location | Basis | Quote |
|---|---|---|---|
| <skill>-C01 | references/<file>.md§<heading> | book:<slug> § <chapter> | |
```

There is exactly one `Rules` row per approved routed rule. A location is a file relative to the skill directory, followed by `§` and text that appears in a heading of that file. Use `book:<slug>` for `agrees` and `refines`, `field` for `field-rule`, and `disputed` for a disputed row. The note records the citation chapter or the correction applied. If a course lesson also supports a rule, append its exact `course:<anchor>`; do not infer an anchor.

`Added` records adopted book candidates under their original candidate IDs. A new practice sourced from a book uses `<skill>-N01`, then increments; include a verbatim book quote of at most 25 words. Keep the coverage map separate from the skill. The external Stage B coverage checker (`check_rebuild.py`) verifies rule routing and uniqueness, heading locations, bases, book tags, course anchors, and candidate rows.

## Row-by-row claim audit

Use independent writer and auditor lanes. The auditor receives the source row, the relevant crosswalk or candidate, the map location, and the skill section. It judges source fidelity, not writing style alone.

For each rule or added practice, the auditor returns one verdict:

- **faithful** — the section states what the source allows and cites the right book;
- **overstated** — it says more than the source or attributes too much to the book;
- **missing** — its meaning is absent or compressed past recognition;
- **misplaced** — it appears under a heading where a reader would not look, or conflicts with another section;
- **contradicts** — a `refines` rule remains in its old, uncorrected form.

The external Stage B claim-audit checker (`check_rebuild_audit.py`) also checks that the writer and auditor lanes differ, every coverage ID has an audit row, the round and status are valid, and the fingerprint matches the reviewed skill.

Run no more than three rounds:

1. **Round 1:** audit every Rules and Added row. Merge findings into an open list.
2. **Fix 1, then round 2:** the writer answers every open finding with a repair or source-backed rejection. Re-audit the open rows; a note by itself is not evidence.
3. **Fix 2, then round 3:** recheck the remaining findings. Any finding that still cannot be reconciled becomes `disputed`; preserve both the auditor's finding and the writer's source-based reply instead of forcing a false agreement.

The stage B programme also cross-checked passed rows through a second independent lane: a seeded 15% sample, escalating to all passed rows when the sample miss rate exceeded 15%. This catches a consistently lenient first audit without making a second full review automatic.

## Dogfood on a real past task

Use a fresh-context reviewer to **run the skill** on a real past task, not to inspect the skill and guess. Give it the skill, every reference, the shared kernel, and the task's input material. Keep the past output closed until the reviewer has written its own artifacts. Store those artifacts as evidence, then compare them with the result produced at the time.

The review asks whether the skill triggered correctly, collided with a sibling, gave enough steps and templates, made each gate actionable, kept links working, avoided contradictions and overreach, and represented its sources honestly. The report records the artifacts made, differences from the past output, ranked findings with causes and fixes, and the parts of the skill that actually helped. State the pass condition before the run: correct trigger, actionable gates, working references, and no high-severity finding left open after fixes.

The external Stage B dogfood checker (`check_dogfood.py`) checks for evidence, findings, a fix note per finding, closure of high-severity findings, and a stage B evolution entry still at `PENDING`.

## Fix rounds and evidence

For claim-audit fixes, inspect each finding against the ledger and crosswalk. Fix valid findings at their source location; update the coverage location if a rule moves. If a finding is wrong, preserve the skill text and cite the exact source evidence in the reply. Keep every other routed rule intact.

For dogfood fixes, resolve each finding, mark dogfood-derived guidance as derived, record one fix or rejection per finding, list the changed coverage IDs, and update `EVOLUTION.md` with task, severity counts, and the fix/rejection counts. Recheck affected claims after edits. Rerun dogfood if a high-severity finding forced a structural change; rerun automated checks after each edit.

## Swap beside the live skill

Only after coverage, source audit, dogfood, and format validation pass should the coordinator swap the rebuilt branch into the live skill path. Keep a `pre-stage-b` tag on the prior live revision as the rollback point. The external Stage B live-swap checker (`check_swap.py`) verifies the live worktree is clean and points at the stage B branch head, the revert tag is an ancestor, the installed skill link resolves to the live path, and spine references do not exceed the current core.

The swap is a local activation step; publication is separate and still requires the publishing gate. If the result fails after activation, restore the prior revision from the tag rather than improvising a new baseline.

## Worked example: core rebuild, run 1

The core rebuild routed 115 rules: 31 `agrees`, 34 `refines`, 49 field rules, and 1 disputed. The writer adopted 23 of 27 candidates. Its `SKILL.md` became a 34-line index over five references; the older manual had 657 lines. The coverage checker and skill-format validator passed before audit.

The first claim audit found three rows to fix; the completed audit had 135 passes and 3 fixed rows. A real past-task dogfood then produced eight findings, including three high-severity ones. The writer fixed all eight and rechecked 22 touched rows. One revision accidentally reversed a disputed decision order; the next fix restored the field rule and recorded the book's alternate order as disputed, and the final round found no open claim. The live swap kept the pre-stage tag as its revert point; nothing was pushed during the swap.

This example is useful because it shows that a green first audit is not the end of the method: dogfood found issues the source-row audit could not, and the fix rounds preserved a real source disagreement instead of smoothing it away.
