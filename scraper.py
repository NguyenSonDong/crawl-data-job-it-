"""Script điều phối thu thập dữ liệu tuyển dụng chuyên sâu Ngành Data & AI (Windows).

Đồ án môn học: Khai Phá Dữ Liệu (ITEC3417) - Thành viên 1 (Giai đoạn 1)
Đề tài: Thu thập và Khai phá Dữ liệu Tuyển dụng Thực tế nhóm ngành Dữ liệu &
        Trí tuệ Nhân tạo (DA, DE, DS, BI, AI/ML) tại Việt Nam.

Ví dụ chạy Live Demo trực tiếp tại lớp trước giảng viên:
    python scraper.py --site itviec --keyword "Data Analyst" --pages 2
    python scraper.py --site topdev --keyword "Data Engineer" --pages 2
    python scraper.py --site vietnamworks --keyword "Data Scientist" --pages 2
    python scraper.py --site topcv --keyword "Business Intelligence" --pages 2
    python scraper.py --list-keywords
"""

import argparse
import sys
from pathlib import Path

from crawlers.itviec import crawl_itviec
from crawlers.topcv import crawl_topcv
from crawlers.topdev import crawl_topdev
from crawlers.vietnamworks import crawl_vietnamworks

# 1. Bộ từ khóa định vị tên vị trí tuyển dụng ngành Data & AI
DATA_ROLE_KEYWORDS: list[str] = [
    "Data Analyst",
    "Data Engineer",
    "Data Scientist",
    "Business Intelligence",
    "BI Analyst",
    "Analytics Engineer",
    "AI Engineer",
    "Machine Learning Engineer",
    "Database Administrator",
    "DBA",
    "Big Data",
    "Data Governance",
]

# 2. Bộ từ khóa kỹ năng cốt lõi hệ sinh thái Data & AI
DATA_SKILL_KEYWORDS: list[str] = [
    "Python",
    "SQL",
    "PowerBI",
    "Tableau",
    "Spark",
    "PyTorch",
    "ETL",
    "Data Warehouse",
]

# Tổng hợp toàn bộ từ khóa định vị mục tiêu ngành Data (DATA_KEYWORDS)
DATA_KEYWORDS: list[str] = DATA_ROLE_KEYWORDS + DATA_SKILL_KEYWORDS

SUPPORTED_SITES = ("itviec", "topcv", "vietnamworks", "topdev", "all")


def run_crawler_for_site(
    site: str,
    keyword: str,
    pages: int,
    limit: int,
    headless: bool,
    out_dir: Path,
    delay_min: float,
    delay_max: float,
) -> list[dict]:
    """Điều phối chạy Crawler tương ứng với từng nền tảng tuyển dụng."""
    site = site.lower().strip()
    out_file = out_dir / f"{site}.jsonl"

    print("=" * 78)
    print(f"🚀 KHỞI CHẠY CRAWLER NGÀNH DATA | NGUỒN: {site.upper()}")
    print(f"   • Từ khóa định vị (Keyword) : '{keyword}'")
    print(f"   • Số trang phân trang       : {pages} trang (Pagination)")
    print(f"   • Chế độ trình duyệt        : {'Headless (Ẩn)' if headless else 'Visible GUI (Live Demo)'}")
    print(f"   • Độ trễ ngẫu nhiên         : {delay_min:.1f}s - {delay_max:.1f}s (Robots.txt etiquette)")
    print(f"   • Tệp lưu trữ JSONL         : {out_file}")
    print("=" * 78, flush=True)

    if site == "itviec":
        return crawl_itviec(
            keyword=keyword,
            pages=pages,
            limit=limit,
            headless=headless,
            out_path=out_file,
            append=True,
            delay_min=delay_min,
            delay_max=delay_max,
        )
    if site == "topcv":
        return crawl_topcv(
            keyword=keyword,
            pages=pages,
            limit=limit,
            headless=headless,
            out_path=out_file,
            append=True,
            delay_min=delay_min,
            delay_max=delay_max,
        )
    if site == "vietnamworks":
        return crawl_vietnamworks(
            keyword=keyword,
            pages=pages,
            limit=limit,
            out_path=out_file,
            append=True,
            delay_min=delay_min,
            delay_max=delay_max,
        )
    if site == "topdev":
        return crawl_topdev(
            keyword=keyword,
            pages=pages,
            limit=limit,
            headless=headless,
            out_path=out_file,
            append=True,
            delay_min=delay_min,
            delay_max=delay_max,
        )
    raise ValueError(f"Nguồn '{site}' không nằm trong danh sách hỗ trợ: {SUPPORTED_SITES}")


def print_keywords_catalog() -> None:
    """Hiển thị danh mục bộ từ khóa định vị ngành Data (`DATA_KEYWORDS`)."""
    print("=" * 78)
    print("📋 BỘ TỪ KHÓA ĐỊNH VỊ MỤC TIÊU NGÀNH DATA & AI (DATA_KEYWORDS)")
    print("=" * 78)
    print(f"\n1. Nhóm Tên Vị Trí Chuyên Môn ({len(DATA_ROLE_KEYWORDS)} từ khóa):")
    for idx, kw in enumerate(DATA_ROLE_KEYWORDS, 1):
        print(f"   {idx:02d}. {kw}")
    print(f"\n2. Nhóm Kỹ Năng Cốt Lõi ({len(DATA_SKILL_KEYWORDS)} từ khóa):")
    for idx, kw in enumerate(DATA_SKILL_KEYWORDS, 1):
        print(f"   {idx:02d}. {kw}")
    print(f"\n=> Tổng cộng: {len(DATA_KEYWORDS)} từ khóa định vị chuẩn Giai đoạn 1.")
    print("=" * 78)


def main() -> None:
    # Đảm bảo hiển thị tiếng Việt UTF-8 trên Windows PowerShell
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Bộ công cụ thu thập dữ liệu tuyển dụng Ngành Data & AI trên Windows (Live Demo & Batch)"
    )
    parser.add_argument(
        "--site",
        type=str,
        default="itviec",
        choices=SUPPORTED_SITES,
        help="Nền tảng cần cào: itviec, topcv, vietnamworks, topdev hoặc all (mặc định: itviec)",
    )
    parser.add_argument(
        "--keyword",
        type=str,
        default="Data Analyst",
        help="Từ khóa ngành Data cần tìm kiếm (mặc định: 'Data Analyst')",
    )
    parser.add_argument(
        "--pages",
        type=int,
        default=2,
        help="Số trang phân trang cần duyệt cho mỗi lần chạy (mặc định: 2)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Giới hạn số lượng tin tối đa (0 = không giới hạn)",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Chạy ẩn trình duyệt (Mặc định tắt để bật cửa sổ Chrome phục vụ Live Demo tại lớp)",
    )
    parser.add_argument(
        "--out-dir",
        type=str,
        default="data/raw",
        help="Thư mục lưu trữ các tệp JSONL thô (mặc định: data/raw)",
    )
    parser.add_argument(
        "--delay-min",
        type=float,
        default=1.5,
        help="Thời gian chờ tối thiểu giữa các trang (giây)",
    )
    parser.add_argument(
        "--delay-max",
        type=float,
        default=3.5,
        help="Thời gian chờ tối đa giữa các trang (giây)",
    )
    parser.add_argument(
        "--list-keywords",
        action="store_true",
        help="In danh sách bộ từ khóa DATA_KEYWORDS và thoát",
    )
    args = parser.parse_args()

    if args.list_keywords:
        print_keywords_catalog()
        return

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    sites_to_run = (
        ["itviec", "topcv", "vietnamworks", "topdev"]
        if args.site == "all"
        else [args.site]
    )

    total_collected: list[dict] = []
    for s in sites_to_run:
        rows = run_crawler_for_site(
            site=s,
            keyword=args.keyword,
            pages=args.pages,
            limit=args.limit,
            headless=args.headless,
            out_dir=out_dir,
            delay_min=args.delay_min,
            delay_max=args.delay_max,
        )
        total_collected.extend(rows)

    print("\n" + "=" * 78)
    print(f"🎉 HOÀN TẤT PHIÊN CÀO DỮ LIỆU! Đã thu thập mới: {len(total_collected)} tin tuyển dụng.")
    if total_collected:
        print("📌 3 bản ghi mẫu vừa thu thập được:")
        for idx, sample in enumerate(total_collected[:3], 1):
            print(
                f"   [{idx}] {sample.get('title')} | {sample.get('company')} "
                f"| {sample.get('location')} | URL: {sample.get('job_url')}"
            )
    print("💡 Bước tiếp theo: Chạy `python step_01_export_raw_csv.py` để trích lọc và xuất data/raw_data.csv")
    print("=" * 78)


if __name__ == "__main__":
    main()
