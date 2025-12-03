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

tran_name_delete = 'CRD_DELETE_COLLECTION_REMINDER_PROFILE'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_profile_code = 'AUTOPROFILE001'
list_error_message_in_use = [f'IsProfileCodeInUse: Reminder Profile is in use.']
value_reminder_codes = ['1DAYS_AFTER_DUEDATE', 'REMID_AFTER_DUE_DATE_7_DAYS']
value_reminder_names = ['Remind after due 7days', 'Remid after duedate 7 days']
value_orders = ['1', '2']
value_list_error_message = None

# data test add
profile_code_test_add = value_profile_code
profile_name_test_add = f'AUTO TEST add {date_time}'
reminder_codes_test_add = value_reminder_codes
reminder_names_test_add = value_reminder_names
orders_test_add = value_orders
list_error_message_test_add = value_list_error_message

# data test add verify
profile_code_test_add_verify = value_profile_code
profile_name_test_add_verify = profile_name_test_add
reminder_codes_test_add_verify = value_reminder_codes
reminder_names_test_add_verify = value_reminder_names
orders_test_add_verify = value_orders

# data test view add
profile_code_test_view_add = value_profile_code
profile_name_test_view_add = profile_name_test_add
reminder_codes_test_view_add = value_reminder_codes
reminder_names_test_view_add = value_reminder_names
orders_test_view_add = value_orders

# data test update
profile_code_test_update = value_profile_code
profile_name_test_update = f'AUTO TEST update {date_time}'
list_error_message_test_update = value_list_error_message

# data test update verify
profile_code_test_update_verify = value_profile_code
profile_name_test_update_verify = profile_name_test_update
reminder_codes_test_update_verify = value_reminder_codes
reminder_names_test_update_verify = value_reminder_names
orders_test_update_verify = value_orders

# data test view update
profile_code_test_view_update = value_profile_code
profile_name_test_view_update = profile_name_test_update
reminder_codes_test_view_update = value_reminder_codes
reminder_names_test_view_update = value_reminder_names
orders_test_view_update = value_orders

# data not change for catalog
catalogue_code = 'AUTODEL001'
catalogue_name = f'AUTO TEST add {date_time}'

class CollectionReminderProfileTest(FormAction):
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

# CRD-Collection Reminder Profile
    def test_001_crd_collection_reminder_profile_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.collection_reminder_profile_add(
            profile_code=profile_code_test_add,
            profile_name=profile_name_test_add,
            reminder_codes=reminder_codes_test_add,
            reminder_names=reminder_names_test_add,
            orders=orders_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.collection_reminder_profile_advanced_search(profile_code=value_profile_code)
        self.assert_search_not_found()

    def test_002_crd_collection_reminder_profile_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.collection_reminder_profile_add_verify(
            transaction_number=transaction_number_add,
            profile_code=profile_code_test_add_verify,
            profile_name=profile_name_test_add_verify,
            reminder_codes=reminder_codes_test_add_verify,
            reminder_names=reminder_names_test_add_verify,
            orders=orders_test_add_verify,
        )

    def test_003_crd_collection_reminder_profile_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.collection_reminder_profile_search_verify(
            profile_code=profile_code_test_add,
            profile_name=profile_name_test_add,
        )

    def test_004_crd_collection_reminder_profile_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_profile_view(
            profile_code=profile_code_test_view_add,
            profile_name=profile_name_test_view_add,
            reminder_codes=reminder_codes_test_view_add,
            reminder_names=reminder_names_test_view_add,
            orders=orders_test_view_add,
        )

    def test_005_login_with_other_user(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print(f'Username: {username_logged}')
        self.logout()
        self.login(username_other_branch, password_other_branch, one_app=ONE_APP)
        global other_username_logged
        other_username_logged = self.get_username()
        print(f'Other username: {other_username_logged}')

    def test_006_crd_collection_reminder_profile_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.collection_reminder_profile_update(
            profile_code=profile_code_test_update,
            profile_name=profile_name_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.collection_reminder_profile_search_verify(
            profile_code=profile_code_test_add,
            profile_name=profile_name_test_add,
        )

    def test_007_crd_collection_reminder_profile_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.collection_reminder_profile_update_verify(
            transaction_number=transaction_number_update,
            profile_code=profile_code_test_update_verify,
            profile_name=profile_name_test_update_verify,
            reminder_codes=reminder_codes_test_update_verify,
            reminder_names=reminder_names_test_update_verify,
            orders=orders_test_update_verify,
        )

    def test_008_crd_collection_reminder_profile_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.collection_reminder_profile_search_verify(
            profile_code=profile_code_test_update,
            profile_name=profile_name_test_update,
        )

    def test_009_crd_collection_reminder_profile_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_profile_view(
            profile_code=profile_code_test_view_update,
            profile_name=profile_name_test_view_update,
            reminder_codes=reminder_codes_test_view_update,
            reminder_names=reminder_names_test_view_update,
            orders=orders_test_view_update,
        )

    def test_010_crd_collection_reminder_profile_in_use_add_catalog(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.credit_catalogue_definition_add(
            catalogue_code=catalogue_code,
            catalogue_name=catalogue_name,
            principal_collection_tenor='1',
            interest_collection_tenor='1',
            fine_collection_tenor='1',
            reminder_profile_code=value_profile_code,
        )
        transaction_number=self.get_transaction_number()
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )

    def test_011_crd_collection_reminder_profile_delete_item_in_use_01_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_profile_delete(
            profile_code=value_profile_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.collection_reminder_profile_search_verify(
            profile_code=value_profile_code,
            profile_name=profile_name_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_profile_code,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_profile_code,
            tran_name=tran_name_delete,
            list_error_message=list_error_message_in_use,
        )

    def test_011_crd_collection_reminder_profile_delete_item_in_use_02_reject(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # reject delete
        self.bo_approval_reject(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_profile_code,
            tran_name=tran_name_delete,
        )
        # search master
        self.collection_reminder_profile_search_verify(
            profile_code=value_profile_code,
        )

    def test_012_crd_collection_reminder_profile_in_use_delete_catalog(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.credit_catalogue_definition_delete(
            catalogue_code=catalogue_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.credit_catalogue_definition_search_verify(
            catalogue_code=catalogue_code,
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=catalogue_code,
            tran_name='CRD_DELETE_CRDCAT',
        )
        self.credit_catalogue_definition_simple_search(catalogue_code)
        self.assert_search_not_found()

    def test_013_crd_collection_reminder_profile_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_profile_delete(
            profile_code=value_profile_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.collection_reminder_profile_search_verify(
            profile_code=profile_code_test_update,
            profile_name=profile_name_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_profile_code,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_profile_code,
            tran_name=tran_name_delete,
        )

    def test_014_crd_collection_reminder_profile_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_profile_advanced_search(profile_code=value_profile_code)
        self.assert_search_not_found()

if __name__ == '__main__': 
    webui_test.main()