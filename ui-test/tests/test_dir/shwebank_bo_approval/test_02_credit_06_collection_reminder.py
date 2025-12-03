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

action_add ='CRD-Collection Reminder-Add'
action_update ='CRD-Collection Reminder-Update'
tran_name_delete = 'CRD_DELETE_COLLECTION_REMINDER'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_reminder_code = 'AUTO00001'
list_error_message_in_use = [f'ReminderInUse: Reminder [{value_reminder_code}] is in use']
value_reminder_basis = 'On Due'
value_remind_officer = True
value_number_of_days = '0'
value_remind_customer = True
value_use_sms = True
value_sms_template = 'Dear ABC,\nThis is auto test add SMS.'
value_use_email = True
value_email_template_id = None
value_list_error_message = None

# data test add
reminder_code_test_add = value_reminder_code
reminder_name_test_add = f'AUTO TEST add {date_time}'
description_test_add = action_add
reminder_basis_test_add = value_reminder_basis
remind_officer_test_add = value_remind_officer
number_of_days_test_add = value_number_of_days
remind_customer_test_add = value_remind_customer
use_sms_test_add = value_use_sms
sms_template_test_add = value_sms_template
use_email_test_add = value_use_email
email_template_id_test_add = value_email_template_id
list_error_message_test_add = value_list_error_message

# data test add verify
reminder_code_test_add_verify = value_reminder_code
reminder_name_test_add_verify = reminder_name_test_add
description_test_add_verify = action_add
reminder_basis_test_add_verify = value_reminder_basis
remind_officer_test_add_verify = value_remind_officer
number_of_days_test_add_verify = value_number_of_days
remind_customer_test_add_verify = value_remind_customer
use_sms_test_add_verify = value_use_sms
sms_template_test_add_verify = value_sms_template
use_email_test_add_verify = value_use_email
email_template_id_test_add_verify = value_email_template_id

# data test view add
reminder_code_test_view_add = value_reminder_code
reminder_name_test_view_add = reminder_name_test_add
description_test_view_add = action_add
reminder_basis_test_view_add = value_reminder_basis
remind_officer_test_view_add = value_remind_officer
number_of_days_test_view_add = value_number_of_days
remind_customer_test_view_add = value_remind_customer
use_sms_test_view_add = value_use_sms
sms_template_test_view_add = value_sms_template
use_email_test_view_add = value_use_email
email_template_id_test_view_add = value_email_template_id

# data test update
reminder_code_test_update = value_reminder_code
reminder_name_test_update = f'AUTO TEST update {date_time}'
description_test_update = action_update
reminder_basis_test_update = 'After Due'
remind_officer_test_update = False
number_of_days_test_update = '160'
remind_customer_test_update = value_remind_customer
use_sms_test_update = value_use_sms
sms_template_test_update = 'Dear ABC,\nThis is auto test update SMS.'
use_email_test_update = False
email_template_id_test_update = value_email_template_id
list_error_message_test_update = value_list_error_message

# data test update verify
reminder_code_test_update_verify = value_reminder_code
reminder_name_test_update_verify = reminder_name_test_update
description_test_update_verify = action_update
reminder_basis_test_update_verify = reminder_basis_test_update
remind_officer_test_update_verify = remind_officer_test_update
number_of_days_test_update_verify = number_of_days_test_update
remind_customer_test_update_verify = value_remind_customer
use_sms_test_update_verify = value_use_sms
sms_template_test_update_verify = sms_template_test_update
use_email_test_update_verify = use_email_test_update
email_template_id_test_update_verify = value_email_template_id

# data test view update
reminder_code_test_view_update = value_reminder_code
reminder_name_test_view_update = reminder_name_test_update
description_test_view_update = action_update
reminder_basis_test_view_update = reminder_basis_test_update
remind_officer_test_view_update = remind_officer_test_update
number_of_days_test_view_update = number_of_days_test_update
remind_customer_test_view_update = value_remind_customer
use_sms_test_view_update = value_use_sms
sms_template_test_view_update = sms_template_test_update
use_email_test_view_update = use_email_test_update
email_template_id_test_view_update = value_email_template_id

# data not change for collection reminder profile
profile_code = 'AUTOPROFILE001'
profile_name = f'AUTO TEST add {date_time}'
reminder_codes = [f'{value_reminder_code}']
reminder_names = [f'{reminder_name_test_update}']
orders = ['1']

class CollectionReminderTest(FormAction):
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

# CRD-Collection Reminder
    def test_001_crd_collection_reminder_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.collection_reminder_add(
            reminder_code=reminder_code_test_add,
            reminder_name=reminder_name_test_add,
            description=description_test_add,
            reminder_basis=reminder_basis_test_add,
            remind_officer=remind_officer_test_add,
            number_of_days=number_of_days_test_add,
            remind_customer=remind_customer_test_add,
            use_sms=use_sms_test_add,
            sms_template=sms_template_test_add,
            use_email=use_email_test_add,
            email_template_id=email_template_id_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.collection_reminder_simple_search(value_reminder_code)
        self.assert_search_not_found()

    def test_002_crd_collection_reminder_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.collection_reminder_add_verify(
            transaction_number=transaction_number_add,
            reminder_code=reminder_code_test_add_verify,
            reminder_name=reminder_name_test_add_verify,
            description=description_test_add_verify,
            reminder_basis=reminder_basis_test_add_verify,
            remind_officer=remind_officer_test_add_verify,
            number_of_days=number_of_days_test_add_verify,
            remind_customer=remind_customer_test_add_verify,
            use_sms=use_sms_test_add_verify,
            sms_template=sms_template_test_add_verify,
            use_email=use_email_test_add_verify,
            email_template_id=email_template_id_test_add_verify,
        )

    def test_003_crd_collection_reminder_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.collection_reminder_search_verify(
            reminder_code=reminder_code_test_add,
            reminder_name=reminder_name_test_add,
            number_of_days=number_of_days_test_add,
        )

    def test_004_crd_collection_reminder_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_view(
            reminder_code=reminder_code_test_view_add,
            reminder_name=reminder_name_test_view_add,
            description=description_test_view_add,
            reminder_basis=reminder_basis_test_view_add,
            remind_officer=remind_officer_test_view_add,
            number_of_days=number_of_days_test_view_add,
            remind_customer=remind_customer_test_view_add,
            use_sms=use_sms_test_view_add,
            sms_template=sms_template_test_view_add,
            use_email=use_email_test_view_add,
            email_template_id=email_template_id_test_view_add,
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

    def test_006_crd_collection_reminder_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.collection_reminder_update(
            reminder_code=reminder_code_test_update,
            reminder_name=reminder_name_test_update,
            description=description_test_update,
            reminder_basis=reminder_basis_test_update,
            remind_officer=remind_officer_test_update,
            number_of_days=number_of_days_test_update,
            remind_customer=remind_customer_test_update,
            use_sms=use_sms_test_update,
            sms_template=sms_template_test_update,
            use_email=use_email_test_update,
            email_template_id=email_template_id_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.collection_reminder_search_verify(
            reminder_code=reminder_code_test_add,
            reminder_name=reminder_name_test_add,
            number_of_days=number_of_days_test_add,
        )

    def test_007_crd_collection_reminder_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.collection_reminder_update_verify(
            transaction_number=transaction_number_update,
            reminder_code=reminder_code_test_update_verify,
            reminder_name=reminder_name_test_update_verify,
            description=description_test_update_verify,
            reminder_basis=reminder_basis_test_update_verify,
            remind_officer=remind_officer_test_update_verify,
            number_of_days=number_of_days_test_update_verify,
            remind_customer=remind_customer_test_update_verify,
            use_sms=use_sms_test_update_verify,
            sms_template=sms_template_test_update_verify,
            use_email=use_email_test_update_verify,
            email_template_id=email_template_id_test_update_verify,
        )

    def test_008_crd_collection_reminder_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.collection_reminder_search_verify(
            reminder_code=reminder_code_test_update,
            reminder_name=reminder_name_test_update,
            number_of_days=number_of_days_test_update,
        )

    def test_009_crd_collection_reminder_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_view(
            reminder_code=reminder_code_test_view_update,
            reminder_name=reminder_name_test_view_update,
            description=description_test_view_update,
            reminder_basis=reminder_basis_test_view_update,
            remind_officer=remind_officer_test_view_update,
            number_of_days=number_of_days_test_view_update,
            remind_customer=remind_customer_test_view_update,
            use_sms=use_sms_test_view_update,
            sms_template=sms_template_test_view_update,
            use_email=use_email_test_view_update,
            email_template_id=email_template_id_test_view_update,
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

    def test_010_crd_collection_reminder_in_use_add_profile(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_profile_add(
            profile_code=profile_code,
            profile_name=profile_name,
            reminder_codes=reminder_codes,
            reminder_names=reminder_names,
            orders=orders,
        )
        transaction_number=self.get_transaction_number()
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )

    def test_011_crd_collection_reminder_delete_item_in_use_01_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_delete(
            reminder_code=value_reminder_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.collection_reminder_search_verify(
            reminder_code=reminder_code_test_update,
            reminder_name=reminder_name_test_update,
            number_of_days=number_of_days_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_reminder_code,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_reminder_code,
            tran_name=tran_name_delete,
            list_error_message=list_error_message_in_use,
        )

    def test_011_crd_collection_reminder_delete_item_in_use_02_reject(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # reject delete
        self.bo_approval_reject(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_reminder_code,
            tran_name=tran_name_delete,
        )
        # search master
        self.collection_reminder_search_verify(
            reminder_code=value_reminder_code,
        )

    def test_012_crd_collection_reminder_in_use_delete_profile(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_profile_delete(
            profile_code=profile_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.collection_reminder_profile_search_verify(
            profile_code=profile_code,
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=profile_code,
            tran_name='CRD_DELETE_COLLECTION_REMINDER_PROFILE',
        )
        self.collection_reminder_profile_simple_search(profile_code)
        self.assert_search_not_found()

    def test_013_crd_collection_reminder_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_delete(
            reminder_code=value_reminder_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.collection_reminder_search_verify(
            reminder_code=reminder_code_test_update,
            reminder_name=reminder_name_test_update,
            number_of_days=number_of_days_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_reminder_code,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_reminder_code,
            tran_name=tran_name_delete,
        )

    def test_014_crd_collection_reminder_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.collection_reminder_simple_search(value_reminder_code)
        self.assert_search_not_found()

if __name__ == '__main__': 
    webui_test.main()