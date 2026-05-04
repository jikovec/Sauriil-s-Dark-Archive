#!/usr/bin/env python3
"""Validate the Sauriil Dark Archive repository structure."""
from __future__ import annotations

from pathlib import Path
import sys
from typing import Iterable

IMAGE_EXTENSIONS = {".png", ".svg", ".ico", ".cur", ".bmp", ".jpg", ".jpeg", ".webp"}

REQUIRED_DIRS = [
    "source/master/raster",
    "source/master/vector",
    "source/master/contact-sheets",
    "source/png/1024",
    "source/png/512",
    "source/png/256",
    "source/png/128",
    "source/png/64",
    "source/png/48",
    "source/png/32",
    "source/png/24",
    "source/png/16",
    "source/svg/full-color",
    "source/svg/symbolic",
    "source/references",
    "mappings",
    "windows/ico/apps",
    "windows/ico/filetypes",
    "windows/ico/folders",
    "windows/ico/drives",
    "windows/ico/shell",
    "windows/shortcuts",
    "windows/registry/dry-run",
    "windows/registry/apply",
    "windows/registry/rollback",
    "windows/iconpackager",
    "windows/winaero",
    "windows/third-party-tool-notes",
    "linux/Sauriil-Dark-Archive/scalable/apps",
    "linux/Sauriil-Dark-Archive/scalable/mimetypes",
    "linux/Sauriil-Dark-Archive/scalable/places",
    "linux/Sauriil-Dark-Archive/scalable/devices",
    "linux/Sauriil-Dark-Archive/scalable/status",
    "linux/Sauriil-Dark-Archive/scalable/actions",
    "linux/Sauriil-Dark-Archive/scalable/symbolic",
    "linux/Sauriil-Dark-Archive/16x16",
    "linux/Sauriil-Dark-Archive/24x24",
    "linux/Sauriil-Dark-Archive/32x32",
    "linux/Sauriil-Dark-Archive/48x48",
    "linux/Sauriil-Dark-Archive/64x64",
    "linux/Sauriil-Dark-Archive/128x128",
    "linux/Sauriil-Dark-Archive/256x256",
    "linux/desktop-overrides",
    "linux/mime-overrides",
    "linux/kde",
    "linux/gnome",
    "linux/xfce",
    "scripts/dry-run",
    "scripts/apply",
    "scripts/rollback",
    "scripts/convert",
    "scripts/test-render",
    "scripts/validate",
    "proof",
    "docs",
]

REQUIRED_FILES = [
    "README.md",
    "docs/windows-plan.md",
    "docs/linux-plan.md",
    "docs/asset-guidelines.md",
    "docs/icon-name-mapping.md",
    "docs/third-party-risk.md",
    "docs/rollback.md",
    "docs/proof-checklist.md",
    "mappings/windows-shortcuts.csv",
    "mappings/windows-filetypes.csv",
    "mappings/windows-drives.csv",
    "mappings/linux-desktop-icons.csv",
    "mappings/linux-mimetypes.csv",
    "mappings/linux-standard-names.csv",
    "linux/Sauriil-Dark-Archive/index.theme",
    "scripts/validate/validate_structure.py",
    "scripts/validate/validate_mappings.py",
    "scripts/validate/validate_index_theme.py",
    "scripts/validate/generate_dry_run_report.py",
    "scripts/convert/normalize_pngs.py",
    "scripts/convert/export_windows_ico.py",
    "scripts/convert/export_linux_png_fallbacks.py",
    "scripts/test-render/render_contact_sheet.py",
    "scripts/dry-run/windows_plan_changes.ps1",
    "scripts/apply/windows_apply_icons.ps1",
    "scripts/rollback/windows_rollback_icons.ps1",
    "scripts/dry-run/linux_plan_install.sh",
    "scripts/apply/linux_install_user_theme.sh",
    "scripts/rollback/linux_rollback_user_theme.sh",
]

REQUIRED_V002_FILES = [
    "docs/v0.0.2-asset-batch.md",
    "proof/v0.0.2-source-asset-inventory.md",
    "proof/v0.0.2-generated-assets.md",
    "proof/v0.0.2-contact-sheet-report.md",
    "proof/v0.0.2-validation-report.md",
    "mappings/icon-assets.csv",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def append_report(root: Path, lines: Iterable[str]) -> None:
    proof = root / "proof"
    proof.mkdir(exist_ok=True)
    report = proof / "validation-report.md"
    existing = report.read_text(encoding="utf-8") if report.exists() else "# Validation Report\n\n"
    report.write_text(existing + "\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    root = repo_root()
    missing_dirs = [d for d in REQUIRED_DIRS if not (root / d).is_dir()]
    missing_files = [f for f in REQUIRED_FILES if not (root / f).is_file()]
    missing_v002_files = [f for f in REQUIRED_V002_FILES if not (root / f).is_file()]

    image_files = [
        rel(path, root)
        for path in root.rglob("*")
        if path.is_file()
        and path.suffix.lower() in IMAGE_EXTENSIONS
        and ".zip" not in path.name.lower()
    ]

    unsafe_image_files = [
        item for item in image_files
        if item.startswith("/usr/share/") or item.startswith("~") or ".." in Path(item).parts
    ]

    windows_apply = (root / "scripts/apply/windows_apply_icons.ps1").read_text(encoding="utf-8")
    linux_apply = (root / "scripts/apply/linux_install_user_theme.sh").read_text(encoding="utf-8")
    gated_scripts_ok = "-Apply" in windows_apply and "--apply" in linux_apply and "/usr/share" in linux_apply

    lines = [
        "## Structure validation",
        "",
        f"- Required directories checked: {len(REQUIRED_DIRS)}",
        f"- Required base files checked: {len(REQUIRED_FILES)}",
        f"- v0.0.2 proof/docs checked: {len(REQUIRED_V002_FILES)}",
        f"- Missing directories: {len(missing_dirs)}",
        f"- Missing base files: {len(missing_files)}",
        f"- Missing v0.0.2 files: {len(missing_v002_files)}",
        f"- Image/icon assets found: {len(image_files)}",
        f"- Unsafe image paths found: {len(unsafe_image_files)}",
        f"- Apply-capable scripts dry-run gated: {'yes' if gated_scripts_ok else 'no'}",
        "",
    ]
    if missing_dirs:
        lines.append("### Missing directories")
        lines.extend(f"- `{item}`" for item in missing_dirs)
        lines.append("")
    if missing_files:
        lines.append("### Missing base files")
        lines.extend(f"- `{item}`" for item in missing_files)
        lines.append("")
    if missing_v002_files:
        lines.append("### Missing v0.0.2 files")
        lines.extend(f"- `{item}`" for item in missing_v002_files)
        lines.append("")
    if unsafe_image_files:
        lines.append("### Unsafe image paths")
        lines.extend(f"- `{item}`" for item in unsafe_image_files)
        lines.append("")
    if not gated_scripts_ok:
        lines.append("### Script gate failure")
        lines.append("- Apply-capable scripts do not contain the required explicit apply gates.")
        lines.append("")

    ok = not missing_dirs and not missing_files and not missing_v002_files and not unsafe_image_files and gated_scripts_ok
    lines.append(f"Result: {'PASS' if ok else 'FAIL'}")
    lines.append("")
    append_report(root, lines)

    print("validate_structure: " + ("PASS" if ok else "FAIL"))
    if missing_dirs:
        print("Missing directories:")
        for item in missing_dirs:
            print(f"  - {item}")
    if missing_files:
        print("Missing base files:")
        for item in missing_files:
            print(f"  - {item}")
    if missing_v002_files:
        print("Missing v0.0.2 files:")
        for item in missing_v002_files:
            print(f"  - {item}")
    if unsafe_image_files:
        print("Unsafe image paths:")
        for item in unsafe_image_files:
            print(f"  - {item}")
    print(f"Image/icon assets found: {len(image_files)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
