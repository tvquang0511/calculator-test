# 📑 AI AUDIT REPORT

| Thông tin chung | Chi tiết |
| :--- | :--- |
| 👥 **Mã nhóm** | `Nhom02` |
| 👤 **Họ và tên / MSSV** | `23120372` |
| 🎯 **Dự án** | `Basic Calculator Automation Testing` |
| 📅 **Ngày lập** | `2026-09-28` |

---

## 📋 BÁO CÁO NHẬT KÝ TƯƠNG TÁC AI

---

### 📍 Tương tác 1: Khởi tạo Test Case ban đầu

> [!NOTE]
> **Công cụ AI:** `ChatGPT`  
> **Thời gian:** `28/09/2026` (~2:00 PM)

* **💬 Câu lệnh (Prompt):**
  ```text
  hãy tạo test case cho Basic Calculator dựa trên chức năng của hệ thống
  ```

* **⚡ Kết quả do AI tạo ra:**
  * **Phân tích chức năng:** Phép tính (`Cộng`, `Trừ`, `Nhân`, `Chia`), xử lý dữ liệu số, `Concatenate` và tùy chọn trả về số nguyên (`Integer`).
  * **Phân loại Test Case:** `Functional Testing`, `Boundary/Exception Testing`, và `UI Testing`.
  * **Cấu trúc dữ liệu:** Cung cấp đầy đủ `ID`, `Mục tiêu`, `Dữ liệu đầu vào`, `Bước thực hiện` và `Expected Result`.

---

### 📍 Tương tác 2: Quy trình Tự động hóa & Hướng dẫn Playwright

> [!NOTE]
> **Công cụ AI:** `ChatGPT`  
> **Thời gian:** `28/09/2026` (~2:00 PM)

* **💬 Câu lệnh (Prompt):**
  ```text
  sau khi có test case thì tạo test script và test run như thế nào?
  ```

* **⚡ Kết quả do AI tạo ra:**
  * **Quy trình kiểm thử:** Giải thích luồng `Test Case` ➔ `Automation Test Script` ➔ `Test Run` ➔ `Test Report`.
  * **Công cụ:** Hướng dẫn sử dụng `Playwright` để tự động hóa.
  * **Lệnh thực thi cơ bản:**
    - Chạy toàn bộ test suite.
    - Chạy file test chỉ định.
    - Chạy test ở chế độ giao diện (`UI / Headed mode`).
    - Mở báo cáo kết quả `HTML Test Report`.

---

### 📍 Tương tác 3: Định dạng & Quản lý Test Case

> [!NOTE]
> **Công cụ AI:** `ChatGPT`  
> **Thời gian:** `28/09/2026` (~2:20 PM)

* **💬 Câu lệnh (Prompt):**
  ```text
  hãy tạo file test case dạng markdown/excel để tôi sử dụng trong bài testing
  ```

* **⚡ Kết quả do AI tạo ra:**
  * **Cấu trúc bảng Test Case:**
    `Test Case ID` | `Requirement/Function` | `Test Description` | `Preconditions` | `Test Steps` | `Test Data` | `Expected Result` | `Actual Result` | `Status`
  * **Quản lý:** Hướng dẫn xuất dữ liệu ra `Excel / CSV` và cách lưu trữ, quản lý tập trung trong Git Repository.

---

### 📍 Tương tác 4: Thực thi Automation Test trên giao diện Web

> [!NOTE]
> **Công cụ AI:** `ChatGPT`  
> **Thời gian:** `28/09/2026` (~2:30 PM)

* **💬 Câu lệnh (Prompt):**
  ```text
  chạy test tất cả test case trên giao diện Basic Calculator và cho tôi biết test nào Pass/Fail
  ```

* **⚡ Kết quả do AI tạo ra:**
  * **Môi trường test:** Hướng dẫn cấu hình Playwright chạy trực tiếp trên website:  
    `https://testsheepnz.github.io/BasicCalculator.html`
  * **Đánh giá kết quả:** Hướng dẫn đọc `Test Run Logs` và `HTML Report` để phân định trạng thái `PASS` hoặc `FAIL`.

---

### 📍 Tương tác 5: Mở rộng độ bao phủ kiểm thử (Test Coverage)

> [!NOTE]
> **Công cụ AI:** `ChatGPT`  
> **Thời gian:** `28/09/2026` (2:30 PM – 3:00 PM)

* **💬 Câu lệnh (Prompt):**
  ```text
  hãy thêm các test case mới để tăng độ bao phủ kiểm thử hệ thống
  ```

* **⚡ Kết quả do AI tạo ra:**
  * **Đề xuất Test Case bổ sung:**
    - `Boundary Value` (Giá trị biên)
    - `Invalid Input` (Dữ liệu không hợp lệ)
    - `Empty Input` (Dữ liệu rỗng)
    - `Division by Zero` (Chia cho số 0)
    - Xử lý chuỗi `Concatenate` & Tùy chọn `Integer`
    - Kiểm tra trạng thái nút bấm (`Button status`) & Giao diện (`UI`)
  * **Định dạng lưu trữ:** Đánh số Test Case mới và lưu dưới định dạng Markdown để push vào Repository.

---

### 📍 Tương tác 6: Viết Test Script & Phát hiện lỗi giao diện (Clear Button)

> [!IMPORTANT]
> **Công cụ AI:** `ChatGPT`  
> **Thời gian:** `28/09/2026` (8:00 PM – 9:00 PM)

* **💬 Câu lệnh (Prompt):**
  ```text
  hãy tạo Playwright test script cho các test case mới và chạy test để tìm lỗi
  ```

* **⚡ Kết quả do AI tạo ra:**
  * **Tạo File Script:** Khởi tạo file script `calculator-20.spec.js`.
  * **Phát hiện Bug:** Xác định sự cố tại chức năng nút `Clear` (Dữ liệu nhập không được xóa đúng so với `Expected Result`).
  * **Phân tích:** Đánh dấu Test Case trạng thái `FAIL` và phân tích lỗi xuất phát từ logic xử lý giao diện/ứng dụng.

---

### 📍 Tương tác 7: Phân tích Report & Lập Bug Report chi tiết

> [!WARNING]
> **Công cụ AI:** `ChatGPT`  
> **Thời gian:** `28/09/2026` (9:00 PM – 9:30 PM)

* **💬 Câu lệnh (Prompt):**
  ```text
  hãy phân tích report và tìm thêm bug theo template
  ```

* **⚡ Kết quả do AI tạo ra:**
  * **Phân tích nâng cao:** Phát hiện lỗi Validation khi gửi dữ liệu rỗng (`Empty Data Validation`) — Hệ thống vẫn cho phép xử lý tiếp dù dữ liệu chưa hợp lệ.
  * **Xuất Báo cáo Lỗi:** Khởi tạo tập tin Bug Report `BUG-10.md` chuẩn template gồm:
    - Mô tả lỗi (`Bug Description`)
    - Các bước tái hiện (`Steps to Reproduce`)
    - Kết quả kỳ vọng (`Expected Result`) vs Kết quả thực tế (`Actual Result`)
    - Nguyên nhân dự kiến (`Root Cause`)