# [BUG][UI] Ô Second number và nút Calculate bị ẩn và vô hiệu hóa, tê liệt ứng dụng

## Found by Test Case
TC-UI-001

## Requirement liên quan
FR-UI-01

## Severity / Priority
Blocker / P0

## Environment
- **Browser:** Chrome 128 / Chromium
- **OS:** Windows 11
- **URL:** src/basicCalculator.html
- **Build:** Build 9

## Steps to reproduce
1. Chọn Build 9
2. Quan sát giao diện form tính toán

## Expected result
Ô Second number và nút Calculate hiển thị bình thường, cho phép nhập liệu và thao tác.

## Actual result
Ô Second number và nút Calculate bị ẩn (hidden = true) và vô hiệu hóa (disabled = true). Không thể thực hiện bất kỳ phép tính nào.

## Evidence
- basicCalculator.html dòng 457-468 set number2Field.hidden = true và calculateButton.hidden = true
