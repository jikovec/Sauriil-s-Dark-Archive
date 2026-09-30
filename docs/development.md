# Development

#repo/development #sauriil/assets #sauriil/mappings

## Workflow

1. Inspect the current default branch, local `git status --short --branch`, and live GitHub Issues/pull requests.
2. Confirm scope against [current-state.md](current-state.md), [decisions.md](decisions.md), and the relevant work item.
3. For material work, use Issue/work object → branch → implementation → verification → pull request.
4. For asset work, inspect [asset-guidelines.md](asset-guidelines.md), [icon-name-mapping.md](icon-name-mapping.md), [source-map.md](source-map.md), and the relevant CSV files under [../mappings](../mappings).
5. Update source assets under [../source/master/raster](../source/master/raster) only when asset changes are requested.
6. Update mapping CSVs before generating platform outputs.
7. Regenerate outputs and proof only when that mutation is in scope.
8. Update the smallest canonical documentation set affected by the change.

Preserve unrelated dirty/untracked work. Do not work directly on `main` for material changes unless explicitly authorized. Do not merge, release, deploy, publish, or run live OS changes merely because implementation is complete.

## Prerequisites

- Python 3 for Python tooling.
- Pillow for image conversion/contact-sheet operations when source images are present.
- Bash for Linux shell scripts.
- Windows PowerShell for Windows scripts.

There is no package manifest or automated dependency installer. Do not invent one as part of unrelated work.

## Asset Source Rules

- Accepted raster masters live in `source/master/raster`.
- Generated normalized PNGs live in `source/png/<size>`.
- Windows ICO outputs live in `windows/ico/<context>`.
- Linux PNG fallbacks live in `linux/Sauriil-Dark-Archive/<size>/<context>`.
- Do not wrap raster art in fake SVG files and call it scalable vector art.

## Mapping Rules

- [../mappings/icon-assets.csv](../mappings/icon-assets.csv) is the routing manifest for conversion scripts.
- Platform mapping files document planned Windows and Linux targets.
- Missing `required` or `active` mapped assets should fail validation.
- `example` and `optional` rows must not be presented as current release coverage.
- The current exporters have a fallback-selection defect for contexts with no manifest rows; see [#6](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/6).

## Generated And Proof Files

Conversion and proof commands may modify tracked generated assets/evidence. Before running them:
- verify that regeneration is part of the work item;
- inspect [commands.md](commands.md) and [testing.md](testing.md);
- record exact commands/results;
- review the resulting diff.

Do not edit/regenerate `VERSIONS/` unless explicitly authorized.

## Documentation Updates

After meaningful changes, update only affected canonical files. Keep [agent-index.json](agent-index.json) aligned when entry points, paths, commands, work routing, or known risks change.

Historical docs under `DOCUMENTATION/` are evidence/context; do not rewrite them as current docs unless historical correction is the explicit task.
