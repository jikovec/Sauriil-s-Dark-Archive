---
name: "sauriil-dark-archive-workflow"
description: "Coordinate Sauriil theme asset, mapping, conversion and proof work, or an explicit request to use the named project workflow modes."
---

# Sauriil's Dark Archive workflow

Coordinate recurring theme-specific source, mapping, conversion and proof work.
Read [AGENTS.md](../../../AGENTS.md), [metadata](../../../.agent/project.yaml)
and the [asset-proof workflow](../../../.agent/workflows/asset-proof.md).
Commands resolve from the repository root.

## Select the requested mode

| Request | Canonical workflow | Project evidence |
|---|---|---|
| inspect | [investigate](../../investigate/SKILL.md) | Source, mappings, overlapping work and proof provenance |
| implement | [build](../../build/SKILL.md), or [fix](../../fix/SKILL.md) for known defects | Original raster intent, output families, small-size readability |
| verify | [verify](../../verify/SKILL.md) | Relevant native checks and visual proof, within regeneration scope |
| prepare delivery | [push](../../push/SKILL.md), preparation only | Exact task paths, target branch, checks and side effects |
| finish | Remaining authorized canonical workflow | Evidence of completed versus remaining steps |

Read only the selected workflow and its required contracts. Do not turn a mode
selection into permission for another operation. In particular, prepare delivery
is read-only preparation. Standing source-delivery authority does not override a
preparation-only request; execute only when the current requested scope includes execution.

Preserve accepted theme names, architecture and asset provenance. Verify mapping
inputs before conversion, review affected output contexts and check small renders.
The shared workflow owns command selection and generated-proof boundaries.

For live OS requests, separately use [deploy](../../deploy/SKILL.md) under the
native deployment/rollback rules. For release artifacts use [release](../../release/SKILL.md).
This general theme skill does not activate an OS or authorize protected archives.

Finish the requested scope and relevant evidence. Retain outstanding visual/human
acceptance as an explicit limit; never infer it from a structural validator.
