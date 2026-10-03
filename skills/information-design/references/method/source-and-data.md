# Source and data: preserve meaning while preparing a dataset

## Reader and scope

**Reader:** a designer moving from a topic to an analysable dataset. **Scope:** check source credibility, preserve the original, understand fields and definitions, join context, and make selection and missingness explicit. Domain source authority and field definitions remain owned by the project.

**Source lessons:** [course 2495 · U3 L07](../course-2495/U03-L07-finding-the-data-the-sources.md) and [L08](../course-2495/U03-L08-the-data.md); [course 4217 · U3 L08](../course-4217/U03-L08-selecting-the-topic.md), [L09](../course-4217/U03-L09-creating-the-dataset-1.md) and [L10](../course-4217/U03-L10-creating-the-dataset-2.md); [course 3601 · U3 L06](../course-3601/U03-L06-where-to-find-data.md), [L07](../course-3601/U03-L07-data-preparation.md) and [L08](../course-3601/U03-L08-knowing-your-data.md); [course 3069 · U2 L04](../course-3069/U02-L04-looking-for-data.md), [L05](../course-3069/U02-L05-harvesting-the-data.md) and [L06](../course-3069/U02-L06-the-data-for-your-visualization.md).

## Find and assess the source

- Check the source's history, affiliated organizations, and how it is cited; inspect its available data tables, charts, notes, and coverage before selecting a dataset. (2495 · U3 · L07 · 01:14–02:08; 2495 · U3 · L07 · 02:08–03:19; 2495 · U3 · L07 · 03:19–04:30; 2495 · U3 · L07 · 04:30–05:38)
- Search for a specific question, open likely results, compare summaries with primary sources, and read methodology for definitions, scope and gaps. (3601 · U3 · L06 · 02:01–03:09; 3601 · U3 · L06 · 03:09–04:40; 3601 · U3 · L06 · 04:40–06:16)
- Choose a subject from a source the designer trusts and is curious about; gather related tables, charts, notes and available years before fixing the dataset. (4217 · U3 · L08 · 00:00–01:39; 4217 · U3 · L08 · 01:39–03:39)
- Name the data source so readers can trace where it came from. (3069 · U2 · L04 · 01:20–04:00)
- If the dataset is built from a text or other source, make repeated passes, record selected elements, and tabulate counts by a meaningful group such as chapter. (3069 · U2 · L05 · 00:00–03:31; 3069 · U2 · L05 · 03:31–06:35)

## Prepare the working data

1. Retain an untouched copy of the download; make a separate working copy. Remove irrelevant rows or columns and clarify headers. (2495 · U3 · L08 · 00:00–01:11; 2495 · U3 · L08 · 01:11–02:27; 3601 · U3 · L07 · 01:16–02:24)
2. Inspect values and categories before choosing the story; use filters, sorts, totals and comparisons to understand the dataset. (2495 · U3 · L08 · 02:27–05:01; 3069 · U2 · L06 · 00:40–01:28; 3069 · U2 · L06 · 01:28–02:44; 3069 · U2 · L06 · 02:44–03:25)
3. Record source definitions before choosing a measure. (3601 · U3 · L08 · 02:24–04:35; 3601 · U3 · L07 · 05:38–07:19) The clean-water example records missing years and uses an available nearby year; it treats coverage gaps as information that may belong in the story. (3601 · U3 · L08 · 04:35–07:26; 3601 · U3 · L08 · 07:26–10:06)
4. When joining context tables, match on stable names or keys, inspect matched-row counts, investigate unmatched rows, and remove unused fields only after checking. (4217 · U3 · L10 · 05:09–09:24; 4217 · U3 · L10 · 15:31–18:56)
5. Put the intended unit and year beside the field; note when a value substitutes for the intended year. In the CO₂ example, population and GDP provide context while per-capita emissions carry the time-series information. (2495 · U3 · L08 · 12:22–15:43; 2495 · U3 · L08 · 15:43–18:34; 2495 · U3 · L09 · 01:08–02:33; 2495 · U3 · L09 · 02:33–03:35)

## Make selection reproducible

Write the filter in reader-facing terms: entity set, ranking or threshold, period, and exclusions. The renewable-energy project selects the 40 countries with the highest share in 2020; the population example uses the top 40 countries above ten million people; the clean-water project considers 138 countries across 2000 and 2020. These are examples of explicit scope, not defaults for other projects. (4217 · U3 · L09 · 03:21–04:02; 4217 · U2 · L05 · 03:40–04:39; 2495 · U2 · L05 · 04:17–06:14; 3601 · U3 · L09 · 03:18–07:00)

The renewable-energy workbook filters to 2020, sorts by share and checks the count of 40 selected countries before joining other fields. Keep that row-count reconciliation with the working data. (4217 · U3 · L09 · 04:02–06:06; 4217 · U3 · L09 · 06:06–09:18; 4217 · U3 · L09 · 09:18–09:44)

**Rule synthesized (derived):** every plotted value should be traceable through its transformation to a source record, and every change of population, period, unit or definition should have a written reason. This joins the courses' preserved working copies, documented selections, unmatched-row checks, and missing-year notes. (derived from 2495 · U3 · L08 · 01:11–02:27; 2495 · U3 · L08 · 02:27–05:01; 4217 · U3 · L10 · 05:09–09:24; 4217 · U3 · L10 · 09:24–12:48; 4217 · U3 · L10 · 12:48–15:31; 4217 · U3 · L10 · 15:31–18:56; 3601 · U3 · L07 · 03:34–05:38; 3601 · U3 · L08 · 07:26–10:06)

## Failures

**Problem 1: a visually convincing but unreconciled dataset.** A missing join or incorrect copied value can become a false mark. Compare copied data and match counts with the source, then resolve every mismatch. (4217 · U3 · L10 · 05:09–09:24; 3601 · U3 · L07 · 03:34–05:38)

**Problem 2: invisible selection.** A static view cannot show every value from a large source. State what was selected and why. (2495 · U2 · L05 · 02:55–04:17; 4217 · U2 · L05 · 03:40–04:39)

## Check before moving on

Pass T2 and T3 when sources, fields, units, filters, joins, exclusions, missing values and substitute years are recorded; counts and values reconcile with the retained source. Return to data preparation for unresolved mismatches, and to scope when readers cannot see the selection rule.

**Practice the teachers set:** retain a source tab, clean a working dataset, explore it with filters and ordering, and record variables. See [course 2495, Unit 3](../course-2495/U03-unit.md), [course 4217, Unit 3](../course-4217/U03-unit.md) and [course 3601, Unit 3](../course-3601/U03-unit.md).

## Freshness and ownership

**Maintainer:** information-design skill owner. **Last reviewed:** 2026-10-02. **Review due:** when a source course, source-data contract or domain methodology changes.
