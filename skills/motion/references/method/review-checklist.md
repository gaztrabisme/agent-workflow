# Review checklist: ten tests for motion plans and renders

Run exact code checks first. Then ask a fresh-context reviewer who did not make the work and can see the rendered artifact. A missing reviewer means a vision result is **not judged**.

## Tests

| # | Test | Pass condition | Return to |
|---|---|---|---|
| T1 | Purpose and evidence | Receiver, message, desired response, runtime and production time are stated; every factual claim has a source or is marked open. | Stage 1: intent and evidence |
| T2 | Premise and tone | A reader can state the subject, function and intended tone without confusing the premise with a production technique. | Stage 2: story and tone |
| T3 | Structure and message | A reviewer can explain the message from the event order; a non-linear structure still provides a comprehensible path. | Stage 2: story and tone |
| T4 | Storyboard and continuity | Panels cover the necessary story beats; framing gives needed information; each transition has a continuity or narrative reason. | Stage 4: storyboard and animatic |
| T5 | Visual system and encoding | Required facts map to declared visual forms, data values/proportions match their source, and repeated elements follow the declared system. | Stage 3: visual direction |
| T6 | Timing and reading | The animatic meets the requested runtime, and a reviewer can read each information group before it changes. | Stage 4: storyboard and animatic |
| T7 | Motion purpose and character | Every major movement has a stated purpose; the reviewer recognizes the intended movement character and attention path. | Stage 5: choreography |
| T8 | Curves and choreography | The motion reaches intended poses without unwanted overshoot; triggers, leaders and followers occur in the stated order. | Stage 5: choreography |
| T9 | Transition, loop and cutoff | Scene joins support the story; a seamless loop joins at the intended pose or a planned jump reads as intentional; no required motion is cut off. | Stage 5: choreography |
| T10 | Render and delivery | `scene-engine validate` passes; rendered dimensions, frame rate, duration, audio/caption presence and file path match the delivery contract. | Stage 6: review and handoff |

## Recheck after a fix

- A story, premise or source-data change reruns T1–T6 and affected later tests.
- A storyboard, scene duration, or transition change reruns T4, T6, T8–T10 as applicable.
- A curve, pose, trigger, or layer timing change reruns T6–T10 as applicable.
- A render setting or asset change reruns T10 and the visual questions that depend on the affected frames.

The return stage identifies where to repair the cause. Do not patch a late render when the failed decision belongs earlier in the story, information or visual system.
