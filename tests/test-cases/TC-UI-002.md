# TC-UI-002: Kiểm tra chức năng và trạng thái của Checkbox "Integers only"

## Requirement ID
FR-UI-02

## Module / Test type / Technique
UI / Functional / Equivalence Partitioning

## Preconditions
- Trang web Calculator đã tải thành công
- Đang ở chế độ phép tính số học (Add, Subtract, Multiply, hoặc Divide)

## Test data
| Trường dữ liệu | Giá trị |
| --- | --- |
| First number | 5.8 |
| Second number | 1 |
| Operation | Divide |
| Integers only | Checked / Unchecked |

## Test steps
1. Nhập `5.8` vào First number và `1` vào Second number
2. Chọn phép tính `Divide`
3. Kiểm tra trạng thái checkbox `#integerSelect`
4. Tích chọn checkbox `#integerSelect` và bấm `Calculate`
5. Quan sát giá trị tại ô `Answer`
6. Bỏ tích chọn checkbox `#integerSelect` và quan sát lại ô `Answer`

## Expected result
Checkbox `#integerSelect` cho phép người dùng click bật/tắt tự do. Khi tích chọn, ô `Answer` hiển thị phần nguyên là `5` (`parseInt(5.8)`). Khi bỏ tích, ô `Answer` khôi phục giá trị số thực `5.8`.

## Status / Related bugs
Not Run / Bug liên quan: BUG-BUILD4-01 (Build 4 khóa cứng checkbox ở trạng thái checked=true và disabled=true).
