# TC-STR-001: Kiểm tra chức năng ghép chuỗi văn bản (Concatenate Strings)

## Requirement ID
FR-STR-01

## Module / Test type / Technique
String / Functional / Equivalence Partitioning

## Preconditions
- Trang web Calculator đã tải thành công

## Test data
| Trường dữ liệu | Giá trị |
| --- | --- |
| First number | Hello |
| Second number | World |
| Operation | Concatenate (4) |

## Test steps
1. Chọn phép tính `Concatenate` từ dropdown `#selectOperationDropdown`
2. Nhập `Hello` vào ô `First number` (`#number1Field`)
3. Nhập `World` vào ô `Second number` (`#number2Field`)
4. Bấm nút `Calculate` (`#calculateButton`)
5. Chờ trạng thái loading hoàn tất và đọc kết quả tại ô `Answer`

## Expected result
Ô `#numberAnswerField` hiển thị chuỗi ghép nối: `HelloWorld`. Không xuất hiện thông báo lỗi. Checkbox `Integers only` tự động bị ẩn đi khi chọn Concatenate.

## Status / Related bugs
Not Run / Bug liên quan: BUG-BUILD3-01 (Build 3 luôn coi input là số, báo lỗi không cho ghép chữ), BUG-BUILD2-01 (Build 2 tráo sang phép cộng).
