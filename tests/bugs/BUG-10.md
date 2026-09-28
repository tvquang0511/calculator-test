# [BUG][Val] Bỏ trống cả 2 ô Number 1 và Number 2 nhưng hệ thống không báo lỗi mà tự động tính bằng 0

## Found by Test Case
TC-090, TC-091

## Requirement liên quan
FR-VAL-01 (Yêu cầu phải kiểm tra dữ liệu đầu vào hợp lệ)

## Severity / Priority
Major / P2

## Environment
- **Browser:** Chrome 128 / Chromium
- **OS:** Windows 11
- **URL:** src/basicCalculator.html
- **Build:** Build 0 (Prototype) và các Build khác

## Steps to reproduce
1. Khởi động ứng dụng Calculator (Build 0).
2. Xóa trắng dữ liệu ở cả hai ô **Number 1** và **Number 2**.
3. Chọn phép tính **Add** (hoặc để mặc định).
4. Nhấn nút **Calculate**.

## Expected result
Hệ thống phải hiển thị thông báo lỗi `Number 1 is not a number` hoặc `Number 2 is not a number` và không thực hiện phép tính.

## Actual result
Hệ thống không hiển thị thông báo lỗi. Ở ô kết quả (Answer) hiển thị `0`. Hệ thống đã âm thầm coi chuỗi rỗng `""` là giá trị `0`.

## Evidence
- **Test Report (index2.html):** Test case `TC-090` và `TC-091` chạy qua xanh nhưng vô tình bộc lộ việc hệ thống chấp nhận chuỗi rỗng.
- **Code Root Cause:** Trong file `basicCalculator.html` (dòng 364), hàm bắt lỗi là `isNaN(num1)`. Trong JavaScript, hàm `isNaN("")` trả về `false`, nên logic kiểm tra lỗi đã bị "qua mặt". Cách fix đúng là kiểm tra thêm `num1.trim() === ""` trước khi parse.
