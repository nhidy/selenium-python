# UI Auto Test

## 1. Environment settings
### 1.1 Install python 3.9.1 (or newer)
- Link tải file cài: https://www.python.org/downloads/windows/
- Link hướng dẫn cài: https://phoenixnap.com/kb/how-to-install-python-3-windows chỉ là tới "Step 5: Verify Pip Was Installed"

### 1.2 Install modules (mở cmd và gõ các lệnh sau và đợi downloads)
```code
python -m pip install pytest
python -m pip install pytest-html
python -m pip install requests
python -m pip install pycryptodome
python -m pip install  selenium
python -m pip install webdriver-manager
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

### 4.3 install modules (mở cmd và gõ các lệnh sau và đợi downloads)
```code
python -m pip install pytest
python -m pip install pytest-html
python -m pip install requests
python -m pip install pycryptodome


pip uninstall selenium 3.141.0
pip install --upgrade selenium
pip install selenium==4.24.0
pip install numpy==1.22.4

pip install pyodbc
pip install setuptools

pip uninstall pandas
pip uninstall openpyxl
pip uninstall numpy
pip uninstall unittest-xml-reporting

python -m pip uninstall pytest-html

pip show pandas
pip show openpyxl
pip show numpy
pip show pyodbc
pip show unittest

pip uninstall webdriver-manager
pip uninstall eyes-core              4.18.3
pip uninstall eyes-selenium
```
