# Skill Authoring Checklist

Run top to bottom for a new skill; use the refine path for an existing one. Each step is a gate by artifact: name what you produced and how it was checked. [book:continuous-delivery], Chapter 7: The Commit Stage

## 1. Decide it should exist

- [ ] The competency recurs, has a distinct trigger and audience, and is not already owned by a sibling. Otherwise add a reference or hand-off. [book:infrastructure-as-code], Pattern: Bundle Module; [book:infrastructure-as-code], Antipattern: Unshared Module
- [ ] Extract shared machinery only when at least three consumers need it. [book:infrastructure-as-code], Pattern: Bundle Module
- [ ] Classify it as **authored** (grounded in the skill's own real practice) or **distilled** (built from documents or methodology). A distilled skill starts `PENDING`; its EVOLUTION validation list must include checking the claims in real use, and internal consistency alone cannot settle it.
- [ ] When distilling a book, course, or talk series, follow `distill-course.md` with this checklist.
- [ ] Keep an evolution loop even when the skill is authored from fire-tested practice. (field rule)

## 2. Ground in what exists

- [ ] Read `../../core/SKILL.md` and each sibling the new skill will touch. Record `Grounded: read core + <siblings> → <conventions/references reused>`. [book:facilitating-software-architecture], Your Radar’s Place in an Advice Process
- [ ] Reference the shared spine at `../../core/references/…`; add only content specific to this skill. [book:facilitating-software-architecture], Chapter 4. The Architecture Advice Process
- [ ] Find the canonical source for each shared convention. When documents conflict, designate one authority and consolidate duplicates into it or mark them obsolete. [book:software-engineering-at-google], Documentation Is Like Code
- [ ] Check whether the existing subject material is a collection or an operating system before deciding to merge or create a separate skill; record the decision and why. [book:facilitating-software-architecture], Your Radar’s Place in an Advice Process

## 3. Write the frontmatter (trigger contract)

- [ ] Make `name` match the skill directory. (field rule)
- [ ] Write a retrieval description with what the skill is, concrete `USE WHEN` situations, user-typed `Keywords:`, and a disambiguation line wherever a sibling overlaps. Leave room for retrieval terms instead of marketing prose. (field rule)
- [ ] Compare sibling descriptions for overlapping trigger verbs. If two skills could fire on the same turn, disambiguate their artifact and audience. The original `core` and `skill-builder` descriptions once used the same trigger; the collision was found in dogfood. (field rule)
- [ ] Ask whether the description would retrieve this skill for the right task and exclude neighboring work. (field rule)

## 4. Write SKILL.md (the shape)

- [ ] Start from `references/templates/SKILL.md.skeleton`; fill its canonical headers so skills remain easy to scan and compare. [book:software-engineering-at-google], Design Docs
- [ ] Include identity, trigger ownership and sibling hand-offs, principles, an at-a-glance flow, declared gates, anti-patterns, composition, and references. Order the sections so readers can stop after the part they need. [book:facilitating-software-architecture], Chapter 6. Architectural Decision Records
- [ ] Disambiguate every trigger overlap by artifact and audience. (field rule)
- [ ] Link each reference or template from `SKILL.md`; do not ship or list orphans. [book:software-engineering-at-google], Guiding Principles

### Draft, then edit

Draft the whole section or digest before editing it. Then make separate passes for claim accuracy, citation and link integrity, audience clarity, and writing consistency; each pass checks one property. Keep editing time in the plan instead of polishing while the structure is still incomplete. [book:hbr-guide-business-writing], Divide the writing process into four separate tasks

## 5. Declare the gates in the skill's terms

- [ ] Name the grounding substrate and link `../../core/references/grounding-gate.md`.
- [ ] Name the primary output and completion evidence; link `../../core/references/output-contract.md` and `../../core/references/wiki-protocol.md`.
- [ ] Declare pushback and teaching; link `../../core/references/pushback-and-teach.md`. Push back to improve the situation and teach the better move, not to win. [book:learning-systems-thinking], Create Space for Your Reactions
- [ ] State the approach and any independent-review lanes; mark the declaration skippable for single-actor work when appropriate. `core` §7 defines the shared declaration.
- [ ] Search the new skill for exact gate prose from core's canonical references. A copied passage is a defect; retain the link instead. (field rule)

## 6. Dogfood with a fresh-context reviewer

- [ ] Use `templates/dogfood-brief.md`; do not improvise a thinner brief. It supplies the real task, context, review questions, pass condition, and evidence location. [book:site-reliability-engineering], Chapter 1. Introduction
- [ ] Have a fresh-context reviewer use the skill on a real task and produce real artifacts. The reviewer should not be the person who built the artifact. [book:looks-good-to-me], Lack of unbiased perspective
- [ ] Ask for a blunt, severity-ranked critique of the artifact. Keep it professional: be hard on the work, defer when approaches are equally valid, and suggest alternatives when the approach is deficient. [book:looks-good-to-me], You have the influence; [book:software-engineering-at-google], Code Review Best Practices
- [ ] Cover triggering, gaps, friction, contradictions, overreach, actionable gates, cross-references, and honesty. Name the most important missing thing. (field rule)
- [ ] Fold findings back into the skill and verify the repaired cross-references. [book:site-reliability-engineering], Chapter 13. Emergency Response
- [ ] Do not ship without an evolution record and the required real-use pass. Dogfooding lets the author adopt a change before asking others to rely on it. [book:building-secure-reliable-systems], Chapter 21. Building a Culture of Security and Reliability

## 7. Wire into the constellation

- [ ] Add forward and return links so readers can enter the workflow from the relevant neighboring skills. Update this skill's references when the build produces a reusable convention. [book:facilitating-software-architecture], Updating Your Blips
- [ ] Keep the skill narrow. Split unrelated responsibilities before a shared container accumulates everything. [book:facilitating-software-architecture], Chapter 4. The Architecture Advice Process

## 8. Ship + record

- [ ] Set up the skill's own repository and `.gitignore` together, before the first commit; ignore `.DS_Store`. [book:pro-git], Ignoring Files
- [ ] Run exact, automated checks before review and make failures fast and useful. Keep the cheap gate under five minutes where practical and no longer than ten without a reason. [book:continuous-delivery], Chapter 7: The Commit Stage
- [ ] Run `npx -y skills-ref@latest validate <skill-path>` before calling the skill done. The validator checks the Agent Skills format.
- [ ] Meet the specification: `name` matches the directory; `description` is at most 1024 characters and contains `USE WHEN` and keywords; `SKILL.md` stays under about 500 lines; declare a license for public skills. [book:swebok], Chapter 10: Software Quality
- [ ] Add `EVOLUTION.md` from the shared skeleton with the birth, sources, dogfood findings and fixes. Set the entry to `PENDING`; do not settle it as `KEEP` until at least two independent real uses. Record authoring decisions with the advice and reason that led to them. [book:facilitating-software-architecture], Chapter 6. Architectural Decision Records
- [ ] Commit with a clear message. [book:pro-git], Commit Guidelines

## Refine (existing skill) — minimal path

- Re-ground in core and touched siblings, run the dogfood path, and record the evolution entry. Never skip the entry.
- Route structural changes—new references, split or merge, frontmatter, wiring, publishing—to skill-builder. Route changes driven by real traces, recurring skipped gates, contradicted substrate, or open verdicts to `evolution`. If both apply, do the structural work here and hand off trace harvesting.
- Back every structural change with a sound reason, whichever ledger owns the follow-up. [book:learning-systems-thinking], The Paradigm We Work In
- Classify the change by reversibility first. Most changes are reversible: use the light real-use path by default, and reserve a full fresh-context dogfood for changes that are irreversible or can fail silently. A real-use trace substitutes for fresh dogfood only when failure is reversible and loud. [book:facilitating-software-architecture], Chapter 12. The Art of Deciding
- When a reference becomes obsolete, mark it clearly and point readers to its replacement before removing it. [book:software-engineering-at-google], Deprecating Documents
- A real-use trace can stand in for a fresh-context dogfood only when the change is reversible and fails loud; a new gate, trigger change, distilled claim, or silent failure requires the full dogfood. (field rule)
