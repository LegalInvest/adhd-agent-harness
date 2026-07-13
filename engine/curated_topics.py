"""
人工精修选题导入：从 publishing/content-packs/问题NNN/meta.json 读取
《问题XXX》系列 400 个经作者人工打磨、点火改写过的选题标题，
作为高质量候选并入问题池，参与滚动竞争（同一套双受众张力评分）。
"""

from __future__ import annotations

import json
import os
import re

PACKS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "publishing", "content-packs"
)

# 标题关键词 → (category_id, spine)
_ROUTES = [
    (["harness", "Harness", "轨道", "脚手架", "拐杖"], ("ai-tools", "拐杖与脚手架")),
    (["时间盲", "时间", "拖延", "启动"], ("time-mgmt", "外部执行功能层")),
    (["幻觉", "骗", "验证"], ("science", "幻觉与验证循环")),
    (["温度", "情绪", "风暴", "波动"], ("emotion", "采样温度与表现波动")),
    (["记忆", "缓存", "备忘"], ("ai-tools", "无状态与外部记忆")),
    (["Agent", "agent", "接口", "前额叶", "外接", "执行器"], ("ai-tools", "生成核心与调度层")),
    (["创始人", "创业", "投资", "变现", "职场", "律师", "法学"], ("career", "生成核心与调度层")),
    (["多巴胺", "刷", "上瘾", "回路"], ("lifestyle", "重锚定与目标漂移")),
    (["超聚焦", "分心", "发散", "专注"], ("focus", "上下文工程")),
    (["学习", "教育", "应试", "考试"], ("learning", "规划循环与任务分解")),
    (["名人", "孤例", "同类", "社交", "聚会"], ("community", "人在回路与身体在场")),
]


def _route(title: str) -> tuple[str, str]:
    for kws, dest in _ROUTES:
        if any(k in title for k in kws):
            return dest
    return ("science", "ADHD 大脑与 LLM 的同构")


def load_curated(packs_dir: str = PACKS_DIR) -> list[dict]:
    """读取全部 meta.json，返回 [{title, subtitle, priority, number, category_id, spine}]"""
    out = []
    if not os.path.isdir(packs_dir):
        return out
    for name in sorted(os.listdir(packs_dir)):
        meta_path = os.path.join(packs_dir, name, "meta.json")
        if not os.path.exists(meta_path):
            continue
        try:
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
        except Exception:  # noqa: BLE001 - 单包损坏不阻断
            continue
        raw = str(meta.get("title", "")).strip()
        if not raw:
            continue
        # 形如 "问题015_主标题？副标题" / "问题001_主标题_副标题"
        body = re.sub(r"^问题\d+_?", "", raw)
        if not body or body.endswith("_existing"):
            continue
        m = re.match(r"^(.+?[？?])(.+)$", body)
        if m:
            title, subtitle = m.group(1).strip(), m.group(2).strip("_ ")
        else:
            parts = body.split("_", 1)
            title = parts[0].strip()
            subtitle = parts[1].strip() if len(parts) > 1 else ""
        cat, spine = _route(title + subtitle)
        out.append({
            "title": title,
            "subtitle": subtitle,
            "priority": meta.get("priority", "B"),
            "number": meta.get("number", 0),
            "category_id": cat,
            "spine": spine,
        })
    return out


if __name__ == "__main__":
    items = load_curated()
    print(f"人工精修选题 {len(items)} 条")
    for it in items[:5]:
        print(f"  [{it['priority']}] {it['title']} | {it['subtitle'][:30]}")
