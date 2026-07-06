$ErrorActionPreference = "SilentlyContinue"

$repoDir = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }
$fixtureRoot = Join-Path $repoDir ".git-sync-fixture"

if (Test-Path -LiteralPath $fixtureRoot) {
    Remove-Item -LiteralPath $fixtureRoot -Recurse -Force
}

if (Test-Path -LiteralPath $fixtureRoot) {
    Write-Host "Test fixture still exists, but it is ignored by .gitignore: $fixtureRoot"
    exit 1
}

Write-Host "Test fixture cleaned."
