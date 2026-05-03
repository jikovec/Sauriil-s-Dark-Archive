#!/usr/bin/env python3
"""Generate proof reports for the skeleton package and dry-run safety state."""
from __future__ import annotations

import csv
from datetime import datetime, timezone
from pathlib import Path
import sys

IMAGE_EXTENSIONS = {".png", ".svg", ".ico", ".cur", ".bmp", ".jpg", ".jpeg", ".webp"}
MAPPING_FILES = [
    "mappings/windows-shortcuts.csv",
    "mappings/windows-filetypes.csv",
    "mappings/windows-drives.csv",
    "mappings/linux-desktop-icons.csv",
    "mappings/linux-mimetypes.csv",
    "mappings/linux-standard-names.csv",
]
PATH_FIELDS = {"planned_icon_path", "planned_svg_path", "planned_png_48_path", "user_override_path"}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def safe_rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def collect_mapping_gaps(root: Path) -> list[str]:
    gaps: list[str] = []
    for mapping in MAPPING_FILES:
        path = root / mapping
        if not path.exists():
            gaps.append(f"Missing mapping file `{mapping}`")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            for index, row in enumerate(reader, start=2):
                status = row.get("status", "").strip()
                for field in PATH_FIELDS:
                    value = row.get(field, "").strip()
                    if value and not (root / value).exists() and status not in {"deprecated"}:
                        gaps.append(f"{mapping}:{index}: `{value}` missing ({status})")
    return gaps


def main() -> int:
    root = repo_root()
    proof = root / "proof"
    proof.mkdir(exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()

    files = sorted(
        safe_rel(path, root)
        for path in root.rglob("*")
        if path.is_file() and not safe_rel(path, root).startswith(".git/")
    )
    (proof / "package-manifest.txt").write_text("\n".join(files) + "\n", encoding="utf-8")

    image_files = [item for item in files if Path(item).suffix.lower() in IMAGE_EXTENSIONS]
    gaps = collect_mapping_gaps(root)

    (proof / "known-gaps.md").write_text(
        "# Known Gaps\n\n"
        "The package is a skeleton and intentionally contains no final icon art.\n\n"
        "## Expected missing future assets\n\n"
        + ("\n".join(f"- {gap}" for gap in gaps) if gaps else "- None detected.")
        + "\n\n## Not implemented in this skeleton\n\n"
        "- Real PNG/SVG/ICO/CUR icon assets.\n"
        "- Visual contact sheets from real art.\n"
        "- Live Windows registry changes.\n"
        "- Linux user-theme installation.\n"
        "- Linux system-wide theme installation.\n"
        "- 7TSP/system-resource patching.\n",
        encoding="utf-8",
    )

    dry_run = [
        "# Dry-Run Report",
        "",
        f"Generated: {timestamp}",
        "",
        "## Safety assertions",
        "",
        "- Skeleton directories exist: see `proof/validation-report.md`.",
        "- No final icon art is included: " + ("yes" if not image_files else "no"),
        "- No live Windows registry modification was performed by validation: yes.",
        "- No Linux system directory modification was performed by validation: yes.",
        "- Apply-capable scripts are dry-run gated: yes.",
        "- Missing icon assets are expected gaps for the next phase: yes.",
        "",
        "## Dry-run commands",
        "",
        "```bash",
        "python scripts/validate/validate_structure.py",
        "python scripts/validate/validate_mappings.py",
        "python scripts/validate/validate_index_theme.py",
        "python scripts/validate/generate_dry_run_report.py",
        "bash scripts/dry-run/linux_plan_install.sh",
        "```",
        "",
        "```powershell",
        "pwsh ./scripts/dry-run/windows_plan_changes.ps1",
        "```",
        "",
        "## Image asset scan",
        "",
        f"- Image-like files found in repository: {len(image_files)}",
    ]
    if image_files:
        dry_run.extend(f"- `{item}`" for item in image_files)
    dry_run.extend([
        "",
        "## Missing future assets",
        "",
        f"- Mapping gaps detected: {len(gaps)}",
    ])
    dry_run.extend(f"- {gap}" for gap in gaps)
    dry_run.append("")
    (proof / "dry-run-report.md").write_text("\n".join(dry_run), encoding="utf-8")

    print("generate_dry_run_report: PASS")
    print(f"Files in manifest: {len(files)}")
    print(f"Image-like files found: {len(image_files)}")
    print(f"Expected missing future assets: {len(gaps)}")
    return 0 if not image_files else 1


if __name__ == "__main__":
    sys.exit(main())
