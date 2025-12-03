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

# customer_code=customer_code_personal
# customer_type='Single customer'
currency_short_code_mmk = '01' # MMK
currency_short_code_usd = '02' # USD
currency_mmk = 'MMK'
currency_usd = 'USD'
# date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
# section_name_test = 'ADD personal ' + str(date_time)

class InternalTransactionTest(FormAction):
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
        global gl_cash_mmk, gl_cash_usd, account_number_mmk_01, account_number_mmk_02, account_number_mmk_03, account_number_mmk_04, account_number_usd_01, account_number_usd_02, account_number_usd_03, account_number_usd_04, account_number_cross_branch_mmk_01, account_number_cross_branch_mmk_02
        gl_cash_mmk=f'{branch_code}-1010301000101-01'
        gl_cash_usd=f'{branch_code}-1010301000101-02'
        account_number_mmk_01=f'{branch_code}-1010107777777-{currency_short_code_mmk}'
        account_number_mmk_02=f'{branch_code}-1100601000000-{currency_short_code_mmk}'
        account_number_mmk_03=f'{branch_code}-1100202020101-{currency_short_code_mmk}'
        account_number_mmk_04=f'{branch_code}-2020202032020-{currency_short_code_mmk}'
        account_number_usd_01=f'{branch_code}-1010107777777-{currency_short_code_usd}'
        account_number_usd_02=f'{branch_code}-1100601000000-{currency_short_code_usd}'
        account_number_usd_03=f'{branch_code}-1100202020101-{currency_short_code_usd}'
        account_number_usd_04=f'{branch_code}-2020202032020-{currency_short_code_usd}'
        if branch_code == '003':
            account_number_cross_branch_mmk_01 = f'004-1010107777777-{currency_short_code_mmk}'
            account_number_cross_branch_mmk_02 = f'004-1100601000000-{currency_short_code_mmk}'
        if branch_code == '004':
            account_number_cross_branch_mmk_01 = f'005-1010107777777-{currency_short_code_mmk}'
            account_number_cross_branch_mmk_02 = f'005-1100601000000-{currency_short_code_mmk}'
        if branch_code == '005':
            account_number_cross_branch_mmk_01 = f'004-1010107777777-{currency_short_code_mmk}'
            account_number_cross_branch_mmk_02 = f'004-1100601000000-{currency_short_code_mmk}'

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
            account_number=account_number_mmk_01
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=account_number_mmk_02
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=account_number_mmk_03
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=account_number_mmk_04
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=account_number_cross_branch_mmk_01
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=account_number_cross_branch_mmk_02
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='USD',
            account_number=account_number_usd_01
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='USD',
            account_number=account_number_usd_02
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='USD',
            account_number=account_number_usd_03
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='USD',
            account_number=account_number_usd_04
        )

    def test_001_act_man_two_debit_one_credit_mmk_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        posting_types = ['Debit', 'Debit', 'Credit']
        gl_accounts = [account_number_mmk_01, account_number_mmk_02, account_number_mmk_03]
        currencies = [currency_mmk, currency_mmk, currency_mmk]
        debit_amount_01 = '60,000.05'
        debit_amount_02 = '40,000.06'
        debit_amounts = [debit_amount_01, debit_amount_02, None]
        credit_amount_01 = '100,000.11'
        credit_amounts = [None, None, credit_amount_01]
        descs = ['Desc 01', 'Desc 02', 'Desc 03']
        section_names = ['Section name 01', 'Section name 02', 'Section name 03']
        total_credit_amount = 'Total Amount = 100,000.11'
        value_date = working_date
        reference_document_no = 'reference document no'
        customer_id = customer_code_personal
        customer_account_id = '0035454544'
        user_defined_4 = 'user defined 4'
        user_defined_5 = 'user defined 5'
        expected_posting = {
            'expected_debits': [
                (account_number_mmk_01, debit_amount_01),
                (account_number_mmk_02, debit_amount_02),
            ],
            'expected_credits': [
                (account_number_mmk_03, credit_amount_01),
            ],
        }
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            expected_posting=expected_posting,
        )

    def test_002_act_man_one_debit_two_credit_mmk_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        posting_types = ['Debit', 'Credit', 'Credit']
        gl_accounts = [account_number_mmk_01, account_number_mmk_02, account_number_mmk_03]
        currencies = [currency_mmk, currency_mmk, currency_mmk]
        debit_amount_01 = '100,000.11'
        debit_amounts = [debit_amount_01, None, None]
        credit_amount_01 = '60,000.05'
        credit_amount_02 = '40,000.06'
        credit_amounts = [None, credit_amount_01, credit_amount_02]
        descs = ['Desc 01', 'Desc 02', 'Desc 03']
        section_names = ['Section name 01', 'Section name 02', 'Section name 03']
        total_credit_amount = 'Total Amount = 100,000.11'
        value_date = working_date
        reference_document_no = 'reference document no'
        customer_id = customer_code_personal
        customer_account_id = '0035454544'
        user_defined_4 = 'user defined 4'
        user_defined_5 = 'user defined 5'
        expected_posting = {
            'expected_debits': [
                (account_number_mmk_01, debit_amount_01),
            ],
            'expected_credits': [
                (account_number_mmk_02, credit_amount_01),
                (account_number_mmk_03, credit_amount_02),
            ],
        }
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            expected_posting=expected_posting,
        )

    def test_003_act_man_two_debit_two_credit_mmk_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        posting_types = ['Credit', 'Credit', 'Debit', 'Debit']
        gl_accounts = [account_number_mmk_01, account_number_mmk_02, account_number_mmk_03, account_number_mmk_04]
        currencies = [currency_mmk, currency_mmk, currency_mmk, currency_mmk]
        debit_amount_01 = '40,000.06'
        debit_amount_02 = '60,000.05'
        debit_amounts = [None, None, debit_amount_01, debit_amount_02]
        credit_amount_01 = '60,000.05'
        credit_amount_02 = '40,000.06'
        credit_amounts = [credit_amount_01, credit_amount_02, None, None]
        descs = ['Desc 01', 'Desc 02', 'Desc 03', 'Desc 04']
        section_names = ['Section name 01', 'Section name 02', 'Section name 03', 'Section name 04']
        total_credit_amount = 'Total Amount = 100,000.11'
        value_date = working_date
        reference_document_no = 'reference document no'
        customer_id = customer_code_personal
        customer_account_id = '0035454544'
        user_defined_4 = 'user defined 4'
        user_defined_5 = 'user defined 5'
        expected_posting = {
            'expected_debits': [
                (account_number_mmk_03, debit_amount_01),
                (account_number_mmk_04, debit_amount_02),
            ],
            'expected_credits': [
                (account_number_mmk_01, credit_amount_01),
                (account_number_mmk_02, credit_amount_02),
            ],
        }
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            expected_posting=expected_posting,
        )

    def test_004_act_man_two_debit_two_credit_usd_not_enter_full_fields_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        posting_types = ['Credit', 'Credit', 'Debit', 'Debit']
        gl_accounts = [account_number_usd_01, account_number_usd_02, account_number_usd_03, account_number_usd_04]
        currencies = [currency_usd, currency_usd, currency_usd, currency_usd]
        debit_amount_01 = '40,000.06'
        debit_amount_02 = '60,000.05'
        debit_amounts = [None, None, debit_amount_01, debit_amount_02]
        credit_amount_01 = '60,000.05'
        credit_amount_02 = '40,000.06'
        credit_amounts = [credit_amount_01, credit_amount_02, None, None]
        descs = [None, None, None, None]
        section_names = ['Section name 01', 'Section name 02', 'Section name 03', 'Section name 04']
        total_credit_amount = 'Total Amount = 100,000.11'
        value_date = working_date
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        expected_posting = {
            'expected_debits': [
                (account_number_usd_03, debit_amount_01),
                (account_number_usd_04, debit_amount_02),
            ],
            'expected_credits': [
                (account_number_usd_01, credit_amount_01),
                (account_number_usd_02, credit_amount_02),
            ],
        }
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            expected_posting=expected_posting,
        )

    def test_005_act_man_not_allow_cross_currency(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [f'ERROR: UnBalance Posting in Currency [{currency_mmk}]']
        posting_types = ['Credit', 'Debit']
        gl_accounts = [account_number_mmk_01, account_number_usd_01]
        currencies = [currency_mmk, currency_usd]
        debit_amount_01 = '40,000.06'
        debit_amounts = [None, debit_amount_01]
        credit_amount_01 = '40,000.06'
        credit_amounts = [credit_amount_01, None]
        descs = [None, None]
        section_names = ['Section name 01', 'Section name 02']
        total_credit_amount = 'Total Amount = 40,000.06'
        value_date = None
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message,
        )
        # reject transaction
        self.transaction_reject(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
        )

    def test_006_act_man_invalid_debit_amount_is_zero(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [f'Positive: Debit Amount must be greater than 0']
        posting_types = ['Debit', 'Credit']
        gl_accounts = [account_number_mmk_01, account_number_mmk_02]
        currencies = [currency_mmk, currency_mmk]
        debit_amount_01 = '0'
        debit_amounts = [debit_amount_01, None]
        credit_amount_01 = '40,000.06'
        credit_amounts = [None, credit_amount_01]
        descs = [None, None]
        section_names = ['Section name 01', 'Section name 02']
        total_credit_amount = 'Total Amount = 40,000.06'
        value_date = None
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            list_error_message=list_error_message
        )

    def test_007_act_man_invalid_credit_amount_is_zero(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [f'Positive: Credit Amount must be greater than 0']
        posting_types = ['Debit', 'Credit']
        gl_accounts = [account_number_mmk_01, account_number_mmk_02]
        currencies = [currency_mmk, currency_mmk]
        debit_amount_01 = '40,000.06'
        debit_amounts = [debit_amount_01, None]
        credit_amount_01 = '0.00'
        credit_amounts = [None, credit_amount_01]
        descs = [None, None]
        section_names = ['Section name 01', 'Section name 02']
        total_credit_amount = 'Total Amount = 0.00'
        value_date = None
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message,
        )
        # reject transaction
        self.transaction_reject(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
        )

    def test_008_act_man_invalid_amount_is_not_equal(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [f'ERROR: UnBalance Posting in Currency [{currency_mmk}]']
        posting_types = ['Debit', 'Credit']
        gl_accounts = [account_number_mmk_01, account_number_mmk_02]
        currencies = [currency_mmk, currency_mmk]
        debit_amount_01 = '40,000.06'
        debit_amounts = [debit_amount_01, None]
        credit_amount_01 = '40,000.05'
        credit_amounts = [None, credit_amount_01]
        descs = [None, None]
        section_names = ['Section name 01', 'Section name 02']
        total_credit_amount = 'Total Amount = 40,000.05'
        value_date = None
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message,
        )
        # reject transaction
        self.transaction_reject(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
        )

    def test_009_act_man_not_allow_cross_branch(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [f'ERROR: Only accounts that belong to the operating branch [{branch_code}] are accepted']
        posting_types = ['Debit', 'Credit']
        gl_accounts = [account_number_cross_branch_mmk_01, account_number_mmk_01]
        currencies = [currency_mmk, currency_mmk]
        debit_amount_01 = '40,000.06'
        debit_amounts = [debit_amount_01, None]
        credit_amount_01 = '40,000.06'
        credit_amounts = [None, credit_amount_01]
        descs = [None, None]
        section_names = ['Section name 01', 'Section name 02']
        total_credit_amount = 'Total Amount = 40,000.06'
        value_date = None
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message,
        )
        # reject transaction
        self.transaction_reject(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
        )

    def test_010_act_man_not_allow_other_branch(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = [f'ERROR: Only accounts that belong to the operating branch [{branch_code}] are accepted']
        posting_types = ['Debit', 'Credit']
        gl_accounts = [account_number_cross_branch_mmk_01, account_number_cross_branch_mmk_02]
        currencies = [currency_mmk, currency_mmk]
        debit_amount_01 = '40,000.06'
        debit_amounts = [debit_amount_01, None]
        credit_amount_01 = '40,000.06'
        credit_amounts = [None, credit_amount_01]
        descs = [None, None]
        section_names = ['Section name 01', 'Section name 02']
        total_credit_amount = 'Total Amount = 40,000.06'
        value_date = None
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message,
        )
        # reject transaction
        self.transaction_reject(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
        )

    def test_011_act_man_debit_account_not_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        gl_not_exist = f'{branch_code}-0000000000000-{currency_short_code_mmk}'
        list_error_message = [f'ERROR: {self.no_mask(gl_not_exist)} does not exist']
        posting_types = ['Debit', 'Credit']
        gl_accounts = [gl_not_exist, account_number_mmk_01]
        currencies = [currency_mmk, currency_mmk]
        debit_amount_01 = '40,000.06'
        debit_amounts = [debit_amount_01, None]
        credit_amount_01 = '40,000.06'
        credit_amounts = [None, credit_amount_01]
        descs = [None, None]
        section_names = ['Section name 01', 'Section name 02']
        total_credit_amount = 'Total Amount = 40,000.06'
        value_date = None
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message,
        )
        # reject transaction
        self.transaction_reject(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
        )

    def test_012_act_man_credit_account_not_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        gl_not_exist = f'{branch_code}-0000000000001-{currency_short_code_mmk}'
        list_error_message = [f'ERROR: {self.no_mask(gl_not_exist)} does not exist']
        posting_types = ['Debit', 'Credit']
        gl_accounts = [account_number_mmk_01, gl_not_exist]
        currencies = [currency_mmk, currency_mmk]
        debit_amount_01 = '40,000.06'
        debit_amounts = [debit_amount_01, None]
        credit_amount_01 = '40,000.06'
        credit_amounts = [None, credit_amount_01]
        descs = [None, None]
        section_names = ['Section name 01', 'Section name 02']
        total_credit_amount = 'Total Amount = 40,000.06'
        value_date = None
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            approve_later='Y'
        )
        transaction_references=act_man_result
        # view transaction before approve
        self.act_man_view(
            transaction_references=transaction_references,
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
        )
        # approve transaction
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
            list_error_message=list_error_message,
        )
        # reject transaction
        self.transaction_reject(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve,
        )

    def test_013_act_man_not_allow_empty_account_and_section_name(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message_under_group = ['Account number: Can not be blank', 'Section name: Can not be blank']
        list_error_message = ['ERROR: Not found posting data']
        posting_types = ['Debit']
        gl_accounts = [None]
        currencies = [None]
        debit_amount_01 = [None]
        debit_amounts = [debit_amount_01]
        credit_amount_01 = [None]
        credit_amounts = [credit_amount_01]
        descs = [None]
        section_names = [None]
        total_credit_amount = None
        value_date = None
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            list_error_message_under_group=list_error_message_under_group,
            list_error_message=list_error_message
        )

    def test_014_act_man_not_allow_empty_section_name(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message_under_group = ['Section name: Can not be blank']
        list_error_message = ['ERROR: Not found posting data']
        posting_types = ['Debit']
        gl_accounts = [account_number_mmk_01]
        currencies = [None]
        debit_amount_01 = [None]
        debit_amounts = [debit_amount_01]
        credit_amount_01 = [None]
        credit_amounts = [credit_amount_01]
        descs = [None]
        section_names = [None]
        total_credit_amount = None
        value_date = None
        reference_document_no = None
        customer_id = None
        customer_account_id = None
        user_defined_4 = None
        user_defined_5 = None
        act_man_result = self.act_man(
            posting_types=posting_types,
            gl_accounts=gl_accounts,
            currencies=currencies,
            debit_amounts=debit_amounts,
            credit_amounts=credit_amounts,
            descs=descs,
            section_names=section_names,
            total_credit_amount=total_credit_amount,
            value_date=value_date,
            reference_document_no=reference_document_no,
            customer_id=customer_id,
            customer_account_id=customer_account_id,
            user_defined_4=user_defined_4,
            user_defined_5=user_defined_5,
            list_error_message_under_group=list_error_message_under_group,
            list_error_message=list_error_message
        )

if __name__ == '__main__': 
    webui_test.main()