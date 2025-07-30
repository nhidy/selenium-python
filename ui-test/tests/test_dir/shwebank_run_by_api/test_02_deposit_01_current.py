import random
import webui_test
import os
from datetime import datetime
from webui_test.logging import log

from webui_test.form_action import FormAction

# Get value from environment variable
RUN_ON_URL = os.getenv("TEST_CONFIG_RUN_ON_URL", "")
USERNAME_LOGIN = os.getenv("TEST_CONFIG_USERNAME_LOGIN", "")
PASSWORD_LOGIN = os.getenv("TEST_CONFIG_PASSWORD_LOGIN", "")
ONE_APP = os.getenv("TEST_CONFIG_ONE_APP", "")
CUSTOMER_CODE = os.getenv("TEST_CONFIG_CUSTOMER_CODE", "")
USERNAME_APPROVE = os.getenv("TEST_CONFIG_USERNAME_APPROVE", "")
PASSWORD_APPROVE = os.getenv("TEST_CONFIG_PASSWORD_APPROVE", "")
USERNAME_REVERSE = os.getenv("TEST_CONFIG_USERNAME_REVERSE", "")
PASSWORD_REVERSE = os.getenv("TEST_CONFIG_PASSWORD_REVERSE", "")

customer_code_personal = CUSTOMER_CODE

# data test for 'Cheque'
stock_type_cq = 'Cheque'
stock_prefix_cq = 'CQ'
number_of_leaves_cq = '25'
number_of_book_cq = '1'
expected_values = ['Paid'] * 3 + ['Damage'] + ['Unpaid'] * 21
list_error_message = [
    'CannotBeReversed: DPT_SRG can not be reversed'
]
# data test for cash deposit
amount_deposit_mask='5,000,000.49'
amount_deposit_to_other_mask='1,000,000.00'
# data test for cheque withdrawal
cheque_amount='10,000.54' # 3 times
# data test for change status of cheque
status_change_of_cheque='Damage'
# data test for close deposit account
expected_current_balance='4,969,998.87'
expected_interest_accrual='0.00'

class DepositCurrentTest(FormAction):
    def get_url(self):
        return RUN_ON_URL

    def data_begin(self):
        global username_approve, password_approve, username_reverse, password_reverse, username, password
        username_approve = USERNAME_APPROVE
        password_approve = PASSWORD_APPROVE
        username_reverse = USERNAME_REVERSE
        password_reverse = PASSWORD_REVERSE
        username = USERNAME_LOGIN
        password = PASSWORD_LOGIN
        self.login(username, password, one_app=ONE_APP)
        global working_date, branch_code
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()
        global gl_account_number
        gl_account_number = f'{branch_code}-1100601000000-01'

    def start_class(self):
        self.data_begin()

    def end_class(self):
        self.logout()

    def reset_browser(self):
        self.logout()
        self.restart_browser()
        self.data_begin()

# Check the data used for testing
    def test_000_check_test_data_must_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=gl_account_number
        )
        if self.check_customer_profile_not_exist(customer_code_personal):
            self.stop()
            self.fail()

# DEPOST CURRENT
    def test_013_current_01_dpt_opn_open_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_account_current_mask, deposit_account_current
        catalogue_code_current='CAMMK0000'
        reason_of_account_opening='Enter value reason of account opening'
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code_current,
            reason_of_account_opening=reason_of_account_opening,
            mpu_card=True,
            passbook_cheque_book=True
        )
        deposit_account_current_mask=dpt_opn_result[1]
        deposit_account_current = deposit_account_current_mask.replace('-', '')

    def test_013_current_02_dpt_apr_approve_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_apr_result = self.dpt_apr(
            account_number=deposit_account_current,
            approve_later='Y'
        )
        transaction_references=dpt_apr_result[0]
        account_number_actual_mask=dpt_apr_result[1]
        self.assertEqual(account_number_actual_mask, deposit_account_current_mask)
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )

    def test_013_current_03_dpt_cdp_cash_deposit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_cdp_result = self.dpt_cdp(
            account_number=deposit_account_current,
            amount_deposit=amount_deposit_mask.replace(',', ''),
            approve_later='Y'
        )
        transaction_references=dpt_cdp_result[0]
        account_number_actual_mask=dpt_cdp_result[1]
        self.assertEqual(account_number_actual_mask, deposit_account_current_mask)
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )

# CHEQUE
    def test_014_cheque_01_dpt_srg_stock_registration_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global from_serial_cq, to_serial_cq
        generated_number = self.gen_serial_number(stock_prefix_cq, stock_type_cq, 24)
        print(f'generated_number: {generated_number}')
        from_serial = generated_number[0]
        to_serial = generated_number[1]
        dpt_srg_result = self.dpt_srg(
            stock_type=stock_type_cq,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix_cq,
            number_of_leaves=number_of_leaves_cq,
            number_of_book=number_of_book_cq,
            approve_later='Y'
        )
        transaction_references=dpt_srg_result[0]
        from_serial_cq = dpt_srg_result[1]
        to_serial_cq = dpt_srg_result[2]
        self.assertEqual(from_serial_cq, from_serial)
        self.assertEqual(to_serial_cq, to_serial)
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )

    def test_014_cheque_02_dpt_sat_stock_assign_to_staff_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_sat_result = self.dpt_sat(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq,
            to_serial=to_serial_cq,
            assigned_staff_code=username
        )
        self.assertEqual(from_serial_cq, dpt_sat_result[1])
        self.assertEqual(to_serial_cq, dpt_sat_result[2])

    def test_014_cheque_03_dpt_ccr_stock_confirm_received_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_ccr_result = self.dpt_ccr(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq,
            to_serial=to_serial_cq,
            approve_later='Y'
        )
        self.assertEqual(from_serial_cq, dpt_ccr_result[1])
        self.assertEqual(to_serial_cq, dpt_ccr_result[2])
        self.transaction_approve(
            transaction_references=dpt_ccr_result[0], 
            username=username_approve,
            password=password_approve
        )

    def test_014_cheque_04_dpt_cis_cheque_book_issued_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_cis_result = self.dpt_cis(
            account_number=deposit_account_current,
            from_serial=from_serial_cq,
            to_serial=to_serial_cq
        )
        self.assertEqual(from_serial_cq, dpt_cis_result[1])
        self.assertEqual(to_serial_cq, dpt_cis_result[2])

    def test_014_cheque_05_dpt_cei_issued_hold_balance_for_cheque_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        cheque_amount='5,000.45'
        dpt_cei_result = self.dpt_cei(
            cheque_no=from_serial_cq,
            cheque_amount=cheque_amount,
            account_number=deposit_account_current_mask,
            approve_later='Y'
        )
        self.assertEqual(from_serial_cq, dpt_cei_result[1])
        self.assertEqual(deposit_account_current_mask, dpt_cei_result[2])
        self.transaction_approve(
            transaction_references=dpt_cei_result[0], 
            username=username_approve,
            password=password_approve
        )

    def test_014_cheque_06_dpt_rec_release_hold_balance_for_cheque_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        cheque_amount='5,000.45'
        dpt_rec_result = self.dpt_rec(
            cheque_no=from_serial_cq,
            cheque_amount=cheque_amount,
            account_number=deposit_account_current_mask,
            approve_later='Y'
        )
        self.assertEqual(from_serial_cq, dpt_rec_result[1])
        self.assertEqual(deposit_account_current_mask, dpt_rec_result[2])
        self.transaction_approve(
            transaction_references=dpt_rec_result[0], 
            username=username_approve,
            password=password_approve
        )

    def test_014_cheque_07_dpt_cdt_deposit_by_cheque_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # open deposit account used for credit account test
        catalogue_code_current='CAMMK0000'
        reason_of_account_opening='Enter value reason of account opening'
        global other_deposit_account_mask
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code_current,
            reason_of_account_opening=reason_of_account_opening
        )
        other_deposit_account_mask=dpt_opn_result[1]
        self.dpt_apr(
            account_number=other_deposit_account_mask,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cdp(
            account_number=other_deposit_account_mask,
            amount_deposit=amount_deposit_to_other_mask,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        dpt_cdt_result = self.dpt_cdt(
            cheque_no=from_serial_cq,
            debit_amount=cheque_amount.replace(',', ''),
            credit_account=other_deposit_account_mask,
            debit_account=deposit_account_current_mask,
            approve_later='Y'
        )
        self.assertEqual(from_serial_cq, dpt_cdt_result[1])
        self.assertEqual(other_deposit_account_mask, dpt_cdt_result[2])
        self.transaction_approve(
            transaction_references=dpt_cdt_result[0], 
            username=username_approve,
            password=password_approve
        )

    def test_014_cheque_08_dpt_cwc_cash_withdrawal_by_cheque_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        next_cheque_no=self.get_next_serial_number(stock_prefix_cq, from_serial_cq, 1)
        dpt_cwc_result = self.dpt_cwc(
            cheque_no=next_cheque_no,
            cheque_amount=cheque_amount,
            account_number=deposit_account_current_mask,
            approve_later='Y'
        )
        self.assertEqual(next_cheque_no, dpt_cwc_result[1])
        self.assertEqual(deposit_account_current_mask, dpt_cwc_result[2])
        self.transaction_approve(
            transaction_references=dpt_cwc_result[0], 
            username=username_approve,
            password=password_approve
        )

    def test_014_cheque_09_dpt_cwm_miscellaneous_debit_by_cheque_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        cheque_no=self.get_next_serial_number(stock_prefix_cq, from_serial_cq, 2)
        dpt_cwm_result = self.dpt_cwm(
            cheque_no=cheque_no,
            cheque_amount=cheque_amount,
            account_number=deposit_account_current_mask,
            credit_accounting=gl_account_number,
            approve_later='Y'
        )
        self.assertEqual(cheque_no, dpt_cwm_result[1])
        self.assertEqual(gl_account_number, dpt_cwm_result[2])
        self.transaction_approve(
            transaction_references=dpt_cwm_result[0], 
            username=username_approve,
            password=password_approve
        )

    def test_014_cheque_10_dpt_cts_change_status_of_stock_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        cheque_no=self.get_next_serial_number(stock_prefix_cq, from_serial_cq, 3)
        dpt_cts_result = self.dpt_cts(
            account_number=deposit_account_current_mask,
            stock_type=stock_type_cq,
            from_serial=cheque_no,
            to_serial=cheque_no,
            status=status_change_of_cheque,
            approve_later='Y'
        )
        self.assertEqual(cheque_no, dpt_cts_result[1])
        self.assertEqual(cheque_no, dpt_cts_result[2])
        self.transaction_approve(
            transaction_references=dpt_cts_result[0], 
            username=username_approve,
            password=password_approve
        )

    def test_014_cheque_11_dpt_ciq_cheque_inquiry_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        serial_numbers = self.get_list_serial_number(stock_prefix_cq, from_serial_cq, to_serial_cq)
        dpt_ciq_result = self.dpt_ciq(
            account_number=deposit_account_current_mask,
            serial_number=from_serial_cq,
            serial_numbers=serial_numbers,
            expected_values=expected_values
        )
        self.assertEqual(from_serial_cq, dpt_ciq_result[1])

    def test_014_cheque_12_dpt_sls_cheque_leaves_status_inquiry_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        serial_numbers = self.get_list_serial_number(stock_prefix_cq, from_serial_cq, to_serial_cq)
        dpt_sls_result = self.dpt_sls(
            from_serial=from_serial_cq,
            to_serial=to_serial_cq,
            serial_numbers=serial_numbers,
            expected_values=expected_values
        )
        self.assertEqual(from_serial_cq, dpt_sls_result[1])
        self.assertEqual(to_serial_cq, dpt_sls_result[2])

    def test_015_current_01_dpt_dls_close_deposit_account_by_deposit_success(self):
        # view account before close
        self.deposit_account_view(
            account_number=deposit_account_current_mask,
            current_balance=expected_current_balance,
            interest_accrual=expected_interest_accrual
        )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # close deposit account
        dpt_dls_result = self.dpt_dls(
            account_number=deposit_account_current_mask,
            another_deposit_account=other_deposit_account_mask,
            balance=expected_current_balance,
            interest_payable_receivable=expected_interest_accrual,
            interest_due='0.00',
            interest_re_calculate='0.00',
            gross_paid_interest_amount='0.00',
            penalty_fee='0.00',
            balance_received=expected_current_balance,
            approve_later='Y'
        )
        self.assertEqual(deposit_account_current_mask, dpt_dls_result[1])
        self.transaction_approve(
            transaction_references=dpt_dls_result[0], 
            username=username_approve,
            password=password_approve
        )
        # view account after close
        self.deposit_account_view(
            account_number=deposit_account_current_mask,
            current_balance='0.00',
            interest_accrual='0.00'
        )
        self.transaction_reverse(
            transaction_references=dpt_dls_result[0],
            username=username_reverse,
            password=password_reverse
        )
        # view account after reverse close
        self.deposit_account_view(
            account_number=deposit_account_current_mask,
            current_balance=expected_current_balance,
            interest_accrual=expected_interest_accrual
        )

    def test_015_current_02_dpt_mls_close_deposit_account_by_gl_success(self):
        # view account before close
        self.deposit_account_view(
            account_number=deposit_account_current_mask,
            current_balance=expected_current_balance,
            interest_accrual=expected_interest_accrual
        )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # close deposit account
        dpt_mls_result = self.dpt_mls(
            account_number=deposit_account_current_mask,
            accounting_number=gl_account_number,
            balance=expected_current_balance,
            interest_payable_receivable=expected_interest_accrual,
            interest_due='0.00',
            interest_re_calculate='0.00',
            gross_paid_interest_amount='0.00',
            penalty_fee='0.00',
            balance_received=expected_current_balance,
            approve_later='Y'
        )
        self.assertEqual(deposit_account_current_mask, dpt_mls_result[1])
        self.transaction_approve(
            transaction_references=dpt_mls_result[0], 
            username=username_approve,
            password=password_approve
        )
        # view account after close
        self.deposit_account_view(
            account_number=deposit_account_current_mask,
            current_balance='0.00',
            interest_accrual='0.00'
        )
        self.transaction_reverse(
            transaction_references=dpt_mls_result[0],
            username=username_reverse,
            password=password_reverse
        )
        # view account after reverse close
        self.deposit_account_view(
            account_number=deposit_account_current_mask,
            current_balance=expected_current_balance,
            interest_accrual=expected_interest_accrual
        )

    def test_015_current_03_dpt_cls_close_deposit_account_by_cash_success(self):
        # view account before close
        self.deposit_account_view(
            account_number=deposit_account_current_mask,
            current_balance=expected_current_balance,
            interest_accrual=expected_interest_accrual
        )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # close deposit account
        dpt_cls_result = self.dpt_cls(
            account_number=deposit_account_current_mask,
            balance=expected_current_balance,
            interest_payable_receivable=expected_interest_accrual,
            interest_due='0.00',
            interest_re_calculate='0.00',
            gross_paid_interest_amount='0.00',
            penalty_fee='0.00',
            balance_received=expected_current_balance,
            approve_later='Y'
        )
        self.assertEqual(deposit_account_current_mask, dpt_cls_result[1])
        self.transaction_approve(
            transaction_references=dpt_cls_result[0], 
            username=username_approve,
            password=password_approve
        )
        # view account after close
        self.deposit_account_view(
            account_number=deposit_account_current_mask,
            current_balance='0.00',
            interest_accrual='0.00'
        )
        self.transaction_reverse(
            transaction_references=dpt_cls_result[0],
            username=username_reverse,
            password=password_reverse
        )
        # view account after reverse close
        self.deposit_account_view(
            account_number=deposit_account_current_mask,
            current_balance=expected_current_balance,
            interest_accrual=expected_interest_accrual
        )

    def test_016_current_01_dpt_his_transaction_history_inquiry_success(self):
        # close deposit again
        dpt_cls_result = self.dpt_cls(
            account_number=deposit_account_current_mask,
            balance=expected_current_balance,
            interest_payable_receivable=expected_interest_accrual,
            interest_due='0.00',
            interest_re_calculate='0.00',
            gross_paid_interest_amount='0.00',
            penalty_fee='0.00',
            balance_received=expected_current_balance,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.assertEqual(deposit_account_current_mask, dpt_cls_result[1])
        # view account after close success
        self.deposit_account_view(
            account_number=deposit_account_current_mask,
            current_balance='0.00',
            interest_accrual='0.00'
        )
        expected_trans_code=['DPT_OPN','DPT_APR','DPT_CDP','DPT_CIS','DPT_CEI','DPT_REC','DPT_CDT','DPT_CWC','DPT_CWM','DPT_CLS']
        expected_users=[username] * 10
        expected_channels=['Core Banking'] * 10
        expected_debits=['0.00'] * 6 + ['10,000.54'] * 3 + ['4,969,998.87']
        expected_credits=['0.00'] * 2 + ['5,000,000.49'] + ['0.00'] * 7
        expected_balances=['0.00'] * 2 + ['5,000,000.49'] * 4 + ['4,989,999.95'] + ['4,979,999.41'] + ['4,969,998.87'] + ['0.00']
        expected_dates=[working_date] * 10
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        dpt_his_result = self.dpt_his(
            account_number=deposit_account_current_mask,
            transaction_codes=expected_trans_code,
            expected_debits=expected_debits,
            expected_credits=expected_credits,
            expected_balances=expected_balances,
            expected_created_bys=expected_users,
            expected_channels=expected_channels,
            expected_transaction_dates=expected_dates
        )
        self.assertEqual(deposit_account_current_mask, dpt_his_result[1])

if __name__ == '__main__': 
    webui_test.main()