"""PreToolUse hook on Agent: refuse a sub-agent brief that has no Load section.

A brief passes when it has a line starting with LOAD (any case, may be indented) and,
after it, at least one of: a "Skills:", "Books:" or "Web docs:" line (References form),
"None found:", or "Not applicable:". Exempt: the built-in helper agents listed below,
and prompts that start with "BRIEF-EXEMPT:" plus a reason (verifiers, compilers).
Anything unexpected (bad JSON, other tools) is allowed through, so other tools never break.
"""

import json
import re
import sys

EXEMPT_TYPES = {"claude-code-guide", "statusline-setup", "Explore", "Plan"}
LOAD_LINE = re.compile(r"^[ \t]*LOAD\b", re.IGNORECASE | re.MULTILINE)
FORMS = re.compile(
    r"(Skills:|Books:|Web docs:|References:[ \t]*\S|None found:[ \t]*\S|Not applicable:[ \t]*\S)",
    re.IGNORECASE,
)
EXEMPT_PREFIX = re.compile(r"^\s*BRIEF-EXEMPT:[ \t]*\S", re.IGNORECASE)

REASON = (
    "Brief refused: no Load section. Add a line starting with LOAD before the task, in one of "
    "three forms: (1) References - 'Skills:' / 'Books:' / 'Web docs:' lines naming the skill "
    "reference files and verified book chapters to read first; (2) 'None found:' with the "
    "knowledge-base searches that returned nothing; (3) 'Not applicable:' with a reason. "
    "Take the entries from the project's skill-and-book map (template: docs/brief-template.md "
    "in the project, rule: project skill references/run/lane-plan.md). Checking-only agents "
    "may start the prompt with 'BRIEF-EXEMPT: <reason>'."
)


def decide(payload: dict) -> str | None:
    """Return a refusal reason, or None to allow."""
    if payload.get("tool_name") != "Agent":
        return None
    tool_input = payload.get("tool_input") or {}
    if tool_input.get("subagent_type") in EXEMPT_TYPES:
        return None
    prompt = tool_input.get("prompt") or ""
    if EXEMPT_PREFIX.match(prompt):
        return None
    load = LOAD_LINE.search(prompt)
    if load and FORMS.search(prompt, load.start()):
        return None
    return REASON


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return
    reason = decide(payload)
    if reason:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }))


if __name__ == "__main__":
    main()
