# Layers and contracts

How to decide what each storage layer holds, who writes it, when it may change, and what the agreement between two layers says.

## Layer roles

Name the layers however the team likes; the names are a convention, not a standard. What must be fixed is each layer's job. Most designs use these four:

| Layer | Holds | Written by | Mutability |
|---|---|---|---|
| Raw (bronze, landing, raw zone) | What the source said, in its original structure | The ingestion or extraction step | Immutable, append-only |
| Cleaned (silver, cleansed zone) | What the source means: typed, standardised, deduplicated, resolved | Deterministic transform code | Rebuilt from raw; never edited by hand |
| Curated (gold, presentation zone) | What the business has accepted or modelled for use | A promotion step: sign-off, or a modelling job | Append-only; enters only through the promotion step |
| Consumption (index, export, semantic views) | What a user asks for | Indexing, export or view jobs | Disposable; rebuilt from curated |

- The raw layer stores data in its original structure, without transformation, as the historical record; it is immutable to keep its original state. The cleaned layer applies quality checks, standardisation and deduplication while staying granular. The curated layer serves specific business use. [book:building-medallion-architectures], The Three-Layered Design
- Keep raw files for reprocessing and for audit, for an extended period; archive them to cheaper storage after processing. [book:practical-lakehouse-architecture], Data Storage (part 1); [book:architecting-data-ml-platforms], Store
- The number of layers follows the job: a simple provider may need two; many sources used for many purposes may need four or five. [book:building-medallion-architectures], Tailored Medallions Architectures
- For documents (PDF, scans), keep the original file in raw storage with metadata on its source, format, uploader and date, and pass that metadata forward to later layers. [book:building-medallion-architectures], Bronze Layer

## Rules for placing work

- **Nothing derived goes into raw.** As soon as a value is scaled, a period label resolved, or two records matched to one entity, it is no longer what the source said. A raw layer that holds derived values cannot be replayed, and replay is the reason to keep an immutable layer. (derived: EVOLUTION.md case 1)
- **Split every transform into detect and resolve.** The raw layer records the observation: the literal string, where it was printed, the unit as printed. The cleaned layer records the interpretation: the typed value in base units, the resolved period, the resolved entity, and which rule produced each. (derived: EVOLUTION.md case 2)
- **Working state is not the curated layer.** A review queue, draft corrections and assignments are mutable by design. Keep them in an operational store, and make the curated layer the promoted output only. (derived: EVOLUTION.md case 5)
- **Measurement is a component, not a layer.** An evaluation harness reads several layers; filing it inside one either double-counts it or loses it in the plan. (derived: EVOLUTION.md case 7)
- **One document is the authority for the layer model.** When the pipeline description, the scope list and the diagram disagree about where data goes, write one layer spec, mark it normative, and list what each other document must change. (derived: EVOLUTION.md case 13)

## Grain and keys

- State the grain of every table in the cleaned and curated layers as its key, for example `(entity, period, basis, concept)`.
- **Put values that must never be compared in separate rows, keyed by the attribute that separates them.** A row that holds both invites the forbidden comparison; separate rows mean no expression can reach both. (derived: EVOLUTION.md case 3)
- **Detect structure per source; never assume it.** Column layout, number of periods, units and sign convention are read from each document. The key says what a value is once the structure is known; it does not say what structure to expect. (derived: EVOLUTION.md case 4)
- The team, not the storage engine, keeps keys unique: most columnar stores do not enforce uniqueness. [book:fundamentals-data-engineering], Batch Transformations (part 3)
- Identity across sources is entity resolution: matching records that refer to the same entity when no shared identifier exists. Name the identifier used, its authority, and the rule for records that lack it. [book:financial-data-engineering], Entity Resolution Described

## Data contracts

A data contract is an agreed interface between the producer of data and its consumers: what the data is, how it is governed, and what quality it meets. [book:financial-data-engineering], Principle 8: Data Contracts; [book:building-medallion-architectures], Data Contracts

Write one contract per boundary: source to raw, raw to cleaned, cleaned to curated, curated to each consumer. Each contract states:

- Structure and types: fields, names, types, defaults and limits. Schemas are the base of a contract. [book:building-event-driven-microservices], Chapter 4. Schemas and Data Contracts
- Meaning: units, scale, currency, sign convention, rounding, period convention. [book:financial-data-engineering], Principle 8: Data Contracts
- Quality: the checks the producer guarantees and what happens to records that fail.
- Timing: when data is ready, and what the consumer does if it is late.
- Owner and contact, and the version. A changed contract is a new version agreed by both sides. [book:financial-data-engineering], Principle 8: Data Contracts
- Validate incoming data against the agreed schema at ingestion. [book:practical-lakehouse-architecture], Core Components of a Data Platform (part 2)

## A model or external service as a source

When an extraction model or third-party service produces the raw records, treat its output as a source with a contract: the fields it returns (value, confidence, location on the page), its version, and what the pipeline does when a field is absent. If the client owns or has accepted that service, its accuracy is their dependency: state the boundary in the assumptions rather than building fallbacks for it. (derived: EVOLUTION.md case 10)

Record the service version on every raw record. A re-extraction with a new version is a new raw record, not an overwrite. (derived: EVOLUTION.md, Evolution 1 test, flag 3)

## Source stakeholders

Name the systems owner and the data owner of every source; they are often different people. Set up a feedback loop with them, so they know how the data is used and you hear about changes before they arrive. [book:fundamentals-data-engineering], Whom You'll Work With
