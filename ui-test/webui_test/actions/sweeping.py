from webui_test.case import *

class SweepingActions(TestCase):

# -------------------------- handle FO - SWEEPING --------------------------
    # DPT_OPSW: DPT - Create Sweeping
    def dpt_opsw(self, sweeping_mode=None, from_date=None, to_date=None, master_account=None, sweeping_type=None, surplus_account=None, surplus_amount=None, deficit_account=None, deficit_amount=None, description=None, fee_collect_method=None, account_number_for_fee=None, master_account_name=None, surplus_account_name=None, deficit_account_name=None, created_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_OPSW', 'Create Sweeping')
        self.wait_for_button_available('Reload Auto Fee')
        self.click_button('Reload Auto Fee')
        self.wait_loading()
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT - Create Sweeping')
        # enter value
        self.key_escape()
        if sweeping_mode:
            self.fo_select('Sweeping mode', sweeping_mode)
        if from_date:
            self.fo_write_date('From Date', from_date)
        if to_date:
            self.fo_write_date('To Date', to_date)
        if master_account:
            self.fo_write('Master account', str(master_account).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if sweeping_type:
            self.fo_select('Sweeping type', sweeping_type)
            self.wait_loading()
        if surplus_account:
            self.fo_write('Surplus account', str(surplus_account).replace('-', ''))
            self.wait_loading()
        if surplus_amount:
            self.fo_write_number('Surplus Amount', surplus_amount)
        if deficit_account:
            self.fo_write('Deficit account', str(deficit_account).replace('-', ''))
            self.wait_loading()
        if deficit_amount:
            self.fo_write_number('Deficit Amount', deficit_amount)
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
        if master_account_name:
            self.fo_assert_text('Master account name', master_account_name)
        if surplus_account_name:
            self.fo_assert_text('Surplus account', surplus_account_name)
        if deficit_account_name:
            self.fo_assert_text('Deficit account name', deficit_account_name)
        if created_date:
            self.fo_assert_date('Created Date', created_date)
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
            print(f'Transaction references DPT_OPSW: {transaction_references}')
            sweeping_mode_out=self.fo_get_select('Sweeping mode')
            print(f'Sweeping mode: {sweeping_mode_out}')
            master_account_out=self.fo_get_value('Master account')
            print(f'Master account: {master_account_out}')
            surplus_account_out=self.fo_get_value('Surplus account')
            print(f'Surplus account: {surplus_account_out}')
            deficit_account_out=self.fo_get_value('Deficit account')
            print(f'Deficit account: {deficit_account_out}')
            return transaction_references, sweeping_mode_out, master_account_out, surplus_account_out, deficit_account_out

    def dpt_opsw_view(self, transaction_references, sweeping_mode=None, from_date=None, to_date=None, master_account=None, sweeping_type=None, surplus_account=None, surplus_amount=None, deficit_account=None, deficit_amount=None, description=None, fee_collect_method=None, account_number_for_fee=None, master_account_name=None, surplus_account_name=None, deficit_account_name=None, created_date=None, expected_posting=None):
        self.transaction_view(transaction_references, 'DPT - Create Sweeping')
        # compare value
        if sweeping_mode:
            self.fo_assert_select('Sweeping mode', sweeping_mode)
        if from_date:
            self.fo_assert_date('From Date', from_date)
        if to_date:
            self.fo_assert_date('To Date', to_date)
        if master_account:
            self.fo_assert_value('Master account', self.deposit_account_number_mask(master_account))
        if sweeping_type:
            self.fo_assert_select('Sweeping type', sweeping_type)
        if surplus_account:
            self.fo_assert_value('Surplus account', self.deposit_account_number_mask(surplus_account))
        if surplus_amount:
            self.fo_assert_value('Surplus Amount', surplus_amount)
        if deficit_account:
            self.fo_assert_value('Deficit account', self.deposit_account_number_mask(deficit_account))
        if deficit_amount:
            self.fo_assert_value('Deficit Amount', deficit_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', account_number_for_fee)
        if master_account_name:
            self.fo_assert_text('Master account name', master_account_name)
        if surplus_account_name:
            self.fo_assert_text('Surplus account', surplus_account_name)
        if deficit_account_name:
            self.fo_assert_text('Deficit account name', deficit_account_name)
        if created_date:
            self.fo_assert_date('Created Date', created_date)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_OPSW: {transaction_references}')
        sweeping_mode_out=self.fo_get_select('Sweeping mode')
        print(f'F8: Sweeping mode: {sweeping_mode_out}')
        master_account_out=self.fo_get_value('Master account')
        print(f'F8: Master account: {master_account_out}')
        surplus_account_out=self.fo_get_value('Surplus account')
        print(f'F8: Surplus account: {surplus_account_out}')
        deficit_account_out=self.fo_get_value('Deficit account')
        print(f'F8: Deficit account: {deficit_account_out}')
        return transaction_references, sweeping_mode_out, master_account_out, surplus_account_out, deficit_account_out

    # DPT_MSW: DPT - Modify Sweeping
    def dpt_msw(self, sweeping_status_active=None, from_date=None, to_date=None, master_account=None, description=None, fee_collect_method=None, account_number_for_fee=None, sweeping_mode=None, master_account_name=None, sweeping_type=None, surplus_account=None, surplus_account_name=None, surplus_amount=None, deficit_account=None, deficit_account_name=None, deficit_amount=None, created_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_MSW', 'Modify sweeping')
        self.wait_for_button_available('Reload Auto Fee')
        self.click_button('Reload Auto Fee')
        self.wait_loading()
        self.wait_for_button_available('Accept')
        self.assert_form_title('DPT - Modify Sweeping')
        # enter value
        if sweeping_status_active is None or sweeping_status_active == '':
            sweeping_status_active = False
        if sweeping_status_active:
            self.fo_click_checkbox('Sweeping status - Active')
        if from_date:
            self.fo_write_date('From Date', from_date)
        if to_date:
            self.fo_write_date('To Date', to_date)
        if master_account:
            self.fo_write('Master account', str(master_account).replace('-', ''))
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
        if sweeping_mode:
            self.fo_assert_select('Sweeping mode', sweeping_mode)
        if master_account_name:
            self.fo_assert_text('Master account name', master_account_name)
        if sweeping_type:
            self.fo_assert_select('Sweeping type', sweeping_type)
        if surplus_account:
            self.fo_assert_value('Surplus account', self.deposit_account_number_mask(surplus_account))
        if surplus_account_name:
            self.fo_assert_text('Surplus account', surplus_account_name)
        if surplus_amount:
            self.fo_assert_value('Surplus Amount', surplus_amount)
        if deficit_account:
            self.fo_assert_value('Deficit account', self.deposit_account_number_mask(deficit_account))
        if deficit_account_name:
            self.fo_assert_text('Deficit account name', deficit_account_name)
        if deficit_amount:
            self.fo_assert_value('Deficit Amount', deficit_amount)
        if created_date:
            self.fo_assert_date('Created Date', created_date)
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
            print(f'Transaction references DPT_MSW: {transaction_references}')
            master_account_out=self.fo_get_value('Master account')
            print(f'Master account: {master_account_out}')
            return transaction_references, master_account_out

    def dpt_msw_view(self, transaction_references, sweeping_status_active=None, from_date=None, to_date=None, master_account=None, description=None, fee_collect_method=None, account_number_for_fee=None, sweeping_mode=None, master_account_name=None, sweeping_type=None, surplus_account=None, surplus_account_name=None, surplus_amount=None, deficit_account=None, deficit_account_name=None, deficit_amount=None, created_date=None, expected_posting=None):
        self.transaction_view(transaction_references, 'DPT - Modify Sweeping')
        # compare value
        if sweeping_status_active is None or sweeping_status_active == '':
            sweeping_status_active = False
        if sweeping_status_active is not None or sweeping_status_active != '':
            self.fo_assert_checkbox('Sweeping status - Active', sweeping_status_active)
        if from_date:
            self.fo_assert_date('From Date', from_date)
        if to_date:
            self.fo_assert_date('To Date', to_date)
        if master_account:
            self.fo_assert_value('Master account', self.deposit_account_number_mask(master_account))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', account_number_for_fee)
        if sweeping_mode:
            self.fo_assert_select('Sweeping mode', sweeping_mode)
        if master_account_name:
            self.fo_assert_text('Master account name', master_account_name)
        if sweeping_type:
            self.fo_assert_select('Sweeping type', sweeping_type)
        if surplus_account:
            self.fo_assert_value('Surplus account', self.deposit_account_number_mask(surplus_account))
        if surplus_account_name:
            self.fo_assert_text('Surplus account', surplus_account_name)
        if surplus_amount:
            self.fo_assert_value('Surplus Amount', surplus_amount)
        if deficit_account:
            self.fo_assert_value('Deficit account', self.deposit_account_number_mask(deficit_account))
        if deficit_account_name:
            self.fo_assert_text('Deficit account name', deficit_account_name)
        if deficit_amount:
            self.fo_assert_value('Deficit Amount', deficit_amount)
        if created_date:
            self.fo_assert_date('Created Date', created_date)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_MSW: {transaction_references}')
        master_account_out=self.fo_get_value('Master account')
        print(f'F8: Master account: {master_account_out}')
        return transaction_references, master_account_out
