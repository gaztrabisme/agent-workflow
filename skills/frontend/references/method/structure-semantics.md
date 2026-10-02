# Structure and semantics

## Let the document express the content

Map the page to meaningful HTML before styling it. Use headings for sections, lists for grouped items, links for navigation, buttons for actions, labels with form controls, and native disclosure or dialog elements when their behavior fits. The HTML standard defines element semantics and conformance; native controls already expose established browser behavior and accessibility semantics. [book:whatwg-html], “Semantics, structure, and APIs of HTML documents”; [book:practical-web-accessibility], “Semantic Markup.”

Make the DOM order follow the reading and interaction order. Use landmarks such as header, navigation, main, and complementary content to help people and automation move through the page. Provide descriptive headings and names that distinguish controls with similar visual treatment. [book:wai-aria-apg], “Use ARIA Landmarks”; [book:mdn-web-docs], “Landmark roles”; [book:web-accessibility-cookbook], “1.4 Optimize Rendering Order.”

## Use ARIA only to fill a semantic gap

Prefer a native element when it matches the action. Add ARIA only when the native element cannot expose the necessary role, accessible name, description, or state. When a custom widget is required, follow the relevant APG pattern and implement its keyboard behavior, focus movement, and state updates as part of the component. [book:mdn-web-docs], “Before using ARIA”; [book:wai-aria-apg], “What Are Accessibility Semantics?”; [book:wai-aria-apg], “Developing a Keyboard Interface.”

Keep accessible states synchronized with what the user sees and can do. For example, a disclosure's expanded state, a tab's selected state, or a checkbox's checked state must update with the interface; stale state makes both assistive technology and browser agents act on the wrong structure. [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface”; [book:wai-aria-apg], “WAI-ARIA Roles, States, and Properties.”

## Forms and changing content

Associate each form field with a visible label. Group related controls with a fieldset and legend where appropriate. Connect instructions and errors to the relevant field, announce important asynchronous updates without moving focus unexpectedly, and preserve the user's entered values when an error can be corrected. [book:web-accessibility-cookbook], “9.2 Identify Form Elements”; [book:web-accessibility-cookbook], “9.3 Describe Form Fields”; [book:mdn-web-docs], “ARIA live regions.”

Use the HTML conformance checker and inspect the accessibility tree for the rendered page. A validator can catch markup errors; it cannot decide whether the chosen semantics and reading order make the user task understandable. [book:whatwg-html], “How to catch mistakes when writing HTML: validators and conformance checkers”; [book:playwright-docs], “Accessibility testing”; (derived: pair structural checks with the rendered, task-specific review described in [src:agent-ready-web/report.md], “F4. The accessibility tree as the agent interface.”)
