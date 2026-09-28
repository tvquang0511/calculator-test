import csv
import os

# Dữ liệu danh sách Test Case
data = [
    ["ID", "Nhóm", "Tên Test Case", "Tiền điều kiện", "Các bước thực hiện", "Kết quả mong đợi"],
    
    # Functional - Happy Path
    ["TC01", "Chức năng cơ bản", "Kiểm tra phép Cộng (Add)", "Chọn Build: Prototype", "1. Nhập First number = 5\n2. Nhập Second number = 3\n3. Chọn Operation = Add\n4. Click Calculate", "Answer hiển thị 8. Không có lỗi."],
    ["TC02", "Chức năng cơ bản", "Kiểm tra phép Trừ (Subtract)", "Chọn Build: Prototype", "1. Nhập First number = 10\n2. Nhập Second number = 4\n3. Chọn Operation = Subtract\n4. Click Calculate", "Answer hiển thị 6. Không có lỗi."],
    ["TC03", "Chức năng cơ bản", "Kiểm tra phép Nhân (Multiply)", "Chọn Build: Prototype", "1. Nhập First number = 7\n2. Nhập Second number = 6\n3. Chọn Operation = Multiply\n4. Click Calculate", "Answer hiển thị 42. Không có lỗi."],
    ["TC04", "Chức năng cơ bản", "Kiểm tra phép Chia (Divide)", "Chọn Build: Prototype", "1. Nhập First number = 20\n2. Nhập Second number = 4\n3. Chọn Operation = Divide\n4. Click Calculate", "Answer hiển thị 5. Không có lỗi."],
    ["TC05", "Chức năng cơ bản", "Kiểm tra Nối chuỗi (Concatenate) với số", "Chọn Build: Prototype", "1. Nhập First number = 5\n2. Nhập Second number = 3\n3. Chọn Operation = Concatenate\n4. Click Calculate", "Answer hiển thị 53. Không có lỗi."],
    ["TC06", "Chức năng cơ bản", "Kiểm tra Nối chuỗi (Concatenate) với chữ", "Chọn Build: Prototype", "1. Nhập First number = Hello \n2. Nhập Second number = World\n3. Chọn Operation = Concatenate\n4. Click Calculate", "Answer hiển thị Hello World. Không có lỗi."],
    
    # Negative & Edge Cases
    ["TC07", "Ngoại lệ & Biên", "Lỗi Chia cho 0 (Divide by Zero)", "Chọn Build: Prototype", "1. Nhập First number = 5\n2. Nhập Second number = 0\n3. Chọn Operation = Divide\n4. Click Calculate", "Hệ thống báo lỗi màu đỏ: 'Divide by zero error!'. Answer không hiển thị kết quả."],
    ["TC08", "Ngoại lệ & Biên", "Nhập chữ vào phép toán Số học", "Chọn Build: Prototype", "1. Nhập First number = abc\n2. Nhập Second number = 5\n3. Chọn Operation = Add\n4. Click Calculate", "Hệ thống báo lỗi: 'Number 1 is not a number'."],
    ["TC09", "Ngoại lệ & Biên", "Nhập ký tự đặc biệt vào phép toán", "Chọn Build: Prototype", "1. Nhập First number = 5\n2. Nhập Second number = !@#\n3. Chọn Operation = Multiply\n4. Click Calculate", "Hệ thống báo lỗi: 'Number 2 is not a number'."],
    ["TC10", "Ngoại lệ & Biên", "Giới hạn ký tự (Max length)", "Chọn Build: Prototype", "1. Nhập 11 số 1 vào First number", "Ô nhập liệu chỉ cho phép nhập tối đa 10 ký tự (do thuộc tính maxlength='10')."],
    
    # UI/UX & Integration
    ["TC11", "Giao diện (UI/UX)", "Tính năng 'Integers only' (Lấy phần nguyên)", "Chọn Build: Prototype", "1. Nhập First = 5, Second = 2\n2. Chọn Operation = Divide\n3. Tick chọn 'Integers only'\n4. Click Calculate", "Answer hiển thị 2 (thay vì 2.5)."],
    ["TC12", "Giao diện (UI/UX)", "Ẩn 'Integers only' khi chọn Concatenate", "Chọn Build: Prototype", "1. Chọn Operation = Concatenate", "Checkbox 'Integers only' bị ẩn đi (hidden)."],
    ["TC13", "Giao diện (UI/UX)", "Chức năng nút 'Clear'", "Chọn Build: Prototype", "1. Thực hiện phép tính bất kỳ\n2. Click nút Clear", "Answer bị xóa trắng. Lỗi (nếu có) bị xóa. Checkbox Integers only bị uncheck."],
    ["TC14", "Giao diện (UI/UX)", "Trạng thái 'Calculating...'", "Chọn Build: Prototype", "1. Nhập số liệu hợp lệ và click Calculate", "Nút Calculate/Clear tạm thời bị disable, xuất hiện hiệu ứng 'Calculating...' và ảnh GIF chờ."]
]

# Lấy đường dẫn thư mục hiện tại của script
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, 'TestCases_BasicCalculator.csv')

# Ghi ra file CSV với encoding utf-8-sig (BOM) để Excel đọc tiếng Việt không bị lỗi font
with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Đã xuất file thành công tại: {csv_file_path}")
