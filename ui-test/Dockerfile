FROM selenium/standalone-chrome

# Cài đặt Python 3.11 và các công cụ cần thiết
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 \
    python3.11-distutils \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*
RUN python3.11 -m pip install --upgrade pip

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép tệp yêu cầu và cài đặt các thư viện Python
COPY requirements.txt .
RUN python3.11 -m pip install --no-cache-dir -r requirements.txt \
    # Thêm dòng này để xóa pip cache ngay sau khi cài đặt
    && rm -rf /root/.cache/pip

# Sao chép toàn bộ mã nguồn của bạn vào container
COPY . .

# Cài đặt dự án của bạn như một gói Python
RUN python3.11 -m pip install --no-cache-dir .

# Đặt biến môi trường để Python có thể tìm thấy các gói cục bộ
ENV PYTHONPATH="${PYTHONPATH}:/app"

ENV TEST_HISTORY_PATH="/test_history"
ENV LOGS_PATH="/logs"
ENV REPORTS_PATH="/reports"

# Thiết lập cổng cho FastAPI
EXPOSE 8000

# Lệnh mặc định để khởi động ứng dụng FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]