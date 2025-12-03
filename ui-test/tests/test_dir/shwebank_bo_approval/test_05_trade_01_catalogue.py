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

action_add ='TRD-Catalogue Definition-Add'
action_update ='TRD-Catalogue Definition-Update'
catalogue_code_in_use = 'BGNUL'
list_error_message_in_use = [f'ERROR: CatalogCode [{catalogue_code_in_use}] is used by other trade account']
tran_name_delete = 'TRD_DELETE_CATALOG'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_catalogue_code = 'AUTO1'
value_business_group = '3-Inward Bank Guarantee'
value_details_category = '1-BID security'
value_term_and_condition = 'Normal'
value_tenor = 'At sight'
value_customer_type = 'Applicant'
value_catalogue_status = 'Normal'
value_user_create = USERNAME_LOGIN
value_approve_by = USERNAME_APPROVE
value_obs_percentage_rate = '0.00'
value_expected_ifc_list_codes = None
value_expected_ifc_names = None
value_expected_ifc_values = None
value_expected_ifc_types = None
value_expected_ifc_tenors = None
value_expected_ifc_tenor_units = None
value_expected_ifc_statuss = None

value_expected_gls_account_aliass = ['###6010101000202**', '###5010101000101**', '###2070501000909**']
value_expected_gls_sys_account_names = ['LIABILITY', 'TRADE', 'SUSPEND']
value_expected_extension_sys_account_names = None
value_expected_extension_replace_bys = None
value_business_lines = None
value_expected_extension_conditions_add = None
value_expected_extension_conditions_view = None

# data test add
catalogue_code_test_add = value_catalogue_code
catalogue_name_test_add = f'AUTO TEST add {date_time}'
business_group_test_add = value_business_group
details_category_test_add = value_details_category
term_and_condition_test_add = value_term_and_condition
tenor_test_add = value_tenor
customer_type_test_add = value_customer_type
catalogue_status_test_add = value_catalogue_status
user_create_test_add = value_user_create
approve_by_test_add = None
obs_percentage_rate_test_add = value_obs_percentage_rate
ifc_codes_test_add = None
sys_account_names_test_add = value_expected_gls_sys_account_names
account_aliass_test_add = value_expected_gls_account_aliass
coa_accounts_test_add = None
replace_bys_test_add = value_expected_extension_replace_bys
system_account_names_test_add = value_expected_extension_sys_account_names
customer_sectors_test_add = None
customer_resident_statuss_test_add = None
business_lines_test_add = value_business_lines
sub_products_test_add = None
bank_identifications_test_add = None
replace_code_test_add = None
list_error_message_test_add = None

# data test add verify
catalogue_code_test_add_verify = value_catalogue_code
catalogue_name_test_add_verify = catalogue_name_test_add
business_group_test_add_verify = value_business_group
details_category_test_add_verify = value_details_category
term_and_condition_test_add_verify = value_term_and_condition
tenor_test_add_verify = value_tenor
customer_type_test_add_verify = value_customer_type
catalogue_status_test_add_verify = value_catalogue_status
user_create_test_add_verify = value_user_create
approve_by_test_add_verify = None
obs_percentage_rate_test_add_verify = value_obs_percentage_rate
expected_ifc_list_codes_test_add_verify = value_expected_ifc_list_codes
expected_ifc_names_test_add_verify = value_expected_ifc_names
expected_ifc_values_test_add_verify = value_expected_ifc_values
expected_ifc_types_test_add_verify = value_expected_ifc_types
expected_ifc_tenors_test_add_verify = value_expected_ifc_tenors
expected_ifc_tenor_units_test_add_verify = value_expected_ifc_tenor_units
expected_ifc_statuss_test_add_verify = value_expected_ifc_statuss
expected_gls_sys_account_names_test_add_verify = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_add_verify = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_add_verify = value_expected_extension_sys_account_names
expected_extension_conditions_test_add_verify = value_expected_extension_conditions_add
expected_extension_replace_bys_test_add_verify = value_expected_extension_replace_bys

# data test view add
catalogue_code_test_view_add = value_catalogue_code
catalogue_name_test_view_add = catalogue_name_test_add
business_group_test_view_add = value_business_group
details_category_test_view_add = value_details_category
term_and_condition_test_view_add = value_term_and_condition
tenor_test_view_add = value_tenor
customer_type_test_view_add = value_customer_type
catalogue_status_test_view_add = value_catalogue_status
user_create_test_view_add = value_user_create
approve_by_test_view_add = value_approve_by
obs_percentage_rate_test_view_add = value_obs_percentage_rate
expected_ifc_list_codes_test_view_add = value_expected_ifc_list_codes
expected_ifc_names_test_view_add = value_expected_ifc_names
expected_ifc_values_test_view_add = value_expected_ifc_values
expected_ifc_types_test_view_add = value_expected_ifc_types
expected_ifc_tenors_test_view_add = value_expected_ifc_tenors
expected_ifc_tenor_units_test_view_add = value_expected_ifc_tenor_units
expected_ifc_statuss_test_view_add = value_expected_ifc_statuss
expected_gls_sys_account_names_test_view_add = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_view_add = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_view_add = value_expected_extension_sys_account_names
expected_extension_conditions_test_view_add = value_expected_extension_conditions_view
expected_extension_replace_bys_test_view_add = value_expected_extension_replace_bys

# data test update
catalogue_code_test_update = value_catalogue_code
catalogue_name_test_update = f'AUTO TEST update {date_time}'
business_group_test_update = value_business_group
details_category_test_update = value_details_category
term_and_condition_test_update = value_term_and_condition
tenor_test_update = value_tenor
customer_type_test_update = value_customer_type
catalogue_status_test_update = value_catalogue_status
user_create_test_update = value_user_create
approve_by_test_update = value_approve_by
obs_percentage_rate_test_update = value_obs_percentage_rate
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
business_group_test_update_verify = value_business_group
details_category_test_update_verify = value_details_category
term_and_condition_test_update_verify = value_term_and_condition
tenor_test_update_verify = value_tenor
customer_type_test_update_verify = value_customer_type
catalogue_status_test_update_verify = value_catalogue_status
user_create_test_update_verify = value_user_create
approve_by_test_update_verify = value_approve_by
obs_percentage_rate_test_update_verify = value_obs_percentage_rate
expected_ifc_list_codes_test_update_verify = value_expected_ifc_list_codes
expected_ifc_names_test_update_verify = value_expected_ifc_names
expected_ifc_values_test_update_verify = value_expected_ifc_values
expected_ifc_types_test_update_verify = value_expected_ifc_types
expected_ifc_tenors_test_update_verify = value_expected_ifc_tenors
expected_ifc_tenor_units_test_update_verify = value_expected_ifc_tenor_units
expected_ifc_statuss_test_update_verify = value_expected_ifc_statuss
expected_gls_sys_account_names_test_update_verify = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_update_verify = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_update_verify = value_expected_extension_sys_account_names
expected_extension_conditions_test_update_verify = value_expected_extension_conditions_view
expected_extension_replace_bys_test_update_verify = value_expected_extension_replace_bys

# data test view update
catalogue_code_test_view_update = value_catalogue_code
catalogue_name_test_view_update = catalogue_name_test_update
business_group_test_view_update = value_business_group
details_category_test_view_update = value_details_category
term_and_condition_test_view_update = value_term_and_condition
tenor_test_view_update = value_tenor
customer_type_test_view_update = value_customer_type
catalogue_status_test_view_update = value_catalogue_status
user_create_test_view_update = value_user_create
approve_by_test_view_update = value_approve_by
obs_percentage_rate_test_view_update = value_obs_percentage_rate
expected_ifc_list_codes_test_view_update = value_expected_ifc_list_codes
expected_ifc_names_test_view_update = value_expected_ifc_names
expected_ifc_values_test_view_update = value_expected_ifc_values
expected_ifc_types_test_view_update = value_expected_ifc_types
expected_ifc_tenors_test_view_update = value_expected_ifc_tenors
expected_ifc_tenor_units_test_view_update = value_expected_ifc_tenor_units
expected_ifc_statuss_test_view_update = value_expected_ifc_statuss
expected_gls_sys_account_names_test_view_update = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_view_update = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_view_update = value_expected_extension_sys_account_names
expected_extension_conditions_test_view_update = value_expected_extension_conditions_view
expected_extension_replace_bys_test_view_update = value_expected_extension_replace_bys

class TradeCatalogueTest(FormAction):
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

# TRD-Catalogue Definition
    def test_001_trd_cat_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.trade_catalogue_definition_add(
            catalogue_code=catalogue_code_test_add,
            catalogue_name=catalogue_name_test_add,
            business_group=business_group_test_add,
            details_category=details_category_test_add,
            term_and_condition=term_and_condition_test_add,
            tenor=tenor_test_add,
            customer_type=customer_type_test_add,
            catalogue_status=catalogue_status_test_add,
            user_create=user_create_test_add,
            approve_by=approve_by_test_add,
            obs_percentage_rate=obs_percentage_rate_test_add,
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
        self.trade_catalogue_definition_simple_search(catalogue_code_test_add)
        self.assert_search_not_found()

    def test_002_trd_cat_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.trade_catalogue_definition_add_verify(
            transaction_number=transaction_number_add,
            catalogue_code=catalogue_code_test_add_verify,
            catalogue_name=catalogue_name_test_add_verify,
            business_group=business_group_test_add_verify,
            details_category=details_category_test_add_verify,
            term_and_condition=term_and_condition_test_add_verify,
            tenor=tenor_test_add_verify,
            customer_type=customer_type_test_add_verify,
            catalogue_status=catalogue_status_test_add_verify,
            user_create=user_create_test_add_verify,
            approve_by=approve_by_test_add_verify,
            obs_percentage_rate=obs_percentage_rate_test_add_verify,
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

    def test_003_trd_cat_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.trade_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_add,
        )

    def test_004_trd_cat_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.trade_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_add,
            catalogue_name=catalogue_name_test_view_add,
            business_group=business_group_test_view_add,
            details_category=details_category_test_view_add,
            term_and_condition=term_and_condition_test_view_add,
            tenor=tenor_test_view_add,
            customer_type=customer_type_test_view_add,
            catalogue_status=catalogue_status_test_view_add,
            user_create=user_create_test_view_add,
            approve_by=approve_by_test_view_add,
            obs_percentage_rate=obs_percentage_rate_test_view_add,
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

    def test_006_trd_cat_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.trade_catalogue_definition_update(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
            business_group=business_group_test_update,
            details_category=details_category_test_update,
            term_and_condition=term_and_condition_test_update,
            tenor=tenor_test_update,
            customer_type=customer_type_test_update,
            catalogue_status=catalogue_status_test_update,
            user_create=user_create_test_update,
            approve_by=approve_by_test_update,
            obs_percentage_rate=obs_percentage_rate_test_update,
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
        self.trade_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_view_add,
        )

    def test_007_trd_cat_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.trade_catalogue_definition_update_verify(
            transaction_number=transaction_number_update,
            catalogue_code=catalogue_code_test_update_verify,
            catalogue_name=catalogue_name_test_update_verify,
            business_group=business_group_test_update_verify,
            details_category=details_category_test_update_verify,
            term_and_condition=term_and_condition_test_update_verify,
            tenor=tenor_test_update_verify,
            customer_type=customer_type_test_update_verify,
            catalogue_status=catalogue_status_test_update_verify,
            user_create=user_create_test_update_verify,
            approve_by=approve_by_test_update_verify,
            obs_percentage_rate=obs_percentage_rate_test_update_verify,
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

    def test_008_trd_cat_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.trade_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
        )

    def test_009_trd_cat_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.trade_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_update,
            catalogue_name=catalogue_name_test_view_update,
            business_group=business_group_test_view_update,
            details_category=details_category_test_view_update,
            term_and_condition=term_and_condition_test_view_update,
            tenor=tenor_test_view_update,
            customer_type=customer_type_test_view_update,
            catalogue_status=catalogue_status_test_view_update,
            user_create=user_create_test_view_update,
            approve_by=approve_by_test_view_update,
            obs_percentage_rate=obs_percentage_rate_test_view_update,
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

    def test_010_trd_cat_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.trade_catalogue_definition_delete(
            catalogue_code=value_catalogue_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.trade_catalogue_definition_search_verify(
            catalogue_code=value_catalogue_code,
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_catalogue_code,
            tran_name=tran_name_delete,
        )

    def test_011_trd_cat_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.trade_catalogue_definition_simple_search(value_catalogue_code)
        self.assert_search_not_found()

    def test_012_trd_cat_delete_item_in_use_01_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.trade_catalogue_definition_delete(
            catalogue_code= catalogue_code_in_use,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.trade_catalogue_definition_search_verify(
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

    def test_012_trd_cat_delete_item_in_use_02_reject(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # reject delete
        self.bo_approval_reject(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=catalogue_code_in_use,
            tran_name=tran_name_delete,
        )
        # search master
        self.trade_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_in_use,
        )

if __name__ == '__main__': 
    webui_test.main()