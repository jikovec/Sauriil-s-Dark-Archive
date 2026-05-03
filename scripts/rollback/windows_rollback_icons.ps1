# Windows rollback skeleton for Sauriil Dark Archive.
# Defaults to dry-run and imports registry backups only with -Apply.
[CmdletBinding()]
param(
    [switch]$Apply
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RepoRoot = Resolve-Path (Join-Path $ScriptDir "..\..")
$RollbackDir = Join-Path $RepoRoot "windows\registry\rollback"

Write-Host "Sauriil Dark Archive Windows rollback"
Write-Host "Mode: $(if ($Apply) { 'APPLY' } else { 'DRY-RUN' })"

$RegFiles = @()
if (Test-Path $RollbackDir) {
    $RegFiles = Get-ChildItem -Path $RollbackDir -Filter "*.reg" -File
}

if ($RegFiles.Count -eq 0) {
    Write-Host "No .reg rollback files found under $RollbackDir"
} else {
    foreach ($File in $RegFiles) {
        if ($Apply) {
            Write-Host "IMPORTING $($File.FullName)"
            & reg.exe import $File.FullName | Out-Null
        } else {
            Write-Host "DRY-RUN would import: reg import $($File.FullName)"
        }
    }
}

Write-Host "Shortcut rollback remains manual unless backed-up .lnk files are later added to windows/shortcuts."
Write-Host "Icon cache refresh command after rollback, if needed: ie4uinit.exe -show; restart Explorer."
if (-not $Apply) {
    Write-Host "No live Windows registry modification was performed. Re-run with -Apply to import backups."
}
