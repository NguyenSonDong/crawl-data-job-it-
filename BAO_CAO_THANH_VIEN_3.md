# BÁO CÁO HỌC THUẬT & BẢO VỆ ĐỒ ÁN KHAI PHÁ DỮ LIỆU (`ITEC3417`) — THÀNH VIÊN 3

> **Tên đề tài:** Thu thập và Khai phá Dữ liệu Tuyển dụng Thực tế nhóm ngành Dữ liệu & Trí tuệ Nhân tạo (*Data Analytics, Data Engineering, Data Science, BI, AI/ML*) tại Việt Nam  
> **Học phần:** Khai Phá Dữ Liệu (`ITEC3417`)  
> **Thành viên thực hiện:** Huỳnh Hữu Phước 
> **Phạm vi phụ trách:** Thành viên 3 (33% khối lượng đồ án) — Decision Tree, Random Forest, Đánh giá mô hình và Tổng hợp kết quả.  
> **Nhánh Git:** `thanh_vien_3`  
> **Ngày:** 18/11/2026
> **Sản phẩm bàn giao:** `TV3_Classification_Decision_Tree.ipynb`, `BAO_CAO_THANH_VIEN_3.md`.

---

## PHẦN 1: GIỚI THIỆU NHIỆM VỤ VÀ MỐI LIÊN HỆ VỚI CÁC GIAI ĐOẠN TRƯỚC

Trong các giai đoạn trước, Thành viên 1 đã thực hiện thu thập và tiền xử lý dữ liệu tuyển dụng. Tiếp đó, Thành viên 2 triển khai phân tích khám phá dữ liệu (EDA), phân cụm K-Means và khai phá luật kết hợp Apriori nhằm tìm hiểu đặc điểm thị trường tuyển dụng, các nhóm nghề nghiệp và mối liên hệ giữa những kỹ năng công nghệ.

Kế thừa bộ dữ liệu đã được làm sạch và các kết quả phân tích trước đó, Thành viên 3 tiếp tục thực hiện bài toán phân lớp có giám sát nhằm dự đoán khoảng lương tuyển dụng dựa trên yêu cầu kỹ năng và số năm kinh nghiệm.

Hai thuật toán được sử dụng là **Decision Tree** và **Random Forest**. Kết quả được đánh giá bằng Accuracy, Precision, Recall, F1-score và Confusion Matrix. Đồng thời, nghiên cứu tiến hành trực quan hóa cây quyết định và phân tích Feature Importance để xác định các thuộc tính có vai trò quan trọng trong quá trình phân lớp.

Phần thực nghiệm của Thành viên 3 được trình bày tiếp nối các mục 2.2, 2.3 và 2.4 của Thành viên 2, bắt đầu từ **Mục 2.5 – Phân lớp bằng Decision Tree và Random Forest**.

Các kết quả sau đó được tổng hợp và thảo luận nhằm làm rõ những phát hiện chính, giới hạn của dữ liệu và hiệu quả của các phương pháp được áp dụng.

---

## PHẦN 2: DỮ LIỆU ĐẦU VÀO VÀ PHƯƠNG PHÁP THỰC HIỆN

### 2.1. Dữ liệu sử dụng trong bài toán phân lớp

Nghiên cứu sử dụng bộ dữ liệu `data/clean_data.csv`, là sản phẩm đã được Thành viên 1 thu thập và tiền xử lý, đồng thời được Thành viên 2 sử dụng trong các bước EDA, K-Means và Apriori.

Bộ dữ liệu gồm **1.547 tin tuyển dụng với 85 thuộc tính**, trong đó có 60 thuộc tính kỹ năng công nghệ được mã hóa dưới dạng nhị phân (0/1).

Trong giai đoạn này, dữ liệu được sử dụng để xây dựng các mô hình học máy có giám sát nhằm dự đoán khoảng lương tuyển dụng dựa trên kỹ năng và số năm kinh nghiệm.

### 2.2. Xác định đặc trưng đầu vào và nhãn phân lớp

Dữ liệu được chia thành hai thành phần chính:

**Tập đặc trưng đầu vào (X):**

Sử dụng 61 thuộc tính, bao gồm:

- 60 thuộc tính kỹ năng có tên bắt đầu bằng `Skill_*`, chẳng hạn `Skill_Python`, `Skill_SQL`, `Skill_Machine_Learning`, `Skill_LLM_GenAI`.
- Thuộc tính `So_Nam_Kinh_Nghiem`, biểu diễn số năm kinh nghiệm được yêu cầu.

Các thuộc tính kỹ năng được biểu diễn như sau:

- Giá trị `1`: Tin tuyển dụng có ghi nhận yêu cầu kỹ năng.
- Giá trị `0`: Tin tuyển dụng không ghi nhận yêu cầu kỹ năng.

**Nhãn mục tiêu (y):**

Sử dụng thuộc tính `Khoang_Luong_Phan_Lop`, bao gồm ba nhóm lương:

| Nhóm lương | Số tin | Tỷ lệ (%) |
|---|---:|---:|
| Dưới 15M | 199 | 12,86 |
| 15M - 30M | 746 | 48,22 |
| Trên 30M | 602 | 38,91 |
| **Tổng cộng** | **1.547** | **100,00** |

*Sai lệch nhỏ khi cộng tỷ lệ có thể xuất phát từ việc làm tròn.*

**Nhận xét:** Nhóm lương 15M - 30M chiếm tỷ lệ lớn nhất, trong khi nhóm Dưới 15M có ít quan sát nhất. Sự chênh lệch số lượng giữa các lớp cần được xem xét khi đánh giá mô hình.

Các thuộc tính như `Luong_Min`, `Luong_Max`, `Luong_Trung_Binh` và `Luong_Trung_Binh_Imputed` không được đưa vào X vì chứa thông tin trực tiếp liên quan đến nhãn cần dự đoán, có nguy cơ gây rò rỉ dữ liệu (*Data Leakage*).

Qua kiểm tra, tập 61 đặc trưng đầu vào và nhãn mục tiêu không có giá trị thiếu.

### 2.3. Phân chia tập huấn luyện và kiểm tra

Sử dụng hàm `train_test_split()` của thư viện scikit-learn để chia dữ liệu theo tỷ lệ 80% huấn luyện và 20% kiểm tra.

**Cấu hình thực nghiệm:**

| Tham số | Giá trị | Ý nghĩa |
|---|---|---|
| `test_size` | `0.2` | Dành 20% dữ liệu để kiểm tra |
| `random_state` | `42` | Đảm bảo khả năng tái lập |
| `stratify` | `y` | Duy trì tỷ lệ các nhóm lương |

**Kết quả phân chia:**

| Tập dữ liệu | Số quan sát | Số đặc trưng |
|---|---:|---:|
| Training Set | 1.237 | 61 |
| Testing Set | 310 | 61 |
| **Tổng cộng** | **1.547** | **61** |

Phân bố nhãn trong các tập:

| Nhóm lương | Train | Test |
|---|---:|---:|
| Dưới 15M | 159 | 40 |
| 15M - 30M | 597 | 149 |
| Trên 30M | 481 | 121 |
| **Tổng cộng** | **1.237** | **310** |

**Nhận xét:** Tham số `stratify=y` giúp duy trì tỷ lệ các nhóm lương giữa tập huấn luyện và tập kiểm tra.

Tập Train được sử dụng để huấn luyện mô hình, còn tập Test được giữ riêng nhằm đánh giá khả năng dự đoán trên dữ liệu chưa tham gia quá trình học.

### 2.4. Phương pháp xây dựng và đánh giá mô hình

Nghiên cứu sử dụng hai thuật toán học máy có giám sát:

**Decision Tree (Cây quyết định):**

Xây dựng mô hình phân lớp bằng cách liên tục phân chia dữ liệu dựa trên các điều kiện thuộc tính. Thuật toán sử dụng tiêu chí Gini để lựa chọn những phép chia phù hợp.

**Random Forest (Rừng ngẫu nhiên):**

Là phương pháp học máy kết hợp nhiều cây quyết định, sử dụng quá trình lấy mẫu bootstrap và lựa chọn ngẫu nhiên tập con đặc trưng để xây dựng các cây.

Hai mô hình được huấn luyện trên cùng tập Train và đánh giá trên cùng tập Test nhằm đảm bảo tính nhất quán trong quá trình so sánh.

Các chỉ số đánh giá bao gồm:

- **Accuracy:** Tỷ lệ dự đoán chính xác.
- **Precision:** Mức độ chính xác của các dự đoán thuộc từng lớp.
- **Recall:** Khả năng nhận diện các quan sát thực sự thuộc từng lớp.
- **F1-score:** Chỉ số kết hợp Precision và Recall.
- **Confusion Matrix:** Ma trận thể hiện số lượng dự đoán đúng và sai giữa các lớp.

Ngoài ra, sử dụng `plot_tree()` để trực quan hóa cấu trúc cây quyết định và `feature_importances_` để phân tích mức độ quan trọng của các thuộc tính đầu vào.

Kết quả thực nghiệm chi tiết được trình bày tại **Mục 2.5 – Xây dựng mô hình phân lớp** và **Mục 2.6 – Đánh giá mô hình và rút trích luật**.

### 2.5. Lưu ý về chất lượng nhãn lương

Trong tổng số 1.547 tin tuyển dụng, có 391 tin công bố mức lương và 1.156 tin ghi lương thỏa thuận, tương ứng khoảng 74,73% dữ liệu không có mức lương công bố.

Bộ dữ liệu đã qua tiền xử lý có sử dụng giá trị lương điền khuyết tại thuộc tính `Luong_Trung_Binh_Imputed` để phục vụ việc xây dựng nhãn phân lớp.

Do đó, các kết quả đánh giá mô hình phản ánh khả năng dự đoán nhãn lương đã xử lý, bao gồm cả những nhãn được suy ra từ quá trình điền khuyết.

**Hạn chế:** Độ chính xác của mô hình trên toàn bộ tập Test không đồng nghĩa với độ chính xác dự đoán mức lương thực tế được doanh nghiệp công bố.

Vấn đề này cần được xem xét khi thảo luận kết quả và đưa ra kết luận nghiên cứu.

---

## PHẦN 3: NỘI DUNG CHƯƠNG 2 – XÂY DỰNG MÔ HÌNH DECISION TREE VÀ RANDOM FOREST

### Bước 2.5 – Phân lớp khoảng lương tuyển dụng

#### 2.5.1. Mục tiêu bài toán phân lớp

Tiếp nối các phương pháp phân tích khám phá dữ liệu (EDA), phân cụm K-Means và khai phá luật kết hợp Apriori của Thành viên 2, giai đoạn này áp dụng phương pháp học máy có giám sát nhằm dự đoán khoảng lương tuyển dụng dựa trên yêu cầu kỹ năng và số năm kinh nghiệm.

Hai thuật toán được sử dụng bao gồm:

- **Decision Tree:** Phân lớp dựa trên các quy tắc phân chia dữ liệu theo cấu trúc cây.
- **Random Forest:** Kết hợp nhiều cây quyết định để đưa ra kết quả dự đoán.

Mục tiêu là xây dựng, đánh giá và so sánh khả năng dự đoán của hai mô hình trên cùng bộ dữ liệu kiểm tra.

#### 2.5.2. Chuẩn bị dữ liệu đầu vào

Sử dụng bộ dữ liệu đã làm sạch gồm 1.547 tin tuyển dụng và 85 thuộc tính.

Tập dữ liệu được xác định như sau:

- **X:** 61 đặc trưng đầu vào, bao gồm 60 kỹ năng `Skill_*` và thuộc tính `So_Nam_Kinh_Nghiem`.
- **y:** Nhãn `Khoang_Luong_Phan_Lop`, gồm ba nhóm Dưới 15M, 15M - 30M và Trên 30M.

Các thuộc tính trực tiếp liên quan đến giá trị lương không được đưa vào tập đặc trưng để hạn chế rò rỉ dữ liệu.

Chi tiết về cấu trúc dữ liệu và phân bố nhãn đã được trình bày tại Phần 2 của báo cáo.

#### 2.5.3. Phân chia tập huấn luyện và kiểm tra

Sử dụng `train_test_split()` để chia dữ liệu theo tỷ lệ 80% huấn luyện và 20% kiểm tra.

Cấu hình thực nghiệm:

- `test_size=0.2`
- `random_state=42`
- `stratify=y`

| Tập dữ liệu | Số quan sát | Số đặc trưng |
|---|---:|---:|
| Train | 1.237 | 61 |
| Test | 310 | 61 |
| **Tổng cộng** | **1.547** | **61** |

**Nhận xét:** Việc sử dụng `stratify=y` giúp duy trì tỷ lệ các nhóm lương giữa hai tập dữ liệu. Cả hai mô hình sử dụng cùng tập Train và Test để đảm bảo tính nhất quán khi so sánh.

---

#### 2.5.4. Xây dựng mô hình Decision Tree

**a. Nguyên lý thuật toán**

Decision Tree (Cây quyết định) là thuật toán học máy có giám sát, thực hiện phân lớp bằng cách liên tục chia dữ liệu thành những tập con dựa trên điều kiện của các thuộc tính.

Trong nghiên cứu này, thuật toán sử dụng chỉ số Gini để lựa chọn các điểm phân chia nhằm giảm mức độ hỗn tạp giữa các nhóm lương.

Công thức Gini:

\[
Gini = 1 - \sum_{i=1}^{K} p_i^2
\]

Trong đó:

- \(K\): Số lớp trong bài toán phân lớp.
- \(p_i\): Tỷ lệ quan sát thuộc lớp thứ \(i\).

Giá trị Gini càng nhỏ cho thấy mức độ hỗn tạp của nút càng thấp.

**b. Cấu hình mô hình**

Mô hình được xây dựng bằng `DecisionTreeClassifier` thuộc thư viện scikit-learn.

| Tham số | Giá trị | Ý nghĩa |
|---|---|---|
| `criterion` | `gini` | Sử dụng chỉ số Gini |
| `max_depth` | 5 | Giới hạn độ sâu tối đa của cây |
| `min_samples_leaf` | 10 | Mỗi nút lá có ít nhất 10 quan sát |
| `random_state` | 42 | Đảm bảo khả năng tái lập thí nghiệm |

Việc giới hạn độ sâu và số mẫu tối thiểu tại nút lá nhằm kiểm soát độ phức tạp của cây và hạn chế nguy cơ học quá khớp dữ liệu huấn luyện.

**c. Kết quả thực nghiệm**

Sau khi huấn luyện trên tập Train và dự đoán trên tập Test, thu được kết quả:

| Chỉ số | Kết quả |
|---|---:|
| Accuracy Train | 83,10% |
| Accuracy Test | 75,48% |
| Độ sâu thực tế | 5 |
| Số nút lá | 27 |
| Số dự đoán đúng trên Test | 234/310 |
| Số dự đoán sai trên Test | 76/310 |

**d. Nhận xét**

- Mô hình đạt Accuracy 83,10% trên tập huấn luyện và 75,48% trên tập kiểm tra.
- Cây quyết định có độ sâu thực tế bằng 5 và gồm 27 nút lá.
- Accuracy trên tập Train cao hơn tập Test khoảng 7,62 điểm phần trăm.
- Kết quả cho thấy mô hình đã học được các quy tắc phân lớp từ dữ liệu kỹ năng và kinh nghiệm.
- Sự chênh lệch giữa Accuracy Train và Test cho thấy cần xem xét khả năng tổng quát hóa của mô hình.

**Kết luận:** Decision Tree bước đầu cho thấy khả năng phân loại khoảng lương trên bộ dữ liệu đã xử lý. Cấu trúc cây có thể trực quan hóa và rút trích thành các quy tắc phân lớp, hỗ trợ việc giải thích kết quả dự đoán.

---

#### 2.5.5. Xây dựng mô hình Random Forest

**a. Nguyên lý thuật toán**

Random Forest (Rừng ngẫu nhiên) là phương pháp học máy kết hợp (*Ensemble Learning*), sử dụng nhiều cây quyết định để thực hiện bài toán phân lớp.

Thuật toán xây dựng các cây từ những mẫu dữ liệu bootstrap và lựa chọn ngẫu nhiên tập con đặc trưng tại các nút phân chia.

Kết quả dự đoán cuối cùng được xác định bằng cách tổng hợp dự đoán của các cây trong rừng.

Phương pháp này nhằm tận dụng kết quả của nhiều cây, giảm sự phụ thuộc vào cấu trúc của một cây quyết định đơn lẻ.

**b. Cấu hình mô hình**

Mô hình được xây dựng bằng `RandomForestClassifier` của thư viện scikit-learn.

| Tham số | Giá trị | Ý nghĩa |
|---|---|---|
| `n_estimators` | 200 | Xây dựng 200 cây quyết định |
| `criterion` | `gini` | Sử dụng chỉ số Gini |
| `max_depth` | 10 | Giới hạn độ sâu tối đa mỗi cây |
| `min_samples_leaf` | 5 | Mỗi nút lá có ít nhất 5 quan sát |
| `max_features` | `sqrt` | Chọn tập con ngẫu nhiên các đặc trưng tại mỗi phép chia |
| `random_state` | 42 | Đảm bảo tính tái lập |
| `n_jobs` | -1 | Sử dụng các bộ xử lý có sẵn |

**c. Kết quả thực nghiệm**

Sau khi huấn luyện mô hình Random Forest với 200 cây quyết định, thu được kết quả:

| Chỉ số | Kết quả |
|---|---:|
| Accuracy Train | 83,91% |
| Accuracy Test | 73,55% |
| Số cây quyết định | 200 |
| Số đặc trưng đầu vào | 61 |
| Số dự đoán đúng trên Test | 228/310 |
| Số dự đoán sai trên Test | 82/310 |

**d. Nhận xét**

- Random Forest đạt Accuracy 83,91% trên tập Train và 73,55% trên tập Test.
- Mô hình kết hợp 200 cây quyết định để thực hiện phân lớp.
- Accuracy Train cao hơn Accuracy Test khoảng 10,36 điểm phần trăm.
- So với Decision Tree, Random Forest đạt Accuracy Train cao hơn nhưng Accuracy Test thấp hơn khoảng 1,94 điểm phần trăm.
- Kết quả cho thấy việc kết hợp nhiều cây không đảm bảo mô hình luôn đạt độ chính xác cao hơn một cây quyết định đơn lẻ.

**Kết luận:** Random Forest đã được xây dựng và huấn luyện thành công. Tuy nhiên, với bộ tham số thử nghiệm hiện tại, mô hình chưa vượt qua Decision Tree về Accuracy trên tập kiểm tra.

---

#### 2.5.6. Tổng hợp kết quả huấn luyện

Bảng so sánh kết quả ban đầu:

| Tiêu chí | Decision Tree | Random Forest |
|---|---:|---:|
| Số cây | 1 | 200 |
| Accuracy Train | 83,10% | 83,91% |
| Accuracy Test | **75,48%** | 73,55% |
| Số dự đoán đúng | **234** | 228 |
| Số dự đoán sai | **76** | 82 |

**Nhận xét tổng hợp:**

Decision Tree đạt Accuracy trên tập kiểm tra cao hơn Random Forest trong hai cấu hình được sử dụng.

Tuy nhiên, chỉ số Accuracy chưa phản ánh đầy đủ hiệu quả phân loại ở từng nhóm lương, đặc biệt khi dữ liệu có sự chênh lệch số lượng giữa các lớp.

Vì vậy, cần tiếp tục đánh giá hai mô hình bằng Precision, Recall, F1-score và Confusion Matrix để có cơ sở so sánh đầy đủ hơn.

Các kết quả đánh giá chi tiết được trình bày ở **Bước 2.6 – Đánh giá mô hình và rút trích luật Cây quyết định**.

---

## PHẦN 4: NỘI DUNG CHƯƠNG 2 – ĐÁNH GIÁ MÔ HÌNH VÀ RÚT TRÍCH LUẬT CÂY QUYẾT ĐỊNH

### Bước 2.6 – Đánh giá mô hình và phân tích đặc trưng

Sau khi xây dựng hai mô hình Decision Tree và Random Forest, nghiên cứu tiến hành đánh giá khả năng phân lớp trên tập Test gồm 310 tin tuyển dụng.

Các nội dung đánh giá bao gồm:

- Tính toán Accuracy, Precision, Recall và F1-score.
- Xây dựng và phân tích Confusion Matrix.
- Trực quan hóa cây quyết định và rút trích các quy tắc phân lớp.
- Phân tích Feature Importance và xác định những kỹ năng có liên hệ với nhóm lương Trên 30M.

#### 2.6.1. Đánh giá bằng Accuracy, Precision, Recall và F1-score

**a. Các chỉ số đánh giá**

Để đánh giá hiệu quả của hai mô hình, nghiên cứu sử dụng bốn chỉ số phân lớp.

**Accuracy** biểu diễn tỷ lệ dự đoán chính xác trên toàn bộ tập kiểm tra.

\[
Accuracy=\frac{\text{Số dự đoán đúng}}{\text{Tổng số quan sát}}
\]

**Precision** đo tỷ lệ dự đoán chính xác trong những quan sát được mô hình phân loại vào một lớp cụ thể.

\[
Precision=\frac{TP}{TP+FP}
\]

**Recall** đo khả năng nhận diện chính xác các quan sát thực sự thuộc một lớp.

\[
Recall=\frac{TP}{TP+FN}
\]

**F1-score** là trung bình điều hòa giữa Precision và Recall.

\[
F1=2\times\frac{Precision\times Recall}{Precision+Recall}
\]

Trong bài toán có ba nhóm lương với số lượng quan sát không đồng đều, nghiên cứu sử dụng Macro Average để tổng hợp Precision, Recall và F1-score.

Macro Average tính trung bình chỉ số của từng lớp với trọng số ngang nhau, giúp đánh giá hiệu quả phân lớp mà không để nhóm có nhiều quan sát chi phối hoàn toàn kết quả.

**b. Kết quả đánh giá tổng thể**

Kết quả đánh giá hai mô hình trên tập Test:

| Chỉ số | Decision Tree | Random Forest |
|---|---:|---:|
| Accuracy | **75,48%** | 73,55% |
| Macro Precision | 74,97% | **81,53%** |
| Macro Recall | **76,61%** | 65,33% |
| Macro F1-score | **75,05%** | 68,58% |

**c. Kết quả đánh giá theo từng nhóm lương**

*Decision Tree:*

| Nhóm lương | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Dưới 15M | 0,6735 | 0,8250 | 0,7416 | 40 |
| 15M - 30M | 0,7246 | 0,8121 | 0,7658 | 149 |
| Trên 30M | 0,8511 | 0,6612 | 0,7442 | 121 |

*Random Forest:*

| Nhóm lương | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Dưới 15M | 1,0000 | 0,3750 | 0,5455 | 40 |
| 15M - 30M | 0,7107 | 0,7584 | 0,7338 | 149 |
| Trên 30M | 0,7353 | 0,8264 | 0,7782 | 121 |

**d. Nhận xét**

- Decision Tree đạt Accuracy 75,48%, cao hơn Random Forest khoảng 1,94 điểm phần trăm.
- Decision Tree có Macro Recall và Macro F1-score cao hơn, cho thấy khả năng nhận diện tương đối cân bằng giữa ba nhóm lương.
- Random Forest có Macro Precision cao hơn, nhưng Macro Recall thấp hơn đáng kể.
- Đối với nhóm Dưới 15M, Random Forest đạt Precision 100% nhưng Recall chỉ đạt 37,5%, cho thấy mô hình bỏ sót nhiều quan sát thuộc nhóm này.
- Đối với nhóm Trên 30M, Random Forest đạt Recall 82,64%, cao hơn Decision Tree với 66,12%.

**Kết luận:** Trong hai cấu hình thực nghiệm hiện tại, Decision Tree cho kết quả tổng thể tốt hơn theo Accuracy và Macro F1-score. Tuy nhiên, hiệu quả phân lớp khác nhau giữa các nhóm lương nên cần kết hợp Confusion Matrix để phân tích chi tiết.

---

#### 2.6.2. Phân tích ma trận nhầm lẫn (Confusion Matrix)

**a. Phương pháp thực hiện**

Confusion Matrix được sử dụng để xác định số lượng quan sát được dự đoán đúng và sai đối với từng nhóm lương.

Trong ma trận:

- Hàng biểu diễn nhãn thực tế.
- Cột biểu diễn nhãn dự đoán.
- Đường chéo chính biểu diễn các trường hợp dự đoán đúng.
- Các phần tử ngoài đường chéo biểu diễn các trường hợp dự đoán sai.

Ma trận được xây dựng bằng hàm `confusion_matrix()` trong thư viện scikit-learn và trực quan hóa thông qua Seaborn Heatmap.

**b. Kết quả Decision Tree**

| Thực tế \ Dự đoán | Dưới 15M | 15M - 30M | Trên 30M |
|---|---:|---:|---:|
| Dưới 15M | **33** | 6 | 1 |
| 15M - 30M | 15 | **121** | 13 |
| Trên 30M | 1 | 40 | **80** |

Tổng số dự đoán chính xác là 234/310, tương ứng Accuracy 75,48%.

**Nhận xét:**

- Nhóm Dưới 15M có 33/40 tin được dự đoán chính xác.
- Nhóm 15M - 30M có 121/149 tin được dự đoán chính xác.
- Nhóm Trên 30M có 80/121 tin được dự đoán chính xác.
- Có 40 tin thực tế thuộc nhóm Trên 30M nhưng bị nhầm sang nhóm 15M - 30M.

Điều này cho thấy Decision Tree còn gặp khó khăn trong việc phân biệt nhóm lương trung bình với nhóm lương cao.

**c. Kết quả Random Forest**

| Thực tế \ Dự đoán | Dưới 15M | 15M - 30M | Trên 30M |
|---|---:|---:|---:|
| Dưới 15M | **15** | 25 | 0 |
| 15M - 30M | 0 | **113** | 36 |
| Trên 30M | 0 | 21 | **100** |

Tổng số dự đoán chính xác là 228/310, tương ứng Accuracy 73,55%.

**Nhận xét:**

- Nhóm Dưới 15M chỉ có 15/40 tin được dự đoán chính xác, trong khi 25 tin bị nhầm sang nhóm 15M - 30M.
- Nhóm 15M - 30M có 113/149 tin được dự đoán chính xác.
- Nhóm Trên 30M có 100/121 tin được dự đoán chính xác.

Random Forest nhận diện nhóm Trên 30M tốt hơn Decision Tree, nhưng bỏ sót nhiều quan sát thuộc nhóm Dưới 15M.

**d. So sánh hai mô hình**

| Tiêu chí | Decision Tree | Random Forest |
|---|---:|---:|
| Dự đoán đúng Dưới 15M | **33/40** | 15/40 |
| Dự đoán đúng 15M - 30M | **121/149** | 113/149 |
| Dự đoán đúng Trên 30M | 80/121 | **100/121** |
| Tổng dự đoán đúng | **234** | 228 |
| Tổng dự đoán sai | **76** | 82 |

**Kết luận:** Decision Tree nhận diện tốt hơn hai nhóm Dưới 15M và 15M - 30M, trong khi Random Forest có ưu thế đối với nhóm Trên 30M.

Các kết quả này phù hợp với sự khác biệt về Recall và F1-score đã được trình bày ở mục 2.6.1.

---

#### 2.6.3. Trực quan hóa và rút trích luật Cây quyết định

**a. Phương pháp thực hiện**

Sử dụng hàm `plot_tree()` trong thư viện scikit-learn để trực quan hóa mô hình Decision Tree đã được huấn luyện.

Mỗi nút trên cây thể hiện:

- Thuộc tính và điều kiện phân chia.
- Chỉ số Gini.
- Số lượng quan sát tại nút (`samples`).
- Phân bố các nhóm lương (`value`).
- Nhóm lương được dự đoán (`class`).

Mô hình Decision Tree có độ sâu thực tế bằng 5 và tổng cộng 27 nút lá.

Để thuận tiện cho việc quan sát, biểu đồ chỉ hiển thị các nút từ độ sâu 0 đến độ sâu 2. Việc giới hạn phần hiển thị không làm thay đổi cấu trúc mô hình đã huấn luyện.

**b. Kết quả rút trích quy tắc**

Kết quả phân tích cây quyết định cho thấy thuộc tính `So_Nam_Kinh_Nghiem` được lựa chọn tại nút gốc.

Điều kiện phân chia đầu tiên:

```text
So_Nam_Kinh_Nghiem <= 3.55
```

Điều này có nghĩa mô hình bắt đầu bằng cách chia các tin tuyển dụng thành hai nhóm theo ngưỡng kinh nghiệm 3,55 năm.

Ở những nút tiếp theo, cây tiếp tục sử dụng số năm kinh nghiệm và một số kỹ năng công nghệ để phân chia dữ liệu.

Ví dụ, phần đầu của cây có các điều kiện:

```text
|--- So_Nam_Kinh_Nghiem <= 3.55
|   |--- So_Nam_Kinh_Nghiem <= 0.90
|   |   |--- Skill_PostgreSQL <= 0.50
|   |   |--- Skill_PostgreSQL >  0.50
|   |--- So_Nam_Kinh_Nghiem >  0.90
|   |   |--- Skill_LLM_GenAI <= 0.50
|   |   |--- Skill_LLM_GenAI >  0.50
|--- So_Nam_Kinh_Nghiem > 3.55
|   |--- So_Nam_Kinh_Nghiem <= 5.55
```

*Đây là các điều kiện phân chia ở phần đầu cây, không phải toàn bộ các đường đi đến nút lá.*

**c. Nhận xét**

- `So_Nam_Kinh_Nghiem` xuất hiện tại nút gốc, cho thấy kinh nghiệm có vai trò đáng chú ý trong phép phân chia đầu tiên.
- Những thuộc tính kỹ năng như `Skill_PostgreSQL` và `Skill_LLM_GenAI` được sử dụng ở các nhánh tiếp theo.
- Cấu trúc cây cho phép quan sát các điều kiện được mô hình sử dụng trong quá trình phân lớp.
- Các quy tắc có thể được rút trích để giải thích cách mô hình đưa ra dự đoán.

**Kết luận:** Việc trực quan hóa Decision Tree giúp giải thích quá trình phân lớp một cách trực quan. Kết quả cho thấy số năm kinh nghiệm và các kỹ năng công nghệ đều được sử dụng để phân chia dữ liệu tuyển dụng.

Tuy nhiên, các quy tắc phản ánh mối liên hệ mà mô hình học được từ dữ liệu, không chứng minh quan hệ nhân quả giữa kỹ năng, kinh nghiệm và mức lương.

---

#### 2.6.4. Phân tích Feature Importance và kỹ năng liên quan đến nhóm lương Trên 30M

**a. Phương pháp phân tích Feature Importance**

Sử dụng thuộc tính `feature_importances_` của Decision Tree và Random Forest để xác định mức độ đóng góp tương đối của từng đặc trưng trong quá trình phân lớp.

Chỉ số Feature Importance phản ánh mức đóng góp vào tổng mức giảm độ hỗn tạp khi mô hình phân chia dữ liệu.

Các giá trị được chuẩn hóa để tổng Feature Importance của các thuộc tính bằng 1.

**b. Kết quả Decision Tree**

Những thuộc tính có Feature Importance cao nhất:

| Đặc trưng | Feature Importance (%) |
|---|---:|
| `So_Nam_Kinh_Nghiem` | **76,22** |
| `Skill_LLM_GenAI` | 6,42 |
| `Skill_PostgreSQL` | 3,88 |
| `Skill_Linux` | 3,12 |
| `Skill_MySQL` | 2,56 |
| `Skill_Java` | 2,48 |
| `Skill_Cloud_Azure` | 1,25 |
| `Skill_Python` | 1,18 |
| `Skill_PowerBI` | 1,08 |
| `Skill_Machine_Learning` | 0,74 |

**Nhận xét:** `So_Nam_Kinh_Nghiem` có mức đóng góp lớn nhất, chiếm khoảng 76,22% tổng Feature Importance.

Trong nhóm kỹ năng công nghệ, LLM/GenAI, PostgreSQL và Linux có mức đóng góp nổi bật.

**c. Kết quả Random Forest**

| Đặc trưng | Feature Importance (%) |
|---|---:|
| `So_Nam_Kinh_Nghiem` | **53,40** |
| `Skill_Machine_Learning` | 4,75 |
| `Skill_LLM_GenAI` | 4,08 |
| `Skill_Python` | 1,46 |
| `Skill_CI_CD` | 1,42 |
| `Skill_SQL_Server` | 1,41 |
| `Skill_Linux` | 1,38 |
| `Skill_Communication` | 1,36 |
| `Skill_Oracle` | 1,34 |
| `Skill_Teamwork` | 1,30 |

**Nhận xét:** Số năm kinh nghiệm tiếp tục là thuộc tính quan trọng nhất, chiếm khoảng 53,40% tổng Feature Importance.

Trong nhóm kỹ năng công nghệ, Machine Learning và LLM/GenAI có mức đóng góp cao hơn các kỹ năng còn lại.

**d. Phân tích kỹ năng liên quan đến nhóm lương Trên 30M**

Để xác định các kỹ năng có liên hệ với nhóm lương cao, nghiên cứu thống kê tỷ lệ tin thuộc nhóm Trên 30M trong số các tin có yêu cầu từng kỹ năng.

Chỉ xét những kỹ năng xuất hiện trong ít nhất 30 tin tuyển dụng nhằm hạn chế ảnh hưởng của các kỹ năng quá hiếm.

Kết quả:

| Kỹ năng | Tổng tin có yêu cầu | Tin Trên 30M | Tỷ lệ Trên 30M (%) |
|---|---:|---:|---:|
| NLP | 54 | 37 | **68,52** |
| MLOps | 58 | 39 | 67,24 |
| Deep Learning | 73 | 49 | 67,12 |
| Machine Learning | 245 | 153 | 62,45 |
| TensorFlow | 42 | 26 | 61,90 |
| Computer Vision | 72 | 43 | 59,72 |
| A/B Testing | 34 | 20 | 58,82 |
| LLM/GenAI | 258 | 150 | 58,14 |
| PyTorch | 50 | 29 | 58,00 |
| Statistics | 158 | 81 | 51,27 |

**Nhận xét:**

- NLP có tỷ lệ tin thuộc nhóm Trên 30M cao nhất trong các kỹ năng được xét, đạt 68,52%.
- MLOps và Deep Learning có tỷ lệ tương ứng 67,24% và 67,12%.
- Machine Learning xuất hiện trong 153 tin thuộc nhóm Trên 30M.
- LLM/GenAI xuất hiện trong 150 tin thuộc nhóm Trên 30M.
- Những kỹ năng liên quan đến AI và Machine Learning có mối liên hệ đáng chú ý với nhóm lương cao trong bộ dữ liệu nghiên cứu.

**e. Kết luận**

Kết quả Feature Importance cho thấy số năm kinh nghiệm đóng góp lớn nhất vào quá trình phân lớp của cả hai mô hình.

Bên cạnh đó, Machine Learning và LLM/GenAI vừa có mức độ quan trọng đáng chú ý trong mô hình Random Forest, vừa xuất hiện trong nhiều tin tuyển dụng thuộc nhóm lương Trên 30M.

Tuy nhiên, Feature Importance không trực tiếp cho biết một kỹ năng làm tăng hay giảm mức lương. Tỷ lệ nhóm lương Trên 30M cũng chỉ phản ánh mối liên hệ thống kê, không chứng minh kỹ năng là nguyên nhân quyết định mức lương.

---

### Nhận xét tổng hợp Bước 2.6

Qua quá trình đánh giá và phân tích, nghiên cứu rút ra những kết quả chính:

- Decision Tree đạt Accuracy 75,48% và Macro F1-score 75,05%, cao hơn Random Forest trong hai cấu hình thử nghiệm.
- Random Forest có khả năng nhận diện nhóm Trên 30M tốt hơn, nhưng bỏ sót nhiều tin thuộc nhóm Dưới 15M.
- Cây quyết định sử dụng số năm kinh nghiệm tại nút gốc với ngưỡng phân chia 3,55 năm.
- Số năm kinh nghiệm là thuộc tính có Feature Importance cao nhất trong cả hai mô hình.
- Các kỹ năng NLP, MLOps, Deep Learning, Machine Learning và LLM/GenAI có tỷ lệ thuộc nhóm Trên 30M tương đối cao trong mẫu nghiên cứu.

**Hạn chế cần lưu ý:** Bộ dữ liệu có 1.156/1.547 tin không công bố mức lương, và nhãn phân lớp đã được xử lý bằng phương pháp điền khuyết. Vì vậy, hiệu quả mô hình chỉ phản ánh khả năng dự đoán nhãn đã xử lý, chưa đủ để khẳng định khả năng dự đoán mức lương thực tế trên toàn thị trường.

Các kết quả này là cơ sở để tiếp tục thảo luận và tổng hợp kết luận của nghiên cứu tại Chương 3.

---

## PHẦN 5: CHƯƠNG 3 – THẢO LUẬN, TỔNG HỢP KẾT QUẢ VÀ KẾT LUẬN

### 3.1. Tổng hợp kết quả nghiên cứu

Nghiên cứu được thực hiện trên bộ dữ liệu gồm 1.547 tin tuyển dụng thuộc năm nhóm ngành Dữ liệu và Trí tuệ nhân tạo tại Việt Nam.

Thông qua quá trình thu thập, tiền xử lý, phân tích khám phá dữ liệu và áp dụng các thuật toán khai phá dữ liệu, nhóm đã thu được những kết quả về đặc điểm tuyển dụng, yêu cầu kỹ năng và mối liên hệ giữa kỹ năng, kinh nghiệm với khoảng lương.

Các phương pháp được sử dụng bao gồm:

- Phân tích khám phá dữ liệu (EDA).
- Phân cụm bằng K-Means.
- Khai phá luật kết hợp bằng Apriori.
- Phân lớp bằng Decision Tree và Random Forest.

**Bảng tổng hợp kết quả nghiên cứu:**

| Phương pháp | Kết quả chính |
|---|---|
| EDA | Khảo sát phân bố ngành nghề, mức lương, kỹ năng, địa lý và mô hình làm việc |
| K-Means | Xây dựng phương án phân cụm K = 3, khám phá ba chân dung nghề nghiệp |
| Apriori | Phát hiện 480 tập kỹ năng phổ biến và 454 luật kết hợp trước bước lọc Lift |
| Decision Tree | Accuracy Test đạt 75,48%; Macro F1-score đạt 75,05% |
| Random Forest | Accuracy Test đạt 73,55%; Macro F1-score đạt 68,58% |

Các kết quả cho thấy mỗi phương pháp khai phá dữ liệu cung cấp một góc nhìn khác nhau.

EDA giúp mô tả đặc điểm dữ liệu tuyển dụng. K-Means và Apriori hỗ trợ khám phá cấu trúc dữ liệu và mối liên hệ giữa những kỹ năng. Trong khi đó, Decision Tree và Random Forest được sử dụng để học các quy tắc phân lớp khoảng lương từ kỹ năng và kinh nghiệm.

Việc kết hợp các phương pháp giúp nghiên cứu không chỉ mô tả dữ liệu mà còn phân tích các đặc điểm liên quan đến nhãn khoảng lương tuyển dụng.

---

### 3.2. Thảo luận các kết quả nghiên cứu

#### 3.2.1. Đặc điểm thị trường tuyển dụng và yêu cầu kỹ năng

Kết quả EDA của Thành viên 2 cho thấy nhóm Database / Data Platform & Ops chiếm tỷ lệ lớn nhất với 527 tin, tương ứng 34,07% tổng số quan sát.

Các nhóm Data Engineer / Big Data và Data Scientist / AI & ML lần lượt chiếm 20,88% và 19,91%.

Về yêu cầu kỹ năng, SQL xuất hiện trong 71,95% tin tuyển dụng, trong khi Python xuất hiện trong 48,87% số tin. Tổ hợp Python và SQL cùng xuất hiện trong 36,65% mẫu dữ liệu.

Kết quả này cho thấy SQL và Python là hai kỹ năng phổ biến trong bộ dữ liệu tuyển dụng được khảo sát.

Bên cạnh đó, phương pháp K-Means với K = 3 cho phép khám phá ba chân dung nghề nghiệp:

- **Cụm 0 – AI & Machine Learning:** Tập trung các tin thuộc nhóm Data Scientist / AI & ML.
- **Cụm 1 – General Data & Analytics:** Có thành phần đa dạng, bao gồm nhiều nhóm ngành Data.
- **Cụm 2 – Data Engineering & Infrastructure:** Tập trung các vị trí liên quan đến kỹ thuật dữ liệu và hạ tầng.

Kết quả Apriori cũng cho thấy những tổ hợp kỹ năng thuộc Cloud, DevOps và cơ sở dữ liệu có xu hướng xuất hiện cùng nhau.

Ví dụ, luật `AWS, Azure → GCP` có Confidence 74,31% và Lift 6,8018, cho thấy mối liên hệ đồng xuất hiện mạnh giữa các kỹ năng trong mẫu dữ liệu.

Những kết quả trên cung cấp cơ sở để hiểu rõ hơn về các nhóm kỹ năng trong dữ liệu tuyển dụng, đồng thời hỗ trợ việc diễn giải những đặc trưng được mô hình phân lớp sử dụng.

Tuy nhiên, kết quả phân cụm và luật kết hợp không chứng minh quan hệ nhân quả giữa các kỹ năng hoặc giữa kỹ năng và mức lương.

#### 3.2.2. Hiệu quả của mô hình Decision Tree và Random Forest

Hai mô hình Decision Tree và Random Forest được huấn luyện trên 1.237 tin tuyển dụng và đánh giá trên tập Test gồm 310 tin.

Kết quả thực nghiệm:

| Chỉ số | Decision Tree | Random Forest |
|---|---:|---:|
| Accuracy | **75,48%** | 73,55% |
| Macro Precision | 74,97% | **81,53%** |
| Macro Recall | **76,61%** | 65,33% |
| Macro F1-score | **75,05%** | 68,58% |

Decision Tree đạt Accuracy cao hơn Random Forest khoảng 1,94 điểm phần trăm và Macro F1-score cao hơn khoảng 6,47 điểm phần trăm.

Kết quả cho thấy Decision Tree có khả năng phân lớp tương đối cân bằng hơn giữa ba nhóm lương trong hai cấu hình thực nghiệm đã sử dụng.

Tuy nhiên, Random Forest có ưu thế đối với nhóm lương Trên 30M.

Cụ thể:

- Decision Tree nhận diện đúng 80/121 tin thuộc nhóm Trên 30M.
- Random Forest nhận diện đúng 100/121 tin thuộc nhóm Trên 30M.

Ngược lại, đối với nhóm Dưới 15M:

- Decision Tree nhận diện đúng 33/40 tin.
- Random Forest chỉ nhận diện đúng 15/40 tin.

Kết quả Confusion Matrix cho thấy hai mô hình có những ưu điểm và hạn chế khác nhau khi phân loại từng nhóm lương.

**Nhận xét:** Trong các cấu hình thử nghiệm hiện tại, Decision Tree cho kết quả tốt hơn về Accuracy và Macro F1-score. Tuy nhiên, chưa thể khẳng định thuật toán này luôn hiệu quả hơn Random Forest đối với những bộ dữ liệu khác hoặc cấu hình tham số khác.

#### 3.2.3. Vai trò của kinh nghiệm và kỹ năng đối với phân lớp khoảng lương

Kết quả Feature Importance cho thấy số năm kinh nghiệm là thuộc tính có mức độ quan trọng cao nhất trong cả hai mô hình.

Cụ thể:

| Thuộc tính | Decision Tree | Random Forest |
|---|---:|---:|
| `So_Nam_Kinh_Nghiem` | 76,22% | 53,40% |

Trong mô hình Decision Tree, thuộc tính `So_Nam_Kinh_Nghiem` được sử dụng tại nút gốc với điều kiện phân chia:

`So_Nam_Kinh_Nghiem <= 3.55`

Điều này cho thấy mô hình sử dụng số năm kinh nghiệm ngay trong phép phân chia đầu tiên để phân biệt các nhóm dữ liệu.

Bên cạnh đó, một số kỹ năng công nghệ cũng có mức độ đóng góp đáng chú ý.

Đối với Decision Tree, các kỹ năng nổi bật gồm:

- LLM/GenAI.
- PostgreSQL.
- Linux.

Đối với Random Forest, các kỹ năng nổi bật gồm:

- Machine Learning.
- LLM/GenAI.
- Python.

Những kết quả này cho thấy mô hình sử dụng cả kinh nghiệm và kỹ năng chuyên môn để phân lớp khoảng lương, trong đó số năm kinh nghiệm có mức đóng góp lớn nhất theo chỉ số Feature Importance.

Tuy nhiên, Feature Importance phản ánh mức độ đóng góp vào các phép chia của mô hình, không thể sử dụng trực tiếp để kết luận rằng một thuộc tính là nguyên nhân làm tăng mức lương.

#### 3.2.4. Các kỹ năng liên quan đến nhóm lương Trên 30M

Kết quả phân tích các tin tuyển dụng thuộc nhóm lương Trên 30M cho thấy một số kỹ năng chuyên sâu có tỷ lệ xuất hiện trong nhóm lương cao tương đối lớn.

| Kỹ năng | Số tin yêu cầu kỹ năng | Tin Trên 30M | Tỷ lệ (%) |
|---|---:|---:|---:|
| NLP | 54 | 37 | 68,52 |
| MLOps | 58 | 39 | 67,24 |
| Deep Learning | 73 | 49 | 67,12 |
| Machine Learning | 245 | 153 | 62,45 |
| LLM/GenAI | 258 | 150 | 58,14 |

*Tỷ lệ được tính trong số các tin có yêu cầu từng kỹ năng, với điều kiện kỹ năng xuất hiện trong ít nhất 30 tin tuyển dụng.*

Trong số các kỹ năng được xét, NLP có tỷ lệ thuộc nhóm Trên 30M cao nhất, đạt 68,52%.

MLOps và Deep Learning cũng có tỷ lệ cao, lần lượt đạt 67,24% và 67,12%.

Đặc biệt, Machine Learning và LLM/GenAI xuất hiện trong số lượng tương đối lớn các tin tuyển dụng thuộc nhóm Trên 30M, lần lượt là 153 và 150 tin.

Kết quả này cho thấy một số kỹ năng chuyên sâu về Trí tuệ nhân tạo và Học máy có mối liên hệ đáng chú ý với nhóm lương cao trong bộ dữ liệu nghiên cứu.

Tuy nhiên, các kỹ năng có thể đồng thời xuất hiện với những yêu cầu khác như kinh nghiệm, cấp bậc và chuyên môn công việc. Vì vậy, không thể kết luận rằng chỉ riêng việc sở hữu một kỹ năng sẽ quyết định mức lương cao.

---

### 3.3. Hạn chế của nghiên cứu

Mặc dù đã xây dựng và đánh giá được các mô hình phân lớp, nghiên cứu vẫn tồn tại một số hạn chế.

**Thứ nhất, giới hạn về quy mô và phạm vi dữ liệu.**

Bộ dữ liệu gồm 1.547 tin tuyển dụng được thu thập từ những nền tảng tuyển dụng đã lựa chọn.

Do đó, kết quả phản ánh đặc điểm của mẫu dữ liệu nghiên cứu, chưa thể khẳng định đại diện chính xác cho toàn bộ thị trường lao động ngành Dữ liệu/CNTT tại Việt Nam.

**Thứ hai, tỷ lệ tin tuyển dụng không công bố lương cao.**

Trong tổng số 1.547 tin tuyển dụng:

- 391 tin có công bố mức lương.
- 1.156 tin ghi lương thỏa thuận.

Như vậy, khoảng 74,73% dữ liệu không có mức lương được công bố trực tiếp.

Dữ liệu đã qua tiền xử lý sử dụng giá trị lương điền khuyết để xây dựng nhãn khoảng lương cho các tin không công bố lương.

Điều này có thể ảnh hưởng đến tính chính xác của nhãn mục tiêu và kết quả đánh giá mô hình phân lớp.

**Thứ ba, giới hạn của các mô hình phân lớp.**

Hai mô hình Decision Tree và Random Forest được xây dựng với những bộ tham số thử nghiệm cụ thể.

Kết quả trên tập Test cho thấy sự khác biệt về hiệu quả phân lớp giữa các nhóm lương.

Bên cạnh đó, Accuracy trên tập Train cao hơn tập Test ở cả hai mô hình, phản ánh sự chênh lệch giữa khả năng học trên dữ liệu huấn luyện và khả năng dự đoán trên dữ liệu kiểm tra.

Vì vậy, các kết quả hiện tại chỉ phản ánh hiệu quả của những cấu hình mô hình đã thực nghiệm, chưa khẳng định đây là các cấu hình tối ưu.

**Thứ tư, giới hạn trong việc diễn giải mối liên hệ giữa kỹ năng và mức lương.**

Các kết quả Feature Importance, phân cụm, luật kết hợp và thống kê nhóm lương cao chỉ phản ánh những mối liên hệ trong dữ liệu.

Chúng không chứng minh mối quan hệ nhân quả giữa kỹ năng, kinh nghiệm và mức lương.

Đặc biệt, kết quả thống kê nhóm Trên 30M chịu ảnh hưởng từ chất lượng nhãn lương đã được xử lý.

---

### 3.4. Kết luận chung

Nghiên cứu đã áp dụng các phương pháp khai phá dữ liệu nhằm phân tích đặc điểm tuyển dụng ngành Dữ liệu và Trí tuệ nhân tạo tại Việt Nam.

Thông qua việc kết hợp EDA, K-Means, Apriori, Decision Tree và Random Forest, nhóm đã thu được những kết quả về phân bố ngành nghề, yêu cầu kỹ năng, mối liên hệ giữa các kỹ năng và khả năng phân lớp khoảng lương.

Các kết quả chính bao gồm:

1. **Phân tích khám phá dữ liệu:** Xác định SQL và Python là hai kỹ năng phổ biến trong bộ dữ liệu, đồng thời ghi nhận sự khác biệt về phân bố ngành nghề, mức lương và mô hình làm việc.

2. **Phân cụm K-Means:** Với phương án K = 3, nghiên cứu khám phá được ba chân dung nghề nghiệp gồm AI & Machine Learning, General Data & Analytics và Data Engineering & Infrastructure.

3. **Khai phá luật kết hợp Apriori:** Phát hiện các tổ hợp kỹ năng thường xuất hiện cùng nhau, đặc biệt trong nhóm kỹ năng Cloud, DevOps và cơ sở dữ liệu.

4. **Phân lớp bằng Decision Tree và Random Forest:** Cả hai mô hình đều có khả năng dự đoán nhãn khoảng lương trong bộ dữ liệu đã xử lý. Decision Tree đạt Accuracy 75,48%, cao hơn Random Forest với Accuracy 73,55% trong các cấu hình thử nghiệm.

5. **Phân tích Feature Importance:** Số năm kinh nghiệm là thuộc tính có mức độ quan trọng cao nhất trong cả hai mô hình phân lớp.

6. **Phân tích nhóm lương Trên 30M:** Những kỹ năng như NLP, MLOps, Deep Learning, Machine Learning và LLM/GenAI có mối liên hệ đáng chú ý với nhóm lương cao trong mẫu nghiên cứu.

Nhìn chung, nghiên cứu đã vận dụng các thuật toán khai phá dữ liệu để mô tả, khám phá và phân lớp dữ liệu tuyển dụng ngành Data.

Kết quả cung cấp cơ sở tham khảo về đặc điểm tuyển dụng, sự phân bố yêu cầu kỹ năng và những thuộc tính liên quan đến việc phân loại khoảng lương.

Tuy nhiên, do phần lớn tin tuyển dụng không công bố lương trực tiếp và nhãn lương có sử dụng dữ liệu điền khuyết, các kết quả phân lớp cần được diễn giải trong phạm vi bộ dữ liệu đã xử lý, không được xem là bằng chứng về khả năng dự đoán chính xác mức lương thực tế trên toàn bộ thị trường lao động.
