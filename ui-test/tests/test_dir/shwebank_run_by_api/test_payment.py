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

# data test payment
beneficiary_branch_test = '5'
sender_name_test = 'Sender name'
sender_id_test = 'Sender id'
receiver_name_test = 'Receiver name'
send_currency_test = 'MMK'
send_amount_test = '5,000,000.43'
# total_amount_payable_test = '5,000,200.43'
receive_amount_test = '5,000,000.43'
product_code_test = '61040101'
ordering_institution_test = 'Ordering Institution'
nostro_bank_test = '14'
receiver_id_test = 'Receiver id'
remitting_amount_test = '5,000,000.43'
beneficiary_bank_test = 'Beneficiary bank'
beneficiary_account_number_test = 'ABC753434'
sender_to_receiver_info_test = 'Sender info'
amount_before_fees_test = '5,000,000.54'

class PaymentTest(FormAction):
    def get_url(self):
        return RUN_ON_URL

    def data_begin(self):
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
        global gl_account_number_test
        gl_account_number_test = f'{branch_code}-1100601000000-01'

    def start_class(self):
        self.data_begin()

    def end_class(self):
        self.logout()

    def reset_browser(self):
        self.logout()
        self.restart_browser()
        self.data_begin()

# Check the data used for testing
    def test_000_check_test_data_must_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=gl_account_number_test
        )
        if self.check_customer_profile_not_exist(customer_code_personal):
            self.stop()
            self.fail()

    def test_001_pmt_oit_outward_internal_bank_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global pmt_oit_reference_number
        beneficiary_branch = beneficiary_branch_test
        product_code = None
        sender_name = sender_name_test
        sender_id = sender_id_test
        sender_address = None
        sender_phone = None
        sender_type = None
        receiver_name = receiver_name_test
        receiver_id = None
        receiver_address = None
        receiver_phone = None
        receiver_type = None
        country = None
        purpose = None
        sender_to_receiver_info = None
        test_key = None
        goods_type = None
        goods_list = None
        payment_by = None
        account_number = None
        cheque_no = None
        send_currency = send_currency_test
        send_amount = send_amount_test
        cross_rate = None
        description = None
        region = None
        reference_number = None
        total_amount_payable = None
        receive_currency = None
        receive_amount = receive_amount_test
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        pmt_oit_result = self.pmt_oit(
            beneficiary_branch=beneficiary_branch,
            product_code=product_code,
            sender_name=sender_name,
            sender_id=sender_id,
            sender_address=sender_address,
            sender_phone=sender_phone,
            sender_type=sender_type,
            receiver_name=receiver_name,
            receiver_id=receiver_id,
            receiver_address=receiver_address,
            receiver_phone=receiver_phone,
            receiver_type=receiver_type,
            country=country,
            purpose=purpose,
            sender_to_receiver_info=sender_to_receiver_info,
            test_key=test_key,
            goods_type=goods_type,
            goods_list=goods_list,
            payment_by=payment_by,
            account_number=account_number,
            cheque_no=cheque_no,
            send_currency=send_currency,
            send_amount=send_amount,
            cross_rate=cross_rate,
            description=description,
            region=region,
            reference_number=reference_number,
            total_amount_payable=total_amount_payable,
            receive_currency=receive_currency,
            receive_amount=receive_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=pmt_oit_result[0]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        pmt_oit_view_result = self.pmt_oit_view(
            transaction_references=transaction_references,
            beneficiary_branch=beneficiary_branch,
            product_code=product_code,
            sender_name=sender_name,
            sender_id=sender_id,
            sender_address=sender_address,
            sender_phone=sender_phone,
            sender_type=sender_type,
            receiver_name=receiver_name,
            receiver_id=receiver_id,
            receiver_address=receiver_address,
            receiver_phone=receiver_phone,
            receiver_type=receiver_type,
            country=country,
            purpose=purpose,
            sender_to_receiver_info=sender_to_receiver_info,
            test_key=test_key,
            goods_type=goods_type,
            goods_list=goods_list,
            payment_by=payment_by,
            account_number=account_number,
            cheque_no=cheque_no,
            send_currency=send_currency,
            send_amount=send_amount,
            cross_rate=cross_rate,
            description=description,
            region=region,
            reference_number=reference_number,
            total_amount_payable=total_amount_payable,
            receive_currency=receive_currency,
            receive_amount=receive_amount,
            expected_posting=expected_posting,
        )
        pmt_oit_reference_number=pmt_oit_view_result[1]

if __name__ == '__main__': 
    webui_test.main()