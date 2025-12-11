


# system_code_table
# Choose name: system_code_table_add
def system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
    # open form
    self.close_all_form()
    self.click_menu('System Code Table', 'Accounting System Code Table')
    self.wait_for_button_available('Add')
    self.click_button('Add')
    self.wait_for_button_available('Save')
    self.assert_form_title('ACT-System Code Table-Add')
    # enter value
    if code_id:
        self.bo_write_text_single('Code Id', code_id)
    if code_name:
        self.bo_write_text_single('Code Name', code_name)
    if caption_of_code:
        self.bo_write_text_single('Caption Of Code', caption_of_code)
    if english:
        self.bo_click_collap('Multi Caption Of Code')
        self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
    if vietnamese:
        self.bo_click_collap('Multi Caption Of Code')
        self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
    if laothian:
        self.bo_click_collap('Multi Caption Of Code')
        self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
    if khmer:
        self.bo_click_collap('Multi Caption Of Code')
        self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
    if myanmar:
        self.bo_click_collap('Multi Caption Of Code')
        self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
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
        code_id_out=self.bo_get_text_single('Code Id')
        print(f'Code Id: {code_id_out}')
        code_name_out=self.bo_get_text_single('Code Name')
        print(f'Code Name: {code_name_out}')
        code_of_group_out=self.bo_get_select_single('Code Of Group')
        print(f'Code Of Group: {code_of_group_out}')
        return code_id_outcode_name_outcode_of_group_out


def system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
    # open form
    self.bo_approval_view(
        transaction_number=transaction_number,
        form_title='ACT-System Code Table-Add'
    )
    # verify value
    if code_id:
        self.bo_assert_text_single('Code Id', code_id)
    if code_name:
        self.bo_assert_text_single('Code Name', code_name)
    if caption_of_code:
        self.bo_assert_text_single('Caption Of Code', caption_of_code)
    if english:
        self.bo_click_collap('Multi Caption Of Code')
        self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
    if vietnamese:
        self.bo_click_collap('Multi Caption Of Code')
        self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
    if laothian:
        self.bo_click_collap('Multi Caption Of Code')
        self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
    if khmer:
        self.bo_click_collap('Multi Caption Of Code')
        self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
    if myanmar:
        self.bo_click_collap('Multi Caption Of Code')
        self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
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

# TEST CASE: ADD SUCCESS
def test_000_system_code_table_add_success(self):
    print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    code_id_test = None
    code_name_test = None
    caption_of_code_test = None
    english_test = None
    vietnamese_test = None
    laothian_test = None
    khmer_test = None
    myanmar_test = None
    code_of_group_test = None
    code_index_test = None
    code_value_test = None
    field_link_test = None
    is_visible_test = None

    system_code_table_add_result = self.system_code_table_add(
        code_id=code_id_test,
        code_name=code_name_test,
        caption_of_code=caption_of_code_test,
        english=english_test,
        vietnamese=vietnamese_test,
        laothian=laothian_test,
        khmer=khmer_test,
        myanmar=myanmar_test,
        code_of_group=code_of_group_test,
        code_index=code_index_test,
        code_value=code_value_test,
        field_link=field_link_test,
        is_visible=is_visible_test,
    )
    code_id_out=system_code_table_add_result[0]
    code_name_out=system_code_table_add_result[1]
    code_of_group_out=system_code_table_add_result[2]

# TEST CASE: ADD ERROR
def test_000_system_code_table_add_error(self):
    print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    code_id_test = None
    code_name_test = None
    caption_of_code_test = None
    english_test = None
    vietnamese_test = None
    laothian_test = None
    khmer_test = None
    myanmar_test = None
    code_of_group_test = None
    code_index_test = None
    code_value_test = None
    field_link_test = None
    is_visible_test = None
    list_error_message = None

    system_code_table_add_result = self.system_code_table_add(
        code_id=code_id_test,
        code_name=code_name_test,
        caption_of_code=caption_of_code_test,
        english=english_test,
        vietnamese=vietnamese_test,
        laothian=laothian_test,
        khmer=khmer_test,
        myanmar=myanmar_test,
        code_of_group=code_of_group_test,
        code_index=code_index_test,
        code_value=code_value_test,
        field_link=field_link_test,
        is_visible=is_visible_test,
        list_error_message=list_error_message,
    )
