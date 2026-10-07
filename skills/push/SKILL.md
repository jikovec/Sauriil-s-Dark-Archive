---
name: "push"
description: "Finalize completed local work through the repository's normal commit, push, pull-request, check, and merge workflow."
---

# Push

## Purpose

Deliver completed task-owned local source through its normal repository lifecycle.

## Shared contracts

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

1. Inspect current worktree, branch, upstream, related PR and task ownership.
2. Review the actual change; preserve unrelated work and private/generated artifacts.
3. Establish relevant verification against the exact candidate.
4. Stage an explicit path allowlist and create coherent commits if needed.
5. Push the intended branch and create/update its PR without duplicating work.
6. Inspect current head checks/reviews; remediate task-caused issues.
7. When authorized and requirements pass, merge the reviewed head.
8. Fetch and verify resulting remote/default-branch identity and safe local status.

## Decision rules

Follow configured draft defaults; mark ready only when the requested merge
endpoint and actual review justify it. Do not bypass external requirements.
Use release for versioned artifacts/tags; push does not imply release or activation.

## Completion and handoff

Provide commit/PR/merge evidence, checks and preserved checkout status.
Distinguish a pushed branch from a merged default branch.
