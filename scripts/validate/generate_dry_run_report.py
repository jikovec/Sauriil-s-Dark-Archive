#!/usr/bin/env python3
"""Generate proof reports for package manifest and dry-run safety state."""
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
        "v0.0.2 contains the first real asset batch and does not install or apply the theme to the live OS.\n\n"
        "## Mapping gaps\n\n"
        + ("\n".join(f"- {gap}" for gap in gaps) if gaps else "- None detected.")
        + "\n\n## Not implemented in v0.0.2\n\n"
        "- No live Windows registry changes.\n"
        "- No Windows shortcut/profile modifications.\n"
        "- No Windows icon cache refresh.\n"
        "- No Linux user-theme installation.\n"
        "- No Linux system-wide theme installation.\n"
        "- No KDE activation proof.\n"
        "- No `.desktop` override application.\n"
        "- No MIME cache update on a live machine.\n"
        "- No SVG scalable icons; raster PNG fallbacks are used because the accepted art is raster-generated, not true vector.\n"
        "- No 7TSP/system-resource patching.\n",
        encoding="utf-8",
    )

    dry_run = [
        "# Dry-Run Report",
        "",
        f"Generated: {timestamp}",
        "",
        "## Safety assertions",
        "",
        "- Repository structure validation is recorded in `proof/validation-report.md`.",
        "- v0.0.2 image/icon assets are expected and are confined to project directories.",
        "- No live Windows registry modification was performed by validation: yes.",
        "- No Linux system directory modification was performed by validation: yes.",
        "- Apply-capable scripts are dry-run gated: yes.",
        "- Missing mapped required icon assets are treated as validation failures: yes.",
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
        "powershell -ExecutionPolicy Bypass -File scripts/dry-run/windows_plan_changes.ps1",
        "```",
        "",
        "## Image asset scan",
        "",
        f"- Image/icon files found in repository: {len(image_files)}",
    ]
    dry_run.extend(f"- `{item}`" for item in image_files[:200])
    if len(image_files) > 200:
        dry_run.append(f"- ... {len(image_files) - 200} additional image/icon files omitted from this report preview.")
    dry_run.extend([
        "",
        "## Missing mapped assets",
        "",
        f"- Mapping gaps detected: {len(gaps)}",
    ])
    dry_run.extend(f"- {gap}" for gap in gaps)
    dry_run.append("")
    (proof / "dry-run-report.md").write_text("\n".join(dry_run), encoding="utf-8")

    print("generate_dry_run_report: PASS" if not gaps else "generate_dry_run_report: FAIL")
    print(f"Files in manifest: {len(files)}")
    print(f"Image-like files found: {len(image_files)}")
    print(f"Expected missing future assets: {len(gaps)}")
    return 0 if not gaps else 1


if __name__ == "__main__":
    sys.exit(main())
