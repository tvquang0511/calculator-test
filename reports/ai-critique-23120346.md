# Nhận xét và Đánh giá về AI (AI Critique Report)

**Sinh viên thực hiện:** 
- Họ và tên: Tạ Vũ Quang
- Mã số sinh viên (MSSV): 23120346
- Môn học: Kiểm thử Phần mềm (Software Testing)

---

## Đánh giá và Phản biện về quá trình hợp tác với AI

Trong quá trình thực hiện bài tập kiểm thử ứng dụng Basic Calculator, trợ lý AI đã hỗ trợ đắc lực trong việc khởi tạo khung kiểm thử và tự động hóa mã nguồn, nhưng cũng bộc lộ một số giới hạn và thiếu sót quan trọng. Cụ thể, khi thiết kế kịch bản kiểm thử cho phép chia cho 0 và bản Build 4, AI ban đầu đã không lường trước được hành vi bất thường của mã nguồn giao diện: ứng dụng web kết thúc hàm tính toán mà không mở khóa màn hình chờ (loading spinner), đồng thời checkbox bị vô hiệu hóa (disabled). Điều này khiến kịch bản tự động hóa bằng Playwright rơi vào trạng thái chờ đợi vô hạn và bị lỗi timeout 30 giây khi chạy trên môi trường CI/CD của GitHub Actions.

Nguyên nhân AI không phát hiện ra vấn đề ngay từ đầu là do AI chỉ phân tích luồng logic toán học thuần túy trên lý thuyết mà thiếu khả năng trải nghiệm thực tế trạng thái giao diện động (dynamic DOM state) trong điều kiện runtime. AI có xu hướng mặc định rằng các thành phần giao diện luôn ở trạng thái sẵn sàng nhận tương tác (enabled), phản ánh sự thiên kiến về một môi trường kiểm thử lý tưởng.

Bài học cốt lõi rút ra về nguyên tắc hợp tác với AI là: AI là một công cụ tăng tốc tuyệt vời để phác thảo cấu trúc và sinh mã lặp lại, nhưng người kỹ sư bắt buộc phải giữ vai trò kiểm soát và đánh giá chất lượng cuối cùng (Human-in-the-loop). Tester không được tin tưởng tuyệt đối vào mã do AI tạo ra mà phải trực tiếp thực thi, phân tích kỹ các ngoại lệ biên thực tế và hiểu sâu sắc hành vi hệ thống để kịp thời tinh chỉnh kịch bản kiểm thử đạt độ ổn định cao nhất.
