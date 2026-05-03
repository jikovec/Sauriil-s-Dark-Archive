#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/../.." && pwd)"
PROOF_DIR="${REPO_ROOT}/proof"
REPORT_PATH="${PROOF_DIR}/linux-dry-run.md"
THEME_SOURCE="${REPO_ROOT}/linux/Sauriil-Dark-Archive"
THEME_TARGET="${HOME}/.local/share/icons/Sauriil-Dark-Archive"
DESKTOP_TARGET="${HOME}/.local/share/applications"

mkdir -p "$PROOF_DIR"

case "$THEME_TARGET" in
    /usr/share/*) echo "Refusing unsafe target: $THEME_TARGET" >&2; exit 3 ;;
esac
case "$DESKTOP_TARGET" in
    /usr/share/*) echo "Refusing unsafe target: $DESKTOP_TARGET" >&2; exit 3 ;;
esac

{
    echo "# Linux Dry-Run Install Plan"
    echo
    echo "No install was performed."
    echo "No /usr/share directory was modified."
    echo
    echo "- Theme source: ${THEME_SOURCE}"
    echo "- Theme target: ${THEME_TARGET}"
    echo "- Desktop override target: ${DESKTOP_TARGET}"
    echo
    echo "## Planned copy"
    echo
    echo "- Would copy linux/Sauriil-Dark-Archive to ${THEME_TARGET}"
    echo "- Would copy mapped .desktop overrides only to ${DESKTOP_TARGET}"
    echo
    echo "## Missing mapped icons"
} > "$REPORT_PATH"

echo "Sauriil Dark Archive Linux dry-run planner"
echo "Repository: $REPO_ROOT"
echo "Mode: DRY-RUN ONLY"
echo "Would install theme to: $THEME_TARGET"
echo "Would install desktop overrides to: $DESKTOP_TARGET"

python3 - <<'PY' "$REPO_ROOT" "$REPORT_PATH"
import csv
import sys
from pathlib import Path
root = Path(sys.argv[1])
report = Path(sys.argv[2])
fields = ("planned_icon_path", "planned_svg_path", "planned_png_48_path", "user_override_path")
files = [
    "mappings/linux-desktop-icons.csv",
    "mappings/linux-mimetypes.csv",
    "mappings/linux-standard-names.csv",
]
lines = []
for rel in files:
    path = root / rel
    if not path.exists():
        lines.append(f"- Missing CSV `{rel}`")
        continue
    with path.open(newline="", encoding="utf-8") as handle:
        for index, row in enumerate(csv.DictReader(handle), start=2):
            status = row.get("status", "")
            for field in fields:
                value = row.get(field, "")
                if value and not (root / value).exists() and status != "deprecated":
                    lines.append(f"- {rel}:{index}: `{value}` missing ({status})")
if not lines:
    lines.append("- None detected.")
with report.open("a", encoding="utf-8") as handle:
    handle.write("\n".join(lines) + "\n\nResult: DRY-RUN PASS\n")
print(f"Expected missing future Linux assets: {len(lines) if lines != ['- None detected.'] else 0}")
PY

echo "WROTE $REPORT_PATH"
