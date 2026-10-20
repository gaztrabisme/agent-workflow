# Engineering validation for physical assemblies

Use the sections that address a consequential unknown in the current product. This is a menu of evidence, not a requirement to run every simulation. Simple calculations or a small physical coupon may answer a question better than a detailed solver with uncertain inputs. Preserve the user's architecture unless evidence calls for a correction.

## Define the claim and its evidence

Before a check, record the question, geometry revision, inputs and provenance, method, acceptance criterion and exclusions. Distinguish measured values, manufacturer data, inferred properties and trial assumptions. Choose limits from the actual use case; another project's loads, clearance, sample count, material or safety factor are not defaults.

Record four distinct outcomes: digital check passed within its scope, failed, inconclusive, or physical test not run. Zero nominal collision, solver completion and successful slicing are different claims. Do not turn a simulation into a physical rating or a failed sensitivity case into an overall pass.

## Ordered assembly and service paths

An exploded view separates parts for inspection; it does not establish an assembly sequence.

- Define an ordered sequence of incoming parts or subassemblies, starting pose, insertion motion, seated pose and necessary access. Record any fixture, hand support or underside access required by that order.
- At each operation, check the incoming geometry against **all previously installed parts**, including devices, retainers and connected plugs. Checking only the mating pair misses keys trapped by neighboring structure.
- Test intermediate positions along the insertion path and relevant rotations. State sampling resolution, collision tolerance and excluded objects. A sampled path can miss a narrow obstruction; refine near critical features or use swept/continuous checks when the claim requires them.
- Preassembled groups need their own credible internal assembly order. Account for every required part and the timing of cable connection/routing.
- Classify intentional contacts by interface and purpose. Wedge overlap near seating is not permission for that pair to intersect anywhere along its travel. Rigid-path checks cannot establish snap deflection, elastomer insertion force or press-fit retention; keep those conditional unless modeled or measured.
- Check reverse removal, release motion, fingers/tools and cable slack. A clear rigid reverse path does not prove that a loaded wedge can be gripped or a compliant latch released.

Store each operation's installed-part membership as an immutable snapshot. Assert that incoming parts are not already installed and later parts have not leaked into earlier stages. Include accessories at their real installation step: a foot, clamp or shroud can obstruct an otherwise clear plug approach.

Where a failure mode matters, add a discriminating negative control, such as withdrawal while locked, unplugging with the obstructing cover fitted, or pushing an oversized complete plug through a socket mounting bore. Label the expected failure and preserve the collision witness. This demonstrates that the check detects that obstruction, not that every other motion is safe.

For moving assemblies, represent detents, stops, pin withdrawal and any temporary support of the payload. Evaluate intermediate poses as well as intended locked positions. State whether the evidence covers sampled configurations or the complete swept movement.

Check critical features directly in addition to generic mesh validity: a bore can erase its housing wall while leaving a valid solid, and a closed mesh can contain a blind recess that traps its key. Sections, remaining-wall measurements and local material probes can reveal these defects.

## Dimensional uncertainty and fit

An artist mesh or stand-inclusive product dimension is not a certificate of the bare device's contact geometry. Check scale and local proportions against measurements or dimensioned drawings, including protrusions and port locations. Preserve the uncertainty when only part of the geometry is known.

For consequential fits, vary plausible male oversize, hole undersize, positional error, material shrinkage and support/first-layer effects. Be explicit about total versus per-side or radial versus diametral clearance. Use worst-case stacks or a justified statistical model; arbitrary probabilities do not improve uncertain inputs.

Perturb the device envelope and inspect the actual interfaces, not only its bounding box. Uniform scaling is a useful sensitivity trial but cannot represent independent local shape errors. If plausible variation produces collision or loss of retention, leave final fit open and identify the specific measurement or local correction needed. Do not scale all printed parts to compensate for one joint.

For soft pads, distinguish nominal gap, preload, compression strain and pressure. Geometry alone does not supply an elastomer stress–strain law or friction coefficient. Test both excess compression and lost contact; a pad that fits visually may neither protect nor retain the device.

## Loads, locks and structural simulation

Begin with a free-body/load-path model and simple section calculations. Include payload weight and lever arms, adjustment forces, cable pull, locking torque and relevant handling or proof loads. Document why each load is chosen and which members or interfaces carry it. Shear, bearing, bending, net section and retention may control different features.

Use finite-element analysis when it can resolve a design decision. For an analysis claim:

- Mesh the current manufacturing geometry. State units, element formulation, material law and whether infill, layer orientation, contacts and supports are represented or idealized.
- Use data for the exact material variant where possible. Bulk or vendor test data does not automatically describe a printed part. A flexural modulus used as an elastic proxy is an assumption, not a calibrated tensile/orthotropic law.
- Apply traceable forces, moments and constraints. A fully fixed face may be much stiffer than an actual washer, joint or sliding contact; explain the consequence or examine a less favorable boundary case. A local member model does not qualify the whole assembly.
- Verify solver setup with an appropriate known benchmark and force/reaction balance. Where force couples matter, check the applied/resultant moment too.
- Refine the mesh and compare the outputs that govern the decision. Converged displacement does not imply converged peak stress. Investigate singularities and load/constraint artifacts rather than hiding them with an averaged stress plot. Retain an unconverged outcome as inconclusive.
- Distinguish stiffness, stress and failure criteria. Isotropic von Mises stress is only a proxy for anisotropic prints; linear elasticity does not establish creep, layer failure, fatigue, snap force or nonlinear contact retention.

Render actual computed fields with units and legends. Label any deformation magnification. Preserve enough geometry, load definitions, mesh/settings and field data to reproduce the result. If inputs dominate uncertainty, prioritize material/contact coupons over increasingly elaborate simulation.

## Complete-assembly stability

Include fixed and moving printed parts, payload, hardware, pads and any ballast. Estimate mass and centre of gravity per part at each relevant pose. For sliced parts, separate object extrusion from supports/brims; do not count discarded support as stabilizing mass. A CAD solid centroid is only a proxy for nonuniform infill, so label it or improve the estimate.

Sweep consequential mass, CG, pose and load uncertainties. Compare overturning moments about the actual support polygon and sliding force using an explicit friction assumption. Include force application height and direction, controls pressed by the user, adjustment loads and cable forces where relevant. A broad base does not guarantee stability, and a tipping pass does not establish resistance to sliding. Report the controlling scenario and sensitivity to unmeasured friction; static calculations do not qualify impact or snags.

For moving cable geometry and external anchors, use [cable-aware-design.md](cable-aware-design.md). Do not silently infer cable tension from a geometrically feasible route.

## Slicer evidence and smallest useful prototypes

Slice current, individually oriented manufacturing parts with a named and recorded profile. A provisional profile may support a geometry/process trial; it does not authorize machine-ready G-code. Record nozzle, layer settings, perimeters/infill, support strategy and material assumptions. Soft contact parts need a separate elastomer process, not the rigid body's profile.

Review every printed part, including small keys, caps and trays, rather than inspecting only the hero shell. For consequential orientation choices, compare support access, bearing surfaces, layer direction and bed contact; a large exhaustive orientation sweep is optional. Verify bed margins from actual extrusion including bead width, support and brim when available. Inspect regenerated layers after local cable-clearance cuts, especially thin roof strips and isolated rail fragments.

Inspect actual extrusion layers at bearing roofs, blind sockets, channels, narrow ligaments and other critical features. Trace how support is reached and removed before assembly; successful slicing alone can leave trapped support or an undersized mating surface after cleanup. Separate supports, bridges and product extrusion in evidence views. Revisit orientation or split where cleanup is implausible.

Create a small first-print sequence:

1. Size gauges establish the local printer/material clearance range.
2. Cropped joint/feature coupons reproduce mating surfaces, orientation, bridge/support conditions and extraction access.
3. Contact mock-ups fit the real device, pads and connectors.
4. Mechanism prototypes with representative dummy payloads test retention, deflection, drift, wear, cable movement and stability before using valuable hardware.

For a panel connector, pair a clearance gauge with a crop of the actual mounting panel when they answer different questions. Preserve anti-rotation flats, thickness, washer/nut bearing and parent print orientation. Record nominal versus total/per-side allowances. Check hand insertion, rotation, seating, removal and repeat cycles; use the oversized plug as a negative fit control where appropriate. Do not force the fitting into compliance by tightening the nut or silently filing the first test.

Explain what a cropped coupon omits, such as full-part stiffness or support height. Pair each test with measurement tools, loading/setup, a decision rule and a recorded result. Calipers, scales, measured weights/lever arms and a force gauge often close gaps a solver cannot; specify a dial indicator or other instrument only when the required resolution warrants it. Distinguish proposed targets from completed tests and from published standards.

## Maker feedback becomes acceptance criteria

A maker's slicer screenshot is evidence of a concern, not evidence that a physical print failed. Preserve the message, candidate file/revision and printer/profile identity when available. Map each concern to a named part and feature. If the pictured filename and message disagree, inspect both plausible parts and retain that uncertainty.

Before redesign, record each affected feature's defect, location, measurement, process-dependent threshold and rationale, baseline result, revised result, geometry/orientation/profile identity, remaining physical gate and smallest discriminating test. Screen the rest of the printed inventory for the same failure class. Solid validity, successful slicing and clear assembly do not substitute for manufacturing criteria.

Use the preceding geometry as a negative control. A check intended to catch the reported defect must flag that defect before its revised result is used as evidence. Store measured values and an annotated view, not only a pass count. If the concern cannot be reproduced, keep it unresolved and obtain the relevant file/profile rather than adjusting a threshold to produce a pass.

Choose measurements that expose the mechanism:

- **Bed seating:** identify the intended bearing plane, its coplanar area and disconnected contact regions, and its distance from the lowest protrusion in the proposed manufacturing pose. Distinguish a hypothetical flipped baseline from an actually exported revised orientation. Brim and generated support do not make an elevated broad face sit on the bed.
- **Fragile features:** measure finished Boolean geometry at the named web, root or rail; primitive dimensions can hide a sliver left by a clearance cut. Record thickness, unsupported span and structural connection at meaningful sections, with coverage limits. Geometry alone does not establish layer strength or handling force.
- **Layer formation:** inspect actual first object extrusion and feature-start layers, including small islands. A filter selecting only substantial layers can omit the fragile feature being investigated. Separate object paths from brim/support and connect each view to the measured feature.
- **Cleanup:** trace tool access and support extraction in the as-printed state. Uncertain removal without damage stays a physical gate; an open cavity is not automatically cleanable.

When a split removes a printing obstruction, engineer the new joint: location, retention, tolerance, root and fastener ligaments, screw-tip extent, tool approach, assembly/removal order and load path. Preserve the required external form and service access. Rerun collision and assembly checks with new parts present at their real installation stages. Do not replace a difficult print with an inaccessible or fragile joint.

Inspect the meaning of intentional-contact exemptions after joint changes. A screw pilot may deliberately overlap a simplified thread envelope; a flat screw head bearing on a roof does not justify burying the head inside a rib. Limit exemptions to the actual interface and pose, and check the entire fastener/tool approach through lower rails and ledges, not just the seated hardware.

Test artifacts must preserve the cause of the concern. A long thin rail needs its relevant full span/root and parent orientation; a two-anchor seat needs both anchors if rocking or spacing governs. Explain when a coupon omits full-part warping, stiffness, support height or load. Keep full-shell fabrication conditional until operator cleanup and fit results are recorded; corrected geometry is a revised candidate, not physical qualification.

## Efficient checks without weakening their claims

Use bounding-box rejection and cached geometry before expensive solid intersections. Skip a declared contact only within its allowed interface/pose range. For repeated motion checks, a conservative proxy may replace complex purchased CAD if containment of the exact geometry is independently checked and the approximation is recorded. A clear conservative proxy supports clearance; a proxy collision may be a false positive and needs refinement before claiming an actual interference.

A negative control that asks whether a path is blocked may stop at its first verified collision. Record the witness, actually evaluated poses and unevaluated remainder; do not claim a complete sweep or the earliest collision along the path. Positive path checks must cover their declared samples. Keep simplification, collision thresholds and sampling limits visible in the report.

For long pipelines, freeze the geometry/input identity before parallel read-only checks and keep a single writer for each output. Preserve failed attempts. Resume completed operations only when geometry, inputs, relevant analysis semantics, membership and motion signatures agree; changed cases must run again. Capture checkpoints before reuse, verify hashes and completeness, and distinguish a staged/resumed run from an uninterrupted rebuild. Never attach new source hashes to old results without establishing their applicability.

## Corrections and reproducibility

Preserve the preceding revision and failed evidence. Fix the authoritative source, regenerate affected exports, analyses, slices and renders, and ensure the review uses that same revision. Record which results were invalidated; do not keep a strength or mass claim attached to geometry that changed afterward.

Keep analysis inputs, tool versions, assumptions, thresholds, excluded contacts and outcomes with the handoff. Revision IDs or hashes can prevent stale-file mistakes in larger pipelines. Separate canonical CAD, posed review meshes and oriented manufacturing files. Exclude unreleased trial G-code from the print handoff, and keep a clear next-test sequence when real fit or strength remains open.

When you report a study's result, say whether you ran it or only read its report. Before rerunning a script you did not write, copy its output files (2026-10-18: a script that did not parse `--help` treated it as a normal run and overwrote its saved results).
