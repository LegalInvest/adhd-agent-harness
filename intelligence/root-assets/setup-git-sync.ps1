param(
    [string]$RemoteUrl = "",
    [string]$UserName = "",
    [string]$UserEmail = "",
    [string]$Branch = "main",
    [string]$RemoteName = "origin"
)

$ErrorActionPreference = "Stop"

$repoDir = if ($PSScriptRoot) { $PSScriptRoot } else { (Get-Location).Path }
$configPath = Join-Path $repoDir "git-sync.config.json"

function Read-Required {
    param(
        [string]$Value,
        [string]$Prompt
    )
    if ($Value) { return $Value }
    $answer = Read-Host $Prompt
    if (-not $answer) {
        throw "$Prompt is required."
    }
    return $answer
}

$RemoteUrl = Read-Required -Value $RemoteUrl -Prompt "Git remote URL"
$UserName = Read-Required -Value $UserName -Prompt "Git user name"
$UserEmail = Read-Required -Value $UserEmail -Prompt "Git user email"

$config = [ordered]@{
    remoteUrl = $RemoteUrl
    remoteName = $RemoteName
    branch = $Branch
    userName = $UserName
    userEmail = $UserEmail
}

$config | ConvertTo-Json -Depth 4 | Set-Content -Encoding UTF8 -LiteralPath $configPath
Write-Host "Wrote $configPath"

& powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $repoDir "git-sync.ps1") -ConfigPath $configPath -InitOnly -CheckAuth
