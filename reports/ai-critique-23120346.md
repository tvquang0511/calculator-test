# AI Critique Report

**Sinh viên thực hiện:** 
- Họ và tên: Trần Vũ Quang
- Mã số sinh viên (MSSV): 23120346
- Môn học: Kiểm thử Phần mềm (Software Testing)

---

Trong quá trình thực hiện bài tập kiểm thử Basic Calculator, trợ lý AI đóng vai trò đắc lực trong việc khởi tạo cấu trúc kiểm thử, tự động hóa script Playwright và chuẩn hóa tài liệu GitHub. Tuy nhiên, AI đã bộc lộ những sai sót và sự thiên kiến nhất định.

Cụ thể, khi thiết kế kịch bản tự động, AI ban đầu đã đưa ra mã nguồn chưa hoàn thiện dẫn đến lỗi timeout 30 giây trên CI/CD: AI không lường trước được rằng mã nguồn web khi chia cho 0 sẽ dừng hàm mà không ẩn màn hình chờ (spinner), và ở Build 4, checkbox 'Integers only' bị khóa (disabled) khiến thao tác click bị treo. AI không phát hiện ra vấn đề này ngay từ đầu vì nó chỉ suy luận dựa trên logic lý thuyết thông thường trong môi trường lý tưởng, hoàn toàn thiếu khả năng tương tác với trạng thái DOM thực tế tại runtime.

Từ trải nghiệm này, tôi rút ra bài học sâu sắc về nguyên tắc hợp tác với AI là "Tin tưởng nhưng luôn phải kiểm chứng" (Trust, but Verify). AI là công cụ tăng năng suất tuyệt vời để tạo bản nháp và tự động hóa tác vụ lặp lại, nhưng con người (Human-in-the-loop) phải giữ vai trò quyết định, trực tiếp thực thi kịch bản, phân tích log lỗi và kiểm soát chất lượng cuối cùng.
