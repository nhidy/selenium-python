# 1. Tổng quan công nghệ
- Ngôn ngữ: Python (yêu cầu 3.9+).
- Framework kiểm thử: Selenium WebDriver (v4.34.0) kết hợp với `unittest`.
- Test Runner Service: FastAPI (dùng để kích hoạt test từ xa hoặc qua giao diện API).
- Core Framework: Module `webui_test` (được cài đặt như một thư viện Python).

# 2. Cấu trúc dự án 
- `main.py`: Entry point chính. Đây là một ứng dụng FastAPI server. Nó cung cấp các API để:
  - Trigger chạy test (`POST /run_test`).
  - Kiểm tra trạng thái test (`GET /get_test_status/{run_id}`).
  - Quản lý lịch sử, logs, và báo cáo (reports).
- `tests/`: Chứa các kịch bản test (test scripts) và file `run_by_api.py` (script thực thi test thực tế).
- `webui_test/`: Thư viện lõi chứa các hàm wrapper cho Selenium, xử lý thao tác form, logging, và report.
- `requirements.txt`: Danh sách các thư viện phụ thuộc.

# 3. Quy trình vận hành
## Bước 1: Thiết lập môi trường
- Cài đặt Python 3.9+.
- Tạo và kích hoạt virtual environment (`venv`).
- Cài đặt các thư viện phụ thuộc: `pip install -r requirements.txt`.
- Cài đặt module `webui_test`: `python setup.py install`.
## Bước 2: Khởi chạy Test Server
Chạy file `main.py` để khởi động FastAPI server:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```
Server sẽ lắng nghe các yêu cầu chạy test tại port 8000.

## Bước 3: Thực thi Test
### Qua API (Khuyên dùng cho tích hợp hệ thống/CI) Gửi request POST tới http://<IP>:8000/run_test với body JSON chứa cấu hình test (phiên bản, server, user login, danh sách file test cần chạy...).
- Luồng xử lý:
  - `main.py` nhận request, tạo một `run_id`.
  - Nó khởi tạo một background thread.
  - Thread này dùng `subprocess` để gọi lệnh chạy file `tests/run_by_api.py` với các tham số từ request.
  - `run_by_api.py` sử dụng `unittest` để load và chạy các test case từ thư mục `tests/test_dir/...`.
  - Kết quả được lưu vào file JSON `history` và HTML `report`.

# 4. Cơ chế hoạt động chi tiết
- Khi `run_by_api.py` chạy, nó sẽ:
  - Parse các tham số đầu vào (browser, headless, login info...).
  - Load các file test được chỉ định (hoặc chạy tất cả nếu không chỉ định).
  - Gọi `webui_test.main()` để thực thi test suite.
  - Sinh ra file report HTML trong thư mục `reports/`.
- `main.py` giám sát tiến trình này và cập nhật trạng thái (running/completed/failed) để người dùng có thể tra cứu qua API.