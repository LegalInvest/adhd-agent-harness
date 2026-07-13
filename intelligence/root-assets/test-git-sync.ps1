param(
    [switch]$KeepFixtures
)

$ErrorActionPreference = "Stop"

$repoDir = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }
$fixtureRoot = Join-Path $repoDir ".git-sync-fixture"
$workDir = Join-Path $fixtureRoot "work"
$remoteDir = Join-Path $fixtureRoot "remote.git"
$syncSource = Join-Path $repoDir "git-sync.ps1"
$ignoreSource = Join-Path $repoDir ".gitignore"

function Invoke-Checked {
    param(
        [string]$FilePath,
        [string[]]$Arguments,
        [string]$WorkingDirectory
    )
    Push-Location $WorkingDirectory
    try {
        $previousErrorActionPreference = $ErrorActionPreference
        $previousNativeErrorActionPreference = $Global:PSNativeCommandUseErrorActionPreference
        try {
            $ErrorActionPreference = "Continue"
            if (Get-Variable -Name PSNativeCommandUseErrorActionPreference -Scope Global -ErrorAction SilentlyContinue) {
                $Global:PSNativeCommandUseErrorActionPreference = $false
            }
            $output = & $FilePath @Arguments 2>&1
            $code = $LASTEXITCODE
        } finally {
            $ErrorActionPreference = $previousErrorActionPreference
            if (Get-Variable -Name PSNativeCommandUseErrorActionPreference -Scope Global -ErrorAction SilentlyContinue) {
                $Global:PSNativeCommandUseErrorActionPreference = $previousNativeErrorActionPreference
            }
        }

        if ($code -ne 0) {
            throw "$FilePath $($Arguments -join ' ') failed:`n$($output -join "`n")"
        }
        return ($output -join "`n")
    } finally {
        Pop-Location
    }
}

if (Test-Path -LiteralPath $fixtureRoot) {
    Remove-Item -LiteralPath $fixtureRoot -Recurse -Force
}

New-Item -ItemType Directory -Force -Path $workDir | Out-Null
New-Item -ItemType Directory -Force -Path $remoteDir | Out-Null

try {
    Copy-Item -LiteralPath $syncSource -Destination (Join-Path $workDir "git-sync.ps1") -Force
    Copy-Item -LiteralPath $ignoreSource -Destination (Join-Path $workDir ".gitignore") -Force
    Set-Content -LiteralPath (Join-Path $workDir "README.md") -Value "# Fixture`n" -Encoding UTF8
    Set-Content -LiteralPath (Join-Path $workDir "note.md") -Value "hello" -Encoding UTF8

    Invoke-Checked -FilePath "git" -Arguments @("init", "--bare", $remoteDir) -WorkingDirectory $fixtureRoot | Out-Null
    $env:GIT_CEILING_DIRECTORIES = $fixtureRoot

    $config = [ordered]@{
        remoteUrl = $remoteDir
        remoteName = "origin"
        branch = "main"
        userName = "Git Sync Test"
        userEmail = "git-sync-test@example.invalid"
    }
    $config | ConvertTo-Json -Depth 4 | Set-Content -Encoding UTF8 -LiteralPath (Join-Path $workDir "git-sync.config.json")

    Invoke-Checked -FilePath "powershell" -Arguments @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", (Join-Path $workDir "git-sync.ps1"),
        "-ConfigPath", (Join-Path $workDir "git-sync.config.json"),
        "-Message", "test: initial sync"
    ) -WorkingDirectory $workDir | Out-Null

    $remoteHead = Invoke-Checked -FilePath "git" -Arguments @("--git-dir", $remoteDir, "rev-parse", "--verify", "refs/heads/main") -WorkingDirectory $fixtureRoot
    if (-not $remoteHead.Trim()) {
        throw "Remote main branch was not created."
    }

    Add-Content -LiteralPath (Join-Path $workDir "note.md") -Value "world" -Encoding UTF8

    Invoke-Checked -FilePath "powershell" -Arguments @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", (Join-Path $workDir "git-sync.ps1"),
        "-ConfigPath", (Join-Path $workDir "git-sync.config.json"),
        "-Message", "test: second sync"
    ) -WorkingDirectory $workDir | Out-Null

    $count = Invoke-Checked -FilePath "git" -Arguments @("--git-dir", $remoteDir, "rev-list", "--count", "main") -WorkingDirectory $fixtureRoot
    if ([int]$count.Trim() -lt 2) {
        throw "Expected at least two commits in remote, got $count."
    }

    $statePath = Join-Path $workDir ".git-sync\latest.json"
    if (-not (Test-Path -LiteralPath $statePath)) {
        throw "Missing latest sync state file."
    }

    Write-Host "E2E OK: local init, commit, push, second push, and state file all passed."
} finally {
    if (-not $KeepFixtures -and (Test-Path -LiteralPath $fixtureRoot)) {
        Remove-Item -LiteralPath $fixtureRoot -Recurse -Force
    }
}
