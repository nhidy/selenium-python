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

# data test
# date_time=datetime.now().strftime('%d%m%Y 002')
# customer information
customer_code=customer_code_personal
customer_type='Single customer'
currency_short_code_mmk = '01' # MMK
currency_short_code_usd = '02' # USD

class FXTransactionTest(FormAction):
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
        global gl_cash_mmk, gl_cash_usd, account_number_debit_mmk, account_number_credit_mmk, account_number_debit_usd, account_number_credit_usd, ifcc_gl_number_346, ifcc_gl_number_302
        gl_cash_mmk=f'{branch_code}-1010301000101-01'
        gl_cash_usd=f'{branch_code}-1010301000101-02'
        account_number_debit_mmk=f'{branch_code}-1010107777777-{currency_short_code_mmk}'
        account_number_credit_mmk=f'{branch_code}-1100601000000-{currency_short_code_mmk}'
        account_number_debit_usd=f'{branch_code}-1010107777777-{currency_short_code_usd}'
        account_number_credit_usd=f'{branch_code}-1100601000000-{currency_short_code_usd}'
        ifcc_gl_number_346=f'{branch_code}-2070501000101-{currency_short_code_mmk}'
        ifcc_gl_number_302=f'{branch_code}-3030301000101-{currency_short_code_mmk}'
        global deposit_gl_mmk, deposit_gl_usd, deposit_gl_sgd
        deposit_gl_mmk=f'{branch_code}-2020301010202-01'
        deposit_gl_usd=f'{branch_code}-2020301010101-02'
        deposit_gl_sgd=f'{branch_code}-2020301010101-04'

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
            account_number=account_number_debit_mmk
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=account_number_credit_mmk
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='USD',
            account_number=account_number_debit_usd
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='USD',
            account_number=account_number_credit_usd
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=ifcc_gl_number_346
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=ifcc_gl_number_302
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=deposit_gl_mmk
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='USD',
            account_number=deposit_gl_usd
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='SGD',
            account_number=deposit_gl_sgd
        )

    def test_000_02_create_other_deposit_account_use_for_testing(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_account_current_usd, deposit_account_current_sgd, deposit_account_current_mmk
        catalogue_code_current_usd='CAUSD0000'
        catalogue_code_current_mmk='CAMMK0000'
        catalogue_code_current_sgd='CASGD0000'
        reason_of_account_opening='Enter value reason of account opening'
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code_current_usd,
            reason_of_account_opening=reason_of_account_opening
        )
        deposit_account_current_usd=dpt_opn_result[1]

        self.dpt_apr(
            account_number=deposit_account_current_usd,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cdp(
            account_number=deposit_account_current_usd,
            amount_deposit='3,000,000.45',
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code_current_sgd,
            reason_of_account_opening=reason_of_account_opening
        )
        deposit_account_current_sgd=dpt_opn_result[1]

        self.dpt_apr(
            account_number=deposit_account_current_sgd,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cdp(
            account_number=deposit_account_current_sgd,
            amount_deposit='3,000,000.45',
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code=catalogue_code_current_mmk,
            reason_of_account_opening=reason_of_account_opening
        )
        deposit_account_current_mmk=dpt_opn_result[1]

        self.dpt_apr(
            account_number=deposit_account_current_mmk,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cdp(
            account_number=deposit_account_current_mmk,
            amount_deposit='3,000,000.45',
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )

    def test_001_act_act_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        accounting_type_debit = 'Accounting'
        accounting_type_credit = 'Accounting'
        enter_side = 'D'
        account_name_debit=''
        currency_debit=''
        type_debit = ''
        account_name_credit=''
        currency_credit=''
        type_credit = ''
        debit_amount = '1,000,000.45'
        market_dr_rate = ''
        cross_rate = ''
        market_cr_rate = ''
        reverse_rate = ''
        credit_amount = '1,000,000.45'
        fee_amount = '2,500.00'
        receive_amount = '997,500.45'
        full_name = ''
        paper_type = ''
        paper_number = ''
        telephone = ''
        address = ''
        nationality = ''
        description = ''
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.10000']
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.10000 / 100 * 1,000,000.45) = 2,500.00
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '1,000.00'
        act_act_result = self.act_act(
            accounting_type_debit=accounting_type_debit,
            account_number_debit=account_number_debit_mmk,
            account_name_debit=account_name_debit,
            currency_debit=currency_debit,
            type_debit=type_debit,
            accounting_type_credit=accounting_type_credit,
            account_number_credit=account_number_credit_mmk,
            account_name_credit=account_name_credit,
            currency_credit=currency_credit,
            type_credit=type_credit,
            enter_side=enter_side,
            market_dr_rate=market_dr_rate,
            cross_rate=cross_rate,
            market_cr_rate=market_cr_rate,
            debit_amount=debit_amount,
            reverse_rate=reverse_rate,
            credit_amount=credit_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            customer_type=customer_type,
            customer_code=customer_code,
            full_name=full_name,
            paper_type=paper_type,
            paper_number=paper_number,
            telephone=telephone,
            address=address,
            nationality=nationality,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later='Y'
        )
        transaction_references=act_act_result
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        act_act_view_result = self.act_act_view(
            transaction_references=transaction_references,
        )
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (account_number_debit_mmk, debit_amount),
                (account_number_credit_mmk, fee_amount),
            ],
            'expected_credits': [
                (account_number_credit_mmk, credit_amount),
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        self.assert_posting_data(**expected_posting_01)

    def test_002_csh_csh_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        enter_side = 'D'
        account_name_debit=''
        currency_debit='MMK'
        type_debit = ''
        account_name_credit=''
        currency_credit='MMK'
        type_credit = ''
        debit_amount = '1,000,000.45'
        market_dr_rate = ''
        cross_rate = ''
        market_cr_rate = ''
        reverse_rate = ''
        credit_amount = '1,000,000.45'
        fee_amount = '2,500.00'
        receive_amount = '997,500.45'
        full_name = ''
        paper_type = ''
        paper_number = ''
        telephone = ''
        address = ''
        nationality = ''
        description = ''
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.10000']
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.10000 / 100 * 1,000,000.45) = 2,500.00
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '1,000.00'
        csh_csh_result = self.csh_csh(
            account_name_debit=account_name_debit,
            currency_debit=currency_debit,
            type_debit=type_debit,
            account_name_credit=account_name_credit,
            currency_credit=currency_credit,
            type_credit=type_credit,
            enter_side=enter_side,
            market_dr_rate=market_dr_rate,
            cross_rate=cross_rate,
            market_cr_rate=market_cr_rate,
            debit_amount=debit_amount,
            reverse_rate=reverse_rate,
            credit_amount=credit_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            customer_type=customer_type,
            customer_code=customer_code,
            full_name=full_name,
            paper_type=paper_type,
            paper_number=paper_number,
            telephone=telephone,
            address=address,
            nationality=nationality,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later='Y'
        )
        transaction_references=csh_csh_result
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        csh_csh_view_result = self.csh_csh_view(
            transaction_references=transaction_references,
        )
        # check account number of posting
        expected_posting_01 = {
            'expected_debits': [
                (gl_cash_mmk, debit_amount),
                (gl_cash_mmk, fee_amount),
            ],
            'expected_credits': [
                (gl_cash_mmk, credit_amount),
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        self.assert_posting_data(**expected_posting_01)

    def test_003_dpt_dpt_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        accounting_type_debit = ''
        account_number_debit = deposit_account_current_sgd
        accounting_type_credit = ''
        account_number_credit = deposit_account_current_mmk
        enter_side = 'D'
        account_name_debit=''
        currency_debit=''
        type_debit = ''
        account_name_credit=''
        currency_credit=''
        type_credit = ''
        debit_amount = '1,000.45'
        market_dr_rate = '1,559.80000000'
        cross_rate = '1,559.80000000'
        market_cr_rate = '1.00000000'
        reverse_rate = '0.00064111'
        credit_amount = '1,560,501.91'
        fee_amount = '1,700.00'
        receive_amount = '1,558,801.91'
        full_name = ''
        paper_type = ''
        paper_number = ''
        telephone = ''
        address = ''
        nationality = ''
        description = ''
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.01000']
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.01000 / 100 * 1,560,501.91) = 200.00 (Floor)
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '200.00'
        dpt_dpt_result = self.dpt_dpt(
            accounting_type_debit=accounting_type_debit,
            account_number_debit=account_number_debit,
            account_name_debit=account_name_debit,
            currency_debit=currency_debit,
            type_debit=type_debit,
            accounting_type_credit=accounting_type_credit,
            account_number_credit=account_number_credit,
            account_name_credit=account_name_credit,
            currency_credit=currency_credit,
            type_credit=type_credit,
            enter_side=enter_side,
            market_dr_rate=market_dr_rate,
            cross_rate=cross_rate,
            market_cr_rate=market_cr_rate,
            debit_amount=debit_amount,
            reverse_rate=reverse_rate,
            credit_amount=credit_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            customer_type=customer_type,
            customer_code=customer_code,
            full_name=full_name,
            paper_type=paper_type,
            paper_number=paper_number,
            telephone=telephone,
            address=address,
            nationality=nationality,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later='Y'
        )
        transaction_references=dpt_dpt_result
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        expected_posting = {
            'expected_debits': [
                (f'{branch_code}502010100010101', credit_amount),
                (deposit_gl_sgd, debit_amount),
                (deposit_gl_mmk, fee_amount),
            ],
            'expected_credits': [
                (deposit_gl_mmk, credit_amount),
                (f'{branch_code}602010100010104', debit_amount),
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        dpt_dpt_view_result = self.dpt_dpt_view(
            transaction_references=transaction_references,
            expected_posting=expected_posting
        )

    def test_004_dpt_dpt_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        accounting_type_debit = ''
        account_number_debit = deposit_account_current_sgd
        accounting_type_credit = ''
        account_number_credit = deposit_account_current_mmk
        enter_side = 'D'
        account_name_debit=''
        currency_debit=''
        type_debit = ''
        account_name_credit=''
        currency_credit=''
        type_credit = ''
        debit_amount = '1,000.45'
        market_dr_rate = '1,559.80000000'
        cross_rate = '1,559.80000000'
        market_cr_rate = '1.00000000'
        reverse_rate = '0.00064111'
        credit_amount = '1,560,501.91'
        fee_amount = '1,700.00'
        receive_amount = '1,558,801.91'
        full_name = ''
        paper_type = ''
        paper_number = ''
        telephone = ''
        address = ''
        nationality = ''
        description = ''
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.01000']
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.01000 / 100 * 1,560,501.91) = 200.00 (Floor)
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '200.00'
        expected_posting = {
            'expected_debits': [
                (f'{branch_code}502010100010101', credit_amount),
                (deposit_gl_sgd, debit_amount),
                (deposit_gl_mmk, fee_amount),
            ],
            'expected_credits': [
                (deposit_gl_mmk, credit_amount),
                (f'{branch_code}602010100010104', debit_amount),
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        dpt_dpt_result = self.dpt_dpt(
            accounting_type_debit=accounting_type_debit,
            account_number_debit=account_number_debit,
            account_name_debit=account_name_debit,
            currency_debit=currency_debit,
            type_debit=type_debit,
            accounting_type_credit=accounting_type_credit,
            account_number_credit=account_number_credit,
            account_name_credit=account_name_credit,
            currency_credit=currency_credit,
            type_credit=type_credit,
            enter_side=enter_side,
            market_dr_rate=market_dr_rate,
            cross_rate=cross_rate,
            market_cr_rate=market_cr_rate,
            debit_amount=debit_amount,
            reverse_rate=reverse_rate,
            credit_amount=credit_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            customer_type=customer_type,
            customer_code=customer_code,
            full_name=full_name,
            paper_type=paper_type,
            paper_number=paper_number,
            telephone=telephone,
            address=address,
            nationality=nationality,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
            expected_posting=expected_posting
        )
        transaction_references=dpt_dpt_result
        dpt_dpt_view_result = self.dpt_dpt_view(
            transaction_references=transaction_references,
            expected_posting=expected_posting
        )

    def test_005_act_dpt_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # accounting_type_debit = ''
        account_number_debit = account_number_debit_usd
        accounting_type_credit = ''
        account_number_credit = deposit_account_current_mmk
        enter_side = 'C'
        account_name_debit=''
        currency_debit=''
        type_debit = ''
        account_name_credit=''
        currency_credit=''
        type_credit = ''
        debit_amount = '1,000.45'
        market_dr_rate = '2,422.00000000'
        cross_rate = '2,422.00000000'
        market_cr_rate = '1.00000000'
        reverse_rate = '0.00041288'
        credit_amount = '2,423,089.90'
        fee_amount = '2,832.70'
        receive_amount = '2,420,257.20'
        full_name = ''
        paper_type = ''
        paper_number = ''
        telephone = ''
        address = ''
        nationality = ''
        description = ''
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.05500']
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.05500 / 100 * 2,423,089.90) = 1,332.70
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '1,332.70'
        act_dpt_result = self.act_dpt(
            account_number_debit=account_number_debit,
            account_name_debit=account_name_debit,
            currency_debit=currency_debit,
            type_debit=type_debit,
            accounting_type_credit=accounting_type_credit,
            account_number_credit=account_number_credit,
            account_name_credit=account_name_credit,
            currency_credit=currency_credit,
            type_credit=type_credit,
            enter_side=enter_side,
            market_dr_rate=market_dr_rate,
            cross_rate=cross_rate,
            market_cr_rate=market_cr_rate,
            debit_amount=debit_amount,
            reverse_rate=reverse_rate,
            credit_amount=credit_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            customer_type=customer_type,
            customer_code=customer_code,
            full_name=full_name,
            paper_type=paper_type,
            paper_number=paper_number,
            telephone=telephone,
            address=address,
            nationality=nationality,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later='Y'
        )
        transaction_references=act_dpt_result
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        expected_posting = {
            'expected_debits': [
                (f'{branch_code}502010100010101', credit_amount),
                (account_number_debit, debit_amount),
                (deposit_gl_mmk, fee_amount),
            ],
            'expected_credits': [
                (deposit_gl_mmk, credit_amount),
                (f'{branch_code}602010100010102', debit_amount),
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        act_dpt_view_result = self.act_dpt_view(
            transaction_references=transaction_references,
            expected_posting=expected_posting
        )

    def test_006_dpt_act_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # deposit_account_current_usd = '12-004-438858-2'
        # accounting_type_debit = ''
        account_number_debit = deposit_account_current_usd
        accounting_type_credit = ''
        account_number_credit = account_number_credit_mmk
        enter_side = 'C'
        account_name_debit=''
        currency_debit=''
        type_debit = ''
        account_name_credit=''
        currency_credit=''
        type_credit = ''
        debit_amount = '1,000.45'
        market_dr_rate = '2,422.00000000'
        cross_rate = '2,422.00000000'
        market_cr_rate = '1.00000000'
        reverse_rate = '0.00041288'
        credit_amount = '2,423,089.90'
        fee_amount = '2,832.70'
        receive_amount = '2,420,257.20'
        full_name = ''
        paper_type = ''
        paper_number = ''
        telephone = ''
        address = ''
        nationality = ''
        description = ''
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.05500']
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.05500 / 100 * 2,423,089.90) = 1,332.70
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '1,332.70'
        
        self.dpt_cdp(
            account_number=deposit_account_current_usd,
            amount_deposit=debit_amount,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        
        dpt_act_result = self.dpt_act(
            account_number_debit=account_number_debit,
            account_name_debit=account_name_debit,
            currency_debit=currency_debit,
            type_debit=type_debit,
            accounting_type_credit=accounting_type_credit,
            account_number_credit=account_number_credit,
            account_name_credit=account_name_credit,
            currency_credit=currency_credit,
            type_credit=type_credit,
            enter_side=enter_side,
            market_dr_rate=market_dr_rate,
            cross_rate=cross_rate,
            market_cr_rate=market_cr_rate,
            debit_amount=debit_amount,
            reverse_rate=reverse_rate,
            credit_amount=credit_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            customer_type=customer_type,
            customer_code=customer_code,
            full_name=full_name,
            paper_type=paper_type,
            paper_number=paper_number,
            telephone=telephone,
            address=address,
            nationality=nationality,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later='Y'
        )
        transaction_references=dpt_act_result
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        expected_posting = {
            'expected_debits': [
                (f'{branch_code}502010100010101', credit_amount),
                (deposit_gl_usd, debit_amount),
                (account_number_credit_mmk, fee_amount),
            ],
            'expected_credits': [
                (account_number_credit_mmk, credit_amount),
                (f'{branch_code}602010100010102', debit_amount),
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        dpt_act_view_result = self.dpt_act_view(
            transaction_references=transaction_references,
            expected_posting=expected_posting
        )

    def test_007_act_csh_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # accounting_type_debit = ''
        account_number_debit = account_number_debit_usd
        accounting_type_credit = ''
        enter_side = 'D'
        account_name_debit=''
        currency_debit='USD'
        type_debit = ''
        account_name_credit=''
        currency_credit='MMK'
        type_credit = ''
        debit_amount = '1,000.45'
        market_dr_rate = '2,422.00000000'
        cross_rate = '2,422.00000000'
        market_cr_rate = '1.00000000'
        reverse_rate = '0.00041288'
        credit_amount = '2,423,089.90'
        fee_amount = '2,832.70'
        receive_amount = '2,420,257.20'
        full_name = ''
        paper_type = ''
        paper_number = ''
        telephone = ''
        address = ''
        nationality = ''
        description = ''
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.05500']
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.05500 / 100 * 2,423,089.90) = 1,332.70
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '1,332.70'
        act_csh_result = self.act_csh(
            account_number_debit=account_number_debit,
            account_name_debit=account_name_debit,
            currency_debit=currency_debit,
            type_debit=type_debit,
            accounting_type_credit=accounting_type_credit,
            account_name_credit=account_name_credit,
            currency_credit=currency_credit,
            type_credit=type_credit,
            enter_side=enter_side,
            market_dr_rate=market_dr_rate,
            cross_rate=cross_rate,
            market_cr_rate=market_cr_rate,
            debit_amount=debit_amount,
            reverse_rate=reverse_rate,
            credit_amount=credit_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            customer_type=customer_type,
            customer_code=customer_code,
            full_name=full_name,
            paper_type=paper_type,
            paper_number=paper_number,
            telephone=telephone,
            address=address,
            nationality=nationality,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later='Y'
        )
        transaction_references=act_csh_result
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        expected_posting = {
            'expected_debits': [
                (f'{branch_code}502010100010101', credit_amount),
                (account_number_debit_usd, debit_amount),
                (gl_cash_mmk, fee_amount),
            ],
            'expected_credits': [
                (gl_cash_mmk, credit_amount),
                (f'{branch_code}602010100010102', debit_amount),
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        act_csh_view_result = self.act_csh_view(
            transaction_references=transaction_references,
            expected_posting=expected_posting
        )

    def test_008_dpt_csh_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # deposit_account_current_usd = '12-004-438858-2'
        # accounting_type_debit = ''
        account_number_debit = deposit_account_current_usd
        accounting_type_credit = ''
        enter_side = 'D'
        account_name_debit=''
        currency_debit='USD'
        type_debit = ''
        account_name_credit=''
        currency_credit='MMK'
        type_credit = ''
        debit_amount = '1,000.45'
        market_dr_rate = '2,422.00000000'
        cross_rate = '2,422.00000000'
        market_cr_rate = '1.00000000'
        reverse_rate = '0.00041288'
        credit_amount = '2,423,089.90'
        fee_amount = '2,832.70'
        receive_amount = '2,420,257.20'
        full_name = ''
        paper_type = ''
        paper_number = ''
        telephone = ''
        address = ''
        nationality = ''
        description = ''
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.05500']
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.05500 / 100 * 2,423,089.90) = 1,332.70
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '1,332.70'
        expected_posting = {
            'expected_debits': [
                (f'{branch_code}502010100010101', credit_amount),
                (deposit_gl_usd, debit_amount),
                (gl_cash_mmk, fee_amount),
            ],
            'expected_credits': [
                (gl_cash_mmk, credit_amount),
                (f'{branch_code}602010100010102', debit_amount),
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        
        self.dpt_cdp(
            account_number=deposit_account_current_usd,
            amount_deposit=debit_amount,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        dpt_csh_result = self.dpt_csh(
            account_number_debit=account_number_debit,
            account_name_debit=account_name_debit,
            currency_debit=currency_debit,
            type_debit=type_debit,
            accounting_type_credit=accounting_type_credit,
            account_name_credit=account_name_credit,
            currency_credit=currency_credit,
            type_credit=type_credit,
            enter_side=enter_side,
            market_dr_rate=market_dr_rate,
            cross_rate=cross_rate,
            market_cr_rate=market_cr_rate,
            debit_amount=debit_amount,
            reverse_rate=reverse_rate,
            credit_amount=credit_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            customer_type=customer_type,
            customer_code=customer_code,
            full_name=full_name,
            paper_type=paper_type,
            paper_number=paper_number,
            telephone=telephone,
            address=address,
            nationality=nationality,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
            expected_posting=expected_posting
        )
        transaction_references=dpt_csh_result
        # self.transaction_approve(
        #     transaction_references=transaction_references, 
        #     username=username_approve,
        #     password=password_approve
        # )
        # view transaction again
        dpt_csh_view_result = self.dpt_csh_view(
            transaction_references=transaction_references,
            expected_posting=expected_posting
        )

    def test_009_csh_act_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # accounting_type_debit = ''
        accounting_type_credit = ''
        account_number_credit = account_number_credit_mmk
        enter_side = 'C'
        account_name_debit=''
        currency_debit='USD'
        type_debit = ''
        account_name_credit=''
        currency_credit='MMK'
        type_credit = ''
        debit_amount = '1,000.45'
        market_dr_rate = '2,422.00000000'
        cross_rate = '2,422.00000000'
        market_cr_rate = '1.00000000'
        reverse_rate = '0.00041288'
        credit_amount = '2,423,089.90'
        fee_amount = '2,832.70'
        receive_amount = '2,420,257.20'
        full_name = ''
        paper_type = ''
        paper_number = ''
        telephone = ''
        address = ''
        nationality = ''
        description = ''
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.05500']
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.05500 / 100 * 2,423,089.90) = 1,332.70
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '1,332.70'
        
        csh_act_result = self.csh_act(
            account_name_debit=account_name_debit,
            currency_debit=currency_debit,
            type_debit=type_debit,
            accounting_type_credit=accounting_type_credit,
            account_number_credit=account_number_credit,
            account_name_credit=account_name_credit,
            currency_credit=currency_credit,
            type_credit=type_credit,
            enter_side=enter_side,
            market_dr_rate=market_dr_rate,
            cross_rate=cross_rate,
            market_cr_rate=market_cr_rate,
            debit_amount=debit_amount,
            reverse_rate=reverse_rate,
            credit_amount=credit_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            customer_type=customer_type,
            customer_code=customer_code,
            full_name=full_name,
            paper_type=paper_type,
            paper_number=paper_number,
            telephone=telephone,
            address=address,
            nationality=nationality,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later='Y'
        )
        transaction_references=csh_act_result
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        expected_posting = {
            'expected_debits': [
                (f'{branch_code}502010100010101', credit_amount),
                (gl_cash_usd, debit_amount),
                (account_number_credit_mmk, fee_amount),
            ],
            'expected_credits': [
                (account_number_credit_mmk, credit_amount),
                (f'{branch_code}602010100010102', debit_amount),
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        csh_act_view_result = self.csh_act_view(
            transaction_references=transaction_references,
            expected_posting=expected_posting
        )

    def test_010_csh_dpt_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # accounting_type_debit = ''
        accounting_type_credit = ''
        account_number_credit = deposit_account_current_mmk
        enter_side = 'C'
        account_name_debit=''
        currency_debit='USD'
        type_debit = ''
        account_name_credit=''
        currency_credit='MMK'
        type_credit = ''
        debit_amount = '1,000.45'
        market_dr_rate = '2,422.00000000'
        cross_rate = '2,422.00000000'
        market_cr_rate = '1.00000000'
        reverse_rate = '0.00041288'
        credit_amount = '2,423,089.90'
        fee_amount = '2,832.70'
        receive_amount = '2,420,257.20'
        full_name = ''
        paper_type = ''
        paper_number = ''
        telephone = ''
        address = ''
        nationality = ''
        description = ''
        ifc_codes = ['346', '302']
        values = ['1,500.00000', '0.05500']
        total_fee = f'Total Amount = {fee_amount}' # 1,500.00000 + (0.05500 / 100 * 2,423,089.90) = 1,332.70
        fee_amount_346 = '1,500.00'
        fee_amount_302 = '1,332.70'
        
        csh_dpt_result = self.csh_dpt(
            account_name_debit=account_name_debit,
            currency_debit=currency_debit,
            type_debit=type_debit,
            accounting_type_credit=accounting_type_credit,
            account_number_credit=account_number_credit,
            account_name_credit=account_name_credit,
            currency_credit=currency_credit,
            type_credit=type_credit,
            enter_side=enter_side,
            market_dr_rate=market_dr_rate,
            cross_rate=cross_rate,
            market_cr_rate=market_cr_rate,
            debit_amount=debit_amount,
            reverse_rate=reverse_rate,
            credit_amount=credit_amount,
            fee_amount=fee_amount,
            receive_amount=receive_amount,
            customer_type=customer_type,
            customer_code=customer_code,
            full_name=full_name,
            paper_type=paper_type,
            paper_number=paper_number,
            telephone=telephone,
            address=address,
            nationality=nationality,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later='Y'
        )
        transaction_references=csh_dpt_result
        self.transaction_approve(
            transaction_references=transaction_references, 
            username=username_approve,
            password=password_approve
        )
        # view transaction again
        expected_posting = {
            'expected_debits': [
                (f'{branch_code}502010100010101', credit_amount),
                (gl_cash_usd, debit_amount),
                (deposit_gl_mmk, fee_amount),
            ],
            'expected_credits': [
                (deposit_gl_mmk, credit_amount),
                (f'{branch_code}602010100010102', debit_amount),
                (ifcc_gl_number_346, fee_amount_346),
                (ifcc_gl_number_302, fee_amount_302),
            ],
        }
        csh_dpt_view_result = self.csh_dpt_view(
            transaction_references=transaction_references,
            expected_posting=expected_posting
        )

if __name__ == '__main__': 
    webui_test.main()