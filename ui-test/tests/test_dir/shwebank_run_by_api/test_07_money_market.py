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
CUSTOMER_CODE_CORPORATE = os.getenv("TEST_CONFIG_CUSTOMER_CODE_CORPORATE", "")
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

customer_code_corporate = CUSTOMER_CODE_CORPORATE

# data test
catalogue_code_deposit_mmk = 'TMMDPT1001'
catalogue_code_deposit_usd = 'TMMDPT1002'
trade_type_deposit = 'MM Deposit'
catalogue_code_placement_mmk = 'TMMPLA1001'
catalogue_code_placement_usd = 'TMMPLA1002'
trade_type_placement = 'MM Placement'
currency_code_mmk = 'MMK'
currency_code_usd = 'USD'
amount_mmk = '1,000,000.54'
amount_usd = '10,000.65'
tenor_test = '0'
tenor_unit_day = 'Day'
tenor_unit_days = 'Days'
settlement_by_cash = 'Cash'
settlement_by_deposit = 'Deposit'
settlement_by_gl = 'GL'

class MoneyMarketTest(FormAction):
    def get_url(self):
        return RUN_ON_URL

    def data_begin(self):
        # get username_reverse and password_reverse
        global username_approve, password_approve, username_reverse, password_reverse, username_login, password_login, username_approve_other_branch, password_approve_other_branch, username_reverse_other_branch, password_reverse_other_branch, username_other_branch, password_other_branch
        username_approve = USERNAME_APPROVE
        password_approve = PASSWORD_APPROVE
        username_reverse = USERNAME_REVERSE
        password_reverse = PASSWORD_REVERSE
        username_login = USERNAME_LOGIN
        password_login = PASSWORD_LOGIN
        username_approve_other_branch = USERNAME_APPROVE_OTHER_BRANCH
        password_approve_other_branch = PASSWORD_APPROVE_OTHER_BRANCH
        username_reverse_other_branch = USERNAME_REVERSE_OTHER_BRANCH
        password_reverse_other_branch = PASSWORD_REVERSE_OTHER_BRANCH
        username_other_branch = USERNAME_LOGIN_OTHER_BRANCH
        password_other_branch = PASSWORD_LOGIN_OTHER_BRANCH
        self.login(username_login, password_login, one_app=ONE_APP)
        global working_date, branch_code
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()
        global gl_account_number_mmk, gl_account_number_usd
        gl_account_number_mmk = f'{branch_code}-1100601000000-01'
        gl_account_number_usd = f'{branch_code}-1100601000000-02'

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
            account_number=gl_account_number_mmk
        )
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='USD',
            account_number=gl_account_number_usd
        )
        if self.check_customer_profile_not_exist(customer_code_corporate):
            self.stop()
            self.fail()

    def test_001_mm_deposit_mmk_01_tmm_opn_open_account_success_no_need_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global account_mm_deposit_mmk_mask
        counterparty_code_test = customer_code_corporate
        catalogue_code_test = catalogue_code_deposit_mmk
        currency_code_test = currency_code_mmk
        trade_type_test = trade_type_deposit
        tenor_unit_test = tenor_unit_day

        tmm_opn_result = self.tmm_opn(
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
        )
        transaction_references=tmm_opn_result[0]
        account_mm_deposit_mmk_mask=tmm_opn_result[1]
        self.tmm_opn_view(
            transaction_references=transaction_references,
            account_number=account_mm_deposit_mmk_mask,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
        )

    def test_001_mm_deposit_mmk_02_tmm_app_approve_account_success_no_need_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_deposit_mmk_mask
        counterparty_code_test = customer_code_corporate
        catalogue_code_test = catalogue_code_deposit_mmk
        currency_code_test = currency_code_mmk
        trade_type_test = trade_type_deposit
        tenor_unit_test = tenor_unit_days

        tmm_app_result = self.tmm_app(
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
        )
        transaction_references=tmm_app_result[0]
        self.tmm_app_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date
        )

    def test_001_mm_deposit_mmk_03_tmm_dep_deposit_to_account_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_deposit_mmk_mask
        counterparty_code_test = customer_code_corporate
        category_code_test = catalogue_code_deposit_mmk
        currency_code_test = currency_code_mmk
        amount_test = amount_mmk
        approve_later = 'Y'
        username = username_approve
        password = password_approve

        tmm_dep_result = self.tmm_dep(
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            category_code=category_code_test,
            currency_code_01=currency_code_test,
            amount=amount_test,
            approve_later=approve_later,
        )
        transaction_references=tmm_dep_result[0]
        account_number_out=tmm_dep_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
        )
        self.tmm_dep_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            category_code=category_code_test,
            currency_code_01=currency_code_test,
            amount=amount_test,
        )

    def test_001_mm_deposit_mmk_04_tmm_wcd_withdraw_and_close_account_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_deposit_mmk_mask
        description_test = None
        account_name_test = None
        debit_by_test = None
        currency_code_test = currency_code_mmk
        account_no_test = None
        interest_accrual_test = None
        interest_due_test = None
        interest_prepaid_test = None
        principal_amount_test = amount_mmk
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        tmm_wcd_result = self.tmm_wcd(
            account_number=account_number_test,
            description=description_test,
            account_name=account_name_test,
            debit_by=debit_by_test,
            currency_code=currency_code_test,
            account_no=account_no_test,
            interest_accrual=interest_accrual_test,
            interest_due=interest_due_test,
            interest_prepaid=interest_prepaid_test,
            principal_amount=principal_amount_test,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=tmm_wcd_result[0]
        account_number_out=tmm_wcd_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.tmm_wcd_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            description=description_test,
            account_name=account_name_test,
            debit_by=debit_by_test,
            currency_code=currency_code_test,
            account_no=account_no_test,
            interest_accrual=interest_accrual_test,
            interest_due=interest_due_test,
            interest_prepaid=interest_prepaid_test,
            principal_amount=principal_amount_test,
            expected_posting=expected_posting,
        )

    def test_002_mm_deposit_usd_01_tmm_opn_open_account_success_no_need_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global account_mm_deposit_usd_mask
        counterparty_code_test = customer_code_corporate
        catalogue_code_test = catalogue_code_deposit_usd
        currency_code_test = currency_code_usd
        trade_type_test = trade_type_deposit
        tenor_unit_test = tenor_unit_day

        tmm_opn_result = self.tmm_opn(
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
        )
        transaction_references=tmm_opn_result[0]
        account_mm_deposit_usd_mask=tmm_opn_result[1]
        self.tmm_opn_view(
            transaction_references=transaction_references,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
        )

    def test_002_mm_deposit_usd_02_tmm_app_approve_account_success_no_need_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_deposit_usd_mask
        counterparty_code_test = customer_code_corporate
        catalogue_code_test = catalogue_code_deposit_usd
        currency_code_test = currency_code_usd
        trade_type_test = trade_type_deposit
        tenor_unit_test = tenor_unit_days

        tmm_app_result = self.tmm_app(
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
        )
        transaction_references=tmm_app_result[0]
        self.tmm_app_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
        )

    def test_002_mm_deposit_usd_03_tmm_dep_deposit_to_account_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_deposit_usd_mask
        counterparty_code_test = customer_code_corporate
        category_code_test = catalogue_code_deposit_usd
        currency_code_test = currency_code_usd
        amount_test = amount_usd
        approve_later = 'Y'
        username = username_approve
        password = password_approve

        tmm_dep_result = self.tmm_dep(
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            category_code=category_code_test,
            currency_code_01=currency_code_test,
            amount=amount_test,
            approve_later=approve_later,
        )
        transaction_references=tmm_dep_result[0]
        account_number_out=tmm_dep_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
        )
        self.tmm_dep_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            category_code=category_code_test,
            currency_code_01=currency_code_test,
            amount=amount_test,
        )

    def test_002_mm_deposit_usd_04_tmm_wcd_withdraw_and_close_account_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_deposit_usd_mask
        description_test = None
        account_name_test = None
        debit_by_test = None
        currency_code_test = currency_code_usd
        account_no_test = None
        interest_accrual_test = None
        interest_due_test = None
        interest_prepaid_test = None
        principal_amount_test = amount_usd
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        tmm_wcd_result = self.tmm_wcd(
            account_number=account_number_test,
            description=description_test,
            account_name=account_name_test,
            debit_by=debit_by_test,
            currency_code=currency_code_test,
            account_no=account_no_test,
            interest_accrual=interest_accrual_test,
            interest_due=interest_due_test,
            interest_prepaid=interest_prepaid_test,
            principal_amount=principal_amount_test,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=tmm_wcd_result[0]
        account_number_out=tmm_wcd_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.tmm_wcd_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            description=description_test,
            account_name=account_name_test,
            debit_by=debit_by_test,
            currency_code=currency_code_test,
            account_no=account_no_test,
            interest_accrual=interest_accrual_test,
            interest_due=interest_due_test,
            interest_prepaid=interest_prepaid_test,
            principal_amount=principal_amount_test,
            expected_posting=expected_posting,
        )

    def test_003_mm_placement_mmk_01_tmm_opn_open_account_success_no_need_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global account_mm_placement_mmk_mask
        counterparty_code_test = customer_code_corporate
        catalogue_code_test = catalogue_code_placement_mmk
        currency_code_test = currency_code_mmk
        trade_type_test = trade_type_placement
        tenor_unit_test = tenor_unit_day

        tmm_opn_result = self.tmm_opn(
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            on_value_date_settlement_by=settlement_by_gl,
            on_value_date_account_no_act=gl_account_number_mmk,
            on_maturity_settlement_by=settlement_by_gl,
            on_maturity_account_no_act=gl_account_number_mmk,
        )
        transaction_references=tmm_opn_result[0]
        account_mm_placement_mmk_mask=tmm_opn_result[1]
        self.tmm_opn_view(
            transaction_references=transaction_references,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
            on_value_date_settlement_by=settlement_by_gl,
            on_value_date_account_no_act=gl_account_number_mmk,
            on_maturity_settlement_by=settlement_by_gl,
            on_maturity_account_no_act=gl_account_number_mmk,
        )

    def test_003_mm_placement_mmk_02_tmm_app_approve_account_success_no_need_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_placement_mmk_mask
        counterparty_code_test = customer_code_corporate
        catalogue_code_test = catalogue_code_placement_mmk
        currency_code_test = currency_code_mmk
        trade_type_test = trade_type_placement
        tenor_unit_test = tenor_unit_days

        tmm_app_result = self.tmm_app(
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
        )
        transaction_references=tmm_app_result[0]
        self.tmm_app_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
        )

    def test_003_mm_placement_mmk_03_tmm_pma_placement_to_account_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_placement_mmk_mask
        amount_test = amount_mmk
        description_test = None
        counterparty_type_test = None
        counterparty_code_test = customer_code_corporate
        counterparty_mm_limit_bcy_test = None
        category_code_test = catalogue_code_placement_mmk
        trade_type_test = trade_type_placement
        currency_code_01_test = currency_code_mmk
        account_name_test = None
        credit_by_test = settlement_by_gl
        currency_code_02_test = None
        account_no_test = gl_account_number_mmk
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        tmm_pma_result = self.tmm_pma(
            account_number=account_number_test,
            amount=amount_test,
            description=description_test,
            counterparty_type=counterparty_type_test,
            counterparty_code=counterparty_code_test,
            counterparty_mm_limit_bcy=counterparty_mm_limit_bcy_test,
            category_code=category_code_test,
            trade_type=trade_type_test,
            currency_code_01=currency_code_01_test,
            account_name=account_name_test,
            credit_by=credit_by_test,
            currency_code_02=currency_code_02_test,
            account_no=account_no_test,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=tmm_pma_result[0]
        account_number_out=tmm_pma_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.tmm_pma_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            amount=amount_test,
            description=description_test,
            counterparty_type=counterparty_type_test,
            counterparty_code=counterparty_code_test,
            counterparty_mm_limit_bcy=counterparty_mm_limit_bcy_test,
            category_code=category_code_test,
            trade_type=trade_type_test,
            currency_code_01=currency_code_01_test,
            account_name=account_name_test,
            credit_by=credit_by_test,
            currency_code_02=currency_code_02_test,
            account_no=account_no_test,
            expected_posting=expected_posting,
        )

    def test_003_mm_placement_mmk_04_tmm_wcp_withdraw_and_close_placement_account_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_placement_mmk_mask
        description_test = None
        account_name_test = None
        debit_by_test = settlement_by_gl
        currency_code_test = currency_code_mmk
        account_no_test = gl_account_number_mmk
        interest_accrual_test = None
        interest_payable_test = None
        interest_due_test = None
        principal_amount_test = amount_mmk
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        tmm_wcp_result = self.tmm_wcp(
            account_number=account_number_test,
            description=description_test,
            account_name=account_name_test,
            debit_by=debit_by_test,
            currency_code=currency_code_test,
            account_no=account_no_test,
            interest_accrual=interest_accrual_test,
            interest_payable=interest_payable_test,
            interest_due=interest_due_test,
            principal_amount=principal_amount_test,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=tmm_wcp_result[0]
        account_number_out=tmm_wcp_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.tmm_wcp_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            description=description_test,
            account_name=account_name_test,
            debit_by=debit_by_test,
            currency_code=currency_code_test,
            account_no=account_no_test,
            interest_accrual=interest_accrual_test,
            interest_payable=interest_payable_test,
            interest_due=interest_due_test,
            principal_amount=principal_amount_test,
            expected_posting=expected_posting,
        )

    def test_004_mm_placement_usd_01_tmm_opn_open_account_success_no_need_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global account_mm_placement_usd_mask
        counterparty_code_test = customer_code_corporate
        catalogue_code_test = catalogue_code_placement_usd
        currency_code_test = currency_code_usd
        trade_type_test = trade_type_placement
        tenor_unit_test = tenor_unit_day

        tmm_opn_result = self.tmm_opn(
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            on_value_date_settlement_by=settlement_by_gl,
            on_value_date_account_no_act=gl_account_number_usd,
            on_maturity_settlement_by=settlement_by_gl,
            on_maturity_account_no_act=gl_account_number_usd,
        )
        transaction_references=tmm_opn_result[0]
        account_mm_placement_usd_mask=tmm_opn_result[1]
        self.tmm_opn_view(
            transaction_references=transaction_references,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
            on_value_date_settlement_by=settlement_by_gl,
            on_value_date_account_no_act=gl_account_number_usd,
            on_maturity_settlement_by=settlement_by_gl,
            on_maturity_account_no_act=gl_account_number_usd,
        )

    def test_004_mm_placement_usd_02_tmm_app_approve_account_success_no_need_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_placement_usd_mask
        counterparty_code_test = customer_code_corporate
        catalogue_code_test = catalogue_code_placement_usd
        currency_code_test = currency_code_usd
        trade_type_test = trade_type_placement
        tenor_unit_test = tenor_unit_days

        tmm_app_result = self.tmm_app(
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
        )
        transaction_references=tmm_app_result[0]
        self.tmm_app_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            counterparty_code=counterparty_code_test,
            catalogue_code=catalogue_code_test,
            currency_code=currency_code_test,
            trade_type=trade_type_test,
            tenor=tenor_test,
            tenor_unit=tenor_unit_test,
            value_date=working_date,
            trade_date=working_date,
            maturity_date=working_date,
        )

    def test_004_mm_placement_usd_03_tmm_pma_placement_to_account_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_placement_usd_mask
        amount_test = amount_usd
        description_test = None
        counterparty_type_test = None
        counterparty_code_test = customer_code_corporate
        counterparty_mm_limit_bcy_test = None
        category_code_test = catalogue_code_placement_usd
        trade_type_test = trade_type_placement
        currency_code_01_test = currency_code_usd
        account_name_test = None
        credit_by_test = settlement_by_gl
        currency_code_02_test = currency_code_usd
        account_no_test = gl_account_number_usd
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        tmm_pma_result = self.tmm_pma(
            account_number=account_number_test,
            amount=amount_test,
            description=description_test,
            counterparty_type=counterparty_type_test,
            counterparty_code=counterparty_code_test,
            counterparty_mm_limit_bcy=counterparty_mm_limit_bcy_test,
            category_code=category_code_test,
            trade_type=trade_type_test,
            currency_code_01=currency_code_01_test,
            account_name=account_name_test,
            credit_by=credit_by_test,
            currency_code_02=currency_code_02_test,
            account_no=account_no_test,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=tmm_pma_result[0]
        account_number_out=tmm_pma_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.tmm_pma_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            amount=amount_test,
            description=description_test,
            counterparty_type=counterparty_type_test,
            counterparty_code=counterparty_code_test,
            counterparty_mm_limit_bcy=counterparty_mm_limit_bcy_test,
            category_code=category_code_test,
            trade_type=trade_type_test,
            currency_code_01=currency_code_01_test,
            account_name=account_name_test,
            credit_by=credit_by_test,
            currency_code_02=currency_code_02_test,
            account_no=account_no_test,
            expected_posting=expected_posting,
        )

    def test_004_mm_placement_usd_04_tmm_wcp_withdraw_and_close_placement_account_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number_test = account_mm_placement_usd_mask
        description_test = None
        account_name_test = None
        debit_by_test = settlement_by_gl
        currency_code_test = currency_code_usd
        account_no_test = gl_account_number_usd
        interest_accrual_test = None
        interest_payable_test = None
        interest_due_test = None
        principal_amount_test = amount_usd
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        tmm_wcp_result = self.tmm_wcp(
            account_number=account_number_test,
            description=description_test,
            account_name=account_name_test,
            debit_by=debit_by_test,
            currency_code=currency_code_test,
            account_no=account_no_test,
            interest_accrual=interest_accrual_test,
            interest_payable=interest_payable_test,
            interest_due=interest_due_test,
            principal_amount=principal_amount_test,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=tmm_wcp_result[0]
        account_number_out=tmm_wcp_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.tmm_wcp_view(
            transaction_references=transaction_references,
            account_number=account_number_test,
            description=description_test,
            account_name=account_name_test,
            debit_by=debit_by_test,
            currency_code=currency_code_test,
            account_no=account_no_test,
            interest_accrual=interest_accrual_test,
            interest_payable=interest_payable_test,
            interest_due=interest_due_test,
            principal_amount=principal_amount_test,
            expected_posting=expected_posting,
        )

if __name__ == '__main__': 
    webui_test.main()