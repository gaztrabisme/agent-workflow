Derived from skill-builder dogfood 2026-10-01; this procedure turns the authoring checklist into a repeatable critique of an existing skill.

# Review or refine an existing skill

Use this procedure when the requested work is to critique a skill package, repair its structure, or decide whether a proposed refinement is sound. For a direct, small edit, use the relevant checklist steps and the same validation gates without writing a full review.

## 1. Fix the review boundary

Read the approved proposal and rule destinations when they exist. Record the target artifact, audience, trigger, dependencies, and all routed rules. Treat dropped rules and rules routed to other skills as out of scope. If there is no proposal, record the target's current stated scope and label it as unapproved rather than inferring approval.

Read the target's `SKILL.md`, every shipped reference and script, its evolution record, the shared kernel, and each sibling it names. Note missing siblings and sources that cannot be checked. Keep prior output closed until the reviewer has produced their own result.

Write a short scope and grounding record before judging the package. Use `templates/refine-review-report.md` for the review artifact.

## 2. Turn the build checklist into review checks

Use the table to check the same decisions the authoring checklist asks a builder to make. Record evidence and the artifact that answers each check. A checker can prove only the condition named in its row; a green tool result is not a substitute for the manual review.

| Build check | Review question | Evidence to record | Mechanized check |
|---|---|---|---|
| 1. Decide it should exist | Does the package own a recurring competency with a distinct trigger and audience, or is it a one-off/duplicate/reference need? | Scope decision and sibling comparison | Stage B routing checker when available; otherwise compare the approved destination rows manually |
| 2. Ground in what exists | Do sources, core conventions, and named sibling boundaries support the current instructions? Do relative sibling pointers resolve? | Grounding note; unresolved inputs listed | `scripts/check_refs.py` checks local links and warns on absent sibling targets; source fidelity still needs human review |
| 3. Trigger contract | Would the description retrieve the skill for its intended task and exclude neighboring skills? | Compare frontmatter descriptions and name the artifact/audience boundary | `scripts/check_refs.py --format` checks metadata shape; sibling overlap is a manual check |
| 4. Operating-manual shape | Does `SKILL.md` have the expected sections, and are all shipped references, scripts, and tests named from it? | Package inventory and section comparison | `scripts/check_refs.py --skeleton <path>` checks headings, paths, and named-versus-shipped files |
| 5. Gates | Does each gate name an actionable check and point to a definition that exists? Is copied shared-gate prose being passed off as local procedure? | Gate table with linked definition and observed result | Local-link checks can find broken paths; compare canonical gate text manually |
| 6. Dogfood | Can a fresh reviewer use the skill on a real task and produce the promised artifact? Are limitations honestly recorded? | Dogfood evidence and ranked findings | Stage B dogfood checker when available; otherwise inspect the evidence and closure notes |
| 7. Wiring | Do hand-offs, cross-links, and return paths match the skill's scope? Are listed references useful rather than orphaned? | Link/hand-off review | `scripts/check_refs.py` checks internal links and named package files; assess ownership manually |
| 8. Ship and record | Are package checks, tests, license/privacy handling, format validation, and evolution entry accounted for? | Check-results table and `PENDING` evolution entry | `scripts/check_refs.py --format`, target tests, `scripts/scrub_check.py` when publishing, and `skills-ref validate`; Stage B checkers are external |

For distilled skills, also audit the method claims against their source anchors and factual library. Use the course playbook's claim-audit and render/check steps; the general review table does not replace those specialized checks.

## 3. Inspect the package and references

Run `scripts/check_refs.py` against the target. It checks package paths, whether files under `references/`, `scripts/`, and `tests/` are named by `SKILL.md`, and whether optional skeleton headings are present. For distilled work, it also checks anchors against the configured source corpus. A zero-anchor result is a failure unless the caller explicitly chose `--no-anchor-check` for a non-distilled package; an empty corpus must never read as a passing citation audit.

Read warnings about `../sibling/...` pointers. If the sibling is missing from the review workspace, report the pointer as unresolved and mark the dependent gate deferred. Do not infer that the link works from its spelling.

## 4. Write and resolve findings

Use `templates/refine-review-report.md`. Each finding must name a defect, show the evidence, explain its effect, and suggest a concrete repair. Rank by severity. Include a check-results table that says what ran, what passed, what failed, and what was blocked or not judged.

For each finding, test it against the approved scope and the rule's source. Fix valid findings in the package. Reject out-of-scope findings with the boundary evidence; reject a package defect only when the review setup itself created it and record that reason. Mark dogfood-derived additions as derived. Preserve each routed rule and scope rules separately if they appear to conflict.

After edits, recheck every affected reference, skeleton section, and package file inventory. Run the target's existing test suite and applicable automated checks. Rerun the official `skills-ref validate` gate; when it cannot run, report it as blocked and run `scripts/check_refs.py --format` as the offline format fallback. The fallback is not an official validator pass.

Append one resolution per finding to `fix-notes.md`, list changed coverage IDs in `touched.txt`, and add a stage-specific evolution entry that records the task, severity counts, and fixed/rejected counts. Keep the verdict `PENDING` until the required independent real uses are complete.

## 5. Know what the shipped checks prove

| Check | What it can establish | What it cannot establish |
|---|---|---|
| `scripts/check_refs.py` | Local Markdown links, code-form local paths in `SKILL.md`, package inventory named from `SKILL.md`, optional skeleton headings, optional format fields, and source anchors when configured | Whether an instruction is correct, useful, or faithfully derived |
| `scripts/scrub_check.py` | Matches from its configured private denylist in the worktree or history | Whether the denylist covers every sensitive identifier |
| `skills-ref validate` | Agent Skills metadata/format requirements that the installed official validator implements | Source fidelity, package privacy, sibling ownership, or dogfood quality |
| Stage B programme checkers | Coverage, audit, dogfood, and swap contracts when the programme supplies them | They are not included in this installed skill package; see `rebuild-from-sources.md` for the external-tool boundary and local fallback |
