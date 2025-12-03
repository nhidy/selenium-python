# UI-TEST
## 1. Environment settings
### 1.1 Install python 3.9.1 (or newer)
- Link tải file cài: https://www.python.org/downloads/windows/
- Link hướng dẫn cài: https://phoenixnap.com/kb/how-to-install-python-3-windows chỉ là tới "Step 5: Verify Pip Was Installed"


## 2. Virtual Environment
### 2.1 Create venv
```code
cd \cbs-neptune-autotest\ui-test
python -m venv venv
```
### 2.2 Active venv
```code
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\venv\Scripts\activate
```

### 2.3 Install libs
```code
pip install -r requirements.txt
```

## 3. Modules webui_test settings after active `venv`
### 3.1 Install modules webui_test and build source
```code
python setup.py install
```
Output: `Finished processing dependencies for webui-test==2.0.0`

### 3.2 Uninstall modules webui_test
```code
python -m pip uninstall webui_test
```

```code
Found existing installation: webui-test 2.0.0
Uninstalling webui-test-2.0.0:
  Would remove:
    d:\2022_autotest\source-code\cbs-neptune-autotest\ui-test\venv\lib\site-packages\webui_test-2.0.0-py3.9.egg
    d:\2022_autotest\source-code\cbs-neptune-autotest\ui-test\venv\scripts\charts_script.html
    d:\2022_autotest\source-code\cbs-neptune-autotest\ui-test\venv\scripts\heading.html
    d:\2022_autotest\source-code\cbs-neptune-autotest\ui-test\venv\scripts\report.html
    d:\2022_autotest\source-code\cbs-neptune-autotest\ui-test\venv\scripts\stylesheet.html
    d:\2022_autotest\source-code\cbs-neptune-autotest\ui-test\venv\scripts\template.html
Proceed (Y/n)?
```
- Hủy uninstall với ký tự `n`.
- Xác nhận uninstall với ký tự `y`. Output: `Successfully uninstalled webui-test-2.0.0`. 

### 3.3 Start FastAPI
#### 3.3.1 Run FastAPI at local for testing script
```code
uvicorn main:app --host 0.0.0.0 --port 8000
```
- Swagger UI: http://127.0.0.1:8000/docs

#### 3.3.2 Run FastAPI at server side
**Server Ubuntu**
- Cài đặt screen (nếu chưa có):
```
sudo apt update && sudo apt install screen # Debian/Ubuntu
sudo yum install screen # CentOS/RHEL
```

- Bắt đầu một phiên screen mới:
```
screen -S uitest_fastapi_server # '-S' đặt tên cho phiên để dễ quản lý
```

- Trong phiên screen này, chạy lệnh FastAPI của bạn (không dùng --reload):
```
cd /root/jits/cbs-neptune-autotest/ui-test
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000
```
- Tách rời khỏi phiên screen:
  - Nhấn tổ hợp phím: Ctrl + A, sau đó nhấn D.
  - Bạn sẽ quay lại terminal ban đầu và thấy thông báo như [detached from 12345. uitest_fastapi_server]. Server của bạn vẫn đang chạy.
- Thoát SSH an toàn.
- Để kết nối lại vào phiên screen sau này:
```
screen -r uitest_fastapi_server # Kết nối lại bằng tên
```
- Hoặc nếu bạn không nhớ tên:
```
screen -ls # Liệt kê các phiên screen đang chạy
screen -r <PID_or_session_name> # Kết nối lại
```

**Server Window**
- Run with cmd
```code
cd /cbs-neptune-autotest/ui-test
.\venv\Scripts\activate
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### 3.3.3 Run FastAPI with Docker
- Dockerfile
```code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

#### 3.3.4 Check status FastAPI
- Swagger UI: http://{{IP}}:8000/docs
- IP: ip of server

## 4. Run test script
### 4.1 Run file after active `venv`
- Cần chỉnh nội dung trỏ đến file test script nào trong file **run.py**
```code
cd ui-test\tests
python run.py
```

### 4.2 Run by API
#### 4.2.1 Run test suite
**HTTP Method:** `POST`

**URL:** `http://{{IP}}:8000/run_test`
- IP mà server chạy trên cùng 1 máy local: `127.0.0.1`
- IP theo server WINDOW đã cài: `192.168.1.226`
- IP theo server UBUNTU đã cài: `27.3.1.113`

**Body:**
| No | Parameter | Is require | Type | Length | Default value | Description |
| -- | --------- | ---------- | ---- | ------ | ------------- | ----------- |
| 1 | release_version | `Yes` | String |  |  | Release version cần run test suite |
| 2 | server_name | `Yes` | String |  |  | Server name cần run test suite |
| 3 | run_on_url | `Yes` | String |  |  | URL cần run test suite |
| 4 | username_login | `Yes` | String |  |  | user login vào hệ thống |
| 5 | password_login | `Yes` | String |  |  | password của user login vào hệ thống |
| 6 | one_app | `Yes` | String |  |  | user login được phân quyền chỉ có một app. `Y`: một app; `N`: nhiều app |
| 7 | browser | `Yes` | String |  |  | Google Edge: `edge` or `ed`; Google Chrome: `chrome` or `google chrome` or `gc`; Firefox: `firefox` or `ff` |
| 8 | headless | `Yes` | String |  |  | `Y`: chạy không UI; `N`: chạy có UI |
| 9 | customer_code | No | String |  |  | Customer code có mask |
| 10 | username_approve | `Yes` | String |  |  | user approve |
| 11 | password_approve | `Yes` | String |  |  | password của user approve |
| 12 | username_reverse | `Yes` | String |  |  | user reverse |
| 13 | password_reverse | `Yes` | String |  |  | password của user reverse |
| 14 | test_files | `Yes` | `Array` |  |  | tên file test under folder `test_dir/shwebank_run_by_api/`, nếu truyền [] sẽ chạy hết các file theo thứ tự mặt định |
| 15 | report_name | `Yes` | String |  |  | tên report muốn đặt tên |
| 16 | debug_mode | No | String |  |  | `Y`: chạy không xuất report; `N`: chạy có xuất report |
| 17 | hour_to_run | No | `Int` |  |  | giờ để run |
| 18 | minute_to_run | No | `Int` |  |  | phút để run |
| 19 | username_login_other_branch | No | String |  |  | user khác chi nhánh login vào hệ thống |
| 20 | password_login_other_branch | No | String |  |  | password của user khác chi nhánh login vào hệ thống |
| 21 | username_approve_other_branch | No | String |  |  | user khác chi nhánh approve |
| 22 | password_approve_other_branch | No | String |  |  | password của user khác chi nhánh approve |
| 23 | username_reverse_other_branch | No | String |  |  | user khác chi nhánh reverse |
| 24 | password_reverse_other_branch | No | String |  |  | password của user khác chi nhánh reverse |

**Example:**
```json
{
    "release_version": "Core-4.7.1",
    "server_name": "104",
    "run_on_url": "https://test-cbs.shwesit.jits.digital/login/",
    "username_login": "cashier003",
    "password_login": "Sh@123456",
    "one_app": "N",
    "browser": "edge",
    "headless": "N",
    "customer_code": "1-1-000000",
    "username_approve": "automanager",
    "password_approve": "Sh@123456",
    "username_reverse": "automanager",
    "password_reverse": "Sh@123456",
    "test_files": [
        "test_01_customer",
        "test_04_mortgage",
        "test_03_credit_compound"
    ],
    "report_name": "run_all",
    "debug_mode": null,
    "hour_to_run": null,
    "minute_to_run": null,
    "username_login_other_branch": null,
    "password_login_other_branch": null,
    "username_approve_other_branch": null,
    "password_approve_other_branch": null,
    "username_reverse_other_branch": null,
    "password_reverse_other_branch": null
}
```

### Response message
| No | Parameter | Type | Length | Description |
| -- | --------- | ---- | ------ | ----------- |
| 1 | message | String |  |  |
| 2 | run_id | String |  | Giá trị `UUID` |
| 3 | status | String |  | Trạng thái run: `running`, `completed`, `failed` |

**Example:**
```json
{
    "message": "Test run initiated",
    "run_id": "5eab1248-9b06-4108-aff6-b3ae60f25ecf",
    "status": "running"
}
```

#### 4.2.2 Check status run test suite

**HTTP Method:** `GET`

**URL:** `http://{{IP}}:8000/get_test_status/{{run_id}}`

**Body:**
| No | Parameter | Is require | Type | Length | Default value | Description |
| -- | --------- | ---------- | ---- | ------ | ------------- | ----------- |
| 1 | run_id | `Yes` | `UUID` |  |  | Giá trị của key `run_id` được trả về sau khi chạy API `/run_test` |

**Example:**
```
http://{{IP}}:8000/get_test_status/609b033b-d288-4ce9-b19f-241c6a8f83ed
```

### Response message
| No | Parameter | Type | Length | Description |
| -- | --------- | ---- | ------ | ----------- |
| 1 | run_id | String |  | Giá trị của key `run_id` yêu cầu check trạng thái run |
| 2 | status | String |  | `running`: đang run; `completed`: đã run hoàn thành, `failed`: đã run thất bại |
| 3 | result | Object |  | Thông tin log và report sau khi run |

**Example:**
```json
{
    "run_id": "609b033b-d288-4ce9-b19f-241c6a8f83ed",
    "status": "completed",
    "result": {
        "status": "completed",
        "passed": false,
        "output_log": "",
        "total_tests": 0,
        "failures": 1,
        "errors": 0,
        "skipped": 0,
        "successful": -1,
        "report_path": "D:\\2022_AutoTest\\source-code\\cbs-neptune-autotest\\ui-test\\reports\\Core-4.7.1-104-run_folders_30072025_195910.html"
    }
}
```

## 4. Optional
### 4.1  Uninstall selenium 3.141.0 and msedge-selenium-tools
```code
pip uninstall selenium 3.141.0
pip uninstall msedge-selenium-tools
```
### 4.2 Check thư viện đang dùng
```code
pip list
```