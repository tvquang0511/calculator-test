# Test Case: TC02 - Kiểm tra Phép tính Cộng (Addition Operation)

## 1. Thông tin chung
- **Test Case ID:** `TC02_Addition_Operation`
- **Tên Test Case:** Kiểm tra tính đúng đắn của phép cộng hai số dương và phát hiện lỗi tráo đổi chức năng.
- **Module:** Math Calculation
- **Mức độ ưu tiên:** High
- **Người thực hiện:** QA/Tester

## 2. Tiền điều kiện (Pre-conditions)
- Trình duyệt đã mở trang web Calculator.

## 3. Dữ liệu kiểm thử (Test Data)
- **First Number (`#number1Field`):** `10`
- **Second Number (`#number2Field`):** `20`
- **Operation (`#selectOperationDropdown`):** `0` (Add)

## 4. Các bước thực hiện (Test Steps)
1. Chọn Build cần kiểm thử trên dropdown `#selectBuild`.
2. Nhập `10` vào ô `First number` (`#number1Field`).
3. Nhập `20` vào ô `Second number` (`#number2Field`).
4. Chọn phép tính `Add` từ dropdown `#selectOperationDropdown`.
5. Nhấp chuột vào nút `Calculate` (`#calculateButton`).
6. Chờ thông báo "Calculating ..." biến mất.
7. Đọc giá trị tại ô `Answer` (`#numberAnswerField`).

## 5. Kết quả mong đợi chuẩn (Prototype Baseline)
- Kết quả phép tính: `10 + 20 = 30`.
- Ô `#numberAnswerField` hiển thị giá trị: `30`.
- Không có thông báo lỗi hiển thị ở `#errorMsgField`.

## 6. Ghi chú phát hiện lỗi trên các Build
- **Build 2:** Bị đổi sang ghép chuỗi (Concatenate), ô `#numberAnswerField` hiển thị `1020` thay vì `30`.
- **Build 9:** Không thể thực hiện vì nút `Calculate` và ô `Second number` bị ẩn.
