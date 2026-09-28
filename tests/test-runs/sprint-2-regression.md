# BÁO CÁO THỰC THI KIỂM THỬ HỒI QUY - SPRINT 2 (SPRINT 2 REGRESSION RUN)

- **Dự án:** Basic Calculator Automation Testing
- **Chu kỳ thực thi:** Sprint 2 Regression Testing Cycle
- **Môi trường:** Windows 11 / Google Chrome & Chromium Headless (Playwright Test Engine)
- **Tài liệu tham chiếu:** `Basic_Calculator_Test_Design.xlsx` / `tests/comprehensive/calculator-80.spec.js`
- **Phạm vi kiểm thử:** Chạy toàn bộ bộ kiểm thử hồi quy mở rộng (80 Test Cases từ `TC-001` đến `TC-080`) trên Prototype và kiểm tra tính nhạy phát hiện defect trên các Build 1 đến 9.

---

## 1. Tổng quan Kết quả Thực thi

| Chỉ số | Giá trị | Tỷ lệ (%) |
| :--- | :---: | :---: |
| **Tổng số Test Cases thực thi** | 80 | 100% |
| **Passed (Đạt)** | 80 | 100% |
| **Failed (Không đạt)** | 0 | 0% |
| **Blocked (Bị nghẽn)** | 0 | 0% |
| **Thời gian thực thi trung bình** | ~28s (4 workers) | - |

---

## 2. Kết quả chi tiết theo Kịch bản Kiểm thử (Test Scenarios)

| Scenario ID | Test Scenario | Số lượng TC | Trạng thái | Ghi chú |
| :--- | :--- | :---: | :---: | :--- |
| **TS-001** | Addition (Phép cộng) | 11 | ✅ PASS | Đạt 100% với số dương, âm, 0, thập phân, số lớn 9 chữ số. |
| **TS-002** | Subtraction (Phép trừ) | 10 | ✅ PASS | Đạt 100% với kết quả dương, âm, bằng 0, số thập phân. |
| **TS-003** | Multiplication (Phép nhân) | 9 | ✅ PASS | Đạt 100% khi nhân với 0, 1, -1, số âm, số lớn. |
| **TS-004** | Division (Phép chia) | 10 | ✅ PASS | Đạt 100% với chia hết, có dư, số thập phân, chia số 0. |
| **TS-005** | Division by Zero (Chia cho 0) | 2 | ✅ PASS | Hệ thống bắt lỗi `Divide by zero error!` chính xác. |
| **TS-006** | Concatenate (Nối chuỗi) | 10 | ✅ PASS | Ghép chuỗi số, leading zero, chữ cái, ký tự đặc biệt, ô rỗng. |
| **TS-007** | Integers only (Ép kiểu số nguyên) | 6 | ✅ PASS | Kiểm tra cắt đuôi thập phân (`parseInt`), ép số nguyên dương/âm. |
| **TS-008** | Concatenate vs Integers only Dependency | 2 | ✅ PASS | Checkbox Integers only tự động ẩn & disabled khi chọn Concatenate. |
| **TS-009** | Input Validation (Kiểm tra dữ liệu nhập) | 7 | ✅ PASS | Báo lỗi chuẩn khi nhập ký tự chữ cái, đặc biệt, nhiều dấu chấm. |
| **TS-010** | Boundary Value Analysis (Giá trị biên) | 1 | ✅ PASS | Kiểm soát giới hạn `maxlength=10` trên ô nhập liệu. |
| **TS-011** | Clear Button Functionality | 2 | ✅ PASS | Xóa đúng kết quả Answer, reset checkbox Integers only, xóa lỗi đỏ. |
| **TS-012** | UI Loading & State | 1 | ✅ PASS | Trạng thái hiển thị spinner và restore nút bấm sau tính toán. |
| **TS-013** | Build Regression Testing | 9 | ✅ PASS | 9 Test Cases tự động phát hiện được 100% sai lệch của Build 1 đến 9. |

---

## 3. Khả năng phát hiện Bug của Bộ Test Suite trên Builds 1 - 9

| Build | Defect được gài sẵn trong Build | Mã Test Case phát hiện | Kết quả phát hiện |
| :---: | :--- | :---: | :---: |
| **Build 1** | Bỏ sót Input Validation, chấp nhận chuỗi không hợp lệ | `TC-071` | ✅ Phát hiện: Ra `NaN` thay vì báo lỗi |
| **Build 2** | Tráo đổi phép Add và Concatenate | `TC-072` | ✅ Phát hiện: `10 + 20` ra chuỗi `"1020"` |
| **Build 3** | Ép kiểu số học cho Concatenate | `TC-073` | ✅ Phát hiện: Nối chữ cái báo lỗi `"Number 1 is not a number"` |
| **Build 4** | Khóa cứng tùy chọn Integers only ở trạng thái ON | `TC-074` | ✅ Phát hiện: Kết quả luôn bị ép số nguyên, checkbox bị disabled |
| **Build 5** | Nút Clear bị vô hiệu hóa | `TC-075` | ✅ Phát hiện: Nút Clear bị disabled ngay khi chọn build |
| **Build 6** | Thiếu kiểm tra chia cho 0 | `TC-076` | ✅ Phát hiện: `12 / 0` ra `Infinity` thay vì báo lỗi |
| **Build 7** | Sử dụng kết quả Answer cũ làm First Number | `TC-077` | ✅ Phát hiện: Lần tính sau lấy kết quả lần trước |
| **Build 8** | Hoán đổi vị trí First Number và Second Number | `TC-078` | ✅ Phát hiện: `10 - 2` bị đảo thành `2 - 10 = -8` |
| **Build 9** | Ẩn và vô hiệu hóa các phần tử giao diện | `TC-079` | ✅ Phát hiện: Ô Second number và nút Calculate bị ẩn |

---

## 4. Kết luận Đợt Regression

- Toàn bộ 80 Test Cases trong bộ kịch bản tự động hóa đều vượt qua trên Prototype (chuẩn).
- Toàn bộ các khiếm khuyết trong các Build từ 1 đến 9 đều được bộ test case `TS-013` khoanh vùng và phát hiện chính xác 100%.
- Không phát sinh lỗi regression mới trên mã nguồn test framework.
