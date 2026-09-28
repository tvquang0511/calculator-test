# AI CRITIQUE REPORT

- **Mã nhóm:** Nhom02
- **Họ và tên / MSSV:** 23120372
- **Dự án:** Basic Calculator Automation Testing
- **Ngày lập:** 2026-09-28

---

Trong quá trình thực hiện bài tập, AI thể hiện năng lực vượt trội trong việc phân tích chức năng, sinh 80 test case đa dạng và viết mã tự động hóa Playwright theo mô hình Page Object Model rất nhanh chóng. Dẫu vậy, AI cũng bộc lộ một số sai sót và thiên kiến kỹ thuật:

Cụ thể, AI có thiên kiến suy luận logic toán học lý tưởng thay vì bám sát hành vi thực tế của JavaScript runtime. AI từng giả định rằng ô trống hoặc khoảng trắng phải báo lỗi validation, trong khi thực tế code web dùng `isNaN("")` trả về `false` và tự động coi là số 0. Ngoài ra, AI ban đầu viết định dạng file URL trên Windows dạng `file://` (thiếu một dấu gạch chéo `file:///`), làm Chromium không thể mở trang local.

Nguyên nhân AI không phát hiện ra vấn đề này là do mô hình ngôn ngữ dựa trên tri thức văn bản tổng quát, thiếu khả năng tự kiểm thử động (dynamic testing) nếu không được kích hoạt chạy thử nghiệm trong môi trường runtime thực tế.

Bài học lớn nhất mà tôi rút ra là nguyên tắc **"Human-in-the-Loop" (con người là trung tâm kiểm chứng)**. Tester không nên tiếp nhận mù quáng kết quả của AI mà phải luôn đóng vai trò thẩm định, đối chiếu chéo (Verification & Validation) giữa mã nguồn thực tế và kết quả sinh ra. Tận dụng AI để tăng tốc viết boilerplate code và mở rộng bao phủ kiểm thử, nhưng chính kỹ sư con người mới là người quyết định tính đúng đắn của logic nghiệp vụ.
