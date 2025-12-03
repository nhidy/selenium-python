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
USERNAME_LOGIN_OTHER_BRANCH = os.getenv("TEST_CONFIG_USERNAME_LOGIN_OTHER_BRANCH", "")
PASSWORD_LOGIN_OTHER_BRANCH = os.getenv("TEST_CONFIG_PASSWORD_LOGIN_OTHER_BRANCH", "")
USERNAME_APPROVE_OTHER_BRANCH = os.getenv("TEST_CONFIG_USERNAME_APPROVE_OTHER_BRANCH", "")
PASSWORD_APPROVE_OTHER_BRANCH = os.getenv("TEST_CONFIG_PASSWORD_APPROVE_OTHER_BRANCH", "")
USERNAME_REVERSE_OTHER_BRANCH = os.getenv("TEST_CONFIG_USERNAME_REVERSE_OTHER_BRANCH", "")
PASSWORD_REVERSE_OTHER_BRANCH = os.getenv("TEST_CONFIG_PASSWORD_REVERSE_OTHER_BRANCH", "")

customer_code_single_mask = CUSTOMER_CODE

# path of folder content data_attached
main_path = '../../data_attached/'
# data test for Trade Finance
category_code = 'BGNUL'
applicant = 'Federation of Myanmar Licensed Contractors Associations (MLCA)'
beneficiary = 'Public Rental Housing'
beneficiary_address = '27, Nguyen Huu Tho, Tan Hung, Q7, HCM'
currency_code = 'MMK'
currency_short_code = '01' # MMK
issued_date = '18/06/2025'
effect_date = '19/06/2025'
guarantee_period = '6'
guarantee_period_unit = 'Months'
maturity_date = '18/12/2025'
sg_bg_amount = '9,537,000.00'
guarantee_amount_no_margin = '9,537,000.00'
released_guarantee_amount_no_margin_and_secured='14,037,000.00'
margin_rate = '15.00'
margin_amount = '1,430,550.00'
guarantee_amount_have_margin = '8,106,450.00'
secured_amount = '4,500,000.00'
released_guarantee_amount_have_margin_and_secured='12,606,450.00'
project_name = 'the contract regarding Public Rental Housing Project Lot (1) (Building No - 65, 67) for ground floor room insulation work at Dagon Myothit (South) in Yangon'
bg_number = 'BG-027/SB(HO)2024-2025'
send_to = f'Director General\nDepartment of Urban and Housing Development\nMinistry of Construction'
# data test document attachment
file_test = 'autotest_attach.jpg'
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'{main_path}{file_test}'))
expire_date='15/11/2064'
document_description='AUTO TEST'
expire_date_update='25/11/2064'
document_description_update='AUTO TEST update'

expected_account_gl_names = ['LIABILITY', 'TRADE', 'SUSPEND']
status_active = 'Active'
status_normal = 'Normal'
status_closed = 'Closed'
# data test fee
ifc_9 = '9'
value_9 = '0.50000' # Fee = 0.50000 * SG amount = 47,685.00 
total_fee_amount_9 = '47,685.00'
total_fee_9 = f'Total Amount = {total_fee_amount_9}'
ifc_10 = '10'
value_10 = '1.00000' # Fee = 1.00000 * SG amount = 95,370.00
total_fee_amount_10 = '95,370.00'
total_fee_10 = f'Total Amount = {total_fee_amount_10}'
# data test extension 1st
extend_period_1st = '3'
extend_period_unit_1st = 'Months'
extend_to_date_1st = '18/03/2026'
extension_date_1st = '25/11/2025'
effective_date_extension_1st = '19/12/2025'
# data test extension 2nd
extend_period_2nd = '9'
extend_period_unit_2nd = 'Months'
extend_to_date_2nd = '18/12/2026'
extension_date_2nd = '20/11/2025'
effective_date_extension_2nd = '19/03/2026'
# data test extension 3rd
extend_period_3rd = '1'
extend_period_unit_3rd = 'Year'
extend_to_date_3rd = '18/12/2027'
extension_date_3rd = '25/11/2026'
effective_date_extension_3rd = '19/12/2026'
# data test margin deposit
deposit_catalog_saving = 'BSMMK0000'
current_balance_003_1st = '5,000,000.00'
current_balance_003_after_verify_bg_have_fee = '3,474,080.00'
current_balance_003_after_collect_fee_extend_bg = '3,426,395.00'
current_balance_003_after_close_bg = '4,856,945.00'
# data test release margin deposit
deposit_catalog_current = 'CAMMK0000'
current_balance_004_1st = '1,000.00'
current_balance_004_after_close_bg = '1,431,550.00'
current_balance_005_1st = '1,574,605.00'
current_balance_005_after_verify_bg_no_fee = '1,479,235.00'
current_balance_005_after_verify_bg_have_fee = '48,685.00'
current_balance_005_after_collect_fee_extend_bg = '1,000.00'
# data test GL IBT
ibt_branch_trade_gl_number = '004-1101001010707-01'
ibt_branch_deposit_gl_number = '005-1101001010606-01'
fee_collect_gl_number_003 = '003-1010107777777-01'
fee_collect_gl_number_004 = '004-1010107777777-01'
# data test secure mortgage
catalogue_code_mortgage = '00000003'
# data test for 'Cheque'
stock_type_cq = 'Cheque'
stock_prefix_cq = 'CQ'
number_of_leaves_cq = '25'
number_of_book_cq = '1'
expected_values = ['Unpaid'] * 3 + ['Paid'] + ['Unpaid'] * 21

class TradeTest(FormAction):
    def get_url(self):
        return RUN_ON_URL

    def data_begin(self):
        global username_approve, password_approve, username_reverse, password_reverse, username, password, username_cross_branch, password_cross_branch, username_approve_cross_branch, password_approve_cross_branch, username_reverse_cross_branch, password_reverse_cross_branch
        username_approve = USERNAME_APPROVE
        password_approve = PASSWORD_APPROVE
        username_reverse = USERNAME_REVERSE
        password_reverse = PASSWORD_REVERSE
        username = USERNAME_LOGIN
        password = PASSWORD_LOGIN
        username_cross_branch = USERNAME_LOGIN_OTHER_BRANCH
        password_cross_branch = PASSWORD_LOGIN_OTHER_BRANCH
        username_approve_cross_branch = USERNAME_APPROVE_OTHER_BRANCH
        password_approve_cross_branch = PASSWORD_APPROVE_OTHER_BRANCH
        username_reverse_cross_branch = USERNAME_REVERSE_OTHER_BRANCH
        password_reverse_cross_branch = PASSWORD_REVERSE_OTHER_BRANCH
        self.login(username, password, one_app=ONE_APP)
        global working_date, branch_code
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()
        global expected_account_gl_numbers, liability_gl_number, trade_gl_number, suspend_gl_number, cash_gl_number, ifcc_gl_number
        liability_gl_number = f'{branch_code}-6010101000202-{currency_short_code}'
        trade_gl_number = f'{branch_code}-5010101000101-{currency_short_code}'
        suspend_gl_number = f'{branch_code}-2070501000909-{currency_short_code}'
        expected_account_gl_numbers=[str(liability_gl_number).replace('-',''), str(trade_gl_number).replace('-',''), str(suspend_gl_number).replace('-','')]
        cash_gl_number = f'{branch_code}-1010301000101-{currency_short_code}'
        ifcc_gl_number = f'{branch_code}-3030901000101-{currency_short_code}'

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
            branch_code='003',
            currency_code='MMK',
            account_number=fee_collect_gl_number_003
        )
        self.add_gl_level_9_use_for_testing(
            branch_code='004',
            currency_code='MMK',
            account_number=fee_collect_gl_number_004
        )
        if self.check_customer_profile_not_exist(customer_code_single_mask):
            self.stop()
            self.fail()

# CASE 01: NO NEED TO DEPOSIT/CASH MARGIN AND SECURE GUARANTEE
    def test_001_bg_process_01_trd_sni_issue_for_collection_no_margin_and_no_secure_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global trade_account_mask_01
        # make transaction
        trd_sni_result = self.trd_sni(
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_no_margin,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            approve_later='Y'
        )
        transaction_references=trd_sni_result[0]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sni_view_result = self.trd_sni_view(
            transaction_references=transaction_references,
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_no_margin,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            addition_margin_rate='0',
            margin_amount='0.00',
            secured_amount='0.00'
        )
        trade_account_mask_01=trd_sni_view_result[1]
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_01,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )

    def test_001_bg_process_02_document_attachment_add_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        self.trade_document_attachment_add(
            account_number=trade_account_mask_01,
            file_path=file_path,
            expire_date=expire_date,
            document_description=document_description
        )

    def test_001_bg_process_03_document_attachment_view_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        self.trade_document_attachment_view(
            account_number=trade_account_mask_01,
            expire_date=expire_date,
            document_description=document_description
        )

    def test_001_bg_process_04_document_attachment_approve_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        self.trade_document_attachment_approve(
            account_number=trade_account_mask_01
        )

    def test_001_bg_process_05_document_attachment_update_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        self.trade_document_attachment_update(
            account_number=trade_account_mask_01,
            expire_date=expire_date_update,
            document_description=document_description_update
        )

    def test_001_bg_process_06_trd_siv_verify_no_margin_collect_fee_by_cash_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_01,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )
        # make transaction
        trd_siv_result = self.trd_siv(
            account_number=trade_account_mask_01,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_no_margin,
            margin_rate='0.00',
            margin_amount='0.00',
            secured_amount='0.00',
            applicant=applicant,
            approve_later='Y'
        )
        transaction_references=trd_siv_result[0]
        self.assertEqual(trade_account_mask_01, trd_siv_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_siv_view_result = self.trd_siv_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_01,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_no_margin,
            margin_rate='0.00',
            margin_amount='0.00',
            secured_amount='0.00',
            applicant=applicant
        )
        transaction_references=trd_siv_view_result[0]
        self.assertEqual(trade_account_mask_01, trd_siv_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (trade_gl_number, sg_bg_amount),
                (cash_gl_number, total_fee_amount_10),
            ],
            'expected_credits': [
                (liability_gl_number, sg_bg_amount),
                (ifcc_gl_number, total_fee_amount_10),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_01,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_001_bg_process_07_trd_sbx_extension_collect_fee_by_cash_1st_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_01,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_01,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_01, trd_sbx_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_01,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_01, trd_sbx_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (cash_gl_number, total_fee_amount_9),
            ],
            'expected_credits': [
                (ifcc_gl_number, total_fee_amount_9),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_01,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_001_bg_process_08_trd_sbx_extension_collect_fee_by_cash_2nd_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_01,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=extend_to_date_1st,
            extend_period=extend_period_2nd,
            extend_period_unit=extend_period_unit_2nd,
            extend_to_date=extend_to_date_2nd,
            bg_number=bg_number,
            extension_time='2',
            extension_date=extension_date_2nd,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_01, trd_sbx_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_01,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=extend_to_date_1st,
            extend_period=extend_period_2nd,
            extend_period_unit=extend_period_unit_2nd,
            extend_to_date=extend_to_date_2nd,
            bg_number=bg_number,
            extension_time='2',
            extension_date=extension_date_2nd,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_01, trd_sbx_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (cash_gl_number, total_fee_amount_10),
            ],
            'expected_credits': [
                (ifcc_gl_number, total_fee_amount_10),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_01,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            extension_date=extension_date_2nd,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_2nd,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_2nd,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=extend_period_2nd,
            guarantee_period_unit=extend_period_unit_2nd,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_001_bg_process_09_trd_sbx_extension_collect_fee_by_cash_3rd_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_01,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=extend_to_date_2nd,
            extend_period=extend_period_3rd,
            extend_period_unit=extend_period_unit_3rd,
            extend_to_date=extend_to_date_3rd,
            bg_number=bg_number,
            extension_time='3',
            extension_date=extension_date_3rd,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_01, trd_sbx_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_01,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=extend_to_date_2nd,
            extend_period=extend_period_3rd,
            extend_period_unit=extend_period_unit_3rd,
            extend_to_date=extend_to_date_3rd,
            bg_number=bg_number,
            extension_time='3',
            extension_date=extension_date_3rd,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_01, trd_sbx_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (cash_gl_number, total_fee_amount_10),
            ],
            'expected_credits': [
                (ifcc_gl_number, total_fee_amount_10),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_01,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            extension_date=extension_date_3rd,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_3rd,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_3rd,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=extend_period_3rd,
            guarantee_period_unit=extend_period_unit_3rd,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_001_bg_process_10_trd_scl_close_no_release_margin_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_01,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers
        )
        # make transaction
        trd_scl_result = self.trd_scl(
            account_number=trade_account_mask_01,
            sg_bg_amount=sg_bg_amount,
            margin_rate='0.00',
            margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            secured_amount='0.00',
            bg_number=bg_number,
            approve_later='Y'
        )
        transaction_references=trd_scl_result[0]
        self.assertEqual(trade_account_mask_01, trd_scl_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_scl_view_result = self.trd_scl_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_01,
            sg_bg_amount=sg_bg_amount,
            margin_rate='0.00',
            margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            secured_amount='0.00',
            bg_number=bg_number
        )
        transaction_references=trd_scl_view_result[0]
        self.assertEqual(trade_account_mask_01, trd_scl_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (liability_gl_number, sg_bg_amount),
            ],
            'expected_credits': [
                (trade_gl_number, sg_bg_amount),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_01,
            account_status=status_closed,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            extension_date=extension_date_3rd,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_3rd,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_3rd,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount=sg_bg_amount,
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount=guarantee_amount_no_margin,
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=extend_period_3rd,
            guarantee_period_unit=extend_period_unit_3rd,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount,
            release_off_balance_sheet_amount=sg_bg_amount
        )


# CASE 2: NEED TO CASH MARGIN AND NO NEED TO SECURE GUARANTEE
    def test_002_bg_process_01_trd_sni_issue_for_collection_need_margin_and_no_secure_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global trade_account_mask_02
        # make transaction
        trd_sni_result = self.trd_sni(
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            guarantee_amount=guarantee_amount_have_margin,
            addition_margin_rate=margin_rate,
            margin_amount=margin_amount,
            approve_later='Y'
        )
        transaction_references=trd_sni_result[0]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sni_view_result = self.trd_sni_view(
            transaction_references=transaction_references,
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            guarantee_amount=guarantee_amount_have_margin,
            addition_margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount='0.00'
        )
        trade_account_mask_02=trd_sni_view_result[1]
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_02,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )

    def test_002_bg_process_02_document_attachment_add_empty_date_and_desc_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        self.trade_document_attachment_add(
            account_number=trade_account_mask_02,
            file_path=file_path
        )

    def test_002_bg_process_03_document_attachment_view_empty_date_and_desc_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        self.trade_document_attachment_view(
            account_number=trade_account_mask_02,
            expire_date='',
            document_description=''
        )

    def test_002_bg_process_04_document_attachment_approve_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        self.trade_document_attachment_approve(
            account_number=trade_account_mask_02
        )

    def test_002_bg_process_05_document_attachment_update_empty_date_and_desc_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        self.trade_document_attachment_update(
            account_number=trade_account_mask_02
        )

    def test_002_bg_process_06_trd_siv_verify_margin_and_collect_fee_by_cash_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_02,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )
        # make transaction
        trd_siv_result = self.trd_siv(
            account_number=trade_account_mask_02,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_have_margin,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount='0.00',
            applicant=applicant,
            margin_method='Cash',
            approve_later='Y'
        )
        transaction_references=trd_siv_result[0]
        self.assertEqual(trade_account_mask_02, trd_siv_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_siv_view_result = self.trd_siv_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_02,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_have_margin,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount='0.00',
            applicant=applicant,
            margin_method='Cash'
        )
        transaction_references=trd_siv_view_result[0]
        self.assertEqual(trade_account_mask_02, trd_siv_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (trade_gl_number, sg_bg_amount),
                (cash_gl_number, margin_amount),
                (cash_gl_number, total_fee_amount_10),
            ],
            'expected_credits': [
                (liability_gl_number, sg_bg_amount),
                (suspend_gl_number, margin_amount),
                (ifcc_gl_number, total_fee_amount_10),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_02,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_002_bg_process_07_trd_sbx_extension_collect_fee_by_cash_1st_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_02,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_02,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_02, trd_sbx_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_02,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_02, trd_sbx_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (cash_gl_number, total_fee_amount_9),
            ],
            'expected_credits': [
                (ifcc_gl_number, total_fee_amount_9),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_02,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_002_bg_process_08_trd_sbx_extension_collect_fee_by_cash_2nd_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_02,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=extend_to_date_1st,
            extend_period=extend_period_2nd,
            extend_period_unit=extend_period_unit_2nd,
            extend_to_date=extend_to_date_2nd,
            bg_number=bg_number,
            extension_time='2',
            extension_date=extension_date_2nd,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_02, trd_sbx_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_02,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=extend_to_date_1st,
            extend_period=extend_period_2nd,
            extend_period_unit=extend_period_unit_2nd,
            extend_to_date=extend_to_date_2nd,
            bg_number=bg_number,
            extension_time='2',
            extension_date=extension_date_2nd,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_02, trd_sbx_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (cash_gl_number, total_fee_amount_10),
            ],
            'expected_credits': [
                (ifcc_gl_number, total_fee_amount_10),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_02,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=extension_date_2nd,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_2nd,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_2nd,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=extend_period_2nd,
            guarantee_period_unit=extend_period_unit_2nd,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_002_bg_process_09_trd_sbx_extension_collect_fee_by_cash_3rd_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_02,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=extend_to_date_2nd,
            extend_period=extend_period_3rd,
            extend_period_unit=extend_period_unit_3rd,
            extend_to_date=extend_to_date_3rd,
            bg_number=bg_number,
            extension_time='3',
            extension_date=extension_date_3rd,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_02, trd_sbx_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_02,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=extend_to_date_2nd,
            extend_period=extend_period_3rd,
            extend_period_unit=extend_period_unit_3rd,
            extend_to_date=extend_to_date_3rd,
            bg_number=bg_number,
            extension_time='3',
            extension_date=extension_date_3rd,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_02, trd_sbx_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (cash_gl_number, total_fee_amount_10),
            ],
            'expected_credits': [
                (ifcc_gl_number, total_fee_amount_10),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_02,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=extension_date_3rd,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_3rd,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_3rd,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=extend_period_3rd,
            guarantee_period_unit=extend_period_unit_3rd,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_002_bg_process_10_trd_scl_close_release_margin_by_cash_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_02,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers
        )
        # make transaction
        trd_scl_result = self.trd_scl(
            account_number=trade_account_mask_02,
            margin_method='Cash',
            sg_bg_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            secured_amount='0.00',
            bg_number=bg_number,
            approve_later='Y'
        )
        transaction_references=trd_scl_result[0]
        self.assertEqual(trade_account_mask_02, trd_scl_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_scl_view_result = self.trd_scl_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_02,
            sg_bg_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            secured_amount='0.00',
            bg_number=bg_number
        )
        transaction_references=trd_scl_view_result[0]
        self.assertEqual(trade_account_mask_02, trd_scl_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (liability_gl_number, sg_bg_amount),
                (suspend_gl_number, margin_amount),
            ],
            'expected_credits': [
                (trade_gl_number, sg_bg_amount),
                (cash_gl_number, margin_amount),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_02,
            account_status=status_closed,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date=working_date,
            extension_date=extension_date_3rd,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_3rd,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_3rd,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount=guarantee_amount_have_margin,
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=extend_period_3rd,
            guarantee_period_unit=extend_period_unit_3rd,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount,
            release_off_balance_sheet_amount=sg_bg_amount
        )


# CASE 3: NEED TO DEPOSIT MARGIN AND NO NEED TO SECURE GUARANTEE
    def test_003_bg_process_01_trd_sni_issue_for_collection_need_margin_and_no_secure_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global trade_account_mask_03
        # make transaction
        trd_sni_result = self.trd_sni(
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            guarantee_amount=guarantee_amount_have_margin,
            addition_margin_rate=margin_rate,
            margin_amount=margin_amount,
            approve_later='Y'
        )
        transaction_references=trd_sni_result[0]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sni_view_result = self.trd_sni_view(
            transaction_references=transaction_references,
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            guarantee_amount=guarantee_amount_have_margin,
            addition_margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount='0.00'
        )
        trade_account_mask_03=trd_sni_view_result[1]
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_03,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )

    def test_003_bg_process_02_document_attachment_add_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.trade_document_attachment_add(
            account_number=trade_account_mask_03,
            file_path=file_path,
            expire_date=expire_date,
            document_description=document_description
        )

    def test_003_bg_process_03_document_attachment_approve_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.trade_document_attachment_approve(
            account_number=trade_account_mask_03
        )

    def test_003_bg_process_04_open_deposit_margin_cross_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_account_number, deposit_gl_number
        self.logout()
        self.login(username_cross_branch, password_cross_branch, one_app=ONE_APP)
        global branch_code_deposit
        branch_code_deposit = self.get_logged_branch_code()
        deposit_gl_number = f'{branch_code_deposit}-2020302010202-01'
        # open deposit account
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_single_mask,
            customer_type='Single customer',
            catalogue_code=deposit_catalog_saving,
            reason_of_account_opening='test margin'
        )
        deposit_account_number = dpt_opn_result[1]
        # approve deposit account
        self.dpt_apr(
            account_number=deposit_account_number,
            approve_on_form='Y',
            username=username_approve_cross_branch,
            password=password_approve_cross_branch,
        )
        # cash deposit account
        self.dpt_cdp(
            account_number=deposit_account_number,
            amount_deposit=current_balance_003_1st,
            approve_on_form='Y',
            username=username_approve_cross_branch,
            password=password_approve_cross_branch,
        )

    def test_003_bg_process_05_login_with_main_user_again(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # login main user again
        self.logout()
        self.login(username, password, one_app=ONE_APP)

    def test_003_bg_process_06_trd_siv_verify_margin_and_collect_fee_by_deposit_cross_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_03,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )
        # make transaction
        trd_siv_result = self.trd_siv(
            account_number=trade_account_mask_03,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_have_margin,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount='0.00',
            applicant=applicant,
            margin_method='Deposit',
            margin_deposit_account=deposit_account_number,
            fee_collect_method='Deposit',
            account_number_for_fee=str(deposit_account_number).replace('-', ''),
            approve_later='Y'
        )
        transaction_references=trd_siv_result[0]
        self.assertEqual(trade_account_mask_03, trd_siv_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_siv_view_result = self.trd_siv_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_03,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_have_margin,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount='0.00',
            applicant=applicant,
            margin_method='Deposit',
            margin_deposit_account=deposit_account_number
        )
        transaction_references=trd_siv_view_result[0]
        self.assertEqual(trade_account_mask_03, trd_siv_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (trade_gl_number, sg_bg_amount),
                (ibt_branch_trade_gl_number, margin_amount),
                (deposit_gl_number, margin_amount),
                (ibt_branch_trade_gl_number, total_fee_amount_10),
                (deposit_gl_number, total_fee_amount_10),
            ],
            'expected_credits': [
                (liability_gl_number, sg_bg_amount),
                (suspend_gl_number, margin_amount),
                (ibt_branch_deposit_gl_number, margin_amount),
                (ifcc_gl_number, total_fee_amount_10),
                (ibt_branch_deposit_gl_number, total_fee_amount_10),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_03,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account=deposit_account_number,
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # check deposit account information
        self.deposit_account_view(
            account_number=deposit_account_number,
            current_balance=current_balance_003_after_verify_bg_have_fee,
            earmark_block_amount='0.00'
        )
        # check deposit account history
        expected_trans_code=['DPT_OPN','DPT_APR','DPT_CDP']
        expected_users=[username_cross_branch] * 3
        expected_channels=['Core Banking'] * 3
        expected_debits=['0.00'] * 3
        expected_credits=['0.00'] * 2 + ['5,000,000.00']
        expected_balances=['0.00'] * 2 + ['5,000,000.00']
        expected_dates=[working_date] * 3
        dpt_his_result = self.dpt_his(
            account_number=deposit_account_number,
            transaction_codes=expected_trans_code,
            expected_debits=expected_debits,
            expected_credits=expected_credits,
            expected_balances=expected_balances,
            expected_created_bys=expected_users,
            expected_channels=expected_channels,
            expected_transaction_dates=expected_dates
        )
        self.assertEqual(deposit_account_number, dpt_his_result[1])
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Debit', 4, '95,370.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Debit', 5, '1,430,550.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Balance', 4, '4,904,630.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Balance', 5, '3,474,080.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Created by', 4, username)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Created by', 5, username)

    def test_003_bg_process_07_trd_sbx_extension_collect_fee_by_deposit_cross_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_03,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account=deposit_account_number,
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_03,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            fee_collect_method='Deposit',
            account_number_for_fee=str(deposit_account_number).replace('-', ''),
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_03, trd_sbx_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_03,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            fee_collect_method='Deposit',
            account_number_for_fee=str(deposit_account_number).replace('-', '')
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_03, trd_sbx_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (ibt_branch_trade_gl_number, total_fee_amount_9),
                (deposit_gl_number, total_fee_amount_9),
            ],
            'expected_credits': [
                (ifcc_gl_number, total_fee_amount_9),
                (ibt_branch_deposit_gl_number, total_fee_amount_9),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_03,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account=deposit_account_number,
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # check deposit account information
        self.deposit_account_view(
            account_number=deposit_account_number,
            current_balance=current_balance_003_after_collect_fee_extend_bg,
            earmark_block_amount='0.00'
        )
        # check deposit account history
        expected_trans_code=['DPT_OPN','DPT_APR','DPT_CDP','TRD_SBX']
        expected_users=[username_cross_branch] * 3 + [username]
        expected_channels=['Core Banking'] * 4
        expected_debits=['0.00'] * 3 + ['47,685.00']
        expected_credits=['0.00'] * 2 + ['5,000,000.00'] + ['0.00']
        expected_balances=['0.00'] * 2 + ['5,000,000.00'] + ['3,426,395.00']
        expected_dates=[working_date] * 4
        dpt_his_result = self.dpt_his(
            account_number=deposit_account_number,
            transaction_codes=expected_trans_code,
            expected_debits=expected_debits,
            expected_credits=expected_credits,
            expected_balances=expected_balances,
            expected_created_bys=expected_users,
            expected_channels=expected_channels,
            expected_transaction_dates=expected_dates
        )
        self.assertEqual(deposit_account_number, dpt_his_result[1])
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Debit', 4, '95,370.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Debit', 5, '1,430,550.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Balance', 4, '4,904,630.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Balance', 5, '3,474,080.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Created by', 4, username)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Created by', 5, username)

    def test_003_bg_process_08_trd_scl_close_release_margin_by_deposit_cross_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_03,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers
        )
        # make transaction
        trd_scl_result = self.trd_scl(
            account_number=trade_account_mask_03,
            margin_method='Deposit',
            margin_deposit_account=deposit_account_number,
            sg_bg_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            secured_amount='0.00',
            bg_number=bg_number,
            approve_later='Y'
        )
        transaction_references=trd_scl_result[0]
        self.assertEqual(trade_account_mask_03, trd_scl_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_scl_view_result = self.trd_scl_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_03,
            sg_bg_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            secured_amount='0.00',
            bg_number=bg_number
        )
        transaction_references=trd_scl_view_result[0]
        self.assertEqual(trade_account_mask_03, trd_scl_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (liability_gl_number, sg_bg_amount),
                (suspend_gl_number, margin_amount),
                (ibt_branch_deposit_gl_number, margin_amount),
            ],
            'expected_credits': [
                (trade_gl_number, sg_bg_amount),
                (ibt_branch_trade_gl_number, margin_amount),
                (deposit_gl_number, margin_amount),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_03,
            account_status=status_closed,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date=working_date,
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account=deposit_account_number,
            released_margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount=guarantee_amount_have_margin,
            secured_amount='0.00',
            released_secured_amount='0.00',
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount,
            release_off_balance_sheet_amount=sg_bg_amount
        )
        # check deposit account information
        self.deposit_account_view(
            account_number=deposit_account_number,
            current_balance=current_balance_003_after_close_bg,
            earmark_block_amount='0.00'
        )
        # check deposit account history
        expected_trans_code=['DPT_OPN','DPT_APR','DPT_CDP','TRD_SBX','TRD_SCL']
        expected_users=[username_cross_branch] * 3 + [username] * 2
        expected_channels=['Core Banking'] * 5
        expected_debits=['0.00'] * 3 + ['47,685.00'] + ['0.00']
        expected_credits=['0.00'] * 2 + ['5,000,000.00'] + ['0.00'] + ['1,430,550.00']
        expected_balances=['0.00'] * 2 + ['5,000,000.00'] + ['3,426,395.00'] + ['4,856,945.00']
        expected_dates=[working_date] * 5
        dpt_his_result = self.dpt_his(
            account_number=deposit_account_number,
            transaction_codes=expected_trans_code,
            expected_debits=expected_debits,
            expected_credits=expected_credits,
            expected_balances=expected_balances,
            expected_created_bys=expected_users,
            expected_channels=expected_channels,
            expected_transaction_dates=expected_dates
        )
        self.assertEqual(deposit_account_number, dpt_his_result[1])
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Debit', 4, '95,370.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Debit', 5, '1,430,550.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Balance', 4, '4,904,630.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Balance', 5, '3,474,080.00')
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Created by', 4, username)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Created by', 5, username)


# RESTART BROWSER
    def test_003_bg_process_09_restart_browser(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.reset_browser()


# CASE 4: NEED TO CASH MARGIN AND SECURE GUARANTEE
    def test_004_bg_process_01_trd_sni_issue_for_collection_need_margin_and_need_secure_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global trade_account_mask_04
        # make transaction
        trd_sni_result = self.trd_sni(
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            guarantee_amount=guarantee_amount_have_margin,
            addition_margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount=secured_amount,
            approve_later='Y'
        )
        transaction_references=trd_sni_result[0]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sni_view_result = self.trd_sni_view(
            transaction_references=transaction_references,
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            guarantee_amount=guarantee_amount_have_margin,
            addition_margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount=secured_amount
        )
        trade_account_mask_04=trd_sni_view_result[1]
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )

    def test_004_bg_process_02_document_attachment_add_and_approve_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction add
        self.trade_document_attachment_add(
            account_number=trade_account_mask_04,
            file_path=file_path
        )
        # make transaction approve
        self.trade_document_attachment_approve(
            account_number=trade_account_mask_04
        )

    def test_004_bg_process_03_open_and_approve_mortgage_account_cross_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.logout()
        self.login(username_cross_branch, password_cross_branch, one_app=ONE_APP)
        global branch_code_mortgage
        branch_code_mortgage = self.get_logged_branch_code()
        # open mortgage account
        global mortgage_account_cross_branch_mask
        mtg_opn_result = self.mtg_opn(
            customer_code=customer_code_single_mask,
            catalogue_code=catalogue_code_mortgage,
            collateral_asset_value=secured_amount,
            reference_number='Ref AUTO TEST',
            evaluate_by='By AUTO TEST',
            approve_on_form='Y',
            username=username_approve_cross_branch,
            password=password_approve_cross_branch,
            
        )
        mortgage_account_cross_branch_mask = mtg_opn_result[1]
        # approve mortgage account
        self.mtg_apr(
            account_number=mortgage_account_cross_branch_mask,
            approve_on_form='Y',
            username=username_approve_cross_branch,
            password=password_approve_cross_branch,
        )
        # view mortgage account information
        self.mortgage_account_view(
            account_number=mortgage_account_cross_branch_mask,
            customer_code=customer_code_single_mask,
            branch_code=branch_code_mortgage,
            collateral_account_status=status_normal,
            catalogue_code=catalogue_code_mortgage,
            open_date=working_date,
            collateral_asset_value=secured_amount,
            market_value='0.00',
            forced_sale_value=secured_amount,
            current_secure_amount='0.00',
            cc_amount='0.00',
            released_collateral_amount='0.00'
        )

    def test_004_bg_process_04_login_with_main_user_again(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # login main user again
        self.logout()
        self.login(username, password, one_app=ONE_APP)

    def test_004_bg_process_05_trd_gsc_guarantee_by_secure_collateral_cross_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        trd_gsc_result = self.trd_gsc(
            mortgage_account_number=mortgage_account_cross_branch_mask,
            mortgage_account_currency=currency_code,
            asset_booking_value=secured_amount,
            total_secured_amount_of_mortgage='0.00',
            trade_finance_account_number=trade_account_mask_04,
            trade_finance_account_currency=currency_code,
            secure_required=secured_amount,
            secured_amount_for_tf_account='0.00',
            total_secured_amount_of_tf_account='0.00',
            amount_secure_from_this_asset=secured_amount,
            amount_secured_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            customer_code=customer_code_single_mask,
            base_amount=secured_amount,
            approve_later='Y'
        )
        transaction_references=trd_gsc_result[0]
        self.assertEqual(mortgage_account_cross_branch_mask, trd_gsc_result[1])
        self.assertEqual(trade_account_mask_04, trd_gsc_result[2])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_gsc_view_result = self.trd_gsc_view(
            transaction_references=transaction_references,
            mortgage_account_number=mortgage_account_cross_branch_mask,
            mortgage_account_currency=currency_code,
            asset_booking_value=secured_amount,
            total_secured_amount_of_mortgage='0.00',
            trade_finance_account_number=trade_account_mask_04,
            trade_finance_account_currency=currency_code,
            secure_required=secured_amount,
            secured_amount_for_tf_account='0.00',
            total_secured_amount_of_tf_account='0.00',
            amount_secure_from_this_asset=secured_amount,
            amount_secured_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            customer_code=customer_code_single_mask,
            base_amount=secured_amount
        )
        transaction_references=trd_gsc_view_result[0]
        self.assertEqual(mortgage_account_cross_branch_mask, trd_gsc_view_result[1])
        self.assertEqual(trade_account_mask_04, trd_gsc_view_result[2])
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )
        # view mortgage account information
        self.mortgage_account_view(
            account_number=mortgage_account_cross_branch_mask,
            customer_code=customer_code_single_mask,
            branch_code=branch_code_mortgage,
            collateral_account_status=status_normal,
            catalogue_code=catalogue_code_mortgage,
            open_date=working_date,
            collateral_asset_value=secured_amount,
            market_value='0.00',
            forced_sale_value=secured_amount,
            current_secure_amount=secured_amount,
            cc_amount='0.00',
            released_collateral_amount='0.00'
        )

    def test_004_bg_process_06_trd_siv_verify_margin_and_collect_fee_by_cash_success(self):
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )
        # make transaction
        trd_siv_result = self.trd_siv(
            account_number=trade_account_mask_04,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_have_margin,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount=secured_amount,
            applicant=applicant,
            margin_method='Cash',
            approve_later='Y'
        )
        transaction_references=trd_siv_result[0]
        self.assertEqual(trade_account_mask_04, trd_siv_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_siv_view_result = self.trd_siv_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_04,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_have_margin,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount=secured_amount,
            applicant=applicant,
            margin_method='Cash'
        )
        transaction_references=trd_siv_view_result[0]
        self.assertEqual(trade_account_mask_04, trd_siv_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (trade_gl_number, sg_bg_amount),
                (cash_gl_number, margin_amount),
                (cash_gl_number, total_fee_amount_10),
            ],
            'expected_credits': [
                (liability_gl_number, sg_bg_amount),
                (suspend_gl_number, margin_amount),
                (ifcc_gl_number, total_fee_amount_10),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_004_bg_process_07_trd_sbx_extension_collect_fee_by_gl_cross_branch_error(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_04,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            fee_collect_method='Accounting',
            account_number_for_fee=str(fee_collect_gl_number_003).replace('-', ''),
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_04, trd_sbx_result[1])
        # approve transaction
        list_error_message = [
            'AccountInvalid: Accounting account is invalid - en[004 - 003]'
        ]
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
            allow_approve='N',
            list_error_message=list_error_message
        )
        # reject transaction
        self.transaction_reject(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_04,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            fee_collect_method='Accounting',
            account_number_for_fee=str(fee_collect_gl_number_003).replace('-', '')
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_04, trd_sbx_view_result[1])
        # view account information after reject
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_004_bg_process_08_trd_sbx_extension_collect_fee_by_gl_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_04,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            fee_collect_method='Accounting',
            account_number_for_fee=str(fee_collect_gl_number_004).replace('-', ''),
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_04, trd_sbx_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_04,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            fee_collect_method='Accounting',
            account_number_for_fee=str(fee_collect_gl_number_004).replace('-', '')
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_04, trd_sbx_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (fee_collect_gl_number_004, total_fee_amount_9),
            ],
            'expected_credits': [
                (ifcc_gl_number, total_fee_amount_9),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_004_bg_process_09_trd_rsc_release_secure_collateral_cross_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        trd_rsc_result = self.trd_rsc(
            mortgage_account_number=mortgage_account_cross_branch_mask,
            asset_booking_value=secured_amount,
            mortgage_account_currency=currency_code,
            trade_finance_account_number=trade_account_mask_04,
            trade_finance_account_currency=currency_code,
            secured_amount_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            release_amount_in_mortgage_currency=secured_amount,
            release_amount_in_tf_currency=secured_amount,
            customer_code=customer_code_single_mask,
            base_amount=secured_amount,
            approve_later='Y'
        )
        transaction_references=trd_rsc_result[0]
        self.assertEqual(mortgage_account_cross_branch_mask, trd_rsc_result[1])
        self.assertEqual(trade_account_mask_04, trd_rsc_result[2])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_rsc_view_result = self.trd_rsc_view(
            transaction_references=transaction_references,
            mortgage_account_number=mortgage_account_cross_branch_mask,
            asset_booking_value=secured_amount,
            mortgage_account_currency=currency_code,
            trade_finance_account_number=trade_account_mask_04,
            trade_finance_account_currency=currency_code,
            secured_amount_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            release_amount_in_mortgage_currency=secured_amount,
            release_amount_in_tf_currency=secured_amount,
            customer_code=customer_code_single_mask,
            base_amount=secured_amount
        )
        transaction_references=trd_rsc_view_result[0]
        self.assertEqual(mortgage_account_cross_branch_mask, trd_rsc_view_result[1])
        self.assertEqual(trade_account_mask_04, trd_rsc_view_result[2])
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount=secured_amount,
            secured_amount=secured_amount,
            released_secured_amount=secured_amount,
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # view mortgage account information
        self.mortgage_account_view(
            account_number=mortgage_account_cross_branch_mask,
            customer_code=customer_code_single_mask,
            branch_code=branch_code_mortgage,
            collateral_account_status=status_normal,
            catalogue_code=catalogue_code_mortgage,
            open_date=working_date,
            collateral_asset_value=secured_amount,
            market_value='0.00',
            forced_sale_value=secured_amount,
            current_secure_amount='0.00',
            cc_amount='0.00',
            released_collateral_amount=secured_amount
        )

    def test_004_bg_process_10_open_deposit_release_margin_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_account_release_margin, deposit_gl_number_release_margin
        deposit_gl_number_release_margin = f'{branch_code}-2020301010202-01'
        # open deposit account
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_single_mask,
            customer_type='Single customer',
            catalogue_code=deposit_catalog_current,
            reason_of_account_opening='test release margin'
        )
        deposit_account_release_margin = dpt_opn_result[1]

    def test_004_bg_process_11_approve_and_deposit_money_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # login checker user
        self.logout()
        self.login(username_approve, password_approve)
        # approve deposit account
        self.dpt_apr(
            account_number=deposit_account_release_margin
        )
        # login main user again
        self.logout()
        self.login(username, password, one_app=ONE_APP)
        # cash deposit account
        dpt_cdp_result = self.dpt_cdp(
            account_number=deposit_account_release_margin,
            amount_deposit=current_balance_004_1st,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.assertEqual(deposit_account_release_margin, dpt_cdp_result[1])

    def test_004_bg_process_12_trd_scl_close_release_margin_by_deposit_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers
        )
        # make transaction
        trd_scl_result = self.trd_scl(
            account_number=trade_account_mask_04,
            margin_method='Deposit',
            margin_deposit_account=deposit_account_release_margin,
            sg_bg_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            secured_amount=secured_amount,
            bg_number=bg_number,
            approve_later='Y'
        )
        transaction_references=trd_scl_result[0]
        self.assertEqual(trade_account_mask_04, trd_scl_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_scl_view_result = self.trd_scl_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_04,
            margin_method='Deposit',
            margin_deposit_account=deposit_account_release_margin,
            sg_bg_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            secured_amount=secured_amount,
            bg_number=bg_number
        )
        transaction_references=trd_scl_view_result[0]
        self.assertEqual(trade_account_mask_04, trd_scl_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (liability_gl_number, sg_bg_amount),
                (suspend_gl_number, margin_amount),
            ],
            'expected_credits': [
                (trade_gl_number, sg_bg_amount),
                (deposit_gl_number_release_margin, margin_amount),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_04,
            account_status=status_closed,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date=working_date,
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount=released_guarantee_amount_have_margin_and_secured,
            secured_amount=secured_amount,
            released_secured_amount=secured_amount,
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount,
            release_off_balance_sheet_amount=sg_bg_amount
        )
        # check deposit account history
        expected_trans_code=['DPT_OPN','DPT_APR','DPT_CDP','TRD_SCL']
        expected_users=[username] + [username_approve] + [username] * 2
        expected_channels=['Core Banking'] * 4
        expected_debits=['0.00'] * 4
        expected_credits=['0.00'] * 2 + [current_balance_004_1st] + [margin_amount]
        expected_balances=['0.00'] * 2 + [current_balance_004_1st] + [current_balance_004_after_close_bg]
        expected_dates=[working_date] * 4
        dpt_his_result = self.dpt_his(
            account_number=deposit_account_release_margin,
            transaction_codes=expected_trans_code,
            expected_debits=expected_debits,
            expected_credits=expected_credits,
            expected_balances=expected_balances,
            expected_created_bys=expected_users,
            expected_channels=expected_channels,
            expected_transaction_dates=expected_dates
        )
        self.assertEqual(deposit_account_release_margin, dpt_his_result[1])
        # check deposit account information
        self.deposit_account_view(
            account_number=deposit_account_release_margin,
            current_balance=current_balance_004_after_close_bg,
            earmark_block_amount='0.00'
        )

# CASE 5: NEED TO DEPOSIT MARGIN AND SECURE GUARANTEE
    def test_005_bg_process_01_trd_sni_issue_for_collection_need_margin_and_need_secure_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global trade_account_mask_05
        # make transaction
        trd_sni_result = self.trd_sni(
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            guarantee_amount=guarantee_amount_have_margin,
            addition_margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount=secured_amount,
            approve_later='Y'
        )
        transaction_references=trd_sni_result[0]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sni_view_result = self.trd_sni_view(
            transaction_references=transaction_references,
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            guarantee_amount=guarantee_amount_have_margin,
            addition_margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount=secured_amount
        )
        trade_account_mask_05=trd_sni_view_result[1]
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_05,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )

    def test_005_bg_process_02_document_attachment_add_and_approve_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction add
        self.trade_document_attachment_add(
            account_number=trade_account_mask_05,
            file_path=file_path,
            expire_date=expire_date,
            document_description=document_description
        )
        # make transaction approve
        self.trade_document_attachment_approve(
            account_number=trade_account_mask_05
        )

    def test_005_bg_process_03_open_and_approve_mortgage_account_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # open mortgage account
        global mortgage_account_same_branch_mask
        mtg_opn_result = self.mtg_opn(
            customer_code=customer_code_single_mask,
            catalogue_code=catalogue_code_mortgage,
            collateral_asset_value=secured_amount,
            reference_number='Ref AUTO TEST',
            evaluate_by='By AUTO TEST',
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        mortgage_account_same_branch_mask = mtg_opn_result[1]
        # login checker user
        self.logout()
        self.login(username_approve, password_approve)
        # approve mortgage account
        self.mtg_apr(
            account_number=mortgage_account_same_branch_mask,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        # login main user again
        self.logout()
        self.login(username, password, one_app=ONE_APP)
        # view mortgage account information
        self.mortgage_account_view(
            account_number=mortgage_account_same_branch_mask,
            customer_code=customer_code_single_mask,
            branch_code=branch_code,
            collateral_account_status=status_normal,
            catalogue_code=catalogue_code_mortgage,
            open_date=working_date,
            collateral_asset_value=secured_amount,
            market_value='0.00',
            forced_sale_value=secured_amount,
            current_secure_amount='0.00',
            cc_amount='0.00',
            released_collateral_amount='0.00'
        )

    def test_005_bg_process_04_trd_gsc_guarantee_by_secure_collateral_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        trd_gsc_result = self.trd_gsc(
            mortgage_account_number=mortgage_account_same_branch_mask,
            mortgage_account_currency=currency_code,
            asset_booking_value=secured_amount,
            total_secured_amount_of_mortgage='0.00',
            trade_finance_account_number=trade_account_mask_05,
            trade_finance_account_currency=currency_code,
            secure_required=secured_amount,
            secured_amount_for_tf_account='0.00',
            total_secured_amount_of_tf_account='0.00',
            amount_secure_from_this_asset=secured_amount,
            amount_secured_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            customer_code=customer_code_single_mask,
            base_amount=secured_amount,
            approve_later='Y'
        )
        transaction_references=trd_gsc_result[0]
        self.assertEqual(mortgage_account_same_branch_mask, trd_gsc_result[1])
        self.assertEqual(trade_account_mask_05, trd_gsc_result[2])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_gsc_view_result = self.trd_gsc_view(
            transaction_references=transaction_references,
            mortgage_account_number=mortgage_account_same_branch_mask,
            mortgage_account_currency=currency_code,
            asset_booking_value=secured_amount,
            total_secured_amount_of_mortgage='0.00',
            trade_finance_account_number=trade_account_mask_05,
            trade_finance_account_currency=currency_code,
            secure_required=secured_amount,
            secured_amount_for_tf_account='0.00',
            total_secured_amount_of_tf_account='0.00',
            amount_secure_from_this_asset=secured_amount,
            amount_secured_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            customer_code=customer_code_single_mask,
            base_amount=secured_amount
        )
        transaction_references=trd_gsc_view_result[0]
        self.assertEqual(mortgage_account_same_branch_mask, trd_gsc_view_result[1])
        self.assertEqual(trade_account_mask_05, trd_gsc_view_result[2])
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_05,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )
        # view mortgage account information
        self.mortgage_account_view(
            account_number=mortgage_account_same_branch_mask,
            customer_code=customer_code_single_mask,
            branch_code=branch_code,
            collateral_account_status=status_normal,
            catalogue_code=catalogue_code_mortgage,
            open_date=working_date,
            collateral_asset_value=secured_amount,
            market_value='0.00',
            forced_sale_value=secured_amount,
            current_secure_amount=secured_amount,
            cc_amount='0.00',
            released_collateral_amount='0.00'
        )

    def test_005_bg_process_05_open_deposit_margin_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_account_same_branch, deposit_gl_number_same_branch
        deposit_gl_number_same_branch = f'{branch_code}-2020301010202-01'
        # open deposit account
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_single_mask,
            customer_type='Single customer',
            catalogue_code=deposit_catalog_current,
            reason_of_account_opening='test release margin'
        )
        deposit_account_same_branch = dpt_opn_result[1]

    def test_005_bg_process_06_approve_and_deposit_money_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # login checker user
        self.logout()
        self.login(username_approve, password_approve)
        # approve deposit account
        self.dpt_apr(
            account_number=deposit_account_same_branch
        )
        # login main user again
        self.logout()
        self.login(username, password, one_app=ONE_APP)
        # cash deposit account
        dpt_cdp_result = self.dpt_cdp(
            account_number=deposit_account_same_branch,
            amount_deposit=current_balance_005_1st,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.assertEqual(deposit_account_same_branch, dpt_cdp_result[1])

    def test_005_bg_process_07_cheque_01_dpt_srg_stock_registration_success(self):
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

    def test_005_bg_process_07_cheque_02_dpt_sat_stock_assign_to_staff_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_sat_result = self.dpt_sat(
            stock_type=stock_type_cq,
            from_serial=from_serial_cq,
            to_serial=to_serial_cq,
            assigned_staff_code=username
        )
        self.assertEqual(from_serial_cq, dpt_sat_result[1])
        self.assertEqual(to_serial_cq, dpt_sat_result[2])

    def test_005_bg_process_07_cheque_03_dpt_ccr_stock_confirm_received_success(self):
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

    def test_005_bg_process_07_cheque_04_dpt_cis_cheque_book_issued_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_cis_result = self.dpt_cis(
            account_number=deposit_account_same_branch,
            from_serial=from_serial_cq,
            to_serial=to_serial_cq,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
        )
        self.assertEqual(from_serial_cq, dpt_cis_result[1])
        self.assertEqual(to_serial_cq, dpt_cis_result[2])

    def test_005_bg_process_08_trd_siv_verify_margin_and_collect_fee_by_deposit_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_05,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )
        # make transaction
        trd_siv_result = self.trd_siv(
            account_number=trade_account_mask_05,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_have_margin,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount=secured_amount,
            applicant=applicant,
            margin_method='Deposit',
            margin_deposit_account=deposit_account_same_branch,
            cheque_no=self.get_next_serial_number(stock_prefix_cq, from_serial_cq, 3),
            fee_collect_method='Deposit',
            account_number_for_fee=str(deposit_account_same_branch).replace('-', ''),
            approve_later='Y'
        )
        transaction_references=trd_siv_result[0]
        self.assertEqual(trade_account_mask_05, trd_siv_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_siv_view_result = self.trd_siv_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_05,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_have_margin,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            secured_amount=secured_amount,
            applicant=applicant,
            margin_method='Deposit',
            margin_deposit_account=deposit_account_same_branch,
            cheque_no=self.get_next_serial_number(stock_prefix_cq, from_serial_cq, 3),
            fee_collect_method='Deposit',
            account_number_for_fee=str(deposit_account_same_branch).replace('-', '')
        )
        transaction_references=trd_siv_view_result[0]
        self.assertEqual(trade_account_mask_05, trd_siv_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (trade_gl_number, sg_bg_amount),
                (deposit_gl_number_same_branch, margin_amount),
                (deposit_gl_number_same_branch, total_fee_amount_10),
            ],
            'expected_credits': [
                (liability_gl_number, sg_bg_amount),
                (suspend_gl_number, margin_amount),
                (ifcc_gl_number, total_fee_amount_10),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_05,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account=deposit_account_same_branch,
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # check deposit account information
        self.deposit_account_view(
            account_number=deposit_account_same_branch,
            current_balance=current_balance_005_after_verify_bg_have_fee,
            earmark_block_amount='0.00'
        )
        # check deposit account history
        expected_trans_code=['DPT_OPN','DPT_APR','DPT_CDP','DPT_CIS']
        expected_users=[username] + [username_approve] + [username] * 2
        expected_channels=['Core Banking'] * 4
        expected_debits=['0.00'] * 4
        expected_credits=['0.00'] * 2 + [current_balance_005_1st] + ['0.00']
        expected_balances=['0.00'] * 2 + [current_balance_005_1st] * 2
        expected_dates=[working_date] * 4
        dpt_his_result = self.dpt_his(
            account_number=deposit_account_same_branch,
            transaction_codes=expected_trans_code,
            expected_debits=expected_debits,
            expected_credits=expected_credits,
            expected_balances=expected_balances,
            expected_created_bys=expected_users,
            expected_channels=expected_channels,
            expected_transaction_dates=expected_dates
        )
        self.assertEqual(deposit_account_same_branch, dpt_his_result[1])
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Debit', 5, total_fee_amount_10)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Debit', 6, margin_amount)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Balance', 5, current_balance_005_after_verify_bg_no_fee)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Balance', 6, current_balance_005_after_verify_bg_have_fee)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Created by', 5, username)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Created by', 6, username)

    def test_005_bg_process_09_cheque_01_dpt_ciq_cheque_inquiry_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        serial_numbers = self.get_list_serial_number(stock_prefix_cq, from_serial_cq, to_serial_cq)
        dpt_ciq_result = self.dpt_ciq(
            account_number=deposit_account_same_branch,
            serial_number=from_serial_cq,
            serial_numbers=serial_numbers,
            expected_values=expected_values
        )
        self.assertEqual(from_serial_cq, dpt_ciq_result[1])

    def test_005_bg_process_09_cheque_02_dpt_sls_cheque_leaves_status_inquiry_success(self):
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

    def test_005_bg_process_10_trd_sbx_extension_collect_fee_by_deposit_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_05,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account=deposit_account_same_branch,
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_05,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            fee_collect_method='Deposit',
            account_number_for_fee=str(deposit_account_same_branch).replace('-', ''),
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_05, trd_sbx_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_05,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            fee_collect_method='Deposit',
            account_number_for_fee=str(deposit_account_same_branch).replace('-', '')
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_05, trd_sbx_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (deposit_gl_number_same_branch, total_fee_amount_9),
            ],
            'expected_credits': [
                (ifcc_gl_number, total_fee_amount_9),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_05,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account=deposit_account_same_branch,
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # check deposit account information
        self.deposit_account_view(
            account_number=deposit_account_same_branch,
            current_balance=current_balance_005_after_collect_fee_extend_bg,
            earmark_block_amount='0.00'
        )
        # check deposit account history
        expected_trans_code=['DPT_OPN','DPT_APR','DPT_CDP','DPT_CIS','TRD_SBX']
        expected_users=[username] + [username_approve] + [username] * 3
        expected_channels=['Core Banking'] * 5
        expected_debits=['0.00'] * 4 + [total_fee_amount_9]
        expected_credits=['0.00'] * 2 + [current_balance_005_1st] + ['0.00'] * 2
        expected_balances=['0.00'] * 2 + [current_balance_005_1st] * 2 + [current_balance_005_after_collect_fee_extend_bg]
        expected_dates=[working_date] * 5
        dpt_his_result = self.dpt_his(
            account_number=deposit_account_same_branch,
            transaction_codes=expected_trans_code,
            expected_debits=expected_debits,
            expected_credits=expected_credits,
            expected_balances=expected_balances,
            expected_created_bys=expected_users,
            expected_channels=expected_channels,
            expected_transaction_dates=expected_dates
        )
        self.assertEqual(deposit_account_same_branch, dpt_his_result[1])
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Debit', 5, total_fee_amount_10)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Debit', 6, margin_amount)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Balance', 5, current_balance_005_after_verify_bg_no_fee)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Balance', 6, current_balance_005_after_verify_bg_have_fee)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Created by', 5, username)
        self.fo_assert_text_table_index('Transaction code', 'TRD_SIV', 'Created by', 6, username)

    def test_005_bg_process_11_trd_rsc_release_secure_collateral_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        trd_rsc_result = self.trd_rsc(
            mortgage_account_number=mortgage_account_same_branch_mask,
            asset_booking_value=secured_amount,
            mortgage_account_currency=currency_code,
            trade_finance_account_number=trade_account_mask_05,
            trade_finance_account_currency=currency_code,
            secured_amount_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            release_amount_in_mortgage_currency=secured_amount,
            release_amount_in_tf_currency=secured_amount,
            customer_code=customer_code_single_mask,
            base_amount=secured_amount,
            approve_later='Y'
        )
        transaction_references=trd_rsc_result[0]
        self.assertEqual(mortgage_account_same_branch_mask, trd_rsc_result[1])
        self.assertEqual(trade_account_mask_05, trd_rsc_result[2])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_rsc_view_result = self.trd_rsc_view(
            transaction_references=transaction_references,
            mortgage_account_number=mortgage_account_same_branch_mask,
            asset_booking_value=secured_amount,
            mortgage_account_currency=currency_code,
            trade_finance_account_number=trade_account_mask_05,
            trade_finance_account_currency=currency_code,
            secured_amount_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            release_amount_in_mortgage_currency=secured_amount,
            release_amount_in_tf_currency=secured_amount,
            customer_code=customer_code_single_mask,
            base_amount=secured_amount
        )
        transaction_references=trd_rsc_view_result[0]
        self.assertEqual(mortgage_account_same_branch_mask, trd_rsc_view_result[1])
        self.assertEqual(trade_account_mask_05, trd_rsc_view_result[2])
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_05,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account=deposit_account_same_branch,
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount=secured_amount,
            secured_amount=secured_amount,
            released_secured_amount=secured_amount,
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # view mortgage account information
        self.mortgage_account_view(
            account_number=mortgage_account_same_branch_mask,
            customer_code=customer_code_single_mask,
            branch_code=branch_code,
            collateral_account_status=status_normal,
            catalogue_code=catalogue_code_mortgage,
            open_date=working_date,
            collateral_asset_value=secured_amount,
            market_value='0.00',
            forced_sale_value=secured_amount,
            current_secure_amount='0.00',
            cc_amount='0.00',
            released_collateral_amount=secured_amount
        )

    def test_005_bg_process_12_trd_scl_close_release_margin_by_cash_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_05,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers
        )
        # make transaction
        trd_scl_result = self.trd_scl(
            account_number=trade_account_mask_05,
            margin_method='Cash',
            sg_bg_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            secured_amount=secured_amount,
            bg_number=bg_number,
            approve_later='Y'
        )
        transaction_references=trd_scl_result[0]
        self.assertEqual(trade_account_mask_05, trd_scl_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_scl_view_result = self.trd_scl_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_05,
            margin_method='Cash',
            sg_bg_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            secured_amount=secured_amount,
            bg_number=bg_number
        )
        transaction_references=trd_scl_view_result[0]
        self.assertEqual(trade_account_mask_05, trd_scl_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (liability_gl_number, sg_bg_amount),
                (suspend_gl_number, margin_amount),
            ],
            'expected_credits': [
                (trade_gl_number, sg_bg_amount),
                (cash_gl_number, margin_amount),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_05,
            account_status=status_closed,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date=working_date,
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount=sg_bg_amount,
            margin_rate=margin_rate,
            margin_amount=margin_amount,
            margin_deposit_account=deposit_account_same_branch,
            released_margin_amount=margin_amount,
            guarantee_amount=guarantee_amount_have_margin,
            released_guarantee_amount=released_guarantee_amount_have_margin_and_secured,
            secured_amount=secured_amount,
            released_secured_amount=secured_amount,
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount,
            release_off_balance_sheet_amount=sg_bg_amount
        )
        # check deposit account information
        self.deposit_account_view(
            account_number=deposit_account_same_branch,
            current_balance=current_balance_005_after_collect_fee_extend_bg,
            earmark_block_amount='0.00'
        )


# CASE 6: NO NEED TO DEPOSIT/CASH MARGIN AND NEED TO SECURE GUARANTEE
    def test_006_bg_process_01_trd_sni_issue_for_collection_no_margin_and_need_secure_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global trade_account_mask_06
        # make transaction
        trd_sni_result = self.trd_sni(
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            guarantee_amount=guarantee_amount_no_margin,
            secured_amount=secured_amount,
            approve_later='Y'
        )
        transaction_references=trd_sni_result[0]
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sni_view_result = self.trd_sni_view(
            transaction_references=transaction_references,
            category_code=category_code,
            account_holder_code=customer_code_single_mask,
            applicant=applicant,
            beneficiary=beneficiary,
            beneficiary_address=beneficiary_address,
            currency_code=currency_code,
            issued_date=issued_date,
            effect_date=effect_date,
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            maturity_date=maturity_date,
            sg_bg_amount=sg_bg_amount,
            project_name=project_name,
            bg_number=bg_number,
            send_to=send_to,
            guarantee_amount=guarantee_amount_no_margin,
            secured_amount=secured_amount
        )
        trade_account_mask_06=trd_sni_view_result[1]
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_06,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )

    def test_006_bg_process_02_document_attachment_add_and_approve_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction add
        self.trade_document_attachment_add(
            account_number=trade_account_mask_06,
            file_path=file_path,
            expire_date=expire_date,
            document_description=document_description
        )
        # make transaction approve
        self.trade_document_attachment_approve(
            account_number=trade_account_mask_06
        )

    def test_006_bg_process_03_open_and_approve_mortgage_account_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # open mortgage account
        global mortgage_account_same_branch_mask_006
        mtg_opn_result = self.mtg_opn(
            customer_code=customer_code_single_mask,
            catalogue_code=catalogue_code_mortgage,
            collateral_asset_value=secured_amount,
            reference_number='Ref AUTO TEST',
            evaluate_by='By AUTO TEST',
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        mortgage_account_same_branch_mask_006 = mtg_opn_result[1]
        # login checker user
        self.logout()
        self.login(username_approve, password_approve)
        # approve mortgage account
        self.mtg_apr(
            account_number=mortgage_account_same_branch_mask_006,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        # login main user again
        self.logout()
        self.login(username, password, one_app=ONE_APP)
        # view mortgage account information
        self.mortgage_account_view(
            account_number=mortgage_account_same_branch_mask_006,
            customer_code=customer_code_single_mask,
            branch_code=branch_code,
            collateral_account_status=status_normal,
            catalogue_code=catalogue_code_mortgage,
            open_date=working_date,
            collateral_asset_value=secured_amount,
            market_value='0.00',
            forced_sale_value=secured_amount,
            current_secure_amount='0.00',
            cc_amount='0.00',
            released_collateral_amount='0.00'
        )

    def test_006_bg_process_04_trd_gsc_guarantee_by_secure_collateral_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        trd_gsc_result = self.trd_gsc(
            mortgage_account_number=mortgage_account_same_branch_mask_006,
            mortgage_account_currency=currency_code,
            asset_booking_value=secured_amount,
            total_secured_amount_of_mortgage='0.00',
            trade_finance_account_number=trade_account_mask_06,
            trade_finance_account_currency=currency_code,
            secure_required=secured_amount,
            secured_amount_for_tf_account='0.00',
            total_secured_amount_of_tf_account='0.00',
            amount_secure_from_this_asset=secured_amount,
            amount_secured_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            customer_code=customer_code_single_mask,
            base_amount=secured_amount,
            approve_later='Y'
        )
        transaction_references=trd_gsc_result[0]
        self.assertEqual(mortgage_account_same_branch_mask_006, trd_gsc_result[1])
        self.assertEqual(trade_account_mask_06, trd_gsc_result[2])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_gsc_view_result = self.trd_gsc_view(
            transaction_references=transaction_references,
            mortgage_account_number=mortgage_account_same_branch_mask_006,
            mortgage_account_currency=currency_code,
            asset_booking_value=secured_amount,
            total_secured_amount_of_mortgage='0.00',
            trade_finance_account_number=trade_account_mask_06,
            trade_finance_account_currency=currency_code,
            secure_required=secured_amount,
            secured_amount_for_tf_account='0.00',
            total_secured_amount_of_tf_account='0.00',
            amount_secure_from_this_asset=secured_amount,
            amount_secured_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            customer_code=customer_code_single_mask,
            base_amount=secured_amount
        )
        transaction_references=trd_gsc_view_result[0]
        self.assertEqual(mortgage_account_same_branch_mask_006, trd_gsc_view_result[1])
        self.assertEqual(trade_account_mask_06, trd_gsc_view_result[2])
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_06,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )
        # view mortgage account information
        self.mortgage_account_view(
            account_number=mortgage_account_same_branch_mask_006,
            customer_code=customer_code_single_mask,
            branch_code=branch_code,
            collateral_account_status=status_normal,
            catalogue_code=catalogue_code_mortgage,
            open_date=working_date,
            collateral_asset_value=secured_amount,
            market_value='0.00',
            forced_sale_value=secured_amount,
            current_secure_amount=secured_amount,
            cc_amount='0.00',
            released_collateral_amount='0.00'
        )

    def test_006_bg_process_05_trd_siv_verify_no_margin_and_collect_fee_by_cash_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_06,
            account_status=status_active,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount='0.00'
        )
        # make transaction
        trd_siv_result = self.trd_siv(
            account_number=trade_account_mask_06,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_no_margin,
            margin_rate='0.00',
            margin_amount='0.00',
            secured_amount=secured_amount,
            applicant=applicant,
            margin_method='Cash',
            approve_later='Y'
        )
        transaction_references=trd_siv_result[0]
        self.assertEqual(trade_account_mask_06, trd_siv_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_siv_view_result = self.trd_siv_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_06,
            ifc_code=ifc_10,
            value=value_10,
            total_fee_amount=total_fee_amount_10,
            total_fee=total_fee_10,
            sg_bg_amount=sg_bg_amount,
            guarantee_amount=guarantee_amount_no_margin,
            margin_rate='0.00',
            margin_amount='0.00',
            secured_amount=secured_amount,
            applicant=applicant,
            margin_method='Cash'
        )
        transaction_references=trd_siv_view_result[0]
        self.assertEqual(trade_account_mask_06, trd_siv_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (trade_gl_number, sg_bg_amount),
                (cash_gl_number, total_fee_amount_10),
            ],
            'expected_credits': [
                (liability_gl_number, sg_bg_amount),
                (ifcc_gl_number, total_fee_amount_10),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_06,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_006_bg_process_06_trd_sbx_extension_collect_fee_by_gl_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_06,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=issued_date,
            effective_date=effect_date,
            effective_date_extension=effect_date,
            maturity_date=maturity_date,
            maturity_date_extension=maturity_date,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=guarantee_period,
            guarantee_period_unit=guarantee_period_unit,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # make transaction
        trd_sbx_result = self.trd_sbx(
            account_number=trade_account_mask_06,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            fee_collect_method='Accounting',
            account_number_for_fee=str(fee_collect_gl_number_004).replace('-', ''),
            approve_later='Y'
        )
        transaction_references=trd_sbx_result[0]
        self.assertEqual(trade_account_mask_06, trd_sbx_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_sbx_view_result = self.trd_sbx_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_06,
            applicant=applicant,
            beneficiary=beneficiary,
            sg_bg_amount=sg_bg_amount,
            maturity_date=maturity_date,
            extend_period=extend_period_1st,
            extend_period_unit=extend_period_unit_1st,
            extend_to_date=extend_to_date_1st,
            bg_number=bg_number,
            extension_time='1',
            extension_date=extension_date_1st,
            ifc_code=ifc_9,
            value=value_9,
            total_fee_amount=total_fee_amount_9,
            total_fee=total_fee_9,
            fee_collect_method='Accounting',
            account_number_for_fee=str(fee_collect_gl_number_004).replace('-', '')
        )
        transaction_references=trd_sbx_view_result[0]
        self.assertEqual(trade_account_mask_06, trd_sbx_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (fee_collect_gl_number_004, total_fee_amount_9),
            ],
            'expected_credits': [
                (ifcc_gl_number, total_fee_amount_9),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_06,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount='0.00',
            secured_amount=secured_amount,
            released_secured_amount='0.00',
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )

    def test_006_bg_process_07_trd_rsc_release_secure_collateral_same_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # make transaction
        trd_rsc_result = self.trd_rsc(
            mortgage_account_number=mortgage_account_same_branch_mask_006,
            asset_booking_value=secured_amount,
            mortgage_account_currency=currency_code,
            trade_finance_account_number=trade_account_mask_06,
            trade_finance_account_currency=currency_code,
            secured_amount_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            release_amount_in_mortgage_currency=secured_amount,
            release_amount_in_tf_currency=secured_amount,
            customer_code=customer_code_single_mask,
            base_amount=secured_amount,
            approve_later='Y'
        )
        transaction_references=trd_rsc_result[0]
        self.assertEqual(mortgage_account_same_branch_mask_006, trd_rsc_result[1])
        self.assertEqual(trade_account_mask_06, trd_rsc_result[2])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_rsc_view_result = self.trd_rsc_view(
            transaction_references=transaction_references,
            mortgage_account_number=mortgage_account_same_branch_mask_006,
            asset_booking_value=secured_amount,
            mortgage_account_currency=currency_code,
            trade_finance_account_number=trade_account_mask_06,
            trade_finance_account_currency=currency_code,
            secured_amount_for_tf_account=secured_amount,
            exchange_rate='1.000000000',
            release_amount_in_mortgage_currency=secured_amount,
            release_amount_in_tf_currency=secured_amount,
            customer_code=customer_code_single_mask,
            base_amount=secured_amount
        )
        transaction_references=trd_rsc_view_result[0]
        self.assertEqual(mortgage_account_same_branch_mask_006, trd_rsc_view_result[1])
        self.assertEqual(trade_account_mask_06, trd_rsc_view_result[2])
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_06,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date='',
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount='0.00',
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount=secured_amount,
            secured_amount=secured_amount,
            released_secured_amount=secured_amount,
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount
        )
        # view mortgage account information
        self.mortgage_account_view(
            account_number=mortgage_account_same_branch_mask_006,
            customer_code=customer_code_single_mask,
            branch_code=branch_code,
            collateral_account_status=status_normal,
            catalogue_code=catalogue_code_mortgage,
            open_date=working_date,
            collateral_asset_value=secured_amount,
            market_value='0.00',
            forced_sale_value=secured_amount,
            current_secure_amount='0.00',
            cc_amount='0.00',
            released_collateral_amount=secured_amount
        )

    def test_006_bg_process_08_trd_scl_close_no_margin_success(self):
        # view account information before
        self.trade_account_view(
            account_number=trade_account_mask_06,
            account_status=status_normal,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers
        )
        # make transaction
        trd_scl_result = self.trd_scl(
            account_number=trade_account_mask_06,
            sg_bg_amount=sg_bg_amount,
            margin_rate='0.00',
            margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            secured_amount=secured_amount,
            bg_number=bg_number,
            approve_later='Y'
        )
        transaction_references=trd_scl_result[0]
        self.assertEqual(trade_account_mask_06, trd_scl_result[1])
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        trd_scl_view_result = self.trd_scl_view(
            transaction_references=transaction_references,
            account_number=trade_account_mask_06,
            sg_bg_amount=sg_bg_amount,
            margin_rate='0.00',
            margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            secured_amount=secured_amount,
            bg_number=bg_number
        )
        transaction_references=trd_scl_view_result[0]
        self.assertEqual(trade_account_mask_06, trd_scl_view_result[1])
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (liability_gl_number, sg_bg_amount),
            ],
            'expected_credits': [
                (trade_gl_number, sg_bg_amount),
            ],
        }
        self.assert_posting_data(**expected_posting_01)
        # view account information after
        self.trade_account_view(
            account_number=trade_account_mask_06,
            account_status=status_closed,
            expected_account_gl_names=expected_account_gl_names,
            expected_account_gl_numbers=expected_account_gl_numbers,
            account_name=applicant,
            branch_code=branch_code,
            category_code=category_code,
            currency_code=currency_code,
            counter_party_name=beneficiary,
            counter_party_address=beneficiary_address,
            open_date=issued_date,
            close_date=working_date,
            extension_date=extension_date_1st,
            effective_date=effect_date,
            effective_date_extension=effective_date_extension_1st,
            maturity_date=maturity_date,
            maturity_date_extension=extend_to_date_1st,
            last_transaction_date=working_date,
            amount=sg_bg_amount,
            release_amount=sg_bg_amount,
            margin_rate='0.00',
            margin_amount='0.00',
            margin_deposit_account='',
            released_margin_amount='0.00',
            guarantee_amount=guarantee_amount_no_margin,
            released_guarantee_amount=released_guarantee_amount_no_margin_and_secured,
            secured_amount=secured_amount,
            released_secured_amount=secured_amount,
            guarantee_period=extend_period_1st,
            guarantee_period_unit=extend_period_unit_1st,
            bg_number=bg_number,
            project_name=project_name,
            send_to=send_to,
            off_balance_sheet_amount=sg_bg_amount,
            release_off_balance_sheet_amount=sg_bg_amount
        )

if __name__ == '__main__': 
    webui_test.main()