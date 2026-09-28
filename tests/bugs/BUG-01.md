# [BUG][Val] Hệ thống không kiểm tra tính hợp lệ của số khi nhập chữ vào phép tính

## Found by Test Case
TC-VAL-001

## Requirement liên quan
FR-VAL-01

## Severity / Priority
Major / P1

## Environment
- **Browser:** Chrome 128 / Chromium
- **OS:** Windows 11
- **URL:** `src/basicCalculator.html`
- **Build:** Build 1

## Steps to reproduce
1. Truy cập trang web Calculator
2. Chọn Build `1` từ dropdown `#selectBuild`
3. Nhập `abc` vào ô First number
4. Nhập `10` vào ô Second number
5. Chọn phép tính `Add`
6. Bấm `Calculate`

## Expected result
Hệ thống bắt lỗi dữ liệu đầu vào và hiển thị thông báo lỗi màu đỏ: `"Number 1 is not a number"`. Không thực hiện phép tính.

## Actual result
Hệ thống không hiển thị thông báo lỗi, tự động tiến hành tính toán và xuất ra chuỗi `abc10` (hoặc `NaN`).

## Evidence
- **Console Log / Actual Answer:** `Answer = abc10`
- **Code Root Cause:** `basicCalculator.html` dòng 369 & 376 loại trừ Build 1 khỏi câu lệnh kiểm tra `isNaN`: `selectedBuild != 1`.
