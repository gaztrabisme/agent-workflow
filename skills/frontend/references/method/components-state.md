# Components and state in the project's framework

## Follow the installed framework

Read the installed React or Angular version and the project's local conventions before writing components. Use matching official docs and current framework types; do not copy a pattern from a different major. Inherited code should keep its framework, version, styling approach, state model, and test runner unless an audit identifies a concrete blocker. [src:platform-apps/report.md], “F5. Principles that transfer across frameworks”; [book:react-dev], “Your First Component”; [book:angular-dev], “Components and directives”; [book:angular-up-and-running], “Creating a Component.”

Keep component boundaries useful to the project: components should express reusable behavior or a meaningful visual unit, while data access and side effects remain explicit. Use the framework's standard event, input, and state mechanisms; avoid adding a second store or a new UI dependency to solve a one-off need. [src:platform-apps/report.md], “F7. Styling, component primitives, design tokens, data and state”; [book:fluent-react], “Immutable state”; [book:angular-dev], “Keep components and directives focused on presentation.”

## Model UI state deliberately

Represent related state together, avoid contradictory or duplicated fields, and derive values that can be computed from the source state. In React, render components as pure functions of props and state, and synchronize with external systems only when needed. [book:react-dev], “Choosing the State Structure”; [book:react-dev], “Keeping Components Pure.”

Use TypeScript types that reflect domain concepts and narrow data from network, storage, or model output before using it. Prefer a safe unknown value at untrusted boundaries over an unchecked assertion or broad any. [book:effective-typescript], “Item 36: Use a Distinct Type for Special Values”; [book:effective-typescript], “Item 41: Name Types Using the Language of Your Problem Domain”; [book:effective-typescript], “Item 46: Use unknown Instead of any for Values with an Unknown Type”; [book:effective-typescript], “Item 59: Use Never Types to Perform Exhaustiveness Checking.”

For async and review flows, specify idle, loading, success, empty, error, and pending-confirmation states where applicable. Each state should have meaningful content, available actions, and accessible status feedback; partial data and retry behavior should not be left implicit. (derived: [book:react-dev], “State: a component's memory”; [book:angular-dev], “Using signals in components”; [src:agent-ready-web/report.md], “UC5d — Extraction review interfaces.”)

For a chart implementation, preserve the supplied data mapping and keep visual marks driven by their data rather than hard-coded copies. D3's data-binding examples are useful implementation background; chart meaning and renderer selection remain with information-design and the project. [book:d3js-in-action], “D3 is about deriving the appearance of web page elements from bound data”; [src:graphics-motion/report.md], “F2. 2D rendering choices.”

## Make each state testable

For each key component, list its inputs, state transitions, keyboard path, visible feedback, and side effects. Test meaningful transitions with the project's browser or component test setup. Use the project's framework docs and official migration tools for a needed upgrade, and separate a major upgrade from feature work. [src:platform-apps/report.md], “F5. Principles that transfer across frameworks”; [book:playwright-docs], “Assertions”; (derived: route each failed assertion to its state or component owner.)
