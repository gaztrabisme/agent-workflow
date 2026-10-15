# Data contract: WBS workbook template

The data folder holds YAML files, UTF-8, in English. File names come from `project.yaml` (`data.files`).
Field names below are the template's own; a project whose YAML uses other names maps them in
`data.fields` (for example `task_id: my_id`). Anything marked **(project.yaml)** is a per-project setting.

## Hard rules
- **Every figure has a source.** A day figure is copied from a named plan row, or is the arithmetic of the
  effort rule below. Added tasks, proposed changes and removals cite it in `source`.
- **No invented numbers.** Where no source exists, the row is not added; ask the person who holds the figure.
  An estimate is allowed when its method is written in `basis` and it is marked `highlight: true` (filled
  with the fill-in colour for the plan owner to confirm).
- **Text caps:** each shown item is at most `text.cap` characters (criteria: per line); a sub-task name at most
  `text.subtask_name_cap` **(project.yaml)**.
- **No person names in shown text.** Write the role ("tech lead", "BA"). Names may appear only in `source`
  fields, which go to the internal sheet (`internal_sheets`) **(project.yaml)**. The same holds for our own
  working-file names and decision tags (`text.internal_source_patterns`).
- **Proposed changes to someone else's figures** go only in the proposals file. Their `reason` starts with
  `marking.proposal_prefix` **(project.yaml)**; the workbook gives the row the proposal fill.

## Effort rule **(project.yaml: effort_rule)**
For a task with `dev` days:
- with add-ons: `qc = addons.qc x dev`, `ba = addons.ba x dev`; without: `qc = ba = null`;
- `effort = (dev + qc + ba)` rounded UP to the next multiple of `round_up_to`.
Tasks of the `no_dev_roles` carry no dev and no add-ons; their `effort` is the figure itself.
When changing a task's dev, keep whether it had add-ons.

## plan_tasks (never edited by hand)
```yaml
tasks:
  - task_id: 1.1.1.1      # dot id; the first feature_key_parts parts name the plan feature (project.yaml)
    sheet: Platform       # shown as Section
    module: Survey
    task: Site survey
    basis: "survey 2 + report 1.5 = 3.5"   # how the plan owner reached the figure
    role: DevOps engineer # one of roles.known (project.yaml)
    dev: 3.5
    qc: null
    ba: null
    effort: 3.5
    dod: "Survey report accepted"           # shown as the criterion when there is no criteria entry
    phase: Phase 1        # plan.overhead_phase marks an overhead row: shown, never in a total
options:                  # optional extras: shown, never in a total
  - {section: S-1, option: "Extra panels", task: "...", role: Installer, dev: 3.0, qc: null, ba: null, effort: 3.0}
```

## feature_map
```yaml
rows:                     # WBS rows, in sheet order
  - {id: A.1, group: ..., module: ..., feature: ..., description: ..., acceptance: "...", owner: Us,
     note: null, source: "Feature list, row A.1"}   # owner: one of owners.all; other fields per columns.wbs
map:                      # every plan feature maps to one WBS row
  - {plan_feature: 1.1.1, wbs_id: F.1}
task_map:                 # optional: single tasks mapped elsewhere than their feature
  - {task_id: 1.2.3.4, wbs_id: A.2, reason: "..."}
```
Required non-empty row fields: `wbs_required_fields` **(project.yaml)**.

## changes
```yaml
status:                   # status changes to plan tasks (never to overhead rows)
  - {task_id: 1.3.1.1, status: out_removed_by_client, owner: Us, reason: "...", source: "Q&A log, row 22"}
add:                      # tasks the plan lacks
  - {id: X-01, wbs_id: N.1, task: "...", basis: "...", role: ..., dev: 3.0, qc: 1.5, ba: 0.75, effort: 5.5,
     status: in, source: "...", dod: "...", highlight: false}
```
- `status` values and their labels: `statuses.change`; added-task values: `statuses.add` **(project.yaml)**.
- Values in `statuses.needs_source` require `source` and `reason`; the source must contain
  `statuses.removal_source_marker`.
- Added IDs start with `ids.change_add_prefix`. `source` is required on every added task.
- `highlight: true` marks our own estimate for the plan owner to confirm (fill `marking.highlight_fill`).

## proposals (optional)
```yaml
change:                   # existing tasks whose figures we propose to change
  - {task_id: 1.1.1.2, dev: 2.5, qc: 1.25, ba: 0.625, effort: 4.5,
     reason: "<proposal_prefix> why, within the text cap", source: "where the number is copied from"}
add:                      # tasks we propose adding
  - {id: P-01, wbs_id: A.1, task: "...", role: ..., dev: 3.0, qc: null, ba: null, effort: 3.0, status: in,
     dod: "...", reason: "<proposal_prefix> ...", source: "..."}
```
A task may not be both proposed for change and out of scope (`statuses.out_of_scope`).
Added IDs start with `ids.proposal_add_prefix`.

## task criteria files (`data.files.task_criteria_pattern`; all matching files are merged)
```yaml
tasks:
  - task_id: 1.1.1.1
    subtasks:             # names within the sub-task cap; days multiples of criteria.subtask_step,
      - {name: "...", days: 2.0}   # each at most criteria.subtask_max_days; they sum EXACTLY to the effort
    acs: ["...", "..."]   # criteria.min..criteria.max checkable criteria
```
Required for every in-scope task with effort above `criteria.over_days`. A task at or below it shows its `dod`.
A criterion with a % or time target (`criteria.clause_trigger`) ends with `criteria.clause` **(project.yaml)**.

## stories, story_source (optional)
```yaml
stories:
  - us_id: US-01
    title: "..."
    story: null           # or "As a ..., I want ..., so that ..."
    acs: ["..."]          # verbatim from story_source when origin is stories.verbatim_origin
    wbs_ids: [A.1]
    origin: given         # one of stories.origins (project.yaml)
    source: "..."
```
Every WBS row whose id starts with `stories.required_row_prefixes` and carries our in-scope effort needs a story.

## dependencies, assumptions, glossary (optional)
```yaml
# dependencies
- {id: DEP-01, item: "...", from: Client, needed_by: "a milestone in words", blocks: [A.1], status: Open,
   if_late: "what we assume or do if it is late", source: "..."}   # from, status: dependencies.* (project.yaml)
# assumptions
- {category: Scope, text: "...", source: "..."}
# glossary (shown on the internal sheet)
- {term: "...", meaning: "..."}
```

## Workbook built from this data
Sheets and their order, names and columns come from `sheets` and `columns` **(project.yaml)**:
master inputs (rate, man-days per month, PM %, contingency %), an effort summary computed by formulas over
the task detail, the WBS rows with SUMIFS totals, task detail (one row per task, sub-task rows below it),
user stories, assumptions, dependencies, and the internal references sheet (every citation, the glossary,
and the one colour legend).
