# AI Audit Report

Tôi sử dụng các công cụ AI cho những tác vụ sau: Phân tích mã nguồn và chức năng của ứng dụng Basic Calculator, thiết kế các kịch bản kiểm thử (Test Cases), viết script automation bằng Playwright, chuẩn hóa thư mục và định dạng báo cáo theo quy chuẩn GitHub QA, đồng bộ dữ liệu test case từ Excel sang Markdown, chẩn đoán lỗi kiểm thử tự động trên CI/CD. Dưới đây là thông tin chi tiết cho mỗi lần tương tác dựa trên toàn bộ lịch sử trò chuyện:

---

**1. Tương tác 1**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 2:21 PM
- **Câu lệnh (prompt) của bạn:** `https://testsheepnz.github.io/BasicCalculator.html thiết kế test case để kiểm thử trang web này cho tôi`
- **Kết quả do AI tạo ra:** AI đã cào mã nguồn `basicCalculator.html`, phân tích chức năng các trường nhập liệu, phép toán và 9 bản Build chứa lỗi. AI đề xuất bộ khung kiểm thử gồm các kỹ thuật Phân vùng tương đương (EP), Phân tích giá trị biên (BVA) và Đoán lỗi.

**2. Tương tác 2**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 2:27 PM
- **Câu lệnh (prompt) của bạn:** `bạn có viết các test case dựa trên file html chưa, có 9 prototype, tôi cần một bộ test case mẫu để chạy test run cho 9 prototype này, sau đó viết báo cáo tìm điểm khác biệt`
- **Kết quả do AI tạo ra:** AI xây dựng bộ 10 Test Case mẫu tinh gọn bao phủ các nhánh lỗi của 9 Build, lập bảng Ma trận kết quả thực thi (Execution Matrix) và viết báo cáo đối chiếu nguyên nhân gây lỗi chi tiết trong mã nguồn JavaScript.

**3. Tương tác 3**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 2:29 PM
- **Câu lệnh (prompt) của bạn:** `bạn hãy viết các test case vào thư mục tests/test-case, mỗi test case là 1 file md, sau đó hướng dẫn tôi viết script để chạy và viết báo cáo (playwright)`
- **Kết quả do AI tạo ra:** AI tạo các file Markdown đặc tả test case, cấu hình `package.json`, `playwright.config.js`, và viết script `tests/test-runner.js` tự động quét 10 Build và sinh file báo cáo `test-run-report.md` và `test-summary-report.md`.

**4. Tương tác 4**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 2:39 PM
- **Câu lệnh (prompt) của bạn:** `có 2 folder test case, playwright đang chạy folder nào để tôi xóa cái còn lại`
- **Kết quả do AI tạo ra:** AI giải thích Playwright chỉ chạy các file kịch bản `.spec.js` chứ không chạy file `.md`, đồng thời tư vấn giữ lại thư mục chuẩn `tests/test-cases` và hướng dẫn câu lệnh `git rm` để xóa thư mục trùng lặp.

**5. Tương tác 5**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 2:43 PM
- **Câu lệnh (prompt) của bạn:** `bạn viết lại theo quy chuẩn và template này nhé` *(Đính kèm 2 ảnh slide quy ước mã TC-[MODULE]-[NUMBER] và template Markdown chuẩn)*
- **Kết quả do AI tạo ra:** AI viết lại toàn bộ các test case theo mã chuẩn (`TC-UI-001`, `TC-MATH-001`, `TC-STR-001`, `TC-VAL-001`), cấu trúc đầy đủ các trường: Requirement ID, Preconditions, bảng Test Data, Steps, Expected Result, Status / Related bugs.

**6. Tương tác 6**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 2:49 PM
- **Câu lệnh (prompt) của bạn:** `bạn hãy đọc 2 file pdf nói về các quy chuẩn quản lý test case và bug report sau đó sửa lại cho phù hợp`
- **Kết quả do AI tạo ra:** AI đọc 2 tài liệu slide PDF, tổ chức lại thư mục test case theo module con (`math/`, `str/`, `ui/`, `val/`), tạo Issue Template `.github/ISSUE_TEMPLATE/bug_report.md`, cấu hình CI `.github/workflows/test.yml`, sinh 9 file hồ sơ bug trong `tests/bugs/`, và lập bảng Traceability Matrix theo Slide 14.

**7. Tương tác 7**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 3:05 PM
- **Câu lệnh (prompt) của bạn:** `giải thích luồng test cho tôi hiểu nhé`
- **Kết quả do AI tạo ra:** AI vẽ sơ đồ Mermaid và giải thích chi tiết chu trình 7 bước: Requirement $\rightarrow$ Test Case $\rightarrow$ Test Run $\rightarrow$ Bug Report $\rightarrow$ Fix in PR $\rightarrow$ Retest $\rightarrow$ Traceability Matrix.

**8. Tương tác 8**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 3:12 PM
- **Câu lệnh (prompt) của bạn:** `file nào sẽ chạy test case, và test runs được sinh tự động khi chạy test hay sao, và khi tìm được bug thì report lại hay có tự động tạo issue hay không`
- **Kết quả do AI tạo ra:** AI làm rõ vai trò của 2 file thực thi (`test-runner.js` và `calculator.spec.js`), xác nhận cơ chế tự động ghi đè file kết quả test run và hướng dẫn 2 cách tạo Issue (thủ công qua Web/Template hoặc tự động hóa bằng GitHub CLI).

**9. Tương tác 9**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 3:14 PM
- **Câu lệnh (prompt) của bạn:** `cái build là cái gì vậy`
- **Kết quả do AI tạo ra:** AI giải thích khái niệm Software Build trong kỹ thuật phần mềm và mục đích thực tế của menu Build trên trang web Basic Calculator (Prototype là bản chuẩn, Build 1-9 là các bản lỗi để thử tài Tester).

**10. Tương tác 10**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 3:20 PM
- **Câu lệnh (prompt) của bạn:** `Run npm test ... 2 failed ... đây là lỗi gì vậy`
- **Kết quả do AI tạo ra:** AI phân tích log lỗi timeout 30s của GitHub Actions: chỉ ra lỗi 1 do trang web quên mở khóa spinner khi chia cho 0, lỗi 2 do kịch bản cố click checkbox bị disabled ở Build 4. AI đã sửa mã nguồn `CalculatorPage.js` và `calculator.spec.js` để vượt qua 90/90 tests.

**11. Tương tác 11**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 3:27 PM
- **Câu lệnh (prompt) của bạn:** `80 test case kia chưa có trong folder test-cases ấy, do là tôi và bạn tôi làm hơi khác nhau, giờ làm sao để gộp lại theo chuẩn`
- **Kết quả do AI tạo ra:** AI viết script Python `convert_excel_tc_to_markdown.py` tự động trích xuất 80 Test Case từ file Excel / Python của bạn cùng nhóm và chuyển đổi sang 80 file Markdown chuẩn Slide 7 vào đúng các thư mục module.

**12. Tương tác 12**
- **Tên công cụ AI:** Antigravity IDE (Gemini 3.8 Flash)
- **Ngày và giờ:** 28/09/2026 10:51 PM
- **Câu lệnh (prompt) của bạn:** `tôi thấy trong bug report có các FR ấy nhưng khi tìm lại không thấy, nó nằm ở đâu vậy`
- **Kết quả do AI tạo ra:** AI giải thích nguồn gốc các mã FR (Functional Requirements) được chuẩn hóa từ phần Instructions của trang web để phục vụ Traceability Matrix, đồng thời tạo file tài liệu độc lập `tests/functional-requirements.md` đặc tả chi tiết 11 yêu cầu chức năng.
