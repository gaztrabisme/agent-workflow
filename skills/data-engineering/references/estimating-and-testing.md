# Estimating and testing data work

How to size data engineering work and what to test. The estimate method itself (basis per row, ranges, contingency, derived percentages) is in `../../project/references/estimating.md`; this module adds what is specific to data work.

## Decompose against the layer model

- Write the layer spec before the estimate, and file each task under the layer or component it builds. Work filed under the wrong group hides the layer's real cost and makes a later move look like a saving or an addition when it is neither. (derived: EVOLUTION.md case 14)
- When a task moves between layers (for example a detection step moving from the rules engine to the cleaning layer), move its effort with it and say so.

## Drivers

Size each row by what drives it, and name the driver:

| Work | Driver | Not the driver |
|---|---|---|
| Ingestion | number of distinct source formats and contracts, if ingestion is a reusable configured framework | number of tables or files |
| Orchestration | number of distinct pipeline patterns | number of workflows |
| Cleaning and mapping | number of concepts in the vocabulary, and the transforms each needs | number of documents |
| Quality checks | number of rules, plus their false-positive suppressions | |
| Run cost and throughput | source volume: documents per period times pages per document, measured on a sample | an assumed average |

The ingestion and orchestration rows are from the source below; the other three rows are (derived: EVOLUTION.md case 15).

- Do not estimate ingestion by the number of tables or orchestration by the number of workflows; build reusable, configurable frameworks and estimate those. [book:practical-lakehouse-architecture], Estimation and Planning Phase
- A driver that has not been enumerated (for example "about 200 fields" with no field list) is an assumption. Mark every row that depends on it, show how much effort it moves, and set a date by which it is fixed. (derived: EVOLUTION.md case 15)
- Measure volume drivers on real samples before they reach a cost estimate; an assumed average can be off by several times. (derived: EVOLUTION.md case 15)

## Activities that are often left out

Add a row for each, or state why it is not needed: [book:practical-lakehouse-architecture], Estimation and Planning Phase

- Data modelling and mapping documents worked out with data owners; often underestimated.
- Time for the team to learn the chosen table format and engine.
- Deployment pipelines.
- Data quality validation, governance, security and monitoring.
- For a replacement of an existing system: understanding it, migrating history, reconciling old and new results, running both in parallel for several cycles, and decommissioning.

Also for document pipelines: labelling a golden sample, adjudicating disagreements between labellers, and the review interface the reviewers work in. (derived: EVOLUTION.md case 7)

## Test plan

| Test | What it proves | Data |
|---|---|---|
| Unit | Each transform does what it should, with business logic separated from the glue code | very small hand-made inputs |
| Contract | Each layer's output matches its contract: schema, units, keys | generated and real samples |
| Functional | Validation, ingestion, processing and storage behave on realistic volumes | large samples |
| Integration | The whole pipeline meets its validity criteria end to end | fake data first, then production data |
| Idempotency | Running twice on unchanged input changes nothing | any fixed input |
| Replay | Rebuilding a derived layer from raw reproduces it exactly, or differs only where a transform changed | a frozen raw snapshot |
| Rule suppression | Each legitimate-difference case does not fire its rule | one constructed case per suppression |
| Error injection | Each class of error the rules claim to catch is caught | verified-correct records with known errors inserted |

Sources: [book:data-quality-fundamentals], Measuring and Maintaining High Data Reliability at Ingestion (part 1); [book:building-medallion-architectures], Idempotency as a Key Design Principle

- Error injection makes a detection rate measurable: insert errors of a known class into records already verified correct, so the denominator is known. Report the rate per error class, never pooled. (derived: EVOLUTION.md case 7)
- Assert transforms with queries that return failing rows and expect none. [book:data-quality-fundamentals], dbt Unit Testing
- Code-level test practice (test-first, fixtures, test runners) belongs to `../../dev/SKILL.md`; model evaluation design belongs to `../../applied-ml-problem-solver/SKILL.md`.
