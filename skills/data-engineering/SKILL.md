---
name: data-engineering
description: "Data engineering design, review and planning for a delivery: ingestion, layered storage (raw/bronze, cleaned/silver, curated/gold, consumption), orchestration, data contracts, data quality checks and monitoring, lineage back to the source document, idempotent re-runs and backfills, and estimating and testing data work. USE WHEN designing or reviewing a layer model or pipeline, deciding what each layer holds and who writes it, writing a data contract, placing quality checks, tracing a value to its source page, planning a replay or backfill, or sizing data work. Not `dev` (code), `applied-ml-problem-solver` (model and evaluation decisions), `solution-architect` (client-facing solution), `infrastructure` (environments, deployment, cloud cost) or `information-design` (charts). Keywords: data engineering, pipeline, ETL, ingestion, medallion, bronze silver gold, lakehouse, data contract, schema, data quality, circuit breaker, lineage, provenance, idempotent, replay, backfill, upsert, entity resolution."
license: MIT
---

# Data engineering

Produces a data design record and its checks for the engineer or technical lead building the data side of a delivery: what each storage layer holds, who writes it and when it may change; the contracts between layers; where quality checks run and what stops the pipeline; how a value is traced back to its source; how the pipeline is re-run and backfilled; and the estimate and test plan for that work.

> Inherits the `core` kernel — see `../core/SKILL.md`. Follow shared gates through their canonical references; do not copy their definitions.

## When it fires — and when a sibling owns it

- **This skill:** layer model, data contracts, pipeline and re-run design, quality checks and monitoring, lineage, and the estimate and tests for data work.
- **`dev` instead:** writing or reviewing the pipeline's code, unit tests per change, root-cause analysis of a code defect. This skill hands `dev` the design; `dev` builds it.
- **`applied-ml-problem-solver` instead:** choosing and evaluating an extraction or mapping model, labels and accuracy metrics. This skill treats a model's output as a source with a contract.
- **`solution-architect` instead:** the client-facing architecture, options and response pack. This skill supplies the data design that sits under it.
- **`infrastructure` instead:** environments, deployment pipelines, provisioning and cloud cost of the data platform.
- **`information-design` instead:** charts and dashboards on top of the curated data.
- **`project` instead:** the WBS, schedule and price; this skill supplies the data rows and their basis.

> **Disambiguation:** decide on artifact and audience. A layer model, contract, check plan or lineage design for the person building the data side is this skill; code is `dev`; a model choice is `applied-ml-problem-solver`; the client's view of the solution is `solution-architect`.

## Principles

1. **Every layer has one job, one writer and one mutability rule.** The raw layer holds what the source said and is never changed; later layers are rebuilt from it. [book:building-medallion-architectures], The Three-Layered Design
2. **Fix the transform and replay; never hand-edit a derived layer.** A pipeline that gives the same result on every run is what makes replay safe. [book:building-medallion-architectures], Idempotency as a Key Design Principle
3. **Write the contract before the code.** Structure, meaning, units, rounding and timing are agreed between producer and consumer. [book:financial-data-engineering], Principle 8: Data Contracts
4. **A failed check stops the data, not only the report.** [book:data-quality-fundamentals], Managing Data Quality with Apache Airflow
5. **Every published value points back to its source location and the transforms applied to it**, with the evidence for each transform. (derived: EVOLUTION.md case 2)
6. **Models interpret; deterministic code computes.** A language model may decide which value maps to which concept; sums, scaling and comparisons run in code. (derived: EVOLUTION.md case 9)

## The flow

| Step | Goal | Module |
|---|---|---|
| Layers and contracts | Decide what each layer holds, its grain, writer, mutability and contract | [layers-and-contracts](references/layers-and-contracts.md) |
| Pipelines and re-runs | Orchestrate, make every step re-runnable, plan replay and backfill | [pipelines-and-reruns](references/pipelines-and-reruns.md) |
| Data quality | Place checks, decide what stops the pipeline, monitor, keep false positives down | [data-quality](references/data-quality.md) |
| Lineage | Trace each value to its source page and its transforms | [lineage-and-traceability](references/lineage-and-traceability.md) |
| Estimate and test | Size the work by its drivers; test transforms, contracts and replay | [estimating-and-testing](references/estimating-and-testing.md) |
| Design review | Check an existing layer model or pipeline diagram against all of the above | [design-review](references/design-review.md) |

Scale to the request: a question about one layer reads one module; a new design or a review runs the design-review checklist.

## Gates (declared, inherited from core)

- **Grounding gate** — substrate: the source documents and samples, the existing layer spec and diagrams, the downstream consumers' requirements, and the knowledge-base books cited here. See `../core/references/grounding-gate.md`.
- **Output Contract** — the design record names each layer's job, grain, writer and mutability; each contract; each check with its stop rule; the lineage fields; and the re-run procedure. An unfinished item is listed as open, not omitted. See `../core/references/output-contract.md` and `../core/references/wiki-protocol.md`.
- **Pushback and teach** — see `../core/references/pushback-and-teach.md`.

## Anti-patterns

- A raw layer that also stores derived values, so it can no longer be replayed. (derived: EVOLUTION.md case 1)
- Correcting a value by editing a derived row instead of the transform.
- A consumer reading a layer earlier than the one its promise depends on, or data entering the consumption layer without passing the layers before it. (derived: EVOLUTION.md case 6)
- A document layout, column structure or unit assumed instead of detected per source. (derived: EVOLUTION.md case 4)
- Arithmetic done by a language model.
- Three documents describing the same layer three ways, with none marked as the authority. (derived: EVOLUTION.md case 13)

## Composition

- **Inherits:** `core`.
- **Hands off to:** `dev` to build; `applied-ml-problem-solver` for extraction and mapping model decisions; `infrastructure` for environments and cost; `project` for the WBS rows and price; `solution-architect` for the client-facing view.

## References

- [references/layers-and-contracts.md](references/layers-and-contracts.md) — layer roles, grain, writers, mutability, detect versus resolve, data contracts.
- [references/pipelines-and-reruns.md](references/pipelines-and-reruns.md) — orchestration, idempotency, replay, backfill, schema change.
- [references/data-quality.md](references/data-quality.md) — check types and placement, stop rules, monitoring, false-positive sources.
- [references/lineage-and-traceability.md](references/lineage-and-traceability.md) — field-level provenance, transform evidence, signed versus unsigned data.
- [references/estimating-and-testing.md](references/estimating-and-testing.md) — estimate drivers, commonly missed activities, test plan.
- [references/design-review.md](references/design-review.md) — checklist for reviewing a layer model or pipeline design.
- [EVOLUTION.md](EVOLUTION.md) — birth record, cases behind the derived rules, and the first test.
