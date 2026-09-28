# TC-UI-003: Kiểm tra chức năng nút "Clear" để reset giao diện

## Requirement ID
FR-UI-03

## Module / Test type / Technique
UI / Functional / State Reset

## Preconditions
- Trang web Calculator đã tải thành công
- Trên màn hình đang có giá trị kết quả trong ô `Answer` và/hoặc thông báo lỗi đỏ

## Test data
| Trường dữ liệu | Giá trị |
| --- | --- |
| First number | 10 |
| Second number | 20 |
| Operation | Add |

## Test steps
1. Nhập First number = 10, Second number = 20, chọn Add và bấm `Calculate`
2. Đợi kết quả hiển thị tại ô `Answer`
3. Nhấp chuột vào nút `Clear` (`#clearButton`)
4. Quan sát ô `Answer`, thông báo lỗi `#errorMsgField` và checkbox `#integerSelect`

## Expected result
Nút `Clear` ở trạng thái tương tác được (`enabled`). Khi bấm `Clear`: ô `Answer` bị xóa sạch (rỗng `""`), thông báo lỗi bị xóa hoàn toàn, và checkbox `#integerSelect` tự động bỏ chọn (`checked = false`).

## Status / Related bugs
Not Run / Bug liên quan: BUG-BUILD5-01 (Build 5 làm vô hiệu hóa nút Clear).
