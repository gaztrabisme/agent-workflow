# Interactive HTML design review

The standard final presentation is a portable local HTML review that lets the user understand the product, inspect its construction and find the files needed to make or test it. Name the entry point `review.html` unless the project already has an equivalent entry point. Adapt the presentation to the product; the headphone stand's colours, dimensions and component count are not universal defaults.

## Presentation structure

- **Identity and status:** product name, revision and actual maturity. State the design intent briefly and keep provisional fit or material assumptions visible near the model.
- **Interactive assembly:** make the rotatable model the primary content, with nearby controls and a compact dimensional summary. Use an assembled three-quarter view initially. Explain drag, zoom and reset controls in a small visible hint.
- **Design explanation:** describe the choices that matter to the user, such as silhouette, materials, load path, joints, replacement and service. Keep implementation details out of the product explanation.
- **Rendered views:** include the inspected hero, front, side and rear views; add underside, exploded or diagnostic views when they reveal construction. Caption what each view establishes and identify illustrative finishes or placeholder hardware.
- **Evidence and next steps:** distinguish checks that passed from tests not yet run. State the next measurement, coupon or physical test needed to advance maturity.
- **Handoff links:** link to the editable CAD and parameter input, per-part manufacturing files or their archive, assembly/print guide, validation report and test record. Explain which files are for review and which are for manufacture.

Use restrained typography, clear hierarchy, generous spacing and a palette that suits the product. On a wide viewport, a large model beside an inspection panel is a useful default; stack them on narrower screens. Scale the amount of text and the controls to the design's complexity.

## Inspection controls

Provide rotation, zoom, reset and useful view presets. Add controls according to the geometry available:

| Design feature | Useful control |
|---|---|
| Multiple assembled parts | An exploded-view slider and individual component visibility |
| Purchased hardware or fit-critical occupied space | Separate hardware and clearance-envelope toggles with a clear legend |
| Cables, connectors or service movement | Cable and service-volume overlays that can be inspected independently |
| Concealed joints or internal compartments | A cutaway/section control or visibility toggle that exposes the relevant construction |
| Adjustable mechanism | Angle controls reflecting actual limits, detents and unlock/lock operation |
| Audited assembly sequence | Step/play controls driven by the checked insertion paths and installed-part order |

Do not add inert controls or invent hidden geometry to fill the interface. Exploded offsets should make every component inspectable and may be illustrative; do not present the animation as a validated assembly path. Label an uncapped cutaway as such, so the rendering is not mistaken for an open or defective solid.

When presenting an audited sequence, show the current operation and any compliant fitting, hand support or access still requiring a trial. Use the same transforms and subassembly definitions as the audit. Animation is a presentation of that evidence, not a new collision or force test.

## Explain concealed connections and service

When a user questions how a cable or part gets through an opening, inspect the CAD and assembly evidence before defending the render. Show a close-up with outside/panel/inside roles, labels anchored to current geometry, and a short installation sequence. If the previous explanation was wrong, correct it plainly and fix the source where necessary. Transparency alone can make a seated connection look like a cable passing through a wall; distinguish the separate bodies and the opening explicitly.

Drive motion and prerequisite visibility from the audit. Show which covers and restraints must be released. Cable shapes checked at discrete poses should snap to those poses or have interpolation explicitly labeled unverified; a smooth animation adds no validation. Keep a failed retained route distinct from a passing released route and derive both counts from current results.

On narrow screens, collapse lengthy audit details while keeping the explanation, controls and a useful portion of the model visible. Do not let text panels hide the connection they explain.

## Keep the review faithful to the engineering

- Use named parts and assembly transforms from the current source. Preserve distinct classes for printed parts, purchased items, contact/clearance envelopes and service volumes.
- Populate dimensions, selected hardware, revision, validation results and maturity from current project data. Avoid hard-coded values that become stale when parameters change.
- After any revision that removes or renames a part, grep `cad/handoff.py`, `cad/viewer_template.html`, README, ledger, test record and order plan for the old part names and the old process words (PETG, Ender, cover, shim, splice) before rebuilding the review page. The viewer template hard-codes part names in its JavaScript (for example `m.name==='body'`), and the stale text surfaces only in the rendered page.
- Rebuild the affected viewer data and views after geometry changes. After an evidence-only update, refresh the labels and handoff package without claiming that physical validation advanced.
- Make diagnostic visibility and colours legible. Camera clipping, transparency, lighting and occlusion must not hide defects or suggest verified clearance where only an assumed envelope exists.
- A rendered wood texture, metallic shader or smooth surface is a finish intention unless supported by the manufacturing process and a sample. Keep these distinctions visible in captions or material notes.
- Show actual solver fields or slicer paths when discussing strength or printability, with units, assumptions and evidence scope. Preserve failures and inconclusive results alongside passes; distinguish proposed test targets from measured results.

## Portability and delivery

Prefer embedded model data and bundled scripts/assets so the review works locally without external CDNs, accounts or network access. Relative asset links are acceptable: include the complete folder in the archive and test the packaged arrangement. Keep a downloadable rotatable model and rendered views available as fallbacks.

Extend the project's working geometry/export pipeline rather than creating a parallel model for the page. The viewer implementation is flexible: use a suitable WebGL library, a lightweight viewer or an existing compatible component. A model plus an HTML presentation is the deliverable; no particular JavaScript framework is required.

If ordinary browser file-origin behavior requires a local server and the environment permits it, include a simple documented launch method and a durable local entry point. Do not use another server or surface to bypass an explicit access denial. A temporary localhost tab must not be the user's only way to revisit the design. If interactive viewing is unavailable, retain a useful HTML presentation with rendered views and a downloadable assembly, and state the interaction limitation.

## Presentation QA and final handoff

Open the actual generated page in a browser. Verify that the assembly loads with correct proportions, orientation and scale; inspect the initial composition and a narrower layout. Exercise the view presets, reset, exploded slider and applicable visibility/cutaway controls. Check that exploded parts remain in frame and that overlays can be distinguished from manufactured geometry.

Test state transitions, not only that buttons respond. “Complete assembly” or reset should restore normal parts, visibility, transforms, clipping and diagnostic modes after explosion, isolation and motion playback. Airflow intent should visibly identify inlet, fan direction, path and outlet; label it separately from computed flow or measured cooling.

Use a real browser/WebGL session when available, inspect screenshots and check page errors. Scope automation selectors to their actual panel or accessible role; adding another disclosure must not make a generic selector ambiguous. Before retrying a failed check, distinguish a test-harness defect from a product defect and inspect related selectors/state assumptions.

Check the images, captions, dimensions, evidence labels and download links against the current project. In particular, ensure the visible maturity matches the test record and that the packaged review retains its required assets. This is presentation QA, not a substitute for CAD validation or a physical experiment.

If browser QA is unavailable, check source syntax, model data, local links and control logic where possible, and inspect the exported renders directly. Record browser/GPU interaction as unverified; a mocked rendering test cannot establish visual correctness or usability. Check that the archive contains its required assets and clearly separates trial analysis files from released manufacturing output.

For a portable archive, extract it to a fresh location and load that copy with the documented launch method. Check model/images, local links, narrow layout and unexpected network dependencies. Verify final package hashes after the last edit; source-folder success alone does not establish archive portability. Keep historical reports labeled with their original geometry and distinguish them from current checks.

Make the review visible when the host application supports opening the finished artifact. In the final response, link the HTML review prominently alongside the downloadable design package, show a representative image when useful, and state any material test gate that remains open. The user should be able to explore the design without reconstructing its assembly from filenames.
