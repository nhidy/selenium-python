# UI Auto Test

## 1. Environment settings
### 1.1 Install python 3.9.1 (or newer)
- Link tải file cài: https://www.python.org/downloads/windows/
- Link hướng dẫn cài: https://phoenixnap.com/kb/how-to-install-python-3-windows chỉ là tới "Step 5: Verify Pip Was Installed"

### 1.2 Install modules (mở cmd và gõ các lệnh sau và đợi downloads)
```code
python -m pip install selenium==4.24.0
python -m pip install numpy
python -m pip install parameterized
python -m pip install colorama
python -m pip install openpyxl
python -m pip install PyYAML
python -m pip install unittest-xml-reporting
python -m pip install jinja2
python -m pip install markupsafe
python -m pip install fastapi
python -m pip install uvicorn
python -m pip install pandas
python -m pip install pyautogui
```

## 2. Modules webui_test settings
### 2.1 Install modules webui_test and build source
```code
cd \cbs-neptune-autotest\ui-test
python setup.py install
```
Output: `Finished processing dependencies for webui-test==2.0.0`

### 2.2 Uninstall modules webui_test
```code
cd \cbs-neptune-autotest\ui-test
python -m pip uninstall webui_test
```

Yêu cầu xác nhận uninstall
```code
Found existing installation: webui-test 2.0.0
Uninstalling webui-test-2.0.0:
  Would remove:
    c:\users\laptopnct\appdata\local\programs\python\python39\lib\site-packages\webui_test-2.0.0-py3.9.egg
    c:\users\laptopnct\appdata\local\programs\python\python39\scripts\charts_script.html
    c:\users\laptopnct\appdata\local\programs\python\python39\scripts\heading.html
    c:\users\laptopnct\appdata\local\programs\python\python39\scripts\report.html
    c:\users\laptopnct\appdata\local\programs\python\python39\scripts\stylesheet.html
    c:\users\laptopnct\appdata\local\programs\python\python39\scripts\template.html
Proceed (y/n)?
```
- Hủy uninstall với ký tự `n`.
- Xác nhận uninstall với ký tự `y`. Output: `Successfully uninstalled webui-test-2.0.0`. 
  - Nếu khác output này vì cmd không đủ quyền, cần phải xóa bằng tay trong thư mục path khi module webui_test được cài đặt "C:\Users\LaptopNCT\AppData\Local\Programs\Python\Python39\Lib\site-packages\" tùy theo máy tính mà phần "C:\Users\LaptopNCT\AppData\Local\" sẽ thay đổi.

## 3. Run test script
### 3.1 Run file lẻ
- Cần chỉnh nội dung trỏ đến file test script nào trong file **run.py**

```code
cd ui-test\tests
python run.py
```

### 3.2 Run file theo lô, giả lập nhiều users
```
cd  ..\cbs-neptune-autotest\ui-test\tests
example: run_multiple_scripts.bat 11 41
```

Note: 
- git pull
- Sửa file excel path
- Sủa nội dung file "run_multiple_scripts.bat"
- Các driver sẽ được tự động tải về ở path "C:\Users\LaptopNCT\.wdm\drivers"

### 3.3 Run theo API từ local
#### 3.3.1 Run test suite
**HTTP Method:** `POST`

**URL:** `http://{{IP}}:8000/run_tests_async`
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
| 14 | test_suite | `Yes` | String |  |  | tên test suite bao gồm folder name under folder `test_dir/shwebank/` |
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
    "release_version": "Core-4.5.1",
    "server_name": "104",
    "run_on_url": "https://test-cbs.shwesit.jits.digital/login/",
    "username_login": "autoteller",
    "password_login": "Sh@123456",
    "one_app": "Y",
    "browser": "edge",
    "headless": "N",
    "customer_code": "1-1-001797",
    "username_approve": "automanager",
    "password_approve": "Sh@123456",
    "username_reverse": "automanager",
    "password_reverse": "Sh@123456",
    "test_suite":"test_04_deposit_t1_pri_plus_int",
    "report_name": "test_DPT_T1_P+I",
    "debug_mode": null,
    "hour_to_run" : null,
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
| 1 | task_id | String |  | Giá trị `UUID` |

**Example:**
```json
{
    "message": "Test script started in background",
    "task_id": "a45c441a-9873-4afb-9db1-816c4ca84405"
}
```

#### 3.3.2 Kiểm tra trạng thái run test suite

**HTTP Method:** `GET`

**URL:** `http://{{IP}}:8000/tasks/{{task_id}}`

**Body:**
| No | Parameter | Is require | Type | Length | Default value | Description |
| -- | --------- | ---------- | ---- | ------ | ------------- | ----------- |
| 1 | task_id | `Yes` | `UUID` |  |  | Giá trị của key `task_id` được trả về sau khi chạy API `/run_tests_async` |

**Example:**
```
http://{{IP}}:8000/tasks/a45c441a-9873-4afb-9db1-816c4ca84405
```

### Response message
| No | Parameter | Type | Length | Description |
| -- | --------- | ---- | ------ | ----------- |
| 1 | task_id | String |  | Giá trị của key `task_id` yêu cầu check trạng thái run |
| 2 | status | String |  | `running`: task đang run; `completed`: task đã run hoàn thành (Note: sẽ bị xóa sau một thời gian), `failed`: task đã run thất bại |
| 3 | stdout | String |  | Thông tin log và report sau khi run |
| 4 | exec_status | String |  | Thông tin kết quả run |
| 5 | return_code | Int |  | `0`: thành công, `-1`: lỗi, `null`: đang run |

**Example:**
```json
{
    "task_id": "a45c441a-9873-4afb-9db1-816c4ca84405",
    "status": "running",
    "stdout": null,
    "exec_status": null,
    "return_code": null
}
```

```json
{
    "task_id": "d2f8b984-d224-4fc9-a568-a5bb2d080cf6",
    "status": "completed",
    "stdout": "...[32m2025-07-25 10:51:38 [INFO] Logout successful.[0m\n[33m2025-07-25 10:51:38 [WARNING] Killing driver: '<selenium.webdriver.edge.webdriver.WebDriver (session=\"5016b15a9a465bf7c9d0d6f23ce85001\")>'[0m\n[32m2025-07-25 10:51:42 [INFO] generated html file: file:///C:\\Users\\jwellet\\Desktop\\cbs-neptune-autotest\\ui-test\\tests\\reports\\test_04_regression_deposit_t1_fd_pri_plus_int_rollover_api_result_25072025_102853.html[0m\nAll tests completed successfully.\n[33m2025-07-25 10:51:42 [WARNING] Killing driver: 'None'[0m\n",
    "exec_status": "There was an error managing msedgedriver (error sending request for url (https://msedgedriver.azureedge.net/LATEST_RELEASE_138_WINDOWS)); using driver found in the cache\n.1.2.3.4.5.6.7.8.9.10.11.12.13.14.15.16.17.18.19.20.21",
    "return_code": 0
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