# 📊 Thu thập và Khai phá Dữ liệu Tuyển dụng Nhóm ngành Dữ liệu & Trí tuệ Nhân tạo (Data & AI) tại Việt Nam

> **Đồ án môn học:** Khai Phá Dữ Liệu (`ITEC3417`)  
> **Phân hệ hiện tại:** Nhánh làm việc của **Thành viên 1** (`thanh-vien-1-nganh-data`) — Phụ trách **Giai đoạn 1 (Thu thập dữ liệu - 15%)** và **Giai đoạn 2 - Bước 2.1 (Tiền xử lý & Làm sạch dữ liệu - 10%)**.  
> **Môi trường tối ưu:** **Windows / macOS / Linux**, Python `3.12` (chốt trong `.python-version`, hỗ trợ 3.11 – 3.14).

---

## 🎯 1. Mục tiêu & Phạm vi Đề tài

Dự án tập trung thu thập, chuẩn hóa và khai phá dữ liệu tuyển dụng thực tế của **Hệ sinh thái Ngành Dữ liệu & Trí tuệ Nhân tạo (Data & AI)** tại Việt Nam từ 4 nền tảng tuyển dụng uy tín nhất (**ITviec, TopCV, VietnamWorks, TopDev**), bao gồm 5 phân khúc nghề nghiệp:
1. **`Data Analyst / BI`**: Data Analyst, Business Intelligence (BI), Business Analyst (Data-driven), Product/Financial/Risk/Marketing Data Analyst.
2. **`Data Engineer / Big Data`**: Data Engineer, Big Data Engineer, Analytics Engineer, ETL/Data Warehouse/Data Lake Engineer, Data Architect.
3. **`Data Scientist / AI & ML`**: Data Scientist, Machine Learning Engineer, AI Engineer, Deep Learning, Computer Vision, NLP, LLM/GenAI, MLOps.
4. **`Database / Data Platform & Ops`**: Database Administrator (DBA), Data Governance, Data Quality, Cloud/System Data Infrastructure.
5. **`Data-Driven Software Engineer`**: Kỹ sư phần mềm/Backend làm việc trực tiếp với cơ sở dữ liệu lớn, hệ thống lưu trữ và đường ống dữ liệu.

---

## 📂 2. Cấu trúc Cây Thư mục Chuẩn mực (Thành viên 1)

```text
root/
├── .python-version               # Chốt phiên bản Python (3.12) cho uv
├── .gitignore                    # Chỉ chặn .venv/, __pycache__/, .ruff_cache/ (KHÔNG chặn thư mục data/)
├── pyproject.toml                # Khai báo thư viện + khoảng phiên bản Python cho phép (dùng với uv)
├── uv.lock                       # Khoá chính xác phiên bản thư viện cho Windows / macOS / Linux
├── requirements.txt              # Bản xuất từ uv.lock cho người dùng pip (cùng phiên bản, mọi hệ điều hành)
├── README.md                     # Hướng dẫn chạy Crawler ngành Data và Pipeline làm sạch trên Windows
├── crawlers/                     # Gói công cụ cào dữ liệu (ITviec, TopCV, VietnamWorks, TopDev)
│   ├── __init__.py               # Khởi tạo package và xuất các hàm dùng chung
│   ├── base.py                   # Tiện ích đọc/ghi JSONL, polite_sleep (Robots.txt etiquette), simulate_infinite_scroll
│   ├── browser.py                # Quản lý trình duyệt Chrome/Playwright tối ưu cho Windows 10/11
│   ├── itviec.py                 # Crawler ITviec (Pagination + Wait DOM + Infinite Scroll + Random Sleep)
│   ├── topcv.py                  # Crawler TopCV (Pagination + Wait DOM + Infinite Scroll + Random Sleep)
│   ├── vietnamworks.py           # Crawler VietnamWorks (AJAX JSON API + Pagination + Random Sleep)
│   └── topdev.py                 # Crawler TopDev (Pagination + Wait DOM + Infinite Scroll + Random Sleep)
├── scraper.py                    # Script chạy tổng hợp theo từ khóa ngành Data & phục vụ Live Demo tại lớp
├── step_01_export_raw_csv.py     # Script lọc/gộp dữ liệu nhóm ngành Data, lọc trùng và xuất ra data/raw_data.csv
├── step_02_clean_data.py         # Script tiền xử lý Bước 2.1 chuyên sâu cho ngành Data -> xuất data/clean_data.csv
├── notebooks/
│   └── TV1_Data_Cleaning_Pipeline.ipynb # Notebook trình bày trực quan từng bước làm sạch dữ liệu ngành Data
├── data/
│   ├── raw/                      # Chứa các file .jsonl gốc đã cào (itviec, topcv, vietnamworks, topdev)
│   ├── raw_data.csv              # ĐẦU RA BẮT BUỘC GIAI ĐOẠN 1 (và bản sao đồng bộ raw_jobs_data.csv)
│   └── clean_data.csv            # ĐẦU RA BẮT BUỘC BƯỚC 2.1 (Bàn giao cho Thành viên 2 & 3 làm EDA, K-Means, Apriori, Decision Tree)
└── BAO_CAO_THANH_VIEN_1.md       # Báo cáo học thuật Chương 1, Chương 2 (chuyên sâu ngành Data) & Cẩm nang vấn đáp 10 điểm
```

---

## ⚙️ 3. Hướng dẫn Cài đặt (Windows / macOS / Linux)

Dự án chốt **Python 3.12** (file `.python-version`) và **khoá phiên bản thư viện** trong `uv.lock`
(file khoá dùng chung cho mọi hệ điều hành). Nhờ vậy ai tải về cũng cài ra **đúng cùng một bộ thư viện**.

| File | Vai trò |
|---|---|
| `.python-version` | Phiên bản Python chuẩn của dự án: `3.12` |
| `pyproject.toml` | Danh sách thư viện + khoảng phiên bản cho phép (Python 3.11 – 3.14) |
| `uv.lock` | Khoá chính xác phiên bản mọi thư viện cho Windows, macOS, Linux |
| `requirements.txt` | Bản xuất từ `uv.lock` cho người dùng `pip` (cùng phiên bản) |

### Cách 1 – Dùng `uv` (khuyến nghị, tự tải đúng Python 3.12)

Cài uv một lần: <https://docs.astral.sh/uv/getting-started/installation/>

```bash
# Chạy tại thư mục gốc dự án (giống nhau trên Windows / macOS / Linux)
uv sync                               # tạo .venv bằng Python 3.12 + cài đúng phiên bản trong uv.lock
uv run playwright install chromium    # chỉ cần nếu chạy crawler
uv run jupyter lab                    # mở notebook
```

> Nếu đã có thư mục `.venv` cũ tạo bằng phiên bản Python khác, `uv sync` sẽ tự xoá và tạo lại cho đúng 3.12.

### Cách 2 – Dùng `pip` + `venv` (cần cài sẵn Python 3.12; 3.11 – 3.14 vẫn chạy được)

```powershell
# Windows (PowerShell)
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install chromium
```

```bash
# macOS / Linux
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
playwright install chromium
```

Trong VS Code / Jupyter, chọn kernel trỏ tới `.venv` của dự án trước khi chạy notebook.

### Thêm hoặc nâng cấp thư viện

Sửa `pyproject.toml` (hoặc `uv add <tên-thư-viện>`), sau đó cập nhật cả hai file khoá:

```bash
uv lock
uv export --format requirements-txt --no-hashes --no-header --no-annotate -o requirements.txt
```

> **Lưu ý về cảnh báo `vert: bool was deprecated in Matplotlib 3.11`:** cảnh báo này phát sinh bên trong
> `seaborn 0.13.2` (bản mới nhất) khi vẽ `sns.boxplot` với Matplotlib ≥ 3.10, không phải lỗi của code dự án
> và không ảnh hưởng biểu đồ. Notebook `TV2_EDA_Clustering_Apriori.ipynb` đã ẩn đúng cảnh báo này ở ô import.

---

## 🚀 4. Hướng dẫn Thực thi Pipeline & Live Demo tại Lớp

### 4.1. Chạy Live Demo Cào Dữ Liệu Trực Tiếp (Giai đoạn 1 - Code Audit)
Khi giảng viên yêu cầu chạy thử công cụ thu thập dữ liệu ngay tại lớp, mở PowerShell và gõ:

```powershell
# Xem danh sách 20 từ khóa định vị mục tiêu ngành Data (DATA_KEYWORDS)
.\.venv\Scripts\python.exe scraper.py --list-keywords

# Live Demo bật trình duyệt Chrome cào trực tiếp 2 trang vị trí "Data Analyst" trên ITviec
.\.venv\Scripts\python.exe scraper.py --site itviec --keyword "Data Analyst" --pages 2

# Hoặc cào vị trí "Data Engineer" trên TopDev / VietnamWorks / TopCV
.\.venv\Scripts\python.exe scraper.py --site topdev --keyword "Data Engineer" --pages 2
.\.venv\Scripts\python.exe scraper.py --site vietnamworks --keyword "Data Scientist" --pages 2
.\.venv\Scripts\python.exe scraper.py --site topcv --keyword "Business Intelligence" --pages 2
```

### 4.2. Chạy Bước 1: Trích lọc dữ liệu Ngành Data & Xuất `data/raw_data.csv`
Đọc toàn bộ kho dữ liệu `.jsonl` trong `data/raw/`, lọc trùng theo `job_url` và trích lọc theo chiến lược 2 tầng ngành Data để xuất tệp `data/raw_data.csv` (kèm bản sao `data/raw_jobs_data.csv`):

```powershell
.\.venv\Scripts\python.exe step_01_export_raw_csv.py
```

### 4.3. Chạy Bước 2: Tiền xử lý, Làm sạch & Bóc tách 60 Kỹ năng Ngành Data (`data/clean_data.csv`)
Thực thi toàn bộ 5 nhiệm vụ tiền xử lý Bước 2.1 bằng Biểu thức chính quy (Regex) và Từ điển Kỹ năng chuyên sâu ngành Data:

```powershell
.\.venv\Scripts\python.exe step_02_clean_data.py
```

---

## 🤝 5. Tài liệu Báo cáo & Bàn giao cho Thành viên 2 và Thành viên 3

Toàn bộ cơ sở lý thuyết, thống kê mô tả dữ liệu thực tế, giải phẫu từng dòng code Regex, kịch bản bảo vệ vấn đáp 10 điểm và hướng dẫn chọn cột chạy thuật toán **EDA, K-Means Clustering, Apriori, Decision Tree** được trình bày chi tiết trong:
- 📄 **[BAO_CAO_THANH_VIEN_1.md](BAO_CAO_THANH_VIEN_1.md)**
- 📓 **[notebooks/TV1_Data_Cleaning_Pipeline.ipynb](notebooks/TV1_Data_Cleaning_Pipeline.ipynb)**
