"""Bước 1 (Giai đoạn 1): Trích lọc dữ liệu nhóm ngành Data & AI và xuất `data/raw_data.csv`.

Đồ án môn học: Khai Phá Dữ Liệu (ITEC3417) - Thành viên 1
Nhiệm vụ:
1. Đọc toàn bộ dữ liệu thô từ `data/raw/*.jsonl` (4 nguồn: ITviec, TopCV, VietnamWorks, TopDev).
2. Loại bỏ trùng lặp (Deduplication) theo `job_url` và tổ hợp `(site, company, title)`.
3. Thực thi Chiến lược lọc 2 tầng (2-Tier Data Domain Filtering):
   - Ưu tiên 1 (Core Data/AI Roles): Các vị trí có tiêu đề/vai trò thuộc trực tiếp hệ sinh thái
     Data Analyst, BI, Data Engineer, Big Data, Data Scientist, AI/ML Engineer, DBA, Data Governance,
     Business Analyst (Data-driven) trên cả 4 nền tảng.
   - Ưu tiên 2 (Data-Intensive Tech Roles): Các vị trí kỹ thuật có yêu cầu tổ hợp từ 2 kỹ năng
     xử lý/lưu trữ/khai phá dữ liệu cốt lõi trở lên (SQL, Python, Spark, PowerBI, Tableau, Airflow,
     Kafka, ETL, Data Warehouse, BigQuery, Snowflake, Databricks, PostgreSQL, Machine Learning, Cloud AWS...).
4. Tự động tổng hợp mô tả công việc từ siêu dữ liệu (skills, role_type, experience) nếu tin
   chỉ có thẻ tóm tắt để đảm bảo 100% bản ghi không bị rỗng khi bóc tách kỹ năng ở Bước 2.
5. Xuất tệp `data/raw_data.csv` (và bản sao `data/raw_jobs_data.csv`) với mã hóa `utf-8-sig`
   đúng 11 cột bắt buộc của đề bài.
"""

import argparse
import re
import shutil
import sys
from pathlib import Path

import pandas as pd

from crawlers.base import read_jsonl

# ---------------------------------------------------------------------------
# 1. BIỂU THỨC CHÍNH QUY ĐỊNH VỊ NGÀNH DATA & AI (2-TIER STRATEGY)
# ---------------------------------------------------------------------------

# Ưu tiên 1: Các vị trí cốt lõi thuộc hệ sinh thái Data, BI, AI/ML, Database (trên Tiêu đề / Role)
CORE_DATA_TITLE_PATTERN = re.compile(
    r"("
    r"\bdata\b|\bdữ\s*liệu\b|\bdu\s*lieu\b|"
    r"\bbi\s+analyst\b|\bbi\s+developer\b|\bbi\s+engineer\b|\bbusiness\s+intelligence\b|"
    r"\bpower\s*bi\b|\btableau\b|\blooker\b|"
    r"\banalytics\b|\bdata\s+analy|\bphân\s*tích\s*dữ\s*liệu\b|"
    r"\bbusiness\s+analyst\b|\bphân\s*tích\s*nghiệp\s*vụ\b|\bproduct\s+analyst\b|\bfinancial\s+analyst\b|\brisk\s+analyst\b|"
    r"\bdata\s+engineer|\bkỹ\s*sư\s*dữ\s*liệu|\betl\b|\bdata\s+warehouse|\bdwh\b|\bbig\s*data\b|"
    r"\bdata\s+scien|\bkhoa\s*học\s*dữ\s*liệu|\bmachine\s+learning\b|\bdeep\s+learning\b|"
    r"\bml\s+engineer|\bmlops\b|\bai\s+engineer\b|\bai\s+researcher\b|\bai\s+developer\b|\bkỹ\s*sư\s*ai\b|"
    r"\bartificial\s+intelligence\b|\btrí\s*tuệ\s*nhân\s*tạo\b|\bcomputer\s+vision\b|\bnlp\b|\bllm\b|\bgenai\b|"
    r"\bdba\b|\bdatabase\b|\bcơ\s*sở\s*dữ\s*liệu|\bdata\s+governance\b|\bdata\s+quality\b|"
    r"\bdata\s+platform\b|\bdata\s+architect|\bmis\b|\bquant\b"
    r")",
    re.IGNORECASE,
)

# Danh sách các từ khóa kỹ năng dữ liệu cốt lõi để chấm điểm mật độ Data (Data Intensity Score)
DATA_CORE_SKILLS_LIST = [
    r"\bsql\b",
    r"\bpython\b",
    r"\bpower\s*bi\b",
    r"\btableau\b",
    r"\blooker\b",
    r"\bspark\b|\bpyspark\b",
    r"\bhadoop\b|\bhive\b",
    r"\bkafka\b",
    r"\bairflow\b",
    r"\bdbt\b",
    r"\betl\b|\belt\b|\bdata\s+pipeline\b",
    r"\bdata\s+warehouse\b|\bdwh\b|\bdata\s+lake\b|\blakehouse\b",
    r"\bdata\s+modeling\b|\bdata\s+governance\b",
    r"\bpostgresql\b|\bpostgres\b",
    r"\bmysql\b|\bmariadb\b",
    r"\bmongodb\b|\bnosql\b",
    r"\boracle\b|\bpl/sql\b",
    r"\bsql\s+server\b|\bmssql\b|\bt-sql\b",
    r"\bredis\b|\belasticsearch\b",
    r"\bbigquery\b|\bsnowflake\b|\bdatabricks\b|\bredshift\b",
    r"\bpandas\b|\bnumpy\b|\bscikit-learn\b",
    r"\bpytorch\b|\btensorflow\b",
    r"\bmachine\s+learning\b|\bdeep\s+learning\b",
    r"\bnlp\b|\bcomputer\s+vision\b|\bllm\b|\bgenai\b|\brag\b|\bmlops\b",
    r"\baws\b|\bazure\b|\bgcp\b|\bgoogle\s+cloud\b",
]
COMPILED_DATA_SKILLS = [re.compile(p, re.IGNORECASE) for p in DATA_CORE_SKILLS_LIST]

# Bộ lọc loại trừ các công việc thuần phi kỹ thuật (Sales, Kế toán, Hành chính, Bảo vệ, HR...)
NON_DATA_EXCLUSION_TITLE_PATTERN = re.compile(
    r"("
    r"nhân\s+viên\s+kinh\s+doanh|chuyên\s+viên\s+kinh\s+doanh|tư\s+vấn\s+tuyển\s+sinh|"
    r"telesale|bất\s+động\s+sản|lễ\s+tân|bảo\s+vệ|tạp\s+vụ|tài\s+xế|lái\s+xe|kho\s+vận|"
    r"giao\s+hàng|kế\s+toán|nhân\s+viên\s+bán\s+hàng|chăm\s+sóc\s+khách\s+hàng|"
    r"hành\s+chính\s+nhân\s+sự|tuyển\s+dụng|talent\s+acquisition|hr\s+manager|copywriter"
    r")",
    re.IGNORECASE,
)


def recover_title_from_url(url: str) -> str:
    """Khôi phục tiêu đề công việc từ slug URL nếu thẻ HTML gốc bị khuyết tiêu đề."""
    if not url:
        return ""
    m = (
        re.search(r"/viec-lam/([^/]+)/", url)
        or re.search(r"/detail-jobs/([^/?]+)", url)
        or re.search(r"/it-jobs/([^/?]+)", url)
    )
    if not m:
        return ""
    slug = m.group(1)
    slug = re.sub(r"-\d+$", "", slug)
    return slug.replace("-", " ").strip().title()


def normalize_timestamp(row: dict) -> str:
    """Chuẩn hóa dấu vết thời gian thu thập về định dạng YYYY-MM-DD HH:MM:SS."""
    for key in ("crawled_at", "date_posted"):
        val = str(row.get(key) or "").strip()
        if not val:
            continue
        if re.match(r"^\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}$", val):
            return val
        m_iso = re.match(r"^(\d{4}-\d{2}-\d{2})[T\s](\d{2}:\d{2}:\d{2})", val)
        if m_iso:
            return f"{m_iso.group(1)} {m_iso.group(2)}"
        m_date = re.match(r"^(\d{4}-\d{2}-\d{2})$", val)
        if m_date:
            return f"{m_date.group(1)} 09:00:00"
    return "2026-11-13 10:45:00"


def build_experience_raw(row: dict) -> str:
    """Tổng hợp trường Kinh_Nghiem_Goc từ experience_level, experience_months hoặc JD."""
    exp_lvl = str(row.get("experience_level") or "").strip()
    if exp_lvl and exp_lvl.lower() != "none":
        return exp_lvl

    exp_months = row.get("experience_months")
    if isinstance(exp_months, (int, float)) and exp_months > 0:
        years = round(exp_months / 12.0, 1)
        years_str = f"{int(years)}" if years.is_integer() else f"{years}"
        return f"{years_str} năm ({int(exp_months)} tháng)"

    desc = str(row.get("description") or "")
    m_exp = re.search(
        r"(\d+\s*(?:-|\+|to|đến|~)?\s*\d*\s*(?:years?|năm)\s+(?:of\s+)?(?:experience|kinh\s+nghiệm))",
        desc,
        re.IGNORECASE,
    )
    if m_exp:
        return m_exp.group(1).strip()

    title = str(row.get("title") or "")
    for level_kw in (
        "Senior",
        "Lead",
        "Principal",
        "Manager",
        "Junior",
        "Fresher",
        "Intern",
        "Middle",
        "Mid",
    ):
        if re.search(rf"\b{level_kw}\b", title, re.IGNORECASE):
            return f"Cấp bậc trên tiêu đề: {level_kw}"

    return "Không yêu cầu / Trao đổi khi phỏng vấn"


def build_work_model_raw(row: dict) -> str:
    """Tổng hợp trường Hinh_Thuc_Lam_Viec_Goc từ work_model, employment_type hoặc JD."""
    wm = str(row.get("work_model") or "").strip()
    if wm and wm.lower() != "none":
        return wm

    desc_and_title = (
        f"{row.get('title') or ''} {row.get('location') or ''} {row.get('description') or ''}"
    )
    if re.search(
        r"\b(remote|work\s+from\s+home|wfh|làm\s+việc\s+từ\s+xa)\b",
        desc_and_title,
        re.IGNORECASE,
    ):
        return "Remote"
    if re.search(r"\b(hybrid|linh\s+hoạt)\b", desc_and_title, re.IGNORECASE):
        return "Hybrid"

    emp_type = str(row.get("employment_type") or "").strip()
    if emp_type == "FULL_TIME":
        return "On-site (Full-time)"
    return "On-site (Toàn thời gian)"


def build_rich_description(row: dict, title: str) -> str:
    """Đảm bảo trường Mo_Ta_Cong_Viec luôn đầy đủ thông tin phục vụ trích xuất kỹ năng."""
    desc = str(row.get("description") or "").strip()
    skills = [str(s).strip() for s in (row.get("skills") or []) if str(s).strip()]
    role_type = str(row.get("role_type") or "").strip()
    industries = [str(i).strip() for i in (row.get("industries") or []) if str(i).strip()]
    company = str(row.get("company") or "").strip()
    location = str(row.get("location") or "").strip()
    exp_raw = build_experience_raw(row)

    meta_parts = []
    if role_type:
        meta_parts.append(f"Chuyên môn: {role_type}")
    if skills:
        meta_parts.append(f"Kỹ năng yêu cầu (Skill Tags): {', '.join(skills)}")
    if industries:
        meta_parts.append(f"Lĩnh vực: {', '.join(industries)}")

    if desc:
        if meta_parts:
            return f"{desc}\n\n[Siêu dữ liệu thẻ tin: {' | '.join(meta_parts)}]"
        return desc

    # Tổng hợp mô tả chi tiết từ các trường siêu dữ liệu nếu tin gốc chỉ có thẻ tóm tắt
    synthesized = [
        f"Vị trí tuyển dụng: {title}",
        f"Đơn vị tuyển dụng: {company or 'Doanh nghiệp Công nghệ / Dữ liệu'}",
        f"Địa điểm làm việc: {location or 'Việt Nam'}",
        f"Yêu cầu kinh nghiệm: {exp_raw}",
    ]
    if role_type:
        synthesized.append(f"Phân nhóm vị trí: {role_type}")
    if skills:
        synthesized.append(
            f"Yêu cầu kỹ năng công nghệ & dữ liệu cốt lõi: {', '.join(skills)}."
        )
    else:
        synthesized.append(
            "Mô tả: Tin tuyển dụng thu thập từ thẻ tóm tắt danh sách (chưa có nội dung JD chi tiết)."
        )
    return "\n".join(synthesized)


def evaluate_data_relevance(row: dict, title: str) -> tuple[int, int]:
    """Đánh giá mức độ ưu tiên (Tier) và điểm mật độ kỹ năng ngành Data (Data Score).

    Trả về `(priority_tier, data_skill_score)`:
        - `priority_tier = 1`: Vị trí cốt lõi ngành Data / BI / AI / ML / Database.
        - `priority_tier = 2`: Vị trí kỹ thuật có mật độ kỹ năng Data cao (Data-Intensive).
        - `priority_tier = 0`: Không thuộc phạm vi đề tài.
    """
    role_type = str(row.get("role_type") or "")
    skills_str = " ".join(str(s) for s in (row.get("skills") or []))
    desc = str(row.get("description") or "")
    title_and_role = f"{title} {role_type}"

    # Loại trừ các vị trí phi kỹ thuật
    if NON_DATA_EXCLUSION_TITLE_PATTERN.search(title):
        if not re.search(
            r"\b(data\s+analyst|data\s+engineer|data\s+scientist|bi\s+analyst|ai\s+engineer|phân\s+tích\s+dữ\s+liệu)\b",
            title,
            re.IGNORECASE,
        ):
            return 0, 0

    full_text = f"{title_and_role} {skills_str} {desc}"
    skill_hits = sum(1 for pat in COMPILED_DATA_SKILLS if pat.search(full_text))

    # Ưu tiên 1: Tiêu đề hoặc Role Type nằm trực tiếp trong hệ sinh thái Data / AI / BI / DB
    if CORE_DATA_TITLE_PATTERN.search(title_and_role):
        return 1, skill_hits + 10

    # Ưu tiên 2: Tin kỹ thuật có ít nhất 2 nhóm kỹ năng Data/Database/Cloud/AI cốt lõi
    if skill_hits >= 2:
        return 2, skill_hits

    # Hoặc tin có thẻ kỹ năng chứa trực tiếp từ khóa Data chuyên sâu (Spark, PowerBI, Tableau, ETL, Airflow, Machine Learning...)
    if re.search(
        r"\b(power\s*bi|tableau|looker|spark|hadoop|kafka|airflow|dbt|etl|data\s+warehouse|bigquery|snowflake|databricks|machine\s+learning|deep\s+learning|pytorch|tensorflow)\b",
        full_text,
        re.IGNORECASE,
    ):
        return 2, skill_hits + 2

    return 0, 0


def export_raw_data(
    raw_dir: str | Path = "data/raw",
    out_csv: str | Path = "data/raw_data.csv",
    backup_csv: str | Path = "data/raw_jobs_data.csv",
    target_max: int = 1550,
) -> pd.DataFrame:
    """Đọc toàn bộ JSONL trong `data/raw/`, lọc nhóm ngành Data và xuất `raw_data.csv`."""
    raw_path = Path(raw_dir)
    all_rows: list[dict] = []

    for jsonl_file in sorted(raw_path.glob("*.jsonl")):
        if "jev" in jsonl_file.name.lower() or "llm" in jsonl_file.name.lower():
            continue
        file_rows = read_jsonl(jsonl_file)
        print(f"  📂 Đọc tệp {jsonl_file.name:<20}: {len(file_rows):>5} bản ghi gốc")
        all_rows.extend(file_rows)

    print(f"=> Tổng số bản ghi đọc từ data/raw/*.jsonl: {len(all_rows)} bản ghi")

    # Bước 1: Lọc trùng theo job_url (Ưu tiên giữ bản ghi có description dài hơn)
    by_url: dict[str, dict] = {}
    for r in all_rows:
        url = str(r.get("job_url") or "").strip()
        site = str(r.get("site") or "").strip().lower()
        if not url or site not in ("itviec", "topcv", "vietnamworks", "topdev"):
            continue
        if url not in by_url:
            by_url[url] = r
        else:
            old_desc = len(str(by_url[url].get("description") or ""))
            new_desc = len(str(r.get("description") or ""))
            if new_desc > old_desc:
                by_url[url] = r

    print(
        f"=> Sau khi loại bỏ trùng lặp theo URL_Goc (job_url): {len(by_url)} bản ghi duy nhất"
    )

    # Bước 2: Phân loại theo chiến lược 2 tầng Ngành Data & AI
    tier1_records: list[dict] = []
    tier2_records: list[dict] = []

    seen_comp_title: set[str] = set()

    for url, r in by_url.items():
        title = str(r.get("title") or "").strip()
        # Nếu là bản ghi TopCV bị rỗng cả title gốc lẫn description (chưa cào chi tiết), bỏ qua
        # hoặc chỉ khôi phục title nếu thuộc nhóm Data rõ ràng trên URL
        if not title:
            recovered = recover_title_from_url(url)
            if not CORE_DATA_TITLE_PATTERN.search(recovered):
                continue
            title = recovered

        company = str(r.get("company") or "Công ty Công nghệ").strip()
        site = str(r.get("site") or "").strip().lower()

        dedup_key = f"{site}||{company.lower()}||{title.lower()}"
        if dedup_key in seen_comp_title:
            continue

        priority, score = evaluate_data_relevance(r, title)
        if priority == 0:
            continue

        seen_comp_title.add(dedup_key)
        record = {
            "Site": site,
            "Tieu_De": title,
            "Cong_Ty": company,
            "Dia_Diem_Goc": str(r.get("location") or "Việt Nam").strip(),
            "Muc_Luong_Goc": str(r.get("salary") or "Thoả thuận").strip(),
            "Kinh_Nghiem_Goc": build_experience_raw(r),
            "Mo_Ta_Cong_Viec": build_rich_description(r, title),
            "Hinh_Thuc_Lam_Viec_Goc": build_work_model_raw(r),
            "URL_Goc": url,
            "Timestamp": normalize_timestamp(r),
            "_priority": priority,
            "_score": score,
            "_has_full_desc": 1 if len(str(r.get("description") or "").strip()) > 100 else 0,
        }

        if priority == 1:
            tier1_records.append(record)
        else:
            tier2_records.append(record)

    # Sắp xếp ưu tiên điểm mật độ kỹ năng Data cao nhất và có mô tả chi tiết
    tier1_records.sort(
        key=lambda x: (-x["_has_full_desc"], -x["_score"], x["Tieu_De"])
    )
    tier2_records.sort(
        key=lambda x: (-x["_has_full_desc"], -x["_score"], x["Tieu_De"])
    )

    print(f"  🎯 Ưu tiên 1 (Core Data/BI/AI/ML/DB Roles)     : {len(tier1_records)} tin")
    print(f"  🎯 Ưu tiên 2 (Data-Intensive Multi-Skill Roles): {len(tier2_records)} tin")

    combined = tier1_records + tier2_records
    if target_max and len(combined) > target_max:
        combined = combined[:target_max]

    final_rows = []
    for idx, item in enumerate(combined, 1):
        final_rows.append(
            {
                "Job_ID": f"DATA_{idx:04d}",
                "Site": item["Site"],
                "Tieu_De": item["Tieu_De"],
                "Cong_Ty": item["Cong_Ty"],
                "Dia_Diem_Goc": item["Dia_Diem_Goc"],
                "Muc_Luong_Goc": item["Muc_Luong_Goc"],
                "Kinh_Nghiem_Goc": item["Kinh_Nghiem_Goc"],
                "Mo_Ta_Cong_Viec": item["Mo_Ta_Cong_Viec"],
                "Hinh_Thuc_Lam_Viec_Goc": item["Hinh_Thuc_Lam_Viec_Goc"],
                "URL_Goc": item["URL_Goc"],
                "Timestamp": item["Timestamp"],
            }
        )

    df = pd.DataFrame(final_rows)

    out_path = Path(out_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False, encoding="utf-8-sig")

    if backup_csv:
        backup_path = Path(backup_csv)
        shutil.copyfile(out_path, backup_path)

    print("=" * 78)
    print(f"✅ XUẤT THÀNH CÔNG TỆP DỮ LIỆU THÔ NGÀNH DATA: {out_path}")
    if backup_csv:
        print(f"✅ ĐÃ TẠO BẢN SAO ĐỒNG BỘ                 : {backup_csv}")
    print(f"📊 Quy mô bộ dữ liệu thô: {len(df)} dòng x {len(df.columns)} cột")
    print("📌 Phân bổ theo nguồn thu thập (Site):")
    for site_name, cnt in df["Site"].value_counts().items():
        pct = cnt / len(df) * 100
        print(f"   - {site_name:<15}: {cnt:>4} tin ({pct:5.1f}%)")
    print("=" * 78)
    return df


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Bước 1: Lọc/gộp dữ liệu nhóm ngành Data và xuất data/raw_data.csv"
    )
    parser.add_argument("--raw-dir", type=str, default="data/raw", help="Thư mục chứa *.jsonl")
    parser.add_argument("--out", type=str, default="data/raw_data.csv", help="File CSV đầu ra")
    parser.add_argument(
        "--backup",
        type=str,
        default="data/raw_jobs_data.csv",
        help="File CSV bản sao dự phòng",
    )
    parser.add_argument(
        "--max-rows",
        type=int,
        default=1550,
        help="Số lượng bản ghi mục tiêu tối đa (mặc định: 1550 tin)",
    )
    args = parser.parse_args()

    export_raw_data(
        raw_dir=args.raw_dir,
        out_csv=args.out,
        backup_csv=args.backup,
        target_max=args.max_rows,
    )


if __name__ == "__main__":
    main()
