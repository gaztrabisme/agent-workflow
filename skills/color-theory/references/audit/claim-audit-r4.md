# Claim audit
Writer: glm (install wiring)
Auditor: glm (fresh session, did not write the line)
Round: 4

| # | File | Anchor | Claim | Verdict | Note |
|---|---|---|---|---|---|

No added line carries a course anchor, so the table is empty.

## Added sentences

`install-r4.diff` adds one line, at `SKILL.md:22`, in the section "When it fires, and when a sibling owns it":

> **`visual-design` instead:** composition, form and layout — the visual structure of a graphic, page or identity. This skill answers that artifact's colour decisions.

**Routing statement, not a course claim.** The sentence delegates composition, form and layout to the sibling skill `visual-design` and states this skill's remaining scope (the artifact's colour decisions). It carries no anchor of the form `1140 · U… · L… · HH:MM–HH:MM` (or 1560/5642 equivalents), names no lesson, unit or course, and asserts no method content. The em-dash definition "the visual structure of a graphic, page or identity" scopes the sibling's domain in the writer's own words; nothing in it is presented as the teacher's teaching. It parallels the existing sibling lines in the same list — `batch-photo-retouching` (`SKILL.md:19`), the interface-style and chart-type exclusions (`SKILL.md:20–21`) and `domestika-course-archive` (`SKILL.md:23`) — none of which cite the course either. Since no method claim is made, the grounding gate ("do not state a method claim without an anchor") is not engaged.

Findings: None.

Two non-claim observations, recorded for the maintainer; neither affects the verdict:

- Spelling: the line writes "colour" where the rest of the file, including the neighbouring scope sentences ("A color decision or color fact belongs here", `SKILL.md:25`), uses "color".
- The disambiguation note at `SKILL.md:25` summarises the siblings as photo fidelity and course packaging, with interface style and chart choice going to "whichever skill builds the deliverable". The newly added `visual-design` routing is now the one sibling category that note does not cover. The note was not modified by this diff, so this is a pre-existing summary lagging the new line, not a claim introduced by it.
