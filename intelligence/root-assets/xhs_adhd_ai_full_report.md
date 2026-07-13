# ADHD Scout for Xiaohongshu
# 用法: .\adhd_scout.ps1 -Keyword "ADHD vibe coding" -Limit 10
# 或:   .\adhd_scout.ps1 -Preset "vibe" -Limit 5

param(
    [string]$Keyword = "",
    [string]$Preset = "",
    [int]$Limit = 10,
    [switch]$Analyze,
    [string]$Url = ""
)

# 预设关键词库（ADHD × AI 交叉检索专用）
$presets = @{
    "adhd" = "ADHD"
    "vibe" = "ADHD vibe coding"
    "xie" = "ADHD 邪修"
    "ai" = "ADHD AI工具"
    "cursor" = "ADHD Cursor"
    "agent" = "ADHD Agent"
    "focus" = "ADHD 专注力"
    "startup" = "ADHD 启动困难"
    "emotion" = "ADHD 情绪"
    "adult" = "成人 ADHD 确诊"
}

# 解析 preset
if ($Preset -and $presets.ContainsKey($Preset)) {
    $Keyword = $presets[$Preset]
}

if (-not $Keyword -and -not $Url) {
    Write-Host "用法示例：" -ForegroundColor Cyan
    Write-Host "  .\adhd_scout.ps1 -Keyword 'ADHD vibe coding' -Limit 10"
    Write-Host "  .\adhd_scout.ps1 -Preset vibe -Limit 5"
    Write-Host "  .\adhd_scout.ps1 -Analyze -Url 'https://www.xiaohongshu.com/explore/xxxxx'"
    Write-Host ""
    Write-Host "可用预设："
    $presets.GetEnumerator() | ForEach-Object { Write-Host "  $($_.Key) → $($_.Value)" }
    exit
}

# 工具目录
$baseDir = "C:\tools\xiaohongshu-adhd-scout"
$searchTool = "$baseDir\redbook-search-comment-mcp\search.py"
$analyzeTool = "$baseDir\xiaohongshu-summarizer-skill"

# 检查工具是否已安装
if (-not (Test-Path $searchTool)) {
    Write-Host "[错误] redbook-search-comment-mcp 未安装" -ForegroundColor Red
    Write-Host "请先按《小红书ADHD侦察工具_安装指南.md》完成 Step 1–4" -ForegroundColor Yellow
    exit 1
}

# 执行搜索
if ($Keyword) {
    Write-Host "=== 小红书 ADHD 侦察 ===" -ForegroundColor Cyan
    Write-Host "关键词: $Keyword" -ForegroundColor Green
    Write-Host "数量: $Limit" -ForegroundColor Green
    Write-Host ""

    # 调用 Python 搜索脚本
    & python $searchTool --keyword $Keyword --limit $Limit

    Write-Host ""
    Write-Host "=== 搜索完成 ===" -ForegroundColor Cyan
    Write-Host "把上面的结果复制给 Agent，让它帮你分析内容质量和选题价值。" -ForegroundColor Gray
}

# 执行单条分析
if ($Analyze -and $Url) {
    if (-not (Test-Path $analyzeTool)) {
        Write-Host "[错误] xiaohongshu-summarizer-skill 未安装" -ForegroundColor Red
        exit 1
    }

    Write-Host "=== 分析笔记 ===" -ForegroundColor Cyan
    Write-Host "URL: $Url" -ForegroundColor Green
    Write-Host ""

    Set-Location $analyzeTool
    & npm run analyze --url=$Url
}
