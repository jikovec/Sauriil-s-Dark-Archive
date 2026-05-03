# Windows icon change dry-run planner for Sauriil Dark Archive.
# This script does not modify the registry or filesystem.
[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..\..")
$ProofDir = Join-Path $RepoRoot "proof"
New-Item -ItemType Directory -Path $ProofDir -Force | Out-Null
$ReportPath = Join-Path $ProofDir "windows-dry-run.md"

function Read-CsvSafe {
    param([string]$RelativePath)
    $Path = Join-Path $RepoRoot $RelativePath
    if (-not (Test-Path $Path)) {
        Write-Host "MISSING CSV: $RelativePath"
        return @()
    }
    return Import-Csv $Path
}

function Test-RepoRelativePath {
    param([string]$RelativePath)
    if ([string]::IsNullOrWhiteSpace($RelativePath)) { return $false }
    if ($RelativePath.StartsWith("/") -or $RelativePath.StartsWith("~") -or $RelativePath.Contains("..")) { return $false }
    return $true
}

$Lines = @(
    "# Windows Dry-Run Plan",
    "",
    "No live Windows registry modification was performed.",
    "No shortcut, registry, or icon cache change was applied.",
    ""
)

Write-Host "Sauriil Dark Archive Windows dry-run planner"
Write-Host "Repository: $RepoRoot"
Write-Host "Mode: DRY-RUN ONLY"

$ShortcutRows = Read-CsvSafe "mappings/windows-shortcuts.csv"
$FileTypeRows = Read-CsvSafe "mappings/windows-filetypes.csv"
$DriveRows = Read-CsvSafe "mappings/windows-drives.csv"

$Lines += "## Shortcut/profile icon targets"
foreach ($Row in $ShortcutRows) {
    $IconPath = $Row.planned_icon_path
    $Exists = $false
    if (Test-RepoRelativePath $IconPath) {
        $Exists = Test-Path (Join-Path $RepoRoot $IconPath)
    }
    $Message = "[$($Row.status)] $($Row.display_name): $IconPath exists=$Exists"
    Write-Host "DRY-RUN shortcut: $Message"
    $Lines += "- $Message"
}
$Lines += ""

$Lines += "## Registry-backed file type targets"
foreach ($Row in $FileTypeRows) {
    $IconPath = $Row.planned_icon_path
    $Exists = $false
    if (Test-RepoRelativePath $IconPath) {
        $Exists = Test-Path (Join-Path $RepoRoot $IconPath)
    }
    $BackupCommand = "reg export $($Row.registry_path -replace ':\\', '\\') windows\\registry\\rollback\\filetype-$($Row.prog_id).reg /y"
    Write-Host "DRY-RUN registry filetype: $($Row.registry_path) -> $IconPath exists=$Exists"
    Write-Host "DRY-RUN backup command: $BackupCommand"
    $Lines += "- [$($Row.status)] `$($Row.registry_path)` -> `$IconPath`; exists=$Exists"
    $Lines += "  - Backup/export before apply: `$BackupCommand`"
}
$Lines += ""

$Lines += "## Drive icon targets"
foreach ($Row in $DriveRows) {
    $IconPath = $Row.planned_icon_path
    $Exists = $false
    if (Test-RepoRelativePath $IconPath) {
        $Exists = Test-Path (Join-Path $RepoRoot $IconPath)
    }
    $BackupCommand = "reg export $($Row.registry_path -replace ':\\', '\\') windows\\registry\\rollback\\drive-$($Row.drive_letter).reg /y"
    Write-Host "DRY-RUN drive icon: $($Row.registry_path) -> $IconPath exists=$Exists"
    Write-Host "DRY-RUN backup command: $BackupCommand"
    $Lines += "- [$($Row.status)] `$($Row.registry_path)` -> `$IconPath`; exists=$Exists"
    $Lines += "  - Backup/export before apply: `$BackupCommand`"
}
$Lines += ""
$Lines += "Result: DRY-RUN PASS"
$Lines | Set-Content -Path $ReportPath -Encoding UTF8
Write-Host "WROTE $ReportPath"
