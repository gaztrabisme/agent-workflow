# Artifact integrity — the engagement is a graph, not a folder

By mid-engagement you have a proposal, a cost model, an acceptance annex, a clarification workbook, a WBS,
and a couple of translations. Every one of them restates the same underlying facts. **When they disagree,
nobody wrote a bad sentence — the same fact simply has four values in four files.**

This is a different failure from the one the Final QA pass catches. Final QA is *within-document*: labels
matching content, totals recomputed, numbering walked (`rfi-rfp-response.md`). This page is
*across-artifact*: the same population counted twice, an ID referenced after deletion, a translation two
revisions behind. Run both — neither finds the other's defects.

The checks below are **mechanical**. They need no judgment, they can be scripted, and they are the cheapest
credibility insurance in the engagement.

---

## Rule 0 — Declare one ID spine

Pick it in Phase 0 and never have two:

- **Enterprise bid** → the client's **requirement refs**. Their document numbers everything; inherit it.
- **Fixed-price delivery** → **acceptance-criteria IDs** you author (`TC-<phase>.<function>.<n>` or similar).

Everything else is a *view* over the spine: clarification questions cite spine IDs, prerequisites serve
spine IDs, WBS packages deliver spine IDs, the cost model prices the functions the spine groups into.
A view that can't cite the spine is either mis-scoped or orphaned — both worth knowing.

Write the spine's **current version** into every artifact that keys to it ("built against acceptance annex
v0.3"). Most of the failures below are really version-skew wearing a costume.

---

## The checks

### C1 — Count reconciliation
The same population counted in N artifacts must produce N equal numbers.

> *Observed:* an engagement's acceptance-criteria count read **52** in the project wiki, **51** in the
> checklist spreadsheet (and in that sheet's own title), **49** in the current governing annex, and **48**
> in the translated annex. Four numbers, one population, all live. The count gates payment.

Count from the artifact, never by incrementing a remembered figure.

### C2 — Dangling references
Every spine ID referenced anywhere must exist in the current spine version.

> *Observed:* two clarification questions still cited criteria that had been deleted a revision earlier.
> The client would have been asked to answer questions about tests that no longer existed.

### C3 — Orphans
Every spine ID should be covered by the views that claim coverage — or explicitly waived with a reason.

> *Observed:* ten acceptance criteria had no clarification question behind them, meaning ten tests whose
> preconditions nobody had asked the client to provide.

Orphans are not always defects — some criteria genuinely need nothing. But an *unexamined* orphan is a
test that fails on acceptance day for a reason you could have surfaced months earlier.

### C3a — The inverse orphan: a link is not a warrant

C3 asks whether every spine ID is covered. The inverse is the dangerous one, because it **passes**: a
client-facing claim cites a spine ID that exists — and that does not deliver the claimed capability.

**Traceability proves a link exists. It does not prove the target satisfies the source.** A gate written as
*"every claim must name a real task"* is satisfied by any real task, including the adjacent one.

> *Observed.* A slide claimed four reviewer actions, badged in-scope. The traceability map behind it carried
> a note — *"approve and correct are built; comment and escalate are not separately scoped"* — while the
> mockup beside it drew a button for one of them. It passed **five automated gates and three cold reviewers**,
> because the claim named task `4.2.3` and `4.2.3` exists. The client-facing artifact promised a capability
> the plan did not fund, and the record that knew it was sitting in the file the gate read.

**Two rules follow, and the second is the general one.**

- **Check the target's content, not just its existence.** For each claim, the question is *"does what this
  task delivers cover what this sentence promises?"* — a comparison no ID-set operation can perform. It needs
  either a capability field on the task that the gate can read, or a human pass over the claim/target pairs.
- **A field that records a gap is not a control unless something reads it.** The note above was *correct*.
  It had been written deliberately, by someone who understood the gap. It changed nothing, because no gate
  consumed that field — so it functioned as documentation while reading, to every later reviewer, as
  governance. **If your traceability map carries caveat or exception fields, either the gate consumes them or
  they should be deleted**, since their presence suppresses the very suspicion that would catch the defect.

This is the same family as *"a ✓ you typed is a proxy, not a gate"* below, and as the sibling failure in this
skill's Evolution 7: consistency gates check that claims agree, not that the load-bearing one survived. **A
gate can run, pass, and have checked the wrong property.** When a gate has never failed on a class of defect,
ask what property it actually asserts before concluding the class does not occur.

### C4 — Version lineage
One artifact per class is current; the rest are history. Check that **filename, internal version cell, and
content actually agree**.

> *Observed:* a workbook named `..._v1.0.xlsx` whose version cell read `v3.0` and whose row counts matched
> a different file entirely. Anyone picking files by name would have edited the wrong one.

Retire superseded copies to an `archive/` folder rather than leaving them adjacent to the live one.

### C5 — Language parity, and the governing text
On a bilingual engagement, **declare which language governs** — usually the contract's legal language —
and treat every other language as *a translation with a lag*. State the lag.

> *Observed:* the governing-language acceptance annex was at v0.3 with **7** functions; the translated
> annex was at v0.1 with **8** — it still committed to a function the governing text had deleted, complete
> with six acceptance criteria. Separately, the translated clarification workbook was one revision behind,
> so two questions and one client obligation existed only in the governing language and would never have
> been asked.

**Scope divergence between language versions is the highest-severity finding on this page.** A translation
that promises more than the governing text is a commitment someone can hold you to, and a translation that
promises less is a question you never asked. Diff the *structure* (function lists, ID sets, counts) across
languages, not just the prose.

### C6 — Priced ↔ committed
The cost model and the commitment artifact must agree on what is being delivered.

> *Observed:* the cost model still carried a line item — effort and money — for a function the governing
> acceptance annex had dropped. Either the price was overstated or the scope was under-committed; both are
> discoverable in the room.

Run it both directions: **priced-but-not-committed** (you're charging for something you haven't promised)
and **committed-but-not-priced** (you've promised something you're not being paid for). The second is worse.

### C7 — One carrier per class, with a named owner
Each artifact class — WBS, cost model, clarification sheet, acceptance criteria — has exactly **one** live
file and **one** named owner. Parallel authorship without this produces silent forks.

> *Observed:* four parallel WBS lineages across three authors, and two files with the *same name* in
> different folders whose contents had diverged. Not a duplicate — a fork, invisible to anyone reading by
> filename.

Byte-identical duplicates are the mild version (retire one). Same-name divergent files are the dangerous
version: every reader believes they read the current one.

### C8 — One namespace per concept
Before choosing an ID prefix, check it against **every other register in the engagement**. Renaming a
register to suit a stakeholder is exactly when collisions get created.

> *Observed:* a PM asked for the obligations register to be re-framed as "dependencies", so `O-01…O-06`
> became `D-01…D-12` — colliding with decision records `D-001…D-013` already in the wiki. One page then
> read "D-10 · Funding approval" three lines from "D-009/D-010" meaning decisions.

A prefix is part of the spine. Accommodating a stakeholder's vocabulary is right; minting a second meaning
for a live prefix is not. Rename the *label*, keep the prefix unique.

**Fixing this pays for itself immediately.** On the same engagement the collision was resolved by moving the
dependency register to `O-` (client) and `F-` (internal) — and that is what made the next decision ID
mintable at all, because the project instructions had frozen `D-` while it was ambiguous. A colliding prefix
does not just confuse readers; it blocks the register that owns it.

**Preserve the numbers when a register shrinks.** Dropping rows and renumbering breaks every cross-reference
already written elsewhere. Leave the gaps — `O-01, O-02, O-05` with `O-03`/`O-04` absent is honest and cheap;
resequencing is neither.

### C8a — Two registers for two audiences is correct, not a defect

C8 says one namespace per **concept**. It does not say one register per **name**. Where the same word serves
two different consumers with different decisions, splitting is the right answer and merging is the bug.

> *Observed:* an engineering task inventory needed *assumptions that change the build* — sign conventions,
> per-column execution, skip-vs-fail on absent input. The proposal carried *assumptions the client must
> correct* — the accuracy reading, zero-tolerance scope, a deadline's provenance. Both are "assumptions".
> They share almost no rows, serve different readers, and a merged register is unreadable to both.

Resolution: distinct prefixes (`EA-` engineering, `A-` proposal), and **an explicit note in the index saying
they are deliberate and must not be reconciled** — otherwise the next integrity pass reads two registers with
overlapping names and "fixes" them. A deliberate split needs a recorded reason, or the machinery in this file
will treat it as the defect it is designed to catch.

### C9 — Attributed quotations are cross-artifact facts

A quoted sentence attributed to the client propagates faster than any number, because it is the thing people
reach for when they need the argument to land. Two properties must hold, and neither is checked by anything
else on this page:

- **Verbatim in a source of record.** The exact characters, in that order, in the transcript or thread —
  not a faithful summary of them. `core`'s grounding gate owns *whose sentence is this*; this check owns
  *does the string exist*.
- **Byte-identical everywhere it appears.** One quotation drifting across a proposal, a deck and a wiki page
  is the same failure as one population counted four ways (**C1**) — and it is harder to spot, because each
  version reads fine alone.

> *Observed.* A quotation attributed to a named client partner and tagged `(Confirmed)`, in the orientation
> document every new contributor is told to read first, turned out to be a colleague's summary from an
> internal chat. One copy-paste from a client slide. The same engagement had already purged an invented
> accuracy figure from four documents, and a guard sentence recorded in three files was a composite that
> appeared on no page of the artifact it was guarding.

**Do it cheaply and it becomes a gate:** extract every quoted string above a length threshold, filter to those
attributed to a **named external speaker**, and search the source of record for each. The filter is what makes
it usable — unscoped, the same check returns hundreds of correct-but-irrelevant matches and gets ignored. See
`core/references/grounding-gate.md` → *Scope the check until its output is all signal*.

⚠ **A quotation you cannot locate is not necessarily false — but it is not quotable.** Drop the quotation
marks and state the substance in your own voice, which is almost always sufficient and costs nothing.

---

## The check must execute, not narrate

**A ✓ you typed is a proxy, not a gate.** A reconciliation written as prose is true at the moment of typing
and goes stale silently — and it goes stale in the one place a reader trusts most.

> *Observed:* an estimate's reconciliation section asserted `WBS total vs feature-build line | 58 = 58 ✓`
> while the WBS total row three sections above read **59**. The same engagement carried three live values
> for total effort (106 / 120 / 121) across four artifacts, and its project instructions stated
> *"numeric reconciliation has been run."* Every check on this page was present. None had executed.

So:

- **Totals and counts live in formulas**, computed from the detail rows, not typed onto a summary. A typed
  total is a claim; a formula is a check that cannot disagree with its own source.
- **Cross-artifact checks live in a script** that re-reads the artifacts and re-derives the numbers. Twenty
  lines, run every round.
- **Never record a check as passed in prose.** Record *how it was run* and let the artifact carry the result.
- **Ground the defect statement too, not just the artifact.** A defect *description* propagates like any other
  claim, and nobody re-checks it because it looks like a finding rather than an assertion.

> *Observed, on the same estimate.* The three-live-totals defect above was recorded everywhere as
> *"106 / 120 / 121"* — and `106` **appeared nowhere in any artifact.** It was wrong when first written, and
> the string was then copied verbatim into four files as the canonical description of the problem. The real
> defect was two totals, `120` and `121`, and it was **definitional rather than arithmetic**: one counted
> nominal capacity, the other counted requirement. Nobody could have resolved it from the description, because
> the description was fiction. A phantom number was propagating faster than the real ones.

The rule: when you write down a defect, run the same search you would run on a client claim. *"Three totals:
106/120/121"* is a grep away from being verified or falsified, and one of those numbers did not survive it.

If a workbook must ship with cached values for readers who lack a formula engine, keep the formulas and
open-and-resave to populate the cache — do not replace formulas with literals. Literal-only workbooks lose
the self-checking property, which is the whole reason the numbers were trustworthy.

---

## When to run

- **Before any artifact goes to the client** — alongside, not instead of, the Final QA pass.
- **After every answer-folding round** — folding client answers is exactly when views drift apart.
- **At the shape boundary** — when an enterprise bid converts to a delivery contract and requirement refs
  become acceptance criteria. This migration is the most defect-prone moment in an engagement.
- **Before signature.** Anything wrong here becomes contractual.

## Doing it cheaply

Extract the ID sets and compare them; don't read for it. Pull every spine ID from each artifact, then take
set differences: `referenced − existing` gives C2, `existing − covered` gives C3, and comparing counts
gives C1. Spreadsheets and documents both yield to a short script, and structure-diffing two language
versions is the same operation run twice. A check you have to *remember* to do carefully is a check that
eventually doesn't happen; a check that's twenty lines of script gets run every round.

## Report findings as questions, not corrections

An integrity finding on a client-shared artifact is often a *clarification*, not a unilateral fix — the
divergence may encode a real decision someone made and didn't propagate. Establish which version is
intended before rewriting the others, and log the reconciliation like any other change.
