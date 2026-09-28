# [BUG][Math] Phép chia cho 0 không bắt lỗi ngoại lệ, hiển thị Infinity

## Found by Test Case
TC-MATH-004

## Requirement liên quan
FR-MATH-04

## Severity / Priority
Major / P1

## Environment
- **Browser:** Chrome 128 / Chromium
- **OS:** Windows 11
- **URL:** src/basicCalculator.html
- **Build:** Build 6

## Steps to reproduce
1. Chọn Build 6
2. Nhập First number = 10, Second number = 0
3. Chọn phép tính Divide
4. Bấm Calculate

## Expected result
Xuất hiện thông báo lỗi: Divide by zero error! Không hiển thị kết quả tính.

## Actual result
Không xuất hiện thông báo lỗi, ô Answer hiển thị giá trị Infinity.

## Evidence
- basicCalculator.html dòng 399 bỏ qua điều kiện kiểm tra selectedBuild != 6
