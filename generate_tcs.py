import os

test_cases = [
    ("math", "TC-081", "Kiểm tra phép cộng với số âm", "Add", "-10", "-5", "Unchecked", "Answer hiển thị -15. Không báo lỗi.", "FR-MATH-01", "Math / Negative"),
    ("math", "TC-082", "Kiểm tra phép trừ tạo ra kết quả âm", "Subtract", "5", "10", "Unchecked", "Answer hiển thị -5. Không báo lỗi.", "FR-MATH-02", "Math / Negative"),
    ("math", "TC-083", "Kiểm tra phép nhân số âm và dương", "Multiply", "-7", "6", "Unchecked", "Answer hiển thị -42. Không báo lỗi.", "FR-MATH-03", "Math / Negative"),
    ("math", "TC-084", "Kiểm tra phép chia tạo ra số thập phân âm", "Divide", "-5", "2", "Unchecked", "Answer hiển thị -2.5. Không báo lỗi.", "FR-MATH-04", "Math / Negative"),
    ("math", "TC-085", "Kiểm tra Integers only với kết quả âm", "Divide", "-5", "2", "Checked", "Answer hiển thị -2.", "FR-MATH-04", "Math / Negative"),
    ("val", "TC-086", "Kiểm tra xử lý khoảng trắng ở đầu số", "Add", "  5", "3", "Unchecked", "Answer hiển thị 8.", "FR-VAL-01", "Val / Edge"),
    ("val", "TC-087", "Kiểm tra xử lý số 0 ở đầu", "Add", "007", "003", "Unchecked", "Answer hiển thị 10.", "FR-VAL-01", "Val / Edge"),
    ("val", "TC-088", "Kiểm tra bỏ trống trường First number", "Add", "", "5", "Unchecked", "Hiển thị lỗi: Number 1 is not a number", "FR-VAL-01", "Val / Negative"),
    ("val", "TC-089", "Kiểm tra bỏ trống trường Second number", "Add", "5", "", "Unchecked", "Hiển thị lỗi: Number 2 is not a number", "FR-VAL-01", "Val / Negative"),
    ("val", "TC-090", "Kiểm tra bỏ trống cả hai trường", "Add", "", "", "Unchecked", "Hiển thị lỗi liên quan đến giá trị rỗng", "FR-VAL-01", "Val / Negative"),
    ("val", "TC-091", "Kiểm tra nhập dấu chấm phân cách", "Add", ".", "5", "Unchecked", "Hiển thị lỗi: Number 1 is not a number", "FR-VAL-01", "Val / Negative"),
    ("str", "TC-092", "Nối chuỗi với một trường rỗng", "Concatenate", "Hello", "", "Unchecked", "Answer hiển thị Hello", "FR-STR-01", "Str / Edge"),
    ("str", "TC-093", "Nối chuỗi gồm toàn khoảng trắng", "Concatenate", "   ", "   ", "Unchecked", "Answer hiển thị khoảng trắng tương ứng", "FR-STR-01", "Str / Edge"),
    ("ui", "TC-094", "Tính toán liên tiếp không clear", "Subtract", "10", "5", "Unchecked", "Answer cập nhật kết quả mới bình thường", "FR-UI-01", "UI / Flow"),
    ("val", "TC-095", "Kiểm tra số dạng khoa học", "Add", "1e3", "5", "Unchecked", "Xử lý được thành 1005 hoặc báo lỗi hợp lệ", "FR-VAL-01", "Val / Edge"),
    ("ui", "TC-096", "Kiểm tra trường Answer là ReadOnly", "Add", "1", "1", "Unchecked", "Trường Answer không thể focus hoặc nhập liệu", "FR-UI-02", "UI / Security"),
    ("val", "TC-097", "Kiểm tra HTML Injection", "Add", "<h1>5</h1>", "3", "Unchecked", "Hiển thị lỗi, không render HTML trên giao diện", "FR-VAL-01", "Val / Security"),
    ("math", "TC-098", "Kiểm tra phép chia ra số vô tỉ", "Divide", "1", "3", "Unchecked", "Hiển thị kết quả 0.3333333333333333", "FR-MATH-04", "Math / Edge"),
    ("build", "TC-099", "Kiểm tra tính năng Add trên Build 2", "Add", "5", "3", "Unchecked", "Answer hiển thị 53 (do lỗi đảo tính năng)", "FR-BUILD-02", "Build / Specific"),
    ("build", "TC-100", "Kiểm tra nút Clear trên Build 5", "Add", "5", "3", "Unchecked", "Nút Clear bị vô hiệu hóa (disabled)", "FR-BUILD-05", "Build / Specific")
]

template = """# TC-{cat_upper}-{tc_num} ({tc_id}): {tc_name}

## Requirement ID
{req_id}

## Module / Test type / Technique
{module_type}

## Preconditions
- Basic Calculator page is accessible.

## Test data
| Trường dữ liệu | Giá trị |
| --- | --- |
| First number | {num1} |
| Second number | {num2} |
| Operation | {op} |
| Integers only | {int_only} |
| Build | {build} |

## Test steps
1. Mở trang Basic Calculator.
2. Chọn Build = {build}.
3. Nhập `{num1}` vào First number.
4. Nhập `{num2}` vào Second number.
5. Chọn Operation = {op}.
6. Tích/Bỏ tích Integers only: {int_only}.
7. Nhấn Calculate.

## Expected result
{expected}

## Status / Related bugs
Not Run / None
"""

base_dir = r"d:\KAN\N4\KTPM\btcalcu\tests\test-cases"

for cat, tc_id, name, op, num1, num2, int_only, expected, req_id, module_type in test_cases:
    tc_num = tc_id.split("-")[1]
    
    build_val = "Prototype"
    if tc_id == "TC-099": build_val = "2"
    if tc_id == "TC-100": build_val = "5"

    content = template.format(
        cat_upper=cat.upper(),
        tc_num=tc_num,
        tc_id=tc_id,
        tc_name=name,
        req_id=req_id,
        module_type=module_type,
        num1=num1,
        num2=num2,
        op=op,
        int_only=int_only,
        expected=expected,
        build=build_val
    )
    
    file_path = os.path.join(base_dir, cat, f"{tc_id}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Đã tạo 20 test cases thành công.")
