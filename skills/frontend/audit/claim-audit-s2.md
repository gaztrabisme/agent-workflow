# Claim audit

Writer: codex
Auditor: glm
Round: 1

Scope: citations in `references/method/brief-baseline.md`, `references/method/components-state.md`, `references/method/layout-css.md`. One row per unique (file, anchor) pair; repeated occurrences of the same anchor within a file are covered by that row. 45 citation occurrences → 39 pairs.

| # | File | Anchor | Claim | Verdict | Note |
|---|---|---|---|---|---|
| 1 | references/method/brief-baseline.md | [src:platform-apps/report.md], “Rule A: choose the support target by who opens the output” | Derived note: research separates controlled render environments from client browsers | supported | |
| 2 | references/method/brief-baseline.md | [src:platform-apps/report.md], “6. Working inside other people's codebases; greenfield.” | Derived note: existing codebases get preservation rules | supported | |
| 3 | references/method/brief-baseline.md | [book:css-in-depth-2e], “7 Responsive design” | Derived note: content-first planning grounds brief-first guidance | supported | |
| 4 | references/method/brief-baseline.md | [book:practical-web-accessibility], “Linear Layouts.” | Derived note: content order precedes styling decisions | supported | |
| 5 | references/method/brief-baseline.md | [src:platform-apps/report.md], “F5. Principles that transfer across frameworks.” | Identify framework, version, router, CSS system, primitives, test runner, tokens, lint commands | overstated | F5 lists framework major, router mode, change-detection defaults, test runner and TypeScript only; CSS system, component primitives, design tokens and build/lint commands appear under F7 and F6, which this paragraph does not cite. The rest of the paragraph (docs matching installed version, newer-major advice breaking older apps, preserving conventions) is in F5 and section 6. |
| 6 | references/method/brief-baseline.md | [book:web-dev-baseline], “Baseline” | Baseline states which features are safe to use today | supported | |
| 7 | references/method/brief-baseline.md | [doc:https://web.dev/baseline/] | Check live Baseline status for features in core interactions | supported | |
| 8 | references/method/brief-baseline.md | [book:wcag-22], “Success Criterion 1.4.10 Reflow” | Derived note: record zoom/reflow expectations | supported | |
| 9 | references/method/brief-baseline.md | [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.” | Derived note: accessibility, keyboard checks, performance ground recorded targets | supported | |
| 10 | references/method/components-state.md | [src:platform-apps/report.md], “F5. Principles that transfer across frameworks” | Detect versions; docs match installed version; keep framework, state model, test runner | supported | |
| 11 | references/method/components-state.md | [book:react-dev], “Your First Component” | Official React component model documents to follow | supported | |
| 12 | references/method/components-state.md | [book:angular-dev], “Components and directives” | Angular's official component conventions: selectors, naming, member grouping | supported | |
| 13 | references/method/components-state.md | [book:angular-up-and-running], “Creating a Component.” | CLI component generation with recommended naming convention | supported | |
| 14 | references/method/components-state.md | [src:platform-apps/report.md], “F7. Styling, component primitives, design tokens, data and state” | Keep codebase's primitives; add stores only if already present | supported | |
| 15 | references/method/components-state.md | [book:fluent-react], “Immutable state” | React state as immutable snapshots; predictable transitions, fewer side effects | supported | |
| 16 | references/method/components-state.md | [book:angular-dev], “Keep components and directives focused on presentation.” | Component code relates to UI; decoupled logic moves out | supported | |
| 17 | references/method/components-state.md | [book:react-dev], “Choosing the State Structure” | Group related state; avoid contradictions and duplication; derive computable values | supported | |
| 18 | references/method/components-state.md | [book:react-dev], “Keeping Components Pure.” | Components render as pure functions; impurities live outside render | supported | |
| 19 | references/method/components-state.md | [book:effective-typescript], “Item 36: Use a Distinct Type for Special Values” | Special sentinel values need a distinct, narrower type | supported | |
| 20 | references/method/components-state.md | [book:effective-typescript], “Item 41: Name Types Using the Language of Your Problem Domain” | Type names use the problem domain's language | supported | |
| 21 | references/method/components-state.md | [book:effective-typescript], “Item 46: Use unknown Instead of any for Values with an Unknown Type” | Prefer unknown over any at untrusted boundaries; narrow before use | supported | |
| 22 | references/method/components-state.md | [book:effective-typescript], “Item 59: Use Never Types to Perform Exhaustiveness Checking.” | Never-based exhaustiveness checking catches missed cases | supported | |
| 23 | references/method/components-state.md | [book:react-dev], “State: a component's memory” | Derived note: state is component memory updated by interactions | supported | |
| 24 | references/method/components-state.md | [book:angular-dev], “Using signals in components” | Derived note: signal and computed manage component state | supported | |
| 25 | references/method/components-state.md | [src:agent-ready-web/report.md], “UC5d — Extraction review interfaces.” | Derived note: review flows need confirmation and correction logging | supported | |
| 26 | references/method/components-state.md | [book:d3js-in-action], “D3 is about deriving the appearance of web page elements from bound data” | Visual marks derive from bound data, not hard-coded copies | supported | |
| 27 | references/method/components-state.md | [src:graphics-motion/report.md], “F2. 2D rendering choices.” | Renderer thresholds (SVG/Canvas/WebGL) are measured research output | supported | |
| 28 | references/method/components-state.md | [book:playwright-docs], “Assertions” | Auto-retrying assertions verify rendered element states | supported | |
| 29 | references/method/layout-css.md | [book:css-in-depth-2e], “4 Flexbox” | Flexbox lays out elements in rows and columns | supported | |
| 30 | references/method/layout-css.md | [book:css-in-depth-2e], “5 Grid layout” | Grid layout underpins the base-layout guidance | supported | |
| 31 | references/method/layout-css.md | [book:css-in-depth-2e], “7 Responsive design” | Breakpoints chosen per design; container queries style by container size | supported | |
| 32 | references/method/layout-css.md | [src:platform-apps/report.md], “F7. Styling, component primitives, design tokens, data and state.” | Keep inherited styling system; token file generates custom properties | supported | |
| 33 | references/method/layout-css.md | [book:wcag-22], “Success Criterion 1.4.10 Reflow” | Content reflows at 320 CSS px without loss or 2-D scrolling | supported | |
| 34 | references/method/layout-css.md | [book:css-in-depth-2e], “2.6 Custom properties (aka CSS variables)” | Custom properties declare reusable values, reducing repetition | supported | |
| 35 | references/method/layout-css.md | [book:css-in-depth-2e], “8 Cascade layers and nesting” | Layers organize reset, theme, component rules; explicit cascade control | supported | |
| 36 | references/method/layout-css.md | [book:css-in-depth-2e], “1.5.1 Using the cascade for progressive enhancement.” | Unknown declarations ignored; base experience keeps working | supported | |
| 37 | references/method/layout-css.md | [src:platform-apps/report.md], “F1. Web platform features, 2023–2026” | Feature status is a dated snapshot; re-check live status | supported | |
| 38 | references/method/layout-css.md | [book:web-dev-baseline], “How to choose your Baseline target” | Guidance exists for choosing a Baseline support target | supported | |
| 39 | references/method/layout-css.md | [doc:https://web.dev/baseline/] | Check live feature status; support target; fallbacks for limited features | supported | |

## Verdict summary

- 38 supported, 1 overstated (#5), 0 unsupported, 0 derived-unlabelled.
- Derived claims are labelled "(derived: …)" and their citations genuinely ground them, so they are recorded as supported.

## Portability check

```
grep -rnE 'dataviz|design-taste-frontend|minimalist-ui|high-end-visual-design|redesign-existing-projects|frontend-design|batch-photo-retouching|Read tool|Bash tool|subagent_type' /Users/GaryT/Documents/Work/lab/design-programme/briefs/runs-3-5/scratch/ca-frontend-r1-2-134716/SKILL.md /Users/GaryT/Documents/Work/lab/design-programme/briefs/runs-3-5/scratch/ca-frontend-r1-2-134716/references/method
```

Output: no matches (grep exit 1). None of the tracked cross-skill or tool-specific terms appear in `SKILL.md` or `references/method/`.

## Coverage

- Pre-audit `check_claims.py --sources` reported 171 citations, 171 unaudited for the whole skill; this file audits all 39 unique (file, anchor) pairs in the s2 scope (brief-baseline.md, components-state.md, layout-css.md).
- Citations not reached: none.
