# Lineage and traceability

How to trace any published value back to the source and the transforms applied to it, and how to say how much a value has been checked.

## Two kinds of lineage

- **Pipeline lineage** maps how datasets flow from sources through transformations to reports, and shows what a change upstream affects downstream. [book:data-quality-fundamentals], Building End-to-End Field-Level Lineage for Modern Data Systems
- **Value provenance** links each instance of the data to the process that created it and to the instance before it. [book:machine-learning-production-systems], ML Metadata

A design needs both. Pipeline lineage answers "what breaks if this transform changes"; value provenance answers "why does this number differ from the page".

- Go to field level; table level is too coarse to fix problems quickly. Build lineage from metadata, logs and queries rather than reading the data itself, and keep it updated automatically. [book:data-quality-fundamentals], Basic Lineage Requirements
- Identify the data elements, trace each back to its origin, and keep a repository of sources and their elements. [book:data-governance-definitive-guide], Data Lineage Monitoring
- Lineage follows the data lifecycle: extraction, transformation, storage, usage and archiving. [book:financial-data-engineering], Principle 5: Data Lineage

## What travels with each value

For data extracted from documents, every value in the cleaned and curated layers carries:

1. **A reference to the raw record** it came from, by key, not a copy: document, page, text span or bounding box, and the extractor version.
2. **The transform** applied, by rule identifier and version.
3. **The transform's evidence**: where the unit or scale was declared, which header text gave the column, which token matched the entity identifier.

Without the third item the value cannot be defended. "Scale applied x1000" does not answer a reviewer who sees a different number on the page; "scale applied x1000, declared in the statement header on page 42, characters 118 to 126" does. (derived: EVOLUTION.md case 2)

Add, for curated values: the checks the value passed, and the reviewer's decision if it was reviewed. (derived: EVOLUTION.md case 8)

## Signed and unsigned data

- Say what kind of approval each curated value carries. A reviewer who signs a document after resolving its flagged fields has approved those fields directly; the rest of the document is approved by association. Wherever a consumer retrieves narrative text or unreviewed fields, say which kind of approval it has; one word such as "verified" must not cover both. (derived: EVOLUTION.md case 8)
- Promotion records the approval at the grain it was given: field by field for figures, per document for text, as the design states.
- A value without a promotion record is unsigned, and any consumer that shows it must be able to say so.

## Consumers and mixed provenance

- A consumer reads from the layer whose promise it makes. If the product promises reviewed figures, the index and the exports read the curated layer; if they read the cleaned layer, the output is unreviewed and must be labelled that way. (derived: EVOLUTION.md case 6)
- Data loaded from elsewhere (a client's earlier manual extracts, a third-party feed) enters through the raw layer, or carries a provenance field that marks it as unverified. Otherwise a query mixes reviewed and unreviewed values with nothing to tell them apart. (derived: EVOLUTION.md case 6)
- Each consumption record keeps a pointer back to the curated row it was built from.

## Keep the original

- Keep the original source file, and its hash, for as long as any derived value may be questioned. The page image is what a reviewer compares against. [book:practical-lakehouse-architecture], Data Storage (part 1)
- Pass source metadata (origin, format, uploader, date) forward to later layers. [book:building-medallion-architectures], Bronze Layer

## Lineage in the review interface

Show the reviewer the source page region next to the value, the transform chain, and the rule that flagged it. A correction is recorded with who made it and when, and re-runs the checks it affects. (derived: EVOLUTION.md case 8)
