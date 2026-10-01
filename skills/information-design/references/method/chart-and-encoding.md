# Chart and encoding: choose forms for the question and precision

## Reader and scope

**Reader:** a designer who has a reader's question and checked fields. **Scope:** choose a chart form, map each field to a visible channel, set scales and ordering, then test with the actual data. Course chart examples are options, not an exhaustive taxonomy. Palette science belongs with `color-theory`; broad composition belongs with `visual-design`.

**Source lessons:** [course 4217 · U2 L03](../course-4217/U02-L03-a-visual-translation-of-contents-the-role-of-perception.md) and [L04](../course-4217/U02-L04-the-questions-to-start-with.md); [course 3601 · U2 L03](../course-3601/U02-L03-what-is-data.md), [U3 L09](../course-3601/U03-L09-transforming-data-into-visuals.md) and [U4 L12](../course-3601/U04-L12-laying-out-all-the-components.md); [course 2495 · U2 L03](../course-2495/U02-L03-designing-visual-alphabets.md), [U3 L09](../course-2495/U03-L09-from-google-sheets-to-the-paper.md), [U4 L11](../course-2495/U04-L11-designing-the-skeleton-with-rawgraphs.md), [L12](../course-2495/U04-L12-editing-with-adobe-illustrator-1.md), [L13](../course-2495/U04-L13-adobe-illustrator-2.md) and [L14](../course-2495/U04-L14-adobe-illustrator-3.md); [course 3069 · U3 L08](../course-3069/U03-L08-method-and-colours.md) and [L10](../course-3069/U03-L10-incorporating-the-elements-into-your-design-1.md).

## Match the chart to the relation

| Reader task or data relation | Starting form shown in the courses | Check before keeping it | Source |
|---|---|---|---|
| Change through many time points | Line chart; the values occupy positions on a time axis. | Does the line preserve the time order and show the trend the question asks about? | (4217 · U2 · L03 · 02:18–04:02; 4217 · U2 · L04 · 01:08–02:25) |
| Compare only a start and end point | Slope chart, with a shared scale for each series. | Are endpoints and period named, with crossings or outliers still readable? | (3601 · U3 · L09 · 03:18–07:00) |
| Compare many groups or regions | Small multiples can split a crowded comparison. Keep axes consistent when comparing panels. | Does every panel use the same scale and category definition? | (3601 · U3 · L09 · 03:18–07:00; 3601 · U4 · L12 · 06:48–09:26) |
| Compare two quantitative fields | Scatterplot; each mark's position carries both values. | Are both axes named, and is the mark order meaningful? | (4217 · U2 · L03 · 02:18–04:02) |
| Add a third quantitative field | Bubble chart adds area to the two positional fields. | Is area only supporting a comparison that does not require fine precision? | (4217 · U2 · L03 · 02:18–04:02; 2495 · U2 · L03 · 01:31–03:02; 3069 · U3 · L08 · 01:07–03:16) |
| Compare category amounts | Bar or span forms are shown among the course examples. | Is the scale honest and is category order purposeful? | (4217 · U2 · L03 · 01:32–02:18; 4217 · U2 · L03 · 02:18–04:02) |
| Show a repeated series in a custom visual model | A radial time-series structure is built for the CO₂ example. | Does one mark or segment represent a fixed, labelled time unit? | (2495 · U4 · L12 · 04:22–05:31; 2495 · U4 · L12 · 05:31–07:47; 2495 · U4 · L12 · 07:47–09:35) |

These forms also appear as editable starting files in [templates/README.md](../../templates/README.md). A chart form used in an example is not a universal recommendation; the task and field types still govern.

## Assign channels and preserve value meaning

- Make a channel-to-field table before drawing. (derived: this turns the courses' visual-variable lists and chart-to-data examples into an explicit mapping step; 4217 · U2 · L03 · 00:00–01:32; 4217 · U2 · L03 · 02:18–04:02; 2495 · U2 · L03 · 01:31–03:02)
- Possible visual variables include position, orientation, shape, size, line thickness, texture and repeated elements. (2495 · U2 · L03 · 01:31–03:02) Course 4217 also lists opacity and colour. (4217 · U2 · L03 · 00:00–01:32)
- Record whether each field is nominal, ordinal, discrete quantitative or continuous quantitative before assigning its scale and mark. (3601 · U2 · L03 · 00:00–02:43)
- When readers must compare numerical ratios, course 4217 cites a ranking of position, length, area, angle and intensity, in that order. It describes this as typical precision for verbally stating the ratio between two values, not as an all-purpose chart selector. (4217 · U2 · L03 · 02:18–04:02)
- Course 3601 likewise prefers length for small changes on a finite percentage scale and allows area when the range is broad and exact precision matters less. (3601 · U3 · L09 · 07:00–09:50)
- Course 4217 says project needs can make engagement or exploration more important than immediacy; a bar is not automatically better just because it reads quickly. (4217 · U2 · L03 · 01:32–02:18; 4217 · U2 · L04 · 04:45–05:21)
- In course 2495's CO₂ example, contextual axes change from actual values to ordinal positions to improve spacing, while actual population and GDP values are labelled separately. State that distinction explicitly whenever using this technique. (2495 · U4 · L11 · 01:31–02:46; 2495 · U4 · L11 · 02:46–04:21; 2495 · U4 · L14 · 03:01–05:47; 2495 · U4 · L14 · 05:47–08:17)
- Align marks with their data positions and keep only the guides that clarify order; trim guide lines that extend into marks or add noise. (2495 · U4 · L13 · 06:55–10:10; 2495 · U4 · L13 · 13:27–15:44)
- Repeated marks can encode count: the book example changes chapter-circle area with word count and repeats character marks for chapter appearances. Check the count against the table before treating a decorative symbol as data. (3069 · U3 · L10 · 03:41–06:15; 3069 · U3 · L10 · 16:11–18:44)
- Use a zero baseline for bars representing magnitude unless the project has a clearly justified alternative; if an axis starts above zero, label it and check how much it changes perceived difference. (4217 · U2 · L03 · 04:02–05:37)

**Where courses pull in different directions:** the ranking and the small-change example favor position or length when precision matters, while course 4217 permits less immediate forms for engagement and discovery. These are compatible if the brief states which reader task has priority and the key keeps the values recoverable. This is a synthesis, not a new claim about all charts. (derived from 4217 · U2 · L03 · 02:18–04:02; 4217 · U2 · L04 · 04:45–05:21; 3601 · U3 · L09 · 07:00–09:50)

**Rule synthesized (derived):** choose the lowest-complexity channel that can carry the required comparison; add expressive form only when it supports the stated reading and its data mapping remains explicit. Derived from the channel ranking, the project-needs discussion, and the teachers' practice of testing ideas against actual values. (derived from 4217 · U2 · L03 · 02:18–04:02; 4217 · U2 · L04 · 00:00–01:08; 2495 · U4 · L10 · 05:08–06:30)

## Failures

**Problem 1: precise values hidden in low-precision marks.** Bubble area may add a third measure, but the course ranking places it below position and length. Put the precise measure on position or length when the task depends on fine comparisons, or provide a quantitative reference. (4217 · U2 · L03 · 02:18–04:02; 3601 · U3 · L09 · 07:00–09:50)

**Problem 2: rank mistaken for magnitude.** Ordinal axes space items evenly and do not preserve the numeric difference between them. Label the axis as rank/order and state actual values separately. (2495 · U4 · L11 · 01:31–02:46; 2495 · U4 · L11 · 02:46–04:21; 2495 · U4 · L14 · 03:01–05:47; 2495 · U4 · L14 · 05:47–08:17)

**Problem 3: scales that exaggerate or contradict.** Include zero for bar magnitudes by default; if a purposeful break or non-zero baseline is used, mark it clearly and review the impression it creates. (4217 · U2 · L03 · 04:02–05:37)

## Check before moving on

Pass T5 and T6 when every field has a named encoding, the chosen form fits the question, and each displayed value matches the source through the stated scale. Return to chart choice if a comparison is hard to read; return to data preparation if the binding is wrong.

**Practice the teachers set:** sketch several encodings, plot the data to validate them, and change the form if the actual marks do not work. See [course 3601, Unit 3](../course-3601/U03-unit.md) and [course 2495, Unit 4](../course-2495/U04-unit.md).

## Freshness and ownership

**Maintainer:** information-design skill owner. **Last reviewed:** 2026-10-02. **Review due:** when a source course or chart convention changes.
