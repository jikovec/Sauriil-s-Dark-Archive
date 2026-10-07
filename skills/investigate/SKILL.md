---
name: "investigate"
description: "Inspect repository, runtime, or work state to establish current behaviour, root cause, or required work without changing implementation by default."
---

# Investigate

## Purpose

Establish what is happening and what work is needed, without implementing it.

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml). For theme assets/mappings/proof,
use [asset-proof](../../.agent/workflows/asset-proof.md) and the linked native docs.
Load scope/memory contracts only for persistent context, registry, cross-project
relationships or promotion. Commands resolve from the repository root.

## Workflow

1. Define the question and smallest useful evidence surface.
2. Read current source/config and relevant logs or existing proof without regenerating it.
3. Consult live Git/work state when it bears on the question; load git-github then.
4. Trace the causal path and compare plausible explanations against actual evidence.
5. Use a non-mutating reproduction where possible; state any unavailable runtime.
6. Separate observed facts, supported conclusions, inference and unknowns.
7. Identify the smallest justified next action and its affected scope.

## Decision rules

Default is read-only. Do not silently transition from diagnosis to implementation.
Use research for external standards/options, verify for a specific completion claim,
and pull only when synchronization is requested.

## Completion and handoff

Answer the question with source references, evidence limits and the causal finding.
A proposed fix is not an implemented fix.
