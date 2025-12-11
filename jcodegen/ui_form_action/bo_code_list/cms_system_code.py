


# system_code_table
# Choose name: system_code_table_view
def system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None):
    # search
    self.system_code_table_simple_search(str().replace('-', ''))
    self.assert_table_data('', 1, )
    # view
    self.click_table_menu('View', 1)
    self.wait_for_button_available('Modify')
    self.assert_form_title('CMS-System Code Table-View')
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

def system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None, list_error_message=None):
    # view
    self.system_code_table_view(A=A)
    self.click_button('Modify')
    self.wait_loading()
    # update value
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
        print('Action update failed!')
    else:
    # verify success
        self.assert_button_disable('Save')
        self.check_notification('Saved successfully!')
        return 


def system_code_table_delete(self, param_name, list_error_message=None, expected_message=None):
    # search
    self.system_code_table_simple_search(str(param_name).replace('-', ''))
    self.assert_table_data('', 1, param_name)
    # delete
    self.click_table_menu('Delete', 1)
    self.wait_loading()
    self.click_button_in_popup('Yes')
    if list_error_message:
    # verify error
        self.assert_error_message()
        self.assert_list_error_message(list_error_message)
        print(f"Action delete '{param_name}' failed!")
    else:
    # verify success
        if expected_message:
            self.assert_notification(expected_message)
        print(f'Deleted: {param_name}')
        return param_name



def system_code_table_view_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None):
    # open form
    self.bo_approval_view(
        transaction_number=transaction_number,
        form_title='CMS-System Code Table-View'
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



# TEST CASE: VIEW SUCCESS
def test_000_system_code_table_view_success(self):
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

    system_code_table_view_result = self.system_code_table_view(
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

# TEST CASE: UPDATE SUCCESS
def test_000_system_code_table_update_success(self):
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

    system_code_table_update_result = self.system_code_table_update(
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

# TEST CASE: UPDATE ERROR
def test_000_system_code_table_update_error(self):
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

    system_code_table_update_result = self.system_code_table_update(
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

# TEST CASE: DELETE SUCCESS
def test_000_system_code_table_delete_success(self):
    print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    system_code_table_delete_result = self.system_code_table_delete(
    
    )

# TEST CASE: DELETE ERROR
def test_000_system_code_table_delete_error(self):
    print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    list_error_message = None

    system_code_table_delete_result = self.system_code_table_delete(
        
        list_error_message=list_error_message,
    )
