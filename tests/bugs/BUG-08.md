# [BUG][Math] Hoán đổi vị trí giữa First number và Second number trước khi tính toán

## Found by Test Case
TC-MATH-002, TC-MATH-003

## Requirement liên quan
FR-MATH-02, FR-MATH-03

## Severity / Priority
Critical / P0

## Environment
- **Browser:** Chrome 128 / Chromium
- **OS:** Windows 11
- **URL:** src/basicCalculator.html
- **Build:** Build 8

## Steps to reproduce
1. Chọn Build 8
2. Nhập First number = 15, Second number = 5
3. Chọn phép tính Subtract
4. Bấm Calculate

## Expected result
Answer = 10 (15 - 5).

## Actual result
Answer = -10 (Hệ thống tính 5 - 15 = -10).

## Evidence
- basicCalculator.html dòng 363-367 hoán đổi vị trí: var temp = num1; num1 = num2; num2 = temp;
