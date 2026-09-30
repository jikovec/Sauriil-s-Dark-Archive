# Repository Governance Baseline — 2026-09-30

#agent/report #repo/index #repo/security #repo/development

## Scope And Authority

This report records the documentation, governance, metadata, and hygiene baseline performed under [GitHub Issue #10](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/10).

Authoritative baseline inspected:

```text
repository: jikovec/Sauriil-s-Dark-Archive
default branch: main
revision: 1246dde9fa9956351bfd54fe43ccae2da1217c3a
```

The pass inspected the tracked repository tree, current root/docs/proof/report/handoff surfaces, current scripts and mappings relevant to documentation claims, Git history, live open Issues, and open pull requests. No open pull request conflicted with the work before branch creation.

Direct inspection of the user's local checkout's untracked/ignored state was unavailable in this execution environment; tracked remote repository state was inspected completely and that limitation is preserved below rather than inferred away.

## Key Findings

- The existing `docs/` layer was already the canonical home for architecture, development, testing, deployment, platform plans, and project state.
- Root discovery policy was incomplete: no security, contribution, support, changelog, editor, attributes, or PR-template surface existed.
- Active documentation overstated the safety significance of apply gates and historical proof.
- Current source has tracked Linux/Windows apply-safety gaps (#2/#3), missing behavioral regression coverage (#4), missing Windows PowerShell evidence (#5), an exporter fallback defect (#6), and a proof-clobbering mapping validator (#7).
- No selected repository license, Code of Conduct, or private vulnerability-reporting route was established; owner decisions are tracked in [#11](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/11).
- The only tracked cleanup-pattern matches were three intentional release ZIPs under `VERSIONS/`.

## Requested Artifact Applicability

| Artifact | Disposition | Reason |
|---|---|---|
| `SECURITY.md` | created | Executable live-OS mutation paths and dependency/security boundaries require public reporting guidance. |
| `AGENTS.md` | improved | Existing canonical agent policy needed live work-ledger routing and current authority/safety rules. |
| `README.md` | corrected/improved | Needed accurate status, prerequisites, policy links, license state, and apply-safety caveats. |
| `DEPLOYMENT.md` | represented elsewhere | `docs/deployment.md` is canonical and was improved. |
| `robots.txt` | not applicable | No deployed/indexable web surface. |
| `LICENSE.md` / `LICENSE` | owner/legal decision | No license is selected; tracked in #11. |
| `CONTRIBUTING.md` | created | Public repo plus live Issues/PR workflow warrants contributor guidance. |
| `CODE_OF_CONDUCT.md` | owner decision | No conduct standard/version has been selected; tracked in #11. |
| `SUPPORT.md` | created | Clarifies Issues/security boundaries without inventing support guarantees. |
| `CHANGELOG.md` | created | Documented v0.0.1/v0.0.2 release boundaries and intentional release archives exist. Entries derive from canonical release docs/proof, not commit titles. |
| `ARCHITECTURE.md` | represented elsewhere | `docs/architecture.md` is canonical and was improved. |
| `DEVELOPMENT.md` | represented elsewhere | `docs/development.md` is canonical and was improved. |
| `TESTING.md` | represented elsewhere | `docs/testing.md` is canonical and was corrected. |
| `INSTALLATION.md` | not currently applicable | No supported/verified installation channel is established; live apply has tracked safety gaps and platform plans remain canonical. |
| `CONFIGURATION.md` | represented by existing domain docs | Configuration-like data is the mapping/XDG/source model; there is no independent user configuration system. |
| `TROUBLESHOOTING.md` | not applicable | No stable evidence-backed recurring failure catalogue justifies a standalone file yet. |
| `GOVERNANCE.md` | represented elsewhere | Current authority/workflow is adequately expressed by `AGENTS.md`, `CONTRIBUTING.md`, GitHub ownership, and the work ledger; no invented committee model added. |
| `MAINTAINERS.md` | not applicable | No verified maintainer roster beyond repository ownership requires a separate file. |
| `CODEOWNERS` | not applicable | No ownership partition/review model was established; a one-owner catch-all would add noise, not governance. |
| `THIRD_PARTY_NOTICES.md` | not established as required | No vendored third-party code/assets with a verified notice obligation were identified. Pillow is an external runtime dependency, not vendored. |
| `NOTICE.md` | not applicable | No established license/dependency model requires it. |
| `.gitattributes` | created | Text/binary classification and LF normalization rules are useful in a mixed text/binary cross-platform repository. |
| `.editorconfig` | created | Captures observed UTF-8/LF/final-newline and script/JSON indentation conventions. |
| `CITATION.cff` | not applicable | Repository is not currently maintained as a formally citable research/software release. |
| `sitemap.xml` | not applicable | No indexable website is deployed from this repository. |

## Created

- `SECURITY.md`
- `CONTRIBUTING.md`
- `SUPPORT.md`
- `CHANGELOG.md`
- `.editorconfig`
- `.gitattributes`
- `.github/PULL_REQUEST_TEMPLATE.md`

No Issue form was added: the current repository has a small live work ledger and no stable multi-form taxonomy that would justify extra template surface.

## Improved / Corrected

- `README.md`
- `AGENTS.md`
- `.gitignore`
- `00_Index.md`
- `docs/INDEX.md`
- `docs/current-state.md`
- `docs/agent-index.md`
- `docs/agent-index.json`
- `docs/project-overview.md`
- `docs/architecture.md`
- `docs/development.md`
- `docs/commands.md`
- `docs/testing.md`
- `docs/proof-checklist.md`
- `docs/security-model.md`
- `docs/deployment.md`
- `docs/windows-plan.md`
- `docs/linux-plan.md`
- `docs/rollback.md`
- `docs/roadmap.md`
- `docs/connections.md`

The main consistency repair is that accepted platform plans are now distinguished from current implementation/proof. Apply gates are authorization guards, not behavioral safety evidence.

## Hygiene

### Removed

No tracked files were removed. The remote tracked tree contained no safe disposable cache/build/temp/log/backup artifact from the requested cleanup catalogue.

### Preserved Exceptions

The following cleanup-pattern matches were deliberately preserved because repository documentation identifies them as intentional release/history artifacts:

- `VERSIONS/v0 WinRAR SauriilDarkArchive HQ 48x48.zip`
- `VERSIONS/v0.0.1 Sauriil-Dark-Archive.zip`
- `VERSIONS/v0.0.2 Sauriil-Dark-Archive.zip`

The current protected WinRAR archive change remains separately tracked in #8; this pass did not rewrite or normalize any archive.

### Ignore Rules

`.gitignore` now covers:
- local Obsidian and worktree/agent scratch;
- OS/editor noise;
- Python/cache output;
- local build/dist/coverage/temp/backup directories;
- disposable backup/reject/log files.

It intentionally does **not** ignore `VERSIONS/`, `*.zip`, `*.tar.gz`, `*.patch`, or `*.diff` globally.

## Validation

Validation of implementation commit `296dfc18f2846d3c069624f6b40254514ad9c115`:

| Check | Result | Evidence |
|---|---|---|
| Remote comparison to baseline | passed | exactly 28 intended changed files; branch one commit ahead, zero behind |
| Recursive branch tree | passed | complete/non-truncated; 498 entries |
| `docs/agent-index.json` parse | passed | JSON parsed successfully |
| Changed Markdown relative-link scan | passed | 24 changed Markdown files; 0 broken repository-relative links |
| Changed relative heading-fragment links | not applicable | none introduced |
| Added-line whitespace/conflict-marker scan | passed | 0 trailing-whitespace findings; 0 conflict markers |
| `.editorconfig` structural parse | passed | 0 malformed active lines |
| `.gitattributes` structural parse | passed | 0 malformed active lines |
| Tracked cleanup-pattern scan | passed with preserved exceptions | only the three intentional `VERSIONS/*.zip` files matched |
| Tracked `.obsidian/` scan | passed | 0 tracked entries |
| Expected ignore-rule coverage | passed | all selected recurrence-prevention rules present |
| Unsafe global archive ignore scan | passed | no `*.zip`, `*.tar.gz`, or `/VERSIONS/` ignore |
| Added-line sensitive-path/secret heuristic | passed | 0 findings |
| `git status --short --branch` on the user's local checkout | unavailable | connected local checkout was not reachable from this execution environment |
| exact `git diff --check` command | unavailable | no local checkout; remote added-line whitespace/conflict scan used as a narrower substitute |
| product/asset proof regeneration | not run | documentation/governance-only scope; commands mutate proof/generated assets and current `validate_mappings.py` has tracked defect #7 |
| live OS apply/rollback | not run | explicitly outside scope and current safety gaps remain open |

## Git / GitHub Delivery State

- Work object: [#10](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/10)
- Owner-policy decisions: [#11](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/11)
- Branch: `docs/governance-baseline-20260930`
- Pull request: [#12](https://github.com/jikovec/Sauriil-s-Dark-Archive/pull/12)
- PR readback before this report update: open, non-draft, mergeable, targeting `main`
- GitHub status checks reported on the then-current PR head: none
- GitHub Actions pull-request workflow runs reported on the then-current PR head: none
- Merge: not performed
- Deployment/publication/release: not performed
- Live OS modification: not performed

The pull request head is the authoritative revision for current delivery state.

## Remaining Owner Decisions

Only the decisions in #11 remain owner-dependent from this baseline:
- repository license (or explicit decision to remain without an open-source license);
- whether/which Code of Conduct to adopt;
- private vulnerability-reporting route.

No license, community commitment, private contact, bounty, SLA, maintainer roster, or deployment authority was invented by this pass.
