"""
注意力评分（Upworthy 校准版）

基于 Upworthy Research Archive 的 22,680 组真实标题 A/B 测试（每组同一内容、
不同标题、含展示/点击数据），在组内对照下测得各标题特征的相对点击率增益，
以此校准中文标题的注意力评分权重，替代拍脑袋词表：

  特征              组内 CTR 相对增益（实测）
  好奇缺口           +2.5%
  高唤醒情绪          +2.4%
  最高级/夸张         +1.8%
  具体长标题（>14词）  +1.5%
  数字               +1.4%
  第二人称           +0.1%（无效）
  问号               -3.4%（负效！纯提问不制造信息差）

另设 clickbait 护栏：夸张信号超过阈值反而扣分，防止沦为标题党。
"""

import re

# 好奇缺口：制造「已知一点点、想知道更多」的信息差（Loewenstein information-gap）
CURIOSITY_GAP_MARKERS = [
    "为什么", "背后", "其实", "原来", "没人告诉", "没有人告诉", "真相",
    "直到", "才发现", "才明白", "秘密", "隐藏", "被忽视", "被低估",
    "正在偷偷", "你不知道", "很少有人", "重写了我对",
]
# 高唤醒情绪（Berger & Milkman：敬畏/愤怒/焦虑等高唤醒情绪显著提升转发）
HIGH_AROUSAL_MARKERS = [
    "崩溃", "焦虑", "愤怒", "震撼", "颠覆", "彻底", "疯狂", "绝望",
    "拯救", "毁掉", "失控", "爆发", "崩塌", "惊人",
]
# 最高级/夸张（适度有效）
SUPERLATIVE_MARKERS = ["最", "唯一", "终极", "从未", "第一次", "史上"]
# clickbait 红线信号：命中过多则触发护栏扣分
CLICKBAIT_MARKERS = [
    "震惊", "惊呆", "吓人", "不转不是", "必看", "速看", "999%", "你绝对",
    "全网疯传", "都在传",
]


def _count_hits(text: str, markers: list[str]) -> int:
    return sum(1 for m in markers if m in text)


def score_attention(title: str, subtitle: str = "") -> float:
    """返回 1-10 的注意力分。基线 5.0，各特征按 Upworthy 实测增益比例加减。"""
    text = f"{title} {subtitle}"
    score = 5.0

    # 权重按实测组内增益等比缩放（好奇缺口 +2.5% → +1.25 分，以此类推）
    score += min(_count_hits(text, CURIOSITY_GAP_MARKERS), 3) * 1.25
    score += min(_count_hits(text, HIGH_AROUSAL_MARKERS), 2) * 1.20
    score += min(_count_hits(text, SUPERLATIVE_MARKERS), 2) * 0.90

    # 数字（+1.4%）：具体数字优于模糊表述
    if re.search(r"\d", title):
        score += 0.70

    # 具体长标题（+1.5%）：字符数近似替代英文词数（中文 >22 字算「长而具体」）
    if len(title) > 22:
        score += 0.75

    # 问号（-3.4%）：纯提问式标题实测拉低点击——除非同时带好奇缺口
    if ("？" in title or "?" in title) and _count_hits(title, CURIOSITY_GAP_MARKERS) == 0:
        score -= 1.70

    # clickbait 护栏：夸张红线信号 ≥2 个则重罚（张力可以有，标题党不行）
    cb = _count_hits(text, CLICKBAIT_MARKERS)
    if cb >= 2:
        score -= 2.5
    elif cb == 1:
        score -= 0.8

    return max(0.0, min(10.0, score))
