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

action_add ='ADM-Branch Linkage-Add'
action_update ='ADM-Branch Linkage-Update'
tran_name_delete = 'ADM_DELETE_BRANCHLKG'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
master_branch_code = '002'
master_branch_name = 'Yangon Head Office Branch'
linkage_branch_code = '003'
linkage_branch_name = 'Bayint Naung Branch'
value_master_branch_add = f'{master_branch_code}  - {master_branch_name}'
value_linkage_branch_add = f'{linkage_branch_code}  - {linkage_branch_name}'
value_master_branch = f'{master_branch_code} - {master_branch_name}'
value_linkage_branch = f'{linkage_branch_code} - {linkage_branch_name}'
value_linkage_type = 'Agent hub'
# value_description = None
value_list_error_message = None

# data test add
master_branch_test_add = value_master_branch
linkage_branch_test_add = value_linkage_branch
linkage_type_test_add = value_linkage_type
description_test_add = f'AUTO TEST add {date_time}'
list_error_message_test_add = value_list_error_message

# data test add verify
master_branch_test_add_verify = value_master_branch_add
linkage_branch_test_add_verify = value_linkage_branch_add
linkage_type_test_add_verify = value_linkage_type
description_test_add_verify = description_test_add

# data test view add
master_branch_test_view_add = value_master_branch
linkage_branch_test_view_add = value_linkage_branch
linkage_type_test_view_add = value_linkage_type
description_test_view_add = description_test_add

# data test update
master_branch_test_update = value_master_branch
linkage_branch_test_update = value_linkage_branch
linkage_type_test_update = value_linkage_type
description_test_update = f'AUTO TEST update {date_time}'
list_error_message_test_update = value_list_error_message

# data test update verify
master_branch_test_update_verify = value_master_branch
linkage_branch_test_update_verify = value_linkage_branch
linkage_type_test_update_verify = value_linkage_type
description_test_update_verify = description_test_update
list_error_message_test_update_verify = value_list_error_message

# data test view update
master_branch_test_view_update = value_master_branch
linkage_branch_test_view_update = value_linkage_branch
linkage_type_test_view_update = value_linkage_type
description_test_view_update = description_test_update

class BranchLinkageTest(FormAction):
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

# ADM-Branch Linkage
    def test_001_adm_branch_linkage_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.branch_linkage_add(
            master_branch=master_branch_test_add,
            linkage_branch=linkage_branch_test_add,
            linkage_type=linkage_type_test_add,
            description=description_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.branch_linkage_simple_search(description_test_add)
        self.assert_search_not_found()

    def test_002_adm_branch_linkage_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.branch_linkage_add_verify(
            transaction_number=transaction_number_add,
            master_branch=master_branch_test_add_verify,
            linkage_branch=linkage_branch_test_add_verify,
            linkage_type=linkage_type_test_add_verify,
            description=description_test_add_verify,
        )

    def test_003_adm_branch_linkage_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.branch_linkage_search_verify(
            master_branch_code=master_branch_code,
            linkage_branch_code=linkage_branch_code,
            linkage_type=value_linkage_type,
            linkage_description=description_test_add,
        )

    def test_004_adm_branch_linkage_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.branch_linkage_view(
            master_branch=master_branch_test_view_add,
            linkage_branch=linkage_branch_test_view_add,
            linkage_type=linkage_type_test_view_add,
            description=description_test_view_add,
        )

    def test_005_login_with_other_user(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print(f'Username: {username_logged}')
        self.logout()
        self.login(username_other_branch, password_other_branch, one_app=ONE_APP)
        global other_username_logged
        other_username_logged = self.get_username()
        print(f'Other username: {other_username_logged}')

    def test_006_adm_branch_linkage_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.branch_linkage_update(
            master_branch=master_branch_test_update,
            linkage_branch=linkage_branch_test_update,
            linkage_type=linkage_type_test_update,
            description_search=description_test_add,
            description_update=description_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.branch_linkage_search_verify(
            master_branch_code=master_branch_code,
            linkage_branch_code=linkage_branch_code,
            linkage_type=value_linkage_type,
            linkage_description=description_test_add,
        )

    def test_007_adm_branch_linkage_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.branch_linkage_update_verify(
            transaction_number=transaction_number_update,
            master_branch=master_branch_test_update_verify,
            linkage_branch=linkage_branch_test_update_verify,
            linkage_type=linkage_type_test_update_verify,
            description=description_test_update_verify,
        )

    def test_008_adm_branch_linkage_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.branch_linkage_search_verify(
            master_branch_code=master_branch_code,
            linkage_branch_code=linkage_branch_code,
            linkage_type=value_linkage_type,
            linkage_description=description_test_update,
        )

    def test_009_adm_branch_linkage_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.branch_linkage_view(
            master_branch=master_branch_test_view_update,
            linkage_branch=linkage_branch_test_view_update,
            linkage_type=linkage_type_test_view_update,
            description=description_test_view_update,
        )

    def test_010_adm_branch_linkage_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.branch_linkage_delete(
            description=description_test_update,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.branch_linkage_search_verify(
            master_branch_code=master_branch_code,
            linkage_branch_code=linkage_branch_code,
            linkage_type=value_linkage_type,
            linkage_description=description_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            status='Pending to approve',
            user_name=other_username_logged,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            status='Pending to approve',
            user_name=other_username_logged,
            tran_name=tran_name_delete,
        )

    def test_011_adm_branch_linkage_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.branch_linkage_simple_search(description_test_update)
        self.assert_search_not_found()

if __name__ == '__main__': 
    webui_test.main()