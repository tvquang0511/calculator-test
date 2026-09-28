# [BUG][Math] Lấy giá trị Answer cũ thay thế cho First number ở lần tính tiếp theo

## Found by Test Case
TC-MATH-005

## Requirement liên quan
FR-MATH-05

## Severity / Priority
Critical / P0

## Environment
- **Browser:** Chrome 128 / Chromium
- **OS:** Windows 11
- **URL:** src/basicCalculator.html
- **Build:** Build 7

## Steps to reproduce
1. Chọn Build 7
2. Lần 1: Nhập 2 + 3, bấm Calculate -> Answer = 5
3. Lần 2: Nhập First number = 10, Second number = 20, bấm Calculate

## Expected result
Lần 2 Answer = 30 (10 + 20).

## Actual result
Lần 2 Answer = 25 (Hệ thống lấy Answer cũ là 5 thế vào First number: 5 + 20 = 25).

## Evidence
- basicCalculator.html dòng 361-363 gán num1 = answer;
