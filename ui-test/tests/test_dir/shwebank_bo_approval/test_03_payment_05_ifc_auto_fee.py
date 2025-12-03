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

action_add ='PMT-IFC Auto Fee-Add'
action_update ='PMT-IFC Auto Fee-Update'
tran_name_delete = 'PMT_IFC_DELETE_IFCAUTOFEE'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_transaction_code = 'PMT_OIT'
value_ifc_code = '305'
value_condition = 'Region != CurrentRegion'
value_active = True
value_exchange = False
value_list_error_message = None

# data test add
transaction_code_test_add = value_transaction_code
ifc_code_test_add = value_ifc_code
condition_test_add = value_condition
active_test_add = value_active
exchange_test_add = value_exchange
list_error_message_test_add = None

# data test add verify
transaction_code_test_add_verify = value_transaction_code
ifc_code_test_add_verify = value_ifc_code
condition_test_add_verify = value_condition
active_test_add_verify = value_active
exchange_test_add_verify = value_exchange

# data test view add
transaction_code_test_view_add = value_transaction_code
ifc_code_test_view_add = value_ifc_code
condition_test_view_add = value_condition
active_test_view_add = value_active
exchange_test_view_add = value_exchange

# data test update
transaction_code_test_update = value_transaction_code
ifc_code_test_update = value_ifc_code
condition_test_update = 'Region == "R1"'
active_test_update = False
exchange_test_update = True
list_error_message_test_update = value_list_error_message

# data test update verify
transaction_code_test_update_verify = value_transaction_code
ifc_code_test_update_verify = value_ifc_code
condition_test_update_verify = condition_test_update
active_test_update_verify = active_test_update
exchange_test_update_verify = exchange_test_update

# data test view update
transaction_code_test_view_update = value_transaction_code
ifc_code_test_view_update = value_ifc_code
condition_test_view_update = condition_test_update
active_test_view_update = active_test_update
exchange_test_view_update = exchange_test_update

class PaymentIFCAutoFeeTest(FormAction):
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

# PMT-IFC Auto Fee
    def test_001_pmt_ifc_auto_fee_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.payment_ifc_auto_fee_add(
            transaction_code=transaction_code_test_add,
            ifc_code=ifc_code_test_add,
            condition=condition_test_add,
            active=active_test_add,
            exchange=exchange_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.payment_ifc_auto_fee_advanced_search(transaction_code=value_transaction_code, ifc_code=value_ifc_code)
        self.assert_search_not_found()

    def test_002_pmt_ifc_auto_fee_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.payment_ifc_auto_fee_add_verify(
            transaction_number=transaction_number_add,
            transaction_code=transaction_code_test_add_verify,
            ifc_code=ifc_code_test_add_verify,
            condition=condition_test_add_verify,
            active=active_test_add_verify,
            exchange=exchange_test_add_verify,
        )

    def test_003_pmt_ifc_auto_fee_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global value_ifc_code
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.payment_ifc_auto_fee_search_verify(
            transaction_code=transaction_code_test_add,
            ifc_code=ifc_code_test_add,
            transaction_name=None,
            ifc_name=None,
        )

    def test_004_pmt_ifc_auto_fee_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_ifc_auto_fee_view(
            transaction_code=transaction_code_test_view_add,
            ifc_code=ifc_code_test_view_add,
            condition=condition_test_view_add,
            active=active_test_view_add,
            exchange=exchange_test_view_add,
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

    def test_006_pmt_ifc_auto_fee_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.payment_ifc_auto_fee_update(
            transaction_code=transaction_code_test_update,
            ifc_code=ifc_code_test_update,
            condition=condition_test_update,
            active=active_test_update,
            exchange=exchange_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.payment_ifc_auto_fee_search_verify(
            transaction_code=transaction_code_test_add,
            ifc_code=ifc_code_test_add,
            transaction_name=None,
            ifc_name=None,
        )

    def test_007_pmt_ifc_auto_fee_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.payment_ifc_auto_fee_update_verify(
            transaction_number=transaction_number_update,
            transaction_code=transaction_code_test_update_verify,
            ifc_code=ifc_code_test_update_verify,
            condition=condition_test_update_verify,
            active=active_test_update_verify,
            exchange=exchange_test_update_verify,
        )

    def test_008_pmt_ifc_auto_fee_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.payment_ifc_auto_fee_search_verify(
            transaction_code=transaction_code_test_update,
            ifc_code=ifc_code_test_update,
            transaction_name=None,
            ifc_name=None,
        )

    def test_009_pmt_ifc_auto_fee_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_ifc_auto_fee_view(
            transaction_code=transaction_code_test_view_update,
            ifc_code=ifc_code_test_view_update,
            condition=condition_test_view_update,
            active=active_test_view_update,
            exchange=exchange_test_view_update,
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

    def test_010_pmt_ifc_auto_fee_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_ifc_auto_fee_delete(
            transaction_code=value_transaction_code,
            ifc_code=value_ifc_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.payment_ifc_auto_fee_search_verify(
            transaction_code=transaction_code_test_update,
            ifc_code=ifc_code_test_update,
            transaction_name=None,
            ifc_name=None,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=f'{value_transaction_code} | {value_ifc_code}',
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=f'{value_transaction_code} | {value_ifc_code}',
            tran_name=tran_name_delete,
        )

    def test_011_pmt_ifc_auto_fee_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_ifc_auto_fee_advanced_search(transaction_code=value_transaction_code, ifc_code=value_ifc_code)
        self.assert_search_not_found()

if __name__ == '__main__': 
    webui_test.main()