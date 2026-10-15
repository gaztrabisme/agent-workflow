# Design Cell

Parallel authorship. N functional roles each design their slice from one shared ground truth, reconcile against each other on **interface contracts**, and converge into a single coherent spec that the build runs from.

This is the third fan-out mode, and the only one that *produces* rather than investigates:

| Mode | Agents find | Converge to |
|---|---|---|
| `task-force-protocol.md` | facts | verified synthesis |
| **design cell** | **decisions** | **one coherent spec** |
| `persona-fanout.md` | reactions | objection register |

## When it fires

Use a design cell when different roles build separate parts that must integrate. Have those teams interact and align their subsystem work regularly; do not limit joint design to the moment two disciplines happen to foresee incompatible halves. [book:pmbok-guide-7e], 3.5. Recognize, Evaluate, and Respond to System Interactions.

## The failure it is engineered against

N agents given one context and told to "design your part, then review each other" reliably produce mush, for three reasons:

1. **Agents rubber-stamp.** Asked "any thoughts?", a reviewer with no stake says the work looks reasonable.
2. **Roles overlap.** The architect and the backend both spec the data model, differently, and nobody owns the conflict.
3. **The merge staples.** Four documents concatenated, no reconciliation, and the reader inherits the job.

Every rule below exists to make disagreement **mechanical rather than conversational**.

---

## Step 0 — Ground the user narratives *before* casting anyone

The user is not a producer and not a persona. Their document is a **derivation over real testimony** — closer to a research stream than a role-play. So it comes first, and if there is real data it is read, not imagined.

**Grounding the narrative — say who was asked and what record supports it. These source descriptions apply to the narrative as a whole, not as labels on every claim:**

| Tier | Meaning | Treatment |
|---|---|---|
| **Testimony** | transcripts, recorded answers, logged behaviour | Derive and **quote**. Name the corpus and its bias. |
| **Second-hand** | someone who talks to them relayed it | Derive, mark the single source. |
| **None** | nobody has asked this person anything | **Say so. Do not invent one.** It becomes an open ask, not a document. |

A fabricated portrait is worse than a missing one: it is confident, plausible, and the whole cell designs to it. In TODAY, describe only behavior supported by testimony or direct observation; put unsupported questions in OPEN instead of tagging each sentence OBSERVED, INFERRED, or ASSUMED. Per `../../../core/references/grounding-gate.md`, a claim you cannot ground is not made. [book:research-methods-psychology], How Scientists Work.

**Cast users with genuinely different needs separately, not as one composite.** People can describe the same situation through different mental models; averaging them can hide the problem the design must resolve. [book:learning-systems-thinking], Point of view blindness.

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
   Quote the source for each claim. Keep each statement within what the
   testimony or direct observation supports; place unknowns in OPEN.

2. TUESDAY MORNING — the day-in-the-life once it works
   Narrative, not features. A normal Tuesday, the thing exists.
   What do I open, what do I see, what do I do next, and what stopped
   being my problem? Where would I still not trust it?
   What would make me abandon it in week one?

Close with: CHANGE RESISTANCE — low / medium / high, and what would
lower it. NEGATIVE SPACE — what this corpus cannot tell you about me.
```

The two sections do different jobs: **TODAY** records what people actually do; include observed steps, current costs, attempts that stopped, and actions they would never take. **TUESDAY** describes outcomes without prescribing solutions. The no-feature-list rule keeps the brief focused on the problem and its value before solutionizing. [book:swebok], 3.2. Elicitation Techniques; [book:learning-systems-thinking], The Bridges.

---

## Step 1 — Cast producers by **decision**, not by topic

Overlap is the enemy. Name one accountable owner for each decision; each mandate names decisions it owns exclusively and decisions it must not make. [book:facilitating-software-architecture], Make Who Is Accountable for Each Decision Explicit; [book:facilitating-software-architecture], Dangers of seeking advice only via established, hierarchical relationships.

| Role | Owns exclusively | Never decides |
|---|---|---|
| **Solution architect** | system decomposition, technology selection, and module/integration boundaries; this cell also holds NFRs [book:facilitating-software-architecture], Architectural decisions. | effort, sequencing, UI |
| **Delivery manager** | phasing, effort, release split, cut order, acceptance criteria | architecture, data model |
| **Backend** | data model, API contracts, state machine, persistence, failure semantics | UI, phasing, stack selection |
| **Frontend** | interaction, screens, client state, error surfaces, empty states | data model, tech stack |

Acceptance criteria and effort sit with delivery deliberately — *whoever will be held to an estimate owns authoring it* (`delivery/SKILL.md`, the pre-signature exception). Adjust the cast to the work; keep the exclusivity.

## Step 2 — The producer brief

Each producer gets the ground truth (`AGENTS.md` + `wiki/` — the existing source of record, not a parallel brief that drifts), the user narratives, its mandate, and this closing contract: [book:software-engineering-at-google], Documentation Is Like Code.

```
Design your slice. Decide only what your mandate owns; where you need
someone else's decision, record it as a NEED — do not decide it for them.
Name the accountable author for your decisions.

Close your document with exactly this block:

DECISIONS I OWN   <what you decided, one line each>
I PROVIDE         <what other roles may rely on — be specific enough to build against>
I NEED            <from which role, exactly what>
I ASSUME          <about someone else's domain — anything you took for granted>
OPEN              <what you could not decide, and what would settle it>
```

The contract is what makes reconciliation findable instead of felt; its author is accountable for those decisions and is the point of contact. [book:facilitating-software-architecture], The Structure of an ADR.

## Step 3 — Cross-review, on contracts only, one round

Each producer reads the others' contract blocks — **not their prose** — and reviews **from its own mandate's interest**: *does this let me hit what I'm accountable for?* Not "is this good." A reviewer with a stake does not rubber-stamp.

One round. Keep the decision with its owner and seek advice without iterating toward broad consensus. [book:facilitating-software-architecture], The Architecture Advice Process Is Fast.

**The user narratives stay out of this round.** They are the target, not a party to the negotiation — putting them in invites the cell to talk them out of their own reality.

## Step 4 — Reconcile (a fresh agent, never a producer)

Producers defend their own work. The reconciler gets all documents, all contract blocks, and the narratives — and runs five mechanical checks. Use a fresh reconciler outside the producer group. [book:swebok], 5.1. Practical Considerations.

1. **Unmet NEED** — someone needs X; nobody provides it.
2. **Contradicted ASSUME** — A assumed X about B's domain; B decided not-X.
3. **Contested decision** — two roles claim the same decision, differently.
4. **Orphan PROVIDE** — nobody needs it. Speculative work; cut it or justify it.
5. **Narrative miss** — a TUESDAY requirement no producer's contract serves.

Then it writes **the single coherent spec** — one document, one voice, contradictions resolved or escalated. Independent, uncoordinated ideas do not gain conceptual integrity by being concatenated. Not a merge of four documents; the document the intent asked for. [book:learning-systems-thinking], Chapter 2. Crafting Conceptual Integrity.

## Step 5 — Unresolved contradictions become forks, not another round

Anything the reconciler could not settle goes to the Plan Block's `DECIDE NOW` for the next run — a real fork with options and consequences, including why the alternatives lost. Never a second cross-review round, never a silent pick. [book:facilitating-software-architecture], Consequences.

## Step 6 — The users react to the coherent spec

Now `persona-fanout.md` fires, and it is sharper than a generic review because each user scores the spec **against their own TUESDAY**. Ask impacted people for feedback before seeking their agreement; *"This does not produce my Tuesday"* is a stronger finding than an unanchored objection. The two appearances are a loop: author the target, then judge against it. [book:learning-systems-thinking], Get Feedback from People You Need.

## Step 7 — Hand to build

The coherent spec and objection register become the build input: one uniquely identifiable requirement spine, traceable to the work that satisfies each requirement. Do not create a second numbering system. [book:swebok], 7.4. Requirements Tracing.

---

## Anti-patterns

- **Casting by topic** ("someone do security") — guarantees overlap and orphaned decisions.
- **Cross-review as "any thoughts?"** — rubber-stamping. Review from a stake, against contracts.
- **A producer reconciling** — they defend their own slice.
- **Iterating to consensus** — agreement is not correctness.
- **Inventing a user narrative** when testimony exists, or inventing one when it doesn't.
- **Narratives inside the cross-review round** — the target must not be negotiable.
- **Stapling four documents** and calling it the spec. See `convergence.md`.
