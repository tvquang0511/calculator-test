# Test Case: TC03 - Kiểm tra Phép tính Trừ (Subtraction Operation)

## 1. Thông tin chung
- **Test Case ID:** `TC03_Subtraction_Operation`
- **Tên Test Case:** Kiểm tra phép trừ và phát hiện lỗi tráo đổi thứ tự hai toán tử (Number 1 và Number 2).
- **Module:** Math Calculation
- **Mức độ ưu tiên:** High
- **Người thực hiện:** QA/Tester

## 2. Tiền điều kiện (Pre-conditions)
- Trình duyệt đã mở trang web Calculator.

## 3. Dữ liệu kiểm thử (Test Data)
- **First Number (`#number1Field`):** `15`
- **Second Number (`#number2Field`):** `5`
- **Operation (`#selectOperationDropdown`):** `1` (Subtract)

## 4. Các bước thực hiện (Test Steps)
1. Chọn Build cần kiểm thử trên dropdown `#selectBuild`.
2. Nhập `15` vào ô `First number`.
3. Nhập `5` vào ô `Second number`.
4. Chọn phép tính `Subtract` từ dropdown `#selectOperationDropdown`.
5. Nhấp chuột vào nút `Calculate`.
6. Chờ thông báo loading biến mất.
7. Đọc giá trị tại ô `Answer`.

## 5. Kết quả mong đợi chuẩn (Prototype Baseline)
- Kết quả phép tính: `15 - 5 = 10`.
- Ô `#numberAnswerField` hiển thị giá trị: `10`.
- Không có thông báo lỗi hiển thị ở `#errorMsgField`.

## 6. Ghi chú phát hiện lỗi trên các Build
- **Build 8:** Đảo ngược vị trí của Number 1 và Number 2 (tính thành $5 - 15$), kết quả hiển thị là `-10` thay vì `10`.
- **Build 9:** Không thực hiện được do UI bị ẩn.
