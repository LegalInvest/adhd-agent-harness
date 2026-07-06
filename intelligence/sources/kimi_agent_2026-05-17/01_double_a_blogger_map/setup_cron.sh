#!/bin/bash
# ADHD×AI 情报自动流 - 定时任务设置脚本
# 每日8:00自动运行，生成情报日报

echo "正在设置ADHD×AI情报自动流定时任务..."

# 获取脚本绝对路径
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/adhd_ai_intelligence_system.py"
LOG_FILE="$SCRIPT_DIR/adhd_ai_data/cron.log"

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "错误: 需要安装 Python 3"
    exit 1
fi

# 安装依赖
echo "安装依赖..."
pip3 install feedparser anthropic python-dotenv requests 2>/dev/null || pip install feedparser anthropic python-dotenv requests

# 创建数据目录
mkdir -p "$SCRIPT_DIR/adhd_ai_data/briefings"
mkdir -p "$SCRIPT_DIR/adhd_ai_data/ideas"
mkdir -p "$SCRIPT_DIR/adhd_ai_data/creators"
mkdir -p "$SCRIPT_DIR/adhd_ai_data/tools"

# 添加定时任务
crontab -l > /tmp/current_crontab 2>/dev/null || true

# 移除旧任务
sed -i '/adhd_ai_intelligence_system.py/d' /tmp/current_crontab

# 添加新任务: 每天8:00运行
NEW_JOB="0 8 * * * cd \"$SCRIPT_DIR\" && /usr/bin/env python3 \"$PYTHON_SCRIPT\" >> \"$LOG_FILE\" 2>&1"
echo "$NEW_JOB" >> /tmp/current_crontab

crontab /tmp/current_crontab
rm /tmp/current_crontab

echo "✅ 定时任务设置完成!"
echo "   运行时间: 每天 8:00"
echo "   脚本路径: $PYTHON_SCRIPT"
echo "   日志文件: $LOG_FILE"
echo ""
echo "📋 手动运行测试:"
echo "   cd \"$SCRIPT_DIR\" && python3 adhd_ai_intelligence_system.py"
echo ""
echo "📋 查看已设置的任务:"
echo "   crontab -l"
echo ""
echo "📋 停止定时任务:"
echo "   crontab -e  # 删除对应行"
