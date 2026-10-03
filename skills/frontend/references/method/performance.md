# Performance

## Set a product budget before optimizing

Ask which pages and interactions matter, under what device and network conditions, and what performance budget the product owner accepts. Measure a representative baseline before tuning. Performance trade-offs depend on the workload and the people using it; a single synthetic score does not describe every user or route. [book:web-performance-engineering], “Evaluating UX Performance: Key Metrics”; [book:web-performance-engineering], “Setting Up Performance Budgets and Alerts”; [book:web-performance-in-action], “1.1.1 Web performance and the user experience.”

Use the Core Web Vitals as field targets where real-user measurement is available: at the 75th percentile, LCP at or below 2.5 seconds, INP at or below 200 milliseconds, and CLS at or below 0.1. INP is the current Core Web Vital for responsiveness and replaces FID; these are web.dev's good field thresholds, not a substitute for a product-specific budget or test of a key interaction. [doc:https://web.dev/articles/inp]; [book:web-dev-baseline], “Defining the Core Web Vitals metrics thresholds”; [book:web-performance-engineering], “Largest Contentful Paint (LCP): Viewing Content Quickly”; [book:web-performance-engineering], “Cumulative Layout Shift (CLS): Visual Stability.”

## Measure and correct causes

Use Lighthouse or browser performance tooling for repeatable lab diagnostics; use field data for production experience when available. Separate the two in the report. If a route has poor loading, responsiveness, or stability, find the costly resources, scripts, layout shifts, or handlers before changing architecture. [book:web-performance-engineering], “Lighthouse: Performance Auditing”; [book:web-performance-engineering], “Chrome DevTools Performance Panel: Deep Diagnostics with AI Assistance”; [book:web-performance-engineering], “Chapter 6. Trade-Offs in Performance Optimizations.”

Preserve image dimensions or aspect ratio to avoid layout shifts. Choose image sizes for their rendered contexts, defer non-critical media, avoid unnecessary client code, and measure the result on the target route. (derived: [book:web-performance-in-action], “6.4 Lazy loading images”; [book:web-performance-in-action], “7.4 Optimizing the loading of fonts”; [book:web-dev-baseline], “Responsive Images.”)

For a repeatable lab run without field data, use a scripted Playwright route: fix browser, viewport, and data fixture; collect LCP and CLS with `PerformanceObserver`; wait for a stable state marker; run each named key interaction at least five times; and record the time from the trusted input event through the next two animation frames plus the state reached. Report the median and slowest sample as an interaction-to-paint lab proxy, not as field INP. Set a product budget before comparing the result, and reserve space for data-driven content or reveal the populated layout in one step to avoid layout shifts. (derived: dogfood 2026-10-02, F7; derived: dogfood 2026-10-02, F13)

Example instrumentation for a Playwright spec; adapt the selector, route, and data fixture to the task. The two-frame timing is deliberately named a lab proxy, not INP.

```ts
type LabWindow = Window & {
  __lab: { lcp: number | null; cls: number; interactionMs: number[] };
};

await page.addInitScript(() => {
  const w = window as LabWindow;
  w.__lab = { lcp: null, cls: 0, interactionMs: [] };
  new PerformanceObserver((list) => {
    const entries = list.getEntries();
    const last = entries.at(-1);
    if (last) w.__lab.lcp = last.startTime;
  }).observe({ type: 'largest-contentful-paint', buffered: true });
  new PerformanceObserver((list) => {
    for (const entry of list.getEntries() as (PerformanceEntry & { value: number; hadRecentInput: boolean })[]) {
      if (!entry.hadRecentInput) w.__lab.cls += entry.value;
    }
  }).observe({ type: 'layout-shift', buffered: true });
  document.addEventListener('click', (event) => {
    if (!event.isTrusted) return;
    const started = event.timeStamp;
    requestAnimationFrame(() => requestAnimationFrame(() => {
      w.__lab.interactionMs.push(performance.now() - started);
    }));
  }, true);
});

await page.goto('/?day=10');
await expect(page.locator('main')).toHaveAttribute('data-state', 'ready');
const next = page.getByRole('button', { name: 'Next day' });
for (let sample = 0; sample < 5; sample += 1) {
  await next.click();
  await expect(page.locator('main')).toHaveAttribute('data-state', 'ready');
}
const lab = await page.evaluate(() => (window as LabWindow).__lab);
const ordered = [...lab.interactionMs].sort((a, b) => a - b);
const medianInteractionMs = ordered[Math.floor(ordered.length / 2)];
console.log({ ...lab, medianInteractionMs, slowestInteractionMs: Math.max(...ordered) });
```

Report browser/version, viewport, route/data, the five sampled actions, and the observed page state beside these values. A slowest sample is a diagnostic for this fixed lab setup, not a field percentile.

(derived: keep optimizations proportionate to the workload and users, applying the trade-off guidance in [book:web-performance-engineering], “Chapter 6. Trade-Offs in Performance Optimizations.”) The book covers CSS and script-loading techniques, but older implementation examples may not fit current browsers or bundlers; validate a proposed optimization in the project's current build and real rendered route. [book:web-performance-in-action], “3.3 Performance-tuning your CSS”; [book:web-performance-in-action], “8.1 Affecting script-loading behavior”; (derived: verify current toolchain behavior before adopting older examples.)
