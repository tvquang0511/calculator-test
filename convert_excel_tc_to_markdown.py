import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Đọc nội dung file export_test_cases_to_excel.py để lấy mảng tc_data
with open("export_test_cases_to_excel.py", "r", encoding="utf-8") as f:
    content = f.read()

# Trích xuất đoạn tc_data = [...]
match = re.search(r"tc_data = \[\s*(\[.*?\])\s*\]\s*#", content, re.DOTALL)
if not match:
    # Thử tìm đến cuối mảng tc_data
    match = re.search(r"tc_data = \[(.*?)\]\s*(?:for row_idx|\n#|\nws3\.column)", content, re.DOTALL)

print("Match found:", bool(match))

# Thay vì parse regex phức tạp, ta có thể import trực tiếp biến tc_data bằng cách execute file hoặc import
# Vì export_test_cases_to_excel.py cần openpyxl, ta kiểm tra xem openpyxl có sẵn không
import sys

# Tạo môi trường thực thi để lấy tc_data
local_vars = {}
# Đọc và thực thi chỉ phần định nghĩa tc_data
data_code = content[content.find("tc_data = [") : content.find("for row_idx, r in enumerate(tc_data")]
exec(data_code, {}, local_vars)
tc_data = local_vars["tc_data"]

print(f"Tổng số test case đọc được: {len(tc_data)}")

# Bản đồ phân loại module và Requirement ID
def get_module_and_req(tc_id):
    num = int(tc_id.replace("TC-", ""))
    if 1 <= num <= 11:
        return "math", "FR-MATH-01", f"TC-MATH-{num:03d}"
    elif 12 <= num <= 21:
        return "math", "FR-MATH-02", f"TC-MATH-{num:03d}"
    elif 22 <= num <= 30:
        return "math", "FR-MATH-03", f"TC-MATH-{num:03d}"
    elif 31 <= num <= 40:
        return "math", "FR-MATH-04", f"TC-MATH-{num:03d}"
    elif 41 <= num <= 42:
        return "math", "FR-MATH-05", f"TC-MATH-{num:03d}"
    elif 43 <= num <= 52:
        return "str", "FR-STR-01", f"TC-STR-{num:03d}"
    elif 53 <= num <= 60:
        return "ui", "FR-UI-02", f"TC-UI-{num:03d}"
    elif 61 <= num <= 68:
        return "val", "FR-VAL-01", f"TC-VAL-{num:03d}"
    elif num in (69, 70, 80):
        return "ui", "FR-UI-01", f"TC-UI-{num:03d}"
    elif 71 <= num <= 79:
        return "build", "FR-BUILD-01", f"TC-BUILD-{num:03d}"
    else:
        return "general", "FR-GEN-01", f"TC-GEN-{num:03d}"

# Tạo các thư mục module và dọn dẹp file cũ
base_dir = os.path.join("tests", "test-cases")
for mod in ["math", "str", "ui", "val", "build"]:
    mod_path = os.path.join(base_dir, mod)
    os.makedirs(mod_path, exist_ok=True)
    for old_file in os.listdir(mod_path):
        if old_file.endswith(".md"):
            os.remove(os.path.join(mod_path, old_file))

# Xử lý từng test case và xuất file Markdown chuẩn Slide 7
count = 0
for tc in tc_data:
    tc_id = tc[0]       # TC-001
    scenario = tc[1]    # Tên kịch bản
    procedure = tc[2]   # Mô tả
    steps_raw = tc[3]   # Steps
    input_raw = tc[4]   # Input
    expected = tc[5]    # Expected result
    test_type = tc[6]   # Test type
    priority = tc[7]    # Priority
    precondition = tc[8]# Precondition
    postcondition = tc[9]# Postcondition

    mod, req_id, std_code = get_module_and_req(tc_id)

    # Chuyển input_raw thành bảng Markdown
    input_lines = [line.strip() for line in input_raw.split("\n") if line.strip()]
    input_table = "| Trường dữ liệu | Giá trị |\n| --- | --- |\n"
    for line in input_lines:
        if "=" in line:
            parts = line.split("=", 1)
            k = parts[0].strip()
            v = parts[1].strip()
            input_table += f"| {k} | {v} |\n"
        else:
            input_table += f"| Dữ liệu | {line} |\n"

    # Chuyển steps thành danh sách đánh số tuần tự 1., 2., 3.
    steps_lines = [s.strip() for s in steps_raw.split("\n") if s.strip()]
    formatted_steps = ""
    for idx, s in enumerate(steps_lines, 1):
        clean_s = re.sub(r"^Step\s*\d+:\s*", "", s)
        formatted_steps += f"{idx}. {clean_s}\n"

    # Xử lý related bug nếu là build regression
    related_bug = "None"
    num = int(tc_id.replace("TC-", ""))
    if 71 <= num <= 79:
        build_num = num - 70
        related_bug = f"BUG-{build_num:02d} (Phát hiện lỗi Build {build_num})"

    # Nội dung Markdown theo đúng chuẩn Slide 7
    md_content = f"""# {std_code} ({tc_id}): {scenario}

## Requirement ID
{req_id}

## Module / Test type / Technique
{mod.capitalize()} / {test_type} / {priority} Priority

## Preconditions
- {precondition}

## Test data
{input_table.strip()}

## Test steps
{formatted_steps.strip()}

## Expected result
{expected}

## Status / Related bugs
Not Run / {related_bug}
"""

    file_path = os.path.join(base_dir, mod, f"{tc_id}.md")
    with open(file_path, "w", encoding="utf-8") as out:
        out.write(md_content)
    count += 1

print(f"✅ Đã tạo thành công {count} file test case Markdown chuẩn vào tests/test-cases/")
