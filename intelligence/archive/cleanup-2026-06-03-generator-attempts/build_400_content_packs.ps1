# Safe generator for 400 closed-loop content pack shells.
# Run from the project root in PowerShell:
#   .\src\build_400_content_packs.ps1
# This script copies existing drafts into content-packs. It does not delete or move originals.

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$PackRoot = Join-Path $ProjectRoot "content-packs"
$IndexRoot = Join-Path $ProjectRoot "indexes"

New-Item -ItemType Directory -Force -Path $PackRoot | Out-Null
New-Item -ItemType Directory -Force -Path $IndexRoot | Out-Null

function Get-RootDraftForNumber($n) {
    $num = "{0:D3}" -f $n
    $matches = Get-ChildItem -Path $ProjectRoot -File -Filter "问题$num`_*.md" -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -notmatch "发布包|回流" } |
        Sort-Object Name
    if ($matches.Count -gt 0) { return $matches[0] }
    return $null
}

$rows = @()

for ($i = 1; $i -le 400; $i++) {
    $num = "{0:D3}" -f $i
    $packDir = Join-Path $PackRoot "问题$num"
    New-Item -ItemType Directory -Force -Path $packDir | Out-Null

    $draftTarget = Join-Path $packDir "01_正文.md"
    $draftSource = Get-RootDraftForNumber $i
    $hasDraft = $false
    $title = "问题$num"

    if ($draftSource -ne $null) {
        Copy-Item -Path $draftSource.FullName -Destination $draftTarget -Force
        $hasDraft = $true
        $title = [System.IO.Path]::GetFileNameWithoutExtension($draftSource.Name)
    } elseif (-not (Test-Path $draftTarget)) {
        Set-Content -Path $draftTarget -Encoding UTF8 -Value "# 问题$num｜待补正文`n`n状态：待写。`n"
    }

    $files = @(
        @{ name = "02_发布包.md"; content = "# 问题$num 发布包`n`n状态：待补。`n`n## 公众号版`n`n## 小红书版`n`n## 知乎版`n`n## 短视频口播版`n`n## 回流指标`n" },
        @{ name = "03_小红书版.md"; content = "# 问题$num 小红书版`n`n状态：待补。`n`n## 标题`n`n## 正文`n`n## 标签`n`n## 评论引导`n" },
        @{ name = "04_知乎版.md"; content = "# 问题$num 知乎版`n`n状态：待补。`n`n## 适配问题`n`n## 回答`n" },
        @{ name = "05_短视频口播.md"; content = "# 问题$num 短视频口播`n`n状态：待补。`n`n## 前三秒钩子`n`n## 60 秒口播`n`n## 结尾动作`n" },
        @{ name = "06_评论回流问题.md"; content = "# 问题$num 评论回流问题`n`n状态：待补。`n`n## 唯一评论问题`n`n## 分层追问`n" },
        @{ name = "07_48小时回流表.md"; content = "# 问题$num 发布后 48 小时回流表`n`n状态：待补。`n`n| 指标 | 数值 | 备注 |`n|---|---:|---|`n| 浏览 | 0 | |`n| 点赞 | 0 | |`n| 收藏 | 0 | |`n| 评论 | 0 | |`n| 私信 | 0 | |`n| 可产品化信号 | 0 | |`n" },
        @{ name = "08_模板入口.md"; content = "# 问题$num 模板入口`n`n状态：待补。`n`n## 入口类型`n`n## 使用说明`n`n## 可复制模板`n" }
    )

    foreach ($f in $files) {
        $path = Join-Path $packDir $f.name
        if (-not (Test-Path $path)) {
            Set-Content -Path $path -Encoding UTF8 -Value $f.content
        }
    }

    $priority = "B"
    if ($i -in @(361,394,379,321,395,297,353,356,281,306,375,387,390,391,400,337,333,350,359,393)) { $priority = "S" }
    elseif ($i -in @(289,320,313,318,367,370,377,381,389,396,399,392)) { $priority = "A" }
    elseif ($i -in @(397,398)) { $priority = "D" }

    $status = if ($hasDraft) { "draft_present_assets_pending" } else { "draft_missing_assets_pending" }

    $meta = [ordered]@{
        id = "问题$num"
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
    ($meta | ConvertTo-Json -Depth 5) | Set-Content -Path $metaPath -Encoding UTF8

    $rows += [pscustomobject]@{
        id = "问题$num"
        priority = $priority
        draft = $hasDraft
        status = $status
        pack = "content-packs/问题$num"
    }
}

$indexPath = Join-Path $IndexRoot "400闭环资产总索引.md"
$lines = @()
$lines += "# 400闭环资产总索引"
$lines += ""
$lines += "生成时间：2026-06-02"
$lines += ""
$lines += "| 编号 | 优先级 | 正文 | 状态 | 资产包 |"
$lines += "|---|---|---|---|---|"
foreach ($r in $rows) {
    $draftText = if ($r.draft) { "已有" } else { "待补" }
    $lines += "| $($r.id) | $($r.priority) | $draftText | $($r.status) | $($r.pack) |"
}
Set-Content -Path $indexPath -Encoding UTF8 -Value ($lines -join "`n")

$gapPath = Join-Path $IndexRoot "400缺口清单.md"
$gapLines = @()
$gapLines += "# 400缺口清单"
$gapLines += ""
$gapLines += "生成时间：2026-06-02"
$gapLines += ""
$gapLines += "## 缺正文"
$gapLines += ""
foreach ($r in $rows | Where-Object { -not $_.draft }) {
    $gapLines += "- $($r.id)"
}
Set-Content -Path $gapPath -Encoding UTF8 -Value ($gapLines -join "`n")

Write-Host "Done: created/updated 400 content pack shells under content-packs/."
Write-Host "Index: indexes/400闭环资产总索引.md"
Write-Host "Gaps: indexes/400缺口清单.md"
