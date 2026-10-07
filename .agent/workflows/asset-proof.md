# Asset and proof workflow

Use for theme source, mappings, conversion and proof work. Read the relevant
[commands](../../docs/commands.md), [testing](../../docs/testing.md),
[proof checklist](../../docs/proof-checklist.md), [source map](../../docs/source-map.md)
and [asset guidelines](../../docs/asset-guidelines.md).

1. Establish exact source/mapping inputs, output paths and accepted visual intent.
   Preserve original concepts, raster master provenance and small-size readability.
2. Inspect the affected converter/validator before selecting commands. Python 3
   and Pillow serve raster work; Bash and PowerShell serve their respective OS
   paths. No package manifest or pinned environment is declared; check availability
   rather than silently installing or substituting runtimes.
3. Choose whether the task includes generated assets/proof. Conversion with
   `--apply`, contact sheets, validators and planners can mutate tracked output.
   A docs-only task uses read-only docs checks, not this generation sequence.
4. Run only the necessary native commands from the repository root. Review changed
   mappings and every affected output family. Keep proof tied to exact inputs.
5. For visual changes, inspect contact sheets and small-size rendering; automated
   structure checks cannot approve authored meaning. Record unresolved human review.
6. Inspect Git diff for unintended proof overwrites, fallback contexts and archive
   changes. Track causal defects separately if out of scope; do not mask them.
7. Separate static/dry-run evidence from OS installation and rollback acceptance.
   Use [deployment](../contracts/deployment.md) for any requested live operation.

Relevant live Issues #2–#7 track known installer/exporter/proof hazards at bootstrap.
Retrieve their current state before relying on them. No toolkit step fixes or
waives those defects. Release archives remain protected independently of proof work.
