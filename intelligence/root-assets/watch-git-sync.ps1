param(
    [string]$ConfigPath = ".\git-sync.config.json",
    [int]$DebounceSeconds = 60
)

$ErrorActionPreference = "Stop"

$repoDir = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }
$syncScript = Join-Path $repoDir "git-sync.ps1"
$logDir = Join-Path $repoDir ".git-sync"
$logPath = Join-Path $logDir "watch.log"

if (-not (Test-Path -LiteralPath $syncScript)) {
    throw "Missing git-sync.ps1 next to watch-git-sync.ps1."
}

New-Item -ItemType Directory -Force -Path $logDir | Out-Null

function Write-WatchLog {
    param([string]$Message)
    $line = "$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') $Message"
    Add-Content -Encoding UTF8 -LiteralPath $logPath -Value $line
    Write-Host $line
}

function Invoke-Sync {
    $arguments = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $syncScript,
        "-ConfigPath", $ConfigPath,
        "-Message", "auto-sync: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    )

    & powershell @arguments *>&1 | ForEach-Object {
        Write-WatchLog $_.ToString()
    }
}

$watcher = New-Object System.IO.FileSystemWatcher
$watcher.Path = $repoDir
$watcher.IncludeSubdirectories = $true
$watcher.EnableRaisingEvents = $true
$watcher.NotifyFilter = [System.IO.NotifyFilters]'FileName, DirectoryName, LastWrite, Size'

$script:pending = $false
$script:lastEvent = Get-Date
$ignoredPattern = '\\.git(\\|$)|\\.git-sync(\\|$)'

$action = {
    $path = $Event.SourceEventArgs.FullPath
    if ($path -match $using:ignoredPattern) {
        return
    }

    $script:pending = $true
    $script:lastEvent = Get-Date
}

$subscriptions = @(
    Register-ObjectEvent -InputObject $watcher -EventName Created -Action $action,
    Register-ObjectEvent -InputObject $watcher -EventName Changed -Action $action,
    Register-ObjectEvent -InputObject $watcher -EventName Deleted -Action $action,
    Register-ObjectEvent -InputObject $watcher -EventName Renamed -Action $action
)

Write-WatchLog "Watching $repoDir. Debounce: ${DebounceSeconds}s. Press Ctrl+C to stop."

try {
    while ($true) {
        Start-Sleep -Seconds 5

        if ($script:pending -and ((Get-Date) - $script:lastEvent).TotalSeconds -ge $DebounceSeconds) {
            $script:pending = $false
            Write-WatchLog "Changes detected. Starting sync."
            try {
                Invoke-Sync
            } catch {
                Write-WatchLog "Sync failed: $($_.Exception.Message)"
            }
        }
    }
} finally {
    foreach ($subscription in $subscriptions) {
        Unregister-Event -SubscriptionId $subscription.Id -ErrorAction SilentlyContinue
    }
    $watcher.Dispose()
}
