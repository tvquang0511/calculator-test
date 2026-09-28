# TC-UI-001: Kiểm tra tính khả dụng và hiển thị của các thành phần giao diện

## Requirement ID
FR-UI-01

## Module / Test type / Technique
UI / Functional / State Verification

## Preconditions
- Trình duyệt đã mở trang `basicCalculator.html` (Local hoặc link Github Pages)
- Người dùng đang ở màn hình chính của Calculator

## Test data
| Trường dữ liệu | Giá trị |
| --- | --- |
| Build Selection | Prototype (hoặc Build 0-9) |

## Test steps
1. Truy cập vào trang web Calculator
2. Chọn Build từ dropdown `#selectBuild`
3. Quan sát và kiểm tra sự hiện diện (visibility) của các trường `#number1Field`, `#number2Field`, `#selectOperationDropdown`, `#calculateButton`, `#clearButton`, `#numberAnswerField`
4. Kiểm tra trạng thái tương tác (enabled/disabled) của các ô nhập và nút bấm

## Expected result
Tất cả các phần tử UI trên đều hiển thị đầy đủ trên màn hình (`visible`). Các ô nhập số và các nút `Calculate`, `Clear` ở trạng thái sẵn sàng nhận tương tác (`enabled`). Ô `Answer` có thuộc tính `readonly`.

## Status / Related bugs
Not Run / Bug liên quan: BUG-BUILD9-01 (Build 9 ẩn ô Number 2 và nút Calculate), BUG-BUILD5-01 (Build 5 vô hiệu hóa nút Clear).
