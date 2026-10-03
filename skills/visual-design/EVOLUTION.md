# Evolution

## Evolution 1

- **Classification:** distilled from a paid course.
- **Source:** course 5642, *Specialization in Graphic Design and Visual Communication*, units 2 and 4–7; structured notes at notes/U02.md and notes/U04.md through notes/U07.md.
- **Grounded:** read skill-builder's authoring playbook and templates, the color-theory skill and its method references, owner decisions 2–7 and 16, and render-kit's AGENTS.md. Reused the course-skill structure, anchor discipline, staged flow, code-first then fresh-context vision review, and render-kit output contract.
- **Method:** seven derived stages synthesize the lesson methods into brief, concept, form, composition, type/system, medium/variants and review.
- **Measurement:** T1–T12 each name the course method, a tool-independent measure or vision question, a default and whether that default is from the course or chosen by this skill.
- **Checks script:** `scripts/checks.py` (`grid`, `balance`, `space`, `scale`, `focal`) with good and bad samples; 16 unit tests pass.
- **Claim audit:** round 1 (Claude and GLM, independent of the Codex writer) found 39 of 343 citations not supported (19 overstated, 19 unsupported, 1 derived but unlabelled). Codex fixed them; round 2 (GLM) re-audited 53 pairs, all supported; round 3 (GLM) checked the dogfood fixes. Final table: 334 of 334 supported.
- **Dogfood:** a fresh Codex session composed the day-10 slide of a fictional drilling report, critiqued v1 through the review checklist and revised it; both versions pass `rk check`. Independent Claude vision review of v2: 13 yes, 0 no; `rk brief --verify` exits 0. Evidence: `lab/design-programme/dogfood/run-2/visual/`.
- **Dogfood findings folded in (labelled derived):** a content-verification step before concept and layout for fact-dense reports (High); `scale` compares unique declared levels; a panel example for the negative-space estimate; `VD-T` prefixes beside color-theory's tests; T11 not applicable without variants.
- **Science crosswalk:** not applicable as a separate library; this skill covers form and composition. Colour decisions are disambiguated to color-theory.
- **Validation still required:** validate the distilled claims against real use; test the planned checks.py subcommands from render-kit renders; run a fresh-context vision review; fold findings into the method; recheck source anchors and the Agent Skills spec.
- **Verdict:** PENDING — one dogfood pass; it earns KEEP after a second real use.
