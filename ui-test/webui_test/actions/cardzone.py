from webui_test.case import *

class CardzoneActions(TestCase):

# -------------------------- handle BO - CARDZONE --------------------------
    # Terminal Management
    def terminal_management_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Cardzone', 'Terminal Management')
        self.wait_for_button_available('Search')
        self.assert_form_title('Terminal management-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def terminal_management_advanced_search(self, channel=None, terminal_id=None, branch=None, account_number_or_gl=None, terminal_address=None, intelligent_deposit=None, merchant_id=None, status=None):
        self.close_all_form()
        self.click_menu('Cardzone', 'Terminal Management')
        self.wait_for_button_available('Search')
        self.assert_form_title('Terminal management-Search')
        self.key_escape()
        if channel:
            self.adv_search_select('Channel', channel)
        if terminal_id:
            self.adv_search_text('Terminal ID', terminal_id)
        if branch:
            self.adv_search_text('Branch', branch)
        if account_number_or_gl:
            self.adv_search_text('Account number or GL', account_number_or_gl)
        if terminal_address:
            self.adv_search_text('Terminal address', terminal_address)
        self.key_escape()
        if intelligent_deposit:
            self.adv_search_select('Intelligent deposit', intelligent_deposit)
        if merchant_id:
            self.adv_search_text('Merchant ID', merchant_id)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def terminal_management_add(self, channel=None, terminal_id=None, branch=None, account_number_or_gl=None, terminal_address=None, intelligent_deposit=None, merchant_id=None, status=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Cardzone', 'Terminal Management')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('Terminal management-Add')
        # enter value
        self.key_escape()
        if channel:
            self.select('Channel', channel)
        if terminal_id:
            self.write_textarea('Terminal ID', terminal_id)
        self.key_escape()
        if branch:
            self.select('Branch', branch)
        if account_number_or_gl:
            self.write_textarea('Account number or GL', account_number_or_gl)
        if terminal_address:
            self.write_textarea('Terminal address', terminal_address)
        self.key_escape()
        if intelligent_deposit:
            self.select('Intelligent deposit', intelligent_deposit)
        if merchant_id:
            self.write_textarea('Merchant ID', merchant_id)
        self.key_escape()
        if status:
            self.select('Status', status)
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
            self.assert_notification('Saved successfully!')
            terminal_id_out=self.bo_get_text_data('Terminal ID')
            print(f"Terminal ID: '{terminal_id_out}'")
            return terminal_id_out

    def terminal_management_view(self, channel=None, terminal_id=None, branch=None, account_number_or_gl=None, terminal_address=None, intelligent_deposit=None, merchant_id=None, status=None):
        # search
        self.terminal_management_simple_search(terminal_id)
        self.assert_table_data('Terminal ID', 1, terminal_id)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('Terminal management-View')
        # verify value
        if channel:
            self.bo_assert_value_data('Channel', channel)
        if terminal_id:
            self.bo_assert_text_data('Terminal ID', terminal_id)
        if branch:
            self.bo_assert_value_data('Branch', branch)
        if account_number_or_gl:
            self.bo_assert_text_data('Account number or GL', account_number_or_gl)
        if terminal_address:
            self.bo_assert_text_data('Terminal address', terminal_address)
        if intelligent_deposit:
            self.bo_assert_value_data('Intelligent deposit', intelligent_deposit)
        if merchant_id:
            self.bo_assert_text_data('Merchant ID', merchant_id)
        if status:
            self.bo_assert_value_data('Status', status)

    def terminal_management_update(self, channel=None, terminal_id=None, branch=None, account_number_or_gl=None, terminal_address=None, intelligent_deposit=None, merchant_id=None, status=None, list_error_message=None):
        # view
        self.terminal_management_view(terminal_id=terminal_id)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.key_escape()
        if channel:
            self.select('Channel', channel)
        self.key_escape()
        if branch:
            self.select('Branch', branch)
        if account_number_or_gl:
            self.write_textarea('Account number or GL', account_number_or_gl)
        if terminal_address:
            self.write_textarea('Terminal address', terminal_address)
        self.key_escape()
        if intelligent_deposit:
            self.select('Intelligent deposit', intelligent_deposit)
        if merchant_id:
            self.write_textarea('Merchant ID', merchant_id)
        self.key_escape()
        if status:
            self.select('Status', status)
        # assert value
        if terminal_id:
            self.bo_assert_text_data('Terminal ID', terminal_id)
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
            self.assert_notification('Saved successfully!')
            terminal_id_out=self.bo_get_text_data('Terminal ID')
            print(f"Terminal ID: '{terminal_id_out}'")
            return terminal_id_out

    def terminal_management_delete(self, terminal_id, list_error_message=None, expected_message=None):
        # search
        self.terminal_management_simple_search(terminal_id)
        self.assert_table_data('Terminal ID', 1, terminal_id)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{terminal_id}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{terminal_id}'")
            return terminal_id

    # Merchant management
    def merchant_management_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Cardzone', 'Merchant Management')
        self.wait_for_button_available('Search')
        self.assert_form_title('Merchant management-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def merchant_management_advanced_search(self, merchant_id=None, merchant_account=None, branch=None, status=None):
        self.close_all_form()
        self.click_menu('Cardzone', 'Merchant Management')
        self.wait_for_button_available('Search')
        self.assert_form_title('Merchant management-Search')
        if merchant_id:
            self.adv_search_text('Merchant ID', merchant_id)
        if merchant_account:
            self.adv_search_text('Merchant account', merchant_account)
        if branch:
            self.adv_search_text('Branch', branch)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def merchant_management_add(self, merchant_id=None, merchant_account=None, branch=None, status=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Cardzone', 'Merchant Management')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('Merchant management-Add')
        # enter value
        if merchant_id:
            self.write_textarea('Merchant ID', merchant_id)
        if merchant_account:
            self.write_textarea('Merchant account', merchant_account)
        self.key_escape()
        if branch:
            self.select('Branch', branch)
        self.key_escape()
        if status:
            self.select('Status', status)
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
            self.assert_notification('Saved successfully!')
            merchant_id_out=self.bo_get_text_data('Merchant ID')
            print(f"Merchant ID: '{merchant_id_out}")
            return merchant_id_out

    def merchant_management_view(self, merchant_id=None, merchant_account=None, branch=None, status=None):
        # search
        self.merchant_management_simple_search(merchant_id)
        self.assert_table_data('Merchant ID', 1, merchant_id)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('Merchant management-View')
        # verify value
        if merchant_id:
            self.bo_assert_text_data('Merchant ID', merchant_id)
        if merchant_account:
            self.bo_assert_text_data('Merchant account', merchant_account)
        if branch:
            self.bo_assert_value_data('Branch', branch)
        if status:
            self.bo_assert_value_data('Status', status)

    def merchant_management_update(self, merchant_id=None, merchant_account=None, branch=None, status=None, list_error_message=None):
        # view
        self.merchant_management_view(merchant_id=merchant_id)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if merchant_account:
            self.write_textarea('Merchant account', merchant_account)
        self.key_escape()
        if branch:
            self.select('Branch', branch)
        self.key_escape()
        if status:
            self.select('Status', status)
        # assert value
        if merchant_id:
            self.bo_assert_text_data('Merchant ID', merchant_id)
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
            self.assert_notification('Saved successfully!')
            merchant_id_out=self.bo_get_text_data('Merchant ID')
            print(f'Merchant ID: {merchant_id_out}')
            return merchant_id_out

    def merchant_management_delete(self, merchant_id, list_error_message=None, expected_message=None):
        # search
        self.merchant_management_simple_search(merchant_id)
        self.assert_table_data('Merchant ID', 1, merchant_id)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{merchant_id}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{merchant_id}'")
            return merchant_id

    # Card Bin Management
    def card_bin_management_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Cardzone', 'Card Bin Management')
        self.wait_for_button_available('Search')
        self.assert_form_title('Card Bin Management-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def card_bin_management_advanced_search(self, institution_name=None, institution_id=None, bin_name=None, bin_value=None, bin_type=None):
        self.close_all_form()
        self.click_menu('Cardzone', 'Card Bin Management')
        self.wait_for_button_available('Search')
        self.assert_form_title('Card Bin Management-Search')
        if institution_name:
            self.adv_search_text('Institution Name', institution_name)
        if institution_id:
            self.adv_search_text('Institution ID', institution_id)
        if bin_name:
            self.adv_search_text('Bin Name', bin_name)
        if bin_value:
            self.adv_search_text('BIN', bin_value)
        if bin_type:
            self.adv_search_text('Type', bin_type)
        self.click_button_search_advanced()
        self.wait_loading()

    def card_bin_management_add(self, institution_name=None, institution_id=None, bin_name=None, bin_value=None, bin_type=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Cardzone', 'Card Bin Management')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('Card Bin Management-Add')
        # enter value
        if institution_name:
            self.bo_write_text_data('Institution Name', institution_name)
        if institution_id:
            self.bo_write_text_data('Institution ID', institution_id)
        if bin_name:
            self.bo_write_text_data('BIN Name', bin_name)
        if bin_value:
            self.bo_write_text_data('BIN', bin_value)
        if bin_type:
            self.bo_write_text_data('Type', bin_type)
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
            self.assert_notification('Saved successfully!')
            institution_id_out=self.bo_get_text_data('Institution ID')
            print(f"Institution ID: '{institution_id_out}'")
            return institution_id_out

    def card_bin_management_view(self, institution_name=None, institution_id=None, bin_name=None, bin_value=None, bin_type=None):
        # search
        self.card_bin_management_simple_search(institution_id)
        self.assert_table_data('Institution ID', 1, institution_id)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('Card Bin Management-View')
        # verify value
        if institution_name:
            self.bo_assert_text_data('Institution Name', institution_name)
        if institution_id:
            self.bo_assert_text_data('Institution ID', institution_id)
        if bin_name:
            self.bo_assert_text_data('BIN Name', bin_name)
        if bin_value:
            self.bo_assert_text_data('BIN', bin_value)
        if bin_type:
            self.bo_assert_text_data('Type', bin_type)

    def card_bin_management_update(self, institution_name=None, institution_id=None, bin_name=None, bin_value=None, bin_type=None, list_error_message=None):
        # view
        self.card_bin_management_view(institution_id=institution_id)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if institution_name:
            self.bo_write_text_data('Institution Name', institution_name)
        if bin_name:
            self.bo_write_text_data('BIN Name', bin_name)
        if bin_value:
            self.bo_write_text_data('BIN', bin_value)
        if bin_type:
            self.bo_write_text_data('Type', bin_type)
        # assert value
        if institution_id:
            self.bo_assert_text_data('Institution ID', institution_id)
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
            self.assert_notification('Saved successfully!')
            institution_id_out=self.bo_get_text_data('Institution ID')
            print(f"Institution ID: '{institution_id_out}'")
            return institution_id_out

    def card_bin_management_delete(self, institution_id, list_error_message=None, expected_message=None):
        # search
        self.card_bin_management_simple_search(institution_id)
        self.assert_table_data('Institution ID', 1, institution_id)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{institution_id}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{institution_id}'")
            return institution_id

# -------------------------- handle BO approval - CARDZONE --------------------------
    # Terminal Management - Data Verification
    def terminal_management_add_verify(self, transaction_number, channel=None, terminal_id=None, branch=None, account_number_or_gl=None, terminal_address=None, intelligent_deposit=None, merchant_id=None, status=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Terminal management-Add'
        )
        # verify value
        if channel:
            self.bo_assert_select_single('Channel', channel)
        if terminal_id:
            self.bo_assert_text_single('Terminal ID', terminal_id)
        if branch:
            self.bo_assert_select_single('Branch', branch)
        if account_number_or_gl:
            self.bo_assert_text_single('Account number or GL', account_number_or_gl)
        if terminal_address:
            self.bo_assert_text_single('Terminal address', terminal_address)
        if intelligent_deposit:
            self.bo_assert_select_single('Intelligent deposit', intelligent_deposit)
        if merchant_id:
            self.bo_assert_text_single('Merchant ID', merchant_id)
        if status:
            self.bo_assert_select_single('Status', status)

    def terminal_management_update_verify(self, transaction_number, channel=None, terminal_id=None, branch=None, account_number_or_gl=None, terminal_address=None, intelligent_deposit=None, merchant_id=None, status=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Terminal management-View'
        )
        # verify value
        if channel:
            self.bo_assert_select_single('Channel', channel)
        if terminal_id:
            self.bo_assert_text_single('Terminal ID', terminal_id)
        if branch:
            self.bo_assert_select_single('Branch', branch)
        if account_number_or_gl:
            self.bo_assert_text_single('Account number or GL', account_number_or_gl)
        if terminal_address:
            self.bo_assert_text_single('Terminal address', terminal_address)
        if intelligent_deposit:
            self.bo_assert_select_single('Intelligent deposit', intelligent_deposit)
        if merchant_id:
            self.bo_assert_text_single('Merchant ID', merchant_id)
        if status:
            self.bo_assert_select_single('Status', status)

    def terminal_management_search_verify(self, channel=None, terminal_id=None, branch=None, account_number_or_gl=None, terminal_address=None, intelligent_deposit=None, merchant_id=None, status=None):
        # search and verify
        self.terminal_management_simple_search(terminal_id)
        self.assert_table_data('Terminal ID', 1, terminal_id)
        if channel:
            self.assert_table_data('Channel', 1, channel)
        if branch:
            self.assert_table_data('Branch', 1, branch)
        if account_number_or_gl:
            self.assert_table_data('Account number or GL', 1, account_number_or_gl)
        if terminal_address:
            self.assert_table_data('Terminal address', 1, terminal_address)
        if intelligent_deposit:
            self.assert_table_data('Intelligent deposit', 1, intelligent_deposit)
        if merchant_id:
            self.assert_table_data('Merchant ID', 1, merchant_id)
        if status:
            self.assert_table_data('Status', 1, status)

    # Merchant management - Data Verification
    def merchant_management_add_verify(self, transaction_number, merchant_id=None, merchant_account=None, branch=None, status=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Merchant management-Add'
        )
        # verify value
        if merchant_id:
            self.bo_assert_text_single('Merchant ID', merchant_id)
        if merchant_account:
            self.bo_assert_text_single('Merchant account', merchant_account)
        if branch:
            self.bo_assert_select_single('Branch', branch)
        if status:
            self.bo_assert_select_single('Status', status)

    def merchant_management_update_verify(self, transaction_number, merchant_id=None, merchant_account=None, branch=None, status=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Merchant management-View'
        )
        # verify value
        if merchant_id:
            self.bo_assert_text_single('Merchant ID', merchant_id)
        if merchant_account:
            self.bo_assert_text_single('Merchant account', merchant_account)
        if branch:
            self.bo_assert_select_single('Branch', branch)
        if status:
            self.bo_assert_select_single('Status', status)

    def merchant_management_search_verify(self, merchant_id=None, merchant_account=None, branch=None, status=None):
        # search and verify
        self.merchant_management_simple_search(merchant_id)
        self.assert_table_data('Merchant ID', 1, merchant_id)
        if merchant_account:
            self.assert_table_data('Merchant account', 1, merchant_account)
        if branch:
            self.assert_table_data('Branch', 1, branch)
        if status:
            self.assert_table_data('Status', 1, status)

    # Card Bin Management - Data Verification
    def card_bin_management_add_verify(self, transaction_number, institution_name=None, institution_id=None, bin_name=None, bin_value=None, bin_type=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Card Bin Management-Add'
        )
        # verify value
        if institution_name:
            self.bo_assert_text_single('Institution Name', institution_name)
        if institution_id:
            self.bo_assert_text_single('Institution ID', institution_id)
        if bin_name:
            self.bo_assert_text_single('BIN Name', bin_name)
        if bin_value:
            self.bo_assert_text_single('BIN', bin_value)
        if bin_type:
            self.bo_assert_text_single('Type', bin_type)

    def card_bin_management_update_verify(self, transaction_number, institution_name=None, institution_id=None, bin_name=None, bin_value=None, bin_type=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Card Bin Management-View'
        )
        # verify value
        if institution_name:
            self.bo_assert_text_single('Institution Name', institution_name)
        if institution_id:
            self.bo_assert_text_single('Institution ID', institution_id)
        if bin_name:
            self.bo_assert_text_single('BIN Name', bin_name)
        if bin_value:
            self.bo_assert_text_single('BIN', bin_value)
        if bin_type:
            self.bo_assert_text_single('Type', bin_type)

    def card_bin_management_search_verify(self, institution_name=None, institution_id=None, bin_name=None, bin_value=None, bin_type=None):
        # search and verify
        self.card_bin_management_simple_search(institution_id)
        self.assert_table_data('Institution ID', 1, institution_id)
        if institution_name:
            self.assert_table_data('Institution Name', 1, institution_name)
        if bin_name:
            self.assert_table_data('BIN Name', 1, bin_name)
        if bin_value:
            self.assert_table_data('BIN', 1, bin_value)
        if bin_type:
            self.assert_table_data('Type', 1, bin_type)

