# AI AUDIT REPORT

- **Mã nhóm:** Nhom02
- **Họ và tên / MSSV:** 23120372
- **Dự án:** Basic Calculator Automation Testing
- **Ngày lập:** 2026-09-28

---

## Tuyên bố sử dụng AI
> **Tôi sử dụng các công cụ AI cho những tác vụ sau:**
> 1. Phân tích chức năng và đặc tả hành vi của ứng dụng web Basic Calculator (`https://testsheepnz.github.io/BasicCalculator.html`).
> 2. Thiết kế danh sách Test Scenarios và chi tiết 80 Test Cases áp dụng các kỹ thuật EP, BVA, Error Guessing, Negative Testing, Dependency Testing.
> 3. Lập Ma trận bao phủ kiểm thử (Test Coverage Matrix) và tổng hợp danh sách các yêu cầu còn mơ hồ (Requirement Ambiguities).
> 4. Xuất toàn bộ dữ liệu thiết kế kiểm thử thành tệp bảng tính Excel (`Basic_Calculator_Test_Design.xlsx`) đa sheet chuẩn quốc tế.
> 5. Xây dựng và triển khai Automation Test Framework bằng Playwright sử dụng mô hình Page Object Model (POM) để tự động hóa 80 Test Cases.
> 6. Đồng bộ mã nguồn, cấu hình CI/CD GitHub Actions, chuẩn hóa cấu trúc repository và kiểm tra tính tương thích của các template theo chuẩn quản lý QA trên GitHub.

---

## Nhật ký chi tiết các lần tương tác với AI

### Lần tương tác 1: Thiết kế Kịch bản kiểm thử (Test Scenario) và Test Case toàn diện
- **Tên công cụ AI:** Google Antigravity IDE (Mô hình: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 14:15:02 (GMT+7)
- **Câu lệnh (Prompt):**
  > "Bạn là một Senior Software Tester / QA Engineer có kinh nghiệm thiết kế Test Scenario và Test Case. Hãy thiết kế kịch bản kiểm thử (Test Scenario) và Test Case cho website: https://testsheepnz.github.io/BasicCalculator.html... [Yêu cầu đầy đủ 5 phần: Functional Analysis, Test Scenarios, Test Cases, Coverage Matrix, Requirement / Ambiguity, không làm sơ sài, bao phủ toàn bộ số âm, 0, thập phân, chia cho 0, Integers only, Concatenate, Builds 1-9]"
- **Kết quả do AI tạo ra:**
  - Báo cáo phân tích chức năng (Input fields, Operations, Integers only, Calculate, Clear, Error Label, Builds 0-9).
  - Danh sách 13 Test Scenarios (`TS-001` đến `TS-013`).
  - Bộ 80 Test Cases chi tiết (`TC-001` đến `TC-080`) chuẩn cấu trúc 10 cột, có Step rõ ràng, dữ liệu cụ thể và Expected Result quan sát được.
  - Ma trận bao phủ 11 nhóm tính năng và danh sách 6 điểm mơ hồ / lỗi tiềm năng trong requirement (như chuỗi rỗng bị coi là 0, bug treo giao diện khi chia cho 0 trên Prototype, cơ chế truncate của `parseInt`).

---

### Lần tương tác 2: Xuất dữ liệu kiểm thử thành file Excel chuyên nghiệp
- **Tên công cụ AI:** Google Antigravity IDE (Mô hình: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 14:34:02 (GMT+7)
- **Câu lệnh (Prompt):**
  > "xuất thành file excel"
- **Kết quả do AI tạo ra:**
  - Viết script Python `export_test_cases_to_excel.py` sử dụng thư viện `openpyxl`.
  - Sinh thành công file Excel `Basic_Calculator_Test_Design.xlsx` gồm 5 sheet: `Functional Analysis`, `Test Scenarios`, `Test Cases`, `Coverage Matrix`, `Requirement Ambiguities` với định dạng màu sắc trực quan, tự động căn chỉnh độ rộng cột và bọc chữ (wrap text).

---

### Lần tương tác 3: Xây dựng Playwright Automation Test Framework cho 80 Test Cases
- **Tên công cụ AI:** Google Antigravity IDE (Mô hình: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 14:37:50 (GMT+7)
- **Câu lệnh (Prompt):**
  > "viết script playwright kiểm thử tất cả test case đã sinh"
- **Kết quả do AI tạo ra:**
  - Cài đặt `@playwright/test` và thiết lập cấu hình `playwright.config.js`.
  - Xây dựng Page Object Model `pages/CalculatorPage.js` bao bọc mọi selector và hành vi tương tác trên giao diện.
  - Viết file test suite `tests/calculator.spec.js` tự động hóa toàn bộ 80 Test Cases từ `TC-001` đến `TC-080`.
  - Chạy thực tế bằng 4 workers trên Google Chrome Headless, đạt kết quả 80/80 passed (100%).

---

### Lần tương tác 4: Đọc Git Repository từ xa, chuẩn hóa cấu trúc thư mục và Push
- **Tên công cụ AI:** Google Antigravity IDE (Mô hình: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 14:52:34 (GMT+7)
- **Câu lệnh (Prompt):**
  > "https://github.com/tvquang0511/calculator-test đọc repo và pull về. Kiểm tra thay đổi cấu trúc thư mục của tôi và thực hiện push lên repo cho chuẩn như cấu trúc repo hiện tại(hãy hỏi lại tôi nếu cần thêm thông tin)"
- **Kết quả do AI tạo ra:**
  - Đọc và phân tích cấu trúc repository remote `tvquang0511/calculator-test`.
  - Trao đổi xác nhận với người dùng về phương án lưu trữ file test mở rộng (tạo thư mục riêng `tests/comprehensive/`) và vị trí lưu file Excel (thư mục gốc).
  - Khởi tạo `.gitignore`, chuyển đổi Page Object Model và test suite sang ES Modules (`type: module`), cập nhật `package.json` và cấu hình Playwright tương thích với cả Windows local và GitHub Actions CI.
  - Thực hiện commit và push thành công lên nhánh `main` (`commit 0f48137`).

---

### Lần tương tác 5: Bổ sung các Issue Template và Báo cáo Regression theo chuẩn
- **Tên công cụ AI:** Google Antigravity IDE (Mô hình: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 15:22:07 (GMT+7)
- **Câu lệnh (Prompt):**
  > "project-root/
  > ├── src/
  > ├── tests/
  > │   ├── test-cases/
  > │   │   ├── login/
  > │   │   │   ├── TC-LOGIN-001.md
  > │   │   │   └── TC-LOGIN-002.md
  > │   │   ├── register/
  > │   │   └── checkout/
  > │   ├── test-runs/
  > │   │   ├── sprint-1-test-run.md
  > │   │   └── sprint-2-regression.md
  > │   └── test-summary/
  > │       └── traceability-matrix.md
  > └── .github/ISSUE_TEMPLATE/
  > 
  > test-cases/: thiết kế test case chính thức
  > test-runs/: kết quả thực thi theo sprint hoặc đợt regression
  > test-summary/: báo cáo tổng hợp và traceability matrix
  > .github/ISSUE_TEMPLATE/: mẫu Bug Report, Test Task, Test Run
  > 
  > đọc cấu trúc này và kiểm tra project của tôi đã có đầy đủ chưa"
- **Kết quả do AI tạo ra:**
  - Đối chiếu toàn bộ cây thư mục với chuẩn yêu cầu của môn học.
  - Phát hiện thiếu 2 template issue (`test_task.md`, `test_run.md`) và file báo cáo đợt kiểm thử hồi quy `sprint-2-regression.md`.
  - Tạo mới hoàn chỉnh 3 file trên và push lên GitHub (`commit c884d2e`).

---

### Lần tương tác 6: Đồng bộ mã nguồn mới nhất sau khi tạo 80 file Markdown Test Cases
- **Tên công cụ AI:** Google Antigravity IDE (Mô hình: Gemini 3.8 Flash)
- **Ngày và giờ:** 2026-09-28 15:34:07 (GMT+7)
- **Câu lệnh (Prompt):**
  > "pull code mới nhất"
- **Kết quả do AI tạo ra:**
  - Thực hiện `git pull origin main` kéo về 80 file Markdown chi tiết trong `tests/test-cases/` chia theo các thư mục `math/`, `str/`, `ui/`, `val/`, `build/`.
  - Chạy kiểm thử tự động toàn bộ 90 tests (10 baseline + 80 comprehensive), ghi nhận 90/90 passed (100%).
