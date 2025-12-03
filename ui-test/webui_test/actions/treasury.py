from webui_test.case import *

class TreasuryActions(TestCase):

# -------------------------- handle FO - TREASURY - MONEY MARKET --------------------------
    # TMM_OPN: MM - Open account
    def tmm_opn(self, counterparty_type=None, counterparty_code=None, catalogue_code=None, account_name=None, trade_platform=None, deal_ticket_number=None, currency_code=None, value_date=None, trade_date=None, tenor=None, on_value_date_settlement_by=None, on_value_date_account_no_dpt=None, on_value_date_account_no_act=None, on_maturity_settlement_by=None, on_maturity_account_no_dpt=None, on_maturity_account_no_act=None, other_settlement=None, description=None, account_number=None, trade_type=None, tenor_unit=None, settle_tenor=None, settle_tenor_unit=None, maturity_date=None, on_value_date_currency=None, on_value_date_account_name=None, on_maturity_currency=None, on_maturity_account_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_OPN', 'Open')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Open account')
        # enter value
        self.key_escape()
        if counterparty_type:
            self.fo_select('Counterparty type', counterparty_type)
        if counterparty_code:
            self.fo_write_group('Counterparty code', str(counterparty_code).replace('-', ''))
            self.wait_loading()
        if catalogue_code:
            self.lookup_data('Catalogue code', 'Code', catalogue_code)
        if account_name:
            self.fo_write_text('Account name', account_name)
        self.key_escape()
        if trade_platform:
            self.fo_select('Trade platform', trade_platform)
        if deal_ticket_number:
            self.fo_write_text('Deal ticket number', deal_ticket_number)
        self.key_escape()
        if currency_code:
            self.fo_select('Currency code', currency_code)
        if value_date:
            self.fo_write_date('Value date', value_date)
        if trade_date:
            self.fo_write_date('Trade date', trade_date)
        if tenor:
            self.fo_write_number_group('Tenor', tenor)
        self.key_escape()
        if on_value_date_settlement_by:
            self.fo_select_border('On value date', 'Settlement by', on_value_date_settlement_by)
        if on_value_date_account_no_dpt:
            self.fo_write_border('On value date', 'Account no.', str(on_value_date_account_no_dpt).replace('-', ''))
            self.wait_loading()
        if on_value_date_account_no_act:
            self.fo_write_border('On value date', 'Account no.', str(on_value_date_account_no_act).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if on_maturity_settlement_by:
            self.fo_select_border('On maturity', 'Settlement by', on_maturity_settlement_by)
        if on_maturity_account_no_dpt:
            self.fo_write_border('On maturity', 'Account no.', str(on_maturity_account_no_dpt).replace('-', ''))
            self.wait_loading()
        if on_maturity_account_no_act:
            self.fo_write_border('On maturity', 'Account no.', str(on_maturity_account_no_act).replace('-', ''))
            self.wait_loading()
        if other_settlement:
            self.fo_write_text('Other settlement', other_settlement)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if trade_type:
            self.fo_assert_select('Trade type', trade_type)
        if tenor_unit:
            self.fo_assert_value_data('Tenor unit', tenor_unit)
        if settle_tenor:
            self.fo_assert_value_group('Settle tenor', settle_tenor)
        if settle_tenor_unit:
            self.fo_assert_value_data('Settle tenor unit', settle_tenor_unit)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if on_value_date_currency:
            self.fo_assert_value_border('On value date', 'Currency', on_value_date_currency)
        if on_value_date_account_name:
            self.fo_assert_text_border('On value date', 'Account name', on_value_date_account_name)
        if on_maturity_currency:
            self.fo_assert_value_border('On maturity', 'Currency', on_maturity_currency)
        if on_maturity_account_name:
            self.fo_assert_text_border('On maturity', 'Account name', on_maturity_account_name)
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
            print(f'Transaction references TMM_OPN: {transaction_references}')
            account_number_out=self.fo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def tmm_opn_view(self, transaction_references, counterparty_type=None, counterparty_code=None, catalogue_code=None, account_name=None, trade_platform=None, deal_ticket_number=None, currency_code=None, value_date=None, trade_date=None, tenor=None, on_value_date_settlement_by=None, on_value_date_account_no_dpt=None, on_value_date_account_no_act=None, on_maturity_settlement_by=None, on_maturity_account_no_dpt=None, on_maturity_account_no_act=None, other_settlement=None, description=None, account_number=None, trade_type=None, tenor_unit=None, settle_tenor=None, settle_tenor_unit=None, maturity_date=None, on_value_date_currency=None, on_value_date_account_name=None, on_maturity_currency=None, on_maturity_account_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'MM - Open account')
        # compare value
        if counterparty_type:
            self.fo_assert_select('Counterparty type', counterparty_type)
        if counterparty_code:
            self.fo_assert_value_group('Counterparty code', self.customer_code_mask(counterparty_code))
        if catalogue_code:
            self.fo_assert_text_group('Catalogue code', catalogue_code)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if trade_platform:
            self.fo_assert_select('Trade platform', trade_platform)
        if deal_ticket_number:
            self.fo_assert_text('Deal ticket number', deal_ticket_number)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if trade_date:
            self.fo_assert_date('Trade date', trade_date)
        if tenor:
            self.fo_assert_value_group('Tenor', tenor)
        if on_value_date_settlement_by:
            self.fo_assert_value_border('On value date', 'Settlement by', on_value_date_settlement_by)
        if on_value_date_account_no_dpt:
            self.fo_assert_value_border('On value date', 'Account no.', self.deposit_account_number_mask(on_value_date_account_no_dpt))
        if on_value_date_account_no_act:
            self.fo_assert_value_border('On value date', 'Account no.', self.gl_account_number_mask(on_value_date_account_no_act))
        if on_maturity_settlement_by:
            self.fo_assert_value_border('On maturity', 'Settlement by', on_maturity_settlement_by)
        if on_maturity_account_no_dpt:
            self.fo_assert_value_border('On maturity', 'Account no.', self.deposit_account_number_mask(on_maturity_account_no_dpt))
        if on_maturity_account_no_act:
            self.fo_assert_value_border('On maturity', 'Account no.', self.gl_account_number_mask(on_maturity_account_no_act))
        if other_settlement:
            self.fo_assert_text('Other settlement', other_settlement)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if trade_type:
            self.fo_assert_select('Trade type', trade_type)
        if tenor_unit:
            self.fo_assert_value_data('Tenor unit', tenor_unit)
        if settle_tenor:
            self.fo_assert_value_group('Settle tenor', settle_tenor)
        if settle_tenor_unit:
            self.fo_assert_value_data('Settle tenor unit', settle_tenor_unit)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if on_value_date_currency:
            self.fo_assert_value_border('On value date', 'Currency', on_value_date_currency)
        if on_value_date_account_name:
            self.fo_assert_text_border('On value date', 'Account name', on_value_date_account_name)
        if on_maturity_currency:
            self.fo_assert_value_border('On maturity', 'Currency', on_maturity_currency)
        if on_maturity_account_name:
            self.fo_assert_text_border('On maturity', 'Account name', on_maturity_account_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references TMM_OPN: {transaction_references}')
        account_number_out=self.fo_get_value('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # TMM_AAI: MM - Amendment account information
    def tmm_aai(self, account_number=None, tenor=None, on_value_date_settlement_by=None, on_value_date_account_no_dpt=None, on_value_date_account_no_act=None, on_maturity_settlement_by=None, on_maturity_account_no_dpt=None, on_maturity_account_no_act=None, other_settlement=None, description=None, account_name=None, counterparty_type=None, counterparty_mm_limit_bcy=None, counterparty_code=None, catalogue_code=None, trade_type=None, currency_code=None, trade_platform=None, value_date=None, deal_ticket_number=None, tenor_unit=None, trade_date=None, maturity_date=None, settle_tenor=None, settle_tenor_unit=None, on_value_date_currency=None, on_value_date_account_name=None, on_maturity_currency=None, on_maturity_account_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_AAI', 'Amendment')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Amendment account information')
        # enter value
        if account_number:
            self.fo_write('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if tenor:
            self.fo_write_number_group('Tenor', tenor)
        self.key_escape()
        if on_value_date_settlement_by:
            self.fo_select_border('On value date', 'Settlement by', on_value_date_settlement_by)
        if on_value_date_account_no_dpt:
            self.fo_write_border('On value date', 'Account no.', str(on_value_date_account_no_dpt).replace('-', ''))
            self.wait_loading()
        if on_value_date_account_no_act:
            self.fo_write_border('On value date', 'Account no.', str(on_value_date_account_no_act).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if on_maturity_settlement_by:
            self.fo_select_border('On maturity', 'Settlement by', on_maturity_settlement_by)
        if on_maturity_account_no_dpt:
            self.fo_write_border('On maturity', 'Account no.', str(on_maturity_account_no_dpt).replace('-', ''))
            self.wait_loading()
        if on_maturity_account_no_act:
            self.fo_write_border('On maturity', 'Account no.', str(on_maturity_account_no_act).replace('-', ''))
            self.wait_loading()
        if other_settlement:
            self.fo_write_text('Other settlement', other_settlement)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if counterparty_type:
            self.fo_assert_select('Counterparty type', counterparty_type)
        if counterparty_mm_limit_bcy:
            self.fo_assert_value('Counterparty MM limit (BCY)', counterparty_mm_limit_bcy)
        if counterparty_code:
            self.fo_assert_value_group('Counterparty code', self.customer_code_mask(counterparty_code))
        if catalogue_code:
            self.fo_assert_text_group('Catalogue code', catalogue_code)
        if trade_type:
            self.fo_assert_select('Trade type', trade_type)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if trade_platform:
            self.fo_assert_select('Trade platform', trade_platform)
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if deal_ticket_number:
            self.fo_assert_text('Deal ticket number', deal_ticket_number)
        if tenor_unit:
            self.fo_assert_value_data('Tenor unit', tenor_unit)
        if trade_date:
            self.fo_assert_date('Trade date', trade_date)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if settle_tenor:
            self.fo_assert_value_group('Settle tenor', settle_tenor)
        if settle_tenor_unit:
            self.fo_assert_value_data('Settle tenor unit', settle_tenor_unit)
        if on_value_date_currency:
            self.fo_assert_value_border('On value date', 'Currency', on_value_date_currency)
        if on_value_date_account_name:
            self.fo_assert_text_border('On value date', 'Account name', on_value_date_account_name)
        if on_maturity_currency:
            self.fo_assert_value_border('On maturity', 'Currency', on_maturity_currency)
        if on_maturity_account_name:
            self.fo_assert_text_border('On maturity', 'Account name', on_maturity_account_name)
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
            print(f'Transaction references TMM_AAI: {transaction_references}')
            account_number_out=self.fo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def tmm_aai_view(self, transaction_references, account_number=None, tenor=None, on_value_date_settlement_by=None, on_value_date_account_no_dpt=None, on_value_date_account_no_act=None, on_maturity_settlement_by=None, on_maturity_account_no_dpt=None, on_maturity_account_no_act=None, other_settlement=None, description=None, account_name=None, counterparty_type=None, counterparty_mm_limit_bcy=None, counterparty_code=None, catalogue_code=None, trade_type=None, currency_code=None, trade_platform=None, value_date=None, deal_ticket_number=None, tenor_unit=None, trade_date=None, maturity_date=None, settle_tenor=None, settle_tenor_unit=None, on_value_date_currency=None, on_value_date_account_name=None, on_maturity_currency=None, on_maturity_account_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'MM - Amendment account information')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if tenor:
            self.fo_assert_value_group('Tenor', tenor)
        if on_value_date_settlement_by:
            self.fo_assert_value_border('On value date', 'Settlement by', on_value_date_settlement_by)
        if on_value_date_account_no_dpt:
            self.fo_assert_value_border('On value date', 'Account no.', self.deposit_account_number_mask(on_value_date_account_no_dpt))
        if on_value_date_account_no_act:
            self.fo_assert_value_border('On value date', 'Account no.', self.gl_account_number_mask(on_value_date_account_no_act))
        if on_maturity_settlement_by:
            self.fo_assert_value_border('On maturity', 'Settlement by', on_maturity_settlement_by)
        if on_maturity_account_no_dpt:
            self.fo_assert_value_border('On maturity', 'Account no.', self.deposit_account_number_mask(on_maturity_account_no_dpt))
        if on_maturity_account_no_act:
            self.fo_assert_value_border('On maturity', 'Account no.', self.gl_account_number_mask(on_maturity_account_no_act))
        if other_settlement:
            self.fo_assert_text('Other settlement', other_settlement)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if counterparty_type:
            self.fo_assert_select('Counterparty type', counterparty_type)
        if counterparty_mm_limit_bcy:
            self.fo_assert_value('Counterparty MM limit (BCY)', counterparty_mm_limit_bcy)
        if counterparty_code:
            self.fo_assert_value_group('Counterparty code', self.customer_code_mask(counterparty_code))
        if catalogue_code:
            self.fo_assert_text_group('Catalogue code', catalogue_code)
        if trade_type:
            self.fo_assert_select('Trade type', trade_type)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if trade_platform:
            self.fo_assert_select('Trade platform', trade_platform)
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if deal_ticket_number:
            self.fo_assert_text('Deal ticket number', deal_ticket_number)
        if tenor_unit:
            self.fo_assert_value_data('Tenor unit', tenor_unit)
        if trade_date:
            self.fo_assert_date('Trade date', trade_date)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if settle_tenor:
            self.fo_assert_value_group('Settle tenor', settle_tenor)
        if settle_tenor_unit:
            self.fo_assert_value_data('Settle tenor unit', settle_tenor_unit)
        if on_value_date_currency:
            self.fo_assert_value_border('On value date', 'Currency', on_value_date_currency)
        if on_value_date_account_name:
            self.fo_assert_text_border('On value date', 'Account name', on_value_date_account_name)
        if on_maturity_currency:
            self.fo_assert_value_border('On maturity', 'Currency', on_maturity_currency)
        if on_maturity_account_name:
            self.fo_assert_text_border('On maturity', 'Account name', on_maturity_account_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references TMM_AAI: {transaction_references}')
        account_number_out=self.fo_get_value('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # TMM_APP: MM - Approve MM account
    def tmm_app(self, account_number=None, description=None, counterparty_type=None, counterparty_code=None, catalogue_code=None, trade_type=None, account_name=None, deal_ticket_number=None, sequence_number=None, currency_code=None, trade_date=None, settle_tenor=None, settle_tenor_unit=None, value_date=None, trade_platform=None, tenor=None, tenor_unit=None, maturity_date=None, dealer_id=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_APP', 'Approve')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Approve MM account')
        # enter value
        if account_number:
            self.fo_write('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if counterparty_type:
            self.fo_assert_select('Counterparty type', counterparty_type)
        if counterparty_code:
            self.fo_assert_value_group('Counterparty code', self.customer_code_mask(counterparty_code))
        if catalogue_code:
            self.fo_assert_text_group('Catalogue code', catalogue_code)
        if trade_type:
            self.fo_assert_select('Trade type', trade_type)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if deal_ticket_number:
            self.fo_assert_text('Deal ticket number', deal_ticket_number)
        if sequence_number:
            self.fo_assert_value('Sequence number', sequence_number)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if trade_date:
            self.fo_assert_date('Trade date', trade_date)
        if settle_tenor:
            self.fo_assert_value_group('Settle tenor', settle_tenor)
        if settle_tenor_unit:
            self.fo_assert_value_data('Settle tenor unit', settle_tenor_unit)
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if trade_platform:
            self.fo_assert_select('Trade platform', trade_platform)
        if tenor:
            self.fo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.fo_assert_value_data('Tenor unit', tenor_unit)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if dealer_id:
            self.fo_assert_text('Dealer ID', dealer_id)
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
            print(f'Transaction references TMM_APP: {transaction_references}')
            account_number_out=self.fo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def tmm_app_view(self, transaction_references, account_number=None, description=None, counterparty_type=None, counterparty_code=None, catalogue_code=None, trade_type=None, account_name=None, deal_ticket_number=None, sequence_number=None, currency_code=None, trade_date=None, settle_tenor=None, settle_tenor_unit=None, value_date=None, trade_platform=None, tenor=None, tenor_unit=None, maturity_date=None, dealer_id=None, expected_posting=None):
        self.transaction_view(transaction_references, 'MM - Approve MM account')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if counterparty_type:
            self.fo_assert_select('Counterparty type', counterparty_type)
        if counterparty_code:
            self.fo_assert_value_group('Counterparty code', self.customer_code_mask(counterparty_code))
        if catalogue_code:
            self.fo_assert_text_group('Catalogue code', catalogue_code)
        if trade_type:
            self.fo_assert_select('Trade type', trade_type)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if deal_ticket_number:
            self.fo_assert_text('Deal ticket number', deal_ticket_number)
        if sequence_number:
            self.fo_assert_value('Sequence number', sequence_number)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if trade_date:
            self.fo_assert_date('Trade date', trade_date)
        if settle_tenor:
            self.fo_assert_value_group('Settle tenor', settle_tenor)
        if settle_tenor_unit:
            self.fo_assert_value_data('Settle tenor unit', settle_tenor_unit)
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if trade_platform:
            self.fo_assert_select('Trade platform', trade_platform)
        if tenor:
            self.fo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.fo_assert_value_data('Tenor unit', tenor_unit)
        if maturity_date:
            self.fo_assert_date('Maturity date', maturity_date)
        if dealer_id:
            self.fo_assert_text('Dealer ID', dealer_id)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references TMM_APP: {transaction_references}')
        account_number_out=self.fo_get_value('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # TMM_DEP: MM - Deposit to MM account
    def tmm_dep(self, account_number=None, amount=None, description=None, counterparty_type=None, counterparty_code=None, counterparty_mm_limit_bcy=None, category_code=None, trade_type=None, currency_code_01=None, account_name=None, settlement_by=None, currency_code_02=None, account_no=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_DEP', 'Deposit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Deposit to MM account')
        # enter value
        if account_number:
            self.fo_write('Account number', self.no_mask(account_number))
            self.wait_loading()
        if amount:
            self.fo_write_number('Amount', amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if counterparty_type:
            self.fo_assert_select('Counterparty type', counterparty_type)
        if counterparty_code:
            self.fo_assert_text_group('Counterparty code', self.no_mask(counterparty_code))
        if counterparty_mm_limit_bcy:
            self.fo_assert_value('Counterparty MM limit (BCY)', counterparty_mm_limit_bcy)
        if category_code:
            self.fo_assert_text_group('Category code', category_code)
        if trade_type:
            self.fo_assert_select('Trade type', trade_type)
        if currency_code_01:
            self.fo_assert_select('Currency code', currency_code_01)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if settlement_by:
            self.fo_assert_select('Settlement by', settlement_by)
        if currency_code_02:
            self.fo_assert_select('Currency code', currency_code_02)
        if account_no:
            self.fo_assert_text_group('Account No.', self.no_mask(account_no))
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
            print(f'Transaction references TMM_DEP: {transaction_references}')
            account_number_out=self.fo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def tmm_dep_view(self, transaction_references, account_number=None, amount=None, description=None, counterparty_type=None, counterparty_code=None, counterparty_mm_limit_bcy=None, category_code=None, trade_type=None, currency_code_01=None, account_name=None, settlement_by=None, currency_code_02=None, account_no=None, expected_posting=None):
        self.transaction_view(transaction_references, 'MM - Deposit to MM account')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if amount:
            self.fo_assert_value('Amount', amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if counterparty_type:
            self.fo_assert_select('Counterparty type', counterparty_type)
        if counterparty_code:
            self.fo_assert_text_group('Counterparty code', self.no_mask(counterparty_code))
        if counterparty_mm_limit_bcy:
            self.fo_assert_value('Counterparty MM limit (BCY)', counterparty_mm_limit_bcy)
        if category_code:
            self.fo_assert_text_group('Category code', category_code)
        if trade_type:
            self.fo_assert_select('Trade type', trade_type)
        if currency_code_01:
            self.fo_assert_select('Currency code', currency_code_01)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if settlement_by:
            self.fo_assert_select('Settlement by', settlement_by)
        if currency_code_02:
            self.fo_assert_select('Currency code', currency_code_02)
        if account_no:
            self.fo_assert_text_group('Account No.', self.no_mask(account_no))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references TMM_DEP: {transaction_references}')
        account_number_out=self.fo_get_value('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # TMM_PMA: MM - Placement to MM account
    def tmm_pma(self, account_number=None, amount=None, description=None, counterparty_type=None, counterparty_code=None, counterparty_mm_limit_bcy=None, category_code=None, trade_type=None, currency_code_01=None, account_name=None, credit_by=None, currency_code_02=None, account_no=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_PMA', 'Placement')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Placement to MM account')
        # enter value
        if account_number:
            self.fo_write('Account number', self.no_mask(account_number))
            self.wait_loading()
        if amount:
            self.fo_write_number('Amount', amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if counterparty_type:
            self.fo_assert_select('Counterparty type', counterparty_type)
        if counterparty_code:
            self.fo_assert_value_group('Counterparty code', self.customer_code_mask(counterparty_code))
        if counterparty_mm_limit_bcy:
            self.fo_assert_value('Counterparty MM limit (BCY)', counterparty_mm_limit_bcy)
        if category_code:
            self.fo_assert_text_group('Category code', category_code)
        if trade_type:
            self.fo_assert_select('Trade type', trade_type)
        if currency_code_01:
            self.fo_assert_select('Currency code', currency_code_01)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if credit_by:
            self.fo_assert_select('Credit by', credit_by)
        if currency_code_02:
            self.fo_assert_select('Currency code', currency_code_02)
        if account_no:
            self.fo_assert_text_group('Account No.', self.no_mask(account_no))
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
            print(f'Transaction references TMM_PMA: {transaction_references}')
            account_number_out=self.fo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def tmm_pma_view(self, transaction_references, account_number=None, amount=None, description=None, counterparty_type=None, counterparty_code=None, counterparty_mm_limit_bcy=None, category_code=None, trade_type=None, currency_code_01=None, account_name=None, credit_by=None, currency_code_02=None, account_no=None, expected_posting=None):
        self.transaction_view(transaction_references, 'MM - Placement to MM account')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if amount:
            self.fo_assert_value('Amount', amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if counterparty_type:
            self.fo_assert_select('Counterparty type', counterparty_type)
        if counterparty_code:
            self.fo_assert_value_group('Counterparty code', self.customer_code_mask(counterparty_code))
        if counterparty_mm_limit_bcy:
            self.fo_assert_value('Counterparty MM limit (BCY)', counterparty_mm_limit_bcy)
        if category_code:
            self.fo_assert_text_group('Category code', category_code)
        if trade_type:
            self.fo_assert_select('Trade type', trade_type)
        if currency_code_01:
            self.fo_assert_select('Currency code', currency_code_01)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if credit_by:
            self.fo_assert_select('Credit by', credit_by)
        if currency_code_02:
            self.fo_assert_select('Currency code', currency_code_02)
        if account_no:
            self.fo_assert_text_group('Account No.', self.no_mask(account_no))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references TMM_PMA: {transaction_references}')
        account_number_out=self.fo_get_value('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # TMM_IAD: MM - Interest adjustment
    def tmm_iad(self, account_number=None, ifc_code=None, adjust_interest_accrual=None, adjust_interest_due=None, description=None, accout_name=None, interest_payable=None, currency_code=None, interest_accrual=None, interest_due=None, new_interest_accrual=None, new_interest_due=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_IAD', 'adjustment')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Interest adjustment')
        # enter value
        if account_number:
            self.fo_write('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if ifc_code:
            self.fo_write_group('IFC code', ifc_code)
            self.wait_loading()
        if adjust_interest_accrual:
            self.fo_write_number('Adjust interest accrual', adjust_interest_accrual)
        if adjust_interest_due:
            self.fo_write_number('Adjust interest due', adjust_interest_due)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if accout_name:
            self.fo_assert_text('Accout name', accout_name)
        if interest_payable:
            self.fo_assert_value('Interest payable', interest_payable)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if new_interest_accrual:
            self.fo_assert_value('New interest accrual', new_interest_accrual)
        if new_interest_due:
            self.fo_assert_value('New interest due', new_interest_due)
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
            print(f'Transaction references TMM_IAD: {transaction_references}')
            account_number_out=self.fo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def tmm_iad_view(self, transaction_references, account_number=None, ifc_code=None, adjust_interest_accrual=None, adjust_interest_due=None, description=None, accout_name=None, interest_payable=None, currency_code=None, interest_accrual=None, interest_due=None, new_interest_accrual=None, new_interest_due=None, expected_posting=None):
        self.transaction_view(transaction_references, 'MM - Interest adjustment')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if ifc_code:
            self.fo_assert_value_group('IFC code', ifc_code)
        if adjust_interest_accrual:
            self.fo_assert_value('Adjust interest accrual', adjust_interest_accrual)
        if adjust_interest_due:
            self.fo_assert_value('Adjust interest due', adjust_interest_due)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if accout_name:
            self.fo_assert_text('Accout name', accout_name)
        if interest_payable:
            self.fo_assert_value('Interest payable', interest_payable)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if new_interest_accrual:
            self.fo_assert_value('New interest accrual', new_interest_accrual)
        if new_interest_due:
            self.fo_assert_value('New interest due', new_interest_due)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references TMM_IAD: {transaction_references}')
        account_number_out=self.fo_get_value('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # TMM_ICL: MM - Interest Collection
    def tmm_icl(self, account_number=None, debit_by=None, currency_code_debit=None, account_debit_dpt=None, account_debit_act=None, cross_rate=None, description=None, account_name=None, currency_code=None, interest_accrual=None, interest_payable=None, account_name_debit=None, interest_due=None, interest_amount_collection=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_ICL', 'collection')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Interest Collection')
        # enter value
        if account_number:
            self.fo_write('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if debit_by:
            self.fo_select_data('Debit by', debit_by)
        self.key_escape()
        if currency_code_debit:
            self.fo_select_data('Currency Code Debit', currency_code_debit)
        if account_debit_dpt:
            self.fo_write('Account Debit', str(account_debit_dpt).replace('-', ''))
            self.wait_loading()
        if account_debit_act:
            self.fo_write('Account Debit', str(account_debit_act).replace('-', ''))
            self.wait_loading()
        if cross_rate:
            self.fo_write_number('Cross rate', cross_rate)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if interest_payable:
            self.fo_assert_value('Interest payable', interest_payable)
        if account_name_debit:
            self.fo_assert_text('Account name debit', account_name_debit)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_amount_collection:
            self.fo_assert_value('Interest Amount Collection', interest_amount_collection)
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
            print(f'Transaction references TMM_ICL: {transaction_references}')
            account_number_out=self.fo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def tmm_icl_view(self, transaction_references, account_number=None, debit_by=None, currency_code_debit=None, account_debit_dpt=None, account_debit_act=None, cross_rate=None, description=None, account_name=None, currency_code=None, interest_accrual=None, interest_payable=None, account_name_debit=None, interest_due=None, interest_amount_collection=None, expected_posting=None):
        self.transaction_view(transaction_references, 'MM - Interest Collection')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if debit_by:
            self.fo_assert_value_data('Debit by', debit_by)
        if currency_code_debit:
            self.fo_assert_value_data('Currency Code Debit', currency_code_debit)
        if account_debit_dpt:
            self.fo_assert_value('Account Debit', self.deposit_account_number_mask(account_debit_dpt))
        if account_debit_act:
            self.fo_assert_value('Account Debit', self.gl_account_number_mask(account_debit_act))
        if cross_rate:
            self.fo_assert_value('Cross rate', cross_rate)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if interest_payable:
            self.fo_assert_value('Interest payable', interest_payable)
        if account_name_debit:
            self.fo_assert_text('Account name debit', account_name_debit)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_amount_collection:
            self.fo_assert_value('Interest Amount Collection', interest_amount_collection)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references TMM_ICL: {transaction_references}')
        account_number_out=self.fo_get_value('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # TMM_IRP: MM - Interest repayment
    def tmm_irp(self, account_number=None, credit_by=None, currency_code_credit=None, account_credit_dpt=None, account_credit_act=None, cross_rate=None, description=None, account_name=None, currency_code=None, interest_accrual=None, interest_payable=None, account_name_credit=None, interest_due=None, amount_rate=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_IRP', 'repayment')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Interest repayment')
        # enter value
        if account_number:
            self.fo_write('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        self.key_escape()
        if credit_by:
            self.fo_select_data('Credit by', credit_by)
        self.key_escape()
        if currency_code_credit:
            self.fo_select_data('Currency code credit', currency_code_credit)
        if account_credit_dpt:
            self.fo_write('Account credit', str(account_credit_dpt).replace('-', ''))
            self.wait_loading()
        if account_credit_act:
            self.fo_write('Account credit', str(account_credit_act).replace('-', ''))
            self.wait_loading()
        if cross_rate:
            self.fo_write_number('Cross rate', cross_rate)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if interest_payable:
            self.fo_assert_value('Interest payable', interest_payable)
        if account_name_credit:
            self.fo_assert_text('Account name credit', account_name_credit)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if amount_rate:
            self.fo_assert_value('Amount rate', amount_rate)
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
            print(f'Transaction references TMM_IRP: {transaction_references}')
            account_number_out=self.fo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def tmm_irp_view(self, transaction_references, account_number=None, credit_by=None, currency_code_credit=None, account_credit_dpt=None, account_credit_act=None, cross_rate=None, description=None, account_name=None, currency_code=None, interest_accrual=None, interest_payable=None, account_name_credit=None, interest_due=None, amount_rate=None, expected_posting=None):
        self.transaction_view(transaction_references, 'MM - Interest repayment')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if credit_by:
            self.fo_assert_value_data('Credit by', credit_by)
        if currency_code_credit:
            self.fo_assert_value_data('Currency code credit', currency_code_credit)
        if account_credit_dpt:
            self.fo_assert_value('Account credit', self.deposit_account_number_mask(account_credit_dpt))
        if account_credit_act:
            self.fo_assert_value('Account credit', self.gl_account_number_mask(account_credit_act))
        if cross_rate:
            self.fo_assert_value('Cross rate', cross_rate)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if interest_payable:
            self.fo_assert_value('Interest payable', interest_payable)
        if account_name_credit:
            self.fo_assert_text('Account name credit', account_name_credit)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if amount_rate:
            self.fo_assert_value('Amount rate', amount_rate)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references TMM_IRP: {transaction_references}')
        account_number_out=self.fo_get_value('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # TMM_HIS: MM - Transaction history
    def tmm_his(self, account_number=None, from_date=None, to_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_HIS', 'history')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Transaction history')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if from_date:
            self.fo_write_date('From date', from_date)
        if to_date:
            self.fo_write_date('To date', to_date)
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
            print(f'Transaction references TMM_HIS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    # TMM_WCD: MM - Withdraw and close MM Deposit account
    def tmm_wcd(self, account_number=None, description=None, account_name=None, debit_by=None, currency_code=None, account_no=None, interest_accrual=None, interest_due=None, interest_prepaid=None, principal_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_WCD', 'Withdraw and close MM Deposit account')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Withdraw and close MM Deposit account')
        # enter value
        if account_number:
            self.fo_write('Account number', self.no_mask(account_number))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if debit_by:
            self.fo_assert_select('Debit by', debit_by)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if account_no:
            self.fo_assert_text_group('Account No.', self.no_mask(account_no))
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_prepaid:
            self.fo_assert_value('Interest prepaid', interest_prepaid)
        if principal_amount:
            self.fo_assert_value('Principal amount', principal_amount)
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
            print(f'Transaction references TMM_WCD: {transaction_references}')
            account_number_out=self.fo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def tmm_wcd_view(self, transaction_references, account_number=None, description=None, account_name=None, debit_by=None, currency_code=None, account_no=None, interest_accrual=None, interest_due=None, interest_prepaid=None, principal_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'MM - Withdraw and close MM Deposit account')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if debit_by:
            self.fo_assert_select('Debit by', debit_by)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if account_no:
            self.fo_assert_text_group('Account No.', self.no_mask(account_no))
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if interest_prepaid:
            self.fo_assert_value('Interest prepaid', interest_prepaid)
        if principal_amount:
            self.fo_assert_value('Principal amount', principal_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references TMM_WCD: {transaction_references}')
        account_number_out=self.fo_get_value('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # TMM_WCP: MM - Withdraw and close MM Placement account
    def tmm_wcp(self, account_number=None, description=None, account_name=None, debit_by=None, currency_code=None, account_no=None, interest_accrual=None, interest_payable=None, interest_due=None, principal_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TMM_WCP', 'Withdraw and close MM Placement account')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MM - Withdraw and close MM Placement account')
        # enter value
        if account_number:
            self.fo_write('Account number', self.no_mask(account_number))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if debit_by:
            self.fo_assert_select('Debit by', debit_by)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if account_no:
            self.fo_assert_text_group('Account No.', self.no_mask(account_no))
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if interest_payable:
            self.fo_assert_value('Interest payable', interest_payable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if principal_amount:
            self.fo_assert_value('Principal amount', principal_amount)
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
            print(f'Transaction references TMM_WCP: {transaction_references}')
            account_number_out=self.fo_get_value('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def tmm_wcp_view(self, transaction_references, account_number=None, description=None, account_name=None, debit_by=None, currency_code=None, account_no=None, interest_accrual=None, interest_payable=None, interest_due=None, principal_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'MM - Withdraw and close MM Placement account')
        # compare value
        if account_number:
            self.fo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if debit_by:
            self.fo_assert_select('Debit by', debit_by)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if account_no:
            self.fo_assert_text_group('Account No.', self.no_mask(account_no))
        if interest_accrual:
            self.fo_assert_value('Interest accrual', interest_accrual)
        if interest_payable:
            self.fo_assert_value('Interest payable', interest_payable)
        if interest_due:
            self.fo_assert_value('Interest due', interest_due)
        if principal_amount:
            self.fo_assert_value('Principal amount', principal_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references TMM_WCP: {transaction_references}')
        account_number_out=self.fo_get_value('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

# -------------------------- handle FO - TREASURY - FOREX --------------------------
    # TFX_OFO: FX - Outright (Spot, Forward)
    def tfx_ofo(self, counterparty_code, catalogue_code, contract_rate, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TFX_OFO', 'Outright')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FX - Outright (Spot, Forward)')
        # enter value
        self.lookup_data('Counterparty code', 'Code', str(counterparty_code).replace('-', ''))
        self.lookup_data('Catalogue code', 'Code', catalogue_code, "N")
        if self.fo_get_select('Trade type')=='Buy':
            if debit_currency:
                self.fo_select('Debit currency', debit_currency)
            if credit_currency:
                self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if self.fo_get_select('Trade type')=='Sell':
            if credit_currency:
                self.fo_select('Credit currency', credit_currency)
            if debit_currency:
                self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        self.fo_write_number('Contract rate', contract_rate)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        # Debit info
        if debit_by:
            self.select('Debit by', debit_by)
        if self.fo_get_select('Trade type')=='Buy':
            if debit_amount:
                self.fo_write_number_border('Debit', 'Amount', debit_amount)
            if credit_amount:
                self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if debit_account_no_dpt:
            self.fo_write_border('Debit', 'Account No. DPT', debit_account_no_dpt)
        if debit_account_no_act:
            self.fo_write_border('Debit', 'Account No. ACT', debit_account_no_act)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # Credit info
        if credit_by:
            self.select('Credit by', credit_by)
        if self.fo_get_select('Trade type')=='Sell':
            if credit_amount:
                self.fo_write_number_border('Credit', 'Amount', credit_amount)
            if debit_amount:
                self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if credit_account_no_dpt:
            self.fo_write_border('Credit', 'Account No. DPT', credit_account_no_dpt)
        if credit_account_no_act:
            self.fo_write_border('Credit', 'Account No. ACT', credit_account_no_act)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
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
            print(f'Transaction references TFX_OFO: {transaction_references}')
            forex_account_mask=self.fo_get_value('Account number')
            print(f'Account number: {forex_account_mask}')
            return transaction_references, forex_account_mask

    def tfx_ofo_view(self, transaction_references, account_number=None, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FX - Outright (Spot, Forward)')
        # compare value
        if account_number:
            self.assertEqual(self.fo_get_value('Account number'), self.treasury_account_number_mask(account_number))
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)

    # TFX_FAC: FX - Approve for FX Outright
    def tfx_fac(self, account_number, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TFX_FAC', 'Approve')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FX - Approve for FX Outright')
        # enter value
        self.fo_write('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
        self.wait_loading()
        # compare value
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
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
            print(f'Transaction references TFX_FAC: {transaction_references}')
            forex_account_mask=self.fo_get_value('Account number')
            print(f'Account number: {forex_account_mask}')
            return transaction_references, forex_account_mask

    def tfx_fac_view(self, transaction_references, account_number=None, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FX - Approve for FX Outright')
        # compare value
        if account_number:
            self.assertEqual(self.fo_get_value('Account number'), self.treasury_account_number_mask(account_number))
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)

    # TFX_OAA: FX - Outright Account Amendment
    def tfx_oaa(self, account_number, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, contract_rate_update=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, swap_point_update=None, debit_currency=None, credit_currency=None, debit_by=None, debit_by_update=None, debit_amount=None, debit_amount_update=None, debit_account_no_dpt=None, debit_account_no_dpt_update=None, debit_account_no_act=None, debit_account_no_act_update=None, debit_account_name=None, debit_account_name_update=None, credit_by=None, credit_by_update=None, credit_amount=None, credit_amount_update=None, credit_account_no_dpt=None, credit_account_no_dpt_update=None, credit_account_no_act=None, credit_account_no_act_update=None, credit_account_name=None, credit_account_name_update=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TFX_OAA', 'Amendment')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FX - Outright Account Amendment')
        # enter value
        self.fo_write('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        # compare value
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        # enter value modify
        if contract_rate_update:
            self.fo_write_number('Contract rate', contract_rate_update)
        if swap_point_update:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point_update)
        # modify debit info
        if debit_by_update:
            self.select('Debit by', debit_by_update)
        if self.fo_get_select('Trade type')=='Buy':
            if debit_amount_update:
                self.fo_write_number_border('Debit', 'Amount', debit_amount_update)
            if credit_amount_update:
                self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount_update)
        if debit_account_no_dpt_update:
            self.fo_write_border('Debit', 'Account No. DPT', debit_account_no_dpt_update)
        if debit_account_no_act_update:
            self.fo_write_border('Debit', 'Account No. ACT', debit_account_no_act_update)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_account_name_update:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name_update)
        # modify credit info
        if credit_by_update:
            self.select('Credit by', credit_by_update)
        if self.fo_get_select('Trade type')=='Sell':
            if credit_amount_update:
                self.fo_write_number_border('Credit', 'Amount', credit_amount_update)
            if debit_amount_update:
                self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount_update)
        if credit_account_no_dpt_update:
            self.fo_write_border('Credit', 'Account No. DPT', credit_account_no_dpt_update)
        if credit_account_no_act_update:
            self.fo_write_border('Credit', 'Account No. ACT', credit_account_no_act_update)
        if credit_currency:
            self.key_escape()
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_account_name_update:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name_update)
        self.wait_loading()
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
            print(f'Transaction references TFX_OAA: {transaction_references}')
            forex_account_mask=self.fo_get_value('Account number')
            print(f'Account number: {forex_account_mask}')
            return transaction_references, forex_account_mask

    def tfx_oaa_view(self, transaction_references, account_number=None, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FX - Outright Account Amendment')
        # compare value
        if account_number:
            self.assertEqual(self.fo_get_value('Account number'), self.treasury_account_number_mask(account_number))
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)

    # TFX_FCA: FX - Cancel Account
    def tfx_fca(self, account_number, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('TFX_FCA', 'Cancel')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FX - Cancel Account')
        # enter value
        self.fo_write('Account number', str(account_number).replace('-', ''))
        self.wait_loading()
        self.fo_write_text('Description', 'AUTO TEST')
        self.wait_loading()
        # compare value
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        if ifc_codes:
            self.add_fees(ifc_codes, values, total_fee)
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
            print(f'Transaction references TFX_FCA: {transaction_references}')
            forex_account_mask=self.fo_get_value('Account number')
            print(f'Account number: {forex_account_mask}')
            return transaction_references, forex_account_mask

    def tfx_fca_view(self, transaction_references, account_number=None, counterparty_code=None, catalogue_code=None, trade_type=None, contract_rate=None, account_name=None, value_date=None, reference_rate=None, swap_point=None, debit_currency=None, credit_currency=None, debit_by=None, debit_amount=None, debit_account_no_dpt=None, debit_account_no_act=None, debit_account_name=None, credit_by=None, credit_amount=None, credit_account_no_dpt=None, credit_account_no_act=None, credit_account_name=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FX - Cancel Account')
        # compare value
        if account_number:
            self.assertEqual(self.fo_get_value('Account number'), self.treasury_account_number_mask(account_number))
        if counterparty_code:
            self.assertEqual(self.fo_get_value_group('Counterparty code'), counterparty_code)
        if catalogue_code:
            self.assertEqual(self.fo_get_text_group('Catalogue code'), catalogue_code)
        if trade_type:
            self.assertEqual(self.fo_get_select('Trade type'), trade_type)
        if value_date:
            self.assertEqual(self.fo_get_date('Value date'), value_date)
        if account_name:
            self.assertEqual(self.fo_get_text('Account name'), account_name)
        if debit_currency:
            self.assertEqual(self.fo_get_select('Debit currency'), debit_currency)
        if credit_currency:
            self.assertEqual(self.fo_get_select('Credit currency'), credit_currency)
        if reference_rate:
            self.assertEqual(self.fo_get_value('Reference rate'), reference_rate)
        if swap_point:
            self.assertEqual(self.fo_get_value('Swap point'), swap_point)
        if contract_rate:
            self.assertEqual(self.fo_get_value('Contract rate'), contract_rate)
        # compare debit info
        if debit_by:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Debit by'), debit_by)
        if debit_currency:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Currency'), debit_currency)
        if debit_amount:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Amount'), debit_amount)
        if debit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. DPT'), debit_account_no_dpt)
        if debit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Debit', 'Account No. ACT'), debit_account_no_act)
        if debit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Debit', 'Account name'), debit_account_name)
        # compare credit info
        if credit_by:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Credit by'), credit_by)
        if credit_currency:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Currency'), credit_currency)
        if credit_amount:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Amount'), credit_amount)
        if credit_account_no_dpt:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. DPT'), credit_account_no_dpt)
        if credit_account_no_act:
            self.assertEqual(self.get_text_input_below_border('Credit', 'Account No. ACT'), credit_account_no_act)
        if credit_account_name:
            self.assertEqual(self.get_text_textarea_below_border('Credit', 'Account name'), credit_account_name)
        if expected_posting:
            self.assert_posting_data(**expected_posting)

# -------------------------- handle BO - TREASURY --------------------------
    # TRS-IFC Item Definition
    def treasury_ifc_item_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Treasury', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-IFC Item Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def treasury_ifc_item_definition_advanced_search(self, ifc_code_from=None, ifc_code_to=None, ifc_name=None, value_type=None, ifc_type=None, value_from=None, value_to=None, tenor_from=None, tenor_to=None, tenor_unit=None, active_condition=None, status=None):
        self.close_all_form()
        self.click_menu('Treasury', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-IFC Item Definition-Search')
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

    def treasury_ifc_item_definition_add(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, charge_on=None, sys_account_names=None, account_aliass=None, list_transaction=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Treasury', 'IFC', 'IFC Item Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('TRS-IFC Item Definition-Add')
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

    def treasury_ifc_item_definition_view(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, charge_on=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # search
        self.treasury_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRS-IFC Item Definition-View')
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

    def treasury_ifc_item_definition_update(self, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, charge_on=None, list_transaction=None, list_error_message=None):
        # view
        self.treasury_ifc_item_definition_view(ifc_code=ifc_code)
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

    def treasury_ifc_item_definition_delete(self, ifc_code, list_error_message=None, expected_message=None):
        # search
        self.treasury_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
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

    # TRS-IFC Auto Fee
    def treasury_ifc_auto_fee_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Treasury', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-IFC Auto Fee-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def treasury_ifc_auto_fee_advanced_search(self, transaction_code=None, transaction_name=None, ifc_code=None, ifc_name=None):
        self.close_all_form()
        self.click_menu('Treasury', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-IFC Auto Fee-Search')
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

    def treasury_ifc_auto_fee_add(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Treasury', 'IFC', 'IFC Auto Fee')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('TRS-IFC Auto Fee-Add')
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

    def treasury_ifc_auto_fee_view(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # search
        self.treasury_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        if transaction_code:
            self.assert_table_data('Transaction code', 1, transaction_code)
        if ifc_code:
            self.assert_table_data('IFC code', 1, ifc_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRS-IFC Auto Fee-View')
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

    def treasury_ifc_auto_fee_update(self, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # view
        self.treasury_ifc_auto_fee_view(transaction_code=transaction_code, ifc_code=ifc_code)
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

    def treasury_ifc_auto_fee_delete(self, transaction_code, ifc_code, list_error_message=None, expected_message=None):
        # search
        self.treasury_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
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

    # TRS-Catalogue Definition
    def treasury_catalogue_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Treasury', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-Catalogue Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def treasury_catalogue_definition_advanced_search(self, catalogue_code=None, catalogue_name=None, trade_group=None, details_category=None, trade_type=None, margin_trading=None, market=None, catalogue_status=None, settle_tenor=None, settle_tenor_unit=None, tenor=None, tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, rollover_option=None, revaluation=None, user_create=None, approve_by=None):
        self.close_all_form()
        self.click_menu('Treasury', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-Catalogue Definition-Search')
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.adv_search_text('Catalogue name', catalogue_name)
        self.key_escape()
        if trade_group:
            self.adv_search_select('Trade Group', trade_group)
        self.key_escape()
        if details_category:
            self.adv_search_select('Details category', details_category)
        self.key_escape()
        if trade_type:
            self.adv_search_select('Trade Type', trade_type)
        self.key_escape()
        if margin_trading:
            self.adv_search_select('Margin Trading', margin_trading)
        self.key_escape()
        if market:
            self.adv_search_select('Market', market)
        self.key_escape()
        if catalogue_status:
            self.adv_search_select('Catalogue status', catalogue_status)
        if settle_tenor:
            self.adv_search('Settle Tenor', settle_tenor)
        self.key_escape()
        if settle_tenor_unit:
            self.adv_search_select('Settle Tenor Unit', settle_tenor_unit)
        if tenor:
            self.adv_search('Tenor', tenor)
        self.key_escape()
        if tenor_unit:
            self.adv_search_select('Tenor Unit', tenor_unit)
        if interest_tenor:
            self.adv_search('Interest Tenor', interest_tenor)
        self.key_escape()
        if interest_tenor_unit:
            self.adv_search_select('Interest Tenor Unit', interest_tenor_unit)
        self.key_escape()
        if rollover_option:
            self.adv_search_select('Rollover Option', rollover_option)
        self.key_escape()
        if revaluation:
            self.adv_search_select('Revaluation', revaluation)
        if user_create:
            self.adv_search_text('User create', user_create)
        if approve_by:
            self.adv_search_text('Approve by', approve_by)
        self.click_button_search_advanced()
        self.wait_loading()

    def treasury_catalogue_definition_add(self, catalogue_code=None, catalogue_name=None, trade_group=None, details_category=None, trade_type=None, margin_trading=None, market=None, catalogue_status=None, settle_tenor=None, settle_tenor_unit=None, tenor=None, tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, rollover_option=None, revaluation=None, user_create=None, approve_by=None, ifc_codes=None, sys_account_names=None, account_aliass=None, coa_accounts=None, replace_bys=None, system_account_names=None, customer_sectors=None, customer_resident_statuss=None, business_lines=None, sub_products=None, bank_identifications=None, replace_code=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Treasury', 'Catalogue Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('TRS-Catalogue Definition-Add')
        # enter value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_write('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        self.key_escape()
        if trade_group:
            self.bo_select('Trade Group', trade_group)
        self.key_escape()
        if details_category:
            self.bo_select('Details category', details_category)
        self.key_escape()
        if trade_type:
            self.bo_select('Trade Type', trade_type)
        self.key_escape()
        if margin_trading:
            self.bo_select('Margin Trading', margin_trading)
        self.key_escape()
        if market:
            self.bo_select('Market', market)
        self.key_escape()
        if catalogue_status:
            self.bo_select('Catalogue status', catalogue_status)
        if settle_tenor:
            self.bo_write_number('Settle Tenor', settle_tenor)
        self.key_escape()
        if settle_tenor_unit:
            self.bo_select('Settle Tenor Unit', settle_tenor_unit)
        if tenor:
            self.bo_write_number('Tenor', tenor)
        self.key_escape()
        if tenor_unit:
            self.bo_select('Tenor Unit', tenor_unit)
        if interest_tenor:
            self.bo_write_number('Interest Tenor', interest_tenor)
        self.key_escape()
        if interest_tenor_unit:
            self.bo_select('Interest Tenor Unit', interest_tenor_unit)
        self.key_escape()
        if rollover_option:
            self.bo_select('Rollover Option', rollover_option)
        self.key_escape()
        if revaluation:
            self.bo_select('Revaluation', revaluation)
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

    def treasury_catalogue_definition_view(self, catalogue_code=None, catalogue_name=None, trade_group=None, details_category=None, trade_type=None, margin_trading=None, market=None, catalogue_status=None, settle_tenor=None, settle_tenor_unit=None, tenor=None, tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, rollover_option=None, revaluation=None, user_create=None, approve_by=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # search
        self.treasury_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalog Code', 1, catalogue_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRS-Catalogue Definition-View')
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if trade_group:
            self.bo_assert_select('Trade Group', trade_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if trade_type:
            self.bo_assert_select('Trade Type', trade_type)
        if margin_trading:
            self.bo_assert_select('Margin Trading', margin_trading)
        if market:
            self.bo_assert_select('Market', market)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if settle_tenor:
            self.bo_assert_value('Settle Tenor', settle_tenor)
        if settle_tenor_unit:
            self.bo_assert_select('Settle Tenor Unit', settle_tenor_unit)
        if tenor:
            self.bo_assert_value('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select('Tenor Unit', tenor_unit)
        if interest_tenor:
            self.bo_assert_value('Interest Tenor', interest_tenor)
        if interest_tenor_unit:
            self.bo_assert_select('Interest Tenor Unit', interest_tenor_unit)
        if rollover_option:
            self.bo_assert_select('Rollover Option', rollover_option)
        if revaluation:
            self.bo_assert_select('Revaluation', revaluation)
        if user_create:
            self.bo_assert_text_group('User create', user_create)
        if approve_by:
            self.bo_assert_text_group('Approve by', approve_by)
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

    def treasury_catalogue_definition_update(self, catalogue_code=None, catalogue_name=None, trade_group=None, details_category=None, trade_type=None, margin_trading=None, market=None, catalogue_status=None, settle_tenor=None, settle_tenor_unit=None, tenor=None, tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, rollover_option=None, revaluation=None, user_create=None, approve_by=None, ifc_codes=None, sys_account_names=None, account_aliass=None, coa_accounts=None, replace_bys=None, system_account_names=None, customer_sectors=None, customer_resident_statuss=None, business_lines=None, sub_products=None, bank_identifications=None, replace_code=None, list_error_message=None):
        # view
        self.treasury_catalogue_definition_view(catalogue_code=catalogue_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        self.key_escape()
        if trade_group:
            self.bo_select('Trade Group', trade_group)
        self.key_escape()
        if details_category:
            self.bo_select('Details category', details_category)
        self.key_escape()
        if trade_type:
            self.bo_select('Trade Type', trade_type)
        self.key_escape()
        if margin_trading:
            self.bo_select('Margin Trading', margin_trading)
        self.key_escape()
        if market:
            self.bo_select('Market', market)
        self.key_escape()
        if catalogue_status:
            self.bo_select('Catalogue status', catalogue_status)
        if settle_tenor:
            self.bo_write_number('Settle Tenor', settle_tenor)
        self.key_escape()
        if settle_tenor_unit:
            self.bo_select('Settle Tenor Unit', settle_tenor_unit)
        if tenor:
            self.bo_write_number('Tenor', tenor)
        self.key_escape()
        if tenor_unit:
            self.bo_select('Tenor Unit', tenor_unit)
        if interest_tenor:
            self.bo_write_number('Interest Tenor', interest_tenor)
        self.key_escape()
        if interest_tenor_unit:
            self.bo_select('Interest Tenor Unit', interest_tenor_unit)
        self.key_escape()
        if rollover_option:
            self.bo_select('Rollover Option', rollover_option)
        self.key_escape()
        if revaluation:
            self.bo_select('Revaluation', revaluation)
        # assert value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_text('Catalogue code', catalogue_code)
        if user_create:
            self.bo_assert_text_group('User create', user_create)
        if approve_by:
            self.bo_assert_text_group('Approve by', approve_by)
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
            catalogue_code_out=self.bo_get_text('Catalogue code')
            print(f'Catalogue code: {catalogue_code_out}')
            return catalogue_code_out

    def treasury_catalogue_definition_delete(self, catalogue_code, list_error_message=None, expected_message=None):
        # search
        self.treasury_catalogue_definition_simple_search(catalogue_code)
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

    # TRS-Treasury account information
    def treasury_account_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Treasury', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-Account Information Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def treasury_account_advanced_search(self, account_number=None, catalogue_code=None, branch_code=None, category=None, currency_code=None, account_status=None, account_name=None, dealer_code=None, counterparty_code=None):
        self.close_all_form()
        self.click_menu('Treasury', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('TRS-Account Information Search')
        if account_number:
            self.adv_search('Account number', str(account_number).replace('-', ''))
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        if branch_code:
            self.adv_search_text('Branch code', branch_code)
        if category:
            self.adv_search_text('Category', category)
        self.key_escape()
        if currency_code:
            self.adv_search_select('Currency code', currency_code)
        self.key_escape()
        if account_status:
            self.adv_search_select('Account status', account_status)
        if account_name:
            self.adv_search_text('Account name', account_name)
        if dealer_code:
            self.adv_search_text('Dealer code', dealer_code)
        if counterparty_code:
            self.adv_search('Counterparty code', str(counterparty_code).replace('-', ''))
        self.click_button_search_advanced()
        self.wait_loading()

    def treasury_account_view(self, account_number=None, account_name=None, counterparty_type=None, counterparty_code=None, branch_code=None, catalogue_code=None, currency_code=None, trade_group=None, details_category=None, trade_type=None, deal_ticket_number=None, account_status=None, margin_trading_y_n=None, margin_trading_rate=None, open_date=None, value_date=None, tenor=None, tenor_unit=None, settle_tenor=None, settle_tenor_unit=None, interest_payment_tenor=None, interest_payment_tenor_unit=None, from_date=None, to_date=None, last_transaction_date=None, close_date=None, rollover_option=None, rollover_to_catalogue=None, dealer=None, created_by=None, approved_by=None, account_manager_staff_code=None, amount=None, average_price=None, margin_amount=None, interest_accrual_amount=None, intpayable_receivebe=None, interest_due=None, interest_overdue=None, interest_suspense=None, interest_prepaid=None, interest_not_paid=None, interest_payment_method=None, interest_paid=None, settlement_by_on_value_date=None, currency_on_value_date=None, account_no_on_value_date=None, settlement_by_on_maturity=None, currency_on_maturity=None, account_no_on_maturity=None, trade_date=None, tenor_p1=None, tenor_unit_p1=None, value_date_p1=None, broker=None, debit_by=None, debit_account=None, debit_currency=None, debit_amount=None, reference_rate=None, swap_point=None, trade_rate=None, forward_rate=None, credit_by=None, credit_account=None, credit_currency=None, credit_amount=None, trade_date_p2=None, tenor_p2=None, tenor_unit_p2=None, value_date_p2=None, broker_p2=None, debit_by_p2=None, debit_account_p2=None, debit_currency_p2=None, debit_amount_p2=None, spot_rate_p2=None, swap_point_p2=None, trade_rate_p2=None, forward_rate_p2=None, credit_by_p2=None, credit_account_p2=None, credit_currency_p2=None, credit_amount_p2=None, other_reference=None, other_settlement_instruction=None, remark=None, user_define_field=None, expected_account_gl_names=None, expected_account_gl_numbers=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_base_values=None, expected_ifc_is_linkeds=None, expected_ifc_values=None, expected_ifc_margin_values=None, expected_ifc_statuses=None, expected_ifc_outstandings=None, expected_ifc_paids=None, expected_ifc_basic_balances=None, expected_ifc_codes=None, expected_ifc_gl_names=None, expected_ifc_gl_numbers=None):
        # search
        self.treasury_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.treasury_account_number_mask(account_number))
        if account_status:
            self.assert_table_data('Account status', 1, account_status)
        if catalogue_code:
            self.assert_table_data('Category code', 1, catalogue_code)
        if counterparty_code:
            self.assert_table_data('Counterparty code', 1, counterparty_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRS-Account Information-View')
        # verify value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if counterparty_type:
            self.bo_assert_select('Counterparty type', counterparty_type)
        if counterparty_code:
            self.bo_assert_value_group('Counterparty code', self.customer_code_mask(counterparty_code))
        if branch_code:
            self.bo_assert_text_group('Branch code', branch_code)
        if catalogue_code:
            self.bo_assert_text('Category code', catalogue_code)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if trade_group:
            self.bo_assert_select('Trade group', trade_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if trade_type:
            self.bo_assert_select('Trade type', trade_type)
        if deal_ticket_number:
            self.bo_assert_text('Deal ticket number', deal_ticket_number)
        if account_status:
            self.bo_assert_select('Account status', account_status)
        if margin_trading_y_n:
            self.bo_assert_select('Margin trading (Y/N)', margin_trading_y_n)
        if margin_trading_rate:
            self.bo_assert_value('Margin trading rate', margin_trading_rate)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if value_date:
            self.bo_assert_date('Value date', value_date)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor unit', tenor_unit)
        if settle_tenor:
            self.bo_assert_value_group('Settle tenor', settle_tenor)
        if settle_tenor_unit:
            self.bo_assert_select_group('Settle tenor unit', settle_tenor_unit)
        if interest_payment_tenor:
            self.bo_assert_value_group('Interest payment tenor', interest_payment_tenor)
        if interest_payment_tenor_unit:
            self.bo_assert_select_group('Interest payment tenor unit', interest_payment_tenor_unit)
        if from_date:
            self.bo_assert_date('From date', from_date)
        if to_date:
            self.bo_assert_date('To date', to_date)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if rollover_option:
            self.bo_assert_select('Rollover option', rollover_option)
        if rollover_to_catalogue:
            self.bo_assert_value_group('Rollover to catalogue', rollover_to_catalogue)
        if dealer:
            self.bo_assert_text('Dealer', dealer)
        if created_by:
            self.bo_assert_text('Created by', created_by)
        if approved_by:
            self.bo_assert_text('Approved by', approved_by)
        if account_manager_staff_code:
            self.bo_assert_text('Account manager staff code', account_manager_staff_code)
        self.bo_click_tab('Balance information')
        if amount:
            self.bo_assert_value('Amount', amount)
        if average_price:
            self.bo_assert_value('Average price', average_price)
        if margin_amount:
            self.bo_assert_value('Margin amount', margin_amount)
        if interest_accrual_amount:
            self.bo_assert_value('Interest accrual amount', interest_accrual_amount)
        if intpayable_receivebe:
            self.bo_assert_value('Int.payable/receivebe', intpayable_receivebe)
        if interest_due:
            self.bo_assert_value('Interest due', interest_due)
        if interest_overdue:
            self.bo_assert_value('Interest overdue', interest_overdue)
        if interest_suspense:
            self.bo_assert_value('Interest suspense', interest_suspense)
        if interest_prepaid:
            self.bo_assert_value('Interest prepaid', interest_prepaid)
        if interest_not_paid:
            self.bo_assert_value('Interest not paid', interest_not_paid)
        if interest_payment_method:
            self.bo_assert_select('Interest payment method', interest_payment_method)
        if interest_paid:
            self.bo_assert_value('Interest paid', interest_paid)
        self.bo_click_tab('Settlement information')
        if settlement_by_on_value_date:
            self.bo_click_collap('On value date')
            self.bo_assert_value_multi('On value date', 'Settlement by', settlement_by_on_value_date)
        if currency_on_value_date:
            self.bo_click_collap('On value date')
            self.bo_assert_value_multi('On value date', 'Currency', currency_on_value_date)
        if account_no_on_value_date:
            self.bo_click_collap('On value date')
            self.bo_assert_text_multi('On value date', 'Account No', self.no_mask(account_no_on_value_date))
        if settlement_by_on_maturity:
            self.bo_click_collap('On maturity')
            self.bo_assert_value_multi('On maturity', 'Settlement by', settlement_by_on_maturity)
        if currency_on_maturity:
            self.bo_click_collap('On maturity')
            self.bo_assert_value_multi('On maturity', 'Currency', currency_on_maturity)
        if account_no_on_maturity:
            self.bo_click_collap('On maturity')
            self.bo_assert_text_multi('On maturity', 'Account No', self.no_mask(account_no_on_maturity))
        if trade_date:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Trade date', trade_date)
        if tenor_p1:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Tenor', tenor_p1)
        if tenor_unit_p1:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Tenor unit', tenor_unit_p1)
        if value_date_p1:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Value date', value_date_p1)
        if broker:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Broker', broker)
        if debit_by:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Debit by', debit_by)
        if debit_account:
            self.bo_click_collap('Phase 1')
            self.bo_assert_text_multi('Phase 1', 'Debit account', self.no_mask(debit_account))
        if debit_currency:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Debit currency', debit_currency)
        if debit_amount:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Debit amount', debit_amount)
        if reference_rate:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Reference rate', reference_rate)
        if swap_point:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Swap point', swap_point)
        if trade_rate:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Trade rate', trade_rate)
        if forward_rate:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Forward rate', forward_rate)
        if credit_by:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Credit by', credit_by)
        if credit_account:
            self.bo_click_collap('Phase 1')
            self.bo_assert_text_multi('Phase 1', 'Credit account', self.no_mask(credit_account))
        if credit_currency:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Credit currency', credit_currency)
        if credit_amount:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Credit amount', credit_amount)
        if trade_date_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Trade date', trade_date_p2)
        if tenor_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Tenor', tenor_p2)
        if tenor_unit_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Tenor unit', tenor_unit_p2)
        if value_date_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Value date', value_date_p2)
        if broker_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Broker', broker_p2)
        if debit_by_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Debit by', debit_by_p2)
        if debit_account_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_text_multi('Phase 2', 'Debit account', self.no_mask(debit_account_p2))
        if debit_currency_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Debit currency', debit_currency_p2)
        if debit_amount_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Debit amount', debit_amount_p2)
        if spot_rate_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Spot rate', spot_rate_p2)
        if swap_point_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Swap point', swap_point_p2)
        if trade_rate_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Trade rate', trade_rate_p2)
        if forward_rate_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Forward rate', forward_rate_p2)
        if credit_by_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Credit by', credit_by_p2)
        if credit_account_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_text_multi('Phase 2', 'Credit account', self.no_mask(credit_account_p2))
        if credit_currency_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Credit currency', credit_currency_p2)
        if credit_amount_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Credit amount', credit_amount_p2)
        self.bo_click_tab('Additional infofmation')
        if other_reference:
            self.bo_assert_text('Other reference', other_reference)
        if other_settlement_instruction:
            self.bo_assert_text('Other settlement instruction', other_settlement_instruction)
        if remark:
            self.bo_assert_text('Remark', remark)
        if user_define_field:
            self.bo_assert_text('User define field', user_define_field)
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

    def treasury_account_update(self, account_number=None, account_name=None, counterparty_type=None, counterparty_code=None, branch_code=None, catalogue_code=None, currency_code=None, trade_group=None, details_category=None, trade_type=None, deal_ticket_number=None, account_status=None, margin_trading_y_n=None, margin_trading_rate=None, open_date=None, value_date=None, tenor=None, tenor_unit=None, settle_tenor=None, settle_tenor_unit=None, interest_payment_tenor=None, interest_payment_tenor_unit=None, from_date=None, to_date=None, last_transaction_date=None, close_date=None, rollover_option=None, rollover_to_catalogue=None, dealer=None, created_by=None, approved_by=None, account_manager_staff_code=None, amount=None, average_price=None, margin_amount=None, interest_accrual_amount=None, intpayable_receivebe=None, interest_due=None, interest_overdue=None, interest_suspense=None, interest_prepaid=None, interest_not_paid=None, interest_payment_method=None, interest_paid=None, settlement_by_on_value_date=None, currency_on_value_date=None, account_no_on_value_date=None, settlement_by_on_maturity=None, currency_on_maturity=None, account_no_on_maturity=None, trade_date=None, tenor_p1=None, tenor_unit_p1=None, value_date_p1=None, broker=None, debit_by=None, debit_account=None, debit_currency=None, debit_amount=None, reference_rate=None, swap_point=None, trade_rate=None, forward_rate=None, credit_by=None, credit_account=None, credit_currency=None, credit_amount=None, trade_date_p2=None, tenor_p2=None, tenor_unit_p2=None, value_date_p2=None, broker_p2=None, debit_by_p2=None, debit_account_p2=None, debit_currency_p2=None, debit_amount_p2=None, spot_rate_p2=None, swap_point_p2=None, trade_rate_p2=None, forward_rate_p2=None, credit_by_p2=None, credit_account_p2=None, credit_currency_p2=None, credit_amount_p2=None, other_reference=None, other_settlement_instruction=None, remark=None, user_define_field=None, list_error_message=None):
        # view
        self.treasury_account_view(account_number=account_number)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        self.key_escape()
        if margin_trading_y_n:
            self.bo_select('Margin trading (Y/N)', margin_trading_y_n)
        if margin_trading_rate:
            self.bo_write_number('Margin trading rate', margin_trading_rate)
        self.key_escape()
        if rollover_option:
            self.bo_select('Rollover option', rollover_option)
        if rollover_to_catalogue:
            self.bo_write_group('Rollover to catalogue', rollover_to_catalogue)
        self.bo_click_tab('Balance information')
        if average_price:
            self.bo_write_number('Average price', average_price)
        self.bo_click_tab('Additional infofmation')
        if other_reference:
            self.bo_write_text('Other reference', other_reference)
        if other_settlement_instruction:
            self.bo_write_text('Other settlement instruction', other_settlement_instruction)
        if remark:
            self.bo_write_text('Remark', remark)
        if user_define_field:
            self.bo_write_text('User define field', user_define_field)
        # assert value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_value('Account number', self.treasury_account_number_mask(account_number))
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if counterparty_type:
            self.bo_assert_select('Counterparty type', counterparty_type)
        if counterparty_code:
            self.bo_assert_value_group('Counterparty code', self.customer_code_mask(counterparty_code))
        if branch_code:
            self.bo_assert_text_group('Branch code', branch_code)
        if catalogue_code:
            self.bo_assert_text('Category code', catalogue_code)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if trade_group:
            self.bo_assert_select('Trade group', trade_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if trade_type:
            self.bo_assert_select('Trade type', trade_type)
        if deal_ticket_number:
            self.bo_assert_text('Deal ticket number', deal_ticket_number)
        if account_status:
            self.bo_assert_select('Account status', account_status)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if value_date:
            self.bo_assert_date('Value date', value_date)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor unit', tenor_unit)
        if settle_tenor:
            self.bo_assert_value_group('Settle tenor', settle_tenor)
        if settle_tenor_unit:
            self.bo_assert_select_group('Settle tenor unit', settle_tenor_unit)
        if interest_payment_tenor:
            self.bo_assert_value_group('Interest payment tenor', interest_payment_tenor)
        if interest_payment_tenor_unit:
            self.bo_assert_select_group('Interest payment tenor unit', interest_payment_tenor_unit)
        if from_date:
            self.bo_assert_date('From date', from_date)
        if to_date:
            self.bo_assert_date('To date', to_date)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if dealer:
            self.bo_assert_text('Dealer', dealer)
        if created_by:
            self.bo_assert_text('Created by', created_by)
        if approved_by:
            self.bo_assert_text('Approved by', approved_by)
        if account_manager_staff_code:
            self.bo_assert_text('Account manager staff code', account_manager_staff_code)
        self.bo_click_tab('Balance information')
        if amount:
            self.bo_assert_value('Amount', amount)
        if margin_amount:
            self.bo_assert_value('Margin amount', margin_amount)
        if interest_accrual_amount:
            self.bo_assert_value('Interest accrual amount', interest_accrual_amount)
        if intpayable_receivebe:
            self.bo_assert_value('Int.payable/receivebe', intpayable_receivebe)
        if interest_due:
            self.bo_assert_value('Interest due', interest_due)
        if interest_overdue:
            self.bo_assert_value('Interest overdue', interest_overdue)
        if interest_suspense:
            self.bo_assert_value('Interest suspense', interest_suspense)
        if interest_prepaid:
            self.bo_assert_value('Interest prepaid', interest_prepaid)
        if interest_not_paid:
            self.bo_assert_value('Interest not paid', interest_not_paid)
        if interest_payment_method:
            self.bo_assert_select('Interest payment method', interest_payment_method)
        if interest_paid:
            self.bo_assert_value('Interest paid', interest_paid)
        self.bo_click_tab('Settlement information')
        if settlement_by_on_value_date:
            self.bo_click_collap('On value date')
            self.bo_assert_value_multi('On value date', 'Settlement by', settlement_by_on_value_date)
        if currency_on_value_date:
            self.bo_click_collap('On value date')
            self.bo_assert_value_multi('On value date', 'Currency', currency_on_value_date)
        if account_no_on_value_date:
            self.bo_click_collap('On value date')
            self.bo_assert_text_multi('On value date', 'Account No', self.no_mask(account_no_on_value_date))
        if settlement_by_on_maturity:
            self.bo_click_collap('On maturity')
            self.bo_assert_value_multi('On maturity', 'Settlement by', settlement_by_on_maturity)
        if currency_on_maturity:
            self.bo_click_collap('On maturity')
            self.bo_assert_value_multi('On maturity', 'Currency', currency_on_maturity)
        if account_no_on_maturity:
            self.bo_click_collap('On maturity')
            self.bo_assert_text_multi('On maturity', 'Account No', self.no_mask(account_no_on_maturity))
        if trade_date:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Trade date', trade_date)
        if tenor_p1:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Tenor', tenor_p1)
        if tenor_unit_p1:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Tenor unit', tenor_unit_p1)
        if value_date_p1:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Value date', value_date_p1)
        if broker:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Broker', broker)
        if debit_by:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Debit by', debit_by)
        if debit_account:
            self.bo_click_collap('Phase 1')
            self.bo_assert_text_multi('Phase 1', 'Debit account', self.no_mask(debit_account))
        if debit_currency:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Debit currency', debit_currency)
        if debit_amount:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Debit amount', debit_amount)
        if reference_rate:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Reference rate', reference_rate)
        if swap_point:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Swap point', swap_point)
        if trade_rate:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Trade rate', trade_rate)
        if forward_rate:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Forward rate', forward_rate)
        if credit_by:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Credit by', credit_by)
        if credit_account:
            self.bo_click_collap('Phase 1')
            self.bo_assert_text_multi('Phase 1', 'Credit account', self.no_mask(credit_account))
        if credit_currency:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Credit currency', credit_currency)
        if credit_amount:
            self.bo_click_collap('Phase 1')
            self.bo_assert_value_multi('Phase 1', 'Credit amount', credit_amount)
        if trade_date_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Trade date', trade_date_p2)
        if tenor_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Tenor', tenor_p2)
        if tenor_unit_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Tenor unit', tenor_unit_p2)
        if value_date_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Value date', value_date_p2)
        if broker_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Broker', broker_p2)
        if debit_by_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Debit by', debit_by_p2)
        if debit_account_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_text_multi('Phase 2', 'Debit account', self.no_mask(debit_account_p2))
        if debit_currency_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Debit currency', debit_currency_p2)
        if debit_amount_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Debit amount', debit_amount_p2)
        if spot_rate_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Spot rate', spot_rate_p2)
        if swap_point_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Swap point', swap_point_p2)
        if trade_rate_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Trade rate', trade_rate_p2)
        if forward_rate_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Forward rate', forward_rate_p2)
        if credit_by_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Credit by', credit_by_p2)
        if credit_account_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_text_multi('Phase 2', 'Credit account', self.no_mask(credit_account_p2))
        if credit_currency_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Credit currency', credit_currency_p2)
        if credit_amount_p2:
            self.bo_click_collap('Phase 2')
            self.bo_assert_value_multi('Phase 2', 'Credit amount', credit_amount_p2)
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

    def treasury_account_delete(self, account_number, list_error_message=None):
        # search
        self.treasury_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, self.treasury_account_number_mask(account_number))
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
            self.treasury_account_simple_search(str(account_number).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {account_number}')
            return account_number

# -------------------------- handle BO approval - TREASURY --------------------------
    # TRS-Catalogue Definition - Data Verification
    def treasury_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, trade_group=None, details_category=None, trade_type=None, margin_trading=None, market=None, catalogue_status=None, settle_tenor=None, settle_tenor_unit=None, tenor=None, tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, rollover_option=None, revaluation=None, user_create=None, approve_by=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if trade_group:
            self.bo_assert_select('Trade Group', trade_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if trade_type:
            self.bo_assert_select('Trade Type', trade_type)
        if margin_trading:
            self.bo_assert_select('Margin Trading', margin_trading)
        if market:
            self.bo_assert_select('Market', market)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if settle_tenor:
            self.bo_assert_value('Settle Tenor', settle_tenor)
        if settle_tenor_unit:
            self.bo_assert_select('Settle Tenor Unit', settle_tenor_unit)
        if tenor:
            self.bo_assert_value('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select('Tenor Unit', tenor_unit)
        if interest_tenor:
            self.bo_assert_value('Interest Tenor', interest_tenor)
        if interest_tenor_unit:
            self.bo_assert_select('Interest Tenor Unit', interest_tenor_unit)
        if rollover_option:
            self.bo_assert_select('Rollover Option', rollover_option)
        if revaluation:
            self.bo_assert_select('Revaluation', revaluation)
        if user_create:
            self.bo_assert_text('User create', user_create)
        if approve_by:
            self.bo_assert_text('Approve by', approve_by)
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

    def treasury_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, trade_group=None, details_category=None, trade_type=None, margin_trading=None, market=None, catalogue_status=None, settle_tenor=None, settle_tenor_unit=None, tenor=None, tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, rollover_option=None, revaluation=None, user_create=None, approve_by=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if trade_group:
            self.bo_assert_select('Trade Group', trade_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if trade_type:
            self.bo_assert_select('Trade Type', trade_type)
        if margin_trading:
            self.bo_assert_select('Margin Trading', margin_trading)
        if market:
            self.bo_assert_select('Market', market)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if settle_tenor:
            self.bo_assert_value('Settle Tenor', settle_tenor)
        if settle_tenor_unit:
            self.bo_assert_select('Settle Tenor Unit', settle_tenor_unit)
        if tenor:
            self.bo_assert_value('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select('Tenor Unit', tenor_unit)
        if interest_tenor:
            self.bo_assert_value('Interest Tenor', interest_tenor)
        if interest_tenor_unit:
            self.bo_assert_select('Interest Tenor Unit', interest_tenor_unit)
        if rollover_option:
            self.bo_assert_select('Rollover Option', rollover_option)
        if revaluation:
            self.bo_assert_select('Revaluation', revaluation)
        if user_create:
            self.bo_assert_text_group('User create', user_create)
        if approve_by:
            self.bo_assert_text_group('Approve by', approve_by)
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

    def treasury_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, trade_group=None, details_category=None, trade_type=None, margin_trading=None, market=None, status=None, settle_tenor=None, settle_tenor_unit=None, tenor=None, tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, rollover_option=None, revaluation=None, creator=None, approve_by=None):
        # search and verify
        self.treasury_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalog Code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalog name', 1, catalogue_name)
        if trade_group:
            self.assert_table_data('Trade Group', 1, trade_group)
        if details_category:
            self.assert_table_data('Details category', 1, details_category)
        if trade_type:
            self.assert_table_data('Trade Type', 1, trade_type)
        if margin_trading:
            self.assert_table_data('Margin Trading', 1, margin_trading)
        if market:
            self.assert_table_data('Market', 1, market)
        if status:
            self.assert_table_data('Status', 1, status)
        if settle_tenor:
            self.assert_table_data('Settle Tenor', 1, settle_tenor)
        if settle_tenor_unit:
            self.assert_table_data('Settle Tenor Unit', 1, settle_tenor_unit)
        if tenor:
            self.assert_table_data('Tenor', 1, tenor)
        if tenor_unit:
            self.assert_table_data('Tenor Unit', 1, tenor_unit)
        if interest_tenor:
            self.assert_table_data('Interest Tenor', 1, interest_tenor)
        if interest_tenor_unit:
            self.assert_table_data('Interest Tenor Unit', 1, interest_tenor_unit)
        if rollover_option:
            self.assert_table_data('Rollover Option', 1, rollover_option)
        if revaluation:
            self.assert_table_data('Revaluation', 1, revaluation)
        if creator:
            self.assert_table_data('Creator', 1, creator)
        if approve_by:
            self.assert_table_data('Approve by', 1, approve_by)

    # TRS-IFC Item Definition - Data Verification
    def treasury_ifc_item_definition_add_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-IFC Item Definition-Add'
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

    def treasury_ifc_item_definition_update_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-IFC Item Definition-View'
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

    def treasury_ifc_item_definition_search_verify(self, ifc_code, ifc_name=None, value_type=None, ifc_type=None, value=None, tenor=None, tenor_unit=None, active_condition=None, status=None):
        # search and verify
        self.treasury_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
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

    def treasury_get_ifc_code(self, ifc_name):
        self.treasury_ifc_item_definition_simple_search(ifc_name)
        self.assert_table_data('IFC name', 1, ifc_name)
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRS-IFC Item Definition-View')
        self.bo_click_tab('General information')
        ifc_code_out=self.bo_get_value('IFC code')
        print(f'IFC code: {ifc_code_out}')
        return ifc_code_out

    # TRS-IFC Auto Fee - Data Verification
    def treasury_ifc_auto_fee_add_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-IFC Auto Fee-Add'
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

    def treasury_ifc_auto_fee_update_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-IFC Auto Fee-View'
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

    def treasury_ifc_auto_fee_search_verify(self, transaction_code, ifc_code, transaction_name=None, ifc_name=None):
        # search
        self.treasury_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        # verify value
        self.assert_table_data('Transaction code', 1, transaction_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        if transaction_name:
            self.assert_table_data('Transaction name', 1, transaction_name)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)

