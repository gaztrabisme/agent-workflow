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
