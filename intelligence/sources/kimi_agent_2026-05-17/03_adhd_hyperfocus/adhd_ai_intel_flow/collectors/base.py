"""
ADHD×AI 情报自动流 - 收集器基类
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import hashlib

@dataclass
class RawItem:
    """原始数据项"""
    id: str                          # 唯一ID
    source: str                      # 来源 (arxiv/reddit/news/...)
    source_name: str                 # 来源名称
    title: str                       # 标题
    content: str                     # 内容/摘要
    url: str                         # 链接
    author: Optional[str] = None     # 作者
    published_at: Optional[datetime] = None  # 发布时间
    raw_data: dict = field(default_factory=dict)  # 原始数据
    tags: List[str] = field(default_factory=list)  # 标签
    score: int = 0                   # 热度分数

    def __post_init__(self):
        if not self.id:
            self.id = hashlib.md5(f"{self.source}:{self.url}".encode()).hexdigest()[:12]

class BaseCollector(ABC):
    """收集器基类"""

    def __init__(self, config: dict):
        self.config = config
        self.enabled = config.get('enabled', True)

    @abstractmethod
    def collect(self) -> List[RawItem]:
        """执行数据收集，返回原始数据列表"""
        pass

    @property
    @abstractmethod
    def source_name(self) -> str:
        """返回来源名称"""
        pass
