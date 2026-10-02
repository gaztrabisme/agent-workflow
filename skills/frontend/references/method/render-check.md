# Render and check

## Run exact checks first

Use the project's lint, type-check, build, and behavior tests first. For browser behavior, drive the page with Playwright role-based locators and assert the resulting visible and accessible state. Add axe checks where the project has them; automated accessibility checks do not cover all user barriers. [book:playwright-docs], “Accessibility testing”; [book:playwright-docs], “Frame.getByRole”; [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.”

Fix console errors, failed resources, broken navigation, incorrect state, and overflowing or clipped content before asking for a vision review. A screenshot comparison is meaningful only with a recorded viewport, browser, font, and render environment. [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance”; [src:agent-ready-web/report.md], “UC7 — Coding agents that must see and check what they built”; [book:playwright-docs], “Assertions.”

## Render every key page and state

Add data-rk-stage to identify the area that should be captured and checked. Add data-rk-focal only when one element or area is intentionally the focal point. Run the owner tool's check for each key page and state. Fix every fail; inspect each skipped or incomplete result and record why it cannot be evaluated automatically. [render-kit/AGENTS.md](../../render-kit/AGENTS.md).

After code checks, use render-kit to prepare a brief with specific visual questions. Ask a reviewer who did not make the page to judge hierarchy, wrapping, clipping, spacing, responsive behavior, and whether the expected task or state is visually clear. Verify the review answers; a no means revise and render again. If a suitable reviewer is unavailable, mark the vision checks not-judged. [render-kit/AGENTS.md](../../render-kit/AGENTS.md); [src:platform-apps/report.md], “Rule B: HTML first, then verify what renders.”

Repeat the loop after changes that affect markup, styles, fonts, content length, breakpoints, or state. Keep the same viewport and font environment for screenshot comparison, and distinguish pixel changes from behavioral results. [src:agent-ready-web/report.md], “UC7 — Coding agents that must see and check what they built”; [book:playwright-docs], “Assertions”; (derived: a visual pass does not substitute for a behavior pass.)

## Record the result

For each route and state, record the build/test result, render-kit status, automated accessibility findings, manual keyboard steps, vision answers, and any skipped or not-judged check. Do not collapse different evidence types into a single quality score. (derived: [render-kit/AGENTS.md](../../render-kit/AGENTS.md); [book:playwright-docs], “Accessibility testing”; [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.”)
