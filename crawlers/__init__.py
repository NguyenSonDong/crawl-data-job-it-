"""Gói công cụ thu thập dữ liệu tuyển dụng ngành Data & AI tại Việt Nam (Windows).

Hỗ trợ 4 nền tảng tuyển dụng IT/Data lớn nhất tại Việt Nam:
- ITviec (crawlers.itviec)
- TopCV (crawlers.topcv)
- VietnamWorks (crawlers.vietnamworks)
- TopDev (crawlers.topdev)
"""

from crawlers.base import (
    interactive_scrape,
    polite_sleep,
    read_jsonl,
    simulate_infinite_scroll,
    write_jsonl,
)
from crawlers.browser import USER_AGENT, browser

__all__ = [
    "USER_AGENT",
    "browser",
    "interactive_scrape",
    "polite_sleep",
    "read_jsonl",
    "simulate_infinite_scroll",
    "write_jsonl",
]
