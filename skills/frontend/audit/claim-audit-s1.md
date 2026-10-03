# Claim audit

Writer: codex
Auditor: glm
Round: 1

Scope: `SKILL.md`, `references/method/accessibility.md`, `references/method/agent-ready.md`, `references/method/audit-first-redesign.md`. Every citation in scope was read against the cited section of the named source. 53 citations, 53 rows.

| # | File | Anchor | Claim | Verdict | Note |
|---|---|---|---|---|---|
| 1 | SKILL.md | [src:platform-apps/report.md], “Verdicts,” with responsive layout guidance in [book:css-in-depth-2e], “7 Responsive design.” | Baseline combines client-context rules with responsive layout guidance (derived) | supported | |
| 2 | SKILL.md | [book:whatwg-html], “Semantics, structure, and APIs of HTML documents” | HTML elements carry built-in browser and accessibility behaviour | supported | |
| 3 | SKILL.md | [book:mdn-web-docs], “Before using ARIA.” | Prefer semantic HTML; add ARIA only where native elements cannot express role, name, state | supported | |
| 4 | SKILL.md | [src:platform-apps/report.md], “F5. Principles that transfer across frameworks.” | Detect framework, version, CSS approach, conventions, commands; stay unless audit justifies change | overstated | F5 says detect framework major, router mode, zone/zoneless and OnPush default, test runner and TypeScript before writing; keep the project's test runner; upgrade only with official tooling, one major at a time. It never lists CSS approach or component conventions, and it conditions change on official migration tooling, not on audit evidence. |
| 5 | SKILL.md | [book:wcag-22], “5. Conformance” | Accessibility conformance is a formal requirement with defined levels | supported | |
| 6 | SKILL.md | [book:web-performance-engineering], “Chapter 2. Measuring What Matters.” | Measure with lab and field data on real devices and conditions | supported | |
| 7 | SKILL.md | [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface” | Expose accurate roles, names, states; agents read the accessibility tree | supported | |
| 8 | SKILL.md | [book:wai-aria-apg], “What Are Accessibility Semantics?” | Accessibility semantics are role, properties and state conveyed to assistive technology | supported | |
| 9 | SKILL.md | [src:platform-apps/report.md], “Rule B: HTML first, then verify what renders” | Code validity alone cannot establish rendered quality; verify the rendered result | supported | |
| 10 | references/method/accessibility.md | [book:wcag-22], “5. Conformance” | Use WCAG 2.2 AA as default engineering target; AA is a defined conformance level | supported | |
| 11 | references/method/accessibility.md | [src:gaps/report.md], “G1. Accessibility law by deliverable type and jurisdiction.” | Obligation falls on the operator; standards and dates differ by jurisdiction and contract | supported | |
| 12 | references/method/accessibility.md | [book:wai-aria-apg], “Button Pattern” | APG pattern specifies required keyboard interaction and states for a widget | supported | |
| 13 | references/method/accessibility.md | [book:wai-aria-apg], “Dialog (Modal) Pattern” | Dialog pattern specifies keyboard interaction and focus behaviour | supported | |
| 14 | references/method/accessibility.md | [book:web-accessibility-cookbook], “6.2 Make Elements Focusable” | Keyboard users must reach every interactive element via Tab | supported | |
| 15 | references/method/accessibility.md | [book:practical-web-accessibility], “Semantic Markup.” | Valid semantic markup and heading structure underpin screen-reader access | supported | |
| 16 | references/method/accessibility.md | [book:wcag-22], “Success Criterion 1.4.3 Contrast (Minimum)” | 4.5:1 normal text, 3:1 large-scale text, with criterion exceptions | supported | |
| 17 | references/method/accessibility.md | [book:wcag-22], “Success Criterion 1.4.11 Non-text Contrast.” | 3:1 for visual information identifying controls and states | supported | |
| 18 | references/method/accessibility.md | [book:wcag-22], “Success Criterion 1.4.10 Reflow” | Reflow at 320 CSS pixels without two-dimensional scrolling or loss of function | supported | |
| 19 | references/method/accessibility.md | [book:wcag-22], “Success Criterion 2.4.7 Focus Visible” | Keyboard focus indicator must be visible | supported | |
| 20 | references/method/accessibility.md | [book:wcag-22], “Success Criterion 2.4.11 Focus Not Obscured (Minimum).” | Focused component not entirely hidden by author-created content | supported | |
| 21 | references/method/accessibility.md | [book:wcag-22], “Success Criterion 2.5.8 Target Size (Minimum)” | 24 by 24 CSS pixel minimum pointer target with defined exceptions | supported | |
| 22 | references/method/accessibility.md | [book:mdn-web-docs], “prefers-reduced-motion” | Media feature detects reduced-motion preference; reduce, not remove, non-essential motion | supported | |
| 23 | references/method/accessibility.md | [book:wcag-22], “Success Criterion 1.4.3 Contrast (Minimum)” | Text contrast requirement applies in every theme variant | supported | |
| 24 | references/method/accessibility.md | [book:wcag-22], “Success Criterion 1.4.11 Non-text Contrast.” | Non-text contrast requirement applies in every palette variant | supported | |
| 25 | references/method/accessibility.md | [src:platform-apps/report.md], “F2. Una Kravets, ‘Modern UI Patterns’, CSS Day 2026 — five UX principles.” | Reduced motion keeps opacity feedback; themed palettes need their own contrast tests | supported | |
| 26 | references/method/accessibility.md | [book:playwright-docs], “Accessibility testing” | Automated scans catch some problems; manual testing still required | supported | |
| 27 | references/method/accessibility.md | [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.” | Automation finds only part; sources disagree on share; manual checks remain necessary | supported | |
| 28 | references/method/accessibility.md | [book:wcag-22], “5.2 Conformance Requirements” | Report scope checked; conformance is for full pages and complete processes (derived) | supported | |
| 29 | references/method/accessibility.md | [book:practical-web-accessibility], “Accessibility Tree.” | Accessibility tree inspectable in DevTools for manual review (derived) | supported | |
| 30 | references/method/agent-ready.md | [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface” | Benchmarks: accessibility-tree beats coordinate-only; stale state misleads agents | supported | |
| 31 | references/method/agent-ready.md | [book:wai-aria-apg], “Providing Accessible Names and Descriptions.” | Accessible names and descriptions are a core author responsibility, with naming techniques | supported | |
| 32 | references/method/agent-ready.md | [src:agent-ready-web/report.md], “UC7 — Coding agents that must see and check what they built” | UI tasks end with scripted checks via role-based locators | supported | |
| 33 | references/method/agent-ready.md | [src:agent-ready-web/report.md], “UC4 — Dashboards and domain visualisations” | Keep filter controls native and labelled | supported | |
| 34 | references/method/agent-ready.md | [book:playwright-docs], “Frame.getByRole.” | Role-based locator API exists, returning a Locator | supported | |
| 35 | references/method/agent-ready.md | [src:agent-ready-web/report.md], “UC4 — Dashboards and domain visualisations” | Chart data reachable as a text table or accessible summary | supported | |
| 36 | references/method/agent-ready.md | [src:agent-ready-web/report.md], “UC5a — Exposing an internal tool or AI app to browser agents (WebMCP)” | Prepare, do not depend; feature-detect behind registerTool check | supported | |
| 37 | references/method/agent-ready.md | [src:agent-ready-web/report.md], “F1. WebMCP: tools that a web page declares for in-browser agents” | CG-DRAFT spec, changing API shape, tools run in the signed-in session | supported | |
| 38 | references/method/agent-ready.md | [doc:https://developer.chrome.com/docs/ai/webmcp/] | WebMCP preview; check current spec and browser status before integrating | supported | Live page not read; verdict rests on consistency with the research, whose F1 cites this Chrome docs page (updated 2026-08-07) and reports it as preview with changing API. |
| 39 | references/method/agent-ready.md | [src:agent-ready-web/report.md], “F1. WebMCP: tools that a web page declares for in-browser agents” | Typed schemas, handlers reusing UI code, cancellation signal, untrusted descriptions | supported | |
| 40 | references/method/agent-ready.md | [src:agent-ready-web/report.md], “F6. Security of agent-facing interfaces” | Tool annotations untrusted; confirm consequential and irreversible actions | supported | |
| 41 | references/method/agent-ready.md | [src:agent-ready-web/report.md], “UC5c — Showing Gary's UI inside AI clients” | Standard stable while host display modes and extras differ | supported | |
| 42 | references/method/audit-first-redesign.md | [src:platform-apps/report.md], “6. Working inside other people's codebases; greenfield” | Confirm app runs with project commands; inspect routes, states, conventions; capture renders | overstated | Section 6 says keep the framework, installed version and house style, upgrade only via official tooling one major at a time, and check support windows before estimating. It does not prescribe inspecting routes, content, responsive states, controls or error paths, nor capturing renders before changes. |
| 43 | references/method/audit-first-redesign.md | [src:output-pipelines/report.md], “F9. Capturing demos of real apps with source access” | Deterministic fixed-viewport capture of an unmodified app with source access | supported | |
| 44 | references/method/audit-first-redesign.md | [book:playwright-docs], “Assertions.” | Auto-retrying assertions wait until the condition is met | supported | |
| 45 | references/method/audit-first-redesign.md | [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.” | Run codebase's own build and tests, axe scan; manual keyboard pass | supported | |
| 46 | references/method/audit-first-redesign.md | [src:gaps/report.md], “G2. Testing tools for the render-and-check loop” | Engines catch different, partly overlapping defect subsets | supported | |
| 47 | references/method/audit-first-redesign.md | [book:playwright-docs], “Accessibility testing.” | Automated accessibility tests detect some problems; many need manual testing | supported | |
| 48 | references/method/audit-first-redesign.md | [book:wcag-22], “5.2 Conformance Requirements” | Conformance covers full pages; all level criteria met in full (derived) | supported | |
| 49 | references/method/audit-first-redesign.md | [src:platform-apps/report.md], “F5. Principles that transfer across frameworks.” | Verify in a running app headless, then assert in Playwright (derived) | supported | |
| 50 | references/method/audit-first-redesign.md | [src:platform-apps/report.md], “F5. Principles that transfer across frameworks.” | Keep test runner; upgrade one major at a time; consistency beats style guide | supported | |
| 51 | references/method/audit-first-redesign.md | [src:graphics-motion/report.md], “6. Existing codebases” | Keep existing animation and chart libraries; switch only on a blocker | supported | |
| 52 | references/method/audit-first-redesign.md | [src:agent-ready-web/report.md], “UC6 — Existing Angular and React codebases.” | Default: audit before changing; fix names, labels and native controls first | supported | |
| 53 | references/method/audit-first-redesign.md | [src:platform-apps/report.md], “Rule B: HTML first, then verify what renders” | Every verdict assumes a headless check of the rendered result (derived) | supported | |

## Portability check

```
$ grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|redesign-existing-projects|frontend-design|batch-photo-retouching|Read tool|Bash tool|subagent_type' <skill>/SKILL.md <skill>/references/method
(no output; grep exit 1 — no matches)
```

No sibling-skill names or tool-specific terms appear in `SKILL.md` or `references/method/`.

## Coverage

All 53 citations in scope were reached and checked; none left unaudited. Non-supported rows: #4 and #42 (`overstated`), returned to the writer.
