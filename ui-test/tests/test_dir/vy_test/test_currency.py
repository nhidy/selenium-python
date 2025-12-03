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

random_num1 = f"{random.randint(29, 98)}"
random_num2 = f"{random.randint(100, 999)}"
random_num3 = f"{random.randint(29, 999)}"
date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# data not change
value_currency_code = 'DEF'
value_short_currency_code = random_num1
value_currency_number = random_num2
value_currency_name_1 = 'Currency name 1'
value_currency_name_2 = 'Currency name 2'
value_currency_name_3 = 'Currency name 3'
value_master_name_1 = 'Master name 1'
value_master_name_2 = 'Master name 2'
value_master_name_3 = 'Master name 3'
value_decimal_name_1 = 'Decimal name 1'
value_decimal_name_2 = 'Decimal name 2'
value_decimal_name_3 = 'Decimal name 3'
value_decimal_digits = '2'
value_rounding_digits = '2'
value_status_of_currency = None
value_order = random_num3

# data test add
currency_code_test_add = value_currency_code
short_currency_code_test_add = value_short_currency_code
currency_number_test_add = value_currency_number
currency_name_1_test_add = value_currency_name_1
currency_name_2_test_add = value_currency_name_2
currency_name_3_test_add = value_currency_name_3
master_name_1_test_add = value_master_name_1
master_name_2_test_add = value_master_name_2
master_name_3_test_add = value_master_name_3
decimal_name_1_test_add = value_decimal_name_1
decimal_name_2_test_add = value_decimal_name_2
decimal_name_3_test_add = value_decimal_name_3
decimal_digits_test_add = value_decimal_digits
rounding_digits_test_add = value_rounding_digits
status_of_currency_test_add = value_status_of_currency
order_test_add = value_order

# data test update
currency_code_test_update = value_currency_code
short_currency_code_test_update = value_short_currency_code
currency_number_test_update = value_currency_number
currency_name_1_test_update = 'Currency name update'
currency_name_2_test_update = value_currency_name_2
currency_name_3_test_update = value_currency_name_3
master_name_1_test_update = value_master_name_1
master_name_2_test_update = 'Master name update'
master_name_3_test_update = value_master_name_3
decimal_name_1_test_update = value_decimal_name_1
decimal_name_2_test_update = value_decimal_name_2
decimal_name_3_test_update = 'Decimal name update'
decimal_digits_test_update = value_decimal_digits
rounding_digits_test_update = value_rounding_digits
status_of_currency_test_update = 'Not use'
order_test_update = value_order

class CurrencyTest(FormAction):
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

    def test_001_currency_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.currency_add(
            currency_code = currency_code_test_add,
            short_currency_code = short_currency_code_test_add,
            currency_number = currency_number_test_add,
            currency_name_1 = currency_name_1_test_add,
            currency_name_2 = currency_name_2_test_add,
            currency_name_3 = currency_name_3_test_add,
            master_name_1 = master_name_1_test_add,
            master_name_2 = master_name_2_test_add,
            master_name_3 = master_name_3_test_add,
            decimal_name_1 = decimal_name_1_test_add,
            decimal_name_2 = decimal_name_2_test_add,
            decimal_name_3 = decimal_name_3_test_add,
            decimal_digits = decimal_digits_test_add,
            rounding_digits = rounding_digits_test_add,
            status_of_currency = status_of_currency_test_add,
            order = order_test_add 
        )

    def test_002_currency_view(self):
        self.currency_view(
            currency_code = currency_code_test_add,
            short_currency_code = short_currency_code_test_add,
            currency_number = currency_number_test_add,
            currency_name_1 = currency_name_1_test_add,
            currency_name_2 = currency_name_2_test_add,
            currency_name_3 = currency_name_3_test_add,
            master_name_1 = master_name_1_test_add,
            master_name_2 = master_name_2_test_add,
            master_name_3 = master_name_3_test_add,
            decimal_name_1 = decimal_name_1_test_add,
            decimal_name_2 = decimal_name_2_test_add,
            decimal_name_3 = decimal_name_3_test_add,
            decimal_digits = decimal_digits_test_add,
            rounding_digits = rounding_digits_test_add,
            status_of_currency = status_of_currency_test_add,
            order = order_test_add 
        )

    def test_003_currency_update(self):
        self.currency_update(
            currency_code = currency_code_test_update,
            short_currency_code = short_currency_code_test_update,
            currency_number = currency_number_test_update,
            currency_name_1 = currency_name_1_test_update,
            currency_name_2 = currency_name_2_test_update,
            currency_name_3 = currency_name_3_test_update,
            master_name_1 = master_name_1_test_update,
            master_name_2 = master_name_2_test_update,
            master_name_3 = master_name_3_test_update,
            decimal_name_1 = decimal_name_1_test_update,
            decimal_name_2 = decimal_name_2_test_update,
            decimal_name_3 = decimal_name_3_test_update,
            decimal_digits = decimal_digits_test_update,
            rounding_digits = rounding_digits_test_update,
            status_of_currency = status_of_currency_test_update,
            order = order_test_update
        )

    def test_004_currency_delete(self):
        self.currency_delete(
            currency_code = currency_code_test_add
        )

if __name__ == '__main__': 
    webui_test.main()