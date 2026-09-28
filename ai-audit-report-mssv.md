# AI Audit Report

Tôi sử dụng các công cụ AI cho những tác vụ sau: Sinh dữ liệu kiểm thử (Test Cases), tự động hóa kịch bản kiểm thử (Playwright), rà soát log lỗi CI/CD, và hỗ trợ định dạng báo cáo lỗi (Bug Reports). Dưới đây là thông tin chi tiết cho mỗi lần tương tác chính trong quá trình làm bài:

---

**1. Tạo dữ liệu Test Case và xuất ra file Excel/CSV**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026
- **Câu lệnh (prompt):** "thêm danh sach các tc cào excel di"
- **Kết quả do AI tạo ra:** AI đã viết script Python (`export_tc.py`) để xuất 90 kịch bản kiểm thử (Test Cases) hiện có ra định dạng file Excel/CSV để dễ quản lý.

**2. Khởi tạo mã nguồn Automation Test bằng Playwright**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026
- **Câu lệnh (prompt):** "chạy test tất cae tc đó trong giao diện url https://testsheepnz.github.io/BasicCalculator.html"
- **Kết quả do AI tạo ra:** AI khởi tạo cấu hình Playwright và viết mã tự động hóa (`calculator-80.spec.js`...) để tự động nhập liệu và kiểm tra trên trình duyệt Chromium.

**3. Bổ sung Test Cases để tăng độ bao phủ (Coverage)**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026
- **Câu lệnh (prompt):** "@[d:\KAN\N4\KTPM\btcalcu\tests\test-cases] thêm 20 test case vào để test hệ thống đi"
- **Kết quả do AI tạo ra:** AI tạo thêm 20 Test Cases phức tạp hơn (TC-081 đến TC-100) bao gồm các trường hợp Boundary, lỗi Null/Empty, và Edge Cases. 

**4. Hỗ trợ quy trình tạo Bug Report và Issue trên GitHub**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026
- **Câu lệnh (prompt):** "trong bài tập testing này, làm sao để tạo issue và bug report" / "title bug đặt như nào"
- **Kết quả do AI tạo ra:** AI giải thích phương pháp Docs-as-code cho Bug Report, cung cấp template Markdown chuẩn và hướng dẫn cách đặt Title Bug ngắn gọn (Ví dụ: `[BUG][Math] ...`).

**5. Hướng dẫn tư duy Exploratory Testing để tìm bug mới**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026
- **Câu lệnh (prompt):** "làm sao để biết thêm bug mới"
- **Kết quả do AI tạo ra:** AI hướng dẫn chuyển từ Scripted Testing sang Kiểm thử khám phá, gợi ý kiểm tra XSS (nhập mã HTML/JS), kiểm tra ranh giới, nhập giá trị rỗng, và kiểm thử bảo mật.

**6. Cập nhật mã tự động hóa cho 20 Test Cases mới và Debug lỗi CI/CD**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026
- **Câu lệnh (prompt):** "sao tôi đã them tc và push lên mà sao cicd vẫn chỉ chạy 90 tc" / "looix nayf la sao"
- **Kết quả do AI tạo ra:** AI nhận ra cần tạo file `calculator-20.spec.js`. Sau đó, AI đã đọc log lỗi từ CI/CD (Fail ở TC-096), phân tích nguyên nhân do nút Clear không xóa ô input, và tự động sửa mã test case, đẩy lên Github để CI/CD xanh 100%.

**7. Phân tích báo cáo Test Report và sinh Bug 10**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026
- **Câu lệnh (prompt):** "@[d:\KAN\N4\KTPM\btcalcu\index2.html] phân tích report này và viết thêm bug theo template đi"
- **Kết quả do AI tạo ra:** Mặc dù Report báo Pass 100%, AI đã tự động phát hiện ra một "Logic Flaw" của hệ thống khi nhận chuỗi rỗng `""` (Hệ thống tính là 0 thay vì báo lỗi). AI đã dựa vào đó để sinh ra file `BUG-10.md` cực kỳ chuẩn xác.
