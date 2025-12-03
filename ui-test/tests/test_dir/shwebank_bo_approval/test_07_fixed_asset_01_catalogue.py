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

action_add ='FAC-Fixed Asset Catalogue Definition-Add'
action_update ='FAC-Fixed Asset Catalogue Definition-Update'
catalogue_code_in_use = '00000102'
# list_error_message_in_use = [f'Category code is already in used [{catalogue_code_in_use}]']
list_error_message_in_use = [f'ERROR: Category code is already in used [{catalogue_code_in_use}]']
tran_name_delete = 'SQL_DELETE_FACCAT'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_catalogue_code = 'AUTO0001'
value_fixed_asset_type = 'Life'
value_fixed_asset_classification = 'Building and renovation'
value_depreciation_method = 'Streight line method'
value_catalogue_status = 'Normal'
value_fixed_asset_life_time = '80'
value_life_time_unit = 'Year(s)'
value_created_by = USERNAME_LOGIN
value_approve_by = USERNAME_APPROVE

value_expected_gls_account_aliass = ['###1070201000101**', '###2050201000101**', '###4050201000101**', '###4051101000101**', '###3050101000101**']
value_expected_gls_sys_account_names = ['FASSET', 'ACCUMULATE', 'DEPRECIATION', 'EXPENSE', 'INCOME']
value_list_error_message = None

# data test add
catalogue_code_test_add = value_catalogue_code
catalogue_name_test_add = f'AUTO TEST add {date_time}'
fixed_asset_type_test_add = value_fixed_asset_type
fixed_asset_classification_test_add = value_fixed_asset_classification
depreciation_method_test_add = value_depreciation_method
catalogue_status_test_add = value_catalogue_status
fixed_asset_life_time_test_add = value_fixed_asset_life_time
life_time_unit_test_add = value_life_time_unit
sys_account_names_test_add = value_expected_gls_sys_account_names
coa_accounts_test_add = None
account_aliass_test_add = value_expected_gls_account_aliass
list_error_message_test_add = value_list_error_message

# data test add verify
catalogue_code_test_add_verify = value_catalogue_code
catalogue_name_test_add_verify = catalogue_name_test_add
fixed_asset_type_test_add_verify = value_fixed_asset_type
fixed_asset_classification_test_add_verify = value_fixed_asset_classification
depreciation_method_test_add_verify = value_depreciation_method
catalogue_status_test_add_verify = value_catalogue_status
fixed_asset_life_time_test_add_verify = value_fixed_asset_life_time
life_time_unit_test_add_verify = value_life_time_unit
expected_gls_sys_account_names_test_add_verify = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_add_verify = value_expected_gls_account_aliass

# data test view add
catalogue_code_test_view_add = value_catalogue_code
catalogue_name_test_view_add = catalogue_name_test_add
fixed_asset_type_test_view_add = value_fixed_asset_type
fixed_asset_classification_test_view_add = value_fixed_asset_classification
depreciation_method_test_view_add = value_depreciation_method
catalogue_status_test_view_add = value_catalogue_status
fixed_asset_life_time_test_view_add = value_fixed_asset_life_time
life_time_unit_test_view_add = value_life_time_unit
created_by_test_view_add = value_created_by
approve_by_test_view_add = value_approve_by
expected_gls_sys_account_names_test_view_add = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_view_add = value_expected_gls_account_aliass

# data test update
catalogue_code_test_update = value_catalogue_code
catalogue_name_test_update = f'AUTO TEST update {date_time}'
fixed_asset_type_test_update = 'Percent'
fixed_asset_classification_test_update = 'Freehold buildings'
depreciation_method_test_update = value_depreciation_method
catalogue_status_test_update = 'Close'
fixed_asset_life_time_test_update = None
life_time_unit_test_update = None
created_by_test_update = value_created_by
approve_by_test_update = value_approve_by
sys_account_names_test_update = None
coa_accounts_test_update = None
account_aliass_test_update = None
list_error_message_test_update = value_list_error_message

# data test update verify
catalogue_code_test_update_verify = value_catalogue_code
catalogue_name_test_update_verify = catalogue_name_test_update
fixed_asset_type_test_update_verify = fixed_asset_type_test_update
fixed_asset_classification_test_update_verify = fixed_asset_classification_test_update
depreciation_method_test_update_verify = value_depreciation_method
catalogue_status_test_update_verify = catalogue_status_test_update
fixed_asset_life_time_test_update_verify = value_fixed_asset_life_time
life_time_unit_test_update_verify = value_life_time_unit
created_by_test_update_verify = value_created_by
approve_by_test_update_verify = value_approve_by
expected_gls_sys_account_names_test_update_verify = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_update_verify = value_expected_gls_account_aliass

# data test view update
catalogue_code_test_view_update = value_catalogue_code
catalogue_name_test_view_update = catalogue_name_test_update
fixed_asset_type_test_view_update = fixed_asset_type_test_update
fixed_asset_classification_test_view_update = fixed_asset_classification_test_update
depreciation_method_test_view_update = value_depreciation_method
catalogue_status_test_view_update = catalogue_status_test_update
fixed_asset_life_time_test_view_update = value_fixed_asset_life_time
life_time_unit_test_view_update = value_life_time_unit
created_by_test_view_update = value_created_by
approve_by_test_view_update = value_approve_by
expected_gls_sys_account_names_test_view_update = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_view_update = value_expected_gls_account_aliass

class FixedAssetCatalogueTest(FormAction):
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

# FAC-Fixed Asset Catalogue Definition
    def test_001_fac_cat_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.fixed_asset_catalogue_definition_add(
            catalogue_code=catalogue_code_test_add,
            catalogue_name=catalogue_name_test_add,
            fixed_asset_type=fixed_asset_type_test_add,
            fixed_asset_classification=fixed_asset_classification_test_add,
            depreciation_method=depreciation_method_test_add,
            catalogue_status=catalogue_status_test_add,
            fixed_asset_life_time=fixed_asset_life_time_test_add,
            life_time_unit=life_time_unit_test_add,
            sys_account_names=sys_account_names_test_add,
            coa_accounts=coa_accounts_test_add,
            account_aliass=account_aliass_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.fixed_asset_catalogue_definition_simple_search(catalogue_code_test_add)
        self.assert_search_not_found()

    def test_002_fac_cat_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.fixed_asset_catalogue_definition_add_verify(
            transaction_number=transaction_number_add,
            catalogue_code=catalogue_code_test_add_verify,
            catalogue_name=catalogue_name_test_add_verify,
            fixed_asset_type=fixed_asset_type_test_add_verify,
            fixed_asset_classification=fixed_asset_classification_test_add_verify,
            depreciation_method=depreciation_method_test_add_verify,
            catalogue_status=catalogue_status_test_add_verify,
            fixed_asset_life_time=fixed_asset_life_time_test_add_verify,
            life_time_unit=life_time_unit_test_add_verify,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_add_verify,
            expected_gls_account_aliass=expected_gls_account_aliass_test_add_verify,
        )

    def test_003_fac_cat_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.fixed_asset_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_add,
        )

    def test_004_fac_cat_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.fixed_asset_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_add,
            catalogue_name=catalogue_name_test_view_add,
            fixed_asset_type=fixed_asset_type_test_view_add,
            fixed_asset_classification=fixed_asset_classification_test_view_add,
            depreciation_method=depreciation_method_test_view_add,
            catalogue_status=catalogue_status_test_view_add,
            fixed_asset_life_time=fixed_asset_life_time_test_view_add,
            life_time_unit=life_time_unit_test_view_add,
            created_by=created_by_test_view_add,
            approve_by=approve_by_test_view_add,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_view_add,
            expected_gls_account_aliass=expected_gls_account_aliass_test_view_add,
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

    def test_006_fac_cat_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.fixed_asset_catalogue_definition_update(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
            fixed_asset_type=fixed_asset_type_test_update,
            fixed_asset_classification=fixed_asset_classification_test_update,
            depreciation_method=depreciation_method_test_update,
            catalogue_status=catalogue_status_test_update,
            fixed_asset_life_time=fixed_asset_life_time_test_update,
            life_time_unit=life_time_unit_test_update,
            created_by=created_by_test_update,
            approve_by=approve_by_test_update,
            sys_account_names=sys_account_names_test_update,
            coa_accounts=coa_accounts_test_update,
            account_aliass=account_aliass_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.fixed_asset_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_view_add,
        )

    def test_007_fac_cat_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.fixed_asset_catalogue_definition_update_verify(
            transaction_number=transaction_number_update,
            catalogue_code=catalogue_code_test_update_verify,
            catalogue_name=catalogue_name_test_update_verify,
            fixed_asset_type=fixed_asset_type_test_update_verify,
            fixed_asset_classification=fixed_asset_classification_test_update_verify,
            depreciation_method=depreciation_method_test_update_verify,
            catalogue_status=catalogue_status_test_update_verify,
            fixed_asset_life_time=fixed_asset_life_time_test_update_verify,
            life_time_unit=life_time_unit_test_update_verify,
            created_by=created_by_test_update_verify,
            approve_by=approve_by_test_update_verify,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_update_verify,
            expected_gls_account_aliass=expected_gls_account_aliass_test_update_verify,
        )

    def test_008_fac_cat_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.fixed_asset_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
        )

    def test_009_fac_cat_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.fixed_asset_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_update,
            catalogue_name=catalogue_name_test_view_update,
            fixed_asset_type=fixed_asset_type_test_view_update,
            fixed_asset_classification=fixed_asset_classification_test_view_update,
            depreciation_method=depreciation_method_test_view_update,
            catalogue_status=catalogue_status_test_view_update,
            fixed_asset_life_time=fixed_asset_life_time_test_view_update,
            life_time_unit=life_time_unit_test_view_update,
            created_by=created_by_test_view_update,
            approve_by=approve_by_test_view_update,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_view_update,
            expected_gls_account_aliass=expected_gls_account_aliass_test_view_update,
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

    def test_010_fac_cat_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.fixed_asset_catalogue_definition_delete(
            catalogue_code=value_catalogue_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.fixed_asset_catalogue_definition_search_verify(
            catalogue_code=value_catalogue_code,
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_catalogue_code,
            tran_name=tran_name_delete,
        )

    def test_011_fac_cat_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.fixed_asset_catalogue_definition_simple_search(value_catalogue_code)
        self.assert_search_not_found()

    def test_012_fac_cat_delete_item_in_use_01_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.fixed_asset_catalogue_definition_delete(
            catalogue_code= catalogue_code_in_use,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.fixed_asset_catalogue_definition_search_verify(
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

    def test_012_fac_cat_delete_item_in_use_02_reject(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # reject delete
        self.bo_approval_reject(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=catalogue_code_in_use,
            tran_name=tran_name_delete,
        )
        # search master
        self.fixed_asset_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_in_use,
        )

if __name__ == '__main__': 
    webui_test.main()