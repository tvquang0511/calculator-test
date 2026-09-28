# BÁO CÁO TỔNG KẾT & PHÂN TÍCH ĐIỂM KHÁC BIỆT (DEFECT SUMMARY REPORT)

- **Dự án:** Kiểm thử tự động hóa Basic Calculator (TestSheepNZ)
- **Tài liệu tham chiếu:** [basicCalculator.html](file:///d:/document/university/n4hk1/test/calculator-test/src/basicCalculator.html)
- **Tác giả:** Đội ngũ QA / Automation Test

---

## 1. Mục tiêu Kiểm thử
Xây dựng và thực thi bộ kiểm thử tự động (Automation Test Suite) nhằm:
1. Xác định hành vi chuẩn trên phiên bản **Prototype**.
2. Tìm ra chính xác các khiếm khuyết (Bugs/Defects) và điểm khác biệt trong từng phiên bản từ **Build 1 đến Build 9**.

---

## 2. Bảng Tổng hợp Điểm Khác Biệt & Phân loại Khiếm khuyết

| STT | Phiên bản | Test Case vi phạm | Hành vi sai lệch thực tế | Hành vi chuẩn (Prototype) | Nguyên nhân mã nguồn (Code Root Cause) | Mức độ nghiêm trọng |
| :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| 1 | **Build 1** | `TC07` | Bỏ qua kiểm tra kiểu số; nhập chữ vẫn tính và trả về `NaN` hoặc ghép chuỗi `abc10` | Bắt lỗi dữ liệu và hiển thị: `"Number 1 is not a number"` | Dòng 369 & 376 loại trừ Build 1: `selectedBuild != 1` | **High** |
| 2 | **Build 2** | `TC02`, `TC06` | Tráo đổi ngược logic giữa `Add` và `Concatenate` (`Add` thành nối chuỗi, `Concatenate` thành cộng) | Phép tính nào thực hiện đúng nghiệp vụ phép tính đó | Dòng 347–356 hoán đổi giá trị selection 0 và 4 | **Critical** |
| 3 | **Build 3** | `TC06` | Luôn ép mọi input là số; chặn không cho ghép chuỗi văn bản bằng cảnh báo lỗi | Cho phép ghép chuỗi văn bản tự do | Dòng 313–317 luôn ép `isNumber = true` nếu `selectedBuild == 3` | **High** |
| 4 | **Build 4** | `TC04`, `TC08` | Checkbox "Integers only" bị khóa cứng (disabled & checked), luôn ép kết quả về số nguyên | Người dùng tùy ý bật/tắt checkbox để lấy số thực | Dòng 492–504 set `disabled = true` và `checked = true` | **Medium** |
| 5 | **Build 5** | `TC09` | Nút "Clear" bị vô hiệu hóa (`disabled = true`) ngay khi chọn Build, không thể nhấp | Nút "Clear" luôn sẵn sàng hoạt động | Dòng 451–455 gán `clearButton.disabled = true` | **Medium** |
| 6 | **Build 6** | `TC05` | Bỏ qua kiểm tra chia cho 0, hiển thị kết quả là `Infinity` | Báo lỗi màu đỏ: `"Divide by zero error!"` | Dòng 399 bỏ qua điều kiện: `selectedBuild != 6` | **High** |
| 7 | **Build 7** | `TC10` | Lấy giá trị của ô Answer cũ làm First Number cho lần tính tiếp theo | Luôn lấy đúng giá trị người dùng nhập trong ô First Number | Dòng 361–363 gán `num1 = answer;` | **Critical** |
| 8 | **Build 8** | `TC03`, `TC04` | Hoán đổi giá trị giữa Number 1 và Number 2 trước khi tính toán ($15 - 5$ thành $5 - 15 = -10$) | Giữ nguyên đúng thứ tự người dùng đã nhập | Dòng 363–367 hoán đổi vị trí: `num1 = num2; num2 = temp;` | **Critical** |
| 9 | **Build 9** | `TC01` - `TC10` | Ẩn và vô hiệu hóa ô `Second number` cùng nút `Calculate`, làm tê liệt toàn bộ ứng dụng | Giao diện đầy đủ và các chức năng hoạt động bình thường | Dòng 457–468 set `hidden = true` và `disabled = true` | **Blocker** |

---

## 3. Đánh giá Chất lượng & Khuyến nghị
1. **Tính độc lập giữa các phiên bản:** Các lỗi trong Builds 1-9 bao phủ đầy đủ các khía cạnh kiểm thử: UI Availability, Validation, Business Logic, Exception Handling, và State Management.
2. **Khuyến nghị tự động hóa:**
   - Sử dụng script Playwright `tests/test-runner.js` để tự động hóa việc quét toàn bộ các phiên bản trong vòng dưới 10 giây.
   - Thiết lập báo cáo CI/CD để tự động tạo ma trận so sánh sau mỗi lần có bản Build mới.
