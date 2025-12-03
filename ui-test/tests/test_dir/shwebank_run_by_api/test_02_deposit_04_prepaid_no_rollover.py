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
CUSTOMER_CODE_CORPORATE = os.getenv("TEST_CONFIG_CUSTOMER_CODE_CORPORATE", "")
USERNAME_APPROVE = os.getenv("TEST_CONFIG_USERNAME_APPROVE", "")
PASSWORD_APPROVE = os.getenv("TEST_CONFIG_PASSWORD_APPROVE", "")
USERNAME_REVERSE = os.getenv("TEST_CONFIG_USERNAME_REVERSE", "")
PASSWORD_REVERSE = os.getenv("TEST_CONFIG_PASSWORD_REVERSE", "")

customer_code_personal = CUSTOMER_CODE
customer_code_corporate = CUSTOMER_CODE_CORPORATE

# data test for 'Receipt'
stock_type_fr = 'Receipt'
stock_prefix_fr = 'FR'
number_of_leaves_fr = '1'
number_of_book_fr = '1'

# data test for prepaid fixed deposit
catalogue_code='PR007MMK1'
deposit_type='Fixed Deposit'
deposit_sub_type='Shwe Prepaid Fixed Deposit Account'
rollover_option='No rollover'
auto_transfer_option='Auto collection(transfer) for both P and I'
reason_of_account_opening='Reason opening prepaid FD (T6) account'
# 
expected_account_gl_name='DEPOSIT'
expected_ifc_codes=['155'] * 2
expected_ifc_gl_names=['PREPAID_INTEREST', 'PAID_INTEREST']
# data test for deposit money
amount_deposit_mask='50,000,000.49'
interest_prepaid = '81,506.88'
# data test for other account
amount_deposit_to_other_mask='51,000,000.96'
current_balance_other_1st_receive_interest='1,081,507.35'
# data test for withdrawal money
withdraw_amount='5,000,000.54'
# data test for close
balance_close='49,918,493.61'
interest_payable_receivable='0.00'
interest_due='0.00'
interest_re_calculate='0.00'
gross_paid_interest_amount='0.00'
penalty_fee='0.00'
# balance_received=current_balance_1st
balance_received=amount_deposit_mask
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

class DepositPrepaidNoRolloverTest(FormAction):
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
        global expected_account_gl_number, expected_ifc_gl_numbers, expected_other_account_gl_number, expected_ifc_gl_prepaid_interest, expected_ifc_gl_paid_interest
        expected_account_gl_number=f'{branch_code}-2020202032020-01'
        expected_ifc_gl_prepaid_interest=f'{branch_code}-1100701001212-01'
        expected_ifc_gl_paid_interest=f'{branch_code}-4010201011414-01'
        expected_ifc_gl_numbers=[expected_ifc_gl_prepaid_interest, expected_ifc_gl_paid_interest]
        global gl_account_number, gl_cash, ifcc_gl_number_346, ifcc_gl_number_302
        gl_account_number=f'{branch_code}-1100601000000-01'
        gl_cash=f'{branch_code}-1010301000101-01'
        expected_other_account_gl_number=f'{branch_code}-2020301010202-01'
        ifcc_gl_number_346=f'{branch_code}-2070501000101-01'
        ifcc_gl_number_302=f'{branch_code}-3030301000101-01'

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
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=expected_account_gl_number
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=expected_other_account_gl_number
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=expected_ifc_gl_prepaid_interest
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=expected_ifc_gl_paid_interest
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

# PREPAID FIXED DEPOSIT - PRINCIPAL ROLLOVER ONLY (T6)
    def test_001_prepaid_7d_dpt_opn_open_account_success(self):
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
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_002_prepaid_7d_dpt_apr_approve_account_success(self):
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
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_003_prepaid_7d_dpt_trf_get_money_from_other_deposit_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_trf_result = self.dpt_trf(
            debit_account=other_deposit_account_mask,
            amount=amount_deposit_mask,
            credit_account=deposit_account_fd_mask,
            approve_later='Y'
        )
        transaction_references=dpt_trf_result[0]
        transaction_numbers.append(transaction_references)
        self.assertEqual(other_deposit_account_mask, dpt_trf_result[1])
        self.assertEqual(deposit_account_fd_mask, dpt_trf_result[2])
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # verify prepaid fixed deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            current_balance=amount_deposit_mask,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )
        # verify other deposit account
        self.deposit_account_view(
            account_number=other_deposit_account_mask,
            account_status=status_normal,
            current_balance=current_balance_other_1st_receive_interest
        )

# RECEIPT FOR PREPAID INTEREST FIXED DEPOSIT
    def test_004_receipt_for_prepaid_7d_dpt_srg_stock_registration_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global from_serial_fr, to_serial_fr
        generated_number = self.gen_serial_number(stock_prefix_fr, stock_type_fr, 0)
        print(f'generated_number: {generated_number}')
        from_serial = generated_number[0]
        to_serial = generated_number[1]
        dpt_srg_result = self.dpt_srg(
            stock_type=stock_type_fr,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix_fr,
            number_of_leaves=number_of_leaves_fr,
            number_of_book=number_of_book_fr,
            approve_later='Y'
        )
        transaction_references=dpt_srg_result[0]
        from_serial_fr = dpt_srg_result[1]
        to_serial_fr = dpt_srg_result[2]
        self.assertEqual(from_serial_fr, from_serial)
        self.assertEqual(to_serial_fr, to_serial)
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )

    def test_005_receipt_for_prepaid_7d_dpt_sat_stock_assign_to_staff_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_sat_result = self.dpt_sat(
            stock_type=stock_type_fr,
            from_serial=from_serial_fr,
            to_serial=to_serial_fr,
            assigned_staff_code=username
        )
        self.assertEqual(from_serial_fr, dpt_sat_result[1])
        self.assertEqual(to_serial_fr, dpt_sat_result[2])

    def test_006_receipt_for_prepaid_7d_dpt_ccr_stock_confirm_received_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_ccr_result = self.dpt_ccr(
            stock_type=stock_type_fr,
            from_serial=from_serial_fr,
            to_serial=to_serial_fr,
            approve_later='Y'
        )
        self.assertEqual(from_serial_fr, dpt_ccr_result[1])
        self.assertEqual(to_serial_fr, dpt_ccr_result[2])
        self.transaction_approve(
            transaction_references=dpt_ccr_result[0], 
            username=username_approve,
            password=password_approve
        )

    def test_007_receipt_for_prepaid_7d_dpt_cer_receipt_issue_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_cer_result = self.dpt_cer(
            account_number=deposit_account_fd_mask,
            cerfiticate_serial=from_serial_fr,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        transaction_numbers.append(dpt_cer_result[0])
        self.assertEqual(from_serial_fr, dpt_cer_result[1])
        # verify deposit account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            passbook_or_receipt_number=str(from_serial_fr).replace('-',''),
            current_balance=amount_deposit_mask,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_008_prepaid_7d_dpt_cwr_cash_withdrawal_error(self):
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
            passbook_or_receipt_number=str(from_serial_fr).replace('-',''),
            current_balance=amount_deposit_mask,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_009_prepaid_7d_dpt_mwr_miscellaneous_withdrawal_error(self):
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
            passbook_or_receipt_number=str(from_serial_fr).replace('-',''),
            current_balance=amount_deposit_mask,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_010_prepaid_7d_dpt_trf_transfer_money_to_other_deposit_account_error(self):
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
            passbook_or_receipt_number=str(from_serial_fr).replace('-',''),
            current_balance=amount_deposit_mask,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )
        # verify credit deposit account
        self.deposit_account_view(
            account_number=other_deposit_account_mask,
            account_status=status_normal,
            current_balance=current_balance_other_1st_receive_interest
        )

    def test_011_prepaid_7d_dpt_cas_change_account_status_error(self):
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
            passbook_or_receipt_number=from_serial_fr,
            current_balance=amount_deposit_mask,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_012_prepaid_7d_dpt_blk_block_account_success(self):
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
            passbook_or_receipt_number=from_serial_fr,
            current_balance=amount_deposit_mask,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_013_prepaid_7d_dpt_rls_release_block_account_success(self):
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
            passbook_or_receipt_number=from_serial_fr,
            current_balance=amount_deposit_mask,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_014_prepaid_7d_dpt_emk_hold_balance_success(self):
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
            passbook_or_receipt_number=from_serial_fr,
            current_balance=amount_deposit_mask,
            earmark_block_amount=hold_amount,
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_015_prepaid_7d_dpt_erl_release_hold_balance_success(self):
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
            passbook_or_receipt_number=from_serial_fr,
            current_balance=amount_deposit_mask,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_016_prepaid_7d_dpt_dls_close_deposit_account_is_linked_by_deposit_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.dpt_dls_error(
            account_number=deposit_account_fd_mask,
            error_message=f'Deposit account [{self.no_mask(deposit_account_fd_mask)}] is linked'
        )
        self.dpt_dls_error(
            account_number=deposit_account_fd_mask,
            another_deposit_account=other_deposit_account_mask,
            list_error_message=[f'AccountIsLinked: Deposit account [{self.no_mask(deposit_account_fd_mask)}] is linked']
        )

    def test_017_prepaid_7d_dpt_mls_close_deposit_account_is_linked_by_gl_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.dpt_mls_error(
            account_number=deposit_account_fd_mask,
            error_message=f'Deposit account [{self.no_mask(deposit_account_fd_mask)}] is linked'
        )
        self.dpt_mls_error(
            account_number=deposit_account_fd_mask,
            accounting_number=gl_account_number,
            list_error_message=[f'AccountIsLinked: Deposit account [{self.no_mask(deposit_account_fd_mask)}] is linked']
        )

    def test_018_prepaid_7d_dpt_cls_close_deposit_account_is_linked_by_cash_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.dpt_cls_error(
            account_number=deposit_account_fd_mask,
            error_message=f'Deposit account [{self.no_mask(deposit_account_fd_mask)}] is linked'
        )
        self.dpt_cls_error(
            account_number=deposit_account_fd_mask,
            gross_paid_interest_amount='0.00',
            list_error_message=[f'AccountIsLinked: Deposit account [{self.no_mask(deposit_account_fd_mask)}] is linked']
        )

# DELETE ACCOUNT LINKAGE
    def test_019_prepaid_7d_delete_account_linkage_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify deposit account before
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number=other_deposit_account_mask,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_fr,
            current_balance=amount_deposit_mask,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
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
            passbook_or_receipt_number=from_serial_fr,
            current_balance=amount_deposit_mask,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_020_prepaid_7d_dpt_dls_close_deposit_account_by_deposit_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [
            f'InvalidEarlywdr: Invalid Early withdrawal [No] of account [{self.no_mask(deposit_account_fd_mask)}]'
        ]
        # close deposit account error
        self.dpt_dls(
            account_number=deposit_account_fd_mask,
            another_deposit_account=other_deposit_account_mask,
            balance=amount_deposit_mask,
            interest_payable_receivable=interest_payable_receivable,
            interest_due=interest_due,
            interest_re_calculate=interest_re_calculate,
            gross_paid_interest_amount=gross_paid_interest_amount,
            penalty_fee=penalty_fee,
            balance_received=balance_received,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message
        )
        # view account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance=amount_deposit_mask,
            interest_accrual=expected_interest_accrual,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_fr,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )
        # view another account
        self.deposit_account_view(
            account_number=other_deposit_account_mask,
            current_balance=current_balance_other_1st_receive_interest,
            account_status=status_normal,
            earmark_block_amount='0.00',
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_other_account_gl_number
        )

    def test_021_prepaid_7d_dpt_mls_close_deposit_account_by_gl_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [
            f'InvalidEarlywdr: Invalid Early withdrawal [No] of account [{self.no_mask(deposit_account_fd_mask)}]'
        ]
        # close deposit account error
        self.dpt_mls(
            account_number=deposit_account_fd_mask,
            accounting_number=gl_account_number,
            balance=amount_deposit_mask,
            interest_payable_receivable=interest_payable_receivable,
            interest_due=interest_due,
            interest_re_calculate=interest_re_calculate,
            gross_paid_interest_amount=gross_paid_interest_amount,
            penalty_fee=penalty_fee,
            balance_received=balance_received,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message
        )
        # view account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance=amount_deposit_mask,
            interest_accrual=expected_interest_accrual,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_fr,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_022_prepaid_7d_dpt_cls_close_deposit_account_by_cash_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [
            f'InvalidEarlywdr: Invalid Early withdrawal [No] of account [{self.no_mask(deposit_account_fd_mask)}]'
        ]
        # close deposit account error
        self.dpt_cls(
            account_number=deposit_account_fd_mask,
            balance=amount_deposit_mask,
            interest_payable_receivable=interest_payable_receivable,
            interest_due=interest_due,
            interest_re_calculate=interest_re_calculate,
            gross_paid_interest_amount=gross_paid_interest_amount,
            penalty_fee=penalty_fee,
            balance_received=balance_received,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message
        )
        # view account
        self.deposit_account_view(
            account_number=deposit_account_fd_mask,
            linkage_account_number='',
            current_balance=amount_deposit_mask,
            interest_accrual=expected_interest_accrual,
            account_status=status_normal,
            passbook_or_receipt_number=from_serial_fr,
            earmark_block_amount='0.00',
            rollover_option=rollover_option,
            reason_of_account_opening=reason_of_account_opening,
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_account_gl_number,
            expected_ifc_codes=expected_ifc_codes,
            expected_ifc_gl_names=expected_ifc_gl_names,
            expected_ifc_gl_numbers=expected_ifc_gl_numbers,
            early_withdrawal='No',
        )

    def test_023_prepaid_7d_dpt_his_transaction_history_inquiry_success(self):
        expected_trans_code=['DPT_OPN','DPT_APR','DPT_TRF','DPT_CER','DPT_BLK','DPT_RLS','DPT_EMK','DPT_ERL']
        expected_users=[username] * 8
        expected_channels=['Core Banking'] * 8
        expected_debits=['0.00'] * 8 + [amount_deposit_mask]
        expected_credits=['0.00'] * 2 + [amount_deposit_mask] + ['0.00'] * 6
        expected_balances=['0.00'] * 2 + [amount_deposit_mask] * 6 + ['0.00']
        expected_dates=[working_date] * 8
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
        # view another account after close success
        self.deposit_account_view(
            account_number=other_deposit_account_mask,
            current_balance=current_balance_other_1st_receive_interest,
            account_status=status_normal,
            earmark_block_amount='0.00',
            expected_account_gl_name=expected_account_gl_name,
            expected_account_gl_number=expected_other_account_gl_number
        )

# Check invalid case
    def test_024_prepaid_7d_dpt_opn_check_open_account_with_to_account_number_not_same_customer_at_accept(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_corporate,
            customer_type='Single customer',
            catalogue_code='CAMMK0000',
            reason_of_account_opening='Enter value reason of account opening'
        )
        other_deposit_account=dpt_opn_result[1]
        self.dpt_apr(
            account_number=other_deposit_account,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        list_error_message = [
            f'ERROR: Invalid account number [{self.no_mask(other_deposit_account)}]'
        ]
        self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code,
            reason_of_account_opening=reason_of_account_opening,
            to_account_number=other_deposit_account,
            list_error_message=list_error_message,
        )

    def test_025_prepaid_7d_dpt_opn_check_open_account_with_to_account_number_not_same_currency_at_accept(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code='CAUSD0000',
            reason_of_account_opening='Enter value reason of account opening'
        )
        other_deposit_account_usd=dpt_opn_result[1]
        self.dpt_apr(
            account_number=other_deposit_account_usd,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        list_error_message = [
            f'InvalidCurrency: Invalid currency code [USD-MMK]'
        ]
        self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code,
            reason_of_account_opening=reason_of_account_opening,
            to_account_number=other_deposit_account_usd,
            list_error_message=list_error_message,
        )

    def test_026_prepaid_01_check_deposit_account_with_new_fields_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_account_prepaid_new_fields
        reason_of_account_opening='Enter value reason of account opening'
        business_purpose_code='A011130'
        employer_organization_name='Employer Name'
        safe_deposit_locker_number='0T5633433WQ'
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code,
            reason_of_account_opening=reason_of_account_opening,
            to_account_number=other_deposit_account_mask,
            business_purpose_code=business_purpose_code,
            employer_organization_name=employer_organization_name,
            safe_deposit_locker_number=safe_deposit_locker_number,
            mpu_card=True,
            passbook_cheque_book=True,
        )
        deposit_account_prepaid_new_fields=dpt_opn_result[1]
        self.deposit_account_view(
            account_number=deposit_account_prepaid_new_fields,
            business_purpose_code=business_purpose_code,
            employer_organization_name=employer_organization_name,
            reason_of_account_opening=reason_of_account_opening,
            safe_deposit_locker_number=safe_deposit_locker_number
        )
        reason_of_account_opening_update_1st='Update value reason of account opening'
        safe_deposit_locker_number_update_1st='Up0T5633433WQ'
        self.deposit_account_update(
            account_number=deposit_account_prepaid_new_fields,
            reason_of_account_opening=reason_of_account_opening_update_1st,
            safe_deposit_locker_number=safe_deposit_locker_number_update_1st
        )
        self.deposit_account_view(
            account_number=deposit_account_prepaid_new_fields,
            business_purpose_code=business_purpose_code,
            employer_organization_name=employer_organization_name,
            reason_of_account_opening=reason_of_account_opening_update_1st,
            safe_deposit_locker_number=safe_deposit_locker_number_update_1st
        )
        self.dpt_apr(
            account_number=deposit_account_prepaid_new_fields,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.deposit_account_view(
            account_number=deposit_account_prepaid_new_fields,
            business_purpose_code=business_purpose_code,
            employer_organization_name=employer_organization_name,
            reason_of_account_opening=reason_of_account_opening_update_1st,
            safe_deposit_locker_number=safe_deposit_locker_number_update_1st
        )
        reason_of_account_opening_update_2nd='Update 2nd value reason of acc opening'
        safe_deposit_locker_number_update_2nd='Up2nd33433WQ'
        self.deposit_account_update(
            account_number=deposit_account_prepaid_new_fields,
            reason_of_account_opening=reason_of_account_opening_update_2nd,
            safe_deposit_locker_number=safe_deposit_locker_number_update_2nd
        )
        self.deposit_account_modify_approve(
            account_number=deposit_account_prepaid_new_fields
        )
        self.deposit_account_view(
            account_number=deposit_account_prepaid_new_fields,
            business_purpose_code=business_purpose_code,
            employer_organization_name=employer_organization_name,
            reason_of_account_opening=reason_of_account_opening_update_2nd,
            safe_deposit_locker_number=safe_deposit_locker_number_update_2nd
        )

    def test_027_dpt_account_linkage_add_with_lookup_field_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        master_module_name = 'DEPOSIT'
        master_account_code = deposit_account_fd_mask
        currency_for_fee = 'MMK'
        linkage_module_name = 'DEPOSIT'
        linkage_account_code = other_deposit_account_mask
        linkage_account_name = None
        linkage_type = 'Linkage Deposit - Deposit'
        linkage_classification = 'Auto collection(transfer) for both P and I'
        linkage_description = 'Linkage description auto test'
        amount_for_fee_calculation = '1,000,000.00'
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.05500']
        fee_amount = '2,050.00'
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.05500 / 100 * 1,000,000.00) = 2,050.00
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '550.00'
        expected_posting = {
            'expected_debits': [
                (expected_other_account_gl_number, fee_amount),
            ],
            'expected_credits': [
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        dpt_opal_result = self.dpt_opal_lookup(
            master_module_name=master_module_name,
            master_account_code=master_account_code,
            currency_for_fee=currency_for_fee,
            linkage_module_name=linkage_module_name,
            linkage_account_code=linkage_account_code,
            linkage_type=linkage_type,
            linkage_classification=linkage_classification,
            linkage_description=linkage_description,
            fee_collect_method='Deposit',
            account_number_for_fee=linkage_account_code,
            amount_for_fee_calculation=amount_for_fee_calculation,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later='Y',
        )
        transaction_references=dpt_opal_result
        print('View transaction before approve')
        self.dpt_opal_view(
            transaction_references=transaction_references,
            master_module_name=master_module_name,
            master_account_code=master_account_code,
            currency_for_fee=currency_for_fee,
            linkage_module_name=linkage_module_name,
            linkage_account_code=linkage_account_code,
            linkage_account_name=linkage_account_name,
            linkage_type=linkage_type,
            linkage_classification=linkage_classification,
            linkage_description=linkage_description,
            fee_collect_method='Deposit',
            account_number_for_fee=linkage_account_code,
            amount_for_fee_calculation=amount_for_fee_calculation,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
        )
        # approve
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        print('View transaction after approve')
        self.dpt_opal_view(
            transaction_references=transaction_references,
            master_module_name=master_module_name,
            master_account_code=master_account_code,
            currency_for_fee=currency_for_fee,
            linkage_module_name=linkage_module_name,
            linkage_account_code=linkage_account_code,
            linkage_account_name=linkage_account_name,
            linkage_type=linkage_type,
            linkage_classification=linkage_classification,
            linkage_description=linkage_description,
            fee_collect_method='Deposit',
            account_number_for_fee=linkage_account_code,
            amount_for_fee_calculation=amount_for_fee_calculation,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
        )

    def test_028_dpt_account_linkage_delete_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_account_linkage_delete_result = self.dpt_account_linkage_delete(
            master_account_number=deposit_account_fd_mask
        )
        self.assertEqual(self.no_mask(deposit_account_fd_mask), dpt_account_linkage_delete_result)

    def test_029_dpt_account_linkage_add_with_enter_data_field_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        master_module_name = 'DEPOSIT'
        master_account_code = deposit_account_fd_mask
        currency_for_fee = 'MMK'
        linkage_module_name = 'DEPOSIT'
        linkage_account_code = other_deposit_account_mask
        linkage_account_name = None
        linkage_type = 'Linkage Deposit - Deposit'
        linkage_classification = 'Auto collection(transfer) for both P and I'
        linkage_description = 'Linkage description auto test'
        amount_for_fee_calculation = '1,000,000.00'
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.05500']
        fee_amount = '2,050.00'
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.05500 / 100 * 1,000,000.00) = 2,050.00
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '550.00'
        expected_posting = {
            'expected_debits': [
                (gl_cash, fee_amount),
            ],
            'expected_credits': [
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        dpt_opal_result = self.dpt_opal(
            master_module_name=master_module_name,
            master_account_code=master_account_code,
            currency_for_fee=currency_for_fee,
            linkage_module_name=linkage_module_name,
            linkage_account_code=linkage_account_code,
            linkage_type=linkage_type,
            linkage_classification=linkage_classification,
            linkage_description=linkage_description,
            fee_collect_method='Cash',
            amount_for_fee_calculation=amount_for_fee_calculation,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later='Y',
        )
        transaction_references=dpt_opal_result
        print('View transaction before approve')
        self.dpt_opal_view(
            transaction_references=transaction_references,
            master_module_name=master_module_name,
            master_account_code=master_account_code,
            currency_for_fee=currency_for_fee,
            linkage_module_name=linkage_module_name,
            linkage_account_code=linkage_account_code,
            linkage_account_name=linkage_account_name,
            linkage_type=linkage_type,
            linkage_classification=linkage_classification,
            linkage_description=linkage_description,
            fee_collect_method='Cash',
            amount_for_fee_calculation=amount_for_fee_calculation,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
        )
        # approve
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        print('View transaction after approve')
        self.dpt_opal_view(
            transaction_references=transaction_references,
            master_module_name=master_module_name,
            master_account_code=master_account_code,
            currency_for_fee=currency_for_fee,
            linkage_module_name=linkage_module_name,
            linkage_account_code=linkage_account_code,
            linkage_account_name=linkage_account_name,
            linkage_type=linkage_type,
            linkage_classification=linkage_classification,
            linkage_description=linkage_description,
            fee_collect_method='Cash',
            amount_for_fee_calculation=amount_for_fee_calculation,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
        )

if __name__ == '__main__':
    webui_test.main()