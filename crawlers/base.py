"""Các hàm tiện ích dùng chung cho hệ thống Crawler ngành Data trên Windows.

Bao gồm 3 kỹ thuật cốt lõi phục vụ kiểm tra mã nguồn (Code Audit):
1. Đọc/Ghi JSONL chuẩn UTF-8 tương thích Windows PowerShell (`pathlib.Path`).
2. Cơ chế chờ ngẫu nhiên (`polite_sleep` với `random.uniform`) tuân thủ đạo đức
   thu thập dữ liệu (Robots.txt etiquette) và tránh bị chặn IP (Rate-Limit).
3. Cơ chế cuộn trang vô tận (`simulate_infinite_scroll`) kích hoạt AJAX/DOM tải động.
"""

import json
import random
import time
from datetime import datetime
from pathlib import Path
from typing import Callable, Iterable

from bs4 import BeautifulSoup


def write_jsonl(path: Path | str, rows: Iterable[dict]) -> int:
    """Ghi nối tiếp (append) danh sách bản ghi vào tệp JSONL với mã hóa UTF-8."""
    out_path = Path(path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with out_path.open("a", encoding="utf-8") as fh:
        for row in rows:
            if "crawled_at" not in row:
                row["crawled_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            count += 1
    return count


def read_jsonl(path: Path | str) -> list[dict]:
    """Đọc toàn bộ bản ghi từ tệp JSONL (trả về danh sách rỗng nếu tệp chưa tồn tại)."""
    in_path = Path(path)
    if not in_path.exists():
        return []
    rows: list[dict] = []
    with in_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def polite_sleep(
    min_sec: float = 1.5,
    max_sec: float = 3.5,
    label: str = "Crawler",
) -> float:
    """Kỹ thuật 3 (Code Audit): Thời gian chờ ngẫu nhiên tuân thủ Robots.txt etiquette.

    Sử dụng phân phối đều `random.uniform(min_sec, max_sec)` để mô phỏng hành vi
    duyệt web tự nhiên của người dùng thật, không gửi request dồn dập làm quá tải
    máy chủ tuyển dụng.
    """
    delay = round(random.uniform(min_sec, max_sec), 2)
    print(f"  [{label}] ⏳ Chờ ngẫu nhiên {delay:.2f}s (Robots.txt etiquette)...", flush=True)
    time.sleep(delay)
    return delay


def simulate_infinite_scroll(
    page,
    steps: int = 3,
    scroll_pause: float = 0.7,
) -> None:
    """Kỹ thuật 2 (Code Audit): Vượt qua cơ chế tải động (Infinite Scroll / Lazy DOM).

    Cuộn trang từng bước từ trên xuống cuối trang để kích hoạt các sự kiện
    IntersectionObserver / AJAX tải đầy đủ danh sách thẻ công việc (job cards).
    """
    for step in range(1, steps + 1):
        ratio = step / steps
        try:
            page.evaluate(
                f"window.scrollTo(0, Math.floor(document.body.scrollHeight * {ratio}));"
            )
            page.wait_for_timeout(int(scroll_pause * 1000))
        except Exception:
            break


def interactive_scrape(
    page,
    parse_fn: Callable[[BeautifulSoup], list[dict]],
    out_path: Path | str,
    *,
    interval: float = 2.0,
    label: str = "crawler",
) -> dict[str, dict]:
    """Chế độ cào tương tác liên tục khi người dùng thao tác trên trình duyệt."""
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    collected: dict[str, dict] = {}
    if out.exists():
        for row in read_jsonl(out):
            if row.get("job_url"):
                collected[row["job_url"]] = row
    try:
        while True:
            try:
                soup = BeautifulSoup(page.content(), "lxml")
                for row in parse_fn(soup):
                    url = row.get("job_url")
                    if url and url not in collected:
                        row.setdefault(
                            "crawled_at",
                            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        )
                        collected[url] = row
                with out.open("w", encoding="utf-8") as fh:
                    for row in collected.values():
                        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
                print(f"[{label}] Đã thu thập {len(collected)} tin duy nhất", flush=True)
            except Exception as exc:
                print(f"[{label}] Đang chuyển trang: {str(exc)[:60]}", flush=True)
            time.sleep(interval)
    except KeyboardInterrupt:
        pass
    print(f"[{label}] Hoàn tất: {len(collected)} tin -> {out}")
    return collected
