# Test Case: TC04 - Kiểm tra Phép tính Chia ra số thập phân

## 1. Thông tin chung
- **Test Case ID:** `TC04_Division_Decimal_Result`
- **Tên Test Case:** Kiểm tra phép chia cho ra số thực thập phân chính xác khi không bật "Integers only".
- **Module:** Math Calculation
- **Mức độ ưu tiên:** High
- **Người thực hiện:** QA/Tester

## 2. Tiền điều kiện (Pre-conditions)
- Trình duyệt đã mở trang web Calculator.

## 3. Dữ liệu kiểm thử (Test Data)
- **First Number (`#number1Field`):** `7`
- **Second Number (`#number2Field`):** `2`
- **Operation (`#selectOperationDropdown`):** `3` (Divide)

## 4. Các bước thực hiện (Test Steps)
1. Chọn Build cần kiểm thử trên dropdown `#selectBuild`.
2. Đảm bảo checkbox `Integers only` không được chọn (nếu có thể tương tác).
3. Nhập `7` vào ô `First number`.
4. Nhập `2` vào ô `Second number`.
5. Chọn phép tính `Divide` từ dropdown `#selectOperationDropdown`.
6. Nhấp chuột vào nút `Calculate`.
7. Chờ thông báo loading biến mất.
8. Đọc giá trị tại ô `Answer`.

## 5. Kết quả mong đợi chuẩn (Prototype Baseline)
- Kết quả phép tính: $7 / 2 = 3.5$.
- Ô `#numberAnswerField` hiển thị giá trị: `3.5`.
- Không có lỗi hiển thị.

## 6. Ghi chú phát hiện lỗi trên các Build
- **Build 4:** Bị khóa cứng ở chế độ Integers only, trả về `3` thay vì `3.5`.
- **Build 8:** Đảo ngược vị trí thành $2 / 7$, trả về xấp xỉ `0.285714...` thay vì `3.5`.
- **Build 9:** Không thực hiện được do UI bị ẩn.
