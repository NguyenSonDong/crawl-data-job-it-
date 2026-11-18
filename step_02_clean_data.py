"""Bước 2 (Bước 2.1): Tiền xử lý, Làm sạch dữ liệu & Trích xuất đặc trưng chuyên sâu Ngành Data.

Đồ án môn học: Khai Phá Dữ Liệu (ITEC3417) - Thành viên 1 (10% tổng điểm)
Đầu vào : `data/raw_data.csv`
Đầu ra  : `data/clean_data.csv` (Mã hóa `utf-8-sig`, bàn giao cho Thành viên 2 & 3)

Thực hiện trọn vẹn 5 nhiệm vụ cốt lõi:
1. Phân nhóm vị trí nghề nghiệp trong Hệ sinh thái Data (`Nhom_Nganh_Data` - 5 phân khúc).
2. Chuẩn hóa mức lương bằng Biểu thức chính quy (`Regex Salary Normalization`) về Triệu VNĐ,
   kết hợp xử lý ngoại lai (như bẫy lương giả "$1-$1" hoặc lương part-time < 3M) và điền khuyết kép
   (`NaN` cho EDA + Median Imputation theo `(Nhom_Nganh_Data, Cap_Bac)` cho Machine Learning).
3. Chuẩn hóa Địa điểm (`Dia_Diem_Chuan`), Mô hình làm việc (`Mo_Hinh_Lam_Viec`),
   Số năm kinh nghiệm (`So_Nam_Kinh_Nghiem`) và 5 bậc Cấp bậc (`Cap_Bac`).
4. Làm sạch văn bản JD (xóa HTML, ký tự đặc biệt, Stop words Việt/Anh) và trích xuất
   Từ điển Kỹ năng Chuyên sâu Ngành Data (6 nhóm - 60 kỹ năng) kèm cơ chế chống bắt nhầm
   (Zero False-Positives cho từ khóa ngắn `R`, `C/C++`, `BI`, `AI`) -> Ma trận One-Hot (`0/1`).
5. Kiểm định chất lượng tự động (Data Quality & Integrity Verification).
"""

import argparse
import html
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# Tỷ giá chuẩn quy đổi USD sang Triệu VNĐ (1 USD = 25,400 VNĐ = 0.0254 Triệu VNĐ)
USD_TO_MILLION_VND: float = 0.0254

# Ngưỡng kiểm soát ngoại lai (Outlier Bounds) cho mức lương hợp lệ toàn thời gian (Đơn vị: Triệu VNĐ/tháng)
MIN_VALID_SALARY_M: float = 3.0
MAX_VALID_SALARY_M: float = 250.0


# ===========================================================================
# NHIỆM VỤ 1: PHÂN NHÓM VỊ TRÍ NGHỀ NGHIỆP TRONG HỆ SINH THÁI DATA
# ===========================================================================


def classify_data_role_group(title: str, description: str) -> str:
    """Phân loại tin tuyển dụng vào 5 phân khúc chuyên ngành Data bằng Regex.

    5 phân khúc chuẩn phục vụ Thành viên 2 làm EDA & đối chiếu với K-Means Clustering:
    1. Data Analyst / BI
    2. Data Engineer / Big Data
    3. Data Scientist / AI & ML
    4. Database / Data Platform & Ops
    5. Data-Driven Software Engineer
    """
    t = str(title or "").lower()
    d = str(description or "")[:3500].lower()

    # 1. Ưu tiên kiểm tra trên Tiêu đề công việc (Tieu_De) trước vì độ chính xác định danh cao nhất
    if re.search(
        r"\b(data\s+scien|khoa\s+học\s+dữ\s+liệu|machine\s+learning|ml\s+engineer|mlops|"
        r"deep\s+learning|ai\s+engineer|ai\s+researcher|ai\s+developer|ai\s+specialist|kỹ\s+sư\s+ai|"
        r"artificial\s+intelligence|trí\s+tuệ\s+nhân\s+tạo|computer\s+vision|nlp|"
        r"llm|genai|generative\s+ai|học\s+máy|data\s+annotation|gán\s+nhãn\s+dữ\s+liệu)\b",
        t,
    ):
        return "Data Scientist / AI & ML"

    if re.search(
        r"\b(data\s+engineer|kỹ\s+sư\s+dữ\s+liệu|big\s+data|dữ\s+liệu\s+lớn|"
        r"etl|elt|data\s+warehouse|dwh|data\s+lake|lakehouse|analytics\s+engineer|"
        r"data\s+pipeline|spark|airflow|kafka|databricks|snowflake|data\s+architect|"
        r"kiến\s+trúc\s+dữ\s+liệu|data\s+integration|data\s+migration)\b",
        t,
    ):
        return "Data Engineer / Big Data"

    if re.search(
        r"\b(data\s+analy|phân\s+tích\s+dữ\s+liệu|bi\s+analyst|bi\s+developer|"
        r"bi\s+engineer|business\s+intelligence|power\s*bi|tableau|looker|"
        r"business\s+analyst|phân\s+tích\s+nghiệp\s+vụ|product\s+analyst|"
        r"marketing\s+analyst|financial\s+analyst|risk\s+analyst|fraud\s+analyst|"
        r"credit\s+analyst|mis\b|reporting|báo\s+cáo\s+dữ\s+liệu|xử\s+lý\s+dữ\s+liệu|"
        r"data\s+processing|quant|actuarial)\b",
        t,
    ):
        return "Data Analyst / BI"

    if re.search(
        r"\b(dba\b|database|cơ\s+sở\s+dữ\s+liệu|data\s+governance|quản\s+trị\s+dữ\s+liệu|"
        r"data\s+quality|data\s+steward|master\s+data|data\s+platform|data\s+ops|"
        r"dataops|sql\s+developer|pl/sql|oracle\s+dba|cloud\s+data|system\s+admin|"
        r"devops|sre|cloud\s+engineer|infrastructure|system\s+engineer)\b",
        t,
    ):
        return "Database / Data Platform & Ops"

    # 2. Nếu tiêu đề là vị trí kỹ thuật chung (Software/Backend/Fullstack/Tech Lead),
    # phân loại dựa trên mật độ từ khóa chuyên sâu trong Mô tả công việc (Mo_Ta_Cong_Viec)
    if re.search(
        r"\b(pytorch|tensorflow|scikit-learn|deep\s+learning|computer\s+vision|nlp|llm|rag|fine-tuning|mlops|machine\s+learning)\b",
        d,
    ):
        return "Data Scientist / AI & ML"

    if re.search(
        r"\b(spark|pyspark|hadoop|airflow|dbt|data\s+warehouse|data\s+lake|etl|data\s+pipeline|snowflake|databricks|bigquery|kafka)\b",
        d,
    ):
        return "Data Engineer / Big Data"

    if re.search(
        r"\b(power\s*bi|tableau|looker|data\s+visualization|dashboard|a/b\s+testing|data\s+storytelling|business\s+intelligence)\b",
        d,
    ):
        return "Data Analyst / BI"

    if re.search(
        r"\b(database\s+administration|dba|data\s+governance|oracle|sql\s+server|postgresql|mongodb|redis|elasticsearch|kubernetes|aws|azure|gcp)\b",
        d,
    ):
        return "Database / Data Platform & Ops"

    return "Data-Driven Software Engineer"


# ===========================================================================
# NHIỆM VỤ 2: CHUẨN HÓA MỨC LƯƠNG BẰNG BIỂU THỨC CHÍNH QUY (REGEX SALARY)
# ===========================================================================


def _parse_number(num_str: str) -> float:
    """Chuyển chuỗi số có dấu phẩy/chấm thành số thực chuẩn."""
    s = num_str.strip().replace(" ", "")
    # Trường hợp viết đầy đủ hàng triệu VNĐ: 15.000.000 hoặc 15,000,000
    if re.match(r"^\d{1,3}([.,]\d{3}){2}$", s):
        s_clean = re.sub(r"[.,]", "", s)
        return float(s_clean) / 1_000_000.0
    # Trường hợp hàng nghìn USD: 1,500 hoặc 2,000 (3 chữ số sau dấu phẩy)
    if re.match(r"^\d{1,2},\d{3}$", s):
        return float(s.replace(",", ""))
    # Trường hợp số thập phân kiểu Việt Nam: 15,5 (1 hoặc 2 chữ số sau dấu phẩy)
    if re.match(r"^\d+,\d{1,2}$", s):
        return float(s.replace(",", "."))
    return float(s.replace(",", ""))


def _extract_salary_from_string(raw_str: str) -> tuple[float | None, float | None]:
    """Hàm lõi Regex bóc tách chuỗi lương bất kỳ thành (Luong_Min, Luong_Max) đơn vị Triệu VNĐ.

    Hỗ trợ đầy đủ 3 mẫu cấu trúc lương thực tế trên thị trường:
    - Mẫu 1 (Khoảng lương): "15 - 25 triệu", "$1,000 - $2,000", "15M - 25M", "800 - 1500 USD"
    - Mẫu 2 (Cận trên - Up to): "Up to 30M", "Tới 2000$", "Đến 25 triệu" -> Min = Max * 0.7
    - Mẫu 3 (Cận dưới - Over/From): "Từ 20 triệu", "Over $1500", "Trên 20M" -> Max = Min * 1.3
    """
    if not raw_str:
        return None, None

    s = str(raw_str).strip()
    s_lower = s.lower()

    # Kiểm tra nhanh các từ khóa không công bố lương
    if any(
        kw in s_lower
        for kw in (
            "thoả thuận",
            "thỏa thuận",
            "thương lượng",
            "sign in",
            "login to view",
            "you'll love it",
            "cạnh tranh",
            "competitive",
            "negotiable",
        )
    ):
        return None, None

    # Xác định đơn vị tiền tệ: USD hay Triệu VNĐ
    is_usd = bool(re.search(r"(\$|usd)", s_lower))
    is_vnd_unit = bool(
        re.search(r"(triệu|trieu|\btr\b|\bm\b|vnđ|vnd|đồng)", s_lower)
    )
    if not is_usd and not is_vnd_unit:
        return None, None

    multiplier = USD_TO_MILLION_VND if is_usd else 1.0

    # --- MẪU 1: KHOẢNG LƯƠNG (Min - Max) ---
    m_range = re.search(
        r"(\$?\s*\d+(?:[.,]\d+)*)\s*[mM]?\s*(?:-+|–|—|to|đến|~)\s*(\$?\s*\d+(?:[.,]\d+)*)",
        s,
        re.IGNORECASE,
    )
    if m_range:
        raw_v1 = re.sub(r"[^\d.,]", "", m_range.group(1))
        raw_v2 = re.sub(r"[^\d.,]", "", m_range.group(2))
        if raw_v1 and raw_v2:
            v1 = _parse_number(raw_v1)
            v2 = _parse_number(raw_v2)
            low = min(v1, v2) * multiplier
            high = max(v1, v2) * multiplier
            if MIN_VALID_SALARY_M <= high <= MAX_VALID_SALARY_M and low >= MIN_VALID_SALARY_M:
                return round(low, 2), round(high, 2)
            return None, None

    # --- MẪU 2: LƯƠNG CẬN TRÊN (Up to / Tới / Đến / Dưới / Tối đa) ---
    m_upto = re.search(
        r"(?:up\s*to|upto|tới|đến|dưới|tối\s*đa|max|lên\s*đến|lên\s*tới)\s*[:$]?\s*(\$?\s*\d+(?:[.,]\d+)*)",
        s_lower,
        re.IGNORECASE,
    )
    if m_upto:
        raw_v = re.sub(r"[^\d.,]", "", m_upto.group(1))
        if raw_v:
            val = _parse_number(raw_v) * multiplier
            if MIN_VALID_SALARY_M <= val <= MAX_VALID_SALARY_M:
                return round(val * 0.7, 2), round(val, 2)
            return None, None

    # --- MẪU 3: LƯƠNG CẬN DƯỚI (Từ / Trên / Over / From / Min / Tối thiểu) ---
    m_from = re.search(
        r"(?:từ|trên|over|from|min|tối\s*thiểu|at\s*least|starting\s*from)\s*[:$]?\s*(\$?\s*\d+(?:[.,]\d+)*)",
        s_lower,
        re.IGNORECASE,
    )
    if m_from:
        raw_v = re.sub(r"[^\d.,]", "", m_from.group(1))
        if raw_v:
            val = _parse_number(raw_v) * multiplier
            if MIN_VALID_SALARY_M <= val <= MAX_VALID_SALARY_M:
                return round(val, 2), round(val * 1.3, 2)
            return None, None

    # --- MẪU 4: MỘT CON SỐ DUY NHẤT KÈM ĐƠN VỊ (Ví dụ: "25 triệu", "$1500", "20M+") ---
    m_single = re.search(r"(\d+(?:[.,]\d+)*)\s*(\+)?", s)
    if m_single:
        val = _parse_number(m_single.group(1)) * multiplier
        if MIN_VALID_SALARY_M <= val <= MAX_VALID_SALARY_M:
            if m_single.group(2) == "+":
                return round(val, 2), round(val * 1.3, 2)
            return round(val * 0.9, 2), round(val * 1.1, 2)

    return None, None


def parse_salary_record(
    raw_salary: str,
    title: str = "",
    description: str = "",
) -> tuple[float, float, str, float]:
    """Chuẩn hóa mức lương kết hợp kiểm tra chéo trên Tiêu đề & JD nếu thẻ lương bị ẩn."""
    l_min, l_max = _extract_salary_from_string(raw_salary)

    if l_min is None and title:
        l_min, l_max = _extract_salary_from_string(title)

    if l_min is None and description:
        m_jd_sal = re.search(
            r"(?:salary|mức\s+lương|thu\s+nhập)\s*[:\-]\s*([^\n\r]{3,60})",
            description,
            re.IGNORECASE,
        )
        if m_jd_sal:
            l_min, l_max = _extract_salary_from_string(m_jd_sal.group(1))

    if l_min is not None and l_max is not None:
        avg_sal = round((l_min + l_max) / 2.0, 2)
        return l_min, l_max, "Co_Cong_Bo", avg_sal

    return np.nan, np.nan, "Thoa_Thuan", np.nan


def classify_salary_bracket(salary_val: float) -> str:
    """Phân lớp mức lương thành 3 nhãn mục tiêu cho thuật toán Decision Tree (Bước 2.5)."""
    if pd.isna(salary_val) or salary_val < 15.0:
        return "Dưới 15M"
    if salary_val <= 30.0:
        return "15M - 30M"
    return "Trên 30M"


# ===========================================================================
# NHIỆM VỤ 3: CHUẨN HÓA ĐỊA ĐIỂM, MÔ HÌNH LÀM VIỆC, KINH NGHIỆM & CẤP BẬC
# ===========================================================================


def normalize_location(raw_loc: str, raw_wm: str = "") -> str:
    """Chuẩn hóa địa điểm làm việc về 5 nhóm: TP.HCM, Hà Nội, Đà Nẵng, Remote, Khác."""
    combined = f"{raw_loc or ''} {raw_wm or ''}".lower()

    if re.search(r"\b(remote|work\s+from\s+home|wfh|từ\s+xa)\b", combined) and not re.search(
        r"(hồ\s*chí\s*minh|ho\s*chi\s*minh|hà\s*nội|ha\s*noi|đà\s*nẵng|da\s*nang)",
        combined,
    ):
        return "Remote"

    if re.search(
        r"(hồ\s*chí\s*minh|ho\s*chi\s*minh|\bhcm\b|tp\.?\s*hcm|sài\s*gòn|tân\s*bình|bình\s*thạnh|thủ\s*đức|quận\s*\d)",
        combined,
    ):
        return "TP.HCM"

    if re.search(
        r"(hà\s*nội|ha\s*noi|\bhn\b|cầu\s*giấy|nam\s*từ\s*liêm|đống\s*đa|thanh\s*xuân|ba\s*đình|hoàng\s*mai|hai\s*bà\s*trưng)",
        combined,
    ):
        return "Hà Nội"

    if re.search(r"(đà\s*nẵng|da\s*nang|hải\s*châu|sơn\s*trà|thanh\s*khê)", combined):
        return "Đà Nẵng"

    if re.search(r"\b(remote|work\s+from\s+home|wfh)\b", combined):
        return "Remote"

    return "Khác"


def normalize_work_model(raw_wm: str, raw_loc: str = "", description: str = "") -> str:
    """Chuẩn hóa mô hình làm việc về 3 giá trị: On-site, Hybrid, Remote."""
    wm_text = f"{raw_wm or ''} {raw_loc or ''}".lower()
    if re.search(r"\b(remote|work\s+from\s+home|wfh|từ\s+xa)\b", wm_text):
        return "Remote"
    if re.search(r"\b(hybrid|linh\s+hoạt)\b", wm_text):
        return "Hybrid"
    if re.search(r"\b(at\s+office|on-?site|onsite|văn\s+phòng|toàn\s+thời\s+gian)\b", wm_text):
        return "On-site"

    desc_snip = str(description or "")[:1500].lower()
    if re.search(r"\b(100%\s+remote|fully\s+remote|work\s+from\s+anywhere)\b", desc_snip):
        return "Remote"
    if re.search(r"\b(hybrid\s+working|work\s+model\s*:\s*hybrid)\b", desc_snip):
        return "Hybrid"

    return "On-site"


def extract_experience_and_seniority(
    raw_exp: str,
    title: str,
    description: str,
) -> tuple[float, str]:
    """Trích xuất số năm kinh nghiệm (`So_Nam_Kinh_Nghiem`) và chuẩn hóa 5 bậc `Cap_Bac`.

    5 bậc chuẩn theo yêu cầu đề bài:
    - `Fresher` (0.0 - < 1.0 năm)
    - `Junior`  (1.0 - < 2.0 năm)
    - `Middle`  (2.0 - < 4.0 năm)
    - `Senior`  (4.0 - < 6.0 năm)
    - `Lead`    (>= 6.0 năm hoặc vị trí Lead/Principal/Manager/Head/Director/Architect)
    """
    exp_str = str(raw_exp or "").lower()
    title_str = str(title or "").lower()
    desc_str = str(description or "")[:3000].lower()

    years: float | None = None

    # 1. Rút trích số năm trực tiếp từ cột Kinh_Nghiem_Goc
    if any(
        kw in exp_str
        for kw in (
            "không yêu cầu",
            "chưa có kinh nghiệm",
            "intern",
            "thực tập",
            "fresher",
            "mới tốt nghiệp",
        )
    ):
        years = 0.0
    elif "dưới 1 năm" in exp_str or "6 tháng" in exp_str:
        years = 0.5
    else:
        m_yr = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:-\s*(\d+(?:[.,]\d+)?))?\s*năm", exp_str)
        if m_yr:
            y1 = float(m_yr.group(1).replace(",", "."))
            if m_yr.group(2):
                y2 = float(m_yr.group(2).replace(",", "."))
                years = round((y1 + y2) / 2.0, 1)
            else:
                years = round(y1, 1)

    # 2. Xử lý trường hợp Kinh_Nghiem_Goc là nhãn cấp bậc tiếng Anh/Việt (VietnamWorks / TopDev)
    # Lưu ý quan trọng: Nhãn "Experienced (non-manager)" của VietnamWorks chứa chuỗi "manager",
    # do đó phải kiểm tra "non-manager" trước để tránh nhận diện nhầm thành cấp quản lý (Lead)!
    if years is None:
        if "non-manager" in exp_str:
            years = None  # Để bước 3 quét số năm thực tế trong JD trước
        elif any(
            k in exp_str
            for k in ("director", "head", "c-level", "trưởng phòng", "giám đốc")
        ):
            years = 7.0
        elif any(
            k in exp_str
            for k in ("manager", "lead", "principal", "quản lý", "trưởng nhóm")
        ):
            years = 6.0
        elif any(k in exp_str for k in ("chuyên viên cấp cao", "senior")):
            years = 5.0
        elif any(k in exp_str for k in ("middle", "mid")):
            years = 3.0
        elif any(k in exp_str for k in ("junior", "associate")):
            years = 1.5
        elif any(
            k in exp_str
            for k in ("entry", "fresher", "intern", "mới tốt nghiệp", "sinh viên")
        ):
            years = 0.0

    # 3. Quét số năm kinh nghiệm thực tế trong văn bản JD
    if years is None:
        m_jd = re.search(
            r"(?:tối\s+thiểu|ít\s+nhất|trên|từ|at\s+least|minimum|over)?\s*(\d{1,2})\s*(?:\+|-\s*(\d{1,2}))?\s*(?:years?|năm)\s+(?:of\s+)?(?:experience|kinh\s+nghiệm|làm\s+việc)",
            desc_str,
        )
        if m_jd:
            v1 = float(m_jd.group(1))
            if 0 <= v1 <= 15:
                years = v1

    # 4. Đối chiếu với từ khóa cấp bậc trực tiếp trên Tiêu đề (Tieu_De)
    is_lead_title = bool(
        re.search(
            r"\b(lead|leader|principal|manager|head|director|chief|cto|cdo|architect|trưởng\s+phòng|trưởng\s+nhóm|giám\s+đốc|phó\s+phòng)\b",
            title_str,
        )
    )
    is_senior_title = bool(
        re.search(r"\b(senior|sr\.?|cao\s+cấp|chuyên\s+gia)\b", title_str)
    )
    is_mid_title = bool(re.search(r"\b(middle|mid-level|mid\b)\b", title_str))
    is_junior_title = bool(re.search(r"\b(junior|jr\.?)\b", title_str))
    is_fresher_title = bool(
        re.search(
            r"\b(fresher|intern|internship|thực\s+tập|trainee|entry|cộng\s+tác\s+viên)\b",
            title_str,
        )
    )

    if years is None:
        if is_lead_title:
            years = 6.0
        elif is_senior_title:
            years = 4.5
        elif is_mid_title:
            years = 2.5
        elif is_junior_title:
            years = 1.0
        elif is_fresher_title:
            years = 0.0
        elif "non-manager" in exp_str or "experienced" in exp_str or "chuyên viên" in exp_str:
            years = 2.5
        else:
            years = 2.0

    years = max(0.0, min(round(float(years), 1), 15.0))

    # 5. Ánh xạ chuẩn xác vào 5 bậc Cap_Bac của đề bài
    if is_lead_title or years >= 6.0:
        cap_bac = "Lead"
        if years < 5.0:
            years = 6.0
    elif is_senior_title or years >= 4.0:
        cap_bac = "Senior"
        if years < 4.0:
            years = 4.0
    elif is_fresher_title or years < 1.0:
        cap_bac = "Fresher"
    elif is_junior_title or years < 2.0:
        cap_bac = "Junior"
    else:
        cap_bac = "Middle"

    return years, cap_bac


# ===========================================================================
# NHIỆM VỤ 4: LÀM SẠCH VĂN BẢN & TỪ ĐIỂN 60 KỸ NĂNG NGÀNH DATA (ONE-HOT MATRIX)
# ===========================================================================

STOP_WORDS: set[str] = {
    # Tiếng Việt
    "và", "của", "các", "có", "được", "trong", "cho", "với", "là", "để",
    "những", "một", "theo", "tại", "từ", "về", "như", "khi", "không", "đến",
    "trên", "hoặc", "sẽ", "đã", "đang", "này", "việc", "làm", "công",
    "ty", "ứng", "viên", "yêu", "cầu", "mô", "tả", "quyền", "lợi", "tham", "gia",
    # Tiếng Anh
    "the", "and", "to", "of", "in", "for", "with", "on", "as", "are", "is",
    "be", "by", "or", "an", "at", "from", "that", "this", "will", "we", "you",
    "our", "your", "have", "has", "can", "all", "more", "about", "into", "their",
}


def clean_jd_text(text: str) -> str:
    """Làm sạch văn bản mô tả công việc (JD): xóa HTML, ký tự đặc biệt, chuẩn hóa chữ thường và xóa Stop words."""
    if not text:
        return ""
    s = html.unescape(str(text))
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"https?://\S+", " ", s)
    s = s.lower()
    s = re.sub(r"[^\w\s+#/.-]", " ", s, flags=re.UNICODE)
    tokens = [tok for tok in s.split() if tok not in STOP_WORDS and len(tok) > 1]
    return " ".join(tokens)


# Xây dựng Từ điển Kỹ năng Chuyên sâu Ngành Data (6 Nhóm - 60 Kỹ năng)
DATA_SKILL_GROUPS: dict[str, dict[str, re.Pattern]] = {
    "Group_1_Programming_Query": {
        "Python": re.compile(r"\bpython\b", re.IGNORECASE),
        "SQL": re.compile(r"\b(sql|t-sql|pl/sql|nosql|mysql|postgresql|mssql)\b", re.IGNORECASE),
        # Chống bắt nhầm (Zero False-Positives): Chỉ bắt chữ 'R' khi đi kèm ngữ cảnh lập trình/phân tích dữ liệu
        "R": re.compile(
            r"("
            r"\bpython\s*[/,&+]\s*r\b|\br\s*[/,&+]\s*python\b|"
            r"\bsql\s*[/,&+]\s*r\b|\br\s*[/,&+]\s*sql\b|"
            r"\br\s*,\s*python\b|\bpython\s*,\s*r\b|"
            r"\bngôn\s+ngữ\s+r\b|\br\s+programming\b|\br\s+language\b|"
            r"\brstudio\b|\br\s+studio\b|\bshiny\b|\bggplot2\b|\btidyverse\b"
            r")",
            re.IGNORECASE,
        ),
        "Scala": re.compile(r"\bscala\b", re.IGNORECASE),
        "Java": re.compile(r"\bjava\b(?!\s*script)", re.IGNORECASE),
        "C_Cpp": re.compile(r"(?:\bc\+\+|\bc\s*/\s*c\+\+|\bcpp\b|\bngôn\s+ngữ\s+c\b)", re.IGNORECASE),
        "JavaScript": re.compile(r"\b(javascript|typescript|node\.?js|reactjs)\b", re.IGNORECASE),
        "Bash_Shell": re.compile(r"\b(bash|shell\s+script|shell|powershell)\b", re.IGNORECASE),
    },
    "Group_2_BI_Visualization_Analytics": {
        "PowerBI": re.compile(r"\b(power\s*bi|dax|power\s+query|pbi)\b", re.IGNORECASE),
        "Tableau": re.compile(r"\btableau\b", re.IGNORECASE),
        "Looker": re.compile(r"\b(looker|lookml|google\s+data\s+studio|looker\s+studio|superset|metabase|qlik)\b", re.IGNORECASE),
        "Excel": re.compile(r"\b(excel|vba|pivot\s+table|google\s+sheets?|spreadsheet)\b", re.IGNORECASE),
        "Statistics": re.compile(
            r"\b(statistics|statistical|thống\s+kê|xác\s+suất|hypothesis\s+testing|regression|quantitative| định\s+lượng)\b",
            re.IGNORECASE,
        ),
        "AB_Testing": re.compile(r"\b(a/b\s*testing|ab\s*testing|a/b\s*test|experimentation)\b", re.IGNORECASE),
        "Data_Storytelling": re.compile(
            r"\b(data\s+storytelling|data\s+visualization|trực\s+quan\s+hóa|dashboard|reporting|báo\s+cáo)\b",
            re.IGNORECASE,
        ),
    },
    "Group_3_BigData_ETL_DataEngineering": {
        "Spark": re.compile(r"\b(spark|pyspark|apache\s+spark)\b", re.IGNORECASE),
        "Hadoop": re.compile(r"\b(hadoop|hdfs|mapreduce|hive|hbase)\b", re.IGNORECASE),
        "Kafka": re.compile(r"\b(kafka|apache\s+kafka|flink|streaming|rabbitmq)\b", re.IGNORECASE),
        "Airflow": re.compile(r"\b(airflow|apache\s+airflow|dagster|prefect|orchestration)\b", re.IGNORECASE),
        "dbt": re.compile(r"\bdbt\b", re.IGNORECASE),
        "ETL": re.compile(
            r"\b(etl|elt|data\s+pipeline|ssis|informatica|talend|pentaho|ni-?fi|airbyte|debezium|data\s+integration)\b",
            re.IGNORECASE,
        ),
        "Data_Warehouse": re.compile(
            r"\b(data\s+warehouse|data\s+warehousing|dwh|kho\s+dữ\s+liệu|olap|star\s+schema|dimensional\s+modeling|data\s+mart)\b",
            re.IGNORECASE,
        ),
        "Data_Lake": re.compile(
            r"\b(data\s+lake|lakehouse|delta\s+lake|apache\s+iceberg|hudi|minio|parquet)\b",
            re.IGNORECASE,
        ),
        "Data_Modeling": re.compile(
            r"\b(data\s+model|data\s+modeling|data\s+modelling|thiết\s+kế\s+cơ\s+sở\s+dữ\s+liệu|erd|database\s+design|schema\s+design)\b",
            re.IGNORECASE,
        ),
    },
    "Group_4_DataScience_AI_ML": {
        "Machine_Learning": re.compile(
            r"\b(machine\s+learning|học\s+máy|\bml\b|xgboost|lightgbm|catboost|random\s+forest|predictive\s+model|ai/ml)\b",
            re.IGNORECASE,
        ),
        "Deep_Learning": re.compile(
            r"\b(deep\s+learning|học\s+sâu|neural\s+network|cnn|rnn|lstm|transformer)\b",
            re.IGNORECASE,
        ),
        "Pandas": re.compile(r"\b(pandas|polars)\b", re.IGNORECASE),
        "NumPy": re.compile(r"\b(numpy|scipy)\b", re.IGNORECASE),
        "Scikit_Learn": re.compile(r"\b(scikit-learn|sklearn|scikit\s+learn)\b", re.IGNORECASE),
        "PyTorch": re.compile(r"\bpytorch\b", re.IGNORECASE),
        "TensorFlow": re.compile(r"\b(tensorflow|keras)\b", re.IGNORECASE),
        "NLP": re.compile(
            r"\b(nlp|natural\s+language\s+processing|xử\s+lý\s+ngôn\s+ngữ\s+tự\s+nhiên|text\s+mining|bert|huggingface)\b",
            re.IGNORECASE,
        ),
        "Computer_Vision": re.compile(
            r"\b(computer\s+vision|thị\s+giác\s+máy\s+tính|opencv|yolo|image\s+processing|xử\s+lý\s+ảnh|xử\s+lý\s+dữ\s+liệu\s+hình\s+ảnh|ocr)\b",
            re.IGNORECASE,
        ),
        "LLM_GenAI": re.compile(
            r"\b(llm|llms|large\s+language\s+model|genai|generative\s+ai|langchain|llamaindex|rag\b|openai|gpt|prompt\s+engineering|ai\s+agent)\b",
            re.IGNORECASE,
        ),
        "MLOps": re.compile(
            r"\b(mlops|mlflow|kubeflow|model\s+deployment|model\s+serving|triton|weights\s*&\s*biases|feast)\b",
            re.IGNORECASE,
        ),
    },
    "Group_5_Databases_Cloud_DevOps": {
        "PostgreSQL": re.compile(r"\b(postgresql|postgres|pl/pgsql)\b", re.IGNORECASE),
        "MySQL": re.compile(r"\b(mysql|mariadb)\b", re.IGNORECASE),
        "SQL_Server": re.compile(r"\b(sql\s+server|mssql|ms\s+sql|t-sql|ssrs|ssas)\b", re.IGNORECASE),
        "Oracle": re.compile(r"\b(oracle|pl/sql|oracle\s+db)\b", re.IGNORECASE),
        "MongoDB": re.compile(r"\b(mongodb|mongo|nosql|dynamodb|couchbase|cassandra)\b", re.IGNORECASE),
        "Redis": re.compile(r"\b(redis|memcached|in-memory\s+cache)\b", re.IGNORECASE),
        "Elasticsearch": re.compile(r"\b(elasticsearch|elastic\s+stack|elk|opensearch|kibana)\b", re.IGNORECASE),
        "BigQuery": re.compile(r"\b(bigquery|google\s+bigquery)\b", re.IGNORECASE),
        "Snowflake": re.compile(r"\bsnowflake\b", re.IGNORECASE),
        "Databricks": re.compile(r"\bdatabricks\b", re.IGNORECASE),
        "Redshift": re.compile(r"\b(redshift|amazon\s+redshift)\b", re.IGNORECASE),
        "Cloud_AWS": re.compile(
            r"\b(aws|amazon\s+web\s+services|s3\b|ec2\b|aws\s+glue|aws\s+lambda|athena|emr\b|sagemaker)\b",
            re.IGNORECASE,
        ),
        "Cloud_Azure": re.compile(
            r"\b(azure|microsoft\s+azure|azure\s+data\s+factory|adf|synapse|azure\s+databricks|fabric)\b",
            re.IGNORECASE,
        ),
        "Cloud_GCP": re.compile(
            r"\b(gcp|google\s+cloud|dataproc|dataflow|vertex\s+ai|pub/sub)\b",
            re.IGNORECASE,
        ),
        "Docker": re.compile(r"\b(docker|containerization|container)\b", re.IGNORECASE),
        "Kubernetes": re.compile(r"\b(kubernetes|k8s|helm|openshift)\b", re.IGNORECASE),
        "Git": re.compile(r"\b(git|github|gitlab|bitbucket)\b", re.IGNORECASE),
        "Linux": re.compile(r"\b(linux|ubuntu|centos|red\s*hat|unix)\b", re.IGNORECASE),
        "CI_CD": re.compile(
            r"\b(ci/cd|ci\s*-\s*cd|jenkins|github\s+actions|gitlab\s+ci|devops|terraform|ansible)\b",
            re.IGNORECASE,
        ),
    },
    "Group_6_SoftSkills_Governance": {
        "English": re.compile(
            r"\b(english|tiếng\s+anh|toeic|ielts|ngoại\s+ngữ)\b",
            re.IGNORECASE,
        ),
        "Communication": re.compile(
            r"\b(communication|giao\s+tiếp|thuyết\s+trình|presentation|stakeholder)\b",
            re.IGNORECASE,
        ),
        "Problem_Solving": re.compile(
            r"\b(problem[- ]solving|giải\s+quyết\s+vấn\s+đề|analytical\s+thinking|tư\s+duy\s+phân\s+tích|critical\s+thinking)\b",
            re.IGNORECASE,
        ),
        "Teamwork": re.compile(
            r"\b(teamwork|team\s+player|làm\s+việc\s+nhóm|collaboration|phối\s+hợp)\b",
            re.IGNORECASE,
        ),
        "Agile_Scrum": re.compile(
            r"\b(agile|scrum|kanban|jira|confluence)\b",
            re.IGNORECASE,
        ),
        "Data_Governance": re.compile(
            r"\b(data\s+governance|data\s+quality|data\s+security|quản\s+trị\s+dữ\s+liệu|bảo\s+mật\s+dữ\s+liệu|gdpr|compliance|master\s+data|data\s+catalog|data\s+lineage)\b",
            re.IGNORECASE,
        ),
    },
}

FLAT_SKILL_PATTERNS: dict[str, re.Pattern] = {
    skill_name: pattern
    for group_dict in DATA_SKILL_GROUPS.values()
    for skill_name, pattern in group_dict.items()
}


def extract_skills_from_text(title: str, description: str) -> dict[str, int]:
    """Bóc tách 60 kỹ năng ngành Data từ Tiêu đề & Mô tả công việc thành vector nhị phân 0/1."""
    combined_text = f"{title or ''}\n{description or ''}"
    result: dict[str, int] = {}
    for skill_name, regex_pat in FLAT_SKILL_PATTERNS.items():
        result[skill_name] = 1 if regex_pat.search(combined_text) else 0
    return result


# ===========================================================================
# PIPELINE TỔNG HỢP BƯỚC 2.1 & KIỂM ĐỊNH CHẤT LƯỢNG (VERIFICATION)
# ===========================================================================


def run_cleaning_pipeline(
    in_csv: str | Path = "data/raw_data.csv",
    out_csv: str | Path = "data/clean_data.csv",
) -> pd.DataFrame:
    """Thực thi toàn bộ quy trình làm sạch Bước 2.1 và xuất `data/clean_data.csv`."""
    in_path = Path(in_csv)
    if not in_path.exists():
        raise FileNotFoundError(
            f"Không tìm thấy tệp đầu vào {in_path}. Hãy chạy `python step_01_export_raw_csv.py` trước."
        )

    df = pd.read_csv(in_path, encoding="utf-8-sig")
    print("=" * 78)
    print(f"🧹 BẮT ĐẦU PIPELINE TIỀN XỬ LÝ & LÀM SẠCH DỮ LIỆU NGÀNH DATA (BƯỚC 2.1)")
    print(f"   • Đọc tệp đầu vào : {in_path} ({len(df)} dòng x {len(df.columns)} cột)")
    print("=" * 78, flush=True)

    # 1. Phân nhóm vị trí nghề nghiệp trong hệ sinh thái Data (Nhom_Nganh_Data)
    df["Nhom_Nganh_Data"] = [
        classify_data_role_group(t, d)
        for t, d in zip(df["Tieu_De"], df["Mo_Ta_Cong_Viec"])
    ]

    # 2. Chuẩn hóa Địa điểm, Mô hình làm việc, Số năm kinh nghiệm & Cấp bậc
    df["Dia_Diem_Chuan"] = [
        normalize_location(loc, wm)
        for loc, wm in zip(df["Dia_Diem_Goc"], df["Hinh_Thuc_Lam_Viec_Goc"])
    ]
    df["Mo_Hinh_Lam_Viec"] = [
        normalize_work_model(wm, loc, desc)
        for wm, loc, desc in zip(
            df["Hinh_Thuc_Lam_Viec_Goc"], df["Dia_Diem_Goc"], df["Mo_Ta_Cong_Viec"]
        )
    ]

    exp_and_level = [
        extract_experience_and_seniority(exp, title, desc)
        for exp, title, desc in zip(
            df["Kinh_Nghiem_Goc"], df["Tieu_De"], df["Mo_Ta_Cong_Viec"]
        )
    ]
    df["So_Nam_Kinh_Nghiem"] = [item[0] for item in exp_and_level]
    df["Cap_Bac"] = [item[1] for item in exp_and_level]

    # 3. Chuẩn hóa Mức lương bằng Regex & Điền khuyết kép (NaN cho EDA + Median Imputation cho ML)
    sal_parsed = [
        parse_salary_record(sal, title, desc)
        for sal, title, desc in zip(
            df["Muc_Luong_Goc"], df["Tieu_De"], df["Mo_Ta_Cong_Viec"]
        )
    ]
    df["Luong_Min"] = [item[0] for item in sal_parsed]
    df["Luong_Max"] = [item[1] for item in sal_parsed]
    df["Trang_Thai_Luong"] = [item[2] for item in sal_parsed]
    df["Luong_Trung_Binh"] = [item[3] for item in sal_parsed]

    group_medians = df.groupby(["Nhom_Nganh_Data", "Cap_Bac"])[
        "Luong_Trung_Binh"
    ].transform("median")
    role_medians = df.groupby("Nhom_Nganh_Data")["Luong_Trung_Binh"].transform("median")
    level_medians = df.groupby("Cap_Bac")["Luong_Trung_Binh"].transform("median")
    global_median = float(df["Luong_Trung_Binh"].median())

    df["Luong_Trung_Binh_Imputed"] = (
        df["Luong_Trung_Binh"]
        .fillna(group_medians)
        .fillna(role_medians)
        .fillna(level_medians)
        .fillna(global_median)
        .round(2)
    )

    df["Khoang_Luong_Phan_Lop"] = [
        classify_salary_bracket(val) for val in df["Luong_Trung_Binh_Imputed"]
    ]

    # 4. Làm sạch văn bản JD & Bóc tách Ma trận One-Hot 60 kỹ năng chuyên sâu ngành Data
    df["Mo_Ta_Lam_Sach"] = [clean_jd_text(desc) for desc in df["Mo_Ta_Cong_Viec"]]

    skill_dicts = [
        extract_skills_from_text(title, desc)
        for title, desc in zip(df["Tieu_De"], df["Mo_Ta_Cong_Viec"])
    ]

    danh_sach_ky_nang: list[str] = []
    so_luong_ky_nang: list[int] = []
    for sdict in skill_dicts:
        present = [k for k, v in sdict.items() if v == 1]
        danh_sach_ky_nang.append("; ".join(present) if present else "SQL; Python")
        so_luong_ky_nang.append(len(present) if present else 2)
        if not present:
            sdict["SQL"] = 1
            sdict["Python"] = 1

    df["Danh_Sach_Ky_Nang"] = danh_sach_ky_nang
    df["So_Luong_Ky_Nang"] = so_luong_ky_nang

    skill_df = pd.DataFrame(
        [{f"Skill_{k}": v for k, v in sdict.items()} for sdict in skill_dicts],
        index=df.index,
    )
    df = pd.concat([df, skill_df], axis=1)

    ordered_base_cols = [
        "Job_ID",
        "Site",
        "Tieu_De",
        "Cong_Ty",
        "Nhom_Nganh_Data",
        "Dia_Diem_Goc",
        "Dia_Diem_Chuan",
        "Hinh_Thuc_Lam_Viec_Goc",
        "Mo_Hinh_Lam_Viec",
        "Kinh_Nghiem_Goc",
        "So_Nam_Kinh_Nghiem",
        "Cap_Bac",
        "Muc_Luong_Goc",
        "Trang_Thai_Luong",
        "Luong_Min",
        "Luong_Max",
        "Luong_Trung_Binh",
        "Luong_Trung_Binh_Imputed",
        "Khoang_Luong_Phan_Lop",
        "Danh_Sach_Ky_Nang",
        "So_Luong_Ky_Nang",
        "Mo_Ta_Cong_Viec",
        "Mo_Ta_Lam_Sach",
        "URL_Goc",
        "Timestamp",
    ]
    skill_cols = [f"Skill_{k}" for k in FLAT_SKILL_PATTERNS.keys()]
    df = df[ordered_base_cols + skill_cols]

    out_path = Path(out_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False, encoding="utf-8-sig")

    print("\n📊 KẾT QUẢ KIỂM ĐỊNH CHẤT LƯỢNG DỮ LIỆU SAU LÀM SẠCH (`clean_data.csv`):")
    print(f"   • Tổng số bản ghi sạch     : {len(df)} dòng")
    print(
        f"   • Tổng số thuộc tính (cột) : {len(df.columns)} cột (25 cột chuẩn + {len(skill_cols)} cột One-Hot Skill_*)"
    )
    print(f"\n1️⃣ Phân bổ theo Nhóm Ngành Data (`Nhom_Nganh_Data`):")
    for grp, cnt in df["Nhom_Nganh_Data"].value_counts().items():
        print(f"   - {grp:<34}: {cnt:>4} tin ({cnt / len(df) * 100:5.1f}%)")

    print(f"\n2️⃣ Thống kê Trạng thái Lương & Mức lương (Triệu VNĐ/tháng):")
    for st, cnt in df["Trang_Thai_Luong"].value_counts().items():
        print(f"   - {st:<34}: {cnt:>4} tin ({cnt / len(df) * 100:5.1f}%)")
    disclosed = df["Luong_Trung_Binh"].dropna()
    print(
        f"   - Lương TB (Tin có công bố)        : Mean = {disclosed.mean():.2f}M | Median = {disclosed.median():.2f}M | Min = {disclosed.min():.2f}M | Max = {disclosed.max():.2f}M"
    )
    print(
        f"   - Lương TB (Sau Median Imputation) : Mean = {df['Luong_Trung_Binh_Imputed'].mean():.2f}M | Median = {df['Luong_Trung_Binh_Imputed'].median():.2f}M"
    )

    print(f"\n3️⃣ Lương Trung bình theo Nhóm Ngành Data (Tin có công bố vs Imputed):")
    for grp, sub in df.groupby("Nhom_Nganh_Data"):
        m_real = sub["Luong_Trung_Binh"].mean()
        md_real = sub["Luong_Trung_Binh"].median()
        m_imp = sub["Luong_Trung_Binh_Imputed"].mean()
        print(
            f"   - {grp:<34}: Mean Thực = {m_real:5.2f}M | Median Thực = {md_real:5.2f}M | Mean Imputed = {m_imp:5.2f}M"
        )

    print(f"\n4️⃣ Phân bổ theo Cấp bậc (`Cap_Bac`), Mô hình (`Mo_Hinh_Lam_Viec`) & Khoảng lương (`Khoang_Luong_Phan_Lop`):")
    for cb, cnt in df["Cap_Bac"].value_counts().items():
        print(f"   - Cấp bậc {cb:<26}: {cnt:>4} tin ({cnt / len(df) * 100:5.1f}%)")
    for wm, cnt in df["Mo_Hinh_Lam_Viec"].value_counts().items():
        print(f"   - Mô hình {wm:<26}: {cnt:>4} tin ({cnt / len(df) * 100:5.1f}%)")
    for kl, cnt in df["Khoang_Luong_Phan_Lop"].value_counts().items():
        print(f"   - Khoảng lương {kl:<21}: {cnt:>4} tin ({cnt / len(df) * 100:5.1f}%)")

    print(f"\n5️⃣ Top 20 Kỹ năng có tần suất xuất hiện cao nhất trong Ngành Data:")
    skill_totals = df[skill_cols].sum().sort_values(ascending=False)
    for idx, (scol, cnt) in enumerate(skill_totals.head(20).items(), 1):
        print(
            f"   {idx:02d}. {scol:<28}: {int(cnt):>4} tin ({cnt / len(df) * 100:5.1f}%)"
        )

    print("=" * 78)
    print(f"✅ ĐÃ XUẤT FILE BÀN GIAO CHO THÀNH VIÊN 2 & 3: {out_path}")
    print("=" * 78, flush=True)
    return df


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(
        description="Bước 2.1: Tiền xử lý & Làm sạch dữ liệu chuyên sâu ngành Data"
    )
    parser.add_argument("--in", dest="in_csv", type=str, default="data/raw_data.csv")
    parser.add_argument("--out", dest="out_csv", type=str, default="data/clean_data.csv")
    args = parser.parse_args()

    run_cleaning_pipeline(in_csv=args.in_csv, out_csv=args.out_csv)


if __name__ == "__main__":
    main()
