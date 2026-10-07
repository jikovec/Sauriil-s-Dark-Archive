# Verification contract

Classify each relevant check as exactly one of: **passed**, **failed**,
**blocked/unavailable**, **intentionally bypassed**, or **not required**.
An unexecuted check is never passed. Historical proof is not a fresh pass.

Use the strongest proportionate native evidence for the changed behavior. Follow
[testing](../../docs/testing.md) and [asset-proof](../workflows/asset-proof.md).
For toolkit/docs edits run the toolkit validator, JSON parse and diff whitespace;
review changed Markdown links. Do not regenerate assets/proof to validate prose.

Record command, revision/scope, result and material limitation. Rerun affected
checks after repairs, not unrelated suites mechanically. Never weaken acceptance
criteria or hide failures to produce a pass. Static structure, semantic correctness,
provider discovery, remote CI, deployment and human/live acceptance are separate.
Missing runtimes/dependencies remain unavailable until legitimately resolved.
