param(
    [switch]$NoLlm
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$LogDir = Join-Path $RepoRoot "logs"
if (-not (Test-Path $LogDir)) {
    New-Item -ItemType Directory -Path $LogDir | Out-Null
}

$Stamp = Get-Date -Format "yyyy-MM-dd_HHmmss"
$LogPath = Join-Path $LogDir "daily-scout-$Stamp.log"
$Python = (Get-Command python).Source
$Engine = Join-Path $RepoRoot "engines\self_growing_engine.py"

if (-not (Test-Path $Engine)) {
    throw "Missing engine script: $Engine"
}

$Args = @($Engine)
if ($NoLlm) {
    $Args += "--no-llm"
}

Push-Location $RepoRoot
try {
    "[run-daily-scout] repo=$RepoRoot" | Tee-Object -FilePath $LogPath
    "[run-daily-scout] python=$Python" | Tee-Object -FilePath $LogPath -Append

    # Step 1: Collect + score + LLM annotate → evidence cards
    $Injector = Join-Path $RepoRoot "engines\evidence_injector.py"
    & $Python $Engine @Args 2>&1 | Tee-Object -FilePath $LogPath -Append
    if ($LASTEXITCODE -ne 0) {
        throw "self_growing_engine.py exited with $LASTEXITCODE"
    }

    # Step 2: Inject evidence into content packs + rank weak packs
    "[run-daily-scout] injecting evidence into content packs..." | Tee-Object -FilePath $LogPath -Append
    & $Python -X utf8 $Injector 2>&1 | Tee-Object -FilePath $LogPath -Append
    if ($LASTEXITCODE -ne 0) {
        throw "evidence_injector.py exited with $LASTEXITCODE"
    }

    "[run-daily-scout] done" | Tee-Object -FilePath $LogPath -Append
}
finally {
    Pop-Location
}
