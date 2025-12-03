from webui_test.case import *

class TradeActions(TestCase):

# -------------------------- handle FO - TRADE FINANCE --------------------------
    # TRD_SNI: SG/BG - Issue SG/BG for collection
    def trd_sni(self, category_code, account_holder_code, applicant, beneficiary, currency_code, issued_date, effect_date, guarantee_period, guarantee_period_unit, sg_bg_amount, project_name, bg_number, send_to, maturity_date=None, addition_margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, country_code=None, beneficiary_address=None, account_holder_type=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_SNI', '7738')
        self.wait_for_button_available('Accept')
        self.assert_form_title('7738: SG/BG - Issue SG/BG for collection')
        # enter value
        self.key_escape()
        if account_holder_type:
            self.fo_select('Account holder type', account_holder_type)
        self.fo_write_group('Category code', category_code)
        self.fo_write_group('Account holder code', account_holder_code)
        self.fo_write_text('Applicant', applicant)
        self.fo_write_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_write_text('Beneficiary address', beneficiary_address)
        self.key_escape()
        self.fo_select('Currency code', currency_code)
        self.key_escape()
        if country_code:
            self.fo_select('Country code', country_code)
        self.fo_write_date('Issued date', issued_date)
        self.fo_write_date('Effect date', effect_date)
        self.key_escape()
        self.fo_select('Guarantee period', guarantee_period)
        self.key_escape()
        self.fo_select('Guarantee period unit', guarantee_period_unit)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        self.fo_write_number('SG/BG amount', sg_bg_amount)
        if addition_margin_rate:
            self.fo_write_number('Addition margin rate', str(addition_margin_rate).replace('.00', ''))
            if self.fo_get_value('Addition margin rate')!= str(addition_margin_rate).replace('.00', ''):
                self.fo_write_number('Addition margin rate', str(addition_margin_rate).replace('.00', ''))
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_write_number('Secured amount', secured_amount)
            self.key_escape()
        self.fo_write_text('Project name', project_name)
        self.fo_write_text('BG number', bg_number)
        self.fo_write_text_multi_line('Send to', send_to)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references TRD_SNI: {transaction_references}')
            trade_account_mask=self.fo_get_value('Account number')
            print(f'Account number: {trade_account_mask}')
            return transaction_references, trade_account_mask

    def trd_sni_view(self, transaction_references, account_number=None, category_code=None, account_holder_code=None, applicant=None, beneficiary=None, currency_code=None, issued_date=None, effect_date=None, guarantee_period=None, guarantee_period_unit=None, sg_bg_amount=None, project_name=None, bg_number=None, send_to=None, maturity_date=None, addition_margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, country_code=None, beneficiary_address=None, account_holder_type=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '7738: SG/BG - Issue SG/BG for collection')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.trade_account_number_mask(account_number))
        if account_holder_type:
            self.fo_assert_select('Account holder type', account_holder_type)
        if category_code:
            self.fo_assert_value_group('Category code', category_code)
        if account_holder_code:
            self.fo_assert_value_group('Account holder code', account_holder_code)
        if applicant:
            self.fo_assert_text('Applicant', applicant)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if country_code:
            self.fo_assert_select('Country code', country_code)
        if issued_date:
            self.fo_assert_date('Issued date', issued_date)
        if effect_date:
            self.fo_assert_date('Effect date', effect_date)
        if guarantee_period:
            self.fo_assert_select('Guarantee period', guarantee_period)
        if guarantee_period_unit:
            self.fo_assert_select('Guarantee period unit', guarantee_period_unit)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if sg_bg_amount:
            self.fo_assert_value('SG/BG amount', sg_bg_amount)
        if addition_margin_rate:
            self.fo_assert_value('Addition margin rate', str(addition_margin_rate).replace('.00', ''))
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if description:
            self.fo_assert_text('Description', description)
        if project_name:
            self.fo_assert_text('Project name', project_name)
        if bg_number:
            self.fo_assert_text('BG number', bg_number)
        if send_to:
            self.fo_assert_text_multi_line('Send to', send_to)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        trade_account_mask=self.fo_get_value('Account number')
        print(f'Account number: {trade_account_mask}')
        return transaction_references, trade_account_mask

    # TRD_GSC: 7734: OLC - Guarantee by secure collateral
    def trd_gsc(self, mortgage_account_number, trade_finance_account_number, amount_secure_from_this_asset, mortgage_account_currency=None, asset_booking_value=None, total_secured_amount_of_mortgage=None, trade_finance_account_currency=None, secure_required=None, secured_amount_for_tf_account=None, total_secured_amount_of_tf_account=None, amount_secured_for_tf_account=None, exchange_rate=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, base_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_GSC', '7734')
        self.wait_for_button_available('Accept')
        self.assert_form_title('7734: OLC - Guarantee by secure collateral')
        # enter value
        self.fo_write_group('Mortgage account number', mortgage_account_number)
        self.wait_loading()
        if mortgage_account_currency:
            self.fo_assert_select('Mortgage account currency', mortgage_account_currency)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if total_secured_amount_of_mortgage:
            self.fo_assert_value('Total secured amount of Mortgage', total_secured_amount_of_mortgage)
        self.fo_write_group('Trade finance account number', trade_finance_account_number)
        self.wait_loading()
        if trade_finance_account_currency:
            self.fo_assert_select('Trade finance account currency', trade_finance_account_currency)
        if secure_required:
            self.fo_assert_value('Secure required', secure_required)
        if secured_amount_for_tf_account:
            self.fo_assert_value('Secured amount for TF account', secured_amount_for_tf_account)
        if total_secured_amount_of_tf_account:
            self.fo_assert_value('Total secured amount of TF account', total_secured_amount_of_tf_account)
        if amount_secure_from_this_asset:
            self.fo_write_number('Amount secure from this asset', amount_secure_from_this_asset)
            self.fo_assert_value_group('Amount secured for TF account', amount_secure_from_this_asset)
        if amount_secured_for_tf_account:
            self.fo_write_number_group('Amount secured for TF account', amount_secured_for_tf_account)
        if exchange_rate:
            self.fo_assert_value('Exchange rate', exchange_rate)
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if base_amount:
            self.fo_assert_value('Base amount', base_amount)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
        # click 'Accept'
        self.click_button('Accept')
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
            print(f'Transaction references TRD_GSC: {transaction_references}')
            mortgage_account_mask=self.fo_get_value_group('Mortgage account number')
            print(f'Mortgage account number: {mortgage_account_mask}')
            trade_account_mask=self.fo_get_value_group('Trade finance account number')
            print(f'Trade finance account number: {trade_account_mask}')
            return transaction_references, mortgage_account_mask, trade_account_mask

    def trd_gsc_view(self, transaction_references, mortgage_account_number=None, mortgage_account_currency=None, asset_booking_value=None, total_secured_amount_of_mortgage=None, trade_finance_account_number=None, trade_finance_account_currency=None, secure_required=None, secured_amount_for_tf_account=None, total_secured_amount_of_tf_account=None, amount_secure_from_this_asset=None, amount_secured_for_tf_account=None, exchange_rate=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, base_amount=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '7734: OLC - Guarantee by secure collateral')
        # compare value
        if mortgage_account_number:
            self.fo_assert_value_group('Mortgage account number', mortgage_account_number)
        if mortgage_account_currency:
            self.fo_assert_select('Mortgage account currency', mortgage_account_currency)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if total_secured_amount_of_mortgage:
            self.fo_assert_value('Total secured amount of Mortgage', total_secured_amount_of_mortgage)
        if trade_finance_account_number:
            self.fo_assert_value_group('Trade finance account number', trade_finance_account_number)
        if trade_finance_account_currency:
            self.fo_assert_select('Trade finance account currency', trade_finance_account_currency)
        if secure_required:
            self.fo_assert_value('Secure required', secure_required)
        if secured_amount_for_tf_account:
            self.fo_assert_value('Secured amount for TF account', secured_amount_for_tf_account)
        if total_secured_amount_of_tf_account:
            self.fo_assert_value('Total secured amount of TF account', total_secured_amount_of_tf_account)
        if amount_secure_from_this_asset:
            self.fo_assert_value('Amount secure from this asset', amount_secure_from_this_asset)
        if amount_secured_for_tf_account:
            self.fo_assert_value_group('Amount secured for TF account', amount_secured_for_tf_account)
        if exchange_rate:
            self.fo_assert_value('Exchange rate', exchange_rate)
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if base_amount:
            self.fo_assert_value('Base amount', base_amount)
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        mortgage_account_mask=self.fo_get_value_group('Mortgage account number')
        print(f'Mortgage account number: {mortgage_account_mask}')
        trade_account_mask=self.fo_get_value_group('Trade finance account number')
        print(f'Trade finance account number: {trade_account_mask}')
        return transaction_references, mortgage_account_mask, trade_account_mask

    # TRD_SIV: SG - Insurance verify
    def trd_siv(self, account_number, sg_bg_amount=None, margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, margin_method=None, margin_deposit_account=None, cheque_no=None, applicant=None, applicant_address=None, applicant_more_description=None, beneficiary=None, beneficiary_address=None, total_fee_amount=None, fee_collect_method=None, account_number_for_fee=None, ifc_code=None, value=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_SIV', 'Issurance verify')
        self.wait_for_button_available('Accept')
        self.assert_form_title('SG - Issurance verify')
        # enter value
        self.fo_write_group('Account number', account_number)
        if ifc_code:
            # add fee
            self.click_button('Add')
            self.wait_loading()
            self.fo_write_text_group('Interest/fee/charge code', ifc_code)
            self.wait_loading()
            self.fo_write_number('Value', value)
            self.wait_loading()
            self.click_button('Apply')
            self.wait_loading()
            if total_fee:
                self.assert_total_fee_table_data(total_fee)
            if total_fee_amount:
                self.fo_assert_value('Total fee amount', total_fee_amount)
        if sg_bg_amount:
            self.fo_assert_value('SG/BG amount', sg_bg_amount)
        if margin_rate:
            self.fo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        self.key_escape()
        if margin_method:
            self.fo_select('Margin method', margin_method)
        if cheque_no:
            self.fo_write('Cheque no', cheque_no)
            self.wait_loading()
            self.fo_assert_value_group('Margin deposit account', margin_deposit_account)
        if margin_deposit_account:
            self.fo_write_group('Margin deposit account', margin_deposit_account)
        if applicant:
            self.fo_assert_text('Applicant', applicant)
        if applicant_address:
            self.fo_assert_text('Applicant address', applicant_address)
        if applicant_more_description:
            self.fo_assert_text('Applicant more description', applicant_more_description)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_group('Account number for fee', str(account_number_for_fee).replace('-', ''))
        self.fo_write_text('Description', 'AUTO TEST')
        self.key_escape()
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references TRD_SIV: {transaction_references}')
            trade_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {trade_account_mask}')
            return transaction_references, trade_account_mask

    def trd_siv_view(self, transaction_references, account_number=None, sg_bg_amount=None, margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, margin_method=None, margin_deposit_account=None, cheque_no=None, applicant=None, applicant_address=None, applicant_more_description=None, beneficiary=None, beneficiary_address=None, total_fee_amount=None, fee_collect_method=None, account_number_for_fee=None, ifc_code=None, value=None, total_fee=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'SG - Issurance verify')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.trade_account_number_mask(account_number))
        if sg_bg_amount:
            self.fo_assert_value('SG/BG amount', sg_bg_amount)
        if margin_rate:
            self.fo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if margin_method:
            self.fo_assert_select('Margin method', margin_method)
        if margin_deposit_account:
            self.fo_assert_value_group('Margin deposit account', margin_deposit_account)
        if cheque_no:
            self.fo_assert_value('Cheque no', cheque_no)
        if applicant:
            self.fo_assert_text('Applicant', applicant)
        if applicant_address:
            self.fo_assert_text('Applicant address', applicant_address)
        if applicant_more_description:
            self.fo_assert_text('Applicant more description', applicant_more_description)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if description:
            self.fo_assert_text('Description', description)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_value_group('Account number for fee', account_number_for_fee)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
            self.assert_table_data('Value type', 1, 'Percentage')
            self.assert_table_data('Fee', 1, total_fee_amount)
        if value:
            self.assert_table_data('Value', 1, value)
        if total_fee:
            self.assert_total_fee_table_data(total_fee)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        trade_account_mask=self.fo_get_value_group('Account number')
        print(f'Account number: {trade_account_mask}')
        return transaction_references, trade_account_mask

    # TRD_RSC: 7757: OLC - Release secure collateral
    def trd_rsc(self, mortgage_account_number, trade_finance_account_number, release_amount_in_mortgage_currency, asset_booking_value=None, mortgage_account_currency=None, trade_finance_account_currency=None, exchange_rate=None, release_amount_in_tf_currency=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, base_amount=None, secured_amount_for_tf_account=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_RSC', 'Release')
        self.wait_for_button_available('Accept')
        self.assert_form_title('7757: OLC - Release secure collateral')
        # enter value
        self.fo_write_group('Mortgage account number', mortgage_account_number)
        self.wait_loading()
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if mortgage_account_currency:
            self.fo_assert_select('Mortgate account currency', mortgage_account_currency)
        self.fo_write_group('Trade finance account number', trade_finance_account_number)
        self.wait_loading()
        if trade_finance_account_currency:
            self.fo_assert_select('Trade finance account currency', trade_finance_account_currency)
        if secured_amount_for_tf_account:
            self.fo_assert_value('Secured amount for TF account', secured_amount_for_tf_account)
        if exchange_rate:
            self.fo_assert_value('Exchange rate', exchange_rate)
        if release_amount_in_mortgage_currency:
            self.fo_write_number('Release amount in mortgage currency', release_amount_in_mortgage_currency)
            self.fo_assert_value_group('Release amount in TF currency', release_amount_in_mortgage_currency)
        if release_amount_in_tf_currency:
            self.fo_write_number_group('Release amount in TF currency', release_amount_in_tf_currency)
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if base_amount:
            self.fo_assert_value('Base amount', base_amount)
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references TRD_RSC: {transaction_references}')
            mortgage_account_mask=self.fo_get_value_group('Mortgage account number')
            print(f'Mortgage account number: {mortgage_account_mask}')
            trade_account_mask=self.fo_get_value_group('Trade finance account number')
            print(f'Trade finance account number: {trade_account_mask}')
            return transaction_references, mortgage_account_mask, trade_account_mask

    def trd_rsc_view(self, transaction_references, mortgage_account_number=None, asset_booking_value=None, mortgage_account_currency=None, trade_finance_account_number=None, trade_finance_account_currency=None, exchange_rate=None, release_amount_in_mortgage_currency=None, release_amount_in_tf_currency=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, base_amount=None, description=None, secured_amount_for_tf_account=None, expected_posting=None):
        self.transaction_view(transaction_references, '7757: OLC - Release secure collateral')
        # compare value
        if mortgage_account_number:
            self.fo_assert_value_group('Mortgage account number', mortgage_account_number)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if mortgage_account_currency:
            self.fo_assert_select('Mortgate account currency', mortgage_account_currency)
        if trade_finance_account_number:
            self.fo_assert_value_group('Trade finance account number', trade_finance_account_number)
        if trade_finance_account_currency:
            self.fo_assert_select('Trade finance account currency', trade_finance_account_currency)
        if secured_amount_for_tf_account:
            self.fo_assert_value('Secured amount for TF account', secured_amount_for_tf_account)
        if exchange_rate:
            self.fo_assert_value('Exchange rate', exchange_rate)
        if release_amount_in_mortgage_currency:
            self.fo_assert_value('Release amount in mortgage currency', release_amount_in_mortgage_currency)
        if release_amount_in_tf_currency:
            self.fo_assert_value_group('Release amount in TF currency', release_amount_in_tf_currency)
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if base_amount:
            self.fo_assert_value('Base amount', base_amount)
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        mortgage_account_mask=self.fo_get_value_group('Mortgage account number')
        print(f'Mortgage account number: {mortgage_account_mask}')
        trade_account_mask=self.fo_get_value_group('Trade finance account number')
        print(f'Trade finance account number: {trade_account_mask}')
        return transaction_references, mortgage_account_mask, trade_account_mask

    # TRD_SBX: SG/BG - Extension
    def trd_sbx(self, account_number, beneficiary=None, maturity_date=None, extend_period=None, bg_number=None, fee_collect_method=None, total_fee_amount=None, applicant=None, sg_bg_amount=None, extend_to_date=None, extend_period_unit=None, extension_time=None, extension_date=None, account_number_for_fee=None, ifc_code=None, value=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_SBX', 'Extension')
        self.wait_for_button_available('Accept')
        self.assert_form_title('SG/BG - Extension')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.key_escape()
        if applicant:
            self.fo_assert_text_group('Applicant', applicant)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if sg_bg_amount:
            self.fo_assert_value('SG/BG Amount', sg_bg_amount)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if extension_date:
            self.fo_write_date('Extension date', extension_date)
        self.key_escape()
        if extend_period:
            self.fo_select('Extend period', extend_period)
        self.key_escape()
        if extend_period_unit:
            self.fo_select('Extend period unit', extend_period_unit)
        if extend_to_date:
            self.fo_assert_date('Extend to date', extend_to_date)
        if bg_number:
            self.fo_assert_text('BG number', bg_number)
        if extension_time:
            self.fo_assert_value('Extension time', extension_time)
            self.fo_assert_text('Extension BG number', f'{bg_number} Ex-{extension_time}')
        # add fee
        if ifc_code:
            self.click_button('Add')
            self.wait_loading()
            self.fo_write_text_group('Interest/fee/charge code', ifc_code)
            self.wait_loading()
            self.fo_write_number('Value', value)
            self.wait_loading()
            self.click_button('Apply')
            self.wait_loading()
            if total_fee:
                self.assert_total_fee_table_data(total_fee)
            if total_fee_amount:
                self.fo_assert_value('Total fee amount', total_fee_amount)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_write_text_group('Account number for fee', str(account_number_for_fee).replace('-', ''))
        self.fo_write_text('Description', 'AUTO TEST')
        self.key_escape()
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references TRD_SBX: {transaction_references}')
            trade_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {trade_account_mask}')
            return transaction_references, trade_account_mask

    def trd_sbx_view(self, transaction_references, account_number=None, beneficiary=None, maturity_date=None, extend_period=None, bg_number=None, fee_collect_method=None, total_fee_amount=None, applicant=None, sg_bg_amount=None, extend_to_date=None, extend_period_unit=None, extension_time=None, extension_date=None, account_number_for_fee=None, ifc_code=None, value=None, total_fee=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'SG/BG - Extension')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.trade_account_number_mask(account_number))
        if applicant:
            self.fo_assert_text_group('Applicant', applicant)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if sg_bg_amount:
            self.fo_assert_value('SG/BG Amount', sg_bg_amount)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if extend_to_date:
            self.fo_assert_date('Extend to date', extend_to_date)
        if extend_period:
            self.fo_assert_select('Extend period', extend_period)
        if extend_period_unit:
            self.fo_assert_select('Extend period unit', extend_period_unit)
        if bg_number:
            self.fo_assert_text('BG number', bg_number)
        if extension_time:
            self.fo_assert_value('Extension time', extension_time)
            self.fo_assert_text('Extension BG number', f'{bg_number} Ex-{extension_time}')
        if extension_date:
            self.fo_assert_date('Extension date', extension_date)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', account_number_for_fee)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if description:
            self.fo_assert_text('Description', description)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
            self.assert_table_data('Value type', 1, 'Percentage')
            self.assert_table_data('Fee', 1, total_fee_amount)
        if value:
            self.assert_table_data('Value', 1, value)
        if total_fee:
            self.assert_total_fee_table_data(total_fee)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        trade_account_mask=self.fo_get_value_group('Account number')
        print(f'Account number: {trade_account_mask}')
        return transaction_references, trade_account_mask

    # TRD_FCC: 7728: IFC - Fee collection
    def trd_fcc(self, account_number, account_holder_type=None, account_holder_code=None, country_code=None, currency_code=None, applicant=None, beneficiary=None, total_fee_amount=None, fee_collect_method=None, account_number_for_fee=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_FCC', '7728')
        self.wait_for_button_available('Accept')
        self.assert_form_title('7728: IFC - Fee collection')
        # enter value
        account_number_value = str(account_number).replace('-', '')
        self.fo_write_group('Account number', account_number_value)
        self.wait_loading()
        self.key_escape()
        if account_holder_type:
            self.fo_assert_select('Account holder type', account_holder_type)
        if account_holder_code:
            self.fo_assert_value('Account holder code', account_holder_code)
        if country_code:
            self.fo_assert_text_group('Country code', country_code)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if applicant:
            self.fo_assert_text('Applicant', applicant)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee=total_fee)
            if total_fee_amount:
                self.fo_assert_value('Total fee amount', total_fee_amount)
        self.key_escape()
        if fee_collect_method:
            self.fo_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            account_number_for_fee_value = str(account_number_for_fee).replace('-', '')
            self.fo_write_text_group('Account number for fee', account_number_for_fee_value)
        self.fo_write_text('Description', 'AUTO TEST')
        self.key_escape()
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references TRD_FCC: {transaction_references}')
            trade_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {trade_account_mask}')
            return transaction_references, trade_account_mask

    def trd_fcc_view(self, transaction_references, account_number=None, account_holder_type=None, account_holder_code=None, country_code=None, currency_code=None, applicant=None, beneficiary=None, total_fee_amount=None, fee_collect_method=None, account_number_for_fee=None, ifc_code=None, value=None, total_fee=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '7728: IFC - Fee collection')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.trade_account_number_mask(account_number))
        if account_holder_type:
            self.fo_assert_select('Account holder type', account_holder_type)
        if account_holder_code:
            self.fo_assert_value('Account holder code', account_holder_code)
        if country_code:
            self.fo_assert_text_group('Country code', country_code)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if applicant:
            self.fo_assert_text('Applicant', applicant)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if total_fee_amount:
            self.fo_assert_value('Total fee amount', total_fee_amount)
        if fee_collect_method:
            self.fo_assert_select('Fee collect method', fee_collect_method)
        if account_number_for_fee:
            self.fo_assert_text_group('Account number for fee', account_number_for_fee)
        if description:
            self.fo_assert_text('Description', description)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
            self.assert_table_data('Value type', 1, 'Flat amount')
            self.assert_table_data('Fee', 1, total_fee_amount)
        if value:
            self.assert_table_data('Value', 1, value)
        if total_fee:
            self.assert_total_fee_table_data(total_fee)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        trade_account_mask=self.fo_get_value_group('Account number')
        print(f'Account number: {trade_account_mask}')
        return transaction_references, trade_account_mask

    # TRD_SCL: 7758: SG - Close
    def trd_scl(self, account_number, sg_bg_amount=None, margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, margin_method=None, margin_deposit_account=None, applicant=None, bg_number=None, beneficiary=None, beneficiary_address=None, maturity_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TRD_SCL', 'Close')
        self.wait_for_button_available('Accept')
        self.assert_form_title('7758: SG - Close')
        # enter value
        self.fo_write_group('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.key_escape()
        self.fo_select('Margin method', 'Cash')
        if sg_bg_amount:
            self.fo_assert_value('SG/BG amount', sg_bg_amount)
        if margin_rate:
            self.fo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        self.key_escape()
        if margin_method:
            self.fo_select('Margin method', margin_method)
        if margin_deposit_account:
            self.fo_write_group('Margin deposit account', margin_deposit_account)
        if applicant:
            self.fo_assert_text_group('Applicant', applicant)
        if bg_number:
            self.fo_assert_text('BG number', bg_number)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        self.fo_write_text('Description', 'AUTO TEST')
        self.key_escape()
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        self.fo_click_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.')
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
            print(f'Transaction references TRD_SCL: {transaction_references}')
            trade_account_mask=self.fo_get_value_group('Account number')
            print(f'Account number: {trade_account_mask}')
            return transaction_references, trade_account_mask

    def trd_scl_view(self, transaction_references, account_number=None, sg_bg_amount=None, margin_rate=None, margin_amount=None, guarantee_amount=None, secured_amount=None, margin_method=None, margin_deposit_account=None, applicant=None, bg_number=None, beneficiary=None, beneficiary_address=None, maturity_date=None, description=None, expected_posting=None):
        self.transaction_view(transaction_references, '7758: SG - Close')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.trade_account_number_mask(account_number))
        if sg_bg_amount:
            self.fo_assert_value('SG/BG amount', sg_bg_amount)
        if margin_rate:
            self.fo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.fo_assert_value('Margin amount', margin_amount)
        if guarantee_amount:
            self.fo_assert_value('Guarantee amount', guarantee_amount)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if margin_method:
            self.fo_assert_select('Margin method', margin_method)
        if margin_deposit_account:
            self.fo_assert_value_group('Margin deposit account', margin_deposit_account)
        if applicant:
            self.fo_assert_text_group('Applicant', applicant)
        if bg_number:
            self.fo_assert_text('BG number', bg_number)
        if beneficiary:
            self.fo_assert_text('Beneficiary', beneficiary)
        if beneficiary_address:
            self.fo_assert_text('Beneficiary address', beneficiary_address)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if description:
            self.fo_assert_text('Description', description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        trade_account_mask=self.fo_get_value_group('Account number')
        print(f'Account number: {trade_account_mask}')
        return transaction_references, trade_account_mask

# -------------------------- handle BO - TRADE FINANCE --------------------------
    # TRD-IFC Item Definition
    def trade_ifc_item_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Trade Finance', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-IFC Item Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def trade_ifc_item_definition_advanced_search(self, ifc_code_from=None, ifc_code_to=None, ifc_name=None, value_type=None, ifc_type=None, value_from=None, value_to=None, tenor_from=None, tenor_to=None, tenor_unit=None, active_condition=None, status=None):
        self.close_all_form()
        self.click_menu('Trade Finance', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-IFC Item Definition-Search')
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

    def trade_ifc_item_definition_add(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, charge_on=None, sys_account_names=None, account_aliass=None, list_transaction=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Trade Finance', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('TRD-IFC Item Definition-Add')
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
        self.key_escape()
        if charge_on:
            self.bo_select('Charge on', charge_on)
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

    def trade_ifc_item_definition_view(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, charge_on=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # search
        self.trade_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-IFC Item Definition-View')
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
        if charge_on:
            self.bo_assert_select('Charge on', charge_on)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def trade_ifc_item_definition_update(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, charge_on=None, list_transaction=None, list_error_message=None):
        # view
        self.trade_ifc_item_definition_view(ifc_code=ifc_code)
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
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        if floor_value:
            self.bo_write_number('Floor value', floor_value)
        if ceiling_value:
            self.bo_write_number('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_write_text('Value basis', value_basis)
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
        if ifc_status:
            self.bo_select('IFC status', ifc_status)
        if effect_date:
            self.bo_write_date('Effect Date', effect_date)
        if effect_value:
            self.bo_write_number('Effect Value', effect_value)
        self.key_escape()
        if charge_on:
            self.bo_select('Charge on', charge_on)
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
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor', tenor_unit)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
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

    def trade_ifc_item_definition_delete(self, ifc_code, list_error_message=None, expected_message=None):
        # search
        self.trade_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
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

    # TRD-IFC Auto Fee
    def trade_ifc_auto_fee_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Trade Finance', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-IFC Auto Fee-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def trade_ifc_auto_fee_advanced_search(self, transaction_code=None, transaction_name=None, ifc_code=None, ifc_name=None):
        self.close_all_form()
        self.click_menu('Trade Finance', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-IFC Auto Fee-Search')
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

    def trade_ifc_auto_fee_add(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Trade Finance', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('TRD-IFC Auto Fee-Add')
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

    def trade_ifc_auto_fee_view(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # search
        self.trade_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        if transaction_code:
            self.assert_table_data('Transaction code', 1, transaction_code)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-IFC Auto Fee-View')
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

    def trade_ifc_auto_fee_update(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # view
        self.trade_ifc_auto_fee_view(transaction_code=transaction_code, ifc_code=ifc_code)
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

    def trade_ifc_auto_fee_delete(self, transaction_code=None, ifc_code=None, list_error_message=None, expected_message=None):
        # search
        self.trade_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
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

    # TRD-Catalogue Definition
    def trade_catalogue_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Trade Finance', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-Catalogue Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def trade_catalogue_definition_advanced_search(self, catalogue_code=None, catalog_name=None, business_group=None, category=None, term=None, customer_type=None, catalogue_status=None, creator=None, status=None, obs_percentage_rate=None):
        self.close_all_form()
        self.click_menu('Trade Finance', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-Catalogue Definition-Search')
        if catalogue_code:
            self.adv_search('Catalogue code', catalogue_code)
        if catalog_name:
            self.adv_search_text('Catalog name', catalog_name)
        self.key_escape()
        if business_group:
            self.adv_search_select('Business group', business_group)
        self.key_escape()
        if category:
            self.adv_search_select('Category', category)
        self.key_escape()
        if term:
            self.adv_search_select('Term', term)
        self.key_escape()
        if customer_type:
            self.adv_search_select('Customer type', customer_type)
        self.key_escape()
        if catalogue_status:
            self.adv_search_select('Catalogue status', catalogue_status)
        if creator:
            self.adv_search_text('Creator', creator)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        if obs_percentage_rate:
            self.adv_search_text('OBS percentage/rate', obs_percentage_rate)
        self.click_button_search_advanced()
        self.wait_loading()

    def trade_catalogue_definition_add(self, catalogue_code=None, catalogue_name=None, business_group=None, details_category=None, term_and_condition=None, tenor=None, customer_type=None, catalogue_status=None, user_create=None, approve_by=None, obs_percentage_rate=None, ifc_codes=None, sys_account_names=None, account_aliass=None, coa_accounts=None, replace_bys=None, system_account_names=None, customer_sectors=None, customer_resident_statuss=None, business_lines=None, sub_products=None, bank_identifications=None, replace_code=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Trade Finance', 'Catalogue Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('TRD-Catalogue Definition-Add')
        # enter value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_write('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        self.key_escape()
        if business_group:
            self.bo_select('Business group', business_group)
        self.key_escape()
        if details_category:
            self.bo_select('Details category', details_category)
        self.key_escape()
        if term_and_condition:
            self.bo_select('Term and condition', term_and_condition)
        self.key_escape()
        if tenor:
            self.bo_select('Tenor', tenor)
        self.key_escape()
        if customer_type:
            self.bo_select('Customer type', customer_type)
        self.key_escape()
        if catalogue_status:
            self.bo_select('Catalogue status', catalogue_status)
        if obs_percentage_rate:
            self.bo_write_number('OBS percentage/rate', obs_percentage_rate)
        # assert value
        self.bo_click_tab('General information')
        if user_create:
            self.bo_assert_text('User create', user_create)
        if approve_by:
            self.bo_assert_text('Approve by', approve_by)
        self.bo_click_tab('IFC information ')
        if ifc_codes:
            for ifc_code in ifc_codes:
                self.click_button_in_tab('Add')
                self.wait_loading()
                self.select('IFC Code', ifc_code)
                self.click_button_in_tab('Apply')
                self.wait_loading()
        self.bo_click_tab('GLs information ')
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

    def trade_catalogue_definition_view(self, catalogue_code=None, catalogue_name=None, business_group=None, details_category=None, term_and_condition=None, tenor=None, customer_type=None, catalogue_status=None, user_create=None, approve_by=None, obs_percentage_rate=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # search
        self.trade_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalog Code', 1, catalogue_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-Catalogue Definition-View')
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if business_group:
            self.bo_assert_select('Business group', business_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if term_and_condition:
            self.bo_assert_select('Term and condition', term_and_condition)
        if tenor:
            self.bo_assert_select('Tenor', tenor)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if user_create:
            self.bo_assert_text_group('User create', user_create)
        if approve_by:
            self.bo_assert_text_group('Approve by', approve_by)
        if obs_percentage_rate:
            self.bo_assert_value('OBS percentage/rate', obs_percentage_rate)
        self.bo_click_tab('IFC information ')
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
        self.bo_click_tab('GLs information ')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')

    def trade_catalogue_definition_update(self, catalogue_code=None, catalogue_name=None, business_group=None, details_category=None, term_and_condition=None, tenor=None, customer_type=None, catalogue_status=None, user_create=None, approve_by=None, obs_percentage_rate=None, ifc_codes=None, sys_account_names=None, account_aliass=None, coa_accounts=None, replace_bys=None, system_account_names=None, customer_sectors=None, customer_resident_statuss=None, business_lines=None, sub_products=None, bank_identifications=None, replace_code=None, list_error_message=None):
        # view
        self.trade_catalogue_definition_view(catalogue_code=catalogue_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        # assert value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if business_group:
            self.bo_assert_select('Business group', business_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if term_and_condition:
            self.bo_assert_select('Term and condition', term_and_condition)
        if tenor:
            self.bo_assert_select('Tenor', tenor)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if user_create:
            self.bo_assert_text_group('User create', user_create)
        if approve_by:
            self.bo_assert_text_group('Approve by', approve_by)
        if obs_percentage_rate:
            self.bo_assert_value('OBS percentage/rate', obs_percentage_rate)
        self.bo_click_tab('IFC information ')
        if ifc_codes:
            for ifc_code in ifc_codes:
                self.click_button_in_tab('Add')
                self.wait_loading()
                self.select('IFC Code', ifc_code)
                self.click_button_in_tab('Apply')
                self.wait_loading()
        self.bo_click_tab('GLs information ')
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

    def trade_catalogue_definition_delete(self, catalogue_code, list_error_message=None, expected_message=None):
        # search
        self.trade_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalog Code', 1, catalogue_code)
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

    # TRD-Trade account information
    def trade_account_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Trade Finance', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-Account Information Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def trade_account_advanced_search(self, account_number=None, customer_code=None, account_name=None, customer_type=None, branch_code=None, catalogue_code=None, currency_code=None, account_status=None):
        self.close_all_form()
        self.click_menu('Trade Finance', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-Account Information Search')
        if account_number:
            self.adv_search('Account number', str(account_number).replace('-', ''))
        if customer_code:
            self.adv_search('Customer code', str(customer_code).replace('-', ''))
        if account_name:
            self.adv_search_text('Account name', account_name)
        self.key_escape()
        if customer_type:
            self.adv_search_select('Customer type', customer_type)
        if branch_code:
            self.adv_search_text('Branch code', branch_code)
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        self.key_escape()
        if currency_code:
            self.adv_search_select('Currency code', currency_code)
        self.key_escape()
        if account_status:
            self.adv_search_select('Account Status', account_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def trade_account_view(self, account_number, account_status=None, category_code=None, customer_code=None, account_name=None, account_holder_type=None, branch_code=None, currency_code=None, business_group=None, details_category=None, term_and_condition=None, tenor=None, reference_number=None, customer_type=None, counter_party_name=None, counter_party_address=None, usance_days=None, holding_days=None, open_date=None, close_date=None, extension_date=None, effective_date=None, effective_date_extension=None, maturity_date=None, maturity_date_extension=None, last_date_of_shippment=None, last_transaction_date=None, previous_ac_status=None, document_status=None, previous_doc_status=None, place_of_maturity=None, country=None, partial_shipments=None, transhipment=None, created_by=None, approved_by=None, account_manager_staff_code=None, term_code=None, amount=None, release_amount=None, amount_paid=None, lower_tolerance=None, upper_tolerance=None, margin_deposit_account=None, margin_rate=None, margin_amount=None, released_margin_amount=None, guarantee_amount=None, released_guarantee_amount=None, secured_amount=None, released_secured_amount=None, off_balance_sheet_amount=None, release_off_balance_sheet_amount=None, off_balance_percentage=None, holding_amount=None, amount_sent_for_collection=None, amount_accept_of_payment=None, amount_arrived_of_payment=None, fee_amount=None, paid_fee_amount=None, negotiation_amount=None, transfer_amount=None, discounted_reta_reduction_rate=None, obs_percentage_rate=None, business_step_status_string=None, current_business_step=None, confirm=None, advising_maner=None, amend_no=None, draft_number=None, first_ref_account_number=None, cycle=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quarter_debit=None, quarter_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, expected_account_gl_names=None, expected_account_gl_numbers=None, expected_ifc_codes=None, expected_ifc_gl_names=None, expected_ifc_gl_numbers=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_base_values=None, expected_ifc_is_linkeds=None, expected_ifc_values=None, expected_ifc_margin_values=None, expected_ifc_statuses=None, expected_ifc_outstandings=None, expected_ifc_paids=None, expected_ifc_basic_balances=None, issuing_bank=None, confirming_bank=None, negotiating_bank=None, paying_bank=None, advising_bank=None, remitting_bank=None, reference_number_in_agent_bank=None, remark=None, guarantee_period=None, guarantee_period_unit=None, bg_number=None, project_name=None, send_to=None, user_define_field=None):
        # search trade account
        self.trade_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.trade_account_number_mask(account_number))
        if account_status:
            self.assert_table_data('Account status', 1, account_status)
        if category_code:
            self.assert_table_data('Category code', 1, category_code)
        if customer_code:
            self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code))
        # view trade account
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-Account Information-View')
        # verify value tab 'Account GLs Information'
        self.bo_click_tab('Account GLs Information')
        if expected_account_gl_names:
            for account_gl_name, account_gl_number in zip(expected_account_gl_names, expected_account_gl_numbers):
                self.bo_assert_text_table_account_gls(account_gl_name, str(account_gl_number).replace('-',''))
        # verify value tab 'General information'
        self.bo_click_tab('General information')
        self.bo_assert_value('Account number', self.trade_account_number_mask(account_number))
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if customer_code:
            self.bo_assert_value_group('Account holder code', self.customer_code_mask(customer_code))
        if account_holder_type:
            self.bo_assert_select('Account holder type', account_holder_type)
        if branch_code:
            self.bo_assert_text_group('Branch code', branch_code)
        if category_code:
            self.bo_assert_text_group('Category code', category_code)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if business_group:
            self.bo_assert_select('Business group', business_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if term_and_condition:
            self.bo_assert_select('Term and condition', term_and_condition)
        if tenor:
            self.bo_assert_select('Tenor', tenor)
        if reference_number:
            self.bo_assert_text('Reference number', reference_number)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if counter_party_name:
            self.bo_assert_text('Counter party name', counter_party_name)
        if counter_party_address:
            self.bo_assert_text('Counter party address', counter_party_address)
        if usance_days:
            self.bo_assert_value('Usance days', usance_days)
        if holding_days:
            self.bo_assert_value('Holding days', holding_days)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if extension_date:
            self.bo_assert_date('Extension date', extension_date)
        if effective_date:
            self.bo_assert_date('Effective date', effective_date)
        if effective_date_extension:
            self.bo_assert_date('Effective date extension', effective_date_extension)
        if maturity_date:
            self.bo_assert_date('Maturity date', maturity_date)
        if maturity_date_extension:
            self.bo_assert_date('Maturity date extension', maturity_date_extension)
        if last_date_of_shippment:
            self.bo_assert_date('Last date of shippment', last_date_of_shippment)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if account_status:
            self.bo_assert_select('Account status', account_status)
        if previous_ac_status:
            self.bo_assert_select('Previous A/c status', previous_ac_status)
        if document_status:
            self.bo_assert_select('Document status', document_status)
        if previous_doc_status:
            self.bo_assert_select('Previous doc status', previous_doc_status)
        if place_of_maturity:
            self.bo_assert_text('Place of Maturity', place_of_maturity)
        if country:
            self.bo_assert_select('Country', country)
        if partial_shipments:
            self.bo_assert_select('Partial shipments', partial_shipments)
        if transhipment:
            self.bo_assert_select('Transhipment', transhipment)
        if created_by:
            self.bo_assert_text('Created by', created_by)
        if approved_by:
            self.bo_assert_text('Approved by', approved_by)
        if account_manager_staff_code:
            self.bo_assert_text('Account manager staff code', account_manager_staff_code)
        # verify value tab 'Commercial term'
        self.bo_click_tab('Commercial term')
        if term_code:
            self.bo_assert_select('Term code', term_code)
        if amount:
            self.bo_assert_value('Amount', amount)
        if release_amount:
            self.bo_assert_value('Release amount', release_amount)
        if amount_paid:
            self.bo_assert_value('Amount paid', amount_paid)
        if lower_tolerance:
            self.bo_assert_value('Lower tolerance', lower_tolerance)
        if upper_tolerance:
            self.bo_assert_value('Upper tolerance', upper_tolerance)
        if margin_deposit_account:
            self.bo_assert_value('Margin deposit account', self.deposit_account_number_mask(margin_deposit_account))
        if margin_rate:
            self.bo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.bo_assert_value('Margin amount', margin_amount)
        if released_margin_amount:
            self.bo_assert_value('Released margin amount', released_margin_amount)
        if guarantee_amount:
            self.bo_assert_value('Guarantee amount', guarantee_amount)
        if released_guarantee_amount:
            self.bo_assert_value('Released guarantee amount', released_guarantee_amount)
        if secured_amount:
            self.bo_assert_value('Secured amount', secured_amount)
        if released_secured_amount:
            self.bo_assert_value('Released secured amount', released_secured_amount)
        if off_balance_sheet_amount:
            self.bo_assert_value('Off-balance sheet amount', off_balance_sheet_amount)
        if release_off_balance_sheet_amount:
            self.bo_assert_value('Release off-balance sheet amount', release_off_balance_sheet_amount)
        if off_balance_percentage:
            self.bo_assert_value('Off Balance Percentage', off_balance_percentage)
        if holding_amount:
            self.bo_assert_value('Holding amount', holding_amount)
        if amount_sent_for_collection:
            self.bo_assert_value('Amount sent for collection', amount_sent_for_collection)
        if amount_accept_of_payment:
            self.bo_assert_value('Amount accept of payment', amount_accept_of_payment)
        if amount_arrived_of_payment:
            self.bo_assert_value('Amount arrived of payment', amount_arrived_of_payment)
        if fee_amount:
            self.bo_assert_value('Fee amount', fee_amount)
        if paid_fee_amount:
            self.bo_assert_value('Paid fee amount', paid_fee_amount)
        if negotiation_amount:
            self.bo_assert_value('Negotiation amount', negotiation_amount)
        if transfer_amount:
            self.bo_assert_value('Transfer amount', transfer_amount)
        if discounted_reta_reduction_rate:
            self.bo_assert_value('Discounted reta/reduction rate', discounted_reta_reduction_rate)
        if obs_percentage_rate:
            self.bo_assert_value('OBS percentage/rate', obs_percentage_rate)
        if business_step_status_string:
            self.bo_assert_text('Business step status string', business_step_status_string)
        if current_business_step:
            self.bo_assert_text('Current business step', current_business_step)
        if confirm:
            self.bo_assert_select('Confirm', confirm)
        if advising_maner:
            self.bo_assert_select('Advising maner', advising_maner)
        if amend_no:
            self.bo_assert_value('Amend no', amend_no)
        if draft_number:
            self.bo_assert_text('Draft number', draft_number)
        if first_ref_account_number:
            self.bo_assert_text('1st ref account number', first_ref_account_number)
        if cycle:
            self.bo_assert_value('Cycle', cycle)
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
        # verify value tab 'IFC list'
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
        # verify value tab 'IFC GLs Information'
        self.bo_click_tab('IFC GLs Information')
        if expected_ifc_codes:
            for ifc_code, ifc_gl_name, ifc_gl_number in zip(expected_ifc_codes, expected_ifc_gl_names, expected_ifc_gl_numbers):
                self.bo_assert_text_table_ifc_gls(ifc_code, ifc_gl_name, str(ifc_gl_number).replace('-',''))
        # verify value tab 'Other information'
        self.bo_click_tab('Other information')
        if issuing_bank:
            self.bo_assert_text('Issuing bank', issuing_bank)
        if confirming_bank:
            self.bo_assert_value_group('Confirming bank', confirming_bank)
        if negotiating_bank:
            self.bo_assert_value_group('Negotiating bank', negotiating_bank)
        if paying_bank:
            self.bo_assert_value_group('Paying bank', paying_bank)
        if advising_bank:
            self.bo_assert_value_group('Advising bank', advising_bank)
        if remitting_bank:
            self.bo_assert_value_group('Remitting bank', remitting_bank)
        if reference_number_in_agent_bank:
            self.bo_assert_text('Reference number in agent bank', reference_number_in_agent_bank)
        if remark:
            self.bo_assert_text('Remark', remark)
        if guarantee_period:
            self.bo_assert_select('Guarantee period', guarantee_period)
        if guarantee_period_unit:
            self.bo_assert_select('Guarantee period unit', guarantee_period_unit)
        if bg_number:
            self.bo_assert_text('BG number', bg_number)
        if project_name:
            self.bo_assert_text('Project name', project_name)
        if send_to:
            self.fo_assert_text_multi_line('Send to', send_to)
        if user_define_field:
            self.bo_assert_text('User define field', user_define_field)
        # verify value tab 'Document attachment'
        self.bo_click_tab('Document attachment')

    def trade_account_update(self, account_number=None, account_name=None, account_holder_code=None, account_holder_type=None, branch_code=None, category_code=None, currency_code=None, business_group=None, details_category=None, term_and_condition=None, tenor=None, reference_number=None, customer_type=None, counter_party_name=None, counter_party_address=None, usance_days=None, holding_days=None, open_date=None, close_date=None, extension_date=None, effective_date=None, effective_date_extension=None, maturity_date=None, maturity_date_extension=None, last_date_of_shippment=None, last_transaction_date=None, account_status=None, previous_a_c_status=None, document_status=None, previous_doc_status=None, place_of_maturity=None, country=None, partial_shipments=None, transhipment=None, created_by=None, approved_by=None, account_manager_staff_code=None, term_code=None, amount=None, release_amount=None, amount_paid=None, lower_tolerance=None, upper_tolerance=None, margin_deposit_account=None, margin_rate=None, margin_amount=None, released_margin_amount=None, guarantee_amount=None, released_guarantee_amount=None, secured_amount=None, released_secured_amount=None, off_balance_sheet_amount=None, release_off_balance_sheet_amount=None, off_balance_percentage=None, holding_amount=None, amount_sent_for_collection=None, amount_accept_of_payment=None, amount_arrived_of_payment=None, fee_amount=None, paid_fee_amount=None, negotiation_amount=None, transfer_amount=None, discounted_reta_reduction_rate=None, obs_percentage_rate=None, business_step_status_string=None, current_business_step=None, confirm=None, advising_maner=None, amend_no=None, draft_number=None, first_ref_account_number=None, cycle=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quarter_debit=None, quarter_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, issuing_bank=None, confirming_bank=None, negotiating_bank=None, paying_bank=None, advising_bank=None, remitting_bank=None, reference_number_in_agent_bank=None, remark=None, guarantee_period=None, guarantee_period_unit=None, bg_number=None, project_name=None, send_to=None, user_define_field=None, list_error_message=None):
        # view
        self.trade_account_view(account_number=account_number)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if account_name:
            self.bo_write_text('Account name', account_name)
        self.bo_click_tab('Commercial term')
        self.key_escape()
        if term_code:
            self.bo_select('Term code', term_code)
        self.bo_click_tab('Other information')
        if confirming_bank:
            self.bo_write_group('Confirming bank', confirming_bank)
        if negotiating_bank:
            self.bo_write_group('Negotiating bank', negotiating_bank)
        if paying_bank:
            self.bo_write_group('Paying bank', paying_bank)
        if advising_bank:
            self.bo_write_group('Advising bank', advising_bank)
        if remitting_bank:
            self.bo_write_group('Remitting bank', remitting_bank)
        if reference_number_in_agent_bank:
            self.bo_write_text('Reference number in agent bank', reference_number_in_agent_bank)
        if remark:
            self.bo_write_text('Remark', remark)
        if user_define_field:
            self.bo_write_text('User define field', user_define_field)
        # assert value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_value('Account number', self.trade_account_number_mask(account_number))
        if account_holder_code:
            self.bo_assert_value_group('Account holder code', self.customer_code_mask(account_holder_code))
        if account_holder_type:
            self.bo_assert_select('Account holder type', account_holder_type)
        if branch_code:
            self.bo_assert_text_group('Branch code', branch_code)
        if category_code:
            self.bo_assert_text_group('Category code', category_code)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if business_group:
            self.bo_assert_select('Business group', business_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if term_and_condition:
            self.bo_assert_select('Term and condition', term_and_condition)
        if tenor:
            self.bo_assert_select('Tenor', tenor)
        if reference_number:
            self.bo_assert_text('Reference number', reference_number)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if counter_party_name:
            self.bo_assert_text('Counter party name', counter_party_name)
        if counter_party_address:
            self.bo_assert_text('Counter party address', counter_party_address)
        if usance_days:
            self.bo_assert_value('Usance days', usance_days)
        if holding_days:
            self.bo_assert_value('Holding days', holding_days)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if extension_date:
            self.bo_assert_date('Extension date', extension_date)
        if effective_date:
            self.bo_assert_date('Effective date', effective_date)
        if effective_date_extension:
            self.bo_assert_date('Effective date extension', effective_date_extension)
        if maturity_date:
            self.bo_assert_date('Maturity date', maturity_date)
        if maturity_date_extension:
            self.bo_assert_date('Maturity date extension', maturity_date_extension)
        if last_date_of_shippment:
            self.bo_assert_date('Last date of shippment', last_date_of_shippment)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if account_status:
            self.bo_assert_select('Account status', account_status)
        if previous_a_c_status:
            self.bo_assert_select('Previous A/c status', previous_a_c_status)
        if document_status:
            self.bo_assert_select('Document status', document_status)
        if previous_doc_status:
            self.bo_assert_select('Previous doc status', previous_doc_status)
        if place_of_maturity:
            self.bo_assert_text('Place of Maturity', place_of_maturity)
        if country:
            self.bo_assert_select('Country', country)
        if partial_shipments:
            self.bo_assert_select('Partial shipments', partial_shipments)
        if transhipment:
            self.bo_assert_select('Transhipment', transhipment)
        if created_by:
            self.bo_assert_text('Created by', created_by)
        if approved_by:
            self.bo_assert_text('Approved by', approved_by)
        if account_manager_staff_code:
            self.bo_assert_text('Account manager staff code', account_manager_staff_code)
        self.bo_click_tab('Commercial term')
        if amount:
            self.bo_assert_value('Amount', amount)
        if release_amount:
            self.bo_assert_value('Release amount', release_amount)
        if amount_paid:
            self.bo_assert_value('Amount paid', amount_paid)
        if lower_tolerance:
            self.bo_assert_value('Lower tolerance', lower_tolerance)
        if upper_tolerance:
            self.bo_assert_value('Upper tolerance', upper_tolerance)
        if margin_deposit_account:
            self.bo_assert_value('Margin deposit account', self.deposit_account_number_mask(margin_deposit_account))
        if margin_rate:
            self.bo_assert_value('Margin rate', margin_rate)
        if margin_amount:
            self.bo_assert_value('Margin amount', margin_amount)
        if released_margin_amount:
            self.bo_assert_value('Released margin amount', released_margin_amount)
        if guarantee_amount:
            self.bo_assert_value('Guarantee amount', guarantee_amount)
        if released_guarantee_amount:
            self.bo_assert_value('Released guarantee amount', released_guarantee_amount)
        if secured_amount:
            self.bo_assert_value('Secured amount', secured_amount)
        if released_secured_amount:
            self.bo_assert_value('Released secured amount', released_secured_amount)
        if off_balance_sheet_amount:
            self.bo_assert_value('Off-balance sheet amount', off_balance_sheet_amount)
        if release_off_balance_sheet_amount:
            self.bo_assert_value('Release off-balance sheet amount', release_off_balance_sheet_amount)
        if off_balance_percentage:
            self.bo_assert_value('Off Balance Percentage', off_balance_percentage)
        if holding_amount:
            self.bo_assert_value('Holding amount', holding_amount)
        if amount_sent_for_collection:
            self.bo_assert_value('Amount sent for collection', amount_sent_for_collection)
        if amount_accept_of_payment:
            self.bo_assert_value('Amount accept of payment', amount_accept_of_payment)
        if amount_arrived_of_payment:
            self.bo_assert_value('Amount arrived of payment', amount_arrived_of_payment)
        if fee_amount:
            self.bo_assert_value('Fee amount', fee_amount)
        if paid_fee_amount:
            self.bo_assert_value('Paid fee amount', paid_fee_amount)
        if negotiation_amount:
            self.bo_assert_value('Negotiation amount', negotiation_amount)
        if transfer_amount:
            self.bo_assert_value('Transfer amount', transfer_amount)
        if discounted_reta_reduction_rate:
            self.bo_assert_value('Discounted reta/reduction rate', discounted_reta_reduction_rate)
        if obs_percentage_rate:
            self.bo_assert_value('OBS percentage/rate', obs_percentage_rate)
        if business_step_status_string:
            self.bo_assert_text('Business step status string', business_step_status_string)
        if current_business_step:
            self.bo_assert_text('Current business step', current_business_step)
        if confirm:
            self.bo_assert_select('Confirm', confirm)
        if advising_maner:
            self.bo_assert_select('Advising maner', advising_maner)
        if amend_no:
            self.bo_assert_value('Amend no', amend_no)
        if draft_number:
            self.bo_assert_text('Draft number', draft_number)
        if first_ref_account_number:
            self.bo_assert_text('1st ref account number', first_ref_account_number)
        if cycle:
            self.bo_assert_value('Cycle', cycle)
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
        self.bo_click_tab('Other information')
        if issuing_bank:
            self.bo_assert_text('Issuing bank', issuing_bank)
        if guarantee_period:
            self.bo_assert_select('Guarantee period', guarantee_period)
        if guarantee_period_unit:
            self.bo_assert_select('Guarantee period unit', guarantee_period_unit)
        if bg_number:
            self.bo_assert_text('BG number', bg_number)
        if project_name:
            self.bo_assert_text('Project name', project_name)
        if send_to:
            self.bo_assert_text_multi_line('Send to', send_to)
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

    def trade_account_delete(self, account_number, list_error_message=None):
        # search
        self.trade_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.trade_account_number_mask(account_number))
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
            self.trade_account_simple_search(str(account_number).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {account_number}')
            return account_number

    # TRD-Document attachment
    def trade_document_attachment_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Trade Finance', 'Document Attachment')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-Document attachment-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def trade_document_attachment_advanced_search(self, account_number=None, document_name=None, document_type=None, status=None, open_date_from=None, open_date_to=None, last_date_from=None, last_date_to=None, expire_date_from=None, expire_date_to=None):
        self.close_all_form()
        self.click_menu('Trade Finance', 'Document Attachment')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-Document attachment-Search')
        if account_number:
            self.adv_search('Account number', str(account_number).replace('-', ''))
        if document_name:
            self.adv_search_text('Document name', document_name)
        if document_type:
            self.adv_search_text('Document type', document_type)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        if open_date_from:
            self.adv_search_group('Open date from', open_date_from)
        if open_date_to:
            self.adv_search_group('Open date to', open_date_to)
        if last_date_from:
            self.adv_search_group('Last date from', last_date_from)
        if last_date_to:
            self.adv_search_group('Last date to', last_date_to)
        if expire_date_from:
            self.adv_search_group('Expire date from', expire_date_from)
        if expire_date_to:
            self.adv_search_group('Expire date to', expire_date_to)
        self.click_button_search_advanced()
        self.wait_loading()

    def trade_document_attachment_add(self, account_number, file_path, expire_date=None, document_description=None, import_date=None, last_update_date=None, document_type=None, document_name=None):
        # open form
        self.close_all_form()
        self.click_menu('Trade Finance', 'Document Attachment')
        self.wait_for_button_available('Add')
        self.assert_form_title('TRD-Document attachment-Search')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('TRD-Document attachment-Add')
        # choose file
        self.bo_choose_file(file_path)
        # enter value
        self.bo_set_value('Account number', account_number)
        if expire_date:
            self.bo_set_value('Expire Date', expire_date)
        if document_description:
            self.bo_set_text('Document description', document_description)
        self.click_button('Save')
        self.assert_button_disable('Save')
        self.check_notification('Save successfully')
        account_number = self.bo_get_value_data('Account number')
        # search and verify
        self.trade_document_attachment_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account Number', 1, self.trade_account_number_mask(account_number))
        self.assert_table_data('Approve date', 1, ' ')
        self.assert_table_data('Status', 1, 'Pending Approve')
        if expire_date:
            self.assert_table_data('Expire date', 1, expire_date)
        if document_description:
            self.assert_table_data('Document description', 1, document_description)
        if import_date:
            self.assert_table_data('Import date', 1, import_date)
        if last_update_date:
            self.assert_table_data('Last update date', 1, last_update_date)
        if document_type:
            self.assert_table_data('Document type', 1, document_type)
        if document_name:
            self.assert_table_data('Document name', 1, document_name)
        print('Account number: ' + account_number)
        return account_number

    def trade_document_attachment_view(self, account_number, expire_date=None, document_description=None, status=None, approve_date=None, import_date=None, last_update_date=None, document_type=None, document_name=None):
        # search and verify trade document attachment
        self.trade_document_attachment_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account Number', 1, self.trade_account_number_mask(account_number))
        if approve_date:
            self.assert_table_data('Approve date', 1, approve_date)
        if status:
            self.assert_table_data('Status', 1, status)
        if expire_date:
            self.assert_table_data('Expire date', 1, expire_date)
        if document_description:
            self.assert_table_data('Document description', 1, document_description)
        if import_date:
            self.assert_table_data('Import date', 1, import_date)
        if last_update_date:
            self.assert_table_data('Last update date', 1, last_update_date)
        if document_type:
            self.assert_table_data('Document type', 1, document_type)
        if document_name:
            self.assert_table_data('Document name', 1, document_name)
        # view trade document attachment
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-Document attachment-View')
        self.click_close_notification()
        # verify value tab 'General'
        self.bo_assert_value_data('Account number', self.trade_account_number_mask(account_number))
        if expire_date:
            self.bo_assert_value_data('Expire Date', expire_date)
        if document_description:
            self.bo_assert_text_data('Document description', document_description)

    def trade_document_attachment_update(self, account_number, expire_date=None, document_description=None, status=None, approve_date=None, import_date=None, last_update_date=None, document_type=None, document_name=None):
        self.trade_document_attachment_view(account_number)
        self.wait_loading()
        self.click_button('Modify')
        # update value tab 'General'
        if expire_date:
            self.bo_set_value('Expire Date', expire_date)
        if document_description:
            self.bo_set_text('Document description', document_description)
        # click 'Save'
        self.click_button('Save')
        self.assert_button_disable('Save')
        self.check_notification('Save successfully')
        account_number = self.bo_get_value_data('Account number')
        # search and verify
        self.trade_document_attachment_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account Number', 1, self.trade_account_number_mask(account_number))
        if approve_date:
            self.assert_table_data('Approve date', 1, approve_date)
        if status:
            self.assert_table_data('Status', 1, status)
        if expire_date:
            self.assert_table_data('Expire date', 1, expire_date)
        if document_description:
            self.assert_table_data('Document description', 1, document_description)
        if import_date:
            self.assert_table_data('Import date', 1, import_date)
        if last_update_date:
            self.assert_table_data('Last update date', 1, last_update_date)
        if document_type:
            self.assert_table_data('Document type', 1, document_type)
        if document_name:
            self.assert_table_data('Document name', 1, document_name)
        print('Account number: ' + account_number)
        return account_number

    def trade_document_attachment_approve(self, account_number, expire_date=None, document_description=None, approve_date=None, import_date=None, last_update_date=None, document_type=None, document_name=None):
        self.trade_document_attachment_view(account_number)
        self.wait_loading()
        self.click_button('Approve')
        self.assert_button_disable('Approve')
        self.wait_loading()
        self.check_notification('Approve successfully')
        account_number = self.bo_get_value_data('Account number')
        # search and verify
        self.trade_document_attachment_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account Number', 1, self.trade_account_number_mask(account_number))
        self.assert_table_data('Status', 1, 'Normal')
        if approve_date:
            self.assert_table_data('Approve date', 1, approve_date)
        if expire_date:
            self.assert_table_data('Expire date', 1, expire_date)
        if document_description:
            self.assert_table_data('Document description', 1, document_description)
        if import_date:
            self.assert_table_data('Import date', 1, import_date)
        if last_update_date:
            self.assert_table_data('Last update date', 1, last_update_date)
        if document_type:
            self.assert_table_data('Document type', 1, document_type)
        if document_name:
            self.assert_table_data('Document name', 1, document_name)
        print('Account number: ' + account_number)
        return account_number

    def trade_document_attachment_delete(self, account_number, list_error_message=None):
        # search
        self.trade_document_attachment_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account Number', 1, self.trade_account_number_mask(account_number))
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
            self.trade_document_attachment_simple_search(str(account_number).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {account_number}')
            return account_number

    def trade_document_attachment_get_information(self, account_number, account_name=None):
        self.trade_document_attachment_view(account_number)
        # click 'Get information'
        self.click_button('Get information')
        self.wait_loading()
        # verify
        self.assert_form_title_header_popup('Document Viewer')
        self.bo_assert_info_signature('Account number', self.no_mask(account_number))
        if account_name:
            self.bo_assert_info_signature('Account name', account_name)
        self.close_popup()

    # TRD-Account Linkage
    def trade_account_linkage_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Trade Finance', 'Account Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-Account Linkage-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def trade_account_linkage_advanced_search(self, master_module_name=None, master_account_number=None, master_account_name=None):
        self.close_all_form()
        self.click_menu('Trade Finance', 'Account Linkage')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRD-Account Linkage-Search')
        self.key_escape()
        if master_module_name:
            self.adv_search_select('Master module name', master_module_name)
        if master_account_number:
            self.adv_search_text('Master account number', str(master_account_number).replace('-', ''))
        if master_account_name:
            self.adv_search_text('Master account name', master_account_name)
        self.click_button_search_advanced()
        self.wait_loading()

    def trade_account_linkage_add(self):
        # # open form
        # self.close_all_form()
        # self.click_menu('Trade Finance', 'Account Linkage')
        # self.wait_for_button_available('Add')
        # self.click_button('Add')
        # self.wait_for_button_available('Accept')
        # self.assert_form_title('TRD-Account Linkage-Add')
        # # enter value
        print("The method has not yet been implemented. Please contact TESTER to do it.")
        return self.fail()

    def trade_account_linkage_view(self, master_module_name=None, master_account_number=None, row=None, linkage_module_name=None, linkage_account_code=None, linkage_account_name=None, linkage_description=None, linkage_type=None, linkage_classification=None):
        if row is None:
            row = 1
        # search
        self.trade_account_linkage_simple_search(str(master_account_number).replace('-', ''))
        self.assert_table_data('Master account number', 1, master_account_number)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-Account Linkage-View')
        # verify value
        self.bo_click_tab('General information')
        if master_module_name:
            self.bo_assert_select('Master module name', master_module_name)
        if master_account_number:
            self.bo_assert_value_group('Master account number', master_account_number)
        if linkage_module_name:
            self.assert_table_data('Linkage module name', row, linkage_module_name)
        if linkage_account_code:
            self.assert_table_data('Linkage account code', row, linkage_account_code)
        if linkage_account_name:
            self.assert_table_data('Linkage account name', row, linkage_account_name)
        if linkage_description:
            self.assert_table_data('Linkage description', row, linkage_description)
        if linkage_type:
            self.assert_table_data('Linkage type', row, linkage_type)
        if linkage_classification:
            self.assert_table_data('Linkage class', row, linkage_classification)

    def trade_account_linkage_update(self, master_module_name=None, master_account_number=None, list_error_message=None):
        # # view
        # self.trade_account_linkage_view(master_account_number=master_account_number)
        # self.click_button('Modify')
        # self.wait_loading()
        # # update value
        # # assert value
        # self.bo_click_tab('General information')
        # if master_module_name:
        #     self.bo_assert_select('Master module name', master_module_name)
        # if master_account_number:
        #     self.bo_assert_value_group('Master account number', master_account_number)
        # self.wait_loading()
        # # click 'Save'
        # self.click_button('Save')
        # if list_error_message:
        # # verify error
        #     self.assert_error_message()
        #     self.assert_list_error_message(list_error_message)
        #     print('Action update failed!')
        # else:
        # # verify success
        #     self.assert_button_disable('Save')
        #     self.check_notification('Saved successfully!')
        #     self.bo_click_tab('General information')
        #     master_account_number_out=self.bo_get_value_group('Master account number')
        #     print(f'Master account number: {master_account_number_out}')
        #     return master_account_number_out
        print("The method has not yet been implemented. Please contact TESTER to do it.")

    def trade_account_linkage_delete(self, master_account_number, list_error_message=None):
        # search
        self.trade_account_linkage_simple_search(str(master_account_number).replace('-', ''))
        self.assert_table_data('Master account number', 1, master_account_number)
        # delete
        self.click_table_menu('Delete', 1)
        self.wait_loading()
        self.click_button_in_popup('Yes')
        if list_error_message:
        # verify error
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            print(f"Action delete '{master_account_number}' failed!")
        else:
        # verify success
            self.check_notification('Deleted successfully')
            self.wait_loading()
            self.trade_account_linkage_simple_search(str(master_account_number).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {master_account_number}')
            return master_account_number

# -------------------------- handle BO approval - TRADE --------------------------
    # TRD-Catalogue Definition - Data Verification
    def trade_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, business_group=None, details_category=None, term_and_condition=None, tenor=None, customer_type=None, catalogue_status=None, user_create=None, approve_by=None, obs_percentage_rate=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if business_group:
            self.bo_assert_select('Business group', business_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if term_and_condition:
            self.bo_assert_select('Term and condition', term_and_condition)
        if tenor:
            self.bo_assert_select('Tenor', tenor)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if user_create:
            self.bo_assert_text('User create', user_create)
        if approve_by:
            self.bo_assert_text('Approve by', approve_by)
        if obs_percentage_rate:
            self.bo_assert_value('OBS percentage/rate', obs_percentage_rate)
        self.bo_click_tab('IFC information ')
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
        self.bo_click_tab('GLs information ')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')

    def trade_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, business_group=None, details_category=None, term_and_condition=None, tenor=None, customer_type=None, catalogue_status=None, user_create=None, approve_by=None, obs_percentage_rate=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if business_group:
            self.bo_assert_select('Business group', business_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if term_and_condition:
            self.bo_assert_select('Term and condition', term_and_condition)
        if tenor:
            self.bo_assert_select('Tenor', tenor)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if user_create:
            self.bo_assert_text_group('User create', user_create)
        if approve_by:
            self.bo_assert_text_group('Approve by', approve_by)
        if obs_percentage_rate:
            self.bo_assert_value('OBS percentage/rate', obs_percentage_rate)
        self.bo_click_tab('IFC information ')
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
        self.bo_click_tab('GLs information ')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')

    def trade_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, business_group=None, category=None, term=None, customer_type=None, creator=None, status=None, obs_percentage_rate=None):
        # search and verify
        self.trade_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalog Code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalog name', 1, catalogue_name)
        if business_group:
            self.assert_table_data('Business group', 1, business_group)
        if category:
            self.assert_table_data('Category', 1, category)
        if term:
            self.assert_table_data('Term', 1, term)
        if customer_type:
            self.assert_table_data('Customer type', 1, customer_type)
        if creator:
            self.assert_table_data('Creator', 1, creator)
        if status:
            self.assert_table_data('Status', 1, status)
        if obs_percentage_rate:
            self.assert_table_data('OBS percentage/rate', 1, obs_percentage_rate)

    # TRD-IFC Item Definition - Data Verification
    def trade_ifc_item_definition_add_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-IFC Item Definition-Add'
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

    def trade_ifc_item_definition_update_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-IFC Item Definition-View'
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

    def trade_ifc_item_definition_search_verify(self, ifc_code, ifc_name=None, value_type=None, ifc_type=None, value=None, tenor=None, tenor_unit=None, active_condition=None, status=None):
        # search and verify
        self.trade_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
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

    def trade_get_ifc_code(self, ifc_name):
        self.trade_ifc_item_definition_simple_search(ifc_name)
        self.assert_table_data('IFC name', 1, ifc_name)
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-IFC Item Definition-View')
        self.bo_click_tab('General information')
        ifc_code_out=self.bo_get_value('IFC code')
        print(f'IFC code: {ifc_code_out}')
        return ifc_code_out

    # TRD-IFC Auto Fee - Data Verification
    def trade_ifc_auto_fee_add_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-IFC Auto Fee-Add'
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

    def trade_ifc_auto_fee_update_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-IFC Auto Fee-View'
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

    def trade_ifc_auto_fee_search_verify(self, transaction_code, ifc_code, transaction_name=None, ifc_name=None):
        # search
        self.trade_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        # verify value
        self.assert_table_data('Transaction code', 1, transaction_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        if transaction_name:
            self.assert_table_data('Transaction name', 1, transaction_name)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)

