from webui_test.case import *

class CreditActions(TestCase):

# -------------------------- handle FO - CREDIT --------------------------
    # CRD_PLO: Open product limit
    def crd_plo(self, product_limit_name=None, customer_type=None, customer_code=None, reference_id=None, currency=None, limit_amount=None, limit_type=None, description=None, product_limit_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_PLO', 'Open product limit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Open product limit')
        # enter value
        if product_limit_name:
            self.fo_write_text('Product limit name', product_limit_name)
        self.key_escape()
        if customer_type:
            self.fo_select('Customer type', customer_type)
        if customer_code:
            self.fo_write_group('Customer code', str(customer_code).replace('-', ''))
            self.wait_loading()
        if reference_id:
            self.fo_write_text('Reference id', reference_id)
        self.key_escape()
        if currency:
            self.fo_select('Currency', currency)
        if limit_amount:
            self.fo_write_number('Limit amount', limit_amount)
        self.key_escape()
        if limit_type:
            self.fo_select('Limit type', limit_type)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if product_limit_code:
            self.fo_assert_value_group('Product limit code', self.product_limit_code_mask(product_limit_code))
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_PLO: {transaction_references}')
            product_limit_code_out=self.fo_get_value_group('Product limit code')
            print(f'Product limit code: {product_limit_code_out}')
            return transaction_references, product_limit_code_out

    def crd_plo_view(self, transaction_references, product_limit_name=None, customer_type=None, customer_code=None, reference_id=None, currency=None, limit_amount=None, limit_type=None, description=None, product_limit_code=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Open product limit')
        # compare value
        if product_limit_name:
            self.fo_assert_text('Product limit name', product_limit_name)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if reference_id:
            self.fo_assert_text('Reference id', reference_id)
        if currency:
            self.fo_assert_select('Currency', currency)
        if limit_amount:
            self.fo_assert_value('Limit amount', limit_amount)
        if limit_type:
            self.fo_assert_select('Limit type', limit_type)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if product_limit_code:
            self.fo_assert_value_group('Product limit code', self.product_limit_code_mask(product_limit_code))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_PLO: {transaction_references}')
        product_limit_code_out=self.fo_get_value_group('Product limit code')
        print(f'F8: Product limit code: {product_limit_code_out}')
        return transaction_references, product_limit_code_out

    # CRD_PLA: Approve product limit
    def crd_pla(self, product_limit_code=None, description=None, product_limit_name=None, customer_type=None, customer_code=None, reference_id=None, currency=None, credit_limit=None, limit_type=None, status=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_PLA', 'Approve product limit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Approve product limit')
        # enter value
        if product_limit_code:
            self.fo_write_group('Product limit code', str(product_limit_code).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if product_limit_name:
            self.fo_assert_text('Product limit name', product_limit_name)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if reference_id:
            self.fo_assert_text('Reference id', reference_id)
        if currency:
            self.fo_assert_text('Currency', currency)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if limit_type:
            self.fo_assert_select('Limit type', limit_type)
        if status:
            self.fo_assert_select('Status', status)
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
            print(f'Transaction references CRD_PLA: {transaction_references}')
            product_limit_code_out=self.fo_get_value_group('Product limit code')
            print(f'Product limit code: {product_limit_code_out}')
            return transaction_references, product_limit_code_out

    def crd_pla_view(self, transaction_references, product_limit_code=None, description=None, product_limit_name=None, customer_type=None, customer_code=None, reference_id=None, currency=None, credit_limit=None, limit_type=None, status=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Approve product limit')
        # compare value
        if product_limit_code:
            self.fo_assert_value_group('Product limit code', self.product_limit_code_mask(product_limit_code))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if product_limit_name:
            self.fo_assert_text('Product limit name', product_limit_name)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if reference_id:
            self.fo_assert_text('Reference id', reference_id)
        if currency:
            self.fo_assert_text('Currency', currency)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if limit_type:
            self.fo_assert_select('Limit type', limit_type)
        if status:
            self.fo_assert_select('Status', status)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_PLA: {transaction_references}')
        product_limit_code_out=self.fo_get_value_group('Product limit code')
        print(f'F8: Product limit code: {product_limit_code_out}')
        return transaction_references, product_limit_code_out

    # CRD_SPLO: Open sub-product limit
    def crd_splo(self, sub_product_limit_name=None, customer_type=None, customer_code=None, product_limit_code=None, reference_id=None, currency=None, credit_facility=None, limit_amount=None, description=None, sub_product_limit_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_SPLO', 'Open sub product limit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Open sub-product limit')
        # enter value
        if sub_product_limit_name:
            self.fo_write_text('Sub product limit name', sub_product_limit_name)
        self.key_escape()
        if customer_type:
            self.fo_select('Customer type', customer_type)
        if customer_code:
            self.fo_write_group('Customer code', str(customer_code).replace('-', ''))
            self.wait_loading()
        if product_limit_code:
            self.fo_write_group('Product limit code', str(product_limit_code).replace('-', ''))
            self.wait_loading()
        if reference_id:
            self.fo_write_text('Reference id', reference_id)
        self.key_escape()
        if currency:
            self.fo_select('Currency', currency)
        self.key_escape()
        if credit_facility:
            self.fo_select('Credit facility', credit_facility)
        if limit_amount:
            self.fo_write_number('Limit amount', limit_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if sub_product_limit_code:
            self.fo_assert_value_group('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_SPLO: {transaction_references}')
            sub_product_limit_code_out=self.fo_get_value_group('Sub product limit code')
            print(f'Sub product limit code: {sub_product_limit_code_out}')
            return transaction_references, sub_product_limit_code_out

    def crd_splo_view(self, transaction_references, sub_product_limit_name=None, customer_type=None, customer_code=None, product_limit_code=None, reference_id=None, currency=None, credit_facility=None, limit_amount=None, description=None, sub_product_limit_code=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Open sub-product limit')
        # compare value
        if sub_product_limit_name:
            self.fo_assert_text('Sub product limit name', sub_product_limit_name)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if product_limit_code:
            self.fo_assert_value_group('Product limit code', self.product_limit_code_mask(product_limit_code))
        if reference_id:
            self.fo_assert_text('Reference id', reference_id)
        if currency:
            self.fo_assert_select('Currency', currency)
        if credit_facility:
            self.fo_assert_select('Credit facility', credit_facility)
        if limit_amount:
            self.fo_assert_value('Limit amount', limit_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if sub_product_limit_code:
            self.fo_assert_value_group('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_SPLO: {transaction_references}')
        sub_product_limit_code_out=self.fo_get_value_group('Sub product limit code')
        print(f'F8: Sub product limit code: {sub_product_limit_code_out}')
        return transaction_references, sub_product_limit_code_out

    # CRD_SPLA: CRD-Approve Sub Product Limit
    def crd_spla(self, sub_product_limit_code=None, description=None, sub_product_limit_name=None, customer_type=None, customer_code=None, reference_id=None, product_limit_code=None, currency=None, credit_limit=None, status=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_SPLA', 'Approve sub product limit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('CRD-Approve Sub Product Limit')
        # enter value
        if sub_product_limit_code:
            self.fo_write_group('Sub product limit code', str(sub_product_limit_code).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if sub_product_limit_name:
            self.fo_assert_text('Sub product limit name', sub_product_limit_name)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if reference_id:
            self.fo_assert_text('Reference id', reference_id)
        if product_limit_code:
            self.fo_assert_value_group('Product limit code', self.product_limit_code_mask(product_limit_code))
        if currency:
            self.fo_assert_text('Currency', currency)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if status:
            self.fo_assert_select('Status', status)
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
            print(f'Transaction references CRD_SPLA: {transaction_references}')
            sub_product_limit_code_out=self.fo_get_value_group('Sub product limit code')
            print(f'Sub product limit code: {sub_product_limit_code_out}')
            return transaction_references, sub_product_limit_code_out

    def crd_spla_view(self, transaction_references, sub_product_limit_code=None, description=None, sub_product_limit_name=None, customer_type=None, customer_code=None, reference_id=None, product_limit_code=None, currency=None, credit_limit=None, status=None, expected_posting=None):
        self.transaction_view(transaction_references, 'CRD-Approve Sub Product Limit')
        # compare value
        if sub_product_limit_code:
            self.fo_assert_value_group('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if sub_product_limit_name:
            self.fo_assert_text('Sub product limit name', sub_product_limit_name)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if reference_id:
            self.fo_assert_text('Reference id', reference_id)
        if product_limit_code:
            self.fo_assert_value_group('Product limit code', self.product_limit_code_mask(product_limit_code))
        if currency:
            self.fo_assert_text('Currency', currency)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if status:
            self.fo_assert_select('Status', status)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_SPLA: {transaction_references}')
        sub_product_limit_code_out=self.fo_get_value_group('Sub product limit code')
        print(f'F8: Sub product limit code: {sub_product_limit_code_out}')
        return transaction_references, sub_product_limit_code_out

    # CRD_OPN: 5500: Open new credit account
    def crd_opn(self, customer_type=None, customer_code=None, sub_product_limit_code=None, catalogue_code=None, company_name=None, sub_product=None, credit_classification=None, account_holder_name=None, sale_price=None, down_payment=None, down_payment_amount=None, dealer_name=None, type_of_commodity=None, credit_limit=None, margin=None, from_date=None, to_date=None, first_prin_repayment_date=None, first_int_repayment_date=None, grace_period_for_principal=None, branch_cd=None, description=None, purpose_of_loan=None, account_number=None, catalogue_name=None, credit_sub_type=None, credit_facility=None, currency_code=None, maximum_limit=None, interest_rate=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_OPN', '5500')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5500: Open new credit account')
        # enter value
        self.key_escape()
        if customer_type:
            self.fo_select('Customer type', customer_type)
        if customer_code:
            self.fo_write('Customer code', self.no_mask(customer_code))
            self.wait_loading()
        if sub_product_limit_code:
            self.fo_write_group('Sub product limit code', self.no_mask(sub_product_limit_code))
            self.wait_loading()
        if catalogue_code:
            self.fo_write('Catalogue code', catalogue_code)
            self.wait_loading()
        if company_name:
            self.fo_write_text('Company name', company_name)
        self.key_escape()
        if sub_product:
            self.fo_select('Sub-product', sub_product)
        self.key_escape()
        if credit_classification:
            self.fo_select('Credit classification', credit_classification)
        if account_holder_name:
            self.fo_write_text('Account holder name', account_holder_name)
        if sale_price:
            self.fo_write_number('Sale price', sale_price)
        if down_payment:
            self.fo_write_number('Down payment %', down_payment)
        if down_payment_amount:
            self.fo_write_number(' Down payment amount', down_payment_amount)
        if dealer_name:
            self.fo_write_text('Dealer name', dealer_name)
        if type_of_commodity:
            self.fo_write_text('Type of commodity', type_of_commodity)
        if credit_limit:
            self.fo_write_number('Credit limit', credit_limit)
        if margin:
            self.fo_write_number('Margin', margin)
        if from_date:
            self.fo_write_date('From date', from_date)
        if to_date:
            self.fo_write_date('To date', to_date)
        if first_prin_repayment_date:
            self.fo_write_date('First prin. repayment date', first_prin_repayment_date)
        if first_int_repayment_date:
            self.fo_write_date('First int. repayment date', first_int_repayment_date)
        if grace_period_for_principal:
            self.fo_write_number('Grace period for principal', grace_period_for_principal)
        if branch_cd:
            self.fo_write_group('Branch cd', branch_cd)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if purpose_of_loan:
            self.fo_write_text_group('Purpose of loan', purpose_of_loan)
        if account_number:
            self.fo_assert_value_group('Account number', self.credit_account_number_mask(account_number))
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if credit_sub_type:
            self.fo_assert_select('Credit sub type', credit_sub_type)
        if credit_facility:
            self.fo_assert_select('Credit facility', credit_facility)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if maximum_limit:
            self.fo_assert_value('Maximum limit', maximum_limit)
        if interest_rate:
            self.fo_assert_value('Interest rate', interest_rate)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_OPN: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def crd_opn_lookup(self, customer_type=None, customer_code=None, sub_product_limit_code=None, catalogue_code=None, company_name=None, sub_product=None, credit_classification=None, account_holder_name=None, sale_price=None, down_payment=None, down_payment_amount=None, dealer_name=None, type_of_commodity=None, credit_limit=None, margin=None, from_date=None, to_date=None, first_prin_repayment_date=None, first_int_repayment_date=None, grace_period_for_principal=None, branch_cd=None, description=None, purpose_of_loan_name=None, account_number=None, catalogue_name=None, credit_sub_type=None, credit_facility=None, currency_code=None, maximum_limit=None, interest_rate=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_OPN', '5500')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5500: Open new credit account')
        # enter value
        self.key_escape()
        if customer_type:
            self.fo_select('Customer type', customer_type)
        if customer_code:
            customer_code_value = self.no_mask(customer_code)
            self.lookup_data_text(
                title='Customer code',
                value_search_code=customer_code_value,
                value_code=customer_code_value
            )
            self.wait_loading()
        if sub_product_limit_code:
            sub_product_limit_code_value = self.no_mask(sub_product_limit_code)
            self.lookup_data_text(
                title='Sub product limit code',
                value_search_code=sub_product_limit_code_value,
                value_code=sub_product_limit_code_value
            )
            self.wait_loading()
        if catalogue_code:
            self.lookup_data_text(
                title='Catalogue code',
                value_search_code=catalogue_code,
                value_code=catalogue_code
            )
            self.wait_loading()
        if company_name:
            self.fo_write_text('Company name', company_name)
        self.key_escape()
        if sub_product:
            self.fo_select('Sub-product', sub_product)
        self.key_escape()
        if credit_classification:
            self.fo_select('Credit classification', credit_classification)
        if account_holder_name:
            self.fo_write_text('Account holder name', account_holder_name)
        if sale_price:
            self.fo_write_number('Sale price', sale_price)
        if down_payment:
            self.fo_write_number('Down payment %', down_payment)
        if down_payment_amount:
            self.fo_write_number(' Down payment amount', down_payment_amount)
        if dealer_name:
            self.fo_write_text('Dealer name', dealer_name)
        if type_of_commodity:
            self.fo_write_text('Type of commodity', type_of_commodity)
        if credit_limit:
            self.fo_write_number('Credit limit', credit_limit)
        if margin:
            self.fo_write_number('Margin', margin)
        if from_date:
            self.fo_write_date('From date', from_date)
        if to_date:
            self.fo_write_date('To date', to_date)
        if first_prin_repayment_date:
            self.fo_write_date('First prin. repayment date', first_prin_repayment_date)
        if first_int_repayment_date:
            self.fo_write_date('First int. repayment date', first_int_repayment_date)
        if grace_period_for_principal:
            self.fo_write_number('Grace period for principal', grace_period_for_principal)
        if branch_cd:
            self.lookup_data_text(
                title='Branch cd',
                value_search_code=branch_cd,
                value_code=branch_cd
            )
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if purpose_of_loan_name:
            self.lookup_data_text(
                title='Purpose of loan',
                value_search_name=purpose_of_loan_name,
                value_name=purpose_of_loan_name
            )
        if account_number:
            self.fo_assert_value_group('Account number', self.credit_account_number_mask(account_number))
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if credit_sub_type:
            self.fo_assert_select('Credit sub type', credit_sub_type)
        if credit_facility:
            self.fo_assert_select('Credit facility', credit_facility)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if maximum_limit:
            self.fo_assert_value('Maximum limit', maximum_limit)
        if interest_rate:
            self.fo_assert_value('Interest rate', interest_rate)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            transaction_references=self.assert_transaction_number_not_null()
            print(f'Transaction references CRD_OPN: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def crd_opn_view(self, transaction_references, customer_type=None, customer_code=None, sub_product_limit_code=None, catalogue_code=None, company_name=None, sub_product=None, credit_classification=None, account_holder_name=None, sale_price=None, down_payment=None, down_payment_amount=None, dealer_name=None, type_of_commodity=None, credit_limit=None, margin=None, from_date=None, to_date=None, first_prin_repayment_date=None, first_int_repayment_date=None, grace_period_for_principal=None, branch_cd=None, description=None, purpose_of_loan=None, account_number=None, catalogue_name=None, credit_sub_type=None, credit_facility=None, currency_code=None, maximum_limit=None, interest_rate=None, expected_posting=None):
        self.transaction_view(transaction_references, '5500: Open new credit account')
        # compare value
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if sub_product_limit_code:
            self.fo_assert_value_group('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if catalogue_code:
            self.fo_assert_value('Catalogue code', catalogue_code)
        if company_name:
            self.fo_assert_text('Company name', company_name)
        if sub_product:
            self.fo_assert_select('Sub-product', sub_product)
        if credit_classification:
            self.fo_assert_select('Credit classification', credit_classification)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if sale_price:
            self.fo_assert_value('Sale price', sale_price)
        if down_payment:
            self.fo_assert_value('Down payment %', down_payment)
        if down_payment_amount:
            self.fo_assert_value(' Down payment amount', down_payment_amount)
        if dealer_name:
            self.fo_assert_text('Dealer name', dealer_name)
        if type_of_commodity:
            self.fo_assert_text('Type of commodity', type_of_commodity)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if margin:
            self.fo_assert_value('Margin', margin)
        if from_date:
            self.fo_assert_date('From date', from_date)
        if to_date:
            self.fo_assert_date('To date', to_date)
        if first_prin_repayment_date:
            self.fo_assert_date('First prin. repayment date', first_prin_repayment_date)
        if first_int_repayment_date:
            self.fo_assert_date('First int. repayment date', first_int_repayment_date)
        if grace_period_for_principal:
            self.fo_assert_value('Grace period for principal', grace_period_for_principal)
        if branch_cd:
            self.fo_assert_value_group('Branch cd', branch_cd)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if purpose_of_loan:
            self.fo_assert_text_group('Purpose of loan', purpose_of_loan)
        if account_number:
            self.fo_assert_value_group('Account number', self.credit_account_number_mask(account_number))
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if credit_sub_type:
            self.fo_assert_select('Credit sub type', credit_sub_type)
        if credit_facility:
            self.fo_assert_select('Credit facility', credit_facility)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if maximum_limit:
            self.fo_assert_value('Maximum limit', maximum_limit)
        if interest_rate:
            self.fo_assert_value('Interest rate', interest_rate)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_OPN: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # CRD_APR: 5550: Approve credit account
    def crd_apr(self, account_number=None, deposit_account=None, description=None, customer_type=None, account_holder_name=None, catalogue_code=None, catalogue_name=None, currency_code=None, credit_limit=None, interest_rate=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_APR', '5550')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5550: Approve credit account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if deposit_account:
            self.fo_write_group('Deposit account', str(deposit_account).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if catalogue_code:
            self.fo_assert_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.fo_assert_text('Currency code', currency_code)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if interest_rate:
            self.fo_assert_value('Interest rate', interest_rate)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_APR: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def crd_apr_view(self, transaction_references, account_number=None, deposit_account=None, description=None, customer_type=None, account_holder_name=None, catalogue_code=None, catalogue_name=None, currency_code=None, credit_limit=None, interest_rate=None, expected_posting=None):
        self.transaction_view(transaction_references, '5550: Approve credit account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.credit_account_number_mask(account_number))
        if deposit_account:
            self.fo_assert_value_group('Deposit account', self.deposit_account_number_mask(deposit_account))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if catalogue_code:
            self.fo_assert_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.fo_assert_text('Currency code', currency_code)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if interest_rate:
            self.fo_assert_value('Interest rate', interest_rate)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_APR: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # CRD_REJ: 55842: Reject credit account
    def crd_rej(self, account_number=None, description=None, current_status=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_REJ', '55842')
        self.wait_for_button_available('Accept')
        self.assert_form_title('55842: Reject credit account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if current_status:
            self.fo_assert_select('Current status', current_status)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_REJ: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def crd_rej_view(self, transaction_references, account_number=None, description=None, current_status=None, expected_posting=None):
        self.transaction_view(transaction_references, '55842: Reject credit account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.credit_account_number_mask(account_number))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if current_status:
            self.fo_assert_select('Current status', current_status)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_REJ: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # CRD_MDR: 5521: Miscellaneous disbursement
    def crd_mdr(self, credit_account=None, disbursement_amount=None, accounting_account=None, receiver_name=None, receiver_address=None, home=None, office=None, description=None, fee_collect_method=None, schedule_template=None, receiver_code=None, remaining_provision_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_MDR', '5521')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5521: Miscellaneous disbursement')
        # enter value
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        if disbursement_amount:
            self.fo_write_number('Disbursement amount', disbursement_amount)
        if accounting_account:
            self.fo_write_group('Accounting account', str(accounting_account).replace('-', ''))
            self.wait_loading()
        if receiver_name:
            self.fo_write_text('Receiver name', receiver_name)
        if receiver_address:
            self.fo_write_text('Receiver address', receiver_address)
        if home:
            self.fo_click_collap('Receiver description')
            self.fo_write_text_multi('Receiver description', 'Home', home)
        if office:
            self.fo_click_collap('Receiver description')
            self.fo_write_text_multi('Receiver description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        self.key_escape()
        if schedule_template:
            self.fo_select('Schedule template', schedule_template)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if receiver_code:
            self.fo_assert_value('Receiver code', self.customer_code_mask(receiver_code))
        if remaining_provision_amount:
            self.fo_assert_value('Remaining provision amount', remaining_provision_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_MDR: {transaction_references}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            accounting_account_out=self.fo_get_value_group('Accounting account')
            print(f'Accounting account: {accounting_account_out}')
            return transaction_references, credit_account_out, accounting_account_out

    def crd_mdr_view(self, transaction_references, credit_account=None, disbursement_amount=None, accounting_account=None, receiver_name=None, receiver_address=None, home=None, office=None, description=None, fee_collect_method=None, schedule_template=None, receiver_code=None, remaining_provision_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '5521: Miscellaneous disbursement')
        # compare value
        if credit_account:
            self.fo_assert_value_group('Credit account', self.credit_account_number_mask(credit_account))
        if disbursement_amount:
            self.fo_assert_value('Disbursement amount', disbursement_amount)
        if accounting_account:
            self.fo_assert_value_group('Accounting account', self.gl_account_number_mask(accounting_account))
        if receiver_name:
            self.fo_assert_text('Receiver name', receiver_name)
        if receiver_address:
            self.fo_assert_text('Receiver address', receiver_address)
        if home:
            self.fo_click_collap('Receiver description')
            self.fo_assert_text_multi('Receiver description', 'Home', home)
        if office:
            self.fo_click_collap('Receiver description')
            self.fo_assert_text_multi('Receiver description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if schedule_template:
            self.fo_assert_select('Schedule template', schedule_template)
        if receiver_code:
            self.fo_assert_value('Receiver code', self.customer_code_mask(receiver_code))
        if remaining_provision_amount:
            self.fo_assert_value('Remaining provision amount', remaining_provision_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_MDR: {transaction_references}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        accounting_account_out=self.fo_get_value_group('Accounting account')
        print(f'F8: Accounting account: {accounting_account_out}')
        return transaction_references, credit_account_out, accounting_account_out

    # CRD_TDR: 5523: Disbursement by transfer
    def crd_tdr(self, credit_account=None, disbursement_amount_deposit=None, deposit_account=None, deposit_account_name=None, receiver_name=None, receiver_address=None, home=None, office=None, description=None, fee_collect_method=None, schedule_template=None, receiver_code=None, remaining_provision_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_TDR', '5523')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5523: Disbursement by transfer')
        # enter value
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        if disbursement_amount_deposit:
            self.fo_write_number('Disbursement amount (Deposit)', disbursement_amount_deposit)
        if deposit_account:
            self.fo_write_group('Deposit account', str(deposit_account).replace('-', ''))
            self.wait_loading()
        if deposit_account_name:
            self.fo_write_text('Deposit account name', deposit_account_name)
        if receiver_name:
            self.fo_write_text('Receiver name', receiver_name)
        if receiver_address:
            self.fo_write_text('Receiver address', receiver_address)
        if home:
            self.fo_click_collap('Receiver description')
            self.fo_write_text_multi('Receiver description', 'Home', home)
        if office:
            self.fo_click_collap('Receiver description')
            self.fo_write_text_multi('Receiver description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        self.key_escape()
        if schedule_template:
            self.fo_select('Schedule template', schedule_template)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if receiver_code:
            self.fo_assert_value('Receiver code', self.customer_code_mask(receiver_code))
        if remaining_provision_amount:
            self.fo_assert_value('Remaining provision amount', remaining_provision_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_TDR: {transaction_references}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            deposit_account_out=self.fo_get_value_group('Deposit account')
            print(f'Deposit account: {deposit_account_out}')
            return transaction_references, credit_account_out, deposit_account_out

    def crd_tdr_view(self, transaction_references, credit_account=None, disbursement_amount_deposit=None, deposit_account=None, deposit_account_name=None, receiver_name=None, receiver_address=None, home=None, office=None, description=None, fee_collect_method=None, schedule_template=None, receiver_code=None, remaining_provision_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '5523: Disbursement by transfer')
        # compare value
        if credit_account:
            self.fo_assert_value_group('Credit account', self.credit_account_number_mask(credit_account))
        if disbursement_amount_deposit:
            self.fo_assert_value('Disbursement amount (Deposit)', disbursement_amount_deposit)
        if deposit_account:
            self.fo_assert_value_group('Deposit account', self.deposit_account_number_mask(deposit_account))
        if deposit_account_name:
            self.fo_assert_text('Deposit account name', deposit_account_name)
        if receiver_name:
            self.fo_assert_text('Receiver name', receiver_name)
        if receiver_address:
            self.fo_assert_text('Receiver address', receiver_address)
        if home:
            self.fo_click_collap('Receiver description')
            self.fo_assert_text_multi('Receiver description', 'Home', home)
        if office:
            self.fo_click_collap('Receiver description')
            self.fo_assert_text_multi('Receiver description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if schedule_template:
            self.fo_assert_select('Schedule template', schedule_template)
        if receiver_code:
            self.fo_assert_value('Receiver code', self.customer_code_mask(receiver_code))
        if remaining_provision_amount:
            self.fo_assert_value('Remaining provision amount', remaining_provision_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_TDR: {transaction_references}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        deposit_account_out=self.fo_get_value_group('Deposit account')
        print(f'F8: Deposit account: {deposit_account_out}')
        return transaction_references, credit_account_out, deposit_account_out

    # CRD_BLK: 55840: Block credit account
    def crd_blk(self, credit_account=None, customer_name=None, customer_address=None, home=None, office=None, description=None, customer_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_BLK', '55840')
        self.wait_for_button_available('Accept')
        self.assert_form_title('55840: Block credit account')
        # enter value
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if home:
            self.fo_click_collap('Customer description')
            self.fo_write_text_multi('Customer description', 'Home', home)
        if office:
            self.fo_click_collap('Customer description')
            self.fo_write_text_multi('Customer description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
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
            print(f'Transaction references CRD_BLK: {transaction_references}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            return transaction_references, credit_account_out

    def crd_blk_view(self, transaction_references, credit_account=None, customer_name=None, customer_address=None, home=None, office=None, description=None, customer_code=None, expected_posting=None):
        self.transaction_view(transaction_references, '55840: Block credit account')
        # compare value
        if credit_account:
            self.fo_assert_value_group('Credit account', self.credit_account_number_mask(credit_account))
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if home:
            self.fo_click_collap('Customer description')
            self.fo_assert_text_multi('Customer description', 'Home', home)
        if office:
            self.fo_click_collap('Customer description')
            self.fo_assert_text_multi('Customer description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_BLK: {transaction_references}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        return transaction_references, credit_account_out

    # CRD_CAS: CRD-55841: Change Account Status
    def crd_cas(self, account_number=None, new_status=None, description=None, current_status=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_CAS', '55841')
        self.wait_for_button_available('Accept')
        self.assert_form_title('CRD-55841: Change Account Status')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if new_status:
            self.fo_select('New status', new_status)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if current_status:
            self.fo_assert_select('Current status', current_status)
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
            print(f'Transaction references CRD_CAS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def crd_cas_view(self, transaction_references, account_number=None, new_status=None, description=None, current_status=None, expected_posting=None):
        self.transaction_view(transaction_references, 'CRD-55841: Change Account Status')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.credit_account_number_mask(account_number))
        if new_status:
            self.fo_assert_select('New status', new_status)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if current_status:
            self.fo_assert_select('Current status', current_status)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_CAS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # CRD_MIPM: 5511: Miscelaneous interest and principal collection
    def crd_mipm(self, credit_account=None, interest_collect=None, penalty_interest_collect=None, principal_collect=None, penalty_principal_collect=None, gl_account_number=None, payee_name=None, payee_address=None, home=None, office=None, description=None, fee_collect_method=None, interest_due_amount=None, accrued_interest_amount=None, interest_receivable_amount=None, total_interest=None, total_penalty_interest=None, total_principal_amount=None, principal_due_amount=None, total_penalty_principal=None, advance_repayment_principal_mode=None, payee_code=None, value_date=None, remaining_provision_amount=None, total_collect_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_MIPM', '5511')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5511: Miscelaneous interest and principal collection')
        # enter value
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        if interest_collect:
            self.fo_write_number('Interest collect', interest_collect)
        if penalty_interest_collect:
            self.fo_write_number('Penalty interest collect', penalty_interest_collect)
        if principal_collect:
            self.fo_write_number('Principal collect', principal_collect)
        if penalty_principal_collect:
            self.fo_write_number('Penalty principal collect', penalty_principal_collect)
        if gl_account_number:
            self.fo_write_group('GL account number', str(gl_account_number).replace('-', ''))
            self.wait_loading()
        if payee_name:
            self.fo_write_text('Payee name', payee_name)
        if payee_address:
            self.fo_write_text('Payee address', payee_address)
        if home:
            self.fo_click_collap('Payee description')
            self.fo_write_text_multi('Payee description', 'Home', home)
        if office:
            self.fo_click_collap('Payee description')
            self.fo_write_text_multi('Payee description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if interest_due_amount:
            self.fo_assert_value('Interest due amount', interest_due_amount)
        if accrued_interest_amount:
            self.fo_assert_value('Accrued interest amount', accrued_interest_amount)
        if interest_receivable_amount:
            self.fo_assert_value('Interest receivable amount', interest_receivable_amount)
        if total_interest:
            self.fo_assert_value('Total interest', total_interest)
        if total_penalty_interest:
            self.fo_assert_value('Total penalty interest', total_penalty_interest)
        if total_principal_amount:
            self.fo_assert_value('Total principal amount', total_principal_amount)
        if principal_due_amount:
            self.fo_assert_value('Principal due amount', principal_due_amount)
        if total_penalty_principal:
            self.fo_assert_value('Total penalty principal', total_penalty_principal)
        if advance_repayment_principal_mode:
            self.fo_assert_select('Advance repayment principal mode', advance_repayment_principal_mode)
        if payee_code:
            self.fo_assert_value('Payee code', self.customer_code_mask(payee_code))
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if remaining_provision_amount:
            self.fo_assert_value('Remaining provision amount', remaining_provision_amount)
        if total_collect_amount:
            self.fo_assert_value('Total Collect Amount', total_collect_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_MIPM: {transaction_references}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            gl_account_number_out=self.fo_get_value_group('GL account number')
            print(f'GL account number: {gl_account_number_out}')
            return transaction_references, credit_account_out, gl_account_number_out

    def crd_mipm_view(self, transaction_references, credit_account=None, interest_collect=None, penalty_interest_collect=None, principal_collect=None, penalty_principal_collect=None, gl_account_number=None, payee_name=None, payee_address=None, home=None, office=None, description=None, fee_collect_method=None, interest_due_amount=None, accrued_interest_amount=None, interest_receivable_amount=None, total_interest=None, total_penalty_interest=None, total_principal_amount=None, principal_due_amount=None, total_penalty_principal=None, advance_repayment_principal_mode=None, payee_code=None, value_date=None, remaining_provision_amount=None, total_collect_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '5511: Miscelaneous interest and principal collection')
        # compare value
        if credit_account:
            self.fo_assert_value_group('Credit account', self.credit_account_number_mask(credit_account))
        if interest_collect:
            self.fo_assert_value('Interest collect', interest_collect)
        if penalty_interest_collect:
            self.fo_assert_value('Penalty interest collect', penalty_interest_collect)
        if principal_collect:
            self.fo_assert_value('Principal collect', principal_collect)
        if penalty_principal_collect:
            self.fo_assert_value('Penalty principal collect', penalty_principal_collect)
        if gl_account_number:
            self.fo_assert_value_group('GL account number', self.gl_account_number_mask(gl_account_number))
        if payee_name:
            self.fo_assert_text('Payee name', payee_name)
        if payee_address:
            self.fo_assert_text('Payee address', payee_address)
        if home:
            self.fo_click_collap('Payee description')
            self.fo_assert_text_multi('Payee description', 'Home', home)
        if office:
            self.fo_click_collap('Payee description')
            self.fo_assert_text_multi('Payee description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if interest_due_amount:
            self.fo_assert_value('Interest due amount', interest_due_amount)
        if accrued_interest_amount:
            self.fo_assert_value('Accrued interest amount', accrued_interest_amount)
        if interest_receivable_amount:
            self.fo_assert_value('Interest receivable amount', interest_receivable_amount)
        if total_interest:
            self.fo_assert_value('Total interest', total_interest)
        if total_penalty_interest:
            self.fo_assert_value('Total penalty interest', total_penalty_interest)
        if total_principal_amount:
            self.fo_assert_value('Total principal amount', total_principal_amount)
        if principal_due_amount:
            self.fo_assert_value('Principal due amount', principal_due_amount)
        if total_penalty_principal:
            self.fo_assert_value('Total penalty principal', total_penalty_principal)
        if advance_repayment_principal_mode:
            self.fo_assert_select('Advance repayment principal mode', advance_repayment_principal_mode)
        if payee_code:
            self.fo_assert_value('Payee code', self.customer_code_mask(payee_code))
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if remaining_provision_amount:
            self.fo_assert_value('Remaining provision amount', remaining_provision_amount)
        if total_collect_amount:
            self.fo_assert_value('Total Collect Amount', total_collect_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_MIPM: {transaction_references}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        gl_account_number_out=self.fo_get_value_group('GL account number')
        print(f'F8: GL account number: {gl_account_number_out}')
        return transaction_references, credit_account_out, gl_account_number_out

    # CRD_IPCT: 5513: Principal and interest collection by transfer
    def crd_ipct(self, credit_account=None, interest_collect=None, penalty_interest_collect=None, principal_collect=None, penalty_principal_collect=None, deposit_account=None, payee_name=None, payee_address=None, home=None, office=None, description=None, fee_collect_method=None, interest_due_amount=None, accrued_interest_amount=None, interest_receivable_amount=None, total_interest=None, total_penalty_interest=None, total_principal_amount=None, principal_due_amount=None, total_penalty_principal=None, advance_repayment_principal_mode=None, payee_code=None, value_date=None, remaining_provision_amount=None, total_collect_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_IPCT', '5513')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5513: Principal and interest collection by transfer')
        # enter value
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        if interest_collect:
            self.fo_write_number('Interest collect', interest_collect)
        if penalty_interest_collect:
            self.fo_write_number('Penalty interest collect', penalty_interest_collect)
        if principal_collect:
            self.fo_write_number('Principal collect', principal_collect)
        if penalty_principal_collect:
            self.fo_write_number('Penalty principal collect', penalty_principal_collect)
        if deposit_account:
            self.fo_write_group('Deposit account', str(deposit_account).replace('-', ''))
            self.wait_loading()
        if payee_name:
            self.fo_write_text('Payee name', payee_name)
        if payee_address:
            self.fo_write_text('Payee address', payee_address)
        if home:
            self.fo_click_collap('Payee description')
            self.fo_write_text_multi('Payee description', 'Home', home)
        if office:
            self.fo_click_collap('Payee description')
            self.fo_write_text_multi('Payee description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if interest_due_amount:
            self.fo_assert_value('Interest due amount', interest_due_amount)
        if accrued_interest_amount:
            self.fo_assert_value('Accrued interest amount', accrued_interest_amount)
        if interest_receivable_amount:
            self.fo_assert_value('Interest receivable amount', interest_receivable_amount)
        if total_interest:
            self.fo_assert_value('Total interest', total_interest)
        if total_penalty_interest:
            self.fo_assert_value('Total penalty interest', total_penalty_interest)
        if total_principal_amount:
            self.fo_assert_value('Total principal amount', total_principal_amount)
        if principal_due_amount:
            self.fo_assert_value('Principal due amount', principal_due_amount)
        if total_penalty_principal:
            self.fo_assert_value('Total penalty principal', total_penalty_principal)
        if advance_repayment_principal_mode:
            self.fo_assert_select('Advance repayment principal mode', advance_repayment_principal_mode)
        if payee_code:
            self.fo_assert_value('Payee code', self.customer_code_mask(payee_code))
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if remaining_provision_amount:
            self.fo_assert_value('Remaining provision amount', remaining_provision_amount)
        if total_collect_amount:
            self.fo_assert_value('Total Collect Amount', total_collect_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_IPCT: {transaction_references}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            deposit_account_out=self.fo_get_value_group('Deposit account')
            print(f'Deposit account: {deposit_account_out}')
            return transaction_references, credit_account_out, deposit_account_out

    def crd_ipct_view(self, transaction_references, credit_account=None, interest_collect=None, penalty_interest_collect=None, principal_collect=None, penalty_principal_collect=None, deposit_account=None, payee_name=None, payee_address=None, home=None, office=None, description=None, fee_collect_method=None, interest_due_amount=None, accrued_interest_amount=None, interest_receivable_amount=None, total_interest=None, total_penalty_interest=None, total_principal_amount=None, principal_due_amount=None, total_penalty_principal=None, advance_repayment_principal_mode=None, payee_code=None, value_date=None, remaining_provision_amount=None, total_collect_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '5513: Principal and interest collection by transfer')
        # compare value
        if credit_account:
            self.fo_assert_value_group('Credit account', self.credit_account_number_mask(credit_account))
        if interest_collect:
            self.fo_assert_value('Interest collect', interest_collect)
        if penalty_interest_collect:
            self.fo_assert_value('Penalty interest collect', penalty_interest_collect)
        if principal_collect:
            self.fo_assert_value('Principal collect', principal_collect)
        if penalty_principal_collect:
            self.fo_assert_value('Penalty principal collect', penalty_principal_collect)
        if deposit_account:
            self.fo_assert_value_group('Deposit account', self.deposit_account_number_mask(deposit_account))
        if payee_name:
            self.fo_assert_text('Payee name', payee_name)
        if payee_address:
            self.fo_assert_text('Payee address', payee_address)
        if home:
            self.fo_click_collap('Payee description')
            self.fo_assert_text_multi('Payee description', 'Home', home)
        if office:
            self.fo_click_collap('Payee description')
            self.fo_assert_text_multi('Payee description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if interest_due_amount:
            self.fo_assert_value('Interest due amount', interest_due_amount)
        if accrued_interest_amount:
            self.fo_assert_value('Accrued interest amount', accrued_interest_amount)
        if interest_receivable_amount:
            self.fo_assert_value('Interest receivable amount', interest_receivable_amount)
        if total_interest:
            self.fo_assert_value('Total interest', total_interest)
        if total_penalty_interest:
            self.fo_assert_value('Total penalty interest', total_penalty_interest)
        if total_principal_amount:
            self.fo_assert_value('Total principal amount', total_principal_amount)
        if principal_due_amount:
            self.fo_assert_value('Principal due amount', principal_due_amount)
        if total_penalty_principal:
            self.fo_assert_value('Total penalty principal', total_penalty_principal)
        if advance_repayment_principal_mode:
            self.fo_assert_select('Advance repayment principal mode', advance_repayment_principal_mode)
        if payee_code:
            self.fo_assert_value('Payee code', self.customer_code_mask(payee_code))
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if remaining_provision_amount:
            self.fo_assert_value('Remaining provision amount', remaining_provision_amount)
        if total_collect_amount:
            self.fo_assert_value('Total Collect Amount', total_collect_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_IPCT: {transaction_references}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        deposit_account_out=self.fo_get_value_group('Deposit account')
        print(f'F8: Deposit account: {deposit_account_out}')
        return transaction_references, credit_account_out, deposit_account_out

    # CRD_APIFC: 5561: CRD-Adjust Credit Penatly Fee
    def crd_apifc(self, account_number=None, ifc_code=None, adjustment_amount=None, description=None, customer_code=None, account_name=None, current_ifc_amount=None, ifc_type=None, new_ifc_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_APIFC', '5561')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5561: CRD-Adjust Credit Penatly Fee')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if ifc_code:
            self.fo_write_text_group('IFC code', ifc_code)
        if adjustment_amount:
            self.fo_write_number('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if current_ifc_amount:
            self.fo_assert_value('Current IFC amount', current_ifc_amount)
        if ifc_type:
            self.fo_assert_select('IFC Type', ifc_type)
        if new_ifc_amount:
            self.fo_assert_value('New ifc amount', new_ifc_amount)
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
            print(f'Transaction references CRD_APIFC: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def crd_apifc_view(self, transaction_references, account_number=None, ifc_code=None, adjustment_amount=None, description=None, customer_code=None, account_name=None, current_ifc_amount=None, ifc_type=None, new_ifc_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '5561: CRD-Adjust Credit Penatly Fee')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.credit_account_number_mask(account_number))
        if ifc_code:
            self.fo_assert_text_group('IFC code', ifc_code)
        if adjustment_amount:
            self.fo_assert_value('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if current_ifc_amount:
            self.fo_assert_value('Current IFC amount', current_ifc_amount)
        if ifc_type:
            self.fo_assert_select('IFC Type', ifc_type)
        if new_ifc_amount:
            self.fo_assert_value('New ifc amount', new_ifc_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_APIFC: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # CRD_CLA: 5563: Credit limit adjustment
    def crd_cla(self, credit_account=None, adjustment_amount=None, description=None, outstanding_balance=None, current_credit_limit=None, new_credit_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_CLA', '5563')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5563: Credit limit adjustment')
        # enter value
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        if adjustment_amount:
            self.fo_write_number('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if outstanding_balance:
            self.fo_assert_value('Outstanding balance', outstanding_balance)
        if current_credit_limit:
            self.fo_assert_value('Current credit limit', current_credit_limit)
        if new_credit_amount:
            self.fo_assert_value('New credit amount', new_credit_amount)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_CLA: {transaction_references}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            return transaction_references, credit_account_out

    def crd_cla_view(self, transaction_references, credit_account=None, adjustment_amount=None, description=None, outstanding_balance=None, current_credit_limit=None, new_credit_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '5563: Credit limit adjustment')
        # compare value
        if credit_account:
            self.fo_assert_value_group('Credit account', self.credit_account_number_mask(credit_account))
        if adjustment_amount:
            self.fo_assert_value('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if outstanding_balance:
            self.fo_assert_value('Outstanding balance', outstanding_balance)
        if current_credit_limit:
            self.fo_assert_value('Current credit limit', current_credit_limit)
        if new_credit_amount:
            self.fo_assert_value('New credit amount', new_credit_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_CLA: {transaction_references}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        return transaction_references, credit_account_out

    # CRD_EXT: 5598: Extend credit account
    def crd_ext(self, credit_account=None, new_expire_date=None, home=None, office=None, description=None, credit_limit=None, oustanding_balance=None, old_expire_date=None, creditor_name=None, creditor_code=None, creditor_address=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_EXT', '5598')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5598: Extend credit account')
        # enter value
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        if new_expire_date:
            self.fo_write_date('New expire date', new_expire_date)
        if home:
            self.fo_click_collap('Creditor description')
            self.fo_write_text_multi('Creditor description', 'Home', home)
        if office:
            self.fo_click_collap('Creditor description')
            self.fo_write_text_multi('Creditor description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if oustanding_balance:
            self.fo_assert_value('Oustanding balance', oustanding_balance)
        if old_expire_date:
            self.fo_assert_date('Old expire date', old_expire_date)
        if creditor_name:
            self.fo_assert_text('Creditor name', creditor_name)
        if creditor_code:
            self.fo_assert_value('Creditor code', self.customer_code_mask(creditor_code))
        if creditor_address:
            self.fo_assert_text('Creditor address', creditor_address)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_EXT: {transaction_references}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            return transaction_references, credit_account_out

    def crd_ext_view(self, transaction_references, credit_account=None, new_expire_date=None, home=None, office=None, description=None, credit_limit=None, oustanding_balance=None, old_expire_date=None, creditor_name=None, creditor_code=None, creditor_address=None, expected_posting=None):
        self.transaction_view(transaction_references, '5598: Extend credit account')
        # compare value
        if credit_account:
            self.fo_assert_value_group('Credit account', self.credit_account_number_mask(credit_account))
        if new_expire_date:
            self.fo_assert_date('New expire date', new_expire_date)
        if home:
            self.fo_click_collap('Creditor description')
            self.fo_assert_text_multi('Creditor description', 'Home', home)
        if office:
            self.fo_click_collap('Creditor description')
            self.fo_assert_text_multi('Creditor description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if oustanding_balance:
            self.fo_assert_value('Oustanding balance', oustanding_balance)
        if old_expire_date:
            self.fo_assert_date('Old expire date', old_expire_date)
        if creditor_name:
            self.fo_assert_text('Creditor name', creditor_name)
        if creditor_code:
            self.fo_assert_value('Creditor code', self.customer_code_mask(creditor_code))
        if creditor_address:
            self.fo_assert_text('Creditor address', creditor_address)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_EXT: {transaction_references}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        return transaction_references, credit_account_out

    # CRD_IFC: 5562: CRD-Adjust Credit Interest
    def crd_ifc(self, account_number=None, ifc_code=None, adjustment_amount=None, description=None, customer_code=None, account_name=None, current_ifc_amount=None, ifc_type=None, new_ifc_amount=None, adjusted_accrual_interest=None, adjusted_due_interest=None, adjusted_payable_interest=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_IFC', '5562')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5562: CRD-Adjust Credit Interest')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if ifc_code:
            self.fo_write_text_group('IFC code', ifc_code)
        if adjustment_amount:
            self.fo_write_number('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if current_ifc_amount:
            self.fo_assert_value('Current IFC amount', current_ifc_amount)
        if ifc_type:
            self.fo_assert_select('IFC Type', ifc_type)
        if new_ifc_amount:
            self.fo_assert_value('New ifc amount', new_ifc_amount)
        if adjusted_accrual_interest:
            self.fo_assert_value('Adjusted accrual interest', adjusted_accrual_interest)
        if adjusted_due_interest:
            self.fo_assert_value('Adjusted due interest', adjusted_due_interest)
        if adjusted_payable_interest:
            self.fo_assert_value('Adjusted payable interest', adjusted_payable_interest)
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
            print(f'Transaction references CRD_IFC: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def crd_ifc_view(self, transaction_references, account_number=None, ifc_code=None, adjustment_amount=None, description=None, customer_code=None, account_name=None, current_ifc_amount=None, ifc_type=None, new_ifc_amount=None, adjusted_accrual_interest=None, adjusted_due_interest=None, adjusted_payable_interest=None, expected_posting=None):
        self.transaction_view(transaction_references, '5562: CRD-Adjust Credit Interest')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.credit_account_number_mask(account_number))
        if ifc_code:
            self.fo_assert_text_group('IFC code', ifc_code)
        if adjustment_amount:
            self.fo_assert_value('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if current_ifc_amount:
            self.fo_assert_value('Current IFC amount', current_ifc_amount)
        if ifc_type:
            self.fo_assert_select('IFC Type', ifc_type)
        if new_ifc_amount:
            self.fo_assert_value('New ifc amount', new_ifc_amount)
        if adjusted_accrual_interest:
            self.fo_assert_value('Adjusted accrual interest', adjusted_accrual_interest)
        if adjusted_due_interest:
            self.fo_assert_value('Adjusted due interest', adjusted_due_interest)
        if adjusted_payable_interest:
            self.fo_assert_value('Adjusted payable interest', adjusted_payable_interest)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_IFC: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # CRD_NPL: CRD-NPL Processing
    def crd_npl(self, credit_account=None, new_group=None, description=None, current_group=None, principal_amount=None, payable_interest_amount=None, penalty_principal=None, penalty_interest=None, secure_amount=None, shortfall_amount=None, current_provision_amount=None, new_provision_amount=None, credit_account_currency=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_NPL', 'NPL')
        self.wait_for_button_available('Accept')
        self.assert_form_title('CRD-NPL Processing')
        # enter value
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if new_group:
            self.fo_select('New group', new_group)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if current_group:
            self.fo_assert_select('Current group', current_group)
        if principal_amount:
            self.fo_assert_value('Principal amount', principal_amount)
        if payable_interest_amount:
            self.fo_assert_value('Payable interest amount', payable_interest_amount)
        if penalty_principal:
            self.fo_assert_value('Penalty principal', penalty_principal)
        if penalty_interest:
            self.fo_assert_value('Penalty interest', penalty_interest)
        if secure_amount:
            self.fo_assert_value('Secure amount', secure_amount)
        if shortfall_amount:
            self.fo_assert_value('Shortfall amount', shortfall_amount)
        if current_provision_amount:
            self.fo_assert_value('Current provision amount', current_provision_amount)
        if new_provision_amount:
            self.fo_assert_value('New provision amount', new_provision_amount)
        if credit_account_currency:
            self.fo_assert_select('Credit account currency', credit_account_currency)
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
            print(f'Transaction references CRD_NPL: {transaction_references}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            return transaction_references, credit_account_out

    def crd_npl_view(self, transaction_references, credit_account=None, new_group=None, description=None, current_group=None, principal_amount=None, payable_interest_amount=None, penalty_principal=None, penalty_interest=None, secure_amount=None, shortfall_amount=None, current_provision_amount=None, new_provision_amount=None, credit_account_currency=None, expected_posting=None):
        self.transaction_view(transaction_references, 'CRD-NPL Processing')
        # compare value
        if credit_account:
            self.fo_assert_value_group('Credit account', self.credit_account_number_mask(credit_account))
        if new_group:
            self.fo_assert_select('New group', new_group)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if current_group:
            self.fo_assert_select('Current group', current_group)
        if principal_amount:
            self.fo_assert_value('Principal amount', principal_amount)
        if payable_interest_amount:
            self.fo_assert_value('Payable interest amount', payable_interest_amount)
        if penalty_principal:
            self.fo_assert_value('Penalty principal', penalty_principal)
        if penalty_interest:
            self.fo_assert_value('Penalty interest', penalty_interest)
        if secure_amount:
            self.fo_assert_value('Secure amount', secure_amount)
        if shortfall_amount:
            self.fo_assert_value('Shortfall amount', shortfall_amount)
        if current_provision_amount:
            self.fo_assert_value('Current provision amount', current_provision_amount)
        if new_provision_amount:
            self.fo_assert_value('New provision amount', new_provision_amount)
        if credit_account_currency:
            self.fo_assert_select('Credit account currency', credit_account_currency)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_NPL: {transaction_references}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        return transaction_references, credit_account_out

    # CRD_FOC: 5571: Fee collection by cash
    def crd_foc(self, credit_account_number=None, amount_for_fee_calculation=None, description=None, total_fee_on_form=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_FOC', '5571')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5571: Fee collection by cash')
        # enter value
        if credit_account_number:
            self.fo_write_group('Credit account number', str(credit_account_number).replace('-', ''))
            self.wait_loading()
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_FOC: {transaction_references}')
            credit_account_number_out=self.fo_get_value_group('Credit account number')
            print(f'Credit account number: {credit_account_number_out}')
            return transaction_references, credit_account_number_out

    def crd_foc_view(self, transaction_references, credit_account_number=None, amount_for_fee_calculation=None, description=None, total_fee_on_form=None, expected_posting=None):
        self.transaction_view(transaction_references, '5571: Fee collection by cash')
        # compare value
        if credit_account_number:
            self.fo_assert_value_group('Credit account number', self.credit_account_number_mask(credit_account_number))
        if amount_for_fee_calculation:
            self.fo_assert_value('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_FOC: {transaction_references}')
        credit_account_number_out=self.fo_get_value_group('Credit account number')
        print(f'F8: Credit account number: {credit_account_number_out}')
        return transaction_references, credit_account_number_out

    # CRD_FCD: 5572: Fee collection by deposit
    def crd_fcd(self, credit_account_number=None, deposit_account_number=None, amount_for_fee_calculation=None, description=None, total_fee_on_form=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_FCD', '5572')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5572: Fee collection by deposit')
        # enter value
        if credit_account_number:
            self.fo_write_group('Credit account number', str(credit_account_number).replace('-', ''))
            self.wait_loading()
        if deposit_account_number:
            self.fo_write_group('Deposit account number', str(deposit_account_number).replace('-', ''))
            self.wait_loading()
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_FCD: {transaction_references}')
            credit_account_number_out=self.fo_get_value_group('Credit account number')
            print(f'Credit account number: {credit_account_number_out}')
            deposit_account_number_out=self.fo_get_value_group('Deposit account number')
            print(f'Deposit account number: {deposit_account_number_out}')
            return transaction_references, credit_account_number_out, deposit_account_number_out

    def crd_fcd_view(self, transaction_references, credit_account_number=None, deposit_account_number=None, amount_for_fee_calculation=None, description=None, total_fee_on_form=None, expected_posting=None):
        self.transaction_view(transaction_references, '5572: Fee collection by deposit')
        # compare value
        if credit_account_number:
            self.fo_assert_value_group('Credit account number', self.credit_account_number_mask(credit_account_number))
        if deposit_account_number:
            self.fo_assert_value_group('Deposit account number', self.deposit_account_number_mask(deposit_account_number))
        if amount_for_fee_calculation:
            self.fo_assert_value('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_FCD: {transaction_references}')
        credit_account_number_out=self.fo_get_value_group('Credit account number')
        print(f'F8: Credit account number: {credit_account_number_out}')
        deposit_account_number_out=self.fo_get_value_group('Deposit account number')
        print(f'F8: Deposit account number: {deposit_account_number_out}')
        return transaction_references, credit_account_number_out, deposit_account_number_out

    # CRD_FCG: 5573: Miscellaneous fee collection
    def crd_fcg(self, credit_account_number=None, gl_account_number=None, amount_for_fee_calculation=None, description=None, total_fee_on_form=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_FCG', '5573')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5573: Miscellaneous fee collection')
        # enter value
        if credit_account_number:
            self.fo_write_group('Credit account number', str(credit_account_number).replace('-', ''))
            self.wait_loading()
        if gl_account_number:
            self.fo_write_group('GL account number', str(gl_account_number).replace('-', ''))
            self.wait_loading()
        if amount_for_fee_calculation:
            self.fo_write_number('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_FCG: {transaction_references}')
            credit_account_number_out=self.fo_get_value_group('Credit account number')
            print(f'Credit account number: {credit_account_number_out}')
            gl_account_number_out=self.fo_get_value_group('GL account number')
            print(f'GL account number: {gl_account_number_out}')
            return transaction_references, credit_account_number_out, gl_account_number_out

    def crd_fcg_view(self, transaction_references, credit_account_number=None, gl_account_number=None, amount_for_fee_calculation=None, description=None, total_fee_on_form=None, expected_posting=None):
        self.transaction_view(transaction_references, '5573: Miscellaneous fee collection')
        # compare value
        if credit_account_number:
            self.fo_assert_value_group('Credit account number', self.credit_account_number_mask(credit_account_number))
        if gl_account_number:
            self.fo_assert_value_group('GL account number', self.gl_account_number_mask(gl_account_number))
        if amount_for_fee_calculation:
            self.fo_assert_value('Amount for fee calculation', amount_for_fee_calculation)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_FCG: {transaction_references}')
        credit_account_number_out=self.fo_get_value_group('Credit account number')
        print(f'F8: Credit account number: {credit_account_number_out}')
        gl_account_number_out=self.fo_get_value_group('GL account number')
        print(f'F8: GL account number: {gl_account_number_out}')
        return transaction_references, credit_account_number_out, gl_account_number_out

    # CRD_RFC: 55711: Fee refund by cash
    def crd_rfc(self, credit_account_number=None, description=None, total_fee_on_form=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_RFC', '55711')
        self.wait_for_button_available('Accept')
        self.assert_form_title('55711: Fee refund by cash')
        # enter value
        if credit_account_number:
            self.fo_write_group('Credit account number', str(credit_account_number).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_RFC: {transaction_references}')
            credit_account_number_out=self.fo_get_value_group('Credit account number')
            print(f'Credit account number: {credit_account_number_out}')
            return transaction_references, credit_account_number_out

    def crd_rfc_view(self, transaction_references, credit_account_number=None, description=None, total_fee_on_form=None, expected_posting=None):
        self.transaction_view(transaction_references, '55711: Fee refund by cash')
        # compare value
        if credit_account_number:
            self.fo_assert_value_group('Credit account number', self.credit_account_number_mask(credit_account_number))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_RFC: {transaction_references}')
        credit_account_number_out=self.fo_get_value_group('Credit account number')
        print(f'F8: Credit account number: {credit_account_number_out}')
        return transaction_references, credit_account_number_out

    # CRD_RFD: 55721: Fee refund by transfer
    def crd_rfd(self, credit_account_number=None, deposit_account_number=None, description=None, total_fee_on_form=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_RFD', '55721')
        self.wait_for_button_available('Accept')
        self.assert_form_title('55721: Fee refund by transfer')
        # enter value
        if credit_account_number:
            self.fo_write_group('Credit account number', str(credit_account_number).replace('-', ''))
            self.wait_loading()
        if deposit_account_number:
            self.fo_write_group('Deposit account number', str(deposit_account_number).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_RFD: {transaction_references}')
            credit_account_number_out=self.fo_get_value_group('Credit account number')
            print(f'Credit account number: {credit_account_number_out}')
            deposit_account_number_out=self.fo_get_value_group('Deposit account number')
            print(f'Deposit account number: {deposit_account_number_out}')
            return transaction_references, credit_account_number_out, deposit_account_number_out

    def crd_rfd_view(self, transaction_references, credit_account_number=None, deposit_account_number=None, description=None, total_fee_on_form=None, expected_posting=None):
        self.transaction_view(transaction_references, '55721: Fee refund by transfer')
        # compare value
        if credit_account_number:
            self.fo_assert_value_group('Credit account number', self.credit_account_number_mask(credit_account_number))
        if deposit_account_number:
            self.fo_assert_value_group('Deposit account number', self.deposit_account_number_mask(deposit_account_number))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_RFD: {transaction_references}')
        credit_account_number_out=self.fo_get_value_group('Credit account number')
        print(f'F8: Credit account number: {credit_account_number_out}')
        deposit_account_number_out=self.fo_get_value_group('Deposit account number')
        print(f'F8: Deposit account number: {deposit_account_number_out}')
        return transaction_references, credit_account_number_out, deposit_account_number_out

    # CRD_FRG: 55731: Miscellaneous fee refund
    def crd_frg(self, credit_account_number=None, gl_account_number=None, description=None, total_fee_on_form=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_FRG', '55731')
        self.wait_for_button_available('Accept')
        self.assert_form_title('55731: Miscellaneous fee refund')
        # enter value
        if credit_account_number:
            self.fo_write_group('Credit account number', str(credit_account_number).replace('-', ''))
            self.wait_loading()
        if gl_account_number:
            self.fo_write_group('GL account number', str(gl_account_number).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_FRG: {transaction_references}')
            credit_account_number_out=self.fo_get_value_group('Credit account number')
            print(f'Credit account number: {credit_account_number_out}')
            gl_account_number_out=self.fo_get_value_group('GL account number')
            print(f'GL account number: {gl_account_number_out}')
            return transaction_references, credit_account_number_out, gl_account_number_out

    def crd_frg_view(self, transaction_references, credit_account_number=None, gl_account_number=None, description=None, total_fee_on_form=None, expected_posting=None):
        self.transaction_view(transaction_references, '55731: Miscellaneous fee refund')
        # compare value
        if credit_account_number:
            self.fo_assert_value_group('Credit account number', self.credit_account_number_mask(credit_account_number))
        if gl_account_number:
            self.fo_assert_value_group('GL account number', self.gl_account_number_mask(gl_account_number))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if total_fee_on_form:
            self.fo_assert_value('Total fee', total_fee_on_form)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_FRG: {transaction_references}')
        credit_account_number_out=self.fo_get_value_group('Credit account number')
        print(f'F8: Credit account number: {credit_account_number_out}')
        gl_account_number_out=self.fo_get_value_group('GL account number')
        print(f'F8: GL account number: {gl_account_number_out}')
        return transaction_references, credit_account_number_out, gl_account_number_out

    # CRD_CLS: 5590: Close account
    def crd_cls(self, credit_account=None, home=None, office=None, description=None, current_group=None, creditor_name=None, creditor_code=None, creditor_address=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_CLS', '5590')
        self.wait_for_button_available('Accept')
        self.assert_form_title('5590: Close account')
        # enter value
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        if home:
            self.fo_click_collap('Creditor description')
            self.fo_write_text_multi('Creditor description', 'Home', home)
        if office:
            self.fo_click_collap('Creditor description')
            self.fo_write_text_multi('Creditor description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if current_group:
            self.fo_assert_select('Current group', current_group)
        if creditor_name:
            self.fo_assert_text('Creditor name', creditor_name)
        if creditor_code:
            self.fo_assert_value('Creditor code', self.customer_code_mask(creditor_code))
        if creditor_address:
            self.fo_assert_text('Creditor address', creditor_address)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references CRD_CLS: {transaction_references}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            return transaction_references, credit_account_out

    def crd_cls_view(self, transaction_references, credit_account=None, home=None, office=None, description=None, current_group=None, creditor_name=None, creditor_code=None, creditor_address=None, expected_posting=None):
        self.transaction_view(transaction_references, '5590: Close account')
        # compare value
        if credit_account:
            self.fo_assert_value_group('Credit account', self.credit_account_number_mask(credit_account))
        if home:
            self.fo_click_collap('Creditor description')
            self.fo_assert_text_multi('Creditor description', 'Home', home)
        if office:
            self.fo_click_collap('Creditor description')
            self.fo_assert_text_multi('Creditor description', 'Office', office)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if current_group:
            self.fo_assert_select('Current group', current_group)
        if creditor_name:
            self.fo_assert_text('Creditor name', creditor_name)
        if creditor_code:
            self.fo_assert_value('Creditor code', self.customer_code_mask(creditor_code))
        if creditor_address:
            self.fo_assert_text('Creditor address', creditor_address)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_CLS: {transaction_references}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        return transaction_references, credit_account_out

    # CRD_HIS: CRD-5560: History Inquiry
    def crd_his(self, account_number=None, from_date=None, to_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_HIS', '5560')
        self.wait_for_button_available('Accept')
        self.assert_form_title('CRD-5560: History Inquiry')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if from_date:
            self.fo_write_date('From Date', from_date)
        if to_date:
            self.fo_write_date('To Date', to_date)
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
            print(f'Transaction references CRD_HIS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    # CRD_SPAD: CRD-Adjust Sub Product Limit
    def crd_spad(self, sub_product_limit_code=None, adjustment_amount=None, description=None, current_limit=None, avaiable_limit=None, outstanding_balance=None, new_limit_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_SPAD', 'Adjust sub product limit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('CRD-Adjust Sub Product Limit')
        # enter value
        if sub_product_limit_code:
            self.fo_write_group('Sub product limit code', str(sub_product_limit_code).replace('-', ''))
            self.wait_loading()
        if adjustment_amount:
            self.fo_write_number('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if current_limit:
            self.fo_assert_value('Current limit', current_limit)
        if avaiable_limit:
            self.fo_assert_value('Avaiable limit', avaiable_limit)
        if outstanding_balance:
            self.fo_assert_value('Outstanding balance', outstanding_balance)
        if new_limit_amount:
            self.fo_assert_value('New limit amount', new_limit_amount)
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
            print(f'Transaction references CRD_SPAD: {transaction_references}')
            sub_product_limit_code_out=self.fo_get_value_group('Sub product limit code')
            print(f'Sub product limit code: {sub_product_limit_code_out}')
            return transaction_references, sub_product_limit_code_out

    def crd_spad_view(self, transaction_references, sub_product_limit_code=None, adjustment_amount=None, description=None, current_limit=None, avaiable_limit=None, outstanding_balance=None, new_limit_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'CRD-Adjust Sub Product Limit')
        # compare value
        if sub_product_limit_code:
            self.fo_assert_value_group('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if adjustment_amount:
            self.fo_assert_value('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if current_limit:
            self.fo_assert_value('Current limit', current_limit)
        if avaiable_limit:
            self.fo_assert_value('Avaiable limit', avaiable_limit)
        if outstanding_balance:
            self.fo_assert_value('Outstanding balance', outstanding_balance)
        if new_limit_amount:
            self.fo_assert_value('New limit amount', new_limit_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_SPAD: {transaction_references}')
        sub_product_limit_code_out=self.fo_get_value_group('Sub product limit code')
        print(f'F8: Sub product limit code: {sub_product_limit_code_out}')
        return transaction_references, sub_product_limit_code_out

    # CRD_PLAD: CRD-Adjust Product Limit
    def crd_plad(self, product_limit_code=None, adjustment_amount=None, description=None, current_limit=None, avaiable_limit=None, outstanding_balance=None, new_limit_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_PLAD', 'Adjust product limit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('CRD-Adjust Product Limit')
        # enter value
        if product_limit_code:
            self.fo_write_group('Product limit code', str(product_limit_code).replace('-', ''))
            self.wait_loading()
        if adjustment_amount:
            self.fo_write_number('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if current_limit:
            self.fo_assert_value('Current limit', current_limit)
        if avaiable_limit:
            self.fo_assert_value('Avaiable limit', avaiable_limit)
        if outstanding_balance:
            self.fo_assert_value('Outstanding balance', outstanding_balance)
        if new_limit_amount:
            self.fo_assert_value('New limit amount', new_limit_amount)
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
            print(f'Transaction references CRD_PLAD: {transaction_references}')
            product_limit_code_out=self.fo_get_value_group('Product limit code')
            print(f'Product limit code: {product_limit_code_out}')
            return transaction_references, product_limit_code_out

    def crd_plad_view(self, transaction_references, product_limit_code=None, adjustment_amount=None, description=None, current_limit=None, avaiable_limit=None, outstanding_balance=None, new_limit_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'CRD-Adjust Product Limit')
        # compare value
        if product_limit_code:
            self.fo_assert_value_group('Product limit code', self.product_limit_code_mask(product_limit_code))
        if adjustment_amount:
            self.fo_assert_value('Adjustment amount', adjustment_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if current_limit:
            self.fo_assert_value('Current limit', current_limit)
        if avaiable_limit:
            self.fo_assert_value('Avaiable limit', avaiable_limit)
        if outstanding_balance:
            self.fo_assert_value('Outstanding balance', outstanding_balance)
        if new_limit_amount:
            self.fo_assert_value('New limit amount', new_limit_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_PLAD: {transaction_references}')
        product_limit_code_out=self.fo_get_value_group('Product limit code')
        print(f'F8: Product limit code: {product_limit_code_out}')
        return transaction_references, product_limit_code_out

    # CRD_SPLC: CRD-Close Sub Product Limit
    def crd_splc(self, sub_product_limit_code=None, description=None, currency=None, sub_product_limit=None, avaiable_limit=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_SPLC', 'Close sub product limit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('CRD-Close Sub Product Limit')
        # enter value
        if sub_product_limit_code:
            self.fo_write_group('Sub product limit code', str(sub_product_limit_code).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if currency:
            self.fo_assert_text('Currency', currency)
        if sub_product_limit:
            self.fo_assert_value('Sub product limit', sub_product_limit)
        if avaiable_limit:
            self.fo_assert_value('Avaiable limit', avaiable_limit)
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
            print(f'Transaction references CRD_SPLC: {transaction_references}')
            sub_product_limit_code_out=self.fo_get_value_group('Sub product limit code')
            print(f'Sub product limit code: {sub_product_limit_code_out}')
            return transaction_references, sub_product_limit_code_out

    def crd_splc_view(self, transaction_references, sub_product_limit_code=None, description=None, currency=None, sub_product_limit=None, avaiable_limit=None, expected_posting=None):
        self.transaction_view(transaction_references, 'CRD-Close Sub Product Limit')
        # compare value
        if sub_product_limit_code:
            self.fo_assert_value_group('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if currency:
            self.fo_assert_text('Currency', currency)
        if sub_product_limit:
            self.fo_assert_value('Sub product limit', sub_product_limit)
        if avaiable_limit:
            self.fo_assert_value('Avaiable limit', avaiable_limit)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_SPLC: {transaction_references}')
        sub_product_limit_code_out=self.fo_get_value_group('Sub product limit code')
        print(f'F8: Sub product limit code: {sub_product_limit_code_out}')
        return transaction_references, sub_product_limit_code_out

    # CRD_PLC: CRD-Close Product Limit
    def crd_plc(self, product_limit_code=None, description=None, currency=None, product_limit=None, avaiable_limit=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('CRD_PLC', 'Close product limit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('CRD-Close Product Limit')
        # enter value
        if product_limit_code:
            self.fo_write_group('Product limit code', str(product_limit_code).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if currency:
            self.fo_assert_text('Currency', currency)
        if product_limit:
            self.fo_assert_value('Product limit', product_limit)
        if avaiable_limit:
            self.fo_assert_value('Avaiable limit', avaiable_limit)
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
            print(f'Transaction references CRD_PLC: {transaction_references}')
            product_limit_code_out=self.fo_get_value_group('Product limit code')
            print(f'Product limit code: {product_limit_code_out}')
            return transaction_references, product_limit_code_out

    def crd_plc_view(self, transaction_references, product_limit_code=None, description=None, currency=None, product_limit=None, avaiable_limit=None, expected_posting=None):
        self.transaction_view(transaction_references, 'CRD-Close Product Limit')
        # compare value
        if product_limit_code:
            self.fo_assert_value_group('Product limit code', self.product_limit_code_mask(product_limit_code))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if currency:
            self.fo_assert_text('Currency', currency)
        if product_limit:
            self.fo_assert_value('Product limit', product_limit)
        if avaiable_limit:
            self.fo_assert_value('Avaiable limit', avaiable_limit)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references CRD_PLC: {transaction_references}')
        product_limit_code_out=self.fo_get_value_group('Product limit code')
        print(f'F8: Product limit code: {product_limit_code_out}')
        return transaction_references, product_limit_code_out

# -------------------------- handle BO - CREDIT --------------------------
    # CRD-IFC Item Definition
    def credit_ifc_item_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Credit', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-IFC Item Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def credit_ifc_item_definition_advanced_search(self, ifc_code_from=None, ifc_code_to=None, ifc_name=None, value_type=None, ifc_type=None, value_from=None, value_to=None, tenor_from=None, tenor_to=None, tenor_unit=None, active_condition=None, status=None):
        self.close_all_form()
        self.click_menu('Credit', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-IFC Item Definition-Search')
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

    def credit_ifc_item_definition_add(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, sys_account_names=None, account_aliass=None, list_transaction=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Credit', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CRD-IFC Item Definition-Add')
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

    def credit_ifc_item_definition_view(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # search
        self.credit_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-IFC Item Definition-View')
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

    def credit_ifc_item_definition_update(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, list_transaction=None, list_error_message=None):
        # view
        self.credit_ifc_item_definition_view(ifc_code=ifc_code)
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

    def credit_ifc_item_definition_delete(self, ifc_code, list_error_message=None, expected_message=None):
        # search
        self.credit_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
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

    # CRD-IFC Auto Fee
    def credit_ifc_auto_fee_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Credit', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-IFC Auto Fee-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def credit_ifc_auto_fee_advanced_search(self, transaction_code=None, transaction_name=None, ifc_code=None, ifc_name=None):
        self.close_all_form()
        self.click_menu('Credit', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-IFC Auto Fee-Search')
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

    def credit_ifc_auto_fee_add(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Credit', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CRD-IFC Auto Fee-Add')
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

    def credit_ifc_auto_fee_view(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # search
        self.credit_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        if transaction_code:
            self.assert_table_data('Transaction code', 1, transaction_code)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-IFC Auto Fee-View')
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

    def credit_ifc_auto_fee_update(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # view
        self.credit_ifc_auto_fee_view(transaction_code=transaction_code, ifc_code=ifc_code)
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

    def credit_ifc_auto_fee_delete(self, transaction_code, ifc_code, list_error_message=None, expected_message=None):
        # search
        self.credit_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
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

    # CRD-Catalogue Definition
    def credit_catalogue_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Credit', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Catalogue Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def credit_catalogue_definition_advanced_search(self, catalogue_code=None, catalogue_name=None, currency=None, credit_type=None, credit_facility=None, tenor_type=None, status=None):
        self.close_all_form()
        self.click_menu('Credit', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Catalogue Definition-Search')
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.adv_search_text('Catalogue name', catalogue_name)
        if currency:
            self.adv_search_text('Currency', currency)
        self.key_escape()
        if credit_type:
            self.adv_search_select('Credit type', credit_type)
        self.key_escape()
        if credit_facility:
            self.adv_search_select('Credit facility', credit_facility)
        self.key_escape()
        if tenor_type:
            self.adv_search_select('Tenor type', tenor_type)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def credit_catalogue_definition_add(self, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, interest_computation_mode=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, reminder_profile_code=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, ifc_codes=None, sys_account_names=None, account_aliass=None, coa_accounts=None, replace_bys=None, system_account_names=None, business_lines=None, customer_sectors=None, customer_resident_statuss=None, sub_products=None, bank_identifications=None, replace_code=None, email=None, push_notification=None, sms=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Credit', 'Catalogue Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CRD-Catalogue Definition-Add')
        # enter value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_write('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        self.key_escape()
        if secure_type:
            self.bo_select('Secure type', secure_type)
        if secure_rate:
            self.bo_write_number('Secure rate', secure_rate)
        self.key_escape()
        if secured_by_currency:
            self.bo_select('Secured by currency', secured_by_currency)
        self.key_escape()
        if credit_type:
            self.bo_select('Credit type', credit_type)
        self.key_escape()
        if credit_sub_type:
            self.bo_select('Credit sub type', credit_sub_type)
        self.key_escape()
        if tenor_type:
            self.bo_select('Tenor type', tenor_type)
        self.key_escape()
        if interest_computation_mode:
            self.bo_select('Interest computation mode', interest_computation_mode)
        self.key_escape()
        if credit_purpose:
            self.bo_select('Credit purpose', credit_purpose)
        self.key_escape()
        if credit_classification:
            self.bo_select('Credit classification', credit_classification)
        self.key_escape()
        if credit_facility:
            self.bo_select('Credit facility', credit_facility)
        self.key_escape()
        if disbursement_mode:
            self.bo_select('Disbursement mode', disbursement_mode)
        self.key_escape()
        if is_provision:
            self.bo_select('Is provision?', is_provision)
        self.key_escape()
        if classification_option:
            self.bo_select('Classification option', classification_option)
        self.key_escape()
        if status:
            self.bo_select('Status', status)
        if reminder_profile_code:
            self.bo_write('Reminder Profile code', reminder_profile_code)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_write_number_group('Principal collection tenor', principal_collection_tenor)
        self.key_escape()
        if principal_collection_tenor_unit:
            self.bo_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_write_number('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_write_number('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_write_number_group('Interest collection tenor', interest_collection_tenor)
        self.key_escape()
        if interest_collection_tenor_unit:
            self.bo_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_write_number('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_write_number('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_write_number_group('Fine collection tenor', fine_collection_tenor)
        self.key_escape()
        if fine_collection_tenor_unit:
            self.bo_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_write_number('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_write_number('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if watch:
            self.bo_write_number('Watch', watch)
        if substandard:
            self.bo_write_number('Substandard', substandard)
        if doubtful:
            self.bo_write_number('Doubtful', doubtful)
        if loss:
            self.bo_write_number('Loss', loss)
        self.bo_click_tab('IFC information')
        if ifc_codes:
            for ifc_code in ifc_codes:
                self.click_button_in_tab('Add')
                self.wait_loading()
                self.select_table('IFC Code', ifc_code)
                self.click_button_in_tab('Apply')
                self.wait_loading()
        self.bo_click_tab('GLs Information')
        if sys_account_names:
            count = len(sys_account_names)
            if not all(
                len(lst) == count for lst in [
                    account_aliass,
                    coa_accounts if coa_accounts else [None] * count
                ]
            ):
                raise ValueError("All input lists must have the same length or be None.")
            for i in range(count):
                self.add_gls_entry(i, sys_account_names, account_aliass, coa_accounts)
        self.bo_click_tab('Extension Group of Account Information')
        if replace_bys:
            count = len(replace_bys)
            if not all(
                len(lst) == count for lst in [
                    system_account_names, business_lines,
                    customer_sectors or [None] * count,
                    customer_resident_statuss or [None] * count,
                    sub_products or [None] * count,
                    bank_identifications or [None] * count
                ]
            ):
                raise ValueError("All input lists must have the same length or be None.")
            for i in range(count):
                self.add_extension_group_entry(
                    i,
                    replace_bys,
                    system_account_names,
                    business_lines,
                    customer_sectors,
                    customer_resident_statuss,
                    sub_products,
                    bank_identifications,
                    replace_code
                )
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is True:
            self.bo_click_checkbox_multi('Notification type', 'Email')
        if email is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Email')
        if push_notification is True:
            self.bo_click_checkbox_multi('Notification type', 'Push Notification')
        if push_notification is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Push Notification')
        if sms is True:
            self.bo_click_checkbox_multi('Notification type', 'SMS')
        if sms is False:
            self.bo_click_uncheckbox_multi('Notification type', 'SMS')
        # assert value
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
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

    def credit_catalogue_definition_view(self, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, interest_computation_mode=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, reminder_profile_code=None, created_by=None, approved_by=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_account_aliass=None, expected_gls_sys_account_names=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None, email=None, push_notification=None, sms=None):
        # search
        self.credit_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-Catalogue Definition-View')
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if secured_by_currency:
            self.bo_assert_select('Secured by currency', secured_by_currency)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if interest_computation_mode:
            self.bo_assert_select('Interest computation mode', interest_computation_mode)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if status:
            self.bo_assert_select('Status', status)
        if reminder_profile_code:
            self.bo_assert_value('Reminder Profile code', reminder_profile_code)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_assert_value('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_assert_value('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_assert_value('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_assert_value('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_assert_value_group('Fine collection tenor', fine_collection_tenor)
        if fine_collection_tenor_unit:
            self.bo_assert_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_assert_value('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_assert_value('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('IFC Information')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def credit_catalogue_definition_update(self, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, interest_computation_mode=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, reminder_profile_code=None, created_by=None, approved_by=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, email=None, push_notification=None, sms=None, list_error_message=None):
        # view
        self.credit_catalogue_definition_view(catalogue_code=catalogue_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        self.key_escape()
        if secure_type:
            self.bo_select('Secure type', secure_type)
        if secure_rate:
            self.bo_write_number('Secure rate', secure_rate)
        self.key_escape()
        if secured_by_currency:
            self.bo_select('Secured by currency', secured_by_currency)
        self.key_escape()
        if credit_type:
            self.bo_select('Credit type', credit_type)
        self.key_escape()
        if credit_sub_type:
            self.bo_select('Credit sub type', credit_sub_type)
        self.key_escape()
        if tenor_type:
            self.bo_select('Tenor type', tenor_type)
        self.key_escape()
        if interest_computation_mode:
            self.bo_select('Interest computation mode', interest_computation_mode)
        self.key_escape()
        if credit_purpose:
            self.bo_select('Credit purpose', credit_purpose)
        self.key_escape()
        if credit_classification:
            self.bo_select('Credit classification', credit_classification)
        self.key_escape()
        if credit_facility:
            self.bo_select('Credit facility', credit_facility)
        self.key_escape()
        if disbursement_mode:
            self.bo_select('Disbursement mode', disbursement_mode)
        self.key_escape()
        if is_provision:
            self.bo_select('Is provision?', is_provision)
        self.key_escape()
        if classification_option:
            self.bo_select('Classification option', classification_option)
        self.key_escape()
        if status:
            self.bo_select('Status', status)
        if reminder_profile_code:
            self.bo_write('Reminder Profile code', reminder_profile_code)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_write_number_group('Principal collection tenor', principal_collection_tenor)
        self.key_escape()
        if principal_collection_tenor_unit:
            self.bo_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_write_number('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_write_number('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_write_number_group('Interest collection tenor', interest_collection_tenor)
        self.key_escape()
        if interest_collection_tenor_unit:
            self.bo_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_write_number('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_write_number('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_write_number_group('Fine collection tenor', fine_collection_tenor)
        self.key_escape()
        if fine_collection_tenor_unit:
            self.bo_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_write_number('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_write_number('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_write_number('Standard', standard)
        if watch:
            self.bo_write_number('Watch', watch)
        if substandard:
            self.bo_write_number('Substandard', substandard)
        if doubtful:
            self.bo_write_number('Doubtful', doubtful)
        if loss:
            self.bo_write_number('Loss', loss)
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is True:
            self.bo_click_checkbox_multi('Notification type', 'Email')
        if email is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Email')
        if push_notification is True:
            self.bo_click_checkbox_multi('Notification type', 'Push Notification')
        if push_notification is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Push Notification')
        if sms is True:
            self.bo_click_checkbox_multi('Notification type', 'SMS')
        if sms is False:
            self.bo_click_uncheckbox_multi('Notification type', 'SMS')
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

    def credit_catalogue_definition_delete(self, catalogue_code, list_error_message=None, expected_message=None):
        # search
        self.credit_catalogue_definition_simple_search(catalogue_code)
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

    # CRD-Product Limit
    def product_limit_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Credit', 'Product Limit')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Product Limit-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def product_limit_advanced_search(self, product_limit_code=None, product_limit_name=None, customer_type=None, customer_code=None, customer_name=None, limit_type=None, currency=None, limit_amount_from=None, limit_amount_to=None, status=None):
        self.close_all_form()
        self.click_menu('Credit', 'Product Limit')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Product Limit-Search')
        if product_limit_code:
            self.adv_search('Product limit code', str(product_limit_code).replace('-', ''))
        if product_limit_name:
            self.adv_search_text('Product limit name', product_limit_name)
        self.key_escape()
        if customer_type:
            self.adv_search_select('Customer type', customer_type)
        if customer_code:
            self.adv_search('Customer code', str(customer_code).replace('-', ''))
        if customer_name:
            self.adv_search_text('Customer name', customer_name)
        self.key_escape()
        if limit_type:
            self.adv_search_select('Limit type', limit_type)
        if currency:
            self.adv_search_text('Currency', currency)
        if limit_amount_from:
            self.adv_search_group('Limit amount from', limit_amount_from)
        if limit_amount_to:
            self.adv_search_group('Limit amount to', limit_amount_to)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def product_limit_view(self, product_limit_code=None, product_name=None, customer_type=None, customer_code=None, reference_code=None, currency=None, amount=None, available_amount=None, limit_type=None, status=None, created_user=None, approved_user=None, secure_type=None, secure_rate=None):
        # search
        self.product_limit_simple_search(self.no_mask(product_limit_code))
        self.assert_table_data('Product limit code', 1, self.no_mask(product_limit_code))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-Product Limit-View')
        # verify value
        self.bo_click_tab('General information')
        if product_limit_code:
            self.bo_assert_value('Product limit code', self.product_limit_code_mask(product_limit_code))
        if product_name:
            self.bo_assert_text('Product name', product_name)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if customer_code:
            self.bo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if reference_code:
            self.bo_assert_text('Reference code', reference_code)
        if currency:
            self.bo_assert_select('Currency', currency)
        if amount:
            self.bo_assert_value('Amount', amount)
        if available_amount:
            self.bo_assert_value('Available amount', available_amount)
        if limit_type:
            self.bo_assert_select('Limit type', limit_type)
        if status:
            self.bo_assert_select('Status', status)
        if created_user:
            self.bo_assert_text_group('Created user', created_user)
        if approved_user:
            self.bo_assert_text_group('Approved user', approved_user)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)

    def product_limit_update(self, product_limit_code=None, product_name=None, customer_type=None, customer_code=None, reference_code=None, currency=None, amount=None, available_amount=None, limit_type=None, status=None, created_user=None, approved_user=None, secure_type=None, secure_rate=None, list_error_message=None):
        # view
        self.product_limit_view(product_limit_code=product_limit_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if product_name:
            self.bo_write_text('Product name', product_name)
        self.key_escape()
        if customer_type:
            self.bo_select('Customer type', customer_type)
        if customer_code:
            self.bo_write_group('Customer code', customer_code)
        if reference_code:
            self.bo_write_text('Reference code', reference_code)
        self.key_escape()
        if currency:
            self.bo_select('Currency', currency)
        if amount:
            self.bo_write_number('Amount', amount)
        self.key_escape()
        if limit_type:
            self.bo_select('Limit type', limit_type)
        self.key_escape()
        if secure_type:
            self.bo_select('Secure type', secure_type)
        if secure_rate:
            self.bo_write_number('Secure rate', secure_rate)
        # assert value
        self.bo_click_tab('General information')
        if product_limit_code:
            self.bo_assert_value('Product limit code', self.product_limit_code_mask(product_limit_code))
        if available_amount:
            self.bo_assert_value('Available amount', available_amount)
        if status:
            self.bo_assert_select('Status', status)
        if created_user:
            self.bo_assert_text_group('Created user', created_user)
        if approved_user:
            self.bo_assert_text_group('Approved user', approved_user)
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
            product_limit_code_out=self.bo_get_value('Product limit code')
            print(f'Product limit code: {product_limit_code_out}')
            return product_limit_code_out

    # CRD-Sub Product Limit
    def sub_product_limit_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Credit', 'Sub Product Limit')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Sub Product Limit-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def sub_product_limit_advanced_search(self, sub_product_limit_code=None, sub_product_limit_name=None, product_limit_code=None, customer_type=None, customer_code=None, customer_name=None, currency=None, limit_amount_from=None, limit_amount_to=None, status=None):
        self.close_all_form()
        self.click_menu('Credit', 'Sub Product Limit')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Sub Product Limit-Search')
        if sub_product_limit_code:
            self.adv_search('Sub product limit code', str(sub_product_limit_code).replace('-', ''))
        if sub_product_limit_name:
            self.adv_search_text('Sub product limit name', sub_product_limit_name)
        if product_limit_code:
            self.adv_search('Product limit code', str(product_limit_code).replace('-', ''))
        self.key_escape()
        if customer_type:
            self.adv_search_select('Customer type', customer_type)
        if customer_code:
            self.adv_search('Customer code', str(customer_code).replace('-', ''))
        if customer_name:
            self.adv_search_text('Customer name', customer_name)
        if currency:
            self.adv_search_text('Currency', currency)
        if limit_amount_from:
            self.adv_search_group('Limit amount from', limit_amount_from)
        if limit_amount_to:
            self.adv_search_group('Limit amount to', limit_amount_to)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def sub_product_limit_view(self, sub_product_limit_code=None, sub_product_name=None, customer_type=None, customer_code=None, product_code=None, reference_code=None, currency=None, amount=None, available_amount=None, credit_facility=None, status=None, created_user=None, approved_user=None):
        # search
        self.sub_product_limit_simple_search(self.no_mask(sub_product_limit_code))
        self.assert_table_data('Sub product limit code', 1, self.no_mask(sub_product_limit_code))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-Sub Product Limit-View')
        # verify value
        self.bo_click_tab('General information')
        if sub_product_limit_code:
            self.bo_assert_value('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if sub_product_name:
            self.bo_assert_text('Sub product name', sub_product_name)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if customer_code:
            self.bo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if product_code:
            self.bo_assert_value_group('Product code', self.product_limit_code_mask(product_code))
        if reference_code:
            self.bo_assert_text('Reference code', reference_code)
        if currency:
            self.bo_assert_select('Currency', currency)
        if amount:
            self.bo_assert_value('Amount', amount)
        if available_amount:
            self.bo_assert_value('Available amount', available_amount)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if status:
            self.bo_assert_select('Status', status)
        if created_user:
            self.bo_assert_text_group('Created user', created_user)
        if approved_user:
            self.bo_assert_text_group('Approved user', approved_user)

    def sub_product_limit_update(self, sub_product_limit_code=None, sub_product_name=None, customer_type=None, customer_code=None, product_code=None, reference_code=None, currency=None, amount=None, available_amount=None, credit_facility=None, status=None, created_user=None, approved_user=None, list_error_message=None):
        # view
        self.sub_product_limit_view(sub_product_limit_code=sub_product_limit_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if sub_product_name:
            self.bo_write_text('Sub product name', sub_product_name)
        if reference_code:
            self.bo_write_text('Reference code', reference_code)
        self.key_escape()
        if currency:
            self.bo_select('Currency', currency)
        if amount:
            self.bo_write_number('Amount', amount)
        self.key_escape()
        if credit_facility:
            self.bo_select('Credit facility', credit_facility)
        # assert value
        self.bo_click_tab('General information')
        if sub_product_limit_code:
            self.bo_assert_value('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if customer_code:
            self.bo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if product_code:
            self.bo_assert_value_group('Product code', self.product_limit_code_mask(product_code))
        if available_amount:
            self.bo_assert_value('Available amount', available_amount)
        if status:
            self.bo_assert_select('Status', status)
        if created_user:
            self.bo_assert_text_group('Created user', created_user)
        if approved_user:
            self.bo_assert_text_group('Approved user', approved_user)
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
            sub_product_limit_code_out=self.bo_get_value('Sub product limit code')
            print(f'Sub product limit code: {sub_product_limit_code_out}')
            return sub_product_limit_code_out

    # CRD-Account Information
    def credit_account_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Credit', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Account Information-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def credit_account_advanced_search(self, account_number=None, account_name=None, currency_code=None, customer_code=None, category_code=None, credit_type=None, tenor_type=None, status=None, old_a_c_no=None, sub_product_limit=None):
        self.close_all_form()
        self.click_menu('Credit', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Account Information-Search')
        if account_number:
            self.adv_search_text('Account number', str(account_number).replace('-', ''))
        if account_name:
            self.adv_search_text('Account name', account_name)
        if currency_code:
            self.adv_search_text('Currency code', currency_code)
        if customer_code:
            self.adv_search('Customer code', str(customer_code).replace('-', ''))
        if category_code:
            self.adv_search_text('Category code', category_code)
        self.key_escape()
        if credit_type:
            self.adv_search_select('Credit type', credit_type)
        self.key_escape()
        if tenor_type:
            self.adv_search_select('Tenor type', tenor_type)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        if old_a_c_no:
            self.adv_search_text('Old a/c no', old_a_c_no)
        if sub_product_limit:
            self.adv_search_text('sub product limit', str(sub_product_limit).replace('-', ''))
        self.click_button_search_advanced()
        self.wait_loading()

    def credit_account_view(self, account_number=None, account_name=None, linked_deposit_account=None, application_code=None, currency_code=None, account_holder_type=None, customer_code=None, branch_code=None, status=None, classification_status=None, realize_status=None, ranking_status=None, sub_product_limit_code=None, catalogue_code=None, credit_type=None, credit_sub_type=None, tenor_type=None, credit_facility=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, begin_of_tenor=None, end_of_tenor=None, open_date=None, close_date=None, last_marked_date=None, last_transaction_date=None, sub_product=None, created_by=None, approved_by=None, loan_officer_staff_id=None, dealer_name=None, type_of_commodity=None, purpose_of_loan=None, company_name=None, credit_limit=None, sale_price=None, down_payment=None, down_payment_amount=None, earmark_limit=None, limit_effective_from=None, limit_effective_to=None, limit_from_third_party=None, operative_limit_from_third_party=None, disbursement_amount=None, outstanding_balance=None, installment_amount=None, normal_principal_amount=None, overdue_principal=None, rounded_amount_of_principal=None, write_off_amount_of_principal=None, principal_paid_amount=None, write_off_amount_of_principal_paid=None, provision_of_principal=None, interest_accrual_amount=None, interest_receivable=None, interest_prepaid=None, overdue_interest=None, interest_paid=None, write_off_amount_of_interest_paid=None, outstanding_total=None, provision_of_interest=None, penalty_principle=None, penalty_interest=None, month_average_balance=None, quarter_average_balance=None, semi_annual_average_balance=None, year_average_balance=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quarter_debit=None, quarter_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, first_date_of_principal_repayment=None, first_date_of_interest_payment=None, grace_period_for_principal=None, is_syndicated=None, interest_computation_mode=None, secure_type=None, minimum_secure_rate=None, secure_amount=None, credit_purpose=None, credit_classification=None, disbursement_mode=None, is_restructured=None, is_provision=None, classification_option=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, remark=None, reference_id=None, provision_of_other=None, expected_account_gl_names=None, expected_account_gl_numbers=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_base_values=None, expected_ifc_is_linkeds=None, expected_ifc_values=None, expected_ifc_margin_values=None, expected_ifc_statuses=None, expected_ifc_outstandings=None, expected_ifc_paids=None, expected_ifc_basic_balances=None, expected_ifc_codes=None, expected_ifc_gl_names=None, expected_ifc_gl_numbers=None, email=None, push_notification=None, sms=None):
        # search
        self.credit_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.credit_account_number_mask(account_number))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-Account Information-View')
        # verify value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_value('Account number', self.credit_account_number_mask(account_number))
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if linked_deposit_account:
            self.bo_assert_value_group('Linked deposit account', self.deposit_account_number_mask(linked_deposit_account))
        if application_code:
            self.bo_assert_text('Application code', application_code)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if account_holder_type:
            self.bo_assert_select('Account holder type', account_holder_type)
        if customer_code:
            self.bo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if branch_code:
            self.bo_assert_text('Branch code', branch_code)
        if status:
            self.bo_assert_select('Status', status)
        if classification_status:
            self.bo_assert_select('Classification status', classification_status)
        if realize_status:
            self.bo_assert_select('Realize status', realize_status)
        if ranking_status:
            self.bo_assert_select('Ranking status', ranking_status)
        if sub_product_limit_code:
            self.bo_assert_value('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if catalogue_code:
            self.bo_assert_text('Catalogue code', catalogue_code)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if principal_collection_tenor:
            self.bo_assert_value('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select('Principal collection tenor', principal_collection_tenor_unit)
        if interest_collection_tenor:
            self.bo_assert_value('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select('Interest collection tenor', interest_collection_tenor_unit)
        if begin_of_tenor:
            self.bo_assert_date('Begin of tenor', begin_of_tenor)
        if end_of_tenor:
            self.bo_assert_date('End of tenor', end_of_tenor)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if last_marked_date:
            self.bo_assert_date('Last marked date', last_marked_date)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if sub_product:
            self.bo_assert_select('Sub product', sub_product)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if loan_officer_staff_id:
            self.bo_assert_value_group('Loan officer staff id', loan_officer_staff_id)
        if dealer_name:
            self.bo_assert_text('Dealer name', dealer_name)
        if type_of_commodity:
            self.bo_assert_text('Type of commodity', type_of_commodity)
        if purpose_of_loan:
            self.bo_assert_value_group('Purpose of loan', purpose_of_loan)
        if company_name:
            self.bo_assert_text_group('Company name', company_name)
        self.bo_click_tab('Outstanding information')
        if credit_limit:
            self.bo_assert_value('Credit limit', credit_limit)
        if sale_price:
            self.bo_assert_value('Sale price', sale_price)
        if down_payment:
            self.bo_assert_value('Down payment %', down_payment)
        if down_payment_amount:
            self.bo_assert_value('Down payment amount', down_payment_amount)
        if earmark_limit:
            self.bo_assert_value('Earmark limit', earmark_limit)
        if limit_effective_from:
            self.bo_assert_date('Limit effective from', limit_effective_from)
        if limit_effective_to:
            self.bo_assert_date('Limit effective to', limit_effective_to)
        if limit_from_third_party:
            self.bo_assert_value('Limit from third party', limit_from_third_party)
        if operative_limit_from_third_party:
            self.bo_assert_value('Operative limit from third party', operative_limit_from_third_party)
        if disbursement_amount:
            self.bo_assert_value('Disbursement amount', disbursement_amount)
        if outstanding_balance:
            self.bo_assert_value('Outstanding balance', outstanding_balance)
        if installment_amount:
            self.bo_assert_value('Installment amount', installment_amount)
        if normal_principal_amount:
            self.bo_assert_value('Normal principal amount', normal_principal_amount)
        if overdue_principal:
            self.bo_assert_value('Overdue principal', overdue_principal)
        if rounded_amount_of_principal:
            self.bo_assert_value('Rounded amount of principal', rounded_amount_of_principal)
        if write_off_amount_of_principal:
            self.bo_assert_value('Write off amount of principal', write_off_amount_of_principal)
        if principal_paid_amount:
            self.bo_assert_value('Principal paid amount', principal_paid_amount)
        if write_off_amount_of_principal_paid:
            self.bo_assert_value('Write off amount of principal paid', write_off_amount_of_principal_paid)
        if provision_of_principal:
            self.bo_assert_value('Provision of principal', provision_of_principal)
        if interest_accrual_amount:
            self.bo_assert_value('Interest accrual amount', interest_accrual_amount)
        if interest_receivable:
            self.bo_assert_value('Interest receivable', interest_receivable)
        if interest_prepaid:
            self.bo_assert_value('Interest prepaid', interest_prepaid)
        if overdue_interest:
            self.bo_assert_value('Overdue interest ', overdue_interest)
        if interest_paid:
            self.bo_assert_value('Interest paid', interest_paid)
        if write_off_amount_of_interest_paid:
            self.bo_assert_value('Write off amount of interest paid', write_off_amount_of_interest_paid)
        if outstanding_total:
            self.bo_assert_value('Outstanding total', outstanding_total)
        if provision_of_interest:
            self.bo_assert_value('Provision of interest', provision_of_interest)
        if penalty_principle:
            self.bo_assert_value('Penalty principle', penalty_principle)
        if penalty_interest:
            self.bo_assert_value('Penalty interest', penalty_interest)
        if month_average_balance:
            self.bo_assert_value('Month average balance', month_average_balance)
        if quarter_average_balance:
            self.bo_assert_value('Quarter average balance', quarter_average_balance)
        if semi_annual_average_balance:
            self.bo_assert_value('Semi-annual average balance', semi_annual_average_balance)
        if year_average_balance:
            self.bo_assert_value('Year average balance', year_average_balance)
        if week_debit:
            self.bo_assert_value('Week debit', week_debit)
        if week_credit:
            self.bo_assert_value('Week credit', week_credit)
        if month_debit:
            self.bo_assert_value('Month debit', month_debit)
        if month_credit:
            self.bo_assert_value('Month credit', month_credit)
        if quarter_debit:
            self.bo_assert_value('Quarter debit', quarter_debit)
        if quarter_credit:
            self.bo_assert_value('Quarter credit', quarter_credit)
        if semi_annual_debit:
            self.bo_assert_value('Semi-annual debit', semi_annual_debit)
        if semi_annual_credit:
            self.bo_assert_value('Semi-annual credit', semi_annual_credit)
        if year_debit:
            self.bo_assert_value('Year debit', year_debit)
        if year_credit:
            self.bo_assert_value('Year credit', year_credit)
        self.bo_click_tab('Term and condition')
        if first_date_of_principal_repayment:
            self.bo_assert_date('First date of principal repayment', first_date_of_principal_repayment)
        if first_date_of_interest_payment:
            self.bo_assert_date('First date of interest payment', first_date_of_interest_payment)
        if grace_period_for_principal:
            self.bo_assert_value('Grace Period For Principal ', grace_period_for_principal)
        if is_syndicated:
            self.bo_assert_select('Is syndicated?', is_syndicated)
        if interest_computation_mode:
            self.bo_assert_select('Interest computation mode', interest_computation_mode)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if minimum_secure_rate:
            self.bo_assert_value('Minimum secure rate', minimum_secure_rate)
        if secure_amount:
            self.bo_assert_value('Secure amount', secure_amount)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_restructured:
            self.bo_assert_select('Is restructured', is_restructured)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('Additional information')
        if remark:
            self.bo_assert_text('Remark', remark)
        if reference_id:
            self.bo_assert_text('Reference id', reference_id)
        if provision_of_other:
            self.bo_assert_value('Provision of other', provision_of_other)
        self.bo_click_tab('Account GLs Information')
        if expected_account_gl_names:
            for account_gl_name, account_gl_number in zip(expected_account_gl_names, expected_account_gl_numbers):
                self.bo_assert_text_table_account_gls(account_gl_name, self.no_mask(account_gl_number))
        self.bo_click_tab('IFC list')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table('IFC code', ifc_code, 'IFC name', ifc_name)
        if expected_ifc_base_values:
            for ifc_code, ifc_base_value in zip(expected_ifc_list_codes, expected_ifc_base_values):
                self.bo_assert_text_table('IFC code', ifc_code, 'Base value', ifc_base_value)
        if expected_ifc_is_linkeds:
            for ifc_code, ifc_is_linked in zip(expected_ifc_list_codes, expected_ifc_is_linkeds):
                self.bo_assert_text_table('IFC code', ifc_code, 'Is linked', ifc_is_linked)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table('IFC code', ifc_code, 'IFC Value', ifc_value)
        if expected_ifc_margin_values:
            for ifc_code, ifc_margin_value in zip(expected_ifc_list_codes, expected_ifc_margin_values):
                self.bo_assert_text_table('IFC code', ifc_code, 'Margin Value', ifc_margin_value)
        if expected_ifc_statuses:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuses):
                self.bo_assert_text_table('IFC code', ifc_code, 'Status', ifc_status)
        if expected_ifc_outstandings:
            for ifc_code, ifc_outstanding in zip(expected_ifc_list_codes, expected_ifc_outstandings):
                self.bo_assert_text_table('IFC code', ifc_code, 'Oustanding', ifc_outstanding)
        if expected_ifc_paids:
            for ifc_code, ifc_paid in zip(expected_ifc_list_codes, expected_ifc_paids):
                self.bo_assert_text_table('IFC code', ifc_code, 'Paid', ifc_paid)
        if expected_ifc_basic_balances:
            for ifc_code, ifc_basic_balance in zip(expected_ifc_list_codes, expected_ifc_basic_balances):
                self.bo_assert_text_table('IFC code', ifc_code, 'Basic balance', ifc_basic_balance)
        self.bo_click_tab('IFC GLs Information')
        if expected_ifc_codes:
            for ifc_code, ifc_gl_name, ifc_gl_number in zip(expected_ifc_codes, expected_ifc_gl_names, expected_ifc_gl_numbers):
                self.bo_assert_text_table_ifc_gls(ifc_code, ifc_gl_name, self.no_mask(ifc_gl_number))
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def credit_account_update(self, account_number=None, account_name=None, linked_deposit_account=None, application_code=None, currency_code=None, account_holder_type=None, customer_code=None, branch_code=None, status=None, classification_status=None, realize_status=None, ranking_status=None, sub_product_limit_code=None, catalogue_code=None, credit_type=None, credit_sub_type=None, tenor_type=None, credit_facility=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, begin_of_tenor=None, end_of_tenor=None, open_date=None, close_date=None, last_marked_date=None, last_transaction_date=None, sub_product=None, created_by=None, approved_by=None, loan_officer_staff_id=None, dealer_name=None, type_of_commodity=None, purpose_of_loan=None, company_name=None, credit_limit=None, sale_price=None, down_payment=None, down_payment_amount=None, earmark_limit=None, limit_effective_from=None, limit_effective_to=None, limit_from_third_party=None, operative_limit_from_third_party=None, disbursement_amount=None, outstanding_balance=None, installment_amount=None, normal_principal_amount=None, overdue_principal=None, rounded_amount_of_principal=None, write_off_amount_of_principal=None, principal_paid_amount=None, write_off_amount_of_principal_paid=None, provision_of_principal=None, interest_accrual_amount=None, interest_receivable=None, interest_prepaid=None, overdue_interest=None, interest_paid=None, write_off_amount_of_interest_paid=None, outstanding_total=None, provision_of_interest=None, penalty_principle=None, penalty_interest=None, month_average_balance=None, quarter_average_balance=None, semi_annual_average_balance=None, year_average_balance=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quarter_debit=None, quarter_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, first_date_of_principal_repayment=None, first_date_of_interest_payment=None, grace_period_for_principal=None, is_syndicated=None, interest_computation_mode=None, secure_type=None, minimum_secure_rate=None, secure_amount=None, credit_purpose=None, credit_classification=None, disbursement_mode=None, is_restructured=None, is_provision=None, classification_option=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, remark=None, reference_id=None, provision_of_other=None, email=None, push_notification=None, sms=None, list_error_message=None):
        # view
        self.credit_account_view(account_number=account_number)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if account_name:
            self.bo_write_text('Account name', account_name)
        self.key_escape()
        if ranking_status:
            self.bo_select('Ranking status', ranking_status)
        if principal_collection_tenor:
            self.bo_write_number('Principal collection tenor', principal_collection_tenor)
        self.key_escape()
        if principal_collection_tenor_unit:
            self.bo_select('Principal collection tenor', principal_collection_tenor_unit)
        if interest_collection_tenor:
            self.bo_write_number('Interest collection tenor', interest_collection_tenor)
        self.key_escape()
        if interest_collection_tenor_unit:
            self.bo_select('Interest collection tenor', interest_collection_tenor_unit)
        if loan_officer_staff_id:
            self.bo_write_group('Loan officer staff id', loan_officer_staff_id)
        if dealer_name:
            self.bo_write_text('Dealer name', dealer_name)
        if type_of_commodity:
            self.bo_write_text('Type of commodity', type_of_commodity)
        if purpose_of_loan:
            self.bo_write_group('Purpose of loan', purpose_of_loan)
        if company_name:
            self.bo_write_text_group('Company name', company_name)
        self.bo_click_tab('Outstanding information')
        if limit_from_third_party:
            self.bo_write_number('Limit from third party', limit_from_third_party)
        if operative_limit_from_third_party:
            self.bo_write_number('Operative limit from third party', operative_limit_from_third_party)
        self.bo_click_tab('Term and condition')
        if first_date_of_principal_repayment:
            self.bo_write_date('First date of principal repayment', first_date_of_principal_repayment)
        if first_date_of_interest_payment:
            self.bo_write_date('First date of interest payment', first_date_of_interest_payment)
        self.key_escape()
        if secure_type:
            self.bo_select('Secure type', secure_type)
        if minimum_secure_rate:
            self.bo_write_number('Minimum secure rate', minimum_secure_rate)
        self.key_escape()
        if credit_purpose:
            self.bo_select('Credit purpose', credit_purpose)
        self.key_escape()
        if credit_classification:
            self.bo_select('Credit classification', credit_classification)
        self.key_escape()
        if disbursement_mode:
            self.bo_select('Disbursement mode', disbursement_mode)
        self.key_escape()
        if is_restructured:
            self.bo_select('Is restructured', is_restructured)
        self.key_escape()
        if is_provision:
            self.bo_select('Is provision?', is_provision)
        self.key_escape()
        if classification_option:
            self.bo_select('Classification option', classification_option)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_write_number('Standard', standard)
        if watch:
            self.bo_write_number('Watch', watch)
        if substandard:
            self.bo_write_number('Substandard', substandard)
        if doubtful:
            self.bo_write_number('Doubtful', doubtful)
        if loss:
            self.bo_write_number('Loss', loss)
        self.bo_click_tab('Additional information')
        if remark:
            self.bo_write_text('Remark', remark)
        if reference_id:
            self.bo_write_text('Reference id', reference_id)
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is True:
            self.bo_click_checkbox_multi('Notification type', 'Email')
        if email is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Email')
        if push_notification is True:
            self.bo_click_checkbox_multi('Notification type', 'Push Notification')
        if push_notification is False:
            self.bo_click_uncheckbox_multi('Notification type', 'Push Notification')
        if sms is True:
            self.bo_click_checkbox_multi('Notification type', 'SMS')
        if sms is False:
            self.bo_click_uncheckbox_multi('Notification type', 'SMS')
        # assert value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_value('Account number', self.credit_account_number_mask(account_number))
        if linked_deposit_account:
            self.bo_assert_value_group('Linked deposit account', self.deposit_account_number_mask(linked_deposit_account))
        if application_code:
            self.bo_assert_text('Application code', application_code)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if account_holder_type:
            self.bo_assert_select('Account holder type', account_holder_type)
        if customer_code:
            self.bo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if branch_code:
            self.bo_assert_text('Branch code', branch_code)
        if status:
            self.bo_assert_select('Status', status)
        if classification_status:
            self.bo_assert_select('Classification status', classification_status)
        if realize_status:
            self.bo_assert_select('Realize status', realize_status)
        if sub_product_limit_code:
            self.bo_assert_value('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if catalogue_code:
            self.bo_assert_text('Catalogue code', catalogue_code)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if begin_of_tenor:
            self.bo_assert_date('Begin of tenor', begin_of_tenor)
        if end_of_tenor:
            self.bo_assert_date('End of tenor', end_of_tenor)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if last_marked_date:
            self.bo_assert_date('Last marked date', last_marked_date)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if sub_product:
            self.bo_assert_select('Sub product', sub_product)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.bo_click_tab('Outstanding information')
        if credit_limit:
            self.bo_assert_value('Credit limit', credit_limit)
        if sale_price:
            self.bo_assert_value('Sale price', sale_price)
        if down_payment:
            self.bo_assert_value('Down payment %', down_payment)
        if down_payment_amount:
            self.bo_assert_value('Down payment amount', down_payment_amount)
        if earmark_limit:
            self.bo_assert_value('Earmark limit', earmark_limit)
        if limit_effective_from:
            self.bo_assert_date('Limit effective from', limit_effective_from)
        if limit_effective_to:
            self.bo_assert_date('Limit effective to', limit_effective_to)
        if disbursement_amount:
            self.bo_assert_value('Disbursement amount', disbursement_amount)
        if outstanding_balance:
            self.bo_assert_value('Outstanding balance', outstanding_balance)
        if installment_amount:
            self.bo_assert_value('Installment amount', installment_amount)
        if normal_principal_amount:
            self.bo_assert_value('Normal principal amount', normal_principal_amount)
        if overdue_principal:
            self.bo_assert_value('Overdue principal', overdue_principal)
        if rounded_amount_of_principal:
            self.bo_assert_value('Rounded amount of principal', rounded_amount_of_principal)
        if write_off_amount_of_principal:
            self.bo_assert_value('Write off amount of principal', write_off_amount_of_principal)
        if principal_paid_amount:
            self.bo_assert_value('Principal paid amount', principal_paid_amount)
        if write_off_amount_of_principal_paid:
            self.bo_assert_value('Write off amount of principal paid', write_off_amount_of_principal_paid)
        if provision_of_principal:
            self.bo_assert_value('Provision of principal', provision_of_principal)
        if interest_accrual_amount:
            self.bo_assert_value('Interest accrual amount', interest_accrual_amount)
        if interest_receivable:
            self.bo_assert_value('Interest receivable', interest_receivable)
        if interest_prepaid:
            self.bo_assert_value('Interest prepaid', interest_prepaid)
        if overdue_interest:
            self.bo_assert_value('Overdue interest ', overdue_interest)
        if interest_paid:
            self.bo_assert_value('Interest paid', interest_paid)
        if write_off_amount_of_interest_paid:
            self.bo_assert_value('Write off amount of interest paid', write_off_amount_of_interest_paid)
        if outstanding_total:
            self.bo_assert_value('Outstanding total', outstanding_total)
        if provision_of_interest:
            self.bo_assert_value('Provision of interest', provision_of_interest)
        if penalty_principle:
            self.bo_assert_value('Penalty principle', penalty_principle)
        if penalty_interest:
            self.bo_assert_value('Penalty interest', penalty_interest)
        if month_average_balance:
            self.bo_assert_value('Month average balance', month_average_balance)
        if quarter_average_balance:
            self.bo_assert_value('Quarter average balance', quarter_average_balance)
        if semi_annual_average_balance:
            self.bo_assert_value('Semi-annual average balance', semi_annual_average_balance)
        if year_average_balance:
            self.bo_assert_value('Year average balance', year_average_balance)
        if week_debit:
            self.bo_assert_value('Week debit', week_debit)
        if week_credit:
            self.bo_assert_value('Week credit', week_credit)
        if month_debit:
            self.bo_assert_value('Month debit', month_debit)
        if month_credit:
            self.bo_assert_value('Month credit', month_credit)
        if quarter_debit:
            self.bo_assert_value('Quarter debit', quarter_debit)
        if quarter_credit:
            self.bo_assert_value('Quarter credit', quarter_credit)
        if semi_annual_debit:
            self.bo_assert_value('Semi-annual debit', semi_annual_debit)
        if semi_annual_credit:
            self.bo_assert_value('Semi-annual credit', semi_annual_credit)
        if year_debit:
            self.bo_assert_value('Year debit', year_debit)
        if year_credit:
            self.bo_assert_value('Year credit', year_credit)
        self.bo_click_tab('Term and condition')
        if grace_period_for_principal:
            self.bo_assert_value('Grace Period For Principal ', grace_period_for_principal)
        if is_syndicated:
            self.bo_assert_select('Is syndicated?', is_syndicated)
        if interest_computation_mode:
            self.bo_assert_select('Interest computation mode', interest_computation_mode)
        if secure_amount:
            self.bo_assert_value('Secure amount', secure_amount)
        self.bo_click_tab('Additional information')
        if provision_of_other:
            self.bo_assert_value('Provision of other', provision_of_other)
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
            account_number_out=self.bo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return account_number_out

    def credit_account_delete(self, account_number, list_error_message=None):
        # search
        self.credit_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.credit_account_number_mask(account_number))
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{account_number}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.credit_account_simple_search(str(account_number).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {account_number}')
            return account_number

    # CRD-Approve Account Modification
    def credit_account_modify_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Credit', 'Approve Account Modification')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Approve Account Modification-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def credit_account_modify_advanced_search(self, account_number=None, account_name=None, currency_code=None, customer_code=None, category_code=None, credit_type=None, tenor_type=None, status=None, old_a_c_no=None, sub_product_limit=None):
        self.close_all_form()
        self.click_menu('Credit', 'Approve Account Modification')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Approve Account Modification-Search')
        if account_number:
            self.adv_search_text('Account number', str(account_number).replace('-', ''))
        if account_name:
            self.adv_search_text('Account name', account_name)
        if currency_code:
            self.adv_search_text('Currency code', currency_code)
        if customer_code:
            self.adv_search_text('Customer code', str(customer_code).replace('-', ''))
        if category_code:
            self.adv_search_text('Category code', category_code)
        self.key_escape()
        if credit_type:
            self.adv_search_select('Credit type', credit_type)
        self.key_escape()
        if tenor_type:
            self.adv_search_select('Tenor type', tenor_type)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        if old_a_c_no:
            self.adv_search_text('Old a/c no', old_a_c_no)
        if sub_product_limit:
            self.adv_search_text('sub product limit', str(sub_product_limit).replace('-', ''))
        self.click_button_search_advanced()
        self.wait_loading()

    def credit_account_modify_view(self, account_number=None, account_name=None, application_code=None, currency_code=None, account_holder_type=None, customer_code=None, branch_code=None, status=None, classification_status=None, realize_status=None, ranking_status=None, rksts_modification=None, sub_product_limit_code=None, catalogue_code=None, credit_type=None, credit_sub_type=None, tenor_type=None, credit_facility=None, principal_collection_tenor=None, prtn_modification=None, principal_collection_tenor_unit=None, prtnun_modification=None, interest_collection_tenor=None, inttn_modification=None, interest_collection_tenor_unit=None, inttnun_modification=None, begin_of_tenor=None, end_of_tenor=None, open_date=None, close_date=None, last_marked_date=None, last_transaction_date=None, sub_product=None, subproduct_modification=None, created_by=None, approved_by=None, loan_officer_staff_id=None, crmcd_modification=None, dealer_name=None, type_of_commodity=None, company_name=None, purpose_of_loan=None, credit_limit=None, sale_price=None, down_payment=None, down_payment_amount=None, earmark_limit=None, limit_effective_from=None, lfrdt_modification=None, limit_effective_to=None, ltodt_modification=None, limit_from_third_party=None, olimit_modification=None, operative_limit_from_third_party=None, oolimit_modification=None, disbursement_amount=None, outstanding_balance=None, installment_amount=None, normal_principal_amount=None, due_amount=None, rounded_amount_of_principal=None, write_off_amount_of_principal=None, principal_paid_amount=None, write_off_amount_of_principal_paid=None, provision_of_principal=None, interest_accrual_amount=None, interest_due=None, interest_paid=None, write_off_amount_of_interest_paid=None, provision_of_interest=None, month_average_balance=None, quarter_average_balance=None, semi_annual_average_balance=None, year_average_balance=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quarter_debit=None, quarter_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, first_date_of_principal_repayment=None, pfstdt_modification=None, first_date_of_interest_payment=None, intfstdt_modification=None, grace_period_for_principal=None, is_syndicated=None, interest_computation_mode=None, intmode_modification=None, secure_type=None, minimum_secure_rate=None, credit_purpose=None, crdprp_modification=None, credit_classification=None, crdcls_modification=None, disbursement_mode=None, dbmode_modification=None, is_restructured=None, isrestruct_modification=None, is_provision=None, isprv_modification=None, classification_option=None, restruct_modification=None, principal_grace_period=None, normal=None, prv_p_rate0_modification=None, special_mention=None, prv_p_rate1_modification=None, sub_statandard=None, prv_p_rate2_modification=None, doubful=None, prv_p_rate3_modification=None, lost=None, prv_p_rate4_modification=None, remark=None, reference_id=None, provision_of_other=None, fpamt_modification=None, email=None, push_notification=None, sms=None):
        # search
        self.credit_account_modify_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.credit_account_number_mask(account_number))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-Approve Account Modification-View')
        # verify value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_value('Account number', self.credit_account_number_mask(account_number))
        if account_name:
            self.bo_assert_text_group('Account name', account_name)
        if application_code:
            self.bo_assert_text('Application code', application_code)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if account_holder_type:
            self.bo_assert_select('Account holder type', account_holder_type)
        if customer_code:
            self.bo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if branch_code:
            self.bo_assert_text('Branch code', branch_code)
        if status:
            self.bo_assert_select('Status', status)
        if classification_status:
            self.bo_assert_select('Classification status', classification_status)
        if realize_status:
            self.bo_assert_select('Realize status', realize_status)
        if ranking_status:
            self.bo_assert_select_group('Ranking status', ranking_status)
        if rksts_modification:
            self.bo_assert_select_group('rksts_modification', rksts_modification)
        if sub_product_limit_code:
            self.bo_assert_value('Sub product limit code', self.sub_product_limit_code_mask(sub_product_limit_code))
        if catalogue_code:
            self.bo_assert_text('Catalogue code', catalogue_code)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if prtn_modification:
            self.bo_assert_value_group('prtn_modification', prtn_modification)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if prtnun_modification:
            self.bo_assert_select_group('prtnun_modification', prtnun_modification)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if inttn_modification:
            self.bo_assert_value_group('inttn_modification', inttn_modification)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if inttnun_modification:
            self.bo_assert_select_group('inttnun_modification', inttnun_modification)
        if begin_of_tenor:
            self.bo_assert_date('Begin of tenor', begin_of_tenor)
        if end_of_tenor:
            self.bo_assert_date('End of tenor', end_of_tenor)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if last_marked_date:
            self.bo_assert_date('Last marked date', last_marked_date)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if sub_product:
            self.bo_assert_select_group('Sub product', sub_product)
        if subproduct_modification:
            self.bo_assert_select_group('subproduct_modification', subproduct_modification)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if loan_officer_staff_id:
            self.bo_assert_value_group('Loan officer staff id', loan_officer_staff_id)
        if crmcd_modification:
            self.bo_assert_value_group('crmcd_modification', crmcd_modification)
        if dealer_name:
            self.bo_assert_text_group('Dealer name', dealer_name)
        if type_of_commodity:
            self.bo_assert_text_group('Type of commodity', type_of_commodity)
        if company_name:
            self.bo_assert_text('Company name', company_name)
        if purpose_of_loan:
            self.bo_assert_text_group('Purpose of loan', purpose_of_loan)
        self.bo_click_tab('Outstanding information')
        if credit_limit:
            self.bo_assert_value('Credit limit', credit_limit)
        if sale_price:
            self.bo_assert_value('Sale price', sale_price)
        if down_payment:
            self.bo_assert_value('Down payment %', down_payment)
        if down_payment_amount:
            self.bo_assert_value('Down payment amount', down_payment_amount)
        if earmark_limit:
            self.bo_assert_value('Earmark limit', earmark_limit)
        if limit_effective_from:
            self.bo_assert_date_group('Limit effective from', limit_effective_from)
        if lfrdt_modification:
            self.bo_assert_date_group('lfrdt_modification', lfrdt_modification)
        if limit_effective_to:
            self.bo_assert_date_group('Limit effective to', limit_effective_to)
        if ltodt_modification:
            self.bo_assert_date_group('ltodt_modification', ltodt_modification)
        if limit_from_third_party:
            self.bo_assert_value_group('Limit from third party', limit_from_third_party)
        if olimit_modification:
            self.bo_assert_value_group('olimit_modification', olimit_modification)
        if operative_limit_from_third_party:
            self.bo_assert_value_group('Operative limit from third party', operative_limit_from_third_party)
        if oolimit_modification:
            self.bo_assert_value_group('oolimit_modification', oolimit_modification)
        if disbursement_amount:
            self.bo_assert_value('Disbursement amount', disbursement_amount)
        if outstanding_balance:
            self.bo_assert_value('Outstanding balance', outstanding_balance)
        if installment_amount:
            self.bo_assert_value('Installment amount', installment_amount)
        if normal_principal_amount:
            self.bo_assert_value('Normal principal amount', normal_principal_amount)
        if due_amount:
            self.bo_assert_value('Due amount', due_amount)
        if rounded_amount_of_principal:
            self.bo_assert_value('Rounded amount of principal', rounded_amount_of_principal)
        if write_off_amount_of_principal:
            self.bo_assert_value('Write off amount of principal', write_off_amount_of_principal)
        if principal_paid_amount:
            self.bo_assert_value('Principal paid amount', principal_paid_amount)
        if write_off_amount_of_principal_paid:
            self.bo_assert_value('Write off amount of principal paid', write_off_amount_of_principal_paid)
        if provision_of_principal:
            self.bo_assert_value('Provision of principal', provision_of_principal)
        if interest_accrual_amount:
            self.bo_assert_value('Interest accrual amount', interest_accrual_amount)
        if interest_due:
            self.bo_assert_value('Interest due', interest_due)
        if interest_paid:
            self.bo_assert_value('Interest paid', interest_paid)
        if write_off_amount_of_interest_paid:
            self.bo_assert_value('Write off amount of interest paid', write_off_amount_of_interest_paid)
        if provision_of_interest:
            self.bo_assert_value('Provision of interest', provision_of_interest)
        if month_average_balance:
            self.bo_assert_value('Month average balance', month_average_balance)
        if quarter_average_balance:
            self.bo_assert_value('Quarter average balance', quarter_average_balance)
        if semi_annual_average_balance:
            self.bo_assert_value('Semi-annual average balance', semi_annual_average_balance)
        if year_average_balance:
            self.bo_assert_value('Year average balance', year_average_balance)
        if week_debit:
            self.bo_assert_value('Week debit', week_debit)
        if week_credit:
            self.bo_assert_value('Week credit', week_credit)
        if month_debit:
            self.bo_assert_value('Month debit', month_debit)
        if month_credit:
            self.bo_assert_value('Month credit', month_credit)
        if quarter_debit:
            self.bo_assert_value('Quarter debit', quarter_debit)
        if quarter_credit:
            self.bo_assert_value('Quarter credit', quarter_credit)
        if semi_annual_debit:
            self.bo_assert_value('Semi-annual debit', semi_annual_debit)
        if semi_annual_credit:
            self.bo_assert_value('Semi-annual credit', semi_annual_credit)
        if year_debit:
            self.bo_assert_value('Year debit', year_debit)
        if year_credit:
            self.bo_assert_value('Year credit', year_credit)
        self.bo_click_tab('Term and condition')
        if first_date_of_principal_repayment:
            self.bo_assert_date_group('First date of principal repayment', first_date_of_principal_repayment)
        if pfstdt_modification:
            self.bo_assert_date_group('pfstdt_modification', pfstdt_modification)
        if first_date_of_interest_payment:
            self.bo_assert_date_group('First date of interest payment', first_date_of_interest_payment)
        if intfstdt_modification:
            self.bo_assert_date_group('intfstdt_modification', intfstdt_modification)
        if grace_period_for_principal:
            self.bo_assert_value_group('Grace period for principal', grace_period_for_principal)
        if is_syndicated:
            self.bo_assert_select('Is syndicated?', is_syndicated)
        if interest_computation_mode:
            self.bo_assert_select_group('Interest computation mode', interest_computation_mode)
        if intmode_modification:
            self.bo_assert_select_group('intmode_modification', intmode_modification)
        if secure_type:
            self.bo_assert_select_group('Secure type', secure_type)
        if minimum_secure_rate:
            self.bo_assert_value_group('Minimum secure rate', minimum_secure_rate)
        if credit_purpose:
            self.bo_assert_select_group('Credit purpose', credit_purpose)
        if crdprp_modification:
            self.bo_assert_select_group('crdprp_modification', crdprp_modification)
        if credit_classification:
            self.bo_assert_select_group('Credit classification', credit_classification)
        if crdcls_modification:
            self.bo_assert_select_group('crdcls_modification', crdcls_modification)
        if disbursement_mode:
            self.bo_assert_select_group('Disbursement mode', disbursement_mode)
        if dbmode_modification:
            self.bo_assert_select_group('dbmode_modification', dbmode_modification)
        if is_restructured:
            self.bo_assert_select_group('Is restructured', is_restructured)
        if isrestruct_modification:
            self.bo_assert_select_group('isrestruct_modification', isrestruct_modification)
        if is_provision:
            self.bo_assert_select_group('Is provision?', is_provision)
        if isprv_modification:
            self.bo_assert_select_group('isprv_modification', isprv_modification)
        if classification_option:
            self.bo_assert_select_group('Classification option', classification_option)
        if restruct_modification:
            self.bo_assert_select_group('restruct_modification', restruct_modification)
        if principal_grace_period:
            self.bo_assert_value_group('Principal grace period', principal_grace_period)
        self.bo_click_tab('Provision rate of principal')
        if normal:
            self.bo_assert_value_group('Normal', normal)
        if prv_p_rate0_modification:
            self.bo_assert_value_group('prv_p_rate0_modification', prv_p_rate0_modification)
        if special_mention:
            self.bo_assert_value_group('Special mention', special_mention)
        if prv_p_rate1_modification:
            self.bo_assert_value_group('prv_p_rate1_modification', prv_p_rate1_modification)
        if sub_statandard:
            self.bo_assert_value_group('Sub statandard', sub_statandard)
        if prv_p_rate2_modification:
            self.bo_assert_value_group('prv_p_rate2_modification', prv_p_rate2_modification)
        if doubful:
            self.bo_assert_value_group('Doubful', doubful)
        if prv_p_rate3_modification:
            self.bo_assert_value_group('prv_p_rate3_modification', prv_p_rate3_modification)
        if lost:
            self.bo_assert_value_group('Lost', lost)
        if prv_p_rate4_modification:
            self.bo_assert_value_group('prv_p_rate4_modification', prv_p_rate4_modification)
        self.bo_click_tab('Additional information')
        if remark:
            self.bo_assert_text_group('Remark', remark)
        if reference_id:
            self.bo_assert_text_group('Reference id', reference_id)
        if provision_of_other:
            self.bo_assert_value_group('Provision of other', provision_of_other)
        if fpamt_modification:
            self.bo_assert_value_group('fpamt_modification', fpamt_modification)
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def credit_account_modify_approve(self, account_number):
        self.credit_account_modify_view(account_number)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Approve')
        self.wait_loading()
        self.check_notification('Approve successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Account number', self.credit_account_number_mask(account_number))
        account_number_out=self.bo_get_value('Account number')
        print(f'Account number: {account_number_out}')
        self.credit_account_modify_simple_search(str(account_number_out).replace('-', ''))
        self.assert_search_not_found()
        return account_number_out

    def credit_account_modify_reject(self, account_number):
        self.credit_account_modify_view(account_number)
        self.click_button('View Modification')
        self.wait_loading()
        self.click_button('Reject')
        self.wait_loading()
        self.check_notification('Reject successfully')
        # back to tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Account number', self.credit_account_number_mask(account_number))
        account_number_out=self.bo_get_value('Account number')
        print(f'Account number: {account_number_out}')
        self.credit_account_modify_simple_search(str(account_number_out).replace('-', ''))
        self.assert_search_not_found()
        return account_number_out

    # CRD-Collection Reminder
    def collection_reminder_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Credit', 'Collection Reminder')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Collection Reminder-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def collection_reminder_advanced_search(self, reminder_code=None, reminder_name=None, number_of_days_from=None, number_of_days_to=None, remind_officer=None, remind_customer=None, use_email=None):
        self.close_all_form()
        self.click_menu('Credit', 'Collection Reminder')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Collection Reminder-Search')
        if reminder_code:
            self.adv_search_text('Reminder code', reminder_code)
        if reminder_name:
            self.adv_search_text('Reminder name', reminder_name)
        if number_of_days_from:
            self.adv_search_text_group('Number of days (From)', number_of_days_from)
        if number_of_days_to:
            self.adv_search_text_group('Number of days (To)', number_of_days_to)
        if remind_officer is True:
            self.adv_click_checkbox('Remind officer')
        if remind_officer is False:
            self.adv_click_uncheckbox('Remind officer')
        if remind_customer is True:
            self.adv_click_checkbox('Remind customer')
        if remind_customer is False:
            self.adv_click_uncheckbox('Remind customer')
        if use_email is True:
            self.adv_click_checkbox('Use Email')
        if use_email is False:
            self.adv_click_uncheckbox('Use Email')
        self.click_button_search_advanced()
        self.wait_loading()

    def collection_reminder_add(self, reminder_code=None, reminder_name=None, description=None, reminder_basis=None, remind_officer=None, number_of_days=None, remind_customer=None, use_sms=None, sms_template=None, use_email=None, email_template_id=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Credit', 'Collection Reminder')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CRD-Collection Reminder-Add')
        # enter value
        if reminder_code:
            self.bo_write_text('Reminder code', reminder_code)
        if reminder_name:
            self.bo_write_text('Reminder name', reminder_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.bo_write_text('Description', description)
        self.key_escape()
        if reminder_basis:
            self.bo_select('Reminder basis', reminder_basis)
        if remind_officer is True:
            self.bo_click_checkbox('Remind officer')
        if remind_officer is False:
            self.bo_click_uncheckbox('Remind officer')
        if number_of_days:
            self.bo_write_number('Number of days', number_of_days)
        if remind_customer is True:
            self.bo_click_checkbox('Remind customer')
        if remind_customer is False:
            self.bo_click_uncheckbox('Remind customer')
        if use_sms is True:
            self.bo_click_checkbox('Use SMS')
        if use_sms is False:
            self.bo_click_uncheckbox('Use SMS')
        if sms_template:
            self.bo_write_text_multi_line('Sms template', sms_template)
        if use_email is True:
            self.bo_click_checkbox('Use Email')
        if use_email is False:
            self.bo_click_uncheckbox('Use Email')
        self.key_escape()
        if email_template_id:
            self.bo_select('Email template id', email_template_id)
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
            reminder_code_out=self.bo_get_text('Reminder code')
            print(f'Reminder code: {reminder_code_out}')
            return reminder_code_out

    def collection_reminder_view(self, reminder_code=None, reminder_name=None, description=None, reminder_basis=None, remind_officer=None, number_of_days=None, remind_customer=None, use_sms=None, sms_template=None, use_email=None, email_template_id=None):
        # search
        self.collection_reminder_simple_search(reminder_code)
        self.assert_table_data('Reminder code', 1, reminder_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-Collection Reminder-View')
        # verify value
        self.bo_click_tab('General information')
        if reminder_code:
            self.bo_assert_text('Reminder code', reminder_code)
        if reminder_name:
            self.bo_assert_text('Reminder name', reminder_name)
        if description:
            self.bo_assert_text('Description', description)
        if reminder_basis:
            self.bo_assert_select('Reminder basis', reminder_basis)
        if remind_officer is not None:
            self.bo_assert_checkbox('Remind officer', remind_officer)
        if number_of_days:
            self.bo_assert_value('Number of days', number_of_days)
        if remind_customer is not None:
            self.bo_assert_checkbox('Remind customer', remind_customer)
        if use_sms is not None:
            self.bo_assert_checkbox('Use SMS', use_sms)
        if sms_template:
            self.bo_assert_text_multi_line('Sms template', sms_template)
        if use_email is not None:
            self.bo_assert_checkbox('Use Email', use_email)
        if email_template_id:
            self.bo_assert_select('Email template id', email_template_id)

    def collection_reminder_update(self, reminder_code=None, reminder_name=None, description=None, reminder_basis=None, remind_officer=None, number_of_days=None, remind_customer=None, use_sms=None, sms_template=None, use_email=None, email_template_id=None, list_error_message=None):
        # view
        self.collection_reminder_view(reminder_code=reminder_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if reminder_name:
            self.bo_write_text('Reminder name', reminder_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.bo_write_text('Description', description)
        self.key_escape()
        if reminder_basis:
            self.bo_select('Reminder basis', reminder_basis)
        if remind_officer is True:
            self.bo_click_checkbox('Remind officer')
        if remind_officer is False:
            self.bo_click_uncheckbox('Remind officer')
        if number_of_days:
            self.bo_write_number('Number of days', number_of_days)
        if remind_customer is True:
            self.bo_click_checkbox('Remind customer')
        if remind_customer is False:
            self.bo_click_uncheckbox('Remind customer')
        if use_sms is True:
            self.bo_click_checkbox('Use SMS')
        if use_sms is False:
            self.bo_click_uncheckbox('Use SMS')
        if sms_template:
            self.bo_write_text_multi_line('Sms template', sms_template)
        if use_email is True:
            self.bo_click_checkbox('Use Email')
        if use_email is False:
            self.bo_click_uncheckbox('Use Email')
        self.key_escape()
        if email_template_id:
            self.bo_select('Email template id', email_template_id)
        # assert value
        self.bo_click_tab('General information')
        if reminder_code:
            self.bo_assert_text('Reminder code', reminder_code)
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
            reminder_code_out=self.bo_get_text('Reminder code')
            print(f'Reminder code: {reminder_code_out}')
            return reminder_code_out

    def collection_reminder_delete(self, reminder_code, list_error_message=None, expected_message=None):
        # search
        self.collection_reminder_simple_search(reminder_code)
        self.assert_table_data('Reminder code', 1, reminder_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{reminder_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{reminder_code}'")
            return reminder_code

    # CRD-Collection Reminder Profile
    def collection_reminder_profile_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Credit', 'Collection Reminder Profile')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Collection Reminder Profile-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def collection_reminder_profile_advanced_search(self, profile_code=None, profile_name=None):
        self.close_all_form()
        self.click_menu('Credit', 'Collection Reminder Profile')
        self.wait_for_button_available('Search')
        self.assert_form_title('CRD-Collection Reminder Profile-Search')
        if profile_code:
            self.adv_search_text('Profile code', profile_code)
        if profile_name:
            self.adv_search_text('Profile name', profile_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def collection_reminder_profile_add(self, profile_code=None, profile_name=None, reminder_codes=None, reminder_names=None, orders=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Credit', 'Collection Reminder Profile')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('CRD-Collection Reminder Profile-Add')
        # enter value
        if profile_code:
            self.bo_write_text('Profile code', profile_code)
        if profile_name:
            self.bo_write_text('Profile name', profile_name)
        if reminder_codes:
            self.add_reminders(reminder_codes, orders, reminder_names)
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
            profile_code_out=self.bo_get_text('Profile code')
            print(f'Profile code: {profile_code_out}')
            return profile_code_out

    def collection_reminder_profile_view(self, profile_code=None, profile_name=None, reminder_codes=None, reminder_names=None, orders=None):
        # search
        self.collection_reminder_profile_advanced_search(profile_code=profile_code)
        self.assert_table_data('Profile code', 1, profile_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-Collection Reminder Profile-View')
        # verify value
        if profile_code:
            self.bo_assert_text('Profile code', profile_code)
        if profile_name:
            self.bo_assert_text('Profile name', profile_name)
        if reminder_names:
            for reminder_code, reminder_name in zip(reminder_codes, reminder_names):
                self.bo_assert_text_table('Reminder code', reminder_code, 'Reminder name', reminder_name)
        if orders:
            for reminder_code, order in zip(reminder_codes, orders):
                self.bo_assert_text_table('Reminder code', reminder_code, 'Order', order)

    def collection_reminder_profile_update(self, profile_code=None, profile_name=None, list_error_message=None):
        # view
        self.collection_reminder_profile_view(profile_code=profile_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        if profile_name:
            self.bo_write_text('Profile name', profile_name)
        # assert value
        if profile_code:
            self.bo_assert_text('Profile code', profile_code)
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
            profile_code_out=self.bo_get_text('Profile code')
            print(f'Profile code: {profile_code_out}')
            return profile_code_out

    def collection_reminder_profile_delete(self, profile_code, list_error_message=None, expected_message=None):
        # search
        self.collection_reminder_profile_advanced_search(profile_code=profile_code)
        self.assert_table_data('Profile code', 1, profile_code)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{profile_code}' failed!")
        else:
        # verify success
            if expected_message:
                self.assert_notification(expected_message)
            print(f"Deleted: '{profile_code}'")
            return profile_code

# -------------------------- handle BO approval - CREDIT --------------------------
    # CRD-Catalogue Definition - Data Verification
    def credit_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, interest_computation_mode=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, reminder_profile_code=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_account_aliass=None, expected_gls_sys_account_names=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None, email=None, push_notification=None, sms=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if secured_by_currency:
            self.bo_assert_select('Secured by currency', secured_by_currency)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if interest_computation_mode:
            self.bo_assert_select('Interest computation mode', interest_computation_mode)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if status:
            self.bo_assert_select('Status', status)
        if reminder_profile_code:
            self.bo_assert_value('Reminder Profile code', reminder_profile_code)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_assert_value('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_assert_value('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_assert_value('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_assert_value('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_assert_value_group('Fine collection tenor', fine_collection_tenor)
        if fine_collection_tenor_unit:
            self.bo_assert_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_assert_value('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_assert_value('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('IFC information')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def credit_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, interest_computation_mode=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, reminder_profile_code=None, created_by=None, approved_by=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_account_aliass=None, expected_gls_sys_account_names=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None, email=None, push_notification=None, sms=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if secured_by_currency:
            self.bo_assert_select('Secured by currency', secured_by_currency)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if interest_computation_mode:
            self.bo_assert_select('Interest computation mode', interest_computation_mode)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if status:
            self.bo_assert_select('Status', status)
        if reminder_profile_code:
            self.bo_assert_value('Reminder Profile code', reminder_profile_code)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_assert_value('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_assert_value('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_assert_value('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_assert_value('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_assert_value_group('Fine collection tenor', fine_collection_tenor)
        if fine_collection_tenor_unit:
            self.bo_assert_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_assert_value('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_assert_value('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('IFC Information')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def credit_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, currency=None, credit_type=None, credit_facility=None, tenor_type=None, status=None):
        # search and verify
        self.credit_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue name', 1, catalogue_name)
        if currency:
            self.assert_table_data('Currency', 1, currency)
        if credit_type:
            self.assert_table_data('Credit type', 1, credit_type)
        if credit_facility:
            self.assert_table_data('Credit facility', 1, credit_facility)
        if tenor_type:
            self.assert_table_data('Tenor type', 1, tenor_type)
        if status:
            self.assert_table_data('Status', 1, status)

    # CRD-IFC Item Definition - Data Verification
    def credit_ifc_item_definition_add_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-IFC Item Definition-Add'
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

    def credit_ifc_item_definition_update_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-IFC Item Definition-View'
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

    def credit_ifc_item_definition_search_verify(self, ifc_code, ifc_name=None, value_type=None, ifc_type=None, value=None, tenor=None, tenor_unit=None, active_condition=None, status=None):
        # search and verify
        self.credit_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
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

    def credit_get_ifc_code(self, ifc_name):
        self.credit_ifc_item_definition_simple_search(ifc_name)
        self.assert_table_data('IFC name', 1, ifc_name)
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-IFC Item Definition-View')
        self.bo_click_tab('General information')
        ifc_code_out=self.bo_get_value('IFC code')
        print(f'IFC code: {ifc_code_out}')
        return ifc_code_out

    # CRD-IFC Auto Fee - Data Verification
    def credit_ifc_auto_fee_add_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-IFC Auto Fee-Add'
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

    def credit_ifc_auto_fee_update_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-IFC Auto Fee-View'
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

    def credit_ifc_auto_fee_search_verify(self, transaction_code, ifc_code, transaction_name=None, ifc_name=None):
        # search
        self.credit_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        # verify value
        self.assert_table_data('Transaction code', 1, transaction_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        if transaction_name:
            self.assert_table_data('Transaction name', 1, transaction_name)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)

    # CRD-Collection Reminder - Data Verification
    def collection_reminder_add_verify(self, transaction_number, reminder_code=None, reminder_name=None, description=None, reminder_basis=None, remind_officer=None, number_of_days=None, remind_customer=None, use_sms=None, sms_template=None, use_email=None, email_template_id=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Collection Reminder-Add'
        )
        # verify value
        if reminder_code:
            self.bo_assert_text('Reminder code', reminder_code)
        if reminder_name:
            self.bo_assert_text('Reminder name', reminder_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.bo_assert_text('Description', description)
        if reminder_basis:
            self.bo_assert_select('Reminder basis', reminder_basis)
        if remind_officer is not None:
            self.bo_assert_checkbox('Remind officer', remind_officer)
        if number_of_days:
            self.bo_assert_value('Number of days', number_of_days)
        if remind_customer is not None:
            self.bo_assert_checkbox('Remind customer', remind_customer)
        if use_sms is not None:
            self.bo_assert_checkbox('Use SMS', use_sms)
        if sms_template:
            self.bo_assert_text_multi_line('Sms template', sms_template)
        if use_email is not None:
            self.bo_assert_checkbox('Use Email', use_email)
        if email_template_id:
            self.bo_assert_select('Email template id', email_template_id)

    def collection_reminder_update_verify(self, transaction_number, reminder_code=None, reminder_name=None, description=None, reminder_basis=None, remind_officer=None, number_of_days=None, remind_customer=None, use_sms=None, sms_template=None, use_email=None, email_template_id=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Collection Reminder-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if reminder_code:
            self.bo_assert_text('Reminder code', reminder_code)
        if reminder_name:
            self.bo_assert_text('Reminder name', reminder_name)
        if description:
            self.bo_assert_text('Description', description)
        if reminder_basis:
            self.bo_assert_select('Reminder basis', reminder_basis)
        if remind_officer is not None:
            self.bo_assert_checkbox('Remind officer', remind_officer)
        if number_of_days:
            self.bo_assert_value('Number of days', number_of_days)
        if remind_customer is not None:
            self.bo_assert_checkbox('Remind customer', remind_customer)
        if use_sms is not None:
            self.bo_assert_checkbox('Use SMS', use_sms)
        if sms_template:
            self.bo_assert_text_multi_line('Sms template', sms_template)
        if use_email is not None:
            self.bo_assert_checkbox('Use Email', use_email)
        if email_template_id:
            self.bo_assert_select('Email template id', email_template_id)

    def collection_reminder_search_verify(self, reminder_code=None, reminder_name=None, number_of_days=None, remind_officer=None, remind_customer=None, use_email=None):
        # search
        self.collection_reminder_simple_search(reminder_code)
        # verify value
        if reminder_code:
            self.assert_table_data('Reminder code', 1, reminder_code)
        if reminder_name:
            self.assert_table_data('Reminder name', 1, reminder_name)
        if number_of_days:
            self.assert_table_data('Number of days', 1, number_of_days)
        if remind_officer:
            self.assert_table_data('Remind officer', 1, remind_officer)
        if remind_customer:
            self.assert_table_data('Remind customer', 1, remind_customer)
        if use_email:
            self.assert_table_data('Use Email', 1, use_email)

    # CRD-Collection Reminder Profile - Data Verification
    def collection_reminder_profile_add_verify(self, transaction_number, profile_code=None, profile_name=None, reminder_codes=None, reminder_names=None, orders=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Collection Reminder Profile-Add'
        )
        # verify value
        if profile_code:
            self.bo_assert_text('Profile code', profile_code)
        if profile_name:
            self.bo_assert_text('Profile name', profile_name)
        if reminder_names:
            for reminder_code, reminder_name in zip(reminder_codes, reminder_names):
                self.bo_assert_text_table('Reminder code', reminder_code, 'Reminder name', reminder_name)
        if orders:
            for reminder_code, order in zip(reminder_codes, orders):
                self.bo_assert_text_table('Reminder code', reminder_code, 'Order', order)

    def collection_reminder_profile_update_verify(self, transaction_number, profile_code=None, profile_name=None, reminder_codes=None, reminder_names=None, orders=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Collection Reminder Profile-View'
        )
        # verify value
        if profile_code:
            self.bo_assert_text('Profile code', profile_code)
        if profile_name:
            self.bo_assert_text('Profile name', profile_name)
        if reminder_names:
            for reminder_code, reminder_name in zip(reminder_codes, reminder_names):
                self.bo_assert_text_table('Reminder code', reminder_code, 'Reminder name', reminder_name)
        if orders:
            for reminder_code, order in zip(reminder_codes, orders):
                self.bo_assert_text_table('Reminder code', reminder_code, 'Order', order)

    def collection_reminder_profile_search_verify(self, profile_code, profile_name=None):
        # search
        self.collection_reminder_profile_advanced_search(profile_code=profile_code)
        # verify value
        self.assert_table_data('Profile code', 1, profile_code)
        if profile_name:
            self.assert_table_data('Profile name', 1, profile_name)

