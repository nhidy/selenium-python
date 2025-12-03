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

customer_code=customer_code_personal
customer_type='Single customer'
date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

class ChangeCustomerPhoneEmailAddressTest(FormAction):
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

# Check the data used for testing
    def test_000_01_check_test_data_must_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        if self.check_customer_profile_not_exist(customer_code_personal):
            self.stop()
            self.fail()

    def test_001_ctm_cpa_approve_later_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        home_01 = 'Legal address - Home'
        street_01 = 'Legal address - Street'
        ward_01 = 'Legal address - Ward'
        township_01 = 'Legal address - Township'
        province_01 = '11. Mon State'
        home_02 = 'Contact local address - Home'
        street_02 = 'Contact local address - Street'
        ward_02 = 'Contact local address - Ward'
        township_02 = 'Contact local address - Township'
        province_02 = '12. Rakhine State'
        home_phone = '0123xxxxxx'
        mobile_phone = '0909xxxxxx'
        email_address = 'abc123@jits.com.vn'
        description = None
        ctm_cpa_result = self.ctm_cpa(
            customer_code=customer_code_personal,
            home_01=home_01,
            street_01=street_01,
            ward_01=ward_01,
            township_01=township_01,
            province_01=province_01,
            home_02=home_02,
            street_02=street_02,
            ward_02=ward_02,
            township_02=township_02,
            province_02=province_02,
            home_phone=home_phone,
            mobile_phone=mobile_phone,
            email_address=email_address,
            approve_later='Y'
        )
        transaction_references=ctm_cpa_result[0]
        # view transaction before approve
        self.ctm_cpa_view(
            transaction_references=transaction_references,
            customer_code=customer_code_personal,
            home_01=home_01,
            street_01=street_01,
            ward_01=ward_01,
            township_01=township_01,
            province_01=province_01,
            home_02=home_02,
            street_02=street_02,
            ward_02=ward_02,
            township_02=township_02,
            province_02=province_02,
            home_phone=home_phone,
            mobile_phone=mobile_phone,
            email_address=email_address,
            description=description
        )
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username_approve,
            password=password_approve
        )
        # view transaction after approve
        self.ctm_cpa_view(
            transaction_references=transaction_references,
            customer_code=customer_code_personal,
            home_01=home_01,
            street_01=street_01,
            ward_01=ward_01,
            township_01=township_01,
            province_01=province_01,
            home_02=home_02,
            street_02=street_02,
            ward_02=ward_02,
            township_02=township_02,
            province_02=province_02,
            home_phone=home_phone,
            mobile_phone=mobile_phone,
            email_address=email_address,
            description=description
        )
        
    def test_002_ctm_cpa_approve_on_form_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        home_01 = 'Legal address - Home'
        street_01 = 'Legal address - Street'
        ward_01 = 'Legal address - Ward'
        township_01 = 'Legal address - Township'
        province_01 = '11. Mon State'
        home_02 = 'Contact local address - Home'
        street_02 = 'Contact local address - Street'
        ward_02 = 'Contact local address - Ward'
        township_02 = 'Contact local address - Township'
        province_02 = '12. Rakhine State'
        home_phone = '0123xxxxxx'
        mobile_phone = '0909xxxxxx'
        email_address = 'abc123@jits.com.vn'
        description = None
        ctm_cpa_result = self.ctm_cpa(
            customer_code=customer_code_personal,
            home_01=home_01,
            street_01=street_01,
            ward_01=ward_01,
            township_01=township_01,
            province_01=province_01,
            home_02=home_02,
            street_02=street_02,
            ward_02=ward_02,
            township_02=township_02,
            province_02=province_02,
            home_phone=home_phone,
            mobile_phone=mobile_phone,
            email_address=email_address,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        transaction_references=ctm_cpa_result[0]
        ctm_cpa_result = self.ctm_cpa_view(
            transaction_references=transaction_references,
            customer_code=customer_code_personal,
            home_01=home_01,
            street_01=street_01,
            ward_01=ward_01,
            township_01=township_01,
            province_01=province_01,
            home_02=home_02,
            street_02=street_02,
            ward_02=ward_02,
            township_02=township_02,
            province_02=province_02,
            home_phone=home_phone,
            mobile_phone=mobile_phone,
            email_address=email_address,
            description=description
        )

if __name__ == '__main__': 
    webui_test.main()