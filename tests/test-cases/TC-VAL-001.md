# TC-VAL-001: Bắt lỗi khi nhập ký tự không phải số trong phép toán số học

## Requirement ID
FR-VAL-01

## Module / Test type / Technique
Validation / Negative Testing / Input Validation

## Preconditions
- Trang web Calculator đã tải thành công

## Test data
| Trường dữ liệu | Giá trị |
| --- | --- |
| First number | abc |
| Second number | 10 |
| Operation | Add (0) |

## Test steps
1. Nhập `abc` vào ô `First number` (`#number1Field`)
2. Nhập `10` vào ô `Second number` (`#number2Field`)
3. Chọn phép tính `Add` từ dropdown `#selectOperationDropdown`
4. Bấm nút `Calculate` (`#calculateButton`)
5. Quan sát thông báo lỗi và ô kết quả

## Expected result
Hệ thống bắt lỗi định dạng dữ liệu đầu vào. Xuất hiện thông báo lỗi màu đỏ tại `#errorMsgField`: `"Number 1 is not a number"`. Không thực hiện phép tính và mở khóa lại nút `Calculate`.

## Status / Related bugs
Not Run / Bug liên quan: BUG-BUILD1-01 (Build 1 bỏ qua xác thực số, trả về chuỗi `abc10` hoặc `NaN` thay vì báo lỗi).
