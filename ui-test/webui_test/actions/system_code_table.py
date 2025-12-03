from webui_test.case import *

class SystemCodeTableActions(TestCase):

# -------------------------- handle BO - SYSTEM CODE TABLE --------------------------
    # ACT-System Code Table
    def accounting_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Accounting System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def accounting_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Accounting System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def accounting_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Accounting System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ACT-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def accounting_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.accounting_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ACT-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def accounting_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.accounting_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def accounting_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.accounting_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # ADM-System Code Table
    def admin_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Admin System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def admin_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Admin System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('ADM-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def admin_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Admin System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ADM-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def admin_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.admin_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ADM-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def admin_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.admin_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def admin_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.admin_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # BCH-System Code Table
    def batch_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Batch System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('BCH-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def batch_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Batch System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('BCH-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def batch_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Batch System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('BCH-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def batch_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.batch_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('BCH-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def batch_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.batch_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def batch_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.batch_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # CAR-System Code Table
    def card_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Card System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('CAR-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def card_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Card System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('CAR-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def card_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Card System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CAR-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def card_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.card_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CAR-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def card_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.card_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def card_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.card_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # CSH-System Code Table
    def cash_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Cash System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('CSH-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def cash_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Cash System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('CSH-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def cash_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Cash System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CSH-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def cash_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.cash_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CSH-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def cash_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.cash_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def cash_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.cash_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # CRD-System Code Table
    def credit_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Credit System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def credit_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Credit System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def credit_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Credit System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CRD-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def credit_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.credit_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def credit_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.credit_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def credit_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.credit_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # CTM-System Code Table
    def customer_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Customer System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def customer_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Customer System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('CTM-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def customer_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Customer System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CTM-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def customer_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.customer_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CTM-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def customer_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.customer_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def customer_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.customer_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # DPT-System Code Table
    def deposit_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Deposit System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def deposit_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Deposit System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def deposit_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Deposit System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('DPT-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def deposit_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.deposit_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('DPT-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def deposit_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.deposit_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def deposit_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.deposit_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # FX-System Code Table
    def fx_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'FX System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('FX-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def fx_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'FX System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('FX-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def fx_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'FX System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('FX-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def fx_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.fx_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('FX-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def fx_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.fx_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def fx_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.fx_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # FAC-System Code Table
    def fixed_asset_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Fixed Asset System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('FAC-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def fixed_asset_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Fixed Asset System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('FAC-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def fixed_asset_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Fixed Asset System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('FAC-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def fixed_asset_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.fixed_asset_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('FAC-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def fixed_asset_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.fixed_asset_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def fixed_asset_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.fixed_asset_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # MTG-System Code Table
    def mortgage_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Mortgage System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('MTG-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def mortgage_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Mortgage System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('MTG-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def mortgage_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Mortgage System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('MTG-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def mortgage_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.mortgage_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('MTG-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def mortgage_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.mortgage_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def mortgage_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.mortgage_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # PMT-System Code Table
    def payment_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Payment System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def payment_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Payment System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def payment_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Payment System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('PMT-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def payment_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.payment_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('PMT-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def payment_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.payment_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def payment_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.payment_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # TRS-System Code Table
    def treasury_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Treasury System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def treasury_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Treasury System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def treasury_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Treasury System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('TRS-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def treasury_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.treasury_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRS-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def treasury_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.treasury_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def treasury_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.treasury_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # VCH-System Code Table
    def voucher_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Voucher System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('VCH-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def voucher_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Voucher System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('VCH-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def voucher_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Voucher System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('VCH-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def voucher_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.voucher_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('VCH-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def voucher_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.voucher_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def voucher_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.voucher_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # TRD-System Code Table
    def trade_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'Trade Finance System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def trade_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, index=None, index_form=None, index_to=None, field_link=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'Trade Finance System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def trade_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'Trade Finance System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('TRD-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
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
            return code_id_out, code_name_out, code_of_group_out

    def trade_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # search
        self.trade_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-System Code Table-View')
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def trade_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, list_error_message=None):
        # view
        self.trade_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def trade_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.trade_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

    # CMS-System Code Table
    def cms_system_code_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('System Code Table', 'CMS System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('CMS-System Code Table-Search')
        self.wait_loading()
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def cms_system_code_table_advanced_search(self, code_id=None, code_name=None, caption_of_code=None, code_of_group=None, index=None, index_form=None, index_to=None, field_link=None, application_code=None):
        self.close_all_form()
        self.click_menu('System Code Table', 'CMS System Code Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('CMS-System Code Table-Search')
        self.wait_loading()
        collap_name='Advanced Search'
        if code_id:
            self.adv_search_text('Code Id', code_id, collap_name=collap_name)
        if code_name:
            self.adv_search_text('Code Name', code_name, collap_name=collap_name)
        if caption_of_code:
            self.adv_search_text('Caption Of Code', caption_of_code, collap_name=collap_name)
        self.key_escape()
        if code_of_group:
            self.adv_search_select('Code Of Group', code_of_group)
        if index:
            self.adv_search('Index', index, collap_name=collap_name)
        if index_form:
            self.adv_search_group('Index Form', index_form, collap_name=collap_name)
        if index_to:
            self.adv_search_group('Index To', index_to, collap_name=collap_name)
        if field_link:
            self.adv_search_text('Field Link', field_link, collap_name=collap_name)
        self.key_escape()
        if application_code:
            self.adv_search_select('Application Code', application_code)
        self.click_button_search_advanced()
        self.wait_loading()

    def cms_system_code_table_add(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('System Code Table', 'CMS System Code Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CMS-System Code Table-Add')
        # enter value
        if code_id:
            self.bo_write_text_data('Code Id', code_id)
        if code_name:
            self.bo_write_text_data('Code Name', code_name)
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        self.key_escape()
        if code_of_group:
            self.bo_select_data('Code Of Group', code_of_group)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        self.key_escape()
        if application_code:
            self.select_table('Application Code', application_code)
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
            return code_id_out, code_name_out, code_of_group_out

    def cms_system_code_table_view(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None):
        # search
        self.cms_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
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
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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
        if application_code:
            self.bo_assert_select_single('Application Code', application_code)

    def cms_system_code_table_update(self, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None, list_error_message=None):
        # view
        self.cms_system_code_table_view(code_id=code_id, code_name=code_name)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if caption_of_code:
            self.bo_write_text_data('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_write_text_multi_single('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_index:
            self.bo_write_number_single('Code Index', code_index)
        if code_value:
            self.bo_write_text_data('Code Value', code_value)
        if field_link:
            self.bo_write_text_data('Field Link', field_link)
        if is_visible is False:
            self.bo_click_uncheckbox_single('Is Visible?')
        if is_visible is True:
            self.bo_click_checkbox_single('Is Visible?')
        self.key_escape()
        if application_code:
            self.select_table('Application Code', application_code)
        # assert value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
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
            code_id_out=self.bo_get_text_single('Code Id')
            print(f'Code Id: {code_id_out}')
            code_name_out=self.bo_get_text_single('Code Name')
            print(f'Code Name: {code_name_out}')
            code_of_group_out=self.bo_get_select_single('Code Of Group')
            print(f'Code Of Group: {code_of_group_out}')
            return code_id_out, code_name_out, code_of_group_out

    def cms_system_code_table_delete(self, code_id=None, code_name=None, list_error_message=None, expected_message=None):
        # search
        self.cms_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{code_id}' and '{code_name}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{code_id}' and '{code_name}'")
            return code_id, code_name

# -------------------------- handle BO approval - SYSTEM CODE TABLE --------------------------
    # ACT-System Code Table - Data Verification
    def accounting_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
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
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def accounting_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ACT-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def accounting_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.accounting_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # ADM-System Code Table - Data Verification
    def admin_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def admin_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def admin_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.admin_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # BCH-System Code Table - Data Verification
    def batch_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='BCH-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def batch_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='BCH-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def batch_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.batch_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # CAR-System Code Table - Data Verification
    def card_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CAR-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def card_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CAR-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def card_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.card_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # CSH-System Code Table - Data Verification
    def cash_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CSH-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def cash_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CSH-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def cash_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.cash_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # CRD-System Code Table - Data Verification
    def credit_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def credit_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def credit_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.credit_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # CTM-System Code Table - Data Verification
    def customer_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CTM-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def customer_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CTM-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def customer_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.customer_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # DPT-System Code Table - Data Verification
    def deposit_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def deposit_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def deposit_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.deposit_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # FX-System Code Table - Data Verification
    def fx_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FX-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def fx_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FX-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def fx_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.fx_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # FAC-System Code Table - Data Verification
    def fixed_asset_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FAC-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def fixed_asset_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FAC-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def fixed_asset_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.fixed_asset_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # MTG-System Code Table - Data Verification
    def mortgage_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='MTG-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def mortgage_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='MTG-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def mortgage_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.mortgage_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # PMT-System Code Table - Data Verification
    def payment_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def payment_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def payment_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.payment_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # TRS-System Code Table - Data Verification
    def treasury_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def treasury_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def treasury_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.treasury_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # VCH-System Code Table - Data Verification
    def voucher_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='VCH-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def voucher_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='VCH-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def voucher_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.voucher_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # TRD-System Code Table - Data Verification
    def trade_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def trade_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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

    def trade_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.trade_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # CMS-System Code Table - Data Verification
    def cms_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None):
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
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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
        if application_code:
            self.bo_assert_select_single('Application Code', application_code)

    def cms_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None):
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
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
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
        if application_code:
            self.bo_assert_select_single('Application Code', application_code)

    def cms_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None, application_code=None):
        # search and verify
        self.cms_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)
        if application_code:
            self.assert_table_data('Application Code', 1, application_code)

