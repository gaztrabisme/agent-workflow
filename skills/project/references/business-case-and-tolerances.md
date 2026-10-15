# Business case, margin and tolerances

Why the project is worth doing, for the client and for us, and how far the plan may move before someone above the PM decides. Effort figures come from [the estimating reference](estimating.md); change requests after signature are recorded under `delivery`'s [change control](../../delivery/references/change-control.md).

## Two business cases

A supplier's project has two business cases, and both must hold:

- **The client's:** why they are buying. It must stay desirable (benefits outweigh cost and risk), viable (the work can be delivered) and achievable (using it will produce the benefits). The client owns it.
- **Ours:** whether bidding and delivering the project is worth it to us, which on a fixed price means a margin. The person accountable for supplier delivery owns it (on a presale, the delivery head or the internal review board).

[book:prince2-managing-successful-projects], 6.3. Guidance for effective business case management; 6.1. The business case theme

Our business case never appears in a client document. Keep the assumptions that explain how the price is built (PM percentage, contingency policy, margin) on an internal sheet, separate from the assumptions the client reads (as the wbs-estimate skill does).

Both are checked again at each decision point: the end of the presale, each impact assessment of a change or risk, each stage end. A project that has stopped being worth doing is stopped; that frees the money and people. [book:prince2-managing-successful-projects], 3.1. Continued business justification

## Per-feature view for the PM

For the PM who sets the price, prepare one row per feature with estimated cost, price, margin and the concessions made so far. From it, list options: which features can run below cost, what that does to the total margin, and what would recover it. The PM takes the decision and the client conversation; the view only prepares it. (derived: LSP 2026-10-12 — a senior PM described managing each feature's profit or loss and giving ground on one feature while holding the total; none of the skills produced that view.)

Check the total on the worst case as well as the expected one: the highest-effort or lowest-delivery outcome. A bid that is profitable only on the expected case should say so. [book:prince2-managing-successful-projects], 6.4. Techniques: investment appraisal; [book:prince2-agile], 9.3: PRINCE2 Agile guidance for the business case theme

## Tolerances

A tolerance is how far a plan may move on one aspect before the level above decides. Six aspects can carry one: time, cost, scope, quality, benefits and risk. The level above sets it: the client or the internal board for the project, the project board for a stage, the PM for a team's work package. [book:prince2-managing-successful-projects], 3.5. Manage by exception; 12.2. PRINCE2’s requirements for managing progress

- Inside tolerance, the PM adjusts freely. A feature running below cost is fine while the forecast project margin stays inside its tolerance.
- An exception is a **forecast** breach, not an actual one. Escalate when the forecast crosses the line, one level at a time, with the options.
- Write the tolerances down at the start of the presale; without them every adjustment needs a meeting, or none does.

## Fixed price, fixed scope

On a fixed price with fixed scope, the only thing left to flex is our margin. To keep something else that can flex:

- Rank the client's requirements (must, should, could) with the client, so a cut follows an agreed order instead of a negotiation. [book:prince2-agile], 6.1: The concept of flexing what is delivered
- Cut features, not quality: dropping testing, documentation or design to hit a date or price is the cut to avoid. [book:prince2-agile], 6.4: The five targets in more detail
- State every exclusion the same way in every document the client reads. When one slide offers a feature and another excludes it, the client reads the generous version and the team absorbs it. (derived: LSP 2026-10-12 — after a price cut, the deck still offered a mobile app the WBS had dropped, and described turnkey delivery including civil works while an assumption had the client supply power, network and cabinets.)
- A client requirement dropped from the bid is a deviation from the request: list it as excluded, so it can return as a priced change.
- Trace a scope cut through every text that describes the scope: acceptance criteria, demo lists, appendices, slides. Promises live in the text, not only in the dependency graph.
- Keep a short list of what the bid will not promise, each with its reason (as the proposal-architect skill does).

## Concessions and closing a price gap

A concession by the supplier (free work, a lower rate, a removed onsite cost, an allocation cut below the agreed formula) is a decision for the person who sets the price (the PM, or the internal review board when the amount exceeds the PM's tolerance). Put it to them as a separate line with its amount; never build it into the estimate as if it were scope.

When a feature does not fit the price, trade scope for scope of similar size. If nothing in scope can go, take the gap to the person who sets the price, with its size, and with what each way of closing it would take.

When the person who sets the price chooses differently from your recommendation: recommend once, state the cost of their choice once, then implement their choice (as the proposal-architect skill does).

## Cutting to reach a price

When a total is reduced to meet a price, show the price-driven part as its own line on the bridge from the previous total, as an accepted margin or risk, and keep the re-derived estimate beside it. Do not fold it into productivity factors. The solution-architect rules against tuning an assumption until the estimate fits apply here too ([estimation and costing](../../solution-architect/references/estimation-and-costing.md)). (derived: LSP 2026-10-12 — the estimate fell 45% after the internal review board called the price too high; about 90% of the cut was attributed to AI-assisted coding, with AI applied twice.)

## Recovering a loss through change requests

A change request is legitimate when it prices a real change of scope that the client asks for and approves, on the change's own merits. The routes to fund an extra-cost change are a change budget agreed with the client, a larger budget from the client, or removing other scope. Tolerance does not fund changes. [book:prince2-managing-successful-projects], 11.4. Technique: recommended issue and change control procedure

On a fixed price, a cost overrun lands on our business case, not the client's. Recovering it by loading price onto an unrelated change request is overcharging the client; do not prepare that option. [book:prince2-managing-successful-projects], 10.3. Guidance for effective risk management

Where the contract allows it, a new requirement can be traded for lower-priority work of similar size instead of priced. [book:prince2-agile], 28.3: Guidance on how to structure an agile contract
