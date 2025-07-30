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

# data test for 'Passbook for Savings'
stock_type_sb = 'Passbook for Savings'
stock_prefix_sb = 'SB'
number_of_leaves_sb = '1'
number_of_book_sb = '10'

# data test for deposit account
catalogue_code='SAMMK0000'
deposit_type='Savings'
deposit_sub_type='Savings Account'
rollover_option='No rollover'
reason_of_account_opening='Reason opening Savings (S1) account'
expected_account_gl_name='DEPOSIT'
expected_ifc_codes=['101'] * 2
expected_ifc_gl_names=['PAID_INTEREST', 'INTEREST']
# data test for cash deposit
amount_deposit_mask='5,000,000.49' # 3 times
current_balance_2nd='10,000,000.98'
current_balance_3rd='15,000,001.47'
amount_deposit_to_other_mask='6,000,000.00'
current_balance_other='999,999.51'
# data test for cash withdrawal
withdraw_amount='1,000,000.54' # 3 times
current_balance_other_2nd='2,000,000.05'
current_balance_withdrawal_1st='14,000,000.93'
current_balance_withdrawal_2nd='13,000,000.39'
current_balance_withdrawal_3rd='11,999,999.85'
# data test deposit status
status_pending='Pending to approve'
status_new='New'
status_normal='Normal'
status_dormant='Dormant'
status_block='Block'
status_closed='Closed'
status_reject='Reject'
# data test for change status of cheque
status_change_of_cheque='Damage'
# data test for close deposit account
# expected_current_balance='4,969,998.87'
expected_interest_accrual='0.00'
transaction_numbers=[]

class DepositS1SavingsTest(FormAction):
    def get_url(self):
        return RUN_ON_URL

    def data_begin(self):
        global username_approve, password_approve, username_reverse, password_reverse, username, password, transaction_numbers
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
        global expected_account_gl_number, expected_ifc_gl_numbers
        expected_account_gl_number=f'{branch_code}202030201010101'
        expected_ifc_gl_numbers=[f'{branch_code}401020201010101', f'{branch_code}207010100010101']
        global gl_account_number
        gl_account_number=f'{branch_code}-1100601000000-01'

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

# DEPOST SAVINGS (S1)
    def test_013_savings_01_dpt_opn_open_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_account_saving_mask, deposit_account_saving
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code,
            reason_of_account_opening=reason_of_account_opening,
            mpu_card=True,
            passbook_cheque_book=True
        )
        transaction_numbers.append(dpt_opn_result[0])
        deposit_account_saving_mask=dpt_opn_result[1]
        deposit_account_saving = str(deposit_account_saving_mask).replace('-', '')
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_pending,
            account_holder=customer_code_personal,
            catalogue_code=catalogue_code,
            branch_id=branch_code,
            deposit_type=deposit_type,
            deposit_sub_type=deposit_sub_type,
            open_date=working_date,
            is_restricted='No',
            current_balance='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_013_savings_02_dpt_apr_approve_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_apr_result = self.dpt_apr(
            account_number=deposit_account_saving,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        transaction_numbers.append(dpt_apr_result[0])
        account_number_actual_mask=dpt_apr_result[1]
        self.assertEqual(account_number_actual_mask, deposit_account_saving_mask)
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_new,
            current_balance='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_013_savings_03_dpt_cdp_cash_deposit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_cdp_result = self.dpt_cdp(
            account_number=deposit_account_saving,
            amount_deposit=amount_deposit_mask.replace(',', ''),
            approve_later='Y'
        )
        transaction_references=dpt_cdp_result[0]
        account_number_actual_mask=dpt_cdp_result[1]
        transaction_numbers.append(transaction_references)
        self.assertEqual(account_number_actual_mask, deposit_account_saving_mask)
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            current_balance=amount_deposit_mask,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_013_savings_04_dpt_mdp_miscellaneous_deposit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_mdp_result = self.dpt_mdp(
            account_number=deposit_account_saving_mask,
            amount_deposit=amount_deposit_mask.replace(',', ''),
            debit_accounting=gl_account_number,
            approve_later='Y'
        )
        transaction_references=dpt_mdp_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_saving_mask, dpt_mdp_result[1])
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            current_balance=current_balance_2nd,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_013_savings_05_dpt_trf_get_money_from_other_deposit_account_success(self):
        global other_deposit_account_mask
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code='CAMMK0000',
            reason_of_account_opening='Enter value reason of account opening'
        )
        other_deposit_account_mask=dpt_opn_result[1]
        self.dpt_apr(
            account_number=other_deposit_account_mask,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_mdp(
            account_number=other_deposit_account_mask,
            amount_deposit=amount_deposit_to_other_mask,
            debit_accounting=gl_account_number,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_trf_result = self.dpt_trf(
            debit_account=other_deposit_account_mask,
            amount=amount_deposit_mask,
            credit_account=deposit_account_saving_mask,
            approve_later='Y'
        )
        transaction_references=dpt_trf_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(other_deposit_account_mask, dpt_trf_result[1])
        self.assertEqual(deposit_account_saving_mask, dpt_trf_result[2])
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # verify credit deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            current_balance=current_balance_3rd,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        # verify debit deposit account
        self.deposit_account_view(
            account_number=other_deposit_account_mask,
            account_status=status_normal,
            current_balance=current_balance_other
        )

# PASSBOOK FOR SAVINGS
    def test_014_passbook_for_savings_01_dpt_srg_stock_registration_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global from_serial_sb, to_serial_sb
        generated_number = self.gen_serial_number(stock_prefix_sb, stock_type_sb, 9)
        print(f'generated_number: {generated_number}')
        from_serial = generated_number[0]
        to_serial = generated_number[1]
        dpt_srg_result = self.dpt_srg(
            stock_type=stock_type_sb,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix_sb,
            number_of_leaves=number_of_leaves_sb,
            number_of_book=number_of_book_sb,
            approve_later='Y'
        )
        transaction_references=dpt_srg_result[0]
        from_serial_sb = dpt_srg_result[1]
        to_serial_sb = dpt_srg_result[2]
        self.assertEqual(from_serial_sb, from_serial)
        self.assertEqual(to_serial_sb, to_serial)
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )

    def test_014_passbook_for_savings_02_dpt_sat_stock_assign_to_staff_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_sat_result = self.dpt_sat(
            stock_type=stock_type_sb,
            from_serial=from_serial_sb,
            to_serial=to_serial_sb,
            assigned_staff_code=username
        )
        self.assertEqual(from_serial_sb, dpt_sat_result[1])
        self.assertEqual(to_serial_sb, dpt_sat_result[2])

    def test_014_passbook_for_savings_03_dpt_ccr_stock_confirm_received_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_ccr_result = self.dpt_ccr(
            stock_type=stock_type_sb,
            from_serial=from_serial_sb,
            to_serial=to_serial_sb,
            approve_later='Y'
        )
        self.assertEqual(from_serial_sb, dpt_ccr_result[1])
        self.assertEqual(to_serial_sb, dpt_ccr_result[2])
        self.transaction_approve(
            transaction_references=dpt_ccr_result[0], 
            username=username_approve,
            password=password_approve
        )

    def test_014_passbook_for_savings_04_dpt_sbi_cheque_book_issued_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_sbi_result = self.dpt_sbi(
            account_number=deposit_account_saving_mask,
            serial_no=from_serial_sb
        )
        transaction_numbers.append(dpt_sbi_result[0])
        self.assertEqual(from_serial_sb, dpt_sbi_result[1])
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            passbook_or_receipt_number=str(from_serial_sb).replace('-',''),
            current_balance=current_balance_3rd,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_015_savings_01_dpt_trf_transfer_money_to_other_deposit_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_trf_result = self.dpt_trf(
            debit_account=deposit_account_saving_mask,
            amount=withdraw_amount.replace(',', ''),
            credit_account=other_deposit_account_mask,
            passbook_number=from_serial_sb,
            approve_later='Y'
        )
        transaction_references=dpt_trf_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_saving_mask, dpt_trf_result[1])
        self.assertEqual(other_deposit_account_mask, dpt_trf_result[2])
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # verify debit deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            passbook_or_receipt_number=str(from_serial_sb).replace('-',''),
            current_balance=current_balance_withdrawal_1st,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        # verify credit deposit account
        self.deposit_account_view(
            account_number=other_deposit_account_mask,
            account_status=status_normal,
            current_balance=current_balance_other_2nd
        )

    def test_015_savings_02_dpt_cwr_cash_withdrawal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_cwr_result = self.dpt_cwr(
            account_number=deposit_account_saving_mask,
            withdraw_amount=withdraw_amount.replace(',', ''),
            passbook_number=from_serial_sb,
            approve_later='Y'
        )
        transaction_references=dpt_cwr_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_saving_mask, dpt_cwr_result[1])
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            passbook_or_receipt_number=str(from_serial_sb).replace('-',''),
            current_balance=current_balance_withdrawal_2nd,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_015_savings_03_dpt_mwr_miscellaneous_withdrawal_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_mwr_result = self.dpt_mwr(
            account_number=deposit_account_saving_mask,
            withdraw_amount=withdraw_amount,
            credit_accounting=gl_account_number,
            passbook_number=from_serial_sb,
            approve_later='Y'
        )
        transaction_references=dpt_mwr_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_saving_mask, dpt_mwr_result[1])
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_withdrawal_3rd,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_016_savings_01_dpt_cas_change_account_status_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # change from 'Normal' to 'Dormant'
        dpt_cas_result = self.dpt_cas(
            account_number=deposit_account_saving_mask,
            new_status=status_dormant,
            current_status=status_normal,
            approve_later='Y'
        )
        transaction_references=dpt_cas_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_saving_mask, dpt_cas_result[1])
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_dormant,
            dormant_date=working_date,
            last_change_dormant_to_normal_date='',
            passbook_or_receipt_number=from_serial_sb,
            # current_balance=current_balance_withdrawal_3rd,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        # change from 'Dormant' to 'Normal'
        dpt_cas_result = self.dpt_cas(
            account_number=deposit_account_saving_mask,
            new_status=status_normal,
            current_status=status_dormant,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        transaction_references=dpt_cas_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_saving_mask, dpt_cas_result[1])
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            dormant_date=working_date,
            last_change_dormant_to_normal_date=working_date,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_withdrawal_3rd,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_017_savings_01_dpt_blk_block_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_blk_result = self.dpt_blk(
            account_number=deposit_account_saving_mask,
            approve_later='Y'
        )
        transaction_references=dpt_blk_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_saving_mask, dpt_blk_result[1])
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_block,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_withdrawal_3rd,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_017_savings_02_dpt_rls_release_block_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_rls_result = self.dpt_rls(
            account_number=deposit_account_saving_mask,
            approve_later='Y'
        )
        transaction_references=dpt_rls_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_saving_mask, dpt_rls_result[1])
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_withdrawal_3rd,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_018_savings_01_dpt_emk_hold_balance_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        hold_amount='200,000.45'
        dpt_emk_result = self.dpt_emk(
            account_number=deposit_account_saving_mask,
            hold_amount=hold_amount,
            expired_date=working_date,
            reference_code='Other',
            approve_later='Y'
        )
        transaction_references=dpt_emk_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_saving_mask, dpt_emk_result[1])
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_withdrawal_3rd,
            earmark_block_amount=hold_amount,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_018_savings_02_dpt_erl_release_hold_balance_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        hold_amount='200,000.45'
        dpt_erl_result = self.dpt_erl(
            account_number=deposit_account_saving_mask,
            holding_amount=hold_amount,
            earmark_amount=hold_amount,
            expired_date=working_date,
            reference_code='Other',
            approve_later='Y'
        )
        transaction_references=dpt_erl_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_saving_mask, dpt_erl_result[1])
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_withdrawal_3rd,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_019_savings_01_dpt_dls_close_deposit_account_by_deposit_success(self):
        # view account before close
        # self.deposit_account_view(
        #     account_number=deposit_account_saving_mask,
        #     current_balance=current_balance_withdrawal_3rd,
        #     interest_accrual=expected_interest_accrual
        # )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # close deposit account
        dpt_dls_result = self.dpt_dls(
            account_number=deposit_account_saving_mask,
            another_deposit_account=other_deposit_account_mask,
            balance=current_balance_withdrawal_3rd,
            interest_payable_receivable=expected_interest_accrual,
            interest_due='0.00',
            interest_re_calculate='0.00',
            gross_paid_interest_amount='0.00',
            penalty_fee='0.00',
            balance_received=current_balance_withdrawal_3rd,
            approve_later='Y'
        )
        self.assertEqual(deposit_account_saving_mask, dpt_dls_result[1])
        self.transaction_approve(
            transaction_references=dpt_dls_result[0], 
            username=username_approve,
            password=password_approve
        )
        # view account after close
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
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
            account_number=deposit_account_saving_mask,
            current_balance=current_balance_withdrawal_3rd,
            interest_accrual=expected_interest_accrual
        )

    def test_019_savings_02_dpt_mls_close_deposit_account_by_gl_success(self):
        # view account before close
        # self.deposit_account_view(
        #     account_number=deposit_account_saving_mask,
        #     current_balance=current_balance_withdrawal_3rd,
        #     interest_accrual=expected_interest_accrual
        # )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # close deposit account
        dpt_mls_result = self.dpt_mls(
            account_number=deposit_account_saving_mask,
            accounting_number=gl_account_number,
            balance=current_balance_withdrawal_3rd,
            interest_payable_receivable=expected_interest_accrual,
            interest_due='0.00',
            interest_re_calculate='0.00',
            gross_paid_interest_amount='0.00',
            penalty_fee='0.00',
            balance_received=current_balance_withdrawal_3rd,
            approve_later='Y'
        )
        self.assertEqual(deposit_account_saving_mask, dpt_mls_result[1])
        self.transaction_approve(
            transaction_references=dpt_mls_result[0], 
            username=username_approve,
            password=password_approve
        )
        # view account after close
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
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
            account_number=deposit_account_saving_mask,
            current_balance=current_balance_withdrawal_3rd,
            interest_accrual=expected_interest_accrual
        )

    def test_019_savings_03_dpt_cls_close_deposit_account_by_cash_success(self):
        # view account before close
        # self.deposit_account_view(
        #     account_number=deposit_account_saving_mask,
        #     current_balance=current_balance_withdrawal_3rd,
        #     interest_accrual=expected_interest_accrual
        # )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # close deposit account
        dpt_cls_result = self.dpt_cls(
            account_number=deposit_account_saving_mask,
            balance=current_balance_withdrawal_3rd,
            interest_payable_receivable=expected_interest_accrual,
            interest_due='0.00',
            interest_re_calculate='0.00',
            gross_paid_interest_amount='0.00',
            penalty_fee='0.00',
            balance_received=current_balance_withdrawal_3rd,
            approve_later='Y'
        )
        self.assertEqual(deposit_account_saving_mask, dpt_cls_result[1])
        self.transaction_approve(
            transaction_references=dpt_cls_result[0], 
            username=username_approve,
            password=password_approve
        )
        # view account after close
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
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
            account_number=deposit_account_saving_mask,
            current_balance=current_balance_withdrawal_3rd,
            interest_accrual=expected_interest_accrual
        )

    def test_020_savings_01_dpt_his_transaction_history_inquiry_success(self):
        # close deposit again
        dpt_cls_result = self.dpt_cls(
            account_number=deposit_account_saving_mask,
            balance=current_balance_withdrawal_3rd,
            interest_payable_receivable=expected_interest_accrual,
            interest_due='0.00',
            interest_re_calculate='0.00',
            gross_paid_interest_amount='0.00',
            penalty_fee='0.00',
            balance_received=current_balance_withdrawal_3rd,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        transaction_numbers.append(dpt_cls_result[0])
        self.assertEqual(deposit_account_saving_mask, dpt_cls_result[1])
        # view account after close success
        self.deposit_account_view(
            account_number=deposit_account_saving_mask,
            current_balance='0.00',
            interest_accrual='0.00'
        )
        expected_trans_code=['DPT_OPN','DPT_APR','DPT_CDP','DPT_MDP','DPT_TRF','DPT_SBI','DPT_TRF','DPT_CWR','DPT_MWR','DPT_CAS','DPT_CAS','DPT_BLK','DPT_RLS','DPT_EMK','DPT_ERL','DPT_CLS']
        expected_users=[username] * 16
        expected_channels=['Core Banking'] * 16
        expected_debits=['0.00'] * 6 + ['1,000,000.54'] * 3 + ['0.00'] * 6 + ['11,999,999.85']
        expected_credits=['0.00'] * 2 + ['5,000,000.49'] * 3 + ['0.00'] * 11
        expected_balances=['0.00'] * 2 + ['5,000,000.49'] + ['10,000,000.98'] + ['15,000,001.47'] * 2 + ['14,000,000.93'] + ['13,000,000.39'] + ['11,999,999.85'] * 7 + ['0.00']
        expected_dates=[working_date] * 16
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        dpt_his_result = self.dpt_his(
            account_number=deposit_account_saving_mask,
            transaction_numbers=transaction_numbers,
            expected_transaction_codes=expected_trans_code,
            expected_debits=expected_debits,
            expected_credits=expected_credits,
            expected_balances=expected_balances,
            expected_created_bys=expected_users,
            expected_channels=expected_channels,
            expected_transaction_dates=expected_dates
        )
        self.assertEqual(deposit_account_saving_mask, dpt_his_result[1])

if __name__ == '__main__':
    webui_test.main()