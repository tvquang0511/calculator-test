# Test Case: TC09 - Kiểm tra Chức năng Nút "Clear" (Reset State)

## 1. Thông tin chung
- **Test Case ID:** `TC09_Clear_Button_Functionality`
- **Tên Test Case:** Kiểm tra khả năng xóa dữ liệu, làm sạch lỗi và reset checkbox của nút Clear.
- **Module:** UI State / Reset
- **Mức độ ưu tiên:** High
- **Người thực hiện:** QA/Tester

## 2. Tiền điều kiện (Pre-conditions)
- Trình duyệt đã mở trang web Calculator.

## 3. Dữ liệu kiểm thử (Test Data)
- Đang có giá trị trong ô `Answer` và có lỗi hiển thị.

## 4. Các bước thực hiện (Test Steps)
1. Chọn Build cần kiểm thử trên dropdown `#selectBuild`.
2. Kiểm tra xem nút `#clearButton` có bị vô hiệu hóa hay không.
3. Thực hiện một phép tính để có kết quả hiển thị trên `#numberAnswerField`.
4. Nhấp chuột vào nút `Clear` (`#clearButton`).
5. Quan sát ô `Answer`, thông báo lỗi `#errorMsgField` và checkbox `#integerSelect`.

## 5. Kết quả mong đợi chuẩn (Prototype Baseline)
- Nút `#clearButton` luôn ở trạng thái sẵn sàng nhấp (`isEnabled()`).
- Sau khi nhấp `Clear`:
  - Ô `Answer` bị xóa rỗng (`""`).
  - Thông báo lỗi bị xóa hoàn toàn.
  - Checkbox `#integerSelect` tự động bỏ chọn (`checked = false`).

## 6. Ghi chú phát hiện lỗi trên các Build
- **Build 5:** Nút `#clearButton` bị vô hiệu hóa hoàn toàn (`disabled = true`) ngay khi chọn Build 5, người dùng không thể bấm Clear.
