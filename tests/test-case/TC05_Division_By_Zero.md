# Test Case: TC05 - Kiểm tra Xử lý Ngoại lệ Chia cho 0 (Divide by Zero)

## 1. Thông tin chung
- **Test Case ID:** `TC05_Division_By_Zero`
- **Tên Test Case:** Kiểm tra bắt lỗi chia cho 0 và ngăn chặn kết quả `Infinity`.
- **Module:** Math Calculation / Error Handling
- **Mức độ ưu tiên:** Critical
- **Người thực hiện:** QA/Tester

## 2. Tiền điều kiện (Pre-conditions)
- Trình duyệt đã mở trang web Calculator.

## 3. Dữ liệu kiểm thử (Test Data)
- **First Number (`#number1Field`):** `10`
- **Second Number (`#number2Field`):** `0`
- **Operation (`#selectOperationDropdown`):** `3` (Divide)

## 4. Các bước thực hiện (Test Steps)
1. Chọn Build cần kiểm thử trên dropdown `#selectBuild`.
2. Nhập `10` vào ô `First number`.
3. Nhập `0` vào ô `Second number`.
4. Chọn phép tính `Divide` từ dropdown `#selectOperationDropdown`.
5. Nhấp chuột vào nút `Calculate`.
6. Quan sát thông báo lỗi tại `#errorMsgField` và giá trị tại ô `Answer`.

## 5. Kết quả mong đợi chuẩn (Prototype Baseline)
- Thông báo lỗi màu đỏ xuất hiện: `"Divide by zero error!"`.
- Ô `#numberAnswerField` không hiển thị kết quả hoặc không được ra `Infinity`.

## 6. Ghi chú phát hiện lỗi trên các Build
- **Build 6:** Không kiểm tra phép chia cho 0, không hiển thị thông báo lỗi, ô `Answer` xuất hiện giá trị `Infinity`.
- **Build 9:** Không thực hiện được do UI bị ẩn.
