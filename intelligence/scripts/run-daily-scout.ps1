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
$PyLauncher = Get-Command py.exe -ErrorAction SilentlyContinue
if ($PyLauncher) {
    $Python = (& $PyLauncher.Source -3.12 -c "import sys; print(sys.executable)").Trim()
    if ($LASTEXITCODE -ne 0 -or -not $Python) {
        throw "Unable to resolve the Python 3.12 interpreter through py.exe"
    }
}
else {
    $Python = (Get-Command python.exe -ErrorAction Stop).Source
}
$Engine = Join-Path $RepoRoot "engines\self_growing_engine.py"

if (-not (Test-Path $Engine)) {
    throw "Missing engine script: $Engine"
}

$EngineArgs = @()
if ($NoLlm) {
    $EngineArgs += "--no-llm"
}

Push-Location $RepoRoot
try {
    "[run-daily-scout] repo=$RepoRoot" | Tee-Object -FilePath $LogPath
    "[run-daily-scout] python=$Python" | Tee-Object -FilePath $LogPath -Append

    # Step 1: Collect + score + LLM annotate → evidence cards
    $Injector = Join-Path $RepoRoot "engines\evidence_injector.py"
    $PreviousErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    & $Python -X utf8 $Engine @EngineArgs 2>&1 | ForEach-Object { "$_" } | Tee-Object -FilePath $LogPath -Append
    $EngineExitCode = $LASTEXITCODE
    $ErrorActionPreference = $PreviousErrorActionPreference
    if ($EngineExitCode -ne 0) {
        throw "self_growing_engine.py exited with $EngineExitCode"
    }

    # Step 2: Build review reports only. Updating content-pack drafts requires
    # an explicit human-reviewed run of evidence_injector.py without --no-inject.
    "[run-daily-scout] building review reports (content-pack writes disabled)..." | Tee-Object -FilePath $LogPath -Append
    $PreviousErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    & $Python -X utf8 $Injector --no-inject 2>&1 | ForEach-Object { "$_" } | Tee-Object -FilePath $LogPath -Append
    $InjectorExitCode = $LASTEXITCODE
    $ErrorActionPreference = $PreviousErrorActionPreference
    if ($InjectorExitCode -ne 0) {
        throw "evidence_injector.py exited with $InjectorExitCode"
    }

    "[run-daily-scout] done" | Tee-Object -FilePath $LogPath -Append
}
finally {
    Pop-Location
}
