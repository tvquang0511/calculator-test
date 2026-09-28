# [BUG][UI] Checkbox Integers only bị khóa cứng ở trạng thái Checked

## Found by Test Case
TC-UI-002, TC-MATH-003

## Requirement liên quan
FR-UI-02, FR-MATH-03

## Severity / Priority
Major / P2

## Environment
- **Browser:** Chrome 128 / Chromium
- **OS:** Windows 11
- **URL:** src/basicCalculator.html
- **Build:** Build 4

## Steps to reproduce
1. Chọn Build 4
2. Quan sát checkbox Integers only
3. Thử click bỏ chọn checkbox
4. Thực hiện phép chia 7 / 2

## Expected result
Checkbox cho phép người dùng click bật/tắt. Kết quả 7 / 2 hiển thị 3.5 khi tắt checkbox.

## Actual result
Checkbox bị disabled=true và luôn checked=true. Kết quả 7 / 2 luôn bị làm tròn số nguyên thành 3.

## Evidence
- basicCalculator.html dòng 492-504 ép integerSelect.disabled = true và checked = true
