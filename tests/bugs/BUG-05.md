# [BUG][UI] Nút Clear bị vô hiệu hóa ngay khi tải Build 5

## Found by Test Case
TC-UI-003

## Requirement liên quan
FR-UI-03

## Severity / Priority
Medium / P2

## Environment
- **Browser:** Chrome 128 / Chromium
- **OS:** Windows 11
- **URL:** src/basicCalculator.html
- **Build:** Build 5

## Steps to reproduce
1. Chọn Build 5
2. Quan sát trạng thái nút Clear

## Expected result
Nút Clear ở trạng thái enabled, sẵn sàng click để xóa kết quả.

## Actual result
Nút Clear bị vô hiệu hóa (disabled = true) ngay khi tải Build 5, người dùng không thể nhấn.

## Evidence
- basicCalculator.html dòng 451-455 gán clearButton.disabled = true
