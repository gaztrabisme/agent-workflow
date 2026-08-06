# Design Cell

Parallel authorship. N functional roles each design their slice from one shared ground truth, reconcile against each other on **interface contracts**, and converge into a single coherent spec that the build runs from.

This is the third fan-out mode, and the only one that *produces* rather than investigates:

| Mode | Agents find | Converge to |
|---|---|---|
| `task-force-protocol.md` | facts | verified synthesis |
| **design cell** | **decisions** | **one coherent spec** |
| `persona-fanout.md` | reactions | objection register |

## When it fires

A solution has to be designed across disciplines before anything is built — architecture, delivery shape, backend, frontend all bearing on each other. Not for a single-file feature; not when one person could hold the whole design in their head. The test: **would two competent people design incompatible halves of this?** No → don't run a cell.

## The failure it is engineered against

N agents given one context and told to "design your part, then review each other" reliably produce mush, for three reasons:

1. **Agents rubber-stamp.** Asked "any thoughts?", a reviewer with no stake says the work looks reasonable.
2. **Roles overlap.** The architect and the backend both spec the data model, differently, and nobody owns the conflict.
3. **The merge staples.** Four documents concatenated, no reconciliation, and the reader inherits the job.

Every rule below exists to make disagreement **mechanical rather than conversational**.

---

## Step 0 — Ground the user narratives *before* casting anyone

The user is not a producer and not a persona. Their document is a **derivation over real testimony** — closer to a research stream than a role-play. So it comes first, and if there is real data it is read, not imagined.

**Grounding tiers — declare which one each narrative sits on:**

| Tier | Meaning | Treatment |
|---|---|---|
| **Testimony** | transcripts, recorded answers, logged behaviour | Derive and **quote**. Name the corpus and its bias. |
| **Second-hand** | someone who talks to them relayed it | Derive, mark the single source. |
| **None** | nobody has asked this person anything | **Say so. Do not invent one.** It becomes an open ask, not a document. |

A fabricated portrait is worse than a missing one: it is confident, plausible, and the whole cell designs to it. Per `../../core/references/grounding-gate.md` — a claim you can't ground, you don't make.

**Cast the users who genuinely conflict, not one composite.** A workflow usually has a buyer, a doer, and someone downstream who inherits the result; their ideal outcomes are incompatible, and **that conflict is the product decision**. Averaging them into one "intended user" produces a Tuesday nobody actually wants. (Microsoft's own discovery methodology carries the same rule as an anti-pattern — map submitter / reviewer / approver / finance, or the human-in-the-loop design is broken.)

### The narrative brief — two sections, no feature list

```
You are <user>, grounded in <corpus>. Read it before writing anything.
Do NOT propose features, screens, or solutions. If you catch yourself
describing a tool, stop and describe the outcome instead.

1. TODAY — the reality baseline
   What I actually do, step by step, with real numbers.
   What it costs me now — time, money, failures I absorb.
   What I've already tried and why I stopped.
   What I would never do, no matter how good the tool is.
   Quote the source for every claim. Tier each line: OBSERVED (in the
   corpus) / INFERRED (reasoned from it) / ASSUMED (neither — flag it).

2. TUESDAY MORNING — the day-in-the-life once it works
   Narrative, not features. A normal Tuesday, the thing exists.
   What do I open, what do I see, what do I do next, and what stopped
   being my problem? Where would I still not trust it?
   What would make me abandon it in week one?

Close with: CHANGE RESISTANCE — low / medium / high, and what would
lower it. NEGATIVE SPACE — what this corpus cannot tell you about me.
```

The two sections do different jobs: **TODAY** is the part only they know and is grounded by construction. **TUESDAY** produces requirements without prescribing solutions — an outcome narrative constrains the design without pre-committing it. The no-feature-list rule is what separates this from a wish list; users asked to imagine a product describe a slightly better version of what they already have.

---

## Step 1 — Cast producers by **decision**, not by topic

Overlap is the enemy. Each mandate names decisions it owns *exclusively*, and decisions it must not make.

| Role | Owns exclusively | Never decides |
|---|---|---|
| **Solution architect** | system decomposition, tech selection, integration boundaries, NFRs | effort, sequencing, UI |
| **Delivery manager** | phasing, effort, release split, cut order, acceptance criteria | architecture, data model |
| **Backend** | data model, API contracts, state machine, persistence, failure semantics | UI, phasing, stack selection |
| **Frontend** | interaction, screens, client state, error surfaces, empty states | data model, tech stack |

Acceptance criteria and effort sit with delivery deliberately — *whoever will be held to an estimate owns authoring it* (`delivery/SKILL.md`, the pre-signature exception). Adjust the cast to the work; keep the exclusivity.

## Step 2 — The producer brief

Each producer gets the ground truth (`AGENTS.md` + `wiki/` — the existing source of record, not a parallel brief that drifts), the user narratives, its mandate, and this closing contract:

```
Design your slice. Decide only what your mandate owns; where you need
someone else's decision, record it as a NEED — do not decide it for them.

Close your document with exactly this block:

DECISIONS I OWN   <what you decided, one line each>
I PROVIDE         <what other roles may rely on — be specific enough to build against>
I NEED            <from which role, exactly what>
I ASSUME          <about someone else's domain — anything you took for granted>
OPEN              <what you could not decide, and what would settle it>
```

The contract is what makes reconciliation findable instead of felt.

## Step 3 — Cross-review, on contracts only, one round

Each producer reads the others' contract blocks — **not their prose** — and reviews **from its own mandate's interest**: *does this let me hit what I'm accountable for?* Not "is this good." A reviewer with a stake does not rubber-stamp.

One round. Iterating agents to consensus buys agreement, not correctness.

**The user narratives stay out of this round.** They are the target, not a party to the negotiation — putting them in invites the cell to talk them out of their own reality.

## Step 4 — Reconcile (a fresh agent, never a producer)

Producers defend their own work. The reconciler gets all documents, all contract blocks, and the narratives — and runs five mechanical checks:

1. **Unmet NEED** — someone needs X; nobody provides it.
2. **Contradicted ASSUME** — A assumed X about B's domain; B decided not-X.
3. **Contested decision** — two roles claim the same decision, differently.
4. **Orphan PROVIDE** — nobody needs it. Speculative work; cut it or justify it.
5. **Narrative miss** — a TUESDAY requirement no producer's contract serves.

Then it writes **the single coherent spec** — one document, one voice, contradictions resolved or escalated. Not a merge of four documents; the document the intent asked for.

## Step 5 — Unresolved contradictions become forks, not another round

Anything the reconciler could not settle goes to the Plan Block's `DECIDE NOW` for the next run — a real fork with options and consequences, surfaced to the human. Never a second cross-review round, never a silent pick.

## Step 6 — The users react to the coherent spec

Now `persona-fanout.md` fires, and it is sharper than a generic review because each user scores the spec **against their own TUESDAY**. *"This does not produce my Tuesday"* is a far harder finding than an unanchored objection. The two appearances are a loop: author the target, then judge against it.

## Step 7 — Hand to build

The coherent spec + the objection register become the build input: `dev`/Design's spec, or acceptance-criteria rows that turn into tickets on a harness board. One ID spine from here on — never a second numbering system.

---

## Anti-patterns

- **Casting by topic** ("someone do security") — guarantees overlap and orphaned decisions.
- **Cross-review as "any thoughts?"** — rubber-stamping. Review from a stake, against contracts.
- **A producer reconciling** — they defend their own slice.
- **Iterating to consensus** — agreement is not correctness.
- **Inventing a user narrative** when testimony exists, or inventing one when it doesn't.
- **Narratives inside the cross-review round** — the target must not be negotiable.
- **Stapling four documents** and calling it the spec. See `convergence.md`.
