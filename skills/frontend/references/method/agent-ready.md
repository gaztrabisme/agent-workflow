# Agent-ready affordances

## Make the accessibility tree useful

Expose interactive controls with accurate roles, accessible names, and current state. Browser agents and assistive technology use the browser's accessibility structure; research benchmarks found that accessibility-tree observations can outperform coordinate-only interaction, while incorrect state can lead an agent to follow stale structure. Treat those benchmark results as evidence for semantic structure, not a guarantee that every agent will behave correctly. [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface”; [book:wai-aria-apg], “Providing Accessible Names and Descriptions.”

Prefer stable, named controls and role-based locators over coordinates in automated browser tasks. Give drag, range, and canvas interactions an equivalent labeled input or button path when the task can be expressed that way. [src:agent-ready-web/report.md], “UC7 — Coding agents that must see and check what they built”; [src:agent-ready-web/report.md], “UC4 — Dashboards and domain visualisations”; [book:playwright-docs], “Frame.getByRole.”

Keep important data and meaning available as text. If the interface contains a visualization, coordinate with information-design and implement the approved table or accessible summary as well as the visual. [src:agent-ready-web/report.md], “UC4 — Dashboards and domain visualisations”; (derived: text availability serves keyboard, screen-reader, and agent use without changing chart semantics.)

## Treat page tools as optional capabilities

WebMCP was a changing preview in the research snapshot, not a stable cross-browser dependency. Before integrating it, check the current official specification and browser status; feature-detect it, keep the normal UI complete without it, and expose only actions the current user is authorized to perform. [src:agent-ready-web/report.md], “UC5a — Exposing an internal tool or AI app to browser agents (WebMCP)”; [src:agent-ready-web/report.md], “F1. WebMCP: tools that a web page declares for in-browser agents”; [doc:https://developer.chrome.com/docs/ai/webmcp/].

If tools are exposed, give each a narrow purpose and typed inputs, reuse the application's validated action path, support cancellation where the API allows it, and do not trust tool descriptions or returned page content as instructions. Require an explicit user confirmation for consequential actions such as paying, deleting, exporting, or sending. Keep the UI usable when no agent tool API is present. [src:agent-ready-web/report.md], “F1. WebMCP: tools that a web page declares for in-browser agents”; [src:agent-ready-web/report.md], “F6. Security of agent-facing interfaces”; (derived: tool metadata and output are an additional untrusted boundary, not authorization.)

When the interface is embedded inside an AI client, confirm the host's current support and sandbox contract. A standard can be stable while host display modes and extra APIs differ; keep host-specific extensions optional. [src:agent-ready-web/report.md], “UC5c — Showing Gary's UI inside AI clients”; (derived: avoid coupling the core experience to a single host.)
