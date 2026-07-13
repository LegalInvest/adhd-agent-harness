param(
    [string]$ConfigPath = ".\git-sync.config.json"
)

$ErrorActionPreference = "Stop"

$repoDir = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }
$configFullPath = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath((Join-Path $repoDir $ConfigPath))

function Write-Check {
    param(
        [bool]$Ok,
        [string]$Name,
        [string]$Detail = ""
    )
    $prefix = if ($Ok) { "OK" } else { "NEEDS_INPUT" }
    if ($Detail) {
        Write-Host "[$prefix] $Name - $Detail"
    } else {
        Write-Host "[$prefix] $Name"
    }
}

$git = Get-Command git -ErrorAction SilentlyContinue
Write-Check -Ok ([bool]$git) -Name "Git installed" -Detail $(if ($git) { $git.Source } else { "Install Git for Windows." })

$gh = Get-Command gh -ErrorAction SilentlyContinue
Write-Check -Ok ([bool]$gh) -Name "GitHub CLI installed" -Detail $(if ($gh) { $gh.Source } else { "Install GitHub CLI." })

if ($gh) {
    $previousErrorActionPreference = $ErrorActionPreference
    $previousNativeErrorActionPreference = $Global:PSNativeCommandUseErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        if (Get-Variable -Name PSNativeCommandUseErrorActionPreference -Scope Global -ErrorAction SilentlyContinue) {
            $Global:PSNativeCommandUseErrorActionPreference = $false
        }
        $auth = & gh auth status 2>&1
        $authCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $previousErrorActionPreference
        if (Get-Variable -Name PSNativeCommandUseErrorActionPreference -Scope Global -ErrorAction SilentlyContinue) {
            $Global:PSNativeCommandUseErrorActionPreference = $previousNativeErrorActionPreference
        }
    }
    Write-Check -Ok ($authCode -eq 0) -Name "GitHub login" -Detail (($auth -join " ") -replace "\s+", " ")
}

$configExists = Test-Path -LiteralPath $configFullPath
Write-Check -Ok $configExists -Name "Config file" -Detail $configFullPath

if ($configExists) {
    $config = Get-Content -LiteralPath $configFullPath -Raw -Encoding UTF8 | ConvertFrom-Json
    Write-Check -Ok ([bool]$config.remoteUrl) -Name "remoteUrl" -Detail $config.remoteUrl
    Write-Check -Ok ([bool]$config.userName) -Name "userName" -Detail $config.userName
    Write-Check -Ok ([bool]$config.userEmail) -Name "userEmail" -Detail $config.userEmail
    Write-Check -Ok ([bool]$config.branch) -Name "branch" -Detail $config.branch
} else {
    Write-Host "Create it with:"
    Write-Host '.\setup-git-sync.ps1 -RemoteUrl "https://github.com/YOUR_NAME/YOUR_REPO.git" -UserName "YOUR_NAME" -UserEmail "YOUR_EMAIL@example.com"'
}

Write-Host ""
Write-Host "Local E2E test:"
Write-Host ".\test-git-sync.ps1"
Write-Host ""
Write-Host "First real sync:"
Write-Host ".\git-sync.ps1 -Message `"init: ADHD AI drafts`""
