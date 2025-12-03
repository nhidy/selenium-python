from webui_test.case import *

class OverdraftActions(TestCase):

# -------------------------- handle FO - OVERDRAFT --------------------------
    # DPT_ODO: 1101: Create overdraft contract
    def dpt_odo(self, account_number=None, sub_product_limit_code=None, od_catalog_code=None, credit_classification=None, margin=None, account_holder_name=None, od_include_minimum_balance=None, interest_due_mode=None, od_limit=None, effective_date=None, expire_date=None, contract_number=None, account_holding_branch_name=None, customer_type=None, customer_code=None, deposit_catalogue_code=None, minimum_balance=None, interest_rate=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_ODO', '1101')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1101: Create overdraft contract')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if sub_product_limit_code:
            self.fo_write_group('Sub product limit code', str(sub_product_limit_code).replace('-', ''))
            self.wait_loading()
        if od_catalog_code:
            self.fo_write_group('Od Catalog code', od_catalog_code)
            self.wait_loading()
        self.key_escape()
        if credit_classification:
            self.fo_select('Credit classification', credit_classification)
        if margin:
            self.fo_write_number('Margin', margin)
        if account_holder_name:
            self.fo_write_text('Account holder name', account_holder_name)
        self.key_escape()
        if od_include_minimum_balance:
            self.fo_select('OD include minimum balance', od_include_minimum_balance)
        self.key_escape()
        if interest_due_mode:
            self.fo_select('Interest due mode', interest_due_mode)
        if od_limit:
            self.fo_write_number('OD limit', od_limit)
        if effective_date:
            self.fo_write_date('Effective date', effective_date)
        if expire_date:
            self.fo_write_date('Expire date', expire_date)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if contract_number:
            self.fo_assert_value_group('Contract number', self.deposit_account_number_mask(contract_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if deposit_catalogue_code:
            self.fo_assert_text_group('Deposit catalogue code', deposit_catalogue_code)
        if minimum_balance:
            self.fo_assert_value('Minimum balance', minimum_balance)
        if interest_rate:
            self.fo_assert_value('Interest rate', interest_rate)
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
            print(f'Transaction references DPT_ODO: {transaction_references}')
            contract_number_out=self.fo_get_value_group('Contract number')
            print(f'Contract number: {contract_number_out}')
            return transaction_references, contract_number_out

    def dpt_odo_view(self, transaction_references, account_number=None, sub_product_limit_code=None, od_catalog_code=None, credit_classification=None, margin=None, account_holder_name=None, od_include_minimum_balance=None, interest_due_mode=None, od_limit=None, effective_date=None, expire_date=None, contract_number=None, account_holding_branch_name=None, customer_type=None, customer_code=None, deposit_catalogue_code=None, minimum_balance=None, interest_rate=None, expected_posting=None):
        self.transaction_view(transaction_references, '1101: Create overdraft contract')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if sub_product_limit_code:
            self.fo_assert_value_group('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if od_catalog_code:
            self.fo_assert_value_group('Od Catalog code', od_catalog_code)
        if credit_classification:
            self.fo_assert_select('Credit classification', credit_classification)
        if margin:
            self.fo_assert_value('Margin', margin)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if od_include_minimum_balance:
            self.fo_assert_select('OD include minimum balance', od_include_minimum_balance)
        if interest_due_mode:
            self.fo_assert_select('Interest due mode', interest_due_mode)
        if od_limit:
            self.fo_assert_value('OD limit', od_limit)
        if effective_date:
            self.fo_assert_date('Effective date', effective_date)
        if expire_date:
            self.fo_assert_date('Expire date', expire_date)
        if contract_number:
            self.fo_assert_value_group('Contract number', self.deposit_account_number_mask(contract_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if deposit_catalogue_code:
            self.fo_assert_text_group('Deposit catalogue code', deposit_catalogue_code)
        if minimum_balance:
            self.fo_assert_value('Minimum balance', minimum_balance)
        if interest_rate:
            self.fo_assert_value('Interest rate', interest_rate)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_ODO: {transaction_references}')
        contract_number_out=self.fo_get_value_group('Contract number')
        print(f'F8: Contract number: {contract_number_out}')
        return transaction_references, contract_number_out

    # DPT_ODA: Approve overdraft contract
    def dpt_oda(self, contract_number=None, customer_type=None, account_holding_branch_name=None, holder_name=None, od_catalogue_code=None, od_catalogue_name=None, credit_classification=None, currency_code=None, od_limit=None, interest_rate=None, deposit_account=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_ODA', 'Approve overdraft')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Approve overdraft contract')
        # enter value
        if contract_number:
            self.fo_write('Contract number', str(contract_number).replace('-', ''))
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if holder_name:
            self.fo_assert_text('Holder name', holder_name)
        if od_catalogue_code:
            self.fo_assert_text('Od catalogue code', od_catalogue_code)
        if od_catalogue_name:
            self.fo_assert_text('Od catalogue name', od_catalogue_name)
        if credit_classification:
            self.fo_assert_select('Credit classification', credit_classification)
        if currency_code:
            self.fo_assert_text('Currency code', currency_code)
        if od_limit:
            self.fo_assert_value('Od limit', od_limit)
        if interest_rate:
            self.fo_assert_value('Interest rate', interest_rate)
        if deposit_account:
            self.fo_assert_value('Deposit account', self.deposit_account_number_mask(deposit_account))
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
            print(f'Transaction references DPT_ODA: {transaction_references}')
            contract_number_out=self.fo_get_value('Contract number')
            print(f'Contract number: {contract_number_out}')
            return transaction_references, contract_number_out

    def dpt_oda_view(self, transaction_references, contract_number=None, customer_type=None, account_holding_branch_name=None, holder_name=None, od_catalogue_code=None, od_catalogue_name=None, credit_classification=None, currency_code=None, od_limit=None, interest_rate=None, deposit_account=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Approve overdraft contract')
        # compare value
        if contract_number:
            self.fo_assert_value('Contract number', self.credit_account_number_mask(contract_number))
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if holder_name:
            self.fo_assert_text('Holder name', holder_name)
        if od_catalogue_code:
            self.fo_assert_text('Od catalogue code', od_catalogue_code)
        if od_catalogue_name:
            self.fo_assert_text('Od catalogue name', od_catalogue_name)
        if credit_classification:
            self.fo_assert_select('Credit classification', credit_classification)
        if currency_code:
            self.fo_assert_text('Currency code', currency_code)
        if od_limit:
            self.fo_assert_value('Od limit', od_limit)
        if interest_rate:
            self.fo_assert_value('Interest rate', interest_rate)
        if deposit_account:
            self.fo_assert_value('Deposit account', self.deposit_account_number_mask(deposit_account))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_ODA: {transaction_references}')
        contract_number_out=self.fo_get_value('Contract number')
        print(f'F8: Contract number: {contract_number_out}')
        return transaction_references, contract_number_out

    # DPT_REJ_OD: Reject overdraft contract
    def dpt_rej_od(self, contract_number=None, customer_type=None, account_holding_branch_name=None, holder_name=None, od_catalogue_code=None, od_catalogue_name=None, currency_code=None, od_limit=None, deposit_account=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_REJ_OD', 'Reject overdraft')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Reject overdraft contract')
        # enter value
        if contract_number:
            self.fo_write('Contract number', str(contract_number).replace('-', ''))
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if holder_name:
            self.fo_assert_text('Holder name', holder_name)
        if od_catalogue_code:
            self.fo_assert_text('Od catalogue code', od_catalogue_code)
        if od_catalogue_name:
            self.fo_assert_text('Od catalogue name', od_catalogue_name)
        if currency_code:
            self.fo_assert_text('Currency code', currency_code)
        if od_limit:
            self.fo_assert_value('Od limit', od_limit)
        if deposit_account:
            self.fo_assert_value('Deposit account', self.deposit_account_number_mask(deposit_account))
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
            print(f'Transaction references DPT_REJ_OD: {transaction_references}')
            contract_number_out=self.fo_get_value('Contract number')
            print(f'Contract number: {contract_number_out}')
            return transaction_references, contract_number_out

    def dpt_rej_od_view(self, transaction_references, contract_number=None, customer_type=None, account_holding_branch_name=None, holder_name=None, od_catalogue_code=None, od_catalogue_name=None, currency_code=None, od_limit=None, deposit_account=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Reject overdraft contract')
        # compare value
        if contract_number:
            self.fo_assert_value('Contract number', self.credit_account_number_mask(contract_number))
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if holder_name:
            self.fo_assert_text('Holder name', holder_name)
        if od_catalogue_code:
            self.fo_assert_text('Od catalogue code', od_catalogue_code)
        if od_catalogue_name:
            self.fo_assert_text('Od catalogue name', od_catalogue_name)
        if currency_code:
            self.fo_assert_text('Currency code', currency_code)
        if od_limit:
            self.fo_assert_value('Od limit', od_limit)
        if deposit_account:
            self.fo_assert_value('Deposit account', self.deposit_account_number_mask(deposit_account))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_REJ_OD: {transaction_references}')
        contract_number_out=self.fo_get_value('Contract number')
        print(f'F8: Contract number: {contract_number_out}')
        return transaction_references, contract_number_out

    # DPT_ADJ_LIMIT_OD: Overdraft limit adjustment
    def dpt_adj_limit_od(self, contract_number=None, adjustment_limit=None, description=None, current_overdraft_limit=None, new_overdraft_limit=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_ADJ_LIMIT_OD', 'adjustment')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Overdraft limit adjustment')
        # enter value
        if contract_number:
            self.fo_write('Contract number', str(contract_number).replace('-', ''))
            self.wait_loading()
        if adjustment_limit:
            self.fo_write_number('Adjustment limit', adjustment_limit)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if current_overdraft_limit:
            self.fo_assert_value('Current overdraft limit', current_overdraft_limit)
        if new_overdraft_limit:
            self.fo_assert_value('New overdraft limit', new_overdraft_limit)
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
            print(f'Transaction references DPT_ADJ_LIMIT_OD: {transaction_references}')
            contract_number_out=self.fo_get_value('Contract number')
            print(f'Contract number: {contract_number_out}')
            return transaction_references, contract_number_out

    def dpt_adj_limit_od_view(self, transaction_references, contract_number=None, adjustment_limit=None, description=None, current_overdraft_limit=None, new_overdraft_limit=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Overdraft limit adjustment')
        # compare value
        if contract_number:
            self.fo_assert_value('Contract number', self.credit_account_number_mask(contract_number))
        if adjustment_limit:
            self.fo_assert_value('Adjustment limit', adjustment_limit)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if current_overdraft_limit:
            self.fo_assert_value('Current overdraft limit', current_overdraft_limit)
        if new_overdraft_limit:
            self.fo_assert_value('New overdraft limit', new_overdraft_limit)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_ADJ_LIMIT_OD: {transaction_references}')
        contract_number_out=self.fo_get_value('Contract number')
        print(f'F8: Contract number: {contract_number_out}')
        return transaction_references, contract_number_out

    # DPT_EXT_TENOR_OD: Overdraft extend tenor
    def dpt_ext_tenor_od(self, contract_number=None, new_expire_date=None, description=None, old_expire_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_EXT_TENOR_OD', 'extend')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Overdraft extend tenor')
        # enter value
        if contract_number:
            self.fo_write('Contract number', str(contract_number).replace('-', ''))
            self.wait_loading()
        if new_expire_date:
            self.fo_write_date('New expire date', new_expire_date)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if old_expire_date:
            self.fo_assert_date('Old expire date', old_expire_date)
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
            print(f'Transaction references DPT_EXT_TENOR_OD: {transaction_references}')
            contract_number_out=self.fo_get_value('Contract number')
            print(f'Contract number: {contract_number_out}')
            return transaction_references, contract_number_out

    def dpt_ext_tenor_od_view(self, transaction_references, contract_number=None, new_expire_date=None, description=None, old_expire_date=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Overdraft extend tenor')
        # compare value
        if contract_number:
            self.fo_assert_value('Contract number', self.credit_account_number_mask(contract_number))
        if new_expire_date:
            self.fo_assert_date('New expire date', new_expire_date)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if old_expire_date:
            self.fo_assert_date('Old expire date', old_expire_date)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_EXT_TENOR_OD: {transaction_references}')
        contract_number_out=self.fo_get_value('Contract number')
        print(f'F8: Contract number: {contract_number_out}')
        return transaction_references, contract_number_out

    # DPT_IAJ_OD: Adjust overdraft interest and fee
    def dpt_iaj_od(self, contract_number=None, ifc_code=None, adjustment_amount=None, description=None, customer_code=None, account_name=None, current_ifc_amount=None, ifc_type=None, new_ifc_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_IAJ_OD', 'Adjust overdraft interest and fee')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Adjust overdraft interest and fee')
        # enter value
        if contract_number:
            self.fo_write_group('Contract number', str(contract_number).replace('-', ''))
            self.wait_loading()
        if ifc_code:
            self.fo_write_text_group('IFC code', ifc_code)
            self.wait_loading()
        if adjustment_amount:
            self.fo_write_number('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if current_ifc_amount:
            self.fo_assert_value('Current IFC amount', current_ifc_amount)
        if ifc_type:
            self.fo_assert_select('IFC Type', ifc_type)
        if new_ifc_amount:
            self.fo_assert_value('New ifc amount', new_ifc_amount)
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
            print(f'Transaction references DPT_IAJ_OD: {transaction_references}')
            contract_number_out=self.fo_get_value_group('Contract number')
            print(f'Contract number: {contract_number_out}')
            return transaction_references, contract_number_out

    def dpt_iaj_od_view(self, transaction_references, contract_number=None, ifc_code=None, adjustment_amount=None, description=None, customer_code=None, account_name=None, current_ifc_amount=None, ifc_type=None, new_ifc_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Adjust overdraft interest and fee')
        # compare value
        if contract_number:
            self.fo_assert_value_group('Contract number', self.credit_account_number_mask(contract_number))
        if ifc_code:
            self.fo_assert_text_group('IFC code', ifc_code)
        if adjustment_amount:
            self.fo_assert_value('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if current_ifc_amount:
            self.fo_assert_value('Current IFC amount', current_ifc_amount)
        if ifc_type:
            self.fo_assert_select('IFC Type', ifc_type)
        if new_ifc_amount:
            self.fo_assert_value('New ifc amount', new_ifc_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_IAJ_OD: {transaction_references}')
        contract_number_out=self.fo_get_value_group('Contract number')
        print(f'F8: Contract number: {contract_number_out}')
        return transaction_references, contract_number_out

    # DPT_NPL_OD: OD-NPL Processing
    def dpt_npl_od(self, overdraft_contract=None, new_group=None, description=None, current_group=None, overdraft_balance=None, payable_interest_amount=None, commitment_fee=None, penalty_interest=None, penalty_principal=None, secure_amount=None, shortfall_amount=None, current_provision_amount=None, new_provision_amount=None, overdraft_contract_currency=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_NPL_OD', 'NPL')
        self.wait_for_button_available('Accept')
        self.assert_form_title('OD-NPL Processing')
        # enter value
        if overdraft_contract:
            self.fo_write('Overdraft contract', str(overdraft_contract).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if new_group:
            self.fo_select('New group', new_group)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if current_group:
            self.fo_assert_select('Current group', current_group)
        if overdraft_balance:
            self.fo_assert_value('Overdraft balance', overdraft_balance)
        if payable_interest_amount:
            self.fo_assert_value('Payable interest amount', payable_interest_amount)
        if commitment_fee:
            self.fo_assert_value('Commitment fee', commitment_fee)
        if penalty_interest:
            self.fo_assert_value('Penalty Interest', penalty_interest)
        if penalty_principal:
            self.fo_assert_value('Penalty principal', penalty_principal)
        if secure_amount:
            self.fo_assert_value('Secure amount', secure_amount)
        if shortfall_amount:
            self.fo_assert_value('Shortfall amount', shortfall_amount)
        if current_provision_amount:
            self.fo_assert_value('Current provision amount', current_provision_amount)
        if new_provision_amount:
            self.fo_assert_value('New provision amount', new_provision_amount)
        if overdraft_contract_currency:
            self.fo_assert_select('Overdraft contract currency', overdraft_contract_currency)
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
            print(f'Transaction references DPT_NPL_OD: {transaction_references}')
            overdraft_contract_out=self.fo_get_value('Overdraft contract')
            print(f'Overdraft contract: {overdraft_contract_out}')
            return transaction_references, overdraft_contract_out

    def dpt_npl_od_view(self, transaction_references, overdraft_contract=None, new_group=None, description=None, current_group=None, overdraft_balance=None, payable_interest_amount=None, commitment_fee=None, penalty_interest=None, penalty_principal=None, secure_amount=None, shortfall_amount=None, current_provision_amount=None, new_provision_amount=None, overdraft_contract_currency=None, expected_posting=None):
        self.transaction_view(transaction_references, 'OD-NPL Processing')
        # compare value
        if overdraft_contract:
            self.fo_assert_value('Overdraft contract', self.credit_account_number_mask(overdraft_contract))
        if new_group:
            self.fo_assert_select('New group', new_group)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if current_group:
            self.fo_assert_select('Current group', current_group)
        if overdraft_balance:
            self.fo_assert_value('Overdraft balance', overdraft_balance)
        if payable_interest_amount:
            self.fo_assert_value('Payable interest amount', payable_interest_amount)
        if commitment_fee:
            self.fo_assert_value('Commitment fee', commitment_fee)
        if penalty_interest:
            self.fo_assert_value('Penalty Interest', penalty_interest)
        if penalty_principal:
            self.fo_assert_value('Penalty principal', penalty_principal)
        if secure_amount:
            self.fo_assert_value('Secure amount', secure_amount)
        if shortfall_amount:
            self.fo_assert_value('Shortfall amount', shortfall_amount)
        if current_provision_amount:
            self.fo_assert_value('Current provision amount', current_provision_amount)
        if new_provision_amount:
            self.fo_assert_value('New provision amount', new_provision_amount)
        if overdraft_contract_currency:
            self.fo_assert_select('Overdraft contract currency', overdraft_contract_currency)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_NPL_OD: {transaction_references}')
        overdraft_contract_out=self.fo_get_value('Overdraft contract')
        print(f'F8: Overdraft contract: {overdraft_contract_out}')
        return transaction_references, overdraft_contract_out

    # DPT_CAS_OD: Change Overdraft Contract Status
    def dpt_cas_od(self, contract_number=None, new_status=None, description=None, account_holding_branch_name=None, current_status=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_CAS_OD', 'Change Overdraft Contract Status')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Change Overdraft Contract Status')
        # enter value
        if contract_number:
            self.fo_write_group('Contract Number', str(contract_number).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if new_status:
            self.fo_select('New status', new_status)
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if current_status:
            self.fo_assert_select('Current status', current_status)
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
            print(f'Transaction references DPT_CAS_OD: {transaction_references}')
            contract_number_out=self.fo_get_value_group('Contract Number')
            print(f'Contract Number: {contract_number_out}')
            return transaction_references, contract_number_out

    def dpt_cas_od_view(self, transaction_references, contract_number=None, new_status=None, description=None, account_holding_branch_name=None, current_status=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Change Overdraft Contract Status')
        # compare value
        if contract_number:
            self.fo_assert_value_group('Contract Number', self.credit_account_number_mask(contract_number))
        if new_status:
            self.fo_assert_select('New status', new_status)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if current_status:
            self.fo_assert_select('Current status', current_status)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_CAS_OD: {transaction_references}')
        contract_number_out=self.fo_get_value_group('Contract Number')
        print(f'F8: Contract Number: {contract_number_out}')
        return transaction_references, contract_number_out

    # DPT_DOD: 1194: Close OD Facility by Transfer
    def dpt_dod(self, contract_number=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, deposit_account_number=None, account_holding_branch_name=None, deposit_balance=None, interest_accrual=None, commitment_fee_accrual=None, penalty_interest_accrual=None, penalty_principal_accrual=None, overdraft_balance=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_DOD', '1194')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1194: Close OD Facility by Transfer')
        # enter value
        if contract_number:
            self.fo_write('Contract number', str(contract_number).replace('-', ''))
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
        if depositor_address:
            self.fo_write_text('Depositor address', depositor_address)
        if mobile_phone:
            self.fo_click_collap('Depositor description')
            self.fo_write_text_multi('Depositor description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Depositor description')
            self.fo_write_text_multi('Depositor description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if deposit_account_number:
            self.fo_assert_value_group('Deposit account number', self.deposit_account_number_mask(deposit_account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if deposit_balance:
            self.fo_assert_value('Deposit balance', deposit_balance)
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if commitment_fee_accrual:
            self.fo_assert_value('Commitment fee accrual', commitment_fee_accrual)
        if penalty_interest_accrual:
            self.fo_assert_value('Penalty interest accrual', penalty_interest_accrual)
        if penalty_principal_accrual:
            self.fo_assert_value('Penalty principal accrual', penalty_principal_accrual)
        if overdraft_balance:
            self.fo_assert_value('Overdraft balance', overdraft_balance)
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
            print(f'Transaction references DPT_DOD: {transaction_references}')
            contract_number_out=self.fo_get_value('Contract number')
            print(f'Contract number: {contract_number_out}')
            return transaction_references, contract_number_out

    def dpt_dod_view(self, transaction_references, contract_number=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, description=None, deposit_account_number=None, account_holding_branch_name=None, deposit_balance=None, interest_accrual=None, commitment_fee_accrual=None, penalty_interest_accrual=None, penalty_principal_accrual=None, overdraft_balance=None, expected_posting=None):
        self.transaction_view(transaction_references, '1194: Close OD Facility by Transfer')
        # compare value
        if contract_number:
            self.fo_assert_value('Contract number', self.credit_account_number_mask(contract_number))
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
        if depositor_address:
            self.fo_assert_text('Depositor address', depositor_address)
        if mobile_phone:
            self.fo_click_collap('Depositor description')
            self.fo_assert_text_multi('Depositor description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Depositor description')
            self.fo_assert_text_multi('Depositor description', 'NRC', nrc)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if deposit_account_number:
            self.fo_assert_value_group('Deposit account number', self.deposit_account_number_mask(deposit_account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if deposit_balance:
            self.fo_assert_value('Deposit balance', deposit_balance)
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if commitment_fee_accrual:
            self.fo_assert_value('Commitment fee accrual', commitment_fee_accrual)
        if penalty_interest_accrual:
            self.fo_assert_value('Penalty interest accrual', penalty_interest_accrual)
        if penalty_principal_accrual:
            self.fo_assert_value('Penalty principal accrual', penalty_principal_accrual)
        if overdraft_balance:
            self.fo_assert_value('Overdraft balance', overdraft_balance)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_DOD: {transaction_references}')
        contract_number_out=self.fo_get_value('Contract number')
        print(f'F8: Contract number: {contract_number_out}')
        return transaction_references, contract_number_out

    # DPT_COG: 1196: Close OD Facility by GL
    def dpt_cog(self, contract_number=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, accounting_number=None, description=None, account_number=None, account_holding_branch_name=None, deposit_balance=None, interest_accrual=None, commitment_fee_accrual=None, penalty_interest_accrual=None, penalty_principal_accrual=None, overdraft_balance=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('DPT_COG', '1196')
        self.wait_for_button_available('Accept')
        self.assert_form_title('1196: Close OD Facility by GL')
        # enter value
        if contract_number:
            self.fo_write('Contract number ', str(contract_number).replace('-', ''))
            self.wait_loading()
        if depositor_name:
            self.fo_write_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_write('Depositor id', depositor_id)
        if depositor_address:
            self.fo_write_text('Depositor address', depositor_address)
        if mobile_phone:
            self.fo_click_collap('Depositor description')
            self.fo_write_text_multi('Depositor description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Depositor description')
            self.fo_write_text_multi('Depositor description', 'NRC', nrc)
        if accounting_number:
            self.fo_write_group('Accounting number', str(accounting_number).replace('-', ''))
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
        if deposit_balance:
            self.fo_assert_value('Deposit balance', deposit_balance)
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if commitment_fee_accrual:
            self.fo_assert_value('Commitment fee accrual', commitment_fee_accrual)
        if penalty_interest_accrual:
            self.fo_assert_value('Penalty interest accrual', penalty_interest_accrual)
        if penalty_principal_accrual:
            self.fo_assert_value('Penalty principal accrual', penalty_principal_accrual)
        if overdraft_balance:
            self.fo_assert_value('Overdraft balance', overdraft_balance)
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
            print(f'Transaction references DPT_COG: {transaction_references}')
            contract_number_out=self.fo_get_value('Contract number ')
            print(f'Contract number : {contract_number_out}')
            accounting_number_out=self.fo_get_value_group('Accounting number')
            print(f'Accounting number: {accounting_number_out}')
            return transaction_references, contract_number_out, accounting_number_out

    def dpt_cog_view(self, transaction_references, contract_number=None, depositor_name=None, depositor_id=None, depositor_address=None, mobile_phone=None, nrc=None, accounting_number=None, description=None, account_number=None, account_holding_branch_name=None, deposit_balance=None, interest_accrual=None, commitment_fee_accrual=None, penalty_interest_accrual=None, penalty_principal_accrual=None, overdraft_balance=None, expected_posting=None):
        self.transaction_view(transaction_references, '1196: Close OD Facility by GL')
        # compare value
        if contract_number:
            self.fo_assert_value('Contract number ', self.credit_account_number_mask(contract_number))
        if depositor_name:
            self.fo_assert_text('Depositor name', depositor_name)
        if depositor_id:
            self.fo_assert_value('Depositor id', self.customer_code_mask(depositor_id))
        if depositor_address:
            self.fo_assert_text('Depositor address', depositor_address)
        if mobile_phone:
            self.fo_click_collap('Depositor description')
            self.fo_assert_text_multi('Depositor description', 'Mobile phone', mobile_phone)
        if nrc:
            self.fo_click_collap('Depositor description')
            self.fo_assert_text_multi('Depositor description', 'NRC', nrc)
        if accounting_number:
            self.fo_assert_value_group('Accounting number', self.gl_account_number_mask(accounting_number))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_number:
            self.fo_assert_value_group('Account number', self.deposit_account_number_mask(account_number))
        if account_holding_branch_name:
            self.fo_assert_text('Account holding branch name', account_holding_branch_name)
        if deposit_balance:
            self.fo_assert_value('Deposit balance', deposit_balance)
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if commitment_fee_accrual:
            self.fo_assert_value('Commitment fee accrual', commitment_fee_accrual)
        if penalty_interest_accrual:
            self.fo_assert_value('Penalty interest accrual', penalty_interest_accrual)
        if penalty_principal_accrual:
            self.fo_assert_value('Penalty principal accrual', penalty_principal_accrual)
        if overdraft_balance:
            self.fo_assert_value('Overdraft balance', overdraft_balance)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references DPT_COG: {transaction_references}')
        contract_number_out=self.fo_get_value('Contract number ')
        print(f'F8: Contract number : {contract_number_out}')
        accounting_number_out=self.fo_get_value_group('Accounting number')
        print(f'F8: Accounting number: {accounting_number_out}')
        return transaction_references, contract_number_out, accounting_number_out

# -------------------------- handle BO - OVERDRAFT --------------------------
    # DPT-OD Catalogue Definition
    def overdraft_catalogue_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'OD Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-OD Catalogue Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def overdraft_catalogue_definition_advanced_search(self, catalogue_code=None, catalogue_name=None, currency=None, credit_type=None, tenor_type=None, status=None):
        self.close_all_form()
        self.click_menu('Deposit', 'OD Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-OD Catalogue Definition-Search')
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.adv_search_text('Catalogue name', catalogue_name)
        if currency:
            self.adv_search_text('Currency', currency)
        self.key_escape()
        if credit_type:
            self.adv_search_select('Credit type', credit_type)
        self.key_escape()
        if tenor_type:
            self.adv_search_select('Tenor type', tenor_type)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def overdraft_catalogue_definition_add(self, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, ifc_codes=None, sys_account_names=None, account_aliass=None, coa_accounts=None, replace_bys=None, system_account_names=None, business_lines=None, customer_sectors=None, customer_resident_statuss=None, sub_products=None, bank_identifications=None, replace_code=None, email=None, push_notification=None, sms=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Deposit', 'OD Catalogue Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('DPT-OD Catalogue Definition-Add')
        # enter value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_write('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        self.key_escape()
        if secure_type:
            self.bo_select('Secure type', secure_type)
        if secure_rate:
            self.bo_write_number('Secure rate', secure_rate)
        self.key_escape()
        if secured_by_currency:
            self.bo_select('Secured by currency', secured_by_currency)
        self.key_escape()
        if credit_sub_type:
            self.bo_select('Credit sub type', credit_sub_type)
        self.key_escape()
        if tenor_type:
            self.bo_select('Tenor type', tenor_type)
        self.key_escape()
        if credit_purpose:
            self.bo_select('Credit purpose', credit_purpose)
        self.key_escape()
        if credit_classification:
            self.bo_select('Credit classification', credit_classification)
        self.key_escape()
        if is_provision:
            self.bo_select('Is provision?', is_provision)
        self.key_escape()
        if classification_option:
            self.bo_select('Classification option', classification_option)
        self.key_escape()
        if status:
            self.bo_select('Status', status)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_write_number_group('Principal collection tenor', principal_collection_tenor)
        self.key_escape()
        if principal_collection_tenor_unit:
            self.bo_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_write_number('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_write_number('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_write_number_group('Interest collection tenor', interest_collection_tenor)
        self.key_escape()
        if interest_collection_tenor_unit:
            self.bo_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_write_number('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_write_number('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_write_number_group('Fine collection tenor', fine_collection_tenor)
        self.key_escape()
        if fine_collection_tenor_unit:
            self.bo_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_write_number('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_write_number('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if watch:
            self.bo_write_number('Watch', watch)
        if substandard:
            self.bo_write_number('Substandard', substandard)
        if doubtful:
            self.bo_write_number('Doubtful', doubtful)
        if loss:
            self.bo_write_number('Loss', loss)
        self.bo_click_tab('IFC information')
        if ifc_codes:
            for ifc_code in ifc_codes:
                self.click_button_in_tab('Add')
                self.wait_loading()
                self.select_table('IFC Code', ifc_code)
                self.click_button_in_tab('Apply')
                self.wait_loading()
        self.bo_click_tab('GLs Information')
        if sys_account_names:
            count = len(sys_account_names)
            if not all(
                len(lst) == count for lst in [
                    account_aliass,
                    coa_accounts if coa_accounts else [None] * count
                ]
            ):
                raise ValueError("All input lists must have the same length or be None.")
            for i in range(count):
                self.add_gls_entry(i, sys_account_names, account_aliass, coa_accounts)
        self.bo_click_tab('Extension Group of Account Information')
        if replace_bys:
            count = len(replace_bys)
            if not all(
                len(lst) == count for lst in [
                    system_account_names, business_lines,
                    customer_sectors or [None] * count,
                    customer_resident_statuss or [None] * count,
                    sub_products or [None] * count,
                    bank_identifications or [None] * count
                ]
            ):
                raise ValueError("All input lists must have the same length or be None.")
            for i in range(count):
                self.add_extension_group_entry(
                    i,
                    replace_bys,
                    system_account_names,
                    business_lines,
                    customer_sectors,
                    customer_resident_statuss,
                    sub_products,
                    bank_identifications,
                    replace_code
                )
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is True:
            self.bo_click_checkbox_multi('Notification type', 'Email')
        if email is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Email')
        if push_notification is True:
            self.bo_click_checkbox_multi('Notification type', 'Push Notification')
        if push_notification is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Push Notification')
        if sms is True:
            self.bo_click_checkbox_multi('Notification type', 'SMS')
        if sms is False:
            self.bo_click_uncheckbox_multi('Notification type', 'SMS')
        # assert value
        self.bo_click_tab('General information')
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
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
            self.bo_click_tab('General information')
            catalogue_code_out=self.bo_get_value('Catalogue code')
            print(f'Catalogue code: {catalogue_code_out}')
            return catalogue_code_out

    def overdraft_catalogue_definition_view(self, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, created_by=None, approved_by=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_account_aliass=None, expected_gls_sys_account_names=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None, email=None, push_notification=None, sms=None):
        # search
        self.overdraft_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('DPT-OD Catalogue Definition-View')
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if secured_by_currency:
            self.bo_assert_select('Secured by currency', secured_by_currency)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if status:
            self.bo_assert_select('Status', status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_assert_value('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_assert_value('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_assert_value('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_assert_value('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_assert_value_group('Fine collection tenor', fine_collection_tenor)
        if fine_collection_tenor_unit:
            self.bo_assert_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_assert_value('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_assert_value('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('IFC information')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def overdraft_catalogue_definition_update(self, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, created_by=None, approved_by=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, email=None, push_notification=None, sms=None, list_error_message=None):
        # view
        self.overdraft_catalogue_definition_view(catalogue_code=catalogue_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        self.key_escape()
        if secure_type:
            self.bo_select('Secure type', secure_type)
        if secure_rate:
            self.bo_write_number('Secure rate', secure_rate)
        self.key_escape()
        if secured_by_currency:
            self.bo_select('Secured by currency', secured_by_currency)
        self.key_escape()
        if credit_sub_type:
            self.bo_select('Credit sub type', credit_sub_type)
        self.key_escape()
        if tenor_type:
            self.bo_select('Tenor type', tenor_type)
        self.key_escape()
        if credit_purpose:
            self.bo_select('Credit purpose', credit_purpose)
        self.key_escape()
        if credit_classification:
            self.bo_select('Credit classification', credit_classification)
        self.key_escape()
        if is_provision:
            self.bo_select('Is provision?', is_provision)
        self.key_escape()
        if classification_option:
            self.bo_select('Classification option', classification_option)
        self.key_escape()
        if status:
            self.bo_select('Status', status)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_write_number_group('Principal collection tenor', principal_collection_tenor)
        self.key_escape()
        if principal_collection_tenor_unit:
            self.bo_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_write_number('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_write_number('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_write_number_group('Interest collection tenor', interest_collection_tenor)
        self.key_escape()
        if interest_collection_tenor_unit:
            self.bo_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_write_number('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_write_number('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_write_number_group('Fine collection tenor', fine_collection_tenor)
        self.key_escape()
        if fine_collection_tenor_unit:
            self.bo_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_write_number('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_write_number('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_write_number('Standard', standard)
        if watch:
            self.bo_write_number('Watch', watch)
        if substandard:
            self.bo_write_number('Substandard', substandard)
        if doubtful:
            self.bo_write_number('Doubtful', doubtful)
        if loss:
            self.bo_write_number('Loss', loss)
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is True:
            self.bo_click_checkbox_multi('Notification type', 'Email')
        if email is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Email')
        if push_notification is True:
            self.bo_click_checkbox_multi('Notification type', 'Push Notification')
        if push_notification is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Push Notification')
        if sms is True:
            self.bo_click_checkbox_multi('Notification type', 'SMS')
        if sms is False:
            self.bo_click_uncheckbox_multi('Notification type', 'SMS')
        # assert value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
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
            catalogue_code_out=self.bo_get_value('Catalogue code')
            print(f'Catalogue code: {catalogue_code_out}')
            return catalogue_code_out

    def overdraft_catalogue_definition_delete(self, catalogue_code, list_error_message=None, expected_message=None):
        # search
        self.overdraft_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{catalogue_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{catalogue_code}'")
            return catalogue_code

    # DPT-Overdraft Account Information
    def overdraft_account_view(self, contract_number=None, sub_product_limit_code=None, currency=None, od_catalog_code=None, holder_name=None, include_minimum_balance=None, credit_classification=None, od_limit=None, interest_due_mode=None, from_date=None, to_date=None, contract_status=None, classification_option=None, classification_status=None, secure_type=None, secure_amount=None, secure_rate=None, interest_over_days=None, overdraft_balance=None, provision_amount=None, principal_provision_rate_0=None, principal_provision_rate_1=None, principal_provision_rate_2=None, principal_provision_rate_3=None, principal_provision_rate_4=None, expected_account_gl_names=None, expected_account_gl_numbers=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_base_values=None, expected_ifc_is_linkeds=None, expected_ifc_values=None, expected_ifc_margin_values=None, expected_ifc_statuses=None, expected_ifc_outstandings=None, expected_ifc_paids=None, expected_ifc_basic_balances=None, expected_ifc_codes=None, expected_ifc_gl_names=None, expected_ifc_gl_numbers=None, email=None, push_notification=None, sms=None):
        # search
        self.deposit_account_advanced_search(overdraft_contract=contract_number)
        self.assert_table_data('Overdraft contract', 1, self.deposit_account_number_mask(contract_number))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify OD Contract')
        self.assert_form_title('DPT-Account Information-View')
        # verify value
        self.bo_click_tab('Overdraft contract information')
        if contract_number:
            self.bo_assert_value('Contract number', self.deposit_account_number_mask(contract_number))
        if sub_product_limit_code:
            self.bo_assert_value('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if currency:
            self.bo_assert_text('Currency', currency)
        if od_catalog_code:
            self.bo_assert_value('Od catalog code', od_catalog_code)
        if holder_name:
            self.bo_assert_text('Holder name', holder_name)
        if include_minimum_balance:
            self.bo_assert_select('Include minimum balance ', include_minimum_balance)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if od_limit:
            self.bo_assert_value('Od limit', od_limit)
        if interest_due_mode:
            self.bo_assert_select('Interest due mode', interest_due_mode)
        if from_date:
            self.bo_assert_date('From date', from_date)
        if to_date:
            self.bo_assert_date('To date', to_date)
        if contract_status:
            self.bo_assert_select('Contract status', contract_status)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if classification_status:
            self.bo_assert_select('Classification status', classification_status)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_amount:
            self.bo_assert_value('Secure amount', secure_amount)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if interest_over_days:
            self.bo_assert_text('Interest over days', interest_over_days)
        if overdraft_balance:
            self.bo_assert_value('Overdraft balance', overdraft_balance)
        if provision_amount:
            self.bo_assert_value('Provision amount', provision_amount)
        if principal_provision_rate_0:
            self.bo_assert_value('Principal provision rate 0', principal_provision_rate_0)
        if principal_provision_rate_1:
            self.bo_assert_value('Principal provision rate 1', principal_provision_rate_1)
        if principal_provision_rate_2:
            self.bo_assert_value('Principal provision rate 2', principal_provision_rate_2)
        if principal_provision_rate_3:
            self.bo_assert_value('Principal provision rate 3', principal_provision_rate_3)
        if principal_provision_rate_4:
            self.bo_assert_value('Principal provision rate 4', principal_provision_rate_4)
        self.bo_click_tab('OD Contract GLs Information')
        if expected_account_gl_names:
            for account_gl_name, account_gl_number in zip(expected_account_gl_names, expected_account_gl_numbers):
                self.bo_assert_text_table_account_gls(account_gl_name, str(account_gl_number).replace('-',''))
        self.bo_click_tab('OD IFC list')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table('IFC code', ifc_code, 'IFC name', ifc_name)
        if expected_ifc_base_values:
            for ifc_code, ifc_base_value in zip(expected_ifc_list_codes, expected_ifc_base_values):
                self.bo_assert_text_table('IFC code', ifc_code, 'Base value', ifc_base_value)
        if expected_ifc_is_linkeds:
            for ifc_code, ifc_is_linked in zip(expected_ifc_list_codes, expected_ifc_is_linkeds):
                self.bo_assert_text_table('IFC code', ifc_code, 'Is linked', ifc_is_linked)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table('IFC code', ifc_code, 'IFC Value', ifc_value)
        if expected_ifc_margin_values:
            for ifc_code, ifc_margin_value in zip(expected_ifc_list_codes, expected_ifc_margin_values):
                self.bo_assert_text_table('IFC code', ifc_code, 'Margin Value', ifc_margin_value)
        if expected_ifc_statuses:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuses):
                self.bo_assert_text_table('IFC code', ifc_code, 'Status', ifc_status)
        if expected_ifc_outstandings:
            for ifc_code, ifc_outstanding in zip(expected_ifc_list_codes, expected_ifc_outstandings):
                self.bo_assert_text_table('IFC code', ifc_code, 'Oustanding', ifc_outstanding)
        if expected_ifc_paids:
            for ifc_code, ifc_paid in zip(expected_ifc_list_codes, expected_ifc_paids):
                self.bo_assert_text_table('IFC code', ifc_code, 'Paid', ifc_paid)
        if expected_ifc_basic_balances:
            for ifc_code, ifc_basic_balance in zip(expected_ifc_list_codes, expected_ifc_basic_balances):
                self.bo_assert_text_table('IFC code', ifc_code, 'Basic balance', ifc_basic_balance)
        self.bo_click_tab('OD IFC GLs Information ')
        if expected_ifc_codes:
            for ifc_code, ifc_gl_name, ifc_gl_number in zip(expected_ifc_codes, expected_ifc_gl_names, expected_ifc_gl_numbers):
                self.bo_assert_text_table_ifc_gls(ifc_code, ifc_gl_name, str(ifc_gl_number).replace('-',''))
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def overdraft_account_update(self, contract_number=None, sub_product_limit_code=None, currency=None, od_catalog_code=None, holder_name=None, include_minimum_balance=None, credit_classification=None, od_limit=None, interest_due_mode=None, from_date=None, to_date=None, contract_status=None, classification_option=None, classification_status=None, secure_type=None, secure_amount=None, secure_rate=None, interest_over_days=None, overdraft_balance=None, provision_amount=None, principal_provision_rate_0=None, principal_provision_rate_1=None, principal_provision_rate_2=None, principal_provision_rate_3=None, principal_provision_rate_4=None, email=None, push_notification=None, sms=None, list_error_message=None):
        # view
        self.overdraft_account_view(contract_number=contract_number)
        self.click_button('Modify OD Contract')
        self.wait_loading()
        # update value
        self.bo_click_tab('Overdraft contract information')
        self.key_escape()
        if credit_classification:
            self.bo_select('Credit classification', credit_classification)
        self.key_escape()
        if classification_option:
            self.bo_select('Classification option', classification_option)
        self.key_escape()
        if secure_type:
            self.bo_select('Secure type', secure_type)
        if secure_rate:
            self.bo_write_number('Secure rate', secure_rate)
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is True:
            self.bo_click_checkbox_multi('Notification type', 'Email')
        if email is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Email')
        if push_notification is True:
            self.bo_click_checkbox_multi('Notification type', 'Push Notification')
        if push_notification is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Push Notification')
        if sms is True:
            self.bo_click_checkbox_multi('Notification type', 'SMS')
        if sms is False:
            self.bo_click_uncheckbox_multi('Notification type', 'SMS')
        # assert value
        self.bo_click_tab('Overdraft contract information')
        if contract_number:
            self.bo_assert_value('Contract number', self.deposit_account_number_mask(contract_number))
        if sub_product_limit_code:
            self.bo_assert_value('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if currency:
            self.bo_assert_text('Currency', currency)
        if od_catalog_code:
            self.bo_assert_value('Od catalog code', od_catalog_code)
        if holder_name:
            self.bo_assert_text('Holder name', holder_name)
        if include_minimum_balance:
            self.bo_assert_select('Include minimum balance ', include_minimum_balance)
        if od_limit:
            self.bo_assert_value('Od limit', od_limit)
        if interest_due_mode:
            self.bo_assert_select('Interest due mode', interest_due_mode)
        if from_date:
            self.bo_assert_date('From date', from_date)
        if to_date:
            self.bo_assert_date('To date', to_date)
        if contract_status:
            self.bo_assert_select('Contract status', contract_status)
        if classification_status:
            self.bo_assert_select('Classification status', classification_status)
        if secure_amount:
            self.bo_assert_value('Secure amount', secure_amount)
        if interest_over_days:
            self.bo_assert_text('Interest over days', interest_over_days)
        if overdraft_balance:
            self.bo_assert_value('Overdraft balance', overdraft_balance)
        if provision_amount:
            self.bo_assert_value('Provision amount', provision_amount)
        if principal_provision_rate_0:
            self.bo_assert_value('Principal provision rate 0', principal_provision_rate_0)
        if principal_provision_rate_1:
            self.bo_assert_value('Principal provision rate 1', principal_provision_rate_1)
        if principal_provision_rate_2:
            self.bo_assert_value('Principal provision rate 2', principal_provision_rate_2)
        if principal_provision_rate_3:
            self.bo_assert_value('Principal provision rate 3', principal_provision_rate_3)
        if principal_provision_rate_4:
            self.bo_assert_value('Principal provision rate 4', principal_provision_rate_4)
        self.wait_loading()
        # click 'Save modify OD'
        self.click_button('Save modify OD')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action update failed!')
        else:
        # verify success
            self.assert_button_disable('Save modify OD')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('Overdraft contract information')
            contract_number_out=self.bo_get_value('Contract number')
            print(f'Contract number: {contract_number_out}')
            return contract_number_out

    # DPT-Approve Overdraft Contract Modification
    def overdraft_approve_modify_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Deposit', 'Approve Overdraft Contract Modification')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-Approve Overdraft Contract Modification-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def overdraft_approve_modify_advanced_search(self, contract_number=None, holder_name=None, currency=None, od_limit=None, od_catalog_code=None, contract_status=None, interest_due_mode=None, classification_status=None):
        self.close_all_form()
        self.click_menu('Deposit', 'Approve Overdraft Contract Modification')
        self.wait_for_button_available('Search')
        self.assert_form_title('DPT-Approve Overdraft Contract Modification-Search')
        if contract_number:
            self.adv_search_text('Contract number', str(contract_number).replace('-', ''))
        if holder_name:
            self.adv_search_text('Holder name', holder_name)
        if currency:
            self.adv_search_text('Currency', currency)
        if od_limit:
            self.adv_search('Od limit', od_limit)
        if od_catalog_code:
            self.adv_search_text('Od catalog code', od_catalog_code)
        self.key_escape()
        if contract_status:
            self.adv_search_select('Contract status', contract_status)
        self.key_escape()
        if interest_due_mode:
            self.adv_search_select('Interest due mode', interest_due_mode)
        self.key_escape()
        if classification_status:
            self.adv_search_select('Classification status', classification_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def overdraft_approve_modify_view(self, contract_number=None, sub_product_limit_code=None, currency=None, od_catalog_code=None, holder_name=None, include_minimum_balance=None, credit_classification=None, od_limit=None, interest_due_mode=None, from_date=None, to_date=None, contract_status=None, secure_amount=None, classification_status=None, classification_option=None, restruct_modification=None, overdraft_balance=None, secure_type=None, secure_type_modification=None, provision_amount=None, secure_rate=None, secure_rate_modification=None, interest_over_days=None, principal_provision_rate_0=None, principal_provision_rate_1=None, principal_provision_rate_2=None, principal_provision_rate_3=None, principal_provision_rate_4=None, email=None, push_notification=None, sms=None):
        # search
        self.overdraft_approve_modify_simple_search(str(contract_number).replace('-', ''))
        self.assert_table_data('Contract number', 1, self.deposit_account_number_mask(contract_number))
        # view
        self.click_table_menu(row=1)
        self.wait_for_button_available('View Modification')
        self.assert_form_title('DPT-Approve Overdraft Contract Modification-View')
        # verify value
        self.bo_click_tab('General information')
        if contract_number:
            self.bo_assert_value('Contract number', self.deposit_account_number_mask(contract_number))
        if sub_product_limit_code:
            self.bo_assert_value('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if currency:
            self.bo_assert_text('Currency', currency)
        if od_catalog_code:
            self.bo_assert_value('Od catalog code', od_catalog_code)
        if holder_name:
            self.bo_assert_text('Holder name', holder_name)
        if include_minimum_balance:
            self.bo_assert_select('Include minimum balance ', include_minimum_balance)
        if credit_classification:
            self.bo_assert_select_group('Credit classification', credit_classification)
        if od_limit:
            self.bo_assert_value('Od limit', od_limit)
        if interest_due_mode:
            self.bo_assert_select('Interest due mode', interest_due_mode)
        if from_date:
            self.bo_assert_date('From date', from_date)
        if to_date:
            self.bo_assert_date('To date', to_date)
        if contract_status:
            self.bo_assert_select('Contract status', contract_status)
        if secure_amount:
            self.bo_assert_value('Secure amount', secure_amount)
        if classification_status:
            self.bo_assert_select('Classification status', classification_status)
        if classification_option:
            self.bo_assert_select_group('Classification option', classification_option)
        if restruct_modification:
            self.bo_assert_select_group('restruct_modification', restruct_modification)
        if overdraft_balance:
            self.bo_assert_value('Overdraft balance', overdraft_balance)
        if secure_type:
            self.bo_assert_select_group('Secure type', secure_type)
        if secure_type_modification:
            self.bo_assert_select_group('secure_type_modification', secure_type_modification)
        if provision_amount:
            self.bo_assert_value('Provision amount', provision_amount)
        if secure_rate:
            self.bo_assert_value_group('Secure rate', secure_rate)
        if secure_rate_modification:
            self.bo_assert_value_group('secure_rate_modification', secure_rate_modification)
        if interest_over_days:
            self.bo_assert_text('Interest over days', interest_over_days)
        if principal_provision_rate_0:
            self.bo_assert_value('Principal provision rate 0', principal_provision_rate_0)
        if principal_provision_rate_1:
            self.bo_assert_value('Principal provision rate 1', principal_provision_rate_1)
        if principal_provision_rate_2:
            self.bo_assert_value('Principal provision rate 2', principal_provision_rate_2)
        if principal_provision_rate_3:
            self.bo_assert_value('Principal provision rate 3', principal_provision_rate_3)
        if principal_provision_rate_4:
            self.bo_assert_value('Principal provision rate 4', principal_provision_rate_4)
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def overdraft_approve_modify_approve(self, contract_number):
        self.overdraft_approve_modify_view(contract_number=contract_number)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Approve')
        self.wait_loading()
        self.check_notification('Approve successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Contract number', self.deposit_account_number_mask(contract_number))
        contract_number_out=self.bo_get_value('Contract number')
        print(f'Contract number: {contract_number_out}')
        self.overdraft_approve_modify_simple_search(str(contract_number).replace('-', ''))
        self.assert_search_not_found()
        return contract_number_out

    def overdraft_approve_modify_reject(self, contract_number):
        self.overdraft_approve_modify_view(contract_number=contract_number)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Reject')
        self.wait_loading()
        self.check_notification('Reject successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Contract number', self.deposit_account_number_mask(contract_number))
        contract_number_out=self.bo_get_value('Contract number')
        print(f'Contract number: {contract_number_out}')
        self.overdraft_approve_modify_simple_search(str(contract_number).replace('-', ''))
        self.assert_search_not_found()
        return contract_number_out

# -------------------------- handle BO approval - OVERDRAFT --------------------------
    # DPT-OD Catalogue Definition - Data Verification
    def overdraft_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_account_aliass=None, expected_gls_sys_account_names=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None, email=None, push_notification=None, sms=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-OD Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if secured_by_currency:
            self.bo_assert_select('Secured by currency', secured_by_currency)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if status:
            self.bo_assert_select('Status', status)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_assert_value('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_assert_value('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_assert_value('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_assert_value('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_assert_value_group('Fine collection tenor', fine_collection_tenor)
        if fine_collection_tenor_unit:
            self.bo_assert_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_assert_value('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_assert_value('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('IFC information')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def overdraft_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, created_by=None, approved_by=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_account_aliass=None, expected_gls_sys_account_names=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None, email=None, push_notification=None, sms=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-OD Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if secured_by_currency:
            self.bo_assert_select('Secured by currency', secured_by_currency)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if status:
            self.bo_assert_select('Status', status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_assert_value('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_assert_value('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_assert_value('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_assert_value('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_assert_value_group('Fine collection tenor', fine_collection_tenor)
        if fine_collection_tenor_unit:
            self.bo_assert_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_assert_value('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_assert_value('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('IFC information')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def overdraft_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, currency=None, credit_type=None, credit_facility=None, tenor_type=None, status=None):
        # search and verify
        self.overdraft_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue name', 1, catalogue_name)
        if currency:
            self.assert_table_data('Currency', 1, currency)
        if credit_type:
            self.assert_table_data('Credit type', 1, credit_type)
        if credit_facility:
            self.assert_table_data('Credit facility', 1, credit_facility)
        if tenor_type:
            self.assert_table_data('Tenor type', 1, tenor_type)
        if status:
            self.assert_table_data('Status', 1, status)

