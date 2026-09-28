# Test Case: TC07 - Kiểm tra Bắt lỗi Nhập Ký tự không phải số (Input Validation)

## 1. Thông tin chung
- **Test Case ID:** `TC07_Input_Validation_NaN`
- **Tên Test Case:** Kiểm tra xác thực tính hợp lệ của dữ liệu đầu vào trong các phép tính toán học.
- **Module:** Validation / Error Handling
- **Mức độ ưu tiên:** High
- **Người thực hiện:** QA/Tester

## 2. Tiền điều kiện (Pre-conditions)
- Trình duyệt đã mở trang web Calculator.

## 3. Dữ liệu kiểm thử (Test Data)
- **First Number (`#number1Field`):** `abc`
- **Second Number (`#number2Field`):** `10`
- **Operation (`#selectOperationDropdown`):** `0` (Add)

## 4. Các bước thực hiện (Test Steps)
1. Chọn Build cần kiểm thử trên dropdown `#selectBuild`.
2. Nhập `abc` vào ô `First number`.
3. Nhập `10` vào ô `Second number`.
4. Chọn phép tính `Add` từ dropdown `#selectOperationDropdown`.
5. Nhấp chuột vào nút `Calculate`.
6. Quan sát thông báo lỗi và trạng thái nút tính toán.

## 5. Kết quả mong đợi chuẩn (Prototype Baseline)
- Xuất hiện thông báo lỗi màu đỏ tại `#errorMsgField`: `"Number 1 is not a number"`.
- Hệ thống không tính toán và không hiển thị kết quả rác vào `#numberAnswerField`.
- Nút `Calculate` được mở khóa lại để người dùng chỉnh sửa.

## 6. Ghi chú phát hiện lỗi trên các Build
- **Build 1:** Bỏ qua hoàn toàn việc kiểm tra dữ liệu số (`selectedBuild != 1`), không báo lỗi, tiến hành tính và xuất kết quả `NaN` hoặc ghép chuỗi `abc10`.
- **Build 9:** Không thực hiện được do UI bị ẩn.
