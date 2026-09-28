# Báo cáo Truy vết: Traceability Matrix (Requirement - Test Case - Bug)

Tài liệu này dùng để chứng minh độ bao phủ kiểm thử (Test Coverage), khả năng truy vết lỗi (Defect Traceability) và xác định phạm vi kiểm thử hồi quy (Regression Test).

---

## 1. Bảng Ma trận Truy vết (Traceability Matrix)

| Requirement | Test Case | Module | Result (Prototype) | Result (Builds) | Bug Issue | Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **FR-UI-01** | TC-UI-001 | UI | **Pass** | Blocked | #9 | Open |
| **FR-UI-02** | TC-UI-002 | UI | **Pass** | Fail | #4 | Open |
| **FR-UI-03** | TC-UI-003 | UI | **Pass** | Fail | #5 | Open |
| **FR-MATH-01** | TC-MATH-001 | Math | **Pass** | Fail | #2 | Open |
| **FR-MATH-02** | TC-MATH-002 | Math | **Pass** | Fail | #8 | Open |
| **FR-MATH-03** | TC-MATH-003 | Math | **Pass** | Fail | #4, #8 | Open |
| **FR-MATH-04** | TC-MATH-004 | Math | **Pass** | Fail | #6 | Open |
| **FR-MATH-05** | TC-MATH-005 | Math | **Pass** | Fail | #7 | Open |
| **FR-STR-01** | TC-STR-001 | String | **Pass** | Fail | #2, #3 | Open |
| **FR-VAL-01** | TC-VAL-001 | Validation | **Pass** | Fail | #1 | Open |

---

## 2. Phân tích Độ bao phủ (Coverage) & Truy vết (Traceability)

### 2.1. Coverage (Độ bao phủ yêu cầu)
- **Tổng số Requirement:** 10 yêu cầu chức năng (`FR-UI-01` đến `FR-VAL-01`).
- **Số Requirement đã kiểm thử:** 10/10 (Đạt **100% Coverage**).
- **Kết quả trên Prototype:** 10/10 Pass (Sản phẩm chuẩn đạt yêu cầu chất lượng bàn giao).

### 2.2. Defect Traceability (Truy vết lỗi)
Mỗi bug phát hiện đều được liên kết 2 chiều trực tiếp tới Test Case và Requirement:
- `Bug #1` $\leftrightarrow$ `TC-VAL-001` $\leftrightarrow$ `FR-VAL-01`
- `Bug #2` $\leftrightarrow$ `TC-MATH-001, TC-STR-001` $\leftrightarrow$ `FR-MATH-01, FR-STR-01`
- `Bug #3` $\leftrightarrow$ `TC-STR-001` $\leftrightarrow$ `FR-STR-01`
- `Bug #4` $\leftrightarrow$ `TC-UI-002, TC-MATH-003` $\leftrightarrow$ `FR-UI-02, FR-MATH-03`
- `Bug #5` $\leftrightarrow$ `TC-UI-003` $\leftrightarrow$ `FR-UI-03`
- `Bug #6` $\leftrightarrow$ `TC-MATH-004` $\leftrightarrow$ `FR-MATH-04`
- `Bug #7` $\leftrightarrow$ `TC-MATH-005` $\leftrightarrow$ `FR-MATH-05`
- `Bug #8` $\leftrightarrow$ `TC-MATH-002, TC-MATH-003` $\leftrightarrow$ `FR-MATH-02, FR-MATH-03`
- `Bug #9` $\leftrightarrow$ `TC-UI-001` $\leftrightarrow$ `FR-UI-01`

### 2.3. Regression Scope (Phạm vi kiểm thử hồi quy)
Khi các lỗi trên được Developer sửa và tạo Pull Request (`Fixes #...`), Tester chỉ cần kích hoạt workflow Playwright tự động chạy lại toàn bộ bộ test case `tests/calculator.spec.js` để xác nhận kết quả trước khi đóng Bug Issue.

---

## 3. Bộ chỉ số Bug Report cuối Sprint (Theo chuẩn Slide 14)

| Chỉ số | Số lượng | Ghi chú |
| :--- | :---: | :--- |
| **Total bugs** | **9** | 9 lỗi đặc thù phân bổ trên 9 bản build |
| **Open bugs** | **9** | Đang chờ Developer khắc phục |
| **Closed bugs** | **0** | Chưa merge PR sửa lỗi |
| **Blocker / P0** | **4** | Bug #2, #7, #8, #9 |
| **Critical / Major (P1)** | **3** | Bug #1, #3, #6 |
| **Medium / Minor (P2)** | **2** | Bug #4, #5 |

### Thống kê Bug theo Module:
- **Math:** 5 bugs (Chiếm 55.6% - Module có rủi ro logic cao nhất)
- **UI:** 3 bugs (Chiếm 33.3%)
- **Validation:** 1 bug (Chiếm 11.1%)
- **String:** 1 bug (Tích hợp trong Math/Str)
