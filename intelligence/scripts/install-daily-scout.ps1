param(
    [string]$TaskName = "adhd-ai-daily-scout",
    [string]$At = "08:05",
    [switch]$RunNow,
    [switch]$NoLlm
)

$ErrorActionPreference = "Stop"
$RepoRoot = Split-Path -Parent $PSScriptRoot
$Runner = Join-Path $RepoRoot "scripts\run-daily-scout.ps1"

if (-not (Test-Path $Runner)) {
    throw "Missing runner script: $Runner"
}

$time = [datetime]::ParseExact($At, "HH:mm", $null)
$trigger = New-ScheduledTaskTrigger -Daily -At $time
$argumentParts = @(
    "-NoProfile",
    "-ExecutionPolicy", "Bypass",
    "-File", "`"$Runner`""
)
if ($NoLlm) {
    $argumentParts += "-NoLlm"
}
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument ($argumentParts -join " ") -WorkingDirectory $RepoRoot
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 20)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "Daily ADHD×AI self-growing evidence scout for 400 content packs" -Force | Out-Null

Write-Host "Installed scheduled task: $TaskName at $At"
Write-Host "Runner: $Runner"

if ($RunNow) {
    Start-ScheduledTask -TaskName $TaskName
    Write-Host "Started scheduled task once: $TaskName"
}
