---
name: frontend
description: "Builds and reviews web front ends with semantic HTML, CSS, TypeScript, and the React or Angular stack already used by a project. USE WHEN creating a web page or application, implementing a tested flow, or auditing and improving an existing interface. Covers accessibility, performance, browser support, agent-ready affordances, and rendered verification. UX owns flows and words; information-design owns chart meaning; visual-design owns composition and type; color-theory owns palette decisions; motion owns motion plans. Keywords: frontend, front end, web UI, website, web app, React, Angular, semantic HTML, CSS, TypeScript, accessibility, responsive design, agent-ready web, redesign, UI audit."
license: "Proprietary (private, not for redistribution)"
---

# Frontend

Build and improve production web interfaces in the project's existing environment. The output is working front-end code, a rendered review of key states, and a concise record of measured, vision-judged, not-judged, and skipped checks.

> Inherits the shared kernel. See [core](../core/SKILL.md); use its canonical gates rather than copying them.

## When it fires — and when a sibling owns it

- **This skill:** implement semantic web pages, responsive layouts, TypeScript UI components, application states, accessible interactions, browser support, agent-ready affordances, and browser-rendered verification; audit an existing front end before changing it.
- **UX:** owns research, task flows, interaction intent, and interface wording; implement its agreed behavior and content here.
- **Information design:** owns chart questions, data mappings, and chart keys. Implement the supplied chart specification and preserve an accessible text or tabular route to the data.
- **Visual design:** owns broader composition, visual hierarchy, grids, and typography. Implement its visual direction in the interface.
- **Color theory:** owns palette, color meaning, color-space decisions, and color analysis. Apply agreed tokens and verify contrast here.
- **Motion:** owns motion stories, timing, and choreography. Implement the motion plan and honor user motion preferences.
- **Scene engine:** owns video rendering and app capture pipelines; render-kit owns visual artifact checks. This skill produces the web application and its implementation checks.

> **Grounded:** read core and the sibling skills above, plus render-kit and scene-engine guides. Reused conventions: keep artifact ownership explicit, return each defect to the stage that can fix it, run code checks before vision review, and report review limits.

## Principles / anchoring rules

1. **Start with the task and environment.** Identify users, tasks, key states, target browsers and devices, content, data, project constraints, and success evidence before choosing implementation details. (derived: brief-baseline combines the client-context rules in [src:platform-apps/report.md], “Verdicts,” with responsive layout guidance in [book:css-in-depth-2e], “7 Responsive design.”)
2. **Prefer native semantics and controls.** HTML elements carry browser and accessibility behavior; add ARIA only where native HTML cannot express the required role, name, or state. [book:whatwg-html], “Semantics, structure, and APIs of HTML documents”; [book:mdn-web-docs], “Before using ARIA.”
3. **Follow the project before introducing a stack.** Detect framework, version, CSS approach, component conventions, and commands; continue in the established system unless evidence from the audit justifies a change. [src:platform-apps/report.md], “F5. Principles that transfer across frameworks.”
4. **Treat accessibility and performance as requirements.** Build to the agreed accessibility target and measure the product on representative screens and conditions; an automated score is one input, not a full review. [book:wcag-22], “5. Conformance”; [book:web-performance-engineering], “Chapter 2. Measuring What Matters.”
5. **Make structure legible to people and software agents.** Expose accurate roles, names, states, and keyboard-operable actions in the page; visual styling alone is not an interaction contract. [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface”; [book:wai-aria-apg], “What Are Accessibility Semantics?”
6. **Render the actual artifact and fix what the render shows.** Code validity cannot establish visual fit, legibility, or task clarity. [src:platform-apps/report.md], “Rule B: HTML first, then verify what renders”; [render-kit/AGENTS.md](../../render-kit/AGENTS.md).

## The flow (at a glance)

| Stage | Goal | Main reference | Completion evidence |
|---|---|---|---|
| 1. Brief and baseline | Name audience, task, constraints, browser/device target, and key states | [brief-baseline.md](references/method/brief-baseline.md) | Brief plus a reproducible current-state baseline |
| 2. Structure and semantics | Encode content, controls, labels, landmarks, and state in HTML | [structure-semantics.md](references/method/structure-semantics.md) | DOM and accessibility tree express the task |
| 3. Layout and CSS | Build responsive, resilient layouts in the house style | [layout-css.md](references/method/layout-css.md) | Base and enhanced states render at target sizes |
| 4. Components and state | Implement in the existing framework with explicit state | [components-state.md](references/method/components-state.md) | Project build and key state transitions pass |
| 5. Accessibility | Test conformance target, keyboard, names, focus, and preferences | [accessibility.md](references/method/accessibility.md) | Automated and manual checks are recorded |
| 6. Performance | Measure loading, responsiveness, and layout stability | [performance.md](references/method/performance.md) | Agreed budgets or field thresholds are met |
| 7. Agent-ready affordances | Make controls discoverable and safe for browser agents | [agent-ready.md](references/method/agent-ready.md) | Role-based task paths and any optional tools are checked |
| 8. Render and check | Render key routes and states, fix, and repeat review | [render-check.md](references/method/render-check.md) | render-kit has no unresolved fail; review answers are verified or marked not-judged |
| 9. Audit-first redesign | Establish existing behavior and defects before changing the interface | [audit-first-redesign.md](references/method/audit-first-redesign.md) | Findings, baseline, and return stages are recorded before implementation |

For a redesign, start at stage 9, then run the relevant stages 1–8. For a small fix, record the affected route and state, run the owning stage, and rerun the render and checks that could be affected.

## Execution

1. Read the repository guidance, package manifest, build scripts, test commands, installed framework version, existing design tokens, and representative routes. Use commands and dependency versions already chosen by the project.
2. Turn the brief into a route/state inventory and acceptance checks. For redesigns, capture the current render and behavior before edits.
3. Implement progressively: semantic document structure, CSS layout, then framework behavior. Keep the DOM order meaningful. Use TypeScript types that model domain values; narrow untrusted input before use.
4. Run the project's lint, type-check, build, and focused behavior checks. Use Playwright role-based locators for user actions and state assertions; run the available accessibility analyzer.
5. Mark each rendered page with render-kit capture metadata. Use data-rk-stage for the artifact region and data-rk-focal only when a particular area is the intended visual focal point.
6. Run render-kit on every key page and state. Fix every fail, inspect skipped and incomplete findings, and rerun after each material visual change. Create a reviewer brief with concrete questions; verify answers. Keep vision review explicitly not-judged when no reviewer can see the renders.
7. Report changed routes and states, checks run, visual review outcome, remaining known limits, and follow-up items.

Detailed procedures are in [render-check.md](references/method/render-check.md) and the linked owner guide [render-kit/AGENTS.md](../../render-kit/AGENTS.md).

## Gates (declared, inherited from core)

- **Grounding gate** — use the product brief, project conventions, verified requirements, and rendered interface as the evidence base. Keep assumptions visible. See [grounding-gate.md](../core/references/grounding-gate.md).
- **Output Contract** — deliver working code, implementation checks, rendered evidence for key states, and a report of what was measured, reviewed, not-judged, or skipped. See [output-contract.md](../core/references/output-contract.md) and [wiki-protocol.md](../core/references/wiki-protocol.md).
- **Pushback and teach** — explain when a requested implementation conflicts with semantics, accessibility, support, or the project architecture, and propose a concrete alternative. See [pushback-and-teach.md](../core/references/pushback-and-teach.md).

## Anti-patterns (hard no-list)

- Replacing a project's framework, router, CSS system, test runner, or component library before checking what is installed and why.
- Building visual controls from generic containers when native links, buttons, inputs, and disclosure elements express the behavior.
- Adding ARIA that disagrees with what the interface does, or leaving checked, expanded, selected, busy, and invalid states stale.
- Depending on a limited browser feature without a complete fallback when users open the site in other browsers.
- Hiding key instructions, data, or actions in pixels, hover-only interactions, or inaccessible canvases.
- Treating a passing automated accessibility scan, Lighthouse result, build, or screenshot diff as proof of every quality dimension.
- Making a redesign from a screenshot alone when routes, interaction states, project rules, or runtime behavior can be inspected.
- Introducing chart meaning, product-flow, palette, composition, or motion decisions owned by a neighboring skill.

## Composition

- **Inherits:** [core](../core/SKILL.md) for shared gates.
- **Works with:** [UX](../ux/SKILL.md) for task flows and wording; [information-design](../information-design/SKILL.md) for chart semantics; [visual-design](../visual-design/SKILL.md) for composition and type; [color-theory](../color-theory/SKILL.md) for palette decisions; [motion](../motion/SKILL.md) for choreography.
- **Uses:** [render-kit/AGENTS.md](../../render-kit/AGENTS.md) for rendering and visual checks; [scene-engine/AGENTS.md](../../scene-engine/AGENTS.md) only when a web interface is being captured into a video deliverable.
- **Boundary:** this skill owns the implementation and rendered verification of web interfaces. Neighboring skills own their input decisions and remain available for targeted reviews.

## References

- [references/method/brief-baseline.md](references/method/brief-baseline.md) — task, environment, support target, and baseline.
- [references/method/structure-semantics.md](references/method/structure-semantics.md) — semantic HTML, controls, names, and state.
- [references/method/layout-css.md](references/method/layout-css.md) — responsive layout, CSS organization, and browser support checks.
- [references/method/components-state.md](references/method/components-state.md) — framework conventions, TypeScript boundaries, and UI states.
- [references/method/accessibility.md](references/method/accessibility.md) — WCAG target, APG behavior, automated checks, and manual review.
- [references/method/performance.md](references/method/performance.md) — performance budgets, field metrics, and optimization.
- [references/method/agent-ready.md](references/method/agent-ready.md) — accessible-tree affordances and optional agent tools.
- [references/method/render-check.md](references/method/render-check.md) — render-kit, Playwright, and vision review loop.
- [references/method/audit-first-redesign.md](references/method/audit-first-redesign.md) — evidence-first review of an existing interface.
- [references/method/review-checklist.md](references/method/review-checklist.md) — T1–T20 pass conditions and return stages.
- [references/method/measurement.md](references/method/measurement.md) — reproducible checks and sourced thresholds for T1–T20.
- [references/method/claim-audit.md](references/method/claim-audit.md) — reserved for independent claim audit; evidence belongs in [audit/](audit/).
- [audit/README.md](audit/README.md) — scope and storage rules for the later audit packet.
- [templates/semantic-page.html](templates/semantic-page.html) and [templates/app-shell.html](templates/app-shell.html) — minimal pages marked for render-kit; both are checked with rk check.
- [NOTICE.md](NOTICE.md) — source and licence notices.
- [EVOLUTION.md](EVOLUTION.md) — design-run birth and pending validation record.
- [DISTILL-REPORT.md](DISTILL-REPORT.md) — source coverage, validation results, and outstanding auditor work.
- [scripts/check_refs.py](scripts/check_refs.py) — package links and local reference checks.
