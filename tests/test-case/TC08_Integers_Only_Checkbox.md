# Test Case: TC08 - Kiểm tra Chức năng và Trạng thái của Checkbox "Integers only"

## 1. Thông tin chung
- **Test Case ID:** `TC08_Integers_Only_Checkbox`
- **Tên Test Case:** Kiểm tra khả năng bật/tắt checkbox Integers only và làm tròn số nguyên chính xác.
- **Module:** Math Calculation / UI Setting
- **Mức độ ưu tiên:** High
- **Người thực hiện:** QA/Tester

## 2. Tiền điều kiện (Pre-conditions)
- Trình duyệt đã mở trang web Calculator.

## 3. Dữ liệu kiểm thử (Test Data)
- **First Number (`#number1Field`):** `5.8`
- **Second Number (`#number2Field`):** `1`
- **Operation (`#selectOperationDropdown`):** `3` (Divide)

## 4. Các bước thực hiện (Test Steps)
1. Chọn Build cần kiểm thử trên dropdown `#selectBuild`.
2. Kiểm tra xem checkbox `#integerSelect` có bị khóa (disabled) hay không.
3. Chọn phép tính `Divide`.
4. Nhập `5.8` vào First number và `1` vào Second number.
5. Tích chọn checkbox `#integerSelect`.
6. Nhấp `Calculate`, chờ loading và đọc kết quả ở `#numberAnswerField`.
7. Click bỏ chọn checkbox `#integerSelect` và đọc lại kết quả tại ô `Answer`.

## 5. Kết quả mong đợi chuẩn (Prototype Baseline)
- Checkbox `#integerSelect` cho phép người dùng bật/tắt linh hoạt (`isEnabled()`).
- Khi tích chọn: `Answer` hiển thị phần nguyên là `5` (`parseInt(5.8)`).
- Khi bỏ tích chọn: `Answer` tự động chuyển lại giá trị số thực là `5.8`.

## 6. Ghi chú phát hiện lỗi trên các Build
- **Build 4:** Checkbox `#integerSelect` bị khóa cứng (`disabled = true`) và luôn ở trạng thái được tích (`checked = true`), người dùng không thể đổi về số thực.
- **Build 9:** Không thực hiện được do UI bị ẩn.
