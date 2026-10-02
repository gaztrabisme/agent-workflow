# Accessibility

## Choose and name the target

Use WCAG 2.2 AA as the default engineering target, unless the project brief or contract specifies another standard. This is a build target, not a claim of legal compliance; legal obligations depend on jurisdiction, service type, and contract. The research found standards and dates differ across jurisdictions, so confirm those details with the project owner rather than infer them from a general accessibility target. [book:wcag-22], “5. Conformance”; [src:gaps/report.md], “G1. Accessibility law by deliverable type and jurisdiction.”

Build access into structure and state: semantic HTML, visible labels, logical reading order, keyboard operation, clear focus, useful error feedback, and working zoom and reflow. For a custom widget, use the APG pattern as an interaction specification and test each required key and state. [book:wai-aria-apg], “Button Pattern”; [book:wai-aria-apg], “Dialog (Modal) Pattern”; [book:web-accessibility-cookbook], “6.2 Make Elements Focusable”; [book:practical-web-accessibility], “Semantic Markup.”

When an action disables or removes its own control, move focus to the next logical available control or to the resulting status/heading, and assert the focus destination in the keyboard test. Native control keys can differ by operating system and browser: choose a supported path such as select type-ahead, assert value and focus, and manually test the platform's native popup behavior on each target platform. (derived: dogfood 2026-10-02, F10)

## Check the WCAG criteria that apply

For text contrast, WCAG 2.2 SC 1.4.3 requires 4.5:1 for normal text and 3:1 for large-scale text, subject to the criterion's exceptions. SC 1.4.11 requires 3:1 for the visual information needed to identify active controls and states against adjacent colors. [book:wcag-22], “Success Criterion 1.4.3 Contrast (Minimum)”; [book:wcag-22], “Success Criterion 1.4.11 Non-text Contrast.”

Test reflow at 320 CSS pixels wide for content designed to scroll vertically; check that the primary action remains available and content does not require two-dimensional scrolling except for content that qualifies for a WCAG exception. Check that keyboard focus is visible and not entirely hidden by sticky headers, dialogs, or overlays. [book:wcag-22], “Success Criterion 1.4.10 Reflow”; [book:wcag-22], “Success Criterion 2.4.7 Focus Visible”; [book:wcag-22], “Success Criterion 2.4.11 Focus Not Obscured (Minimum).”

SC 2.5.8 sets a 24 by 24 CSS pixel minimum target size for pointer inputs with defined exceptions. Treat it as a conformance floor and consider larger touch targets where the design permits. [book:wcag-22], “Success Criterion 2.5.8 Target Size (Minimum)”; (derived: use spacing or an equivalent target for constrained dense controls where the criterion allows an exception.)

Honor the reduced-motion preference and keep interaction feedback and necessary state changes understandable when decorative movement is reduced or removed. Recheck text and control contrast in every theme or palette variant. [book:mdn-web-docs], “prefers-reduced-motion”; [book:wcag-22], “Success Criterion 1.4.3 Contrast (Minimum)”; [book:wcag-22], “Success Criterion 1.4.11 Non-text Contrast”; [src:platform-apps/report.md], “F2. Una Kravets, ‘Modern UI Patterns’, CSS Day 2026 — five UX principles.”

## Use automation and human review together

Run the available automated accessibility analyzer on key routes and states, then manually exercise keyboard navigation and inspect the accessibility tree. Automated analysis catches only a portion of accessibility problems; do not report a page as fully accessible because a tool returns zero findings. [book:playwright-docs], “Accessibility testing”; [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.”

Report the standard, routes, states, tools, and manual interactions checked. Mark untested screen-reader combinations or unavailable user testing as not-judged instead of implying they passed. (derived: [book:wcag-22], “5.2 Conformance Requirements”; [book:practical-web-accessibility], “Accessibility Tree.”)
