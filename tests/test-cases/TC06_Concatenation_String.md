# Test Case: TC06 - Kiểm tra Ghép Chuỗi Văn Bản (Concatenate Strings)

## 1. Thông tin chung
- **Test Case ID:** `TC06_Concatenation_String`
- **Tên Test Case:** Kiểm tra chức năng ghép chuỗi ký tự không phải số và đảm bảo không bị chặn bởi hàm kiểm tra số.
- **Module:** String Operation
- **Mức độ ưu tiên:** High
- **Người thực hiện:** QA/Tester

## 2. Tiền điều kiện (Pre-conditions)
- Trình duyệt đã mở trang web Calculator.

## 3. Dữ liệu kiểm thử (Test Data)
- **First Number (`#number1Field`):** `Hello`
- **Second Number (`#number2Field`):** `World`
- **Operation (`#selectOperationDropdown`):** `4` (Concatenate)

## 4. Các bước thực hiện (Test Steps)
1. Chọn Build cần kiểm thử trên dropdown `#selectBuild`.
2. Chọn phép tính `Concatenate` từ dropdown `#selectOperationDropdown`.
3. Nhập `Hello` vào ô `First number`.
4. Nhập `World` vào ô `Second number`.
5. Nhấp chuột vào nút `Calculate`.
6. Chờ thông báo loading biến mất.
7. Đọc giá trị tại ô `Answer` và kiểm tra thông báo lỗi `#errorMsgField`.

## 5. Kết quả mong đợi chuẩn (Prototype Baseline)
- Ô `#numberAnswerField` hiển thị giá trị: `HelloWorld`.
- Không có bất kỳ thông báo lỗi nào ở `#errorMsgField`.
- Checkbox `Integers only` tự động bị ẩn khi chọn Concatenate.

## 6. Ghi chú phát hiện lỗi trên các Build
- **Build 3:** Luôn coi mọi input là số, báo lỗi `"Number 1 is not a number"`, không cho phép ghép chuỗi chữ cái.
- **Build 2:** Bị tráo thành phép cộng (Add), do chuỗi chữ cái cộng lại thành `NaN` hoặc báo lỗi.
- **Build 8:** Ghép ngược thành `WorldHello`.
- **Build 9:** Không thực hiện được do UI bị ẩn.
