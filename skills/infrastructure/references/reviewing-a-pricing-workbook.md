# Reviewing a pricing workbook

How to check a cloud pricing workbook someone else owns: reproduce its totals, find what is wrong, and hand back a list the owner can act on. The method for building one is in [cost-estimate.md](cost-estimate.md); the mechanics of reading and recalculating a workbook are in `../../xlsx/SKILL.md`.

## Ground rules

- **The workbook stays its owner's.** Work on a copy. The output is a defect list with sheet and cell, not an edited file. (derived: EVOLUTION case 2)
- Read both the formulas and the cached values; a figure that exists only as a cached value cannot be checked (`../../xlsx/SKILL.md`, principle 1).
- **Reproduce before judging.** Recalculate the copy and recompute the headline totals from their inputs. A total you cannot reproduce is the first finding.
- Any figure quoted outside the workbook (in an email, a deck, a funding request) is traced back to its cell before the review starts. A quoted figure that no single cell computes is a finding in its own right. (derived: EVOLUTION case 1)

## Pass 1 — Map

List every sheet with its role (rate card, environment, run projection, roll-up) and the period of each total in it. Then answer:

- Is every environment sheet in a total, or excluded with a reason written beside that total?
- Does the number of environment sheets match the environments the plan provisions? An environment with no plan row is unfunded work or an unneeded cost; a planned environment with no sheet is unpriced.

(derived: EVOLUTION cases 1 and 3)

## Pass 2 — Units and periods

- Totals added together have the same period. A monthly run-rate added to a whole-phase total is the defect this pass exists for. (derived: EVOLUTION case 1)
- One hours-per-month constant and one hours-per-week constant across the workbook; search formulas for a second value.
- Phases that share a boundary week do not bill the same week twice for the same environment.
- Each total's label states its period; a label that names a different basis from its formula (a "reserved" title over a pay-as-you-go input) is a finding.

## Pass 3 — Rates and basis

- **One rate, one cell.** Scan formulas for rate values typed as literals and environment sheets for rates copied as values; a change to the rate card must reach every sheet. (derived: EVOLUTION case 2)
- Region and agreement type are stated once, and the rates are for that region. (derived: EVOLUTION case 2)
- Discounts come from a rate card for the stated term; a commitment discount is applied only where usage covers the term. Where one commitment is argued to cover several phases, compare committed units with units in use month by month. [book:cloud-native-devops-kubernetes], Using Reserved Instances; [book:llms-in-production], 6.2.1 Provisioning clusters
- Pausable capacity on pay-as-you-go: check the running-hours input matches the environment plan; a reserved capacity bills every hour whatever the input says. [book:llms-in-production], 6.2.1 Provisioning clusters

## Pass 4 — Drivers

- Each consumption input has a source class (measured, stated by the client, assumption with owner). An input marked "assumption" with no owner or replacement is a finding; the largest driver is checked first.
- Notes and cells agree (a split described in a note equals the split in the cells).
- Production volume traces to the client's business volume times a measured unit size. Test the implied unit size (volume ÷ business count) against measured inputs. (derived: EVOLUTION case 3)
- Ratios between related drivers fit how the workload behaves (output tokens against input tokens, pages per document); a ratio that looks inverted is a question for the owner.

## Pass 5 — Coverage

- Every component in the architecture or resource inventory has a cost row or appears in the exclusion list.
- A component the workbook names in its own notes (a log workspace, a secrets store) and also lists as "not included" is a finding: it will be billed.
- Shared resources are allocated across environments and the allocations add to one resource for the period.
- Flat figures supplied by a person (network, support) name who supplied them and what they include.

(derived: EVOLUTION case 2)

## Pass 6 — Checks

- Recalculate; every check cell reads zero; every roll-up equals the sum of its parts.
- A grand total that adds one-off build to recurring run shows both parts.

## Report

One row per finding:

| # | Class | Finding | Where (sheet!cell) | Effect on total | What to do |
|---|---|---|---|---|---|

- Classes: unit or period, coverage, rate or basis, driver, consistency, label.
- **State the direction of each correction (raises or lowers the total) and recommend it on its merits either way.** A correction that helps the argument is checked twice. (derived: EVOLUTION case 3)
- Put the reproduced headline totals at the top, with any that did not reproduce.
- Mark what is the owner's to decide (rates, SKUs, formulas) and what the reviewer can supply (measured volumes, the component list).
