from webui_test.case import *

class StockActions(TestCase):

# -------------------------- handle FO - STOCK --------------------------
    # DPT_SRG: 11830: Stock registration
    def dpt_srg(self, module=None, stock_type=None, from_serial=None, to_serial=None, number_of_leaves=None, number_of_leaves_update=None, number_of_book=None, number_of_book_update=None, description=None, stock_prefix=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SRG', '11830')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11830: Stock registration')
        # enter value
        self.key_escape()
        if module:
            self.fo_select('Module', module)
            self.wait_loading()
        self.key_escape()
        if stock_type:
            self.fo_select('Stock type', stock_type)
            self.wait_loading()
        if from_serial:
            self.fo_write('From serial', self.no_mask(from_serial))
            self.wait_loading()
        if to_serial:
            self.fo_write('To serial', self.no_mask(to_serial))
            self.wait_loading()
        if number_of_leaves_update:
            self.fo_write_number('Number of leaves', number_of_leaves_update)
        if number_of_book_update:
            self.fo_write_number('Number of book', number_of_book_update)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if number_of_leaves:
            self.fo_assert_value('Number of leaves', number_of_leaves)
        if number_of_book:
            self.fo_assert_value('Number of book', number_of_book)
        if stock_prefix:
            self.fo_assert_text('Stock prefix', stock_prefix)
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
            print(f'Transaction references DPT_SRG: {transaction_references}')
            from_serial_out=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_out}')
            to_serial_out=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_out}')
            return transaction_references, from_serial_out, to_serial_out

    def dpt_srg_view(self, transaction_references, module=None, stock_type=None, from_serial=None, to_serial=None, number_of_leaves=None, number_of_leaves_update=None, number_of_book=None, number_of_book_update=None, description=None, stock_prefix=None, expected_posting=None):
        self.transaction_view(transaction_references, '11830: Stock registration')
        # compare value
        if module:
            self.fo_assert_select('Module', module)
        if stock_type:
            self.fo_assert_select('Stock type', stock_type)
        if from_serial:
            self.fo_assert_value('From serial', self.stock_number_mask(from_serial))
        if to_serial:
            self.fo_assert_value('To serial', self.stock_number_mask(to_serial))
        if number_of_leaves:
            self.fo_assert_value('Number of leaves', number_of_leaves)
        if number_of_leaves_update:
            self.fo_assert_value('Number of leaves', number_of_leaves_update)
        if number_of_book:
            self.fo_assert_value('Number of book', number_of_book)
        if number_of_book_update:
            self.fo_assert_value('Number of book', number_of_book_update)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if stock_prefix:
            self.fo_assert_text('Stock prefix', stock_prefix)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_SRG: {transaction_references}')
        from_serial_out=self.fo_get_value('From serial')
        print(f'F8: From serial: {from_serial_out}')
        to_serial_out=self.fo_get_value('To serial')
        print(f'F8: To serial: {to_serial_out}')
        return transaction_references, from_serial_out, to_serial_out

    # DPT_SAT: 11832: Stock assign to Staff
    def dpt_sat(self, stock_type=None, from_serial=None, to_serial=None, assigned_staff_code=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SAT', '11832')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11832: Stock assign to Staff')
        # enter value
        self.key_escape()
        if stock_type:
            self.fo_select('Stock type', stock_type)
            self.wait_loading()
        if from_serial:
            self.fo_write('From serial', str(from_serial).replace('-', ''))
            self.wait_loading()
        if to_serial:
            self.fo_write('To serial', str(to_serial).replace('-', ''))
            self.wait_loading()
        if assigned_staff_code:
            self.fo_write_group('Assigned staff code', assigned_staff_code)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
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
            print(f'Transaction references DPT_SAT: {transaction_references}')
            from_serial_out=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_out}')
            to_serial_out=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_out}')
            return transaction_references, from_serial_out, to_serial_out

    def dpt_sat_view(self, transaction_references, stock_type=None, from_serial=None, to_serial=None, assigned_staff_code=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '11832: Stock assign to Staff')
        # compare value
        if stock_type:
            self.fo_assert_select('Stock type', stock_type)
        if from_serial:
            self.fo_assert_value('From serial', self.stock_number_mask(from_serial))
        if to_serial:
            self.fo_assert_value('To serial', self.stock_number_mask(to_serial))
        if assigned_staff_code:
            self.fo_assert_value_group('Assigned staff code', assigned_staff_code)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_SAT: {transaction_references}')
        from_serial_out=self.fo_get_value('From serial')
        print(f'F8: From serial: {from_serial_out}')
        to_serial_out=self.fo_get_value('To serial')
        print(f'F8: To serial: {to_serial_out}')
        return transaction_references, from_serial_out, to_serial_out

    # DPT_CCR: DPT-11834: Stock Confirm Received
    def dpt_ccr(self, stock_type=None, from_serial=None, to_serial=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CCR', '11834')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-11834: Stock Confirm Received')
        # enter value
        self.key_escape()
        if stock_type:
            self.fo_select('Stock type', stock_type)
            self.wait_loading()
        if from_serial:
            self.fo_write('From serial', str(from_serial).replace('-', ''))
            self.wait_loading()
        if to_serial:
            self.fo_write('To serial', str(to_serial).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
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
            print(f'Transaction references DPT_CCR: {transaction_references}')
            from_serial_out=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_out}')
            to_serial_out=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_out}')
            return transaction_references, from_serial_out, to_serial_out

    def dpt_ccr_view(self, transaction_references, stock_type=None, from_serial=None, to_serial=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'DPT-11834: Stock Confirm Received')
        # compare value
        if stock_type:
            self.fo_assert_select('Stock type', stock_type)
        if from_serial:
            self.fo_assert_value('From serial', self.stock_number_mask(from_serial))
        if to_serial:
            self.fo_assert_value('To serial', self.stock_number_mask(to_serial))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CCR: {transaction_references}')
        from_serial_out=self.fo_get_value('From serial')
        print(f'F8: From serial: {from_serial_out}')
        to_serial_out=self.fo_get_value('To serial')
        print(f'F8: To serial: {to_serial_out}')
        return transaction_references, from_serial_out, to_serial_out

    # DPT_SRA: DPT-11835: Reject Assigned Stock
    def dpt_sra(self, stock_type=None, from_serial=None, to_serial=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SRA', '11835')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-11835: Reject Assigned Stock')
        # enter value
        self.key_escape()
        if stock_type:
            self.fo_select('Stock type', stock_type)
            self.wait_loading()
        if from_serial:
            self.fo_write('From serial', str(from_serial).replace('-', ''))
            self.wait_loading()
        if to_serial:
            self.fo_write('To serial', str(to_serial).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
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
            print(f'Transaction references DPT_SRA: {transaction_references}')
            from_serial_out=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_out}')
            to_serial_out=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_out}')
            return transaction_references, from_serial_out, to_serial_out

    def dpt_sra_view(self, transaction_references, stock_type=None, from_serial=None, to_serial=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'DPT-11835: Reject Assigned Stock')
        # compare value
        if stock_type:
            self.fo_assert_select('Stock type', stock_type)
        if from_serial:
            self.fo_assert_value('From serial', self.stock_number_mask(from_serial))
        if to_serial:
            self.fo_assert_value('To serial', self.stock_number_mask(to_serial))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_SRA: {transaction_references}')
        from_serial_out=self.fo_get_value('From serial')
        print(f'F8: From serial: {from_serial_out}')
        to_serial_out=self.fo_get_value('To serial')
        print(f'F8: To serial: {to_serial_out}')
        return transaction_references, from_serial_out, to_serial_out

    # DPT_CRT: 11833: Stock returned
    def dpt_crt(self, stock_type=None, from_serial=None, to_serial=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CRT', '11833')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11833: Stock returned')
        # enter value
        self.key_escape()
        if stock_type:
            self.fo_select('Stock type', stock_type)
            self.wait_loading()
        if from_serial:
            self.fo_write('From serial', str(from_serial).replace('-', ''))
            self.wait_loading()
        if to_serial:
            self.fo_write('To serial', str(to_serial).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
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
            print(f'Transaction references DPT_CRT: {transaction_references}')
            from_serial_out=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_out}')
            to_serial_out=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_out}')
            return transaction_references, from_serial_out, to_serial_out

    def dpt_crt_view(self, transaction_references, stock_type=None, from_serial=None, to_serial=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '11833: Stock returned')
        # compare value
        if stock_type:
            self.fo_assert_select('Stock type', stock_type)
        if from_serial:
            self.fo_assert_value('From serial', self.stock_number_mask(from_serial))
        if to_serial:
            self.fo_assert_value('To serial', self.stock_number_mask(to_serial))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CRT: {transaction_references}')
        from_serial_out=self.fo_get_value('From serial')
        print(f'F8: From serial: {from_serial_out}')
        to_serial_out=self.fo_get_value('To serial')
        print(f'F8: To serial: {to_serial_out}')
        return transaction_references, from_serial_out, to_serial_out

    # DPT_SAB: DPT-11831: Stock Assigned To Branch
    def dpt_sab(self, stock_type=None, from_serial=None, to_serial=None, branch_code=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SAB', '11831')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-11831: Stock Assigned To Branch')
        # enter value
        self.key_escape()
        if stock_type:
            self.fo_select('Stock type', stock_type)
            self.wait_loading()
        if from_serial:
            self.fo_write('From serial', str(from_serial).replace('-', ''))
            self.wait_loading()
        if to_serial:
            self.fo_write('To serial', str(to_serial).replace('-', ''))
            self.wait_loading()
        if branch_code:
            self.fo_write_group('Branch code', branch_code)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
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
            print(f'Transaction references DPT_SAB: {transaction_references}')
            from_serial_out=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_out}')
            to_serial_out=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_out}')
            branch_code_out=self.fo_get_value_group('Branch code')
            print(f'Branch code: {branch_code_out}')
            return transaction_references, from_serial_out, to_serial_out, branch_code_out

    def dpt_sab_view(self, transaction_references, stock_type=None, from_serial=None, to_serial=None, branch_code=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'DPT-11831: Stock Assigned To Branch')
        # compare value
        if stock_type:
            self.fo_assert_select('Stock type', stock_type)
        if from_serial:
            self.fo_assert_value('From serial', self.stock_number_mask(from_serial))
        if to_serial:
            self.fo_assert_value('To serial', self.stock_number_mask(to_serial))
        if branch_code:
            self.fo_assert_value_group('Branch code', branch_code)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_SAB: {transaction_references}')
        from_serial_out=self.fo_get_value('From serial')
        print(f'F8: From serial: {from_serial_out}')
        to_serial_out=self.fo_get_value('To serial')
        print(f'F8: To serial: {to_serial_out}')
        branch_code_out=self.fo_get_value_group('Branch code')
        print(f'F8: Branch code: {branch_code_out}')
        return transaction_references, from_serial_out, to_serial_out, branch_code_out

    # DPT_CIS: 11801: Cheque book issued
    def dpt_cis(self, account_number=None, stock_number=None, from_serial=None, to_serial=None, fee_amount=None, description=None, fee_collect_method=None, account_number_for_fee=None, account_holding_branch_name=None, number_of_leaves=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CIS', '11801')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11801: Cheque book issued')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if stock_number:
            self.fo_write_text('Stock number', stock_number)
        if from_serial:
            self.fo_write('From serial', str(from_serial).replace('-', ''))
            self.wait_loading()
        if to_serial:
            self.fo_write('To serial', str(to_serial).replace('-', ''))
            self.wait_loading()
        if fee_amount:
            self.fo_write_number('Fee amount', fee_amount)
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
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if number_of_leaves:
            self.fo_assert_value('Number of leaves', number_of_leaves)
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
            print(f'Transaction references DPT_CIS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            from_serial_out=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_out}')
            to_serial_out=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_out}')
            return transaction_references, from_serial_out, to_serial_out

    def dpt_cis_view(self, transaction_references, account_number=None, stock_number=None, from_serial=None, to_serial=None, fee_amount=None, description=None, fee_collect_method=None, account_number_for_fee=None, account_holding_branch_name=None, number_of_leaves=None, expected_posting=None):
        self.transaction_view(transaction_references, '11801: Cheque book issued')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if stock_number:
            self.fo_assert_text('Stock number', stock_number)
        if from_serial:
            self.fo_assert_value('From serial', self.stock_number_mask(from_serial))
        if to_serial:
            self.fo_assert_value('To serial', self.stock_number_mask(to_serial))
        if fee_amount:
            self.fo_assert_value('Fee amount', fee_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', str(account_number_for_fee).replace('-', ''))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if number_of_leaves:
            self.fo_assert_value('Number of leaves', number_of_leaves)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CIS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        from_serial_out=self.fo_get_value('From serial')
        print(f'F8: From serial: {from_serial_out}')
        to_serial_out=self.fo_get_value('To serial')
        print(f'F8: To serial: {to_serial_out}')
        return transaction_references, from_serial_out, to_serial_out

    # DPT_CEI: 11850:Issued hold balance for cheque
    def dpt_cei(self, cheque_no=None, cheque_amount=None, purpose_of_hold_amount=None, description=None, account_number=None, account_holding_branch_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CEI', '11850')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11850:Issued hold balance for cheque')
        # enter value
        if cheque_no:
            self.fo_write('Cheque no', str(cheque_no).replace('-', ''))
            self.wait_loading()
        if cheque_amount:
            self.fo_write_number('Cheque amount', cheque_amount)
        self.key_escape()
        if purpose_of_hold_amount:
            self.fo_select('Purpose of hold amount', purpose_of_hold_amount)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
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
            print(f'Transaction references DPT_CEI: {transaction_references}')
            cheque_no_out=self.fo_get_value('Cheque no')
            print(f'Cheque no: {cheque_no_out}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, cheque_no_out, account_number_out

    def dpt_cei_view(self, transaction_references, cheque_no=None, cheque_amount=None, purpose_of_hold_amount=None, description=None, account_number=None, account_holding_branch_name=None, expected_posting=None):
        self.transaction_view(transaction_references, '11850:Issued hold balance for cheque')
        # compare value
        if cheque_no:
            self.fo_assert_value('Cheque no', self.stock_number_mask(cheque_no))
        if cheque_amount:
            self.fo_assert_value('Cheque amount', cheque_amount)
        if purpose_of_hold_amount:
            self.fo_assert_select('Purpose of hold amount', purpose_of_hold_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CEI: {transaction_references}')
        cheque_no_out=self.fo_get_value('Cheque no')
        print(f'F8: Cheque no: {cheque_no_out}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, cheque_no_out, account_number_out

    # DPT_REC: 11852:Release hold balance for cheque
    def dpt_rec(self, cheque_no=None, cheque_amount=None, purpose_of_hold_amount=None, description=None, account_number=None, account_holding_branch_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_REC', '11852')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11852:Release hold balance for cheque')
        # enter value
        if cheque_no:
            self.fo_write('Cheque no', str(cheque_no).replace('-', ''))
            self.wait_loading()
        if cheque_amount:
            self.fo_write_number('Cheque amount', cheque_amount)
            self.wait_loading()
        self.key_escape()
        if purpose_of_hold_amount:
            self.fo_select('Purpose of hold amount', purpose_of_hold_amount)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
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
            print(f'Transaction references DPT_REC: {transaction_references}')
            cheque_no_out=self.fo_get_value('Cheque no')
            print(f'Cheque no: {cheque_no_out}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, cheque_no_out, account_number_out

    def dpt_rec_view(self, transaction_references, cheque_no=None, cheque_amount=None, purpose_of_hold_amount=None, description=None, account_number=None, account_holding_branch_name=None, expected_posting=None):
        self.transaction_view(transaction_references, '11852:Release hold balance for cheque')
        # compare value
        if cheque_no:
            self.fo_assert_value('Cheque no', self.stock_number_mask(cheque_no))
        if cheque_amount:
            self.fo_assert_value('Cheque amount', cheque_amount)
        if purpose_of_hold_amount:
            self.fo_assert_select('Purpose of hold amount', purpose_of_hold_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_REC: {transaction_references}')
        cheque_no_out=self.fo_get_value('Cheque no')
        print(f'F8: Cheque no: {cheque_no_out}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, cheque_no_out, account_number_out

    # DPT_CDT: 1111: Deposit by cheque
    def dpt_cdt(self, cheque_no=None, debit_amount=None, credit_account=None, debit_account_name=None, customer_code=None, customer_address=None, mobile_phone=None, nrc=None, description=None, debit_account=None, account_holding_branch_name=None, balance=None, available_balance=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CDT', '1111')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1111: Deposit by cheque')
        # enter value
        if cheque_no:
            self.fo_write('Cheque no', self.no_mask(cheque_no))
            self.wait_loading()
        if debit_amount:
            self.fo_write_number('Debit amount', debit_amount)
            self.wait_loading()
        if credit_account:
            self.fo_write_group('Credit account', self.no_mask(credit_account))
            self.wait_loading()
        if debit_account_name:
            self.fo_write_text('Debit account name', debit_account_name)
        if customer_code:
            self.fo_write('Customer code', customer_code)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if mobile_phone:
            self.fo_click_collap('Customer description')
            self.fo_write_text_multi('Customer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Customer description')
            self.fo_write_text_multi('Customer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if debit_account:
            self.fo_assert_value_group('Debit account', self.deposit_account_number_mask(debit_account))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if balance:
            self.fo_assert_value('Balance', balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
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
            print(f'Transaction references DPT_CDT: {transaction_references}')
            cheque_no_out=self.fo_get_value('Cheque no')
            print(f'Cheque no: {cheque_no_out}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            debit_account_out=self.fo_get_value_group('Debit account')
            print(f'Debit account: {debit_account_out}')
            return transaction_references, cheque_no_out, credit_account_out, debit_account_out

    def dpt_cdt_view(self, transaction_references, cheque_no=None, debit_amount=None, credit_account=None, debit_account_name=None, customer_code=None, customer_address=None, mobile_phone=None, nrc=None, description=None, debit_account=None, account_holding_branch_name=None, balance=None, available_balance=None, expected_posting=None):
        self.transaction_view(transaction_references, '1111: Deposit by cheque')
        # compare value
        if cheque_no:
            self.fo_assert_value('Cheque no', self.stock_number_mask(cheque_no))
        if debit_amount:
            self.fo_assert_value('Debit amount', debit_amount)
        if credit_account:
            self.fo_assert_value_group('Credit account', self.deposit_account_number_mask(credit_account))
        if debit_account_name:
            self.fo_assert_text('Debit account name', debit_account_name)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if mobile_phone:
            self.fo_click_collap('Customer description')
            self.fo_assert_text_multi('Customer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Customer description')
            self.fo_assert_text_multi('Customer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if debit_account:
            self.fo_assert_value_group('Debit account', self.deposit_account_number_mask(debit_account))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if balance:
            self.fo_assert_value('Balance', balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CDT: {transaction_references}')
        cheque_no_out=self.fo_get_value('Cheque no')
        print(f'F8: Cheque no: {cheque_no_out}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        debit_account_out=self.fo_get_value_group('Debit account')
        print(f'F8: Debit account: {debit_account_out}')
        return transaction_references, cheque_no_out, credit_account_out, debit_account_out

    # DPT_CWC: 1121: Cash withdrawal by cheque
    def dpt_cwc(self, cheque_no=None, cheque_amount=None, withdrawer_name=None, withdrawer_id=None, withdrawer_address=None, mobile_phone=None, nrc=None, description=None, account_number=None, account_holding_branch_name=None, current_balance=None, available_balance=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CWC', '1121')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1121: Cash withdrawal by cheque')
        # enter value
        if cheque_no:
            self.fo_write('Cheque no', self.no_mask(cheque_no))
            self.wait_loading()
        if cheque_amount:
            self.fo_write_number('Cheque amount', cheque_amount)
            self.wait_loading()
        if withdrawer_name:
            self.fo_write_text('Withdrawer name', withdrawer_name)
        if withdrawer_id:
            self.fo_write('Withdrawer id', withdrawer_id)
        if withdrawer_address:
            self.fo_write_text('Withdrawer address', withdrawer_address)
        if mobile_phone:
            self.fo_click_collap('Withdrawer description')
            self.fo_write_text_multi('Withdrawer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Withdrawer description')
            self.fo_write_text_multi('Withdrawer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if current_balance:
            self.fo_assert_value('Current balance', current_balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
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
            print(f'Transaction references DPT_CWC: {transaction_references}')
            cheque_no_out=self.fo_get_value('Cheque no')
            print(f'Cheque no: {cheque_no_out}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, cheque_no_out, account_number_out

    def dpt_cwc_view(self, transaction_references, cheque_no=None, cheque_amount=None, withdrawer_name=None, withdrawer_id=None, withdrawer_address=None, mobile_phone=None, nrc=None, description=None, account_number=None, account_holding_branch_name=None, current_balance=None, available_balance=None, expected_posting=None):
        self.transaction_view(transaction_references, '1121: Cash withdrawal by cheque')
        # compare value
        if cheque_no:
            self.fo_assert_value('Cheque no', self.stock_number_mask(cheque_no))
        if cheque_amount:
            self.fo_assert_value('Cheque amount', cheque_amount)
        if withdrawer_name:
            self.fo_assert_text('Withdrawer name', withdrawer_name)
        if withdrawer_id:
            self.fo_assert_value('Withdrawer id', self.customer_code_mask(withdrawer_id))
        if withdrawer_address:
            self.fo_assert_text('Withdrawer address', withdrawer_address)
        if mobile_phone:
            self.fo_click_collap('Withdrawer description')
            self.fo_assert_text_multi('Withdrawer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Withdrawer description')
            self.fo_assert_text_multi('Withdrawer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if current_balance:
            self.fo_assert_value('Current balance', current_balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CWC: {transaction_references}')
        cheque_no_out=self.fo_get_value('Cheque no')
        print(f'F8: Cheque no: {cheque_no_out}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, cheque_no_out, account_number_out

    # DPT_CWM: 1125: Misellaneous debit by cheque
    def dpt_cwm(self, cheque_no=None, cheque_amount=None, credit_accounting=None, accounting_amount=None, accounting_amount_update=None, withdrawer_name=None, withdrawer_code=None, withdrawer_address=None, mobile_phone=None, nrc=None, description=None, account_number=None, account_holding_branch_name=None, current_balance=None, available_balance=None, account_linkage=None, amount_linkage=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CWM', '1125')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1125: Misellaneous debit by cheque')
        # enter value
        if cheque_no:
            self.fo_write('Cheque no', self.no_mask(cheque_no))
            self.wait_loading()
        if cheque_amount:
            self.fo_write_number('Cheque amount', cheque_amount)
            self.wait_loading()
        if credit_accounting:
            self.fo_write_group('Credit accounting', self.no_mask(credit_accounting))
            self.wait_loading()
        if accounting_amount_update:
            self.fo_write_number('Accounting amount', accounting_amount_update)
            self.wait_loading()
        if withdrawer_name:
            self.fo_write_text('Withdrawer name', withdrawer_name)
        if withdrawer_code:
            self.fo_write('Withdrawer code', withdrawer_code)
        if withdrawer_address:
            self.fo_write_text('Withdrawer address', withdrawer_address)
        if mobile_phone:
            self.fo_click_collap('Withdrawer description')
            self.fo_write_text_multi('Withdrawer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Withdrawer description')
            self.fo_write_text_multi('Withdrawer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if accounting_amount:
            self.fo_assert_value('Accounting amount', accounting_amount)
            self.wait_loading()
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if current_balance:
            self.fo_assert_value('Current balance', current_balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
        if account_linkage:
            self.fo_assert_text_group('Account Linkage', account_linkage)
        if amount_linkage:
            self.fo_assert_value('Amount linkage', amount_linkage)
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
            print(f'Transaction references DPT_CWM: {transaction_references}')
            cheque_no_out=self.fo_get_value('Cheque no')
            print(f'Cheque no: {cheque_no_out}')
            credit_accounting_out=self.fo_get_value_group('Credit accounting')
            print(f'Credit accounting: {credit_accounting_out}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, cheque_no_out, credit_accounting_out, account_number_out

    def dpt_cwm_view(self, transaction_references, cheque_no=None, cheque_amount=None, credit_accounting=None, accounting_amount=None, accounting_amount_update=None, withdrawer_name=None, withdrawer_code=None, withdrawer_address=None, mobile_phone=None, nrc=None, description=None, account_number=None, account_holding_branch_name=None, current_balance=None, available_balance=None, account_linkage=None, amount_linkage=None, expected_posting=None):
        self.transaction_view(transaction_references, '1125: Misellaneous debit by cheque')
        # compare value
        if cheque_no:
            self.fo_assert_value('Cheque no', self.stock_number_mask(cheque_no))
        if cheque_amount:
            self.fo_assert_value('Cheque amount', cheque_amount)
        if credit_accounting:
            self.fo_assert_value_group('Credit accounting', self.gl_account_number_mask(credit_accounting))
        if accounting_amount:
            self.fo_assert_value('Accounting amount', accounting_amount)
        if accounting_amount_update:
            self.fo_assert_value('Accounting amount', accounting_amount_update)
        if withdrawer_name:
            self.fo_assert_text('Withdrawer name', withdrawer_name)
        if withdrawer_code:
            self.fo_assert_value('Withdrawer code', self.customer_code_mask(withdrawer_code))
        if withdrawer_address:
            self.fo_assert_text('Withdrawer address', withdrawer_address)
        if mobile_phone:
            self.fo_click_collap('Withdrawer description')
            self.fo_assert_text_multi('Withdrawer description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Withdrawer description')
            self.fo_assert_text_multi('Withdrawer description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if current_balance:
            self.fo_assert_value('Current balance', current_balance)
        if available_balance:
            self.fo_assert_value('Available balance', available_balance)
        if account_linkage:
            self.fo_assert_text_group('Account Linkage', account_linkage)
        if amount_linkage:
            self.fo_assert_value('Amount linkage', amount_linkage)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CWM: {transaction_references}')
        cheque_no_out=self.fo_get_value('Cheque no')
        print(f'F8: Cheque no: {cheque_no_out}')
        credit_accounting_out=self.fo_get_value_group('Credit accounting')
        print(f'F8: Credit accounting: {credit_accounting_out}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, cheque_no_out, credit_accounting_out, account_number_out

    # DPT_CTS: 11837: Change status of stock
    def dpt_cts(self, account_number=None, stock_type=None, from_serial=None, to_serial=None, status=None, description=None, account_holding_branch_name=None, fee_amount=None, stock_prefix=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CTS', '11837')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11837: Change status of stock')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        self.key_escape()
        if stock_type:
            self.fo_select('Stock type', stock_type)
            self.wait_loading()
        if from_serial:
            self.fo_write('From serial', self.no_mask(from_serial))
            self.wait_loading()
        if to_serial:
            self.fo_write('To serial', self.no_mask(to_serial))
            self.wait_loading()
        self.key_escape()
        if status:
            self.fo_select('Status', status)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if fee_amount:
            self.fo_assert_value('Fee amount', fee_amount)
        if stock_prefix:
            self.fo_assert_text('Stock prefix', stock_prefix)
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
            print(f'Transaction references DPT_CTS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            from_serial_out=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_out}')
            to_serial_out=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_out}')
            return transaction_references, from_serial_out, to_serial_out

    def dpt_cts_view(self, transaction_references, account_number=None, stock_type=None, from_serial=None, to_serial=None, status=None, description=None, account_holding_branch_name=None, fee_amount=None, stock_prefix=None, expected_posting=None):
        self.transaction_view(transaction_references, '11837: Change status of stock')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if stock_type:
            self.fo_assert_select('Stock type', stock_type)
        if from_serial:
            self.fo_assert_value('From serial', self.stock_number_mask(from_serial))
        if to_serial:
            self.fo_assert_value('To serial', self.stock_number_mask(to_serial))
        if status:
            self.fo_assert_select('Status', status)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if fee_amount:
            self.fo_assert_value('Fee amount', fee_amount)
        if stock_prefix:
            self.fo_assert_text('Stock prefix', stock_prefix)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CTS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        from_serial_out=self.fo_get_value('From serial')
        print(f'F8: From serial: {from_serial_out}')
        to_serial_out=self.fo_get_value('To serial')
        print(f'F8: To serial: {to_serial_out}')
        return transaction_references, from_serial_out, to_serial_out

    # DPT_CIQ: 1167: Cheque inquiry
    def dpt_ciq(self, account_number=None, serial_number=None, account_holding_branch_name=None, serial_numbers=None, expected_values=None, expected_serial_number=None, expected_value=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CIQ', '1167')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1167: Cheque inquiry')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if serial_number:
            self.fo_write('Serial number', self.no_mask(serial_number))
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
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
            # compare value
            if serial_numbers:
                for serial_no, expected in zip(serial_numbers, expected_values):
                    self.fo_assert_text_table('Serial No.', str(serial_no).replace('-',''), 'Status', expected)
            if expected_serial_number:
                self.fo_assert_text_table('Serial No.', str(expected_serial_number).replace('-',''), 'Status', expected_value)
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_CIQ: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            serial_number_out=self.fo_get_value('Serial number')
            print(f'Serial number: {serial_number_out}')
            return transaction_references, serial_number_out

    # DPT_SLS: DPT-1162: Cheque Leaves Status Inquiry
    def dpt_sls(self, from_serial=None, to_serial=None, serial_numbers=None, expected_values=None, expected_serial_number=None, expected_value=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SLS', '1162')
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT-1162: Cheque Leaves Status Inquiry')
        # enter value
        if from_serial:
            self.fo_write('From serial', self.no_mask(from_serial))
            self.wait_loading()
        if to_serial:
            self.fo_write('To serial', self.no_mask(to_serial))
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
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
            # compare value
            if serial_numbers:
                for serial_no, expected in zip(serial_numbers, expected_values):
                    self.fo_assert_text_table('Serrial No', str(serial_no).replace('-',''), 'Stock leave status', expected)
            if expected_serial_number:
                self.fo_assert_text_table('Serrial No', str(expected_serial_number).replace('-',''), 'Stock leave status', expected_value)
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references DPT_SLS: {transaction_references}')
            from_serial_out=self.fo_get_value('From serial')
            print(f'From serial: {from_serial_out}')
            to_serial_out=self.fo_get_value('To serial')
            print(f'To serial: {to_serial_out}')
            return transaction_references, from_serial_out, to_serial_out

    # DPT_SBI: 11802: Deposit savings book issue
    def dpt_sbi(self, account_number=None, serial_no=None, description=None, fee_collect_method=None, account_number_for_fee=None, account_holding_branch_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_SBI', '11802')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11802: Deposit savings book issue')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if serial_no:
            self.fo_write('Serial no', self.no_mask(serial_no))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', self.no_mask(account_number_for_fee))
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
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
            print(f'Transaction references DPT_SBI: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            serial_no_out=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_out}')
            return transaction_references, serial_no_out

    def dpt_sbi_view(self, transaction_references, account_number=None, serial_no=None, description=None, fee_collect_method=None, account_number_for_fee=None, account_holding_branch_name=None, expected_posting=None):
        self.transaction_view(transaction_references, '11802: Deposit savings book issue')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if serial_no:
            self.fo_assert_value('Serial no', self.stock_number_mask(serial_no))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', self.no_mask(account_number_for_fee))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_SBI: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        serial_no_out=self.fo_get_value('Serial no')
        print(f'F8: Serial no: {serial_no_out}')
        return transaction_references, serial_no_out

    # DPT_FBI: 11804: Fixed deposit book issue
    def dpt_fbi(self, account_number=None, serial_no=None, description=None, fee_collect_method=None, account_number_for_fee=None, account_holding_branch_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_FBI', '11804')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11804: Fixed deposit book issue')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if serial_no:
            self.fo_write('Serial no', self.no_mask(serial_no))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', self.no_mask(account_number_for_fee))
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
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
            print(f'Transaction references DPT_FBI: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            serial_no_out=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_out}')
            return transaction_references, serial_no_out

    def dpt_fbi_view(self, transaction_references, account_number=None, serial_no=None, description=None, fee_collect_method=None, account_number_for_fee=None, account_holding_branch_name=None, expected_posting=None):
        self.transaction_view(transaction_references, '11804: Fixed deposit book issue')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if serial_no:
            self.fo_assert_value('Serial no', self.stock_number_mask(serial_no))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', self.no_mask(account_number_for_fee))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_FBI: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        serial_no_out=self.fo_get_value('Serial no')
        print(f'F8: Serial no: {serial_no_out}')
        return transaction_references, serial_no_out

    # DPT_CER: 11803: Fixed deposit receipt issued
    def dpt_cer(self, account_number=None, cerfiticate_serial=None, description=None, fee_collect_method=None, account_number_for_fee=None, account_holding_branch_name=None, currency=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CER', '11803')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11803: Fixed deposit receipt issued')
        # enter value
        if account_number:
            self.fo_write_group('Account number', self.no_mask(account_number))
            self.wait_loading()
        if cerfiticate_serial:
            self.fo_write('Cerfiticate serial', self.no_mask(cerfiticate_serial))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', self.no_mask(account_number_for_fee))
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if currency:
            self.fo_assert_select('Currency', currency)
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
            print(f'Transaction references DPT_CER: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            cerfiticate_serial_out=self.fo_get_value('Cerfiticate serial')
            print(f'Cerfiticate serial: {cerfiticate_serial_out}')
            return transaction_references, cerfiticate_serial_out

    def dpt_cer_view(self, transaction_references, account_number=None, cerfiticate_serial=None, description=None, fee_collect_method=None, account_number_for_fee=None, account_holding_branch_name=None, currency=None, expected_posting=None):
        self.transaction_view(transaction_references, '11803: Fixed deposit receipt issued')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if cerfiticate_serial:
            self.fo_assert_value('Cerfiticate serial', self.stock_number_mask(cerfiticate_serial))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', self.no_mask(account_number_for_fee))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if currency:
            self.fo_assert_select('Currency', currency)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CER: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        cerfiticate_serial_out=self.fo_get_value('Cerfiticate serial')
        print(f'F8: Cerfiticate serial: {cerfiticate_serial_out}')
        return transaction_references, cerfiticate_serial_out

    # DPT_POI: 11816: Payment order issued
    def dpt_poi(self, serial_no=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, amount=None, currency=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, purpose=None, debit_method=None, debit_account=None, description=None, issued_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_POI', '11816')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11816: Payment order issued')
        # enter value
        if serial_no:
            self.fo_write('Serial no', self.no_mask(serial_no))
            self.wait_loading()
        if expired_date:
            self.fo_write_date('Expired date', expired_date)
        if issuing_name:
            self.fo_write_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_write_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_write_text('Issuer contact number', issuer_contact_number)
        if amount:
            self.fo_write_number('Amount', amount)
        self.key_escape()
        if currency:
            self.fo_select('Currency', currency)
        if beneficiary_name:
            self.fo_write_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_write_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_write_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_write_text('Beneficiary address', beneficiary_address)
        if purpose:
            self.fo_write_text('Purpose', purpose)
        self.key_escape()
        if debit_method:
            self.fo_select('Debit method', debit_method)
        if debit_account:
            self.fo_write_text_group('Debit account', self.no_mask(debit_account))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if issued_date:
            self.fo_assert_date('Issued date', issued_date)
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
            print(f'Transaction references DPT_POI: {transaction_references}')
            serial_no_out=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_out}')
            return transaction_references, serial_no_out

    def dpt_poi_view(self, transaction_references, serial_no=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, amount=None, currency=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, purpose=None, debit_method=None, debit_account=None, description=None, issued_date=None, expected_posting=None):
        self.transaction_view(transaction_references, '11816: Payment order issued')
        # compare value
        if serial_no:
            self.fo_assert_value('Serial no', self.stock_number_mask(serial_no))
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if amount:
            self.fo_assert_value('Amount', amount)
        if currency:
            self.fo_assert_select('Currency', currency)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if purpose:
            self.fo_assert_text('Purpose', purpose)
        if debit_method:
            self.fo_assert_select('Debit method', debit_method)
        if debit_account:
            self.fo_assert_text_group('Debit account', self.no_mask(debit_account))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if issued_date:
            self.fo_assert_date('Issued date', issued_date)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_POI: {transaction_references}')
        serial_no_out=self.fo_get_value('Serial no')
        print(f'F8: Serial no: {serial_no_out}')
        return transaction_references, serial_no_out

    # DPT_POW: 11817: Payment order withdrawal
    def dpt_pow(self, serial_no=None, withdrawal_method=None, credit_account=None, description=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, withdrawal_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_POW', '11817')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11817: Payment order withdrawal')
        # enter value
        if serial_no:
            self.fo_write('Serial no', self.no_mask(serial_no))
            self.wait_loading()
        self.key_escape()
        if withdrawal_method:
            self.fo_select('Withdrawal method', withdrawal_method)
        if credit_account:
            self.fo_write_text_group('Credit account', self.no_mask(credit_account))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if withdrawal_amount:
            self.fo_assert_value('Withdrawal amount', withdrawal_amount)
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
            print(f'Transaction references DPT_POW: {transaction_references}')
            serial_no_out=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_out}')
            return transaction_references, serial_no_out

    def dpt_pow_view(self, transaction_references, serial_no=None, withdrawal_method=None, credit_account=None, description=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, withdrawal_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '11817: Payment order withdrawal')
        # compare value
        if serial_no:
            self.fo_assert_value('Serial no', self.stock_number_mask(serial_no))
        if withdrawal_method:
            self.fo_assert_select('Withdrawal method', withdrawal_method)
        if credit_account:
            self.fo_assert_text_group('Credit account', self.no_mask(credit_account))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if withdrawal_amount:
            self.fo_assert_value('Withdrawal amount', withdrawal_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_POW: {transaction_references}')
        serial_no_out=self.fo_get_value('Serial no')
        print(f'F8: Serial no: {serial_no_out}')
        return transaction_references, serial_no_out

    # DPT_RPO: 11818: Payment order return
    def dpt_rpo(self, serial_no=None, return_method=None, credit_account=None, description=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, return_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_RPO', '11818')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11818: Payment order return')
        # enter value
        if serial_no:
            self.fo_write('Serial no', self.no_mask(serial_no))
            self.wait_loading()
        self.key_escape()
        if return_method:
            self.fo_select('Return method', return_method)
        if credit_account:
            self.fo_write_text_group('Credit account', self.no_mask(credit_account))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if return_amount:
            self.fo_assert_value('Return amount', return_amount)
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
            print(f'Transaction references DPT_RPO: {transaction_references}')
            serial_no_out=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_out}')
            return transaction_references, serial_no_out

    def dpt_rpo_view(self, transaction_references, serial_no=None, return_method=None, credit_account=None, description=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, return_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '11818: Payment order return')
        # compare value
        if serial_no:
            self.fo_assert_value('Serial no', self.stock_number_mask(serial_no))
        if return_method:
            self.fo_assert_select('Return method', return_method)
        if credit_account:
            self.fo_assert_text_group('Credit account', self.no_mask(credit_account))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if return_amount:
            self.fo_assert_value('Return amount', return_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_RPO: {transaction_references}')
        serial_no_out=self.fo_get_value('Serial no')
        print(f'F8: Serial no: {serial_no_out}')
        return transaction_references, serial_no_out

    # DPT_CCI: 11806: Gift cheque issued
    def dpt_cci(self, serial_no=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, amount=None, currency=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, purpose=None, debit_method=None, debit_account=None, description=None, issued_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CCI', '11806')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11806: Gift cheque issued')
        # enter value
        if serial_no:
            self.fo_write('Serial no', self.no_mask(serial_no))
            self.wait_loading()
        if expired_date:
            self.fo_write_date('Expired date', expired_date)
        if issuing_name:
            self.fo_write_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_write_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_write_text('Issuer contact number', issuer_contact_number)
        if amount:
            self.fo_write_number('Amount', amount)
        self.key_escape()
        if currency:
            self.fo_select('Currency', currency)
        if beneficiary_name:
            self.fo_write_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_write_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_write_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_write_text('Beneficiary address', beneficiary_address)
        if purpose:
            self.fo_write_text('Purpose', purpose)
        self.key_escape()
        if debit_method:
            self.fo_select('Debit method', debit_method)
        if debit_account:
            self.fo_write_text_group('Debit account', self.no_mask(debit_account))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if issued_date:
            self.fo_assert_date('Issued date', issued_date)
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
            print(f'Transaction references DPT_CCI: {transaction_references}')
            serial_no_out=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_out}')
            return transaction_references, serial_no_out

    def dpt_cci_view(self, transaction_references, serial_no=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, amount=None, currency=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, purpose=None, debit_method=None, debit_account=None, description=None, issued_date=None, expected_posting=None):
        self.transaction_view(transaction_references, '11806: Gift cheque issued')
        # compare value
        if serial_no:
            self.fo_assert_value('Serial no', self.stock_number_mask(serial_no))
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if amount:
            self.fo_assert_value('Amount', amount)
        if currency:
            self.fo_assert_select('Currency', currency)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if purpose:
            self.fo_assert_text('Purpose', purpose)
        if debit_method:
            self.fo_assert_select('Debit method', debit_method)
        if debit_account:
            self.fo_assert_text_group('Debit account', self.no_mask(debit_account))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if issued_date:
            self.fo_assert_date('Issued date', issued_date)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CCI: {transaction_references}')
        serial_no_out=self.fo_get_value('Serial no')
        print(f'F8: Serial no: {serial_no_out}')
        return transaction_references, serial_no_out

    # DPT_CCW: 11807: Gift Cheque withdrawal
    def dpt_ccw(self, serial_no=None, withdrawal_method=None, credit_account=None, description=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, withdrawal_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CCW', '11807')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11807: Gift Cheque withdrawal')
        # enter value
        if serial_no:
            self.fo_write('Serial no', self.no_mask(serial_no))
            self.wait_loading()
        self.key_escape()
        if withdrawal_method:
            self.fo_select('Withdrawal method', withdrawal_method)
        if credit_account:
            self.fo_write_text_group('Credit account', self.no_mask(credit_account))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if withdrawal_amount:
            self.fo_assert_value('Withdrawal amount', withdrawal_amount)
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
            print(f'Transaction references DPT_CCW: {transaction_references}')
            serial_no_out=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_out}')
            return transaction_references, serial_no_out

    def dpt_ccw_view(self, transaction_references, serial_no=None, withdrawal_method=None, credit_account=None, description=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, withdrawal_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '11807: Gift Cheque withdrawal')
        # compare value
        if serial_no:
            self.fo_assert_value('Serial no', self.stock_number_mask(serial_no))
        if withdrawal_method:
            self.fo_assert_select('Withdrawal method', withdrawal_method)
        if credit_account:
            self.fo_assert_text_group('Credit account', self.no_mask(credit_account))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if withdrawal_amount:
            self.fo_assert_value('Withdrawal amount', withdrawal_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CCW: {transaction_references}')
        serial_no_out=self.fo_get_value('Serial no')
        print(f'F8: Serial no: {serial_no_out}')
        return transaction_references, serial_no_out

    # DPT_RCC: 11808: Gift cheque return
    def dpt_rcc(self, serial_no=None, return_method=None, credit_account=None, description=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, return_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_RCC', '11808')
        self.wait_for_button_available('Accept')
        self.assert_form_title('11808: Gift cheque return')
        # enter value
        if serial_no:
            self.fo_write('Serial no', self.no_mask(serial_no))
            self.wait_loading()
        self.key_escape()
        if return_method:
            self.fo_select('Return method', return_method)
        if credit_account:
            self.fo_write_text_group('Credit account', self.no_mask(credit_account))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if return_amount:
            self.fo_assert_value('Return amount', return_amount)
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
            print(f'Transaction references DPT_RCC: {transaction_references}')
            serial_no_out=self.fo_get_value('Serial no')
            print(f'Serial no: {serial_no_out}')
            return transaction_references, serial_no_out

    def dpt_rcc_view(self, transaction_references, serial_no=None, return_method=None, credit_account=None, description=None, expired_date=None, issuing_name=None, issuer_id_number=None, issuer_contact_number=None, beneficiary_name=None, beneficiary_id_number=None, beneficiary_contact_number=None, beneficiary_address=None, currency=None, stock_amount=None, return_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '11808: Gift cheque return')
        # compare value
        if serial_no:
            self.fo_assert_value('Serial no', self.stock_number_mask(serial_no))
        if return_method:
            self.fo_assert_select('Return method', return_method)
        if credit_account:
            self.fo_assert_text_group('Credit account', self.no_mask(credit_account))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expired_date:
            self.fo_assert_date('Expired date', expired_date)
        if issuing_name:
            self.fo_assert_text('Issuing name', issuing_name)
        if issuer_id_number:
            self.fo_assert_text('Issuer ID number', issuer_id_number)
        if issuer_contact_number:
            self.fo_assert_text('Issuer contact number', issuer_contact_number)
        if beneficiary_name:
            self.fo_assert_text('Beneficiary name', beneficiary_name)
        if beneficiary_id_number:
            self.fo_assert_text('Beneficiary ID number', beneficiary_id_number)
        if beneficiary_contact_number:
            self.fo_assert_text('Beneficiary contact number', beneficiary_contact_number)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency:
            self.fo_assert_select('Currency', currency)
        if stock_amount:
            self.fo_assert_value('Stock amount', stock_amount)
        if return_amount:
            self.fo_assert_value('Return amount', return_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_RCC: {transaction_references}')
        serial_no_out=self.fo_get_value('Serial no')
        print(f'F8: Serial no: {serial_no_out}')
        return transaction_references, serial_no_out
