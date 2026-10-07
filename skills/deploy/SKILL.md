---
name: "deploy"
description: "Deploy the intended repository state through its normal governed deployment process and verify the resulting live state."
---

# Deploy

## Purpose

Carry an explicitly requested target through normal governed deployment.

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [authorization](../../.agent/contracts/authorization.md)
- [verification](../../.agent/contracts/verification.md)
- [deployment](../../.agent/contracts/deployment.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml). For theme assets/mappings/proof,
use [asset-proof](../../.agent/workflows/asset-proof.md) and the linked native docs.
Load scope/memory contracts only for persistent context, registry, cross-project
relationships or promotion. Commands resolve from the repository root.

## Workflow

1. Establish the target OS/service, intended revision, scope and applicable authority.
2. Read current native deployment/security/rollback docs and the exact apply scripts.
3. Check target prerequisites, backups, rollback readiness and required proof.
4. Retrieve live requirements and external protections where applicable.
5. Follow the normal allowed procedure; do not invent a hosted service for this repo.
6. If a gate fails, finish independent preparation and report the exact blocker.
7. If deployment runs, verify installed identity and observed target behavior.
8. Record actual rollback readiness and remaining human/visual acceptance.

## Decision rules

Never silently switch to force-publication semantics. A normal deploy request
keeps all normal gates. OS apply/rollback must have explicit target scope.
Historical asset proof alone is insufficient for live acceptance.

## Completion and handoff

Report intended versus observed deployed state, checks and relevant rollback evidence.
Do not call source merge or dry-run output a live deployment.
