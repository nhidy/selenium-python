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

action_add ='ADM-Branch Profile-Add'
action_update ='ADM-Branch Profile-Update'
tran_name_delete = 'ADM_DELETE_BRANCH'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']
list_error_message_in_use = [f'ERROR: Branch is in use']

# data not change
value_branch_code = '555'
value_list_error_message = None

# data test add
branch_code_test_add = value_branch_code
old_branch_id_test_add = '666'
branch_name_test_add = f'AUTO TEST add {date_time}'
branch_address_test_add = 'No. 149 (C) Yarzadirit Tower, Room No. 8.G/9.G/10.G, Corner of Yarzadirit Road and Thanlyatsoon Road, Botahtaung Township, Yangon'
branch_type_test_add = 'Virtual'
branch_phone_test_add = '09-876-543-232'
home_test_add = '08-876-543-232'
office_test_add = '07-876-543-232'
cell_test_add = '06-876-543-232'
facsimile_test_add = '05-876-543-232'
telex_test_add = '04-876-543-232'
tax_code_test_add = '03-876-543-232'
base_currency_code_test_add = 'USD'
local_currency_code_test_add = 'EUR'
region_test_add = 'Mandalay'
bic_test_add = 'bic add'
domestic_bank_code_test_add = 'Domestic bank code add'
internal_code_test_add = 'Internal code add'
country_test_add = 'Afghanistan'
main_language_test_add = 'German'
time_zone_of_branch_test_add = '(GMT+07:00) Bangkok, Hanoi, Jakarta'
thousand_separate_character_test_add = '.'
decimal_separate_character_test_add = ','
date_format_for_short_test_add = 'M/d/yyyy'
long_date_format_test_add = 'MMMM dd, yyyy'
time_format_test_add = 'h:mm:ss tt'
online_test_add = 'No'
list_error_message_test_add = value_list_error_message

# data test add verify
branch_code_test_add_verify = branch_code_test_add
old_branch_id_test_add_verify = old_branch_id_test_add
branch_name_test_add_verify = branch_name_test_add
branch_address_test_add_verify = branch_address_test_add
branch_type_test_add_verify = branch_type_test_add
branch_phone_test_add_verify = branch_phone_test_add
home_test_add_verify = home_test_add
office_test_add_verify = office_test_add
cell_test_add_verify = cell_test_add
facsimile_test_add_verify = facsimile_test_add
telex_test_add_verify = telex_test_add
tax_code_test_add_verify = tax_code_test_add
base_currency_code_test_add_verify = base_currency_code_test_add
local_currency_code_test_add_verify = local_currency_code_test_add
region_test_add_verify = region_test_add
bic_test_add_verify = bic_test_add
domestic_bank_code_test_add_verify = domestic_bank_code_test_add
internal_code_test_add_verify = internal_code_test_add
country_test_add_verify = country_test_add
main_language_test_add_verify = main_language_test_add
time_zone_of_branch_test_add_verify = time_zone_of_branch_test_add
thousand_separate_character_test_add_verify = thousand_separate_character_test_add
decimal_separate_character_test_add_verify = decimal_separate_character_test_add
date_format_for_short_test_add_verify = date_format_for_short_test_add
long_date_format_test_add_verify = long_date_format_test_add
time_format_test_add_verify = time_format_test_add
online_test_add_verify = online_test_add

# data test view add
branch_code_test_view_add = branch_code_test_add
old_branch_id_test_view_add = old_branch_id_test_add
branch_name_test_view_add = branch_name_test_add
branch_address_test_view_add = branch_address_test_add
branch_phone_test_view_add = branch_phone_test_add
branch_type_test_view_add = branch_type_test_add
home_test_view_add = home_test_add
office_test_view_add = office_test_add
cell_test_view_add = cell_test_add
facsimile_test_view_add = facsimile_test_add
telex_test_view_add = telex_test_add
tax_code_test_view_add = tax_code_test_add
base_currency_code_test_view_add = base_currency_code_test_add
local_currency_code_test_view_add = local_currency_code_test_add
region_test_view_add = region_test_add
bic_test_view_add = bic_test_add
domestic_bank_code_test_view_add = domestic_bank_code_test_add
internal_code_test_view_add = internal_code_test_add
country_test_view_add = country_test_add
main_language_test_view_add = main_language_test_add
time_zone_of_branch_test_view_add = time_zone_of_branch_test_add
thousand_separate_character_test_view_add = thousand_separate_character_test_add
decimal_separate_character_test_view_add = decimal_separate_character_test_add
date_format_for_short_test_view_add = date_format_for_short_test_add
long_date_format_test_view_add = long_date_format_test_add
time_format_test_view_add = time_format_test_add
online_test_view_add = online_test_add

# data test update
branch_code_test_update = value_branch_code
old_branch_id_test_update = '777'
branch_name_test_update = f'AUTO TEST update {date_time}'
branch_address_test_update = 'update No. 149 (C) Yarzadirit Tower, Room No. 8.G/9.G/10.G, Corner of Yarzadirit Road and Thanlyatsoon Road, Botahtaung Township, Yangon'
branch_phone_test_update = '09-886-543-232'
branch_type_test_update = 'Sub-branch'
home_test_update = '08-886-543-232'
office_test_update = '07-886-543-232'
cell_test_update = '06-886-543-232'
facsimile_test_update = '05-886-543-232'
telex_test_update = '04-886-543-232'
tax_code_test_update = '03-886-543-232'
base_currency_code_test_update = 'MMK'
local_currency_code_test_update = 'SGD'
region_test_update = 'Mawlamyine'
bic_test_update = 'bic update'
domestic_bank_code_test_update = 'Domestic bank code update'
internal_code_test_update = 'Internal code update'
country_test_update = 'Albania'
main_language_test_update = 'English'
time_zone_of_branch_test_update = '(GMT+06:30) Yangon Myanmar'
thousand_separate_character_test_update = ','
decimal_separate_character_test_update = '.'
date_format_for_short_test_update = 'dd/MM/yyyy'
long_date_format_test_update = 'dddd, MMMM dd, yyyy'
time_format_test_update = 'hh:mm:ss'
online_test_update = 'Yes'
list_error_message_test_update = value_list_error_message

# data test update verify
branch_code_test_update_verify = branch_code_test_update
old_branch_id_test_update_verify = old_branch_id_test_update
branch_name_test_update_verify = branch_name_test_update
branch_address_test_update_verify = branch_address_test_update
branch_phone_test_update_verify = branch_phone_test_update
branch_type_test_update_verify = branch_type_test_update
home_test_update_verify = home_test_update
office_test_update_verify = office_test_update
cell_test_update_verify = cell_test_update
facsimile_test_update_verify = facsimile_test_update
telex_test_update_verify = telex_test_update
tax_code_test_update_verify = tax_code_test_update
base_currency_code_test_update_verify = base_currency_code_test_update
local_currency_code_test_update_verify = local_currency_code_test_update
region_test_update_verify = region_test_update
bic_test_update_verify = bic_test_update
domestic_bank_code_test_update_verify = domestic_bank_code_test_update
internal_code_test_update_verify = internal_code_test_update
country_test_update_verify = country_test_update
main_language_test_update_verify = main_language_test_update
time_zone_of_branch_test_update_verify = time_zone_of_branch_test_update
thousand_separate_character_test_update_verify = thousand_separate_character_test_update
decimal_separate_character_test_update_verify = decimal_separate_character_test_update
date_format_for_short_test_update_verify = date_format_for_short_test_update
long_date_format_test_update_verify = long_date_format_test_update
time_format_test_update_verify = time_format_test_update
online_test_update_verify = online_test_update

# data test view update
branch_code_test_view_update = branch_code_test_update
old_branch_id_test_view_update = old_branch_id_test_update
branch_name_test_view_update = branch_name_test_update
branch_address_test_view_update = branch_address_test_update
branch_phone_test_view_update = branch_phone_test_update
branch_type_test_view_update = branch_type_test_update
home_test_view_update = home_test_update
office_test_view_update = office_test_update
cell_test_view_update = cell_test_update
facsimile_test_view_update = facsimile_test_update
telex_test_view_update = telex_test_update
tax_code_test_view_update = tax_code_test_update
base_currency_code_test_view_update = base_currency_code_test_update
local_currency_code_test_view_update = local_currency_code_test_update
region_test_view_update = region_test_update
bic_test_view_update = bic_test_update
domestic_bank_code_test_view_update = domestic_bank_code_test_update
internal_code_test_view_update = internal_code_test_update
country_test_view_update = country_test_update
main_language_test_view_update = main_language_test_update
time_zone_of_branch_test_view_update = time_zone_of_branch_test_update
thousand_separate_character_test_view_update = thousand_separate_character_test_update
decimal_separate_character_test_view_update = decimal_separate_character_test_update
date_format_for_short_test_view_update = date_format_for_short_test_update
long_date_format_test_view_update = long_date_format_test_update
time_format_test_view_update = time_format_test_update
online_test_view_update = online_test_update

# data not change for department and user
department_code_in_use = '66666'
department_name_in_use = f'AUTO TEST add {date_time}'
user_name_in_use = f'AUTO TEST add {date_time}'
login_name_in_use = 'autouser66'
branch_code_in_use = f'{value_branch_code} - {branch_name_test_update}'

class BranchProfileTest(FormAction):
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
    def test_001_adm_branch_profile_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.branch_profile_add(
            branch_code=branch_code_test_add,
            old_branch_id=old_branch_id_test_add,
            branch_name=branch_name_test_add,
            branch_address=branch_address_test_add,
            branch_type=branch_type_test_add,
            branch_phone=branch_phone_test_add,
            home=home_test_add,
            office=office_test_add,
            cell=cell_test_add,
            facsimile=facsimile_test_add,
            telex=telex_test_add,
            tax_code=tax_code_test_add,
            base_currency_code=base_currency_code_test_add,
            local_currency_code=local_currency_code_test_add,
            region=region_test_add,
            bic=bic_test_add,
            domestic_bank_code=domestic_bank_code_test_add,
            internal_code=internal_code_test_add,
            country=country_test_add,
            main_language=main_language_test_add,
            time_zone_of_branch=time_zone_of_branch_test_add,
            thousand_separate_character=thousand_separate_character_test_add,
            decimal_separate_character=decimal_separate_character_test_add,
            date_format_for_short=date_format_for_short_test_add,
            long_date_format=long_date_format_test_add,
            time_format=time_format_test_add,
            online=online_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.branch_profile_simple_search(value_branch_code)
        self.assert_search_not_found()

    def test_002_adm_branch_profile_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.branch_profile_add_verify(
            transaction_number=transaction_number_add,
            branch_code=branch_code_test_add_verify,
            old_branch_id=old_branch_id_test_add_verify,
            branch_name=branch_name_test_add_verify,
            branch_address=branch_address_test_add_verify,
            branch_type=branch_type_test_add_verify,
            branch_phone=branch_phone_test_add_verify,
            home=home_test_add_verify,
            office=office_test_add_verify,
            cell=cell_test_add_verify,
            facsimile=facsimile_test_add_verify,
            telex=telex_test_add_verify,
            tax_code=tax_code_test_add_verify,
            base_currency_code=base_currency_code_test_add_verify,
            local_currency_code=local_currency_code_test_add_verify,
            region=region_test_add_verify,
            bic=bic_test_add_verify,
            domestic_bank_code=domestic_bank_code_test_add_verify,
            internal_code=internal_code_test_add_verify,
            country=country_test_add_verify,
            main_language=main_language_test_add_verify,
            time_zone_of_branch=time_zone_of_branch_test_add_verify,
            thousand_separate_character=thousand_separate_character_test_add_verify,
            decimal_separate_character=decimal_separate_character_test_add_verify,
            date_format_for_short=date_format_for_short_test_add_verify,
            long_date_format=long_date_format_test_add_verify,
            time_format=time_format_test_add_verify,
            online=online_test_add_verify,
        )

    def test_003_adm_branch_profile_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.branch_profile_search_verify(
            branch_code=value_branch_code,
            branch_name=branch_name_test_add,
            address=branch_address_test_add,
            base_currency_code=base_currency_code_test_add,
            online_status=online_test_add,
            branch_type=branch_type_test_add,
        )

    def test_004_adm_branch_profile_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.branch_profile_view(
            branch_code=branch_code_test_view_add,
            old_branch_id=old_branch_id_test_view_add,
            branch_name=branch_name_test_view_add,
            branch_address=branch_address_test_view_add,
            branch_phone=branch_phone_test_view_add,
            branch_type=branch_type_test_view_add,
            home=home_test_view_add,
            office=office_test_view_add,
            cell=cell_test_view_add,
            facsimile=facsimile_test_view_add,
            telex=telex_test_view_add,
            tax_code=tax_code_test_view_add,
            base_currency_code=base_currency_code_test_view_add,
            local_currency_code=local_currency_code_test_view_add,
            region=region_test_view_add,
            bic=bic_test_view_add,
            domestic_bank_code=domestic_bank_code_test_view_add,
            internal_code=internal_code_test_view_add,
            country=country_test_view_add,
            main_language=main_language_test_view_add,
            time_zone_of_branch=time_zone_of_branch_test_view_add,
            thousand_separate_character=thousand_separate_character_test_view_add,
            decimal_separate_character=decimal_separate_character_test_view_add,
            date_format_for_short=date_format_for_short_test_view_add,
            long_date_format=long_date_format_test_view_add,
            time_format=time_format_test_view_add,
            online=online_test_view_add,
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

    def test_006_adm_branch_profile_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.branch_profile_update(
            branch_code=branch_code_test_update,
            old_branch_id=old_branch_id_test_update,
            branch_name=branch_name_test_update,
            branch_address=branch_address_test_update,
            branch_phone=branch_phone_test_update,
            branch_type=branch_type_test_update,
            home=home_test_update,
            office=office_test_update,
            cell=cell_test_update,
            facsimile=facsimile_test_update,
            telex=telex_test_update,
            tax_code=tax_code_test_update,
            base_currency_code=base_currency_code_test_update,
            local_currency_code=local_currency_code_test_update,
            region=region_test_update,
            bic=bic_test_update,
            domestic_bank_code=domestic_bank_code_test_update,
            internal_code=internal_code_test_update,
            country=country_test_update,
            main_language=main_language_test_update,
            time_zone_of_branch=time_zone_of_branch_test_update,
            thousand_separate_character=thousand_separate_character_test_update,
            decimal_separate_character=decimal_separate_character_test_update,
            date_format_for_short=date_format_for_short_test_update,
            long_date_format=long_date_format_test_update,
            time_format=time_format_test_update,
            online=online_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.branch_profile_search_verify(
            branch_code=value_branch_code,
            branch_name=branch_name_test_add,
            address=branch_address_test_add,
            base_currency_code=base_currency_code_test_add,
            online_status=online_test_add,
            branch_type=branch_type_test_add,
        )

    def test_007_adm_branch_profile_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.branch_profile_update_verify(
            transaction_number=transaction_number_update,
            branch_code=branch_code_test_update_verify,
            old_branch_id=old_branch_id_test_update_verify,
            branch_name=branch_name_test_update_verify,
            branch_address=branch_address_test_update_verify,
            branch_phone=branch_phone_test_update_verify,
            branch_type=branch_type_test_update_verify,
            home=home_test_update_verify,
            office=office_test_update_verify,
            cell=cell_test_update_verify,
            facsimile=facsimile_test_update_verify,
            telex=telex_test_update_verify,
            tax_code=tax_code_test_update_verify,
            base_currency_code=base_currency_code_test_update_verify,
            local_currency_code=local_currency_code_test_update_verify,
            region=region_test_update_verify,
            bic=bic_test_update_verify,
            domestic_bank_code=domestic_bank_code_test_update_verify,
            internal_code=internal_code_test_update_verify,
            country=country_test_update_verify,
            main_language=main_language_test_update_verify,
            time_zone_of_branch=time_zone_of_branch_test_update_verify,
            thousand_separate_character=thousand_separate_character_test_update_verify,
            decimal_separate_character=decimal_separate_character_test_update_verify,
            date_format_for_short=date_format_for_short_test_update_verify,
            long_date_format=long_date_format_test_update_verify,
            time_format=time_format_test_update_verify,
            online=online_test_update_verify,
        )

    def test_008_adm_branch_profile_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.branch_profile_search_verify(
            branch_code=value_branch_code,
            branch_name=branch_name_test_update,
            address=branch_address_test_update,
            base_currency_code=base_currency_code_test_update,
            online_status=online_test_update,
            branch_type=branch_type_test_update,
        )

    def test_009_adm_branch_profile_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.branch_profile_view(
            branch_code=branch_code_test_view_update,
            old_branch_id=old_branch_id_test_view_update,
            branch_name=branch_name_test_view_update,
            branch_address=branch_address_test_view_update,
            branch_phone=branch_phone_test_view_update,
            branch_type=branch_type_test_view_update,
            home=home_test_view_update,
            office=office_test_view_update,
            cell=cell_test_view_update,
            facsimile=facsimile_test_view_update,
            telex=telex_test_view_update,
            tax_code=tax_code_test_view_update,
            base_currency_code=base_currency_code_test_view_update,
            local_currency_code=local_currency_code_test_view_update,
            region=region_test_view_update,
            bic=bic_test_view_update,
            domestic_bank_code=domestic_bank_code_test_view_update,
            internal_code=internal_code_test_view_update,
            country=country_test_view_update,
            main_language=main_language_test_view_update,
            time_zone_of_branch=time_zone_of_branch_test_view_update,
            thousand_separate_character=thousand_separate_character_test_view_update,
            decimal_separate_character=decimal_separate_character_test_view_update,
            date_format_for_short=date_format_for_short_test_view_update,
            long_date_format=long_date_format_test_view_update,
            time_format=time_format_test_view_update,
            online=online_test_view_update,
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

    def test_010_adm_branch_profile_in_use_add_department_and_user(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.department_profile_add(
            department_code=department_code_in_use,
            department_name=department_name_in_use,
            branch_code=branch_code_in_use,
        )
        transaction_number=self.get_transaction_number()
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        self.user_profile_add(
            user_name=user_name_in_use,
            login_name=login_name_in_use,
            branch_code=branch_code_in_use,
        )
        transaction_number=self.get_transaction_number()
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )

    def test_011_adm_branch_profile_delete_item_in_use_01_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.branch_profile_delete(
            branch_code=value_branch_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.branch_profile_search_verify(
            branch_code=value_branch_code,
            branch_name=branch_name_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_branch_code,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_branch_code,
            tran_name=tran_name_delete,
            list_error_message=list_error_message_in_use,
        )

    def test_011_adm_branch_profile_delete_item_in_use_02_reject(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # reject delete
        self.bo_approval_reject(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_branch_code,
            tran_name=tran_name_delete,
        )
        # search master
        self.branch_profile_search_verify(
            branch_code=value_branch_code,
        )

    def test_012_adm_branch_profile_in_use_delete_department_and_user(self):
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
        # Delete department
        self.department_profile_delete(
            department_code=department_code_in_use,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.department_profile_search_verify(
            department_code=department_code_in_use,
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=department_code_in_use,
            tran_name='ADM_DELETE_DEPARTMENT',
        )
        self.department_profile_simple_search(department_code_in_use)
        self.assert_search_not_found()

    def test_013_adm_branch_profile_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.branch_profile_delete(
            branch_code=value_branch_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.branch_profile_search_verify(
            branch_code=value_branch_code,
            branch_name=branch_name_test_update,
            address=branch_address_test_update,
            base_currency_code=base_currency_code_test_update,
            online_status=online_test_update,
            branch_type=branch_type_test_update,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_branch_code,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_branch_code,
            tran_name=tran_name_delete,
        )

    def test_014_adm_branch_profile_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.branch_profile_simple_search(value_branch_code)
        self.assert_search_not_found()

if __name__ == '__main__':
    webui_test.main()