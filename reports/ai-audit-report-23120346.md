# Báo cáo Sử dụng AI (AI Audit Report)

**Sinh viên thực hiện:** 
- Họ và tên: Tạ Vũ Quang
- Mã số sinh viên (MSSV): 23120346
- Môn học: Kiểm thử Phần mềm (Software Testing)

---

## Tuyên bố sử dụng AI
> **"Tôi sử dụng các công cụ AI cho những tác vụ sau:"**
> 1. Phân tích mã nguồn và chức năng của trang web Basic Calculator.
> 2. Thiết kế kịch bản và khung Test Case chuẩn theo bài giảng.
> 3. Hỗ trợ viết kịch bản kiểm thử tự động bằng Playwright và cấu hình GitHub Actions CI.
> 4. Viết script tự động hóa chuyển đổi 80 test case từ mã nguồn sang Markdown.
> 5. Chẩn đoán và phân tích nguyên nhân lỗi kiểm thử tự động (Debugging Test Failures).

---

## Chi tiết các lần tương tác với AI

### Lần tương tác 1: Khảo sát và thiết kế Test Case ban đầu
- **Tên công cụ AI:** Antigravity AI Assistant (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 - 14:22
- **Câu lệnh (Prompt):** 
  > *"https://testsheepnz.github.io/BasicCalculator.html thiết kế test case để kiểm thử trang web này cho tôi"*
- **Kết quả do AI tạo ra:** 
  - Phân tích mã nguồn `basicCalculator.html`, nhận diện chức năng của Prototype và 9 bản Build chứa lỗi cố ý.
  - Xây dựng bảng phân tích kỹ thuật kiểm thử (EP, BVA, Error Guessing) và đề xuất bộ test case bao phủ chức năng số học, ghép chuỗi, validation và reset giao diện.

---

### Lần tương tác 2: Tổ chức Test Suite và kịch bản Playwright
- **Tên công cụ AI:** Antigravity AI Assistant (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 - 14:29
- **Câu lệnh (Prompt):** 
  > *"bạn hãy viết các test case vào thư mục tests/test-case, mỗi test case là 1 file md, sau đó hướng dẫn tôi viết script để chạy và viết báo cáo (playwright)"*
- **Kết quả do AI tạo ra:** 
  - Tạo cấu trúc thư mục `tests/test-cases/` với 10 file Markdown đặc tả test case.
  - Cấu hình file `package.json`, `playwright.config.js`.
  - Viết kịch bản `tests/test-runner.js` để tự động mở Chromium, lặp qua 10 bản Build và xuất báo cáo `test-run-report.md` và `test-summary-report.md`.

---

### Lần tương tác 3: Chuẩn hóa theo Template bài giảng môn học
- **Tên công cụ AI:** Antigravity AI Assistant (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 - 14:43
- **Câu lệnh (Prompt):** 
  > *(Gửi kèm 2 hình ảnh chụp slide quy ước mã `TC-[MODULE]-[NUMBER]` và template file test case chuẩn)*
  > *"bạn viết lại theo quy chuẩn và template này nhé"*
- **Kết quả do AI tạo ra:** 
  - Viết lại toàn bộ test case theo quy ước `TC-[MODULE]-[NUMBER]` (`TC-UI-001`, `TC-MATH-001`, `TC-STR-001`, `TC-VAL-001`).
  - Chuẩn hóa các đề mục theo template: Requirement ID, Module/Test type/Technique, Preconditions, bảng Test Data, Test Steps, Expected Result, Status / Related bugs.

---

### Lần tương tác 4: Áp dụng quy chuẩn Quản lý Test Case & Bug Report trên GitHub
- **Tên công cụ AI:** Antigravity AI Assistant (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 - 14:50
- **Câu lệnh (Prompt):** 
  > *"bạn hãy đọc 2 file pdf nói về các quy chuẩn quản lý test case và bug report sau đó sửa lại cho phù hợp"*
- **Kết quả do AI tạo ra:** 
  - Đọc nội dung 2 tài liệu `03 - github_testcase_management.pptx.pdf` và `03 - github_bug_management.pptx.pdf`.
  - Tổ chức lại thư mục theo module: `tests/test-cases/math/`, `str/`, `ui/`, `val/`.
  - Tạo mẫu GitHub Issue Template: `.github/ISSUE_TEMPLATE/bug_report.md`.
  - Tạo cấu hình GitHub Actions CI: `.github/workflows/test.yml`.
  - Soạn sẵn 9 hồ sơ Bug chi tiết trong `tests/bugs/` (tương ứng lỗi của 9 Build).
  - Lập bảng ghi nhận Test Run (`sprint-1-test-run.md`) và Ma trận truy vết (`traceability-matrix.md`) theo đúng mẫu Slide 8 và Slide 14.

---

### Lần tương tác 5: Chẩn đoán nguyên nhân lỗi kiểm thử tự động
- **Tên công cụ AI:** Antigravity AI Assistant (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 - 15:20
- **Câu lệnh (Prompt):** 
  > *(Dán log kết quả `npm test` bị timeout tại 2 test case: TC-MATH-004 và TC-074)*
  > *"đây là lỗi gì vậy"*
- **Kết quả do AI tạo ra:** 
  - Chỉ ra lỗi 1: Mã nguồn web khi chia cho 0 bị thiếu lệnh mở khóa giao diện `unlockCalculate()`, khiến Playwright bị treo khi chờ loading spinner ẩn.
  - Chỉ ra lỗi 2: Ở Build 4, checkbox `integerSelect` bị disabled; hàm `performCalculation` cố gắng gọi `setChecked(false)` nên Playwright chờ element enabled đến hết 30s.
  - Sửa code trong `CalculatorPage.js` và `calculator.spec.js` để xử lý mượt mà cả 2 trường hợp ngoại lệ.

---

### Lần tương tác 6: Gộp 80 Test Case từ nhóm vào kho dữ liệu chuẩn
- **Tên công cụ AI:** Antigravity AI Assistant (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 - 15:28
- **Câu lệnh (Prompt):** 
  > *"80 test case kia chưa có trong folder test-cases ấy, do là tôi và bạn tôi làm hơi khác nhau, giờ làm sao để gộp lại theo chuẩn"*
- **Kết quả do AI tạo ra:** 
  - Viết script Python `convert_excel_tc_to_markdown.py` tự động đọc dữ liệu 80 test case từ file `export_test_cases_to_excel.py`.
  - Tự động sinh ra 80 file Markdown chuẩn Slide 7 vào các thư mục `math/`, `str/`, `ui/`, `val/`, `build/`.
  - Đồng bộ hóa 1-to-1 giữa file Excel, code Playwright và kho tài liệu Markdown.
