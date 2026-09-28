# [BUG][Math] Hoán đổi ngược logic giữa phép cộng (Add) và ghép chuỗi (Concatenate)

## Found by Test Case
TC-MATH-001, TC-STR-001

## Requirement liên quan
FR-MATH-01, FR-STR-01

## Severity / Priority
Critical / P0

## Environment
- **Browser:** Chrome 128 / Chromium
- **OS:** Windows 11
- **URL:** src/basicCalculator.html
- **Build:** Build 2

## Steps to reproduce
1. Chọn Build 2
2. Nhập First number = 10, Second number = 20
3. Chọn phép tính Add
4. Bấm Calculate
5. Đổi sang phép tính Concatenate và bấm Calculate

## Expected result
- Khi chọn Add: Answer = 30 (10 + 20)
- Khi chọn Concatenate: Answer = 1020

## Actual result
- Khi chọn Add: Answer = 1020 (ghép chuỗi)
- Khi chọn Concatenate: Answer = 30 (phép cộng)

## Evidence
- basicCalculator.html dòng 347-356 đảo ngược selection giữa 0 và 4
