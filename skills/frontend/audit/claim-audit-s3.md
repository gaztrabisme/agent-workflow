# Claim audit
Writer: codex
Auditor: glm
Round: 1

Scope: citations in `references/method/measurement.md`, `references/method/performance.md`, `references/method/render-check.md` (58 citations: 32 + 15 + 11). One row per citation occurrence; duplicated anchors in a file are separate rows because they anchor different claims. Markdown links to `[render-kit/AGENTS.md](../../tools/render-kit/AGENTS.md)` are local-guide links, not `[book:…]`/`[src:…]`/`[doc:…]` citations, so they have no rows.

| # | File | Anchor | Claim | Verdict | Note |
|---|---|---|---|---|---|
| 1 | references/method/measurement.md | [book:web-performance-engineering], “Setting Up Performance Budgets and Alerts” | Thresholds must be sourced standards or exact outcomes, never invented scores (derived). | supported | |
| 2 | references/method/measurement.md | [src:platform-apps/report.md], “Verdicts,” | T1 brief fields derive from the client-context rules recorded in Verdicts. | supported | |
| 3 | references/method/measurement.md | [book:css-in-depth-2e], “7 Responsive design.” | T1 baseline fields also derive from chapter 7 responsive-layout guidance. | supported | |
| 4 | references/method/measurement.md | [book:web-dev-baseline], “Baseline,” | Target browser set is defined via Baseline feature status. | supported | |
| 5 | references/method/measurement.md | [doc:https://web.dev/baseline/] | Current Baseline definitions come from web.dev/baseline. | supported | Live page unread; consistent with the Baseline section of [book:web-dev-baseline] (“safe to use… current and previous version of all major browsers”). |
| 6 | references/method/measurement.md | [book:whatwg-html], “How to catch mistakes when writing HTML: validators and conformance checkers” | Validate HTML; no validation errors is the T3 threshold. | supported | |
| 7 | references/method/measurement.md | [book:playwright-docs], “Frame.getByRole.” | Use getByRole checks on primary actions and fields. | supported | |
| 8 | references/method/measurement.md | [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface” | Assert ARIA state on toggle; stale or contradictory state fails. | supported | |
| 9 | references/method/measurement.md | [book:wai-aria-apg], “WAI-ARIA Roles, States, and Properties.” | APG patterns specify roles, states and properties per widget. | supported | |
| 10 | references/method/measurement.md | [book:wcag-22], “Success Criterion 1.4.10 Reflow” | No horizontal overflow at 320 CSS px for vertical content, WCAG exceptions apply. | supported | |
| 11 | references/method/measurement.md | [book:css-in-depth-2e], “7 Responsive design.” | Chapter 7 is the layout procedure for the reflow check. | supported | |
| 12 | references/method/measurement.md | [book:css-in-depth-2e], “1.5.1 Using the cascade for progressive enhancement” | Test feature-enabled and fallback modes per progressive enhancement. | supported | |
| 13 | references/method/measurement.md | [doc:https://web.dev/baseline/] | web.dev/baseline is the current feature-status source. | supported | Live page unread; consistent with [book:web-dev-baseline] Baseline content. |
| 14 | references/method/measurement.md | [src:platform-apps/report.md], “F5. Principles that transfer across frameworks.” | Version discipline: detect versions, use version-matched commands and docs. | supported | |
| 15 | references/method/measurement.md | [book:react-dev], “Choosing the State Structure” | State scenarios (loading, empty, success, error, confirmation) coverage and reachability threshold. | unsupported | Section teaches state-structure principles — group related state, avoid contradictions/“impossible” states, redundancy, duplication, deep nesting; it never discusses covering loading/empty/success/error/confirmation states in tests. |
| 16 | references/method/measurement.md | [src:agent-ready-web/report.md], “UC5d — Extraction review interfaces.” | Same T8 claim anchored to extraction-review interfaces. | unsupported | UC5d gives design defaults for extraction-review UIs — click-to-highlight provenance, risk-ordered queue, explicit confirmation for high-stakes fields, corrections logged as eval data; it does not describe state-coverage testing. |
| 17 | references/method/measurement.md | [book:wcag-22], “Success Criterion 1.4.3 Contrast (Minimum).” | 4.5:1 normal, 3:1 large text contrast, SC 1.4.3 exceptions. | supported | |
| 18 | references/method/measurement.md | [book:wcag-22], “Success Criterion 2.4.7 Focus Visible” | Focus indicator visible. | supported | |
| 19 | references/method/measurement.md | [book:wcag-22], “Success Criterion 2.4.11 Focus Not Obscured (Minimum).” | Focused component not entirely hidden by author content. | supported | |
| 20 | references/method/measurement.md | [book:wcag-22], “Success Criterion 2.5.8 Target Size (Minimum).” | Targets at least 24×24 CSS px unless a documented exception. | supported | |
| 21 | references/method/measurement.md | [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance” | Automated tools do not establish full conformance. | supported | |
| 22 | references/method/measurement.md | [book:playwright-docs], “Accessibility testing.” | Automated accessibility checks need manual follow-up. | supported | |
| 23 | references/method/measurement.md | [book:web-dev-baseline], “Defining the Core Web Vitals metrics thresholds” | Field CWV thresholds: p75 LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1. | overstated | This 2020 section defines p75 LCP ≤2500 ms and CLS ≤0.1, but its responsiveness metric is FID ≤100 ms; it predates INP and never states INP ≤200 ms (that figure is in the co-cited web-performance-engineering budget section, row 24). |
| 24 | references/method/measurement.md | [book:web-performance-engineering], “Setting Up Performance Budgets and Alerts.” | Same thresholds anchored to the budgets-and-alerts section. | supported | |
| 25 | references/method/measurement.md | [src:agent-ready-web/report.md], “UC7 — Coding agents that must see and check what they built” | Every UI task ends with role-based scripted interaction checks. | supported | |
| 26 | references/method/measurement.md | [book:playwright-docs], “Frame.getByRole.” | Primary actions locatable via getByRole assertions. | supported | |
| 27 | references/method/measurement.md | [src:agent-ready-web/report.md], “UC4 — Dashboards and domain visualisations.” | Keyboard-only path reaches the same task result without spatial dragging. | unsupported | UC4 says make chart data reachable as text, keep filters native and labelled, expose read-only agent tools; it says nothing about drag/slider keyboard alternatives. The nearest teaching is F4’s “a typed alternative for every drag or slider interaction” in the same report. |
| 28 | references/method/measurement.md | [src:agent-ready-web/report.md], “F1. WebMCP: tools that a web page declares for in-browser agents” | Optional web tools: test absent API, cancellation, unauthorized and malformed calls. | supported | |
| 29 | references/method/measurement.md | [src:agent-ready-web/report.md], “F6. Security of agent-facing interfaces.” | Security testing basis: denied confirmation leaves data unchanged; no side effects. | supported | |
| 30 | references/method/measurement.md | [src:agent-ready-web/report.md], “UC6 — Existing Angular and React codebases” | Record baseline screenshots and exercise main paths before editing. | overstated | UC6 says “audit before changing”: run Lighthouse agentic-browsing and accessibility categories, fix names, labels and native controls first, use framework MCP servers; it does not mention baseline screenshots or exercising route/state paths. |
| 31 | references/method/measurement.md | [src:platform-apps/report.md], “6. Working inside other people's codebases; greenfield.” | Same baseline-before-edit claim anchored to the existing-codebases section. | unsupported | Section says keep the installed framework, version and house style, upgrade only with official tooling one major at a time, and check support windows; it says nothing about recording baselines or pre-edit test runs. |
| 32 | references/method/measurement.md | [src:graphics-motion/report.md], “6. Existing codebases” | Post-edit rerun and baseline comparison anchored to graphics-motion existing-codebases. | unsupported | Section says keep the existing animation/chart libraries, wrap GSAP calls in a seekable timeline and check licences; it says nothing about rerunning checks or comparing baseline and new renders. |
| 33 | references/method/performance.md | [book:web-performance-engineering], “Evaluating UX Performance: Key Metrics” | No single score describes every user; measure UX across metrics. | supported | |
| 34 | references/method/performance.md | [book:web-performance-engineering], “Setting Up Performance Budgets and Alerts” | Product budget: set thresholds and alerts before optimizing. | supported | |
| 35 | references/method/performance.md | [book:web-performance-in-action], “1.1.1 Web performance and the user experience.” | Performance is user experience; slow sites lose users. | supported | |
| 36 | references/method/performance.md | [book:web-dev-baseline], “Defining the Core Web Vitals metrics thresholds” | CWV good thresholds at p75: LCP 2.5 s, INP 200 ms, CLS 0.1. | overstated | Same as row 23: the section gives p75 LCP ≤2500 ms and CLS ≤0.1 but FID ≤100 ms for responsiveness; it never mentions INP (the 200 ms figure is in the co-cited web-performance-engineering sections, rows 37–38). |
| 37 | references/method/performance.md | [book:web-performance-engineering], “Largest Contentful Paint (LCP): Viewing Content Quickly” | LCP good threshold 2.5 s at 75th percentile. | supported | |
| 38 | references/method/performance.md | [book:web-performance-engineering], “Interaction to Next Paint (INP): Ready to React” | INP target: 75th percentile of interactions below 200 ms. | supported | |
| 39 | references/method/performance.md | [book:web-performance-engineering], “Cumulative Layout Shift (CLS): Visual Stability.” | CLS good threshold below 0.1 for 75% of loads. | supported | |
| 40 | references/method/performance.md | [book:web-performance-engineering], “Lighthouse: Performance Auditing” | Lighthouse is lab diagnostics; field data differs. | supported | |
| 41 | references/method/performance.md | [book:web-performance-engineering], “Chrome DevTools Performance Panel: Deep Diagnostics with AI Assistance” | Profile with DevTools Performance panel to find costly scripts and layout. | supported | |
| 42 | references/method/performance.md | [book:web-performance-engineering], “Chapter 6. Trade-Offs in Performance Optimizations.” | Every optimization has a cost; know priorities before choosing. | supported | |
| 43 | references/method/performance.md | [book:web-performance-in-action], “6.4 Lazy loading images” | Preserve image space to avoid shifts; defer below-fold media (derived). | supported | |
| 44 | references/method/performance.md | [book:web-performance-in-action], “7.4 Optimizing the loading of fonts” | Same derived claim: control font loading. | supported | |
| 45 | references/method/performance.md | [book:web-dev-baseline], “Responsive Images.” | Choose image sizes for rendered contexts (derived). | supported | |
| 46 | references/method/performance.md | [book:web-performance-in-action], “3.3 Performance-tuning your CSS” | Book covers CSS tuning; validate older techniques in current toolchain. | derived-unlabelled | Section teaches the CSS-tuning techniques the passage describes, but “keep optimizations proportionate” is the writer’s own maxim (the book’s proportionality/trade-off teaching is Chapter 6, cited one paragraph above), and the “(derived: …)” label covers only the validation clause. |
| 47 | references/method/performance.md | [book:web-performance-in-action], “8.1 Affecting script-loading behavior” | Book covers script-loading techniques; validate in current toolchain. | derived-unlabelled | Same as row 46: the section teaches the script-loading techniques described; the proportionality maxim is unlabelled writer framing. |
| 48 | references/method/render-check.md | [book:playwright-docs], “Accessibility testing” | Automated a11y checks do not cover all barriers. | supported | |
| 49 | references/method/render-check.md | [book:playwright-docs], “Frame.getByRole” | Drive the page with role-based locators. | supported | |
| 50 | references/method/render-check.md | [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.” | Project's own checks first; axe then manual pass. | supported | |
| 51 | references/method/render-check.md | [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance” | Screenshot comparison needs recorded viewport, browser, font, environment. | supported | |
| 52 | references/method/render-check.md | [src:agent-ready-web/report.md], “UC7 — Coding agents that must see and check what they built” | Same claim; fixed-container screenshot comparison. | supported | |
| 53 | references/method/render-check.md | [book:playwright-docs], “Assertions.” | Fix incorrect state before vision review; assertions verify state. | supported | |
| 54 | references/method/render-check.md | [src:platform-apps/report.md], “Rule B: HTML first, then verify what renders.” | Verify the rendered result; HTML first (Rule B). | supported | |
| 55 | references/method/render-check.md | [src:agent-ready-web/report.md], “UC7 — Coding agents that must see and check what they built” | Keep fixed screenshot environment; repeat render-critique-revise loop. | supported | |
| 56 | references/method/render-check.md | [book:playwright-docs], “Assertions” | Distinguish pixel changes from behavioral results (derived). | supported | |
| 57 | references/method/render-check.md | [book:playwright-docs], “Accessibility testing” | Record automated, manual, and vision evidence separately (derived). | supported | |
| 58 | references/method/render-check.md | [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.” | Do not collapse evidence types into one score (derived). | supported | |

Totals: 58 rows — 48 supported, 3 overstated (23, 30, 36), 5 unsupported (15, 16, 27, 31, 32), 2 derived-unlabelled (46, 47).

Portability check (grep for foreign skill names, tool names, subagent references over SKILL.md and references/method):

```
$ grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|redesign-existing-projects|frontend-design|batch-photo-retouching|Read tool|Bash tool|subagent_type' …/SKILL.md …/references/method
(no matches; grep exit status 1)
```

Citations not reached: none — all 58 in-scope citations were checked against the cited sections.
