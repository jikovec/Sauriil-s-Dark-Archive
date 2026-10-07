---
name: "verify"
description: "Independently verify claimed repository, branch, PR, release, deployment, or live state using current evidence."
---

# Verify

## Purpose

Check a specific claim independently against current evidence.

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [verification](../../.agent/contracts/verification.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml). For theme assets/mappings/proof,
use [asset-proof](../../.agent/workflows/asset-proof.md) and the linked native docs.
Load scope/memory contracts only for persistent context, registry, cross-project
relationships or promotion. Commands resolve from the repository root.

## Workflow

1. Identify the claim, expected acceptance criteria and exact revision/target.
2. Inspect authoritative source and relevant existing artifacts without trusting prior claims.
3. Load git-github for branch/PR claims; deployment for release/live claims.
4. Select proportionate native checks with their side effects understood.
5. Execute the checks permitted by scope; classify unavailable checks honestly.
6. Compare results with the original criteria; do not lower them to obtain a pass.
7. Separate local structure, provider discovery, remote checks and live observations.

## Decision rules

Verification does not silently repair implementation. Use fix when remediation is
requested; use review for defect analysis across a change rather than claim checking.
Asset proof regeneration and OS apply require their corresponding scope.

## Completion and handoff

Give a verdict per claim with revision, command/source and result category.
Unverified prior evidence remains historical, and unavailable checks remain unavailable.
