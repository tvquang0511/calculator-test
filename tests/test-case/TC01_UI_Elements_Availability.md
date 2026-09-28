# Test Case: TC01 - Kiểm tra tính khả dụng và hiển thị của các thành phần giao diện

## 1. Thông tin chung
- **Test Case ID:** `TC01_UI_Elements_Availability`
- **Tên Test Case:** Kiểm tra các phần tử UI xuất hiện đầy đủ và không bị vô hiệu hóa bất thường khi tải Build.
- **Module:** UI & Layout
- **Mức độ ưu tiên:** Blocker / High
- **Người thực hiện:** QA/Tester

## 2. Tiền điều kiện (Pre-conditions)
- Trình duyệt đã mở trang `basicCalculator.html` (Local hoặc link Github Pages).

## 3. Dữ liệu kiểm thử (Test Data)
- **Build:** Kiểm tra trên từng Build (`Prototype`, `1` đến `9`).

## 4. Các bước thực hiện (Test Steps)
1. Truy cập vào trang web Calculator.
2. Chọn Build từ dropdown `#selectBuild`.
3. Kiểm tra sự hiện diện (visibility) và trạng thái (enabled/disabled) của các phần tử sau:
   - Ô nhập số thứ nhất (`#number1Field`)
   - Ô nhập số thứ hai (`#number2Field`)
   - Dropdown chọn phép toán (`#selectOperationDropdown`)
   - Nút tính toán (`#calculateButton`)
   - Nút xóa (`#clearButton`)
   - Ô hiển thị kết quả (`#numberAnswerField`)

## 5. Kết quả mong đợi chuẩn (Prototype Baseline)
- Tất cả các phần tử trên đều phải hiển thị đầy đủ trên màn hình (`toBeVisible()`).
- Các ô nhập liệu `#number1Field`, `#number2Field` và các nút bấm `#calculateButton`, `#clearButton` ở trạng thái sẵn sàng nhận tương tác (`toBeEnabled()`).
- Ô `#numberAnswerField` có thuộc tính `readonly`.

## 6. Ghi chú phát hiện lỗi trên các Build
- **Build 9:** Ô `#number2Field` và nút `#calculateButton` bị ẩn (`hidden = true`) và vô hiệu hóa (`disabled = true`). Test case sẽ FAIL tại Build 9.
- **Build 5:** Nút `#clearButton` bị vô hiệu hóa (`disabled = true`).
