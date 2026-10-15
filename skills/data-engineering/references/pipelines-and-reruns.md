# Pipelines and re-runs

How to orchestrate the steps, make every step safe to run again, and plan replay, backfill and schema changes.

## Orchestration

- Model the pipeline as a dependency graph of tasks. The orchestrator starts a task when its upstream tasks finish, watches for data to arrive, raises an error when a condition goes out of bounds, and alerts when a job misses its expected completion time. [book:fundamentals-data-engineering], Orchestration
- Write the expected completion time for each scheduled run into the design, so a late run is an alert and not a surprise. [book:fundamentals-data-engineering], Orchestration
- Use dependencies over a time range where a job needs a full period of input, for example a monthly job that waits until every daily load of that month has finished. [book:fundamentals-data-engineering], Orchestration
- Keep the step sequence in one place. When a pipeline diagram and an architecture diagram both number the steps, the two schemes drift; let one own the order and the other show placement. (derived: EVOLUTION.md case 13)

## Idempotency

A step is idempotent when running it once or many times on the same input gives the same result. [book:designing-distributed-systems-2e], Idempotency

- Require it of every task in the graph. Retries, restarts and backfills all re-run tasks, and code that keeps internal state between runs is often not idempotent. [book:machinelearningengineeringwithpython_secondedition], Building an ETML pipeline with advanced Airflow features (part 1)
- Test it directly: run the pipeline twice on unchanged input and check that no row is added or changed. [book:building-medallion-architectures], Idempotency as a Key Design Principle
- Write by key, not by append, wherever a row can arrive twice: an upsert or merge matches on a key and replaces or inserts. The key is the team's to maintain. [book:fundamentals-data-engineering], Batch Transformations (part 3)
- Record a fingerprint of each input (for example a file hash) and of each build, so a rerun can be shown to have produced the same output. [book:continuous-delivery], The Results of the Commit Stage
- A duplicate source document is caught before extraction by a key that identifies the filing (entity, period, and the file hash), not by the file name. State where each key field comes from; a key field that nothing captures leaves the check without a key. (derived: EVOLUTION.md case 11)

## Replay

Replay is rebuilding a derived layer from the raw layer.

- It is the correction path. When a transform is found wrong, fix the transform, bump its version, and replay; every affected value is corrected without re-reading the source. (derived: EVOLUTION.md case 1)
- It needs an immutable raw layer that holds only what the source said, and transforms that read only from the layer below. [book:practical-lakehouse-architecture], Data Consumption and Delivery
- State what a replay re-runs. A replay of the cleaned layer re-runs the transforms and every check that reads the cleaned layer; it is not free, and it is not the same as re-running one check. (derived: EVOLUTION.md case 12)
- Replay never re-runs an external service unless the design says so. A new extraction is a new raw version, kept beside the old one, so the two can be compared. (derived: EVOLUTION.md case 1)

## Backfill

- A new task or a new transform version usually needs history. Plan the backfill as a run of its own: the range, the order, the expected volume, how its output is checked, and what downstream consumers see while it runs. Orchestrators can backfill new tasks added to the graph. [book:fundamentals-data-engineering], Orchestration
- For a breaking schema change, reprocess history into the new schema before consumers switch, either from the producer's own store or by rewinding its input. [book:building-event-driven-microservices], Reprocessing Historical Data for Breaking Schema Changes

## Schema change

- Validate the schema first when data enters a layer; reject records that do not match, or evolve the schema on purpose. [book:practical-lakehouse-architecture], Data Processing
- A breaking change to a contract is a new contract version, negotiated with the consumer before release. [book:financial-data-engineering], Principle 8: Data Contracts

## Where language models sit in a pipeline

- Let a model do what varies between sources: which extracted value maps to which concept on this document, which of several candidate values was misread. Let code do what does not vary: sums, scaling, unit conversion, comparisons and every rule. A deterministic check can be re-run and explained line by line; a model's judgement cannot. (derived: EVOLUTION.md case 9)
- Store the model's output (the mapping, the proposed correction) with the model version and its evidence, so a replay can either reuse it or re-ask the model on purpose. (derived: EVOLUTION.md case 9)
- Nothing a model proposes is promoted to the curated layer on the model's authority alone. (derived: EVOLUTION.md case 8)
