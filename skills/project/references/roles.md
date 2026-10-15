# Roles

The roles a project needs and who holds each. The skill is written for one person running a project with AI agents; who holds each role is set per project, at the start, in the table below.

## Roles table

Copy this table into the project's record and fill the last column. Role names follow PRINCE2. [book:prince2-managing-successful-projects], C. Roles and responsibilities

| Role | Holds | Held by (default) | Held by (this project) |
|---|---|---|---|
| Executive | The business case; accountable for the project | Someone outside the work (see [Rules that do not depend on headcount](#rules-that-do-not-depend-on-headcount)) | |
| Senior user | Acceptance of the products for the people who will use them | The client | |
| Senior supplier | The supplier's resources and the supplier's business case | Our organisation | |
| Project manager | The plan, day-to-day running, reports to the executive | The one person | |
| Team manager | Producing the products in a work package | The one person, directing agents | |
| Producers | Doing the work in a work package | Agents, each under a brief ([run/flow.md](run/flow.md)) | |
| Project assurance | Checking the work independently of the project manager | An agent with no prior context, briefed with the product's quality criteria, plus the client's acceptance | |
| Change authority | Approving changes within delegated limits | As the project's organisation sets it | |
| Legal review | NDA, contract and data-processing terms | A lawyer; never held by the one person or an agent | |

## Who holds a role

By default the one person and their agents hold every production role. A project's organisation can assign a role to someone else (for example, price and concessions to the project manager, cloud cost to the infrastructure lead). Then our work in that role goes to its holder as a draft for their decision.

## Rules that do not depend on headcount

- **Someone outside the work accepts it.** A one-person company still has a client who accepts and pays, and a business that carries the loss if it fails. PRINCE2 keeps the executive (who owns the business case) and the project manager as two roles, and the executive's accountability cannot be delegated. [book:prince2-managing-successful-projects], 7.2. PRINCE2’s requirements for organization
- **The producer never approves its own work.** Assurance must be independent of the project manager. With one person, the independent reviewer is an agent with no prior context, briefed with the product's quality criteria, plus the client's acceptance. [book:prince2-managing-successful-projects], C. Roles and responsibilities

## Ownership of plan figures

- **Presale WBS and effort estimate:** this skill owns the WBS structure and collecting effort from the leads who will be held to it (the delivery planner or each discipline lead, for their own rows). `solution-architect` decides what belongs in it and owns the response pack. (owner decision 2026-10-11, LSP after-action review)
- **Who confirms estimates:** pre-signature effort figures are authored by the leads who will be held to them; the architect does not author them. A row for another discipline shows who drafted it and which lead confirms it. Rules: [wbs-workbook.md](wbs-workbook.md#drafting-into-a-teams-wbs).
- **Price decisions:** a supplier concession (free work, a lower rate, a cut below the formula) is a decision for the person who sets the price, shown with its amount. Rules: [business-case-and-tolerances.md](business-case-and-tolerances.md#concessions-and-closing-a-price-gap).
- **Release cut and estimates:** the person who owns those decisions makes them; the plan does not fill them in for them. See [anti-patterns.md](anti-patterns.md#planning).
