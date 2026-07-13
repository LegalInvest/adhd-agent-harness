param(
    [string]$ConfigPath = ".\git-sync.config.json",
    [string]$RemoteUrl = "",
    [string]$RemoteName = "",
    [string]$Branch = "",
    [string]$Message = "",
    [string]$UserName = "",
    [string]$UserEmail = "",
    [switch]$InitOnly,
    [switch]$DryRun,
    [switch]$CheckAuth,
    [switch]$AllowPrivatePatterns
)

$ErrorActionPreference = "Stop"

function Write-Step {
    param([string]$Message)
    Write-Host "[git-sync] $Message"
}

function Resolve-RepoDir {
    if ($PSScriptRoot) { return $PSScriptRoot }
    return (Get-Location).Path
}

function Invoke-Native {
    param(
        [string]$FilePath,
        [string[]]$Arguments,
        [switch]$NoThrow
    )
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

    if ($code -ne 0 -and -not $NoThrow) {
        throw "$FilePath $($Arguments -join ' ') failed:`n$($output -join "`n")"
    }

    return [pscustomobject]@{
        Code = $code
        Output = ($output -join "`n").Trim()
    }
}

function Invoke-Git {
    param(
        [string[]]$GitArgs,
        [switch]$NoThrow
    )
    return Invoke-Native -FilePath "git" -Arguments $GitArgs -NoThrow:$NoThrow
}

function Invoke-RepoGit {
    param(
        [string]$GitDir,
        [string]$WorkTree,
        [string[]]$GitArgs,
        [switch]$NoThrow
    )
    $args = @("--git-dir", $GitDir, "--work-tree", $WorkTree) + $GitArgs
    return Invoke-Git -GitArgs $args -NoThrow:$NoThrow
}

function Read-GitValue {
    param(
        [string]$GitDir,
        [string]$WorkTree,
        [string[]]$GitArgs
    )
    $result = Invoke-RepoGit -GitDir $GitDir -WorkTree $WorkTree -GitArgs $GitArgs -NoThrow
    if ($result.Code -ne 0) { return "" }
    return $result.Output.Trim()
}

function Read-Config {
    param([string]$Path)
    $resolved = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($Path)
    if (-not (Test-Path -LiteralPath $resolved)) {
        return [pscustomobject]@{}
    }
    return Get-Content -LiteralPath $resolved -Raw -Encoding UTF8 | ConvertFrom-Json
}

function Merge-Setting {
    param(
        [string]$CliValue,
        [object]$Config,
        [string]$Name,
        [string]$Default = ""
    )
    if ($CliValue) { return $CliValue }
    if ($null -ne $Config -and $Config.PSObject.Properties.Name -contains $Name) {
        $value = $Config.$Name
        if ($null -ne $value -and "$value") { return "$value" }
    }
    return $Default
}

function Test-WorkTreeWrite {
    param([string]$RepoDir)
    $probe = Join-Path $RepoDir ".git-sync-write-test"
    try {
        Set-Content -LiteralPath $probe -Value "ok" -Encoding UTF8
        Remove-Item -LiteralPath $probe -Force
    } catch {
        throw "Cannot write to repository folder: $RepoDir`n$($_.Exception.Message)"
    }
}

function Test-GitHubAuth {
    if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
        return [pscustomobject]@{ Ok = $false; Message = "GitHub CLI is not installed." }
    }
    $result = Invoke-Native -FilePath "gh" -Arguments @("auth", "status") -NoThrow
    return [pscustomobject]@{
        Ok = ($result.Code -eq 0)
        Message = $result.Output
    }
}

function Assert-NoSensitiveContent {
    param(
        [string]$RepoDir,
        [bool]$Skip
    )
    if ($Skip) {
        Write-Step "Sensitive-content scan skipped by -AllowPrivatePatterns."
        return
    }

    $patterns = @(
        "AKIA[0-9A-Z]{16}",
        "ghp_[A-Za-z0-9_]{36,}",
        "github_pat_[A-Za-z0-9_]+",
        "sk-[A-Za-z0-9_-]{20,}",
        "Bearer\s+[A-Za-z0-9._-]+",
        "Authorization\s*[:=]",
        "(?i)api[_-]?key\s*[:=]",
        "(?i)secret\s*[:=]",
        "(?i)token\s*[:=]",
        "(?i)password\s*[:=]"
    )

    $files = Get-ChildItem -LiteralPath $RepoDir -Recurse -File -Force |
        Where-Object {
            $_.FullName -notmatch '\\.git\\' -and
            $_.FullName -notmatch '\\.git-sync\\' -and
            $_.FullName -notmatch '\\.git-sync-fixture\\' -and
            $_.Name -notmatch '(?i)(secret|token|credential|password)' -and
            $_.Length -lt 5MB
        }

    $hits = New-Object System.Collections.Generic.List[string]
    foreach ($file in $files) {
        try {
            $text = Get-Content -LiteralPath $file.FullName -Raw -Encoding UTF8 -ErrorAction Stop
        } catch {
            continue
        }
        foreach ($pattern in $patterns) {
            if ($text -match $pattern) {
                $relative = [System.IO.Path]::GetRelativePath($RepoDir, $file.FullName)
                $hits.Add("$relative matched $pattern")
            }
        }
    }

    if ($hits.Count -gt 0) {
        throw "Sensitive-looking content was found. Review before pushing:`n$($hits -join "`n")"
    }
    Write-Step "Sensitive-content scan passed."
}

function Save-State {
    param(
        [string]$RepoDir,
        [hashtable]$State
    )
    $stateDir = Join-Path $RepoDir ".git-sync"
    New-Item -ItemType Directory -Force -Path $stateDir | Out-Null
    $State | ConvertTo-Json -Depth 6 | Set-Content -Encoding UTF8 -LiteralPath (Join-Path $stateDir "latest.json")
}

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Git is not installed or not available in PATH."
}

$repoDir = Resolve-RepoDir
Set-Location $repoDir
Test-WorkTreeWrite -RepoDir $repoDir

$config = Read-Config -Path $ConfigPath
$RemoteName = Merge-Setting -CliValue $RemoteName -Config $config -Name "remoteName" -Default "origin"
$RemoteUrl = Merge-Setting -CliValue $RemoteUrl -Config $config -Name "remoteUrl"
$Branch = Merge-Setting -CliValue $Branch -Config $config -Name "branch" -Default "main"
$UserName = Merge-Setting -CliValue $UserName -Config $config -Name "userName"
$UserEmail = Merge-Setting -CliValue $UserEmail -Config $config -Name "userEmail"

$stateDir = Join-Path $repoDir ".git-sync"
$gitDir = Join-Path $stateDir "repo.git"
New-Item -ItemType Directory -Force -Path $stateDir | Out-Null

if ($CheckAuth) {
    $auth = Test-GitHubAuth
    if ($auth.Ok) {
        Write-Step "GitHub CLI auth OK."
    } else {
        Write-Step "GitHub CLI auth is not ready: $($auth.Message)"
    }
}

Assert-NoSensitiveContent -RepoDir $repoDir -Skip:$AllowPrivatePatterns

if (-not (Test-Path -LiteralPath $gitDir)) {
    Write-Step "Initializing isolated Git metadata at .git-sync/repo.git."
    Invoke-Git @("init", "--bare", $gitDir) | Out-Null
}

Invoke-RepoGit -GitDir $gitDir -WorkTree $repoDir -GitArgs @("config", "core.quotepath", "false") | Out-Null
Invoke-RepoGit -GitDir $gitDir -WorkTree $repoDir -GitArgs @("symbolic-ref", "HEAD", "refs/heads/$Branch") | Out-Null

if ($UserName) {
    Invoke-RepoGit -GitDir $gitDir -WorkTree $repoDir -GitArgs @("config", "user.name", $UserName) | Out-Null
}
if ($UserEmail) {
    Invoke-RepoGit -GitDir $gitDir -WorkTree $repoDir -GitArgs @("config", "user.email", $UserEmail) | Out-Null
}

$name = Read-GitValue -GitDir $gitDir -WorkTree $repoDir -GitArgs @("config", "--get", "user.name")
$email = Read-GitValue -GitDir $gitDir -WorkTree $repoDir -GitArgs @("config", "--get", "user.email")
if (-not $name -or -not $email) {
    throw "Git identity is not set. Fill userName/userEmail in git-sync.config.json or pass -UserName/-UserEmail."
}

$remotesText = Read-GitValue -GitDir $gitDir -WorkTree $repoDir -GitArgs @("remote")
$remotes = @($remotesText -split "`n" | Where-Object { $_ })
if ($RemoteUrl) {
    if ($remotes -contains $RemoteName) {
        Write-Step "Updating remote $RemoteName."
        Invoke-RepoGit -GitDir $gitDir -WorkTree $repoDir -GitArgs @("remote", "set-url", $RemoteName, $RemoteUrl) | Out-Null
    } else {
        Write-Step "Adding remote $RemoteName."
        Invoke-RepoGit -GitDir $gitDir -WorkTree $repoDir -GitArgs @("remote", "add", $RemoteName, $RemoteUrl) | Out-Null
    }
} elseif (-not ($remotes -contains $RemoteName)) {
    throw "No Git remote is configured. Fill remoteUrl in git-sync.config.json or pass -RemoteUrl."
}

$status = Read-GitValue -GitDir $gitDir -WorkTree $repoDir -GitArgs @("status", "--porcelain")
if ($InitOnly) {
    Save-State -RepoDir $repoDir -State @{
        mode = "init"
        ok = $true
        git_dir = $gitDir
        repo_root = $repoDir
        remote = $RemoteName
        branch = $Branch
        pending_changes = [bool]$status
        checked_at = (Get-Date).ToString("o")
    }
    Write-Step "Repository initialized and remote checked. No commit created."
    exit 0
}

if (-not $status) {
    Save-State -RepoDir $repoDir -State @{
        mode = "sync"
        ok = $true
        git_dir = $gitDir
        repo_root = $repoDir
        remote = $RemoteName
        branch = $Branch
        changed = $false
        checked_at = (Get-Date).ToString("o")
    }
    Write-Step "No changes to sync."
    exit 0
}

Write-Step "Changes detected."
if ($DryRun) {
    Write-Host $status
    Save-State -RepoDir $repoDir -State @{
        mode = "dry-run"
        ok = $true
        git_dir = $gitDir
        repo_root = $repoDir
        remote = $RemoteName
        branch = $Branch
        pending_changes = $status
        checked_at = (Get-Date).ToString("o")
    }
    Write-Step "Dry run completed. Nothing was committed or pushed."
    exit 0
}

Invoke-RepoGit -GitDir $gitDir -WorkTree $repoDir -GitArgs @("add", "-A") | Out-Null

$staged = Read-GitValue -GitDir $gitDir -WorkTree $repoDir -GitArgs @("diff", "--cached", "--name-only")
if (-not $staged) {
    Write-Step "No staged changes to commit."
    exit 0
}

if (-not $Message) {
    $Message = "sync: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
}

Write-Step "Creating commit: $Message"
Invoke-RepoGit -GitDir $gitDir -WorkTree $repoDir -GitArgs @("commit", "-m", $Message) | Out-Null

$upstream = Read-GitValue -GitDir $gitDir -WorkTree $repoDir -GitArgs @("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}")
if ($upstream) {
    Write-Step "Rebasing local changes on $upstream."
    Invoke-RepoGit -GitDir $gitDir -WorkTree $repoDir -GitArgs @("pull", "--rebase", "--autostash") | Out-Null
}

Write-Step "Pushing to $RemoteName/$Branch."
Invoke-RepoGit -GitDir $gitDir -WorkTree $repoDir -GitArgs @("push", "-u", $RemoteName, $Branch) | Out-Null

$commit = Read-GitValue -GitDir $gitDir -WorkTree $repoDir -GitArgs @("rev-parse", "--short", "HEAD")
Save-State -RepoDir $repoDir -State @{
    mode = "sync"
    ok = $true
    git_dir = $gitDir
    repo_root = $repoDir
    remote = $RemoteName
    branch = $Branch
    commit = $commit
    message = $Message
    synced_at = (Get-Date).ToString("o")
}

Write-Step "Synced commit $commit to $RemoteName/$Branch."
