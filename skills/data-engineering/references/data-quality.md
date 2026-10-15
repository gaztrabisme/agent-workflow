# Data quality

Which checks to write, where they run, what stops the pipeline, how to monitor, and how to keep false alarms down.

## Decide what matters first

Agree with the consumers which data matters and to whom before writing checks; testing everything is not possible. [book:data-quality-fundamentals], Understanding Data Quality Downstream

Pick the dimensions that fit the use; there is no fixed list. Common ones: completeness, timeliness, validity, accuracy, consistency, uniqueness. [book:data-quality-fundamentals], Understanding Data Quality Downstream; [book:practical-lakehouse-architecture], Data and ML Model Quality. For financial data add errors, outliers, granularity, duplicates and constraints; typical errors are wrong decimal places, extra or missing digits, inverted rates and rounding. [book:financial-data-engineering], Dimension 1: Data Errors

## Check types

| Check | Asks | Example |
|---|---|---|
| Schema | Does the record match the contract? | types, required fields, formats |
| Null and missing | Is any value unknown or absent? | a required field is empty |
| Volume | Did any data arrive, too little or too much? | page count of a filing far from the batch norm |
| Freshness | How old is the data? | the last load is two days late |
| Distribution | Are values in the accepted range, in one unit? | a value a thousand times its peers |
| Uniqueness | Is anything duplicated? | the same filing ingested twice |
| Known invariants | Does a relationship that must hold, hold? | components sum to the stated total |

Sources: [book:data-quality-fundamentals], dbt Unit Testing; [book:data-quality-fundamentals], Measuring and Maintaining High Data Reliability at Ingestion (part 1)

- Split technical validation (type, length, format) from business validation (value ranges and rules). [book:practical-lakehouse-architecture], Data Processing
- Run checks before transformation and after each transformation step. Load into a staging table, test it, and promote only what passes. [book:data-quality-fundamentals], dbt Unit Testing
- Keep failed records: send them to an error table or the invalid part of the cleaned layer for review, rather than dropping them. [book:practical-lakehouse-architecture], Data Storage (part 1)

## Stop rules

- When a check fails, alert the owner of that data and do not run the downstream steps. [book:data-quality-fundamentals], dbt Unit Testing
- Put circuit breakers in the orchestration: the circuit is closed while data flows and opens when a quality threshold is missed, so bad data does not mix with good. Typical places: after an upstream load, and in the middle of a pipeline when its input is found wrong. [book:data-quality-fundamentals], Managing Data Quality with Apache Airflow
- For each check, write down: the threshold, whether failing stops the pipeline or only flags the record, who is alerted, and how the record is released once fixed.

## Rules that gate, signals that rank

- When the domain gives deterministic relationships (totals, roll-forwards, cross-references), use rule failures to decide what goes to a human, and use model confidence only to order that queue. A confidence threshold only surfaces errors the extractor already doubted; a rule also catches the confidently wrong value. (derived: EVOLUTION.md case 9)
- State the residual: a wrong value that is consistent with every other value breaks no rule. Measure that gap on a labelled sample; do not claim it is zero. (derived: EVOLUTION.md case 9)
- Give each flag a reason a reviewer can act on ("items sum to 6,500, stated total 6,000") rather than a score.

## False positives from legitimate differences

- A rule that is true in general can fire on correct data. Before a rule goes live, list the legitimate reasons it may not hold (a domain standard, a permitted presentation, a currency effect) and encode each as a suppression or an applicability condition with its source. (derived: EVOLUTION.md case 12)
- Decide per rule what happens when an input is absent: skip or fail. Absence of a line is often legitimate. (derived: EVOLUTION.md case 12)
- Normalise units and scale before any comparison; a single document can mix them. (derived: EVOLUTION.md case 12)
- Let users add the rules for the cases where the data must be perfect, from their own judgement, rather than generating rules automatically; a rule that fails on history is a finding to explain. [book:automating-data-quality-monitoring], The Limits of Automation

## Monitoring

- Monitor five things across the whole pipeline: freshness, distribution, volume, schema and lineage. [book:data-quality-fundamentals], Data Observability
- Standard table and column metrics (rows per load, time since last update, share of nulls) get coverage quickly, but cost computation per column and cause alert fatigue: one change can raise ten alerts. Group related alerts and add custom metrics for the segments that matter. [book:automating-data-quality-monitoring], The Limits of Automation
- Compare each new batch's statistics with a baseline batch, with a threshold per field, to catch drift. [book:building-machine-learning-pipelines], 4. Data Validation (part 3)
- Set reliability targets with the consumers: take stock of priorities, learn their tolerance for poor data, set objectives, then measure. A target set without the consumers' agreement is not useful. [book:data-quality-fundamentals], How to Set SLAs, SLOs, and SLIs for Your Data

## Measured rates and their denominator

- A false-positive or error rate depends on which layer it was measured on. Cleaning that moves upstream (unit scaling, column detection) removes failures before a rule sees them, so the rate improves without the rules improving. Report every rate with the layer and the sample it was measured on. (derived: EVOLUTION.md case 7)
- Accuracy and coverage claims go through `../../applied-ml-problem-solver/SKILL.md` when they evaluate a model.
