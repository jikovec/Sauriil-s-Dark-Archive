---
name: "pull"
description: "Safely synchronize local repository state with upstream while preserving unrelated work and reconciling conflicts according to repository conventions."
---

# Pull

## Purpose

Synchronize the intended checkout while preserving existing local work.

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [authorization](../../.agent/contracts/authorization.md)
- [git-github](../../.agent/contracts/git-github.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml). For theme assets/mappings/proof,
use [asset-proof](../../.agent/workflows/asset-proof.md) and the linked native docs.
Load scope/memory contracts only for persistent context, registry, cross-project
relationships or promotion. Commands resolve from the repository root.

## Workflow

1. Inspect branch, HEAD, upstream, dirty/untracked paths and concurrent work.
2. Read relevant live work/refs and fetch the intended remote.
3. Compare divergence and determine the repository's permitted integration strategy.
4. Fast-forward a clean default branch; preserve shared task-branch history.
5. Use isolation or stop before overlapping dirty changes can be overwritten.
6. Resolve only task-owned understood conflicts; preserve uncertain work for review.
7. Run checks proportionate to the integrated changes.
8. Verify local HEAD/upstream/status and report remaining divergence.

## Decision rules

Destructive reset, stash and cleanup are not default synchronization mechanisms.
Use investigate for read-only divergence explanation. Fetch alone is not pull or
checkout synchronization. Do not infer authority for protected-history rewrites.

## Completion and handoff

Report before/after refs, strategy, verification and any preserved or unresolved work.
Do not say synchronized if only the remote-tracking ref changed.
