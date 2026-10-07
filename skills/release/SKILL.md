---
name: "release"
description: "Prepare and complete the repository's normal release workflow, including versioning, notes, tags, artifacts, or release records where applicable."
---

# Release

## Purpose

Prepare only the requested versioned theme release state.

## Shared contracts

- [core](../../.agent/contracts/core.md)
- [authorization](../../.agent/contracts/authorization.md)
- [verification](../../.agent/contracts/verification.md)
- [git-github](../../.agent/contracts/git-github.md)
- [deployment](../../.agent/contracts/deployment.md)
- [handoff](../../.agent/contracts/handoff.md)

## Project context

Read [project metadata](../../.agent/project.yaml). For theme assets/mappings/proof,
use [asset-proof](../../.agent/workflows/asset-proof.md) and the linked native docs.
Load scope/memory contracts only for persistent context, registry, cross-project
relationships or promotion. Commands resolve from the repository root.

## Workflow

1. Establish intended version/revision and the exact requested release outputs.
2. Inspect existing version/proof/notes conventions without opening protected archives
   unless archive inspection or regeneration is explicitly in scope.
3. Discover actual tagging, artifact and release-record mechanics; do not invent CI.
4. Review applicable safety, visual and proof gates for the intended artifact.
5. Produce only authorized notes/version changes/artifacts, retaining provenance.
6. Run applicable checks; identify blocked runtime or human acceptance separately.
7. Create requested tags/release records only when their scope is authorized.
8. Read back the published version/artifact identity when publication was included.

## Decision rules

Source push/merge is distinct from release; release does not deploy the theme.
Use push for finished source only and deploy for target-OS activation.
Unresolved existing live-safety defects cannot be described as live qualification.

## Completion and handoff

Report exact version, source revision, artifacts and remote release state.
State what was not released or accepted live and why, when material.
