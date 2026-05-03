#!/usr/bin/env python3
"""Validate mapping CSV files and report missing future icon assets."""
from __future__ import annotations

import csv
from pathlib import Path
import sys
from typing import Iterable

VALID_STATUSES = {"example", "optional", "required", "active", "deprecated"}
FATAL_MISSING_STATUSES = {"required", "active"}
PATH_FIELDS = {"planned_icon_path", "planned_svg_path", "planned_png_48_path", "user_override_path"}

CSV_REQUIREMENTS = {
    "mappings/windows-shortcuts.csv": [
        "status", "target_kind", "display_name", "shortcut_hint", "planned_icon_path", "backup_hint", "notes",
    ],
    "mappings/windows-filetypes.csv": [
        "status", "extension", "prog_id", "registry_path", "planned_icon_path", "scope", "notes",
    ],
    "mappings/windows-drives.csv": [
        "status", "drive_letter", "registry_path", "planned_icon_path", "scope", "notes",
    ],
    "mappings/linux-desktop-icons.csv": [
        "status", "desktop_file_name", "desktop_source_hint", "user_override_path", "icon_name", "planned_icon_path", "notes",
    ],
    "mappings/linux-mimetypes.csv": [
        "status", "mime_type", "icon_name", "planned_svg_path", "planned_png_48_path", "notes",
    ],
    "mappings/linux-standard-names.csv": [
        "status", "context", "standard_name", "planned_svg_path", "planned_png_48_path", "notes",
    ],
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def append_report(root: Path, lines: Iterable[str]) -> None:
    report = root / "proof" / "validation-report.md"
    existing = report.read_text(encoding="utf-8") if report.exists() else "# Validation Report\n\n"
    report.write_text(existing + "\n".join(lines).rstrip() + "\n", encoding="utf-8")


def is_safe_relative(value: str) -> bool:
    if not value:
        return True
    if value.startswith(("/", "~", "$HOME", "%USERPROFILE%", "%LOCALAPPDATA%")):
        return False
    path = Path(value)
    if path.is_absolute():
        return False
    return ".." not in path.parts


def main() -> int:
    root = repo_root()
    errors: list[str] = []
    gaps: list[str] = []
    row_count = 0

    for rel_path, expected_headers in CSV_REQUIREMENTS.items():
        path = root / rel_path
        if not path.is_file():
            errors.append(f"Missing CSV: {rel_path}")
            continue
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            headers = reader.fieldnames or []
            if headers != expected_headers:
                errors.append(f"{rel_path}: headers differ from expected order")
                continue
            for index, row in enumerate(reader, start=2):
                row_count += 1
                status = (row.get("status") or "").strip()
                if status not in VALID_STATUSES:
                    errors.append(f"{rel_path}:{index}: invalid status `{status}`")
                    continue
                for field, value in row.items():
                    if field not in PATH_FIELDS or not value:
                        continue
                    if not is_safe_relative(value):
                        errors.append(f"{rel_path}:{index}: unsafe repository path in `{field}`: {value}")
                        continue
                    target = root / value
                    if not target.exists():
                        message = f"{rel_path}:{index}: missing future asset `{value}` ({status})"
                        if status in FATAL_MISSING_STATUSES:
                            errors.append(message)
                        elif status != "deprecated":
                            gaps.append(message)
                if status == "example" and "Example" not in " ".join(row.values()) and "example" not in " ".join(row.values()).lower():
                    errors.append(f"{rel_path}:{index}: example row is not clearly marked as example")

    lines = [
        "## Mapping validation",
        "",
        f"- CSV files checked: {len(CSV_REQUIREMENTS)}",
        f"- Rows checked: {row_count}",
        f"- Non-fatal missing future asset gaps: {len(gaps)}",
        f"- Fatal errors: {len(errors)}",
        "",
    ]
    if gaps:
        lines.append("### Expected gaps")
        lines.extend(f"- {gap}" for gap in gaps)
        lines.append("")
    if errors:
        lines.append("### Errors")
        lines.extend(f"- {error}" for error in errors)
        lines.append("")
    lines.append(f"Result: {'PASS' if not errors else 'FAIL'}")
    lines.append("")
    append_report(root, lines)

    gap_report = root / "proof" / "known-gaps.md"
    gap_report.write_text(
        "# Known Gaps\n\n"
        "This skeleton intentionally contains no final icon art. Missing mapped assets below are expected until the asset phase.\n\n"
        + ("\n".join(f"- {gap}" for gap in gaps) if gaps else "- No mapping gaps detected.\n"),
        encoding="utf-8",
    )

    print("validate_mappings: " + ("PASS" if not errors else "FAIL"))
    print(f"Rows checked: {row_count}")
    print(f"Expected missing future assets: {len(gaps)}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
