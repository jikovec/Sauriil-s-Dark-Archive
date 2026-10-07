---
name: "review"
description: "Review a change, branch, pull request, or implementation for material correctness, regression, architecture, security, and maintainability issues."
---

# Review

## Purpose

Find material defects in the specified implementation or change.

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

1. Establish the exact diff/revision, intended behavior and governing contracts.
2. Load git-github for branches/PRs and retrieve current relevant review/check state.
3. Inspect affected callers, mappings, scripts and tests around the changed paths.
4. Prioritize correctness, requested behavior, regressions and contract violations.
5. Consider architecture, security, test coverage and maintainability; raise style
   only when material. Include performance/accessibility where actually relevant.
6. Substantiate findings with a reachable scenario, impact and precise file reference.
7. Separate actionable findings from questions, untested risks and unrelated defects.

## Decision rules

Do not bury defects in style noise or invent findings to fill a quota.
Review is analytically independent and does not silently authorize fixes.
Use verify for completion claims; use fix when asked to repair a finding.

## Completion and handoff

Report findings in severity order, or explicitly state no actionable findings found.
Name verification performed and meaningful remaining coverage limits.
