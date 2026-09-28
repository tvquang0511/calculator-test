# Test Case: TC10 - Kiểm tra Tính Độc Lập giữa các lần Tính Liên tiếp (Consecutive Calculations)

## 1. Thông tin chung
- **Test Case ID:** `TC10_Consecutive_Calculations`
- **Tên Test Case:** Kiểm tra phép tính lần sau không bị ảnh hưởng bởi kết quả của phép tính lần trước.
- **Module:** Calculation State
- **Mức độ ưu tiên:** Critical
- **Người thực hiện:** QA/Tester

## 2. Tiền điều kiện (Pre-conditions)
- Trình duyệt đã mở trang web Calculator.

## 3. Dữ liệu kiểm thử (Test Data)
- **Lần tính 1:** `Number 1 = 2`, `Number 2 = 3`, `Operation = Add` (Kết quả = 5).
- **Lần tính 2:** `Number 1 = 10`, `Number 2 = 20`, `Operation = Add`.

## 4. Các bước thực hiện (Test Steps)
1. Chọn Build cần kiểm thử trên dropdown `#selectBuild`.
2. **Thực hiện Lần tính 1:** Nhập `2` và `3`, chọn `Add`, bấm `Calculate` -> Chờ ra kết quả `5`.
3. **Thực hiện Lần tính 2:** Không bấm nút Clear, nhập đè `Number 1 = 10`, nhập `Number 2 = 20`, chọn `Add`.
4. Bấm `Calculate`.
5. Chờ loading hoàn tất và đọc kết quả ở ô `Answer`.

## 5. Kết quả mong đợi chuẩn (Prototype Baseline)
- Lần 2 tính toán đúng giá trị người dùng vừa nhập: $10 + 20 = 30$.
- Ô `#numberAnswerField` hiển thị giá trị: `30`.

## 6. Ghi chú phát hiện lỗi trên các Build
- **Build 7:** Thay vì dùng `Number 1 = 10`, hệ thống tự động lấy giá trị `Answer` cũ là `5` làm số thứ nhất ($5 + 20$), dẫn đến kết quả sai hiển thị là `25` thay vì `30`.
- **Build 9:** Không thực hiện được do UI bị ẩn.
