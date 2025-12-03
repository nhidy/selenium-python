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

action_add ='Terminal management-Add'
action_update ='Terminal management-Update'
tran_name_delete = 'CAR_DEL_TRMID'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_channel = 'ATM'
value_terminal_id = 'AUTO0001'
value_branch = '002 - Yangon Head Office Branch'
value_account_number_or_gl = '08665534543'
value_terminal_address = 'Terminal address add'
value_intelligent_deposit = 'No'
value_merchant_id = 'Merchant ID add'
value_status = 'Open'
value_list_error_message = None

# data test add
channel_test_add = value_channel
terminal_id_test_add = value_terminal_id
branch_test_add = value_branch
account_number_or_gl_test_add = value_account_number_or_gl
terminal_address_test_add = value_terminal_address
intelligent_deposit_test_add = value_intelligent_deposit
merchant_id_test_add = value_merchant_id
status_test_add = value_status
list_error_message_test_add = value_list_error_message

# data test add verify
channel_test_add_verify = channel_test_add
terminal_id_test_add_verify = terminal_id_test_add
branch_test_add_verify = branch_test_add
account_number_or_gl_test_add_verify = account_number_or_gl_test_add
terminal_address_test_add_verify = terminal_address_test_add
intelligent_deposit_test_add_verify = intelligent_deposit_test_add
merchant_id_test_add_verify = merchant_id_test_add
status_test_add_verify = status_test_add

# data test view add
channel_test_view_add = channel_test_add
terminal_id_test_view_add = terminal_id_test_add
branch_test_view_add = branch_test_add
account_number_or_gl_test_view_add = account_number_or_gl_test_add
terminal_address_test_view_add = terminal_address_test_add
intelligent_deposit_test_view_add = intelligent_deposit_test_add
merchant_id_test_view_add = merchant_id_test_add
status_test_view_add = status_test_add

# data test update
channel_test_update = 'Ecommerce'
terminal_id_test_update = value_terminal_id
branch_test_update = '003 - Bayint Naung Branch'
account_number_or_gl_test_update = '08885534543'
terminal_address_test_update = 'Terminal address update'
intelligent_deposit_test_update = 'Yes'
merchant_id_test_update = 'Merchant ID update'
status_test_update = 'Close'
list_error_message_test_update = value_list_error_message

# data test update verify
channel_test_update_verify = channel_test_update
terminal_id_test_update_verify = terminal_id_test_update
branch_test_update_verify = branch_test_update
account_number_or_gl_test_update_verify = account_number_or_gl_test_update
terminal_address_test_update_verify = terminal_address_test_update
intelligent_deposit_test_update_verify = intelligent_deposit_test_update
merchant_id_test_update_verify = merchant_id_test_update
status_test_update_verify = status_test_update

# data test view update
channel_test_view_update = channel_test_update
terminal_id_test_view_update = terminal_id_test_update
branch_test_view_update = branch_test_update
account_number_or_gl_test_view_update = account_number_or_gl_test_update
terminal_address_test_view_update = terminal_address_test_update
intelligent_deposit_test_view_update = intelligent_deposit_test_update
merchant_id_test_view_update = merchant_id_test_update
status_test_view_update = status_test_update

class TerminalManagementTest(FormAction):
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

# Terminal Management
    def test_001_car_terminal_management_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.terminal_management_add(
            channel=channel_test_add,
            terminal_id=terminal_id_test_add,
            branch=branch_test_add,
            account_number_or_gl=account_number_or_gl_test_add,
            terminal_address=terminal_address_test_add,
            intelligent_deposit=intelligent_deposit_test_add,
            merchant_id=merchant_id_test_add,
            status=status_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.terminal_management_simple_search(value_terminal_id)
        self.assert_search_not_found()

    def test_002_car_terminal_management_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.terminal_management_add_verify(
            transaction_number=transaction_number_add,
            channel=channel_test_add_verify,
            terminal_id=terminal_id_test_add_verify,
            branch=branch_test_add_verify,
            account_number_or_gl=account_number_or_gl_test_add_verify,
            terminal_address=terminal_address_test_add_verify,
            intelligent_deposit=intelligent_deposit_test_add_verify,
            merchant_id=merchant_id_test_add_verify,
            status=status_test_add_verify,
        )

    def test_003_car_terminal_management_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.terminal_management_search_verify(
            channel=channel_test_add,
            terminal_id=terminal_id_test_add,
            branch=branch_test_add,
            account_number_or_gl=account_number_or_gl_test_add,
            terminal_address=terminal_address_test_add,
            intelligent_deposit=intelligent_deposit_test_add,
            merchant_id=merchant_id_test_add,
            status=status_test_add,
        )

    def test_004_car_terminal_management_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.terminal_management_view(
            channel=channel_test_view_add,
            terminal_id=terminal_id_test_view_add,
            branch=branch_test_view_add,
            account_number_or_gl=account_number_or_gl_test_view_add,
            terminal_address=terminal_address_test_view_add,
            intelligent_deposit=intelligent_deposit_test_view_add,
            merchant_id=merchant_id_test_view_add,
            status=status_test_view_add,
        )

    def test_005_login_with_other_user(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print(f'Username: {username_logged}')
        self.logout()
        self.login(username_other_branch, password_other_branch, one_app=ONE_APP)
        global other_username_logged
        other_username_logged = self.get_username()
        print(f'Other username: {other_username_logged}')

    def test_006_car_terminal_management_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.terminal_management_update(
            channel=channel_test_update,
            terminal_id=terminal_id_test_update,
            branch=branch_test_update,
            account_number_or_gl=account_number_or_gl_test_update,
            terminal_address=terminal_address_test_update,
            intelligent_deposit=intelligent_deposit_test_update,
            merchant_id=merchant_id_test_update,
            status=status_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.terminal_management_search_verify(
            channel=channel_test_add,
            terminal_id=terminal_id_test_add,
            branch=branch_test_add,
            account_number_or_gl=account_number_or_gl_test_add,
            terminal_address=terminal_address_test_add,
            intelligent_deposit=intelligent_deposit_test_add,
            merchant_id=merchant_id_test_add,
            status=status_test_add,
        )

    def test_007_car_terminal_management_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.terminal_management_update_verify(
            transaction_number=transaction_number_update,
            channel=channel_test_update_verify,
            terminal_id=terminal_id_test_update_verify,
            branch=branch_test_update_verify,
            account_number_or_gl=account_number_or_gl_test_update_verify,
            terminal_address=terminal_address_test_update_verify,
            intelligent_deposit=intelligent_deposit_test_update_verify,
            merchant_id=merchant_id_test_update_verify,
            status=status_test_update_verify,
        )

    def test_008_car_terminal_management_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.terminal_management_search_verify(
            channel=channel_test_update,
            terminal_id=terminal_id_test_update,
            branch=branch_test_update,
            account_number_or_gl=account_number_or_gl_test_update,
            terminal_address=terminal_address_test_update,
            intelligent_deposit=intelligent_deposit_test_update,
            merchant_id=merchant_id_test_update,
            status=status_test_update,
        )

    def test_009_car_terminal_management_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.terminal_management_view(
            channel=channel_test_view_update,
            terminal_id=terminal_id_test_view_update,
            branch=branch_test_view_update,
            account_number_or_gl=account_number_or_gl_test_view_update,
            terminal_address=terminal_address_test_view_update,
            intelligent_deposit=intelligent_deposit_test_view_update,
            merchant_id=merchant_id_test_view_update,
            status=status_test_view_update,
        )

    def test_010_car_terminal_management_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.terminal_management_delete(
            terminal_id=value_terminal_id,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.terminal_management_search_verify(
            channel=channel_test_update,
            terminal_id=terminal_id_test_update,
            branch=branch_test_update,
            account_number_or_gl=account_number_or_gl_test_update,
            terminal_address=terminal_address_test_update,
            intelligent_deposit=intelligent_deposit_test_update,
            merchant_id=merchant_id_test_update,
            status=status_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            status='Pending to approve',
            user_name=other_username_logged,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete,
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            tran_name=tran_name_delete,
            status='Pending to approve',
            user_name=other_username_logged,
        )

    def test_011_car_terminal_management_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.terminal_management_simple_search(value_terminal_id)
        self.assert_search_not_found()

if __name__ == '__main__': 
    webui_test.main()