# TC-MATH-005: Kiểm tra tính độc lập giữa các lần tính toán liên tiếp

## Requirement ID
FR-MATH-05

## Module / Test type / Technique
Math / Functional / State & Memory Independence

## Preconditions
- Trang web Calculator đã tải thành công

## Test data
| Trường dữ liệu | Giá trị Lần 1 | Giá trị Lần 2 |
| --- | --- | --- |
| First number | 2 | 10 |
| Second number | 3 | 20 |
| Operation | Add | Add |

## Test steps
1. **Lần 1:** Nhập Number 1 = 2, Number 2 = 3, chọn Add, bấm `Calculate` -> Chờ hiển thị kết quả `5`
2. **Lần 2:** Không bấm nút Clear, nhập đè `10` vào ô `First number` và `20` vào ô `Second number`, chọn Add
3. Bấm `Calculate` và quan sát kết quả tại ô `Answer`

## Expected result
Lần tính thứ 2 phải độc lập hoàn toàn với lần tính thứ 1. Kết quả phải tính dựa trên đúng các số vừa nhập: $10 + 20 = 30$. Ô `#numberAnswerField` hiển thị giá trị `30`.

## Status / Related bugs
Not Run / Bug liên quan: BUG-BUILD7-01 (Build 7 lấy giá trị của Answer cũ thế vào First number, tính ra $5 + 20 = 25$).
