# BÁO CÁO THỰC THI KIỂM THỬ (TEST RUN REPORT)

- **Dự án:** Basic Calculator Automation Testing
- **Hệ điều hành / Môi trường:** Windows / Chromium Headless (Playwright)
- **Tài liệu nguồn:** `src/basicCalculator.html` / https://testsheepnz.github.io/BasicCalculator.html
- **Phạm vi kiểm thử:** Chạy toàn bộ 10 Test Cases trên **Prototype (Chuẩn)** và **Builds 1 đến 9**.

---

## 1. Bảng Ma trận Thực thi (Execution Matrix)

| Test ID | Tên Test Case | Prototype | Build 1 | Build 2 | Build 3 | Build 4 | Build 5 | Build 6 | Build 7 | Build 8 | Build 9 |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **TC-UI-001** | UI Elements Availability | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** |
| **TC-UI-002** | Integers Only Checkbox | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** |
| **TC-UI-003** | Clear Button Functionality | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS |
| **TC-MATH-001** | Addition Operation (10+20) | ✅ PASS | ✅ PASS | ❌ **FAIL** | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** |
| **TC-MATH-002** | Subtraction Operation (15-5) | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** | ❌ **FAIL** |
| **TC-MATH-003** | Division with Decimal (7/2) | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** | ❌ **FAIL** |
| **TC-MATH-004** | Division by Zero (10/0) | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** | ✅ PASS | ✅ PASS | ❌ **FAIL** |
| **TC-MATH-005** | Consecutive Calculations | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** | ✅ PASS | ❌ **FAIL** |
| **TC-STR-001** | Concatenate Strings | ✅ PASS | ✅ PASS | ❌ **FAIL** | ❌ **FAIL** | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** |
| **TC-VAL-001** | Input Validation (NaN) | ✅ PASS | ❌ **FAIL** | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ❌ **FAIL** |

---

## 2. Chi tiết Kết quả ghi nhận trên từng Build

### 2.0. Prototype (Baseline)
- **Tỷ lệ đạt:** 10/10 PASS (100%)
- **Đánh giá:** Mọi chức năng tính toán, kiểm tra dữ liệu, xử lý ngoại lệ và thao tác giao diện hoạt động hoàn hảo theo đúng đặc tả.

### 2.1. Build 1
- **TC-VAL-001 - FAIL:** Nhập `abc` vào First Number và bấm `Add`, hệ thống không báo lỗi `"Number 1 is not a number"` mà vẫn tiến hành xử lý, trả về chuỗi `abc10`.

### 2.2. Build 2
- **TC-MATH-001 - FAIL:** Chọn `Add` với `10` và `20`, kết quả trả về `1020` (bị biến thành ghép chuỗi).
- **TC-STR-001 - FAIL:** Chọn `Concatenate` với `10` và `20`, kết quả trả về `30` (bị biến thành phép cộng).

### 2.3. Build 3
- **TC-STR-001 - FAIL:** Chọn `Concatenate` và nhập chuỗi văn bản `"Hello"` và `"World"`, hệ thống báo lỗi `"Number 1 is not a number"` và không cho phép ghép chuỗi chữ cái.

### 2.4. Build 4
- **TC-MATH-003 - FAIL:** Phép chia `7 / 2` cho ra kết quả `3` thay vì `3.5`.
- **TC-UI-002 - FAIL:** Checkbox "Integers only" bị vô hiệu hóa (`disabled`) và luôn bị tích chọn (`checked`).

### 2.5. Build 5
- **TC-UI-003 - FAIL:** Nút "Clear" bị vô hiệu hóa (`disabled = true`) ngay khi chọn Build 5, người dùng không thể xóa dữ liệu hay reset kết quả.

### 2.6. Build 6
- **TC-MATH-004 - FAIL:** Thực hiện `10 / 0`, hệ thống không báo lỗi `"Divide by zero error!"` mà xuất kết quả `Infinity`.

### 2.7. Build 7
- **TC-MATH-005 - FAIL:** Lần 1 tính `2 + 3 = 5`. Lần 2 nhập `10 + 20`, hệ thống lấy kết quả cũ là `5` thế vào Number 1, dẫn đến kết quả sai: $5 + 20 = 25$ (kỳ vọng: $30$).

### 2.8. Build 8
- **TC-MATH-002 - FAIL:** Phép trừ `15 - 5` bị đảo ngược thành $5 - 15 = -10$.
- **TC-MATH-003 - FAIL:** Phép chia `7 / 2` bị đảo ngược thành $2 / 7 \approx 0.2857$.

### 2.9. Build 9
- **TC-UI-001 đến TC-VAL-001 - FAIL (Trừ TC-UI-003):** Ô `Second number` và nút `Calculate` bị ẩn (`hidden = true`) và vô hiệu hóa (`disabled = true`), làm tê liệt toàn bộ các thao tác tính toán.
