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

action_add ='ADM-User Profile-Add'
action_update ='ADM-User Profile-Update'
tran_name_delete = 'ADM_DELETE_USER_ACCOUNT'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_old_user_id = '0754354'
value_user_name = f'AUTO TEST add {date_time}'
value_login_name = 'autouser01'

value_branch_code = '003'
value_branch_name = 'Bayint Naung Branch'
value_branch_code_add = f'{value_branch_code}  - {value_branch_name}'
value_branch_code_add_view = f'{value_branch_code} - {value_branch_name}'
value_department_name = '003 - BYN'

value_cashier = True
value_officer = True
value_chief_cashier = True
value_operation_staff = True
value_dealer = True
value_inter_branch_user = False
value_branch_manager_authorized = False
value_hr = False
value_email = 'autouser01@gmail.com'
value_remark = 'Team 01'
value_status_of_this_record = 'Active'
value_password = None
value_main_language = 'German'
value_user_phone = '09-886-543-232'
value_home = '08-886-543-232'
value_office = '07-886-543-232'
value_cell = '06-886-543-232'
value_facsimile = '05-886-543-232'
value_telex = '04-886-543-232'
value_time_zone_of_user = '(GMT+06:30) Yangon Myanmar'
value_thousand_separate_character_in_amount_field = ','
value_decimal_separate_character_in_amount_field = '.'
value_date_format_for_short = 'M/d/yy'
value_long_date_format = 'MMMM dd, yyyy'
value_time_format = 'h:mm:ss tt'
value_expire_date_of_this_user = '31/12/2030'
value_id_of_policy_apply_for_this_user = 'Single session policy'
value_is_online = 'No'
value_list_error_message = None

# data test add
user_code_test_add = None
old_user_id_test_add = value_old_user_id
user_name_test_add = value_user_name
login_name_test_add = value_login_name
branch_code_test_add = value_branch_code_add_view
department_name_test_add = value_department_name
cashier_test_add = value_cashier
officer_test_add = value_officer
chief_cashier_test_add = value_chief_cashier
operation_staff_test_add = value_operation_staff
dealer_test_add = value_dealer
inter_branch_user_test_add = value_inter_branch_user
branch_manager_authorized_test_add = value_branch_manager_authorized
hr_test_add = value_hr
email_test_add = value_email
remark_test_add = value_remark
status_of_this_record_test_add = value_status_of_this_record
password_test_add = value_password
main_language_test_add = value_main_language
user_phone_test_add = value_user_phone
home_test_add = value_home
office_test_add = value_office
cell_test_add = value_cell
facsimile_test_add = value_facsimile
telex_test_add = value_telex
time_zone_of_user_test_add = value_time_zone_of_user
thousand_separate_character_in_amount_field_test_add = value_thousand_separate_character_in_amount_field
decimal_separate_character_in_amount_field_test_add = value_decimal_separate_character_in_amount_field
date_format_for_short_test_add = value_date_format_for_short
long_date_format_test_add = value_long_date_format
time_format_test_add = value_time_format
expire_date_of_this_user_test_add = value_expire_date_of_this_user
id_of_policy_apply_for_this_user_test_add = value_id_of_policy_apply_for_this_user
list_error_message_test_add = value_list_error_message

# data test add verify
user_code_test_add_verify = None
old_user_id_test_add_verify = old_user_id_test_add
user_name_test_add_verify = user_name_test_add
login_name_test_add_verify = login_name_test_add
branch_code_test_add_verify = value_branch_code_add
department_name_test_add_verify = department_name_test_add
cashier_test_add_verify = cashier_test_add
officer_test_add_verify = officer_test_add
chief_cashier_test_add_verify = chief_cashier_test_add
operation_staff_test_add_verify = operation_staff_test_add
dealer_test_add_verify = dealer_test_add
inter_branch_user_test_add_verify = inter_branch_user_test_add
branch_manager_authorized_test_add_verify = branch_manager_authorized_test_add
hr_test_add_verify = hr_test_add
email_test_add_verify = email_test_add
remark_test_add_verify = remark_test_add
status_of_this_record_test_add_verify = status_of_this_record_test_add
password_test_add_verify = password_test_add
main_language_test_add_verify = main_language_test_add
user_phone_test_add_verify = user_phone_test_add
home_test_add_verify = home_test_add
office_test_add_verify = office_test_add
cell_test_add_verify = cell_test_add
facsimile_test_add_verify = facsimile_test_add
telex_test_add_verify = telex_test_add
time_zone_of_user_test_add_verify = time_zone_of_user_test_add
thousand_separate_character_in_amount_field_test_add_verify = thousand_separate_character_in_amount_field_test_add
decimal_separate_character_in_amount_field_test_add_verify = decimal_separate_character_in_amount_field_test_add
date_format_for_short_test_add_verify = date_format_for_short_test_add
long_date_format_test_add_verify = long_date_format_test_add
time_format_test_add_verify = time_format_test_add
expire_date_of_this_user_test_add_verify = expire_date_of_this_user_test_add
id_of_policy_apply_for_this_user_test_add_verify = id_of_policy_apply_for_this_user_test_add

# data test view add
user_code_test_view_add = value_login_name
old_user_id_test_view_add = old_user_id_test_add
user_name_test_view_add = user_name_test_add
login_name_test_view_add = login_name_test_add
branch_code_test_view_add = branch_code_test_add
department_name_test_view_add = department_name_test_add
cashier_test_view_add = cashier_test_add
officer_test_view_add = officer_test_add
chief_cashier_test_view_add = chief_cashier_test_add
operation_staff_test_view_add = operation_staff_test_add
dealer_test_view_add = dealer_test_add
inter_branch_user_test_view_add = inter_branch_user_test_add
branch_manager_authorized_test_view_add = branch_manager_authorized_test_add
hr_test_view_add = hr_test_add
email_test_view_add = email_test_add
remark_test_view_add = remark_test_add
status_of_this_record_test_view_add = status_of_this_record_test_add
password_test_view_add = password_test_add
main_language_test_view_add = main_language_test_add
user_phone_test_view_add = user_phone_test_add
home_test_view_add = home_test_add
office_test_view_add = office_test_add
cell_test_view_add = cell_test_add
facsimile_test_view_add = facsimile_test_add
telex_test_view_add = telex_test_add
time_zone_of_user_test_view_add = time_zone_of_user_test_add
thousand_separate_character_in_amount_field_test_view_add = thousand_separate_character_in_amount_field_test_add
decimal_separate_character_in_amount_field_test_view_add = decimal_separate_character_in_amount_field_test_add
date_format_for_short_test_view_add = date_format_for_short_test_add
long_date_format_test_view_add = long_date_format_test_add
time_format_test_view_add = time_format_test_add
expire_date_of_this_user_test_view_add = expire_date_of_this_user_test_add
id_of_policy_apply_for_this_user_test_view_add = id_of_policy_apply_for_this_user_test_add


value_branch_code_up = '002'
value_branch_name_up = 'Yangon Head Office Branch'
# value_branch_code_update = f'{value_branch_code_up}  - {value_branch_name_up}'
value_branch_code_update_view = f'{value_branch_code_up} - {value_branch_name_up}'
value_department_name_update = '002 - HO-Br'
# data test update
user_code_test_update = value_login_name
old_user_id_test_update = '0778354'
user_name_test_update = f'AUTO TEST update {date_time}'
login_name_test_update = value_login_name
branch_code_test_update = value_branch_code_update_view
department_name_test_update = value_department_name_update
cashier_test_update = False
officer_test_update = False
chief_cashier_test_update = False
operation_staff_test_update = True
dealer_test_update = True
inter_branch_user_test_update = True
branch_manager_authorized_test_update = True
hr_test_update = True
email_test_update = 'autouser01update@gmail.com'
remark_test_update = 'Team 01 update'
status_of_this_record_test_update = 'Active'
password_test_update = value_password
main_language_test_update = 'English'
user_phone_test_update = '09-996-543-232'
home_test_update = '08-996-543-232'
office_test_update = '07-996-543-232'
cell_test_update = '06-996-543-232'
facsimile_test_update = '05-996-543-232'
telex_test_update = '04-996-543-232'
time_zone_of_user_test_update = '(GMT-12:00) International Date Line West'
thousand_separate_character_in_amount_field_test_update = '.'
decimal_separate_character_in_amount_field_test_update = ','
date_format_for_short_test_update = 'MM/dd/yy'
long_date_format_test_update = 'dddd, dd MMMM, yyyy'
time_format_test_update = 'H:mm:ss'
expire_date_of_this_user_test_update = '31/12/2045'
id_of_policy_apply_for_this_user_test_update = 'Multi-Device Session Policy'
list_error_message_test_update = value_list_error_message

# data test update verify
user_code_test_update_verify = user_code_test_update
old_user_id_test_update_verify = old_user_id_test_update
user_name_test_update_verify = user_name_test_update
login_name_test_update_verify = login_name_test_update
branch_code_test_update_verify = branch_code_test_update
department_name_test_update_verify = department_name_test_update
cashier_test_update_verify = cashier_test_update
officer_test_update_verify = officer_test_update
chief_cashier_test_update_verify = chief_cashier_test_update
operation_staff_test_update_verify = operation_staff_test_update
dealer_test_update_verify = dealer_test_update
inter_branch_user_test_update_verify = inter_branch_user_test_update
branch_manager_authorized_test_update_verify = branch_manager_authorized_test_update
hr_test_update_verify = hr_test_update
email_test_update_verify = email_test_update
remark_test_update_verify = remark_test_update
status_of_this_record_test_update_verify = status_of_this_record_test_update
password_test_update_verify = password_test_update
main_language_test_update_verify = main_language_test_update
user_phone_test_update_verify = user_phone_test_update
home_test_update_verify = home_test_update
office_test_update_verify = office_test_update
cell_test_update_verify = cell_test_update
facsimile_test_update_verify = facsimile_test_update
telex_test_update_verify = telex_test_update
time_zone_of_user_test_update_verify = time_zone_of_user_test_update
thousand_separate_character_in_amount_field_test_update_verify = thousand_separate_character_in_amount_field_test_update
decimal_separate_character_in_amount_field_test_update_verify = decimal_separate_character_in_amount_field_test_update
date_format_for_short_test_update_verify = date_format_for_short_test_update
long_date_format_test_update_verify = long_date_format_test_update
time_format_test_update_verify = time_format_test_update
expire_date_of_this_user_test_update_verify = expire_date_of_this_user_test_update
id_of_policy_apply_for_this_user_test_update_verify = id_of_policy_apply_for_this_user_test_update

# data test view update
user_code_test_view_update = user_code_test_update
old_user_id_test_view_update = old_user_id_test_update
user_name_test_view_update = user_name_test_update
login_name_test_view_update = login_name_test_update
branch_code_test_view_update = branch_code_test_update
department_name_test_view_update = department_name_test_update
cashier_test_view_update = cashier_test_update
officer_test_view_update = officer_test_update
chief_cashier_test_view_update = chief_cashier_test_update
operation_staff_test_view_update = operation_staff_test_update
dealer_test_view_update = dealer_test_update
inter_branch_user_test_view_update = inter_branch_user_test_update
branch_manager_authorized_test_view_update = branch_manager_authorized_test_update
hr_test_view_update = hr_test_update
email_test_view_update = email_test_update
remark_test_view_update = remark_test_update
status_of_this_record_test_view_update = status_of_this_record_test_update
password_test_view_update = password_test_update
main_language_test_view_update = main_language_test_update
user_phone_test_view_update = user_phone_test_update
home_test_view_update = home_test_update
office_test_view_update = office_test_update
cell_test_view_update = cell_test_update
facsimile_test_view_update = facsimile_test_update
telex_test_view_update = telex_test_update
time_zone_of_user_test_view_update = time_zone_of_user_test_update
thousand_separate_character_in_amount_field_test_view_update = thousand_separate_character_in_amount_field_test_update
decimal_separate_character_in_amount_field_test_view_update = decimal_separate_character_in_amount_field_test_update
date_format_for_short_test_view_update = date_format_for_short_test_update
long_date_format_test_view_update = long_date_format_test_update
time_format_test_view_update = time_format_test_update
expire_date_of_this_user_test_view_update = expire_date_of_this_user_test_update
id_of_policy_apply_for_this_user_test_view_update = id_of_policy_apply_for_this_user_test_update

class UserProfileTest(FormAction):
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

# ADM-User Profile
    def test_001_adm_user_profile_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.user_profile_add(
            user_code=user_code_test_add,
            old_user_id=old_user_id_test_add,
            user_name=user_name_test_add,
            login_name=login_name_test_add,
            branch_code=branch_code_test_add,
            department_name=department_name_test_add,
            cashier=cashier_test_add,
            officer=officer_test_add,
            chief_cashier=chief_cashier_test_add,
            operation_staff=operation_staff_test_add,
            dealer=dealer_test_add,
            inter_branch_user=inter_branch_user_test_add,
            branch_manager_authorized=branch_manager_authorized_test_add,
            hr=hr_test_add,
            email=email_test_add,
            remark=remark_test_add,
            status_of_this_record=status_of_this_record_test_add,
            password=password_test_add,
            main_language=main_language_test_add,
            user_phone=user_phone_test_add,
            home=home_test_add,
            office=office_test_add,
            cell=cell_test_add,
            facsimile=facsimile_test_add,
            telex=telex_test_add,
            time_zone_of_user=time_zone_of_user_test_add,
            thousand_separate_character_in_amount_field=thousand_separate_character_in_amount_field_test_add,
            decimal_separate_character_in_amount_field=decimal_separate_character_in_amount_field_test_add,
            date_format_for_short=date_format_for_short_test_add,
            long_date_format=long_date_format_test_add,
            time_format=time_format_test_add,
            expire_date_of_this_user=expire_date_of_this_user_test_add,
            id_of_policy_apply_for_this_user=id_of_policy_apply_for_this_user_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.user_profile_simple_search(value_login_name)
        self.assert_search_not_found()

    def test_002_adm_user_profile_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.user_profile_add_verify(
            transaction_number=transaction_number_add,
            user_code=user_code_test_add_verify,
            old_user_id=old_user_id_test_add_verify,
            user_name=user_name_test_add_verify,
            login_name=login_name_test_add_verify,
            branch_code=branch_code_test_add_verify,
            department_name=department_name_test_add_verify,
            cashier=cashier_test_add_verify,
            officer=officer_test_add_verify,
            chief_cashier=chief_cashier_test_add_verify,
            operation_staff=operation_staff_test_add_verify,
            dealer=dealer_test_add_verify,
            inter_branch_user=inter_branch_user_test_add_verify,
            branch_manager_authorized=branch_manager_authorized_test_add_verify,
            hr=hr_test_add_verify,
            email=email_test_add_verify,
            remark=remark_test_add_verify,
            status_of_this_record=status_of_this_record_test_add_verify,
            password=password_test_add_verify,
            main_language=main_language_test_add_verify,
            user_phone=user_phone_test_add_verify,
            home=home_test_add_verify,
            office=office_test_add_verify,
            cell=cell_test_add_verify,
            facsimile=facsimile_test_add_verify,
            telex=telex_test_add_verify,
            time_zone_of_user=time_zone_of_user_test_add_verify,
            thousand_separate_character_in_amount_field=thousand_separate_character_in_amount_field_test_add_verify,
            decimal_separate_character_in_amount_field=decimal_separate_character_in_amount_field_test_add_verify,
            date_format_for_short=date_format_for_short_test_add_verify,
            long_date_format=long_date_format_test_add_verify,
            time_format=time_format_test_add_verify,
            expire_date_of_this_user=expire_date_of_this_user_test_add_verify,
            id_of_policy_apply_for_this_user=id_of_policy_apply_for_this_user_test_add_verify,
        )

    def test_003_adm_user_profile_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.user_profile_search_verify(
            user_code=value_login_name,
            user_name=user_name_test_add,
            login_name=value_login_name,
            branch_name=value_branch_name,
            department_name=department_name_test_add,
            status=status_of_this_record_test_add,
            is_online=value_is_online,
            email=email_test_add,
        )

    def test_004_adm_user_profile_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.user_profile_view(
            user_code=user_code_test_view_add,
            old_user_id=old_user_id_test_view_add,
            user_name=user_name_test_view_add,
            login_name=login_name_test_view_add,
            branch_code=branch_code_test_view_add,
            department_name=department_name_test_view_add,
            cashier=cashier_test_view_add,
            officer=officer_test_view_add,
            chief_cashier=chief_cashier_test_view_add,
            operation_staff=operation_staff_test_view_add,
            dealer=dealer_test_view_add,
            inter_branch_user=inter_branch_user_test_view_add,
            branch_manager_authorized=branch_manager_authorized_test_view_add,
            hr=hr_test_view_add,
            email=email_test_view_add,
            remark=remark_test_view_add,
            status_of_this_record=status_of_this_record_test_view_add,
            password=password_test_view_add,
            main_language=main_language_test_view_add,
            user_phone=user_phone_test_view_add,
            home=home_test_view_add,
            office=office_test_view_add,
            cell=cell_test_view_add,
            facsimile=facsimile_test_view_add,
            telex=telex_test_view_add,
            time_zone_of_user=time_zone_of_user_test_view_add,
            thousand_separate_character_in_amount_field=thousand_separate_character_in_amount_field_test_view_add,
            decimal_separate_character_in_amount_field=decimal_separate_character_in_amount_field_test_view_add,
            date_format_for_short=date_format_for_short_test_view_add,
            long_date_format=long_date_format_test_view_add,
            time_format=time_format_test_view_add,
            expire_date_of_this_user=expire_date_of_this_user_test_view_add,
            id_of_policy_apply_for_this_user=id_of_policy_apply_for_this_user_test_view_add,
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

    def test_006_adm_user_profile_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.user_profile_update(
            user_code=user_code_test_update,
            old_user_id=old_user_id_test_update,
            user_name=user_name_test_update,
            login_name=login_name_test_update,
            branch_code=branch_code_test_update,
            department_name=department_name_test_update,
            cashier=cashier_test_update,
            officer=officer_test_update,
            chief_cashier=chief_cashier_test_update,
            operation_staff=operation_staff_test_update,
            dealer=dealer_test_update,
            inter_branch_user=inter_branch_user_test_update,
            branch_manager_authorized=branch_manager_authorized_test_update,
            hr=hr_test_update,
            email=email_test_update,
            remark=remark_test_update,
            status_of_this_record=status_of_this_record_test_update,
            password=password_test_update,
            main_language=main_language_test_update,
            user_phone=user_phone_test_update,
            home=home_test_update,
            office=office_test_update,
            cell=cell_test_update,
            facsimile=facsimile_test_update,
            telex=telex_test_update,
            time_zone_of_user=time_zone_of_user_test_update,
            thousand_separate_character_in_amount_field=thousand_separate_character_in_amount_field_test_update,
            decimal_separate_character_in_amount_field=decimal_separate_character_in_amount_field_test_update,
            date_format_for_short=date_format_for_short_test_update,
            long_date_format=long_date_format_test_update,
            time_format=time_format_test_update,
            expire_date_of_this_user=expire_date_of_this_user_test_update,
            id_of_policy_apply_for_this_user=id_of_policy_apply_for_this_user_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.user_profile_search_verify(
            user_code=value_login_name,
            user_name=user_name_test_add,
            login_name=value_login_name,
            branch_name=value_branch_name,
            department_name=department_name_test_add,
            status=status_of_this_record_test_add,
            is_online=value_is_online,
            email=email_test_add,
        )

    def test_007_adm_user_profile_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.user_profile_update_verify(
            transaction_number=transaction_number_update,
            user_code=user_code_test_update_verify,
            old_user_id=old_user_id_test_update_verify,
            user_name=user_name_test_update_verify,
            login_name=login_name_test_update_verify,
            branch_code=branch_code_test_update_verify,
            department_name=department_name_test_update_verify,
            cashier=cashier_test_update_verify,
            officer=officer_test_update_verify,
            chief_cashier=chief_cashier_test_update_verify,
            operation_staff=operation_staff_test_update_verify,
            dealer=dealer_test_update_verify,
            inter_branch_user=inter_branch_user_test_update_verify,
            branch_manager_authorized=branch_manager_authorized_test_update_verify,
            hr=hr_test_update_verify,
            email=email_test_update_verify,
            remark=remark_test_update_verify,
            status_of_this_record=status_of_this_record_test_update_verify,
            password=password_test_update_verify,
            main_language=main_language_test_update_verify,
            user_phone=user_phone_test_update_verify,
            home=home_test_update_verify,
            office=office_test_update_verify,
            cell=cell_test_update_verify,
            facsimile=facsimile_test_update_verify,
            telex=telex_test_update_verify,
            time_zone_of_user=time_zone_of_user_test_update_verify,
            thousand_separate_character_in_amount_field=thousand_separate_character_in_amount_field_test_update_verify,
            decimal_separate_character_in_amount_field=decimal_separate_character_in_amount_field_test_update_verify,
            date_format_for_short=date_format_for_short_test_update_verify,
            long_date_format=long_date_format_test_update_verify,
            time_format=time_format_test_update_verify,
            expire_date_of_this_user=expire_date_of_this_user_test_update_verify,
            id_of_policy_apply_for_this_user=id_of_policy_apply_for_this_user_test_update_verify,
        )

    def test_008_adm_user_profile_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.user_profile_search_verify(
            user_code=value_login_name,
            user_name=user_name_test_update,
            login_name=value_login_name,
            branch_name=value_branch_name_up,
            department_name=department_name_test_update,
            status=status_of_this_record_test_update,
            is_online=value_is_online,
            email=email_test_update,
        )

    def test_009_adm_user_profile_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.user_profile_view(
            user_code=user_code_test_view_update,
            old_user_id=old_user_id_test_view_update,
            user_name=user_name_test_view_update,
            login_name=login_name_test_view_update,
            branch_code=branch_code_test_view_update,
            department_name=department_name_test_view_update,
            cashier=cashier_test_view_update,
            officer=officer_test_view_update,
            chief_cashier=chief_cashier_test_view_update,
            operation_staff=operation_staff_test_view_update,
            dealer=dealer_test_view_update,
            inter_branch_user=inter_branch_user_test_view_update,
            branch_manager_authorized=branch_manager_authorized_test_view_update,
            hr=hr_test_view_update,
            email=email_test_view_update,
            remark=remark_test_view_update,
            status_of_this_record=status_of_this_record_test_view_update,
            password=password_test_view_update,
            main_language=main_language_test_view_update,
            user_phone=user_phone_test_view_update,
            home=home_test_view_update,
            office=office_test_view_update,
            cell=cell_test_view_update,
            facsimile=facsimile_test_view_update,
            telex=telex_test_view_update,
            time_zone_of_user=time_zone_of_user_test_view_update,
            thousand_separate_character_in_amount_field=thousand_separate_character_in_amount_field_test_view_update,
            decimal_separate_character_in_amount_field=decimal_separate_character_in_amount_field_test_view_update,
            date_format_for_short=date_format_for_short_test_view_update,
            long_date_format=long_date_format_test_view_update,
            time_format=time_format_test_view_update,
            expire_date_of_this_user=expire_date_of_this_user_test_view_update,
            id_of_policy_apply_for_this_user=id_of_policy_apply_for_this_user_test_view_update,
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

    def test_010_adm_user_profile_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.user_profile_delete(
            user_code=value_login_name,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.user_profile_search_verify(
            user_code=value_login_name,
            user_name=user_name_test_update,
            login_name=value_login_name,
            branch_name=value_branch_name_up,
            department_name=department_name_test_update,
            status=status_of_this_record_test_update,
            is_online=value_is_online,
            email=email_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_login_name,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_login_name,
            tran_name=tran_name_delete,
        )

    def test_011_adm_user_profile_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.user_profile_simple_search(value_login_name)
        self.assert_search_not_found()

if __name__ == '__main__': 
    webui_test.main()