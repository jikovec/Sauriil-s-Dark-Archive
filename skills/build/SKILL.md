---
name: "build"
description: "Implement substantial repository changes and carry them through relevant verification and normal repository completion workflow."
---

# Build

## Purpose

Implement the requested end state while preserving the existing theme architecture.

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

1. Establish the requested outcome, current instructions, relevant source and Git baseline.
2. Inspect live related work to avoid duplicating another branch or Issue.
3. Identify inputs, generated outputs, protected paths and acceptance evidence.
4. Make ordinary implementation choices and complete the smallest coherent change.
5. Follow the asset-proof workflow only when asset/proof regeneration is in scope.
6. Run proportionate checks, repair task-caused failures and update stale affected docs.
7. Review the final diff and complete the authorized Git/GitHub lifecycle.
8. Report actual source delivery and separate any requested live acceptance.

## Decision rules

Use fix for a bounded known defect. `develop` is an alias for this workflow.
A local-only request ends locally. Do not automatically release, deploy or publish.
Dependency or design changes must serve the requested behavior.

## Completion and handoff

Show the implemented behavior, relevant checks and actual delivery endpoint.
Include unresolved visual or live acceptance separately from structural passes.
