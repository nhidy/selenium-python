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

# data test for 'Passbook for Fixed Deposit'
stock_type_fb = 'Passbook for Fixed Deposit'
stock_prefix_fb = 'FB'
number_of_leaves_fb = '1'
number_of_book_fb = '1'

# data test for fixed deposit account
catalogue_code='FD01POMMK'
deposit_type='Fixed Deposit'
deposit_sub_type='Fixed Deposit Account - 1 M'
rollover_option='Principal rollover only'
auto_transfer_option='Auto collection(transfer) for Interest'

reason_of_account_opening='Reason opening FD 1M (T1) account'
expected_account_gl_name='DEPOSIT'
expected_ifc_codes=['114'] * 2
expected_ifc_gl_names=['PAID_INTEREST', 'INTEREST']
# data test for deposit money
amount_deposit_mask='50,000,000.49'
current_balance_1st='50,000,000.49'
amount_deposit_to_other_mask='51,000,000.96'
current_balance_other_1st_after_trf='1,000,000.47'
current_balance_other_2nd_after_dls='101,000,001.45'
# data test for withdrawal money
withdraw_amount='5,000,000.54'
# data test for close
balance_close=current_balance_1st
interest_payable_receivable='0.00'
interest_due='0.00'
interest_re_calculate='0.00'
gross_paid_interest_amount='0.00'
penalty_fee='0.00'
balance_received=current_balance_1st
# data test deposit status
status_pending='Pending to approve'
status_new='New'
status_normal='Normal'
status_dormant='Dormant'
status_block='Block'
status_closed='Closed'
status_reject='Reject'
# data test for close deposit account
expected_interest_accrual='0.00'
transaction_numbers=[]

class Deposit1MPrincipalRolloverOnlyTest(FormAction):
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
        global expected_account_gl_number, expected_ifc_gl_numbers, expected_other_account_gl_number
        expected_account_gl_number=f'{branch_code}-2020302030101-01'
        expected_ifc_gl_numbers=[f'{branch_code}-4010201010101-01', f'{branch_code}-2070101000202-01']
        global gl_account_number, gl_cash
        gl_account_number=f'{branch_code}-1100601000000-01'
        gl_cash=f'{branch_code}-1010301000101-01'
        expected_other_account_gl_number=f'{branch_code}-2020301010202-01'

    def start_class(self):
        self.data_begin()

    def end_class(self):
        self.logout()

    def reset_browser(self):
        self.logout()
        self.restart_browser()
        self.data_begin()

# Check the data used for testing
    def test_000_01_check_test_data_must_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=gl_account_number
        )
        if self.check_customer_profile_not_exist(customer_code_personal):
            self.stop()
            self.fail()

# Create other deposit account use for testing
    def test_000_02_create_other_deposit_account_use_for_testing(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
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

# FIXED DEPOSIT (FD) 1 MONTH - PRINCIPAL ROLLOVER ONLY (T1)
    def test_001_fixed_1m_dpt_opn_open_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_account_fd_mask
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code,
            reason_of_account_opening=reason_of_account_opening,
            to_account_number=other_deposit_account_mask,
            mpu_card=True,
            passbook_cheque_book=True
        )
        transaction_numbers.append(dpt_opn_result[0])
        deposit_account_fd_mask=dpt_opn_result[1]
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
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

    def test_002_fixed_1m_dpt_apr_approve_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_apr_result = self.dpt_apr(
            account_number=deposit_account_fd_mask,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        transaction_numbers.append(dpt_apr_result[0])
        account_number_actual_mask=dpt_apr_result[1]
        self.assertEqual(account_number_actual_mask, deposit_account_fd_mask)
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
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

    def test_003_fixed_1m_dpt_mdp_miscellaneous_deposit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_mdp_result = self.dpt_mdp(
            account_number=deposit_account_fd_mask,
            amount_deposit=amount_deposit_mask,
            debit_accounting=gl_account_number,
            approve_later='Y'
        )
        transaction_references=dpt_mdp_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_fd_mask, dpt_mdp_result[1])
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            current_balance=current_balance_1st,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

# PASSBOOK FOR FIXED DEPOSIT
    def test_004_passbook_for_fixed_1m_dpt_srg_stock_registration_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global from_serial_sb, to_serial_sb
        generated_number = self.gen_serial_number(stock_prefix_fb, stock_type_fb, 0)
        print(f'generated_number: {generated_number}')
        from_serial = generated_number[0]
        to_serial = generated_number[1]
        dpt_srg_result = self.dpt_srg(
            stock_type=stock_type_fb,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix_fb,
            number_of_leaves=number_of_leaves_fb,
            number_of_book=number_of_book_fb,
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

    def test_005_passbook_for_fixed_1m_dpt_sat_stock_assign_to_staff_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_sat_result = self.dpt_sat(
            stock_type=stock_type_fb,
            from_serial=from_serial_sb,
            to_serial=to_serial_sb,
            assigned_staff_code=username
        )
        self.assertEqual(from_serial_sb, dpt_sat_result[1])
        self.assertEqual(to_serial_sb, dpt_sat_result[2])

    def test_006_passbook_for_fixed_1m_dpt_ccr_stock_confirm_received_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_ccr_result = self.dpt_ccr(
            stock_type=stock_type_fb,
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

    def test_007_passbook_for_fixed_1m_dpt_fbi_book_issue_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_sbi_result = self.dpt_fbi(
            account_number=deposit_account_fd_mask,
            serial_no=from_serial_sb,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        transaction_numbers.append(dpt_sbi_result[0])
        self.assertEqual(from_serial_sb, dpt_sbi_result[1])
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            passbook_or_receipt_number=str(from_serial_sb).replace('-',''),
            current_balance=current_balance_1st,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_008_fixed_1m_dpt_cwr_cash_withdrawal_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [
            'Passbook number: Can not be blank'
        ]
        self.dpt_cwr(
            account_number=deposit_account_fd_mask,
            withdraw_amount=withdraw_amount,
            withdrawer_name='Test',
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            passbook_or_receipt_number=str(from_serial_sb).replace('-',''),
            current_balance=current_balance_1st,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_009_fixed_1m_dpt_mwr_miscellaneous_withdrawal_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        deposit_account_fd = str(deposit_account_fd_mask).replace('-','')
        list_error_message = [
            f'InvalidDpttype: Invalid deposit type of account [{deposit_account_fd}]- en'
        ]
        self.dpt_mwr(
            account_number=deposit_account_fd_mask,
            withdraw_amount=withdraw_amount,
            credit_accounting=gl_account_number,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            passbook_or_receipt_number=str(from_serial_sb).replace('-',''),
            current_balance=current_balance_1st,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
    
    def test_010_fixed_1m_dpt_trf_transfer_money_to_other_deposit_account_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        deposit_account_fd = str(deposit_account_fd_mask).replace('-','')
        list_error_message = [
            f'InvalidDpttype: Invalid deposit type of account [{deposit_account_fd}]- en'
        ]
        self.dpt_trf(
            debit_account=deposit_account_fd_mask,
            amount=withdraw_amount,
            credit_account=other_deposit_account_mask,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message
        )
        # verify debit deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            passbook_or_receipt_number=str(from_serial_sb).replace('-',''),
            current_balance=current_balance_1st,
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
            current_balance=amount_deposit_to_other_mask
        )

    def test_011_fixed_1m_dpt_cas_change_account_status_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # change from 'Normal' to 'Dormant'
        dpt_cas_result = self.dpt_cas(
            account_number=deposit_account_fd_mask,
            new_status=status_dormant,
            current_status=status_normal,
            approve_later='Y'
        )
        transaction_references=dpt_cas_result[0]
        self.assertEqual(deposit_account_fd_mask, dpt_cas_result[1])
        deposit_account_fd = str(deposit_account_fd_mask).replace('-', '')
        list_error_message = [
            f'Invalid deposit type [Fixed Deposit] of account [{deposit_account_fd}]- en'
        ]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve,
            allow_approve='N',
            list_error_message=list_error_message
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            dormant_date='',
            last_change_dormant_to_normal_date='',
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_1st,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_012_fixed_1m_dpt_blk_block_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_blk_result = self.dpt_blk(
            account_number=deposit_account_fd_mask,
            approve_later='Y'
        )
        transaction_references=dpt_blk_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_fd_mask, dpt_blk_result[1])
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_block,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_1st,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_013_fixed_1m_dpt_rls_release_block_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_rls_result = self.dpt_rls(
            account_number=deposit_account_fd_mask,
            approve_later='Y'
        )
        transaction_references=dpt_rls_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_fd_mask, dpt_rls_result[1])
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_1st,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_014_fixed_1m_dpt_emk_hold_balance_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        hold_amount='200,000.45'
        dpt_emk_result = self.dpt_emk(
            account_number=deposit_account_fd_mask,
            hold_amount=hold_amount,
            expired_date=working_date,
            reference_code='Other',
            approve_later='Y'
        )
        transaction_references=dpt_emk_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_fd_mask, dpt_emk_result[1])
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_1st,
            earmark_block_amount=hold_amount,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_015_fixed_1m_dpt_erl_release_hold_balance_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        hold_amount='200,000.45'
        dpt_erl_result = self.dpt_erl(
            account_number=deposit_account_fd_mask,
            holding_amount=hold_amount,
            earmark_amount=hold_amount,
            expired_date=working_date,
            reference_code='Other',
            approve_later='Y'
        )
        transaction_references=dpt_erl_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(deposit_account_fd_mask, dpt_erl_result[1])
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_1st,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_016_fixed_1m_dpt_dls_close_deposit_account_by_deposit_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.dpt_dls_error(
            account_number=deposit_account_fd_mask,
            error_message=f'Deposit account [{self.no_mask(deposit_account_fd_mask)}] is linked'
        )

    def test_017_fixed_1m_dpt_mls_close_deposit_account_by_gl_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.dpt_mls_error(
            account_number=deposit_account_fd_mask,
            error_message=f'Deposit account [{self.no_mask(deposit_account_fd_mask)}] is linked'
        )

    def test_018_fixed_1m_dpt_cls_close_deposit_account_by_cash_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.dpt_cls_error(
            account_number=deposit_account_fd_mask,
            error_message=f'Deposit account [{self.no_mask(deposit_account_fd_mask)}] is linked'
        )

# DELETE ACCOUNT LINKAGE
    def test_019_fixed_1m_delete_account_linkage_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify deposit account before
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_1st,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        dpt_account_linkage_delete_result = self.dpt_account_linkage_delete(
            master_account_number=deposit_account_fd_mask
        )
        self.assertEqual(str(deposit_account_fd_mask).replace('-', ''), dpt_account_linkage_delete_result)
        # verify deposit account after
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            current_balance=current_balance_1st,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_020_fixed_1m_dpt_dls_close_deposit_account_by_deposit_success(self):
        # view account before close
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance=current_balance_1st,
            interest_accrual=expected_interest_accrual,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # close deposit account
        dpt_dls_result = self.dpt_dls(
            account_number=deposit_account_fd_mask,
            another_deposit_account=other_deposit_account_mask,
            balance=balance_close,
            interest_payable_receivable=interest_payable_receivable,
            interest_due=interest_due,
            interest_re_calculate=interest_re_calculate,
            gross_paid_interest_amount=gross_paid_interest_amount,
            penalty_fee=penalty_fee,
            balance_received=balance_received,
            approve_later='Y'
        )
        self.assertEqual(deposit_account_fd_mask, dpt_dls_result[1])
        self.transaction_approve(
            transaction_references=dpt_dls_result[0], 
            username=username_approve,
            password=password_approve
        )
        # view transaction
        self.transaction_view(
            transaction_references=dpt_dls_result[0]
        )
        self.assertEqual(deposit_account_fd_mask, dpt_dls_result[1])
        # verify posting
        expected_posting_01 = {
            'expected_debits': [
                (expected_account_gl_number, balance_close),
            ],
            'expected_credits': [
                (expected_other_account_gl_number, balance_close),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account after close
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance='0.00',
            interest_accrual='0.00',
            account_status=status_closed,
            passbook_or_receipt_number=from_serial_sb,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        # view another account after close
        self.deposit_account_view(
            account_number=other_deposit_account_mask,
            current_balance=current_balance_other_2nd_after_dls,
            account_status=status_normal,
            earmark_block_amount='0.00',
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_other_account_gl_number
        )
        self.transaction_reverse(
            transaction_references=dpt_dls_result[0],
            username=username_reverse,
            password=password_reverse
        )
        # view account after reverse close
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance=current_balance_1st,
            interest_accrual=expected_interest_accrual,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_021_fixed_1m_dpt_mls_close_deposit_account_by_gl_success(self):
        # view account before close
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance=current_balance_1st,
            interest_accrual=expected_interest_accrual,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # close deposit account
        dpt_mls_result = self.dpt_mls(
            account_number=deposit_account_fd_mask,
            accounting_number=gl_account_number,
            balance=balance_close,
            interest_payable_receivable=interest_payable_receivable,
            interest_due=interest_due,
            interest_re_calculate=interest_re_calculate,
            gross_paid_interest_amount=gross_paid_interest_amount,
            penalty_fee=penalty_fee,
            balance_received=balance_received,
            approve_later='Y'
        )
        self.assertEqual(deposit_account_fd_mask, dpt_mls_result[1])
        self.transaction_approve(
            transaction_references=dpt_mls_result[0],
            username=username_approve,
            password=password_approve
        )
        # view transaction
        self.transaction_view(
            transaction_references=dpt_mls_result[0]
        )
        self.assertEqual(deposit_account_fd_mask, dpt_mls_result[1])
        # verify posting
        expected_posting_01 = {
            'expected_debits': [
                (expected_account_gl_number, balance_close),
            ],
            'expected_credits': [
                (gl_account_number, balance_close),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account after close
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance='0.00',
            interest_accrual='0.00',
            account_status=status_closed,
            passbook_or_receipt_number=from_serial_sb,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        self.transaction_reverse(
            transaction_references=dpt_mls_result[0],
            username=username_reverse,
            password=password_reverse
        )
        # view account after reverse close
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance=current_balance_1st,
            interest_accrual=expected_interest_accrual,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_022_fixed_1m_dpt_cls_close_deposit_account_by_cash_success(self):
        # view account before close
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance=current_balance_1st,
            interest_accrual=expected_interest_accrual,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        self.dpt_cdp(
            account_number=other_deposit_account_mask,
            amount_deposit=current_balance_1st,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # close deposit account
        dpt_cls_result = self.dpt_cls(
            account_number=deposit_account_fd_mask,
            balance=balance_close,
            interest_payable_receivable=interest_payable_receivable,
            interest_due=interest_due,
            interest_re_calculate=interest_re_calculate,
            gross_paid_interest_amount=gross_paid_interest_amount,
            penalty_fee=penalty_fee,
            balance_received=balance_received,
            approve_later='Y'
        )
        self.assertEqual(deposit_account_fd_mask, dpt_cls_result[1])
        self.transaction_approve(
            transaction_references=dpt_cls_result[0], 
            username=username_approve,
            password=password_approve
        )
        # view transaction
        self.transaction_view(
            transaction_references=dpt_cls_result[0]
        )
        self.assertEqual(deposit_account_fd_mask, dpt_cls_result[1])
        # verify posting
        expected_posting_01 = {
            'expected_debits': [
                (expected_account_gl_number, balance_close),
            ],
            'expected_credits': [
                (gl_cash, balance_close),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account after close
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance='0.00',
            interest_accrual='0.00',
            account_status=status_closed,
            passbook_or_receipt_number=from_serial_sb,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        self.transaction_reverse(
            transaction_references=dpt_cls_result[0],
            username=username_reverse,
            password=password_reverse
        )
        # view account after reverse close
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance=current_balance_1st,
            interest_accrual=expected_interest_accrual,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_sb,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )

    def test_023_fixed_1m_dpt_his_transaction_history_inquiry_success(self):
        # close deposit again
        dpt_mls_result = self.dpt_mls(
            account_number=deposit_account_fd_mask,
            accounting_number=gl_account_number,
            balance=balance_close,
            interest_payable_receivable=interest_payable_receivable,
            interest_due=interest_due,
            interest_re_calculate=interest_re_calculate,
            gross_paid_interest_amount=gross_paid_interest_amount,
            penalty_fee=penalty_fee,
            balance_received=balance_received,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        transaction_numbers.append(dpt_mls_result[0])
        self.assertEqual(deposit_account_fd_mask, dpt_mls_result[1])
        # verify posting
        expected_posting_01 = {
            'expected_debits': [
                (expected_account_gl_number, balance_close),
            ],
            'expected_credits': [
                (gl_account_number, balance_close),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account after close success
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance='0.00',
            interest_accrual='0.00',
            account_status=status_closed,
            passbook_or_receipt_number=from_serial_sb,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers
        )
        expected_trans_code=['DPT_OPN','DPT_APR','DPT_MDP','DPT_FBI','DPT_BLK','DPT_RLS','DPT_EMK','DPT_ERL','DPT_MLS']
        expected_users=[username] * 9
        expected_channels=['Core Banking'] * 9
        expected_debits=['0.00'] * 8 + [current_balance_1st]
        expected_credits=['0.00'] * 2 + [current_balance_1st] + ['0.00'] * 6
        expected_balances=['0.00'] * 2 + [current_balance_1st] * 6 + ['0.00']
        expected_dates=[working_date] * 9
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        dpt_his_result = self.dpt_his(
            account_number=deposit_account_fd_mask,
            transaction_numbers=transaction_numbers,
            expected_transaction_codes=expected_trans_code,
            expected_debits=expected_debits,
            expected_credits=expected_credits,
            expected_balances=expected_balances,
            expected_created_bys=expected_users,
            expected_channels=expected_channels,
            expected_transaction_dates=expected_dates
        )
        self.assertEqual(deposit_account_fd_mask, dpt_his_result[1])

if __name__ == '__main__':
    webui_test.main()