# Greenfield default

Use this named default for a new, small web app when the brief does not choose a framework. Keep the project dependency-light and use native HTML controls.

## Stack

- No UI framework: semantic HTML, CSS, and TypeScript.
- Node.js 24 or later; a small static server built with Node's `http` module.
- TypeScript 5.9.3 compiles `src/` into browser JavaScript under `public/js/`.
- Playwright Test `@playwright/test` 1.63.0 for browser behavior and `@axe-core/playwright` 4.13.0 for automated accessibility checks. These match render-kit's Playwright 1.63.0 and axe-core 4.13.0 pins (derived: dogfood 2026-10-02, F1).
- Pin exact dependency versions and commit `package-lock.json`. Install the matching browser once with `npx playwright install chromium`.

## Project scripts

Provide these entry points in `package.json`:

```json
{
  "type": "module",
  "scripts": {
    "build": "tsc -p tsconfig.json",
    "start": "npm run build && node server.mjs",
    "test": "npm run build && playwright test",
    "typecheck": "tsc -p tsconfig.json --noEmit"
  },
  "devDependencies": {
    "@axe-core/playwright": "4.13.0",
    "@playwright/test": "1.63.0",
    "typescript": "5.9.3"
  }
}
```

The static Node server serves `public/` on `127.0.0.1` and does not need a runtime package. Change the port through an environment variable and bind only to the local interface for a local tool. Add project-specific server, data, and test helpers only when the brief requires them.

## Start from the state template

Use [`../../templates/states.html`](../../templates/states.html) as the markup sketch: it contains distinct loading, empty, ready, and error regions, a `[hidden]` guard, a URL-selected `?state=` example, and a ready marker that can be passed to `rk --wait-for`. Move its CSS and TypeScript into the project structure; do not add a framework solely to reproduce the example. (derived: dogfood 2026-10-02, F1)

The app-shell and semantic-page examples remain available for structure and composition. Tests should assert exactly one state region is visible, the ready marker follows successful initialization, and error/empty states expose the appropriate next step.
