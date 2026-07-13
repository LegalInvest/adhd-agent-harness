#!/usr/bin/env python3
"""
ADHD×AI 情报自动流 - 主运行脚本
Usage: python run.py [--daily|--weekly|--test]
"""
import argparse
import yaml
import os
import sys
from datetime import datetime
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from collectors.arxiv import ArxivCollector
from collectors.reddit import RedditCollector
from processors.intelligence_processor import IntelligenceProcessor

class ADHDIntelFlow:
    """ADHD×AI 情报自动流主控制器"""

    def __init__(self, config_path: str = "config/config.yaml"):
        self.config_path = config_path
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        self.output_dir = self.config['output']['output_dir']
        self.today = datetime.now()

    def run_daily(self):
        """运行每日情报收集"""
        print("=" * 60)
        print(f"🧠 ADHD×AI 情报自动流 - 每日运行")
        print(f"⏰ {self.today.strftime('%Y-%m-%d %H:%M')}")
        print("=" * 60)

        # 1. 数据收集
        print("\n📡 阶段 1: 数据收集")
        all_raw_items = self._collect_all()

        if not all_raw_items:
            print("⚠️ 未收集到任何数据")
            return

        # 2. 智能处理
        print(f"\n🧩 阶段 2: 智能处理 ({len(all_raw_items)} 条原始数据)")
        processor = IntelligenceProcessor(self.config_path)
        processed_items = processor.process(all_raw_items)

        # 3. 生成输出
        print(f"\n✍️ 阶段 3: 内容生成 ({len(processed_items)} 条重要情报)")
        self._generate_outputs(processed_items)

        # 4. 深度选题提醒
        deep_items = [p for p in processed_items if p.is_deep_draft_trigger]
        if deep_items:
            print(f"\n🚨 发现 {len(deep_items)} 个深度选题触发器!")
            for item in deep_items:
                print(f"   📌 [{item.importance:.1f}] {item.raw.title[:60]}")

        print("\n✅ 每日运行完成!")

    def _collect_all(self):
        """收集所有数据源"""
        all_items = []

        # arXiv
        if self.config['data_sources']['arxiv']['enabled']:
            print("  📚 [arXiv] 收集论文中...")
            collector = ArxivCollector(self.config['data_sources']['arxiv'])
            items = collector.collect()
            all_items.extend(items)

        # Reddit
        if self.config['data_sources']['reddit']['enabled']:
            print("  👥 [Reddit] 收集社区讨论中...")
            collector = RedditCollector(self.config['data_sources']['reddit'])
            items = collector.collect()
            all_items.extend(items)

        return all_items

    def _generate_outputs(self, items: list):
        """生成所有输出格式"""
        os.makedirs(f"{self.output_dir}/daily", exist_ok=True)
        os.makedirs(f"{self.output_dir}/drafts", exist_ok=True)

        date_str = self.today.strftime('%Y%m%d')

        # 每日简报
        if self.config['output']['formats']['daily_brief']['enabled']:
            self._write_daily_brief(items, f"{self.output_dir}/daily/brief_{date_str}.md")

        # 社交媒体动态
        if self.config['output']['formats']['social_posts']['enabled']:
            self._write_social_posts(items, f"{self.output_dir}/daily/social_{date_str}.md")

        # 深度选题
        deep_items = [p for p in items if p.is_deep_draft_trigger]
        if deep_items:
            self._write_deep_triggers(deep_items, f"{self.output_dir}/drafts/triggers_{date_str}.md")

    def _write_daily_brief(self, items, filepath):
        """生成每日简报"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# ADHD×AI 情报简报 | {self.today.strftime('%Y年%m月%d日')}\n\n")
            f.write(f"> 今日收集 {sum(1 for _ in items)} 条情报 | 重要情报 {len(items)} 条\n\n")
            f.write("---\n\n")

            # 按分类分组
            by_category = {}
            for item in items:
                cat = item.category
                if cat not in by_category:
                    by_category[cat] = []
                by_category[cat].append(item)

            for cat, cat_items in sorted(by_category.items()):
                f.write(f"## {cat} ({len(cat_items)}条)\n\n")
                for item in cat_items[:5]:  # 每类最多5条
                    f.write(f"### [{item.importance:.1f}] {item.raw.title[:100]}\n\n")
                    f.write(f"**来源**: {item.raw.source_name} | **时间**: {item.raw.published_at.strftime('%Y-%m-%d') if item.raw.published_at else '未知'}\n\n")
                    f.write(f"{item.summary_zh}\n\n")
                    f.write(f"💡 **洞察**: {item.key_insight}\n\n")
                    if item.connections:
                        f.write(f"🔗 **知识连接**:\n")
                        for conn in item.connections:
                            f.write(f"  - {conn}\n")
                    f.write(f"\n[原文链接]({item.raw.url})\n\n---\n\n")

        print(f"  📄 每日简报已生成: {filepath}")

    def _write_social_posts(self, items, filepath):
        """生成社交媒体动态"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# 社交媒体动态稿 | {self.today.strftime('%Y年%m月%d日')}\n\n")
            f.write("---\n\n")

            for i, item in enumerate(items[:8], 1):
                f.write(f"## 动态 {i}\n\n")
                f.write(f"```{item.social_post}```\n\n")
                f.write(f"**标签**: {item.category} | **重要性**: {item.importance:.1f}\n\n---\n\n")

        print(f"  📱 社交媒体动态稿已生成: {filepath}")

    def _write_deep_triggers(self, items, filepath):
        """生成深度选题触发器"""
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# 🚨 深度选题触发器 | {self.today.strftime('%Y年%m月%d日')}\n\n")
            f.write("以下情报的重要性评分超过阈值，建议深入研究并生成存稿。\n\n")
            f.write("---\n\n")

            for item in items:
                f.write(f"## [{item.importance:.1f}/10] {item.raw.title[:100]}\n\n")
                f.write(f"**分类**: {item.category}\n")
                f.write(f"**来源**: {item.raw.source_name}\n")
                f.write(f"**链接**: {item.raw.url}\n\n")
                f.write(f"**为什么重要**: {item.key_insight}\n\n")
                f.write(f"**建议角度**: \n")
                f.write(f"- 这是什么？（事实层面）\n")
                f.write(f"- 为什么重要？（意义层面）\n")
                f.write(f"- 和之前的什么发现连接？（知识图谱层面）\n")
                f.write(f"- 对ADHDer有什么实际影响？（行动层面）\n\n---\n\n")

        print(f"  🚨 深度选题触发器已生成: {filepath}")

    def run_test(self):
        """测试运行 - 展示系统能力"""
        print("=" * 60)
        print("🧪 ADHD×AI 情报自动流 - 测试模式")
        print("=" * 60)

        # 使用模拟数据展示系统能力
        from collectors.base import RawItem

        mock_items = [
            RawItem(
                id="test001",
                source="arxiv",
                source_name="arXiv",
                title="Machine Learning Predicts ADHD Treatment Response from Digital Phenotyping Data",
                content="We developed a deep learning model using smartphone sensor data to predict individual response to methylphenidate treatment in ADHD patients. The model achieved 87% accuracy using features extracted from 2-week digital phenotyping periods.",
                url="https://arxiv.org/abs/2605.001",
                author="Zhang et al.",
                published_at=datetime.now(),
                raw_data={"categories": ["cs.AI", "cs.LG"]}
            ),
            RawItem(
                id="test002", 
                source="reddit",
                source_name="r/ADHD",
                title="I built an AI voice assistant that helps me remember to take my meds and it's changed my life",
                content="After years of forgetting my medication, I built a simple AI assistant using Claude API that calls me every morning, asks how I'm feeling, and gently reminds me about my medication. It also keeps a mood log that my psychiatrist finds incredibly useful.",
                url="https://reddit.com/r/ADHD/comments/test002",
                author="u/neurodivergent_coder",
                published_at=datetime.now(),
                raw_data={"score": 2847, "comments": 312},
                score=2847
            ),
            RawItem(
                id="test003",
                source="arxiv",
                source_name="arXiv",
                title="ADHD and Large Language Models: A Study on AI-Assisted Writing Support for Adults with Executive Function Deficits",
                content="This study examines how LLM-based writing assistants affect task completion rates in adults with ADHD. Participants using AI-assisted writing tools showed 43% improvement in essay completion rates compared to control group.",
                url="https://arxiv.org/abs/2605.003",
                author="Johnson & Martinez",
                published_at=datetime.now(),
                raw_data={"categories": ["cs.CL", "cs.HC"]}
            ),
            RawItem(
                id="test004",
                source="reddit",
                source_name="r/ADHD_Programmers",
                title="Is anyone else using Claude Code as an external executive function? It feels like having a second brain",
                content="I've been using Claude Code integrated with my Obsidian vault for 3 months now. It helps me track tasks, organize notes, and most importantly - it asks me the questions I should be asking myself but never do. It's like having an executive function prosthetic.",
                url="https://reddit.com/r/ADHD_Programmers/comments/test004",
                author="u/weskennedy_fan",
                published_at=datetime.now(),
                raw_data={"score": 1523, "comments": 189},
                score=1523
            ),
        ]

        print(f"\n📊 模拟数据: {len(mock_items)} 条")

        # 处理
        processor = IntelligenceProcessor(self.config_path)
        processed = processor.process(mock_items)

        print(f"\n📊 处理后: {len(processed)} 条重要情报")

        for p in processed:
            print(f"\n{'='*50}")
            print(f"📌 [{p.importance:.1f}] {p.category}")
            print(f"   {p.raw.title[:80]}")
            print(f"   💡 {p.key_insight}")
            if p.is_deep_draft_trigger:
                print(f"   🚨 深度选题触发!")

        # 生成输出
        self._generate_outputs(processed)
        print("\n✅ 测试完成!")


def main():
    parser = argparse.ArgumentParser(description="ADHD×AI 情报自动流")
    parser.add_argument("--daily", action="store_true", help="运行每日收集")
    parser.add_argument("--weekly", action="store_true", help="运行周报生成")
    parser.add_argument("--test", action="store_true", help="测试模式(使用模拟数据)")

    args = parser.parse_args()

    flow = ADHDIntelFlow()

    if args.test:
        flow.run_test()
    elif args.weekly:
        print("周报功能开发中...")
    else:
        # 默认运行每日收集
        flow.run_daily()


if __name__ == "__main__":
    main()
