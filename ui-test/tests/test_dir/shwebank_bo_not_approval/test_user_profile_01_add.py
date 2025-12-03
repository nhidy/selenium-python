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

customer_code_personal = CUSTOMER_CODE

# data required
# user_name_test = None
# login_name_test = None
# branch_code_test = None
# department_name_test = None
# cashier_test = True
# officer_test = True
# chief_cashier_test = True
# operation_staff_test = True
# dealer_test = True
# inter_branch_user_test = True
# branch_manager_authorized_test = True
# hr_test = True
# # data optional
# email_test = None
# remark_test = None
# status_of_this_record_test = None
# password_test = None
# main_language_test = None
# user_phone_test = None
# home_test = None
# office_test = None
# cell_test = None
# facsimile_test = None
# telex_test = None
# time_zone_of_user_test = None
# thousand_separate_character_in_amount_field_test = None
# decimal_separate_character_in_amount_field_test = None
# date_format_for_short_test = None
# long_date_format_test = None
# time_format_test = None
# expire_date_of_this_user_test = None
# id_of_policy_apply_for_this_user_test = None

class UserProfileAddTest(FormAction):
    def get_url(self):
        return RUN_ON_URL

    def data_begin(self):
        global username_approve, password_approve, username_reverse, password_reverse, username, password
        username_approve = USERNAME_APPROVE
        password_approve = PASSWORD_APPROVE
        username_reverse = USERNAME_REVERSE
        password_reverse = PASSWORD_REVERSE
        username = USERNAME_LOGIN
        password = PASSWORD_LOGIN
        self.login(username, password, one_app=ONE_APP)
        global working_date, branch_code
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()

    def start_class(self):
        self.data_begin()

    def end_class(self):
        self.logout()

    def reset_browser(self):
        self.logout()
        self.restart_browser()
        self.data_begin()

    def test_001_user_profile_add_teller_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # data required
        user_name_teller = 'Auto Teller 003'
        login_name_teller = 'autoteller003'
        branch_code_teller_add = '003 - Bayint Naung Branch'
        department_name_teller_add = '003 - BYN'
        cashier_teller = True
        officer_teller = True
        if self.check_user_profile_not_exist(login_name_teller):
            user_profile_add_result = self.user_profile_add(
                user_name=user_name_teller,
                login_name=login_name_teller,
                branch_code=branch_code_teller_add,
                department_name=department_name_teller_add,
                cashier=cashier_teller,
                officer=officer_teller,
            )
            user_code_teller=user_profile_add_result[0]
            password_teller=user_profile_add_result[1]
            # os.environ.update("USER_CODE_TELLER", user_code_teller)
            # os.environ.update("PASSWORD_TELLER", password_teller)

    def test_002_user_profile_add_manager_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # data required
        user_name_manager = 'Auto Manager 003'
        login_name_manager = 'automanager003'
        branch_code_manager_add = '003 - Bayint Naung Branch'
        department_name_manager_add = '003 - BYN'
        chief_cashier_manager = True
        officer_manager = True
        if self.check_user_profile_not_exist(login_name_manager):
            user_profile_add_result = self.user_profile_add(
                user_name=user_name_manager,
                login_name=login_name_manager,
                branch_code=branch_code_manager_add,
                department_name=department_name_manager_add,
                chief_cashier=chief_cashier_manager,
                officer=officer_manager,
            )
            user_code_manager=user_profile_add_result[0]
            password_manager=user_profile_add_result[1]
            # os.environ.update("USER_CODE_MANAGER", user_code_manager)
            # os.environ.update("PASSWORD_MANAGER", password_manager)

    # def test_002_user_profile_view_teller_success(self):
    #     print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
    #     # data required
    #     user_name_teller = 'Auto Teller 003'
    #     login_name_teller = 'autoteller003'
    #     branch_code_teller_view = '003 - Bayint Naung Branch'
    #     department_teller_name_view = '003 - BYN'
    #     cashier_teller = True
    #     officer_teller = True
    #     self.user_profile_view(
    #         user_code=login_name_teller,
    #         user_name=user_name_teller,
    #         login_name=login_name_teller,
    #         branch_code=branch_code_teller_view,
    #         department_name=department_teller_name_view,
    #         cashier=cashier_teller,
    #         officer=officer_teller,
    #     )

if __name__ == '__main__': 
    webui_test.main()