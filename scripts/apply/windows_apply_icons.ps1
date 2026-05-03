# Windows icon apply skeleton for Sauriil Dark Archive.
# Refuses to run without -Apply. Example rows are skipped.
[CmdletBinding()]
param(
    [switch]$Apply
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..\..")
$RollbackDir = Join-Path $RepoRoot "windows\registry\rollback"

if (-not $Apply) {
    Write-Error "Refusing to modify Windows. Re-run with -Apply only after reviewing the dry-run report and backups."
    exit 2
}

function Read-CsvSafe {
    param([string]$RelativePath)
    $Path = Join-Path $RepoRoot $RelativePath
    if (-not (Test-Path $Path)) { return @() }
    return Import-Csv $Path
}

function Convert-RegistryProviderPathToRegExePath {
    param([string]$Path)
    return ($Path -replace '^HKCU:\\', 'HKCU\' -replace '^HKLM:\\', 'HKLM\' -replace '^HKCR:\\', 'HKCR\')
}

function Assert-RepoRelativePath {
    param([string]$RelativePath)
    if ([string]::IsNullOrWhiteSpace($RelativePath) -or $RelativePath.StartsWith("/") -or $RelativePath.StartsWith("~") -or $RelativePath.Contains("..")) {
        throw "Unsafe repository-relative path: $RelativePath"
    }
    return Join-Path $RepoRoot $RelativePath
}

New-Item -ItemType Directory -Path $RollbackDir -Force | Out-Null
$FileTypeRows = Read-CsvSafe "mappings/windows-filetypes.csv" | Where-Object { $_.status -in @("required", "active") }
$DriveRows = Read-CsvSafe "mappings/windows-drives.csv" | Where-Object { $_.status -in @("required", "active") }

if (($FileTypeRows.Count + $DriveRows.Count) -eq 0) {
    Write-Host "No required/active Windows registry rows found. Nothing to apply."
    exit 0
}

foreach ($Row in @($FileTypeRows + $DriveRows)) {
    $IconPath = Assert-RepoRelativePath $Row.planned_icon_path
    if (-not (Test-Path $IconPath)) {
        throw "Required icon file is missing: $($Row.planned_icon_path)"
    }
}

foreach ($Row in $FileTypeRows) {
    $RegPath = $Row.registry_path
    $RegExePath = Convert-RegistryProviderPathToRegExePath $RegPath
    $BackupPath = Join-Path $RollbackDir ("filetype-" + ($Row.prog_id -replace '[^A-Za-z0-9_.-]', '_') + ".reg")
    Write-Host "Exporting before apply: reg export $RegExePath $BackupPath /y"
    & reg.exe export $RegExePath $BackupPath /y | Out-Null
    $IconPath = Resolve-Path (Assert-RepoRelativePath $Row.planned_icon_path)
    New-Item -Path $RegPath -Force | Out-Null
    New-ItemProperty -Path $RegPath -Name "(default)" -Value "$IconPath,0" -PropertyType String -Force | Out-Null
    Write-Host "APPLIED file type icon: $RegPath -> $IconPath,0"
}

foreach ($Row in $DriveRows) {
    $RegPath = $Row.registry_path
    $RegExePath = Convert-RegistryProviderPathToRegExePath $RegPath
    $BackupPath = Join-Path $RollbackDir ("drive-" + $Row.drive_letter + ".reg")
    Write-Host "Exporting before apply: reg export $RegExePath $BackupPath /y"
    & reg.exe export $RegExePath $BackupPath /y | Out-Null
    $IconPath = Resolve-Path (Assert-RepoRelativePath $Row.planned_icon_path)
    New-Item -Path $RegPath -Force | Out-Null
    New-ItemProperty -Path $RegPath -Name "(default)" -Value "$IconPath,0" -PropertyType String -Force | Out-Null
    Write-Host "APPLIED drive icon: $RegPath -> $IconPath,0"
}

Write-Host "Apply complete. Restart Explorer or refresh icon cache manually after inspection."
