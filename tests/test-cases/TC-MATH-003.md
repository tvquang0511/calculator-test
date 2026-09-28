# TC-MATH-003: Kiểm tra phép tính chia ra kết quả số thập phân

## Requirement ID
FR-MATH-03

## Module / Test type / Technique
Math / Functional / Precision Testing

## Preconditions
- Trang web Calculator đã tải thành công
- Checkbox `Integers only` không được chọn

## Test data
| Trường dữ liệu | Giá trị |
| --- | --- |
| First number | 7 |
| Second number | 2 |
| Operation | Divide (3) |

## Test steps
1. Nhập `7` vào ô `First number` (`#number1Field`)
2. Nhập `2` vào ô `Second number` (`#number2Field`)
3. Chọn phép tính `Divide` từ dropdown `#selectOperationDropdown`
4. Bấm nút `Calculate` (`#calculateButton`)
5. Chờ trạng thái loading hoàn tất và đọc kết quả tại ô `Answer`

## Expected result
Thực hiện phép tính chia: $7 / 2 = 3.5$. Ô `#numberAnswerField` hiển thị chính xác số thập phân `3.5`.

## Status / Related bugs
Not Run / Bug liên quan: BUG-BUILD4-01 (Build 4 ép về số nguyên `3`), BUG-BUILD8-01 (Build 8 tính ngược $2 / 7 \approx 0.2857$).
