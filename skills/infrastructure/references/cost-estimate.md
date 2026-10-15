# Infrastructure cost estimate

How to build a cloud cost estimate that a reviewer can reproduce: per environment, per service, with each figure's period, driver and source. The fields of a client-facing cost row (layer, component, purpose, region, SKU, sizing driver, billing note, monthly min–max) are set in `../../solution-architect/references/estimation-and-costing.md`, section "Cloud cost by environment"; this module covers how the figures are produced. Workbook mechanics (formulas, recalculation, read-back) are in `../../xlsx/SKILL.md`.

## Workbook structure

| Sheet | Holds |
|---|---|
| Basis | Region, agreement type (pay-as-you-go, enterprise agreement, reseller), currency, list or discounted, price source and retrieval date, exclusions |
| Rate card | One row per meter: rate, unit, source. Every other sheet links here; no rate is typed twice |
| One per environment | Inputs (start and end week, running hours, sizes, volumes), one service per row, a total labelled with its period |
| Run projection | Months after go-live, one column per year, growth assumptions |
| Roll-up | Formulas over the environment totals; every environment sheet included or excluded with the reason beside the total; a check cell that must read zero |
| Changes | When the workbook is derived from another: sheet, cell, old value, new value, reason |

- A roll-up cell is a formula over the detail, never a typed total (`../../xlsx/SKILL.md`, principle 3).
- An exclusion list on the sheet names what is not priced (egress, monitoring ingestion, secrets store, support plans, people). A component named anywhere in the workbook's notes or the architecture and absent from the cost rows must appear in that list. (derived: EVOLUTION case 2)

## Periods

- **One hours-per-month constant in one cell** (730 is the usual convention) and one hours-per-week constant (168). A second value elsewhere is a defect. (derived: EVOLUTION case 1)
- A phase's billing months = weeks × 168 / 730. Monthly rate × billing months = whole-phase cost.
- **Never add a monthly run-rate to a whole-phase total.** Convert first, then add. (derived: EVOLUTION case 1)
- Every total's label states its period and pricing basis: "per month", "whole phase, weeks 1–9", "year 2", "36 months, reserved".
- Keep one-off build cost and recurring run cost in separate columns. A grand total that adds them shows both parts beside it.
- Phases that overlap or share a boundary week: count each week once per environment and check the week slots add up to the plan. (derived: EVOLUTION case 1)

## Pricing basis

- **Pay-as-you-go bills running time only; a reservation bills continually in exchange for a discount**, so pausing a capacity saves money only on pay-as-you-go. [book:llms-in-production], 6.2.1 Provisioning clusters; [book:designing-distributed-systems], Patterns for FaaS. Storage bills whether compute runs or not. (derived: EVOLUTION case 4)
- **Use a reservation only for a period over which the requirement will not change**: it is paid for the whole term, is not refunded if unused, and usually cannot be altered. [book:cloud-native-devops-kubernetes], Using Reserved Instances; [book:llms-in-production], 6.2.1 Provisioning clusters
- A phase shorter than the reservation term is priced pay-as-you-go, with paused hours if the service allows pausing. When a workbook argues that one reservation covers both build and run, check the committed units against the units in use in every month of the term; committed units unused in early months are still billed. (derived: EVOLUTION case 2)
- The discount comes from the provider's rate card for the region, term and agreement, not from a rounded public figure; a one-year discount is not applied to a three-year term without a source. (derived: EVOLUTION case 2)
- Price at the deployment region. When the price source is another region, state it on the Basis sheet and on every affected line. (derived: EVOLUTION case 2)

## Drivers

Every consumption line names its driver, its monthly value, and the driver's source:

| Source class | Meaning | What the reader can do with it |
|---|---|---|
| Measured | Counted from real inputs (pages, files, requests, GB) | Trust it within the sample's limits; state the sample size |
| Stated by the client | A figure the client gave, with where they gave it | Hold the client to it |
| Assumption | Our estimate, with owner and what would replace it | Ask for it to be replaced before it travels |

- **Production volume = the client's stated business volume × a measured unit size** (for example statements per month × measured pages per statement). When the unit size depends on what the client submits (a whole report or an extract), ask the client; do not pick the reading that suits the total. (derived: EVOLUTION case 3)
- Non-production volumes are stated fractions of production with a reason (a test batch, a regression set). (derived: EVOLUTION case 2)
- Related drivers must agree with the notes describing them: if a note says one engine handles about 80% of documents, the page split in the cells says the same. (derived: EVOLUTION case 2)
- The capacity forecast must extend beyond the lead time for acquiring capacity, and load tests tie raw capacity to service capacity. [book:site-reliability-engineering], Provisioning
- Once the system runs, compare the forecast with measured consumption until they match; divergence means the forecast is unstable. [book:site-reliability-engineering], Overloads and Failure
- Review sizing (instance size, container requests, capacity tier) against measured use after go-live; oversizing is usually found first on the monthly bill. [book:cloud-native-devops-kubernetes], Optimizing Pods
- **Correct a driver on its merits, whichever way the correction moves the total.** A correction that happens to help the argument needs more checking, not less. (derived: EVOLUTION case 3)

## Run projection

- A funder or client may assess support against the consumption the solution generates over several years. That projection is driven by production volume over the run, not by build-phase capacity. (derived: EVOLUTION case 3)
- Show pay-as-you-go and committed pricing as two columns; state the commitment term and whether it renews.
- Attribute run cost to the consumption that drives it, so the reader sees which meter dominates; the result is an approximation for decisions, not a bill. [book:building-multi-tenant-saas], Cost-per-Tenant Metrics
- Growth rates per year are assumptions unless the client stated them; mark them so.
- State whether non-production environments are kept after go-live, and price them on that basis.

## Rescoping an existing workbook

To price a smaller scope (one environment instead of three, a shorter phase) from an existing workbook:

1. **Copy the workbook; never edit the owner's file.** Name the copy for the scope it prices.
2. **Map every sheet:** role (rate card, environment, run projection, roll-up) and the period of each total.
3. **Write the target scope as inputs:** which environments run, weeks, running hours, pricing basis, which services are out, volumes.
4. **Change input cells only.** A cell that links to a shared input (a discount on the run sheet) may be overridden with a value for one environment; the shared input stays, so the run projection is unchanged. A computing formula is never overwritten. Log every change in the Changes sheet.
5. **Exclude an environment through its own inputs** (zero duration or zero running hours), keeping its rows, so totals and shared-cost allocations recompute. Deleting a sheet or skipping it in a sum leaves allocations of shared resources wrong. (derived: EVOLUTION case 4)
6. **Recalculate and read back** (`../../xlsx/SKILL.md`, flow steps 3 and 4). Every check cell reads zero; the target total equals the sum of its parts.
7. **Check shared-resource allocations** after the change: their factors should still add to one resource for the period. (derived: EVOLUTION case 4)
8. **Check that the run projection moved only where the scope changed it.**
9. **Retitle and re-note** every label whose wording no longer matches its inputs (a title saying "reserved" over a pay-as-you-go sheet).
