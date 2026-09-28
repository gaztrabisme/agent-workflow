# Distilling a course into a skill

Reader: an agent turning a complete course (or a book, or a talk series) into a skill whose main content is the course's *method*: the ordered way of working it teaches, with the checks at each step. Run this inside the normal `authoring-checklist.md`; this file adds only what is specific to a course source.

Worked example: `../../color-theory/` (Domestika course 1140, distilled 2026-09-26). Its `EVOLUTION.md` records every decision below and what the dogfood run found.

Terms used here:
- **Reading copy:** the course as cleaned, translated text with figures, produced by `../../domestika-course-archive/` (`reading_copy.py export --pdf`) or by hand for other sources.
- **Anchor:** a citation string that locates one section of the source, such as `1140 · U3 · L09 · 05:00–06:14` (course · unit · lesson · video time range). Every section heading in the reading copy carries one.
- **Method digest:** one file in `references/method/` covering one stage of the method, every claim cited to an anchor.
- **Science library:** an existing reference collection on the same subject (facts, formulas, history) that has no method of its own.

## 0. Before starting

- The reading copy has passed its own checks: every lesson approved by the owner, or passed instead by an independent audit loop — an auditor from a different model lane than the writer, against a stated pass condition — and marketing removed. Distilling from an unchecked copy bakes errors into every citation.
- Read the whole course before writing anything. The method is a synthesis across lessons, and courses often teach in a different order from the working order (the color course taught theory last on purpose).

## 1. Decide how an existing skill in the area fits

Look for a skill that already fires on the course's subject. Classify it before deciding anything:

| It is | Then |
|---|---|
| A **collection**: facts and digests, no ordered method | The course becomes the main system. The collection goes inside the new skill as its science library, vendored unchanged with `git subtree add --prefix=references/<name> <url> main --squash`. Never edit it there; update with `git subtree pull`. |
| A **system** with its own method | Do not merge. Add the course as a reference to it, or build a separate skill with a disambiguation clause on both sides. |

Ask the user to confirm the classification. It decides the whole shape.

## 2. Repo layout

```
SKILL.md
EVOLUTION.md
NOTICE.md                  private course material; license of anything vendored
references/
  method/                  one digest per stage (templates/method-digest.md), plus:
    <review>-checklist.md    numbered tests T1…Tn, each with a pass condition and the stage to go back to
    science-crosswalk.md     course claims against the science library (templates/science-crosswalk.md)
    measurement.md           formulas and default thresholds for every measurable test
  course/                  the reading copy: lesson .md files, unit tasks, frames/, the PDF, pdf-index.md
  templates/               fill-in output templates the agent renders and checks (step 5)
  <science-library>/       the vendored collection, unedited
scripts/
  check_refs.py            copied from ../scripts/check_refs.py, so the skill stands alone
  checks.py                measures the tests without the course's own tool (step 5)
```

Keep the method and the source apart. `method/` is the distilled system; `course/` is the evidence it cites. A reader must be able to go from any claim to its anchor, and from the anchor to the lesson text, the figure and the PDF page.

## 3. Write the method digests

- One digest per stage of the working order. Start from `templates/method-digest.md`.
- Every claim carries an anchor. A claim with no anchor is either the teacher's (find the anchor) or yours (label it "derived" and say what it was derived from).
- Keep the teacher's examples; they carry the meaning. Mark anything read off a figure rather than said aloud as "(frame)".
- Each digest ends with the practice task the teacher set, linked to the unit file.
- After every edit run `python3 scripts/check_refs.py .`. It fails on a broken link, a missing file or an anchor that does not exist in `course/`.

## 4. Write the crosswalk

Check each important course claim against the science library and give it one verdict (`templates/science-crosswalk.md`):
- **Agrees:** the science supports the claim as stated.
- **Refines:** the claim works in practice but needs a correction, which is stated.
- **Adds:** the science covers something the course does not.

Record disagreements here; never merge a correction silently into a method digest. The corrections that change how the method is applied also go into `SKILL.md` as a short list.

## 5. Rebuild execution and verification for agents

A course teaches a person working inside one application (the color course used Photoshop throughout). Steps 3 and 4 carry the *method* across: what to decide, in what order. They do not carry how an agent *makes* the work or how it *proves* the work is right, because an agent usually cannot run the course's application and cannot look at its screen. A course skill therefore has three layers, and this step builds the last two.

### Execution: how the agent makes the artifact
- **Output medium.** For each kind of deliverable, name what the agent writes. Shapes, diagrams, charts and icons are SVG. Layouts, slides and pages are HTML that composes the SVG. Raster images are for photographs and textures only. WebGL or WebGPU are for 3D scenes and data too large for SVG. One renderer, headless Chromium, turns any of these into PNG, PDF or video frames, so the check loop below sees exactly what the reader will see.
- **Templates and scripts.** Ship a script or a template instead of an instruction when a step recurs, must be exact, is something agents do badly, or fails silently (text overflowing its box, a color drifting off its ramp). Everything else stays an instruction. Scripts go in `scripts/`, fill-in templates in `references/templates/`.
- **Domain conventions win.** Where the reader's domain has conventions (a drilling engineer's depth axis pointing down, a trading desk's red for losses), they override the course's taste; the skill says so. Components specific to one project belong in that project's code, not in the skill.

### Verification: the render-and-check loop
Render the artifact, check it, fix it, render again. The checks run in a fixed order:
1. **Code checks first**, because they are exact and cheap: contrast and color-vision deficiency, text overflow and collisions, whether each mark matches its data, value and chroma against the plan. Each is a script subcommand with a default threshold.
2. **Vision second**, by a reviewer that did not make the artifact (a fresh context), given the rendered image and specific questions taken from the review checklist, such as "is the focal point the brightest area?", never "does this look good?". When no model with vision is available, those checks are reported as **not judged**; they are never passed silently.
3. **The report** says which checks were measured, judged by vision, not judged, or skipped, and why.

### Measurement outside the course's tool
For every test in the review checklist, give:
- the course's own steps in its tool;
- a tool-independent way to run it: a script subcommand, a formula, or a vision question when no measurement exists;
- a default threshold, marked as the skill's choice where the course gave none.

The color skill shipped without this and its dogfood run failed on it: the tester could not measure a single test. It also found that the course tool's own reading can mislead (HSB saturation reads dark colors as saturated), so check each measure against the science library before adopting it.

### Portability: the skill runs with any agent
- **Hand off only to owned skills**, meaning skills the owner controls and can run anywhere. Where neighbouring work belongs to a skill you do not own, or to a feature built into one vendor's app, state the boundary by artifact ("choosing a chart type is not this skill") instead of naming it.
- **Name no tool that exists in one agent only**, such as a particular agent's file-reading, shell or subagent tool. Say what to do ("open the PDF at page 12", "run `scripts/checks.py contrast`"), not which tool to call. Fix generated text at its source: the color skill's page index named one agent's file-reading tool because the archive script wrote that sentence.
- **Check it before finishing:** search the skill for the names of skills it does not own and for tool names. An empty result is part of the acceptance.

## 6. SKILL.md

Beyond the skeleton (`templates/SKILL.md.skeleton`):
- **Principles** each with an anchor.
- **The flow** as a table: stage · decide · check before moving on · reference.
- **Scale the flow:** the short path for a quick question, the order for a critique of existing work, what to re-check after a fix.
- **Output:** cite anchors or PDF pages; say which tests were measured, judged by vision, not judged, or skipped and why.
- **Execution and verification** from step 5: the output medium per deliverable, the scripts and templates, and the render-and-check loop.
- **When to open the science library**, with the crosswalk's corrections as a list.
- **Grounding gate:** no method claim without an anchor, no fact without a science-library reference.
- The anti-pattern "stating a course principle without its anchor, or presenting a derived summary as the teacher's words".

### Claim audit (when the owner does not review the method)
An auditor from a different model lane than the writer reads every anchored claim beside its source section and gives one verdict: `supported`, `overstated` (says more than the teacher did), `unsupported`, or `derived-unlabelled` (the writer's conclusion without the "derived" label). Anything but `supported` goes back to the writer; at most three rounds.
- **Later rounds replace earlier verdicts** for the same claim, and rows for anchors no longer cited are dropped when the rounds are merged. Otherwise a fixed claim keeps its old verdict and a deleted one keeps failing.
- **Every edit to the method files needs a later audit,** including the small ones at install (a sibling line in SKILL.md) and dogfood fixes. Make those edits before the final audit round, or audit their diff after; an audit older than the files it covers does not count.
- **Dogfood fixes are labelled derived** ("derived: dogfood …") and audited on their diff.

## 7. Dogfood

Use `templates/dogfood-brief.md` with the course-skill tasks listed there: a plan from a brief, a critique of real or mocked work run through the whole review checklist, and a question that must route into the science library. At least one task makes an artifact through the skill's execution path and runs the full render-and-check loop on it, including the vision questions.

## 8. Privacy and install

- Paid course content means a **private** repository, always. `NOTICE.md` says so, names the course and the licence of anything vendored. The `license` frontmatter reads `Proprietary (…)`. Never run the public-publishing steps in `publishing.md` on it.
- Install the skill as the single entry point: unlink any standalone copy of the absorbed collection, update `../../conductor/references/routing-table.md`, and hand the skill's name to the sibling that routed the subject before.
- Check for copies you cannot remove locally. Account-level skills sync back into the app (`anthropic-skills:<name>`, under `~/.claude/skills/synced/`); tell the user to disable them in claude.ai settings.

## 9. Record

`EVOLUTION.md` Evolution 1: classification **distilled**, the sources, the crosswalk count, the dogfood findings and fixes, verdict **PENDING** until two real uses. The skill's claims inherit the course's confidence, not evidence.

## Adding a second course to an existing distilled skill

Export it into its own folder under `references/`, then merge its claims into the existing digests with its own anchors. Where the two courses disagree, record it in the crosswalk as you would a science correction. Extend `check_refs.py --sources` to both folders.
