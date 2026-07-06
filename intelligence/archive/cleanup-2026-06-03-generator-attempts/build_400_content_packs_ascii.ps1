# ASCII-safe generator for 400 content packs.
# This file intentionally contains ASCII only to avoid PowerShell encoding parser errors.
# Run from project root via run_build_400_content_packs.bat.

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$PackRoot = Join-Path $ProjectRoot "content-packs"
$IndexRoot = Join-Path $ProjectRoot "indexes"

New-Item -ItemType Directory -Force -Path $PackRoot | Out-Null
New-Item -ItemType Directory -Force -Path $IndexRoot | Out-Null

# Build Chinese strings from Unicode code points so the source stays ASCII-safe.
$QPrefix = ([string][char]0x95EE) + ([string][char]0x9898) # wenti
$DraftName = "01_" + ([string][char]0x6B63) + ([string][char]0x6587) + ".md"
$PublishName = "02_" + ([string][char]0x53D1) + ([string][char]0x5E03) + ([string][char]0x5305) + ".md"
$XhsName = "03_" + ([string][char]0x5C0F) + ([string][char]0x7EA2) + ([string][char]0x4E66) + ([string][char]0x7248) + ".md"
$ZhihuName = "04_" + ([string][char]0x77E5) + ([string][char]0x4E4E) + ([string][char]0x7248) + ".md"
$VideoName = "05_" + ([string][char]0x77ED) + ([string][char]0x89C6) + ([string][char]0x9891) + ([string][char]0x53E3) + ([string][char]0x64AD) + ".md"
$CommentName = "06_" + ([string][char]0x8BC4) + ([string][char]0x8BBA) + ([string][char]0x56DE) + ([string][char]0x6D41) + ([string][char]0x95EE) + ([string][char]0x9898) + ".md"
$FeedbackName = "07_48" + ([string][char]0x5C0F) + ([string][char]0x65F6) + ([string][char]0x56DE) + ([string][char]0x6D41) + ([string][char]0x8868) + ".md"
$TemplateName = "08_" + ([string][char]0x6A21) + ([string][char]0x677F) + ([string][char]0x5165) + ([string][char]0x53E3) + ".md"

function WriteUtf8($Path, $Value) {
    $Utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($Path, $Value, $Utf8NoBom)
}

function GetRootDraft($n) {
    $num = "{0:D3}" -f $n
    $filter = $QPrefix + $num + "_*.md"
    $matches = Get-ChildItem -Path $ProjectRoot -File -Filter $filter -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -notmatch "publish|packet|feedback" } |
        Sort-Object Name
    if ($matches.Count -gt 0) { return $matches[0] }
    return $null
}

$SPriority = @(361,394,379,321,395,297,353,356,281,306,375,387,390,391,400,337,333,350,359,393)
$APriority = @(289,320,313,318,367,370,377,381,389,396,399,392)
$DPriority = @(397,398)

$rows = @()

for ($i = 1; $i -le 400; $i++) {
    $num = "{0:D3}" -f $i
    $qid = $QPrefix + $num
    $packDir = Join-Path $PackRoot $qid
    New-Item -ItemType Directory -Force -Path $packDir | Out-Null

    $draftPath = Join-Path $packDir $DraftName
    $source = GetRootDraft $i
    $hasDraft = $false
    $title = $qid

    if ($source -ne $null) {
        Copy-Item -Path $source.FullName -Destination $draftPath -Force
        $hasDraft = $true
        $title = [System.IO.Path]::GetFileNameWithoutExtension($source.Name)
    } elseif (-not (Test-Path $draftPath)) {
        WriteUtf8 $draftPath ("# " + $qid + " - draft missing`n`nStatus: draft missing.`n")
    }

    $fileMap = @{}
    $fileMap[$PublishName] = "# " + $qid + " publish packet`n`nStatus: pending.`n`n## WeChat`n`n## XHS`n`n## Zhihu`n`n## Short video`n`n## Metrics`n"
    $fileMap[$XhsName] = "# " + $qid + " XHS version`n`nStatus: pending.`n`n## Title`n`n## Body`n`n## Tags`n`n## Comment prompt`n"
    $fileMap[$ZhihuName] = "# " + $qid + " Zhihu version`n`nStatus: pending.`n`n## Question`n`n## Answer`n"
    $fileMap[$VideoName] = "# " + $qid + " short video script`n`nStatus: pending.`n`n## First 3 seconds`n`n## 60-second script`n`n## CTA`n"
    $fileMap[$CommentName] = "# " + $qid + " comment feedback question`n`nStatus: pending.`n`n## Main question`n`n## Follow-ups`n"
    $fileMap[$FeedbackName] = "# " + $qid + " 48h feedback sheet`n`nStatus: pending.`n`n| Metric | Value | Notes |`n|---|---:|---|`n| Views | 0 | |`n| Likes | 0 | |`n| Saves | 0 | |`n| Comments | 0 | |`n| DMs | 0 | |`n| Product signal | 0 | |`n"
    $fileMap[$TemplateName] = "# " + $qid + " template entry`n`nStatus: pending.`n`n## Entry type`n`n## How to use`n`n## Copyable template`n"

    foreach ($name in $fileMap.Keys) {
        $path = Join-Path $packDir $name
        if (-not (Test-Path $path)) { WriteUtf8 $path $fileMap[$name] }
    }

    $priority = "B"
    if ($SPriority -contains $i) { $priority = "S" }
    elseif ($APriority -contains $i) { $priority = "A" }
    elseif ($DPriority -contains $i) { $priority = "D" }

    $status = "draft_missing_assets_pending"
    if ($hasDraft) { $status = "draft_present_assets_pending" }

    $meta = [ordered]@{
        id = $qid
        number = $i
        title = $title
        priority = $priority
        status = $status
        draft = $hasDraft
        publish_packet = $false
        xhs = $false
        zhihu = $false
        short_video = $false
        comment_question = $false
        feedback_sheet = $false
        template_entry = $false
        closed_loop_ready = $false
        updated_at = "2026-06-02"
    }
    $metaPath = Join-Path $packDir "meta.json"
    WriteUtf8 $metaPath ($meta | ConvertTo-Json -Depth 5)

    $rows += [pscustomobject]@{ id=$qid; priority=$priority; draft=$hasDraft; status=$status; pack=("content-packs/" + $qid) }
}

$indexLines = @()
$indexLines += "# 400 content pack index"
$indexLines += ""
$indexLines += "Generated: 2026-06-02"
$indexLines += ""
$indexLines += "| ID | Priority | Draft | Status | Pack |"
$indexLines += "|---|---|---|---|---|"
foreach ($r in $rows) {
    $draftText = "missing"
    if ($r.draft) { $draftText = "present" }
    $indexLines += "| $($r.id) | $($r.priority) | $draftText | $($r.status) | $($r.pack) |"
}
WriteUtf8 (Join-Path $IndexRoot "400-content-pack-index.md") ($indexLines -join "`n")

$gapLines = @()
$gapLines += "# 400 draft gap list"
$gapLines += ""
$gapLines += "Generated: 2026-06-02"
$gapLines += ""
$gapLines += "## Draft missing"
$gapLines += ""
foreach ($r in $rows | Where-Object { -not $_.draft }) { $gapLines += "- $($r.id)" }
WriteUtf8 (Join-Path $IndexRoot "400-draft-gap-list.md") ($gapLines -join "`n")

$presentCount = ($rows | Where-Object { $_.draft }).Count
$missingCount = 400 - $presentCount
Write-Host "Done: generated 400 content pack shells."
Write-Host "Draft present: $presentCount"
Write-Host "Draft missing: $missingCount"
Write-Host "Index: indexes/400-content-pack-index.md"
Write-Host "Gaps: indexes/400-draft-gap-list.md"
