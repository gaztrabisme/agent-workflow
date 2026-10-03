# Mechanical review and print handoff

Read the sections relevant to the current assembly. These are engineering questions to resolve, not a mandatory approval ceremony.

## Interfaces and assembly

Model the actual contact surfaces, padding, fastener heads, threaded engagement, inserts and tool approach. Account for moving parts and pinch points. Check the path a rigid device and its plugs take during installation and removal, not only the final pose. Explain assembly order; if no order works, change the split or retention.

For multipart or adjustable mechanisms, use [engineering-validation.md](engineering-validation.md) for ordered checks against all installed parts, tolerance sensitivity, load/locking analysis and complete-assembly stability. A plausible sequence, a sampled collision check and demonstrated hand assembly are distinct levels of evidence.

For tabletop objects, consider centre of mass, footprint, non-slip feet, screen touches and cable pull. Keep fragile ports out of the structural load path. Calibrate clearance, insert bores and snap features with the selected material and orientation; nominal CAD dimensions alone do not establish a working fit.

A reference intersection threshold used in another project is not a general acceptance standard. Exclude intentional contact/interference explicitly and test relevant purchased-part envelopes as well as printed parts.

## Cable and electrical packaging

For each connection record endpoints, power/data role, selected or provisional connector, exit direction, cable diameter, bend requirement, service loop and retention. Include separate power supplies when the hardware needs them. Check the complete route through panel openings and around moving/removable parts with real connector dimensions.

Use a conservative swept envelope where practical; otherwise document the route as unverified and request a physical routing check. Curves can overshoot their control points. Inspect actual generated paths and their envelope instead of assuming a neat spline stays inside the shell.

Do not promise simultaneous charging and USB data, or wireless charging, from appearance alone. Confirm device/hub compatibility independently. For a wireless design consider coil alignment, gap, heat and metal placement; a charging puck behind arbitrary aluminium is not a resolved design.

## Cooling integration

Identify the heat source, contact interface, thermal path and expected duty. Keep device surfaces protected and establish allowable contact pressure. A heatsink needs retention in every relevant direction, including during service. Fan mounting pitch, connector and airflow direction must come from the selected part.

Provide inlet/outlet paths and assess obstructions and recirculation. Preserve existing equipment vents. Specify how a thermal prototype will be observed under representative use and what temperature limits are sourced from actual components/materials. Material heat-deflection data is not a universal continuous-service limit.

Distinguish a cooling illustration, geometric aperture/obstruction screening, CFD and a powered thermal test. Arrows or open vents do not establish airflow rate, pressure loss, recirculation or temperature reduction. Use the least elaborate method that answers the unresolved question and state what remains unknown.

## Printing and finishing

Check each oriented part against usable build volume including brim/supports. For example, a 216 mm part centred on a 220 mm bed leaves just 2 mm each side; it may need a revised outline or split. This example is arithmetic, not a universal machine specification.

Balance visible surface quality against layer-direction strength, unsupported ceilings, bridging, support-removal access and bed-contact marks. Avoid burying supports where they cannot be removed. Preserve the agreed look through deliberate seam placement, texture and orientation rather than excess infill alone.

Inspect actual slicer layers at critical interfaces and make local feature coupons where bridging, support scars or extraction access remain uncertain. A watertight STL and a completed slice do not establish a usable bore, removable support or a working joint. Record trial-profile assumptions separately from a confirmed machine process.

Select filament after learning the printer's temperature limits, nozzle, enclosure and operator experience. Standard PETG can suit functional indoor housings, but matte blends, PLA, ASA and reinforced polymers have different properties and process needs. Consult the exact product data; do not assume all variants print alike or that cost predicts suitability. Recommend drying and storage according to that product's guidance.

## Handoff content

A useful handoff identifies:
- Part names, quantities, units and revision; editable source and separate STL/3MF or other suitable manufacturing exports.
- Printer, nozzle and material/profile used for any slicing; orientation, supports, adhesion and critical fit settings.
- Purchased hardware and provisional items; assembly order, fasteners, tools and access.
- Checks actually passed, exclusions, fit coupon and physical tests remaining.

A 3MF may contain meshes only or a slicer project: say which. G-code is machine/profile-specific. Do not present an assembly STEP, GLB or Blender scene as a single printable component. Estimated filament/time must come from the actual slice and be labelled estimates. Deliver the portable model and notes when the printer operator will do the slicing.
