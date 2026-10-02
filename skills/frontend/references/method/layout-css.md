# Layout and CSS

## Build a resilient layout

Use the project's design tokens and styling conventions. Build the base layout with normal flow, flexible sizing, grid, and flexbox; add breakpoints where the content or task requires a structural change. Container-based rules are useful when a component must respond to the space it receives rather than the viewport. [book:css-in-depth-2e], “4 Flexbox”; [book:css-in-depth-2e], “5 Grid layout”; [book:css-in-depth-2e], “7 Responsive design”; [src:platform-apps/report.md], “F7. Styling, component primitives, design tokens, data and state.”

Keep source order meaningful and avoid CSS ordering that contradicts keyboard and reading order. Do not use absolute positioning as the main layout system for content that must grow, translate, or reflow. Check long labels, localization, zoom, and user text at narrow and wide viewports. [book:wcag-22], “Success Criterion 1.4.10 Reflow”; [book:css-in-depth-2e], “7 Responsive design”; (derived: stable order and content-driven sizing reduce layout surprises across user settings and form factors.)

## Organize and enhance CSS

Use custom properties for a small set of project tokens and variants. Keep specificity predictable; cascade layers can organize reset, vendor, theme, and component rules when the project already supports that approach. Progressive enhancement should leave the base experience complete when a newer selector or CSS feature is unavailable. [book:css-in-depth-2e], “2.6 Custom properties (aka CSS variables)”; [book:css-in-depth-2e], “8 Cascade layers and nesting”; [book:css-in-depth-2e], “1.5.1 Using the cascade for progressive enhancement.”

Browser support changes. Check the live feature status before adding a feature that affects layout, navigation, form completion, or rendering; specify the audience support target and make limited features optional enhancements with tested fallback behavior. Static feature matrices in research are dated snapshots, not permanent rules. [src:platform-apps/report.md], “F1. Web platform features, 2023–2026”; [book:web-dev-baseline], “How to choose your Baseline target”; [doc:https://web.dev/baseline/].

## Keep visual decisions with their owners

Implement the supplied visual hierarchy, grid, typography, palette, and motion system without inventing new direction when a sibling has already produced it. For a chart, preserve its supplied data mapping and labels; consult information-design for chart semantics, visual-design for composition and type, color-theory for palette and contrast, and motion for choreography. (derived: [visual-design](../../../visual-design/SKILL.md), [color-theory](../../../color-theory/SKILL.md), [information-design](../../../information-design/SKILL.md), and [motion](../../../motion/SKILL.md) own those input decisions.)
