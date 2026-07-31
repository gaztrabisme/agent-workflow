# Evolution Log — drawio

Section convention per `../core/references/evolution-loop.md`. A change from a single trace ships with
verdict **`PENDING`** and earns `KEEP` only after ≥2 independent real uses exercise it without new friction.

**Why this file starts at Evolution 1 rather than 0.** `references/quality-conventions.md` was already
harvest-derived — its own header says *"distilled from iterative architect-review cycles (two presale
engagements, Jul 2026)"* — but the skill carried no `EVOLUTION.md`, so those changes have no recorded
verdicts and no validation checklist. Evolution 1 opens the loop properly and back-fills verdicts on the
pre-existing conventions where this trace exercised them.

---

## Evolution 1 — 2026-07-30 — Icons that do not exist; the export that travels without you

### Harvest scope

**A competitive presale for a financial-statement verification platform** (Big-4 client, South-East Asia,
Microsoft-brokered). Two diagrams authored and taken through **three practitioner review rounds** in one
session — a solution architect (Nguyen) and a delivery PM (Tri) — plus a fourth round of feedback arriving
via a client-facing deck a colleague built from the output.

Representative because the feedback was **iterative and adversarial from two different roles**, and because
one defect escaped into a client-bound artifact, which is the only way to learn what the loop does not catch.

Traces: 7 diagram exports read as pixels; ~35 crops; 23 icons probe-rendered; one `.pptx` reverse-engineered
to recover the embedded image; four rounds of written reviewer feedback.

### Patterns found

| # | Pattern | I/E | Proof |
|---|---|---|---|
| 1 | **Brand icons are assumed to exist and silently do not.** No Microsoft Fabric, OneLake, Excel, notebook or Spark icon in *any* bundled library. `Service_Fabric` exists and is a different product — using it is a factual error to the audience that matters | H/L | Enumeration across all ten `img/lib` libraries returned zero for `fabric` except Service Fabric, zero for `onelake`, zero for `excel`, zero for `notebook`, zero for `spark` |
| 2 | **The convention said "probe first" and probing is the weaker method.** Visual probing confirms a hit; it cannot enumerate, and it **cannot produce a negative**. The library is a JSON directory inside `app.asar` and is readable in seconds | H/L | 648 azure2 SVG paths and 31 categories recovered by parsing the asar header; the four brand negatives above are only obtainable this way |
| 3 | **A stale export reached a client deck.** Source corrected `23 rules → 42`; the `.png` was not re-exported; a colleague embedded the stale image in a client-facing deck whose body text repeated the wrong count. The index flagged the PNG as stale **in prose** | H/L | Recovered `image9.png` from the `.pptx` and read it: pre-correction L2 box, pre-review lane labels, no working store, no crop component |
| 4 | **Grouping by host destroys reading order, and fixing the vocabulary does not fix it.** Reviewer: *"our design flow logic doesn't quite self-explanatory to me"* — after a full plain-language rewrite | H/L | Complaint persisted through the vocabulary pass; resolved by numbered step badges 1…11 with grouping untouched |
| 5 | **Colour was carrying two orthogonal facts on one channel.** Card fill encoded ours-vs-theirs; a request for coloured section backgrounds collapsed it — and that encoding was the client-facing scope boundary | H/L | Splitting band=platform / fill+border=ownership *increased* the ownership contrast (white card on tint reads better than grey card on white) |
| 6 | **Milestone semantics: a horizontal band in a structurally-ordered list is a lie.** Caught by the PM, not by the loop | H/L | *"chỗ title End W1 nhưng task a thấy qua mấy W2 và 3,4"* — the banner claimed completion above rows that ran three weeks further. The reference schedule *he had supplied* already showed the correct pattern (a vertical `UAT 1` band) |
| 7 | **Micro-bend from an anchor/waypoint mismatch.** A 1.5px disagreement between `entryX` and the waypoint renders as a hooked arrowhead | M/L | Invisible at page zoom, obvious in a crop; fixed by computing the fraction from geometry |
| 8 | **An edge parallel to a container border reads as one line.** The existing rule covered edge-vs-edge only; nothing in the XML suggests a problem because a border is not an edge | M/L | Dashed amber edge 12px below a dashed amber band boundary |
| 9 | **Card text overflow is the most frequent silent defect**, and it is arithmetic | M/L | Two overflows in one export; both within 15% of the usable-width limit |
| 10 | **One canvas cannot carry both hosting and a numbered sequence.** Two genres, two questions, two audiences | H/L | Architect asked for the architecture view; the WBS/build needed the L0–L8 sequence. Split into two files resolved both |
| 11 | **Icon-on-left vs icon-on-top is a tradeoff the conventions prescribed away.** Centred is robust (no width estimation) but costs ~50px of card height, which reduces on-slide scale of everything when the page is height-bound | M/L | Reviewer asked for centring; the page was height-bound against 16:9, so the cost was real and had to be paid down by cutting a box |

**Not a pattern, worth recording:** the *"specification, not explanation"* rule fired correctly and was
followed on the diagrams — and the same author then broke it in a spreadsheet an hour later. The rule is
sound; its **scope statement** was too narrow (it says "a diagram is a deliverable"). Promoted upstream:
see `solution-architect` Evolution 5 and `core` Evolution 3.

### Hypotheses applied

| # | Change | File | Pattern |
|---|---|---|---|
| 1 | **Enumerate from `app.asar`** with a working snippet; visual probe demoted to confirmation | `references/quality-conventions.md` §Icons | 2 |
| 2 | **Named brand negatives** — Fabric / OneLake / Excel / notebooks / Spark do not exist; honest stand-ins; *"a wrong logo costs more credibility than a missing one"* | same | 1 |
| 3 | **Verified-rendering path list expanded** to ~45 probe-confirmed entries incl. the correct lineage notes (`AI_Studio` = AI Foundry, `Form_Recognizers` = Document Intelligence) and `cylinder3` for a deliberately unbranded store | same | 1 |
| 4 | **New: "The export is a derived artifact, and it travels without you"** — re-export in the same edit, name the maintenance dependency, numbers inside images are ungreppable, assume someone already has your export | same | 3 |
| 5 | **New: "Reading order is a separate problem from grouping"** — numbered step badges, do not reorder | same | 4 |
| 6 | **New: "One meaning per colour channel"** — band = platform, fill+border = ownership; the legend must name the channel that carries it; grey bands need to be darker than expected | same | 5 |
| 7 | **New: "Two views, two files"** — separate files not pages; name which file owns each maintenance-dependent number | same | 10 |
| 8 | **Anchor fraction must resolve to the exact waypoint**; edge-parallel-to-border added to Edge Routing | same §Edge Routing | 7, 8 |
| 9 | **Card text-width arithmetic** added to the verification loop's defect list | same §Verification Loop | 9 |
| 10 | **Icon-on-top-centred documented as an alternative with its selector**, incl. "*not centred* is usually a dead-space complaint — try tightening first" | same §Container & Card Styling | 11 |
| 11 | Milestone semantics — a time marker must live on the time axis, not as a horizontal band | `../solution-architect/references/templates/delivery-wbs-workbook.md` *(the instrument that carries it)* | 6 |

### Validation (fill on the next diagram-bearing engagement)

- [ ] Icon set enumerated from the library **before** any icon is chosen, and at least one intended brand icon
      is found not to exist — caught before it ships rather than after.
- [ ] Every canvas figure maintained elsewhere has a **named maintenance dependency** in its index entry, and
      the export is regenerated in the same edit as the source.
- [ ] No stale export reaches a third party. *This is the real test — it is the one that failed here.*
- [ ] A host-grouped architecture diagram ships with an explicit reading order, and a reviewer does not ask
      "where do I start".
- [ ] Colour channels declared before the first fill is chosen; a legend names the channel that carries
      ownership.
- [ ] A milestone appears on the time axis, and no horizontal band implies completion it cannot deliver.
- [ ] Crop-and-read catches ≥1 text overflow or hooked arrowhead **before** a reviewer does.

**Verdict: `PENDING` — every change.** One engagement, one session, one author. Patterns 1, 2 and 3 are the
strongest candidates for early `KEEP` because they are **verifiable facts about the tool** rather than
judgements about taste: the icons either exist or they do not.

**Back-filled verdicts on the pre-existing conventions this trace exercised:**

| Pre-existing rule | Result |
|---|---|
| Verification loop — export, read pixels, crop, fix | **PASS, repeatedly.** Caught two text overflows, one hooked arrowhead, one same-colour parallel pair, one low-contrast band, all invisible in XML. Second independent engagement → **`KEEP` candidate** |
| *Specification, not explanation* | **PASS on the diagrams**, and the author broke it in an adjacent artifact within the hour. → `KEEP` for diagrams; **scope statement too narrow**, promoted upstream |
| Density & Legibility — binding-axis reasoning | **PASS.** Correctly predicted that icon-on-top would cost on-slide scale on a height-bound page, and the cost was paid by cutting a box rather than shrinking type |
| Broken paths fail silently → probe first | **REVISED, not reverted.** Probing works; it is simply the weaker half of a two-step method that must start with enumeration |

---

## Evolution 2 — 2026-07-31 — Transparency is a change, not a flag

### Harvest scope

Same presale engagement as Evolution 1, one day later. **Not an independent trace** — but it exercises the
part of Evolution 1 that was never tested: what happens when the export convention (`-t` by default) meets a
diagram that had previously shipped opaque, in front of a reviewer using a dark viewer.

Trace: two diagrams revised against an adversarial audit; one relayout (page 1780×1250 → 1980×1280, three
components added); 6 crops; three arrow defects reported by the recipient, all of which turned out to be one
cause.

### Patterns found

| # | Pattern | I/E | Proof |
|---|---|---|---|
| 1 | **A transparent export cannot be judged by reading it.** What renders is the viewer's backdrop. Reading it once, on whatever the environment supplies, produced two false conclusions in a single pass | H/L | A default-black title read as *"the title didn't render"*; it was correct on white. The loop said "read the PNG" and the PNG was ambiguous |
| 2 | **Narrow gaps between stacked containers become drawn bars.** Five swimlanes with 10-unit gaps rendered as five heavy black bars that **visually severed every edge crossing them** — three arrows reported as broken, none of which was | H/L | Gaps at 172→182, 332→342, 402→412, 580→590. Invisible on white, opaque bars on anything else |
| 3 | **The dark composite is the diagnostic, and it is the one that gets skipped.** White shows what the slide shows; dark shows the negative space the design is relying on. Only the second finds patterns 1 and 2 | H/L | Both defects were invisible on white and obvious on dark |
| 4 | **Closing a container gap has a zero-risk form and a high-risk form, and they look equally reasonable.** Growing the upper container's height touches nothing; moving the lower container's origin moves every child and invalidates every absolute waypoint below it | M/L | Four lane heights grown, four gaps closed, zero waypoints recomputed, zero children moved — verified by asserting contiguity from the saved file |
| 5 | **Switching an existing diagram opaque → transparent surfaces every concealed defect at once, in the recipient's viewer rather than the author's** | M/L | The diagram had shipped opaque for a week with both defects latent |

### Hypotheses applied

| # | Change | File | Pattern |
|---|---|---|---|
| 1 | **New: "A transparent export must be read on TWO backgrounds"** — the composite snippet, what each pass is for, and the two defects only the dark pass finds | `references/quality-conventions.md` §Verification Loop | 1, 3 |
| 2 | **New: "Narrow gaps between stacked containers become bars"** — contiguity for stacked lanes, ≥40 units for deliberate corridors, and the grow-height-never-move-origin rule with an assertable check | same | 2, 4 |
| 3 | **Transparency section extended** — *"transparency moves work into the diagram, it does not remove it"*; first transparent export of a previously-opaque diagram re-runs the full loop | same §Transparent Backgrounds | 5 |

### Validation (fill on the next diagram-bearing engagement)

- [ ] Every `-t` export is composited on white **and** dark before being called verified.
- [ ] The dark pass catches ≥1 defect the white pass does not.
- [ ] No stacked-lane diagram ships with a gap under 40 units.
- [ ] A container gap is closed by growing a height, and no waypoint needs recomputing as a result.
- [ ] A diagram converted opaque → transparent gets a full loop, not a flag change.

**Verdict: `PENDING` — all three.** Same engagement and same author as Evolution 1, so this validates that
evolution's *diagnosis* (the export is a fork, and it travels without you) rather than independently
confirming its cures. Hypothesis 1 is the load-bearing one; the failure mode to watch is an author who runs
the two composites mechanically and still reads only the white one.

**Back-filled verdict on Evolution 1:**

| Evolution 1 item | Result |
|---|---|
| Verification loop — export, read pixels, crop, fix | **PASS, and found incomplete.** It caught nothing here because its instruction — *"read the PNG"* — is under-specified for a transparent export. Extended rather than revised; the loop was right, its input was ambiguous |
| *Two views, two files* | **PASS.** The reviewer independently asked for the architecture view first and the pipeline as optional follow-up — exactly the split predicted. Second use → **`KEEP` candidate** |
| *Reading order is separate from grouping* | **PASS under change.** Adding two steps mid-sequence renumbered 1…11 → 1…13 with no layout consequence, because the badges are the only ordering mechanism |
| *One meaning per colour channel* | **PASS, and it absorbed a third fact.** "Consumed as-is" and "next phase" both had to ride the card border; solved with dash *length* (short = consumed, long = next phase) rather than a new colour. Worth noting: **border style is a second channel on the same element**, and it has capacity |

---

## Evolution 3 — 2026-07-31 — The destination is the test; and a count that lost its qualifier

**Trigger.** Final check on the client deck that both diagrams had been embedded into. For the first time the
exports were inspected **in situ** — rendered inside the actual slides — rather than as standalone PNGs.

### Patterns found

| # | Pattern | I/E | Proof |
|---|---|---|---|
| 1 | **Compressing a qualified count converts it into a different, false claim.** The catalogue is 42 rules of which 4 are not machine-checkable, so 38 execute. The view with room stated all four numbers correctly; the view with one line said *"42 checks, on every column"* — asserting an execution count nobody claimed | H/L | Two errors in four words, on the author's own diagram, found during a review whose stated purpose was catching exactly this |
| 2 | **A compressed-count error is review-proof, because it matches the source's headline number.** A reviewer checking "does the diagram agree with the document" sees 42 and 42 and passes it | H/L | It survived authoring, an export, a re-export, and being embedded in a client deck |
| 3 | **White/dark compositing is a proxy for the destination, not a substitute.** Both composites were clean; the real backdrop was a slide layout carrying a decorative element behind the transparent diagram — a condition neither synthetic background can simulate | M/L | Only visible when the slide itself was rendered |
| 4 | **Two views of one system are each other's cheapest detector.** Where both state a shared figure, the roomy view is usually right and the compressed one wrong. Diffing them is nearly free and needs no external source | M/L | The pipeline view held the correct split throughout |

### Hypotheses applied

| # | Change | File | Pattern |
|---|---|---|---|
| 1 | **New: "A number that needs a qualifier does not fit in a box — drop the number, not the qualifier"** — the compression mechanism, prefer-operative-over-headline, name diagrams in the project's numbers chain, and diff shared figures across views | `references/quality-conventions.md` §The export is a derived artifact | 1, 2, 4 |

*(Pattern 3 is recorded but **not yet actioned** — the fix belongs in the composite step and the right wording
isn't settled. Candidate: "when the destination is known, render the destination." Left open deliberately
rather than guessed at.)*

### Validation (fill on the next diagram-bearing engagement)

- [ ] No canvas carries a count whose qualifier is not also on the canvas.
- [ ] Where two views share a figure, they are diffed before either ships.
- [ ] Diagram figures appear by name in whatever the project uses as its numbers-reconciliation chain.
- [ ] A transparent export destined for a known template is checked **on that template**, not only on composites.

**Verdict: `PENDING`.** Third consecutive evolution from one engagement and one author, so these validate the
diagnosis rather than independently confirming the cure.

**Back-filled verdict on Evolution 2:**

| Evolution 2 item | Result |
|---|---|
| Two-background compositing | **PASS as process, inconclusive as detector.** Both composites were run on the re-export and were clean. The dark pass found nothing new this round — one data point, not a refutation. But see pattern 3: it did **not** catch the destination-background condition, which is a real limit of the cure, not a lapse in applying it |
| Closed lane gaps | **PASS.** The pipeline rendered correctly inside the deck, on a non-white backdrop — the exact condition that produced the black bars. Second use → **`KEEP` candidate** |
| Grow-height-never-move-origin | **PASS.** No waypoint drift survived into the embedded export |
| Transparency re-runs the full loop | **PASS, and extended.** The loop caught nothing this time because the defect that mattered was *content* (the count), not rendering — a useful reminder that the transparency loop is a rendering gate and does not read the words |
