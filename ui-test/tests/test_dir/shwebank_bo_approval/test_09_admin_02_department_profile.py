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

action_add ='ADM-Department Profile-Add'
action_update ='ADM-Department Profile-Update'
tran_name_delete = 'ADM_DELETE_DEPARTMENT'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']
list_error_message_in_use = [f'ERROR: Department is in use']

# data not change
value_department_code = '55555'
value_list_error_message = None

# data test add
department_code_test_add = value_department_code
department_name_test_add = f'AUTO TEST add {date_time}'
branch_code_test_add = '003 - Bayint Naung Branch'
list_error_message_test_add = value_list_error_message

# data test add verify
department_code_test_add_verify = department_code_test_add
department_name_test_add_verify = department_name_test_add
branch_code_test_add_verify = branch_code_test_add

# data test view add
department_code_test_view_add = department_code_test_add
department_name_test_view_add = department_name_test_add
branch_code_test_view_add = branch_code_test_add

# data test update
department_code_test_update = value_department_code
department_name_test_update = f'AUTO TEST update {date_time}'
branch_code_test_update = '002 - Yangon Head Office Branch'
list_error_message_test_update = value_list_error_message

# data test update verify
department_code_test_update_verify = department_code_test_update
department_name_test_update_verify = department_name_test_update
branch_code_test_update_verify = branch_code_test_update

# data test view update
department_code_test_view_update = department_code_test_update
department_name_test_view_update = department_name_test_update
branch_code_test_view_update = branch_code_test_update

# data not change for user
user_name_in_use = f'AUTO TEST add {date_time}'
login_name_in_use = 'autouser77'

class DepartmentProfileTest(FormAction):
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

# TRD-IFC Auto Fee
    def test_001_adm_department_profile_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.department_profile_add(
            department_code=department_code_test_add,
            department_name=department_name_test_add,
            branch_code=branch_code_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.department_profile_simple_search(value_department_code)
        self.assert_search_not_found()

    def test_002_adm_department_profile_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.department_profile_add_verify(
            transaction_number=transaction_number_add,
            department_code=department_code_test_add_verify,
            department_name=department_name_test_add_verify,
            branch_code=branch_code_test_add_verify,
        )

    def test_003_adm_department_profile_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.department_profile_search_verify(
            department_code=value_department_code,
            department_name=department_name_test_add,
            branch_name=None,
        )

    def test_004_adm_department_profile_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.department_profile_view(
            department_code=department_code_test_view_add,
            department_name=department_name_test_view_add,
            branch_code=branch_code_test_view_add,
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

    def test_006_adm_department_profile_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.department_profile_update(
            department_code=department_code_test_update,
            department_name=department_name_test_update,
            branch_code=branch_code_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.department_profile_search_verify(
            department_code=value_department_code,
            department_name=department_name_test_add,
            branch_name=None,
        )

    def test_007_adm_department_profile_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.department_profile_update_verify(
            transaction_number=transaction_number_update,
            department_code=department_code_test_update_verify,
            department_name=department_name_test_update_verify,
            branch_code=branch_code_test_update_verify,
        )

    def test_008_adm_department_profile_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.department_profile_search_verify(
            department_code=value_department_code,
            department_name=department_name_test_update,
            branch_name=None,
        )

    def test_009_adm_department_profile_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.department_profile_view(
            department_code=department_code_test_view_update,
            department_name=department_name_test_view_update,
            branch_code=branch_code_test_view_update,
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

    def test_010_adm_department_profile_in_use_add_user(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.user_profile_add(
            user_name=user_name_in_use,
            login_name=login_name_in_use,
            branch_code=branch_code_test_update,
            department_name=department_name_test_update,
        )
        transaction_number=self.get_transaction_number()
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )

    def test_011_adm_department_profile_delete_item_in_use_01_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.department_profile_delete(
            department_code=value_department_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.department_profile_search_verify(
            department_code=value_department_code,
            department_name=department_name_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_department_code,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_department_code,
            tran_name=tran_name_delete,
            list_error_message=list_error_message_in_use,
        )

    def test_011_adm_department_profile_delete_item_in_use_02_reject(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # reject delete
        self.bo_approval_reject(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_department_code,
            tran_name=tran_name_delete,
        )
        # search master
        self.department_profile_search_verify(
            department_code=value_department_code,
        )

    def test_012_adm_department_profile_in_use_delete_user(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # Delete user
        self.user_profile_delete(
            user_code=login_name_in_use,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.user_profile_search_verify(
            user_code=login_name_in_use,
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=login_name_in_use,
            tran_name='ADM_DELETE_USER_ACCOUNT',
        )
        self.user_profile_simple_search(login_name_in_use)
        self.assert_search_not_found()

    def test_013_adm_department_profile_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.department_profile_delete(
            department_code=value_department_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.department_profile_search_verify(
            department_code=value_department_code,
            department_name=department_name_test_update,
            branch_name=None,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_department_code,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_department_code,
            tran_name=tran_name_delete,
        )

    def test_014_adm_department_profile_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.department_profile_simple_search(value_department_code)
        self.assert_search_not_found()

if __name__ == '__main__':
    webui_test.main()