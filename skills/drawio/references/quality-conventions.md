# Presentation-Grade draw.io — Quality Conventions & Verification Loop

Distilled from iterative architect-review cycles (two presale engagements, Jul 2026). These rules exist because every one of them was violated once and caught by a human reviewer or a render check — the XML always looked fine.

**Read the content rule first.** *Specification, Not Explanation* is below the verification loop and is the one most likely to be broken, because breaking it feels like being helpful.

## The Verification Loop (non-negotiable for client-facing diagrams)

**"Export succeeded" is not a gate. Pixels are the gate.**

1. Export: `draw.io --export --embed-diagram --format png --scale 2 --border 12 --output name.drawio.png name.drawio`
2. **Read the PNG** and inspect the whole diagram.
3. **Crop suspect regions** (PIL: `Image.open(png).crop((x1,y1,x2,y2))`) — arrowheads, edge labels, corridor areas — and Read the crops. Scale factor: `px = page_units × scale`, plus border.
4. Fix → re-export → re-crop. Repeat until clean.

Defects this loop catches that XML review never does: edges passing through boxes, labels overprinting arrows/borders/each other, arrowheads landing short of targets, broken icon placeholders, **card text overflowing its border**, and **hooked arrowheads from a micro-bend**.

### A transparent export must be read on TWO backgrounds, not one

**Reading a `-t` PNG straight out of the exporter tells you almost nothing reliable**, because what you see is your viewer's backdrop, not the artifact's. Composite it yourself, twice, before judging anything:

```python
from PIL import Image
im = Image.open(png).convert("RGBA")
for name, bg in (("white", (255,255,255,255)), ("dark", (20,20,20,255))):
    Image.alpha_composite(Image.new("RGBA", im.size, bg), im).convert("RGB").save(f"{name}.png")
```

- **On white** — what the slide will actually show. Dark text, thin borders and light fills are only legible here. Read this one for content.
- **On dark** — this is the diagnostic pass, and it is the one people skip. It renders every transparent pixel as ink, so it shows you the **negative space your design is silently relying on**.

Two defects only the dark pass finds:

> *Observed, both in one export.* A title set in default black was invisible in the viewer and read as *"the title didn't render"* — it was fine, the viewer's backdrop was dark. And **five swimlanes separated by 10-unit gaps** turned into five heavy black bars that visually **severed every edge crossing them** — three separate arrows were reported as broken. On the white slide both were invisible. Neither is a rendering bug; both are the design depending on the backdrop.

**A diagram must not depend on the page background to look correct.** If it only reads on white, export it opaque — or fix the geometry so it reads on anything.

### Narrow gaps between stacked containers become bars

A gap of ~10–20 units between adjacent lanes is invisible on white and reads as a **drawn black bar** on anything else. Make stacked lanes **contiguous** — bottom of one exactly equals top of the next. Deliberate corridors (≥40 units, carrying routed edges) are fine: they read as space, not as a bar.

**Close the gap by growing the upper container's height, never by moving the lower one's `y`.** Children hold *relative* coordinates and edge waypoints are *absolute*, so growing a height moves nothing and invalidates nothing; shifting an origin moves every child and breaks every waypoint below it. Assert contiguity after the edit rather than eyeballing it:

```python
for a, b in zip(lanes, lanes[1:]):
    assert a.y + a.h == b.y, f"gap between {a.id} and {b.id}"
```

**Card text overflow is the most common silent one.** For the icon-on-left card pattern, usable text width is
`card_width − spacingLeft − ~10`, and rendered width is roughly `0.6 × fontSize × char_count` for bold,
`0.55 ×` for regular. A bold title 4 characters too long simply prints past the border; nothing errors, and
at full-page zoom it looks like padding. Crop and read every card whose title is within ~15% of the limit.

## The export is a derived artifact, and it travels without you

**An exported PNG/SVG is not a copy of the diagram — it is a fork of it.** The moment the `.drawio` changes,
the export is wrong, and the export is the thing that gets embedded in decks, pasted into chat, and shown to
clients. It carries no indication of its own staleness.

> *Observed, and it cost something.* A `.drawio` source was corrected — a rule count moved from `23` to `42` —
> and the `.png` was not re-exported. The stale export was picked up by a colleague and embedded in a
> **client-facing deck**, whose body text then repeated the wrong count. The number was wrong in two places
> and the diagram was also missing an entire review round's worth of corrections. The project index had
> flagged the PNG as stale in prose; that did not stop it.

Rules that follow:

- **Re-export in the same edit as the source change.** Never "later". If you edit the `.drawio` you own the
  `.png` in the same breath — the export command is one line.
- **Any figure on a canvas that is maintained elsewhere needs a named maintenance dependency**, recorded where
  the file is indexed: *"the L2 box carries the rule counts and must be reconciled against `<doc>` §x whenever
  those move."* A count on a canvas with no named owner will go stale.
- **Numbers inside images are ungreppable.** A repo-wide search for a corrected figure will not find it in a
  PNG, a PPTX, or a PDF. Auditing a figure change therefore means *opening and reading* every artifact that
  embeds the diagram — the search that normally proves completeness is blind here.
- **Assume someone else already has your export.** Before correcting a canvas figure, ask where the previous
  export went. Decks, chat threads and email attachments do not update.

### A number that needs a qualifier does not fit in a box — drop the number, not the qualifier

Staleness is the failure where a canvas figure *was* right. This is the one where it never was: a box has room
for one line, the source figure carries a caveat, and the caveat is what gets cut.

> *Observed, on the author's own diagram, during a review whose whole purpose was catching this class of
> defect.* The catalogue is **42 rules — 20 arithmetic, 18 conformance, 4 not machine-checkable**, so **38
> execute**. The pipeline view had room and stated all four numbers, correctly. The architecture view had one
> line and compressed it to *"**42 checks**, on every column"* — under a box titled *"Check the arithmetic."*
> Two errors in four words: 42 checks do not run (38 do), and the arithmetic family is 20, not 42. The
> reviewer had already made the deck's body text say 38, then handed over a picture saying 42.

The mechanism is that **compression silently converts a qualified count into an unqualified assertion.** "42
in the catalogue, 4 unrunnable" becomes "42 checks", and "42 checks" is a claim about execution that nobody
made. It survives review because it *matches the source document's headline number* — a reviewer checking
"does the diagram agree with the doc" sees 42 and 42 and moves on.

Rules:

- **If the qualifier will not fit, the number must not go on the canvas.** *"Check the arithmetic — does every
  total equal the sum of its parts?"* is complete and cannot go stale. Add the count only where you can also
  carry what it excludes.
- **Prefer the operative number to the headline number.** Put on the canvas the figure describing *what this
  box does* (38 that execute), not the one describing the catalogue it came from (42 that exist).
- **Diagram counts belong in the numbers chain.** Wherever the project records that editing a figure in one
  document requires reconciling others, **name the diagram in that chain.** A count on a canvas is a restatement
  with no back-reference, and it is the last artifact anyone re-checks.
- **When two views share a figure, diff them.** The view with room usually gets it right and the compressed
  view usually gets it wrong. Disagreement between your own two diagrams is the cheapest detector you have.

## Specification, Not Explanation — what belongs in a box

**The most common content failure is a diagram that argues instead of describing.** It is easy to commit because each individual clause feels helpful.

> *Observed.* A verification-engine diagram shipped with a persuasive subtitle ("where the work is agentic, and where it deliberately is not"), three callout boxes of reasoning under the canvas, and justification clauses inside the boxes themselves — "not tested, not tuned, no fallback", "naming varies; the rules do not", "nothing reaches gold on the agent's authority alone". The reviewer's verdict: *"These sound like a sales pitch. Either we explain them fully or don't."*

**The test for every line: could a reader disagree with it?**

- **No** → it is *specification*. Keep it. Component name, mechanical action, inputs and outputs, counts, the service it runs on.
- **Yes** → it is *explanation*. Move it to the design doc or the decision record.

`Writes provenance per value: extracted · agent-corrected · human-corrected` is checkable, so it stays. *"Nothing reaches gold on the agent's authority alone"* is the same fact styled as a promise, so it goes.

This is the `core` **two-channels** rule (`../../core/references/pushback-and-teach.md`) applied to a canvas: the WHY lives in the conversation and in `decisions.md`, never inside the deliverable. A diagram is a deliverable.

**A half-explanation is worse than none.** "Not tested, not tuned, no fallback (D-016)" invites *"why not?"* in a room where you would rather answer that deliberately than have it read off a box.

**What is usually missing instead**, because it was mistaken for detail rather than substance: the **runtime each lane or region executes on** (put it in the lane header), **explicit inputs and outputs** on any box representing a transformation, and **counts** where a set is enumerated elsewhere. These are what an architecture reader actually needs and they are frequently absent from a diagram full of prose.

## Edge Labels

- **Label-gap rule:** a label needs clear whitespace at least as wide as its rendered text (≈ `0.55 × fontSize × char_count` page units). **An offset cannot fix a gap narrower than the label — widen the layout instead.** Nudging just moves the collision.
- Always set `labelBackgroundColor=#ffffff` on labeled edges.
- **Placement controls:** edge geometry `x` (relative, −1…1 along the path) picks *which segment* the label sits on; `<mxPoint as="offset"/>` nudges from there. When two labels collide, separate by segment choice first, offset second.
- Plan label real estate up front: leave 30–60px gutters between containers *on the routes you know will carry labeled edges*; park long labels in open bands above/below containers.

## Edge Routing

- **Corridor routing:** run orthogonal edges through the deliberate gutters between containers. After adding waypoints, trace every segment: crossing a container *border* is fine; crossing a *card or text* is a defect.
- **Swimlane header bars are full-width text zones.** Any vertical exiting through a container's top crosses the header bar — choose a crossing x outside the (centered) title text span, or route out the side through an inter-container band.
- Leave ≥20px of straight final segment for the arrowhead; a bend too close to the target renders a broken-looking arrow.
- Stacked siblings: if an edge from box A must reach something directly below box B, consider **swapping A and B** so the edge drops through empty space instead of through B.
- **Separate the anchor points when several edges touch the same box side.** Two edges left at default anchors land on the same midpoint, and any label there prints over the other edge. Set `exitX/exitY` and `entryX/entryY` to distinct fractions — e.g. one edge leaves a right edge at `exitY=0.28`, another enters it at `entryY=0.78`. Auto-routing will not do this for you, and the collision is invisible at full-page zoom.
- **Two edges of the same colour running parallel in one corridor read as a single path**, even when one is dashed. Either give them clearly different y-bands, or re-anchor one so it takes a different route entirely. A straight vertical off a box's top is almost always cleaner than a three-bend detour sharing someone else's lane.
- **The same applies to an edge running parallel to a container *border*.** A dashed amber edge 12px below a dashed amber container edge is two lines that read as one thick one — and unlike edge-vs-edge, nothing in the XML suggests a problem, because the border is not an edge. If a route must travel alongside a band boundary, either put ≥40px between them or re-anchor to approach from a side instead.
- **The anchor fraction must resolve to the exact waypoint coordinate.** `entryX`/`exitX` are fractions of the target's width; a waypoint is absolute. If they disagree by even 1–2px the router inserts a micro-bend right at the arrowhead and it renders as a **hook**, not an arrow. Compute the fraction from the geometry — `entryX = (x_waypoint − x_target_left) / target_width` — rather than rounding to a tidy `0.65`. This defect is invisible at full-page zoom and only shows in a crop.
- **Budget return corridors before laying out.** Count the backward edges (feedback loops, human-correction paths, promote-to-store paths) *first*, then reserve one x-band each to the right of the last column, plus a y-band each below the lowest box they must clear. Discovering this by collision costs a full relayout; three return paths need three bands, and they must clear the boxes they pass, not just each other.

## One meaning per colour channel

Colour is not one variable. On an architecture diagram it is routinely asked to carry **two orthogonal
facts** — *what platform does this run on* and *who builds it* — and if both ride the same channel, turning
one up destroys the other.

> *Observed.* A diagram used **card fill** for ours-vs-theirs (solid colour = we build it, grey = consumed).
> A reviewer asked for coloured section backgrounds. Raising the band tint collapsed the contrast the
> ownership encoding depended on — and that encoding was the scope boundary the client must not misread.

Split the channels explicitly:

| Channel | Carries | Why this one |
|---|---|---|
| **Band / region background** | *where it runs* — platform, host, environment | Largest area, read first, changes least often |
| **Card fill + border style** | *who owns it* — built by us / consumed as-is / deferred | Reads against the band, so contrast is preserved either way |

Two consequences worth stating:

- **Inverting the fill can strengthen the encoding.** A white card on a tinted band separates *better* than a
  grey card on a white one. Tinting the band made the ownership distinction clearer, not muddier — once the
  channels were separated.
- **The legend must name the channel that actually carries the meaning.** *"Solid fill = built by us"* became
  false the moment fills changed; *"solid coloured **border** = built by us"* is what was true. A legend
  describing the wrong channel is worse than none, because it is checkable and wrong.

Also: grey band bodies need to be **darker than you expect** (~`#ECECEC`, not `#F6F6F6`) before a white card
inside them reads as a distinct object. Caught by cropping the band and reading it, not by looking at the page.

## Reading order is a separate problem from grouping

**Grouping by host is architecturally correct and destroys the reading order.** Once components are grouped
by runtime — agents in one region, deterministic jobs in another — the flow zig-zags between regions and a
viewer cannot tell where to start.

> *Observed.* A reviewer's verdict on a correctly-grouped diagram: *"our design flow logic doesn't quite
> self-explanatory to me."* The vocabulary was fixed first — plain language replacing internal shorthand —
> and it did not resolve the complaint, because the complaint was about *order*, not words.

**Fix: numbered step badges (1…N) on the flow-participating cards.** Small filled circle, top-left, coloured
to the region. Grouping survives, and there is an explicit path to walk. Do **not** reorder to follow the
narrative — that sacrifices the host grouping, which is usually the thing the audience asked for.

Corollary: if a diagram needs both *what runs where* and *in what order at step granularity*, that is
**two diagrams**, not one canvas — see below.

## Two views, two files

An icon-and-service architecture diagram **cannot legibly carry a numbered step sequence**, and a sequence
flowchart cannot carry hosting. They are different genres answering different questions. When both are
needed:

- **Separate files, not separate pages.** Pages get exported as a set, embedded as a set, and go stale as a
  set. Separate files have separate lifecycles and separate recipients.
- **Name which file owns each maintenance-dependent number.** If a rule count, a field count or a task count
  appears on a canvas and is maintained in a document, exactly one diagram should carry it, and the index
  entry must say so. Two canvases carrying the same count is two places to forget.
- Expect a reviewer to ask for the architecture view and a builder to ask for the sequence view. That is the
  signal you needed both, not that one was wrong.

## Container & Card Styling (the ratified look)

- **Sub-containers get colored headers:** `swimlane;startSize=28;fillColor=#<header>;swimlaneFillColor=#ffffff;strokeColor=#<accent>;fontColor=#<dark-accent>;fontStyle=1;pointerEvents=0;`
- **Dominant/region container:** add `dashed=1;dashPattern=6 4;strokeWidth=2` and a tinted `swimlaneFillColor` (e.g. `#f5f9ff`).
- **Icon-on-left cards:** card style `rounded=1;align=left;spacingLeft=44;fontSize=11` with `<b>Name</b><br>short description`; icon is a *separate* `image` cell (~30×30) parented to the same container, positioned over the card's left padding.
- **Icon-on-top-centred is the alternative, and the choice is a real tradeoff.** Card style
  `align=center;verticalAlign=top;spacingTop=<icon_h + 16>`, icon centred at `card_x + (card_w − icon_w)/2`.
  - **Pick it when** a reviewer says content "isn't centred", or when short-text cards leave visible dead
    space on the right. It is also **structurally robust**: nothing depends on estimating text width, so it
    cannot drift on re-export.
  - **Pick icon-on-left when** columns are narrow (≲230px) or the page is **height-bound** against a fixed
    physical target. Icon-on-top costs ~50px of card height, and on a height-bound page that reduces the
    on-slide scale of *everything* — see Density & Legibility below.
  - A reviewer's *"not centred"* is usually a **dead-space** complaint, not a geometry one. Tightening card
    widths to hug content can resolve it without changing the pattern at all. Try that first if the page is
    height-bound.
- Consistent palette per lane family (e.g. channels green `#d5e8d4/#82b366`, platform blue `#dae8fc/#6c8ebf`, offline/jobs orange `#ffe6cc/#d79b00`, core purple `#d9c9f2/#5e35b1`, neutral gray).
- **No meta/provenance in client-facing diagrams:** no "per <person>", "draft", "generated", tool names, or internal cross-references. State facts neutrally. *(An internal working artifact may carry a one-line footer pointing at the documents that hold the reasoning — that is a pointer, not narration.)*
- **Waypoints are absolute; lane geometry is not.** Edges parented to `1` with hardcoded `<Array as="points">` do not move when you resize or reposition a swimlane, so every lane height change silently invalidates every corridor. If a diagram is waypoint-heavy, settle the lane geometry *before* routing, and expect to recompute every waypoint if you change it afterwards. Budget for that when a review asks to tighten the layout.

## Icons

- Azure icons: `image;html=1;image=img/lib/azure2/<category>/<Name>.svg;`
- **Broken paths fail silently** — they render as a generic broken-image placeholder, not an error.

### Enumerate, don't guess — the icon library is on disk

**Do this first.** Every bundled shape lives in the desktop app's `app.asar`, whose header is a JSON
directory you can read without unpacking. This is exhaustive in seconds, and — more valuable — it tells you
what **does not exist**, which visual probing cannot.

```python
import json, struct, zipfile  # zipfile unused; asar is not a zip
p = r"C:\Program Files\draw.io\resources\app.asar"      # macOS: /Applications/draw.io.app/Contents/Resources/
with open(p, "rb") as f:
    _, _, jlen = struct.unpack("<III", f.read(16)[:12]); f.seek(8); raw = f.read(jlen + 8)
s = raw.decode("utf-8", "ignore"); i = s.find("{"); d = 0
for j, ch in enumerate(s[i:], i):
    d += (ch == "{") - (ch == "}")
    if d == 0: break
meta = json.loads(s[i:j + 1])
def walk(n, path=""):
    out = []
    for k, v in n.get("files", {}).items():
        np = f"{path}/{k}" if path else k
        out += walk(v, np) if "files" in v else [np]
    return out
paths = [x for x in walk(meta) if "/img/lib/" in x and x.endswith((".svg", ".png"))]
```

Then **still export a probe grid and read the pixels** before shipping — enumeration proves the file exists,
not that it renders as the product you think it is. A single scratch `.drawio` with one labelled `image`
cell per candidate, exported and read, confirms both at once.

### Brand icons that DO NOT EXIST in any bundled library

Verified by enumeration across all ten libraries (`azure2`, `mscae`, `active_directory`, `dynamics365`,
`ibm`, `sap`, `atlassian`, `allied_telesis`, `cumulus`, `clip_art`), Jul 2026:

- **Microsoft Fabric** — zero. The only `fabric` hits are `Service_Fabric` / `Service_Fabric_Clusters`,
  **an entirely different product**. Using it in a Fabric diagram is a factual error a Microsoft audience
  reads instantly. Nearest defensible stand-in is `analytics/Azure_Synapse_Analytics.svg` (Fabric's
  lineage) — still not Fabric.
- **OneLake** — zero.
- **Excel / any Office app** — zero. `general/Table.svg` is the honest stand-in.
- **Notebooks, Spark** — zero. `general/Code.svg` (`</>`) reads as "code we wrote" without claiming a product.

**When no honest icon exists, use a text-only container header and give the icon budget to the boxes that
have real logos.** A wrong logo costs more credibility than a missing one.

### Verified-rendering azure2 paths (probe-confirmed)

- `ai_machine_learning/`: `AI_Studio.svg` *(= AI Foundry lineage)* · `Cognitive_Services.svg` ·
  `Cognitive_Services_Decisions.svg` · `Computer_Vision.svg` · `Form_Recognizers.svg` *(= Document
  Intelligence lineage — correct, not a substitute)* · `Language_Services.svg` · `Azure_OpenAI.svg` ·
  `Machine_Learning.svg` · `Speech_Services.svg`
- `general/`: `Code.svg` · `Browser.svg` · `Table.svg` · `Files.svg` · `Versions.svg` ·
  `Cost_Management.svg` · `Workflow.svg` · `Production_Ready_Database.svg` · `Module.svg` ·
  `Storage_Container.svg` · `Input_Output.svg` · `Dashboard.svg`
- `analytics/`: `Azure_Synapse_Analytics.svg` · `Azure_Databricks.svg` · `Power_BI_Embedded.svg`
- `power_platform/`: `PowerBI.svg` *(the real Power BI mark — prefer over `Power_BI_Embedded`)* ·
  `PowerApps.svg` · `CopilotStudio.svg` · `Dataverse.svg`
- `app_services/`: `App_Services.svg` · `API_Management_Services.svg` · `Search_Services.svg`
- `databases/Azure_SQL.svg` · `storage/Data_Lake_Storage_Gen1.svg` · `identity/Azure_Active_Directory.svg` ·
  `management_governance/Monitor.svg` · `management_governance/Application_Insights.svg` ·
  `security/Key_Vaults.svg` · `compute/Function_Apps.svg` · `integration/Logic_Apps.svg` ·
  `compute/Kubernetes_Services.svg` · `containers/Kubernetes_Services.svg` · `databases/Azure_Cosmos_DB.svg`
- `networking/`: `ExpressRoute_Circuits.svg` · `Firewalls.svg` · `Virtual_Networks.svg` ·
  `Web_Application_Firewall_Policies_WAF.svg`
- Non-image alternative for a deliberately **unbranded** store: `shape=cylinder3` — reads unmistakably as
  "a database" without naming a product, which is what you want when the product choice is still open.
- **Known broken:** `management_governance/Azure_Purview_Accounts.svg`, `web/Notification_Hubs.svg`

## Working With Review Feedback

- Reviewers flag *classes* of defect, not instances. When one label overlaps, audit **every** label the same way before resending — the verification loop, applied diagram-wide, is cheaper than another review round.
- When embedding exported PNGs into decks (python-pptx), compute placement from real image dimensions (aspect ratio), and re-render the deck page to verify fit — diagrams wider than ~2:1 overflow standard 16:9 content areas easily.

## Icon Density — default to using icons

**Every named service/component gets an icon if a verified one exists.** A text-only card reads as a placeholder; an icon+label card reads as finished. Don't reserve icons for "important" boxes — apply them uniformly across a diagram, including secondary/on-prem boxes when a reasonable icon exists (generic server/database/desktop shapes are fine for legacy or unspecified systems). Only skip an icon when nothing sensible applies (e.g. an abstract "EDW" placeholder with no canonical logo).

Icons should be **visually dominant, not a decorative badge** — size them to roughly 40-60% of the card's shorter dimension, not a small corner mark. If a reviewer says "make the logo bigger," they mean a step change (1.4-1.8×), not a nudge.

## Transparent Backgrounds

**Export client-facing / deck-bound PNGs with `-t` (transparent).** A white background is invisible in draw.io's own canvas but becomes a hard visible box the moment the image lands on a slide with any template background, texture, or corner branding/watermarks — exactly the kind of defect the pixel-verification loop should catch (check it when reading the exported PNG: does it carry a white rectangle that will fight the slide background?). Default to transparent for anything destined for a deck or doc; only export opaque when the image is viewed standalone.

**Transparency moves work into the diagram, it does not remove it.** The moment you pass `-t`, every gap in the layout and every dark-on-default text run becomes background-dependent, and the export can no longer be judged by looking at it. Two obligations follow, both non-optional:

1. **Run the two-background composite** above before calling the export verified.
2. **Switching an existing diagram from opaque to transparent is a change with a blast radius.** Defects that white was quietly concealing — inter-lane gaps, default-black type, cards relying on the page for their fill — all surface at once, and they surface *in the recipient's viewer*, not yours. Re-run the full loop on the first transparent export of a diagram that previously shipped opaque; do not treat it as a flag change.

## Density & Legibility — the real lever for "hard to read" feedback

When a diagram will be scaled down to fit a fixed physical size (a slide), the rendered size of every icon and letter is governed by `physical_size / page_units` — **not** by the fontSize or icon size written in the XML alone. This means the single highest-leverage fix for "text is too small on the slide" is usually **shrinking the page's total footprint** (cutting dead space), not just bumping fontSize:

- Figure out which dimension of the diagram is *binding* against the target physical box: compare the diagram's aspect ratio to `width_max / height_max`. If the diagram is wider (relatively) than the target box, it's width-bound — shrinking page **width** increases the effective on-slide scale; shrinking page height does nothing for legibility there (it only changes how much of the vertical ceiling gets used). If the diagram is taller-relative, it's height-bound and the lever flips.
- Compacting a diagram (tighter cards, shorter labels, smaller gaps) on the *binding* axis is worth more than any single fontSize increase, because it raises the effective size of *everything* — icons, text, line weights — simultaneously.

**The reverse complaint — "it looks empty, should we add more?" — has a different fix order, and the instinct to fill is usually wrong.** Whitespace in a lane diagram is nearly always a *container* problem, not a *content* problem: lanes sized generously at layout time end up twice the height of the boxes inside them.

1. **Tighten every container to hug its content first.** This costs no words and raises the effective on-slide scale of everything, for the reason in the paragraph above.
2. **Then, if it still reads thin, add specification — never prose.** Runtime in the lane header, inputs and outputs on transformation boxes, counts. See *Specification, Not Explanation*.
3. A diagram that shrank while gaining content is the correct outcome. If the page grew, you added narration.

**Practical order of operations when asked to "make it more readable" or "condense":**
1. Bump icon size (see Icon Density above).
2. Condense every card's text to keyword phrases — drop connective words and secondary clauses; a card label is not a sentence.
3. Shrink card padding so the border hugs the icon+text (no more than ~15-20% dead margin).
4. Reduce inter-card / inter-row gaps modestly.
5. Recompute the page's total width/height from the new tighter layout — this compaction, not the individual tweaks, is what makes the exported image read bigger once placed on a slide at a fixed physical size.

**Tightening a gap can turn a previously-safe label into a border collision.** The label-gap rule (min clear width ≈ `0.55 × fontSize × char_count`) was satisfied at the *old* gap size — after compaction, re-check every labeled edge that crosses a gap you shrank, not just the ones you intentionally touched. This is a common self-inflicted defect from density passes: shrinking a 30px gap to 22px can leave a label with no room even though nothing about the label itself changed.

**Risk-managing dense diagrams with many hardcoded edge waypoints:** a full relayout (moving every container/card position) requires recomputing every absolute waypoint and re-verifying every corridor — expensive and error-prone on diagrams with many `<Array as="points">` edges. When the diagram is edge-waypoint-heavy, prefer a **low-risk pass**: enlarge icons and condense text *in place* (same card x/y/width/height, just bigger icon + tighter spacingLeft), which touches nothing edges depend on. Only reflow container/card positions when the ask specifically requires shrinking the overall footprint (e.g. to fit a hard physical-size ceiling) — and budget time to re-verify every affected waypoint when you do.

## Client Review Lessons (recurring feedback patterns)

Feedback from an actual architecture-diagram review round (Jul 2026) that generalizes to most stakeholder reviews of dense technical diagrams:

- *"Make each service's logo bigger"* → icons were decorative-sized relative to the card; fix is Icon Density above, applied aggressively, not incrementally.
- *"Shorten the text to common/frequent keywords"* → cards had full clauses instead of keyword phrases; fix is text condensation (step 2 above).
- *"The border should hug close to the logo and text"* → cards had generous dead padding around a small icon+short label; fix is tightening card height/padding to content (step 3 above).
- *"Reduce spacing between components"* → perceived over-spacing was often actually a symptom of small icons/dense text inside oversized cards, not literally-too-large gaps between cards — enlarging icons and condensing text can resolve this complaint even without touching inter-card gaps. Check both: measure actual gaps against the label-gap rule before assuming they need to shrink.
- *"Cutting content down makes the deck easier to read immediately"* — the standing bias when a reviewer flags density: cut before you shrink fontSize, and cut before you add more explanatory sub-clauses. Every diagram destined for a slide should default toward fewer words and bigger icons over more precise/complete prose.

## Pairing With the drawio MCP

The MCP tools (`open_drawio_xml`, `search_shapes`) open diagrams in the app for interactive viewing/shape lookup. They do not replace the loop: the CLI export + PNG-read is the only channel that shows you what the client will see. Author XML → (optionally) open via MCP for a live look → **always** gate on the exported PNG.

## Deleting a container: derive its children, never list them

Removing a grouped element means removing the container **and everything whose `parent` points at it**. A
hand-written list of children is the failure mode, because containers accumulate cells nobody remembers —
icons, badges, labels added later.

**A cell left pointing at a deleted parent does not raise an error. The CLI exports a ~108×108 stub and
returns exit code 0.** The build "succeeds", the file is written, and the only symptom is that the diagram is
gone. In one session this passed unnoticed until the output's dimensions were checked.

Two rules follow:

- **Derive the child set from the parent reference and repeat until stable** — a dropped child can orphan its
  own children. Then re-scan for any dangling `parent`, `source` or `target` before writing.
- **Assert on the exported image's dimensions, not the return code.** Compare against the previous export; a
  collapse to a few hundred pixels means a structural break, and a large unexplained change in aspect means a
  cell moved outside the expected bounds.

## Height is the binding constraint on a slide, not width

A diagram placed on a slide that also carries an eyebrow and a title usually has ~5.8in of vertical room on a
7.5in slide. Width is then a *consequence* of the aspect ratio, not a free choice — so a diagram that reads
too small is almost never fixed by repositioning it.

**Make the diagram shorter and the width arrives on its own.** In one case cutting a band that consumed a
fifth of the height to say four things stated elsewhere in the deck moved the aspect from 1.66 to 2.04, which
turned the same 5.8in of height into 11.85in of width instead of 9.64in — a 23% linear gain, on top of a
caption type rise, with no change to the placement.

Look for: bands of cross-cutting concerns, generous inter-band gaps (one was 80 units where every other was
30–40), and an internal title that duplicates the slide's own title.

## Export transparent, embed composited

`-t` produces a transparent background, which lets the destination template's decorative artwork show through
the diagram. Composite onto white before embedding:

```python
bg = Image.new("RGBA", im.size, (255, 255, 255, 255))
out = Image.alpha_composite(bg, im.convert("RGBA")).convert("RGB")
```

This also removes a whole class of false review findings — "background curves cross the diagram" — that are
artifacts of the transparency rather than defects in either artifact.

**And keep the on-disk export identical to what is embedded.** Embedding a composited copy while leaving the
transparent original in the repo means the two silently diverge, and any check comparing them fires.

### Verifying a re-export by pixel diff — do not flatten the transparent original first

The natural check after a small edit is to diff the old export against the new one and confirm that only the
intended region moved. If either image is transparent, **`.convert("RGB")` is not a neutral normalisation** —
it discards the alpha channel and paints every transparent pixel **black**. Diff a flattened original against
a composited-on-white new export and roughly **a third of all pixels** report as differing, which reads
exactly like a catastrophic render failure and is not one.

**Composite both onto the same background before comparing**, never convert. For reference, the correct diff
for a two-word text change inside a 3854×1960 diagram was **5,249 pixels of 7.5M — 0.07%, in two horizontal
bands**. That is the shape a real localised edit produces: a tiny percentage, spatially clustered where the
change was. A diff that is both large and *diffuse* is almost always a comparison artifact rather than a
rendering one.
