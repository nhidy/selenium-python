from webui_test.case import *

class CashActions(TestCase):

# -------------------------- handle FO - CASH --------------------------
    # CSH_MOV: CSH-Internal Cash Movement
    def csh_mov(self, to_teller_code=None, amount=None, currency=None, from_teller_code=None, to_teller_name=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CSH_MOV', 'Internal cash movement')
        self.wait_for_button_available('Accept')
        self.assert_form_title('CSH-Internal Cash Movement')
        # enter value
        if to_teller_code:
            self.fo_write_group('To teller code', to_teller_code)
            self.wait_loading()
        if amount:
            self.fo_write_number('Amount', amount)
        self.key_escape()
        if currency:
            self.fo_select('Currency', currency)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if from_teller_code:
            self.fo_assert_value_group('From teller code', from_teller_code)
        if to_teller_name:
            self.fo_assert_text('To teller name', to_teller_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
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
            print(f'Transaction references CSH_MOV: {transaction_references}')
            to_teller_code_out=self.fo_get_value_group('To teller code')
            print(f'To teller code: {to_teller_code_out}')
            return transaction_references, to_teller_code_out

    def csh_mov_view(self, transaction_references, to_teller_code=None, amount=None, currency=None, from_teller_code=None, to_teller_name=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'CSH-Internal Cash Movement')
        # compare value
        if to_teller_code:
            self.fo_assert_value_group('To teller code', to_teller_code)
        if amount:
            self.fo_assert_value('Amount', amount)
        if currency:
            self.fo_assert_select('Currency', currency)
        if from_teller_code:
            self.fo_assert_value_group('From teller code', from_teller_code)
        if to_teller_name:
            self.fo_assert_text('To teller name', to_teller_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CSH_MOV: {transaction_references}')
        to_teller_code_out=self.fo_get_value_group('To teller code')
        print(f'F8: To teller code: {to_teller_code_out}')
        return transaction_references, to_teller_code_out

    # CSH_BMOV: CSH-Internal Branch Cash Movement
    def csh_bmov(self, send_to_branch=None, to_teller_code=None, amount=None, currency=None, from_teller_code=None, to_teller_name=None, description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CSH_BMOV', 'Internal bank cash movement')
        self.wait_for_button_available('Accept')
        self.assert_form_title('CSH-Internal Branch Cash Movement')
        # enter value
        self.key_escape()
        if send_to_branch:
            self.fo_select('Send to branch', send_to_branch)
        if to_teller_code:
            self.fo_write_group('To teller code', to_teller_code)
            self.wait_loading()
        if amount:
            self.fo_write_number('Amount', amount)
        self.key_escape()
        if currency:
            self.fo_select('Currency', currency)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if from_teller_code:
            self.fo_assert_value_group('From teller code', from_teller_code)
        if to_teller_name:
            self.fo_assert_text('To teller name', to_teller_name)
        if description:
            self.fo_assert_text('Description', description)
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
            print(f'Transaction references CSH_BMOV: {transaction_references}')
            return transaction_references

    def csh_bmov_view(self, transaction_references, send_to_branch=None, to_teller_code=None, amount=None, currency=None, from_teller_code=None, to_teller_name=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'CSH-Internal Branch Cash Movement')
        # compare value
        if send_to_branch:
            self.fo_assert_select('Send to branch', send_to_branch)
        if to_teller_code:
            self.fo_assert_value_group('To teller code', to_teller_code)
        if amount:
            self.fo_assert_value('Amount', amount)
        if currency:
            self.fo_assert_select('Currency', currency)
        if from_teller_code:
            self.fo_assert_value_group('From teller code', from_teller_code)
        if to_teller_name:
            self.fo_assert_text('To teller name', to_teller_name)
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CSH_BMOV: {transaction_references}')
        return transaction_references

    # CSH_DNM: Cash denomination
    def csh_dnm(self, currency=None, description=None, closing_cash_balance=None, denom_cash_balance=None, remaining_cash_balance=None, ifc_codes=None, values=None, total_fee=None, denominations=None, type_of_notes=None, sheets=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CSH_DNM', 'Cash denomination')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Cash denomination')
        # enter value
        self.key_escape()
        if currency:
            self.fo_select('Currency', currency)
            self.wait_loading()
        if denominations:
            self.add_sheet(denominations, type_of_notes, sheets)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
            self.wait_loading()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if closing_cash_balance:
            self.fo_assert_value('Closing cash balance', closing_cash_balance)
        if denom_cash_balance:
            self.fo_assert_value('Denom cash balance', denom_cash_balance)
        if remaining_cash_balance:
            self.fo_assert_value('Remaining cash balance', remaining_cash_balance)
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
            print(f'Transaction references CSH_DNM: {transaction_references}')
            return transaction_references

    def csh_dnm_view(self, transaction_references, currency=None, description=None, closing_cash_balance=None, denom_cash_balance=None, remaining_cash_balance=None, expected_posting=None):
        self.transaction_view_no_return_transaction_references(transaction_references, 'Cash denomination')
        # compare value
        if currency:
            self.fo_assert_select('Currency', currency)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if closing_cash_balance:
            self.fo_assert_value('Closing cash balance', closing_cash_balance)
        if denom_cash_balance:
            self.fo_assert_value('Denom cash balance', denom_cash_balance)
        if remaining_cash_balance:
            self.fo_assert_value('Remaining cash balance', remaining_cash_balance)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
