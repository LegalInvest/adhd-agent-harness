"""
GRADE 证据分级（Cochrane 体系的启发式实现）。

按研究类型/来源给证据定级：荟萃分析·系统综述=高，RCT=中高，
队列/纵向=中，横断面/病例=低，预印本/博客/观点=极低。
文章生成时对引用来源显式标注证据等级，把「可信度」做成
中文 ADHD 内容里的差异化卖点。
"""

from __future__ import annotations

LEVELS = ["极低", "低", "中", "中高", "高"]

_RULES = [
    # (等级, 关键词)
    ("高", ["meta-analysis", "meta analysis", "systematic review", "umbrella review",
            "荟萃分析", "系统综述", "cochrane"]),
    ("中高", ["randomized controlled", "randomised controlled", "rct", "double-blind",
              "randomized trial", "随机对照"]),
    ("中", ["cohort", "longitudinal", "prospective study", "controlled study",
            "clinical trial", "队列", "纵向研究"]),
    ("低", ["cross-sectional", "case study", "case report", "survey", "pilot study",
            "observational", "横断面", "问卷调查", "病例报告"]),
]

_VENUE_HIGH = ["nature", "science", "lancet", "jama", "nejm", "bmj",
               "american journal of psychiatry", "biological psychiatry"]
_PREPRINT = ["arxiv", "biorxiv", "medrxiv", "psyarxiv", "techrxiv", "ssrn", "preprint", "预印本"]


def grade(text: str = "", venue: str = "", is_academic: bool = True) -> str:
    """返回证据等级：高 / 中高 / 中 / 低 / 极低"""
    t = (text or "").lower()
    v = (venue or "").lower()
    for level, kws in _RULES:
        if any(k in t for k in kws):
            # 预印本上限降一级
            if any(p in v or p in t for p in _PREPRINT) and level in ("高", "中高"):
                return "中"
            return level
    if any(p in v or p in t for p in _PREPRINT):
        return "低"
    if any(h in v for h in _VENUE_HIGH):
        return "中"
    return "低" if is_academic else "极低"


def label(text: str = "", venue: str = "", is_academic: bool = True) -> str:
    """返回可嵌入文中的标注，如「证据等级：中高（GRADE）」"""
    return f"证据等级：{grade(text, venue, is_academic)}（GRADE）"


if __name__ == "__main__":
    tests = [
        ("A meta-analysis of working memory training in ADHD", "Psychological Bulletin"),
        ("Randomized controlled trial of digital therapeutic", "Lancet Digital Health"),
        ("Cross-sectional survey of AI tool use", ""),
        ("Monotropic Artificial Intelligence", "arXiv"),
        ("某博客经验分享", ""),
    ]
    for t, v in tests:
        print(f"  [{grade(t, v)}] {t} @ {v or '—'}")
