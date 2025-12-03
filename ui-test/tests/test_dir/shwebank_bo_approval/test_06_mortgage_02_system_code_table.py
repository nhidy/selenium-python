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

tran_name_delete = 'MTG_DELETE_CODE_LIST'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']
module_code = 'MTG'

# data not change
value_code_id = 'AUTO01'
value_code_name = 'AUTO'
value_english = 'Test auto English'
value_vietnamese = 'Test auto Vietnamese'
value_laothian = 'Test auto Laothian'
value_khmer = 'Test auto Khmer'
value_myanmar = 'Test auto Myanmar'
value_code_of_group = 'MORTGAGE'
value_code_index = '1'
value_code_value = '01'
value_field_link = None
value_is_visible = True
value_list_error_message = None

# data test add
code_id_test_add = value_code_id
code_name_test_add = value_code_name
caption_of_code_test_add = f'AUTO TEST add {date_time}'
english_test_add = value_english
vietnamese_test_add = value_vietnamese
laothian_test_add = value_laothian
khmer_test_add = value_khmer
myanmar_test_add = value_myanmar
code_of_group_test_add = value_code_of_group
code_index_test_add = value_code_index
code_value_test_add = value_code_value
field_link_test_add = value_field_link
is_visible_test_add = value_is_visible
list_error_message_test_add = value_list_error_message

# data test add verify
code_id_test_add_verify = value_code_id
code_name_test_add_verify = value_code_name
caption_of_code_test_add_verify = caption_of_code_test_add
english_test_add_verify = value_english
vietnamese_test_add_verify = value_vietnamese
laothian_test_add_verify = value_laothian
khmer_test_add_verify = value_khmer
myanmar_test_add_verify = value_myanmar
code_of_group_test_add_verify = value_code_of_group
code_index_test_add_verify = value_code_index
code_value_test_add_verify = value_code_value
field_link_test_add_verify = value_field_link
is_visible_test_add_verify = value_is_visible

# data test view add
code_id_test_view_add = value_code_id
code_name_test_view_add = value_code_name
caption_of_code_test_view_add = caption_of_code_test_add
english_test_view_add = value_english
vietnamese_test_view_add = value_vietnamese
laothian_test_view_add = value_laothian
khmer_test_view_add = value_khmer
myanmar_test_view_add = value_myanmar
code_of_group_test_view_add = value_code_of_group
code_index_test_view_add = value_code_index
code_value_test_view_add = value_code_value
field_link_test_view_add = value_field_link
is_visible_test_view_add = value_is_visible

# data test update
code_id_test_update = value_code_id
code_name_test_update = value_code_name
caption_of_code_test_update = f'AUTO TEST update {date_time}'
english_test_update = 'Test auto update English'
vietnamese_test_update = 'Test auto update Vietnamese'
laothian_test_update = 'Test auto update Laothian'
khmer_test_update = 'Test auto update Khmer'
myanmar_test_update = 'Test auto update Myanmar'
code_of_group_test_update = value_code_of_group
code_index_test_update = '3'
code_value_test_update = '02'
field_link_test_update = value_field_link
is_visible_test_update = False
list_error_message_test_update = value_list_error_message

# data test update verify
code_id_test_update_verify = value_code_id
code_name_test_update_verify = value_code_name
caption_of_code_test_update_verify = caption_of_code_test_update
english_test_update_verify = english_test_update
vietnamese_test_update_verify = vietnamese_test_update
laothian_test_update_verify = laothian_test_update
khmer_test_update_verify = khmer_test_update
myanmar_test_update_verify = myanmar_test_update
code_of_group_test_update_verify = value_code_of_group
code_index_test_update_verify = code_index_test_update
code_value_test_update_verify = code_value_test_update
field_link_test_update_verify = value_field_link
is_visible_test_update_verify = is_visible_test_update

# data test view update
code_id_test_view_update = value_code_id
code_name_test_view_update = value_code_name
caption_of_code_test_view_update = caption_of_code_test_update
english_test_view_update = english_test_update
vietnamese_test_view_update = vietnamese_test_update
laothian_test_view_update = laothian_test_update
khmer_test_view_update = khmer_test_update
myanmar_test_view_update = myanmar_test_update
code_of_group_test_view_update = value_code_of_group
code_index_test_view_update = code_index_test_update
code_value_test_view_update = code_value_test_update
field_link_test_view_update = value_field_link
is_visible_test_view_update = is_visible_test_update

class MortgageSystemCodeTableTest(FormAction):
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
        global working_date, branch_code
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()
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

# MTG-System Code Table
    def test_001_mtg_system_code_table_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.mortgage_system_code_table_add(
            code_id=code_id_test_add,
            code_name=code_name_test_add,
            caption_of_code=caption_of_code_test_add,
            english=english_test_add,
            vietnamese=vietnamese_test_add,
            laothian=laothian_test_add,
            khmer=khmer_test_add,
            myanmar=myanmar_test_add,
            code_of_group=code_of_group_test_add,
            code_index=code_index_test_add,
            code_value=code_value_test_add,
            field_link=field_link_test_add,
            is_visible=is_visible_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.mortgage_system_code_table_simple_search(value_code_id)
        self.assert_search_not_found()

    def test_002_mtg_system_code_table_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.mortgage_system_code_table_add_verify(
            transaction_number=transaction_number_add,
            code_id=code_id_test_add_verify,
            code_name=code_name_test_add_verify,
            caption_of_code=caption_of_code_test_add_verify,
            english=english_test_add_verify,
            vietnamese=vietnamese_test_add_verify,
            laothian=laothian_test_add_verify,
            khmer=khmer_test_add_verify,
            myanmar=myanmar_test_add_verify,
            code_of_group=code_of_group_test_add_verify,
            code_index=code_index_test_add_verify,
            code_value=code_value_test_add_verify,
            field_link=field_link_test_add_verify,
            is_visible=is_visible_test_add_verify,
        )

    def test_003_mtg_system_code_table_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.mortgage_system_code_table_search_verify(
            code_id=value_code_id,
            code_name=value_code_name,
            caption=None,
            index=None,
        )

    def test_004_mtg_system_code_table_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.mortgage_system_code_table_view(
            code_id=code_id_test_view_add,
            code_name=code_name_test_view_add,
            caption_of_code=caption_of_code_test_view_add,
            english=english_test_view_add,
            vietnamese=vietnamese_test_view_add,
            laothian=laothian_test_view_add,
            khmer=khmer_test_view_add,
            myanmar=myanmar_test_view_add,
            code_of_group=code_of_group_test_view_add,
            code_index=code_index_test_view_add,
            code_value=code_value_test_view_add,
            field_link=field_link_test_view_add,
            is_visible=is_visible_test_view_add,
        )

    def test_005_mtg_system_code_table_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.mortgage_system_code_table_update(
            code_id=code_id_test_update,
            code_name=code_name_test_update,
            caption_of_code=caption_of_code_test_update,
            english=english_test_update,
            vietnamese=vietnamese_test_update,
            laothian=laothian_test_update,
            khmer=khmer_test_update,
            myanmar=myanmar_test_update,
            code_of_group=code_of_group_test_update,
            code_index=code_index_test_update,
            code_value=code_value_test_update,
            field_link=field_link_test_update,
            is_visible=is_visible_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.mortgage_system_code_table_search_verify(
            code_id=value_code_id,
            code_name=value_code_name,
            caption=None,
            index=None,
        )

    def test_006_mtg_system_code_table_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.mortgage_system_code_table_update_verify(
            transaction_number=transaction_number_update,
            code_id=code_id_test_update_verify,
            code_name=code_name_test_update_verify,
            caption_of_code=caption_of_code_test_update_verify,
            english=english_test_update_verify,
            vietnamese=vietnamese_test_update_verify,
            laothian=laothian_test_update_verify,
            khmer=khmer_test_update_verify,
            myanmar=myanmar_test_update_verify,
            code_of_group=code_of_group_test_update_verify,
            code_index=code_index_test_update_verify,
            code_value=code_value_test_update_verify,
            field_link=field_link_test_update_verify,
            is_visible=is_visible_test_update_verify,
        )

    def test_007_mtg_system_code_table_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve,
            password=password_approve,
        )
        # search master
        self.mortgage_system_code_table_search_verify(
            code_id=value_code_id,
            code_name=value_code_name,
            caption=None,
            index=None,
        )

    def test_008_mtg_system_code_table_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.mortgage_system_code_table_view(
            code_id=code_id_test_view_update,
            code_name=code_name_test_view_update,
            caption_of_code=caption_of_code_test_view_update,
            english=english_test_view_update,
            vietnamese=vietnamese_test_view_update,
            laothian=laothian_test_view_update,
            khmer=khmer_test_view_update,
            myanmar=myanmar_test_view_update,
            code_of_group=code_of_group_test_view_update,
            code_index=code_index_test_view_update,
            code_value=code_value_test_view_update,
            field_link=field_link_test_view_update,
            is_visible=is_visible_test_view_update,
        )

    def test_009_mtg_system_code_table_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.mortgage_system_code_table_delete(
            code_id=value_code_id,
            code_name=value_code_name,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.mortgage_system_code_table_search_verify(
            code_id=value_code_id,
            code_name=value_code_name,
            caption=None,
            index=None,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=f'{value_code_id} | {module_code} | {value_code_name}',
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve,
            password=password_approve,
            master_code=f'{value_code_id} | {module_code} | {value_code_name}',
            tran_name=tran_name_delete,
        )

    def test_010_mtg_system_code_table_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.mortgage_system_code_table_simple_search(value_code_id)
        self.assert_search_not_found()

if __name__ == '__main__': 
    webui_test.main()