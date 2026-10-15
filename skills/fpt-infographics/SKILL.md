---
name: fpt-infographics
description: "Build an FPT-branded infographic sheet — a single self-contained HTML page rendered to PNG and vector PDF, on the FPT palette and in BR Omega, gated on measured legibility, brand conformance and sourced content. USE WHEN someone asks for a one-pager, a service-offering sheet, a stats poster, a leave-behind, a capability overview or any page-sized visual carrying FPT's mark to a customer or internally. Not `pptx` (slides), not `drawio` (diagrams), not `screencast` (video), not `solution-architect` (the argument rather than its page). Keywords: infographic, one-pager, sheet, poster, leave-behind, service offering, capability, data visualisation, chart, SVG, brand, BR Omega, FPT Orange, legibility, arcminutes, critical print size, Type3, PDF, A3, A4, client-facing, internal."
license: MIT
---

# fpt-infographics — an FPT sheet that is drawn, measured and sourced

Produce one self-contained HTML file, render it to PNG and to a vector PDF, and do not
hand it over until three instruments say it is finished: the page is drawn rather than
typeset, its type clears a measured legibility floor at a **declared viewing condition**,
and every value on it traces to a source.

> Inherits the `core` kernel — `../core/SKILL.md`. Obey its Integrity Constraints;
> declare its gates; reference its files, never copy them.

Derived from the MIT-licensed `epic-infographics` plugin by OrRon. What is inherited,
what is modified and what is new: `NOTICE.md`.

---

## The two layers

The upstream skill says a design language's tokens are law. Here they are not, and the
conflict is settled once so it is not re-argued on every sheet:

| Layer | Owns | Source |
|---|---|---|
| **Brand** | palette, typeface, logo | `references/fpt-brand.md` — law, no exceptions |
| **Design language** | ground, geometry, signature devices, detail density | one file from `references/design-languages/` |

So a sheet is "cutaway, on FPT brand": the warm paper, the ink linework, the numbered
callout discs and the museum placard come from cutaway; every colour and every glyph
comes from the brand. Where a language's palette disagrees with the brand, discard the
language's palette and keep its geometry. Four languages carry the brand well, four need
care and four should not be used at all — the table is `references/fpt-brand.md` §6.

This exists because the brand kept arriving last. On one engagement the guidelines sat in
the project folder from the first hour and version five still shipped in two off-brand
typefaces on a design language's own palette, and putting it right cost a whole rebuild.

---

## Workflow

### 1. Ground before composing
Read the brief, the source documents, and any prior version of the sheet. Record one line:
`Grounded: <files read> → <what constrains this sheet>`. Ungrounded, you will re-decide
what was settled two versions ago. (core spine #5.)

### 2. Declare the viewing condition — before anything is designed
**This is the first decision, not a check at the end.** A3 poster, A4 handout, PDF at
100% on a monitor, projected at four metres, phone-sized post: each sets a different type
floor, and the floor drives the layout, not the reverse. `references/legibility.md`
carries the model, the thresholds and their citations.

    node scripts/legibility.mjs page.html      # no condition: it lists them and exits 1
    node scripts/legibility.mjs page.html --condition a3-print
    node scripts/legibility.mjs page.html --sheet-mm 420 --distance-mm 500

The instrument refuses to give a verdict without one.

### 3. Settle the audience, and what may not appear
Name who receives it. If the source carries anything that must not reach that reader —
deal values, pipeline, account owners, customer names outside a cleared list — decide it
**now** and write the withheld list into the content brief. Two audiences from one source
is supported and is the safer default when internal figures exist: see §Two audiences.

### 4. Pitch the story, then find the object
One sentence the sheet argues. Then one oversized drawn thing the data lives on and
around — upstream calls this Big Object and it is the difference between a sheet and a
slide. `references/composition.md`, always.

### 5. Pick the canvas
`a3-landscape` 1754×1240 · `a4` 1240×1754 · `wide` 1920×1080 · `square` · `story` · `og`.
The canvas and the viewing condition are one decision made twice; keep them consistent.

### 6. Pick the design language
Exactly one file from `references/design-languages/`, filtered through
`references/fpt-brand.md` §6. Take its ground, geometry and devices. Leave its palette.

### 7. Choose varied representations, and mark them
Read `references/data-vocabulary.md`. One hero element plus several support elements of
*different* families. Three bar charts in a row is one representation used three times.

**Mark every drawn representation** so the preflight can count it:

    <svg data-viz="category:wins-by-offering" ...>
    <svg data-viz="process:delivery-phases" ...>

The family prefix is one of the six questions in `data-vocabulary.md` — `magnitude`,
`category`, `part-to-whole`, `time`, `process`, `relation`. The name after the colon is
free text. An unmarked drawing does not exist as far as the gate is concerned, and a page
with none of them is not an infographic, whatever else is true of it.

### 8. Draw every chart at 1:1
**A chart's `viewBox` width must equal the pixel width it is displayed at.** Pass the
width in as a parameter; never let it default. A chart drawn in a 322-unit box and shown
216px wide paints every label at 0.671 of its declared size, and no CSS-based checker can
see it — it reads the declared 11px and is satisfied while the reader gets 7.38px. This
single fault accounted for most of the unreadable text on one shipped sheet.

### 9. Build the type off the floor, not off taste
Compute the floor from the declared condition and the typeface's own x-height, then set
body text at or above it and everything else up from there. In BR Omega the x-height is
0.470 em, which is small for a grotesque — a 12px body is 5.64px of x-height, and that is
under the threshold for fluent reading on anything smaller than a poster.

When the page does not fit, **pay in leading and chrome, never in glyph size.**

### 10. Preflight — mechanical gate
    node scripts/check.mjs page.html --preset a3-landscape

Canvas size is required; there is no default. It reports overflow, collision, contrast,
the representation count and their families, the drawn share of page height, the hero
ratio, and the minimum SVG scale. Fix errors and rerun until clean.

### 11. Brand gate
    node scripts/brandcheck.mjs page.html --width 1754 --height 1240 --ground "#FAF6EC,..."

Declare the design language's ground tones so they are not reported as off-palette —
declaring them is the point, since an undeclared colour is a colour nobody chose. It
prints three judgements no script can settle; answer them in the content brief.

### 12. Legibility gate
    node scripts/legibility.mjs page.html --condition a3-print

Every element at or above the floor, or the sheet is not finished.

### 13. Render, and print a PDF whose fonts are real
    node scripts/render.mjs page.html out.png --preset a3-landscape --scale 1
    node scripts/topdf.mjs  page.html out.pdf --preset a3-landscape
    node scripts/check.mjs  page.html --preset a3-landscape --pdf out.pdf

All three take the same flags, and all three require the canvas — no silent default.

The PDF check exists because BR Omega ships as CFF outlines, which Skia cannot embed and
replaces with Type3 — unhinted, one content stream per glyph, cached by most viewers as a
bitmap and scaled. The text stays selectable and vector, so a check that counts characters
passes, and the reader still sees mush on zoom. Build the fonts with `scripts/fonts.py`
and this does not happen.

### 14. Look at your own PNG — mandatory
Open it. Two faults on the last engagement were found this way and by no other means: a
caption painted over another caption inside a single SVG, which no collision check sees,
and a drawing that had quietly shrunk to a corner vignette.

### 15. Adversarial read against sources — required before delivery
One pass whose only job is to attack the sheet's claims. It catches a class nothing
mechanical does, and on one engagement it caught all of these:

- FPT's own marketing site cited in a footnote so it read as outside corroboration
- quotation marks around questions nobody had said
- a change-arrow on an accuracy level, so 95% accuracy read as "95% better"
- a `POWERED BY` row listing FPT's own accelerators, so the sheet claimed to be powered
  by itself
- a longlist drawn as sixteen identical dots next to a counted 3, asserting a count no
  source gives

### 16. Write the records, then accept
A content brief (every claim, its source, what was withheld and why) and a review note
(what was wrong, what changed, what is known and accepted). Then:

    python scripts/accept.py criteria.toml

Criteria split into **standing** and **new**, and a failure is reported as a failure.
See §The standing/new split.

---

## Two audiences from one source

Where the source carries internal figures, build both sheets from one source file behind
a flag, rather than maintaining two:

- **client** — cleared names only, no deal values, no pipeline, no owners, no pricing.
- **internal** — everything, stamped visibly, with a filename that cannot be confused.

The internal sheet is a real disclosure risk: every account name and deal value on one
page, in a file that looks exactly like the customer's. The stamp and the filename are all
that separate them, so make both loud.

## The standing/new split

Every criterion is **standing** (won by an earlier version, carries forward for ever) or
**new** (introduced by this goal). A standing criterion that fails is reported as FAILED —
never re-worded to match what was built, never quietly dropped.

A later goal may reverse a standing criterion, and then the row is **SUPERSEDED** — which
requires naming the replacing criterion *and* quoting the goal's own words. Both, or it is
an error. A supersession with no quoted clause is indistinguishable from a failure someone
relabelled.

This exists because eight versions of one sheet each got a suite written from scratch, so
a rule won in version 3 regressed in version 4 with nothing to notice.

## Hard rules

Upstream's rules hold — no invented data, truthful geometry, no dual-axis charts, direct
labels over tooltips, text never wears the data colour, numbers formatted for humans, no
emoji as icons, no framework-default palettes. Added here:

- **Every noun traces to a source.** A caption, a label, a row. If you cannot point at the
  document, the measurement or the sentence someone said, it does not ship. The failure is
  never a lie; it is a plausible detail filling a gap — a cause where there is only an
  absence, a role nobody described, a number that rounds a gap into something concrete.
  When there is no source, **say less**. Deleting the sentence is usually right.
- **A label is a noun phrase, four words or fewer.** "What we will hold ourselves to" is
  not a label; "Acceptance criteria" is. The explaining goes in the cell or in the
  presenter's mouth, never in the thing that names it.
- **No label that narrates its own honesty.** `WHAT WE CAN PROVE`, `OUR HONEST POSITION`,
  `NOT CLAIMED`. A sheet covered in them reads as a sheet with something to hide, and this
  was the single largest rejection on the founding engagement.
- **Verbatim answers provenance, not implication.** Quoting a source exactly does not
  license the arrangement. Five separately-sourced questions set in quotation marks assert
  that somebody said them.
- **A line under a table or chart that restates what is on screen gets deleted.**

## Gates (declared, inherited from core)

- **Grounding gate** — substrate is the brief, the source documents, the brand guidelines
  and any prior version. Record `Grounded: … → …`. (`../core/references/grounding-gate.md`)
- **Gate by the artifact** — the render, the measurement and the PDF's font dictionary,
  never "the script ran". (core spine #2)
- **Output Contract** — a sheet is not done without its content brief and review note.
  (`../core/references/wiki-protocol.md`)
- **Pushback & teach** — when a brief asks for something the brand or the sources cannot
  support, say so before building. (`../core/references/pushback-and-teach.md`)
- **Evolve from real use** — `EVOLUTION.md`, verdicts `PENDING` until two independent uses
  confirm. (core spine #8, mechanism in `../evolution/SKILL.md`)

## Anti-patterns (hard no-list)

- **A sheet with nothing drawn on it.** Text blocks in columns. It once scored 13 of 14 on
  its own suite.
- **Measuring legibility with no declared viewing condition** — a px size is not a claim.
- **Letting a chart's viewBox differ from its rendered width.**
- **Shrinking type to make the page fit.** Leading and chrome first, always.
- **Taking a design language's palette** because the file says its tokens are law.
- **Pointing a build at raw `.otf`** and shipping a Type3 PDF.
- **Delivering a render you have not opened.**
- **Re-wording a failed criterion** so the suite reports green.

## Composition

- **Inherits:** `core` — integrity constraints, gate-by-artifact, grounding gate, wiki
  protocol, pushback-and-teach, the evolution loop.
- **Invoked by:** `project` when the artefact is a page-sized visual; directly by name.
- **Hands off to:** `pptx` when the deliverable is slides, `drawio` when it is a diagram,
  `screencast` when it must move, `vietnamese-copywriter` when the sheet is Vietnamese.
- **Derived from:** the `epic-infographics` plugin (MIT, OrRon) — `NOTICE.md`.

## Files

| File | When to read it |
|---|---|
| `references/fpt-brand.md` | Steps 2, 6 and 11 — always |
| `references/legibility.md` | Step 2 — before the layout exists |
| `references/composition.md` | Step 4, always |
| `references/data-vocabulary.md` | Step 7, always |
| `references/charts.md` | Before writing any chart SVG |
| `references/illustration-and-texture.md` | Step 4, always |
| `references/design-languages/*.md` | Step 6 — exactly one |
| `templates/skeleton.html` | Step 9, as the starting file |
| `examples/geu-ai-service-offering/` | A worked example, end to end |
| `NOTICE.md` | What is inherited and what is ours |

| Script | What it does |
|---|---|
| `scripts/fonts.py` | `.otf` → TrueType woff2, then inline as base64 at build time |
| `scripts/check.mjs` | Preflight: overflow, collision, contrast, representations, SVG scale, PDF fonts |
| `scripts/brandcheck.mjs` | Palette, colour-combination rules, logo ground, typeface |
| `scripts/legibility.mjs` | Visual-angle measurement at a declared viewing condition |
| `scripts/render.mjs` | HTML → PNG |
| `scripts/topdf.mjs` | HTML → vector PDF |
| `scripts/accept.py` | Acceptance criteria, standing/new, pass / SUPERSEDED / FAIL |
| `scripts/pagetext.mjs` | The text a reader can see — grep this, not the HTML source |
| `scripts/nocache.py` | Fails if anything points back into the plugin cache |
| `scripts/measure.mjs` | Ad-hoc rendered-geometry measurement while debugging |
| `scripts/slack.mjs` | Where the vertical space is going |
| `scripts/overflow-scan.mjs` | Which block runs past the canvas |
| `scripts/crawl.mjs` | Pull a JS-rendered source page into text |
| `scripts/animate.mjs` | Inherited, untested here — see `references/motion.md` |
