#!/usr/bin/env python3
"""Validate the starter XDG index.theme file."""
from __future__ import annotations

import configparser
from pathlib import Path
import sys
from typing import Iterable


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def append_report(root: Path, lines: Iterable[str]) -> None:
    report = root / "proof" / "validation-report.md"
    existing = report.read_text(encoding="utf-8") if report.exists() else "# Validation Report\n\n"
    report.write_text(existing + "\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    root = repo_root()
    theme_root = root / "linux" / "Sauriil-Dark-Archive"
    index_path = theme_root / "index.theme"
    errors: list[str] = []

    parser = configparser.ConfigParser(strict=False)
    parser.optionxform = str
    if not index_path.is_file():
        errors.append("Missing linux/Sauriil-Dark-Archive/index.theme")
    else:
        parser.read(index_path, encoding="utf-8")

    if "Icon Theme" not in parser:
        errors.append("Missing [Icon Theme] section")
    else:
        meta = parser["Icon Theme"]
        expected = {
            "Name": "Sauriil Dark Archive",
            "Comment": "Dark fantasy archive-machine icon theme skeleton",
            "Inherits": "breeze,hicolor",
        }
        for key, value in expected.items():
            if meta.get(key) != value:
                errors.append(f"[Icon Theme] {key} must be `{value}`")
        directories_value = meta.get("Directories", "")
        directories = [item.strip() for item in directories_value.split(",") if item.strip()]
        if not directories:
            errors.append("Directories list is empty")
        actual_dirs = sorted(
            path.relative_to(theme_root).as_posix()
            for path in theme_root.rglob("*")
            if path.is_dir() and not any(child.is_dir() for child in path.iterdir())
        )
        missing_from_index = sorted(set(actual_dirs) - set(directories))
        missing_on_disk = sorted(set(directories) - set(actual_dirs))
        for item in missing_from_index:
            errors.append(f"Directory exists but is not declared: {item}")
        for item in missing_on_disk:
            errors.append(f"Directory declared but missing: {item}")
        for directory in directories:
            if directory not in parser:
                errors.append(f"Missing [{directory}] section")
                continue
            section = parser[directory]
            type_value = section.get("Type")
            if directory.startswith("scalable/"):
                for key in ("Type", "Size", "MinSize", "MaxSize"):
                    if key not in section:
                        errors.append(f"[{directory}] missing {key}")
                if type_value != "Scalable":
                    errors.append(f"[{directory}] Type must be Scalable")
            else:
                for key in ("Type", "Size"):
                    if key not in section:
                        errors.append(f"[{directory}] missing {key}")
                if type_value != "Fixed":
                    errors.append(f"[{directory}] Type must be Fixed")

    lines = [
        "## index.theme validation",
        "",
        f"- Theme file: `linux/Sauriil-Dark-Archive/index.theme`",
        f"- Errors: {len(errors)}",
        "",
    ]
    if errors:
        lines.append("### Errors")
        lines.extend(f"- {error}" for error in errors)
        lines.append("")
    lines.append(f"Result: {'PASS' if not errors else 'FAIL'}")
    lines.append("")
    append_report(root, lines)

    print("validate_index_theme: " + ("PASS" if not errors else "FAIL"))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
