"""
证据争议雷达（PaperQA2 矛盾检测 + Scite 引用方向 + 活体综述思路）。

在全量学术语料上按争议主题扫描摘要，用结论方向词极性把研究分到
「支持 / 反驳 / 中性」三桶，输出争议地图：
- data/contradictions.json   机器可读（供评分器/写作/引用标注复用）
- docs/CONTRADICTION_MAP.md  人类可读（每个争议都是「验证式问题」文章的天然选题）

每轮增量滚动后重跑本模块 = 活体综述（living review）。

CLI：python -m engine.contradictions
"""

from __future__ import annotations

import json
import re
from pathlib import Path

CORPUS_PATH = Path("data/academic_corpus.json")
JSON_OUT = Path("data/contradictions.json")
MD_OUT = Path("docs/CONTRADICTION_MAP.md")

# 争议主题：name / 主题匹配词（须同时命中 ADHD 语境）/ 中文说明
TOPICS = [
    ("stimulant_longterm", ["stimulant", "methylphenidate", "amphetamine"],
     "兴奋剂药物的长期效应"),
    ("cognitive_training", ["cognitive training", "working memory training", "brain training"],
     "认知/工作记忆训练"),
    ("neurofeedback", ["neurofeedback"], "神经反馈"),
    ("diet", ["diet", "elimination diet", "food additive", "sugar", "omega-3"],
     "饮食干预"),
    ("exercise", ["physical exercise", "physical activity", "aerobic"],
     "运动干预"),
    ("mindfulness", ["mindfulness", "meditation"], "正念冥想"),
    ("digital_intervention", ["digital intervention", "app-based", "video game", "serious game",
                              "mobile health", "mhealth"],
     "数字化干预（App/游戏）"),
    ("screen_time", ["screen time", "media use", "smartphone use"], "屏幕时间与 ADHD"),
    ("medication_growth", ["growth suppression", "height", "growth rate"],
     "药物与生长发育"),
    ("adult_outcome", ["persistence into adulthood", "adult outcome", "remission"],
     "成年后转归"),
]

_POS = ["improve", "improvement", "effective", "efficacy", "benefit", "beneficial",
        "reduce symptom", "reduced symptom", "significant reduction", "significantly reduced",
        "significant improvement", "positive effect", "ameliorat"]
_NEG = ["no significant", "no effect", "not effective", "ineffective", "no evidence",
        "no difference", "did not differ", "failed to", "lack of evidence", "not support",
        "no association", "null effect", "limited evidence", "insufficient evidence"]
_ADHD = ["adhd", "attention-deficit", "attention deficit", "hyperactivity"]


def _polarity(text: str) -> str:
    t = text.lower()
    neg = any(k in t for k in _NEG)
    pos = any(k in t for k in _POS)
    if neg and not pos:
        return "contrast"
    if pos and not neg:
        return "support"
    return "neutral"


def scan(corpus: list[dict]) -> list[dict]:
    out = []
    for key, kws, label in TOPICS:
        buckets: dict[str, list[dict]] = {"support": [], "contrast": [], "neutral": []}
        for p in corpus:
            text = f"{p.get('title', '')} {p.get('abstract', '')}"
            tl = text.lower()
            if not any(a in tl for a in _ADHD):
                continue
            if not any(k in tl for k in kws):
                continue
            buckets[_polarity(text)].append(
                {"id": p.get("id", ""), "title": p.get("title", "")[:160]}
            )
        s, c = len(buckets["support"]), len(buckets["contrast"])
        total = s + c
        if total == 0:
            continue
        # 争议度：两侧都有证据且弱势侧占比越高越有争议
        controversy = round(min(s, c) / total, 3) if total else 0.0
        out.append({
            "topic": key,
            "label": label,
            "support": s,
            "contrast": c,
            "neutral": len(buckets["neutral"]),
            "controversy": controversy,
            "examples_support": buckets["support"][:5],
            "examples_contrast": buckets["contrast"][:5],
        })
    out.sort(key=lambda x: x["controversy"], reverse=True)
    return out


def write_md(rows: list[dict]) -> None:
    lines = [
        "# ADHD 证据争议地图（自动生成）",
        "",
        "> 由 `python -m engine.contradictions` 在全量学术语料上扫描生成，每轮增量滚动后更新（活体综述）。",
        "> 争议度 = 弱势方向占比（0 = 一边倒，0.5 = 五五开）。方向判定为摘要级启发式，仅供选题与写作参考，不构成医疗建议。",
        "",
        "| 主题 | 支持方向 | 反驳/无效方向 | 争议度 |",
        "|---|---|---|---|",
    ]
    for r in rows:
        lines.append(f"| {r['label']} | {r['support']} | {r['contrast']} | {r['controversy']} |")
    lines.append("")
    for r in rows:
        lines.append(f"## {r['label']}（争议度 {r['controversy']}）")
        lines.append("")
        lines.append("支持方向样例：")
        for e in r["examples_support"]:
            lines.append(f"- {e['title']}")
        lines.append("")
        lines.append("反驳/无效方向样例：")
        for e in r["examples_contrast"]:
            lines.append(f"- {e['title']}")
        lines.append("")
    MD_OUT.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    corpus = json.loads(CORPUS_PATH.read_text(encoding="utf-8"))
    rows = scan(corpus)
    JSON_OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    write_md(rows)
    print(f"topics with evidence on both sides: {len(rows)} -> {JSON_OUT}, {MD_OUT}")
    for r in rows[:5]:
        print(f"  {r['label']}: support {r['support']} vs contrast {r['contrast']} (争议度 {r['controversy']})")


if __name__ == "__main__":
    main()
