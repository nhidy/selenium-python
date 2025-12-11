# I. Mô tả
Để phục vụ cho việc render code auto test bằng jcodegen, cần xuất config files theo định dạng xác định từ files cấu hình form.

# II. Cài đặt môi trường
- Cần cài `nodejs`. Link download: https://nodejs.org/en/download

# III. Cấu trúc thư mục
- Folder `raw_forms/fo` chứa các files cấu hình form FO cần chuyển đổi
- Folder `raw_forms/bo` chứa các files cấu hình form BO cần chuyển đổi
- Folder `input_forms/fo` chứa các files cấu hình form FO đã chuyển đổi tạm trước khi chuyển thành file phục vụ cho jcodegen
- Folder `input_forms/bo` chứa các files cấu hình form BO đã chuyển đổi tạm trước khi chuyển thành file phục vụ cho jcodegen
- Folder `config_files/fo` chứa các files phục vụ cho jcodegen phần FO
- Folder `config_files/bo` chứa các files phục vụ cho jcodegen phần BO

# IV. Cách hoạt động
## 1. Chuyển đổi input_forms
- Mở cmd tại thư mục chứa file `get_input_forms.js`
- Chạy lệnh
```
node .\get_input_forms.js
```
- Sau khi chạy lệnh trên, trong folder `input_forms` sẽ có tất cả các files đã chuyển đổi từ các files trong folder `raw_forms`.
- Trong đó:
  - Param `folderRawForms`: `./raw_forms/fo` hoặc `./raw_forms/bo`
  - Param `folderInputForms`: `./input_forms/fo` hoặc `./input_forms/bo`

## 2. Chuyển đổi config_files
- Mở cmd tại thư mục chứa file `get_config_files.js`
- Chạy lệnh
```
node .\get_config_files.js
```
- Sau khi chạy lệnh trên, trong folder `config_files` sẽ có tất cả các files đã chuyển đổi từ các files trong folder `input_forms`.
- Trong đó:
  - Param `folderInputForms`: `./input_forms/fo` hoặc `./input_forms/bo`
  - Param `folderConfigFiles`: `./config_files/fo` hoặc `./config_files/bo`

## 3. Hướng dẫn lấy files cấu hình forms
- Đối với các form đã có file cấu hình trong git: vào thư mục `ShareFile/cms/CONFIGURATION_FOLDER` lấy file cấu hình form tương ứng copy để vào thư mục `raw_forms`
- Đối với các form chưa có file cấu hình, có thể vào swagger của cms (ip:port/api - với ip, port là được dẫn url tới ứng dụng web cms) và run api `/api/Form/DownloadZip` với các tham số file/app tương ứng cần lấy - với value null sẽ download tất cả - và để vào thư mục `raw_forms`
