# Cable-aware design

Use this reference whenever a physical product contains internal, concealed or user-accessible wiring. It turns “hide the cables” into a modelled, checkable design task.

## Build a connection inventory

Record one row per connection:

| Field | What to capture |
|---|---|
| Endpoint A / B | Device, board, power supply or removable panel |
| Role | Power, data, signal, charging or control |
| Connector | Standard and exact plug/receptacle where known |
| Evidence | Measured, manufacturer-specified, inferred or placeholder; source and date |
| Plug envelope | Body, latch, shell, moulded grip and strain relief |
| Cable envelope | Outside diameter or width/height, stiffness and shielding if relevant |
| Route | Ordered 3D points or centreline through the assembly |
| Bend requirement | Manufacturer minimum radius or a clearly labelled provisional radius |
| Service loop | Slack needed to remove the device or panel without unplugging |
| Retention | Clip, channel, tie, grommet or friction feature |
| Intentional contacts | Mating face, entry slot or compliant pad that may overlap by design |

Do not infer a cable's bend radius from a neat spline. If the cable or plug is unknown, create a conservative labelled envelope and keep the design provisional.

## Resolve the connector interface before cutting its opening

Distinguish a cable passing through a wall from a panel-mounted receptacle with a detachable external plug and separate internal leads. Name the parts and specify the actual installation side; never assume every panel jack installs from the same side. Check the largest body that must traverse each opening, including preterminated ends. If no assembly order works, use a plug-sized passage, open slot/split grommet, removable panel or a different interface.

For selected hardware, reconcile the exact mating pair's dimensioned drawings and supplier CAD: panel thickness range, cutout and anti-rotation flats, flange seat, washer/nut stack, thread engagement, insertion depth, grip, molded relief and exit tangent. Record local datums and transforms. A thread cylinder proves neither tightening nor retention, and a supplier maximum mounting torque is not a qualified target for a printed panel.

Purchased assemblies may include loose nuts, uncompressed spring washers or sample cable stubs. Preserve the source and explicitly document installed-state adjustments or exclusions; do not retain a straight supplier stub on top of a routed cable. Model terminal branches, insulation and strain relief when space-critical. An aggregate lead reaching a terminal envelope leaves solder/crimp access and insulation clearance unresolved. Plan termination before surrounding hardware obstructs access.

Record sourcing separately from dimensional authority: exact SKU, source/date, selected versus purchased/received, and local stock versus an importer serving the user's country. Supplier CAD does not establish received-part dimensions or electrical compatibility.

## Model the volume, not only the line

Create separate CAD solids for connector clearance and the cable body. A swept cylinder, swept rectangular section, or a union of rounded segment envelopes can be appropriate; choose a section that matches the cable and document the approximation. Include the moulded strain relief and the direction in which a plug is inserted or withdrawn.

Keep these envelopes as named review objects alongside purchased-component envelopes. They may be excluded from the printable-part export, but they must remain available to the collision and service review. Render them in a diagnostic view or section with a distinct material so the reviewer can see the actual occupied volume.

## Check routes in stages

1. **Static clearance:** cable and connector envelopes do not intersect walls, fasteners, heat sinks, fan rotors or other cables except for listed intentional contacts.
2. **Insertion path:** the rigid plug and device can reach the final pose without passing through the shell or another component.
3. **Service path:** a panel, phone, drive or board can be removed far enough to unplug or inspect it, with the service loop represented.
4. **Load path:** cable pull, connector side load and repeated bending do not rely on a fragile printed port or sharp edge; add strain relief where needed.
5. **Closure path:** covers and panels can close without pinching, crushing or scraping the cable.

Report the tolerance and collision set for each check. Static clearance is evidence about the final pose only; it does not prove bend life, insertion access or electrical compatibility.

## Adjustable products and moving endpoints

Separate cable segments retained to the moving assembly from the free span to a fixed host or strain-relief anchor. Record the anchor coordinates and endpoint tangents where constrained; do not use an arbitrary free-tail length as a universal minimum. If the actual anchor or cable is unknown, label a trial arrangement and keep the real routing gate open.

Check the combined range of all relevant axes, including intermediate movement and service positions. For a span held between retained anchors, keep the same available free length across poses: independently drawing a longer curve at each pose can conceal a taut cable. Use endpoint separation as a necessary lower bound, then account for bend radius, strain relief, routing and useful slack.

Evaluate curvature along the actual generated centreline and collisions using its occupied cross-section. State sampling resolution and any clearance reserve; check tight regions more finely. Include other cables, self-contact, pinch locations and the surrounding workspace when relevant. Independent collision-free pose curves do not prove a continuous transition between them.

A fixed-length curve with acceptable sampled bend radius establishes geometric feasibility only. It does not solve cable stiffness, gravity, friction, tension, connector side load or fatigue. Use a suitable mechanical cable model or a physical motion trial for those claims. Feed measured or bounded cable forces into the assembly's load and stability checks, and identify any untested force assumption.

## Released cable service and feed through exits

If a retained route fails, preserve the failure and evaluate a specific alternative. Releasing a tie changes the boundary conditions; it is not a correction to the failed fixed-length result. For a released route:

- State which covers, ties and external clamps are removed, in what order, and how they are reached before pulling the plug.
- Account for jacket length exchanged through the exit at each pose and the external slack reservoir that supplies or receives it. A long stock cable is not proof of accessible slack. Derive the required slack from the chosen route, with a justified handling allowance; do not reuse another project's value.
- Require a reusable retainer or an explicit cut-and-replace procedure. Restore retention and external strain relief without connector preload.
- Check the released cable against neighboring cables, structures, itself and the grommet; keep only genuinely removed parts out of that collision set. Check closure again after restoring the route.
- Separate modeled occupied length from the complete stock lead; document where unused length stays and how supply terminations are protected from pull.

A service passage can be derived from the union of sampled cable/plug envelopes plus declared clearance. Record corridor-generation pitch separately from collision-check pitch. Reinspect remaining walls, disconnected slivers, supports and load paths after cutting it. Feed friction, handling, stiffness and wear remain physical questions unless actually modeled.

## Route cleanly and serviceably

Prefer short, deliberate routes with smooth direction changes, protected edges and a retained slack pocket near removable parts. Place exits on the hidden face that best matches the real connector direction. Separate power and data when heat, noise or service access makes that useful. Keep mains wiring, low-voltage wiring and removable external leads identifiable in the assembly notes.

Design the reopening strategy with the route: removable covers, access panels, clips, grommets and pull features should let a maker reach the connector without dismantling unrelated structure. A decorative tab is not a latch until its engagement, release and load are modelled.

## Electrical and visual boundaries

Mechanical cable clearance does not establish USB data, USB-C Power Delivery, charging, grounding, polarity or hub compatibility. Verify those independently and record the result beside the mechanical route. Likewise, a textured cable in a beauty render is not manufacturing geometry; the exported cable collision mesh and the reviewed section are the evidence.

## Handoff

Deliver the connection inventory, cable-envelope objects, diagnostic/section view, collision report, intentional-contact list and unresolved measurements with the editable CAD. When a cable is replaced, update its envelope and rerun the affected checks before revising the printable parts.
