# Basic Calculator - Software Testing Project (Nhóm 02)

Dự án kiểm thử tự động hóa và quản lý chất lượng phần mềm cho ứng dụng [Basic Calculator](https://testsheepnz.github.io/BasicCalculator.html) theo quy chuẩn kiểm thử trên GitHub.

---

## 📌 Thành viên Nhóm 02
| STT | Họ và Tên | MSSV | Vai trò |
| :---: | :--- | :---: | :--- |
| 1 | **Tạ Vũ Quang** | **23120346** | Test Design & Automation |
| 2 | Trần Quang Tùng | 20120397 | QA & Test Execution |
| 3 | Phan Trọng Tín | 23120279 | Bug Triage & Regression |
| 4 | Nguyễn Thành Trung | 23120372 | Automation & CI/CD |

---

## 🔗 Đường dẫn xem GitHub Issues (Dành cho Giảng viên)
Toàn bộ các lỗi phát hiện trong quá trình kiểm thử (Bugs 1 đến 10) đã được tạo và quản lý trực tiếp trên GitHub Issues:
👉 **[Xem danh sách GitHub Issues của Dự án](https://github.com/tvquang0511/calculator-test/issues?q=is%3Aissue)**

---

## 📁 Cấu trúc Thư mục Dự án

```text
calculator-test/
├── .github/
│   ├── ISSUE_TEMPLATE/                    # Mẫu Bug Report, Test Run, Test Task (Slide 6 & 12)
│   └── workflows/test.yml                 # Cấu hình GitHub Actions CI chạy tự động Playwright
├── reports/                               # Báo cáo cá nhân của 4 thành viên nhóm
│   ├── ai-audit-report-[mssv].md          # Báo cáo tương tác với AI
│   ├── ai-critique-[mssv].md              # Đoạn văn nhận xét, phản biện về AI (200-300 từ)
│   └── git-commit-log-[mssv].md           # Trích xuất git log --graph --all --stat
├── tests/
│   ├── functional-requirements.md         # Đặc tả 11 Yêu cầu chức năng (FR-xx)
│   ├── test-cases/                        # 80 file Markdown đặc tả Test Case chia theo module
│   │   ├── math/                          # Phép toán cộng, trừ, nhân, chia (TC-001 -> TC-042)
│   │   ├── str/                           # Phép ghép chuỗi Concatenate (TC-043 -> TC-052)
│   │   ├── ui/                            # Tùy chọn Integers only, Clear, Spinner (TC-053 -> TC-060...)
│   │   ├── val/                           # Kiểm tra định dạng số, biên (TC-061 -> TC-068...)
│   │   └── build/                         # Kiểm thử hồi quy các bản Build 1-9 (TC-071 -> TC-079)
│   ├── test-runs/                         # Bảng ghi nhận kết quả Test Run (sprint-1, sprint-2)
│   ├── test-summary/                      # Traceability Matrix & Defect Summary Report
│   ├── bugs/                              # 10 hồ sơ Bug chi tiết (BUG-01 -> BUG-10)
│   ├── comprehensive/                     # Kịch bản kiểm thử tự động Playwright (80 Test Cases)
│   └── calculator.spec.js                 # Kịch bản kiểm thử chuẩn Prototype (10 Test Cases)
├── src/
│   └── basicCalculator.html               # Mã nguồn ứng dụng web kiểm thử
├── Basic_Calculator_Test_Design.xlsx      # Bảng thiết kế 80 test case bằng Excel
├── package.json
└── playwright.config.js
```

---

## 🚀 Hướng dẫn Chạy Kiểm thử Tự động

```bash
# 1. Cài đặt dependencies
npm install

# 2. Cài đặt trình duyệt Playwright
npx playwright install chromium

# 3. Chạy toàn bộ 90 test cases
npm test

# 4. Xem báo cáo giao diện HTML sinh động
npm run test:report
```
