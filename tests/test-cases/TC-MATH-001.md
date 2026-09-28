# TC-MATH-001: Kiểm tra tính đúng đắn của phép tính cộng

## Requirement ID
FR-MATH-01

## Module / Test type / Technique
Math / Functional / Equivalence Partitioning

## Preconditions
- Trang web Calculator đã tải thành công
- Build đang được chọn là Prototype (hoặc build cần kiểm thử)

## Test data
| Trường dữ liệu | Giá trị |
| --- | --- |
| First number | 10 |
| Second number | 20 |
| Operation | Add (0) |

## Test steps
1. Nhập `10` vào ô `First number` (`#number1Field`)
2. Nhập `20` vào ô `Second number` (`#number2Field`)
3. Chọn phép tính `Add` từ dropdown `#selectOperationDropdown`
4. Bấm nút `Calculate` (`#calculateButton`)
5. Chờ trạng thái loading hoàn tất và đọc kết quả tại ô `Answer`

## Expected result
Thực hiện đúng phép tính số học: $10 + 20 = 30$. Ô `#numberAnswerField` hiển thị giá trị `30`, không hiển thị thông báo lỗi.

## Status / Related bugs
Not Run / Bug liên quan: BUG-BUILD2-01 (Build 2 tráo đổi Add thành Concatenate, ra `1020`).
