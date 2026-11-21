# 📑 ĐỀ CƯƠNG BÁO CÁO TỔNG KẾT ĐỒ ÁN MÔN HỌC (`ITEC3417`) — CHUẨN HỌC THUẬT 10 ĐIỂM

> **Tên tệp PDF nộp LMS:** `NhomXX_BaoCao_BaiTapLon.pdf`  
> **Tên đề tài:** **THU THẬP VÀ KHAI PHÁ DỮ LIỆU TUYỂN DỤNG THỰC TẾ TRONG NGÀNH DỮ LIỆU & TRÍ TUỆ NHÂN TẠO (DATA & AI) TẠI VIỆT NAM**  
> **Quy mô trang chuẩn:** **20 – 22 trang** *(Nằm gọn hoàn hảo trong khung yêu cầu 15 – 25 trang của Đề bài, chưa tính Phụ lục mã nguồn)*.  
> **Toàn bộ số liệu trong đề cương này đã được ĐỒNG BỘ 100%** với bộ dữ liệu `data/clean_data.csv` (`1.547 dòng × 86 cột`) và 4 file Notebook trên nhánh `audit-and-fix-final`.

---

## 📊 PHÂN BỔ ĐỘ DÀI TRANG KHUYẾN NGHỊ TOÀN BÁO CÁO (TỔNG: 21 TRANG)

| Phần / Chương mục | Nội dung trọng tâm theo Đề bài PDF (`ITEC3417`) | Thành viên chấp bút chính | Số trang khuyến nghị |
| :--- | :--- | :---: | :---: |
| **Trang bìa, Mục lục & Bảng WBS** | Trang bìa học thuật + Biên bản phân công nhiệm vụ (WBS có chữ ký) + Mục lục | Cả nhóm | **2.0 trang** *(Trang 1–2)* |
| **Chương 1: Tổng quan đề tài** | Lý do chọn lĩnh vực Data & AI; Đối tượng mục tiêu; Bộ 20 từ khóa; 4 Câu hỏi nghiên cứu | **Thành viên 1** | **2.0 trang** *(Trang 3–4)* |
| **Chương 2: Thu thập & Tiền xử lý dữ liệu** | Kiến trúc Crawler đa nguồn; 3 Kỹ thuật vượt chặn; Thống kê `raw_data.csv`; Giải phẫu Regex lương, kinh nghiệm & Từ điển 60 kỹ năng (`clean_data.csv`) | **Thành viên 1** | **4.0 trang** *(Trang 5–8)* |
| **Chương 3: Phân tích Khám phá (EDA)** | Hệ thống biểu đồ đa chiều về mức lương (chung, theo 5 ngành, theo 5 cấp bậc, theo 3 vùng địa lý), Top 15 kỹ năng, Heatmap tương quan & Mô hình làm việc | **Thành viên 2** | **3.5 trang** *(Trang 9–12)* |
| **Chương 4: Gom cụm & Luật kết hợp** | Gom cụm K-Means (`Elbow`, `Silhouette = 0.1603`, `PCA`, 3 chân dung cụm); Luật kết hợp Apriori (`Support`, `Confidence`, `Lift > 1.2`, `Conviction` & 32 Luật nhiễu) | **Thành viên 2** | **4.0 trang** *(Trang 13–16)* |
| **Chương 5: Phân lớp & Dự báo** | Bài toán dự báo khoảng lương; Phát hiện & Khắc phục Data Leakage; Cắt tỉa cành `ccp_alpha` bằng 5-Fold CV; Đối sánh 4 mô hình; Confusion Matrix, Macro F1 & Truy vết lỗi sai | **Thành viên 3** | **3.5 trang** *(Trang 17–20)* |
| **Chương 6: Kết luận & Khuyến nghị** | Tổng kết tri thức KDD; Lộ trình hành trang ứng tuyển cho sinh viên ngành Data/CNTT (có số liệu chứng minh); Hạn chế & Hướng phát triển | **Thành viên 3** | **2.0 trang** *(Trang 21–22)* |

---

## PHẦN MỞ ĐẦU: TRANG BÌA & BIÊN BẢN PHÂN CÔNG NHIỆM VỤ (WBS)
*(Độ dài khuyến nghị: 2 trang đầu tiên — Bắt buộc theo Mục 7.2 của Đề bài để chống ỷ lại và làm căn cứ nhân hệ số điểm cá nhân)*

### Mẫu Trang Bìa (Trang 1)
```text
TRƯỜNG ĐẠI HỌC ........................................
KHOA CÔNG NGHỆ THÔNG TIN
----------------------------------------

BÁO CÁO ĐỒ ÁN MÔN HỌC / BÀI TẬP LỚN
HỌC PHẦN: KHAI PHÁ DỮ LIỆU (ITEC3417)

ĐỀ TÀI:
THU THẬP VÀ KHAI PHÁ DỮ LIỆU TUYỂN DỤNG THỰC TẾ
NHÓM NGÀNH DỮ LIỆU & TRÍ TUỆ NHÂN TẠO (DATA & AI) TẠI VIỆT NAM

Giảng viên hướng dẫn : ........................................
Nhóm thực hiện       : Nhóm XX
Danh sách thành viên :
  1. [Họ và tên Thành viên 1] - MSSV: .............. (Nhóm trưởng)
  2. Ngô Hoàng Long           - MSSV: .............. (Thành viên 2)
  3. Huỳnh Hữu Phước          - MSSV: .............. (Thành viên 3)

TP. Hồ Chí Minh / Hà Nội, Tháng 11 Năm 2026
```

### Mẫu Biên bản Phân công Nhiệm vụ Chi tiết — Work Breakdown Structure (Trang 2)
*(Copy trực tiếp bảng này vào Trang 2 của file Word/PDF, in ra ký tươi hoặc chèn chữ ký số của cả 3 thành viên)*

| STT | Họ và Tên & Vai trò | Giai đoạn & Nhiệm vụ chi tiết đã thực hiện | Sản phẩm bàn giao (Deliverables) | Tỷ lệ đóng góp (%) | Chữ ký xác nhận |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **1** | **[Họ tên TV1]**<br>*(Principal Data Engineer — Trưởng nhóm)* | • Thiết kế kiến trúc Crawler đa nguồn (`Playwright` + `BeautifulSoup4` + `AJAX API`) cho `ITviec`, `TopCV`, `VietnamWorks`, `TopDev` tích hợp đủ 3 kỹ thuật (`Pagination`, `Infinite Scroll`, `Random Sleep`).<br>• Xây dựng chiến lược lọc 2 tầng ngành Data & khử trùng từ `8.320` tin gốc ra `1.547` tin chuẩn (`step_01_export_raw_csv.py`).<br>• Viết thuật toán Regex chuẩn hóa lương (xử lý `/tháng`, `/năm`, `USD/VNĐ`, điền khuyết kép), chuẩn hóa địa điểm, cấp bậc và bóc tách Từ điển 60 Kỹ năng thành Ma trận One-Hot (`step_02_clean_data.py`).<br>• Viết **Chương 1** và **Chương 2** của Báo cáo tổng kết. | • `scraper.py` & `crawlers/`<br>• `step_01_export_raw_csv.py`<br>• `step_02_clean_data.py`<br>• `data/raw_data.csv` (`1.547 × 11`)<br>• `data/clean_data.csv` (`1.547 × 86`)<br>• `TV1_Data_Cleaning_Pipeline.ipynb` | **34%** | *(Ký & ghi rõ họ tên)* |
| **2** | **Ngô Hoàng Long**<br>*(Lead Data Analyst — Thành viên 2)* | • Thực hiện Phân tích khám phá dữ liệu đa chiều (Bước 2.2 - EDA): phân phối lương thực tế (`n = 394`), so sánh lương theo 5 nhóm ngành, 5 cấp bậc (`Fresher` $\rightarrow$ `Lead`) và 3 vùng địa lý (`Hà Nội`, `TP.HCM`, `Đà Nẵng`), Top 15 kỹ năng, Heatmap tương quan Pearson/Phi $60 \times 60$.<br>• Thực hiện Gom cụm K-Means (Bước 2.3): khảo sát `Elbow` ($K=1..10$), `Silhouette Score` ($K=2..10$, đạt đỉnh `0.1603` tại $K=3$), giảm chiều `PCA` và định danh 3 chân dung nghề nghiệp.<br>• Khai phá Luật kết hợp Apriori (Bước 2.4): lọc `472` tập phổ biến, `440` luật theo `Support >= 0.05`, `Confidence >= 0.60`, `Lift > 1.2`, `Conviction` và bóc tách `32` luật nhiễu.<br>• Viết **Chương 3** và **Chương 4** của Báo cáo tổng kết. | • `TV2_EDA_Clustering_Apriori.ipynb`<br>• 12 Biểu đồ EDA, K-Means, PCA, Apriori<br>• Bảng hồ sơ tâm cụm & Bảng luật kết hợp<br>• Nội dung Chương 3 & Chương 4 | **33%** | *(Ký & ghi rõ họ tên)* |
| **3** | **Huỳnh Hữu Phước**<br>*(Senior Data Scientist — Thành viên 3)* | • Xây dựng mô hình Phân lớp dự báo khoảng lương (Bước 2.5): thiết kế thực nghiệm đối chứng giữa tập toàn bộ (`1.547` tin Imputed) và tập lương công bố thực tế không rò rỉ (`394` tin Leakage-Free).<br>• Khảo sát cắt tỉa cành `ccp_alpha` (Cost-Complexity Pruning) bằng 5-Fold Stratified Cross-Validation chống Overfitting; đối sánh 4 mô hình (`DT Overfit`, `DT Pruned ccp_alpha`, `Random Forest`, `Logistic Regression`).<br>• Đánh giá mô hình bằng `Confusion Matrix`, `Macro Precision/Recall/F1`, rút trích luật `IF-THEN`, phân tích `Feature Importance` và truy vết lỗi sai (Error Analysis).<br>• Viết **Chương 5**, **Chương 6**, hợp nhất `NhomXX_MiningPipeline.ipynb` & thiết kế Slide bảo vệ. | • `TV3_Classification_Decision_Tree.ipynb`<br>• `NhomXX_MiningPipeline.ipynb`<br>• `outputs/decision_tree.png` & `feature_importance.png`<br>• Nội dung Chương 5, Chương 6 & Slide | **33%** | *(Ký & ghi rõ họ tên)* |
| | **TỔNG CỘNG** | **Thực hiện trọn vẹn quy trình KDD đầu-cuối (End-to-End Pipeline)** | **Đủ 05 Sản phẩm nộp LMS** | **100%** | |

---

## CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI
*(Độ dài khuyến nghị: **2.0 trang** — Nguồn tham chiếu chính: Phần 2 của `BAO_CAO_THANH_VIEN_1.md`)*

### 1.1. Bối cảnh thực tiễn và Lý do chọn đề tài *(~0.7 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Sự bùng nổ của Chuyển đổi số dựa trên dữ liệu (*Data-driven Digital Transformation*) và Trí tuệ nhân tạo tạo sinh (*Generative AI / LLMs*) tại Việt Nam giai đoạn 2024–2026 khiến nhu cầu tuyển dụng nhân sự Data & AI tăng mạnh trong các ngành Ngân hàng, Fintech, Thương mại điện tử, Viễn thông.
   - Ba bài toán thực tiễn gây khó khăn cho sinh viên và người lao động:
     1. *Sự nhập nhằng về tên gọi vị trí (Role Ambiguity):* Ranh giới giữa Data Analyst, BI, Data Engineer, Data Scientist và AI Engineer ngày càng giao thoa.
     2. *Bất cân xứng thông tin về thu nhập (Salary Information Asymmetry):* Hơn 74% tin tuyển dụng tại Việt Nam ẩn mức lương dưới nhãn *"Thỏa thuận"*.
     3. *Sự dịch chuyển nhanh của Giỏ kỹ năng (Modern Data & AI Tech Stack):* Công cụ đơn lẻ (`Excel`, `SQL` cơ bản) không còn đủ; nhà tuyển dụng đòi hỏi tổ hợp kỹ năng đa nền tảng (`Cloud`, `Docker/Kubernetes`, `Spark/Airflow`, `LLM/GenAI`).
2. **Số liệu / Bảng biểu cần chèn:**
   - Số liệu tổng quan từ dự án: Khảo sát thực nghiệm trên **8.320 tin tuyển dụng CNTT thô**, trích lọc chuyên sâu **1.547 tin tuyển dụng ngành Data & AI** từ 4 sàn việc làm lớn nhất Việt Nam (`TopCV`, `ITviec`, `VietnamWorks`, `TopDev`).
3. **Gợi ý cách diễn giải ăn điểm tối đa:**
   - Nhấn mạnh tính **"Dữ liệu sống thực tế (Real-world Live Data)"** đối lập với các tập dữ liệu đồ chơi (Toy Datasets như Titanic, Iris hay dữ liệu Kaggle nước ngoài), khẳng định giá trị ứng dụng trực tiếp cho sinh viên CNTT Việt Nam.

### 1.2. Đối tượng nghiên cứu và Bộ từ khóa định vị mục tiêu (`DATA_KEYWORDS`) *(~0.6 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Xác định phạm vi nghiên cứu gồm **5 phân khúc nghề nghiệp** trong hệ sinh thái Data & AI: (1) `Data Analyst / BI`, (2) `Data Engineer / Big Data`, (3) `Data Scientist / AI & ML`, (4) `Database / Data Platform & Ops`, (5) `Data-Driven Software Engineer`.
   - Trình bày bộ **20 từ khóa định vị mục tiêu (`DATA_KEYWORDS`)** chia làm 2 nhóm: 12 từ khóa tên vị trí (`DATA_ROLE_KEYWORDS`) và 8 từ khóa kỹ năng cốt lõi (`DATA_SKILL_KEYWORDS`).
2. **Số liệu / Bảng biểu cần chèn:**
   - **Bảng 1.1:** Danh mục 20 từ khóa định vị mục tiêu `DATA_KEYWORDS` (lấy từ `scraper.py` dòng `25–53` hoặc chạy lệnh `python scraper.py --list-keywords`).
3. **Gợi ý cách diễn giải ăn điểm tối đa:**
   - Giải thích tại sao phải kết hợp cả *Từ khóa Vị trí* lẫn *Từ khóa Kỹ năng*: nhiều doanh nghiệp tuyển `"Chuyên viên Phân tích Nghiệp vụ / Quản trị CSDL"` không chứa chữ `"Data"` trên tiêu đề nhưng trong JD lại đòi hỏi `SQL, PowerBI, Python, Spark, ETL` rất sâu.

### 1.3. Câu hỏi nghiên cứu và Mục tiêu của quy trình KDD *(~0.7 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Phát biểu **4 Câu hỏi nghiên cứu cốt lõi (Research Questions - RQ1 đến RQ4)** gắn chặt với 4 bước khai phá ở Giai đoạn 2:
     - **RQ1 (EDA):** Mặt bằng lương thực tế (`394` tin công bố) phân hóa như thế nào giữa 5 nhóm ngành Data, 5 cấp bậc (`Fresher` $\rightarrow$ `Lead`) và 3 vùng kinh tế (`Hà Nội`, `TP.HCM`, `Đà Nẵng`)?
     - **RQ2 (Clustering):** Nếu bỏ qua chức danh trên tiêu đề, các yêu cầu kỹ năng tự nhiên gom thành những cụm chân dung nghề nghiệp (Job Personas) nào trong không gian 60 chiều?
     - **RQ3 (Association Rules):** Những tổ hợp kỹ năng nào đồng xuất hiện mạnh nhất theo `Support`, `Confidence`, `Lift > 1.2` và `Conviction`? Đâu là các "luật nhiễu / bẫy độ tin cậy"?
     - **RQ4 (Classification):** Có thể dự báo khoảng lương (`Dưới 15M`, `15M - 30M`, `Trên 30M`) từ hồ sơ kỹ năng và số năm kinh nghiệm bằng `Decision Tree` (kèm cắt tỉa `ccp_alpha`) hay không, và làm thế nào để kiểm soát rò rỉ dữ liệu (*Data Leakage*) khi 74.5% tin ẩn lương?
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Hình 1.1:** Sơ đồ tổng thể quy trình KDD 5 bước của nhóm (vẽ bằng Mermaid hoặc khối quy trình từ *Web Scraping* $\rightarrow$ *Regex Cleaning & One-Hot* $\rightarrow$ *EDA / K-Means / Apriori / Decision Tree* $\rightarrow$ *Tri thức & Khuyến nghị*).

---

## CHƯƠNG 2: THU THẬP VÀ TIỀN XỬ LÝ DỮ LIỆU
*(Độ dài khuyến nghị: **4.0 trang** — Nguồn tham chiếu chính: `scraper.py`, `crawlers/`, `step_01_export_raw_csv.py`, `step_02_clean_data.py`, `TV1_Data_Cleaning_Pipeline.ipynb`)*

### 2.1. Đặc tả Kiến trúc Công cụ Cào dữ liệu (`crawlers/` & `scraper.py`) *(~1.2 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Giải thích kiến trúc **Hybrid Web Scraping** kết hợp:
     - `Playwright` (`crawlers/browser.py` dòng `18–59`): Khởi chạy Chromium/Chrome với cờ `--disable-blink-features=AutomationControlled` và script ẩn `navigator.webdriver` để vượt tường lửa chống bot cơ bản.
     - `BeautifulSoup4 + lxml` (`itviec.py`, `topcv.py`, `topdev.py`): Phân tích cây DOM sau khi JavaScript đã render hoàn chỉnh.
     - `AJAX JSON API` (`vietnamworks.py` dòng `23–62, 119–138`): Gửi POST request trực tiếp tới `https://ms.vietnamworks.com/job-search/v1.0/search` lấy JSON gốc.
   - Trình bày **3 kỹ thuật bắt buộc (Chốt chặn Code Audit)**:
     1. *Logic phân trang (`Pagination`):* Vòng lặp `for page_num in range(1, pages + 1)` kèm cơ chế dừng sớm khi hết tin (`if not rows: break`).
     2. *Vượt cơ chế tải động (`Wait for DOM & Infinite Scroll`):* Hàm `simulate_infinite_scroll(page, steps=3, scroll_pause=0.7)` trong `crawlers/base.py` (dòng `64–83`) cuộn trang 3 nhịp kích hoạt `IntersectionObserver`.
     3. *Thời gian chờ ngẫu nhiên (`Robots.txt Etiquette`):* Hàm `polite_sleep(min_sec=1.5, max_sec=3.5)` dùng `random.uniform` trong `crawlers/base.py` (dòng `48–62`).
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Hình 2.1:** Sơ đồ kiến trúc đường ống thu thập dữ liệu đa nguồn (Mermaid diagram tại dòng `69–79` file `BAO_CAO_THANH_VIEN_1.md`).
   - Trích dẫn ngắn (5–8 dòng) đoạn code hàm `polite_sleep()` và `simulate_infinite_scroll()` từ `crawlers/base.py`.

### 2.2. Chiến lược Lọc 2 Tầng, Khử trùng & Thống kê Bộ dữ liệu Thô (`data/raw_data.csv`) *(~0.8 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Quy trình xử lý trong `step_01_export_raw_csv.py`:
     - Đọc **8.320 bản ghi gốc** từ 4 tệp `.jsonl` (`topcv.jsonl`: 3.234; `topdev.jsonl`: 3.175; `vietnamworks.jsonl`: 1.061; `itviec.jsonl`: 850).
     - Khử trùng 2 cấp: Theo `URL_Goc` (`job_url`, ưu tiên giữ bản ghi có `description` dài hơn) và theo khóa phức hợp `(Site, Cong_Ty, Tieu_De)`.
     - Chiến lược lọc 2 tầng ngành Data & AI: **Tầng 1 (Core Data/BI/AI/ML/DB Roles)** thu được `760` tin; **Tầng 2 (Data-Intensive Multi-Skill Roles >= 2 kỹ năng dữ liệu cốt lõi)** thu được `787` tin; kết hợp bộ lọc loại trừ tin phi kỹ thuật (`NON_DATA_EXCLUSION_TITLE_PATTERN`).
2. **Số liệu / Bảng biểu cần chèn:**
   - **Bảng 2.1:** Thống kê phân bổ **1.547 tin tuyển dụng** trong `data/raw_data.csv` theo 4 nguồn (`TopCV`: `640` tin - `41.4%`; `ITviec`: `439` tin - `28.4%`; `VietnamWorks`: `397` tin - `25.7%`; `TopDev`: `71` tin - `4.6%`) — lấy từ output **Cell 1 của `TV1_Data_Cleaning_Pipeline.ipynb`**.
   - **Bảng 2.2:** Đặc tả Schema 11 cột của `data/raw_data.csv` (nhấn mạnh 2 cột chốt chặn Data Audit là `URL_Goc` và `Timestamp`).

### 2.3. Chuẩn hóa Mức lương bằng Biểu thức Chính quy (Regex) & Chiến lược Điền khuyết Kép *(~1.0 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Giải phẫu hàm `_extract_salary_from_string()` tại `step_02_clean_data.py` (dòng `144–245`):
     - Quy đổi đồng nhất ngoại tệ `USD` sang **Triệu VNĐ/tháng** theo tỷ giá `1 USD = 0.0254 Triệu VNĐ`.
     - **Xử lý chu kỳ trả lương theo năm (`/năm`, `/year`):** Tự động phát hiện bằng Regex `r"(/\s*năm|\btheo\s+năm\b|/\s*year|\bper\s+year\b|\bannually\b)"` để chia `12.0` (ví dụ khôi phục 3 tin lương năm và chuẩn hóa đúng bản ghi `DATA_1248: "$ 8,000-9,000 /năm"` thành `16.93M – 19.05M/tháng`).
     - Ba mẫu Regex tách lương: **Mẫu 1 (Khoảng `Min - Max`)**, **Mẫu 2 (Cận trên `Up to / Tới` $\rightarrow \text{Min} = \max(0.7 \times \text{Max}, 3.0)$)**, **Mẫu 3 (Cận dưới `Từ / Over` $\rightarrow \text{Max} = 1.3 \times \text{Min}$)**.
     - Chặn biên ngoại lai (`MIN_VALID_SALARY_M = 3.0`, `MAX_VALID_SALARY_M = 250.0`) để loại bỏ bẫy lương ảo `"$ 1-1 /tháng"` trên VietnamWorks.
   - Trình bày **Chiến lược Điền khuyết Kép (Dual Handling Strategy)**:
     - Giữ nguyên `NaN` ở cột `Luong_Trung_Binh` và `Khoang_Luong_Thuc` cho `1.153` tin `"Thoa_Thuan"` (`74.53%`) để phục vụ EDA và Phân lớp Leakage-Free trên đúng **`394` tin `"Co_Cong_Bo"` (`25.47%`)**.
     - Tạo cột `Luong_Trung_Binh_Imputed` điền khuyết bằng `Median` theo cặp `(Nhom_Nganh_Data, Cap_Bac)`.
2. **Số liệu / Bảng biểu cần chèn:**
   - **Bảng 2.3:** Bảng ví dụ 6 chuỗi `Muc_Luong_Goc` phức tạp thực tế trong dữ liệu (`"20 - 40 triệu"`, `"$ 1,000-1,500 /tháng"`, `"Tới $ 1,700 /tháng"`, `"$ 8,000-9,000 /năm"`, `"$ 1-1 /tháng"`, `"Thoả thuận"`) và kết quả sau khi qua hàm Regex (`Luong_Min`, `Luong_Max`, `Luong_Trung_Binh`, `Trang_Thai_Luong`) — lấy từ **Cell 5 của `TV1_Data_Cleaning_Pipeline.ipynb`**.

### 2.4. Chuẩn hóa Địa điểm, Kinh nghiệm, Cấp bậc & Trích xuất Ma trận One-Hot 60 Kỹ năng *(~1.0 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Chuẩn hóa `Dia_Diem_Chuan` (5 nhóm: `Hà Nội`, `TP.HCM`, `Đà Nẵng`, `Remote`, `Khác`), `Mo_Hinh_Lam_Viec` (`On-site`, `Hybrid`, `Remote`), và hàm `extract_experience_and_seniority()` rút trích `So_Nam_Kinh_Nghiem` $\rightarrow$ ánh xạ vào 5 bậc `Cap_Bac` (`Fresher`, `Junior`, `Middle`, `Senior`, `Lead`), nêu rõ kỹ thuật xử lý chuỗi `"Experienced (non-manager)"`.
   - Làm sạch văn bản JD (`clean_jd_text()`: xóa HTML, URL, ký tự đặc biệt, lọc `STOP_WORDS` Việt/Anh) và thiết kế **Từ điển 60 Kỹ năng chuyên sâu ngành Data chia làm 6 nhóm** (`step_02_clean_data.py` dòng `510–660`).
   - Nhấn mạnh **3 kỹ thuật Regex chống bắt nhầm (Zero False-Positives)**:
     1. *Contextual Matching cho ngôn ngữ `R`:* Chỉ khớp khi đi kèm `Python/R`, `R/SQL`, `RStudio`, `R programming`, `ggplot2`, `tidyverse` (`22` tin - `1.42%`).
     2. *Negative Lookahead cho `Java`:* `\bjava\b(?!\s*script)` để không bắt nhầm `JavaScript`.
     3. *Tách biệt `SQL` và `NoSQL`:* Không đưa `nosql` vào biểu thức `Skill_SQL` để tránh 41 ca dương tính giả.
2. **Số liệu / Bảng biểu cần chèn:**
   - **Bảng 2.4:** Bảng tổng hợp 6 nhóm × 60 kỹ năng (`Skill_*`) và cấu trúc 86 cột của tệp đầu ra `data/clean_data.csv` — lấy từ **Cell 7 & Cell 9 của `TV1_Data_Cleaning_Pipeline.ipynb`**.

---

## CHƯƠNG 3: PHÂN TÍCH KHÁM PHÁ DỮ LIỆU (EDA & VISUAL ANALYTICS)
*(Độ dài khuyến nghị: **3.5 trang** — Nguồn tham chiếu chính: Phần 2.2 của `TV2_EDA_Clustering_Apriori.ipynb` và `NhomXX_MiningPipeline.ipynb`)*

### 3.1. Phân phối Mức lương Thực tế và So sánh giữa 5 Phân khúc Ngành Data *(~1.0 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Thống kê mô tả trên **394 tin có công bố lương (`25.47%`)**: `Mean = 27.66 triệu/tháng`, `Median = 25.50 triệu/tháng`, `Std = 13.80 triệu/tháng`, `Min = 3.50 triệu`, `Q1 = 19.00 triệu`, `Q3 = 35.00 triệu`, `Max = 130.00 triệu` (`IQR = Q3 - Q1 = 16.00 triệu`, ngưỡng ngoại lai trên `Q3 + 1.5 * IQR = 59.00 triệu`).
   - So sánh mặt bằng lương giữa 5 phân khúc ngành Data (`Nhom_Nganh_Data`).
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Bảng 3.1:** Phân bố số lượng tin và mức lương thực tế (`Mean`, `Median`) theo 5 nhóm ngành Data — lấy từ **Cell 5 của `TV1_Data_Cleaning_Pipeline.ipynb`** & **Cell 5, Cell 6 của `TV2_EDA_Clustering_Apriori.ipynb`**:
     - `Data Scientist / AI & ML` (`308` tin, `70` có lương): **`Mean = 30.95M`**, `Median = 27.50M` (Dẫn đầu về lương trung bình).
     - `Data Engineer / Big Data` (`285` tin, `75` có lương): `Mean = 30.84M`, **`Median = 30.00M`** (Dẫn đầu tuyệt đối về lương trung vị!).
     - `Database / Data Platform & Ops` (`528` tin, `123` có lương): `Mean = 26.39M`, `Median = 25.00M`.
     - `Data Analyst / BI` (`296` tin, `85` có lương): `Mean = 26.25M`, `Median = 25.00M`.
     - `Data-Driven Software Engineer` (`130` tin, `41` có lương): `Mean = 22.94M`, `Median = 22.50M`.
   - **Hình 3.1:** Biểu đồ Histogram & KDE phân phối mức lương ngành Data có đường `Mean (27.66M)` và `Median (25.50M)` (**Cell 9 của `TV2_EDA_Clustering_Apriori.ipynb`**).
   - **Hình 3.2:** Biểu đồ Boxplot so sánh phân phối mức lương giữa 5 nhóm ngành Data (**Cell 12 của `TV2_EDA_Clustering_Apriori.ipynb`**).
3. **Gợi ý cách diễn giải ăn điểm tối đa:**
   - Giải thích tại sao `Data Engineer / Big Data` có `Median = 30.00M` cao hơn cả `Data Scientist / AI & ML` (`Median = 27.50M`), trong khi `Data Scientist / AI & ML` lại có `Mean = 30.95M` cao hơn: Nhóm `Data Engineer` đòi hỏi kỹ năng hạ tầng thực chiến nên ít tuyển Intern/Fresher lương thấp (sàn lương cao và ổn định), còn nhóm `AI & ML` có độ phân tán rộng (từ thực tập sinh gán nhãn/AI 3.5M–5M cho tới chuyên gia AI Engineer 90M–170M kéo `Mean` lên cao).

### 3.2. Phân tích Mức lương theo 5 Cấp bậc (`Cap_Bac`) — *Tiêu chí bắt buộc Bước 2.2* *(~0.8 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Phân tích bước nhảy thu nhập qua 5 nấc thang thâm niên: `Fresher` $\rightarrow$ `Junior` $\rightarrow$ `Middle` $\rightarrow$ `Senior` $\rightarrow$ `Lead`.
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Bảng 3.2 & Hình 3.3:** Bảng thống kê (`So_Tin, Mean, Median, Q1, Q3, Min, Max`) và Biểu đồ Boxplot mức lương thực tế theo 5 Cấp bậc — lấy trực tiếp từ **Cell 14 của `TV2_EDA_Clustering_Apriori.ipynb`**:
     - `Fresher` (`n = 55`): `Mean = 14.80M` \| `Median = 11.00M` (`Q1 = 7.38M`, `Q3 = 19.50M`).
     - `Junior` (`n = 46`): `Mean = 18.73M` \| `Median = 17.50M` (`Q1 = 15.00M`, `Q3 = 20.00M`).
     - `Middle` (`n = 156`): `Mean = 28.69M` \| `Median = 25.50M` (`Q1 = 21.00M`, `Q3 = 34.51M`).
     - `Senior` (`n = 51`): `Mean = 35.97M` \| `Median = 35.00M` (`Q1 = 30.88M`, `Q3 = 40.00M`).
     - `Lead` (`n = 86`): `Mean = 33.85M` \| `Median = 30.00M` (`Q1 = 24.25M`, `Q3 = 42.50M`).
3. **Gợi ý cách diễn giải ăn điểm tối đa:**
   - Chỉ ra **"Bước nhảy giá trị lớn nhất"** nằm ở giai đoạn từ `Junior` (`Median 17.50M`) lên `Middle` (`Median 25.50M`, tăng `+45.7%`) và từ `Middle` lên `Senior` (`Median 35.00M`, tăng `+37.3%`).
   - Giải thích hiện tượng thú vị tại sao `Lead` có `Median = 30.00M` thấp hơn `Senior` (`35.00M`) trên tập tin công bố lương: Các vị trí `Lead / Manager / Architect` lương khủng (`>50M–100M`) tại các tập đoàn lớn gần như đều ẩn lương (`Thỏa thuận`), trong khi một số vị trí mang danh `"Annotation Leader / Trưởng nhóm xử lý dữ liệu"` tại các công ty gia công dữ liệu công bố mức lương `10–15M` kéo trung vị của `Lead` xuống! (Điểm này liên kết cực kỳ chặt chẽ với phần Truy vết lỗi sai ở Chương 5!).

### 3.3. Top 15 Kỹ năng "Hot" nhất & Ma trận Tương quan Kỹ năng ($60 \times 60$) *(~1.0 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Thống kê tần suất 15 kỹ năng được săn đón nhiều nhất trên `1.547` tin tuyển dụng.
   - Phân tích Ma trận tương quan Pearson (hệ số $\phi$ cho biến nhị phân) kích thước $60 \times 60$ và Top 10 cặp kỹ năng đồng xuất hiện tuyến tính mạnh nhất.
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Bảng 3.3 & Hình 3.4:** Bảng và Biểu đồ Barplot **Top 15 kỹ năng được săn đón nhiều nhất** — lấy từ **Cell 16 của `TV2_EDA_Clustering_Apriori.ipynb`** (`SQL`: `901` tin - `58.24%`; `Python`: `553` tin - `35.75%`; `English`: `543` tin - `35.10%`; `Communication`: `509` tin - `32.90%`; `CI_CD`: `422` tin - `27.28%`; `PostgreSQL`: `357` tin - `23.08%`; `Git`: `344` tin - `22.24%`; `Docker`: `335` tin - `21.65%`; `Problem_Solving`: `322` tin - `20.81%`; `Data_Governance`: `305` tin - `19.72%`; `Cloud_AWS`: `301` tin - `19.46%`...).
   - **Hình 3.5 & Bảng 3.4:** Heatmap tương quan 60 kỹ năng (**Cell 21**) và Bảng Top 10 cặp kỹ năng tương quan dương cao nhất (**Cell 23 của `TV2_EDA_Clustering_Apriori.ipynb`**): `PyTorch - TensorFlow` (`r = 0.8691`), `NumPy - Scikit_Learn` (`r = 0.7284`), `Pandas - NumPy` (`r = 0.7233`), `Docker - Kubernetes` (`r = 0.6657`), `Deep_Learning - TensorFlow` (`r = 0.6569`).

### 3.4. So sánh Nhu cầu & Đãi ngộ theo Khu vực Địa lý (`Hà Nội vs. TP.HCM vs. Đà Nẵng`) và Mô hình Làm việc *(~0.7 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Đối sánh quy mô tuyển dụng và mức lương công bố giữa 3 trung tâm kinh tế: `Hà Nội`, `TP.HCM` và `Đà Nẵng`.
   - Phân tích cơ cấu mô hình làm việc (`On-site`, `Hybrid`, `Remote`) trong ngành Data.
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Bảng 3.5 & Hình 3.6:** Bảng tổng hợp và Biểu đồ đôi (Barplot số lượng tin + Boxplot mức lương) giữa `Hà Nội`, `TP.HCM`, `Đà Nẵng` — lấy từ **Cell 18 của `TV2_EDA_Clustering_Apriori.ipynb`**:
     - `Hà Nội`: `869` tin (`56.17%` thị phần), `289` tin có lương, **`Mean = 28.27M`**, **`Median = 25.50M`** (`Q1 = 20.00M`, `Q3 = 35.00M`).
     - `TP.HCM`: `561` tin (`36.26%` thị phần), `85` tin có lương, **`Mean = 25.78M`**, **`Median = 24.15M`** (`Q1 = 16.50M`, `Q3 = 32.50M`).
     - `Đà Nẵng`: `21` tin (`1.36%` thị phần), `4` tin có lương, **`Mean = 14.80M`**, **`Median = 15.35M`** (`Q1 = 9.88M`, `Q3 = 20.27M`).
   - **Hình 3.7 & Hình 3.8:** Biểu đồ tròn tỷ lệ `Mo_Hinh_Lam_Viec` (`On-site`: `1.401` tin - `90.56%`; `Hybrid`: `102` tin - `6.59%`; `Remote`: `44` tin - `2.84%`) và Biểu đồ cột chồng 100% theo 5 nhóm ngành (**Cell 29 & Cell 30 của `TV2_EDA_Clustering_Apriori.ipynb`**).
3. **Gợi ý cách diễn giải ăn điểm tối đa:**
   - Giải thích tại sao Hà Nội chiếm tới `56.17%` số tin Data và có mức lương trung vị (`25.50M`) nhỉnh hơn TP.HCM (`24.15M`): Hội sở chính (Headquarters) của hầu hết các Ngân hàng TMCP lớn (Vietcombank, Techcombank, MB, VPBank, BIDV, SeABank, MSB...) và các Tập đoàn Viễn thông/Công nghệ (Viettel, VNPT, FPT, CMC) đều đặt tại Hà Nội, nơi tập trung các trung tâm Dữ liệu lớn (Data Center / Core Banking / AI Center).

---

## CHƯƠNG 4: GOM CỤM PHÂN KHÚC THỊ TRƯỜNG & KHAI PHÁ LUẬT KẾT HỢP KỸ NĂNG
*(Độ dài khuyến nghị: **4.0 trang** — Nguồn tham chiếu chính: Phần 2.3 & 2.4 của `TV2_EDA_Clustering_Apriori.ipynb`)*

### 4.1. Gom cụm Phân khúc Thị trường bằng Thuật toán K-Means (Bước 2.3) *(~2.0 trang)*

#### 4.1.1. Biểu diễn Không gian Đặc trưng và Biện luận Số cụm Tối ưu $K$ bằng Elbow & Silhouette Score
1. **Nội dung cốt lõi cần viết:**
   - Ma trận đầu vào $X \in \{0, 1\}^{1547 \times 60}$, chuẩn hóa Z-score bằng `StandardScaler` ($z = \frac{x - \mu}{\sigma}$, tại $K=1$ tổng phương sai $WCSS = 1547 \times 60 = 92.820$).
   - Trình bày công thức tối ưu $WCSS$ và công thức `Silhouette Score` $s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}$.
   - Biện luận chọn **$K = 3$**: Đường cong `WCSS` giảm mạnh từ $K=1$ (`92.820`) xuống $K=3$ (`80.764`), đồng thời **`Silhouette Score` đạt cực đại toàn cục tại $K = 3$ với `0.1603`** (cao hơn tất cả các giá trị $K \in \{2, 4, 5, \dots, 10\}$).
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Bảng 4.1:** Bảng khảo sát `WCSS` và `Silhouette Score` cho $K = 2 \dots 10$ — lấy từ **Cell 40 & Cell 41 của `TV2_EDA_Clustering_Apriori.ipynb`** ($K=2$: `0.1541`; **$K=3$: `0.1603`**; $K=4$: `0.1495`; $K=5$: `0.1523`; $K=6$: `0.1497`...).
   - **Hình 4.1 & Hình 4.2:** Biểu đồ `Elbow Method` (**Cell 37**) và Biểu đồ `Silhouette Score theo K` (**Cell 40**).

#### 4.1.2. Trực quan hóa PCA 2D và Định danh 3 Chân dung Nghề nghiệp (Job Personas)
1. **Nội dung cốt lõi cần viết:**
   - Chiếu dữ liệu 60 chiều và 3 tâm cụm (Centroids) xuống mặt phẳng 2 thành phần chính `PC1` và `PC2` bằng `PCA(n_components=2)` (giữ lại `17.29%` phương sai).
   - Phân tích hồ sơ kỹ năng đặc trưng (`cluster_profiles`) và bảng đối chiếu chéo (`pd.crosstab`) với nhãn ngành gốc để định danh **3 Chân dung Tuyển dụng**:
     1. **Cụm 0 — *Chân dung Kỹ sư Dữ liệu, CSDL & Hạ tầng Cloud-DevOps (`Data Engineering & Infrastructure` — `476` tin, chiếm `30.77%`)*:** Hội tụ mật độ kỹ năng kỹ thuật hệ thống rất cao: `SQL (80.67%)`, `CI/CD (65.76%)`, `Docker (60.08%)`, `PostgreSQL (54.62%)`, `Git (52.94%)`, `English (50.00%)`, `Kubernetes (47.69%)`, `Cloud_AWS (44.12%)`, `Java (42.23%)`, `MongoDB (42.23%)`, `Python (42.02%)`, `Kafka (37.18%)`. Khi đối chiếu với nhãn ngành gốc, **87.60%** tin trong cụm này thuộc `Database / Data Platform & Ops (56.72%)` và `Data Engineer / Big Data (30.88%)`.
     2. **Cụm 1 — *Chân dung Kỹ sư Nghiên cứu AI, Học máy & Học sâu (`AI & Machine Learning` — `62` tin, chiếm `4.01%`)*:** Cụm tinh hoa có độ thuần khiết tuyệt đối (**`100.0%` thuộc phân khúc `Data Scientist / AI & ML`**) và tách biệt rõ nhất trên trục `PC2` của biểu đồ PCA: `Machine_Learning (91.94%)`, `Python (85.48%)`, `Deep_Learning (85.48%)`, `PyTorch (72.58%)`, `Computer_Vision (70.97%)`, `TensorFlow (64.52%)`, `LLM_GenAI (59.68%)`, `NLP (53.23%)`, `MLOps (35.48%)`.
     3. **Cụm 2 — *Chân dung Chuyên viên Phân tích Dữ liệu Tổng hợp & BI (`General Data & Analytics / BI` — `1.009` tin, chiếm `65.22%`)*:** Đại diện cho số đông thị trường tuyển dụng Data/BI/BA với bộ kỹ năng nền tảng và nghiệp vụ: `SQL (49.45%)`, `Python (29.73%)`, `Communication (29.14%)`, `English (28.54%)`, `Data_Storytelling (21.41%)`, `Data_Governance (21.11%)`, `PowerBI (16.35%)`, `Problem_Solving (16.35%)`, `Statistics (12.69%)`, `Excel (10.90%)`.
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Hình 4.3:** Biểu đồ cột phân bố quy mô 3 cụm nghề nghiệp (**Cell 45 của `TV2_EDA_Clustering_Apriori.ipynb`**).
   - **Hình 4.4:** Biểu đồ Scatter Plot trực quan hóa 3 cụm và tâm cụm (dấu `X` đen) trên mặt phẳng `PCA 2D` (**Cell 48**).
   - **Hình 4.5 & Bảng 4.2:** Biểu đồ 3 khung (3-panel horizontal barplot) **Top 10 kỹ năng phổ biến nhất của từng cụm** (**Cell 52**) và Bảng Crosstab thành phần nhóm ngành gốc trong từng cụm (**Cell 53**).

---

### 4.2. Khai phá Luật kết hợp Kỹ năng bằng Thuật toán Apriori (Bước 2.4) *(~2.0 trang)*

#### 4.2.1. Thiết lập Mô hình Giỏ Kỹ năng và Công thức 4 Độ đo (`Support`, `Confidence`, `Lift`, `Conviction`)
1. **Nội dung cốt lõi cần viết:**
   - Biểu diễn mỗi tin tuyển dụng là một giao dịch (Transaction) trên 60 mục kỹ năng Boolean (`True/False`).
   - Trình bày công thức toán học và ý nghĩa của **4 độ đo bắt buộc theo Rubric**:
     $$\text{Support}(A \Rightarrow B) = P(A \cup B), \quad \text{Confidence}(A \Rightarrow B) = P(B \mid A) = \frac{P(A \cup B)}{P(A)}$$
     $$\text{Lift}(A \Rightarrow B) = \frac{\text{Confidence}(A \Rightarrow B)}{P(B)}, \quad \text{Conviction}(A \Rightarrow B) = \frac{1 - P(B)}{1 - \text{Confidence}(A \Rightarrow B)}$$
   - Ngưỡng sàng lọc thực nghiệm: `min_support = 0.05` (tối thiểu `78/1.547` tin), `min_confidence = 0.60` (`60%`), và `Lift > 1.2`.
   - Kết quả tổng quan: Khai phá được **`472` tập kỹ năng phổ biến (`frequent_itemsets`)**, sinh ra **`440` luật kết hợp** có `Confidence >= 60%`, trong đó lọc được **`408` luật kết hợp mạnh (`Lift > 1.2`, chiếm `92.73%`)** và nhận diện **`32` luật nhiễu (`Lift <= 1.2`)**.

#### 4.2.2. Top Luật Kết hợp Kỹ năng Giá trị Cao & Phát hiện "Bẫy Độ tin cậy" (Luật Nhiễu)
1. **Nội dung cốt lõi cần viết:**
   - Phân tích các nhóm luật mạnh nhất (`Lift` từ `4.35` đến `6.80`, `Conviction` từ `2.30` đến `86.99`):
     - *Xu hướng Multi-Cloud:* `{Cloud_AWS, Cloud_Azure} => {Cloud_GCP}` (`Support = 6.92%`, `Confidence = 74.31%`, **`Lift = 6.8018`**, `Conviction = 3.4667`) và `{Cloud_Azure, Cloud_GCP} => {Cloud_AWS}` (`Confidence = 99.07%`, `Lift = 5.0919`, **`Conviction = 86.9864`** — gần như tất định!).
     - *Xu hướng Container & CSDL hiện đại:* `{Kubernetes, PostgreSQL} => {Docker, SQL}` (`Support = 6.46%`, `Confidence = 84.75%`, `Lift = 5.4626`, `Conviction = 5.5385`).
   - **Phân tích các Luật gây nhiễu / Bẫy độ tin cậy (Rubric 2.4 Requirement):**
     - Chỉ ra 32 luật có `Confidence` rất cao (`68% – 70%`) nhưng `Lift <= 1.2` và `Conviction` rất thấp (`~1.32 – 1.38`), điển hình như:
       - `{Communication, English} => {SQL}` (`Support = 13.64%`, `Confidence = 68.73%`, nhưng **`Lift = 1.1801 <= 1.2`**, `Conviction = 1.3354`).
       - `{Data_Storytelling} => {SQL}` (`Support = 11.70%`, `Confidence = 68.56%`, **`Lift = 1.1772 <= 1.2`**, `Conviction = 1.3282`).
     - *Giải thích sâu sắc:* Tại sao `Confidence` gần 70% mà vẫn là luật nhiễu? Bởi vì bản thân kỹ năng `{SQL}` ở vế phải đã xuất hiện trong **`58.24%`** toàn bộ tin tuyển dụng (`P(B) = 0.5824`). Do đó, việc biết thêm `{English, Communication}` chỉ nâng xác suất gặp `{SQL}` lên `1.18` lần (gần như độc lập thống kê!). Nếu không lọc bằng `Lift > 1.2` và `Conviction`, hệ thống gợi ý kỹ năng sẽ rơi vào "bẫy độ tin cậy" khi luôn khuyên mọi ứng viên học `SQL` từ những kỹ năng mềm không liên quan.
   - **Kiểm chứng 2 luật giả thuyết của đề bài:**
     - `{Python, SQL} => {Machine_Learning}`: `Support = 5.69%`, `Confidence = 24.58%`, **`Lift = 1.5521 (> 1.2)`**, `Conviction = 1.1159` (Có liên kết dương thực sự với `Lift = 1.55`, nhưng chỉ 1/4 số tin biết `Python + SQL` là tuyển `Machine Learning` vì `Python + SQL` còn dùng rất nhiều cho `Data Engineering` và `Data Analytics`).
     - `{Docker, Kubernetes} => {Cloud_AWS}`: `Support = 6.53%`, `Confidence = 47.20%`, **`Lift = 2.4257`**, `Conviction = 1.5253` (Mối liên kết cực mạnh gấp `2.43` lần ngẫu nhiên, dù `Confidence = 47.2%` thấp hơn ngưỡng cắt cứng `60%`).
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Bảng 4.3:** Top 15 Luật kết hợp mạnh nhất kèm đủ 4 chỉ số `Support, Confidence, Lift, Conviction` (**Cell 62 & Cell 63 của `TV2_EDA_Clustering_Apriori.ipynb`**).
   - **Bảng 4.4:** Bảng 10 Luật nhiễu / Bẫy độ tin cậy (`Confidence >= 60%` nhưng `Lift <= 1.2`) và Bảng kiểm chứng 2 luật đề bài (**Cell 62 & Cell 72**).
   - **Hình 4.6 & Hình 4.7:** Biểu đồ Barplot Top 10 luật có `Lift` cao nhất (**Cell 65**) và Biểu đồ Scatter Plot phân bố `Support vs. Confidence` theo `Lift` (**Cell 67**).

---

## CHƯƠNG 5: XÂY DỰNG MÔ HÌNH PHÂN LỚP & DỰ BÁO KHOẢNG LƯƠNG
*(Độ dài khuyến nghị: **3.5 trang** — Nguồn tham chiếu chính: `TV3_Classification_Decision_Tree.ipynb`)*

### 5.1. Thiết lập Bài toán Phân lớp & Phát hiện Hiện tượng Rò rỉ Dữ liệu qua Điền khuyết (Target Leakage Discovery) *(~1.0 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Phát biểu bài toán: Dự báo biến mục tiêu 3 lớp khoảng lương (`Dưới 15M`, `15M - 30M`, `Trên 30M`) từ hồ sơ kỹ năng công nghệ (`60` cột `Skill_*`) và thâm niên (`So_Nam_Kinh_Nghiem`).
   - Trình bày **Thiết kế Thực nghiệm Đối chứng 2 Kịch bản (Dual-Scenario Experimental Design)** — điểm sáng học thuật đắt giá nhất của Chương 5:
     - **Kịch bản 1 (Toàn bộ tập dữ liệu sau điền khuyết — `n = 1.547` tin, Train `1.237` / Test `310`, `stratify=y`):** Dự đoán `Khoang_Luong_Phan_Lop`. Kết quả `Decision Tree (max_depth=5)` đạt `Test Accuracy = 81.94%`, `Macro F1 = 80.53%`, vượt xa `Random Forest` (`Test Accuracy = 76.77%`, `Macro F1 = 59.23%`), với `So_Nam_Kinh_Nghiem` chiếm tới **`76.85%` Feature Importance** và nút gốc cắt tại `So_Nam_Kinh_Nghiem <= 3.55`.
     - **Phân tích Phản biện Khoa học (Tại sao Kịch bản 1 đạt Accuracy >81%?):** Chỉ ra rằng trong `1.547` tin có `1.153` tin (`74.53%`) ẩn lương đã được điền khuyết theo `Median` của cặp `(Nhom_Nganh_Data, Cap_Bac)`, mà `Cap_Bac` lại là hàm tất định của `So_Nam_Kinh_Nghiem` (`Senior >= 4.0 năm` $\rightarrow 100\%$ điền lương `Trên 30M`). Do đó, mô hình ở Kịch bản 1 đã học ngược lại quy tắc điền khuyết (*Target Leakage via Imputation*)!
     - **Kịch bản 2 (Chuẩn Khoa học Dữ liệu — Chỉ huấn luyện và kiểm định trên `n = 394` tin công bố lương thực tế `Co_Cong_Bo`, hoàn toàn KHÔNG rò rỉ dữ liệu):** Chia `80% Train (315 tin)` / `20% Test (79 tin)` với `stratify=y_real` (`15M - 30M`: `200` tin; `Trên 30M`: `138` tin; `Dưới 15M`: `56` tin). Toàn bộ bộ biến đổi `ColumnTransformer` (`OneHotEncoder` cho `Dia_Diem_Chuan`, `Mo_Hinh_Lam_Viec` và `StandardScaler`) chỉ được `fit` trên tập `X_train` (`315 × 68`).
2. **Số liệu / Bảng biểu cần chèn:**
   - **Bảng 5.1:** So sánh cấu trúc mẫu và phân bố 3 lớp mục tiêu giữa Kịch bản 1 (`n = 1.547`) và Kịch bản 2 Leakage-Free (`n = 394`) — lấy từ **Cell 9 & Cell 47 của `TV3_Classification_Decision_Tree.ipynb`**.

### 5.2. Khảo sát Cắt tỉa Cành `ccp_alpha` (Cost-Complexity Pruning) Chống Overfitting *(~0.9 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Trình bày nguyên lý cắt tỉa hậu kiểm (**Minimal Cost-Complexity Pruning**) của Breiman: cực tiểu hóa hàm chi phí-độ phức tạp $R_\alpha(T) = R(T) + \alpha |T|$, trong đó $|T|$ là số nút lá và $\alpha \ge 0$ (`ccp_alpha`) là tham số phạt độ phức tạp.
   - Quy trình tìm `ccp_alpha` tối ưu trên tập Train (`315` tin lương thực):
     - Trích xuất đường dẫn cắt tỉa `cost_complexity_pruning_path(X_tr_enc, y_tr)`.
     - Chạy **5-Fold Stratified Cross-Validation** (`scoring="f1_macro"`) cho từng giá trị `ccp_alpha`.
     - Tìm được giá trị tối ưu **`best_ccp_alpha = 0.005442`**, tại đó cây quyết định thu gọn về **`Độ sâu = 8`, `Số nút lá = 29`**, đạt điểm `5-Fold CV Macro F1` cao nhất (`0.5717`).
   - Chứng minh hiệu quả chống Overfitting trên tập Test độc lập (`n_test = 79`):
     - Cây quyết định **chưa tỉa (`ccp_alpha = 0.0`)**: Học vẹt trên tập Train với `Train Accuracy = 93.33%`, `Train Macro F1 = 93.06%`, nhưng khi ra tập Test tụt xuống `Test Accuracy = 59.49%`, **`Test Macro F1 = 55.72%`** (chênh lệch Train–Test lên tới `37.34%`).
     - Cây quyết định **đã tỉa (`ccp_alpha = 0.005442`)**: `Train Macro F1` giảm hợp lý xuống `81.11%`, giúp **`Test Accuracy` tăng lên `62.03%`** và **`Test Macro F1` tăng vọt lên `60.53%` (`+4.81%` điểm Macro F1 so với cây chưa tỉa!)**.
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Hình 5.1 & Bảng 5.2:** Biểu đồ **Validation Curve (`Train Macro F1` vs. `5-Fold CV Macro F1` theo `ccp_alpha`)** và Bảng Top 8 cấu hình `ccp_alpha` — lấy trực tiếp từ **Cell 48 của `TV3_Classification_Decision_Tree.ipynb`**.

### 5.3. Đối sánh Đa Mô hình, Phân tích Ma trận Nhầm lẫn & Feature Importance *(~1.0 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Đối sánh 4 mô hình trên tập Test lương thực tế (`n_test = 79`) và đối chiếu với kết quả trên tập Imputed (`n_test = 310`):
     1. **`Decision Tree (Tỉa ccp_alpha = 0.0054)`:** Dẫn đầu tuyệt đối trên tập lương thực với **`Test Accuracy = 62.03%`**, **`Test Macro F1 = 60.53%`** (`Macro Precision = 59.48%`, `Macro Recall = 63.71%`).
     2. **`Random Forest (200 cây, class_weight="balanced")`:** Đạt `Test Accuracy = 54.43%`, `Test Macro F1 = 55.87%` (`Recall` lớp `Dưới 15M` đạt `72.73%`, lớp `Trên 30M` đạt `67.86%`).
     3. **`Decision Tree (Chưa tỉa - Overfit)`:** `Test Accuracy = 59.49%`, `Test Macro F1 = 55.72%`.
     4. **`Logistic Regression (StandardScaler)`:** `Test Accuracy = 43.04%`, `Test Macro F1 = 42.39%` (thấp nhất do ranh giới giữa kỹ năng, thâm niên và mức lương là phi tuyến tính phức tạp, mô hình tuyến tính không nắm bắt được các luật tương tác bậc cao như cây quyết định).
   - Phân tích cấu trúc Cây quyết định, `Feature Importance` và Top 10 kỹ năng dẫn tới mức lương `Trên 30M`:
     - Bên cạnh `So_Nam_Kinh_Nghiem`, các kỹ năng công nghệ có đóng góp phân nhánh mạnh nhất và tỷ lệ lương `Trên 30M` cao nhất là **`MLOps` (`72.41%` tin `>30M`)**, **`Hadoop` (`70.00%`)**, **`NLP` (`68.52%`)**, **`Deep_Learning` (`67.12%`)**, **`Machine_Learning` (`66.12%` — `162/245` tin)**, **`Airflow` (`62.24%`)**, **`TensorFlow` (`61.90%`)**, **`Computer_Vision` (`59.72%`)**, **`LLM_GenAI` (`58.53%` — `151/258` tin)**.
2. **Số liệu / Bảng biểu / Biểu đồ cần chèn:**
   - **Bảng 5.3:** Bảng đối sánh toàn diện 4 mô hình trên tập lương thực (`Train_Acc, Test_Acc, Train_Macro_F1, Test_Macro_F1, Test_Macro_Precision, Test_Macro_Recall`) — lấy từ **Cell 49 của `TV3_Classification_Decision_Tree.ipynb`** (kèm bảng Kịch bản 1 ở **Cell 27**).
   - **Hình 5.2:** Cặp biểu đồ Heatmap **Confusion Matrix** của `Decision Tree` và `Random Forest` (**Cell 30 & Cell 49**).
   - **Hình 5.3 & Hình 5.4:** Sơ đồ trực quan hóa Cây quyết định (`outputs/decision_tree.png` — **Cell 33**) và Biểu đồ ngang đôi Top 10 `Feature Importance` (`outputs/feature_importance.png` — **Cell 39**).
   - **Bảng 5.4:** Top 10 kỹ năng có tỷ lệ tin thuộc phân khúc lương `Trên 30M` cao nhất (**Cell 40**).

### 5.4. Truy vết Các Trường hợp Dự đoán Sai lệch Lớn (Error Analysis) — *Tiêu chí bắt buộc Bước 2.5* *(~0.6 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Trên tập Test lương thực tế (`79` tin), mô hình `Decision Tree (ccp_alpha = 0.0054)` dự đoán đúng `49/79` tin và dự đoán sai `30/79` tin. Trong 30 ca sai đó, có **28 ca (93.3%) là nhầm lẫn giữa hai khoảng lương liền kề** (`Dưới 15M` $\leftrightarrow$ `15M - 30M` hoặc `15M - 30M` $\leftrightarrow$ `Trên 30M` do các tin nằm sát ranh giới cắt ngưỡng `15.0M` và `30.0M`, ví dụ `DATA_0986` lương thực `15.00M` ngay đúng điểm biên bị đoán `Dưới 15M`, hay `DATA_0674` lương `32.50M` với 3 năm kinh nghiệm bị đoán `15M - 30M`).
   - **Truy vết định danh 02 ca sai lệch nghiêm trọng nhất (nhảy cóc 2 bậc từ `Dưới 15M` sang `Trên 30M`):**
     - Bản ghi **`DATA_0756`** (`Tieu_De = "Truong Nhom Gan Nhan Du Lieu Annotation Leader"`) và **`DATA_0499`** (`Tieu_De = "Trưởng Nhóm Gán Nhãn Dữ Liệu (Annotation Leader)"`):
     - *Nguyên nhân gốc rễ (Root Cause):* Cả 2 tin đều có từ khóa chức danh `"Trưởng Nhóm / Leader"` trên tiêu đề nên được chuẩn hóa thành `Cap_Bac = Lead` với `So_Nam_Kinh_Nghiem = 6.0 năm`. Tuy nhiên, đặc thù công việc **Gán nhãn dữ liệu (Data Annotation)** là lao động bán thủ công nên mức lương công bố thực tế chỉ là **`10 - 12 triệu` (`Luong_Trung_Binh = 11.0M` $\rightarrow$ nhãn thực tế `Dưới 15M`)**. Vì mô hình thấy `So_Nam_Kinh_Nghiem = 6.0 năm`, nhánh cây quyết định đã xếp nhầm 2 bản ghi này vào phân khúc `Trên 30M` (vốn là mức lương chuẩn của các Technical Lead / Data Engineer Lead).
2. **Số liệu / Bảng biểu cần chèn:**
   - **Bảng 5.5:** Bảng truy vết chi tiết các bản ghi dự đoán sai tiêu biểu (`Job_ID`, `Tieu_De`, `Cap_Bac`, `So_Nam_Kinh_Nghiem`, `Muc_Luong_Goc`, `Luong_Trung_Binh`, `Khoang_Luong_Thuc`, `Du_Doan_DT_Pruned`) — lấy trực tiếp từ **Cell 50 của `TV3_Classification_Decision_Tree.ipynb`**.
3. **Gợi ý cách diễn giải ăn điểm tối đa:**
   - Khẳng định việc truy vết ra 2 bản ghi `Annotation Leader` chứng minh mô hình không hề "đoán mò" mà phản ánh rất đúng quy luật chung của thị trường (6 năm kinh nghiệm / Lead $\rightarrow$ lương >30M), đồng thời gợi mở hướng cải tiến cho tương lai: tách riêng đặc trưng `Skill_Data_Annotation` ra khỏi nhóm `Data Scientist / AI & ML` để phân biệt rõ công việc gán nhãn dữ liệu với kỹ sư huấn luyện mô hình AI!

---

## CHƯƠNG 6: KẾT LUẬN VÀ KHUYẾN NGHỊ
*(Độ dài khuyến nghị: **2.0 trang** — Nguồn tham chiếu chính: Phần 5 của `BAO_CAO_THANH_VIEN_3.md` & Phần 4 của `BAO_CAO_THANH_VIEN_2.md`)*

### 6.1. Tổng kết Các Tri thức Khai phá được qua Quy trình KDD *(~0.7 trang)*
1. **Nội dung cốt lõi cần viết:**
   - Tóm lược câu trả lời định lượng cho 4 Câu hỏi nghiên cứu (RQ1 $\rightarrow$ RQ4) đã đặt ra ở Chương 1 bằng một bảng tổng hợp sắc gọn.
2. **Số liệu / Bảng biểu cần chèn:**
   - **Bảng 6.1:** Bảng đối chiếu 4 Câu hỏi nghiên cứu $\leftrightarrow$ Phương pháp KDD $\leftrightarrow$ Phát hiện định lượng cốt lõi (`1.547` tin, `394` tin có lương, `Mean = 27.66M`, `Median = 25.50M`; $K=3$ cụm với `Silhouette = 0.1603`; `408` luật kết hợp mạnh `Lift > 1.2`; `Decision Tree ccp_alpha = 0.0054` đạt `Test Macro F1 = 60.53%` trên tập Leakage-Free và `80.53%` trên tập toàn cục).

### 6.2. Khuyến nghị Thực tiễn cho Sinh viên Ngành CNTT & Khoa học Dữ liệu Chuẩn bị Ứng tuyển *(~0.8 trang)*
1. **Nội dung cốt lõi cần viết (Mỗi khuyến nghị đều gắn với con số chứng minh từ đồ án):**
   - **Khuyến nghị 1 — Trang bị "Cặp bài trùng bắt buộc" `SQL + Python + Tiếng Anh` ngay từ năm 2–3 đại học:** Dữ liệu thực chứng từ `1.547` tin cho thấy `SQL` chiếm **`58.24%` (`901` tin)**, `Python` chiếm **`35.75%` (`553` tin)** và `English` chiếm **`35.10%` (`543` tin)**. Đặc biệt, tổ hợp `{Python, SQL}` cùng xuất hiện trong **`23.14%` (`358` tin)** toàn ngành.
   - **Khuyến nghị 2 — Chiến lược chọn tổ hợp kỹ năng (Skill Combos) theo 3 Chân dung Nghề nghiệp (dựa trên kết quả K-Means & Apriori):**
     - *Hướng 1 — Data Analyst / BI (Cụm 2 - `65.22%` thị phần, lương trung vị `25.00M`):* Học chắc `SQL` + `PowerBI (16.35%)` (ưu tiên hơn `Tableau 5.65%` tại thị trường Việt Nam) + `Excel` + `Statistics` + `Data Storytelling (21.41%)` và kỹ năng `Communication (29.14%)`.
     - *Hướng 2 — Data Engineer & Data Platform (Cụm 0 - `30.77%` thị phần, lương trung vị cao nhất `30.00M`):* Không chỉ học `SQL/Python` mà bắt buộc phải học theo "combo" luật kết hợp Apriori: **`{PostgreSQL/MongoDB} + {Docker, Kubernetes} + {CI/CD} + {Cloud AWS/GCP/Azure}`** (các luật này có `Lift` từ `4.35` đến `6.80` và `Conviction` lên tới `86.99`) kèm `Kafka (37.18%)` và `Airflow (13.87%)`.
     - *Hướng 3 — Data Scientist & AI/ML Engineer (Cụm 1 - lương trung bình cao nhất `30.95M`, đỉnh `130.00M`):* Để bứt phá vào nhóm lương **`Trên 30M`**, sinh viên cần đầu tư vào các kỹ năng có tỷ lệ tin lương `>30M` cao nhất từ mô hình phân lớp: **`MLOps (72.41%)`**, **`NLP (68.52%)`**, **`Deep Learning (67.12%)`**, **`Machine Learning (66.12%)`** và đặc biệt là **`LLM / GenAI (58.53% — 258 tin tuyển dụng)`** cùng bộ đôi `PyTorch + TensorFlow` (hệ số tương quan $\phi = 0.8691$).
   - **Khuyến nghị 3 — Tích lũy kinh nghiệm thực chiến sớm để vượt "Ngưỡng vàng 1.0 năm và 3.55 năm":** Cây quyết định chỉ ra nút phân nhánh quan trọng nhất nằm ở `So_Nam_Kinh_Nghiem <= 0.65 - 1.0 năm` (tách `Fresher` lương trung vị `11.00M` với `Junior` `17.50M`) và `So_Nam_Kinh_Nghiem > 3.55 năm` (tách lên phân khúc `Senior` lương trung vị `35.00M`). Sinh viên nên đi thực tập (Intern/Part-time) hoặc làm đồ án dữ liệu thực tế từ năm 3 để khi ra trường đã có tối thiểu `1.0 năm` kinh nghiệm, rút ngắn thời gian chạm mốc `Middle/Senior`.

### 6.3. Hạn chế của Đề tài và Hướng Phát triển Tiếp theo *(~0.5 trang)*
1. **Nội dung cốt lõi cần viết:**
   - **Hạn chế:** (1) Tỷ lệ tin ẩn lương trên thị trường Việt Nam rất cao (`74.53%`), khiến mẫu lương công bố thực tế còn `394` tin (đặc biệt tại Đà Nẵng chỉ có `4` tin công bố lương); (2) Một số tin trên TopCV chỉ lấy được từ thẻ danh sách bên ngoài nên số kỹ năng bóc tách được ít hơn tin có JD đầy đủ; (3) Biểu diễn kỹ năng dạng nhị phân `0/1` chưa phân biệt được mức độ thành thạo (*Basic vs. Expert*).
   - **Hướng phát triển:** (1) Mở rộng crawler thu thập sâu vào từng trang chi tiết (Detail Page) của 100% tin TopCV và bổ sung nguồn `LinkedIn Jobs Vietnam` / `Glints`; (2) Áp dụng kỹ thuật `TF-IDF` hoặc ` PhoBERT / Sentence Embeddings` kết hợp với ma trận 60 kỹ năng để nâng cao `Macro F1-Score` của mô hình dự báo khoảng lương thực tế.

---

## 🛠️ QUY TRÌNH GHÉP BÁO CÁO PDF, KỊCH BẢN SLIDE 10–12 PHÚT & CHỐT CHẶN VẤN ĐÁP

### 1. Quy trình 4 Bước Ghép Báo cáo PDF (`NhomXX_BaoCao_BaiTapLon.pdf`) trong 2 Giờ
1. **Bước 1 (Chuẩn bị nhánh Git chuẩn):** Đảm bảo toàn nhóm đang ở nhánh **`audit-and-fix-final`** (hoặc merge nhánh này vào `main` bằng lệnh `git checkout main && git merge audit-and-fix-final`). Toàn bộ dữ liệu sạch và biểu đồ mới nhất đã nằm sẵn trong `notebooks/NhomXX_MiningPipeline.ipynb`.
2. **Bước 2 (Ghép nội dung văn bản theo Đề cương 6 Chương):**
   - Tạo 1 file Word / Google Docs / LaTeX chung định dạng khổ A4, font *Times New Roman* hoặc *Inter/Calibri* cỡ 11–12pt, giãn dòng 1.15–1.2, lề chuẩn (Trái 2.5cm, Phải/Trên/Dưới 2.0cm).
   - **TV1** dán nội dung **Trang bìa, Bảng WBS, Chương 1, Chương 2** (lấy từ `BAO_CAO_THANH_VIEN_1.md` và cập nhật các con số theo **Mục 3.2 của file `AUDIT_VA_DANH_GIA_DU_AN.md`**).
   - **TV2** dán nội dung **Chương 3, Chương 4** (lấy từ `BAO_CAO_THANH_VIEN_2.md` kèm các bảng/biểu đồ mới ở `TV2_EDA_Clustering_Apriori.ipynb`).
   - **TV3** dán nội dung **Chương 5, Chương 6** (lấy từ `BAO_CAO_THANH_VIEN_3.md` kèm phần phân tích `ccp_alpha`, Leakage-Free và Truy vết lỗi sai ở Mục 2.7 của `TV3_Classification_Decision_Tree.ipynb`).
3. **Bước 3 (Xuất ảnh biểu đồ độ phân giải cao từ `NhomXX_MiningPipeline.ipynb`):** Mở `notebooks/NhomXX_MiningPipeline.ipynb` trong VS Code hoặc Jupyter Lab, click chuột phải vào từng biểu đồ $\rightarrow$ *Save Image As...* để chèn vào đúng vị trí các Hình `3.1` $\rightarrow$ `5.4` đã chỉ định ở trên.
4. **Bước 4 (Kiểm tra chéo & Xuất PDF):** Ký xác nhận vào Bảng WBS ở Trang 2, cập nhật Mục lục tự động, kiểm tra tổng số trang nằm trong khoảng **18 – 23 trang** và xuất ra tệp **`NhomXX_BaoCao_BaiTapLon.pdf`**.

---

### 2. Cấu trúc Slide Thuyết trình Bảo vệ (`NhomXX_Slide_BaoCao.pdf` — 12 Slides / 10–12 Phút)

| Slide | Tiêu đề Slide | Nội dung & Hình ảnh cốt lõi trên Slide | Người trình bày & Thời lượng |
| :---: | :--- | :--- | :---: |
| **Slide 1** | **Trang bìa & Bảng WBS** | Tên đề tài, Danh sách 3 thành viên + Tỷ lệ đóng góp (34% - 33% - 33%) | **TV1** *(0.5 phút)* |
| **Slide 2** | **Bối cảnh & 4 Câu hỏi Nghiên cứu** | 3 nỗi đau của thị trường tuyển dụng Data & AI Việt Nam + Sơ đồ 4 câu hỏi nghiên cứu gắn với quy trình KDD | **TV1** *(1.0 phút)* |
| **Slide 3** | **Kiến trúc Crawler Đa nguồn & Bộ dữ liệu Thô** | Sơ đồ Hybrid Crawler (`Playwright` + `BS4` + `AJAX API`), 3 kỹ thuật (`Pagination`, `Infinite Scroll`, `Random Sleep`) + Bảng `1.547` tin từ 4 sàn (`TopCV`, `ITviec`, `VietnamWorks`, `TopDev`) | **TV1** *(1.0 phút)* |
| **Slide 4** | **Tiền xử lý Regex Lương & Ma trận 60 Kỹ năng** | Cơ chế Regex tách lương (`/tháng`, `/năm`, `USD/VNĐ`), Điền khuyết kép (`394` tin lương thực vs `1.153` tin thỏa thuận) + Kỹ thuật chống bắt nhầm chữ `R`, `Java`, `NoSQL` | **TV1** *(1.5 phút)* |
| **Slide 5** | **EDA (1): Bức tranh Thu nhập Ngành Data & AI** | Hình 3.1 (Histogram lương `Mean 27.66M`, `Median 25.50M`), Hình 3.2 (Boxplot 5 nhóm ngành: `DE Median 30M`, `DS/AI Mean 30.95M`) & Hình 3.3 (Boxplot 5 cấp bậc `Fresher 11M` $\rightarrow$ `Senior 35M`) | **TV2** *(1.5 phút)* |
| **Slide 6** | **EDA (2): Top 15 Kỹ năng, Địa lý & Mô hình làm việc** | Hình 3.4 (Top 15 kỹ năng: `SQL 58.2%`, `Python 35.8%`, `English 35.1%`), Hình 3.6 (So sánh `Hà Nội 56.2% - 25.5M` vs `TP.HCM 36.3% - 24.15M` vs `Đà Nẵng 15.35M`) & Tỷ lệ `On-site 90.6%` | **TV2** *(1.0 phút)* |
| **Slide 7** | **Gom cụm K-Means: Chọn $K=3$ & Chân dung Nghề nghiệp** | Hình 4.1–4.2 (`Elbow` & `Silhouette` đạt đỉnh `0.1603` tại $K=3$), Hình 4.4 (`PCA 2D`) & Hình 4.5 (3 chân dung: *DE & Infra 30.8%*, *AI & ML 4.0% - thuần khiết 100%*, *General Data/BI 65.2%*) | **TV2** *(1.5 phút)* |
| **Slide 8** | **Luật kết hợp Apriori: Luật Mạnh vs. Bẫy Độ tin cậy** | Bảng Top luật Multi-Cloud & Container (`Lift 4.4 – 6.8`, `Conviction` tới `86.99`) đối lập với Bảng 32 Luật nhiễu kéo về `{SQL}` (`Confidence ~69%` nhưng `Lift <= 1.2`) | **TV2** *(1.0 phút)* |
| **Slide 9** | **Phân lớp Khoảng lương & Phát hiện Data Leakage** | Thiết kế đối chứng Kịch bản 1 (`1.547` tin Imputed - `Acc 81.94%`) vs. Kịch bản 2 (`394` tin Lương Thực Leakage-Free) + Giải thích sắc bén hiện tượng rò rỉ qua điền khuyết | **TV3** *(1.0 phút)* |
| **Slide 10** | **Cắt tỉa Cành `ccp_alpha` & Đối sánh 4 Mô hình** | Hình 5.1 (Validation Curve 5-Fold CV chọn `ccp_alpha = 0.005442`), Bảng đối sánh 4 mô hình (`DT Pruned` dẫn đầu với `Test Macro F1 = 60.53%`, tăng `+4.81%` so với cây chưa tỉa) + Confusion Matrix | **TV3** *(1.0 phút)* |
| **Slide 11** | **Feature Importance, Kỹ năng Lương >30M & Truy vết lỗi** | Hình 5.3–5.4 (Cây quyết định & Feature Importance), Top kỹ năng lương `>30M` (`MLOps 72.4%`, `NLP 68.5%`, `DL 67.1%`, `ML 66.1%`, `LLM/GenAI 58.5%`) + Truy vết 2 ca `Annotation Leader` | **TV3** *(0.5 phút)* |
| **Slide 12** | **Kết luận & Lộ trình Hành trang cho Sinh viên** | 3 Khuyến nghị định lượng thực chiến cho sinh viên Data/CNTT + Lời cảm ơn & Mời Hội đồng đặt câu hỏi / Live Demo | **TV3** *(0.5 phút)* |

---

### 3. Danh sách Câu hỏi Vấn đáp Phản biện Trọng tâm tại Lớp (Chống Bốc thăm Ngẫu nhiên)

#### 🔹 Dành cho Thành viên 1 (Khi bị hỏi về Crawler, Data Audit & Regex Cleaning):
1. **Yêu cầu Live Demo tại chỗ:** *"Em hãy mở terminal chạy trực tiếp crawler cào thử 1–2 trang và mở 1 đường link bất kỳ trong `clean_data.csv` để đối soát."*
   - **Thao tác:** Chạy `.\.venv\Scripts\python.exe scraper.py --site itviec --keyword "Data Analyst" --pages 2` (hoặc `--site vietnamworks`). Mở `data/clean_data.csv`, giữ `Ctrl + Click` vào cột `URL_Goc` để mở bài đăng thực tế.
2. **Câu hỏi mổ xẻ code:** *"Tại sao ban đầu dữ liệu có mức lương tối đa 215.90 triệu/tháng nhưng ở bản báo cáo cuối cùng lại là 130.00 triệu/tháng? Em đã sửa dòng code nào?"*
   - **Trả lời:** Chỉ thẳng vào **dòng `183–188` file `step_02_clean_data.py`**: Bản ghi `DATA_1248` trên VietnamWorks ghi `"$ 8,000-9,000 /năm"`. Nhóm đã bổ sung biểu thức Regex `is_annual` phát hiện từ khóa `/năm`, `/year` để chia `multiplier` cho `12.0`, đưa mức lương của tin này về đúng `17.99 triệu/tháng` và khôi phục thêm 3 tin lương năm khác (`DATA_0153`, `DATA_1142`, `DATA_1249`).

#### 🔹 Dành cho Thành viên 2 (Khi bị hỏi về EDA, K-Means & Apriori):
1. **Câu hỏi mổ xẻ thuật toán K-Means:** *"Em hãy mở Notebook chạy lại hàm tính Silhouette Score và giải thích tại sao Silhouette Score của nhóm chỉ đạt `0.1603` tại $K=3$? Con số `0.1603` có phải là phân cụm kém không?"*
   - **Trả lời:** Mở **Cell 40 của `TV2_EDA_Clustering_Apriori.ipynb`**. Trong không gian nhị phân thưa 60 chiều (60 cột kỹ năng `0/1` đã chuẩn hóa Z-score), các tin tuyển dụng ngành Data đều chia sẻ một tập kỹ năng nền tảng chung (`SQL`, `Python`, `English`), nên khoảng cách Euclid giữa các điểm không tách rời thành các quả cầu cô lập như dữ liệu nhân tạo 2 chiều. Giá trị `0.1603` đạt cực đại rõ rệt tại $K=3$, và quan trọng nhất là kiểm định ngoại tại (External Validation) qua bảng Crosstab ở **Cell 53** chứng minh Cụm 1 đạt độ thuần khiết **100% `Data Scientist / AI & ML`**, còn Cụm 0 chứa **87.6% `Data Engineering & Database Infrastructure`**.
2. **Câu hỏi mổ xẻ Apriori:** *"Độ đo `Conviction` khác gì với `Lift`? Hãy chỉ ra một luật nhiễu trong bài của em."*
   - **Trả lời:** Mở **Cell 62 của `TV2_EDA_Clustering_Apriori.ipynb`**. `Lift` là độ đo đối xứng ($\text{Lift}(A \Rightarrow B) = \text{Lift}(B \Rightarrow A)$), trong khi `Conviction` $= \frac{1 - P(B)}{1 - \text{Conf}(A \Rightarrow B)}$ là độ đo **có hướng** đánh giá tần suất luật bị sai so với khi $A, B$ độc lập. Ví dụ luật `{Communication, English} => {SQL}` có `Confidence = 68.73%` tưởng là cao, nhưng vì `SQL` vốn chiếm `58.24%` toàn mẫu nên `Lift = 1.1801 <= 1.2` và `Conviction = 1.3354` rất thấp — đây chính là bẫy độ tin cậy (luật nhiễu) đã bị nhóm lọc bỏ.

#### 🔹 Dành cho Thành viên 3 (Khi bị hỏi về Decision Tree, `ccp_alpha`, Data Leakage & Error Analysis):
1. **Câu hỏi mổ xẻ Data Leakage:** *"Tại sao nhóm lại trình bày cả mô hình trên 1.547 tin và mô hình trên 394 tin?"*
   - **Trả lời:** Mở **Cell 46–49 của `TV3_Classification_Decision_Tree.ipynb`**. Nhóm chủ động thiết kế thực nghiệm đối chứng để chứng minh tác hại của **Target Leakage qua Imputation**: Khi điền khuyết 74.5% tin ẩn lương bằng `Median` theo `(Nhom_Nganh_Data, Cap_Bac)` trên toàn tập `1.547` tin, cây quyết định chỉ cần học theo `So_Nam_Kinh_Nghiem` (chiếm `76.85%` Feature Importance) là đạt `Accuracy 81.94%`. Khi cô lập hoàn toàn trên `394` tin công bố lương thực tế (`Leakage-Free`), độ chính xác phản ánh đúng độ khó thực tế của thị trường lao động (`Test Accuracy = 62.03%`, `Macro F1 = 60.53%`).
2. **Câu hỏi mổ xẻ `ccp_alpha` & Truy vết lỗi:** *"Làm sao em chọn được `ccp_alpha = 0.005442`? Và tại sao có 2 tin thực tế lương Dưới 15M mà cây quyết định lại dự đoán Trên 30M?"*
   - **Trả lời:** Mở **Cell 48 & Cell 50 của `TV3_Classification_Decision_Tree.ipynb`**:
     - `ccp_alpha = 0.005442` được chọn bằng **5-Fold Stratified Cross-Validation** trên tập Train (`CV Macro F1` đạt đỉnh `0.5717`), giúp giảm số nút lá xuống `29`, chống Overfitting và nâng `Test Macro F1` từ `55.72%` lên `60.53%`.
     - Hai bản ghi dự đoán lệch 2 bậc là `DATA_0756` và `DATA_0499` (*"Trưởng Nhóm Gán Nhãn Dữ Liệu - Annotation Leader"*): có chức danh `Lead` (`6.0 năm` kinh nghiệm) nhưng thuộc mảng gia công gán nhãn dữ liệu thủ công nên lương thực tế chỉ `10 - 12 triệu` (`11.0M`), khiến cây quyết định phân nhánh theo thâm niên `Lead` dự đoán nhầm sang nhóm `Trên 30M`.
