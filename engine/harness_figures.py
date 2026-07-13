"""
名人 Harness 案例库（100 位 ADHD 特质人物的自我管理系统）

这是脊柱论点「harness ＝ 外部执行功能层」的**人类活教材**：从孔子、老子、
王阳明、曾国藩到达芬奇、爱迪生、马斯克……每个人都用一套外挂的自我管理系统
（礼/日课/静坐反省/清单/routine…）补上先天偏弱的执行调度层。这与「给 LLM
套 harness（记忆/分解/验证/重锚定）」结构同构——只不过一个是生物脑外接文化脚手架，
一个是生成模型外接软件脚手架。

来源：用户与豆包整理的《100 位 ADHD 名人 Harness 大全》（姓名 / 时代 /
核心 ADHD 特质 / 专属 Harness 自我管理系统 / 核心思想来源 / 主要成就）。

作为脊柱的第二类第一手证据（人类侧真实案例），在知识萃取 / wiki 取材里
以次高优先级（仅次于 28 篇同构论文）注入，供文章引用真实人物案例。
"""

from __future__ import annotations

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
FIGURES_FILE = os.path.join(DATA_DIR, "harness_figures.json")


def load_figures(path: str = FIGURES_FILE) -> list[dict]:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def _abstract(f: dict) -> str:
    parts = [f"{f['name']}（{f['era']}）"]
    if f.get("adhd_traits"):
        parts.append(f"ADHD 特质：{f['adhd_traits']}")
    if f.get("harness_system"):
        parts.append(f"专属 harness 自我管理系统：{f['harness_system']}")
    if f.get("achievements"):
        parts.append(f"主要成就：{f['achievements']}")
    return "。".join(parts)


def as_articles() -> list[dict]:
    """映射成「文章」结构：每位人物一条，domain=adhd（人类侧的 harness 实证）。"""
    out = []
    for f in load_figures():
        title = f"{f['name']} 的 harness 自我管理系统"
        abstract = _abstract(f)
        out.append({
            "title": title,
            "content": abstract,
            "content_length": len(abstract),
            "url": "",
            "source_title": "100 位 ADHD 名人 Harness 大全",
            "domain": "adhd",
            "is_academic": False,
            "is_harness_figure": True,
            "figure_name": f["name"],
        })
    return out


if __name__ == "__main__":
    figs = load_figures()
    print(f"已加载 {len(figs)} 位名人 harness 案例")
