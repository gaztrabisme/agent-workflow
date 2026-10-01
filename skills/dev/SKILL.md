---
name: dev
description: "Engineering design, implementation, code health assessment, and results analysis for engineers and technical leads. USE WHEN software needs a development-ready design, build, fix, refactor, review, or root-cause analysis. Applied ML/CV/NLP problem and experiment decisions belong to applied-ml-problem-solver; client-facing solution architecture and proposals belong to solution-architect. Keywords: idea, software design, spec, build, implement, feature, bug, refactor, audit, code review, code health, analyze, root cause, results."
license: MIT
---

# Dev

Dev produces engineering design records, code changes and code-level verification evidence for engineers and technical leads. It supports four modes: Design, Build, Sprint, and Assess, including results analysis and hardening. Keep project decisions specific, changes reviewable, and verification tied to the behavior or artifact being delivered.

> Inherits the shared operating gates from ../core/SKILL.md. Use its canonical references for grounding, evidence, completion records, confidentiality and reader-focused writing; do not duplicate those gate definitions here.

## When it fires — and when a sibling owns it

- **Dev:** a software idea needs an engineering specification; code must be built, fixed, refactored, or reviewed; codebase health or results need investigation.
- **applied-ml-problem-solver:** ML, CV, or NLP framing and model or experiment decisions. Dev builds from the returned framing.
- **solution-architect:** client-facing solution choices, architecture and proposal responses. Dev implements accepted engineering decisions.
- **delivery:** signed-engagement acceptance, change control and client obligations. Dev supplies code-level evidence for those records.
- **core:** shared integrity, evidence, grounding, writing and durable-record gates. Dev supplies engineering-specific procedures.

> **Disambiguation:** choose by artifact and audience. Dev produces engineering designs, code changes and verification evidence; solution-architect produces a client-facing solution and response pack, while applied-ml-problem-solver owns ML decision records.

## Engineering principles

Keep this skill as concise operating instruction, not implementation code; add structure only when real use exposes a missing step. [book:software-engineering-at-google], Creating the Rules

- Prefer simple, readable code and the least implementation that fully solves the problem. Understand surrounding code, real inputs and failure modes before minimizing the change. Add machinery only after a measured failure shows it is needed; leave a seam when that keeps a later addition cheap. [book:clean-code], What Is Clean Code?; [book:clean-code], Minimal Classes and Methods; [book:continuous-delivery], Programming for Capacity
- Diagnose whether complexity causes a real problem before removing it. Keep trust-boundary validation, data-loss handling, security, accessibility and hardware calibration; those protect against real conditions. [book:continuous-delivery], Programming for Capacity; [book:llm-security-playbook], Training Data
- Give each file a coherent responsibility. Treat file size as a prompt to inspect cohesion and readability, not a pass/fail limit; around 500 lines is a desirable upper bound, not a hard ceiling. [book:clean-code], The Single Responsibility Principle; [book:clean-code], Vertical Formatting
- Prefer standard-library facilities when they solve the need plainly. Add a dependency when its tested capability is worth its security, runtime, compatibility and maintenance cost; decide case by case whether to reuse, fork or implement. Fork only when the scope is demonstrably narrow and its lifetime makes the fork safe; avoid forking interfaces that cross project or time boundaries. [book:seriouspython], Victor Stinner on Optimization; [book:software-engineering-at-google], Considerations When Importing; [book:software-engineering-at-google], Example: Deciding Between Time and Scale
- Avoid speculative abstractions. Add a base class or shared interface when a second real implementation demonstrates the seam; keep core control flow visible and use callbacks or hooks only when required. A small straightforward metric or data loader can be local code, while a mature dependency may be cheaper to carry than to rederive. Treat frameworks as implementation details; keep policy and boundaries clear, and adopt a runtime only when its value exceeds its carrying cost. [book:real-world-software-development], Extending and Reusing Code; [book:software-engineering-at-google], Example: Deciding Between Time and Scale; [book:clean-architecture], Chapter 32 Frameworks Are Details
- Rank candidate data-science work by value and effort, using incremental net revenue against implementation cost to resolve competing projects. For test planning, start where expected impact is high for low effort; do not apply an impact/effort ratio mechanically to every assessment finding. [book:data-science-hard-parts], Working on a Data Science Project; [book:site-reliability-engineering], Creating a Test and Build Environment
- Keep success criteria fixed and surface a blocker if they cannot be met. [book:building-evolutionary-architectures], Fitness Function-Driven Architecture
- Do not commit unless asked. When a commit is authorized, stage explicit paths, exclude .DS_Store, and use the requested coauthor trailer.

## Engineering flow

| Mode | Engineering purpose | Procedure |
|---|---|---|
| Design | Clarify requirements, research unknowns and produce an engineering specification | modes/design.md |
| Build | Implement an accepted engineering decision and produce code-level verification | modes/build.md |
| Sprint | Coordinate multiple engineering items, dependencies and wave evidence | modes/sprint.md |
| Assess / Analyze | Inspect code health or explain observed results, then record evidence | modes/assess.md |

When an ML/CV/NLP decision is needed, use the applied-ml-problem-solver before designing or building around that decision. Keep the experiment record with that skill; Dev takes the framed decision back for implementation. See ../applied-ml-problem-solver/SKILL.md.

## Pattern selection

Before substantive work, state **Pattern: <choice> — <reason>**. Trivial questions and one-line fixes are exempt. For Light work, make a brief, non-mutating scope pass first so you can tell whether the exemption applies; if the task is substantive, declare the pattern before editing. (derived: dogfood 2026-10-01) Choose deliberately among:

- **Coordinator-direct** for small, mechanical or unambiguous work.
- **Subagent chain** for real logic with failure risk when test authorship, implementation, verification or independent review needs separation.
- **Parallel work** for independent streams; the coordinator reconciles and integrates the results.
- **Intrinsic-artifact gate** when the output invariant can be checked mechanically.
- **Simulation or probe first** for costly or hard-to-reverse forks; run the cheapest experiment that resolves the largest uncertainty.
- **Focused research** when an unknown surfaces, before choosing an approach.

The default failure was doing everything inline without considering another pattern. Select coordinator-direct against the alternatives, rather than arriving there by habit. When mixing patterns, name the dominant choice and where another applies. State why fan-out or a subagent chain does not fit when ruling it out. For mechanical work, use representative files and a structured edit list; use constructive reasoning when each file needs a contextual decision. See modes/sprint.md and references/subagent-briefs.md.

## Knowledge Base and invariant gates

For a domain covered by the project's Knowledge Base, search the whole Knowledge Base before design or implementation and record one cite-or-null result in Key Decisions. For APIs and abstractions already in the codebase, use the project's curated reference listing rather than searching the entire codebase for reusable abstractions. [book:software-engineering-at-google], Guidance. Use a follow-up Knowledge Base search, a generated query passage, or extra query terms only when the first search missed because of vocabulary. For current or uncovered material, use web search; for non-KB work, also inspect the code and official documentation. Vet a proven dependency when its tested capability is cheaper than reimplementation, weighing security, runtime, compatibility and maintenance. Skip the Knowledge Base gate only after stating that the domain is not covered.

The Invariant Gate applies only to multi-tenant data, authorization, external or irreversible effects, and crash/restart recovery. Before implementation, record one Key Decisions line per applicable class and name its proving test: identity, effect durability, failure state, guarantee reachability and measurement units. For example, in a multi-tenant build ask which identity the database sees; after a crash, can the system tell whether a side effect occurred; and if a process dies halfway through, can it recover in a usable state? A security-heavy build repeatedly found critical faults in these seams. Treat a qualifying invariant without a reachable named test as a failed gate. Local writes under a caller-controlled output path are not external effects by themselves; apply the class when an effect crosses a trust or ownership boundary, or cannot be reversed by the caller. (derived: dogfood 2026-10-01) [book:growing-oo-software-by-tests], Unit-Testing Synchronization. Add a class when a critical finding exposes a gap; retire one when it stops appearing across projects. [book:postgresql-14-internals], Clients and the Client-Server Protocol; [book:building-event-driven-microservices], Handling FaaS Function Failures; [book:site-reliability-engineering], A Hierarchy of Automation Classes; [book:building-evolutionary-architectures], What Is a Fitness Function?; [book:site-reliability-engineering], Choosing an Appropriate Resolution for Measurements

For data-recovery claims, prove recovery through repeated exercises. [book:site-reliability-engineering], Hope Is Not a Strategy.

For broader negative claims, use a discriminating instrument that the coordinator runs and records; this is dev field practice.

## Engineering completion

Follow ../core/references/output-contract.md, ../core/references/grounding-gate.md, ../core/references/wiki-protocol.md, and ../core/references/pushback-and-teach.md for shared gates. Engineering-specific completion also requires evidence from the produced artifact, not merely proof that an intended command ran. After a system is running, verify observed behavior through a manual interaction, explicit assertion, or output comparison. State which artifact and behavior were checked. [book:continuous-delivery], The Release Candidate; [book:software-engineering-at-google], Verification

Before using a measurement as a gate, confirm the instrument can distinguish the difference being judged. A number called measured must identify its instrument, units, and rerun procedure. A past import-time guard used a guessed value that was 22% low; a green check with the wrong units did not protect the real limit. [book:site-reliability-engineering], Defining Objectives; [book:site-reliability-engineering], Choosing an Appropriate Resolution for Measurements

Do not hide an unfulfilled requirement. A committed gate may be skipped only with a stated reason; skip only for reversible work that fails loudly. For release checks, set the quality standard in the release plan and block progress until tests and scans meet it. For LSC-style bulk edits, omit project-specific presubmit checks that add irrelevant complexity; this is a standing exemption. [book:software-engineering-at-google], Heterogeneity; [book:hands-on-site-reliability-engineering], Test for quality and security

On first entry to a mode, use the project's version-controlled documentation and wiki convention. Keep canonical project guidance in a version-controlled location with a named owner. Keep mode-specific findings in their named project record; before reporting a mode complete, identify the file and confirm it exists. If the project has no in-repository wiki and the reviewed diff must stay focused on code, use a separate version-controlled engagement workspace with a named owner and canonical location, then link the mode record from the change description. If no such controlled location exists, surface that blocker instead of leaving an untracked substitute. (derived: dogfood 2026-10-01) Shared wiki mechanics remain in core. [book:software-engineering-at-google], Callout: The Google Wiki

## References

- modes/design.md — clarify requirements, research, write the engineering design and hand it to Build.
- modes/build.md — scope, implement, test, verify and review a code change.
- modes/sprint.md — classify items, plan dependencies, execute waves and reconcile outcomes.
- modes/assess.md — assess code, analyze results and harden findings.
- references/subagent-briefs.md — task-specific subagent prompts and review protocols.
- scripts/run-tests.sh — test runner wrapper.
- scripts/run-quality.sh — code quality and security scans.
- scripts/run-command.sh — captures verbose command output.
- scripts/analyze.py — codebase summary and assessment scan.
