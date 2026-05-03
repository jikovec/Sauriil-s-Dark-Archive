#!/usr/bin/env bash
set -euo pipefail

APPLY=0
for arg in "$@"; do
    case "$arg" in
        --apply) APPLY=1 ;;
        *) echo "Unknown argument: $arg" >&2; exit 2 ;;
    esac
done

if [[ "$APPLY" != "1" ]]; then
    echo "Refusing to install. Re-run with --apply only after reviewing dry-run proof." >&2
    exit 2
fi

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"
THEME_SOURCE="${REPO_ROOT}/linux/Sauriil-Dark-Archive"
THEME_TARGET="${HOME}/.local/share/icons/Sauriil-Dark-Archive"
DESKTOP_TARGET="${HOME}/.local/share/applications"

case "$THEME_TARGET" in
    /usr/share/*) echo "Refusing unsafe theme target: $THEME_TARGET" >&2; exit 3 ;;
esac
case "$DESKTOP_TARGET" in
    /usr/share/*) echo "Refusing unsafe desktop target: $DESKTOP_TARGET" >&2; exit 3 ;;
esac
if [[ "$THEME_SOURCE" == /usr/share/* ]]; then
    echo "Refusing unsafe theme source: $THEME_SOURCE" >&2
    exit 3
fi

if [[ ! -f "$THEME_SOURCE/index.theme" ]]; then
    echo "Missing index.theme in $THEME_SOURCE" >&2
    exit 4
fi

mkdir -p "$(dirname "$THEME_TARGET")"
rm -rf "$THEME_TARGET"
cp -a "$THEME_SOURCE" "$THEME_TARGET"
echo "Installed user-scope skeleton theme to $THEME_TARGET"

mkdir -p "$DESKTOP_TARGET"
python3 - <<'PY' "$REPO_ROOT" "$DESKTOP_TARGET"
import csv
import shutil
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
        source_rel = row.get("user_override_path", "")
        if not source_rel or source_rel.startswith(("/", "~")) or ".." in Path(source_rel).parts:
            raise SystemExit(f"Unsafe desktop override path: {source_rel}")
        source = root / source_rel
        if not source.exists():
            raise SystemExit(f"Missing required desktop override: {source_rel}")
        target = desktop_target / source.name
        shutil.copy2(source, target)
        print(f"Installed desktop override: {target}")
PY

if command -v gtk-update-icon-cache >/dev/null 2>&1; then
    gtk-update-icon-cache -f -t "$THEME_TARGET" || true
fi
if command -v kbuildsycoca6 >/dev/null 2>&1; then
    kbuildsycoca6 --noincremental || true
fi

echo "Apply complete. The theme is still a skeleton unless real icon assets were added before installation."
