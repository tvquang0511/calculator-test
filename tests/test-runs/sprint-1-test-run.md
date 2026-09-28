# Test Run: Đợt kiểm thử đánh giá Prototype & Builds (Sprint 1)

- **Ngày chạy:** 2026-09-28
- **Môi trường:** Chrome 128 / Windows 11 / Playwright Automation
- **Người thực hiện:** QA Tester

---

## 1. Kết quả thực thi trên bản chuẩn: Prototype (Baseline)

| Test Case ID | Module | Tester | Result | Related Bug | Note |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **TC-UI-001** | UI | QA Team | **Pass** | None | Tất cả phần tử giao diện hiển thị và tương tác tốt |
| **TC-UI-002** | UI | QA Team | **Pass** | None | Checkbox Integers only bật/tắt chính xác |
| **TC-UI-003** | UI | QA Team | **Pass** | None | Nút Clear xóa kết quả và reset trạng thái |
| **TC-MATH-001** | Math | QA Team | **Pass** | None | Phép cộng $10 + 20 = 30$ chính xác |
| **TC-MATH-002** | Math | QA Team | **Pass** | None | Phép trừ $15 - 5 = 10$ chính xác |
| **TC-MATH-003** | Math | QA Team | **Pass** | None | Phép chia $7 / 2 = 3.5$ chính xác |
| **TC-MATH-004** | Math | QA Team | **Pass** | None | Bắt lỗi chia cho 0 `"Divide by zero error!"` |
| **TC-MATH-005** | Math | QA Team | **Pass** | None | Phép tính độc lập, không nhớ kết quả cũ |
| **TC-STR-001** | String | QA Team | **Pass** | None | Ghép chuỗi `Hello` + `World` = `HelloWorld` |
| **TC-VAL-001** | Validation | QA Team | **Pass** | None | Nhập chữ báo lỗi `"Number 1 is not a number"` |

---

## 2. Kết quả thực thi đánh giá trên các bản Builds (1 - 9)

| Test Case ID | Module | Build | Tester | Result | Related Bug | Note |
| :--- | :--- | :---: | :--- | :---: | :---: | :--- |
| **TC-VAL-001** | Validation | Build 1 | QA Team | **Fail** | #1 | Không kiểm tra kiểu số, trả về `abc10` |
| **TC-MATH-001** | Math | Build 2 | QA Team | **Fail** | #2 | Phép cộng bị biến thành ghép chuỗi (`1020`) |
| **TC-STR-001** | String | Build 2 | QA Team | **Fail** | #2 | Ghép chuỗi bị biến thành phép cộng (`30`) |
| **TC-STR-001** | String | Build 3 | QA Team | **Fail** | #3 | Chặn không cho ghép chuỗi chữ cái |
| **TC-MATH-003** | Math | Build 4 | QA Team | **Fail** | #4 | Bị làm tròn thành `3` thay vì `3.5` |
| **TC-UI-002** | UI | Build 4 | QA Team | **Fail** | #4 | Checkbox Integers only bị khóa cứng |
| **TC-UI-003** | UI | Build 5 | QA Team | **Fail** | #5 | Nút Clear bị disabled, không thể bấm |
| **TC-MATH-004** | Math | Build 6 | QA Team | **Fail** | #6 | Chia cho 0 không báo lỗi, ra `Infinity` |
| **TC-MATH-005** | Math | Build 7 | QA Team | **Fail** | #7 | Lấy Answer cũ thế vào First number ($5 + 20 = 25$) |
| **TC-MATH-002** | Math | Build 8 | QA Team | **Fail** | #8 | Đổi chỗ Number 1 & 2 ($5 - 15 = -10$) |
| **TC-UI-001** | UI | Build 9 | QA Team | **Blocked** | #9 | Ô Number 2 và nút Calculate bị ẩn hoàn toàn |
