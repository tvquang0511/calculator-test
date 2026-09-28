import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

# Create workbook
wb = openpyxl.Workbook()
# Remove default sheet
wb.remove(wb.active)

# Color palettes & styles
font_title = Font(name="Calibri", size=14, bold=True, color="1F497D")
font_header = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
font_sub_header = Font(name="Calibri", size=11, bold=True, color="1F497D")
font_regular = Font(name="Calibri", size=10, color="000000")
font_bold = Font(name="Calibri", size=10, bold=True, color="000000")

fill_header = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
fill_header_scenario = PatternFill(start_color="244062", end_color="244062", fill_type="solid")
fill_header_matrix = PatternFill(start_color="1B365D", end_color="1B365D", fill_type="solid")
fill_header_amber = PatternFill(start_color="C55A11", end_color="C55A11", fill_type="solid")
fill_zebra = PatternFill(start_color="F9FAFB", end_color="F9FAFB", fill_type="solid")

thin_side = Side(border_style="thin", color="D9D9D9")
border_all = Border(left=thin_side, right=thin_side, top=thin_side, bottom=thin_side)
border_header = Border(left=thin_side, right=thin_side, top=thin_side, bottom=Side(border_style="medium", color="0F243E"))

align_left_wrap = Alignment(horizontal="left", vertical="top", wrap_text=True)
align_center = Alignment(horizontal="center", vertical="top")
align_header = Alignment(horizontal="center", vertical="center", wrap_text=True)

# Priority fills
fill_p_high = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")
font_p_high = Font(name="Calibri", size=10, bold=True, color="C00000")
fill_p_med = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
font_p_med = Font(name="Calibri", size=10, bold=True, color="B25900")
fill_p_low = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
font_p_low = Font(name="Calibri", size=10, bold=True, color="375623")

# -------------------------------------------------------------
# SHEET 1: Functional Analysis
# -------------------------------------------------------------
ws1 = wb.create_sheet(title="Functional Analysis")
ws1.views.sheetView[0].showGridLines = True

ws1.append(["BÁO CÁO PHÂN TÍCH CHỨC NĂNG - BASIC CALCULATOR"])
ws1.append(["Website kiểm thử: https://testsheepnz.github.io/BasicCalculator.html"])
ws1.append([])

ws1.cell(1, 1).font = font_title
ws1.cell(2, 1).font = Font(name="Calibri", size=10, italic=True, color="595959")

headers_fa = ["Thành phần", "Tên phần tử / ID", "Loại điều khiển", "Mô tả chi tiết & Quy tắc nghiệp vụ"]
ws1.append(headers_fa)
for col_idx in range(1, len(headers_fa) + 1):
    cell = ws1.cell(4, col_idx)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_header
    cell.border = border_header

fa_data = [
    ["Input", "First number (#number1Field)", "Text Box (maxlength=10)", "Nhận giá trị số thực hiện phép tính toán học hoặc chuỗi ký tự trong phép ghép chuỗi."],
    ["Input", "Second number (#number2Field)", "Text Box (maxlength=10)", "Nhận giá trị số thứ hai hoặc chuỗi ký tự nối sau."],
    ["Operation", "Add (value=0)", "Dropdown Option", "Thực hiện phép cộng toán học First number + Second number."],
    ["Operation", "Subtract (value=1)", "Dropdown Option", "Thực hiện phép trừ toán học First number - Second number."],
    ["Operation", "Multiply (value=2)", "Dropdown Option", "Thực hiện phép nhân toán học First number * Second number."],
    ["Operation", "Divide (value=3)", "Dropdown Option", "Thực hiện phép chia toán học First number / Second number. Chặn chia cho 0 với thông báo 'Divide by zero error!'."],
    ["Operation", "Concatenate (value=4)", "Dropdown Option", "Nối chuỗi 2 giá trị nhập vào, không kiểm tra định dạng số, ẩn và vô hiệu hóa tùy chọn 'Integers only'."],
    ["Option", "Integers only (#integerSelect)", "Checkbox", "Khi bật: Ép kiểu kết quả về số nguyên bằng parseInt(answer). Hỗ trợ cập nhật ngay cả sau khi đã bấm Calculate."],
    ["Action", "Calculate button (#calculateButton)", "Button", "Kích hoạt xử lý tính toán. Hiển thị spinner gif 'Calculating ...' và tạm thời vô hiệu hóa các nút điều khiển."],
    ["Output", "Answer field (#numberAnswerField)", "Text Box (readonly, maxlength=10)", "Hiển thị kết quả tính toán hoặc kết quả ghép chuỗi."],
    ["Output", "Error Message (#errorMsgField)", "Label (color=red)", "Hiển thị thông báo lỗi 'Number 1 is not a number', 'Number 2 is not a number', 'Divide by zero error!'."],
    ["Action", "Clear button (#clearButton)", "Button", "Xóa kết quả trong Answer field, bỏ tích Integers only, xóa thông báo lỗi."],
    ["Build Switch", "Build Selector (#selectBuild)", "Dropdown", "Gồm Prototype (chuẩn) và Build 1 đến 9 chứa các lỗi cố ý nhằm kiểm tra độ nhạy của bộ test suite."]
]

for row_idx, r in enumerate(fa_data, start=5):
    ws1.append(r)
    is_zebra = (row_idx % 2 == 0)
    for c_idx in range(1, len(r) + 1):
        c = ws1.cell(row_idx, c_idx)
        c.font = font_regular
        c.border = border_all
        c.alignment = align_left_wrap
        if is_zebra:
            c.fill = fill_zebra

# Set column widths for WS1
ws1.column_dimensions['A'].width = 18
ws1.column_dimensions['B'].width = 32
ws1.column_dimensions['C'].width = 30
ws1.column_dimensions['D'].width = 65

# -------------------------------------------------------------
# SHEET 2: Test Scenarios
# -------------------------------------------------------------
ws2 = wb.create_sheet(title="Test Scenarios")
ws2.views.sheetView[0].showGridLines = True

ws2.append(["DANH SÁCH TEST SCENARIO - BASIC CALCULATOR"])
ws2.append(["Tổng hợp các kịch bản kiểm thử bao phủ toàn diện chức năng, biên, validation và các build"])
ws2.append([])

ws2.cell(1, 1).font = font_title
ws2.cell(2, 1).font = Font(name="Calibri", size=10, italic=True, color="595959")

headers_ts = ["Scenario ID", "Test Scenario", "Description", "Priority"]
ws2.append(headers_ts)
for col_idx in range(1, len(headers_ts) + 1):
    cell = ws2.cell(4, col_idx)
    cell.font = font_header
    cell.fill = fill_header_scenario
    cell.alignment = align_header
    cell.border = border_header

scenarios_data = [
    ["TS-001", "Kiểm tra phép cộng (Addition)", "Xác minh tính chính xác của phép cộng với các tập dữ liệu số dương, âm, số 0, số thập phân và số lớn", "High"],
    ["TS-002", "Kiểm tra phép trừ (Subtraction)", "Xác minh tính chính xác của phép trừ với số dương, âm, kết quả bằng 0, âm, dương, số thập phân", "High"],
    ["TS-003", "Kiểm tra phép nhân (Multiplication)", "Xác minh tính chính xác của phép nhân với số âm, dương, nhân với 0, nhân với 1, nhân với -1 và số thập phân", "High"],
    ["TS-004", "Kiểm tra phép chia (Division)", "Xác minh tính chính xác của phép chia bao gồm chia hết, chia có dư, chia số thập phân và chia số 0", "High"],
    ["TS-005", "Kiểm tra phép chia cho số 0 (Division by zero)", "Xác minh hệ thống chặn và hiển thị lỗi phù hợp khi thực hiện chia cho 0 hoặc 0 chia 0", "High"],
    ["TS-006", "Kiểm tra tính năng nối chuỗi (Concatenate)", "Xác minh khả năng ghép chuỗi hai toán hạng bao gồm số, chữ cái, ký tự đặc biệt và chuỗi rỗng", "High"],
    ["TS-007", "Kiểm tra tùy chọn số nguyên (Integers only)", "Xác minh việc làm tròn/ép kiểu số nguyên khi bật/tắt tùy chọn này với kết quả nguyên, thập phân âm/dương", "High"],
    ["TS-008", "Kiểm tra mối quan hệ ràng buộc giữa Concatenate và Integers only", "Xác minh trạng thái hiển thị và vô hiệu hóa của checkbox Integers only khi chuyển đổi giữa Concatenate và các phép toán số học", "Medium"],
    ["TS-009", "Kiểm tra Input Validation cho các phép toán số học", "Xác minh thông báo lỗi khi người dùng nhập dữ liệu không phải dạng số (chữ cái, ký tự đặc biệt, nhiều dấu chấm thập phân)", "High"],
    ["TS-010", "Kiểm tra biên giá trị và độ dài nhập liệu (Boundary Value)", "Xác minh hành vi của hệ thống tại các giá trị biên (0, 1, -1, độ dài tối đa 10 ký tự của trường input)", "Medium"],
    ["TS-011", "Kiểm tra chức năng nút Clear và Reset trạng thái", "Xác minh nút Clear xóa đúng kết quả hiển thị, bỏ chọn Integers only và xóa thông báo lỗi", "Medium"],
    ["TS-012", "Kiểm tra trạng thái tải và khóa giao diện (UI Loading & Button State)", "Xác minh trạng thái hiển thị loading spinner và việc disable/enable nút bấm trong chu kỳ tính toán", "Low"],
    ["TS-013", "Kiểm tra tính nhất quán giữa các Build (Build Regression Testing)", "Xác minh các Test Case phát hiện được sự sai lệch hành vi giữa Prototype và các Build từ 1 đến 9", "High"]
]

for row_idx, r in enumerate(scenarios_data, start=5):
    ws2.append(r)
    is_zebra = (row_idx % 2 == 0)
    for c_idx in range(1, len(r) + 1):
        c = ws2.cell(row_idx, c_idx)
        c.font = font_regular
        c.border = border_all
        c.alignment = align_left_wrap
        if c_idx == 1:
            c.alignment = align_center
            c.font = font_bold
        elif c_idx == 4:
            c.alignment = align_center
            if r[3] == "High":
                c.fill = fill_p_high
                c.font = font_p_high
            elif r[3] == "Medium":
                c.fill = fill_p_med
                c.font = font_p_med
            else:
                c.fill = fill_p_low
                c.font = font_p_low
        elif is_zebra:
            c.fill = fill_zebra

ws2.column_dimensions['A'].width = 16
ws2.column_dimensions['B'].width = 38
ws2.column_dimensions['C'].width = 75
ws2.column_dimensions['D'].width = 15

# -------------------------------------------------------------
# SHEET 3: Test Cases
# -------------------------------------------------------------
ws3 = wb.create_sheet(title="Test Cases")
ws3.views.sheetView[0].showGridLines = True

headers_tc = [
    "TC_ID", 
    "Test Scenario", 
    "Test Procedure", 
    "Step", 
    "Input", 
    "Expected Result", 
    "Test Type", 
    "Priority", 
    "Pre-condition", 
    "Post-condition"
]

ws3.append(["BỘ TEST CASE CHI TIẾT - BASIC CALCULATOR"])
ws3.append(["Được thiết kế đầy đủ các kỹ thuật EP, BVA, Negative, Validation, UI và Build Regression Testing"])
ws3.append([])

ws3.cell(1, 1).font = font_title
ws3.cell(2, 1).font = Font(name="Calibri", size=10, italic=True, color="595959")

ws3.append(headers_tc)
for col_idx in range(1, len(headers_tc) + 1):
    cell = ws3.cell(4, col_idx)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = align_header
    cell.border = border_header

tc_data = [
    [
        "TC-001", "Kiểm tra phép cộng hai số nguyên dương", 
        "Kiểm tra calculator thực hiện phép cộng giữa hai số nguyên dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 25 vào First number.\nStep 4: Nhập 15 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 25\nSecond number = 15\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 40. Không có thông báo lỗi hiển thị.",
        "Positive, Functional", "High", "Basic Calculator page is accessible.", "Answer is displayed."
    ],
    [
        "TC-002", "Kiểm tra phép cộng số dương và số âm",
        "Kiểm tra calculator thực hiện phép cộng một số dương và một số âm",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 50 vào First number.\nStep 4: Nhập -20 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 50\nSecond number = -20\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 30.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-003", "Kiểm tra phép cộng số âm và số dương",
        "Kiểm tra calculator thực hiện phép cộng số âm với số dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -35 vào First number.\nStep 4: Nhập 10 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = -35\nSecond number = 10\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -25.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-004", "Kiểm tra phép cộng hai số nguyên âm",
        "Kiểm tra calculator thực hiện phép cộng giữa hai số nguyên âm",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -12 vào First number.\nStep 4: Nhập -18 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = -12\nSecond number = -18\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -30.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-005", "Kiểm tra phép cộng số 0 với một số dương",
        "Kiểm tra cộng 0 với một số dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 0 vào First number.\nStep 4: Nhập 42 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Nhấn Calculate.",
        "First number = 0\nSecond number = 42\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 42.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-006", "Kiểm tra phép cộng một số với số 0",
        "Kiểm tra cộng một số bất kỳ với 0",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 88 vào First number.\nStep 4: Nhập 0 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Nhấn Calculate.",
        "First number = 88\nSecond number = 0\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 88.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-007", "Kiểm tra phép cộng 0 + 0",
        "Kiểm tra cộng hai số 0",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 0 vào First number.\nStep 4: Nhập 0 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Nhấn Calculate.",
        "First number = 0\nSecond number = 0\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 0.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-008", "Kiểm tra phép cộng hai số thập phân",
        "Kiểm tra cộng hai số thập phân dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 12.35 vào First number.\nStep 4: Nhập 7.42 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 12.35\nSecond number = 7.42\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 19.77.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-009", "Kiểm tra phép cộng số thập phân với số nguyên",
        "Kiểm tra cộng một số thập phân và một số nguyên",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 8.75 vào First number.\nStep 4: Nhập 11 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 8.75\nSecond number = 11\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 19.75.",
        "Positive, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-010", "Kiểm tra phép cộng hai số thập phân âm",
        "Kiểm tra cộng hai số thập phân âm",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -4.5 vào First number.\nStep 4: Nhập -3.2 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = -4.5\nSecond number = -3.2\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -7.7.",
        "Positive, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-011", "Kiểm tra phép cộng hai số nguyên lớn đạt giới hạn 10 ký tự",
        "Kiểm tra cộng hai số nguyên có độ dài 9-10 ký tự",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 500000000 vào First number.\nStep 4: Nhập 400000000 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Nhấn Calculate.",
        "First number = 500000000\nSecond number = 400000000\nOperation = Add\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 900000000.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-012", "Kiểm tra phép trừ hai số nguyên dương (kết quả dương)",
        "Kiểm tra trừ hai số nguyên dương sao cho kết quả > 0",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 45 vào First number.\nStep 4: Nhập 20 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 45\nSecond number = 20\nOperation = Subtract\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 25.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-013", "Kiểm tra phép trừ hai số nguyên dương (kết quả âm)",
        "Kiểm tra trừ số nhỏ hơn cho số lớn hơn sao cho kết quả < 0",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 15 vào First number.\nStep 4: Nhập 40 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 15\nSecond number = 40\nOperation = Subtract\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -25.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-014", "Kiểm tra phép trừ hai số giống nhau (kết quả bằng 0)",
        "Kiểm tra trừ hai số bằng nhau",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 99 vào First number.\nStep 4: Nhập 99 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Nhấn Calculate.",
        "First number = 99\nSecond number = 99\nOperation = Subtract\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 0.",
        "Boundary, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-015", "Kiểm tra phép trừ số dương cho số âm",
        "Kiểm tra trừ số dương cho số âm (tương đương phép cộng)",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 30 vào First number.\nStep 4: Nhập -15 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Nhấn Calculate.",
        "First number = 30\nSecond number = -15\nOperation = Subtract\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 45.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-016", "Kiểm tra phép trừ số âm cho số dương",
        "Kiểm tra trừ số âm cho một số dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -20 vào First number.\nStep 4: Nhập 30 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Nhấn Calculate.",
        "First number = -20\nSecond number = 30\nOperation = Subtract\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -50.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-017", "Kiểm tra phép trừ hai số âm",
        "Kiểm tra trừ số âm cho số âm",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -10 vào First number.\nStep 4: Nhập -25 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Nhấn Calculate.",
        "First number = -10\nSecond number = -25\nOperation = Subtract\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 15.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-018", "Kiểm tra phép trừ hai số thập phân",
        "Kiểm tra trừ hai số thập phân dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 15.8 vào First number.\nStep 4: Nhập 4.3 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 15.8\nSecond number = 4.3\nOperation = Subtract\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 11.5.",
        "Positive, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-019", "Kiểm tra phép trừ với số thập phân âm",
        "Kiểm tra trừ số thập phân âm",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -5.75 vào First number.\nStep 4: Nhập 2.25 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Nhấn Calculate.",
        "First number = -5.75\nSecond number = 2.25\nOperation = Subtract\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -8.",
        "Positive, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-020", "Kiểm tra phép trừ số 0 cho một số dương",
        "Kiểm tra trừ số dương từ 0",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 0 vào First number.\nStep 4: Nhập 67 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Nhấn Calculate.",
        "First number = 0\nSecond number = 67\nOperation = Subtract\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -67.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-021", "Kiểm tra phép trừ hai số lớn",
        "Kiểm tra trừ hai số có giá trị lớn",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 99999999 vào First number.\nStep 4: Nhập 11111111 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Nhấn Calculate.",
        "First number = 99999999\nSecond number = 11111111\nOperation = Subtract\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 88888888.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-022", "Kiểm tra phép nhân hai số nguyên dương",
        "Kiểm tra nhân hai số nguyên dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 6 vào First number.\nStep 4: Nhập 7 vào Second number.\nStep 5: Chọn Operation = Multiply.\nStep 6: Nhấn Calculate.",
        "First number = 6\nSecond number = 7\nOperation = Multiply\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 42.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-023", "Kiểm tra phép nhân số dương với số âm",
        "Kiểm tra nhân một số dương với một số âm",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 8 vào First number.\nStep 4: Nhập -5 vào Second number.\nStep 5: Chọn Operation = Multiply.\nStep 6: Nhấn Calculate.",
        "First number = 8\nSecond number = -5\nOperation = Multiply\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -40.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-024", "Kiểm tra phép nhân hai số nguyên âm",
        "Kiểm tra nhân hai số nguyên âm (kết quả số dương)",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -9 vào First number.\nStep 4: Nhập -4 vào Second number.\nStep 5: Chọn Operation = Multiply.\nStep 6: Nhấn Calculate.",
        "First number = -9\nSecond number = -4\nOperation = Multiply\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 36.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-025", "Kiểm tra phép nhân một số với 0",
        "Kiểm tra nhân một số dương với 0",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 123 vào First number.\nStep 4: Nhập 0 vào Second number.\nStep 5: Chọn Operation = Multiply.\nStep 6: Nhấn Calculate.",
        "First number = 123\nSecond number = 0\nOperation = Multiply\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 0.",
        "Boundary, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-026", "Kiểm tra phép nhân 0 với một số",
        "Kiểm tra nhân 0 với một số nguyên",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 0 vào First number.\nStep 4: Nhập -78 vào Second number.\nStep 5: Chọn Operation = Multiply.\nStep 6: Nhấn Calculate.",
        "First number = 0\nSecond number = -78\nOperation = Multiply\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 0.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-027", "Kiểm tra phép nhân một số với 1",
        "Kiểm tra tính chất nhân với đơn vị 1",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 56 vào First number.\nStep 4: Nhập 1 vào Second number.\nStep 5: Chọn Operation = Multiply.\nStep 6: Nhấn Calculate.",
        "First number = 56\nSecond number = 1\nOperation = Multiply\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 56.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-028", "Kiểm tra phép nhân một số với -1",
        "Kiểm tra tính chất đổi dấu khi nhân với -1",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 89 vào First number.\nStep 4: Nhập -1 vào Second number.\nStep 5: Chọn Operation = Multiply.\nStep 6: Nhấn Calculate.",
        "First number = 89\nSecond number = -1\nOperation = Multiply\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -89.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-029", "Kiểm tra phép nhân hai số thập phân",
        "Kiểm tra nhân hai số thập phân",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 2.5 vào First number.\nStep 4: Nhập 1.5 vào Second number.\nStep 5: Chọn Operation = Multiply.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 2.5\nSecond number = 1.5\nOperation = Multiply\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 3.75.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-030", "Kiểm tra phép nhân hai số lớn",
        "Kiểm tra nhân hai số lớn kiểm tra tràn số hoặc hiển thị",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 100000 vào First number.\nStep 4: Nhập 100000 vào Second number.\nStep 5: Chọn Operation = Multiply.\nStep 6: Nhấn Calculate.",
        "First number = 100000\nSecond number = 100000\nOperation = Multiply\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 10000000000.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-031", "Kiểm tra phép chia hết hai số nguyên dương",
        "Kiểm tra chia hai số nguyên dương không có phần dư",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 20 vào First number.\nStep 4: Nhập 4 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 20\nSecond number = 4\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 5.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-032", "Kiểm tra phép chia có dư (kết quả thập phân hữu hạn)",
        "Kiểm tra chia có phần dư hữu hạn",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 5 vào First number.\nStep 4: Nhập 2 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 5\nSecond number = 2\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 2.5.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-033", "Kiểm tra phép chia có phần dư vô hạn tuần hoàn",
        "Kiểm tra hiển thị chuỗi số thập phân dài",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 10 vào First number.\nStep 4: Nhập 3 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 10\nSecond number = 3\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 3.3333333333333335 (giá trị float chuẩn của JS).",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-034", "Kiểm tra phép chia số dương cho số âm",
        "Kiểm tra chia số dương cho số âm",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 18 vào First number.\nStep 4: Nhập -3 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Nhấn Calculate.",
        "First number = 18\nSecond number = -3\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -6.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-035", "Kiểm tra phép chia số âm cho số dương",
        "Kiểm tra chia số âm cho số dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -40 vào First number.\nStep 4: Nhập 8 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Nhấn Calculate.",
        "First number = -40\nSecond number = 8\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -5.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-036", "Kiểm tra phép chia hai số âm",
        "Kiểm tra chia hai số âm (kết quả số dương)",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -50 vào First number.\nStep 4: Nhập -5 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Nhấn Calculate.",
        "First number = -50\nSecond number = -5\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 10.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-037", "Kiểm tra phép chia một số cho 1",
        "Kiểm tra tính chất chia cho 1",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 77 vào First number.\nStep 4: Nhập 1 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Nhấn Calculate.",
        "First number = 77\nSecond number = 1\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 77.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-038", "Kiểm tra phép chia một số cho -1",
        "Kiểm tra tính chất chia cho -1",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 64 vào First number.\nStep 4: Nhập -1 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Nhấn Calculate.",
        "First number = 64\nSecond number = -1\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị -64.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-039", "Kiểm tra phép chia 0 cho một số khác 0",
        "Kiểm tra chia 0 cho số nguyên dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 0 vào First number.\nStep 4: Nhập 9 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Nhấn Calculate.",
        "First number = 0\nSecond number = 9\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 0.",
        "Boundary, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-040", "Kiểm tra phép chia hai số thập phân",
        "Kiểm tra chia hai số thập phân",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 7.5 vào First number.\nStep 4: Nhập 2.5 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Nhấn Calculate.",
        "First number = 7.5\nSecond number = 2.5\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Answer hiển thị 3.",
        "Positive, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-041", "Kiểm tra phép chia một số cho 0 (Division by zero)",
        "Kiểm tra bắt lỗi chia cho 0 khi số bị chia là số dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 15 vào First number.\nStep 4: Nhập 0 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Nhấn Calculate.",
        "First number = 15\nSecond number = 0\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Thông báo lỗi màu đỏ hiển thị: 'Divide by zero error!'. Không hiển thị kết quả Answer.",
        "Negative, Boundary", "High", "User is on the Basic Calculator page.", "Error message is displayed."
    ],
    [
        "TC-042", "Kiểm tra phép chia 0 cho 0 (0 / 0)",
        "Kiểm tra bắt lỗi chia cho 0 khi cả hai số đều bằng 0",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 0 vào First number.\nStep 4: Nhập 0 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Nhấn Calculate.",
        "First number = 0\nSecond number = 0\nOperation = Divide\nIntegers only = Unchecked\nBuild = Prototype",
        "Thông báo lỗi màu đỏ hiển thị: 'Divide by zero error!'. Không thực hiện tính toán.",
        "Negative, Boundary", "High", "User is on the Basic Calculator page.", "Error message is displayed."
    ],
    [
        "TC-043", "Kiểm tra nối chuỗi hai số nguyên (Concatenate Integers)",
        "Kiểm tra nối chuỗi hai số nguyên thông thường",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 12 vào First number.\nStep 4: Nhập 34 vào Second number.\nStep 5: Chọn Operation = Concatenate.\nStep 6: Nhấn Calculate.",
        "First number = 12\nSecond number = 34\nOperation = Concatenate\nBuild = Prototype",
        "Answer hiển thị 1234. Không áp dụng phép cộng số học.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-044", "Kiểm tra nối chuỗi có số 0 đứng đầu (Leading Zero)",
        "Kiểm tra nối chuỗi giữ nguyên chữ số 0 đứng đầu",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 01 vào First number.\nStep 4: Nhập 05 vào Second number.\nStep 5: Chọn Operation = Concatenate.\nStep 6: Nhấn Calculate.",
        "First number = 01\nSecond number = 05\nOperation = Concatenate\nBuild = Prototype",
        "Answer hiển thị 0105. Không bị mất số 0 đứng đầu.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-045", "Kiểm tra nối chuỗi với số 0 đơn lẻ",
        "Kiểm tra nối chuỗi với giá trị 0",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 50 vào First number.\nStep 4: Nhập 0 vào Second number.\nStep 5: Chọn Operation = Concatenate.\nStep 6: Nhấn Calculate.",
        "First number = 50\nSecond number = 0\nOperation = Concatenate\nBuild = Prototype",
        "Answer hiển thị 500.",
        "Positive, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-046", "Kiểm tra nối chuỗi với số âm",
        "Kiểm tra nối chuỗi chứa dấu trừ âm",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -10 vào First number.\nStep 4: Nhập -20 vào Second number.\nStep 5: Chọn Operation = Concatenate.\nStep 6: Nhấn Calculate.",
        "First number = -10\nSecond number = -20\nOperation = Concatenate\nBuild = Prototype",
        "Answer hiển thị -10-20.",
        "Positive, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-047", "Kiểm tra nối chuỗi với số thập phân",
        "Kiểm tra nối chuỗi chứa dấu chấm thập phân",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 3.14 vào First number.\nStep 4: Nhập 2.5 vào Second number.\nStep 5: Chọn Operation = Concatenate.\nStep 6: Nhấn Calculate.",
        "First number = 3.14\nSecond number = 2.5\nOperation = Concatenate\nBuild = Prototype",
        "Answer hiển thị 3.142.5.",
        "Positive, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-048", "Kiểm tra nối chuỗi văn bản chữ cái (Alphabetic)",
        "Kiểm tra nối hai chuỗi ký tự chữ cái khi chọn Concatenate",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập Hello vào First number.\nStep 4: Nhập World vào Second number.\nStep 5: Chọn Operation = Concatenate.\nStep 6: Nhấn Calculate.",
        "First number = Hello\nSecond number = World\nOperation = Concatenate\nBuild = Prototype",
        "Answer hiển thị HelloWorld. Không có lỗi validation.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-049", "Kiểm tra nối chuỗi chữ và số (Alphanumeric)",
        "Kiểm tra nối chuỗi kết hợp chữ và số",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập Test vào First number.\nStep 4: Nhập 123 vào Second number.\nStep 5: Chọn Operation = Concatenate.\nStep 6: Nhấn Calculate.",
        "First number = Test\nSecond number = 123\nOperation = Concatenate\nBuild = Prototype",
        "Answer hiển thị Test123.",
        "Positive, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-050", "Kiểm tra nối chuỗi chứa ký tự đặc biệt",
        "Kiểm tra nối hai chuỗi ký tự đặc biệt",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập #@ vào First number.\nStep 4: Nhập &$ vào Second number.\nStep 5: Chọn Operation = Concatenate.\nStep 6: Nhấn Calculate.",
        "First number = #@\nSecond number = &$\nOperation = Concatenate\nBuild = Prototype",
        "Answer hiển thị #@&$.",
        "Positive, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-051", "Kiểm tra nối chuỗi khi First number để trống",
        "Kiểm tra nối chuỗi có một trường rỗng",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Để trống First number.\nStep 4: Nhập 999 vào Second number.\nStep 5: Chọn Operation = Concatenate.\nStep 6: Nhấn Calculate.",
        "First number = (để trống)\nSecond number = 999\nOperation = Concatenate\nBuild = Prototype",
        "Answer hiển thị 999. Không hiển thị lỗi.",
        "Boundary, Functional", "Medium", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-052", "Kiểm tra nối chuỗi khi cả hai trường đều để trống",
        "Kiểm tra nối hai chuỗi rỗng",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Để trống First number.\nStep 4: Để trống Second number.\nStep 5: Chọn Operation = Concatenate.\nStep 6: Nhấn Calculate.",
        "First number = (để trống)\nSecond number = (để trống)\nOperation = Concatenate\nBuild = Prototype",
        "Answer hiển thị rỗng (chuỗi ''). Không hiển thị lỗi.",
        "Boundary, Functional", "Low", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-053", "Kiểm tra Integers only = ON với kết quả là số nguyên chính xác",
        "Kiểm tra bật Integers only khi kết quả vốn là số nguyên",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 20 vào First number.\nStep 4: Nhập 5 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Tích chọn Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 20\nSecond number = 5\nOperation = Divide\nIntegers only = Checked\nBuild = Prototype",
        "Answer hiển thị 4.",
        "Positive, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-054", "Kiểm tra Integers only = ON với kết quả số thập phân dương (Truncation)",
        "Kiểm tra cơ chế lấy phần nguyên của số thập phân dương",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 10 vào First number.\nStep 4: Nhập 3 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Tích chọn Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 10\nSecond number = 3\nOperation = Divide\nIntegers only = Checked\nBuild = Prototype",
        "Answer hiển thị 3.",
        "Positive, Boundary, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-055", "Kiểm tra Integers only = ON với kết quả thập phân dương sát số nguyên trên",
        "Kiểm tra hệ thống cắt bỏ phần thập phân chứ không làm tròn lên",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 7.99 vào First number.\nStep 4: Nhập 0 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Tích chọn Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 7.99\nSecond number = 0\nOperation = Add\nIntegers only = Checked\nBuild = Prototype",
        "Answer hiển thị 7 (xử lý cắt đuôi parseInt('7.99')).",
        "Boundary, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-056", "Kiểm tra Integers only = ON với kết quả số thập phân âm",
        "Kiểm tra ép kiểu nguyên với số thập phân âm",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập -7 vào First number.\nStep 4: Nhập 2 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Tích chọn Integers only.\nStep 7: Nhấn Calculate.",
        "First number = -7\nSecond number = 2\nOperation = Divide\nIntegers only = Checked\nBuild = Prototype",
        "Answer hiển thị -3 (theo cơ chế parseInt('-3.5')).",
        "Positive, Boundary", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-057", "Kiểm tra Integers only = ON với kết quả trong khoảng (0, 1)",
        "Kiểm tra ép kiểu nguyên với số thập phân nhỏ hơn 1",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 1 vào First number.\nStep 4: Nhập 4 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Tích chọn Integers only.\nStep 7: Nhấn Calculate.",
        "First number = 1\nSecond number = 4\nOperation = Divide\nIntegers only = Checked\nBuild = Prototype",
        "Answer hiển thị 0.",
        "Boundary, Functional", "High", "User is on the Basic Calculator page.", "Answer is displayed."
    ],
    [
        "TC-058", "Kiểm tra bật/tắt Integers only sau khi đã có kết quả tính",
        "Kiểm tra Answer cập nhật động khi toggle Integers only",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 11 vào First number.\nStep 4: Nhập 4 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Bỏ tích Integers only.\nStep 7: Nhấn Calculate.\nStep 8: Quan sát Answer (2.75).\nStep 9: Tích chọn Integers only.",
        "First number = 11\nSecond number = 4\nOperation = Divide\nIntegers only = Toggle from Unchecked to Checked",
        "Tại Step 7: Answer hiển thị 2.75.\nTại Step 9: Answer lập tức đổi thành 2 mà không cần bấm lại Calculate.",
        "Functional, UI", "High", "User is on the Basic Calculator page.", "Answer updated dynamically."
    ],
    [
        "TC-059", "Kiểm tra ẩn và vô hiệu hóa Integers only khi chọn Concatenate",
        "Kiểm tra ràng buộc giao diện giữa Operation Concatenate và checkbox Integers only",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Chọn Operation = Add, quan sát Integers only hiển thị.\nStep 4: Đổi Operation = Concatenate.",
        "Operation = Concatenate\nBuild = Prototype",
        "Checkbox integerSelect và label Integers only bị ẩn hoàn toàn khỏi màn hình (hidden = true) và bị disabled.",
        "Functional, Validation", "High", "User is on the Basic Calculator page.", "Integers only checkbox is hidden."
    ],
    [
        "TC-060", "Kiểm tra hiển thị lại Integers only khi chuyển từ Concatenate sang Add",
        "Kiểm tra khôi phục trạng thái Integers only khi chọn lại phép toán số học",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Chọn Operation = Concatenate (checkbox bị ẩn).\nStep 4: Đổi Operation = Add.",
        "Operation thay đổi từ Concatenate sang Add\nBuild = Prototype",
        "Checkbox integerSelect và nhãn Integers only hiển thị trở lại bình thường và cho phép người dùng thao tác.",
        "Functional, UI", "Medium", "User is on the Basic Calculator page.", "Integers only checkbox is visible."
    ],
    [
        "TC-061", "Kiểm tra Input Validation khi First number là chữ cái",
        "Kiểm tra báo lỗi khi First number chứa ký tự chữ cái trong phép tính số học",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập abc vào First number.\nStep 4: Nhập 10 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Nhấn Calculate.",
        "First number = abc\nSecond number = 10\nOperation = Add\nBuild = Prototype",
        "Hiển thị thông báo lỗi màu đỏ: 'Number 1 is not a number'. Không thực hiện tính toán.",
        "Negative, Validation", "High", "User is on the Basic Calculator page.", "Error message is displayed."
    ],
    [
        "TC-062", "Kiểm tra Input Validation khi Second number là chữ cái",
        "Kiểm tra báo lỗi khi Second number chứa ký tự chữ cái",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 25 vào First number.\nStep 4: Nhập xyz vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Nhấn Calculate.",
        "First number = 25\nSecond number = xyz\nOperation = Add\nBuild = Prototype",
        "Hiển thị thông báo lỗi màu đỏ: 'Number 2 is not a number'. Không thực hiện tính toán.",
        "Negative, Validation", "High", "User is on the Basic Calculator page.", "Error message is displayed."
    ],
    [
        "TC-063", "Kiểm tra Input Validation khi cả hai trường đều là chữ cái",
        "Kiểm tra thứ tự ưu tiên hiển thị lỗi khi cả hai input đều sai",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập aaa vào First number.\nStep 4: Nhập bbb vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Nhấn Calculate.",
        "First number = aaa\nSecond number = bbb\nOperation = Subtract\nBuild = Prototype",
        "Hiển thị thông báo lỗi màu đỏ: 'Number 1 is not a number' (kiểm tra First number trước).",
        "Negative, Validation", "High", "User is on the Basic Calculator page.", "Error message is displayed."
    ],
    [
        "TC-064", "Kiểm tra Input Validation với ký tự đặc biệt",
        "Kiểm tra báo lỗi khi input chứa ký tự đặc biệt",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập @#$% vào First number.\nStep 4: Nhập 5 vào Second number.\nStep 5: Chọn Operation = Multiply.\nStep 6: Nhấn Calculate.",
        "First number = @#$%\nSecond number = 5\nOperation = Multiply\nBuild = Prototype",
        "Hiển thị thông báo lỗi màu đỏ: 'Number 1 is not a number'.",
        "Negative, Validation", "High", "User is on the Basic Calculator page.", "Error message is displayed."
    ],
    [
        "TC-065", "Kiểm tra Input Validation với số chứa nhiều dấu chấm thập phân",
        "Kiểm tra báo lỗi khi nhập định dạng số thập phân không hợp lệ",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 12.3.4 vào First number.\nStep 4: Nhập 6 vào Second number.\nStep 5: Chọn Operation = Divide.\nStep 6: Nhấn Calculate.",
        "First number = 12.3.4\nSecond number = 6\nOperation = Divide\nBuild = Prototype",
        "Hiển thị thông báo lỗi màu đỏ: 'Number 1 is not a number'.",
        "Negative, Validation", "High", "User is on the Basic Calculator page.", "Error message is displayed."
    ],
    [
        "TC-066", "Kiểm tra Input Validation khi trường để trống trong phép toán số học",
        "Kiểm tra hành vi khi người dùng để trống input và nhấn Calculate",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Để trống First number.\nStep 4: Nhập 10 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Nhấn Calculate.",
        "First number = (để trống)\nSecond number = 10\nOperation = Add\nBuild = Prototype",
        "Cần xác nhận requirement: Hệ thống Prototype coi chuỗi rỗng là 0 và tính ra 10 (do isNaN('') === false). Kỳ vọng chuẩn là báo lỗi yêu cầu nhập số.",
        "Negative, Validation, Error Guessing", "High", "User is on the Basic Calculator page.", "Actual behavior vs Expected requirement checked."
    ],
    [
        "TC-067", "Kiểm tra Input Validation khi nhập chuỗi toàn khoảng trắng (Whitespace)",
        "Kiểm tra nhập khoảng trắng vào input",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập các dấu cách '   ' vào First number.\nStep 4: Nhập 8 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Nhấn Calculate.",
        "First number = '   '\nSecond number = 8\nOperation = Add\nBuild = Prototype",
        "Cần xác nhận requirement: JS coi '   ' là 0 và tính ra 8. Kỳ vọng chuẩn là báo lỗi 'Number 1 is not a number'.",
        "Negative, Validation, Error Guessing", "Medium", "User is on the Basic Calculator page.", "Actual behavior vs Expected requirement checked."
    ],
    [
        "TC-068", "Kiểm tra giới hạn độ dài ký tự của trường input (Maxlength = 10)",
        "Kiểm tra người dùng không thể gõ quá 10 ký tự vào ô First number và Second number",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Nhập chuỗi 1234567890123 vào First number.\nStep 3: Quan sát giá trị lưu lại trong ô input.",
        "Nhập 13 ký tự: 1234567890123",
        "Ô First number chỉ nhận tối đa đúng 10 ký tự: 1234567890. Không cho phép gõ thêm ký tự thứ 11.",
        "Boundary, Validation", "Medium", "User is on the Basic Calculator page.", "Input text truncated at 10 chars."
    ],
    [
        "TC-069", "Kiểm tra chức năng nút Clear sau khi tính toán thành công",
        "Kiểm tra nút Clear xóa kết quả hiển thị và reset checkbox Integers only",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 50 vào First number, 20 vào Second number.\nStep 4: Tích chọn Integers only.\nStep 5: Nhấn Calculate để Answer hiển thị 70.\nStep 6: Nhấn nút Clear.",
        "Nhấn nút Clear sau khi có Answer = 70 và Integers only đang Checked",
        "Trường Answer bị xóa rỗng (''). Checkbox Integers only tự động uncheck. First number và Second number vẫn giữ nguyên.",
        "Functional, UI", "Medium", "Answer is 70, Integers only is checked.", "Answer cleared, checkbox unchecked."
    ],
    [
        "TC-070", "Kiểm tra chức năng nút Clear sau khi có lỗi hiển thị",
        "Kiểm tra nút Clear xóa thông báo lỗi",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập abc vào First number, 10 vào Second number.\nStep 4: Nhấn Calculate để xuất hiện lỗi 'Number 1 is not a number'.\nStep 5: Nhấn nút Clear.",
        "Nhấn Clear khi đang có thông báo lỗi hiển thị",
        "Thông báo lỗi đỏ bị xóa rỗng.",
        "Functional, UI", "Medium", "Error message is visible.", "Error message is cleared."
    ],
    [
        "TC-071", "Kiểm tra Build 1: Xác minh việc bỏ sót Input Validation",
        "Kiểm tra Build 1 chấp nhận chuỗi không hợp lệ trong phép toán",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = 1.\nStep 3: Nhập abc vào First number.\nStep 4: Nhập 10 vào Second number.\nStep 5: Chọn Operation = Add.\nStep 6: Nhấn Calculate.",
        "First number = abc\nSecond number = 10\nOperation = Add\nBuild = 1",
        "So sánh với Prototype (báo lỗi): Build 1 không báo lỗi mà thực hiện tính toán (cho ra kết quả NaN).",
        "Functional, Error Guessing", "High", "Build 1 is selected.", "Difference against Prototype detected."
    ],
    [
        "TC-072", "Kiểm tra Build 2: Xác minh đảo lộn giữa Add và Concatenate",
        "Kiểm tra phép cộng và nối chuỗi bị tráo đổi trên Build 2",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = 2.\nStep 3: Nhập 10 vào First number, 20 vào Second number.\nStep 4: Chọn Operation = Add.\nStep 5: Nhấn Calculate.",
        "First number = 10\nSecond number = 20\nOperation = Add\nBuild = 2",
        "So sánh với Prototype (ra 30): Build 2 cho ra kết quả '1020' (thực hiện Concatenate thay vì Add).",
        "Functional, Regression", "High", "Build 2 is selected.", "Difference against Prototype detected."
    ],
    [
        "TC-073", "Kiểm tra Build 3: Xác minh Concatenate bị ép tính toán số học",
        "Kiểm tra tính năng Concatenate trên Build 3 vẫn đòi hỏi số hợp lệ",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = 3.\nStep 3: Nhập Hello vào First number, World vào Second number.\nStep 4: Chọn Operation = Concatenate.\nStep 5: Nhấn Calculate.",
        "First number = Hello\nSecond number = World\nOperation = Concatenate\nBuild = 3",
        "So sánh với Prototype (ra 'HelloWorld'): Build 3 báo lỗi 'Number 1 is not a number' do luôn xử lý như số học.",
        "Functional, Regression", "High", "Build 3 is selected.", "Difference against Prototype detected."
    ],
    [
        "TC-074", "Kiểm tra Build 4: Xác minh tùy chọn Integers only bị khóa cứng",
        "Kiểm tra trạng thái checkbox Integers only trên Build 4",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = 4.\nStep 3: Quan sát checkbox Integers only.\nStep 4: Nhập 10 vào First number, 4 vào Second number, chọn Divide, nhấn Calculate.",
        "Build = 4\nFirst number = 10\nSecond number = 4\nOperation = Divide",
        "Checkbox Integers only bị tick và bị disabled (khóa cứng). Kết quả Answer luôn bị ép thành số nguyên 2 thay vì 2.5.",
        "Functional, UI", "High", "Build 4 is selected.", "Locked integer mode verified."
    ],
    [
        "TC-075", "Kiểm tra Build 5: Xác minh nút Clear bị vô hiệu hóa",
        "Kiểm tra nút Clear trên Build 5",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = 5.\nStep 3: Quan sát thuộc tính nút Clear.",
        "Build = 5",
        "Nút Clear hiển thị ở trạng thái disabled (disabled = true), người dùng không thể bấm được.",
        "Functional, UI", "Medium", "Build 5 is selected.", "Clear button disabled verified."
    ],
    [
        "TC-076", "Kiểm tra Build 6: Xác minh thiếu kiểm tra chia cho 0",
        "Kiểm tra thực hiện phép chia cho 0 trên Build 6",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = 6.\nStep 3: Nhập 12 vào First number, 0 vào Second number.\nStep 4: Chọn Operation = Divide.\nStep 5: Nhấn Calculate.",
        "First number = 12\nSecond number = 0\nOperation = Divide\nBuild = 6",
        "So sánh với Prototype (hiển thị thông báo lỗi): Build 6 không báo lỗi mà hiển thị Answer là Infinity.",
        "Functional, Boundary", "High", "Build 6 is selected.", "Unchecked division by zero detected."
    ],
    [
        "TC-077", "Kiểm tra Build 7: Xác minh dùng kết quả Answer cũ làm First number",
        "Kiểm tra Build 7 lấy Answer trước đó thay vì First number hiện tại",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = 7.\nStep 3: Nhập 10 và 5, chọn Add, Calculate để Answer = 15.\nStep 4: Đổi First number thành 100, Second number = 2, chọn Add, Calculate.",
        "Lần 1: 10 + 5 = 15\nLần 2: First = 100, Second = 2\nBuild = 7",
        "So sánh với Prototype (lần 2 ra 102): Build 7 lấy kết quả cũ 15 + 2 ra Answer = 17.",
        "Functional, Regression", "High", "Build 7 is selected.", "Old answer reuse defect detected."
    ],
    [
        "TC-078", "Kiểm tra Build 8: Xác minh đảo ngược vị trí toán hạng (First và Second)",
        "Kiểm tra Build 8 hoán đổi vị trí First number và Second number",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = 8.\nStep 3: Nhập 10 vào First number.\nStep 4: Nhập 2 vào Second number.\nStep 5: Chọn Operation = Subtract.\nStep 6: Nhấn Calculate.",
        "First number = 10\nSecond number = 2\nOperation = Subtract\nBuild = 8",
        "So sánh với Prototype (10 - 2 = 8): Build 8 hoán đổi thành 2 - 10 và cho ra kết quả -8.",
        "Functional, Regression", "High", "Build 8 is selected.", "Swapped operands defect detected."
    ],
    [
        "TC-079", "Kiểm tra Build 9: Xác minh phần tử giao diện bị ẩn / biến mất",
        "Kiểm tra các trường bị ẩn bất thường trên Build 9",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = 9.\nStep 3: Quan sát giao diện form tính toán.",
        "Build = 9",
        "Trường Second number (number2Field) và nút Calculate (calculateButton) bị ẩn (hidden = true) và vô hiệu hóa.",
        "UI, Functional", "Medium", "Build 9 is selected.", "Elements disappearance verified."
    ],
    [
        "TC-080", "Kiểm tra trạng thái UI trong quá trình tính toán (Spinner & Lock button)",
        "Kiểm tra biểu tượng Calculating hiển thị và nút bấm bị khóa tạm thời",
        "Step 1: Mở trang Basic Calculator.\nStep 2: Chọn Build = Prototype.\nStep 3: Nhập 50 vào First number, 50 vào Second number, chọn Add.\nStep 4: Nhấn Calculate và quan sát ngay lập tức giao diện.",
        "First number = 50\nSecond number = 50\nOperation = Add",
        "Trong khoảng thời gian tính toán: Biểu tượng waiting.gif hiển thị cùng dòng chữ 'Calculating ...', trường Answer tạm ẩn, nút Calculate và Clear bị disabled. Sau đó trở lại bình thường và hiển thị Answer = 100.",
        "UI, Functional", "Low", "User is on the Basic Calculator page.", "Controls restored after calculation."
    ]
]

for row_idx, r in enumerate(tc_data, start=5):
    ws3.append(r)
    is_zebra = (row_idx % 2 == 0)
    for c_idx in range(1, len(r) + 1):
        c = ws3.cell(row_idx, c_idx)
        c.font = font_regular
        c.border = border_all
        c.alignment = align_left_wrap
        
        # Center ID, Priority, Type
        if c_idx == 1:
            c.alignment = align_center
            c.font = font_bold
        elif c_idx == 8:
            c.alignment = align_center
            if r[7] == "High":
                c.fill = fill_p_high
                c.font = font_p_high
            elif r[7] == "Medium":
                c.fill = fill_p_med
                c.font = font_p_med
            else:
                c.fill = fill_p_low
                c.font = font_p_low
        elif is_zebra:
            c.fill = fill_zebra

ws3.column_dimensions['A'].width = 12
ws3.column_dimensions['B'].width = 30
ws3.column_dimensions['C'].width = 35
ws3.column_dimensions['D'].width = 45
ws3.column_dimensions['E'].width = 35
ws3.column_dimensions['F'].width = 42
ws3.column_dimensions['G'].width = 22
ws3.column_dimensions['H'].width = 12
ws3.column_dimensions['I'].width = 28
ws3.column_dimensions['J'].width = 28

# -------------------------------------------------------------
# SHEET 4: Coverage Matrix
# -------------------------------------------------------------
ws4 = wb.create_sheet(title="Coverage Matrix")
ws4.views.sheetView[0].showGridLines = True

ws4.append(["MA TRẬN BAO PHỦ KIỂM THỬ (TEST COVERAGE MATRIX)"])
ws4.append(["Đối chiếu các tính năng với các kỹ thuật kiểm thử và danh sách Test Case tương ứng"])
ws4.append([])

ws4.cell(1, 1).font = font_title
ws4.cell(2, 1).font = Font(name="Calibri", size=10, italic=True, color="595959")

headers_matrix = ["Feature", "Positive", "Negative", "Boundary", "Validation", "Covered TC"]
ws4.append(headers_matrix)
for col_idx in range(1, len(headers_matrix) + 1):
    cell = ws4.cell(4, col_idx)
    cell.font = font_header
    cell.fill = fill_header_matrix
    cell.alignment = align_header
    cell.border = border_header

matrix_data = [
    ["Addition", "x", "", "x", "", "TC-001, TC-002, TC-003, TC-004, TC-005, TC-006, TC-007, TC-008, TC-009, TC-010, TC-011"],
    ["Subtraction", "x", "", "x", "", "TC-012, TC-013, TC-014, TC-015, TC-016, TC-017, TC-018, TC-019, TC-020, TC-021"],
    ["Multiplication", "x", "", "x", "", "TC-022, TC-023, TC-024, TC-025, TC-026, TC-027, TC-028, TC-029, TC-030"],
    ["Division", "x", "", "x", "", "TC-031, TC-032, TC-033, TC-034, TC-035, TC-036, TC-037, TC-038, TC-039, TC-040"],
    ["Division by zero", "", "x", "x", "", "TC-041, TC-042"],
    ["Concatenate", "x", "", "x", "", "TC-043, TC-044, TC-045, TC-046, TC-047, TC-048, TC-049, TC-050, TC-051, TC-052"],
    ["Integers only", "x", "", "x", "x", "TC-053, TC-054, TC-055, TC-056, TC-057, TC-058, TC-059, TC-060"],
    ["Input validation", "", "x", "x", "x", "TC-061, TC-062, TC-063, TC-064, TC-065, TC-066, TC-067, TC-068"],
    ["Calculate & UI State", "x", "", "", "", "TC-080"],
    ["Answer & Clear", "x", "", "", "", "TC-069, TC-070"],
    ["Build", "x", "x", "x", "x", "TC-071, TC-072, TC-073, TC-074, TC-075, TC-076, TC-077, TC-078, TC-079"]
]

for row_idx, r in enumerate(matrix_data, start=5):
    ws4.append(r)
    is_zebra = (row_idx % 2 == 0)
    for c_idx in range(1, len(r) + 1):
        c = ws4.cell(row_idx, c_idx)
        c.font = font_regular
        c.border = border_all
        c.alignment = align_left_wrap
        if c_idx == 1:
            c.font = font_bold
        elif 2 <= c_idx <= 5:
            c.alignment = align_center
            if r[c_idx - 1] == "x":
                c.font = font_bold
                c.fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
        elif is_zebra:
            c.fill = fill_zebra

ws4.column_dimensions['A'].width = 24
ws4.column_dimensions['B'].width = 12
ws4.column_dimensions['C'].width = 12
ws4.column_dimensions['D'].width = 12
ws4.column_dimensions['E'].width = 12
ws4.column_dimensions['F'].width = 75

# -------------------------------------------------------------
# SHEET 5: Requirement Ambiguities
# -------------------------------------------------------------
ws5 = wb.create_sheet(title="Requirement Ambiguities")
ws5.views.sheetView[0].showGridLines = True

ws5.append(["DANH SÁCH YÊU CẦU MƠ HỒ CẦN XÁC NHẬN (REQUIREMENT AMBIGUITIES)"])
ws5.append(["Các điểm thiếu sót hoặc chưa rõ ràng trong requirement được phát hiện qua phân tích kỹ thuật và kiểm thử UI"])
ws5.append([])

ws5.cell(1, 1).font = font_title
ws5.cell(2, 1).font = Font(name="Calibri", size=10, italic=True, color="595959")

headers_amb = ["Issue ID", "Tính năng / Vấn đề", "Hành vi thực tế quan sát được", "Yêu cầu cần BA/PO xác nhận", "Mức độ ảnh hưởng"]
ws5.append(headers_amb)
for col_idx in range(1, len(headers_amb) + 1):
    cell = ws5.cell(4, col_idx)
    cell.font = font_header
    cell.fill = fill_header_amber
    cell.alignment = align_header
    cell.border = border_header

amb_data = [
    [
        "REQ-AMB-01",
        "Xử lý chuỗi rỗng (Empty input) & khoảng trắng (Whitespace)",
        "Hệ thống dùng hàm isNaN() của JS nên coi '' hoặc '   ' là 0 (+'' = 0). Khi để trống ô và tính cộng, kết quả vẫn ra số thay vì báo lỗi.",
        "Có cho phép mặc định ô trống là 0 hay bắt buộc hiển thị lỗi 'Number 1 is required' / 'Number 1 is not a number'?",
        "High"
    ],
    [
        "REQ-AMB-02",
        "Khóa giao diện vĩnh viễn khi chia cho 0 trên Prototype",
        "Khi gặp num2 == 0 trong phép chia, code gọi return ngay sau khi set lỗi đỏ mà không gọi unlockCalculate(). Form Answer bị ẩn và nút bấm bị disable vĩnh viễn.",
        "Xác nhận đây là Defect của Prototype hay chủ ý thiết kế? Kỳ vọng: Báo lỗi nhưng form Answer và các nút phải mở lại để người dùng tiếp tục tính toán.",
        "Critical"
    ],
    [
        "REQ-AMB-03",
        "Quy tắc làm tròn của tùy chọn 'Integers only'",
        "Code dùng parseInt(answer), tức cắt bỏ hoàn toàn phần thập phân (Truncate: 7.99 -> 7, -3.8 -> -3).",
        "Xác nhận cơ chế chuẩn: Truncate (cắt phần lẻ), Round half up (làm tròn số học 7.99 -> 8), Floor (làm tròn xuống), hay Ceiling?",
        "Medium"
    ],
    [
        "REQ-AMB-04",
        "Độ chính xác và định dạng số thập phân (Floating Point)",
        "JavaScript hiển thị chuỗi float dài vô hạn tuần hoàn (ví dụ 10 / 3 = 3.3333333333333335, 0.1 + 0.2 = 0.30000000000000004).",
        "Có cần làm tròn hiển thị (ví dụ 2 hoặc 4 chữ số thập phân) hay giữ nguyên float thô?",
        "Medium"
    ],
    [
        "REQ-AMB-05",
        "Giới hạn giá trị số học và tràn số (Numerical Overflow)",
        "Input có maxlength=10 ký tự nhưng không giới hạn độ lớn số học. Kết quả nhân số lớn (100000 * 100000 = 10000000000) vượt quá 10 ký tự của trường Answer.",
        "Xác định giá trị Min/Max hợp lệ cho phép tính và thông báo khi tràn số.",
        "Medium"
    ],
    [
        "REQ-AMB-06",
        "Phạm vi xóa dữ liệu của nút Clear",
        "Nút Clear chỉ xóa Answer, uncheck Integers only và xóa lỗi, giữ nguyên First number và Second number.",
        "Nút Clear có cần reset cả First number và Second number về rỗng hay giữ nguyên như hiện tại?",
        "Low"
    ]
]

for row_idx, r in enumerate(amb_data, start=5):
    ws5.append(r)
    is_zebra = (row_idx % 2 == 0)
    for c_idx in range(1, len(r) + 1):
        c = ws5.cell(row_idx, c_idx)
        c.font = font_regular
        c.border = border_all
        c.alignment = align_left_wrap
        if c_idx == 1:
            c.alignment = align_center
            c.font = font_bold
        elif c_idx == 5:
            c.alignment = align_center
            if r[4] in ["Critical", "High"]:
                c.fill = fill_p_high
                c.font = font_p_high
            elif r[4] == "Medium":
                c.fill = fill_p_med
                c.font = font_p_med
            else:
                c.fill = fill_p_low
                c.font = font_p_low
        elif is_zebra:
            c.fill = fill_zebra

ws5.column_dimensions['A'].width = 16
ws5.column_dimensions['B'].width = 30
ws5.column_dimensions['C'].width = 45
ws5.column_dimensions['D'].width = 50
ws5.column_dimensions['E'].width = 20

# Save file
file_path = "c:/HCMUS/hk7/Testing/w3/Basic_Calculator_Test_Design.xlsx"
wb.save(file_path)
print(f"SUCCESS: Exported successfully to {file_path}")
