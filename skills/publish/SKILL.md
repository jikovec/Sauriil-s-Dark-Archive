---
name: "publish"
description: "Force-publish the intended state by bypassing only eligible repository or deployment-process gates while preserving external platform protections."
---

# Publish

## Purpose

Handle an explicit force-publication request within eligible process gates.

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

1. Establish the expressly requested publication target, revision and authority.
2. Identify the normal deployment blocker and gather its current evidence.
3. Classify it as repository/process controlled or externally enforced.
4. Refuse to bypass external protections; report their legitimate satisfaction path.
5. For an eligible gate, identify the minimum supported force path and its effects.
6. Verify this path stays within requested scope and preserves domain safety rules.
7. Execute only a real authorized path; keep failed/skipped checks truthful.
8. Verify the resulting publication/live identity and report any acceptance gaps.

## Decision rules

No supported force-publication path currently exists for this asset project.
Do not invent a bypass switch or interpret ordinary push/deploy as this request.
Administrator credentials never permit bypassing required reviews, IAM, Rulesets,
provider protections or protected environment approvals.

## Completion and handoff

Identify the blocker, classification, any intentionally bypassed eligible gate and
actual live result. If no legitimate path exists, return the prepared blocker.
