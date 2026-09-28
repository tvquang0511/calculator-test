# ĐẶC TẢ YÊU CẦU CHỨC NĂNG (FUNCTIONAL REQUIREMENTS - FR)

- **Hệ thống:** Basic Calculator
- **Tài liệu tham chiếu:** [basicCalculator.html](file:///d:/document/university/n4hk1/test/calculator-test/src/basicCalculator.html) / [https://testsheepnz.github.io/BasicCalculator.html](https://testsheepnz.github.io/BasicCalculator.html)
- **Mục đích:** Là tài liệu cơ sở (Baseline) để thiết kế Test Case, đo lường độ bao phủ kiểm thử (Test Coverage) và phục vụ ma trận truy vết lỗi (Traceability Matrix).

---

## 1. Danh mục Yêu cầu Chức năng (Functional Requirements List)

| Mã FR | Tên yêu cầu chức năng | Module | Mô tả tóm tắt | Test Cases liên quan |
| :--- | :--- | :---: | :--- | :--- |
| **`FR-UI-01`** | Hiển thị & Khả dụng của giao diện | UI | Tất cả các ô nhập liệu, dropdown, nút bấm phải hiển thị đầy đủ và tương tác bình thường | TC-069, TC-070, TC-080 |
| **`FR-UI-02`** | Tùy chọn làm tròn số nguyên (Integers only) | UI | Khi bật checkbox: kết quả được ép kiểu về số nguyên (`parseInt`). Checkbox phải tự do bật/tắt | TC-053 đến TC-060 |
| **`FR-UI-03`** | Nút Clear (Reset trạng thái) | UI | Bấm nút Clear phải xóa sạch kết quả ở Answer, uncheck Integers only và xóa thông báo lỗi | TC-069, TC-070 |
| **`FR-MATH-01`** | Phép tính Cộng (Addition) | Math | Tính tổng số học giữa hai số thực hoặc số nguyên ($Number1 + Number2$) | TC-001 đến TC-011 |
| **`FR-MATH-02`** | Phép tính Trừ (Subtraction) | Math | Tính hiệu số học theo đúng thứ tự ($Number1 - Number2$), hỗ trợ ra kết quả âm và số 0 | TC-012 đến TC-021 |
| **`FR-MATH-03`** | Phép tính Nhân (Multiplication) | Math | Tính tích số học ($Number1 \times Number2$), xử lý đúng nhân với 0, số âm, số lớn | TC-022 đến TC-030 |
| **`FR-MATH-04`** | Phép tính Chia (Division) | Math | Tính thương số học ($Number1 / Number2$), hỗ trợ chia hết và chia ra số thập phân | TC-031 đến TC-040 |
| **`FR-MATH-05`** | Xử lý ngoại lệ Chia cho 0 | Math | Khi số chia ($Number2$) bằng 0, hệ thống phải chặn tính toán và báo lỗi `"Divide by zero error!"` | TC-041 đến TC-042 |
| **`FR-STR-01`** | Tính năng Ghép chuỗi (Concatenate) | String | Nối chuỗi hai giá trị nhập vào, không kiểm tra kiểu số, tự động ẩn checkbox Integers only | TC-043 đến TC-052 |
| **`FR-VAL-01`** | Xác thực dữ liệu đầu vào (Input Validation) | Validation | Bắt lỗi khi nhập ký tự không phải số trong phép toán số học (`"Number 1/2 is not a number"`) | TC-061 đến TC-068 |
| **`FR-BUILD-01`**| Kiểm thử hồi quy trên các bản Build | Build | Hệ thống phải duy trì đúng đặc tả trên bản Prototype và phát hiện sai lệch trên Builds 1-9 | TC-071 đến TC-079 |

---

## 2. Chi tiết từng Yêu cầu Chức năng

### FR-UI-01: Hiển thị & Khả dụng của giao diện
- **Mô tả:** Màn hình chính phải hiển thị đầy đủ: ô `First number` (`#number1Field`), ô `Second number` (`#number2Field`), dropdown `Operation`, dropdown `Build`, nút `Calculate` (`#calculateButton`), nút `Clear` (`#clearButton`), ô `Answer` (`#numberAnswerField`).
- **Quy tắc:**
  - Ô `Answer` phải ở chế độ chỉ đọc (`readonly`).
  - Khi đang tính toán, hiển thị form "Calculating ..." cùng ảnh spinner và tạm thời khóa các nút bấm.
- **Tiêu chí nghiệm thu:** Không có phần tử cốt lõi nào bị ẩn hoặc vô hiệu hóa bất thường khi tải ứng dụng.

### FR-UI-02: Tùy chọn làm tròn số nguyên (Integers only)
- **Mô tả:** Cho phép người dùng tùy chọn làm tròn kết quả về số nguyên.
- **Quy tắc:**
  - Khi checkbox `Integers only` được tích (`checked = true`): giá trị hiển thị ở `Answer` là phần nguyên (`parseInt(answer)`).
  - Khi bỏ tích (`checked = false`): giá trị hiển thị ở `Answer` trở lại số thực đầy đủ.
  - Người dùng có thể bật/tắt checkbox này ngay cả sau khi đã bấm `Calculate`.
  - Checkbox này tự động bị ẩn và vô hiệu hóa khi chọn phép toán `Concatenate`.

### FR-UI-03: Nút Clear (Reset trạng thái)
- **Mô tả:** Cho phép người dùng làm mới trạng thái tính toán.
- **Quy tắc:** Khi nhấp chuột vào nút `Clear`:
  - Ô kết quả `Answer` trở về rỗng `""`.
  - Checkbox `Integers only` tự động bỏ chọn (`checked = false`).
  - Thông báo lỗi tại `#errorMsgField` bị xóa sạch.

### FR-MATH-01: Phép tính Cộng (Addition)
- **Mô tả:** Thực hiện cộng hai giá trị số học.
- **Công thức:** $Answer = Number1 + Number2$.
- **Tiêu chí:** Tính đúng với số nguyên dương, số âm, số 0, số thập phân và các số lớn tối đa 10 chữ số.

### FR-MATH-02: Phép tính Trừ (Subtraction)
- **Mô tả:** Thực hiện trừ số thứ nhất cho số thứ hai theo đúng thứ tự toán tử.
- **Công thức:** $Answer = Number1 - Number2$.
- **Tiêu chí:** Phải giữ nguyên đúng thứ tự nhập vào (không được đảo ngược thành $Number2 - Number1$). Hỗ trợ ra kết quả số âm, dương và bằng 0.

### FR-MATH-03: Phép tính Nhân (Multiplication)
- **Mô tả:** Thực hiện nhân hai giá trị số học.
- **Công thức:** $Answer = Number1 \times Number2$.
- **Tiêu chí:** Tính đúng với mọi trường hợp nhân với 0 ($x \times 0 = 0$), nhân với 1, nhân số âm và số thập phân.

### FR-MATH-04: Phép tính Chia (Division)
- **Mô tả:** Thực hiện chia số thứ nhất cho số thứ hai ($Number2 \neq 0$).
- **Công thức:** $Answer = Number1 / Number2$.
- **Tiêu chí:** Hỗ trợ phép chia hết (ra số nguyên) và chia có phần dư hữu hạn hoặc vô hạn (ra số thập phân chính xác).

### FR-MATH-05: Xử lý ngoại lệ Chia cho 0 (Division by zero)
- **Mô tả:** Ngăn chặn việc thực hiện phép toán không hợp lệ khi mẫu số bằng 0.
- **Quy tắc:**
  - Nếu $Number2 = 0$ (hoặc $0 / 0$): Hệ thống không được phép in ra kết quả `Infinity` hay `NaN`.
  - Phải hiển thị thông báo lỗi màu đỏ tại `#errorMsgField`: `"Divide by zero error!"`.

### FR-STR-01: Tính năng Ghép chuỗi (Concatenate)
- **Mô tả:** Thực hiện nối chuỗi ký tự của hai trường nhập liệu.
- **Quy tắc:**
  - Xử lý mọi dữ liệu nhập vào dưới dạng chuỗi văn bản (String), không kiểm tra kiểu số.
  - Cho phép ghép chữ cái (`Hello` + `World` $\rightarrow$ `HelloWorld`), số, ký tự đặc biệt hoặc trường rỗng.
  - Tự động ẩn và khóa checkbox `Integers only`.

### FR-VAL-01: Xác thực dữ liệu đầu vào (Input Validation)
- **Mô tả:** Kiểm tra tính hợp lệ của dữ liệu trước khi thực hiện các phép toán số học (Add, Subtract, Multiply, Divide).
- **Quy tắc:**
  - Nếu `First number` không phải số: Hiển thị lỗi `"Number 1 is not a number"`.
  - Nếu `Second number` không phải số: Hiển thị lỗi `"Number 2 is not a number"`.
  - Nếu cả hai đều không phải số: Ưu tiên báo lỗi `"Number 1 is not a number"`.
  - Độ dài nhập liệu tối đa không vượt quá 10 ký tự (`maxlength="10"`).

### FR-BUILD-01: Tính nhất quán giữa các bản Build
- **Mô tả:** Hỗ trợ kiểm thử hồi quy để kiểm tra hành vi ứng dụng giữa bản mẫu Prototype và các bản Builds 1 đến 9 nhằm phát hiện chính xác các khiếm khuyết được cài cắm.
