# [BUG][Str] Phép ghép chuỗi luôn coi dữ liệu là số, chặn ghép chuỗi chữ cái

## Found by Test Case
TC-STR-001

## Requirement liên quan
FR-STR-01

## Severity / Priority
Major / P1

## Environment
- **Browser:** Chrome 128 / Chromium
- **OS:** Windows 11
- **URL:** src/basicCalculator.html
- **Build:** Build 3

## Steps to reproduce
1. Chọn Build 3
2. Chọn phép tính Concatenate
3. Nhập First number = Hello, Second number = World
4. Bấm Calculate

## Expected result
Answer = HelloWorld, không báo lỗi định dạng số.

## Actual result
Hệ thống báo lỗi màu đỏ: Number 1 is not a number và không cho phép ghép chuỗi.

## Evidence
- basicCalculator.html dòng 313-317 luôn ép isNumber = true khi selectedBuild == 3
