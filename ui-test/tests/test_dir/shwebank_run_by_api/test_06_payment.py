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

    def test_002_pmt_iit_inward_internal_bank_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.logout()
        self.login(username_other_branch, password_other_branch, one_app='Y')
        product_code = None
        message_code = pmt_oit_reference_number
        remitting_branch = None
        sender_name = None
        sender_id = None
        sender_address = None
        sender_phone = None
        sender_type = None
        receiver_name = None
        receiver_id = None
        receiver_address = None
        receiver_phone = None
        receiver_type = None
        country = None
        purpose = None
        sender_to_receiver_information = None
        test_key = None
        goods_type = None
        goods_list = None
        receive_by = None
        account_number = None
        cross_rate = None
        receive_amount = None
        description = None
        region = None
        send_currency = None
        send_amount = None
        receive_currency = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve_other_branch
        password = password_approve_other_branch
        reason = None

        pmt_iit_result = self.pmt_iit(
            product_code=product_code,
            message_code=message_code,
            remitting_branch=remitting_branch,
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
            sender_to_receiver_information=sender_to_receiver_information,
            test_key=test_key,
            goods_type=goods_type,
            goods_list=goods_list,
            receive_by=receive_by,
            account_number=account_number,
            cross_rate=cross_rate,
            receive_amount=receive_amount,
            description=description,
            region=region,
            send_currency=send_currency,
            send_amount=send_amount,
            receive_currency=receive_currency,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=pmt_iit_result[0]
        message_code_out=pmt_iit_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.pmt_iit_view(
            transaction_references=transaction_references,
            product_code=product_code,
            message_code=message_code,
            remitting_branch=remitting_branch,
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
            sender_to_receiver_information=sender_to_receiver_information,
            test_key=test_key,
            goods_type=goods_type,
            goods_list=goods_list,
            receive_by=receive_by,
            account_number=account_number,
            cross_rate=cross_rate,
            receive_amount=receive_amount,
            description=description,
            region=region,
            send_currency=send_currency,
            send_amount=send_amount,
            receive_currency=receive_currency,
            expected_posting=expected_posting,
        )

    def test_003_pmt_oitt_outward_international_bank_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.logout()
        self.login(username_login, password_login, one_app='Y')
        global pmt_oitt_reference_number
        nostro_bank = nostro_bank_test
        beneficiary_bank = beneficiary_bank_test
        bank_address = None
        bank_country = None
        product_code = None
        sender_name = sender_name_test
        sender_id = sender_id_test
        sender_address = None
        sender_phone = None
        sender_type = None
        beneficiary_account_number = beneficiary_account_number_test
        receiver_name = receiver_name_test
        receiver_id = receiver_id_test
        receiver_address = None
        receiver_phone = None
        receiver_type = None
        country = None
        purpose = None
        sender_to_receiver_info = sender_to_receiver_info_test
        test_key_number = None
        goods_type = None
        goods_list = None
        payment_by = None
        account_number = None
        cheque_no = None
        amount_before_fees = amount_before_fees_test
        remitting_currency = None
        cross_rate = None
        reverse_rate = None
        display_rate = None
        remitting_amount = None
        description = None
        nostro_account = gl_account_number_test
        detail_of_charges = None
        reference_number = None
        currency = None
        fee = None
        amount_receive_from_customer = None
        remitting_amount_in_base_currency = None
        payment_exchange_rate = None
        remitting_exchange_rate = None
        fee_in_remitting_currency = None
        message_type = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        pmt_oitt_result = self.pmt_oitt(
            nostro_bank=nostro_bank,
            beneficiary_bank=beneficiary_bank,
            bank_address=bank_address,
            bank_country=bank_country,
            product_code=product_code,
            sender_name=sender_name,
            sender_id=sender_id,
            sender_address=sender_address,
            sender_phone=sender_phone,
            sender_type=sender_type,
            beneficiary_account_number=beneficiary_account_number,
            receiver_name=receiver_name,
            receiver_id=receiver_id,
            receiver_address=receiver_address,
            receiver_phone=receiver_phone,
            receiver_type=receiver_type,
            country=country,
            purpose=purpose,
            sender_to_receiver_info=sender_to_receiver_info,
            test_key_number=test_key_number,
            goods_type=goods_type,
            goods_list=goods_list,
            payment_by=payment_by,
            account_number=account_number,
            cheque_no=cheque_no,
            amount_before_fees=amount_before_fees,
            remitting_currency=remitting_currency,
            cross_rate=cross_rate,
            reverse_rate=reverse_rate,
            display_rate=display_rate,
            remitting_amount=remitting_amount,
            description=description,
            nostro_account=nostro_account,
            detail_of_charges=detail_of_charges,
            reference_number=reference_number,
            currency=currency,
            fee=fee,
            amount_receive_from_customer=amount_receive_from_customer,
            remitting_amount_in_base_currency=remitting_amount_in_base_currency,
            payment_exchange_rate=payment_exchange_rate,
            remitting_exchange_rate=remitting_exchange_rate,
            fee_in_remitting_currency=fee_in_remitting_currency,
            message_type=message_type,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=pmt_oitt_result[0]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        pmt_oitt_view_result = self.pmt_oitt_view(
            transaction_references=transaction_references,
            nostro_bank=nostro_bank,
            beneficiary_bank=beneficiary_bank,
            bank_address=bank_address,
            bank_country=bank_country,
            product_code=product_code,
            sender_name=sender_name,
            sender_id=sender_id,
            sender_address=sender_address,
            sender_phone=sender_phone,
            sender_type=sender_type,
            beneficiary_account_number=beneficiary_account_number,
            receiver_name=receiver_name,
            receiver_id=receiver_id,
            receiver_address=receiver_address,
            receiver_phone=receiver_phone,
            receiver_type=receiver_type,
            country=country,
            purpose=purpose,
            sender_to_receiver_info=sender_to_receiver_info,
            test_key_number=test_key_number,
            goods_type=goods_type,
            goods_list=goods_list,
            payment_by=payment_by,
            account_number=account_number,
            cheque_no=cheque_no,
            amount_before_fees=amount_before_fees,
            remitting_currency=remitting_currency,
            cross_rate=cross_rate,
            reverse_rate=reverse_rate,
            display_rate=display_rate,
            remitting_amount=remitting_amount,
            description=False,
            nostro_account=nostro_account,
            detail_of_charges=detail_of_charges,
            reference_number=reference_number,
            currency=currency,
            fee=fee,
            amount_receive_from_customer=amount_receive_from_customer,
            remitting_amount_in_base_currency=remitting_amount_in_base_currency,
            payment_exchange_rate=payment_exchange_rate,
            remitting_exchange_rate=remitting_exchange_rate,
            fee_in_remitting_currency=fee_in_remitting_currency,
            message_type=message_type,
            expected_posting=expected_posting,
        )
        pmt_oitt_reference_number=pmt_oitt_view_result[1]

    def test_004_approve_outward_message_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_queue_for_outward_approve(pmt_oitt_reference_number)

    def test_005_pmt_kitt_create_inward_domestic_swift_message_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global pmt_kitt_reference_number
        product_code = product_code_test
        ordering_institution = ordering_institution_test
        nostro_bank = nostro_bank_test
        bank_address = None
        bank_country = None
        sender_id = sender_id_test
        sender_name = sender_name_test
        sender_address = None
        sender_phone = None
        sender_type = None
        receiver_name = receiver_name_test
        receiver_id = receiver_id_test
        receiver_address = None
        receiver_phone = None
        receiver_type = None
        country = None
        purpose = None
        sender_to_receiver_information = None
        goods_type = None
        goods_list = None
        remitting_currency = None
        remitting_amount = remitting_amount_test
        receive_by = None
        receive_account_number = None
        receive_amount = receive_amount_test
        description = None
        nostro_account = gl_account_number_test
        reference_number = None
        receive_currency = None
        cross_rate = None
        reverse_rate = None
        display_rate = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        pmt_kitt_result = self.pmt_kitt(
            product_code=product_code,
            ordering_institution=ordering_institution,
            nostro_bank=nostro_bank,
            bank_address=bank_address,
            bank_country=bank_country,
            sender_id=sender_id,
            sender_name=sender_name,
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
            sender_to_receiver_information=sender_to_receiver_information,
            goods_type=goods_type,
            goods_list=goods_list,
            remitting_currency=remitting_currency,
            remitting_amount=remitting_amount,
            receive_by=receive_by,
            receive_account_number=receive_account_number,
            receive_amount=receive_amount,
            description=description,
            nostro_account=nostro_account,
            reference_number=reference_number,
            receive_currency=receive_currency,
            cross_rate=cross_rate,
            reverse_rate=reverse_rate,
            display_rate=display_rate,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=pmt_kitt_result[0]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        pmt_kitt_view_result = self.pmt_kitt_view(
            transaction_references=transaction_references,
            product_code=product_code,
            ordering_institution=ordering_institution,
            nostro_bank=nostro_bank,
            bank_address=bank_address,
            bank_country=bank_country,
            sender_id=sender_id,
            sender_name=sender_name,
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
            sender_to_receiver_information=sender_to_receiver_information,
            goods_type=goods_type,
            goods_list=goods_list,
            remitting_currency=remitting_currency,
            remitting_amount=remitting_amount,
            receive_by=receive_by,
            receive_account_number=receive_account_number,
            receive_amount=receive_amount,
            description=False,
            nostro_account=nostro_account,
            reference_number=reference_number,
            receive_currency=receive_currency,
            cross_rate=cross_rate,
            reverse_rate=reverse_rate,
            display_rate=display_rate,
            expected_posting=expected_posting,
        )
        pmt_kitt_reference_number=pmt_kitt_view_result[1]

    def test_006_approve_inward_message_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_queue_for_inward_approve(
            message_code=pmt_kitt_reference_number,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )

    def test_007_pmt_iitt_inward_international_bank_success_approve_later(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        product_code = None
        message_code = pmt_kitt_reference_number
        ordering_institution = ordering_institution_test
        sender_id = None
        sender_address = None
        sender_name = None
        sender_phone = None
        sender_type = None
        receiver_name = None
        receiver_id = None
        receiver_address = None
        receiver_phone = None
        receiver_type = None
        country = None
        purpose = None
        sender_to_receiver_information = None
        goods_type = None
        goods_list = None
        receive_by = None
        account_number = None
        receive_currency = None
        cross_rate = None
        reverse_rate = None
        display_rate = None
        amount_before_fees = None
        description = None
        detail_of_charges = None
        nostro_bank = None
        reference_number = None
        remitting_currency = None
        remitting_amount = None
        remitting_exchange_rate_bcy = None
        remitting_amount_in_bcy = None
        commission_in_remitting_currency = None
        original_cross_rate = None
        commission = None
        amount_customer_receives = None
        receive_exchange_rate_bcy = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        pmt_iitt_result = self.pmt_iitt(
            product_code=product_code,
            message_code=message_code,
            ordering_institution=ordering_institution,
            sender_id=sender_id,
            sender_address=sender_address,
            sender_name=sender_name,
            sender_phone=sender_phone,
            sender_type=sender_type,
            receiver_name=receiver_name,
            receiver_id=receiver_id,
            receiver_address=receiver_address,
            receiver_phone=receiver_phone,
            receiver_type=receiver_type,
            country=country,
            purpose=purpose,
            sender_to_receiver_information=sender_to_receiver_information,
            goods_type=goods_type,
            goods_list=goods_list,
            receive_by=receive_by,
            account_number=account_number,
            receive_currency=receive_currency,
            cross_rate=cross_rate,
            reverse_rate=reverse_rate,
            display_rate=display_rate,
            amount_before_fees=amount_before_fees,
            description=description,
            detail_of_charges=detail_of_charges,
            nostro_bank=nostro_bank,
            reference_number=reference_number,
            remitting_currency=remitting_currency,
            remitting_amount=remitting_amount,
            remitting_exchange_rate_bcy=remitting_exchange_rate_bcy,
            remitting_amount_in_bcy=remitting_amount_in_bcy,
            commission_in_remitting_currency=commission_in_remitting_currency,
            original_cross_rate=original_cross_rate,
            commission=commission,
            amount_customer_receives=amount_customer_receives,
            receive_exchange_rate_bcy=receive_exchange_rate_bcy,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=pmt_iitt_result[0]
        reference_number_out=pmt_iitt_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.pmt_iitt_view(
            transaction_references=transaction_references,
            product_code=product_code,
            message_code=message_code,
            ordering_institution=ordering_institution,
            sender_id=sender_id,
            sender_address=sender_address,
            sender_name=sender_name,
            sender_phone=sender_phone,
            sender_type=sender_type,
            receiver_name=receiver_name,
            receiver_id=receiver_id,
            receiver_address=receiver_address,
            receiver_phone=receiver_phone,
            receiver_type=receiver_type,
            country=country,
            purpose=purpose,
            sender_to_receiver_information=sender_to_receiver_information,
            goods_type=goods_type,
            goods_list=goods_list,
            receive_by=receive_by,
            account_number=account_number,
            receive_currency=receive_currency,
            cross_rate=cross_rate,
            reverse_rate=reverse_rate,
            display_rate=display_rate,
            amount_before_fees=amount_before_fees,
            description=description,
            detail_of_charges=detail_of_charges,
            nostro_bank=nostro_bank,
            reference_number=reference_number,
            remitting_currency=remitting_currency,
            remitting_amount=remitting_amount,
            remitting_exchange_rate_bcy=remitting_exchange_rate_bcy,
            remitting_amount_in_bcy=remitting_amount_in_bcy,
            commission_in_remitting_currency=commission_in_remitting_currency,
            original_cross_rate=original_cross_rate,
            commission=commission,
            amount_customer_receives=amount_customer_receives,
            receive_exchange_rate_bcy=receive_exchange_rate_bcy,
            expected_posting=expected_posting,
        )

if __name__ == '__main__': 
    webui_test.main()