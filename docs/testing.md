<!-- codex-memory-scaffold:testing -->
# Testing

#repo/testing #sauriil/proof

## Verification Model

The repository does not have a separate unit-test framework or CI workflow. Verification is currently script- and evidence-driven.

Verification families:

- documentation/governance checks;
- static structure and mapping validation;
- asset regeneration checks;
- XDG `index.theme` validation;
- platform dry-run planning;
- live apply/rollback verification, which is not currently established and is never implied by the earlier layers.

## Documentation / Governance Checks

For docs-only changes:

```bash
git status --short --branch
git diff --check
python -m json.tool docs/agent-index.json
```

Also validate relative Markdown links in changed documentation and syntax for any changed YAML/JSON/XML/metadata files.

## Static And Proof Checks

Repository commands are listed in [commands.md](commands.md) and [proof-checklist.md](proof-checklist.md).

Important limitations:

- `validate_structure.py` verifies required paths and token-level apply gates; it does not prove transactional apply/rollback safety. Regression coverage for those invariants is tracked in [#4](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/4).
- `validate_mappings.py` currently rewrites `proof/known-gaps.md` with stale skeleton-era content; see [#7](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/7).
- Exporters can select fallback assets for a context with no manifest rows; see [#6](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/6).
- Proof-generating commands may mutate `proof/`; do not run them merely to validate documentation.

## Platform Dry Runs

Linux dry-run:

```bash
bash scripts/dry-run/linux_plan_install.sh
```

Windows dry-run, when PowerShell is available:

```powershell
powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1
```

The captured v0.0.2 validation executed the Linux planner but skipped the Windows PowerShell planner. That missing evidence is tracked in [#5](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/5).

## Live Apply / Rollback

Live apply and apply-rollback commands are not acceptance tests.

Current source has known safety gaps:
- Linux preflight ordering: [#2](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/2)
- Windows stable icon storage and lossless rollback: [#3](https://github.com/jikovec/Sauriil-s-Dark-Archive/issues/3)

Do not claim live behavior is verified unless a future work item executes an authorized, appropriate verification and preserves the evidence.

## Evidence Levels

Use explicit statuses in reports:

```text
passed
failed
blocked
unavailable
not applicable
not run
```

A historical passing report proves only the checks, revision, and environment it records. An unavailable check is not a pass.

## Current Historical Evidence

- There is no separate unit-test framework or package manifest.
- Proof commands can mutate files under `proof/`; do not run them during a docs-only pass unless proof regeneration is explicitly part of the task.

## Agent Toolkit Checks

```bash
python3 scripts/validate/validate_agent_toolkit.py
python3 -m json.tool docs/agent-index.json
git diff --check
```

The toolkit check reads files only and uses Python 3's standard library. It checks
constrained JSON-compatible YAML metadata/frontmatter, required files, thin adapter
parity, repository-relative links and routing-example coverage. It does not prove
provider discovery, model routing behavior, visual acceptance or live safety.
