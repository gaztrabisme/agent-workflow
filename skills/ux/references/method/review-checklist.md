# Review checklist

Run the checks that apply to the request. For each failure, state what was observed, change the owning stage, and rerun affected checks. Thresholds and course procedures are detailed in [measurement.md](measurement.md).

| Test | Pass condition | Return to stage |
|---|---|---|
| **T1 — Outcome and constraints** | The brief names the user and task, problem, user outcome, business outcome, key assumption, and known development constraints. | Stage 1 — Frame the outcome and the brief |
| **T2 — Evidence and assumptions** | Decision-changing user claims cite a source or are marked as assumptions; the method answers the stated research question; counts are not used to claim causes. | Stage 2 — Research and evidence |
| **T3 — Research synthesis and user model** | Findings retain their source context; provisional profiles are marked; persona goals connect to a real task. If a proto-journey is used, it has five to eight steps and a small set of marked opportunities. | Stage 3 — Synthesize user needs |
| **T4 — Scope and learning** | Each selected feature maps to a user need; the MVP tests a named assumption; business value and effort are visible; priority scores remain discussable inputs. | Stage 4 — Prioritize scope |
| **T5 — Information and route** | Content labels and hierarchy support findability; the task has an entry point, happy path, relevant branches, and completion state; journey and flow serve distinct purposes. | Stage 5 — Map content and flows |
| **T6 — Prototype and fit** | Fidelity suits the question; realistic copy is present in tested states; applicable render-kit checks have no unresolved failures. | Stage 6 — Prototype with real content |
| **T7 — Interaction copy** | Each message fits its state and goal; errors explain the issue and recovery; labels describe the action that actually occurs; language is understandable and useful. | Stage 7 — Write interface content |
| **T8 — Voice and tone** | Voice remains recognizable across the flow; tone fits the user's situation and does not blame or mock the person. | Stage 7 — Write interface content |
| **T9 — User test** | The pilot uses the prototype and real task; outcomes and observed behavior are recorded for each participant; the facilitator remains neutral. | Stage 8 — Test, access, localize, and iterate |
| **T10 — Accessibility and localization** | Required labels and help are available in an understandable order; meaningful images and icons have useful names; text is live; localization receives flow, context, style, terminology, and alternatives. | Stage 8 — Test, access, localize, and iterate |
| **T11 — Learning and iteration** | Results are compared with a stated outcome; measured and judgment-based checks are distinguished; the next change or test is recorded. Missing target or evidence is reported as inconclusive. | Stage 8 — Test, access, localize, and iterate |

## Questions for the fresh-context vision review

Give the reviewer the rendered artifact and ask only questions relevant to the artifact:

- Can a person tell what this screen or flow is for and what to do next?
- Does the content appear where it is needed, and does it fit alongside the controls and other visual elements?
- Can a person follow the task from its entry point through the outcome, including the shown branches?
- Does each error or empty state explain the situation and make a useful next step visible?
- Do the copy and interaction feel coherent across the flow, with tone that fits each situation?
- Do any wording, hierarchy, or layout choices obscure information a person needs before acting?

Use a screen reader and keyboard interaction for T10; a static image review cannot establish spoken order or control access. A missing vision reviewer means the applicable visual questions are **not judged**.
