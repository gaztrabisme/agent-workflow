# Audit-first redesign of an existing interface

## Establish the baseline before changing it

For an existing app, keep its framework, installed version, and house style; upgrade only via official tooling, one major at a time, and check support windows before estimating. [src:platform-apps/report.md], “6. Working inside other people's codebases; greenfield.”

Run the current build, focused tests, automated accessibility checks, and performance checks on the main routes. Inspect keyboard behavior and the accessibility tree manually. Automated results establish findings for the tested rules and state only; the research reports that tool coverage is partial and sources differ on the size of that coverage. [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance”; [src:gaps/report.md], “G2. Testing tools for the render-and-check loop”; [book:playwright-docs], “Accessibility testing.”

## Rank findings by user impact

Separate defects from preferences. Record the route, state, evidence, user impact, likely owner stage, and a test that would show the repair. Fix broken task paths, inaccessible controls, misleading state, and content loss before decorative refinements. (derived: [book:wcag-22], “5.2 Conformance Requirements”; [src:platform-apps/report.md], “F5. Principles that transfer across frameworks.”)

Keep the framework, installed version, router, CSS system, chart and motion libraries, test runner, and project style unless the audit identifies a blocker or the brief explicitly approves a change. Make a focused change, run the existing checks, compare the same route and viewport to the baseline, and route any regression back to the stage that introduced it. [src:platform-apps/report.md], “F5. Principles that transfer across frameworks”; [src:graphics-motion/report.md], “6. Existing codebases”; [src:agent-ready-web/report.md], “UC6 — Existing Angular and React codebases.”

## Report honestly

State which routes and states were inspected, which findings were fixed, which checks were measured, which received vision review, and what remains uncertain. A screenshot-only review cannot establish runtime behavior, and a code-only review cannot establish rendered fit. (derived: [src:platform-apps/report.md], “Rule B: HTML first, then verify what renders”; [render-kit/AGENTS.md](../../../../tools/render-kit/AGENTS.md).)
