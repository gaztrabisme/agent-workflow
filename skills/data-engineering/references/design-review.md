# Design review

A checklist for reviewing a layer model, a pipeline design or an architecture diagram of the data side. Run it against the written spec and the diagram together: most defects are a disagreement between the two. Each item restates a rule from the module linked in the first item of its section; the rule's source is cited in that module.

## How to run it

1. Collect the layer spec, every diagram that shows the data flow, the scope list, and the estimate rows for data work. Note which one is marked as the authority. (derived: EVOLUTION.md case 13)
2. For each item below, record **confirmed** (with the line or box that shows it), **flagged** (what is missing or contradicts, and where), or **not applicable** (why).
3. For each flag, search the other documents for an existing answer before reporting it: an open-items list, a decision record, a scope exclusion. Report it as **already handled** with its location if found.
4. Report flags ranked by what breaks if left: data that cannot be corrected or traced first, then wrong numbers, then cost.

## Layers

- [ ] Each layer has one stated job, one writer and one mutability rule. ([layers-and-contracts](layers-and-contracts.md))
- [ ] The raw layer holds only what the source said; nothing derived is stored there.
- [ ] Original source files are kept, with a hash, for audit and reprocessing.
- [ ] Each transform is split into what was detected (raw) and how it was resolved (cleaned).
- [ ] Working state (queues, drafts, assignments) is kept apart from the curated layer.
- [ ] The grain of every cleaned and curated table is stated as its key.
- [ ] Values that must never be compared sit in separate rows.
- [ ] Layout, columns, units and sign convention are detected per source, not assumed.
- [ ] Every layer named in the spec appears in the diagram, and the diagram adds no layer the spec lacks.

## Contracts

- [ ] Each boundary has a contract: structure, meaning (units, scale, rounding, periods), quality, timing, owner, version.
- [ ] A model or external service that produces raw records has a contract, and its version is stored per record.
- [ ] The controlled vocabulary (the list of concepts a value can map to) has a named owner and source.
- [ ] Entity identity has a stated authority and a rule for records without the identifier.
- [ ] Period and date conventions are decided, including irregular periods and restated comparatives.

## Pipelines and re-runs

- [ ] Every step is idempotent, and writes by key where a record can arrive twice. ([pipelines-and-reruns](pipelines-and-reruns.md))
- [ ] Duplicate source detection uses a key whose fields are all captured before it runs.
- [ ] A wrong value is corrected by fixing the transform and replaying, never by editing a derived row.
- [ ] The replay procedure says what it re-runs and what it does not (external services).
- [ ] Backfill for a new transform version is planned: range, order, check, what consumers see meanwhile.
- [ ] Arithmetic and rule evaluation run in code; any model step stores its output, version and evidence.

## Quality

- [ ] Checks are placed before and after each transformation, with a stop rule, threshold and owner for each. ([data-quality](data-quality.md))
- [ ] Rule failures decide what a human reviews; model confidence only orders the queue.
- [ ] Each domain rule lists its legitimate-difference cases and its behaviour when an input is absent.
- [ ] Monitoring covers freshness, volume, distribution, schema and lineage.
- [ ] Every reported rate names the layer and sample it was measured on.

## Lineage and consumers

- [ ] Each value carries its raw reference, transform version and transform evidence. ([lineage-and-traceability](lineage-and-traceability.md))
- [ ] Promotion into the curated layer happens only through the stated approval step.
- [ ] Each consumer reads the layer whose promise it makes; if it reads an earlier layer, its output is labelled unreviewed.
- [ ] No data enters the consumption layer without passing the layers before it, or without a provenance marker.
- [ ] Field-level and document-level approval are told apart wherever a consumer shows data.

## Plan

- [ ] Estimate rows are filed under the layer or component they build. ([estimating-and-testing](estimating-and-testing.md))
- [ ] Every unenumerated driver is marked, with the effort it moves.
- [ ] Tests cover idempotency, replay, contracts and rule suppressions, not only transforms.
