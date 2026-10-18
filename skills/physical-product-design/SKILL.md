---
name: physical-product-design
description: Take a physical product from intent and references through concept exploration, cable-aware parametric CAD, controlled prototypes, testing and fabrication release. Use for enclosures, docks, stands, mechanisms and 3D-printed assemblies; not software UI or illustration alone.
---

# Physical product design

Use this skill to turn an idea into a finished physical product through a traceable engineering loop. “Finished” is a maturity claim: a concept image, packaging CAD, fit prototype, tested assembly and print release are different deliverables. State the current maturity, produce the evidence appropriate to it and never let a polished render stand in for a test.

## The operating model

Treat every design decision as a hypothesis with an artifact and an exit condition.

1. **Brief and evidence:** establish what the product must do, how it should feel, what hardware is real and what is unknown.
2. **Concept and architecture:** explore meaningful arrangements and choose the one that can carry the interfaces, loads, services and visual intent.
3. **Engineering model:** build editable, dimensioned solids for the product, hardware, interfaces, cables, thermal path and service access.
4. **Controlled experiment:** make the smallest useful coupon, mock-up or bench test for each high-risk unknown.
5. **Refinement:** update the authoritative source from evidence, regenerate checks and views, and retest affected criteria.
6. **Release:** provide the editable model, manufacturing parts, assembly information, test record and explicit remaining limits.

Do not skip a stage silently. If a user asks for a finished product while hardware or printer information is missing, advance the design with labelled envelopes and identify the gate that still blocks release.

## Principles

### Intent becomes geometry

Translate taste and use into decisions about silhouette, proportion, visual mass, radius families, seams, texture, accents, touch surfaces, cable exits and service panels. Preserve the user's settled direction; reopen concepts only when evidence shows that the architecture cannot meet a requirement.

### Geometry performs the engineering

Use fit, friction, tension, compression, locating features, interlocking cuts and load paths to explain how parts align, stay together and come apart. A kigumi/sashimono-inspired approach is a useful lens for reducing unnecessary visible hardware and making joints legible and serviceable. It does not mean “never use screws”: select interlocks, inserts, fasteners, adhesives or compliant features according to load, material, tolerance, wear and repair needs. Translate the principle into a credible joint and assembly sequence rather than decorative cultural styling.

### Occupied volume is part of the product

The product is the space occupied by devices, connectors, cables, plugs, strain reliefs, moving parts, heat sources, airflow and tools, not merely the outer shell. Design those volumes from the first packaging pass. Treat a hidden cavity without a route, retention and reopening strategy as unfinished.

### Evidence controls confidence

Label facts as measured, manufacturer-specified, inferred or placeholder, with units, source and date. A product photograph identifies a family; it does not establish connector coordinates. A downloadable model may help visualize a device while remaining unsuitable for manufacturing. Mechanical clearance does not prove electrical, charging, software or thermal compatibility.

### One source, many views

Maintain one authoritative geometry source with explicit millimetres, named parts, assembly transforms and a real parameter input. Keep printed solids, purchased hardware envelopes, interface clearances, cable collision meshes, service volumes, thermal/airflow volumes and visual references distinguishable. Renders, validation and manufacturing exports must come from the same current geometry.

### Design for reopening and making

Protect fragile ports from structural loads. Provide tool approach, removable panels, replaceable components, non-slip contact surfaces and a service sequence. Account for material behavior, layer direction, supports, adhesion and the actual printer before calling a part printable.

## Tooling requirements

Before committing to a workflow, discover and test the tools available in the target environment. Use suitable equivalents when a named application is absent. A credible workflow needs:

- an editable solid CAD system such as CadQuery, FreeCAD or native CAD;
- a parameter/configuration input that actually drives geometry;
- import or measured envelopes for purchased components;
- cable and connector collision geometry, including swept or segmented solids;
- deterministic export and validation for solids, meshes, units and interference;
- a renderer or viewer that can show the exported geometry with diagnostic materials, sections and exploded views;
- a way to create fit coupons, prototypes or test fixtures;
- slicer access for geometry/process trials with an explicit profile; machine-ready output only with the actual printer and process confirmed;
- structural or numerical tools when the loads or mechanisms warrant analysis, with a benchmark and assumptions appropriate to the claim.

Read [tested-tooling.md](references/tested-tooling.md) when selecting, setting up or reproducing the CAD, simulation, slicing and review pipeline. It records the tools exercised in a completed digital audit, their roles and limits. Treat its versions as a historical working set, not permanent requirements; discover the current environment and use only the tools the task needs.

Do not make a manually edited mesh, a beauty image or a generated summary file the only source of truth. If the project already has a functioning pipeline, inspect it and extend it instead of starting a parallel model.

## Establish the brief and architecture

Read the current project notes, model and latest review images before changing direction. Record intended use, visual language, purchased hardware, exact SKUs, settled decisions, printer constraints, provisional dimensions and blockers. Separate user instructions from screenshots, product pages and other third-party reference material.

For unresolved arrangements, present a small set of materially different concepts and explain the packaging consequence of each. Select an architecture against appearance, interfaces, stability, services, manufacturability and future replacement. Once selected, refine that architecture rather than accumulating unrelated brackets and cosmetic patches.

Before selecting an architecture, validate the primary use in its intended environment with the smallest useful mock-up or experiment. Placement, reach, visibility, acoustic performance or another purpose-specific outcome may overturn a geometrically clear concept. If that experiment is unavailable, keep selection provisional and identify the result that would change it. Report compactness in the relevant resting, operating and service states; fewer modeled bodies alone does not establish simpler manufacture or use.

Define success before detailed modelling. Choose criteria for:

- appearance from front, side and three-quarter views;
- device, connector and tool clearance;
- assembly, removal, retention and stability;
- cable routing, strain relief, ventilation and service access;
- material, printer envelope, orientation and calibrated fits;
- electrical, thermal and acoustic tests where those are part of the product;
- delivery completeness and reproducibility.

Set numerical limits from the actual hardware and process. Do not import a clearance or wall-thickness number as a universal law.

## Engineer interfaces, cables and cooling

Read [mechanical-review.md](references/mechanical-review.md) for the general interface, cooling and print handoff review. Read [cable-aware-design.md](references/cable-aware-design.md) whenever the product has internal, concealed or user-accessible wiring.

Cable-aware design is mandatory for fit-critical wiring:

- inventory every endpoint and role (power, data, charging, signal or control);
- model the receptacle, plug body, latch, moulded grip and strain relief;
- model cable diameter or section, stiffness assumption, bend requirement and retained service loop;
- represent the centreline and occupied volume as a swept or segmented collision solid;
- add retention, protected edges, entry grommets and a reopening path;
- check static clearance, insertion, service removal, closure/pinch and cable-load paths;
- list intentional mating/contact overlaps separately from unintended collisions;
- export the envelopes with the review scene and show them in a diagnostic or section view.

For a concealed connector, establish which body passes through which opening, from which side, and when it is retained or terminated. A seated render cannot answer an assembly-path question. Model the socket, detachable plug and internal lead separately where applicable; use a close-up tied to the checked installation sequence to explain them.

Declare the cable's service boundary conditions: retained spans conserve available length; a released span may exchange jacket through an exit only with accessible slack and an explicit release/feed/restoration procedure. Keep failed retained-route evidence when adopting a different service method. Details are in [cable-aware-design.md](references/cable-aware-design.md).

A render spline is a visual aid, never the cable clearance proof. Mechanical clearance does not establish USB data, USB-C Power Delivery, polarity, grounding, wireless charging or hub compatibility; verify those independently.

Cooling must have a heat source, contact/interface, heat-transfer path, retention, airflow path, power method and service plan. Model the fan frame, bolt pattern, connector and moving envelope from the selected part. Do not claim that thick plastic or an aluminium-looking texture cools anything. Keep unknown fans, heatsinks and thermal pads labelled as envelopes until tested.

## Build, check, render, experiment

Use this loop and repeat it whenever a fit-critical source changes:

**build → export → validate → render → inspect → experiment → fix source → rebuild affected outputs**

Validation should check solid validity, connected-solid count, mesh closure/winding, positive volume, units and the named interference sets. Include printed parts, hardware envelopes, connector bodies, cable collision solids, service envelopes, fan rotors and relevant thermal parts. Report tolerances, intentional contacts and exclusions. Zero static overlap does not prove insertion access, bend life, load capacity or heat performance.

For multipart, adjustable or load-bearing products, read [engineering-validation.md](references/engineering-validation.md). Select the checks that could change the design or its release decision; a simple part does not automatically need finite-element analysis or a large parameter sweep. In particular:

- rehearse ordered insertion and removal against all parts installed at each step;
- test dimensional uncertainty, tolerance stacks and local fit sensitivity;
- assess loads and stability using the complete assembly and explicit material, contact and friction assumptions;
- distinguish sampled motion/cable feasibility from continuous motion and physical behavior;
- inspect actual slicer layers and support-removal access, then target uncertain interfaces with small coupons.

When maker feedback identifies a defect, turn it into a named, measurable acceptance criterion before reworking the part. Demonstrate that the check detects the preserved defective revision, then rerun it on the revised manufacturing geometry. Keep numerical digital criteria separate from operator cleanup, fit and strength gates; see the feedback-to-acceptance workflow in [engineering-validation.md](references/engineering-validation.md).

Preserve the preceding revision when an audit prompts corrections. Record the defect, source change, affected checks and remaining limits. Tie each result to its geometry revision and analysis inputs; regenerate affected evidence after changes without repeating unrelated checks. A completed audit may find a failure or an inconclusive result: retain that result and the next discriminating test rather than converting it to a pass.

Inspect the actual hero, front, side and rear views, adding underside, exploded, section and cable-diagnostic views when they reveal hidden construction. Check perspective, exposure, seams, thickness from multiple angles, exposed wires, floating supports, blocked vents, inaccessible fasteners and misleading textures. Never repair a geometric defect only in a render.

Review consequential lifecycle scenarios: installation, normal use, adjustment, unlocked or partially engaged states, foreseeable handling, wear and removal. Follow the complete user action, including payload support, release access and recovery. Evaluate coupled requirements in a representative assembly when separate feature checks cannot establish their interaction.

Distinguish evidence consistency from independence. CAD, renders and collision reports generated from one reference can share its error; hashes establish identity, not physical accuracy. Record which critical claims depend on a common assumption and which have independent measurements or physical observations. Prioritize an experiment that could change the architecture over further detailing when input uncertainty controls the decision. Apply the existing assembly, manufacturing and evidence gates at the affected feature instead of adding redundant checks.

For every high-risk unknown, write an experiment record with the question, smallest artifact, setup, measurement, decision rule and result. Use fit coupons for joints and connector clearances; mock-ups for insertion and service; bench tests for charging/data; and controlled thermal or acoustic tests for cooling. Coupons should reproduce the actual mating surfaces, print orientation and relevant support conditions; distinguish a size gauge from a representative joint test. Start with the smallest useful subset before committing to a full print. Update the ledger with what the evidence proves and what it does not.

## Maturity and exit criteria

Advance only when the current stage's evidence passes:

| Stage | Exit evidence |
|---|---|
| Concept | Agreed intent, architecture, requirements and known unknowns; concept images clearly labelled. |
| Packaging CAD | Editable source, named hardware/interface/cable volumes, plausible assembly and service sequence, reported collision results. |
| Prototype | Coupons or mock-ups print and fit the real interfaces; adjustments are measured and fed back into CAD. |
| Verified assembly | Representative electrical, thermal, mechanical and acoustic tests pass the defined criteria, with results recorded. |
| Fabrication release | No critical placeholders, per-part manufacturing files, printer/material/orientation notes, assembly instructions and revision record. |

If a requirement cannot yet be tested, keep it open and say exactly which real-world evidence is missing. Do not call a digital prototype physically validated or guarantee printability from watertightness alone.

## Final design presentation: interactive HTML review

Use a local interactive HTML review as the standard user-facing presentation for the final design handoff, unless the user requests another format. This convention also applies when the handoff is packaging CAD or a prototype: label the actual maturity prominently rather than implying fabrication release.

Read [html-design-review.md](references/html-design-review.md) when preparing this presentation. Deliver a portable `review.html` with a rotatable assembly, useful inspection controls, key dimensions, rendered views, evidence and remaining tests, and links to the engineering files. Include exploded views for multipart assemblies and component, clearance-envelope and cutaway controls where they help explain the product.

Generate the viewer geometry, dimensions and evidence from the same current CAD exports, parameters and validation results. Treat the HTML as the presentation layer, not a second geometry source. Inspect the page and exercise its controls before delivery; make it easy for the user to open from the final response and include it in the downloadable package.

## Fabrication and handoff

Confirm the actual printer, usable build area, nozzle, material, operator capability and adhesion/support practice for fabrication. Include brim, purge and support margin. Split or redesign a part that is too close to the bed limit; do not uniformly scale an enclosure and destroy its hardware fits. Earlier slicing may use an explicitly declared trial profile while actual equipment details remain unknown: inspect its layer output, label time/mass estimates and keep machine-ready output unreleased. A successful slice does not establish support removability, adhesion or physical fit.

Ordering from JLC3DP: read [jlc3dp.md](references/jlc3dp.md).

Deliver:

- editable parametric CAD and the real parameter input;
- separate printable parts in appropriate manufacturing formats and a rotatable assembly;
- the interactive HTML design review, its required local assets, and a representative preview image;
- cable connection inventory, collision envelopes, diagnostic/section view and collision report;
- purchased hardware list with sources, measured dimensions and unresolved substitutions;
- assembly order, fasteners/inserts, tools, service access and fit-coupon results;
- printer, material, orientation, support, adhesion and calibration notes;
- physical test record, limitations, revision and the next unresolved decision.

When engineering analyses were performed, include their inputs, units, load cases, material/contact assumptions, solver or slicer version, reproducible source and results. Identify digital passes, failures, inconclusive analyses and physical tests not run separately. Provide a short first-print/test sequence with the tools and measurements needed to close the remaining gates.

A 3MF may contain meshes or a slicer project; say which. G-code is machine/profile-specific and should not be presented as universal. Keep the decision ledger aligned with the files so another agent can resume without reconstructing the reasoning.
