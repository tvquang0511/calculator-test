# Basic Calculator - Software Testing Project (Nhóm 02)

Dự án kiểm thử tự động hóa và quản lý chất lượng phần mềm cho ứng dụng [Basic Calculator](https://testsheepnz.github.io/BasicCalculator.html) tuân thủ đầy đủ quy chuẩn quản lý Test Case và Bug Report trên GitHub.

---

## 🔗 Liên kết Quan trọng dành cho Giảng viên

- 🐞 **Quản lý Bug trên GitHub Issues:** [Xem danh sách toàn bộ Bug Issues](https://github.com/tvquang0511/calculator-test/issues?q=is%3Aissue)
- 🚀 **Kết quả CI/CD tự động:** [Xem lịch sử chạy GitHub Actions](https://github.com/tvquang0511/calculator-test/actions)
- 📊 **Ma trận Truy vết (Traceability Matrix):** [Xem file Traceability Matrix](tests/test-summary/traceability-matrix.md)

---

## 📌 Tổng quan Dự án

Dự án thực hiện kiểm thử ứng dụng **Basic Calculator** bao gồm:
1. **Phiên bản chuẩn (Prototype):** Hoạt động chuẩn xác 100% mọi chức năng tính toán, kiểm tra dữ liệu và giao diện.
2. **Các phiên bản thử nghiệm (Builds 1 đến 9):** Tác giả cố tình cài cắm các lỗi nghiệp vụ khác nhau (bỏ qua kiểm tra số, tráo đổi phép toán, khóa giao diện, lỗi chia cho 0...).
3. **Mục tiêu:** Xây dựng bộ kịch bản kiểm thử tự động (Playwright) và quy trình quản lý chất lượng khép kín để phát hiện, báo cáo và truy vết toàn bộ các lỗi trên.

---

## 📁 Cấu trúc Thư mục Dự án

Cấu trúc thư mục được thiết kế chuẩn mực theo đúng bài giảng môn học:

```text
calculator-test/
├── .github/
│   ├── ISSUE_TEMPLATE/                    # Mẫu Issue chuẩn: Bug Report, Test Run, Test Task
│   │   ├── bug_report.md
│   │   ├── test_run.md
│   │   └── test_task.md
│   └── workflows/
│       └── test.yml                       # GitHub Actions tự động kiểm thử khi push/PR
│
├── reports/                               # Báo cáo bắt buộc của các thành viên nhóm
│   ├── ai-audit-report-[mssv].md          # Báo cáo minh bạch tương tác AI
│   ├── ai-critique-[mssv].md              # Nhận xét, phản biện về AI (200-300 từ)
│   └── git-commit-log-[mssv].md           # Nhật ký trích xuất git log --graph --all --stat
│
├── tests/                                 # Toàn bộ tài liệu và mã nguồn kiểm thử
│   ├── functional-requirements.md         # Đặc tả 11 Yêu cầu chức năng (FR-01 đến FR-11)
│   ├── test-cases/                        # 80 Test Case chi tiết định dạng Markdown chuẩn
│   │   ├── math/                          # Phép toán cộng, trừ, nhân, chia (TC-001 -> TC-042)
│   │   ├── str/                           # Phép ghép chuỗi Concatenate (TC-043 -> TC-052)
│   │   ├── ui/                            # Tùy chọn Integers only, Clear, Spinner (TC-053 -> TC-060...)
│   │   ├── val/                           # Kiểm tra định dạng số, biên (TC-061 -> TC-068...)
│   │   └── build/                         # Kiểm thử hồi quy trên các bản Build (TC-071 -> TC-079)
│   ├── test-runs/                         # Nhật ký thực thi kiểm thử (sprint-1, sprint-2)
│   ├── test-summary/                      # Traceability Matrix & Báo cáo tổng kết khiếm khuyết
│   ├── bugs/                              # 10 hồ sơ Bug chi tiết (BUG-01 -> BUG-10)
│   ├── comprehensive/                     # Bộ 80 kịch bản kiểm thử tự động Playwright (POM)
│   └── calculator.spec.js                 # Bộ 10 kịch bản kiểm thử nghiệm thu Prototype
│
├── src/
│   └── basicCalculator.html               # Mã nguồn ứng dụng web được kiểm thử
├── Basic_Calculator_Test_Design.xlsx      # Bảng thiết kế Test Case bằng Excel
├── package.json                           # Cấu hình dự án Node.js & Playwright
└── playwright.config.js                   # Cấu hình Playwright Test Runner
```

---

## 🔄 Luồng Quy trình Kiểm thử (Testing Workflow)

Quy trình quản lý chất lượng được vận hành liên tục theo 6 bước chuẩn:

$$\text{Requirement (FR)} \longrightarrow \text{Test Case (TC)} \longrightarrow \text{Test Run} \longrightarrow \text{Bug Issue} \longrightarrow \text{Fix (PR)} \longrightarrow \text{Retest \& Close}$$

1. **Requirement (FR):** Phân tích và mã hóa 11 yêu cầu chức năng (`FR-MATH-01`, `FR-VAL-01`...) trong [functional-requirements.md](tests/functional-requirements.md).
2. **Test Case (TC):** Thiết kế 80 test case chi tiết theo quy ước `TC-[MODULE]-[NUMBER]` và lưu trữ dưới dạng file Markdown trong thư mục `tests/test-cases/`.
3. **Test Run:** Thực thi kịch bản kiểm thử tự động bằng Playwright, ghi nhận kết quả và mã bug liên quan vào `tests/test-runs/`.
4. **Bug Report:** Với mỗi test case bị Fail, tạo Issue trên GitHub theo template `.github/ISSUE_TEMPLATE/bug_report.md` với liên kết 2 chiều (`Found by Test Case: TC-xxx`).
5. **Fix & PR:** Lập trình viên sửa lỗi trên branch riêng và tạo Pull Request có ghi chú `Fixes #...` để liên kết tới Bug Issue.
6. **Retest & Traceability:** Tester chạy lại kịch bản kiểm thử, kiểm tra hồi quy, comment xác nhận trước khi đóng bug và tổng hợp vào [traceability-matrix.md](tests/test-summary/traceability-matrix.md).

---

## 🛠️ Hướng dẫn Cài đặt & Chạy Kiểm thử Tự động

### 1. Yêu cầu Môi trường
- Đã cài đặt **Node.js** (phiên bản 18 trở lên).
- Trình duyệt Chrome / Chromium.

### 2. Cài đặt Dependencies
Mở terminal tại thư mục gốc của dự án và chạy:

```bash
# Cài đặt các thư viện phụ thuộc
npm install

# Cài đặt trình duyệt cho Playwright
npx playwright install chromium
```

### 3. Các lệnh thực thi Kiểm thử

| Lệnh chạy | Mô tả |
| :--- | :--- |
| `npm test` | Chạy toàn bộ **90 Test Cases** tự động (Playwright Test Runner) |
| `npm run test:report` | Mở báo cáo kiểm thử trực quan dạng giao diện web HTML của Playwright |
| `npm run test:matrix` | Chạy script quét lần lượt cả **10 bản Build** và tự động xuất ma trận kết quả |

---

## 📋 Tóm tắt Điểm khác biệt & Lỗi phát hiện trên các Build

| Bản Build | Lỗi phát hiện (Defect) | Phân loại lỗi | Mã Bug |
| :--- | :--- | :---: | :---: |
| **Prototype** | Hoạt động chuẩn xác 100% mọi chức năng (Đạt 10/10 PASS) | Baseline | Không |
| **Build 1** | Bỏ qua kiểm tra dữ liệu số; nhập chữ vẫn tính và trả về `NaN` hoặc ghép chuỗi | High | [#1](https://github.com/tvquang0511/calculator-test/issues/1) |
| **Build 2** | Hoán đổi ngược logic: chọn Add thành nối chuỗi, chọn Concatenate thành phép cộng | Critical | [#5](https://github.com/tvquang0511/calculator-test/issues/5) |
| **Build 3** | Luôn ép mọi input là số; chặn không cho ghép chuỗi văn bản bằng cảnh báo lỗi | High | [#6](https://github.com/tvquang0511/calculator-test/issues/6) |
| **Build 4** | Checkbox "Integers only" bị khóa cứng (disabled & checked), luôn ép ra số nguyên | Medium | [#7](https://github.com/tvquang0511/calculator-test/issues/7) |
| **Build 5** | Nút "Clear" bị vô hiệu hóa (`disabled = true`) ngay khi chọn Build | Medium | [#8](https://github.com/tvquang0511/calculator-test/issues/8) |
| **Build 6** | Bỏ qua kiểm tra chia cho 0; hiển thị kết quả là `Infinity` thay vì báo lỗi | High | [#9](https://github.com/tvquang0511/calculator-test/issues/9) |
| **Build 7** | Lấy giá trị của ô Answer cũ làm First Number cho phép tính tiếp theo | Critical | [#10](https://github.com/tvquang0511/calculator-test/issues/10) |
| **Build 8** | Hoán đổi vị trí giữa Number 1 và Number 2 trước khi tính toán ($15 - 5$ thành $5 - 15$) | Critical | [#11](https://github.com/tvquang0511/calculator-test/issues/11) |
| **Build 9** | Ẩn ô `Second number` và nút `Calculate`, làm tê liệt toàn bộ ứng dụng | Blocker | [#12](https://github.com/tvquang0511/calculator-test/issues/12) |

---

## 📦 Hướng dẫn Đóng gói Nộp bài (`MaNhom.zip`)

Để nộp bài, chỉ cần chạy file script đóng gói đã chuẩn bị sẵn:

```bash
python create_submission_zip.py
```

File nén **`Nhom02.zip`** sẽ được tự động tạo với dung lượng nhẹ (~`740 KB`), chứa đầy đủ thư mục `tests/`, `reports/`, `src/`, file Excel thiết kế và tự động loại trừ các thư mục rác (`node_modules`, `.git`).
