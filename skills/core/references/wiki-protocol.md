# Wiki Protocol

Project memory is an agent-maintained record of decisions, findings, work state, and links between artifacts. Use the project's established wiki location; do not bind initialization to one agent harness.

## Source boundaries and canonical pages

- Keep raw source material immutable during wiki operations. [book:building-applications-ai-agents], Data Provenance and Integrity.
- Give wiki pages an owner and a maintenance process; ownerless pages become stale and duplicate. [book:software-engineering-at-google], Callout: The Google Wiki.
- Keep one canonical, versioned source for shared material; link to it from role-specific material instead of maintaining divergent copies. [book:building-design-systems], Define the Sources of Truth.
- Before removing or changing an existing structure, find out why it exists. [book:software-engineering-at-google], Understand Context.
- Add structure only after a real failure shows the absence caused a problem. [book:continuous-delivery], Adding Capacity Tests to the Deployment Pipeline.
- Keep pages, references, gates, and skills only while real work references them; remove or mark obsolete a page that no longer serves a purpose, with a pointer to current information. [book:software-engineering-at-google], Deprecating Documents.

## Index and journal

- Keep the index a short, purpose-labeled hub of links, grouped by topic; list every page with a one-line summary and update the index on ingest or page creation. [book:software-engineering-at-google], Landing Pages.
- Keep log.md append-only, with dated entries and a consistent prefix that supports search. [book:building-applications-ai-agents], Data Provenance and Integrity.

## Ingest and session protocol

- On first encounter with a project or major area, read the index. If there is no wiki, initialize it, inspect the codebase structure, key files, and existing documentation, and record only what you have actually understood. [book:software-engineering-at-google], How Do Googlers Use Code Search?
- At session start, read the index and current work state; read decision records when a decision is due. During work, update current state and useful findings. Create a topic page when a fact will help later work; link related pages. [book:software-engineering-at-google], Scaling Your Questions: Ask the Community; [book:learning-systems-thinking], Link models to show relationships.
- Brief the user on current status, recent breadcrumbs, and pending items. [book:pmbok-guide-7e], Reports.
- On completion, update the relevant pages with outcomes, append the session entry, and update the index when new pages were created. [book:software-engineering-at-google], Documentation Is Like Code.
- For every mode, at minimum append a dated event to log.md and update active-work.md with current state and next steps. [book:pmbok-guide-7e], 4.6.2. Logs and Registers.
- Keep a standing assumption log for unresolved assumptions and constraints; revisit them as evidence arrives. [book:pmbok-guide-7e], 4.6.2. Logs and Registers.

## Decision records and learning

- Record decisions as Context → Decision, including why alternatives lost and the tradeoff. The cited ADR template instead places Decision before Context; the source comparison leaves this ordering conflict disputed, so do not treat the ADR order as a settled exception.
- The cited ADR template is ordered: ID and Title; Status and Date; Author; Decision; Context; Options considered; Consequences; Advice. Its Decision-before-Context order conflicts with the shared core rule above; the source comparison leaves that conflict disputed. [book:facilitating-software-architecture], The Structure of an ADR.
- Keep a standing Rejected Approaches section with the rejected option and why it lost. [book:facilitating-software-architecture], Options.
- Record decisions and rejected approaches whenever a choice is made. [book:facilitating-software-architecture], Options.
- When a shipped direction is reverted, record the mechanism of failure as a reusable lesson. [book:site-reliability-engineering], Keep a History of Outages.
- Treat failure retrospectives as blameless learning records: explain what happened, what conditions enabled it, and the follow-up that can prevent recurrence. [book:site-reliability-engineering], Part III. Practices.
- For a shared rule or skill change, identify a later-use signal that would show whether the change improved work, then revisit it after use. [book:learning-systems-thinking], Feedback Loops Include Learning.

## Health, freshness, and link integrity

- Give maintained pages an owner and last-reviewed date; use metadata reminders when a page goes untouched rather than relying on a session-count threshold. [book:software-engineering-at-google], Deprecating Documents.
- Run a health check when requested. Review whether old pages remain accurate. [book:software-engineering-at-google], Documentation Is Like Code.
- Check for contradictions between pages. [book:building-applications-ai-agents], Coherence.
- Find indexed pages that nothing links to and link them to relevant context or remove them if they no longer serve a purpose. [book:learning-systems-thinking], Link models to show relationships.

## Living state and tailoring

- Rewrite and prune living state pages as the project changes; keep chronological journals append-only. [book:continuous-delivery], Project Lifecycle.
- Tailor processes, tools, and artifacts, including the wiki page set, to project characteristics. Create non-default pages only when their content recurs; do not force every default page into every project. [book:pmbok-guide-7e], Tailor Based on Context.

## Roll-ups, dates, and source records

- Update any parent roll-up in the same session as the source record.
- Before relying on a roll-up for a consequential decision, open the dated source entry it summarizes. [book:research-methods-psychology], Chapter 1: Psychology Is a Way of Thinking.
- Verify a roll-up's claim that an issue is still open against its source record.
- Date-stamp each claim rather than using a section-level date to imply all its content is current. [book:facilitating-software-architecture], Meta-Elements.
- Rewrite a superseded roll-up claim; do not append a newer claim underneath it and leave both standing. [book:facilitating-software-architecture], Further ADR Resources.
- Write specific findings as breadcrumbs, not activity descriptions. [book:site-reliability-engineering], Keep a History of Outages; [book:learning-systems-thinking], Be Missouri.
- Link to an existing page when writing about its concept. [book:learning-systems-thinking], Link models to show relationships.
