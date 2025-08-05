FROM 27.3.1.180/python-edge:latest

WORKDIR /app
COPY . .

ENV TEST_HISTORY_PATH="/test_history"
ENV LOGS_PATH="/logs"
ENV REPORTS_PATH="/reports"

# RUN pip install --upgrade pip setuptools wheel && \
#     pip wheel fastapi uvicorn xmlrunner colorama jinja2 selenium==4.24.0 parameterized openpyxl pandas numpy PyYAML pyautogui unittest-xml-reporting markupsafe setuptools \
#     --no-cache-dir -w /wheels && \
#     pip install --no-cache-dir --no-compile --no-index --find-links=/wheels /wheels/*.whl && \
#     rm -rf /wheels && \
#     find /usr/local/lib/python3.11 -name "test*" -o -name "__pycache__" | xargs rm -rf && \
#     rm -rf /root/.cache

# 1. Cài đặt các thư viện bên ngoài từ requirements.txt
COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# 2. Thêm thư mục webui_test vào PYTHONPATH
# Bước này là để đảm bảo Python tìm thấy module webui_test
ENV PYTHONPATH="${PYTHONPATH}:/app"
# RUN python3 -m pip install --no-cache-dir .

# 3. Xóa các tệp không cần thiết để giảm kích thước image
# RUN find /usr/local/lib/python3.12 -name "test*" -o -name "__pycache__" | xargs rm -rf && \
#     rm -rf /root/.cache
RUN SITE_PACKAGES_PATH=$(python3 -c "import site; print(site.getsitepackages()[0])") && \
    find "$SITE_PACKAGES_PATH" -type d -name "__pycache__" -exec rm -rf {} + && \
    rm -rf /root/.cache

EXPOSE 8000

# CMD ["uvicorn", "main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
