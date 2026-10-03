# Render and check

## Run exact checks first

Use the project's lint, type-check, build, and behavior tests first. For browser behavior, drive the page with Playwright role-based locators and assert the resulting visible and accessible state. Add axe checks where the project has them; automated accessibility checks do not cover all user barriers. [book:playwright-docs], “Accessibility testing”; [book:playwright-docs], “Frame.getByRole”; [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.”

Fix console errors, failed resources, broken navigation, incorrect state, and overflowing or clipped content before asking for a vision review. A screenshot comparison is meaningful only with a recorded viewport, browser, font, and render environment. [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance”; [src:agent-ready-web/report.md], “UC7 — Coding agents that must see and check what they built”; [book:playwright-docs], “Assertions.”

## Render every key page and state

Add data-rk-stage to identify the area that should be captured and checked. Add data-rk-focal only when one element or area is intentionally the focal point. Run the owner tool's check for each key page and state. Fix every fail; inspect each skipped or incomplete result and record why it cannot be evaluated automatically. [render-kit/AGENTS.md](../../../../tools/render-kit/AGENTS.md).

Make interactive states reproducible from their own URLs or fixtures (for example `/?day=27`, `/?state=empty`, and an error fixture). Expose a stable state marker after data and layout are ready, then pass that selector to `--wait-for`; `main[data-state="ready"]` is the pattern used by [states.html](../../templates/states.html). Do not animate or transition when setting the requested state, because rk freezes page time during capture. Example against a running local app: `rk check http://127.0.0.1:4317/?day=27 --wait-for 'main[data-state="ready"][data-rk-ready="true"]' --width 320 --height 900 --out-dir checks/day27-320`. (derived: dogfood 2026-10-02, F3)

Use `data-rk-ignore` only for content that the visual checker cannot judge in its normal captured state, and put it on the smallest affected element or container. Typical patterns are:

```html
<a class="skip-link" href="#main" data-rk-ignore>Skip to main content</a>
<span class="visually-hidden" data-rk-ignore>Additional context</span>
<details data-rk-ignore><summary>More details</summary>...</details>
<div class="table-scroll" tabindex="0" data-rk-ignore>...</div>
```

Use these for an off-screen-until-focused skip link, a standard clipped visually-hidden label, content inside a closed native `<details>`, or the contents of a labelled horizontal scroll region. The ignored pattern still needs a Playwright behavior assertion and an axe check in the relevant state (focus the skip link, open `<details>`, or scroll the region). (derived: dogfood 2026-10-02, F4)

For an intentional failed request in an error-state fixture, record the exact URL, status, reason, recovery assertion, and reviewer/owner in the run notes. Until rk supports a declared expected request, keep the `resources` finding visible and call it an accepted exception only after review; do not suppress the request or report it as a clean zero-fail run. (derived: dogfood 2026-10-02, F2)

After code checks, use render-kit to prepare a brief with specific visual questions. Ask a reviewer who did not make the page to judge hierarchy, wrapping, clipping, spacing, responsive behavior, and whether the expected task or state is visually clear. Verify the review answers; a no means revise and render again. If a suitable reviewer is unavailable, mark the vision checks not-judged. [render-kit/AGENTS.md](../../../../tools/render-kit/AGENTS.md); [src:platform-apps/report.md], “Rule B: HTML first, then verify what renders.”

Prepare one `rk brief` per key state and viewport so each review image and question set names the state under review. Pass `--pdf` only when a PDF deliverable exists. (derived: dogfood 2026-10-02, F11)

Repeat the loop after changes that affect markup, styles, fonts, content length, breakpoints, or state. Keep the same viewport and font environment for screenshot comparison, and distinguish pixel changes from behavioral results. [src:agent-ready-web/report.md], “UC7 — Coding agents that must see and check what they built”; [book:playwright-docs], “Assertions”; (derived: a visual pass does not substitute for a behavior pass.)

## Record the result

For each route and state, record the build/test result, render-kit status, automated accessibility findings, manual keyboard steps, vision answers, and any skipped or not-judged check. Do not collapse different evidence types into a single quality score. (derived: [render-kit/AGENTS.md](../../../../tools/render-kit/AGENTS.md); [book:playwright-docs], “Accessibility testing”; [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.”)
