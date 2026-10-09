---
name: "fix"
description: "Diagnose and repair a known defect, failed check, incomplete prior change, review finding, or inconsistency between authoritative project states."
---

# Fix

## Purpose

Repair a known causal defect or reconcile inconsistent authoritative states.

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [authorization](../../.agent/contracts/authorization.md)
- [verification](../../.agent/contracts/verification.md)
- [git-github](../../.agent/contracts/git-github.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml). For theme assets/mappings/proof,
use [asset-proof](../../.agent/workflows/asset-proof.md) and the linked native docs.
Load scope/memory contracts only for persistent context, registry, cross-project
relationships or promotion. Commands resolve from the repository root.

## Workflow

1. Reproduce or substantiate the defect using current evidence and exact inputs.
2. Trace its cause in source/config before selecting a repair.
3. For reconciliation, separately identify repository, docs, Git, GitHub, runtime,
   registry, memory and prior-handoff states; none are interchangeable evidence.
4. Preserve unrelated work and use isolation for overlapping changes.
5. Apply the narrow complete repair without masking failures or weakening criteria.
6. Add meaningful regression evidence when behavior is affected; rerun relevant checks.
7. Reconcile affected canonical docs and complete the authorized source workflow.

## Decision rules

`reconcile` invokes fix with reconciliation intent, not a duplicate skill.
Load memory/scopes only if reconciliation crosses persistent state; never rewrite
memory to manufacture consistency. Avoid duplicate work objects.
Use build for new substantial functionality without a known defect.

## Completion and handoff

Explain the cause, repair, validation and actual delivery endpoint.
Distinguish repaired source from any still-unverified live state.
