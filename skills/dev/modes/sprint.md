# Sprint Mode

Coordinate multiple engineering items as reviewable work units. Keep their dependencies visible, group changes around ownership and project boundaries, and verify each finished wave before starting dependent work.

## Classify and shard

Classify each item by how it should be executed:

| Type | Meaning | Execution |
|---|---|---|
| Mechanical | The exact edit is predictable without reasoning separately about each file | Structured edit pattern; no reasoning agent |
| Surgical | Targeted change with clear scope | Coordinator-direct |
| Constructive | New behavior or logic | Build mode |
| Exploratory | Cause or scope is not known | Assess or focused research |

Treat work as mechanical only when each exact edit is predictable. Read two or three representative files, record the pattern and its exceptions, then create a structured edit list before applying changes. If a file requires a context-dependent choice, use constructive work for that item instead. [book:software-engineering-at-google], Heterogeneity; [book:software-engineering-at-google], What Is a Large-Scale Change?

Before authorizing fan-out, explain the change to an engineer unfamiliar with it in a concise FAQ and proposed change description. Then apply safe replacements and run each resulting shard through the project's CI before submission. A local build or lint may catch an early problem, but it does not replace the CI checks that prove the shard in its actual integration environment. If changes require per-file reasoning, have an implementation worker handle that work rather than forcing it into a replacement list. [book:software-engineering-at-google], Authorization; [book:software-engineering-at-google], Change Creation; [book:software-engineering-at-google], Sharding and Submitting

Shard multi-file work around project boundaries and ownership so each resulting change can be submitted atomically. Represent dependencies in a directed acyclic graph, identify which units unblock others, and schedule the compatible shards in waves; do not bundle unrelated ownership areas merely because they are sequential. [book:software-engineering-at-google], Sharding and Submitting; [book:continuous-delivery], Managing Dependency Graphs

Name the wave membership and dependency for each item. If assessment feeds implementation, place it before the affected build work. Put shared-file edits together or schedule them sequentially to avoid concurrent writes. [book:continuous-delivery], Managing Dependency Graphs

## Execute in waves

Run mechanical items with the structured edit pattern, surgical items directly, constructive items through Build, and exploratory items through Assess or research. For constructive items, classify weight, apply the TDD decision, select useful independent roles, and run planned gates. The failing-test step grounds TDD; the item weight and worker choice remain this skill's process. [book:learning-test-driven-development], Red-Green-Refactor: The Building Blocks of TDD

After each independent shard is ready, run it through the project's CI before submission. A local build or lint may catch an early problem, but it does not replace the CI checks that prove the shard in its actual integration environment. [book:software-engineering-at-google], Sharding and Submitting

Do not let a red test sit until a later wave. Triage new and pre-existing failures promptly. After each wave, run backend tests, the frontend build where relevant, regression checks, and test-health triage; do not start the next dependent wave until results are clean or every failure has a recorded disposition. [book:software-engineering-at-google], Write, Run, React

Run every gate planned for an item. If one cannot run, state the reason before marking the item complete. A check list makes repeated work consistent; the explicit skip rule is dev's coordination practice. [book:site-reliability-engineering], The Launch Checklist

Track useful, measurable milestones that show delivered value, not only that a wave ended. Report progress at wave milestones, a contradiction, or another decision point. [book:software-engineering-at-google], Milestones

### Close the sprint

Before completion, write a batch summary to the project log and reconcile every item in active work as done, deferred or blocked. Name the remaining gates and the evidence for any item that did not pass.

Treat CRITICAL findings as progression blockers. Treat QUALITY findings as advisory and let the user choose whether to fix, defer or accept them. [book:looks-good-to-me], Blocking issues; [book:looks-good-to-me], Nonblocking issues
