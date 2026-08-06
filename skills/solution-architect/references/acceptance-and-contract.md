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

## Tier criteria by what the instrument can carry

A criterion is only as good as the thing that will measure it. Before writing a number, ask what will produce
it and how big the sample actually is — then place it in one of three tiers, and say on the artifact which
tier it is in.

| Tier | Holds | Test for membership |
|---|---|---|
| **Commit** | Counts, coverage, determinism, and rates whose **denominator you construct** | Could two people compute this to the same value from the same run, with no sampling argument available? |
| **Report** | Every rate measured against a sample you did not construct | State it *with* its sample size and the honest uncertainty, and do not commit |
| **Method** | The measurement contract itself — the definitions, the inputs, the adjudication route | Makes every other number computable. It is a criterion, not preamble |

**Prefer a count to a rate.** A count has no sampling noise, can be measured across the whole population
rather than a labelled subset, and cannot be argued down with a confidence interval. Where the value
proposition can be stated as a count, that is the headline.

### Effective sample size is clusters, not observations

Observations inside one document, one interview, one site are **not independent** — they share a layout, a
respondent, a configuration. A thousand data points drawn from ten documents behave like somewhere between
fifteen and thirty independent observations, not a thousand. A single structural failure produces dozens of
correlated errors in one event.

Consequence: a ±5-point claim on a ten-document sample is not defensible, and a numerate client will say so.
Either widen the sample, or move the number to **report** and state the clustering.

### A denominator you do not control is not measurable

If a metric counts *"the share of X we catch"* and X is produced by a component you have contractually agreed
not to test or tune, the denominator is outside your control and probably small. Worse, the relationship is
perverse: **the better that component performs, the fewer instances exist, and the less provable your number
becomes.** You have tied your evidence to your client's component failing.

**The fix is to construct the denominator.** Inject instances of known class and magnitude into verified-correct
inputs and measure against those. It costs engineering time rather than client-expert time — usually the scarce
resource — and it converts an unmeasurable claim into a committable one.

Three guardrails make a self-set test credible rather than self-serving, and they are what a sceptical buyer
will look for:

- **Publish the suite before the run** and let the client add cases and veto yours.
- **Include the hard classes by name** — specifically the ones your mechanism is least likely to catch. Their
  low scores are the honest boundary of the method and should be reported, not omitted.
- **Report per class, never pooled.** Pooling is how a self-set test is gamed.

State the limitation yourself: a constructed sample measures **sensitivity per class**, not expected live
performance, because injected instances are not distributed like real ones. Both numbers answer real
questions; conflating them is what gets caught.

### Check the set for gameability before you sign it

Every committed criterion should be read as an adversary would: *what is the cheapest way to satisfy this
while delivering nothing?* Criteria that are individually sound are routinely gameable in combination.

The recurring shape is a **workload or volume commitment with no quality floor beside it** — "no more than N
items reach a human" is won outright by a system that surfaces nothing. Where two criteria are only
meaningful together, **bond them on the artifact itself**: say on the card that one is valid only against the
other. An internal understanding does not survive the artifact being read alone, which is exactly when it
will be read.

### When the deal shape changes, replace the criteria — do not renumber them

Criteria authored for one commercial shape cannot be salvaged by editing their numbers; the **shape is the
defect**. A set written as fixed-price acceptance gates carries assumptions — that a miss has a payment
consequence, that thresholds precede evidence, that "done" is binary — which survive any amount of
rewording.

Observed failure mode: a set was correctly recorded as mis-aimed, then "fixed" by retiring three criteria and
restating one with new percentages. **That repeated the original error at smaller scale**, and two independent
reviews caught it within hours. Replace the set, continue the ID namespace rather than reusing numbers, and
banner the retired set at its source so the old IDs cannot be cited by accident.

Watch for what the restatement quietly drops. In the same case the rewrite deleted the only criterion
bounding the reviewer's workload — the number that *was* the value proposition — and nothing caught it,
because consistency gates check that claims agree, not that the important one is still present.
