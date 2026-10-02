# Brief and baseline

## Establish the task and context

Before choosing markup or a framework component, record who uses the interface, the task they need to finish, the content and data involved, the starting point, the successful end state, and what can go wrong. Include the routes and states in scope, supported browsers, viewport and input modes, locale, authentication, network or device constraints, and existing product or domain rules. (derived: the platform research separates controlled render environments from client browsers and gives existing codebases their own preservation rules; [src:platform-apps/report.md], “Rule A: choose the support target by who opens the output”; [src:platform-apps/report.md], “6. Working inside other people's codebases; greenfield.”)

Use the current product brief, UX findings, and project guidance as primary inputs. A visual reference can inform form, but it does not establish behavior or content. Record gaps as assumptions and ask for the evidence needed to resolve them. (derived: [book:css-in-depth-2e], “7 Responsive design”; [book:practical-web-accessibility], “Linear Layouts.”)

## Inspect the project

For an existing application, identify the framework and installed version, router, CSS system, component primitives, test runner, build and lint commands, design tokens, and any route or state-specific conventions before editing. Use documentation matching the installed version. The research found that advice written for a newer framework major can break older applications; preserving the existing conventions is the safe default. [src:platform-apps/report.md], “F5. Principles that transfer across frameworks.”

## Set the browser and device target

Choose a support target from the audience's actual environment. For a client-facing site, do not assume a feature is broadly interoperable because it runs in one current browser. Check the live Baseline status or browser compatibility data for each feature that affects a core interaction; use a fallback or guard for features outside the agreed target. [src:platform-apps/report.md], “Rule A: choose the support target by who opens the output”; [book:web-dev-baseline], “Baseline”; [doc:https://web.dev/baseline/].

Record target browsers, viewport widths, zoom/reflow expectations, pointer and keyboard use, reduced-motion preference, light/dark preference, and representative data. Capture the existing route and key states before a redesign. (derived: [book:css-in-depth-2e], “7 Responsive design”; [book:wcag-22], “Success Criterion 1.4.10 Reflow”; [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.”)

## Brief artifact

Keep a short implementation brief with: audience and main task; routes and state inventory; content/data source; success and failure outcomes; visual references and approved tokens; browser/device support; accessibility target; performance constraints; project commands; acceptance checks; and unresolved questions. (derived: these fields combine the brief inputs needed to test the page against its actual user, data, and execution environment; [book:css-in-depth-2e], “7 Responsive design”; [src:platform-apps/report.md], “F8. Quality: accessibility, testing, performance.”)
