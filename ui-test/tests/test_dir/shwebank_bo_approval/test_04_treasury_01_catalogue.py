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

customer_code_personal = CUSTOMER_CODE

random_num = f"{random.randint(0, 99999):06}"
date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

action_add ='TRS-Catalogue Definition-Add'
action_update ='TRS-Catalogue Definition-Update'
catalogue_code_in_use = 'TMMDPT1001'
list_error_message_in_use = [f'ERROR: CatalogCode [{catalogue_code_in_use}] is used by other treasury account']
tran_name_delete = 'TRS_DELETE_CATALOG'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_catalogue_code = 'AUTO000001'
value_trade_group = 'Monetary market'
value_details_category = 'MM Deposit'
value_trade_type = 'MM Deposit'
value_margin_trading = 'No'
value_market = 'Financial Market'
value_catalogue_status = 'Normal'
value_settle_tenor = '1.00'
value_settle_tenor_unit = 'Days'
value_tenor = '5.00'
value_tenor_unit = 'Day'
value_interest_tenor = '0.00'
value_interest_tenor_unit = 'Lumpsum'
value_rollover_option = 'Principal Rollover Only'
value_revaluation = 'Yes'
value_user_create = USERNAME_LOGIN
value_approve_by = USERNAME_APPROVE
value_ifc_codes = ['MM Deposit Normal Interest (FCY)']
value_expected_ifc_list_codes =  ['4']
value_expected_ifc_names = value_ifc_codes
value_expected_ifc_values = ['0.00000']
value_expected_ifc_types = ['Interest']
value_expected_ifc_tenors = ['360']
value_expected_ifc_tenor_units = ['Day(s)']
value_expected_ifc_statuses = ['Normal']
value_expected_gls_account_aliass = ['###{REF}**']
value_expected_gls_sys_account_names = ['TREASURY']
value_expected_extension_sys_account_names = ['TREASURY', 'TREASURY']
value_expected_extension_replace_bys = ['2010102011212', '2010102010808']
value_business_lines = ['Corporate', 'Institutional']
value_bank_identifications = ['Shinhan', 'MOB']
value_expected_extension_conditions_add = [
    '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-","bank_identification":"0003"}',
    '{"sector":"-","resident_status":"-","categories":"C4","subproduct":"-","bank_identification":"0018"}'
]
value_expected_extension_conditions_view = [
    '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null,"bank_identification":"0003"}',
    '{"sector":null,"resident_status":null,"categories":"C4","subproduct":null,"bank_identification":"0018"}'
]

# data test add
catalogue_code_test_add = value_catalogue_code
catalogue_name_test_add = f'AUTO TEST add {date_time}'
trade_group_test_add = value_trade_group
details_category_test_add = value_details_category
trade_type_test_add = value_trade_type
margin_trading_test_add = value_margin_trading
market_test_add = value_market
catalogue_status_test_add = value_catalogue_status
settle_tenor_test_add = '1'
settle_tenor_unit_test_add = value_settle_tenor_unit
tenor_test_add = '5'
tenor_unit_test_add = value_tenor_unit
interest_tenor_test_add = '0'
interest_tenor_unit_test_add = value_interest_tenor_unit
rollover_option_test_add = value_rollover_option
revaluation_test_add = value_revaluation
user_create_test_add = value_user_create
approve_by_test_add = None
ifc_codes_test_add = value_ifc_codes
sys_account_names_test_add = value_expected_gls_sys_account_names
account_aliass_test_add = value_expected_gls_account_aliass
coa_accounts_test_add = None
replace_bys_test_add = value_expected_extension_replace_bys
system_account_names_test_add = value_expected_extension_sys_account_names
customer_sectors_test_add = None
customer_resident_statuss_test_add = None
business_lines_test_add = value_business_lines
sub_products_test_add = None
bank_identifications_test_add = value_bank_identifications
replace_code_test_add = None
list_error_message_test_add = None

# data test add verify
catalogue_code_test_add_verify = value_catalogue_code
catalogue_name_test_add_verify = catalogue_name_test_add
trade_group_test_add_verify = value_trade_group
details_category_test_add_verify = value_details_category
trade_type_test_add_verify = value_trade_type
margin_trading_test_add_verify = value_margin_trading
market_test_add_verify = value_market
catalogue_status_test_add_verify = value_catalogue_status
settle_tenor_test_add_verify = settle_tenor_test_add
settle_tenor_unit_test_add_verify = settle_tenor_unit_test_add
tenor_test_add_verify = tenor_test_add
tenor_unit_test_add_verify = value_tenor_unit
interest_tenor_test_add_verify = interest_tenor_test_add
interest_tenor_unit_test_add_verify = value_interest_tenor_unit
rollover_option_test_add_verify = value_rollover_option
revaluation_test_add_verify = value_revaluation
user_create_test_add_verify = value_user_create
approve_by_test_add_verify = None
expected_ifc_list_codes_test_add_verify = value_expected_ifc_list_codes
expected_ifc_names_test_add_verify = value_expected_ifc_names
expected_ifc_values_test_add_verify = value_expected_ifc_values
expected_ifc_types_test_add_verify = value_expected_ifc_types
expected_ifc_tenors_test_add_verify = value_expected_ifc_tenors
expected_ifc_tenor_units_test_add_verify = value_expected_ifc_tenor_units
expected_ifc_statuss_test_add_verify = value_expected_ifc_statuses
expected_gls_sys_account_names_test_add_verify = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_add_verify = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_add_verify = value_expected_extension_sys_account_names
expected_extension_conditions_test_add_verify = value_expected_extension_conditions_add
expected_extension_replace_bys_test_add_verify = value_expected_extension_replace_bys

# data test view add
catalogue_code_test_view_add = value_catalogue_code
catalogue_name_test_view_add = catalogue_name_test_add
trade_group_test_view_add = value_trade_group
details_category_test_view_add = value_details_category
trade_type_test_view_add = value_trade_type
margin_trading_test_view_add = value_margin_trading
market_test_view_add = value_market
catalogue_status_test_view_add = value_catalogue_status
settle_tenor_test_view_add = value_settle_tenor
settle_tenor_unit_test_view_add = value_settle_tenor_unit
tenor_test_view_add = value_tenor
tenor_unit_test_view_add = value_tenor_unit
interest_tenor_test_view_add = value_interest_tenor
interest_tenor_unit_test_view_add = value_interest_tenor_unit
rollover_option_test_view_add = value_rollover_option
revaluation_test_view_add = value_revaluation
user_create_test_view_add = value_user_create
approve_by_test_view_add = value_approve_by
expected_ifc_list_codes_test_view_add = value_expected_ifc_list_codes
expected_ifc_names_test_view_add = value_expected_ifc_names
expected_ifc_values_test_view_add = value_expected_ifc_values
expected_ifc_types_test_view_add = value_expected_ifc_types
expected_ifc_tenors_test_view_add = value_expected_ifc_tenors
expected_ifc_tenor_units_test_view_add = value_expected_ifc_tenor_units
expected_ifc_statuss_test_view_add = value_expected_ifc_statuses
expected_gls_sys_account_names_test_view_add = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_view_add = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_view_add = value_expected_extension_sys_account_names
expected_extension_conditions_test_view_add = value_expected_extension_conditions_view
expected_extension_replace_bys_test_view_add = value_expected_extension_replace_bys

# data test update
catalogue_code_test_update = value_catalogue_code
catalogue_name_test_update = f'AUTO TEST update {date_time}'
trade_group_test_update = 'Forex'
details_category_test_update = 'Spot'
trade_type_test_update = 'Sell-Buy'
margin_trading_test_update = 'Yes'
market_test_update = 'Listed Market'
catalogue_status_test_update = 'Close'
settle_tenor_test_update = '2.00'
settle_tenor_unit_test_update = 'Month'
tenor_test_update = '9.00'
tenor_unit_test_update = 'Year'
interest_tenor_test_update = '3.00'
interest_tenor_unit_test_update = 'Week'
rollover_option_test_update = 'No rollover'
revaluation_test_update = 'No'
user_create_test_update = value_user_create
approve_by_test_update = value_approve_by
ifc_codes_test_update = None
sys_account_names_test_update = None
account_aliass_test_update = None
coa_accounts_test_update = None
replace_bys_test_update = None
system_account_names_test_update = None
customer_sectors_test_update = None
customer_resident_statuss_test_update = None
business_lines_test_update = None
sub_products_test_update = None
bank_identifications_test_update = None
replace_code_test_update = None
list_error_message_test_update = None

# data test update verify
catalogue_code_test_update_verify = value_catalogue_code
catalogue_name_test_update_verify = catalogue_name_test_update
trade_group_test_update_verify = trade_group_test_update
details_category_test_update_verify = details_category_test_update
trade_type_test_update_verify = trade_type_test_update
margin_trading_test_update_verify = margin_trading_test_update
market_test_update_verify = market_test_update
catalogue_status_test_update_verify = catalogue_status_test_update
settle_tenor_test_update_verify = settle_tenor_test_update
settle_tenor_unit_test_update_verify = settle_tenor_unit_test_update
tenor_test_update_verify = tenor_test_update
tenor_unit_test_update_verify = tenor_unit_test_update
interest_tenor_test_update_verify = interest_tenor_test_update
interest_tenor_unit_test_update_verify = interest_tenor_unit_test_update
rollover_option_test_update_verify = rollover_option_test_update
revaluation_test_update_verify = revaluation_test_update
user_create_test_update_verify = value_user_create
approve_by_test_update_verify = value_approve_by
expected_ifc_list_codes_test_update_verify = value_expected_ifc_list_codes
expected_ifc_names_test_update_verify = value_expected_ifc_names
expected_ifc_values_test_update_verify = value_expected_ifc_values
expected_ifc_types_test_update_verify = value_expected_ifc_types
expected_ifc_tenors_test_update_verify = value_expected_ifc_tenors
expected_ifc_tenor_units_test_update_verify = value_expected_ifc_tenor_units
expected_ifc_statuss_test_update_verify = value_expected_ifc_statuses
expected_gls_sys_account_names_test_update_verify = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_update_verify = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_update_verify = value_expected_extension_sys_account_names
expected_extension_conditions_test_update_verify = value_expected_extension_conditions_view
expected_extension_replace_bys_test_update_verify = value_expected_extension_replace_bys

# data test view update
catalogue_code_test_view_update = value_catalogue_code
catalogue_name_test_view_update = catalogue_name_test_update
trade_group_test_view_update = trade_group_test_update
details_category_test_view_update = details_category_test_update
trade_type_test_view_update = trade_type_test_update
margin_trading_test_view_update = margin_trading_test_update
market_test_view_update = market_test_update
catalogue_status_test_view_update = catalogue_status_test_update
settle_tenor_test_view_update = settle_tenor_test_update
settle_tenor_unit_test_view_update = settle_tenor_unit_test_update
tenor_test_view_update = tenor_test_update
tenor_unit_test_view_update = tenor_unit_test_update
interest_tenor_test_view_update = interest_tenor_test_update
interest_tenor_unit_test_view_update = interest_tenor_unit_test_update
rollover_option_test_view_update = rollover_option_test_update
revaluation_test_view_update = revaluation_test_update
user_create_test_view_update = value_user_create
approve_by_test_view_update = value_approve_by
expected_ifc_list_codes_test_view_update = value_expected_ifc_list_codes
expected_ifc_names_test_view_update = value_expected_ifc_names
expected_ifc_values_test_view_update = value_expected_ifc_values
expected_ifc_types_test_view_update = value_expected_ifc_types
expected_ifc_tenors_test_view_update = value_expected_ifc_tenors
expected_ifc_tenor_units_test_view_update = value_expected_ifc_tenor_units
expected_ifc_statuss_test_view_update = value_expected_ifc_statuses
expected_gls_sys_account_names_test_view_update = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_view_update = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_view_update = value_expected_extension_sys_account_names
expected_extension_conditions_test_view_update = value_expected_extension_conditions_view
expected_extension_replace_bys_test_view_update = value_expected_extension_replace_bys

class TreasuryCatalogueTest(FormAction):
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
        global working_date, branch_code, username_logged
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()
        username_logged = self.get_username()
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

# TRS-Catalogue Definition
    def test_001_trs_cat_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.treasury_catalogue_definition_add(
            catalogue_code=catalogue_code_test_add,
            catalogue_name=catalogue_name_test_add,
            trade_group=trade_group_test_add,
            details_category=details_category_test_add,
            trade_type=trade_type_test_add,
            margin_trading=margin_trading_test_add,
            market=market_test_add,
            catalogue_status=catalogue_status_test_add,
            settle_tenor=settle_tenor_test_add,
            settle_tenor_unit=settle_tenor_unit_test_add,
            tenor=tenor_test_add,
            tenor_unit=tenor_unit_test_add,
            interest_tenor=interest_tenor_test_add,
            interest_tenor_unit=interest_tenor_unit_test_add,
            rollover_option=rollover_option_test_add,
            revaluation=revaluation_test_add,
            user_create=user_create_test_add,
            approve_by=approve_by_test_add,
            ifc_codes=ifc_codes_test_add,
            sys_account_names=sys_account_names_test_add,
            account_aliass=account_aliass_test_add,
            coa_accounts=coa_accounts_test_add,
            replace_bys=replace_bys_test_add,
            system_account_names=system_account_names_test_add,
            customer_sectors=customer_sectors_test_add,
            customer_resident_statuss=customer_resident_statuss_test_add,
            business_lines=business_lines_test_add,
            sub_products=sub_products_test_add,
            bank_identifications=bank_identifications_test_add,
            replace_code=replace_code_test_add,
            list_error_message=list_error_message_test_add,

        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.treasury_catalogue_definition_simple_search(catalogue_code_test_add)
        self.assert_search_not_found()

    def test_002_trs_cat_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.treasury_catalogue_definition_add_verify(
            transaction_number=transaction_number_add,
            catalogue_code=catalogue_code_test_add_verify,
            catalogue_name=catalogue_name_test_add_verify,
            trade_group=trade_group_test_add_verify,
            details_category=details_category_test_add_verify,
            trade_type=trade_type_test_add_verify,
            margin_trading=margin_trading_test_add_verify,
            market=market_test_add_verify,
            catalogue_status=catalogue_status_test_add_verify,
            settle_tenor=settle_tenor_test_add_verify,
            settle_tenor_unit=settle_tenor_unit_test_add_verify,
            tenor=tenor_test_add_verify,
            tenor_unit=tenor_unit_test_add_verify,
            interest_tenor=interest_tenor_test_add_verify,
            interest_tenor_unit=interest_tenor_unit_test_add_verify,
            rollover_option=rollover_option_test_add_verify,
            revaluation=revaluation_test_add_verify,
            user_create=user_create_test_add_verify,
            approve_by=approve_by_test_add_verify,
            expected_ifc_list_codes=expected_ifc_list_codes_test_add_verify,
            expected_ifc_names=expected_ifc_names_test_add_verify,
            expected_ifc_values=expected_ifc_values_test_add_verify,
            expected_ifc_types=expected_ifc_types_test_add_verify,
            expected_ifc_tenors=expected_ifc_tenors_test_add_verify,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_add_verify,
            expected_ifc_statuss=expected_ifc_statuss_test_add_verify,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_add_verify,
            expected_gls_account_aliass=expected_gls_account_aliass_test_add_verify,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_add_verify,
            expected_extension_conditions=expected_extension_conditions_test_add_verify,
            expected_extension_replace_bys=expected_extension_replace_bys_test_add_verify,
        )

    def test_003_trs_cat_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.treasury_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_add,
        )

    def test_004_trs_cat_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.treasury_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_add,
            catalogue_name=catalogue_name_test_view_add,
            trade_group=trade_group_test_view_add,
            details_category=details_category_test_view_add,
            trade_type=trade_type_test_view_add,
            margin_trading=margin_trading_test_view_add,
            market=market_test_view_add,
            catalogue_status=catalogue_status_test_view_add,
            settle_tenor=settle_tenor_test_view_add,
            settle_tenor_unit=settle_tenor_unit_test_view_add,
            tenor=tenor_test_view_add,
            tenor_unit=tenor_unit_test_view_add,
            interest_tenor=interest_tenor_test_view_add,
            interest_tenor_unit=interest_tenor_unit_test_view_add,
            rollover_option=rollover_option_test_view_add,
            revaluation=revaluation_test_view_add,
            user_create=user_create_test_view_add,
            approve_by=approve_by_test_view_add,
            expected_ifc_list_codes=expected_ifc_list_codes_test_view_add,
            expected_ifc_names=expected_ifc_names_test_view_add,
            expected_ifc_values=expected_ifc_values_test_view_add,
            expected_ifc_types=expected_ifc_types_test_view_add,
            expected_ifc_tenors=expected_ifc_tenors_test_view_add,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_view_add,
            expected_ifc_statuss=expected_ifc_statuss_test_view_add,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_view_add,
            expected_gls_account_aliass=expected_gls_account_aliass_test_view_add,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_view_add,
            expected_extension_conditions=expected_extension_conditions_test_view_add,
            expected_extension_replace_bys=expected_extension_replace_bys_test_view_add,
        )
        self.assert_activity(
            transaction_number=transaction_number_add,
            maker=username_logged,
            action=action_add
        )

    def test_005_login_with_other_user(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print(f'Username: {username_logged}')
        self.logout()
        self.login(username_other_branch, password_other_branch, one_app=ONE_APP)
        global other_username_logged
        other_username_logged = self.get_username()
        print(f'Other username: {other_username_logged}')

    def test_006_trs_cat_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.treasury_catalogue_definition_update(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
            trade_group=trade_group_test_update,
            details_category=details_category_test_update,
            trade_type=trade_type_test_update,
            margin_trading=margin_trading_test_update,
            market=market_test_update,
            catalogue_status=catalogue_status_test_update,
            settle_tenor=settle_tenor_test_update,
            settle_tenor_unit=settle_tenor_unit_test_update,
            tenor=tenor_test_update,
            tenor_unit=tenor_unit_test_update,
            interest_tenor=interest_tenor_test_update,
            interest_tenor_unit=interest_tenor_unit_test_update,
            rollover_option=rollover_option_test_update,
            revaluation=revaluation_test_update,
            user_create=user_create_test_update,
            approve_by=approve_by_test_update,
            ifc_codes=ifc_codes_test_update,
            sys_account_names=sys_account_names_test_update,
            account_aliass=account_aliass_test_update,
            coa_accounts=coa_accounts_test_update,
            replace_bys=replace_bys_test_update,
            system_account_names=system_account_names_test_update,
            customer_sectors=customer_sectors_test_update,
            customer_resident_statuss=customer_resident_statuss_test_update,
            business_lines=business_lines_test_update,
            sub_products=sub_products_test_update,
            bank_identifications=bank_identifications_test_update,
            replace_code=replace_code_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.treasury_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_view_add,
        )

    def test_007_trs_cat_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.treasury_catalogue_definition_update_verify(
            transaction_number=transaction_number_update,
            catalogue_code=catalogue_code_test_update_verify,
            catalogue_name=catalogue_name_test_update_verify,
            trade_group=trade_group_test_update_verify,
            details_category=details_category_test_update_verify,
            trade_type=trade_type_test_update_verify,
            margin_trading=margin_trading_test_update_verify,
            market=market_test_update_verify,
            catalogue_status=catalogue_status_test_update_verify,
            settle_tenor=settle_tenor_test_update_verify,
            settle_tenor_unit=settle_tenor_unit_test_update_verify,
            tenor=tenor_test_update_verify,
            tenor_unit=tenor_unit_test_update_verify,
            interest_tenor=interest_tenor_test_update_verify,
            interest_tenor_unit=interest_tenor_unit_test_update_verify,
            rollover_option=rollover_option_test_update_verify,
            revaluation=revaluation_test_update_verify,
            user_create=user_create_test_update_verify,
            approve_by=approve_by_test_update_verify,
            expected_ifc_list_codes=expected_ifc_list_codes_test_update_verify,
            expected_ifc_names=expected_ifc_names_test_update_verify,
            expected_ifc_values=expected_ifc_values_test_update_verify,
            expected_ifc_types=expected_ifc_types_test_update_verify,
            expected_ifc_tenors=expected_ifc_tenors_test_update_verify,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_update_verify,
            expected_ifc_statuss=expected_ifc_statuss_test_update_verify,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_update_verify,
            expected_gls_account_aliass=expected_gls_account_aliass_test_update_verify,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_update_verify,
            expected_extension_conditions=expected_extension_conditions_test_update_verify,
            expected_extension_replace_bys=expected_extension_replace_bys_test_update_verify,
        )

    def test_008_trs_cat_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.treasury_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
        )

    def test_009_trs_cat_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.treasury_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_update,
            catalogue_name=catalogue_name_test_view_update,
            trade_group=trade_group_test_view_update,
            details_category=details_category_test_view_update,
            trade_type=trade_type_test_view_update,
            margin_trading=margin_trading_test_view_update,
            market=market_test_view_update,
            catalogue_status=catalogue_status_test_view_update,
            settle_tenor=settle_tenor_test_view_update,
            settle_tenor_unit=settle_tenor_unit_test_view_update,
            tenor=tenor_test_view_update,
            tenor_unit=tenor_unit_test_view_update,
            interest_tenor=interest_tenor_test_view_update,
            interest_tenor_unit=interest_tenor_unit_test_view_update,
            rollover_option=rollover_option_test_view_update,
            revaluation=revaluation_test_view_update,
            user_create=user_create_test_view_update,
            approve_by=approve_by_test_view_update,
            expected_ifc_list_codes=expected_ifc_list_codes_test_view_update,
            expected_ifc_names=expected_ifc_names_test_view_update,
            expected_ifc_values=expected_ifc_values_test_view_update,
            expected_ifc_types=expected_ifc_types_test_view_update,
            expected_ifc_tenors=expected_ifc_tenors_test_view_update,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_view_update,
            expected_ifc_statuss=expected_ifc_statuss_test_view_update,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_view_update,
            expected_gls_account_aliass=expected_gls_account_aliass_test_view_update,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_view_update,
            expected_extension_conditions=expected_extension_conditions_test_view_update,
            expected_extension_replace_bys=expected_extension_replace_bys_test_view_update,
        )
        self.assert_activity(
            transaction_number=transaction_number_add,
            maker=username_logged,
            action=action_add
        )
        self.assert_activity(
            transaction_number=transaction_number_update,
            maker=other_username_logged,
            action=action_update
        )

    def test_010_trs_cat_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.treasury_catalogue_definition_delete(
            catalogue_code=value_catalogue_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.treasury_catalogue_definition_search_verify(
            catalogue_code=value_catalogue_code,
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_catalogue_code,
            tran_name=tran_name_delete,
        )

    def test_011_trs_cat_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.treasury_catalogue_definition_simple_search(value_catalogue_code)
        self.assert_search_not_found()

    def test_012_trs_cat_delete_item_in_use_01_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.treasury_catalogue_definition_delete(
            catalogue_code=catalogue_code_in_use,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.treasury_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_in_use,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=catalogue_code_in_use,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=catalogue_code_in_use,
            tran_name=tran_name_delete,
            list_error_message=list_error_message_in_use,
        )

    def test_012_trs_cat_delete_item_in_use_02_reject(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # reject delete
        self.bo_approval_reject(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=catalogue_code_in_use,
            tran_name=tran_name_delete,
        )
        # search master
        self.treasury_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_in_use,
        )

if __name__ == '__main__': 
    webui_test.main()