# TC-MATH-002: Kiểm tra phép tính trừ và thứ tự toán tử

## Requirement ID
FR-MATH-02

## Module / Test type / Technique
Math / Functional / Boundary Value Analysis

## Preconditions
- Trang web Calculator đã tải thành công

## Test data
| Trường dữ liệu | Giá trị |
| --- | --- |
| First number | 15 |
| Second number | 5 |
| Operation | Subtract (1) |

## Test steps
1. Nhập `15` vào ô `First number` (`#number1Field`)
2. Nhập `5` vào ô `Second number` (`#number2Field`)
3. Chọn phép tính `Subtract` từ dropdown `#selectOperationDropdown`
4. Bấm nút `Calculate` (`#calculateButton`)
5. Chờ trạng thái loading hoàn tất và đọc kết quả tại ô `Answer`

## Expected result
Thực hiện phép trừ theo đúng thứ tự $Number1 - Number2 = 15 - 5 = 10$. Ô `#numberAnswerField` hiển thị giá trị `10`.

## Status / Related bugs
Not Run / Bug liên quan: BUG-BUILD8-01 (Build 8 tráo đổi Number 1 và Number 2, tính thành $5 - 15 = -10$).
