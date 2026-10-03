# Chart templates

Copy a starter, replace the illustrative data and labels, preserve the `data-rk-*` markup, and update domains, units and source notes. The sample marks are examples only; they are not operational data. Run `bash scripts/check_templates.sh` from the skill root before adapting or shipping a starter. (derived: dogfood 2026-10-02, F1)

| Template | Form | Status and course basis |
|---|---|---|
| [line-chart.svg](line-chart.svg) | Time series with position on both axes | Course-supported: line charts for change over time (4217 · U2 · L03 · 02:18–04:02; 3601 · U3 · L09 · 03:18–07:00). |
| [bar-chart.svg](bar-chart.svg) | Category magnitude comparison | Course-supported form; bar use for lost-time causes is a derived application (4217 · U2 · L03 · 01:32–02:18). |
| [slope-chart.svg](slope-chart.svg) | Start-to-end comparison | Course-supported (3601 · U3 · L09 · 03:18–07:00). |
| [small-multiples.svg](small-multiples.svg) | Repeated views with shared scales | Course-supported; mud-property use is derived (3601 · U3 · L09 · 03:18–07:00). |
| [scatterplot.svg](scatterplot.svg) | Two quantitative variables by position | Course-supported (4217 · U2 · L03 · 02:18–04:02). |
| [bubble-chart.svg](bubble-chart.svg) | Two positions plus a size measure | Course-supported; area is less precise than position and length in the course-cited channel ranking (4217 · U2 · L03 · 02:18–04:02). |
| [radial-series.svg](radial-series.svg) | Repeated radial series | Course-demonstrated custom form; only use when the data and reader can support it (2495 · U4 · L12 · 04:22–09:35). Its custom polar mapping is marked for manual scale review. |
| [drilling-depth-time.svg](drilling-depth-time.svg) | Measured depth against dated reports, depth increases downward; includes measured and planned layers, lost-time intervals and a visible missing-plan message | **Derived** from the drilling fixture and the course's time-series form. (derived: dogfood 2026-10-02, F6) |
| [drilling-lost-time-split.svg](drilling-lost-time-split.svg) | Non-productive time by cause | **Derived** from the drilling fixture and a category comparison. |
| [drilling-mud-properties.svg](drilling-mud-properties.svg) | Mud measurements against vertical measured depth, with the same depth domain, direction and pixel range in each track | **Derived** from drilling fields and the course's shared-scale small-multiple form; units remain distinct by panel. (derived: dogfood 2026-10-02, F6) |
| [drilling-trajectory.svg](drilling-trajectory.svg) | Northing against easting path, with equal metres-per-pixel scales and labelled ticks | **Derived** from the drilling fixture and positional encoding. (derived: dogfood 2026-10-02, F4) |
| [dashboard.html](dashboard.html) | Composed status, key-number tiles, actionable alerts, a missing-plan state and aligned depth views | **Derived** dashboard starter. (derived: dogfood 2026-10-02, F2) |

The drilling views are adaptation examples. Replace their sample values from a project dataset and follow its domain's units, conventions, limits and review rules.
