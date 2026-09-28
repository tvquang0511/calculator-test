# TC-MATH-004: Kiểm tra xử lý ngoại lệ phép chia cho 0 (Divide by Zero)

## Requirement ID
FR-MATH-04

## Module / Test type / Technique
Math / Functional / Error Guessing & Exception Handling

## Preconditions
- Trang web Calculator đã tải thành công

## Test data
| Trường dữ liệu | Giá trị |
| --- | --- |
| First number | 10 |
| Second number | 0 |
| Operation | Divide (3) |

## Test steps
1. Nhập `10` vào ô `First number` (`#number1Field`)
2. Nhập `0` vào ô `Second number` (`#number2Field`)
3. Chọn phép tính `Divide` từ dropdown `#selectOperationDropdown`
4. Bấm nút `Calculate` (`#calculateButton`)
5. Quan sát thông báo lỗi tại `#errorMsgField` và giá trị ô `Answer`

## Expected result
Hệ thống bắt ngoại lệ chia cho 0, hiển thị thông báo lỗi màu đỏ tại `#errorMsgField`: `"Divide by zero error!"`. Không hiển thị kết quả hoặc không được ra giá trị `Infinity`.

## Status / Related bugs
Not Run / Bug liên quan: BUG-BUILD6-01 (Build 6 không bắt lỗi chia cho 0, hiển thị `Infinity`).
