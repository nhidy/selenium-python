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

action_add ='ADM-System Policy-Add'
action_update ='ADM-System Policy-Update'
tran_name_delete = 'ADM_DELETE_USER_POLICY'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']
list_error_message_in_use = [f'ERROR: User policy is in use']

# data not change
value_list_error_message = None

# data test add
policy_id_test_add = None
description_of_policy_test_add = f'AUTO TEST add {date_time}'
effective_from_test_add = '20/11/2020'
effective_to_test_add = '20/11/2040'
enforce_password_history_test_add = '5'
maximum_password_age_test_add = '90'
minimum_password_length_test_add = '0'
password_must_meet_complexity_requirements_test_add = 'Yes'
at_least_one_lower_case_letter_test_add = 'No'
at_least_one_upper_case_letter_test_add = 'No'
at_least_symbol_character_test_add = None
at_least_one_number_test_add = 'No'
can_login_from_test_add = '00:00'
can_login_to_test_add = '24:00'
the_number_of_failed_logon_attempts_test_add = '0'
session_mode_test_add = 'Single-Device-With-Force-Logout'
list_error_message_test_add = value_list_error_message

# data test add verify
description_of_policy_test_add_verify = description_of_policy_test_add
effective_from_test_add_verify = effective_from_test_add
effective_to_test_add_verify = effective_to_test_add
enforce_password_history_test_add_verify = enforce_password_history_test_add
maximum_password_age_test_add_verify = maximum_password_age_test_add
minimum_password_length_test_add_verify = minimum_password_length_test_add
password_must_meet_complexity_requirements_test_add_verify = password_must_meet_complexity_requirements_test_add
at_least_one_lower_case_letter_test_add_verify = at_least_one_lower_case_letter_test_add
at_least_one_upper_case_letter_test_add_verify = at_least_one_upper_case_letter_test_add
at_least_symbol_character_test_add_verify = at_least_symbol_character_test_add
at_least_one_number_test_add_verify = at_least_one_number_test_add
can_login_from_test_add_verify = can_login_from_test_add
can_login_to_test_add_verify = can_login_to_test_add
the_number_of_failed_logon_attempts_test_add_verify = the_number_of_failed_logon_attempts_test_add
session_mode_test_add_verify = session_mode_test_add

# data test view add
description_of_policy_test_view_add = description_of_policy_test_add
effective_from_test_view_add = effective_from_test_add
effective_to_test_view_add = effective_to_test_add
enforce_password_history_test_view_add = enforce_password_history_test_add
maximum_password_age_test_view_add = maximum_password_age_test_add
minimum_password_length_test_view_add = minimum_password_length_test_add
password_must_meet_complexity_requirements_test_view_add = password_must_meet_complexity_requirements_test_add
at_least_symbol_character_test_view_add = at_least_symbol_character_test_add
at_least_one_upper_case_letter_test_view_add = at_least_one_upper_case_letter_test_add
at_least_one_lower_case_letter_test_view_add = at_least_one_lower_case_letter_test_add
at_least_one_number_test_view_add = at_least_one_number_test_add
can_login_from_test_view_add = can_login_from_test_add
can_login_to_test_view_add = can_login_to_test_add
the_number_of_failed_logon_attempts_test_view_add = the_number_of_failed_logon_attempts_test_add
session_mode_test_view_add = session_mode_test_add

# data test update
description_of_policy_test_update = f'AUTO TEST update {date_time}'
effective_from_test_update = '20/11/2025'
effective_to_test_update = '20/11/2045'
enforce_password_history_test_update = '3'
maximum_password_age_test_update = '190'
minimum_password_length_test_update = '8'
password_must_meet_complexity_requirements_test_update = 'Yes'
at_least_symbol_character_test_update = None
at_least_one_upper_case_letter_test_update = 'Yes'
at_least_one_lower_case_letter_test_update = 'Yes'
at_least_one_number_test_update = 'Yes'
can_login_from_test_update = '09:00'
can_login_to_test_update = '18:00'
the_number_of_failed_logon_attempts_test_update = '4'
session_mode_test_update = 'Single-Device'
list_error_message_test_update = value_list_error_message

# data test update verify
description_of_policy_test_update_verify = description_of_policy_test_update
effective_from_test_update_verify = effective_from_test_update
effective_to_test_update_verify = effective_to_test_update
enforce_password_history_test_update_verify = enforce_password_history_test_update
maximum_password_age_test_update_verify = maximum_password_age_test_update
minimum_password_length_test_update_verify = minimum_password_length_test_update
password_must_meet_complexity_requirements_test_update_verify = password_must_meet_complexity_requirements_test_update
at_least_symbol_character_test_update_verify = at_least_symbol_character_test_update
at_least_one_upper_case_letter_test_update_verify = at_least_one_upper_case_letter_test_update
at_least_one_lower_case_letter_test_update_verify = at_least_one_lower_case_letter_test_update
at_least_one_number_test_update_verify = at_least_one_number_test_update
can_login_from_test_update_verify = can_login_from_test_update
can_login_to_test_update_verify = can_login_to_test_update
the_number_of_failed_logon_attempts_test_update_verify = the_number_of_failed_logon_attempts_test_update
session_mode_test_update_verify = session_mode_test_update

# data test view update
description_of_policy_test_view_update = description_of_policy_test_update
effective_from_test_view_update = effective_from_test_update
effective_to_test_view_update = effective_to_test_update
enforce_password_history_test_view_update = enforce_password_history_test_update
maximum_password_age_test_view_update = maximum_password_age_test_update
minimum_password_length_test_view_update = minimum_password_length_test_update
password_must_meet_complexity_requirements_test_view_update = password_must_meet_complexity_requirements_test_update
at_least_symbol_character_test_view_update = at_least_symbol_character_test_update
at_least_one_upper_case_letter_test_view_update = at_least_one_upper_case_letter_test_update
at_least_one_lower_case_letter_test_view_update = at_least_one_lower_case_letter_test_update
at_least_one_number_test_view_update = at_least_one_number_test_update
can_login_from_test_view_update = can_login_from_test_update
can_login_to_test_view_update = can_login_to_test_update
the_number_of_failed_logon_attempts_test_view_update = the_number_of_failed_logon_attempts_test_update
session_mode_test_view_update = session_mode_test_update

# data not change for user
user_name_in_use = f'AUTO TEST add {date_time}'
login_name_in_use = 'autouser77'

class SystemPolicyTest(FormAction):
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

# ADM-System Policy
    def test_001_adm_system_policy_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.system_policy_add(
            policy_id=policy_id_test_add,
            description_of_policy=description_of_policy_test_add,
            effective_from=effective_from_test_add,
            effective_to=effective_to_test_add,
            enforce_password_history=enforce_password_history_test_add,
            maximum_password_age=maximum_password_age_test_add,
            minimum_password_length=minimum_password_length_test_add,
            password_must_meet_complexity_requirements=password_must_meet_complexity_requirements_test_add,
            at_least_one_lower_case_letter=at_least_one_lower_case_letter_test_add,
            at_least_one_upper_case_letter=at_least_one_upper_case_letter_test_add,
            at_least_symbol_character=at_least_symbol_character_test_add,
            at_least_one_number=at_least_one_number_test_add,
            can_login_from=can_login_from_test_add,
            can_login_to=can_login_to_test_add,
            the_number_of_failed_logon_attempts=the_number_of_failed_logon_attempts_test_add,
            session_mode=session_mode_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.system_policy_advanced_search(desciption_of_policy=description_of_policy_test_add)
        self.assert_search_not_found()

    def test_002_adm_system_policy_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.system_policy_add_verify(
            transaction_number=transaction_number_add,
            description_of_policy=description_of_policy_test_add_verify,
            effective_from=effective_from_test_add_verify,
            effective_to=effective_to_test_add_verify,
            enforce_password_history=enforce_password_history_test_add_verify,
            maximum_password_age=maximum_password_age_test_add_verify,
            minimum_password_length=minimum_password_length_test_add_verify,
            password_must_meet_complexity_requirements=password_must_meet_complexity_requirements_test_add_verify,
            at_least_one_lower_case_letter=at_least_one_lower_case_letter_test_add_verify,
            at_least_one_upper_case_letter=at_least_one_upper_case_letter_test_add_verify,
            at_least_symbol_character=at_least_symbol_character_test_add_verify,
            at_least_one_number=at_least_one_number_test_add_verify,
            can_login_from=can_login_from_test_add_verify,
            can_login_to=can_login_to_test_add_verify,
            the_number_of_failed_logon_attempts=the_number_of_failed_logon_attempts_test_add_verify,
            session_mode=session_mode_test_add_verify,
        )

    def test_003_adm_system_policy_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global value_policy_id
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # get policy id
        value_policy_id = self.system_policy_get_policy_id(description_of_policy_test_add)
        # search and verify master
        self.system_policy_search_verify(
            policy_id=value_policy_id,
            description_of_policy=description_of_policy_test_add,
            effective_from=effective_from_test_add,
            effective_to=effective_to_test_add,
        )

    def test_004_adm_system_policy_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.system_policy_view(
            policy_id=value_policy_id,
            description_of_policy=description_of_policy_test_view_add,
            effective_from=effective_from_test_view_add,
            effective_to=effective_to_test_view_add,
            enforce_password_history=enforce_password_history_test_view_add,
            maximum_password_age=maximum_password_age_test_view_add,
            minimum_password_length=minimum_password_length_test_view_add,
            password_must_meet_complexity_requirements=password_must_meet_complexity_requirements_test_view_add,
            at_least_symbol_character=at_least_symbol_character_test_view_add,
            at_least_one_upper_case_letter=at_least_one_upper_case_letter_test_view_add,
            at_least_one_lower_case_letter=at_least_one_lower_case_letter_test_view_add,
            at_least_one_number=at_least_one_number_test_view_add,
            can_login_from=can_login_from_test_view_add,
            can_login_to=can_login_to_test_view_add,
            the_number_of_failed_logon_attempts=the_number_of_failed_logon_attempts_test_view_add,
            session_mode=session_mode_test_view_add,
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

    def test_006_adm_system_policy_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.system_policy_update(
            policy_id=value_policy_id,
            description_of_policy=description_of_policy_test_update,
            effective_from=effective_from_test_update,
            effective_to=effective_to_test_update,
            enforce_password_history=enforce_password_history_test_update,
            maximum_password_age=maximum_password_age_test_update,
            minimum_password_length=minimum_password_length_test_update,
            password_must_meet_complexity_requirements=password_must_meet_complexity_requirements_test_update,
            at_least_symbol_character=at_least_symbol_character_test_update,
            at_least_one_upper_case_letter=at_least_one_upper_case_letter_test_update,
            at_least_one_lower_case_letter=at_least_one_lower_case_letter_test_update,
            at_least_one_number=at_least_one_number_test_update,
            can_login_from=can_login_from_test_update,
            can_login_to=can_login_to_test_update,
            the_number_of_failed_logon_attempts=the_number_of_failed_logon_attempts_test_update,
            session_mode=session_mode_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.system_policy_search_verify(
            policy_id=value_policy_id,
            description_of_policy=description_of_policy_test_add,
            effective_from=effective_from_test_add,
            effective_to=effective_to_test_add,
        )

    def test_007_adm_system_policy_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.system_policy_update_verify(
            transaction_number=transaction_number_update,
            policy_id=value_policy_id,
            description_of_policy=description_of_policy_test_update_verify,
            effective_from=effective_from_test_update_verify,
            effective_to=effective_to_test_update_verify,
            enforce_password_history=enforce_password_history_test_update_verify,
            maximum_password_age=maximum_password_age_test_update_verify,
            minimum_password_length=minimum_password_length_test_update_verify,
            password_must_meet_complexity_requirements=password_must_meet_complexity_requirements_test_update_verify,
            at_least_symbol_character=at_least_symbol_character_test_update_verify,
            at_least_one_upper_case_letter=at_least_one_upper_case_letter_test_update_verify,
            at_least_one_lower_case_letter=at_least_one_lower_case_letter_test_update_verify,
            at_least_one_number=at_least_one_number_test_update_verify,
            can_login_from=can_login_from_test_update_verify,
            can_login_to=can_login_to_test_update_verify,
            the_number_of_failed_logon_attempts=the_number_of_failed_logon_attempts_test_update_verify,
            session_mode=session_mode_test_update_verify,
        )

    def test_008_adm_system_policy_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.system_policy_search_verify(
            policy_id=value_policy_id,
            description_of_policy=description_of_policy_test_update,
            effective_from=effective_from_test_update,
            effective_to=effective_to_test_update,
        )

    def test_009_adm_system_policy_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.system_policy_view(
            policy_id=value_policy_id,
            description_of_policy=description_of_policy_test_view_update,
            effective_from=effective_from_test_view_update,
            effective_to=effective_to_test_view_update,
            enforce_password_history=enforce_password_history_test_view_update,
            maximum_password_age=maximum_password_age_test_view_update,
            minimum_password_length=minimum_password_length_test_view_update,
            password_must_meet_complexity_requirements=password_must_meet_complexity_requirements_test_view_update,
            at_least_symbol_character=at_least_symbol_character_test_view_update,
            at_least_one_upper_case_letter=at_least_one_upper_case_letter_test_view_update,
            at_least_one_lower_case_letter=at_least_one_lower_case_letter_test_view_update,
            at_least_one_number=at_least_one_number_test_view_update,
            can_login_from=can_login_from_test_view_update,
            can_login_to=can_login_to_test_view_update,
            the_number_of_failed_logon_attempts=the_number_of_failed_logon_attempts_test_view_update,
            session_mode=session_mode_test_view_update,
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

    def test_010_adm_system_policy_in_use_add_user(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.user_profile_add(
            user_name=user_name_in_use,
            login_name=login_name_in_use,
            id_of_policy_apply_for_this_user=description_of_policy_test_update
        )
        transaction_number=self.get_transaction_number()
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )

    def test_011_adm_system_policy_delete_item_in_use_01_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.system_policy_delete(
            policy_id=value_policy_id,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.system_policy_search_verify(
            policy_id=value_policy_id,
            description_of_policy=description_of_policy_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_policy_id,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_policy_id,
            tran_name=tran_name_delete,
            list_error_message=list_error_message_in_use,
        )

    def test_011_adm_system_policy_delete_item_in_use_02_reject(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # reject delete
        self.bo_approval_reject(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_policy_id,
            tran_name=tran_name_delete,
        )
        # search master
        self.system_policy_search_verify(
            policy_id=value_policy_id,
        )

    def test_012_adm_system_policy_in_use_delete_user(self):
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

    def test_013_adm_system_policy_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.system_policy_delete(
            policy_id=value_policy_id,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.system_policy_search_verify(
            policy_id=value_policy_id,
            description_of_policy=description_of_policy_test_update,
            effective_from=effective_from_test_update,
            effective_to=effective_to_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_policy_id,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_policy_id,
            tran_name=tran_name_delete,
        )

    def test_014_adm_system_policy_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.system_policy_advanced_search(policy_id=value_policy_id)
        self.assert_search_not_found()

if __name__ == '__main__':
    webui_test.main()