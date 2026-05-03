#!/usr/bin/env bash
set -euo pipefail

APPLY=0
for arg in "$@"; do
    case "$arg" in
        --apply) APPLY=1 ;;
        *) echo "Unknown argument: $arg" >&2; exit 2 ;;
    esac
done

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"
THEME_TARGET="${HOME}/.local/share/icons/Sauriil-Dark-Archive"
DESKTOP_TARGET="${HOME}/.local/share/applications"

case "$THEME_TARGET" in
    /usr/share/*) echo "Refusing unsafe theme target: $THEME_TARGET" >&2; exit 3 ;;
esac
case "$DESKTOP_TARGET" in
    /usr/share/*) echo "Refusing unsafe desktop target: $DESKTOP_TARGET" >&2; exit 3 ;;
esac

if [[ "$APPLY" != "1" ]]; then
    echo "Sauriil Dark Archive Linux rollback dry-run"
    echo "Would remove user theme: $THEME_TARGET"
    echo "Would remove only mapped required/active .desktop overrides from: $DESKTOP_TARGET"
    echo "No files were removed. Re-run with --apply to perform rollback."
    exit 0
fi

rm -rf "$THEME_TARGET"
echo "Removed user theme: $THEME_TARGET"

python3 - <<'PY' "$REPO_ROOT" "$DESKTOP_TARGET"
import csv
import sys
from pathlib import Path
root = Path(sys.argv[1])
desktop_target = Path(sys.argv[2])
mapping = root / "mappings/linux-desktop-icons.csv"
if not mapping.exists():
    sys.exit(0)
with mapping.open(newline="", encoding="utf-8") as handle:
    for row in csv.DictReader(handle):
        if row.get("status") not in {"required", "active"}:
            continue
        name = Path(row.get("user_override_path", "")).name
        if not name:
            continue
        target = desktop_target / name
        if target.exists():
            target.unlink()
            print(f"Removed desktop override: {target}")
PY

if command -v kbuildsycoca6 >/dev/null 2>&1; then
    kbuildsycoca6 --noincremental || true
fi

echo "Rollback complete. Switch KDE icon theme back to Breeze/Breeze Dark if it was selected manually."
