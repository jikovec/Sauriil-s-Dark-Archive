# Deterministic checks and hooks

No automatic Git or provider hook is installed. The existing repository convention
places executable checks under scripts/validate, so the toolkit check is
[validate_agent_toolkit.py](../../scripts/validate/validate_agent_toolkit.py).

- Trigger: manual check after toolkit/docs edits and before scoped source delivery.
- Purpose: required files, stable metadata, frontmatter, adapter parity, local links,
  routing-case coverage and index consistency.
- Inputs: checked-out repository files; no credentials or network.
- Side effects: none; no generated proof, asset writes or hook registration.
- Runtime: Python 3 standard library; normally under a few seconds.
- Manual invocation: `python3 scripts/validate/validate_agent_toolkit.py` from root.
- Exit semantics: 0 means static checks passed; 1 means invalid/missing content;
  2 is command-line/runtime failure. Failures name the affected path/invariant.
- Failure handling: repair actual content, then rerun; do not bypass to claim a pass.

Reasoning about architecture, authority, risk or completion stays in skills.
Future hooks must document trigger, inputs, side effects, dependencies, timing and
failure semantics and share implementation across providers.
