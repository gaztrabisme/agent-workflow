# Acceptance & contract — where the architecture meets the money

> **Applies to: the fixed-price delivery shape**, and to any enterprise bid you *win* — the moment a
> proposal converts to a contract, this becomes the live phase. See `deal-shapes.md`.

Presale does not end when the proposal lands. On a fixed-price engagement the proposal is the *opening*
position; the artifact that actually binds both parties is the **acceptance annex** — the schedule of
criteria that gate payment. It is written by the solution architect, negotiated line by line, and lived
with for the whole delivery.

Get it wrong in one of two directions and the deal bleeds: criteria too vague and acceptance becomes an
opinion; criteria too tight, or dependent on client inputs nobody committed to, and you own a schedule you
can't control.

---

## 1. Acceptance criteria as the spine

Each criterion gets an ID and becomes the thing everything else keys to (`artifact-integrity.md`).

**Anatomy of a good criterion:**

| Field | Purpose |
|-------|---------|
| **ID** | `TC-<phase>.<function>.<n>` — the spine |
| **Function** | Which delivered capability it proves |
| **Criterion summary** | What must be observably true. One sentence, witnessable. |
| **Preconditions to run the test** | What must physically exist before the test is even executable |
| **Preparing party** | **Us / Client / Both** — who provides the preconditions |
| **Linked clarification question** | The open question whose answer settles this criterion's shape |
| **Ready date** | When the preconditions will be in place |
| **Status** | Not prepared / Prepared / Passed / Failed |

The two columns that do the real work are **preconditions** and **preparing party**. "The assistant answers
only within the user's permissions" is untestable on acceptance day without two accounts in two permission
groups and a document only one of them may see. Naming that precondition — and naming *who* provides it —
converts a promise into a dated dependency. Most fixed-price schedule slips are precondition slips wearing
a technical costume.

**Write criteria in the observable, not the mechanism.** "Every alert carries an evidence image
identifying the event" survives a change of detector. "The YOLO model returns a bounding box" doesn't, and
ties acceptance to an implementation you may want to change.

## 2. The client-obligation register

Distinct from the assumptions register, and frequently confused with it:

- **Assumptions register** — what *we believe* while proceeding without an answer (`templates/assumptions-register.md`).
- **Obligation register** — what the *client must physically deliver*, by when, or the schedule slips.

An assumption that turns out wrong costs you a rework. An unmet obligation costs you the calendar, and
without this register it will be remembered as your delay.

Columns: `# · group · item the client provides · serves criterion · linked question · proposed deadline ·
client focal point · completion date · status`.

Two disciplines make it work:

- **Schedule-relative deadlines**, not absolute dates: "on contract signature", "week 1 of phase 1",
  "before the phase-2 milestone". The register survives a start-date slip without being rewritten, and it
  makes the dependency chain legible.
- **A named client focal point per row.** A deadline with no name is a wish. This is also why the first
  obligation on the list is usually *"nominate a single authorized focal point."*

Group the rows — contract terms · infrastructure · phase 1 · phase 2 · phase 3 — so the client can see
what they owe *now* versus later.

## 3. Commercial risk transfer — the obligations that are really contract terms

The most valuable rows in the register aren't logistics. They are the terms that must land in the contract
*before* signature, because after signature they cost money to fix:

- **A single authorized focal point** with decision authority — and what happens when they're unavailable.
- **Defect-severity definitions** (typically four levels), agreed in writing. Without these, "critical bug"
  is whatever the unhappy party says it is.
- **The client's acceptance-response deadline** — how long they have to accept or reject a submission
  before it is deemed accepted. Open-ended review is an unfunded liability.
- **T0** — what event starts the clock, precisely. Contract signature? Deposit received? Access granted?
  Every schedule commitment is meaningless without it.
- **Volume caps stated numerically** — documents, users, transactions, hours of footage. "Reasonable
  volume" is not a scope boundary.
- **A day rate for change requests**, agreed up front. Negotiating a rate while the client wants something
  is negotiating from the weak side.
- **A standby rate when the client causes delay** — what you charge when your team is held idle waiting on
  an unmet obligation. This is the clause that converts their schedule risk from your problem into a
  priced one, and it is the single most-omitted term.
- **Acceptance-council membership** — who signs, and whether one dissenting voice can block.
- **Warranty and support boundaries** — duration, what counts as a defect versus an enhancement.

**Frame these as protecting both parties**, because they do: the client gets predictability and a defined
escalation path, you get a bounded downside. A vendor who raises them reads as experienced, not defensive.

## 4. The loop between criteria and terms

These two artifacts generate each other, and the loop runs several times:

```
acceptance criteria → preconditions → client obligations → contract terms
        ↑                                                        │
        └──────── terms constrain what you can commit to ────────┘
```

Writing a criterion surfaces a precondition; the precondition needs an owner and a date, which makes it an
obligation; obligations that carry commercial consequence become contract clauses; and the clauses you
*can't* get agreed force you to soften or re-scope the criterion. Run the loop until it converges before
signature — every unclosed cycle is an argument scheduled for delivery.

## 5. Contract anatomy — what the annex sits inside

You will not draft the contract, but you own the schedules attached to it and must recognise where your
architecture creates obligations. A typical service contract carries: definitions · both parties' rights and
obligations · value and payment · implementation time · **acceptance and handover** · warranty and support ·
IP ownership · confidentiality · personal-data protection · **change requests** · force majeure · penalties
and damages · suspension and termination · limitation of liability · notices · governing law and disputes.

The architecture-bearing ones are **acceptance and handover**, **change requests**, **IP**, **personal-data
protection**, and **limitation of liability** — read those clauses against your solution. A data-protection
clause written for a document-management system will not survive an architecture that ships data to a
third-party inference API.

Appendices usually carry: scope and deliverables · **acceptance criteria** · price breakdown and adjustment ·
penalty schedule · notice templates. The acceptance appendix is yours.

## Anti-patterns

- **Criteria that restate features.** "The system has a chatbot" proves nothing and gates nothing.
- **Criteria that depend on client inputs nobody committed to** — untestable on the day, and the delay
  lands on you.
- **Silent scope drift between revisions.** Dropping a function from the annex without repricing, or
  without propagating to the translation, is the defect class in `artifact-integrity.md` C5/C6.
- **Deferring the day rate and standby terms** to "we'll sort it out later." Later is when you have no
  leverage.
- **Treating obligations as assumptions.** An assumption you can proceed on; an unmet obligation stops you.
- **Acceptance criteria written after the price is fixed.** The criteria *are* the scope; pricing before
  they exist is pricing a guess.
