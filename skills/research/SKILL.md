---
name: "research"
description: "Research external technical evidence, standards, APIs, libraries, or alternatives needed for a repository decision or implementation."
---

# Research

## Purpose

Resolve an external technical question needed for a repository decision.

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml). For theme assets/mappings/proof,
use [asset-proof](../../.agent/workflows/asset-proof.md) and the linked native docs.
Load scope/memory contracts only for persistent context, registry, cross-project
relationships or promotion. Commands resolve from the repository root.

## Workflow

1. Frame the decision, constraints and repository-specific evidence already available.
2. Find current primary sources for relevant APIs, standards, tools or alternatives.
3. Read the actual relevant sources, preserving dates/version applicability and links.
4. Compare only viable alternatives against the project's constraints.
5. Distinguish repository evidence, external evidence, inference and recommendation.
6. Explain uncertainty and what would resolve it without presenting a guess as fact.
7. If a durable report was requested, keep it scoped and link sources precisely.

## Decision rules

Default is research-only; no dependency installs or implementation side effects.
Use investigate for local source/runtime facts. Memory is not a substitute for
current external evidence; consult scope/memory policy only when persistence matters.

## Completion and handoff

Give an actionable sourced conclusion, applicable versions and material limitations.
Do not imply a recommendation has been adopted into repository decisions.
