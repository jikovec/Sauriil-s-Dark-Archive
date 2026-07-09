# Development

#repo/development #sauriil/assets #sauriil/mappings

## Workflow

1. Confirm scope against [current-state.md](current-state.md), [decisions.md](decisions.md), and [roadmap.md](roadmap.md).
2. For asset work, inspect [asset-guidelines.md](asset-guidelines.md), [icon-name-mapping.md](icon-name-mapping.md), [source-map.md](source-map.md), and the relevant CSV files under [../mappings](../mappings).
3. Add or update source assets under [../source/master/raster](../source/master/raster) only when asset changes are requested.
4. Update mapping CSVs before generating platform outputs.
5. Regenerate outputs and proof only when that mutation is in scope.
6. Update docs, reports, and [agent-index.json](agent-index.json) when commands, paths, risks, or entry points change.

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
- `example` and `optional` rows should not be presented as current release coverage.

## Documentation Updates

After meaningful repo changes, update the smallest relevant set:

- [current-state.md](current-state.md) for release status, commands, known state, or important paths.
- [source-map.md](source-map.md) when source/generated folders or scripts change.
- [connections.md](connections.md) when docs, proof, scripts, and mappings need new links.
- [roadmap.md](roadmap.md) when planned batches change.
- [agent-index.json](agent-index.json) when machine-readable routing changes.

## Do Not Touch Without Explicit Request

- Release archives in `VERSIONS/`.
- Live OS apply or rollback commands.
- `.obsidian/` local workspace settings.
- Historical docs under `DOCUMENTATION/` unless the task is explicitly historical cleanup.
