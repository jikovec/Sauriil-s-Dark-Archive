<!-- codex-memory-scaffold:project-overview -->
# Sauriil’s theme — project card

#repo/index #sauriil/theme

Reviewed 2026-09-09 against current local source. Display name: **Sauriil’s theme**. Repository and technical asset names remain Sauriil Dark Archive / `Sauriil-s-Dark-Archive`; do not rename identifiers or output paths to match the display name.

This is original dark-fantasy icon-theme software/assets for Windows 11 and Arch Linux/KDE Plasma, owned by Aetheris (repository owner `jikovec`). Elder Scrolls gameplay records and creative lore are separate collections and out of scope. Preserve strong silhouettes, 48×48 identity proof, simplified 16/24px readability and source-to-conversion provenance. Nothing changes the live OS by default.

| Field | Current source-backed state |
|---|---|
| Canonical source | [jikovec/Sauriil-s-Dark-Archive](https://github.com/jikovec/Sauriil-s-Dark-Archive), `main`; work from the accessible catalogue checkout. Machine-specific catalogue paths stay outside public documentation. |
| Implemented baseline | `v0.0.2`: 12 accepted raster masters, normalized PNGs, multi-size Windows ICOs, Linux PNG fallbacks, contact sheets, mapping/structure/theme validators and dry-run planners. Explicit apply/rollback scripts also exist; live acceptance is unproven. |
| Agent setup | The [canonical toolkit](../.agent/README.md) under `.agent/` and `skills/` (see [workflow entry point](agent-workflow.md) and [project workflow](../skills/project/sauriil-dark-archive-workflow/SKILL.md)), Codex [environment actions](../.codex/environments/environment.toml) and the [machine index](agent-index.json). |
| Setup and run | No package manifest, dependency lock, install bootstrap, application server or canonical start command. Environment setup/cleanup strings are empty; five manual actions are defined. See [exact commands and effects](commands.md). |
| Dependencies | Python 3; Pillow for image operations; Bash for Linux scripts; Windows PowerShell and native registry tooling for Windows operations. Contact sheets try DejaVu fonts and fall back to Pillow defaults. Optional Linux cache tools are discovered by installer source. |
| Host readiness | On this review, Python/Python3 and PowerShell were absent from shell PATH. Bundled Python 3.12.14 with Pillow 12.3.0 was verified for this documentation pass only; this does not configure the project's environment actions. |
| Related planned work | [NightTab](../integrations/nighttab/README.md) remains researched/planned, separately gated and not implemented or live-applied. Private exports, bookmarks and profiles stay outside Git. |
| Publication | No tracked or local `.github/workflows`, Sites hosting definition, custom Git hook path or active Git hook was found. Release ZIPs live in `VERSIONS/`; no archive was opened. Remote service settings and current CI runs were not audited. Recheck triggers before separately authorized delivery. |

## Lifecycle and tools

Reference/provenance → accepted raster master → mapping manifests → generated normalized PNG and platform-output branches → contact sheets → structural/mapping/theme proof → dry-run plans → separately authorized manual release packaging. Platform exporters normally read mapped raster masters directly; normalized PNGs are not a mandatory intermediate. Live OS apply/rollback is a separate authorized phase, not the next automatic step.

Shell/filesystem and Git were exercised. The GitHub connector successfully read canonical `main` README during this review; that proves a repository read, not remote write authority. The project workflow skill is available and used. Image generation and browser tools are exposed for suitable future tasks but were not exercised. No project account/cloud connector is required. Optional Pages/gallery and validation CI remain proposals; no plugin, integration or service was enabled.

## Remaining decisions and evidence

- Linux apply currently replaces the theme before checking Python and required desktop overrides. All four required desktop rows have empty `user_override_path`; the script then rejects that path. A separate implementation task should preflight all dependencies/mappings before mutation and prove failure leaves state unchanged before considering live testing.
- Choose a reproducible Python/Pillow setup if asset work is requested; this repository currently declares no install command or pinned dependency environment.
- NightTab requires its supported current native export and disposable validation before implementation/import, as recorded in its existing handoff. Personal browser state was not inspected in this review.
- `v0.0.3`, true SVG assets and expanded platform coverage remain roadmap choices. No release or live-apply decision is needed to finish this orientation task.
- Local `main` HEAD and live remote `main`/HEAD both resolved to `1246dde9fa9956351bfd54fe43ccae2da1217c3a` on 2026-09-09. The checkout contains inherited dirty/untracked work, including workflow and NightTab material; matching HEAD does not mean those files are published.
- Existing release proof is historical evidence, not a new test run. No current CI/deployed identity/live acceptance is asserted. See the [review and durable handoff](../reports/2026-09-09-project-orientation.md).

## What The Repo Contains

- Original raster source icon art under [source/master/raster](../source/master/raster).
- Normalized generated PNGs under [source/png](../source/png).
- Windows multi-size ICO outputs under [windows/ico](../windows/ico).
- Linux XDG icon-theme outputs under [linux/Sauriil-Dark-Archive](../linux/Sauriil-Dark-Archive).
- CSV routing and platform mapping files under [mappings](../mappings).
- Python, PowerShell, and Bash scripts under [scripts](../scripts).
- Validation and proof evidence under [proof](../proof).
- Documentation, reports, and handoffs under [docs](.), [reports](../reports), and [handoffs](../handoffs).

## What The Repo Does Not Claim

- It does not install or apply icons to the live OS by default.
- It does not prove live Windows registry changes, shortcut changes, Linux user-theme activation, or system-wide installation.
- It does not contain true vector SVG artwork for `v0.0.2`.
- It does not use a package manifest, Makefile, or CI workflow.

## Start Points

- Human docs hub: [INDEX.md](INDEX.md)
- Agent orientation: [agent-index.md](agent-index.md)
- Machine-readable index: [agent-index.json](agent-index.json)
- Current release evidence: [../proof/v0.0.2-validation-report.md](../proof/v0.0.2-validation-report.md)
- Roadmap: [roadmap.md](roadmap.md)
