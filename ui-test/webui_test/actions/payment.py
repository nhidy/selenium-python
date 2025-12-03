from webui_test.case import *

class PaymentActions(TestCase):

# -------------------------- handle FO - PAYMENT --------------------------
    # PMT_OIT: 6600: Outward internal bank
    def pmt_oit(self, beneficiary_branch=None, product_code=None, sender_name=None, sender_id=None, sender_address=None, sender_phone=None, sender_type=None, receiver_name=None, receiver_id=None, receiver_address=None, receiver_phone=None, receiver_type=None, country=None, purpose=None, sender_to_receiver_info=None, test_key=None, goods_type=None, goods_list=None, payment_by=None, account_number=None, cheque_no=None, send_currency=None, send_amount=None, cross_rate=None, description=None, region=None, reference_number=None, total_amount_payable=None, receive_currency=None, receive_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('PMT_OIT', '6600')
        self.wait_for_button_available('Reload Auto Fee')
        self.click_button('Reload Auto Fee')
        self.wait_loading()
        self.wait_for_button_available('Accept')
        self.assert_form_title('6600: Outward internal bank')
        # enter value
        if beneficiary_branch:
            self.fo_write_text_group('Beneficiary branch', beneficiary_branch)
            self.wait_loading()
        if product_code:
            self.fo_write_text('Product Code', product_code)
        if sender_name:
            self.fo_write_text('Sender name', sender_name)
        if sender_id:
            self.fo_write_text('Sender id', sender_id)
        if sender_address:
            self.fo_write_text('Sender address', sender_address)
        if sender_phone:
            self.fo_write_text('Sender phone', sender_phone)
        self.key_escape()
        if sender_type:
            self.fo_select('Sender type', sender_type)
        if receiver_name:
            self.fo_write_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_write_text('Receiver id', receiver_id)
        if receiver_address:
            self.fo_write_text('Receiver address', receiver_address)
        if receiver_phone:
            self.fo_write_text('Receiver phone', receiver_phone)
        self.key_escape()
        if receiver_type:
            self.fo_select('Receiver type', receiver_type)
        self.key_escape()
        if country:
            self.fo_select('Country', country)
        self.key_escape()
        if purpose:
            self.fo_select('Purpose', purpose)
        if sender_to_receiver_info:
            self.fo_write_text('Sender to receiver info', sender_to_receiver_info)
        if test_key:
            self.fo_write_text('TEST-KEY', test_key)
        if goods_type:
            self.fo_click_collap('Other information')
            self.fo_select_collap('Other information', 'Goods type', goods_type)
        if goods_list:
            self.fo_click_collap('Other information')
            self.fo_write_text_multi('Other information', 'Goods list', goods_list)
        self.key_escape()
        if payment_by:
            self.fo_select('Payment by', payment_by)
        if account_number:
            self.fo_write_text_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if cheque_no:
            self.fo_write('Cheque No', str(cheque_no).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if send_currency:
            self.fo_select('Send currency', send_currency)
        if send_amount:
            self.fo_write_number('Send amount', send_amount)
        if cross_rate:
            self.fo_write_number('Cross rate', cross_rate)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.click_button('Reload Auto Fee')
        if region:
            self.fo_assert_select('Region', region)
        if reference_number:
            self.fo_assert_text('Reference number', reference_number)
        if total_amount_payable:
            self.fo_assert_value('Total amount payable', total_amount_payable)
        if receive_currency:
            self.fo_assert_select('Receive currency', receive_currency)
        if receive_amount:
            self.fo_assert_value('Receive amount', receive_amount)
        self.wait_loading()
        self.fo_click_checkbox('I have checked the input information and agree to send this transaction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references PMT_OIT: {transaction_references}')
            reference_number_out=self.fo_get_text('Reference number')
            print(f'Reference number: {reference_number_out}')
            return transaction_references, reference_number_out

    def pmt_oit_view(self, transaction_references, beneficiary_branch=None, product_code=None, sender_name=None, sender_id=None, sender_address=None, sender_phone=None, sender_type=None, receiver_name=None, receiver_id=None, receiver_address=None, receiver_phone=None, receiver_type=None, country=None, purpose=None, sender_to_receiver_info=None, test_key=None, goods_type=None, goods_list=None, payment_by=None, account_number=None, cheque_no=None, send_currency=None, send_amount=None, cross_rate=None, description=None, region=None, reference_number=None, total_amount_payable=None, receive_currency=None, receive_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '6600: Outward internal bank')
        # compare value
        if beneficiary_branch:
            self.fo_assert_text_group('Beneficiary branch', beneficiary_branch)
        if product_code:
            self.fo_assert_text('Product Code', product_code)
        if sender_name:
            self.fo_assert_text('Sender name', sender_name)
        if sender_id:
            self.fo_assert_text('Sender id', sender_id)
        if sender_address:
            self.fo_assert_text('Sender address', sender_address)
        if sender_phone:
            self.fo_assert_text('Sender phone', sender_phone)
        if sender_type:
            self.fo_assert_select('Sender type', sender_type)
        if receiver_name:
            self.fo_assert_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_assert_text('Receiver id', receiver_id)
        if receiver_address:
            self.fo_assert_text('Receiver address', receiver_address)
        if receiver_phone:
            self.fo_assert_text('Receiver phone', receiver_phone)
        if receiver_type:
            self.fo_assert_select('Receiver type', receiver_type)
        if country:
            self.fo_assert_select('Country', country)
        if purpose:
            self.fo_assert_select('Purpose', purpose)
        if sender_to_receiver_info:
            self.fo_assert_text('Sender to receiver info', sender_to_receiver_info)
        if test_key:
            self.fo_assert_text('TEST-KEY', test_key)
        if goods_type:
            self.fo_click_collap('Other information')
            self.fo_assert_value_multi('Other information', 'Goods type', goods_type)
        if goods_list:
            self.fo_click_collap('Other information')
            self.fo_assert_text_multi('Other information', 'Goods list', goods_list)
        if payment_by:
            self.fo_assert_select('Payment by', payment_by)
        if account_number:
            self.fo_assert_text_group('Account number', account_number)
        if cheque_no:
            self.fo_assert_value('Cheque No', self.stock_number_mask(cheque_no))
        if send_currency:
            self.fo_assert_select('Send currency', send_currency)
        if send_amount:
            self.fo_assert_value('Send amount', send_amount)
        if cross_rate:
            self.fo_assert_value('Cross rate', cross_rate)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if region:
            self.fo_assert_select('Region', region)
        if reference_number:
            self.fo_assert_text('Reference number', reference_number)
        if total_amount_payable:
            self.fo_assert_value('Total amount payable', total_amount_payable)
        if receive_currency:
            self.fo_assert_select('Receive currency', receive_currency)
        if receive_amount:
            self.fo_assert_value('Receive amount', receive_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('I have checked the input information and agree to send this transaction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references PMT_OIT: {transaction_references}')
        reference_number_out=self.fo_get_text('Reference number')
        print(f'F8: Reference number: {reference_number_out}')
        return transaction_references, reference_number_out

    # PMT_IIT: 6610: Inward internal bank
    def pmt_iit(self, product_code=None, message_code=None, remitting_branch=None, sender_name=None, sender_id=None, sender_address=None, sender_phone=None, sender_type=None, receiver_name=None, receiver_id=None, receiver_address=None, receiver_phone=None, receiver_type=None, country=None, purpose=None, sender_to_receiver_information=None, test_key=None, goods_type=None, goods_list=None, receive_by=None, account_number=None, cross_rate=None, receive_amount=None, description=None, region=None, send_currency=None, send_amount=None, receive_currency=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('PMT_IIT', '6610')
        self.wait_for_button_available('Reload Auto Fee')
        self.click_button('Reload Auto Fee')
        self.wait_loading()
        self.wait_for_button_available('Accept')
        self.assert_form_title('6610: Inward internal bank')
        # enter value
        if product_code:
            self.fo_write_text('Product Code', product_code)
        if message_code:
            self.fo_write('Message code', message_code)
        if remitting_branch:
            self.fo_write_text_group('Remitting Branch', remitting_branch)
        if sender_name:
            self.fo_write_text('Sender name', sender_name)
        if sender_id:
            self.fo_write_text('Sender id', sender_id)
        if sender_address:
            self.fo_write_text('Sender address', sender_address)
        if sender_phone:
            self.fo_write_text('Sender phone', sender_phone)
        self.key_escape()
        if sender_type:
            self.fo_select('Sender type', sender_type)
        if receiver_name:
            self.fo_write_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_write_text('Receiver id', receiver_id)
        if receiver_address:
            self.fo_write_text('Receiver address', receiver_address)
        if receiver_phone:
            self.fo_write_text('Receiver phone', receiver_phone)
        self.key_escape()
        if receiver_type:
            self.fo_select('Receiver type', receiver_type)
        self.key_escape()
        if country:
            self.fo_select('Country', country)
        self.key_escape()
        if purpose:
            self.fo_select('Purpose', purpose)
        if sender_to_receiver_information:
            self.fo_write_text('Sender to receiver information', sender_to_receiver_information)
        if test_key:
            self.fo_write_text('TEST-Key', test_key)
        if goods_type:
            self.fo_click_collap('Other information')
            self.fo_select_collap('Other information', 'Goods type', goods_type)
        if goods_list:
            self.fo_click_collap('Other information')
            self.fo_write_text_multi('Other information', 'Goods list', goods_list)
        self.key_escape()
        if receive_by:
            self.fo_select('Receive by', receive_by)
        if account_number:
            self.fo_write_text_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if cross_rate:
            self.fo_write_number('Cross rate', cross_rate)
        if receive_amount:
            self.fo_write_number('Receive amount', receive_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.click_button('Reload Auto Fee')
        if region:
            self.fo_assert_select('Region', region)
        if send_currency:
            self.fo_assert_select('Send currency', send_currency)
        if send_amount:
            self.fo_assert_value('Send amount', send_amount)
        if receive_currency:
            self.fo_assert_select('Receive currency', receive_currency)
        self.wait_loading()
        self.fo_click_checkbox('I have checked the input information and agree to send this transaction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references PMT_IIT: {transaction_references}')
            message_code_out=self.fo_get_value('Message code')
            print(f'Message code: {message_code_out}')
            return transaction_references, message_code_out

    def pmt_iit_view(self, transaction_references, product_code=None, message_code=None, remitting_branch=None, sender_name=None, sender_id=None, sender_address=None, sender_phone=None, sender_type=None, receiver_name=None, receiver_id=None, receiver_address=None, receiver_phone=None, receiver_type=None, country=None, purpose=None, sender_to_receiver_information=None, test_key=None, goods_type=None, goods_list=None, receive_by=None, account_number=None, cross_rate=None, receive_amount=None, description=None, region=None, send_currency=None, send_amount=None, receive_currency=None, expected_posting=None):
        self.transaction_view(transaction_references, '6610: Inward internal bank')
        # compare value
        if product_code:
            self.fo_assert_text('Product Code', product_code)
        if message_code:
            self.fo_assert_value('Message code', message_code)
        if remitting_branch:
            self.fo_assert_text_group('Remitting Branch', remitting_branch)
        if sender_name:
            self.fo_assert_text('Sender name', sender_name)
        if sender_id:
            self.fo_assert_text('Sender id', sender_id)
        if sender_address:
            self.fo_assert_text('Sender address', sender_address)
        if sender_phone:
            self.fo_assert_text('Sender phone', sender_phone)
        if sender_type:
            self.fo_assert_select('Sender type', sender_type)
        if receiver_name:
            self.fo_assert_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_assert_text('Receiver id', receiver_id)
        if receiver_address:
            self.fo_assert_text('Receiver address', receiver_address)
        if receiver_phone:
            self.fo_assert_text('Receiver phone', receiver_phone)
        if receiver_type:
            self.fo_assert_select('Receiver type', receiver_type)
        if country:
            self.fo_assert_select('Country', country)
        if purpose:
            self.fo_assert_select('Purpose', purpose)
        if sender_to_receiver_information:
            self.fo_assert_text('Sender to receiver information', sender_to_receiver_information)
        if test_key:
            self.fo_assert_text('TEST-Key', test_key)
        if goods_type:
            self.fo_click_collap('Other information')
            self.fo_assert_value_multi('Other information', 'Goods type', goods_type)
        if goods_list:
            self.fo_click_collap('Other information')
            self.fo_assert_text_multi('Other information', 'Goods list', goods_list)
        if receive_by:
            self.fo_assert_select('Receive by', receive_by)
        if account_number:
            self.fo_assert_text_group('Account number', account_number)
        if cross_rate:
            self.fo_assert_value('Cross rate', cross_rate)
        if receive_amount:
            self.fo_assert_value('Receive amount', receive_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if region:
            self.fo_assert_select('Region', region)
        if send_currency:
            self.fo_assert_select('Send currency', send_currency)
        if send_amount:
            self.fo_assert_value('Send amount', send_amount)
        if receive_currency:
            self.fo_assert_select('Receive currency', receive_currency)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('I have checked the input information and agree to send this transaction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references PMT_IIT: {transaction_references}')
        message_code_out=self.fo_get_value('Message code')
        print(f'F8: Message code: {message_code_out}')
        return transaction_references, message_code_out

    # PMT_KITT: 6630: Create inward (domestic/swift) message
    def pmt_kitt(self, product_code=None, ordering_institution=None, nostro_bank=None, bank_address=None, bank_country=None, sender_id=None, sender_name=None, sender_address=None, sender_phone=None, sender_type=None, receiver_name=None, receiver_id=None, receiver_address=None, receiver_phone=None, receiver_type=None, country=None, purpose=None, sender_to_receiver_information=None, goods_type=None, goods_list=None, remitting_currency=None, remitting_amount=None, receive_by=None, receive_account_number=None, receive_amount=None, description=None, nostro_account=None, reference_number=None, receive_currency=None, cross_rate=None, reverse_rate=None, display_rate=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('PMT_KITT', '6630')
        self.wait_for_button_available('Accept')
        self.assert_form_title('6630: Create inward (domestic/swift) message')
        # enter value
        if product_code:
            self.fo_write_text('Product Code', product_code)
        if ordering_institution:
            self.fo_write_text_group('Ordering Institution', ordering_institution)
        if nostro_bank:
            self.fo_write_text_group('Nostro Bank', nostro_bank)
        if bank_address:
            self.fo_write_text('Bank address', bank_address)
        self.key_escape()
        if bank_country:
            self.fo_select('Bank country', bank_country)
        if sender_id:
            self.fo_write_text('Sender id', sender_id)
        if sender_name:
            self.fo_write_text('Sender name', sender_name)
        if sender_address:
            self.fo_write_text('Sender address', sender_address)
        if sender_phone:
            self.fo_write_text('Sender phone', sender_phone)
        self.key_escape()
        if sender_type:
            self.fo_select('Sender type', sender_type)
        if receiver_name:
            self.fo_write_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_write_text('Receiver id', receiver_id)
        if receiver_address:
            self.fo_write_text('Receiver address', receiver_address)
        if receiver_phone:
            self.fo_write_text('Receiver phone', receiver_phone)
        self.key_escape()
        if receiver_type:
            self.fo_select('Receiver type', receiver_type)
        self.key_escape()
        if country:
            self.fo_select('Country', country)
        self.key_escape()
        if purpose:
            self.fo_select('Purpose', purpose)
        if sender_to_receiver_information:
            self.fo_write_text('Sender to receiver information', sender_to_receiver_information)
        if goods_type:
            self.fo_click_collap('Other information')
            self.fo_select_collap('Other information', 'Goods type', goods_type)
        if goods_list:
            self.fo_click_collap('Other information')
            self.fo_write_text_multi('Other information', 'Goods list', goods_list)
        self.key_escape()
        if remitting_currency:
            self.fo_select('Remitting currency', remitting_currency)
        if remitting_amount:
            self.fo_write_number('Remitting amount', remitting_amount)
        self.key_escape()
        if receive_by:
            self.fo_select('Receive by', receive_by)
        if receive_account_number:
            self.fo_write_group('Receive account number', str(receive_account_number).replace('-', ''))
            self.wait_loading()
        if receive_amount:
            self.fo_write_number('Receive amount', receive_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if nostro_account:
            self.fo_write('Nostro Account', str(nostro_account).replace('-', ''))
            self.wait_loading()
        if reference_number:
            self.fo_assert_text_group('Reference number', reference_number)
        if receive_currency:
            self.fo_assert_select('Receive currency', receive_currency)
        if cross_rate:
            self.fo_assert_value('Cross rate', cross_rate)
        if reverse_rate:
            self.fo_assert_value('Reverse rate', reverse_rate)
        if display_rate:
            self.fo_assert_select('Display rate', display_rate)
        self.wait_loading()
        self.fo_click_checkbox('I have checked the input information and agree to send this transaction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references PMT_KITT: {transaction_references}')
            reference_number_out=self.fo_get_text_group('Reference number')
            print(f'Reference number: {reference_number_out}')
            return transaction_references, reference_number_out

    def pmt_kitt_view(self, transaction_references, product_code=None, ordering_institution=None, nostro_bank=None, bank_address=None, bank_country=None, sender_id=None, sender_name=None, sender_address=None, sender_phone=None, sender_type=None, receiver_name=None, receiver_id=None, receiver_address=None, receiver_phone=None, receiver_type=None, country=None, purpose=None, sender_to_receiver_information=None, goods_type=None, goods_list=None, remitting_currency=None, remitting_amount=None, receive_by=None, receive_account_number=None, receive_amount=None, description=None, nostro_account=None, reference_number=None, receive_currency=None, cross_rate=None, reverse_rate=None, display_rate=None, expected_posting=None):
        self.transaction_view(transaction_references, '6630: Create inward (domestic/swift) message')
        # compare value
        if product_code:
            self.fo_assert_text('Product Code', product_code)
        if ordering_institution:
            self.fo_assert_text_group('Ordering Institution', ordering_institution)
        if nostro_bank:
            self.fo_assert_text_group('Nostro Bank', nostro_bank)
        if bank_address:
            self.fo_assert_text('Bank address', bank_address)
        if bank_country:
            self.fo_assert_select('Bank country', bank_country)
        if sender_id:
            self.fo_assert_text('Sender id', sender_id)
        if sender_name:
            self.fo_assert_text('Sender name', sender_name)
        if sender_address:
            self.fo_assert_text('Sender address', sender_address)
        if sender_phone:
            self.fo_assert_text('Sender phone', sender_phone)
        if sender_type:
            self.fo_assert_select('Sender type', sender_type)
        if receiver_name:
            self.fo_assert_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_assert_text('Receiver id', receiver_id)
        if receiver_address:
            self.fo_assert_text('Receiver address', receiver_address)
        if receiver_phone:
            self.fo_assert_text('Receiver phone', receiver_phone)
        if receiver_type:
            self.fo_assert_select('Receiver type', receiver_type)
        if country:
            self.fo_assert_select('Country', country)
        if purpose:
            self.fo_assert_select('Purpose', purpose)
        if sender_to_receiver_information:
            self.fo_assert_text('Sender to receiver information', sender_to_receiver_information)
        if goods_type:
            self.fo_click_collap('Other information')
            self.fo_assert_value_multi('Other information', 'Goods type', goods_type)
        if goods_list:
            self.fo_click_collap('Other information')
            self.fo_assert_text_multi('Other information', 'Goods list', goods_list)
        if remitting_currency:
            self.fo_assert_select('Remitting currency', remitting_currency)
        if remitting_amount:
            self.fo_assert_value('Remitting amount', remitting_amount)
        if receive_by:
            self.fo_assert_select('Receive by', receive_by)
        if receive_account_number:
            self.fo_assert_value_group('Receive account number', receive_account_number)
        if receive_amount:
            self.fo_assert_value('Receive amount', receive_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if nostro_account:
            self.fo_assert_value('Nostro Account', self.gl_account_number_mask(nostro_account))
        if reference_number:
            self.fo_assert_text_group('Reference number', reference_number)
        if receive_currency:
            self.fo_assert_select('Receive currency', receive_currency)
        if cross_rate:
            self.fo_assert_value('Cross rate', cross_rate)
        if reverse_rate:
            self.fo_assert_value('Reverse rate', reverse_rate)
        if display_rate:
            self.fo_assert_select('Display rate', display_rate)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('I have checked the input information and agree to send this transaction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references PMT_KITT: {transaction_references}')
        reference_number_out=self.fo_get_text_group('Reference number')
        print(f'F8: Reference number: {reference_number_out}')
        return transaction_references, reference_number_out

    # PMT_OITT: 6602: Outward international bank
    def pmt_oitt(self, nostro_bank=None, beneficiary_bank=None, bank_address=None, bank_country=None, product_code=None, sender_name=None, sender_id=None, sender_address=None, sender_phone=None, sender_type=None, beneficiary_account_number=None, receiver_name=None, receiver_id=None, receiver_address=None, receiver_phone=None, receiver_type=None, country=None, purpose=None, sender_to_receiver_info=None, test_key_number=None, goods_type=None, goods_list=None, payment_by=None, account_number=None, cheque_no=None, amount_before_fees=None, remitting_currency=None, cross_rate=None, reverse_rate=None, display_rate=None, remitting_amount=None, description=None, nostro_account=None, detail_of_charges=None, reference_number=None, currency=None, fee=None, amount_receive_from_customer=None, remitting_amount_in_base_currency=None, payment_exchange_rate=None, remitting_exchange_rate=None, fee_in_remitting_currency=None, message_type=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('PMT_OITT', '6602')
        self.wait_for_button_available('Accept')
        self.assert_form_title('6602: Outward international bank')
        # enter value
        if nostro_bank:
            self.fo_write_text_group('Nostro bank', nostro_bank)
        if beneficiary_bank:
            self.fo_write_text_group('Beneficiary bank', beneficiary_bank)
        if bank_address:
            self.fo_write_text('Bank address', bank_address)
        self.key_escape()
        if bank_country:
            self.fo_select('Bank country', bank_country)
        if product_code:
            self.fo_write_text('Product Code', product_code)
        if sender_name:
            self.fo_write_text('Sender name', sender_name)
        if sender_id:
            self.fo_write_text('Sender id', sender_id)
        if sender_address:
            self.fo_write_text('Sender address', sender_address)
        if sender_phone:
            self.fo_write_text('Sender phone', sender_phone)
        self.key_escape()
        if sender_type:
            self.fo_select('Sender type', sender_type)
        if beneficiary_account_number:
            self.fo_write_text('beneficiary account number', beneficiary_account_number)
        if receiver_name:
            self.fo_write_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_write_text('Receiver id', receiver_id)
        if receiver_address:
            self.fo_write_text('Receiver address', receiver_address)
        if receiver_phone:
            self.fo_write_text('Receiver phone', receiver_phone)
        self.key_escape()
        if receiver_type:
            self.fo_select('Receiver type', receiver_type)
        self.key_escape()
        if country:
            self.fo_select('Country', country)
        self.key_escape()
        if purpose:
            self.fo_select('Purpose', purpose)
        if sender_to_receiver_info:
            self.fo_write_text('Sender to receiver info', sender_to_receiver_info)
        if test_key_number:
            self.fo_write_text('TEST-KEY number', test_key_number)
        if goods_type:
            self.fo_click_collap('Other information')
            self.fo_select_collap('Other information', 'Goods type', goods_type)
        if goods_list:
            self.fo_click_collap('Other information')
            self.fo_write_text_multi('Other information', 'Goods list', goods_list)
        self.key_escape()
        if payment_by:
            self.fo_select('Payment by', payment_by)
        if account_number:
            self.fo_write_text_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if cheque_no:
            self.fo_write('Cheque No', str(cheque_no).replace('-', ''))
            self.wait_loading()
        if amount_before_fees:
            self.fo_write_number('Amount before fees', amount_before_fees)
        self.key_escape()
        if remitting_currency:
            self.fo_select('Remitting currency', remitting_currency)
        if cross_rate:
            self.fo_write_number('Cross rate', cross_rate)
        if reverse_rate:
            self.fo_write_number('Reverse rate', reverse_rate)
        self.key_escape()
        if display_rate:
            self.fo_select('Display rate', display_rate)
        if remitting_amount:
            self.fo_write_number('Remitting amount', remitting_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if nostro_account:
            self.fo_write('Nostro Account', nostro_account)
        self.key_escape()
        if detail_of_charges:
            self.fo_select('Detail of charges', detail_of_charges)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if reference_number:
            self.fo_assert_text('Reference number', reference_number)
        if currency:
            self.fo_assert_select('Currency', currency)
        if fee:
            self.fo_assert_value('Fee', fee)
        if amount_receive_from_customer:
            self.fo_assert_value('Amount receive from customer', amount_receive_from_customer)
        if remitting_amount_in_base_currency:
            self.fo_assert_value('Remitting amount in base currency', remitting_amount_in_base_currency)
        if payment_exchange_rate:
            self.fo_assert_value('Payment exchange rate', payment_exchange_rate)
        if remitting_exchange_rate:
            self.fo_assert_value('Remitting exchange rate', remitting_exchange_rate)
        if fee_in_remitting_currency:
            self.fo_assert_value('Fee in remitting currency', fee_in_remitting_currency)
        if message_type:
            self.fo_assert_text('Message type', message_type)
        self.wait_loading()
        self.fo_click_checkbox('I have checked the input information and agree to send this transaction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references PMT_OITT: {transaction_references}')
            reference_number_out=self.fo_get_text('Reference number')
            print(f'Reference number: {reference_number_out}')
            return transaction_references, reference_number_out

    def pmt_oitt_view(self, transaction_references, nostro_bank=None, beneficiary_bank=None, bank_address=None, bank_country=None, product_code=None, sender_name=None, sender_id=None, sender_address=None, sender_phone=None, sender_type=None, beneficiary_account_number=None, receiver_name=None, receiver_id=None, receiver_address=None, receiver_phone=None, receiver_type=None, country=None, purpose=None, sender_to_receiver_info=None, test_key_number=None, goods_type=None, goods_list=None, payment_by=None, account_number=None, cheque_no=None, amount_before_fees=None, remitting_currency=None, cross_rate=None, reverse_rate=None, display_rate=None, remitting_amount=None, description=None, nostro_account=None, detail_of_charges=None, reference_number=None, currency=None, fee=None, amount_receive_from_customer=None, remitting_amount_in_base_currency=None, payment_exchange_rate=None, remitting_exchange_rate=None, fee_in_remitting_currency=None, message_type=None, expected_posting=None):
        self.transaction_view(transaction_references, '6602: Outward international bank')
        # compare value
        if nostro_bank:
            self.fo_assert_text_group('Nostro bank', nostro_bank)
        if beneficiary_bank:
            self.fo_assert_text_group('Beneficiary bank', beneficiary_bank)
        if bank_address:
            self.fo_assert_text('Bank address', bank_address)
        if bank_country:
            self.fo_assert_select('Bank country', bank_country)
        if product_code:
            self.fo_assert_text('Product Code', product_code)
        if sender_name:
            self.fo_assert_text('Sender name', sender_name)
        if sender_id:
            self.fo_assert_text('Sender id', sender_id)
        if sender_address:
            self.fo_assert_text('Sender address', sender_address)
        if sender_phone:
            self.fo_assert_text('Sender phone', sender_phone)
        if sender_type:
            self.fo_assert_select('Sender type', sender_type)
        if beneficiary_account_number:
            self.fo_assert_text('beneficiary account number', beneficiary_account_number)
        if receiver_name:
            self.fo_assert_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_assert_text('Receiver id', receiver_id)
        if receiver_address:
            self.fo_assert_text('Receiver address', receiver_address)
        if receiver_phone:
            self.fo_assert_text('Receiver phone', receiver_phone)
        if receiver_type:
            self.fo_assert_select('Receiver type', receiver_type)
        if country:
            self.fo_assert_select('Country', country)
        if purpose:
            self.fo_assert_select('Purpose', purpose)
        if sender_to_receiver_info:
            self.fo_assert_text('Sender to receiver info', sender_to_receiver_info)
        if test_key_number:
            self.fo_assert_text('TEST-KEY number', test_key_number)
        if goods_type:
            self.fo_click_collap('Other information')
            self.fo_assert_value_multi('Other information', 'Goods type', goods_type)
        if goods_list:
            self.fo_click_collap('Other information')
            self.fo_assert_text_multi('Other information', 'Goods list', goods_list)
        if payment_by:
            self.fo_assert_select('Payment by', payment_by)
        if account_number:
            self.fo_assert_text_group('Account number', account_number)
        if cheque_no:
            self.fo_assert_value('Cheque No', self.stock_number_mask(cheque_no))
        if amount_before_fees:
            self.fo_assert_value('Amount before fees', amount_before_fees)
        if remitting_currency:
            self.fo_assert_select('Remitting currency', remitting_currency)
        if cross_rate:
            self.fo_assert_value('Cross rate', cross_rate)
        if reverse_rate:
            self.fo_assert_value('Reverse rate', reverse_rate)
        if display_rate:
            self.fo_assert_select('Display rate', display_rate)
        if remitting_amount:
            self.fo_assert_value('Remitting amount', remitting_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if nostro_account:
            self.fo_assert_value('Nostro Account', self.gl_account_number_mask(nostro_account))
        if detail_of_charges:
            self.fo_assert_select('Detail of charges', detail_of_charges)
        if reference_number:
            self.fo_assert_text('Reference number', reference_number)
        if currency:
            self.fo_assert_select('Currency', currency)
        if fee:
            self.fo_assert_value('Fee', fee)
        if amount_receive_from_customer:
            self.fo_assert_value('Amount receive from customer', amount_receive_from_customer)
        if remitting_amount_in_base_currency:
            self.fo_assert_value('Remitting amount in base currency', remitting_amount_in_base_currency)
        if payment_exchange_rate:
            self.fo_assert_value('Payment exchange rate', payment_exchange_rate)
        if remitting_exchange_rate:
            self.fo_assert_value('Remitting exchange rate', remitting_exchange_rate)
        if fee_in_remitting_currency:
            self.fo_assert_value('Fee in remitting currency', fee_in_remitting_currency)
        if message_type:
            self.fo_assert_text('Message type', message_type)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('I have checked the input information and agree to send this transaction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references PMT_OITT: {transaction_references}')
        reference_number_out=self.fo_get_text('Reference number')
        print(f'F8: Reference number: {reference_number_out}')
        return transaction_references, reference_number_out

    # PMT_IITT: 6612: Inward international bank
    def pmt_iitt(self, product_code=None, message_code=None, ordering_institution=None, sender_id=None, sender_address=None, sender_name=None, sender_phone=None, sender_type=None, receiver_name=None, receiver_id=None, receiver_address=None, receiver_phone=None, receiver_type=None, country=None, purpose=None, sender_to_receiver_information=None, goods_type=None, goods_list=None, receive_by=None, account_number=None, receive_currency=None, cross_rate=None, reverse_rate=None, display_rate=None, amount_before_fees=None, description=None, detail_of_charges=None, nostro_bank=None, reference_number=None, remitting_currency=None, remitting_amount=None, remitting_exchange_rate_bcy=None, remitting_amount_in_bcy=None, commission_in_remitting_currency=None, original_cross_rate=None, commission=None, amount_customer_receives=None, receive_exchange_rate_bcy=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('PMT_IITT', '6612')
        self.wait_for_button_available('Accept')
        self.assert_form_title('6612: Inward international bank')
        # enter value
        if product_code:
            self.fo_write_text('Product Code', product_code)
        if message_code:
            self.lookup_data('Message code', 'Code', message_code)
        if ordering_institution:
            self.fo_write_text_group('Ordering Institution', ordering_institution)
        if sender_id:
            self.fo_write_text('Sender id', sender_id)
        if sender_address:
            self.fo_write_text('Sender address', sender_address)
        if sender_name:
            self.fo_write_text('Sender name', sender_name)
        if sender_phone:
            self.fo_write_text('Sender phone', sender_phone)
        self.key_escape()
        if sender_type:
            self.fo_select('Sender type', sender_type)
        if receiver_name:
            self.fo_write_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_write_text('Receiver id', receiver_id)
        if receiver_address:
            self.fo_write_text('Receiver address', receiver_address)
        if receiver_phone:
            self.fo_write_text('Receiver phone', receiver_phone)
        self.key_escape()
        if receiver_type:
            self.fo_select('Receiver type', receiver_type)
        self.key_escape()
        if country:
            self.fo_select('Country', country)
        self.key_escape()
        if purpose:
            self.fo_select('Purpose', purpose)
        if sender_to_receiver_information:
            self.fo_write_text('Sender to receiver information', sender_to_receiver_information)
        if goods_type:
            self.fo_click_collap('Other information')
            self.fo_select_collap('Other information', 'Goods type', goods_type)
        if goods_list:
            self.fo_click_collap('Other information')
            self.fo_write_text_multi('Other information', 'Goods list', goods_list)
        self.key_escape()
        if receive_by:
            self.fo_select('Receive by', receive_by)
        if account_number:
            self.fo_write_text_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if receive_currency:
            self.fo_select('Receive currency', receive_currency)
        if cross_rate:
            self.fo_write_number('Cross rate', cross_rate)
        if reverse_rate:
            self.fo_write_number('Reverse rate', reverse_rate)
        self.key_escape()
        if display_rate:
            self.fo_select('Display rate', display_rate)
        if amount_before_fees:
            self.fo_write_number('Amount before fees', amount_before_fees)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if detail_of_charges:
            self.fo_select('Detail of charges', detail_of_charges)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if nostro_bank:
            self.fo_assert_text_group('Nostro Bank', nostro_bank)
        if reference_number:
            self.fo_assert_text_group('Reference number', reference_number)
        if remitting_currency:
            self.fo_assert_select('Remitting currency', remitting_currency)
        if remitting_amount:
            self.fo_assert_value('Remitting amount', remitting_amount)
        if remitting_exchange_rate_bcy:
            self.fo_assert_value('Remitting exchange rate/BCY', remitting_exchange_rate_bcy)
        if remitting_amount_in_bcy:
            self.fo_assert_value('Remitting amount in BCY', remitting_amount_in_bcy)
        if commission_in_remitting_currency:
            self.fo_assert_value('Commission in remitting currency', commission_in_remitting_currency)
        if original_cross_rate:
            self.fo_assert_value('Original cross rate', original_cross_rate)
        if commission:
            self.fo_assert_value('Commission', commission)
        if amount_customer_receives:
            self.fo_assert_value('Amount customer receives', amount_customer_receives)
        if receive_exchange_rate_bcy:
            self.fo_assert_value('Receive exchange rate/BCY', receive_exchange_rate_bcy)
        self.wait_loading()
        self.fo_click_checkbox('I have checked the input information and agree to send this transaction.')
        self.wait_loading()
        # click 'Accept'
        self.click_button('Accept')
        # approve
        if approve_later=='Y':
            self.click_button('Later')
        if approve_on_form=='Y':
            self.fo_approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.assert_button_disable('Accept')
            self.switch_to_core_banking()
            self.check_notification('Saved successfully!')
            self.close_voucher()
            if expected_posting:
                self.assert_posting_data(**expected_posting)
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references PMT_IITT: {transaction_references}')
            reference_number_out=self.fo_get_text_group('Reference number')
            print(f'Reference number: {reference_number_out}')
            return transaction_references, reference_number_out

    def pmt_iitt_view(self, transaction_references, product_code=None, message_code=None, ordering_institution=None, sender_id=None, sender_address=None, sender_name=None, sender_phone=None, sender_type=None, receiver_name=None, receiver_id=None, receiver_address=None, receiver_phone=None, receiver_type=None, country=None, purpose=None, sender_to_receiver_information=None, goods_type=None, goods_list=None, receive_by=None, account_number=None, receive_currency=None, cross_rate=None, reverse_rate=None, display_rate=None, amount_before_fees=None, description=None, detail_of_charges=None, nostro_bank=None, reference_number=None, remitting_currency=None, remitting_amount=None, remitting_exchange_rate_bcy=None, remitting_amount_in_bcy=None, commission_in_remitting_currency=None, original_cross_rate=None, commission=None, amount_customer_receives=None, receive_exchange_rate_bcy=None, expected_posting=None):
        self.transaction_view(transaction_references, '6612: Inward international bank')
        # compare value
        if product_code:
            self.fo_assert_text('Product Code', product_code)
        if message_code:
            self.fo_assert_value('Message code', message_code)
        if ordering_institution:
            self.fo_assert_text_group('Ordering Institution', ordering_institution)
        if sender_id:
            self.fo_assert_text('Sender id', sender_id)
        if sender_address:
            self.fo_assert_text('Sender address', sender_address)
        if sender_name:
            self.fo_assert_text('Sender name', sender_name)
        if sender_phone:
            self.fo_assert_text('Sender phone', sender_phone)
        if sender_type:
            self.fo_assert_select('Sender type', sender_type)
        if receiver_name:
            self.fo_assert_text('Receiver name', receiver_name)
        if receiver_id:
            self.fo_assert_text('Receiver id', receiver_id)
        if receiver_address:
            self.fo_assert_text('Receiver address', receiver_address)
        if receiver_phone:
            self.fo_assert_text('Receiver phone', receiver_phone)
        if receiver_type:
            self.fo_assert_select('Receiver type', receiver_type)
        if country:
            self.fo_assert_select('Country', country)
        if purpose:
            self.fo_assert_select('Purpose', purpose)
        if sender_to_receiver_information:
            self.fo_assert_text('Sender to receiver information', sender_to_receiver_information)
        if goods_type:
            self.fo_click_collap('Other information')
            self.fo_assert_value_multi('Other information', 'Goods type', goods_type)
        if goods_list:
            self.fo_click_collap('Other information')
            self.fo_assert_text_multi('Other information', 'Goods list', goods_list)
        if receive_by:
            self.fo_assert_select('Receive by', receive_by)
        if account_number:
            self.fo_assert_text_group('Account number', account_number)
        if receive_currency:
            self.fo_assert_select('Receive currency', receive_currency)
        if cross_rate:
            self.fo_assert_value('Cross rate', cross_rate)
        if reverse_rate:
            self.fo_assert_value('Reverse rate', reverse_rate)
        if display_rate:
            self.fo_assert_select('Display rate', display_rate)
        if amount_before_fees:
            self.fo_assert_value('Amount before fees', amount_before_fees)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if detail_of_charges:
            self.fo_assert_select('Detail of charges', detail_of_charges)
        if nostro_bank:
            self.fo_assert_text_group('Nostro Bank', nostro_bank)
        if reference_number:
            self.fo_assert_text_group('Reference number', reference_number)
        if remitting_currency:
            self.fo_assert_select('Remitting currency', remitting_currency)
        if remitting_amount:
            self.fo_assert_value('Remitting amount', remitting_amount)
        if remitting_exchange_rate_bcy:
            self.fo_assert_value('Remitting exchange rate/BCY', remitting_exchange_rate_bcy)
        if remitting_amount_in_bcy:
            self.fo_assert_value('Remitting amount in BCY', remitting_amount_in_bcy)
        if commission_in_remitting_currency:
            self.fo_assert_value('Commission in remitting currency', commission_in_remitting_currency)
        if original_cross_rate:
            self.fo_assert_value('Original cross rate', original_cross_rate)
        if commission:
            self.fo_assert_value('Commission', commission)
        if amount_customer_receives:
            self.fo_assert_value('Amount customer receives', amount_customer_receives)
        if receive_exchange_rate_bcy:
            self.fo_assert_value('Receive exchange rate/BCY', receive_exchange_rate_bcy)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('I have checked the input information and agree to send this transaction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references PMT_IITT: {transaction_references}')
        reference_number_out=self.fo_get_text_group('Reference number')
        print(f'F8: Reference number: {reference_number_out}')
        return transaction_references, reference_number_out

# -------------------------- handle BO - PAYMENT --------------------------
    # PMT-IFC Item Definition
    def payment_ifc_item_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Payment', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-IFC Item Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def payment_ifc_item_definition_advanced_search(self, ifc_code_from=None, ifc_code_to=None, ifc_name=None, value_type=None, ifc_type=None, value_from=None, value_to=None, tenor_from=None, tenor_to=None, tenor_unit=None, active_condition=None, status=None):
        self.close_all_form()
        self.click_menu('Payment', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-IFC Item Definition-Search')
        if ifc_code_from:
            self.adv_search_group('IFC code from', ifc_code_from)
        if ifc_code_to:
            self.adv_search_group('IFC code to', ifc_code_to)
        if ifc_name:
            self.adv_search_text('IFC name', ifc_name)
        self.key_escape()
        if value_type:
            self.adv_search_select('Value type', value_type)
        self.key_escape()
        if ifc_type:
            self.adv_search_select('IFC type', ifc_type)
        if value_from:
            self.adv_search_group('Value from', value_from)
        if value_to:
            self.adv_search_group('Value to', value_to)
        if tenor_from:
            self.adv_search_group('Tenor from', tenor_from)
        if tenor_to:
            self.adv_search_group('Tenor to', tenor_to)
        self.key_escape()
        if tenor_unit:
            self.adv_search_select('Tenor unit', tenor_unit)
        if active_condition:
            self.adv_search_text('Active condition', active_condition)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def payment_ifc_item_definition_add(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, sys_account_names=None, account_aliass=None, list_transaction=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Payment', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('PMT-IFC Item Definition-Add')
        # enter value
        self.bo_click_tab('General information')
        if ifc_name:
            self.bo_write_text('IFC name', ifc_name)
        self.key_escape()
        if ifc_type:
            self.bo_select('IFC type', ifc_type)
        self.key_escape()
        if ifc_sub_type:
            self.bo_select('IFC sub type', ifc_sub_type)
        self.key_escape()
        if val_base:
            self.bo_select('Val base', val_base)
        self.key_escape()
        if is_linked:
            self.bo_select('Is Linked', is_linked)
        if value:
            self.bo_write_number('Value', value)
        if ifc_linkage:
            self.bo_write_text_group('IFC linkage', ifc_linkage)
        self.key_escape()
        if ifc_operator:
            self.bo_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_write_number('Margin value', margin_value)
        self.key_escape()
        if value_type:
            self.bo_select('Value type', value_type)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        if floor_value:
            self.bo_write_number('Floor value', floor_value)
        if ceiling_value:
            self.bo_write_number('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_write_text('Value basis', value_basis)
        if tenor:
            self.bo_write_number_group('Tenor', tenor)
        self.key_escape()
        if tenor_unit:
            self.bo_select_group('Tenor unit', tenor_unit)
        if active_condition:
            self.bo_write_text('Active condition', active_condition)
        self.key_escape()
        if rounding_rule:
            self.bo_select('Rounding rule', rounding_rule)
        self.key_escape()
        if rounding_basis:
            self.bo_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_write_number('Rounding num', rounding_num)
        self.key_escape()
        if share_fee:
            self.bo_select('Share fee', share_fee)
        self.key_escape()
        if ifc_status:
            self.bo_select('IFC status', ifc_status)
        if effect_date:
            self.bo_write_date('Effect Date', effect_date)
        if effect_value:
            self.bo_write_number('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if sys_account_names:
            count = len(sys_account_names)
            if not all(
                len(lst) == count for lst in [
                    account_aliass
                ]
            ):
                raise ValueError("All input lists must have the same length or be None.")
            for i in range(count):
                self.add_gls_entry(i, sys_account_names, account_aliass)
        self.bo_click_tab('List Transaction')
        self.key_escape()
        if list_transaction:
            self.bo_select_multi('List transaction', list_transaction)
        # assert value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action add failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            ifc_code_out=self.bo_get_value('IFC code')
            print(f'IFC code: {ifc_code_out}')
            return ifc_code_out

    def payment_ifc_item_definition_view(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # search
        self.payment_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('PMT-IFC Item Definition-View')
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def payment_ifc_item_definition_update(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, list_transaction=None, list_error_message=None):
        # view
        self.payment_ifc_item_definition_view(ifc_code=ifc_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if ifc_name:
            self.bo_write_text('IFC name', ifc_name)
        self.key_escape()
        if ifc_sub_type:
            self.bo_select('IFC sub type', ifc_sub_type)
        self.key_escape()
        if val_base:
            self.bo_select('Val base', val_base)
        self.key_escape()
        if is_linked:
            self.bo_select('Is Linked', is_linked)
        if value:
            self.bo_write_number('Value', value)
        if ifc_linkage:
            self.bo_write_text_group('IFC linkage', ifc_linkage)
        self.key_escape()
        if ifc_operator:
            self.bo_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_write_number('Margin value', margin_value)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        if floor_value:
            self.bo_write_number('Floor value', floor_value)
        if ceiling_value:
            self.bo_write_number('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_write_text('Value basis', value_basis)
        if tenor:
            self.bo_write_number_group('Tenor', tenor)
        self.key_escape()
        if tenor_unit:
            self.bo_select_group('Tenor', tenor_unit)
        if active_condition:
            self.bo_write_text('Active condition', active_condition)
        self.key_escape()
        if rounding_rule:
            self.bo_select('Rounding rule', rounding_rule)
        self.key_escape()
        if rounding_basis:
            self.bo_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_write_number('Rounding num', rounding_num)
        self.key_escape()
        if share_fee:
            self.bo_select('Share fee', share_fee)
        self.key_escape()
        if ifc_status:
            self.bo_select('IFC status', ifc_status)
        if effect_date:
            self.bo_write_date('Effect Date', effect_date)
        if effect_value:
            self.bo_write_number('Effect Value', effect_value)
        self.bo_click_tab('List Transaction')
        self.key_escape()
        if list_transaction:
            self.bo_select_multi('List transaction', list_transaction)
        # assert value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action update failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            ifc_code_out=self.bo_get_value('IFC code')
            print(f'IFC code: {ifc_code_out}')
            return ifc_code_out

    def payment_ifc_item_definition_delete(self, ifc_code, list_error_message=None, expected_message=None):
        # search
        self.payment_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{ifc_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f'Deleted: {ifc_code}')
            return ifc_code

    # PMT-IFC Auto Fee
    def payment_ifc_auto_fee_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Payment', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-IFC Auto Fee-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def payment_ifc_auto_fee_advanced_search(self, transaction_code=None, transaction_name=None, ifc_code=None, ifc_name=None):
        self.close_all_form()
        self.click_menu('Payment', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-IFC Auto Fee-Search')
        if transaction_code:
            self.adv_search_text('Transaction code', transaction_code)
        if transaction_name:
            self.adv_search_text('Transaction name', transaction_name)
        if ifc_code:
            self.adv_search_text('IFC code', ifc_code)
        if ifc_name:
            self.adv_search_text('IFC name', ifc_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def payment_ifc_auto_fee_add(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Payment', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('PMT-IFC Auto Fee-Add')
        # enter value
        if transaction_code:
            self.bo_write_group_single('Transaction code', transaction_code)
        if ifc_code:
            self.bo_write_text_group_single('IFC code', ifc_code)
        if condition:
            self.bo_write_text_single('Condition', condition)
        if active is True:
            self.bo_click_checkbox_single('Active')
        if active is False:
            self.bo_click_uncheckbox_single('Active')
        if exchange is True:
            self.bo_click_checkbox_single('Exchange')
        if exchange is False:
            self.bo_click_uncheckbox_single('Exchange')
        # assert value
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action add failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            transaction_code_out=self.bo_get_value_group_single('Transaction code')
            print(f'Transaction code: {transaction_code_out}')
            ifc_code_out=self.bo_get_text_group_single('IFC code')
            print(f'IFC code: {ifc_code_out}')
            return transaction_code_out, ifc_code_out

    def payment_ifc_auto_fee_view(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # search
        self.payment_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        if transaction_code:
            self.assert_table_data('Transaction code', 1, transaction_code)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('PMT-IFC Auto Fee-View')
        # verify value
        self.bo_click_tab('General information')
        if transaction_code:
            self.bo_assert_value_group('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group('IFC code', ifc_code)
        if condition:
            self.bo_assert_text('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def payment_ifc_auto_fee_update(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # view
        self.payment_ifc_auto_fee_view(transaction_code=transaction_code, ifc_code=ifc_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if condition:
            self.bo_write_text('Condition', condition)
        if active is True:
            self.bo_click_checkbox('Active')
        if active is False:
            self.bo_click_uncheckbox('Active')
        if exchange is True:
            self.bo_click_checkbox('Exchange')
        if exchange is False:
            self.bo_click_uncheckbox('Exchange')
        # assert value
        self.bo_click_tab('General information')
        if transaction_code:
            self.bo_assert_value_group('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group('IFC code', ifc_code)
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action update failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            transaction_code_out=self.bo_get_value_group('Transaction code')
            print(f'Transaction code: {transaction_code_out}')
            ifc_code_out=self.bo_get_text_group('IFC code')
            print(f'IFC code: {ifc_code_out}')
            return transaction_code_out, ifc_code_out

    def payment_ifc_auto_fee_delete(self, transaction_code=None, ifc_code=None, list_error_message=None, expected_message=None):
        # search
        self.payment_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        if transaction_code:
            self.assert_table_data('Transaction code', 1, transaction_code)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{transaction_code}' and '{ifc_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{transaction_code}' and '{ifc_code}'")
            return transaction_code, ifc_code

    # PMT-Catalogue Definition
    def payment_catalogue_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Payment', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-Catalogue Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def payment_catalogue_definition_advanced_search(self, catalogue_code=None, catalogue_name=None, output_format=None, direction=None, instrument=None, status=None, export_swift_file=None, send_email=None, message_type=None):
        self.close_all_form()
        self.click_menu('Payment', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-Catalogue Definition-Search')
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.adv_search_text('Catalogue name', catalogue_name)
        self.key_escape()
        if output_format:
            self.adv_search_select('Output format', output_format)
        self.key_escape()
        if direction:
            self.adv_search_select('Direction', direction)
        self.key_escape()
        if instrument:
            self.adv_search_select('Instrument', instrument)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.key_escape()
        if export_swift_file:
            self.adv_search_select('Export Swift File', export_swift_file)
        self.key_escape()
        if send_email:
            self.adv_search_select('Send email', send_email)
        self.key_escape()
        if message_type:
            self.adv_search_select('Message type', message_type)
        self.click_button_search_advanced()
        self.wait_loading()

    def payment_catalogue_definition_add(self, catalogue_code=None, catalogue_name=None, output_format=None, direction=None, instrument=None, purpose=None, holding_days=None, status=None, message_type=None, export_swift=None, send_by_email=None, group_code=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Payment', 'Catalogue Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('PMT-Catalogue Definition-Add')
        # enter value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_write('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        self.key_escape()
        if output_format:
            self.bo_select('Output format', output_format)
        self.key_escape()
        if direction:
            self.bo_select('Direction', direction)
        self.key_escape()
        if instrument:
            self.bo_select('Instrument', instrument)
        self.key_escape()
        if purpose:
            self.bo_select('Purpose', purpose)
        if holding_days:
            self.bo_write_number('Holding days', holding_days)
        self.key_escape()
        if status:
            self.bo_select('Status', status)
        self.key_escape()
        if message_type:
            self.bo_select('Message type', message_type)
        self.key_escape()
        if export_swift:
            self.bo_select('Export swift', export_swift)
        self.key_escape()
        if send_by_email:
            self.bo_select('Send by email', send_by_email)
        self.bo_click_tab('Payment instruction group information')
        self.key_escape()
        if group_code:
            self.bo_select('Group code', group_code)
        # assert value
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action add failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            catalogue_code_out=self.bo_get_value('Catalogue code')
            print(f'Catalogue code: {catalogue_code_out}')
            return catalogue_code_out

    def payment_catalogue_definition_view(self, catalogue_code=None, catalogue_name=None, output_format=None, direction=None, instrument=None, purpose=None, holding_days=None, status=None, created_by=None, approved_by=None, message_type=None, export_swift=None, send_by_email=None, group_code=None):
        # search
        self.payment_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('PMT-Catalogue Definition-View')
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if output_format:
            self.bo_assert_select('Output format', output_format)
        if direction:
            self.bo_assert_select('Direction', direction)
        if instrument:
            self.bo_assert_select('Instrument', instrument)
        if purpose:
            self.bo_assert_select('Purpose', purpose)
        if holding_days:
            self.bo_assert_value('Holding days', holding_days)
        if status:
            self.bo_assert_select('Status', status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if message_type:
            self.bo_assert_select('Message type', message_type)
        if export_swift:
            self.bo_assert_select('Export swift', export_swift)
        if send_by_email:
            self.bo_assert_select('Send by email', send_by_email)
        self.bo_click_tab('Payment instruction group information')
        if group_code:
            self.bo_assert_select('Group code', group_code)

    def payment_catalogue_definition_update(self, catalogue_code=None, catalogue_name=None, output_format=None, direction=None, instrument=None, purpose=None, holding_days=None, status=None, created_by=None, approved_by=None, message_type=None, export_swift=None, send_by_email=None, group_code=None, list_error_message=None):
        # view
        self.payment_catalogue_definition_view(catalogue_code=catalogue_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        self.key_escape()
        if output_format:
            self.bo_select('Output format', output_format)
        self.key_escape()
        if direction:
            self.bo_select('Direction', direction)
        self.key_escape()
        if instrument:
            self.bo_select('Instrument', instrument)
        self.key_escape()
        if purpose:
            self.bo_select('Purpose', purpose)
        if holding_days:
            self.bo_write_number('Holding days', holding_days)
        self.key_escape()
        if status:
            self.bo_select('Status', status)
        self.key_escape()
        if message_type:
            self.bo_select('Message type', message_type)
        self.key_escape()
        if export_swift:
            self.bo_select('Export swift', export_swift)
        self.key_escape()
        if send_by_email:
            self.bo_select('Send by email', send_by_email)
        self.bo_click_tab('Payment instruction group information')
        self.key_escape()
        if group_code:
            self.bo_select('Group code', group_code)
        # assert value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action update failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            catalogue_code_out=self.bo_get_value('Catalogue code')
            print(f'Catalogue code: {catalogue_code_out}')
            return catalogue_code_out

    def payment_catalogue_definition_delete(self, catalogue_code, list_error_message=None, expected_message=None):
        # search
        self.payment_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{catalogue_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{catalogue_code}'")
            return catalogue_code

    # PMT-Payment Queue for Inward
    def payment_queue_for_inward_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Payment', 'Payment Queue For Inward')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-Payment Queue for Inward-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def payment_queue_for_inward_advanced_search(self, message_code=None, ref_no=None, tran_reference=None, tran_date=None, message_direction=None, message_type=None, message_status=None, currency=None, amount=None, receive_bank=None, send_bank=None, receive_branch=None, send_branch=None, receiver_id=None, sender_id=None, location=None, branch_approve_status=None, branch_proccess_status=None, payment_center_approve_status=None, payment_center_process_status=None):
        self.close_all_form()
        self.click_menu('Payment', 'Payment Queue For Inward')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-Payment Queue for Inward-Search')
        if message_code:
            self.adv_search_text('Message code', message_code)
        if ref_no:
            self.adv_search_text('Ref no', ref_no)
        if tran_reference:
            self.adv_search_text('Tran reference', tran_reference)
        if tran_date:
            self.adv_search('Tran date', tran_date)
        self.key_escape()
        if message_direction:
            self.adv_search_select('Message direction', message_direction)
        self.key_escape()
        if message_type:
            self.adv_search_select('Message type', message_type)
        self.key_escape()
        if message_status:
            self.adv_search_select('Message status', message_status)
        if currency:
            self.adv_search_text('Currency', currency)
        if amount:
            self.adv_search('Amount', amount)
        if receive_bank:
            self.adv_search_text('Receive bank', receive_bank)
        if send_bank:
            self.adv_search_text('Send bank', send_bank)
        if receive_branch:
            self.adv_search_text('Receive branch', receive_branch)
        if send_branch:
            self.adv_search_text('Send branch', send_branch)
        if receiver_id:
            self.adv_search_text('Receiver id', receiver_id)
        if sender_id:
            self.adv_search_text('Sender id', sender_id)
        self.key_escape()
        if location:
            self.adv_search_select('Location', location)
        self.key_escape()
        if branch_approve_status:
            self.adv_search_select('Branch Approve Status', branch_approve_status)
        self.key_escape()
        if branch_proccess_status:
            self.adv_search_select('Branch Proccess Status', branch_proccess_status)
        self.key_escape()
        if payment_center_approve_status:
            self.adv_search_select('Payment Center Approve Status', payment_center_approve_status)
        self.key_escape()
        if payment_center_process_status:
            self.adv_search_select('Payment Center Process Status', payment_center_process_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def payment_queue_for_inward_view(self, message_code=None, statement_date=None, transaction_references_number=None, message_direction=None, message_type=None, sender_name=None, receiver_name=None, amount=None, paid_amount=None, share_fee_amount=None, share_fee_paid=None, message_status=None, send_bank_code=None, receiver_bank_code=None, user_create=None, who_approve=None, location=None, payment_center_approve_status=None, payment_center_process_status=None, branch_approve_status=None, branch_process_status=None):
        # search
        self.payment_queue_for_inward_simple_search(message_code)
        if message_code:
            self.assert_table_data('Message code', 1, message_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Approve')
        self.assert_form_title('PMT-Payment Queue for Inward-View')
        # verify value
        if message_code:
            self.bo_assert_text_single('Message Code', message_code)
        if statement_date:
            self.bo_assert_date_single('Statement date', statement_date)
        if transaction_references_number:
            self.bo_assert_text_single('Transaction references number', transaction_references_number)
        if message_direction:
            self.bo_assert_select_single('Message direction', message_direction)
        if message_type:
            self.bo_assert_select_single('Message type', message_type)
        if sender_name:
            self.bo_assert_text_single('Sender name', sender_name)
        if receiver_name:
            self.bo_assert_text_single('Receiver name', receiver_name)
        if amount:
            self.bo_assert_value_single('Amount', amount)
        if paid_amount:
            self.bo_assert_value_single('Paid amount', paid_amount)
        if share_fee_amount:
            self.bo_assert_value_single('Share Fee amount', share_fee_amount)
        if share_fee_paid:
            self.bo_assert_value_single('Share Fee paid', share_fee_paid)
        if message_status:
            self.bo_assert_select_single('Message status', message_status)
        if send_bank_code:
            self.bo_assert_text_single('Send bank code', send_bank_code)
        if receiver_bank_code:
            self.bo_assert_text_single('Receiver bank code', receiver_bank_code)
        if user_create:
            self.bo_assert_text_single('User create', user_create)
        if who_approve:
            self.bo_assert_text_single('Who approve', who_approve)
        if location:
            self.bo_assert_select_single('Location', location)
        if payment_center_approve_status:
            self.bo_assert_select_single('Payment Center Approve Status', payment_center_approve_status)
        if payment_center_process_status:
            self.bo_assert_select_single('Payment Center Process Status', payment_center_process_status)
        if branch_approve_status:
            self.bo_assert_select_single('Branch Approve Status', branch_approve_status)
        if branch_process_status:
            self.bo_assert_select_single('Branch Process Status', branch_process_status)

    def payment_queue_for_inward_approve(self, message_code, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None):
        # view
        self.payment_queue_for_inward_view(message_code=message_code)
        # approve
        self.click_button('Approve')
        self.wait_loading()
        if approve_on_form=='Y':
            self.approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.check_notification('Saved successfully!')

    def payment_queue_for_inward_reject(self, message_code, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None):
        # view
        self.payment_queue_for_inward_view(message_code=message_code)
        # reject
        self.click_button('Reject')
        self.wait_loading()
        if approve_on_form=='Y':
            self.approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.check_notification('Saved successfully!')

    # PMT-Payment Queue for Outward
    def payment_queue_for_outward_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Payment', 'Payment Queue For Outward')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-Payment Queue for Outward-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def payment_queue_for_outward_advanced_search(self, message_code=None, ref_no=None, tran_reference=None, tran_date=None, message_direction=None, message_type=None, message_status=None, currency=None, amount=None, receive_bank=None, send_bank=None, receive_branch=None, send_branch=None, receive_id=None, sender_id=None, location=None, branch_approve_status=None, branch_proccess_status=None, payment_center_approve_status=None, payment_center_process_status=None, receive_institution_bank=None, api_status=None):
        self.close_all_form()
        self.click_menu('Payment', 'Payment Queue For Outward')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-Payment Queue for Outward-Search')
        if message_code:
            self.adv_search_text('Message code', message_code)
        if ref_no:
            self.adv_search_text('Ref no', ref_no)
        if tran_reference:
            self.adv_search_text('Tran reference', tran_reference)
        if tran_date:
            self.adv_search('Tran date', tran_date)
        self.key_escape()
        if message_direction:
            self.adv_search_select('Message direction', message_direction)
        self.key_escape()
        if message_type:
            self.adv_search_select('Message type', message_type)
        self.key_escape()
        if message_status:
            self.adv_search_select('Message status', message_status)
        if currency:
            self.adv_search_text('Currency', currency)
        if amount:
            self.adv_search('Amount', amount)
        if receive_bank:
            self.adv_search_text('Receive bank', receive_bank)
        if send_bank:
            self.adv_search_text('Send bank', send_bank)
        if receive_branch:
            self.adv_search_text('Receive branch', receive_branch)
        if send_branch:
            self.adv_search_text('Send branch', send_branch)
        if receive_id:
            self.adv_search_text('Receive id', receive_id)
        if sender_id:
            self.adv_search_text('Sender id', sender_id)
        self.key_escape()
        if location:
            self.adv_search_select('Location', location)
        self.key_escape()
        if branch_approve_status:
            self.adv_search_select('Branch Approve Status', branch_approve_status)
        self.key_escape()
        if branch_proccess_status:
            self.adv_search_select('Branch Proccess Status', branch_proccess_status)
        self.key_escape()
        if payment_center_approve_status:
            self.adv_search_select('Payment Center Approve Status', payment_center_approve_status)
        self.key_escape()
        if payment_center_process_status:
            self.adv_search_select('Payment Center Process Status', payment_center_process_status)
        if receive_institution_bank:
            self.adv_search_text('Receive institution bank', receive_institution_bank)
        if api_status:
            self.adv_search_text('API Status', api_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def payment_queue_for_outward_view(self, message_code=None, statement_date=None, transaction_references_number=None, message_direction=None, message_type=None, sender_id=None, receiver_id=None, sender_name=None, receiver_name=None, amount=None, paid_amount=None, share_fee_amount=None, share_fee_paid=None, message_status=None, send_bank_code=None, receiver_bank_code=None, user_create=None, who_approve=None, location=None, payment_center_approve_status=None, payment_center_process_status=None, branch_approve_status=None, branch_process_status=None):
        # search
        self.payment_queue_for_outward_simple_search(message_code)
        if message_code:
            self.assert_table_data('Message code', 1, message_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Approve')
        self.assert_form_title('PMT-Payment Queue for Outward-View')
        # verify value
        if message_code:
            self.bo_assert_text_single('Message Code', message_code)
        if statement_date:
            self.bo_assert_date_single('Statement date', statement_date)
        if transaction_references_number:
            self.bo_assert_text_single('Transaction references number', transaction_references_number)
        if message_direction:
            self.bo_assert_select_single('Message direction', message_direction)
        if message_type:
            self.bo_assert_select_single('Message type', message_type)
        if sender_id:
            self.bo_assert_text_single('Sender Id ', sender_id)
        if receiver_id:
            self.bo_assert_text_single('Receiver Id', receiver_id)
        if sender_name:
            self.bo_assert_text_single('Sender name', sender_name)
        if receiver_name:
            self.bo_assert_text_single('Receiver name', receiver_name)
        if amount:
            self.bo_assert_value_single('Amount', amount)
        if paid_amount:
            self.bo_assert_value_single('Paid amount', paid_amount)
        if share_fee_amount:
            self.bo_assert_value_single('Share Fee amount', share_fee_amount)
        if share_fee_paid:
            self.bo_assert_value_single('Share Fee paid', share_fee_paid)
        if message_status:
            self.bo_assert_select_single('Message status', message_status)
        if send_bank_code:
            self.bo_assert_text_single('Send bank code', send_bank_code)
        if receiver_bank_code:
            self.bo_assert_text_single('Receiver bank code', receiver_bank_code)
        if user_create:
            self.bo_assert_text_single('User create', user_create)
        if who_approve:
            self.bo_assert_text_single('Who approve', who_approve)
        if location:
            self.bo_assert_select_single('Location', location)
        if payment_center_approve_status:
            self.bo_assert_select_single('Payment Center Approve Status', payment_center_approve_status)
        if payment_center_process_status:
            self.bo_assert_select_single('Payment Center Process Status', payment_center_process_status)
        if branch_approve_status:
            self.bo_assert_select_single('Branch Approve Status', branch_approve_status)
        if branch_process_status:
            self.bo_assert_select_single('Branch Process Status', branch_process_status)

    def payment_queue_for_outward_approve(self, message_code, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None):
        # view
        self.payment_queue_for_outward_view(message_code=message_code)
        # approve
        self.click_button('Approve')
        self.wait_loading()
        if approve_on_form=='Y':
            self.approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.check_notification('Approve successfully')

    def payment_queue_for_outward_reject(self, message_code, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None):
        # view
        self.payment_queue_for_outward_view(message_code=message_code)
        # reject
        self.click_button('Reject')
        self.wait_loading()
        if approve_on_form=='Y':
            self.approve_in_popup(
                username=username,
                password=password,
                reason=reason
            )
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Transaction failed!')
        else:
        # verify success
            self.check_notification('Reject successfully')

    # PMT-Correspondent Bank
    def correspondent_bank_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Administration', 'List', 'Correspondent Bank')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-Correspondent Bank-Search')
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def correspondent_bank_advanced_search(self, bic_code_of_bank=None, bank_name=None, present_country_code=None, bank_type=None, status=None):
        self.close_all_form()
        self.click_menu('Administration', 'List', 'Correspondent Bank')
        self.wait_for_button_available('Search')
        self.assert_form_title('PMT-Correspondent Bank-Search')
        if bic_code_of_bank:
            self.adv_search_text('BIC code of bank', bic_code_of_bank)
        if bank_name:
            self.adv_search_text('Bank name', bank_name)
        self.key_escape()
        if present_country_code:
            self.adv_search_select('Present country code', present_country_code)
        self.key_escape()
        if bank_type:
            self.adv_search_select('Bank type', bank_type)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def correspondent_bank_add(self, bank_id=None, bic_code_swift_code=None, bank_name=None, present_country=None, city_name=None, address=None, code_of_bank_head_office=None, branch_code=None, type_bank=None, vostro_account_1=None, vostro_account_2=None, vostro_account_3=None, more_description=None, status=None, in_short_list=None, instruction_of_the_bank=None, nostro_account_1=None, nostro_account_2=None, nostro_account_3=None, sending_share_fee_rate=None, receiving_share_fee_rate=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Administration', 'List', 'Correspondent Bank')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('PMT-Correspondent Bank-Add')
        # enter value
        if bic_code_swift_code:
            self.bo_write_text_single('BIC Code/ SWIFT Code', bic_code_swift_code)
        if bank_name:
            self.bo_write_text_single('Bank Name', bank_name)
        self.key_escape()
        if present_country:
            self.bo_select_single('Present Country', present_country)
        if city_name:
            self.bo_write_text_single('City Name', city_name)
        if address:
            self.bo_write_text_single('Address', address)
        if code_of_bank_head_office:
            self.bo_write_text_single('Code Of Bank Head Office', code_of_bank_head_office)
        if branch_code:
            self.bo_write_text_single('Branch Code', branch_code)
        self.key_escape()
        if type_bank:
            self.bo_select_single('Type', type_bank)
        if vostro_account_1:
            self.bo_click_collap('Vostro Account')
            self.bo_write_text_multi_single('Vostro Account', 'Vostro Account 1', vostro_account_1)
        if vostro_account_2:
            self.bo_click_collap('Vostro Account')
            self.bo_write_text_multi_single('Vostro Account', 'Vostro Account 2', vostro_account_2)
        if vostro_account_3:
            self.bo_click_collap('Vostro Account')
            self.bo_write_text_multi_single('Vostro Account', 'Vostro Account 3', vostro_account_3)
        if more_description:
            self.bo_write_text_single('More Description', more_description)
        self.key_escape()
        if status:
            self.bo_select_single('Status', status)
        self.key_escape()
        if in_short_list:
            self.bo_select_single('In Short List', in_short_list)
        if instruction_of_the_bank:
            self.bo_write_text_single('Instruction Of The Bank', instruction_of_the_bank)
        if nostro_account_1:
            self.bo_click_collap('Nostro Account')
            self.bo_write_text_multi_single('Nostro Account', 'Nostro Account 1', nostro_account_1)
        if nostro_account_2:
            self.bo_click_collap('Nostro Account')
            self.bo_write_text_multi_single('Nostro Account', 'Nostro Account 2', nostro_account_2)
        if nostro_account_3:
            self.bo_click_collap('Nostro Account')
            self.bo_write_text_multi_single('Nostro Account', 'Nostro Account 3', nostro_account_3)
        if sending_share_fee_rate:
            self.bo_write_number_single('Sending Share Fee Rate', sending_share_fee_rate)
        if receiving_share_fee_rate:
            self.bo_write_number_single('Receiving Share Fee Rate', receiving_share_fee_rate)
        # assert value
        if bank_id:
            self.bo_assert_text_single('Bank ID', bank_id)
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action add failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            bic_code_swift_code_out=self.bo_get_text_single('BIC Code/ SWIFT Code')
            print(f'BIC Code/ SWIFT Code: {bic_code_swift_code_out}')
            return bic_code_swift_code_out

    def correspondent_bank_view(self, bank_id=None, bic_code_swift_code=None, bank_name=None, present_country=None, city_name=None, address=None, code_of_bank_head_office=None, branch_code=None, type_bank=None, vostro_account_1=None, vostro_account_2=None, vostro_account_3=None, more_description=None, status=None, in_short_list=None, instruction_of_the_bank=None, nostro_account_1=None, nostro_account_2=None, nostro_account_3=None, sending_share_fee_rate=None, receiving_share_fee_rate=None):
        # search
        self.correspondent_bank_simple_search(bic_code_swift_code)
        self.assert_table_data('BIC Code Of Bank', 1, bic_code_swift_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('PMT-Correspondent Bank-View')
        # verify value
        self.bo_click_tab('General information')
        if bank_id:
            self.bo_assert_value('Bank ID', bank_id)
        if bic_code_swift_code:
            self.bo_assert_text('BIC Code/ SWIFT Code', bic_code_swift_code)
        if bank_name:
            self.bo_assert_text('Bank Name', bank_name)
        if present_country:
            self.bo_assert_select('Present Country', present_country)
        if city_name:
            self.bo_assert_text('City Name', city_name)
        if address:
            self.bo_assert_text('Address', address)
        if code_of_bank_head_office:
            self.bo_assert_text('Code Of Bank Head Office', code_of_bank_head_office)
        if branch_code:
            self.bo_assert_text('Branch Code', branch_code)
        if type_bank:
            self.bo_assert_select('Type', type_bank)
        if vostro_account_1:
            self.bo_click_collap('Vostro Account')
            self.bo_assert_text_multi('Vostro Account', 'Vostro Account 1', vostro_account_1)
        if vostro_account_2:
            self.bo_click_collap('Vostro Account')
            self.bo_assert_text_multi('Vostro Account', 'Vostro Account 2', vostro_account_2)
        if vostro_account_3:
            self.bo_click_collap('Vostro Account')
            self.bo_assert_text_multi('Vostro Account', 'Vostro Account 3', vostro_account_3)
        if more_description:
            self.bo_assert_text('More Description', more_description)
        if status:
            self.bo_assert_select('Status', status)
        if in_short_list:
            self.bo_assert_select('In Short List', in_short_list)
        if instruction_of_the_bank:
            self.bo_assert_text('Instruction Of The Bank', instruction_of_the_bank)
        if nostro_account_1:
            self.bo_click_collap('Nostro Account')
            self.bo_assert_text_multi('Nostro Account', 'Nostro Account 1', nostro_account_1)
        if nostro_account_2:
            self.bo_click_collap('Nostro Account')
            self.bo_assert_text_multi('Nostro Account', 'Nostro Account 2', nostro_account_2)
        if nostro_account_3:
            self.bo_click_collap('Nostro Account')
            self.bo_assert_text_multi('Nostro Account', 'Nostro Account 3', nostro_account_3)
        if sending_share_fee_rate:
            self.bo_assert_value('Sending Share Fee Rate', sending_share_fee_rate)
        if receiving_share_fee_rate:
            self.bo_assert_value('Receiving Share Fee Rate', receiving_share_fee_rate)

    def correspondent_bank_update(self, bank_id=None, bic_code_swift_code=None, bank_name=None, present_country=None, city_name=None, address=None, code_of_bank_head_office=None, branch_code=None, type_bank=None, vostro_account_1=None, vostro_account_2=None, vostro_account_3=None, more_description=None, status=None, in_short_list=None, instruction_of_the_bank=None, nostro_account_1=None, nostro_account_2=None, nostro_account_3=None, sending_share_fee_rate=None, receiving_share_fee_rate=None, list_error_message=None):
        # view
        self.correspondent_bank_view(bic_code_swift_code=bic_code_swift_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if bic_code_swift_code:
            self.bo_write_text('BIC Code/ SWIFT Code', bic_code_swift_code)
        if bank_name:
            self.bo_write_text('Bank Name', bank_name)
        self.key_escape()
        if present_country:
            self.bo_select('Present Country', present_country)
        if city_name:
            self.bo_write_text('City Name', city_name)
        if address:
            self.bo_write_text('Address', address)
        if code_of_bank_head_office:
            self.bo_write_text('Code Of Bank Head Office', code_of_bank_head_office)
        if branch_code:
            self.bo_write_text('Branch Code', branch_code)
        self.key_escape()
        if type_bank:
            self.bo_select('Type', type_bank)
        if vostro_account_1:
            self.bo_click_collap('Vostro Account')
            self.bo_write_text_multi('Vostro Account', 'Vostro Account 1', vostro_account_1)
        if vostro_account_2:
            self.bo_click_collap('Vostro Account')
            self.bo_write_text_multi('Vostro Account', 'Vostro Account 2', vostro_account_2)
        if vostro_account_3:
            self.bo_click_collap('Vostro Account')
            self.bo_write_text_multi('Vostro Account', 'Vostro Account 3', vostro_account_3)
        if more_description:
            self.bo_write_text('More Description', more_description)
        self.key_escape()
        if status:
            self.bo_select('Status', status)
        self.key_escape()
        if in_short_list:
            self.bo_select('In Short List', in_short_list)
        if instruction_of_the_bank:
            self.bo_write_text('Instruction Of The Bank', instruction_of_the_bank)
        if nostro_account_1:
            self.bo_click_collap('Nostro Account')
            self.bo_write_text_multi('Nostro Account', 'Nostro Account 1', nostro_account_1)
        if nostro_account_2:
            self.bo_click_collap('Nostro Account')
            self.bo_write_text_multi('Nostro Account', 'Nostro Account 2', nostro_account_2)
        if nostro_account_3:
            self.bo_click_collap('Nostro Account')
            self.bo_write_text_multi('Nostro Account', 'Nostro Account 3', nostro_account_3)
        if sending_share_fee_rate:
            self.bo_write_number('Sending Share Fee Rate', sending_share_fee_rate)
        if receiving_share_fee_rate:
            self.bo_write_number('Receiving Share Fee Rate', receiving_share_fee_rate)
        # assert value
        self.bo_click_tab('General information')
        if bank_id:
            self.bo_assert_value('Bank ID', bank_id)
        self.wait_loading()
        # click 'Save'
        self.click_button('Save')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print('Action update failed!')
        else:
        # verify success
            self.assert_button_disable('Save')
            self.check_notification('Saved successfully!')
            self.bo_click_tab('General information')
            bic_code_swift_code_out=self.bo_get_text('BIC Code/ SWIFT Code')
            print(f'BIC Code/ SWIFT Code: {bic_code_swift_code_out}')
            return bic_code_swift_code_out

    def correspondent_bank_delete(self, bic_code_swift_code, list_error_message=None):
        # search
        self.correspondent_bank_simple_search(bic_code_swift_code)
        self.assert_table_data('BIC Code Of Bank', 1, bic_code_swift_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{bic_code_swift_code}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.correspondent_bank_simple_search(bic_code_swift_code)
            self.assert_search_not_found()
            print(f'Deleted: {bic_code_swift_code}')
            return bic_code_swift_code

# -------------------------- handle BO approval - PAYMENT --------------------------
    # PMT-Catalogue Definition - Data Verification
    def payment_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, output_format=None, direction=None, instrument=None, purpose=None, holding_days=None, status=None, message_type=None, export_swift=None, send_by_email=None, group_code=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if output_format:
            self.bo_assert_select('Output format', output_format)
        if direction:
            self.bo_assert_select('Direction', direction)
        if instrument:
            self.bo_assert_select('Instrument', instrument)
        if purpose:
            self.bo_assert_select('Purpose', purpose)
        if holding_days:
            self.bo_assert_value('Holding days', holding_days)
        if status:
            self.bo_assert_select('Status', status)
        if message_type:
            self.bo_assert_select('Message type', message_type)
        if export_swift:
            self.bo_assert_select('Export swift', export_swift)
        if send_by_email:
            self.bo_assert_select('Send by email', send_by_email)
        self.bo_click_tab('Payment instruction group information')
        if group_code:
            self.bo_assert_select('Group code', group_code)

    def payment_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, output_format=None, direction=None, instrument=None, purpose=None, holding_days=None, status=None, created_by=None, approved_by=None, message_type=None, export_swift=None, send_by_email=None, group_code=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if output_format:
            self.bo_assert_select('Output format', output_format)
        if direction:
            self.bo_assert_select('Direction', direction)
        if instrument:
            self.bo_assert_select('Instrument', instrument)
        if purpose:
            self.bo_assert_select('Purpose', purpose)
        if holding_days:
            self.bo_assert_value('Holding days', holding_days)
        if status:
            self.bo_assert_select('Status', status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if message_type:
            self.bo_assert_select('Message type', message_type)
        if export_swift:
            self.bo_assert_select('Export swift', export_swift)
        if send_by_email:
            self.bo_assert_select('Send by email', send_by_email)
        self.bo_click_tab('Payment instruction group information')
        if group_code:
            self.bo_assert_select('Group code', group_code)

    def payment_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, output_format=None, direction=None, instrument=None, status=None, export_swift_file=None, send_email=None, message_type=None):
        # search and verify
        self.payment_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue name', 1, catalogue_name)
        if output_format:
            self.assert_table_data('Output format', 1, output_format)
        if direction:
            self.assert_table_data('Direction', 1, direction)
        if instrument:
            self.assert_table_data('Instrument', 1, instrument)
        if status:
            self.assert_table_data('Status', 1, status)
        if export_swift_file:
            self.assert_table_data('Export Swift File', 1, export_swift_file)
        if send_email:
            self.assert_table_data('Send email', 1, send_email)
        if message_type:
            self.assert_table_data('Message type', 1, message_type)

    # PMT-IFC Item Definition - Data Verification
    def payment_ifc_item_definition_add_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-IFC Item Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor unit', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def payment_ifc_item_definition_update_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-IFC Item Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def payment_ifc_item_definition_search_verify(self, ifc_code, ifc_name=None, value_type=None, ifc_type=None, value=None, tenor=None, tenor_unit=None, active_condition=None, status=None):
        # search and verify
        self.payment_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        # verify value
        self.assert_table_data('IFC code', 1, ifc_code)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)
        if value_type:
            self.assert_table_data('Value type', 1, value_type)
        if ifc_type:
            self.assert_table_data('IFC type', 1, ifc_type)
        if value:
            self.assert_table_data('Value', 1, value)
        if tenor:
            self.assert_table_data('Tenor', 1, tenor)
        if tenor_unit:
            self.assert_table_data('Tenor unit', 1, tenor_unit)
        if active_condition:
            self.assert_table_data('Active condition', 1, active_condition)
        if status:
            self.assert_table_data('Status', 1, status)

    def payment_get_ifc_code(self, ifc_name):
        self.payment_ifc_item_definition_simple_search(ifc_name)
        self.assert_table_data('IFC name', 1, ifc_name)
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('PMT-IFC Item Definition-View')
        self.bo_click_tab('General information')
        ifc_code_out=self.bo_get_value('IFC code')
        print(f'IFC code: {ifc_code_out}')
        return ifc_code_out

    # PMT-IFC Auto Fee - Data Verification
    def payment_ifc_auto_fee_add_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-IFC Auto Fee-Add'
        )
        # verify value
        if transaction_code:
            self.bo_assert_value_group_single('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group_single('IFC code', ifc_code)
        if condition:
            self.bo_assert_text_single('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def payment_ifc_auto_fee_update_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-IFC Auto Fee-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if transaction_code:
            self.bo_assert_value_group('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group('IFC code', ifc_code)
        if condition:
            self.bo_assert_text('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def payment_ifc_auto_fee_search_verify(self, transaction_code, ifc_code, transaction_name=None, ifc_name=None):
        # search
        self.payment_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        # verify value
        self.assert_table_data('Transaction code', 1, transaction_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        if transaction_name:
            self.assert_table_data('Transaction name', 1, transaction_name)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)

