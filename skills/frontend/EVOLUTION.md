# Evolution Log — frontend

The loop turns real use into skill improvements. Harvest source: implementation tasks, redesign audits, rendered reviews, and corrections from independent claim audit.

---

## Evolution 1 — design run birth

### Harvest scope
- **Grounded:** frontend research synthesis and tracks dated 2026-09-26; official docs and supplied books; sibling skills; render-kit and scene-engine owner guides → defined a staged, framework-preserving build and review workflow.
- **Coverage:** one new skill package, two HTML templates, nine method stages, a T1–T20 checklist, and a measurement map.
- **Evidence limits:** authoring-time synthesis only. No independent claim audit or real-use dogfood is claimed in this record.
- **Evidence class:** authoring-time.

### Settled verdicts
| Prior item | Verdict | Evidence and reason |
|---|---|---|
| Initial authored design | PENDING | Await independent claim audit, successful local validation, and at least two independent real uses. |

### Patterns found
1. **Frontend advice ages quickly at browser and framework boundaries** — Impact: H; Effort: M. Evidence: the 2026 platform track records version-sensitive APIs and changing feature status; the skill requires a current support check and preserves the installed stack.

### Hypotheses applied
1. **Stage the implementation and return each defect to its owner stage** — closes ambiguous hand-offs; approved by the skill owner; check-ins: run the acceptance suite, then collect independent audit and real-use evidence.

### Validation plan
| Change | Expected result | Evidence floor | Evidence class | Owner | Revisit date | Status |
|---|---|---|---|---|---|---|
| Method claims and citations | Each cited claim is supported or labeled derived/open | Independent line-by-line audit with evidence packet | authoring-time | Independent auditor | After draft | PENDING |
| Rendered templates and skill package | Both templates pass rk check and package links validate | Acceptance commands in DISTILL-REPORT.md | authoring-time | Author | 2026-10-02 | PASS |
| Operating method | Trigger, stages, tests, and hand-offs work on real projects | Two independent real uses with recorded findings | natural | Skill owner | After first uses | PENDING |

**Verdict: PENDING** — this authored method remains a hypothesis until independent source review and real use meet the evidence floor.

## Evolution 2 — design run dogfood (2026-10-02)

### Harvest scope
- **Grounded:** one real greenfield dashboard build at `lab/design-programme/dogfood/runs-3-5/frontend/`; its [report](</Users/GaryT/Documents/Work/lab/design-programme/dogfood/runs-3-5/frontend/report.md>) and app supplied the trace.
- **Findings:** F1–F15 in the report; F2, F4, and F11 include render-kit-owned behavior routed to unit `rk-fix3` with frontend-side guidance added here.
- **Evidence limits:** one dogfood run; no independent run has settled these changes. Local acceptance checks validate the package and templates, not the broader method.
- **Evidence class:** natural, single-use.

### Patterns found
1. **A project-preserving rule needs a greenfield default:** without one, a new app forces an undocumented stack choice. F1 added the no-framework HTML/CSS/TypeScript, static Node, Playwright, and axe path.
2. **Rendered checks need explicit state and exception contracts:** URL-addressable states, exclusive regions, ignored accessibility patterns, and per-state briefs make the evidence reproducible. F2–F5 and F11 add those contracts; render-kit implementation items are handed over.
3. **Responsive and keyboard checks need a real narrow/platform path:** chart text can shrink below readable size and self-disabling actions can lose focus despite broad reflow and keyboard coverage. F9–F10 add those checks.

### Changes applied
- Added a greenfield default and a state starter; updated source lookup, HTML-link checks, narrow SVG guidance, keyboard focus, INP lab guidance, sibling assumptions, state assertions, and redesign-only T19–T20 wording.
- Added the frontend handoff link to UX (F14).
- Recorded all findings and renderer handoffs in the frontend dogfood fix notes.

### Validation plan
| Change | Expected result | Evidence floor | Owner | Status |
|---|---|---|---|---|
| Package citations and Markdown links | All cited book/src IDs resolve in the source index and all local Markdown links exist | `python3 scripts/check_refs.py . --no-anchor-check` and `npx -y skills-ref@latest validate .` | Author | PENDING |
| HTML templates | Every starter is clean under render-kit | `rk check` for each `templates/*.html` | Author | PENDING |
| Method changes | A later independent front-end use follows the greenfield path, state procedure, responsive chart rule, and keyboard/performance checks without the same defects | Two independent real uses plus recorded findings | Skill owner | PENDING |

**Verdict: PENDING** — one real-use trace prompted reversible edits; a later independent run must test the revised method before any verdict is settled.
