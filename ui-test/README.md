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
| 6 | browser | No | String |  | `chrome` | Google Edge: `edge` or `ed`; Google Chrome: `chrome` or `google chrome` or `gc`; Firefox: `firefox` or `ff` |
| 7 | customer_code | No | String |  |  | Customer code của personal có mask |
| 8 | customer_code_corporate | No | String |  |  | Customer code của corporate có mask |
| 9 | username_approve | `Yes` | String |  |  | user approve |
| 10 | password_approve | `Yes` | String |  |  | password của user approve |
| 11 | username_reverse | `Yes` | String |  |  | user reverse |
| 12 | password_reverse | `Yes` | String |  |  | password của user reverse |
| 13 | test_files | `Yes` | `Array` |  |  | tên file test under folder `test_dir/shwebank_run_by_api/`, nếu truyền [] sẽ chạy hết các file theo thứ tự mặt định |
| 14 | report_name | `Yes` | String |  |  | tên report muốn đặt tên |
| 15 | username_login_other_branch | No | String |  |  | user khác chi nhánh login vào hệ thống |
| 16 | password_login_other_branch | No | String |  |  | password của user khác chi nhánh login vào hệ thống |
| 17 | username_approve_other_branch | No | String |  |  | user khác chi nhánh approve |
| 18 | password_approve_other_branch | No | String |  |  | password của user khác chi nhánh approve |
| 19 | username_reverse_other_branch | No | String |  |  | user khác chi nhánh reverse |
| 20 | password_reverse_other_branch | No | String |  |  | password của user khác chi nhánh reverse |
| 21 | app_name | No | String |  | `Shwebank` | Tên ứng dụng, ex: Demo Bank. |
| 22 | one_app | No | String |  | `Y` | user login được phân quyền chỉ có một app. `Y`: một app; `N`: nhiều app |
| 23 | headless | No | String |  | `N` | `Y`: chạy không UI; `N`: chạy có UI |
| 24 | f8_config | No | String |  | `S` | Cấu hình search F8 (`S`: Status, `N`: Normal) |
| 25 | folder_name | No | String |  | `shwebank_run_by_api` | Tên thư mục chứa script test, ex: shwebank_bo_approval. |

**Example:**
```json
{
    "release_version": "Core-4.15.1",
    "server_name": "117",
    "run_on_url": "https://demo-cbs.finasit.jits.digital/login/",
    "username_login": "autoteller",
    "password_login": "Jits@123",
    "browser": "edge", // defult: chrome
    "customer_code": "1-1-056856", //117
    "customer_code_corporate": "3-6-000026", //117
    "username_approve": "automanager",
    "password_approve": "Jits@123",
    "username_reverse": "automanager",
    "password_reverse": "Jits@123",
    "test_files": [
        // "check_env"
        "test_01_customer",
        "test_02_deposit_01_current",
        "test_02_deposit_02_s1_savings",
        "test_02_deposit_03_1m_no_rollover",
        "test_02_deposit_03_1m_pri_only",
        "test_02_deposit_03_1m_pri_plus_int",
        "test_02_deposit_04_prepaid_no_rollover",
        "test_02_deposit_04_prepaid_pri_only",
        "test_02_deposit_gift_cheque",
        "test_02_deposit_payment_order",
        "test_03_credit_compound",
        "test_04_mortgage",
        "test_05_fixed_asset",
        "test_06_payment",
        "test_07_money_market",
        // "test_08_fx_transaction"
        "test_08_fx_transaction_section",
        "test_09_trade",
        "test_11_internal_transaction"
        // "test_verify_transaction"
    ],
    "report_name": "shwebank_regression",
    "username_login_other_branch": "autoteller005",
    "password_login_other_branch": "Jits@123",
    "username_approve_other_branch": "automanager005",
    "password_approve_other_branch": "Jits@123",
    "username_reverse_other_branch": "automanager005",
    "password_reverse_other_branch": "Jits@123"
    // "app_name": "Demo Bank" // defult: "Shwebank"
    // "one_app": "N", // defult: Y
    // "headless": "Y", // defult: N
    // "f8_config": "N" // defult: "S"
    // "folder_name": "shwebank_bo_approval"
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
        "total_tests": 1,
        "failures": 1,
        "errors": 0,
        "skipped": 0,
        "successful": 0,
        "report_path": "D:\\2022_AutoTest\\source-code\\cbs-neptune-autotest\\ui-test\\reports\\Core-4.7.1-104-run_folders_30072025_195910.html"
    }
}
```

## 5. Optional
### 5.1  Uninstall selenium 3.141.0 and msedge-selenium-tools
```code
pip uninstall selenium 3.141.0
pip uninstall msedge-selenium-tools
```
### 5.2 Check thư viện đang dùng
```code
pip list
```

## 6. Unit test for ui-test
- Các script unit test các thành phần chính được đặt ở folder `ui-test/tests/unit`:
  - main.py
  - run_by_api.py
  - case.py
  - form_action.py
  - wrapper.py

- Cách run script unit test sau mỗi lần sửa code hàm chính:
```code
py tests/unit/test_config_loading.py
```
- Cách run folder unit sau mỗi lần sửa code hàm chính:
```code
py -m unittest discover tests/unit
```