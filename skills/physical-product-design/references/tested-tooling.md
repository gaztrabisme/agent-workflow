# Tested tooling for physical-product engineering

This stack was exercised during a local macOS product audit in September 2026. It produced parametric CAD, collision and assembly-path checks, numerical studies, local structural FEA, actual slices, renders and a portable review. Physical tests were not performed, and browser/GPU interaction QA was unavailable. Those limits are part of the record.

Use this as a practical starting point when the project lacks a working pipeline. Equivalent tools are acceptable. Do not install the entire stack for a simple part, freeze future projects to these versions or assume applications remain available at the original machine's paths. Versions below are observed historical versions, not claims about the latest releases or universal compatibility.

## Roles and demonstrated capabilities

| Tool | Observed version | Role exercised | Boundary to preserve |
|---|---|---|---|
| Python | 3.11 environment | Orchestrated CAD generation, calculations, exports and reports | Project scripts implement the workflow; Python alone supplies no engineering model |
| CadQuery | 2.8.0 | Editable solids, STEP import/export, boolean interference, point/distance checks, assembly transforms and cropped coupons | Solid validity does not prove minimum wall, insertion access or a printable fit |
| trimesh | 5.1.0 | Reimported mesh closure/winding, volume, component counts, bounds and review geometry | Mesh checks do not certify the accuracy of an artist reference or physical contact |
| NumPy / SciPy | 2.4.6 / 1.17.1 | Transformations, mass/CG and tolerance sweeps, constrained cable-curve optimization | Geometric feasibility is not cable-force equilibrium; optimizer success needs independent constraint checks |
| Gmsh | 4.15.2 | Tetrahedral meshing of current STEP solids at successive mesh sizes | A generated mesh still needs domain, element-quality and refinement checks |
| scikit-fem | 12.0.2 | Scripted linear-elastic solid analysis with a benchmark, loads, constraints and reaction checks | The exercised model was local, isotropic and linear; it did not solve printed-layer failure, nonlinear contact or creep |
| meshio | 5.3.5 | Mesh transfer and VTU field export between meshing, solving and inspection | Preserve node indexing, connectivity, coordinate units and field association when converting |
| PrusaSlicer CLI | 2.9.6 | Sliced individually oriented rigid parts using a recorded trial profile; generated layer, time and extrusion evidence | Slicing success is not print qualification; trial G-code was not released to the printer |
| Blender | 5.2.1 | Background rendering of actual exported geometry, reference-model placement and assembled GLB | Appearance is presentation evidence; textures and smooth shading do not establish material properties or fit |
| Matplotlib | 3.11.2 | Plotted actual FEA fields, mesh refinement, sensitivity results, cable routes and parsed extrusion paths | Plot source data and units; label deformed geometry magnification and analysis assumptions |
| HTML / WebGL | Custom local viewer | Embedded CAD meshes, part visibility, pose controls, sections and assembly-sequence presentation | Viewer was authored; browser/GPU behavior was not verified in this audit |
| Node.js | Version not recorded in the audit | Executed viewer syntax/data/control checks with mocked WebGL | A mocked graphics context checks logic, not rendering, layout or usability |

`uv pip` was used to add missing Python packages to the project's existing virtual environment. A local PrusaSlicer application bundle was used without a system-wide installation. These are environment-management options, not skill prerequisites. FreeCAD/CalculiX were not the solver used in this audit; do not attribute its results to them.

## Select and verify the environment

Inspect the existing project scripts, environment and executable paths first. Reuse a working CAD/export pipeline. Verify imports and relevant executable entry points before promising a capability; distinguish a callable CLI from a merely installed GUI application.

Capture Python/package versions and Blender/slicer versions in the project evidence. Record Node.js and browser versions when review execution is tested. Use a project environment and dependency record so another machine can reproduce the work without inheriting the original user's global setup. Keep executable paths configurable rather than embedding personal home-directory paths in reusable code.

When reproducing an old artifact, start from its recorded versions and profile. When adopting newer tools or a different platform, exercise the relevant export, solver benchmark or slice before trusting compatibility. Retrieve current API/install instructions from official documentation as needed; this reference is not a copied installation manual.

## Data flow and handoff contracts

The exercised pipeline was:

**parameters → CadQuery solids → canonical STEP / oriented STL / posed review meshes → analyses and slicing → data-driven plots, Blender renders and HTML review**

Keep the following contracts explicit:

- **Geometry:** canonical CAD coordinates, part names, units and assembly transforms remain authoritative. Manufacturing STL is oriented for printing; review geometry is posed for inspection. STL does not encode a reliable unit convention, so declare millimetres. Convert deliberately when producing metre-based GLB scenes and check bounds after import/export.
- **Assembly and motion:** custom scripts apply the same transforms to solids used in the viewer. CadQuery boolean/distance queries and sampled motions supply the check; an exploded animation alone does not. Record intentional contacts and sampling limits in structured results.
- **FEA:** STEP is meshed with Gmsh, connectivity is transferred using meshio, and scikit-fem applies the explicit material, loads and constraints. Preserve the mapping from mesh nodes/elements to displacement and stress fields. Export results such as VTU plus structured summaries so plots can be regenerated. The solver setup requires engineering code and verification; it is not an automatic strength certificate.
- **Slicing:** PrusaSlicer receives the manufacturing STL and an explicit profile. Preserve profile settings and slicer version. Keep product extrusion separate from support/brim when estimating assembly mass. If parsing G-code, honor absolute/relative extrusion modes, retractions and extrusion roles; a parser written for one profile's output is not automatically valid for another.
- **Presentation:** Blender and the HTML viewer consume the same current exports. Matplotlib consumes computed result files and actual toolpaths. Derive captions, dimensions and status from those results to avoid a second manually maintained engineering model.

Store geometry revision or hashes, parameters, source scripts, environment/profile records, analysis inputs and relevant result fields together. Bundle the review's local assets. Keep diagnostic G-code separate from released printer output; even a file lacking a complete startup routine may contain heater or motion commands.

## Purchased CAD and mesh-export pitfalls

A valid supplier assembly can contain touching material shells that become non-manifold if every coincident vertex is welded together. Inspect source solid structure before treating this as a printable-part defect. Where appropriate, tessellate and validate shells separately in source coordinates, apply only a documented small seam tolerance within each shell, then transform with adequate precision and preserve separate shell topology. Recheck bounds, volume and closure. Do not repair fit-critical geometry by indiscriminate welding or hole filling. Purchased multi-solid assemblies and connected printed parts have different validation expectations.

A later September 2026 dock audit exercised real Chromium/WebGL interaction checks, panel-connector supplier STEP imports, released cable-feed poses and extracted offline-package checks. This extends the earlier tooling example; it does not retroactively turn its mocked-browser checks into real-browser evidence. No physical fit, powered cooling test or CFD was performed in that later audit.

## Choose the next tool by the unresolved question

- Use CAD sections, boolean checks and small feature probes for geometric defects; more FEA will not fix an erased wall or trapped insertion path.
- Use simple free-body and section calculations before adding a solver. Use the FEA stack when deformation or stress distribution could change a design decision, following [engineering-validation.md](engineering-validation.md).
- Use constrained geometry for moving-cable candidates, then a suitable cable-mechanics model or a real routing trial for tension and fatigue claims. Follow [cable-aware-design.md](cable-aware-design.md).
- Use actual slicer layers and local coupons for bridges, supports and fit. A rendering tool cannot establish support-removal access after printing.
- Use a real browser for final interaction QA when available and permitted. If blocked, retain static/logic checks and rendered fallbacks, with browser/GPU verification explicitly open; follow [html-design-review.md](html-design-review.md).

The remaining physical toolkit depends on the decision: calipers/rulers for interfaces, a scale for mass, actual connectors/cables, a printer and representative materials, measured weights/lever arms or a force gauge for loads, and a dial indicator when displacement resolution warrants it. These bench tools were proposed for the next stage, not used or remotely verified in the digital audit. Additional software does not replace their measurements.
