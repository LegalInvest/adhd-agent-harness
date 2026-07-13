"""
人物案例检索器：为每篇文章注入真实人物 harness 案例。

两个数据源（均来自用户与豆包整理的一手资料）：
- data/harness_figures.json —— 100 位 ADHD 特质名人（孔子/王阳明/达芬奇/马斯克…）
  及其「专属 harness 自我管理系统」，是「harness＝外部执行功能层」的人类活教材。
- data/adhd_entrepreneurs.json —— 500 位 ADHD 创业者/投资人（Branson/Neeleman…，
  含验证等级与来源），外加相关性研究统计（如 ADHD 人群创业概率 6.25 倍）。

按选题的脊柱概念 / 关键词 / 分类做确定性轮转匹配，保证 400 篇文章
覆盖尽可能多的不同人物，且同一篇文章每次重跑取到相同案例（可缓存）。
"""

from __future__ import annotations

import hashlib
import json
import os

from engine import harness_figures

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
ENTREPRENEURS_FILE = os.path.join(DATA_DIR, "adhd_entrepreneurs.json")

# 脊柱概念 → 人物 harness 文本里的匹配信号词
SPINE_SIGNALS = {
    "外部执行功能层": ["清单", "日课", "计划", "秘书", "助理", "流程", "制度", "反省"],
    "生成核心与调度层": ["点子", "创意", "灵感", "委托", "授权", "团队", "合伙"],
    "拐杖与脚手架": ["习惯", "戒", "自律", "训练", "修炼", "日课"],
    "外部记忆": ["笔记", "记录", "手帐", "日记", "备忘"],
    "任务分解": ["拆", "分解", "步骤", "小目标", "清单"],
    "重锚定": ["静坐", "冥想", "反省", "复盘", "祷告", "仪式"],
    "身体在场": ["同伴", "团队", "共修", "问责", "师友"],
}


def _seed(text: str) -> int:
    return int(hashlib.md5(text.encode("utf-8")).hexdigest()[:8], 16)


def load_entrepreneurs(path: str = ENTREPRENEURS_FILE) -> dict:
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


class CaseStudyRetriever:
    def __init__(self):
        self.figures = harness_figures.load_figures()
        data = load_entrepreneurs()
        self.entrepreneurs = [
            p for p in data.get("people", [])
            if p.get("type") == "Person" and p.get("notable_traits")
        ]
        self.correlation_stats = data.get("correlation_research", [])

    @property
    def available(self) -> bool:
        return bool(self.figures or self.entrepreneurs)

    def _match_figures(self, spine: str, keywords: list[str]) -> list[dict]:
        signals = SPINE_SIGNALS.get(spine, [])
        scored = []
        for f in self.figures:
            text = (f.get("harness_system", "") + f.get("adhd_traits", ""))
            score = sum(1 for s in signals if s in text)
            score += sum(1 for k in keywords if k and k in text)
            scored.append((score, f))
        scored.sort(key=lambda x: -x[0])
        return [f for _, f in scored]

    def cases_for_topic(self, topic: dict, offset: int = 0) -> list[dict]:
        """返回 2-3 个与选题匹配的人物案例（1-2 名人 + 1 创业者/投资人）。"""
        spine = topic.get("spine", "")
        keywords = [str(k) for k in topic.get("keywords", [])]
        title = topic.get("title", "")
        cases = []

        ranked = self._match_figures(spine, keywords)
        if ranked:
            # 头部取最匹配的一位，第二位按 offset 轮转保证覆盖面
            top = ranked[0]
            rot = ranked[1:21] or ranked
            second = rot[(_seed(title) + offset) % len(rot)]
            for f in (top, second):
                if any(c["name"] == f["name"] for c in cases):
                    continue
                cases.append({
                    "name": f["name"],
                    "kind": "名人 harness",
                    "text": (
                        f"{f['name']}（{f.get('era','')}）— ADHD 特质：{f.get('adhd_traits','')}；"
                        f"专属 harness：{f.get('harness_system','')}；"
                        f"成就：{f.get('achievements','')}"
                    ),
                })

        if self.entrepreneurs:
            pool = self.entrepreneurs
            if topic.get("category_id") == "entrepreneurship":
                pool = [p for p in pool if p.get("verification_level") in ("S", "A")] or pool
            e = pool[(_seed(title) + offset * 7) % len(pool)]
            desc = (
                f"{e['name']}（{e.get('title','')}, {e.get('organization','')}, "
                f"{e.get('country','')}）— {e.get('diagnosis_type','ADHD')}；"
                f"特质：{e.get('notable_traits','')}"
            )
            if e.get("known_investments"):
                desc += f"；代表作/投资：{e['known_investments']}"
            cases.append({
                "name": e["name"],
                "kind": "ADHD 创业者/投资人",
                "text": desc,
            })
        return cases[:3]

    def stat_for_topic(self, topic: dict) -> str:
        """返回一条创业者相关性统计（真实来源），供文章引用。"""
        if not self.correlation_stats:
            return ""
        s = self.correlation_stats[_seed(topic.get("title", "")) % len(self.correlation_stats)]
        return (
            f"{s.get('metric','')}: ADHD 组 {s.get('adhd_group','')} vs "
            f"对照组 {s.get('control_group','')}（来源：{s.get('source','')}）"
        )


if __name__ == "__main__":
    r = CaseStudyRetriever()
    print(f"名人 {len(r.figures)} / 创业者 {len(r.entrepreneurs)} / 统计 {len(r.correlation_stats)}")
    demo = {"title": "ADHD 的任务分解", "spine": "任务分解", "keywords": ["清单"], "category_id": "time-mgmt"}
    for c in r.cases_for_topic(demo, 3):
        print("-", c["kind"], c["name"], c["text"][:80])
    print(r.stat_for_topic(demo))
