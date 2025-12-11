


# system_code_table
# Choose name: system_code_table_add
def system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None, list_error_message=None):
    # open form
    self.close_all_form()
    self.click_menu('System Code Table', ' System Code Table')
    self.wait_for_button_available('Add')
    self.click_button('Add')
    self.wait_for_button_available('Save')
    self.assert_form_title('CMS-System Code Table-Add')
    # enter value
    if code_id:
        self.bo_write_text_single('Code Id', code_id)
    if code_name:
        self.bo_write_text_single('Code Name', code_name)
    if caption_of_code:
        self.bo_write_text_single('Caption Of Code', caption_of_code)
    self.key_escape()
    if code_of_group:
        self.bo_select_single('Code Of Group', code_of_group)
    if code_index:
        self.bo_write_number_single('Code Index', code_index)
    if code_value:
        self.bo_write_text_single('Code Value', code_value)
    if field_link:
        self.bo_write_text_single('Field Link', field_link)
    if is_visible is False:
    if is_visible:
        self.bo_click_checkbox_single('Is Visible?')
    self.key_escape()
    if application_code:
        self.bo_select_single('Application Code', application_code)
    # assert value
    self.wait_loading()
    # click 'Save'
    self.click_button('Save')
    if list_error_message:
    # verify error
        self.assert_error_message()
        self.assert_list_error_message(list_error_message)
        print('Action add failed!')
    else:
    # verify success
        self.assert_button_disable('Save')
        self.check_notification('Saved successfully!')
        return 


def system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None):
    # open form
    self.bo_approval_view(
        transaction_number=transaction_number,
        form_title='CMS-System Code Table-Add'
    )
    # verify value
    if code_id:
        self.bo_assert_text_single('Code Id', code_id)
    if code_name:
        self.bo_assert_text_single('Code Name', code_name)
    if caption_of_code:
        self.bo_assert_text_single('Caption Of Code', caption_of_code)
    if code_of_group:
        self.bo_assert_select_single('Code Of Group', code_of_group)
    if code_index:
        self.bo_assert_value_single('Code Index', code_index)
    if code_value:
        self.bo_assert_text_single('Code Value', code_value)
    if field_link:
        self.bo_assert_text_single('Field Link', field_link)
    if is_visible is not None:
        self.bo_assert_checkbox('Is Visible?', is_visible)
    if application_code:
        self.bo_assert_select_single('Application Code', application_code)

# TEST CASE: ADD SUCCESS
def test_000_system_code_table_add_success(self):
    print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    code_id_test = None
    code_name_test = None
    caption_of_code_test = None
    code_of_group_test = None
    code_index_test = None
    code_value_test = None
    field_link_test = None
    is_visible_test = None
    application_code_test = None

    system_code_table_add_result = self.system_code_table_add(
        code_id=code_id_test,
        code_name=code_name_test,
        caption_of_code=caption_of_code_test,
        code_of_group=code_of_group_test,
        code_index=code_index_test,
        code_value=code_value_test,
        field_link=field_link_test,
        is_visible=is_visible_test,
        application_code=application_code_test,
    )

# TEST CASE: ADD ERROR
def test_000_system_code_table_add_error(self):
    print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    code_id_test = None
    code_name_test = None
    caption_of_code_test = None
    code_of_group_test = None
    code_index_test = None
    code_value_test = None
    field_link_test = None
    is_visible_test = None
    application_code_test = None
    list_error_message = None

    system_code_table_add_result = self.system_code_table_add(
        code_id=code_id_test,
        code_name=code_name_test,
        caption_of_code=caption_of_code_test,
        code_of_group=code_of_group_test,
        code_index=code_index_test,
        code_value=code_value_test,
        field_link=field_link_test,
        is_visible=is_visible_test,
        application_code=application_code_test,
        list_error_message=list_error_message,
    )
