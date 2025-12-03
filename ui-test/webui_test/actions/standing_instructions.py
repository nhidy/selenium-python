from webui_test.case import *

class StandingInstructionsActions(TestCase):

# -------------------------- handle FO - STANDING INSTRUCTIONS --------------------------
    # EMS_SICLS: Close standing instructions
    def ems_sicls(self, standing_instructions_code=None, description=None, fee_collect_method=None, account_number_for_fee=None, standing_instructions_name=None, standing_instructions_status=None, currency_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('EMS_SICLS', 'Close standing instructions')
        self.wait_for_button_available('Reload Auto Fee')
        self.click_button('Reload Auto Fee')
        self.wait_loading()
        self.wait_for_button_available('Accept')
        self.assert_form_title('Close standing instructions')
        # enter value
        if standing_instructions_code:
            self.fo_write_text('Standing instructions code', standing_instructions_code)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', str(account_number_for_fee).replace('-', ''))
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.click_button('Reload Auto Fee')
        if standing_instructions_name:
            self.fo_assert_text('Standing instructions name', standing_instructions_name)
        if standing_instructions_status:
            self.fo_assert_select('Standing instructions status', standing_instructions_status)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references EMS_SICLS: {transaction_references}')
            standing_instructions_code_out=self.fo_get_text('Standing instructions code')
            print(f'Standing instructions code: {standing_instructions_code_out}')
            return transaction_references, standing_instructions_code_out

    def ems_sicls_view(self, transaction_references, standing_instructions_code=None, description=None, fee_collect_method=None, account_number_for_fee=None, standing_instructions_name=None, standing_instructions_status=None, currency_code=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Close standing instructions')
        # compare value
        if standing_instructions_code:
            self.fo_assert_text('Standing instructions code', standing_instructions_code)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', account_number_for_fee)
        if standing_instructions_name:
            self.fo_assert_text('Standing instructions name', standing_instructions_name)
        if standing_instructions_status:
            self.fo_assert_select('Standing instructions status', standing_instructions_status)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references EMS_SICLS: {transaction_references}')
        standing_instructions_code_out=self.fo_get_text('Standing instructions code')
        print(f'F8: Standing instructions code: {standing_instructions_code_out}')
        return transaction_references, standing_instructions_code_out

# -------------------------- handle BO - STANDING INSTRUCTIONS --------------------------
    # Standing Instructions
    def standing_instructions_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'Standing Instructions')
        self.wait_for_button_available('Search')
        self.assert_form_title('Standing Instructions-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def standing_instructions_advanced_search(self, standing_instructions_code=None, standing_instructions_name=None, status=None, customer_code=None, run_mode=None, retries=None, failure_limit=None, frequency_condition=None, start_date=None, end_date=None, execute_condition=None, standing_instructions_description=None, frequency_type=None):
        self.close_all_form()
        self.click_menu('Deposit', 'Standing Instructions')
        self.wait_for_button_available('Search')
        self.assert_form_title('Standing Instructions-Search')
        if standing_instructions_code:
            self.adv_search_text('Standing instructions code', standing_instructions_code)
        if standing_instructions_name:
            self.adv_search_text('Standing instructions name', standing_instructions_name)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        if customer_code:
            self.adv_search('Customer code', str(customer_code).replace('-', ''))
        self.key_escape()
        if run_mode:
            self.adv_search_select('Run mode', run_mode)
        if retries:
            self.adv_search('Retries', retries)
        if failure_limit:
            self.adv_search('Failure limit', failure_limit)
        if frequency_condition:
            self.adv_search_text('Frequency condition', frequency_condition)
        if start_date:
            self.adv_search('Start date', start_date)
        if end_date:
            self.adv_search('End date', end_date)
        if execute_condition:
            self.adv_search_text('Execute condition', execute_condition)
        if standing_instructions_description:
            self.adv_search_text('Standing instructions description', standing_instructions_description)
        self.key_escape()
        if frequency_type:
            self.adv_search_select('Frequency type', frequency_type)
        self.click_button_search_advanced()
        self.wait_loading()

