"""ADHD×AI 情报自动流 - 数据收集器"""
from collectors.arxiv import ArxivCollector
from collectors.reddit import RedditCollector

__all__ = ['ArxivCollector', 'RedditCollector', 'BaseCollector']
