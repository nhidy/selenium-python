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

random_num = f"{random.randint(5, 999)}"
date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

# data not change
value_iso_2_alpha = 'AB'
value_iso_3_alpha = 'ABC'
value_country_name = 'AUTO TEST Country'
value_country_name_1 = 'Country name 1'
value_country_name_2 = 'Country name 2'
value_country_name_3 = 'Country name 3'
value_country_short_name = 'AUTO'
value_short_name_1 = 'Short name 1'
value_short_name_2 = 'Short name 2'
value_short_name_3 = 'Short name 3'
value_currency_code = 'JPY'
value_main_language = 'Spanish'
value_region_of_country = 'Asia'
value_status_of_country = 'Normal'
value_order = random_num

# data test add
iso_2_alpha_test_add = value_iso_2_alpha
iso_3_alpha_test_add = value_iso_3_alpha
country_name_test_add = value_country_name
country_name_1_test_add = value_country_name_1
country_name_2_test_add = value_country_name_2
country_name_3_test_add = value_country_name_3
country_short_name_test_add = value_country_short_name
short_name_1_test_add = value_short_name_1
short_name_2_test_add = value_short_name_2
short_name_3_test_add = value_short_name_3
currency_code_test_add = value_currency_code
main_language_test_add = value_main_language
region_of_country_test_add = value_region_of_country
status_of_country_test_add = value_status_of_country
order_test_add = value_order

# data test update
iso_2_alpha_test_update = value_iso_2_alpha
iso_3_alpha_test_update = value_iso_3_alpha
country_name_test_update = value_country_name
country_name_1_test_update = 'Country name update'
country_name_2_test_update = value_country_name_2
country_name_3_test_update = value_country_name_3
country_short_name_test_update = value_country_short_name
short_name_1_test_update = value_short_name_1
short_name_2_test_update = value_short_name_2
short_name_3_test_update = 'Short name update'
currency_code_test_update = 'EUR'
main_language_test_update = 'French'
region_of_country_test_update = 'Europe'
status_of_country_test_update = 'Closed'
order_test_update = value_order


class CountryTest(FormAction):
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

    def test_001_country_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.country_add(
            iso_2_alpha = iso_2_alpha_test_add,
            iso_3_alpha = iso_3_alpha_test_add,
            country_name = country_name_test_add,
            country_name_1 = country_name_1_test_add,
            country_name_2 = country_name_2_test_add,
            country_name_3 = country_name_3_test_add,
            country_short_name = country_short_name_test_add,
            short_name_1 = short_name_1_test_add,
            short_name_2 = short_name_2_test_add,
            short_name_3 = short_name_3_test_add,
            currency_code = currency_code_test_add,
            main_language = main_language_test_add,
            region_of_country = region_of_country_test_add,
            status_of_country = status_of_country_test_add,
            order = order_test_add 
        )

    def test_002_country_view(self):
        self.country_view(
            iso_2_alpha = iso_2_alpha_test_add,
            iso_3_alpha = iso_3_alpha_test_add,
            country_name = country_name_test_add,
            country_name_1 = country_name_1_test_add,
            country_name_2 = country_name_2_test_add,
            country_name_3 = country_name_3_test_add,
            country_short_name = country_short_name_test_add,
            short_name_1 = short_name_1_test_add,
            short_name_2 = short_name_2_test_add,
            short_name_3 = short_name_3_test_add,
            currency_code = currency_code_test_add,
            main_language = main_language_test_add,
            region_of_country = region_of_country_test_add,
            status_of_country = status_of_country_test_add,
            order = order_test_add
        )

    def test_003_country_update(self):
        self.country_update(
            iso_2_alpha = iso_2_alpha_test_update,
            iso_3_alpha = iso_3_alpha_test_update,
            country_name = country_name_test_update,
            country_name_1 = country_name_1_test_update,
            country_name_2 = country_name_2_test_update,
            country_name_3 = country_name_3_test_update,
            country_short_name = country_short_name_test_update,
            short_name_1 = short_name_1_test_update,
            short_name_2 = short_name_2_test_update,
            short_name_3 = short_name_3_test_update,
            currency_code = currency_code_test_update,
            main_language = main_language_test_update,
            region_of_country = region_of_country_test_update,
            status_of_country = status_of_country_test_update,
            order = order_test_update
        )

    def test_004_country_delete(self):
        self.country_delete(
            iso_3_alpha = iso_3_alpha_test_add
        )

if __name__ == '__main__': 
    webui_test.main()