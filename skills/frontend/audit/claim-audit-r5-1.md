# Claim audit
Writer: codex
Auditor: glm
Round: 5

Scope: every citation in `references/method/measurement.md` (30 instances) and `references/method/performance.md` (16 instances). All 40 unique (file, anchor) pairs were re-read in their cited sections this round. No non-supported rows were carried from round 4 in this scope; the two `[doc:https://web.dev/articles/inp]` citations are new since the round-4 merge.

| # | File | Anchor | Claim | Verdict | Note |
|---|---|---|---|---|---|
| 1 | references/method/measurement.md | [book:web-performance-engineering], “Setting Up Performance Budgets and Alerts” | Thresholds must be sourced standards or exact outcomes, never invented scores (derived) | supported |  |
| 2 | references/method/measurement.md | [src:platform-apps/report.md], “Verdicts,” | T1 brief fields derive from the client-context rules recorded in Verdicts (derived) | supported |  |
| 3 | references/method/measurement.md | [book:css-in-depth-2e], “7 Responsive design.” | Chapter 7 supplies the responsive-layout planning context for the T1 fields (derived) | supported |  |
| 4 | references/method/measurement.md | [book:web-dev-baseline], “Baseline,” | Target browser set defined via Baseline: features safe to use today | supported |  |
| 5 | references/method/measurement.md | [doc:https://web.dev/baseline/] | Live Baseline status is the current definition source for the target set | supported | Live page not read; consistent with [book:web-dev-baseline] (“safe to use … today”, “current and previous version of all major browsers”). |
| 6 | references/method/measurement.md | [book:playwright-docs], “Frame.getByRole.” | getByRole returns a Locator that locates by ARIA role | supported |  |
| 7 | references/method/measurement.md | [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface” | Tree exposes role, name, state; wrong or stale ARIA state misleads agents | supported |  |
| 8 | references/method/measurement.md | [book:wai-aria-apg], “WAI-ARIA Roles, States, and Properties.” | APG patterns specify roles, states and properties per widget | supported |  |
| 9 | references/method/measurement.md | [book:wcag-22], “Success Criterion 1.4.10 Reflow” | 320 CSS px vertical content without loss or two-dimensional scrolling, with exceptions | supported |  |
| 10 | references/method/measurement.md | [book:css-in-depth-2e], “7 Responsive design.” | Chapter 7 is the layout procedure: mobile-first, media queries, fluid layouts | supported |  |
| 11 | references/method/measurement.md | [book:css-in-depth-2e], “1.5.1 Using the cascade for progressive enhancement” | Unsupported declarations are ignored; base experience stays acceptable | supported |  |
| 12 | references/method/measurement.md | [doc:https://web.dev/baseline/] | Live Baseline status is the current feature-status source for mode testing | supported | Live page not read; consistent with [book:web-dev-baseline]. Anchor shared with row 5 (T2). |
| 13 | references/method/measurement.md | [src:platform-apps/report.md], “F5. Principles that transfer across frameworks.” | Detect versions and modes before writing; version-matched docs; verify headless | supported |  |
| 14 | references/method/measurement.md | [book:react-dev], “Choosing the State Structure” | Scenario check applies React's avoid-contradictions principle (derived) | supported |  |
| 15 | references/method/measurement.md | [src:agent-ready-web/report.md], “UC5d — Extraction review interfaces.” | Scenario check applies UC5d's confirmation requirement for high-stakes actions (derived) | supported |  |
| 16 | references/method/measurement.md | [book:wcag-22], “Success Criterion 1.4.3 Contrast (Minimum).” | 4.5:1 normal text, 3:1 large text, with listed exceptions | supported |  |
| 17 | references/method/measurement.md | [book:wcag-22], “Success Criterion 2.4.7 Focus Visible” | Keyboard focus indicator must be visible | supported |  |
| 18 | references/method/measurement.md | [book:wcag-22], “Success Criterion 2.4.11 Focus Not Obscured (Minimum).” | Focused component not entirely hidden by author-created content | supported |  |
| 19 | references/method/measurement.md | [book:wcag-22], “Success Criterion 2.5.8 Target Size (Minimum).” | Targets at least 24×24 CSS px, with listed exceptions | supported |  |
| 20 | references/method/measurement.md | [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance” | Automated testing finds only part; manual checks remain necessary | supported |  |
| 21 | references/method/measurement.md | [book:playwright-docs], “Accessibility testing.” | Automated scans catch some problems; many need manual testing | supported |  |
| 22 | references/method/measurement.md | [doc:https://web.dev/articles/inp] | Field CWV: p75 LCP ≤2.5s, INP ≤200ms, CLS ≤0.1; lab timings are not INP | supported | New since round 4. Live page not read; consistent with [book:web-performance-engineering] (“INP … replaced FID as one of the CWVs”, p75 interactions below 200 ms) and [src:platform-apps/report.md] F8 (INP ≤200 ms; replaced FID 2024-03-12). |
| 23 | references/method/measurement.md | [book:web-dev-baseline], “Defining the Core Web Vitals metrics thresholds.” | Field CWV have good thresholds assessed at the 75th percentile | supported | The section's 2020 table gives p75 LCP ≤2500 ms, FID ≤100 ms, CLS ≤0.1; the INP ≤200 ms value in the sentence rests on the co-cited doc anchor (row 22). |
| 24 | references/method/measurement.md | [src:agent-ready-web/report.md], “UC7 — Coding agents that must see and check what they built” | Every UI task ends with scripted interactions via role-based locators | supported |  |
| 25 | references/method/measurement.md | [book:playwright-docs], “Frame.getByRole.” | Role-based locators plus assertions reach the expected rendered state | supported | Anchor shared with row 6 (T3). |
| 26 | references/method/measurement.md | [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface.” | Checking the browser result tests the recommended typed alternative (derived) | supported |  |
| 27 | references/method/measurement.md | [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface.” | Every drag or slider interaction has a typed alternative | supported |  |
| 28 | references/method/measurement.md | [src:agent-ready-web/report.md], “F1. WebMCP: tools that a web page declares for in-browser agents” | Tools run in-session behind feature detection; cancellation signal; confirmation hints | supported |  |
| 29 | references/method/measurement.md | [src:agent-ready-web/report.md], “F6. Security of agent-facing interfaces.” | Human in the loop can deny invocations; enforce limits in code, not descriptions | supported |  |
| 30 | references/method/measurement.md | [src:agent-ready-web/report.md], “UC6 — Existing Angular and React codebases.” | Audit before changing: Lighthouse categories; fix names, labels, native controls first | supported |  |
| 31 | references/method/performance.md | [book:web-performance-engineering], “Evaluating UX Performance: Key Metrics” | No single metric tells the whole story; UX is a progression of moments | supported |  |
| 32 | references/method/performance.md | [book:web-performance-engineering], “Setting Up Performance Budgets and Alerts” | Teams establish thresholds and alerts; an example CWV budget is given | supported |  |
| 33 | references/method/performance.md | [book:web-performance-in-action], “1.1.1 Web performance and the user experience.” | Performance is user experience; slow sites lose engagement and revenue | supported |  |
| 34 | references/method/performance.md | [doc:https://web.dev/articles/inp] | INP is the current responsiveness CWV, replacing FID; good threshold ≤200ms p75 | supported | New since round 4. Live page not read; consistent with [book:web-performance-engineering] (“INP … replaced FID as one of the CWVs”; recommended target: 75th percentile below 200 ms) and [src:platform-apps/report.md] F8 (INP ≤200 ms; replaced FID on 2024-03-12). |
| 35 | references/method/performance.md | [book:web-dev-baseline], “Defining the Core Web Vitals metrics thresholds” | CWV are field metrics with good/poor thresholds at the 75th percentile | supported | 2020 table lists LCP ≤2500 ms, FID ≤100 ms, CLS ≤0.1; the INP value rests on the co-cited anchors (rows 34, 36, 37). |
| 36 | references/method/performance.md | [book:web-performance-engineering], “Largest Contentful Paint (LCP): Viewing Content Quickly” | LCP good threshold: under 2.5 s at the 75th percentile of users | supported |  |
| 37 | references/method/performance.md | [book:web-performance-engineering], “Cumulative Layout Shift (CLS): Visual Stability.” | CLS goal: below 0.1 for 75% of page loads | supported |  |
| 38 | references/method/performance.md | [book:web-performance-engineering], “Lighthouse: Performance Auditing” | Lighthouse audits in a controlled lab environment; complements field data | supported |  |
| 39 | references/method/performance.md | [book:web-performance-engineering], “Chrome DevTools Performance Panel: Deep Diagnostics with AI Assistance” | Profile recordings pinpoint costly functions, stalls and layout thrash | supported |  |
| 40 | references/method/performance.md | [book:web-performance-engineering], “Chapter 6. Trade-Offs in Performance Optimizations.” | Diagnose causes and weigh trade-offs before changing architecture | supported |  |
| 41 | references/method/performance.md | [book:web-performance-in-action], “6.4 Lazy loading images” | Lazy-load below-fold images; saves bandwidth and initial load time (labelled derived) | supported |  |
| 42 | references/method/performance.md | [book:web-performance-in-action], “7.4 Optimizing the loading of fonts” | font-display and the font-loading API control font loading (labelled derived) | supported |  |
| 43 | references/method/performance.md | [book:web-dev-baseline], “Responsive Images.” | width/height prevent layout shifts; srcset/picture pick sizes per context (labelled derived) | supported |  |
| 44 | references/method/performance.md | [book:web-performance-engineering], “Chapter 6. Trade-Offs in Performance Optimizations.” | Keep optimizations proportionate to workload and users (labelled derived) | supported |  |
| 45 | references/method/performance.md | [book:web-performance-in-action], “3.3 Performance-tuning your CSS” | Book teaches CSS-tuning techniques (@import avoidance, link parallelism) | supported |  |
| 46 | references/method/performance.md | [book:web-performance-in-action], “8.1 Affecting script-loading behavior” | Book teaches script placement and async loading techniques | supported |  |

## Portability check

```
$ grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|redesign-existing-projects|frontend-design|batch-photo-retouching|Read tool|Bash tool|subagent_type' …/SKILL.md …/references/method
```

No matches (grep exit 1): no leaked skill names, tool names or subagent references in `SKILL.md` or `references/method/`.

## Coverage

All 46 citation instances in scope are listed above (40 unique file/anchor pairs); none skipped. The `[render-kit/AGENTS.md](../../../../tools/render-kit/AGENTS.md)` links in `measurement.md` are project-file links, not `[book:]/[src:]/[doc:]` citations, and are not counted as citations by `check_claims.py --sources`.
