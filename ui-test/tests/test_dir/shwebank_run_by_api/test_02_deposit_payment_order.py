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

# data test for 'Payment Order'
stock_type_po = 'Payment Order'
stock_prefix_po = 'PO'
number_of_leaves_po = '1'
number_of_book_po = '2'
list_error_message = [
    'CannotBeReversed: DPT_SRG can not be reversed'
]
# data test for payment order
expired_date_test = '25/06/2026'
issuing_name_test = 'Issuing name'
issuer_id_number_test = 'issuer-id-number'
issuer_contact_number_test = 'issuer-contact-number'
amount_test = '5,600,450.67'
currency_test = 'MMK'
beneficiary_name_test = 'Beneficiary name'
beneficiary_id_number_test = 'beneficiary-id-number'
beneficiary_contact_number_test = 'beneficiary-contact-number'
beneficiary_address_test = 'beneficiary-address'
purpose_test = 'purpose'
method_cash = 'Cash'
method_deposit = 'Deposit'
method_accounting = 'Accounting'

class DepositPaymentOrderTest(FormAction):
    def get_url(self):
        return RUN_ON_URL

    def data_begin(self):
        global username_approve, password_approve, username_reverse, password_reverse, username_login, password_login
        username_approve = USERNAME_APPROVE
        password_approve = PASSWORD_APPROVE
        username_reverse = USERNAME_REVERSE
        password_reverse = PASSWORD_REVERSE
        username_login = USERNAME_LOGIN
        password_login = PASSWORD_LOGIN
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

# Check the data used for testing
    def test_000_check_test_data_must_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=gl_account_number
        )

# PAYMENT ORDER
    def test_001_payment_order_01_dpt_srg_stock_registration_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global from_serial_po, to_serial_po
        generated_number = self.gen_serial_number(stock_prefix_po, stock_type_po, 1)
        print(f'generated_number: {generated_number}')
        module = None
        stock_type = stock_type_po
        from_serial = generated_number[0]
        to_serial = generated_number[1]
        number_of_leaves = number_of_leaves_po
        number_of_leaves_update = None
        number_of_book = number_of_book_po
        number_of_book_update = None
        description = None
        stock_prefix = stock_prefix_po
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        dpt_srg_result = self.dpt_srg(
            module=module,
            stock_type=stock_type,
            from_serial=from_serial,
            to_serial=to_serial,
            number_of_leaves=number_of_leaves,
            number_of_leaves_update=number_of_leaves_update,
            number_of_book=number_of_book,
            number_of_book_update=number_of_book_update,
            description=description,
            stock_prefix=stock_prefix,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=dpt_srg_result[0]
        from_serial_po=dpt_srg_result[1]
        to_serial_po=dpt_srg_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.dpt_srg_view(
            transaction_references=transaction_references,
            module=module,
            stock_type=stock_type,
            from_serial=from_serial,
            to_serial=to_serial,
            number_of_leaves=number_of_leaves,
            number_of_leaves_update=number_of_leaves_update,
            number_of_book=number_of_book,
            number_of_book_update=number_of_book_update,
            description=description,
            stock_prefix=stock_prefix,
            expected_posting=expected_posting,
        )

    def test_002_payment_order_03_dpt_sat_stock_assign_to_staff_success_no_need_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        stock_type = stock_type_po
        from_serial = from_serial_po
        to_serial = to_serial_po
        assigned_staff_code = username_login

        dpt_sat_result = self.dpt_sat(
            stock_type=stock_type,
            from_serial=from_serial,
            to_serial=to_serial,
            assigned_staff_code=assigned_staff_code,
        )
        transaction_references=dpt_sat_result[0]
        from_serial_out=dpt_sat_result[1]
        to_serial_out=dpt_sat_result[2]
        self.dpt_sat_view(
            transaction_references=transaction_references,
            stock_type=stock_type,
            from_serial=from_serial,
            to_serial=to_serial,
            assigned_staff_code=assigned_staff_code,
        )

    def test_003_payment_order_03_dpt_ccr_stock_confirm_received_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        stock_type = stock_type_po
        from_serial = from_serial_po
        to_serial = to_serial_po
        description = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        dpt_ccr_result = self.dpt_ccr(
            stock_type=stock_type,
            from_serial=from_serial,
            to_serial=to_serial,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=dpt_ccr_result[0]
        from_serial_out=dpt_ccr_result[1]
        to_serial_out=dpt_ccr_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.dpt_ccr_view(
            transaction_references=transaction_references,
            stock_type=stock_type,
            from_serial=from_serial,
            to_serial=to_serial,
            description=description,
            expected_posting=expected_posting,
        )

    def test_004_payment_order_04_dpt_poi_payment_order_issued_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        serial_no = from_serial_po
        expired_date = expired_date_test
        issuing_name = issuing_name_test
        issuer_id_number = issuer_id_number_test
        issuer_contact_number = issuer_contact_number_test
        amount = amount_test
        currency = currency_test
        beneficiary_name = beneficiary_name_test
        beneficiary_id_number = beneficiary_id_number_test
        beneficiary_contact_number = beneficiary_contact_number_test
        beneficiary_address = beneficiary_address_test
        purpose = purpose_test
        debit_method = method_cash
        debit_account = None
        description = None
        issued_date = working_date
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        dpt_poi_result = self.dpt_poi(
            serial_no=serial_no,
            expired_date=expired_date,
            issuing_name=issuing_name,
            issuer_id_number=issuer_id_number,
            issuer_contact_number=issuer_contact_number,
            amount=amount,
            currency=currency,
            beneficiary_name=beneficiary_name,
            beneficiary_id_number=beneficiary_id_number,
            beneficiary_contact_number=beneficiary_contact_number,
            beneficiary_address=beneficiary_address,
            purpose=purpose,
            debit_method=debit_method,
            debit_account=debit_account,
            description=description,
            issued_date=issued_date,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=dpt_poi_result[0]
        serial_no_out=dpt_poi_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.dpt_poi_view(
            transaction_references=transaction_references,
            serial_no=serial_no,
            expired_date=expired_date,
            issuing_name=issuing_name,
            issuer_id_number=issuer_id_number,
            issuer_contact_number=issuer_contact_number,
            amount=amount,
            currency=currency,
            beneficiary_name=beneficiary_name,
            beneficiary_id_number=beneficiary_id_number,
            beneficiary_contact_number=beneficiary_contact_number,
            beneficiary_address=beneficiary_address,
            purpose=purpose,
            debit_method=debit_method,
            debit_account=debit_account,
            description=description,
            issued_date=issued_date,
            expected_posting=expected_posting,
        )

    def test_005_payment_order_05_dpt_pow_payment_order_withdrawal_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        serial_no = from_serial_po
        withdrawal_method = method_cash
        credit_account = None
        description = None
        expired_date = expired_date_test
        issuing_name = issuing_name_test
        issuer_id_number = issuer_id_number_test
        issuer_contact_number = issuer_contact_number_test
        beneficiary_name = beneficiary_name_test
        beneficiary_id_number = beneficiary_id_number_test
        beneficiary_contact_number = beneficiary_contact_number_test
        beneficiary_address = beneficiary_address_test
        currency = currency_test
        stock_amount = amount_test
        withdrawal_amount = amount_test
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        dpt_pow_result = self.dpt_pow(
            serial_no=serial_no,
            withdrawal_method=withdrawal_method,
            credit_account=credit_account,
            description=description,
            expired_date=expired_date,
            issuing_name=issuing_name,
            issuer_id_number=issuer_id_number,
            issuer_contact_number=issuer_contact_number,
            beneficiary_name=beneficiary_name,
            beneficiary_id_number=beneficiary_id_number,
            beneficiary_contact_number=beneficiary_contact_number,
            beneficiary_address=beneficiary_address,
            currency=currency,
            stock_amount=stock_amount,
            withdrawal_amount=withdrawal_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=dpt_pow_result[0]
        serial_no_out=dpt_pow_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.dpt_pow_view(
            transaction_references=transaction_references,
            serial_no=serial_no,
            withdrawal_method=withdrawal_method,
            credit_account=credit_account,
            description=description,
            expired_date=expired_date,
            issuing_name=issuing_name,
            issuer_id_number=issuer_id_number,
            issuer_contact_number=issuer_contact_number,
            beneficiary_name=beneficiary_name,
            beneficiary_id_number=beneficiary_id_number,
            beneficiary_contact_number=beneficiary_contact_number,
            beneficiary_address=beneficiary_address,
            currency=currency,
            stock_amount=stock_amount,
            withdrawal_amount=withdrawal_amount,
            expected_posting=expected_posting,
        )

    def test_006_payment_order_06_dpt_rpo_payment_order_return_success_approve_later(self):
        serial_no = self.get_next_serial_number(stock_prefix_po, from_serial_po, 1)
        return_method = method_accounting
        credit_account = gl_account_number
        description = None
        expired_date = expired_date_test
        issuing_name = issuing_name_test
        issuer_id_number = issuer_id_number_test
        issuer_contact_number = issuer_contact_number_test
        beneficiary_name = beneficiary_name_test
        beneficiary_id_number = beneficiary_id_number_test
        beneficiary_contact_number = beneficiary_contact_number_test
        beneficiary_address = beneficiary_address_test
        currency = currency_test
        stock_amount = amount_test
        return_amount = amount_test
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None
        dpt_poi_result = self.dpt_poi(
            serial_no=serial_no,
            expired_date=expired_date,
            issuing_name=issuing_name,
            issuer_id_number=issuer_id_number,
            issuer_contact_number=issuer_contact_number,
            amount=amount_test,
            currency=currency,
            beneficiary_name=beneficiary_name,
            beneficiary_id_number=beneficiary_id_number,
            beneficiary_contact_number=beneficiary_contact_number,
            beneficiary_address=beneficiary_address,
            purpose=purpose_test,
            debit_method=method_accounting,
            debit_account=gl_account_number,
            description=description,
            issued_date=working_date,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
        )
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        dpt_rpo_result = self.dpt_rpo(
            serial_no=serial_no,
            return_method=return_method,
            credit_account=credit_account,
            description=description,
            expired_date=expired_date,
            issuing_name=issuing_name,
            issuer_id_number=issuer_id_number,
            issuer_contact_number=issuer_contact_number,
            beneficiary_name=beneficiary_name,
            beneficiary_id_number=beneficiary_id_number,
            beneficiary_contact_number=beneficiary_contact_number,
            beneficiary_address=beneficiary_address,
            currency=currency,
            stock_amount=stock_amount,
            return_amount=return_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=dpt_rpo_result[0]
        serial_no_out=dpt_rpo_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.dpt_rpo_view(
            transaction_references=transaction_references,
            serial_no=serial_no,
            return_method=return_method,
            credit_account=credit_account,
            description=description,
            expired_date=expired_date,
            issuing_name=issuing_name,
            issuer_id_number=issuer_id_number,
            issuer_contact_number=issuer_contact_number,
            beneficiary_name=beneficiary_name,
            beneficiary_id_number=beneficiary_id_number,
            beneficiary_contact_number=beneficiary_contact_number,
            beneficiary_address=beneficiary_address,
            currency=currency,
            stock_amount=stock_amount,
            return_amount=return_amount,
            expected_posting=expected_posting,
        )

if __name__ == '__main__': 
    webui_test.main()