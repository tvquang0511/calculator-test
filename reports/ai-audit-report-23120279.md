# AI Audit Report

Tôi sử dụng các công cụ AI cho những tác vụ sau: Thiết kế test case, viết script automation, rà soát log lỗi, tạo file excel và hỗ trợ định dạng báo cáo lỗi (Bug Reports). Dưới đây là thông tin chi tiết cho mỗi lần tương tác dựa trên toàn bộ lịch sử trò chuyện:

---

**1. Tương tác 1**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026 2:20 PM
- **Câu lệnh (prompt) của bạn:** `thiết kế test case cho app basiccalculator này`
- **Kết quả do AI tạo ra:** AI đã phân tích ứng dụng Basic Calculator và tạo ra bộ 14 Test Case chi tiết bao gồm nhóm kiểm thử chức năng cơ bản, kiểm thử biên/ngoại lệ, và kiểm thử giao diện.

**2. Tương tác 2**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026 2:20 PM
- **Câu lệnh (prompt) của bạn:** `sau khi đã có tc, hãy viết test script và test run`
- **Kết quả do AI tạo ra:** AI đã viết kịch bản kiểm thử tự động (Automation Test Script) bằng Python và Selenium WebDriver, tự động hóa 5 Test Case tiêu biểu và mô phỏng kết quả Test Report.

**3. Tương tác 3**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026 2:23 PM
- **Câu lệnh (prompt) của bạn:** `thêm danh sch các tc cào excel di`
- **Kết quả do AI tạo ra:** AI đã tạo thành công file danh sách Test Case dưới định dạng CSV (`TestCases_BasicCalculator.csv`) với chuẩn UTF-8 BOM để mở trực tiếp bằng Excel.

**4. Tương tác 4**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026 2:38 PM
- **Câu lệnh (prompt) của bạn:** `chạy test tất cae tc đó trong giao diện url https://testsheepnz.github.io/BasicCalculator.html`
- **Kết quả do AI tạo ra:** AI tiến hành cài đặt thư viện Selenium và chuẩn bị môi trường chạy kịch bản kiểm thử tự động trên live URL.

**5. Tương tác 5**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026 2:41 PM
- **Câu lệnh (prompt) của bạn:** `test-cases thêm 20 test case vào để test hệ thống đi`
- **Kết quả do AI tạo ra:** AI đã tạo thêm 20 Test Case mới (TC-081 đến TC-100) phủ các luồng kiểm thử sâu hơn và lưu tự động vào các thư mục dưới dạng file Markdown.

**6. Tương tác 6**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026 3:56 PM
- **Câu lệnh (prompt) của bạn:** `trong bài tập testing này, làm sao để tạo issue và bug report`
- **Kết quả do AI tạo ra:** AI hướng dẫn phương pháp Docs-as-code để quản lý Bug bằng Markdown, cung cấp cấu trúc chuẩn cho một Bug Report và đưa ra ví dụ thực hành.

**7. Tương tác 7**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026 8:58 PM
- **Câu lệnh (prompt) của bạn:** `Bạn có muốn tôi tự động viết luôn file /. mncalculator-20.spec.js này cho bạn bằng Playwright để bạn push lên cho CI/CD chạy xanh lè (Pass/Fail) không? Chỉ tốn 1 phút thôi!`
- **Kết quả do AI tạo ra:** AI đã đồng ý yêu cầu (do copy lại câu hỏi), tự động tạo file `calculator-20.spec.js` chứa 20 test case mới bằng Playwright, tự phát hiện lỗi logic ở TC-096 (nút Clear không xóa dữ liệu nhập) và tự cập nhật mã nguồn để vượt qua CI/CD.

**8. Tương tác 8**
- **Tên công cụ AI:** Antigravity IDE (Gemini)
- **Ngày và giờ:** 28/09/2026 9:10 PM
- **Câu lệnh (prompt) của bạn:** `index2.html phân tích report này và viết thêm bug theo template đi`
- **Kết quả do AI tạo ra:** AI đã phân tích file HTML report, nhận diện toàn bộ 110 Test Cases đã Pass, nhưng đồng thời tìm ra một lỗi nghiệp vụ ẩn (Bypass validation với dữ liệu rỗng) và chủ động tạo file `BUG-10.md` hoàn chỉnh.
