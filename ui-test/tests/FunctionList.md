# I. Functions used for testcase
## 1.1 BO screen
### 1.1.1 Enter value functions
- `bo_write`: tag name "input": Viết account number, customer code,… trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_single`: tag name "input": Viết account number, customer code,… trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_group`: tag name "input": Viết account number, customer code,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_group_single`: tag name "input": Viết account number, customer code,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_multi`: tag name "input": Viết account number, customer code,… loại field có multi field con trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
  - collap_name: tên collap của multi field
- `bo_write_multi_single`: tag name "input": Viết account number, customer code,… loại field có multi field con trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
  - collap_name: tên collap của multi field
- `bo_write_text`: tag name "textarea": Viết account name, customer name,… trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_text_single`: tag name "textarea": Viết account name, customer name,… trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_text_group`: tag name "textarea": Viết account name, customer name,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_text_group_single`: tag name "textarea": Viết account name, customer name,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_text_multi`: tag name "textarea": Viết account name, customer name,… loại field có multi field con trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
  - collap_name: tên collap của multi field
- `bo_write_text_multi_single`: tag name "textarea": Viết account name, customer name,… loại field có multi field con trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
  - collap_name: tên collap của multi field
- `bo_write_date`: Viết date trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_date_single`: Viết date trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_number`: Viết number trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_number_single`: Viết number trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_number_group`: Viết number loại field được gom nhóm trong cùng 1 dòng trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_write_number_group_single`: Viết number loại field được gom nhóm trong cùng 1 dòng trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_select`: Chọn giá trị trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_select_single`: Chọn giá trị trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_select_group`: Chọn giá trị loại field được gom nhóm trong cùng 1 dòng trong màn hình BO có tab. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `bo_select_group_single`: Chọn giá trị loại field được gom nhóm trong cùng 1 dòng trong màn hình BO đơn (không có tab). Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu

### 1.1.2 Get functions
- `bo_get_value`: tag name "input": Lấy ra giá trị account number, customer code,… trong màn hình BO có tab
- `bo_get_value_single`: tag name "input": Lấy ra giá trị account number, customer code,… trong màn hình BO đơn (không có tab)
- `bo_get_value_group`: tag name "input": Lấy ra giá trị account number, customer code,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO có tab
- `bo_get_value_group_single`: tag name "input": Lấy ra giá trị account number, customer code,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO đơn (không có tab)
- `bo_get_date`: Lấy ra giá trị date của input, trong màn hình BO có tab
- `bo_get_date_single`: Lấy ra giá trị date của input, trong màn hình BO đơn (không có tab)
- `bo_get_select`: Lấy ra giá trị của select-box, trong màn hình BO có tab
- `bo_get_select_single`: Lấy ra giá trị của select-box, trong màn hình BO đơn (không có tab)
- `bo_get_select_group`: Lấy ra giá trị của select-box, loại field được gom nhóm trong cùng 1 dòng trong màn hình BO có tab
- `bo_get_select_group_single`: Lấy ra giá trị của select-box, loại field được gom nhóm trong cùng 1 dòng trong màn hình BO đơn (không có tab)
- `bo_get_text`: tag name "textarea": Lấy ra giá trị account name, customer name,… trong màn hình BO có tab
- `bo_get_text_single`: tag name "textarea": Lấy ra giá trị account name, customer name,… trong màn hình BO đơn (không có tab)
- `bo_get_text_group`: tag name "textarea": Lấy ra giá trị account name, customer name,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO có tab
- `bo_get_text_group_single`: tag name "textarea": Lấy ra giá trị account name, customer name,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO đơn (không có tab)

### 1.1.3 Assert functions
- `bo_assert_value`: tag name "input": Lấy ra giá trị account number, customer code,… trong màn hình BO có tab
- `bo_assert_value_single`: tag name "input": Lấy ra giá trị account number, customer code,… trong màn hình BO đơn (không có tab)
- `bo_assert_value_group`: tag name "input": Lấy ra giá trị account number, customer code,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO có tab
- `bo_assert_value_group_single`: tag name "input": Lấy ra giá trị account number, customer code,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO đơn (không có tab)
- `bo_assert_date`: Lấy ra giá trị date của input, trong màn hình BO có tab
- `bo_assert_date_single`: Lấy ra giá trị date của input, trong màn hình BO đơn (không có tab)
- `bo_assert_select`: Lấy ra giá trị của select-box, trong màn hình BO có tab
- `bo_assert_select_single`: Lấy ra giá trị của select-box, trong màn hình BO đơn (không có tab)
- `bo_assert_select_group`: Lấy ra giá trị của select-box, loại field được gom nhóm trong cùng 1 dòng trong màn hình BO có tab
- `bo_assert_select_group_single`: Lấy ra giá trị của select-box, loại field được gom nhóm trong cùng 1 dòng trong màn hình BO đơn (không có tab)
- `bo_assert_text`: tag name "textarea": Lấy ra giá trị account name, customer name,… trong màn hình BO có tab
- `bo_assert_text_single`: tag name "textarea": Lấy ra giá trị account name, customer name,… trong màn hình BO đơn (không có tab)
- `bo_assert_text_group`: tag name "textarea": Lấy ra giá trị account name, customer name,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO có tab
- `bo_assert_text_group_single`: tag name "textarea": Lấy ra giá trị account name, customer name,… loại field được gom nhóm trong cùng 1 dòng trong màn hình BO đơn (không có tab)

### 1.1.4 Click functions
- `bo_click_collap`: Click vào collap name của multi field trong màn hình BO có tab. Đầu vào:
  - collap_name: tên collap của multi field
- `bo_click_collap_single`: Click vào collap name của multi field trong màn hình BO đơn (không có tab). Đầu vào:
  - collap_name: tên collap của multi field
- `bo_click_checkbox`: Click vào check-box của title trong màn hình BO có tab. Đầu vào:
  - title: tên title field
- `bo_click_checkbox_single`: Click vào check-box của title trong màn hình BO đơn (không có tab). Đầu vào:
  - title: tên title field

## 1.2 FO screen
### 1.2.1 Enter value functions
- `fo_write`: tag name "input": Viết account number, customer code,… trong màn hình FO. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `fo_write_group`: tag name "input": Viết account number, customer code,… loại field được gom nhóm trong cùng 1 dòng trong màn hình FO. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `fo_write_multi`: tag name "input": Viết account number, customer code,… loại field có multi field con trong màn hình FO. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
  - collap_name: tên collap của multi field
- `fo_write_text`: tag name "textarea": Viết account name, customer name,… trong màn hình FO. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `fo_write_text_group`: tag name "textarea": Viết account name, customer name,… loại field được gom nhóm trong cùng 1 dòng trong màn hình FO. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `fo_write_text_multi`: tag name "textarea": Viết account name, customer name,… loại field có multi field con trong màn hình FO. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
  - collap_name: tên collap của multi field
- `fo_write_date`: Viết date trong màn hình FO. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `fo_write_number`: Viết number trong màn hình FO. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu
- `fo_select`: Chọn giá trị trong màn hình FO. Đầu vào:
  - title: title của trường cần nhập liệu
  - value: giá trị cần nhập liệu

### 1.2.2 Get functions
- `fo_get_value`: tag name "input": Lấy ra giá trị account number, customer code,… trong màn hình FO
- `fo_get_value_group`: tag name "input": Lấy ra giá trị account number, customer code,… loại field được gom nhóm trong cùng 1 dòng trong màn hình FO
- `fo_get_date`: tag name "input": Lấy ra giá trị date của input, trong màn hình FO
- `fo_get_select`: Lấy ra giá trị của select-box, trong màn hình FO
- `fo_get_select_group`: Lấy ra giá trị của select-box, loại field được gom nhóm trong cùng 1 dòng trong màn hình FO
- `fo_get_text`: tag name "textarea": Lấy ra giá trị account name, customer name,… trong màn hình FO
- `fo_get_text_group`: tag name "textarea": Lấy ra giá trị account name, customer name,… loại field được gom nhóm trong cùng 1 dòng trong màn hình FO

### 1.2.3 Click functions
- `fo_click_collap`: Click vào collap name của multi field trong màn hình FO. Đầu vào:
  - collap_name: tên collap của multi field
- `fo_click_checkbox`: Click vào check-box của title trong màn hình FO. Đầu vào:
  - title: tên title field

# II. System commands
- start_class
- end_class
- setUpClass
- tearDownClass
- start
- end
- setUp
- tearDown
- get_url

# III. Special functions
- `open_transaction_journal`: mở màn hình F8
- `close_bank`: đóng bank
- `open_bank`: mở bank
- `start_batch`: start batch
- `get_batch_process`: get percent run batch
- `run_batch`: close branch and start batch
- `get_logged_branch_code`: get branch code của user đang login
- `take_screenshot`: chụp hình màn hình, truyền vào path và tên file *.png
- `lookup_data`: tìm kiếm giá trị và chọn ở popup
  - Đầu vào:
    - title: tên field có lookup
    - column_name: tên cột của bảng trong popup
    - value: giá trị của ô theo cột cần chọn
- `get_text_form_title_header_popup`: get title trong header của popup
- `get_text_form_title_popup`: get title trong content của popup
- `close_popup`: click close popup

 <!-- table function -->
write_search_table_column: search giá trị tại 1 column của table

<!-- scroll to element, scroll to page-->
`scroll_to_element`: scroll tới element
`scroll_to_top_page`: scroll tới đầu trang
`scroll_to_bottom_page` : scroll tới cuối trang

# VI. Các hàm đã chuyển dùng Selenium 4.x
## 4.1 Form functions
- `wait`: đợi bao nhiêu giây, default 1 giây
  - Đầu vào: số seconds cần đợi, không truyền số thì default 1 giây
- `login`: login vào hệ thống
  - Đầu vào: 
    - username: tên đăng nhập
    - password: mật khẩu
- `open_app`: chọn app cần mở sau khi login thành công
  - Đầu vào: app_name cần mở
- `logout`: logout khỏi hệ thống
- `scroll_down`: lăn xuống, default 1000 pixels
- `scroll_up` : lăn lên, default 1000 pixels
- `switch_to_core_banking`: chuyển về màn hình chính "Core Banking"
- `close_voucher`: đóng tất cả các màn hình voucher, ngoại trừ màn hình chính "Core Banking"
- `open_fo`: mở giao dịch FO 

## 4.2 Wait functions
- `wait_for_element_visibility_by_xpath`: đợi element tồn tại trong DOM, không check case bị che bởi các element khác
  - Đầu vào:
    - xpath: chuỗi xpath cần đợi
    - timeout: thời gian đợi, default 120 giây
  - Đầu ra:
    - Trả về element nếu tồn tại
    - Trả về None nếu không tồn tại
- `wait_for_element_enabled_by_xpath`: đợi element có thể click, áp dụng cho tagname là button
  - Đầu vào:
    - xpath: chuỗi xpath cần đợi
    - timeout: thời gian đợi, default 120 giây
  - Đầu ra:
    - Trả về element nếu tồn tại
    - Trả về None nếu không tồn tại
- `wait_for_element_unobscured_by_xpath`: đợi element có hiển thị và không bị che bởi element khác, có thể click, input
  - Đầu vào:
    - xpath: chuỗi xpath cần đợi
    - timeout: thời gian đợi, default 120 giây
  - Đầu ra:
    - Trả về element nếu tồn tại
    - Trả về None nếu không tồn tại
- `wait_until_element_disappears_by_xpath`: đợi element ẩn hoặc không tồn tại trong DOM
  - Đầu vào:
    - xpath: chuỗi xpath cần đợi
    - timeout: thời gian đợi, default 120 giây
  - Đầu ra:
    - Trả về True nếu element đã biến mất
    - Trả về False nếu element vẫn tồn tại
- `wait_for_element_visibility_by_css`: đợi element tồn tại trong DOM, không check case bị che bởi các element khác
  - Đầu vào:
    - css_selector: chuỗi css_selector cần đợi
    - timeout: thời gian đợi, default 120 giây
  - Đầu ra:
    - Trả về element nếu tồn tại
    - Trả về None nếu không tồn tại
- `wait_for_element_enabled_by_css`: đợi element có thể click, áp dụng cho tagname là button
  - Đầu vào:
    - css_selector: chuỗi css_selector cần đợi
    - timeout: thời gian đợi, default 120 giây
  - Đầu ra:
    - Trả về element nếu tồn tại
    - Trả về None nếu không tồn tại
- `wait_for_element_unobscured_by_css`: đợi element có hiển thị và không bị che bởi element khác, có thể click, input
  - Đầu vào:
    - css_selector: chuỗi css_selector cần đợi
    - timeout: thời gian đợi, default 120 giây
  - Đầu ra:
    - Trả về element nếu tồn tại
    - Trả về None nếu không tồn tại
- `wait_until_element_disappears_by_css`: đợi element ẩn hoặc không tồn tại trong DOM
  - Đầu vào:
    - css_selector: chuỗi css_selector cần đợi
    - timeout: thời gian đợi, default 120 giây
  - Đầu ra:
    - Trả về True nếu element đã biến mất
    - Trả về False nếu element vẫn tồn tại
- `wait_loading`: đợi vòng loading ẩn đi rồi làm step tiếp
- `wait_process_bar_loading`: đợi thanh loading ẩn đi rồi làm step tiếp
- `wait_app_loading`: đợi các app hiển thị
- `wait_for_button_available`: đợi nút hiện và có thể click
  - Đầu vào:
    - button_name: tên nút cần đợi

## 4.3 Search function
- `simple_search`: common search ở các form có thể enter
  - Đầu vào: 
    - text: chuỗi cần tìm
    - placeholder: chuỗi placeholder, default 'Search text'
- `simple_search_f8`: common search chỉ ở trên form F8
  - Đầu vào: 
    - text: chuỗi cần tìm
- `advanced_search`: advanced search, write 'value' to 'title' in advanced search screen, flexible parameters for click_collap, field_type, in_group
  - Đầu vào:
    - title: tên field cần tìm
    - value: giá trị cần tìm tương ứng
    - click_collap: có click collap không, default là "N" (không click), Y (có click)
    - field_type: loại tag name của field, default là "I"
      - I: tagname is 'input'. Enter text, date or number to input field (default).
      - A: Textarea, multi-line text input.
      - S: Select, dropdown select field.
    - in_group: field có gom nhóm trong group không, default là "N" (Không trong group), "Y" (ở trong group)
- `click_button_search_advanced`: Click button search trong search advanced

## 4.4 Get text function
- `get_text_form_title`: get text của title
  - Đầu vào: không có
  - Đầu ra: Giá trị text của title
- `get_working_date`: get working date
  - Đầu vào: không có
  - Đầu ra: Giá trị working date DD/MM/YYYY
- `get_text_notification`: get text trong notification
  - Đầu vào: không có
  - Đầu ra:
    - Giá trị text trong thông báo
- `get_text_table_data`: get text trong bảng của BO
  - Đầu vào:
    - column_name: tên cột ở header
    - index: dòng, không tính dòng header
  - Đầu ra: Giá trị text trong ô chỉ định
- `get_status_table_data`: get text trong bảng của BO
  - Đầu vào:
    - column_name: tên cột ở header
    - index: dòng, không tính dòng header
  - Đầu ra: Giá trị text trong ô chỉ định
- `get_total_fee_table_data`: get total fee trong bảng fee của FO
  - Đầu ra: Giá total fee trong bảng fee của FO
- `get_text_table_data_posting`: get text trong bảng posting của FO
  - Đầu vào:
    - posting_side: posting side
    - column_name: tên cột ở header
    - index: dòng, không tính dòng header
  - Đầu ra: Giá trị text trong ô chỉ định
- `get_text_input_in_tab`: get text từ tagname input, loại hiển thị của field là input có mask trong màn hình có tab con
  - Ví dụ: "Account number" trong màn hình account information-view
  - Đầu vào: title của field
  - Đầu ra: Giá trị text của field
- `get_text_input_non_tab`: get text từ tagname input, loại hiển thị của field là input có mask trong màn hình KHÔNG có tab con
  - Ví dụ: "Customer code" trong màn hình giao dịch
  - Đầu vào: title của field
  - Đầu ra: Giá trị text của field
- `get_text_input_in_tab_group`: get text từ tagname input, loại hiển thị của field là input có mask trong màn hình có tab con và group chung một cột
  - Ví dụ: "Deposit tenor" trong màn hình account information-view
  - Đầu vào: title của field
  - Đầu ra: Giá trị text của field
- `get_text_input_non_tab_group`: get text từ tagname input, loại hiển thị của field là input có mask trong màn hình KHÔNG có tab con và group chung một cột
  - Ví dụ: "Account number" trong màn hình giao dịch
  - Đầu vào: title của field
  - Đầu ra: Giá trị text của field
- `get_text_select_in_tab`: get text từ tagname input, loại hiển thị của field là select trong màn hình có tab con
  - Ví dụ: "Currency" trong màn hình account information-view
  - Đầu vào: title của field
  - Đầu ra: Giá trị text của field
- `get_text_select_non_tab`: get text từ tagname input, loại hiển thị của field là select trong màn hình KHÔNG có tab con
  - Ví dụ: "Currency" trong màn hình giao dịch
  - Đầu vào: title của field
  - Đầu ra: Giá trị text của field
- `get_text_select_in_tab_group`: get text từ tagname input, loại hiển thị của field là select trong màn hình có tab con và group chung một cột
  - Ví dụ: "Interest tenor" và "Type of tenor" trong màn hình account information-view
  - Đầu vào:
    - title_front_select title của field phía trước field select
    - title_select title của field select
  - Đầu ra: Giá trị text của field select
- `get_text_select_non_tab_group`: get text từ tagname input, loại hiển thị của field là select trong màn hình KHÔNG có tab con và group chung một cột
  - Ví dụ: chưa hiện thực, vì chưa thấy dạng UI này
  - Đầu vào: 
    - title_front_select title của field phía trước field select
    - title_select title của field select
  - Đầu ra: Giá trị text của field select
- `get_text_textarea_in_tab`: get text từ tagname textarea, loại hiển thị của field là input KHÔNG có mask trong màn hình có tab con
  - Ví dụ: "Account name" trong màn hình account information-view
  - Đầu vào: title của field
  - Đầu ra: Giá trị text của field
- `get_text_textarea_non_tab`: get text từ tagname textarea, loại hiển thị của field là input KHÔNG có mask trong màn hình KHÔNG có tab con
  - Ví dụ: "Account name" trong màn hình giao dịch
  - Đầu vào: title của field
  - Đầu ra: Giá trị text của field
- `get_text`: get text từ title, flexible parameters for field_type, in_tab, in_group

## 4.5 Assert functions
- `assert_notification`: so sánh nội dung notification ở góc phải màn hình
  - Đầu vào: expected_message: nội dung thông báo mong đợi
- `assert_form_title`: so sánh title của form
  - Đầu vào: expected_title: nội dung title form mong đợi
- `assert_page_title`: so sánh title của page
  - Đầu vào: expected_title: nội dung title page mong đợi
- `assert_button_disable`: kiểm tra nút đã disable chưa
  - Đầu vào: button_name: tên nút cần check
- `assert_search_injection`: 
- `assert_search_not_found`: xác nhận tìm kiếm không thấy dữ liệu
- `assert_field_enable`: xác nhận trường có thể edit
- `assert_field_disable`: xác nhận trường không thể thống báo
- `assert_checkbox_enable`: xác nhận checkbox được phép check
- `assert_checkbox_disable`: xác nhận checkbox không được phép check
- assert_field_ui_enable: xác nhận trường có thể edit
- assert_field_ui_disable: xác nhận trường không thể thống báo
- `assert_button_disable`: xác nhận nút không thể click
- assert_field_label_require: xác nhận trường bắt buộc phải có giá trị
- assert_field_not_blank: xác nhận input không được phép để tróng
- assert_field_validation: xác nhận tồn tại lỗi
- assert_field_text:
- `assert_error_message`: xác nhận action xảy ra lỗi
- `assert_list_error_message`: xác nhận nội dung lỗi
- `assert_list_error_message_multi`: xác nhận nội dung lỗi cho trường hợp field là multi
- `assert_table_length`: xác nhận số row của table
- `assert_table_data`: xác nhận dữ liệu trong table đúng với giá trị mong đợi
  - Đầu vào: Tên cột trong bảng (column_name), dòng trong bảng (index), giá trị mong đợi (expected)
- `assert_status_table_data`: xác nhận dữ liệu trong table đúng với giá trị mong đợi
  - Đầu vào: Tên cột trong bảng (column_name), dòng trong bảng (index), giá trị mong đợi (expected)
- `assert_total_fee_table_data`: xác nhận dữ liệu trong table đúng với giá trị mong đợi
  - Đầu vào: Giá trị mong đợi (expected)
- `assert_table_data_posting`: xác nhận dữ liệu trong table posting đúng với giá trị mong đợi
  - Đầu vào: posting side (posting_side), tên cột trong bảng (column_name), dòng trong bảng (index), giá trị mong đợi (expected)
- `assert_search_results`: xác nhận số items trả về sau khi search
- `assert_field_signature`: xác nhận signature icon có tồn tại không
- `assert_form_title_header_popup`: xác nhận title trong header của popup
- `assert_form_title_popup`: xác nhận title trong content của popup
- `assert_fee_grid_exist`: xác nhận lưới fee có trong giao dịch
- `assert_fee_grid_not_exist`: xác nhận lưới fee không có trong giao dịch
- `assert_checked_in_tab`: xác nhận ô check-box đã được check trong screen có tab
- `assert_checked_non_tab`: xác nhận ô check-box đã được check trong screen single

## 4.6 Click functions
- `click_close_notification`: đóng thông báo
- `click_button`: click button
  - Đầu vào: button_name: tên nút cần click
- `click_menu`: click menu
  - Đầu vào:
    - level_01: bắt buộc
    - level_02: không bắt buộc, default None
    - level_03: không bắt buộc, default None
- `bo_click_tab`: click tab trong màn hình BO
  - Đầu vào: tab_name: tên tab cần click
- `click_table_menu`: chọn chức năng ( view, delete) ở mỗi hàng trên table
  - Đầu vào:
    - action: bắt buộc, action ('View', 'Delete')
    - row: bắt buộc, dòng cần action
- `close_all_form`: đóng tất cả các form
- `click_close_form`: đóng form theo index
  - Đầu vào: index: bắt buộc, default là 1
- `click_clear_search`: click clear search ở header
- `click_icon`: click icon
- `select_in_tab`: select value từ tagname input, loại hiển thị của field là select trong màn hình có tab con
  - Ví dụ: Currency trong màn hình account information-view
  - Đầu vào: 
    - title của field
    - value cần chọn
- `select_non_tab`: select value từ tagname input, loại hiển thị của field là select trong màn hình KHÔNG có tab con
  - Ví dụ: Currency trong màn hình giao dịch
  - Đầu vào: 
    - title của field
    - value cần chọn
- `click_collap_multi_in_tab`: chọn vào collap name, loại hiển thị của field là collap trong màn hình có tab con
- `click_collap_multi_non_tab`: chọn vào collap name, loại hiển thị của field là collap trong màn hình KHÔNG có tab con
- `click_input_non_tab`: click vào tagname input, loại hiển thị của field là input có mask trong màn hình KHÔNG có tab con
  - Ví dụ: "Customer code" trong màn hình giao dịch
  - Đầu vào: title của field

## 4.7 Input functions
- `write_text_input_in_tab`: ghi text từ tagname input, loại hiển thị của field là input có mask trong màn hình có tab con
  - Ví dụ: "Email address" trong màn hình customer profile-add
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_text_input_non_tab`: ghi text từ tagname input, loại hiển thị của field là input có mask trong màn hình KHÔNG có tab con
  - Ví dụ: "Customer code" trong màn hình giao dịch
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_text_input_in_tab_group`: ghi text từ tagname input, loại hiển thị của field là input có mask trong màn hình có tab con và group chung một cột
  - Ví dụ: "Deposit tenor" trong màn hình account information-view
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_text_input_non_tab_group`: ghi text từ tagname input, loại hiển thị của field là input có mask trong màn hình KHÔNG có tab con và group chung một cột
  - Ví dụ: "Account number" trong màn hình giao dịch
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_text_input_below_border`: ghi text từ tagname input, loại hiển thị của field là input trong màn hình gom nhóm theo border:
  - Ví dụ: "Amount" trong màn hình giao dịch
  - Đầu vào: 
    - border_name tên gom nhóm border
    - title của field
    - value cần ghi
    - clear_text
- `write_text_textarea_in_tab`: ghi text từ tagname textarea, loại hiển thị của field là input KHÔNG có mask trong màn hình có tab con
  - Ví dụ: "Home phone" trong màn hình customer profile-add
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_text_textarea_non_tab`: ghi text từ tagname textarea, loại hiển thị của field là input KHÔNG có mask trong màn hình KHÔNG có tab con
  - Ví dụ: "Account name" trong màn hình giao dịch
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_date_input_in_tab`: ghi text là date "DD/MM/YYYY" từ tagname input, loại hiển thị của field là date trong màn hình có tab con
  - Ví dụ: "Home phone" trong màn hình customer profile-add
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_date_input_non_tab`: ghi text là date "DD/MM/YYYY" từ tagname input, loại hiển thị của field là date trong màn hình KHÔNG có tab con
  - Ví dụ: "Account name" trong màn hình giao dịch
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_date_below_border`: ghi date từ tagname input, loại hiển thị của field là date trong màn hình gom nhóm theo border:
  - Đầu vào: 
    - border_name tên gom nhóm border
    - title của field
    - value cần ghi
- `write_text_textarea_multi_in_tab`: ghi text từ tagname textarea, loại hiển thị của field là input KHÔNG có mask trong collap multi field, trong màn hình có tab con
  - Ví dụ: "Name" trong màn hình customer profile-add
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_text_textarea_multi_non_tab`: ghi text từ tagname textarea, loại hiển thị của field là input KHÔNG có mask trong collap multi field, trong màn hình KHÔNG có tab con
  - Ví dụ: "Mobile phone" trong màn hình giao dịch
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_text_textarea_below_border`: ghi text từ tagname textarea, loại hiển thị của field là input trong màn hình gom nhóm theo border:
  - Ví dụ: "Account name" trong màn hình giao dịch
  - Đầu vào:
    - border_name tên gom nhóm border
    - title của field
    - value cần ghi
    - clear_text
- `write_text_input_multi_in_tab`: ghi text từ tagname input, loại hiển thị của field là input có mask trong collap multi field, trong màn hình có tab con
  - Ví dụ: "Account No" trong màn hình customer profile-add
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_text_input_multi_non_tab`: ghi text từ tagname input, loại hiển thị của field là input có mask trong collap multi field, trong màn hình KHÔNG có tab con
  - Ví dụ: 
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_decimal_input_non_tab`: ghi số có thập phân vào tagname input, loại hiển thị của field là input có mask số trong màn hình KHÔNG có tab con
  - Ví dụ: "Deposit amount" trong màn hình giao dịch
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_decimal_input_non_tab_group`: ghi số có thập phân vào tagname input, loại hiển thị của field là input có mask số trong màn hình KHÔNG có tab con và gom nhóm
  - Ví dụ: "Deposit amount" trong màn hình giao dịch
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_decimal_input_in_tab_group`: ghi số có thập phân vào tagname input, loại hiển thị của field là input có mask số trong màn hình có tab con và gom nhóm
  - Ví dụ: "Deposit amount" trong màn hình giao dịch
  - Đầu vào: 
    - title của field
    - value cần ghi
- `write_decimal_below_border`: ghi số có số thập phân vào tagname input, loại hiển thị của field là number trong màn hình gom nhóm theo border:
  - Đầu vào: 
    - border_name tên gom nhóm border
    - title của field
    - value cần ghi
- `write_text`: ghi value vào title, flexible parameters for field_type, in_tab, in_group

## 4.8 Clear functions
- `clear_text`: clear value khi nhận vào element có tagname là input
  - Ví dụ: search text trong search common
  - Đầu vào: element của tagname
- `check_disable`: check attribute class có chứa disable khi nhận vào element
  - Đầu vào: element cần check có attribute class có chứa disable không
  - Đầu ra: 
    - True: nếu có
    - False: nếu KHÔNG có

# V. Python knowledge

## 4.1 To handle a dynamic number of parameters in Python

### **1. Using `*args` for Positional Arguments:**

If you're not sure how many positional arguments you'll receive, you can use `*args`. This allows you to pass a variable number of arguments to a function.

#### Example:

```python
def dynamic_params(*args):
    for arg in args:
        print(arg)

# Call with different number of arguments
dynamic_params(1, 2, 3)
dynamic_params('apple', 'banana')
```

**Output:**
```
1
2
3
apple
banana
```

- `*args` collects all the positional arguments into a tuple, which you can then iterate over or access as needed.

### **2. Using `**kwargs` for Keyword Arguments:**

If you're not sure how many keyword arguments (name-value pairs) you'll receive, you can use `**kwargs`. This collects the keyword arguments into a dictionary.

#### Example:

```python
def dynamic_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call with different keyword arguments
dynamic_kwargs(name="John", age=25)
dynamic_kwargs(fruit="apple", color="red")
```

**Output:**
```
name: John
age: 25
fruit: apple
color: red
```

- `**kwargs` collects all the keyword arguments into a dictionary.

### **3. Combining `*args` and `**kwargs`:**

You can combine both `*args` and `**kwargs` to handle an unknown number of both positional and keyword arguments.

#### Example:

```python
def dynamic_args_kwargs(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)

    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call with both types of arguments
dynamic_args_kwargs(1, 2, 3, name="John", age=25)
```

**Output:**
```
Positional arguments:
1
2
3
Keyword arguments:
name: John
age: 25
```

### **4. Example with Selenium (Using Dynamic Parameters for Locators):**

If you're dynamically constructing an XPath or CSS selector based on the number of parameters:

```python
def construct_xpath(base_xpath, *conditions):
    xpath = base_xpath
    for condition in conditions:
        xpath += f"[{condition}]"
    return xpath

# Example use:
base_xpath = "//div"
conditions = ["contains(@class, 'example')", "not(@style='display: none;')"]

final_xpath = construct_xpath(base_xpath, *conditions)
print(final_xpath)
```

**Output:**
```
"//div[contains(@class, 'example')][not(@style='display: none;')]"
```

This approach allows flexibility in the number of conditions passed.

### Conclusion:

- Use `*args` for a variable number of positional arguments.
- Use `**kwargs` for a variable number of keyword arguments.
- Combine both to handle a variable number of both types of arguments.

Let me know if you need more details!