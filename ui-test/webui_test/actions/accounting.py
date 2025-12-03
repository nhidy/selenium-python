from webui_test.case import *

class AccountingActions(TestCase):

# -------------------------- handle FO - ACCOUNTING --------------------------
    # ACT_FEE: 1186: Fee collection by cash
    def act_fee(self, fee_currency=None, customer_name=None, amount_for_fee_calculation=None, description=None, total_fee_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('ACT_FEE', '1186')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1186: Fee collection by cash')
        # enter value
        self.key_escape()
        if fee_currency:
            self.fo_select('Fee currency', fee_currency)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
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
            print(f'Transaction references ACT_FEE: {transaction_references}')
            return transaction_references

    def act_fee_view(self, transaction_references, fee_currency=None, customer_name=None, amount_for_fee_calculation=None, description=None, total_fee_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '1186: Fee collection by cash')
        # compare value
        if fee_currency:
            self.fo_assert_select('Fee currency', fee_currency)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if amount_for_fee_calculation:
            self.fo_assert_value('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references ACT_FEE: {transaction_references}')
        return transaction_references

    # ACT_GFEE: ACT-1187: Miscellaneous Fee Collection
    def act_gfee(self, gl_account_number=None, customer_name=None, amount_for_fee_calculation=None, description=None, currency=None, total_fee_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('ACT_GFEE', '1187')
        self.wait_for_button_available('Accept')
        self.assert_form_title('ACT-1187: Miscellaneous Fee Collection')
        # enter value
        if gl_account_number:
            self.fo_write_group('GL account number', str(gl_account_number).replace('-', ''))
            self.wait_loading()
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if currency:
            self.fo_assert_select('Currency', currency)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
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
            print(f'Transaction references ACT_GFEE: {transaction_references}')
            gl_account_number_out=self.fo_get_value_group('GL account number')
            print(f'GL account number: {gl_account_number_out}')
            return transaction_references, gl_account_number_out

    def act_gfee_view(self, transaction_references, gl_account_number=None, customer_name=None, amount_for_fee_calculation=None, description=None, currency=None, total_fee_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'ACT-1187: Miscellaneous Fee Collection')
        # compare value
        if gl_account_number:
            self.fo_assert_value_group('GL account number', self.gl_account_number_mask(gl_account_number))
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if amount_for_fee_calculation:
            self.fo_assert_value('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if currency:
            self.fo_assert_select('Currency', currency)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references ACT_GFEE: {transaction_references}')
        gl_account_number_out=self.fo_get_value_group('GL account number')
        print(f'F8: GL account number: {gl_account_number_out}')
        return transaction_references, gl_account_number_out

    # ACT_NGL: Create GL level 9 for new branch
    def act_ngl(self, branch=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('ACT_NGL', 'Create GL')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Create GL level 9 for new branch')
        # enter value
        self.key_escape()
        if branch:
            self.fo_select('Branch', branch)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
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
            print(f'Transaction references ACT_NGL: {transaction_references}')
            branch_out=self.fo_get_select('Branch')
            print(f'Branch: {branch_out}')
            return transaction_references, branch_out

    def act_ngl_view(self, transaction_references, branch=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Create GL level 9 for new branch')
        # compare value
        if branch:
            self.fo_assert_select('Branch', branch)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references ACT_NGL: {transaction_references}')
        branch_out=self.fo_get_select('Branch')
        print(f'F8: Branch: {branch_out}')
        return transaction_references, branch_out

# -------------------------- handle FO - FX TRANSACTION --------------------------
    def act_act(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.fo_write_border('Credit', 'Account number', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', self.no_mask(customer_code))
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references ACT_ACT: {transaction_references}')
            return transaction_references

    def act_act_lookup(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.lookup_data_value(
                border_name='Debit',
                title='Account number',
                value_search_code=account_number_debit_value,
                value_code=account_number_debit_value,
            )
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.lookup_data_value(
                border_name='Credit',
                title='Account number',
                value_search_code=account_number_credit_value,
                value_code=account_number_credit_value,
            )
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                border_name='Customer Information',
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value,
            )
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references ACT_ACT: {transaction_references}')
            return transaction_references

    def act_act_view(self, transaction_references, accounting_type_debit=None, accounting_type_credit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_assert_value_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            self.fo_assert_value_border('Debit', 'Account number', self.gl_account_number_mask(account_number_debit))
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_assert_value_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        if accounting_type_credit:
            self.fo_assert_value_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            self.fo_assert_value_border('Credit', 'Account number', self.gl_account_number_mask(account_number_credit))
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_assert_value_border('Credit', 'Type', type_credit)
        if market_dr_rate:
            self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
        if cross_rate:
            self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
        if market_cr_rate:
            self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
        if debit_amount:
            self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
        if reverse_rate:
            self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if fee_amount:
            self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
        if receive_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        if customer_type:
            self.fo_assert_value_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_border('Customer Information', 'Customer code', self.customer_code_mask(customer_code))
        if full_name:
            self.fo_assert_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_assert_value_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_assert_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_assert_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_assert_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_assert_value_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_assert_text_border('Customer Information', 'Section Name', section_name)
        if ifc_codes:
            self.assert_fees(ifc_codes, values, total_fee)
        return transaction_references

    def act_dpt(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.fo_write_border('Credit', 'Account numer', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', self.no_mask(customer_code))
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references ACT_DPT: {transaction_references}')
            return transaction_references

    def act_dpt_lookup(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.lookup_data_value(
                border_name='Debit',
                title='Account number',
                value_search_code=account_number_debit_value,
                value_code=account_number_debit_value,
            )
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.lookup_data_text(
                border_name='Credit',
                title='Account numer',
                value_search_code=account_number_credit_value,
                value_code=account_number_credit_value,
            )
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                border_name='Customer Information',
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value,
            )
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references ACT_DPT: {transaction_references}')
            return transaction_references

    def act_dpt_view(self, transaction_references, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_assert_value_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            self.fo_assert_value_border('Debit', 'Account number', self.gl_account_number_mask(account_number_debit))
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_assert_value_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        if accounting_type_credit:
            self.fo_assert_value_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            self.fo_assert_value_border('Credit', 'Account numer', self.deposit_account_number_mask(account_number_credit))
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_assert_value_border('Credit', 'Type', type_credit)
        if market_dr_rate:
            self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
        if cross_rate:
            self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
        if market_cr_rate:
            self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
        if debit_amount:
            self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
        if reverse_rate:
            self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if fee_amount:
            self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
        if receive_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        if customer_type:
            self.fo_assert_value_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_border('Customer Information', 'Customer code', self.customer_code_mask(customer_code))
        if full_name:
            self.fo_assert_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_assert_value_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_assert_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_assert_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_assert_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_assert_value_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_assert_text_border('Customer Information', 'Section Name', section_name)
        if ifc_codes:
            self.assert_fees(ifc_codes, values, total_fee)
        return transaction_references

    def act_csh(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_write_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_select_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', self.no_mask(customer_code))
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references ACT_CSH: {transaction_references}')
            return transaction_references

    def act_csh_lookup(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.lookup_data_value(
                border_name='Debit',
                title='Account number',
                value_search_code=account_number_debit_value,
                value_code=account_number_debit_value,
            )
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_write_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_select_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                border_name='Customer Information',
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value,
            )
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references ACT_CSH: {transaction_references}')
            return transaction_references

    def act_csh_view(self, transaction_references, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Accounting'
        if accounting_type_debit:
            self.fo_assert_value_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            self.fo_assert_value_border('Debit', 'Account number', self.gl_account_number_mask(account_number_debit))
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_assert_value_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        if accounting_type_credit:
            self.fo_assert_value_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_assert_value_border('Credit', 'Type', type_credit)
        if market_dr_rate:
            self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
        if cross_rate:
            self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
        if market_cr_rate:
            self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
        if debit_amount:
            self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
        if reverse_rate:
            self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if fee_amount:
            self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
        if receive_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        if customer_type:
            self.fo_assert_value_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_border('Customer Information', 'Customer code', self.customer_code_mask(customer_code))
        if full_name:
            self.fo_assert_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_assert_value_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_assert_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_assert_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_assert_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_assert_value_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_assert_text_border('Customer Information', 'Section Name', section_name)
        if ifc_codes:
            self.assert_fees(ifc_codes, values, total_fee)
        return transaction_references

    def csh_csh(self, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_write_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_select_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_write_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', self.no_mask(customer_code))
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references CSH_CSH: {transaction_references}')
            return transaction_references

    def csh_csh_lookup(self, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_write_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_select_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_write_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                border_name='Customer Information',
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value,
            )
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references CSH_CSH: {transaction_references}')
            return transaction_references

    def csh_csh_view(self, transaction_references, accounting_type_debit=None, accounting_type_credit=None, account_name_debit=None, currency_debit=None, type_debit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_assert_value_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_assert_value_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        if accounting_type_credit:
            self.fo_assert_value_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_assert_value_border('Credit', 'Type', type_credit)
        if market_dr_rate:
            self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
        if cross_rate:
            self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
        if market_cr_rate:
            self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
        if debit_amount:
            self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
        if reverse_rate:
            self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if fee_amount:
            self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
        if receive_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        if customer_type:
            self.fo_assert_value_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_border('Customer Information', 'Customer code', self.customer_code_mask(customer_code))
        if full_name:
            self.fo_assert_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_assert_value_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_assert_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_assert_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_assert_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_assert_value_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_assert_text_border('Customer Information', 'Section Name', section_name)
        if ifc_codes:
            self.assert_fees(ifc_codes, values, total_fee)
        return transaction_references

    def csh_act(self, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_write_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_select_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.fo_write_border('Credit', 'Account number', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', self.no_mask(customer_code))
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references CSH_ACT: {transaction_references}')
            return transaction_references

    def csh_act_lookup(self, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_write_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_select_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.lookup_data_value(
                border_name='Credit',
                title='Account number',
                value_search_code=account_number_credit_value,
                value_code=account_number_credit_value,
            )
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                border_name='Customer Information',
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value,
            )
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references CSH_ACT: {transaction_references}')
            return transaction_references

    def csh_act_view(self, transaction_references, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_assert_value_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_assert_value_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        if accounting_type_credit:
            self.fo_assert_value_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            self.fo_assert_value_border('Credit', 'Account number', self.gl_account_number_mask(account_number_credit))
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_assert_value_border('Credit', 'Type', type_credit)
        if market_dr_rate:
            self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
        if cross_rate:
            self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
        if market_cr_rate:
            self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
        if debit_amount:
            self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
        if reverse_rate:
            self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if fee_amount:
            self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
        if receive_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        if customer_type:
            self.fo_assert_value_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_border('Customer Information', 'Customer code', self.customer_code_mask(customer_code))
        if full_name:
            self.fo_assert_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_assert_value_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_assert_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_assert_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_assert_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_assert_value_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_assert_text_border('Customer Information', 'Section Name', section_name)
        if ifc_codes:
            self.assert_fees(ifc_codes, values, total_fee)
        return transaction_references

    def csh_dpt(self, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_write_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_select_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.fo_write_border('Credit', 'Account numer', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', self.no_mask(customer_code))
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references CSH_DPT: {transaction_references}')
            return transaction_references

    def csh_dpt_lookup(self, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_write_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_select_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.lookup_data_text(
                border_name='Credit',
                title='Account numer',
                value_search_code=account_number_credit_value,
                value_code=account_number_credit_value,
            )
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                border_name='Customer Information',
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value,
            )
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references CSH_DPT: {transaction_references}')
            return transaction_references

    def csh_dpt_view(self, transaction_references, accounting_type_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Cash'
        if accounting_type_debit:
            self.fo_assert_value_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_assert_value_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        if accounting_type_credit:
            self.fo_assert_value_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            self.fo_assert_value_border('Credit', 'Account numer', self.deposit_account_number_mask(account_number_credit))
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_assert_value_border('Credit', 'Type', type_credit)
        if market_dr_rate:
            self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
        if cross_rate:
            self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
        if market_cr_rate:
            self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
        if debit_amount:
            self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
        if reverse_rate:
            self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if fee_amount:
            self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
        if receive_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        if customer_type:
            self.fo_assert_value_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_border('Customer Information', 'Customer code', self.customer_code_mask(customer_code))
        if full_name:
            self.fo_assert_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_assert_value_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_assert_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_assert_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_assert_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_assert_value_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_assert_text_border('Customer Information', 'Section Name', section_name)
        if ifc_codes:
            self.assert_fees(ifc_codes, values, total_fee)
        return transaction_references

    def dpt_dpt(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        self.key_escape()
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        self.key_escape()
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        self.key_escape()
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.fo_write_border('Credit', 'Account numer', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        self.key_escape()
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        self.key_escape()
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', self.no_mask(customer_code))
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        self.key_escape()
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        self.key_escape()
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references DPT_DPT: {transaction_references}')
            return transaction_references

    def dpt_dpt_lookup(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        self.key_escape()
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.lookup_data_text(
                border_name='Debit',
                title='Account number',
                value_search_code=account_number_debit_value,
                value_code=account_number_debit_value,
            )
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        self.key_escape()
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        self.key_escape()
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.lookup_data_text(
                border_name='Credit',
                title='Account numer',
                value_search_code=account_number_credit_value,
                value_code=account_number_credit_value,
            )
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        self.key_escape()
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        self.key_escape()
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                border_name='Customer Information',
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value,
            )
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        self.key_escape()
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        self.key_escape()
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references DPT_DPT: {transaction_references}')
            return transaction_references

    def dpt_dpt_view(self, transaction_references, accounting_type_debit=None, accounting_type_credit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        if accounting_type_debit:
            self.fo_assert_value_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            self.fo_assert_value_border('Debit', 'Account number', self.deposit_account_number_mask(account_number_debit))
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_assert_value_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Deposit'
        if accounting_type_credit:
            self.fo_assert_value_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            self.fo_assert_value_border('Credit', 'Account numer', self.deposit_account_number_mask(account_number_credit))
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_assert_value_border('Credit', 'Type', type_credit)
        if market_dr_rate:
            self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
        if cross_rate:
            self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
        if market_cr_rate:
            self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
        if debit_amount:
            self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
        if reverse_rate:
            self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if fee_amount:
            self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
        if receive_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        if customer_type:
            self.fo_assert_value_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_border('Customer Information', 'Customer code', self.customer_code_mask(customer_code))
        if full_name:
            self.fo_assert_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_assert_value_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_assert_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_assert_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_assert_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_assert_value_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_assert_text_border('Customer Information', 'Section Name', section_name)
        if ifc_codes:
            self.assert_fees(ifc_codes, values, total_fee)
        return transaction_references

    def dpt_act(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        self.key_escape()
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        self.key_escape()
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        self.key_escape()
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.fo_write_border('Credit', 'Account number', account_number_credit_value)
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        self.key_escape()
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        self.key_escape()
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', self.no_mask(customer_code))
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        self.key_escape()
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        self.key_escape()
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references DPT_ACT: {transaction_references}')
            return transaction_references

    def dpt_act_lookup(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        self.key_escape()
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.lookup_data_text(
                border_name='Debit',
                title='Account number',
                value_search_code=account_number_debit_value,
                value_code=account_number_debit_value,
            )
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        self.key_escape()
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        self.key_escape()
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            account_number_credit_value = self.no_mask(account_number_credit)
            self.lookup_data_value(
                border_name='Credit',
                title='Account number',
                value_search_code=account_number_credit_value,
                value_code=account_number_credit_value,
            )
            self.wait_loading()
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        self.key_escape()
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        self.key_escape()
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                border_name='Customer Information',
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value,
            )
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        self.key_escape()
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        self.key_escape()
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references DPT_ACT: {transaction_references}')
            return transaction_references

    def dpt_act_view(self, transaction_references, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_number_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        if accounting_type_debit:
            self.fo_assert_value_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            self.fo_assert_value_border('Debit', 'Account number', self.deposit_account_number_mask(account_number_debit))
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_assert_value_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Accounting'
        if accounting_type_credit:
            self.fo_assert_value_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_number_credit:
            self.fo_assert_value_border('Credit', 'Account number', self.gl_account_number_mask(account_number_credit))
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_assert_value_border('Credit', 'Type', type_credit)
        if market_dr_rate:
            self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
        if cross_rate:
            self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
        if market_cr_rate:
            self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
        if debit_amount:
            self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
        if reverse_rate:
            self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if fee_amount:
            self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
        if receive_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        if customer_type:
            self.fo_assert_value_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_border('Customer Information', 'Customer code', self.customer_code_mask(customer_code))
        if full_name:
            self.fo_assert_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_assert_value_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_assert_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_assert_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_assert_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_assert_value_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_assert_text_border('Customer Information', 'Section Name', section_name)
        if ifc_codes:
            self.assert_fees(ifc_codes, values, total_fee)
        return transaction_references

    def dpt_csh(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        self.key_escape()
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.fo_write_border('Debit', 'Account number', account_number_debit_value)
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        self.key_escape()
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        self.key_escape()
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_write_text_border('Credit', 'Account name credit', account_name_credit)
        self.key_escape()
        if currency_credit:
            self.fo_select_border('Credit', 'Currency', currency_credit)
        self.key_escape()
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        self.key_escape()
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_write_border('Customer Information', 'Customer code', self.no_mask(customer_code))
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        self.key_escape()
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        self.key_escape()
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references DPT_CSH: {transaction_references}')
            return transaction_references

    def dpt_csh_lookup(self, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, enter_side=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.click_menu('Front Office', 'FX Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FOF-FX Transaction')
        # enter value
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        self.key_escape()
        if accounting_type_debit:
            self.fo_select_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            account_number_debit_value = self.no_mask(account_number_debit)
            self.lookup_data_text(
                border_name='Debit',
                title='Account number',
                value_search_code=account_number_debit_value,
                value_code=account_number_debit_value,
            )
            self.wait_loading()
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        self.key_escape()
        if type_debit:
            self.fo_select_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        self.key_escape()
        if accounting_type_credit:
            self.fo_select_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_write_text_border('Credit', 'Account name credit', account_name_credit)
        self.key_escape()
        if currency_credit:
            self.fo_select_border('Credit', 'Currency', currency_credit)
        self.key_escape()
        if type_credit:
            self.fo_select_border('Credit', 'Type', type_credit)
        self.key_escape()
        if customer_type:
            self.fo_select_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                border_name='Customer Information',
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value,
            )
        if full_name:
            self.fo_write_text_border('Customer Information', 'Full name', full_name)
        self.key_escape()
        if paper_type:
            self.fo_select_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_write_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_write_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_write_text_border('Customer Information', 'Address', address)
        self.key_escape()
        if nationality:
            self.fo_select_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_write_text_border('Customer Information', 'Section Name', section_name)
        if enter_side=='D':
            if debit_amount:
                self.fo_write_number_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if enter_side=='C':
            if credit_amount:
                self.fo_write_number_border('Rate', 'Credit Amount', credit_amount)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', credit_amount)
        self.fo_assert_value_border('Rate', 'Fee Amount', '0.00')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
            self.wait_loading()
            if market_dr_rate:
                self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
            if cross_rate:
                self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
            if market_cr_rate:
                self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
            if debit_amount:
                self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
            if reverse_rate:
                self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
            if credit_amount:
                self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
            if fee_amount:
                self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
            if receive_amount:
                self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
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
            print(f'Transaction references DPT_CSH: {transaction_references}')
            return transaction_references

    def dpt_csh_view(self, transaction_references, accounting_type_debit=None, account_number_debit=None, account_name_debit=None, currency_debit=None, type_debit=None, accounting_type_credit=None, account_name_credit=None, currency_credit=None, type_credit=None, market_dr_rate=None, cross_rate=None, market_cr_rate=None, debit_amount=None, reverse_rate=None, credit_amount=None, fee_amount=None, receive_amount=None, customer_type=None, customer_code=None, full_name=None, paper_type=None, paper_number=None, telephone=None, address=None, nationality=None, description=None, section_name=None, ifc_codes=None, values=None, total_fee=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FOF-FX Transaction')
        # compare value
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        if accounting_type_debit is None or accounting_type_debit == '':
            accounting_type_debit = 'Deposit'
        if accounting_type_debit:
            self.fo_assert_value_border('Debit', 'Accounting Type', accounting_type_debit)
        if account_number_debit:
            self.fo_assert_value_border('Debit', 'Account number', self.deposit_account_number_mask(account_number_debit))
        if account_name_debit:
            self.fo_assert_text_border('Debit', 'Account name debit', account_name_debit)
        if currency_debit:
            self.fo_assert_value_border('Debit', 'Currency', currency_debit)
        if type_debit:
            self.fo_assert_value_border('Debit', 'Type', type_debit)
        if accounting_type_credit is None or accounting_type_credit == '':
            accounting_type_credit = 'Cash'
        if accounting_type_credit:
            self.fo_assert_value_border('Credit', 'Accounting Type', accounting_type_credit)
        if account_name_credit:
            self.fo_assert_text_border('Credit', 'Account name credit', account_name_credit)
        if currency_credit:
            self.fo_assert_value_border('Credit', 'Currency', currency_credit)
        if type_credit:
            self.fo_assert_value_border('Credit', 'Type', type_credit)
        if market_dr_rate:
            self.fo_assert_value_border('Rate', 'Market DR Rate', market_dr_rate)
        if cross_rate:
            self.fo_assert_value_border('Rate', 'Cross Rate', cross_rate)
        if market_cr_rate:
            self.fo_assert_value_border('Rate', 'Market CR Rate', market_cr_rate)
        if debit_amount:
            self.fo_assert_value_border('Rate', 'Debit Amount', debit_amount)
        if reverse_rate:
            self.fo_assert_value_border('Rate', 'Reverse Rate', reverse_rate)
        if credit_amount:
            self.fo_assert_value_border('Rate', 'Credit Amount', credit_amount)
        if fee_amount:
            self.fo_assert_value_border('Rate', 'Fee Amount', fee_amount)
        if receive_amount:
            self.fo_assert_value_border('Rate', 'Receive Amount', receive_amount)
        if customer_type:
            self.fo_assert_value_border('Customer Information', 'Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_border('Customer Information', 'Customer code', self.customer_code_mask(customer_code))
        if full_name:
            self.fo_assert_text_border('Customer Information', 'Full name', full_name)
        if paper_type:
            self.fo_assert_value_border('Customer Information', 'Paper type', paper_type)
        if paper_number:
            self.fo_assert_text_border('Customer Information', 'Paper number', paper_number)
        if telephone:
            self.fo_assert_text_border('Customer Information', 'Telephone', telephone)
        if address:
            self.fo_assert_text_border('Customer Information', 'Address', address)
        if nationality:
            self.fo_assert_value_border('Customer Information', 'Nationality', nationality)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text_border('Customer Information', 'Description', description)
        if section_name:
            self.fo_assert_text_border('Customer Information', 'Section Name', section_name)
        if ifc_codes:
            self.assert_fees(ifc_codes, values, total_fee)
        return transaction_references

# -------------------------- handle FO - INTERNAL TRANSACTION --------------------------
    # ACT_MAN: ACT-Internal Transaction
    def act_man(self, posting_types=None, gl_accounts=None, currencies=None, debit_amounts=None, credit_amounts=None, descs=None, section_names=None, total_credit_amount=None, value_date=None, reference_document_no=None, customer_id=None, customer_account_id=None, user_defined_4=None, user_defined_5=None, description=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None, list_error_message_under_group=None):
        # open form
        self.close_all_form()
        self.click_menu('Accounting', 'Internal Transaction')
        self.wait_for_button_available('Accept')
        self.assert_form_title('ACT-Internal Transaction')
        # enter value
        if gl_accounts:
            self.add_gl_entries(posting_types=posting_types, gl_accounts=gl_accounts, currencies=currencies, debit_amounts=debit_amounts, credit_amounts=credit_amounts, descs=descs, section_names=section_names, total_credit_amount=total_credit_amount, list_error_message_under_group=list_error_message_under_group)
        if value_date:
            self.fo_write_date('Value date', value_date)
        if reference_document_no:
            self.fo_write_text('Reference document no.', reference_document_no)
        if customer_id:
            self.fo_write_text('Customer ID', customer_id)
        if customer_account_id:
            self.fo_write_text('Customer Account ID', customer_account_id)
        if user_defined_4:
            self.fo_write_text('User defined 4', user_defined_4)
        if user_defined_5:
            self.fo_write_text('User defined 5', user_defined_5)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.write_description_act_man(description)
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
            self.assert_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references ACT_MAN: {transaction_references}')
            return transaction_references

    def act_man_view(self, transaction_references, posting_types=None, gl_accounts=None, currencies=None, debit_amounts=None, credit_amounts=None, descs=None, section_names=None, total_credit_amount=None, value_date=None, reference_document_no=None, customer_id=None, customer_account_id=None, user_defined_4=None, user_defined_5=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'ACT-Internal Transaction')
        # compare value
        if currencies:
            for gl_account, currency in zip(gl_accounts, currencies):
                self.fo_assert_text_table('Account number', self.gl_account_number_mask(gl_account), 'Currency', currency)
        if debit_amounts:
            for gl_account, debit_amount in zip(gl_accounts, debit_amounts):
                if debit_amount is None:
                    debit_amount = '0.00'
                self.fo_assert_text_table('Account number', self.gl_account_number_mask(gl_account), 'Debit', debit_amount)
        if credit_amounts:
            for gl_account, credit_amount in zip(gl_accounts, credit_amounts):
                if credit_amount is None:
                    credit_amount = '0.00'
                self.fo_assert_text_table('Account number', self.gl_account_number_mask(gl_account), 'Credit', credit_amount)
        if descs:
            for gl_account, desc in zip(gl_accounts, descs):
                if desc is None:
                    desc = ' '
                self.fo_assert_text_table('Account number', self.gl_account_number_mask(gl_account), 'Description', desc)
        if section_names:
            for gl_account, section_name in zip(gl_accounts, section_names):
                self.fo_assert_text_table('Account number', self.gl_account_number_mask(gl_account), 'Section Name', section_name)
        if posting_types:
            for gl_account, posting_type in zip(gl_accounts, posting_types):
                if posting_type == 'Debit':
                    posting_type = 'D'
                if posting_type == 'Credit':
                    posting_type = 'C'
                self.fo_assert_text_table('Account number', self.gl_account_number_mask(gl_account), 'D/C', posting_type, xpath_type='preceding')
        if total_credit_amount:
            self.assert_total_fee_table_data(total_credit_amount)
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if reference_document_no:
            self.fo_assert_text('Reference document no.', reference_document_no)
        if customer_id:
            self.fo_assert_text('Customer ID', customer_id)
        if customer_account_id:
            self.fo_assert_text('Customer Account ID', customer_account_id)
        if user_defined_4:
            self.fo_assert_text('User defined 4', user_defined_4)
        if user_defined_5:
            self.fo_assert_text('User defined 5', user_defined_5)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.assert_description_act_man(description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references ACT_MAN: {transaction_references}')
        return transaction_references

# -------------------------- handle BO - ACCOUNTING --------------------------
    # ACT-Bank Account Definition
    def accounting_bank_account_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Accounting', 'Bank Account Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-Bank Account Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def accounting_bank_account_definition_advanced_search(self, account_number=None, account_level_from=None, account_level_to=None, currency=None, account_name=None, classification=None, balance_side=None, group=None):
        self.close_all_form()
        self.click_menu('Accounting', 'Bank Account Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-Bank Account Definition-Search')
        if account_number:
            self.adv_search_text('Account number', str(account_number).replace('-', ''))
        if account_level_from:
            self.adv_search_group('Account level from', account_level_from)
        if account_level_to:
            self.adv_search_group('Account level to', account_level_to)
        if currency:
            self.adv_search_text('Currency', currency)
        if account_name:
            self.adv_search_text('Account name', account_name)
        self.key_escape()
        if classification:
            self.adv_search_select('Classification', classification)
        self.key_escape()
        if balance_side:
            self.adv_search_select('Balance side', balance_side)
        self.key_escape()
        if group:
            self.adv_search_select('Group', group)
        self.click_button_search_advanced()
        self.wait_loading()

    def accounting_bank_account_definition_add(self, account_level, currency_code, account_number, account_name, short_account_name, direct_posting, is_inactive, branch_code, laos_name=None, thai_name=None, khmer_name=None, vietnamese_name=None, account_classification=None, reverse_balance=None, balance_side=None, posting_side=None, account_group=None, account_categories=None, job_process_option=None):
        # Check if the GL account number exists; if not, break the loop
        account_number = str(account_number).replace('-', '')
        if self.check_gl_account_not_exist(account_number):
            print('Account number does not exist')
            # open form
            self.close_all_form()
            self.click_menu('Accounting', 'Bank Account Definition')
            self.wait_for_button_available('Add')
            self.assert_form_title('ACT-Bank Account Definition-Search')
            self.click_button('Add')
            self.wait_for_button_available('Save')
            self.assert_form_title('ACT-Bank Account Definition-Add')
            # enter value
            if account_level:
                self.bo_select_single('Account level', account_level)
            if currency_code:
                self.bo_select_single('Currency code', currency_code)
            if account_number:
                self.bo_set_text('Account number', account_number)
            if account_name:
                self.bo_set_text('Account name', account_name)
            if short_account_name:
                self.bo_set_text('Short account name', short_account_name)
            if laos_name is not None or thai_name is not None or khmer_name is not None or vietnamese_name is not None:
                collap_name = 'Other name'
                self.bo_click_collap_single(collap_name)
                if laos_name:
                    self.bo_write_text_multi_single(collap_name, 'Laos name', laos_name)
                if thai_name:
                    self.bo_write_text_multi_single(collap_name, 'Thai name', thai_name)
                if khmer_name:
                    self.bo_write_text_multi_single(collap_name, 'Khmer name', khmer_name)
                if vietnamese_name:
                    self.bo_write_text_multi_single(collap_name, 'Vietnamese name', vietnamese_name)
            if account_classification:
                self.bo_select_single('Account classification', account_classification)
            if reverse_balance:
                self.bo_select_single('Reverse balance', reverse_balance)
            if balance_side:
                self.bo_select_single('Balance side', balance_side)
            if posting_side:
                self.bo_select_single('Posting side', posting_side)
            if account_group:
                self.bo_select_single('Account group', account_group)
            if account_categories:
                self.bo_select_single('Account categories', account_categories)
            if direct_posting:
                self.bo_select_single('Direct posting', direct_posting)
            if is_inactive:
                self.bo_select_single('Is Inactive', is_inactive)
            if job_process_option:
                self.bo_select_single('Job process option', job_process_option)
            if branch_code:
                self.assertEqual(str(self.bo_get_select_single('Branch Code')).split(' - ')[0], branch_code)
            self.click_button('Save')
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            account_number = self.bo_get_text_data('Account number')
            # search and verify
            self.accounting_bank_account_definition_simple_search(account_number)
            if account_level:
                self.assert_table_data('Account level', 1, str(account_level).split('-')[0])
            if account_number:
                self.assert_table_data('Account number', 1, account_number)
            if currency_code:
                self.assert_table_data('Currency', 1, currency_code)
            if account_name:
                self.assert_table_data('Account name', 1, account_name)
            if account_classification:
                self.assert_table_data('Classification', 1, account_classification)
            if balance_side:
                self.assert_table_data('Balance side', 1, balance_side)
            if account_group:
                self.assert_table_data('Group', 1, account_group)
        else:
            print('Account number already exists')
        print('Account number: ' + account_number)
        return account_number

    def accounting_bank_account_definition_view(self, account_number, account_level=None, currency_code=None, account_name=None, short_account_name=None, laos_name=None, thai_name=None, khmer_name=None, vietnamese_name=None, account_classification=None, reverse_balance=None, balance_side=None, posting_side=None, account_group=None, account_categories=None, direct_posting=None, is_inactive=None, job_process_option=None, branch_code=None):
        account_number = str(account_number).replace('-', '')
        # search GL account
        self.accounting_bank_account_definition_simple_search(account_number)
        if account_number:
            self.assert_table_data('Account number', 1, account_number)
        # view GL account
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ACT-Bank Account Definition-View')
        # verify value tab 'General'
        if account_level:
            self.bo_assert_select('Account level', account_level)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if account_number:
            self.bo_assert_text('Account number', account_number)
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if short_account_name:
            self.bo_assert_text('Short account name', short_account_name)
        if laos_name is not None or thai_name is not None or khmer_name is not None or vietnamese_name is not None:
            collap_name = 'Other name'
            self.bo_click_collap(collap_name)
            if laos_name:
                self.bo_assert_text_multi(collap_name, 'Laos name', laos_name)
            if thai_name:
                self.bo_assert_text_multi(collap_name, 'Thai name', thai_name)
            if khmer_name:
                self.bo_assert_text_multi(collap_name, 'Khmer name', khmer_name)
            if vietnamese_name:
                self.bo_assert_text_multi(collap_name, 'Vietnamese name', vietnamese_name)
        if account_classification:
            self.bo_assert_select('Account classification', account_classification)
        if reverse_balance:
            self.bo_assert_select('Reverse balance', reverse_balance)
        if balance_side:
            self.bo_assert_select('Balance side', balance_side)
        if posting_side:
            self.bo_assert_select('Posting side', posting_side)
        if account_group:
            self.bo_assert_select('Account group', account_group)
        if account_categories:
            self.bo_assert_select('Account categories', account_categories)
        if direct_posting:
            self.bo_assert_select('Direct posting', direct_posting)
        if is_inactive:
            self.bo_assert_select('Is Inactive', is_inactive)
        if job_process_option:
            self.bo_assert_select('Job process option', job_process_option)
        if branch_code:
            self.assertEqual(str(self.bo_get_select('Branch Code')).split(' - ')[0], branch_code)
        print('View account number: ' + account_number)
        return account_number

    def accounting_bank_account_definition_update(self, account_number, account_level=None, currency_code=None, account_name=None, short_account_name=None, laos_name=None, thai_name=None, khmer_name=None, vietnamese_name=None, account_classification=None, reverse_balance=None, balance_side=None, posting_side=None, account_group=None, account_categories=None, direct_posting=None, is_inactive=None, job_process_option=None, branch_code=None):
        self.accounting_bank_account_definition_view(account_number)
        self.wait_loading()
        self.click_button('Modify')
        # update value tab 'General'
        if account_name:
            self.bo_write_text('Account name', account_name)
        if short_account_name:
            self.bo_write_text('Short account name', short_account_name)
        if laos_name is not None or thai_name is not None or khmer_name is not None or vietnamese_name is not None:
            collap_name = 'Other name'
            self.bo_click_collap(collap_name)
            if laos_name:
                self.bo_write_text_multi(collap_name, 'Laos name', laos_name)
            if thai_name:
                self.bo_write_text_multi(collap_name, 'Thai name', thai_name)
            if khmer_name:
                self.bo_write_text_multi(collap_name, 'Khmer name', khmer_name)
            if vietnamese_name:
                self.bo_write_text_multi(collap_name, 'Vietnamese name', vietnamese_name)
        if account_classification:
            self.bo_select('Account classification', account_classification)
        if reverse_balance:
            self.bo_select('Reverse balance', reverse_balance)
        if balance_side:
            self.bo_select('Balance side', balance_side)
        if posting_side:
            self.bo_select('Posting side', posting_side)
        if account_group:
            self.bo_select('Account group', account_group)
        if account_categories:
            self.bo_select('Account categories', account_categories)
        if direct_posting:
            self.bo_select('Direct posting', direct_posting)
        if is_inactive:
            self.bo_select('Is Inactive', is_inactive)
        if job_process_option:
            self.bo_select('Job process option', job_process_option)
        # click 'Save'
        self.click_button('Save')
        self.assert_button_disable('Save')
        self.check_notification('Saved successfully!')
        account_number = self.bo_get_text_data('Account number')
        # search and verify
        self.accounting_bank_account_definition_view(
            account_number=account_number,
            account_level=account_level,
            currency_code=currency_code,
            account_name=account_name,
            short_account_name=short_account_name,
            laos_name=laos_name,
            thai_name=thai_name,
            khmer_name=khmer_name,
            vietnamese_name=vietnamese_name,
            account_classification=account_classification,
            reverse_balance=reverse_balance,
            balance_side=balance_side,
            posting_side=posting_side,
            account_group=account_group,
            account_categories=account_categories,
            direct_posting=direct_posting,
            is_inactive=is_inactive,
            job_process_option=job_process_option,
            branch_code=branch_code
        )
        print('Updated account number: ' + account_number)
        return account_number

    def accounting_bank_account_definition_delete(self, account_number):
        account_number = str(account_number).replace('-', '')
        # search GL account
        self.accounting_bank_account_definition_simple_search(account_number)
        if account_number:
            self.assert_table_data('Account number', 1, account_number)
        # delete GL account
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        self.check_notification('Deleted successfully')
        # search and verify
        self.accounting_bank_account_definition_simple_search(account_number)
        self.assert_search_not_found()
        print('Account number: ' + account_number)
        return account_number

    def check_gl_account_not_exist(self, account_number):
        account_number = str(account_number).replace('-', '')
        # search GL account
        self.accounting_bank_account_definition_simple_search(account_number)
        if (self.get_text_notification(timeout=3) == 'Data not found'):
            return True
        else:
            return False

    def add_gl_level_9_use_for_testing(self, branch_code, currency_code, account_number):
        """
        If the account number already exists, do not add it.
        """
        account_name = f'GL Test ({currency_code})'
        self.accounting_bank_account_definition_add(
            account_level='9-Ninth level of system chart (Details account)',
            currency_code=currency_code,
            account_number=account_number,
            account_name=account_name,
            short_account_name=account_name,
            direct_posting='Yes',
            is_inactive='No',
            branch_code=branch_code
        )

    # ACT-Common Account Definition
    def common_account_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Accounting', 'Accounting Setup', 'Common Account Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-Common Account Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def common_account_definition_advanced_search(self, account_name=None, account_number=None, references_account_number=None, references_account_number_2=None):
        self.close_all_form()
        self.click_menu('Accounting', 'Accounting Setup', 'Common Account Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-Common Account Definition-Search')
        if account_name:
            self.adv_search_text('Account name', account_name)
        if account_number:
            self.adv_search_text('Account number', account_number)
        if references_account_number:
            self.adv_search_text('References account number', references_account_number)
        if references_account_number_2:
            self.adv_search_text('References account number 2', references_account_number_2)
        self.click_button_search_advanced()
        self.wait_loading()

    def common_account_definition_add(self, account_number=None, account_name=None, references_account_number=None, references_account_number_2=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Accounting', 'Accounting Setup', 'Common Account Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ACT-Common Account Definition-Add')
        # enter value
        if account_number:
            self.bo_write_text_single('Account number', account_number)
        if account_name:
            self.bo_write_text_single('Account name', account_name)
        if references_account_number:
            self.bo_write_text_single('References account number', references_account_number)
        if references_account_number_2:
            self.bo_write_text_single('References account number 2', references_account_number_2)
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
            account_number_out=self.bo_get_text_single('Account number')
            print(f'Account number: {account_number_out}')
            account_name_out=self.bo_get_text_single('Account name')
            print(f'Account name: {account_name_out}')
            return account_number_out, account_name_out

    def common_account_definition_view(self, account_number=None, account_name=None, references_account_number=None, references_account_number_2=None):
        # search
        self.common_account_definition_simple_search(account_number)
        self.assert_table_data('Account number', 1, account_number)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ACT-Common Account Definition-View')
        # verify value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_text('Account number', account_number)
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if references_account_number:
            self.bo_assert_text('References account number', references_account_number)
        if references_account_number_2:
            self.bo_assert_text('References account number 2', references_account_number_2)

    def common_account_definition_update(self, account_number=None, account_name=None, references_account_number=None, references_account_number_2=None, list_error_message=None):
        # view
        self.common_account_definition_view(account_number=account_number)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_write_text('Account number', account_number)
        if account_name:
            self.bo_write_text('Account name', account_name)
        if references_account_number:
            self.bo_write_text('References account number', references_account_number)
        if references_account_number_2:
            self.bo_write_text('References account number 2', references_account_number_2)
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
            self.bo_click_tab('General information')
            account_number_out=self.bo_get_text('Account number')
            print(f'Account number: {account_number_out}')
            account_name_out=self.bo_get_text('Account name')
            print(f'Account name: {account_name_out}')
            return account_number_out, account_name_out

    def common_account_definition_delete(self, account_number, list_error_message=None):
        # search
        self.common_account_definition_simple_search(account_number)
        self.assert_table_data('Account number', 1, account_number)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{account_number}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.common_account_definition_simple_search(account_number)
            self.assert_search_not_found()
            print(f'Deleted: {account_number}')
            return account_number

    # ACT-Clearing Account Definition
    def clearing_account_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Accounting', 'Accounting Setup', 'Clearing Account Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-Clearing Account Definition-Search')
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def clearing_account_definition_advanced_search(self, branch_name=None, currency_code=None, clear_branch_name=None, clear_type=None, account_number=None):
        self.close_all_form()
        self.click_menu('Accounting', 'Accounting Setup', 'Clearing Account Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-Clearing Account Definition-Search')
        self.key_escape()
        if branch_name:
            self.adv_search_select('Branch name', branch_name)
        if currency_code:
            self.adv_search_text('Currency code', currency_code)
        self.key_escape()
        if clear_branch_name:
            self.adv_search_select('Clear branch name', clear_branch_name)
        self.key_escape()
        if clear_type:
            self.adv_search_select('Clear type', clear_type)
        if account_number:
            self.adv_search_text('Account number', str(account_number).replace('-', ''))
        self.click_button_search_advanced()
        self.wait_loading()

    def clearing_account_definition_add(self, branch_name=None, currency_code=None, clearing_branch_code=None, clearing_type=None, account_number=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Accounting', 'Accounting Setup', 'Clearing Account Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ACT-Clearing Account Definition-Add')
        # enter value
        self.key_escape()
        if branch_name:
            self.bo_select_single('Branch Name', branch_name)
        self.key_escape()
        if currency_code:
            self.bo_select_single('Currency Code', currency_code)
        self.key_escape()
        if clearing_branch_code:
            self.bo_select_single('Clearing Branch Code', clearing_branch_code)
        self.key_escape()
        if clearing_type:
            self.bo_select_single('Clearing Type', clearing_type)
        if account_number:
            self.bo_write_text_group_single('Account Number', str(account_number).replace('-', ''))
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
            branch_name_out=self.bo_get_select_single('Branch Name')
            print(f'Branch Name: {branch_name_out}')
            currency_code_out=self.bo_get_select_single('Currency Code')
            print(f'Currency Code: {currency_code_out}')
            clearing_branch_code_out=self.bo_get_select_single('Clearing Branch Code')
            print(f'Clearing Branch Code: {clearing_branch_code_out}')
            account_number_out=self.bo_get_text_group_single('Account Number')
            print(f'Account Number: {account_number_out}')
            return branch_name_out, currency_code_out, clearing_branch_code_out, account_number_out

    def clearing_account_definition_view(self, branch_name=None, currency_code=None, clearing_branch_code=None, clearing_type=None, account_number=None):
        # search
        self.clearing_account_definition_advanced_search(branch_name=self.get_branch_name(branch_name), currency_code=currency_code, clear_branch_name=self.get_branch_name(clearing_branch_code), account_number=account_number)
        if branch_name:
            self.assert_table_data('Branch Name', 1, self.get_branch_name(branch_name))
        if currency_code:
            self.assert_table_data('Currency Code', 1, currency_code)
        if clearing_branch_code:
            self.assert_table_data('Clear Branch Name', 1, self.get_branch_name(clearing_branch_code))
        if account_number:
            self.assert_table_data('Account Number', 1, self.no_mask(account_number))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ACT-Clearing Account Definition-View')
        # verify value
        self.bo_click_tab('General information')
        if branch_name:
            self.bo_assert_select('Branch Name', branch_name)
        if currency_code:
            self.bo_assert_select('Currency Code', currency_code)
        if clearing_branch_code:
            self.bo_assert_select('Clearing Branch Code', clearing_branch_code)
        if clearing_type:
            self.bo_assert_select('Clearing Type', clearing_type)
        if account_number:
            self.bo_assert_text_group('Account Number', self.no_mask(account_number))

    def clearing_account_definition_update(self, branch_name=None, currency_code=None, clearing_branch_code=None, clearing_type=None, account_number=None, account_number_update=None, list_error_message=None):
        # view
        self.clearing_account_definition_view(account_number=account_number)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if account_number_update:
            self.bo_write_text_group('Account Number', str(account_number_update).replace('-', ''))
        # assert value
        self.bo_click_tab('General information')
        if branch_name:
            self.bo_assert_select('Branch Name', branch_name)
        if currency_code:
            self.bo_assert_select('Currency Code', currency_code)
        if clearing_branch_code:
            self.bo_assert_select('Clearing Branch Code', clearing_branch_code)
        if clearing_type:
            self.bo_assert_select('Clearing Type', clearing_type)
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
            self.bo_click_tab('General information')
            branch_name_out=self.bo_get_select('Branch Name')
            print(f'Branch Name: {branch_name_out}')
            currency_code_out=self.bo_get_select('Currency Code')
            print(f'Currency Code: {currency_code_out}')
            clearing_branch_code_out=self.bo_get_select('Clearing Branch Code')
            print(f'Clearing Branch Code: {clearing_branch_code_out}')
            account_number_out=self.bo_get_text_group('Account Number')
            print(f'Account Number: {account_number_out}')
            return branch_name_out, currency_code_out, clearing_branch_code_out, account_number_out

    def clearing_account_definition_delete(self, branch_name=None, currency_code=None, clearing_branch_code=None, account_number=None, list_error_message=None):
        # search
        self.clearing_account_definition_advanced_search(branch_name=self.get_branch_name(branch_name), currency_code=currency_code, clear_branch_name=self.get_branch_name(clearing_branch_code), account_number=account_number)
        if branch_name:
            self.assert_table_data('Branch Name', 1, self.get_branch_name(branch_name))
        if currency_code:
            self.assert_table_data('Currency Code', 1, currency_code)
        if clearing_branch_code:
            self.assert_table_data('Clear Branch Name', 1, self.get_branch_name(clearing_branch_code))
        if account_number:
            self.assert_table_data('Account Number', 1, self.no_mask(account_number))
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{branch_name}' and '{currency_code}' and '{clearing_branch_code}' and '{account_number}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.clearing_account_definition_simple_search(str(account_number).replace('-', ''))
            self.assert_search_not_found()
            print(f"Deleted: '{branch_name}' and '{currency_code}' and '{clearing_branch_code}' and '{account_number}'")
            return branch_name, currency_code, clearing_branch_code, account_number

    # ACT-Foreign Exchange Account Definition
    def foreign_exchange_account_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Accounting', 'Accounting Setup', 'Foreign Exchange Account Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-Foreign Exchange Account Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def foreign_exchange_account_definition_advanced_search(self, branch_name=None, account_currency=None, clear_currency=None, clear_type=None, account_number=None):
        self.close_all_form()
        self.click_menu('Accounting', 'Accounting Setup', 'Foreign Exchange Account Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-Foreign Exchange Account Definition-Search')
        self.key_escape()
        if branch_name:
            self.adv_search_select('Branch name', branch_name)
        if account_currency:
            self.adv_search_text('Account currency', account_currency)
        if clear_currency:
            self.adv_search_text('Clear currency', clear_currency)
        self.key_escape()
        if clear_type:
            self.adv_search_select('Clear type', clear_type)
        if account_number:
            self.adv_search_text('Account number', str(account_number).replace('-', ''))
        self.click_button_search_advanced()
        self.wait_loading()

    def foreign_exchange_account_definition_add(self, branch_name=None, account_currency=None, clearing_currency=None, clearing_type=None, account_number=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Accounting', 'Accounting Setup', 'Foreign Exchange Account Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ACT-Foreign Exchange Account Definition-Add')
        # enter value
        self.key_escape()
        if branch_name:
            self.bo_select_single('Branch name', branch_name)
        self.key_escape()
        if account_currency:
            self.bo_select_single('Account currency', account_currency)
        self.key_escape()
        if clearing_currency:
            self.bo_select_single('Clearing currency', clearing_currency)
        self.key_escape()
        if clearing_type:
            self.bo_select_single('Clearing type', clearing_type)
        if account_number:
            self.bo_write_group_single('Account number', str(account_number).replace('-', ''))
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
            branch_name_out=self.bo_get_select_single('Branch name')
            print(f'Branch name: {branch_name_out}')
            account_currency_out=self.bo_get_select_single('Account currency')
            print(f'Account currency: {account_currency_out}')
            clearing_currency_out=self.bo_get_select_single('Clearing currency')
            print(f'Clearing currency: {clearing_currency_out}')
            account_number_out=self.bo_get_value_group_single('Account number')
            print(f'Account number: {account_number_out}')
            return branch_name_out, account_currency_out, clearing_currency_out, account_number_out

    def foreign_exchange_account_definition_view(self, branch_name=None, account_currency=None, clearing_currency=None, clearing_type=None, account_number=None):
        # search
        self.foreign_exchange_account_definition_advanced_search(branch_name=self.get_branch_name(branch_name), account_currency=account_currency, clear_currency=clearing_currency, account_number=account_number)
        if branch_name:
            self.assert_table_data('Branch name', 1, self.get_branch_name(branch_name))
        if account_currency:
            self.assert_table_data('Account currency', 1, account_currency)
        if clearing_currency:
            self.assert_table_data('Clear currency', 1, clearing_currency)
        if account_number:
            self.assert_table_data('Account number', 1, account_number)
        if clearing_type:
            self.assert_table_data('Clear type', 1, clearing_type)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ACT-Foreign Exchange Account Definition-View')
        # verify value
        self.bo_click_tab('General information')
        if branch_name:
            self.bo_assert_select('Branch name', branch_name)
        if account_currency:
            self.bo_assert_select('Account currency', account_currency)
        if clearing_currency:
            self.bo_assert_select('Clearing currency', clearing_currency)
        if clearing_type:
            self.bo_assert_select('Clearing type', clearing_type)
        if account_number:
            self.bo_assert_value_group('Account number', self.no_mask(account_number))

    def foreign_exchange_account_definition_update(self, branch_name=None, account_currency=None, clearing_currency=None, clearing_type=None, account_number=None, account_number_update=None, list_error_message=None):
        # view
        self.foreign_exchange_account_definition_view(branch_name=branch_name, account_currency=account_currency, clearing_currency=clearing_currency, account_number=account_number)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if account_number_update:
            self.bo_write_group('Account number', str(account_number_update).replace('-', ''))
        # assert value
        self.bo_click_tab('General information')
        if branch_name:
            self.bo_assert_select('Branch name', branch_name)
        if account_currency:
            self.bo_assert_select('Account currency', account_currency)
        if clearing_currency:
            self.bo_assert_select('Clearing currency', clearing_currency)
        if clearing_type:
            self.bo_assert_select('Clearing type', clearing_type)
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
            self.bo_click_tab('General information')
            branch_name_out=self.bo_get_select('Branch name')
            print(f'Branch name: {branch_name_out}')
            account_currency_out=self.bo_get_select('Account currency')
            print(f'Account currency: {account_currency_out}')
            clearing_currency_out=self.bo_get_select('Clearing currency')
            print(f'Clearing currency: {clearing_currency_out}')
            account_number_out=self.bo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return branch_name_out, account_currency_out, clearing_currency_out, account_number_out

    def foreign_exchange_account_definition_delete(self, branch_name=None, account_currency=None, clearing_currency=None, account_number=None, list_error_message=None):
        # search
        self.foreign_exchange_account_definition_advanced_search(branch_name=self.get_branch_name(branch_name), account_currency=account_currency, clear_currency=clearing_currency, account_number=account_number)
        if branch_name:
            self.assert_table_data('Branch name', 1, self.get_branch_name(branch_name))
        if account_currency:
            self.assert_table_data('Account currency', 1, account_currency)
        if clearing_currency:
            self.assert_table_data('Clear currency', 1, clearing_currency)
        if account_number:
            self.assert_table_data('Account number', 1, account_number)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{branch_name}' and '{account_currency}' and '{clearing_currency}' and '{account_number}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.foreign_exchange_account_definition_advanced_search(branch_name=self.get_branch_name(branch_name), account_currency=account_currency, clear_currency=clearing_currency, account_number=account_number)
            self.assert_search_not_found()
            print(f"Deleted: '{branch_name}' and '{account_currency}' and '{clearing_currency}' and '{account_number}'")
            return branch_name, account_currency, clearing_currency, account_number

    # ACT-Account Map Table
    def account_map_table_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Accounting', 'Account Map Table')
        self.wait_for_button_available('Search')
        self.assert_form_title('ACT-Account Map Table-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def account_map_table_add(self, neptune_gl_account=None, mapping_gl_account=None, mapping_type=None, account_name=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Accounting', 'Account Map Table')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('ACT-Account Map Table-Add')
        # enter value
        if neptune_gl_account:
            self.bo_write_group_single('Neptune GL Account', str(neptune_gl_account).replace('-', ''))
        if mapping_gl_account:
            self.bo_write_text_single('Mapping GL Account', mapping_gl_account)
        self.key_escape()
        if mapping_type:
            self.bo_select_single('Mapping type', mapping_type)
        if account_name:
            self.bo_write_text_single('Account Name', account_name)
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
            neptune_gl_account_out=self.bo_get_value_group_single('Neptune GL Account')
            print(f'Neptune GL Account: {neptune_gl_account_out}')
            mapping_gl_account_out=self.bo_get_text_single('Mapping GL Account')
            print(f'Mapping GL Account: {mapping_gl_account_out}')
            return neptune_gl_account_out, mapping_gl_account_out

    def account_map_table_view(self, neptune_gl_account=None, mapping_gl_account=None, mapping_type=None, account_name=None):
        # search
        self.account_map_table_simple_search(str(neptune_gl_account).replace('-', ''))
        self.assert_table_data('Neptune GL Account', 1, self.no_mask(neptune_gl_account))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ACT-Account Map Table-View')
        # verify value
        self.bo_click_tab('General information')
        if neptune_gl_account:
            self.bo_assert_value_group('Neptune GL Account', self.no_mask(neptune_gl_account))
        if mapping_gl_account:
            self.bo_assert_text('Mapping GL Account', mapping_gl_account)
        if mapping_type:
            self.bo_assert_select('Mapping type', mapping_type)
        if account_name:
            self.bo_assert_text('Account Name', account_name)

    def account_map_table_update(self, neptune_gl_account=None, mapping_gl_account=None, mapping_type=None, account_name=None, list_error_message=None):
        # view
        self.account_map_table_view(neptune_gl_account=neptune_gl_account)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if mapping_gl_account:
            self.bo_write_text('Mapping GL Account', mapping_gl_account)
        self.key_escape()
        if mapping_type:
            self.bo_select('Mapping type', mapping_type)
        if account_name:
            self.bo_write_text('Account Name', account_name)
        # assert value
        self.bo_click_tab('General information')
        if neptune_gl_account:
            self.bo_assert_value_group('Neptune GL Account', self.no_mask(neptune_gl_account))
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
            self.bo_click_tab('General information')
            neptune_gl_account_out=self.bo_get_value_group('Neptune GL Account')
            print(f'Neptune GL Account: {neptune_gl_account_out}')
            mapping_gl_account_out=self.bo_get_text('Mapping GL Account')
            print(f'Mapping GL Account: {mapping_gl_account_out}')
            return neptune_gl_account_out, mapping_gl_account_out

    def account_map_table_delete(self, neptune_gl_account, list_error_message=None):
        # search
        self.account_map_table_simple_search(str(neptune_gl_account).replace('-', ''))
        self.assert_table_data('Neptune GL Account', 1, self.no_mask(neptune_gl_account))
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{neptune_gl_account}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.account_map_table_simple_search(str(neptune_gl_account).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {neptune_gl_account}')
            return neptune_gl_account

