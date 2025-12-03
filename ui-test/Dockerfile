FROM 27.3.1.180/autotest/test-env:latest

# Sao chép toàn bộ mã nguồn của bạn vào container
COPY . .
# COPY --chown=appuser:appuser . .

# Cài đặt dự án của bạn như một gói Python
RUN python3 -m pip install --no-cache-dir .

# Đặt biến môi trường để Python có thể tìm thấy các gói cục bộ
ENV PYTHONPATH="${PYTHONPATH}:/app"

ENV TEST_HISTORY_PATH="/test_history"
ENV LOGS_PATH="/logs"
ENV REPORTS_PATH="/reports"

# Thiết lập cổng cho FastAPI
EXPOSE 8000

# Lệnh mặc định để khởi động ứng dụng FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]