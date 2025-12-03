from webui_test.case import *

class MortgageActions(TestCase):

# -------------------------- handle FO - MORTGAGE --------------------------
    # MTG_OPN: 4400: Open new collateral account
    def mtg_opn(self, account_name=None, customer_type=None, customer_code=None, catalogue_code=None, collateral_asset_type=None, collateral_asset_class=None, sercurity_paper_type=None, collateral_rate=None, risk_allocation_rate=None, collateral_asset_value=None, market_value=None, forced_sale_value=None, cc_contract=None, cc_amount=None, seq_number=None, reference_number=None, name_of_title=None, house_no=None, plot_no=None, holding_no=None, ward_no=None, block_no=None, area_acre=None, street=None, township=None, division_city=None, location=None, legal_address=None, legal_local_address=None, expiry_date=None, policy_amount=None, company_issues_policy=None, policy_number=None, evaluate_by=None, evaluate_method=None, evaluate_date=None, new_evaluate_date=None, insurance_name=None, insurance_expiry_date=None, description=None, account_number=None, catalogue_name=None, currency_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_OPN', '4400')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4400: Open new collateral account')
        # enter value
        if account_name:
            self.fo_write_text('Account name', account_name)
        self.key_escape()
        if customer_type:
            self.fo_select('Customer type', customer_type)
        if customer_code:
            self.fo_write_group('Customer code', str(customer_code).replace('-', ''))
            self.wait_loading()
        if catalogue_code:
            self.fo_write('Catalogue code', catalogue_code)
        self.key_escape()
        if collateral_asset_type:
            self.fo_select('Collateral asset type', collateral_asset_type)
        self.key_escape()
        if collateral_asset_class:
            self.fo_select('Collateral asset class', collateral_asset_class)
        self.key_escape()
        if sercurity_paper_type:
            self.fo_select('Sercurity paper type', sercurity_paper_type)
        if collateral_rate:
            self.fo_write_number_group('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.fo_write_number('Risk allocation rate', risk_allocation_rate)
        if collateral_asset_value:
            self.fo_write_number('Collateral asset value', collateral_asset_value)
        if market_value:
            self.fo_write_number('Market value', market_value)
        if forced_sale_value:
            self.fo_write_number('Forced sale value', forced_sale_value)
        if cc_contract:
            self.fo_write_text('CC contract', cc_contract)
        if cc_amount:
            self.fo_write_number('CC amount', cc_amount)
        if seq_number:
            self.fo_write_number('Seq number', seq_number)
        if reference_number:
            self.fo_write_text('Reference number', reference_number)
        if name_of_title:
            self.fo_click_collap('Other address')
            self.fo_write_text_multi('Other address', 'Name of title', name_of_title)
        if house_no:
            self.fo_click_collap('Other address')
            self.fo_write_text_multi('Other address', 'House no', house_no)
        if plot_no:
            self.fo_click_collap('Other address')
            self.fo_write_text_multi('Other address', 'Plot no', plot_no)
        if holding_no:
            self.fo_click_collap('Other address')
            self.fo_write_text_multi('Other address', 'Holding no', holding_no)
        if ward_no:
            self.fo_click_collap('Other address')
            self.fo_write_text_multi('Other address', 'Ward no', ward_no)
        if block_no:
            self.fo_click_collap('Other address')
            self.fo_write_text_multi('Other address', 'Block no', block_no)
        if area_acre:
            self.fo_click_collap('Other address')
            self.fo_write_text_multi('Other address', 'Area (acre)', area_acre)
        if street:
            self.fo_click_collap('Other address')
            self.fo_write_text_multi('Other address', 'Street', street)
        if township:
            self.fo_click_collap('Other address')
            self.fo_write_text_multi('Other address', 'Township', township)
        if division_city:
            self.fo_click_collap('Other address')
            self.fo_write_text_multi('Other address', 'Division, city', division_city)
        self.key_escape()
        if location:
            self.fo_select('Location', location)
        if legal_address:
            self.fo_write_text('Legal address', legal_address)
        if legal_local_address:
            self.fo_write_text('Legal local address', legal_local_address)
        if expiry_date:
            self.fo_write_date('Expiry date', expiry_date)
        if policy_amount:
            self.fo_write_number('Policy Amount', policy_amount)
        if company_issues_policy:
            self.fo_write_text('Company issues policy', company_issues_policy)
        if policy_number:
            self.fo_write_text('Policy Number', policy_number)
        if evaluate_by:
            self.fo_write_text('Evaluate by', evaluate_by)
        self.key_escape()
        if evaluate_method:
            self.fo_select('Evaluate method', evaluate_method)
        if evaluate_date:
            self.fo_write_date('Evaluate date', evaluate_date)
        if new_evaluate_date:
            self.fo_write_date('New Evaluate date', new_evaluate_date)
        if insurance_name:
            self.fo_write_text('Insurance Name', insurance_name)
        if insurance_expiry_date:
            self.fo_write_text('Insurance Expiry Date', insurance_expiry_date)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
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
            print(f'Transaction references MTG_OPN: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def mtg_opn_view(self, transaction_references, account_name=None, customer_type=None, customer_code=None, catalogue_code=None, collateral_asset_type=None, collateral_asset_class=None, sercurity_paper_type=None, collateral_rate=None, risk_allocation_rate=None, collateral_asset_value=None, market_value=None, forced_sale_value=None, cc_contract=None, cc_amount=None, seq_number=None, reference_number=None, name_of_title=None, house_no=None, plot_no=None, holding_no=None, ward_no=None, block_no=None, area_acre=None, street=None, township=None, division_city=None, location=None, legal_address=None, legal_local_address=None, expiry_date=None, policy_amount=None, company_issues_policy=None, policy_number=None, evaluate_by=None, evaluate_method=None, evaluate_date=None, new_evaluate_date=None, insurance_name=None, insurance_expiry_date=None, description=None, account_number=None, catalogue_name=None, currency_code=None, expected_posting=None):
        self.transaction_view(transaction_references, '4400: Open new collateral account')
        # compare value
        if account_name:
            self.fo_assert_text('Account name', account_name)
        if customer_type:
            self.fo_assert_select('Customer type', customer_type)
        if customer_code:
            self.fo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if catalogue_code:
            self.fo_assert_value('Catalogue code', catalogue_code)
        if collateral_asset_type:
            self.fo_assert_select('Collateral asset type', collateral_asset_type)
        if collateral_asset_class:
            self.fo_assert_select('Collateral asset class', collateral_asset_class)
        if sercurity_paper_type:
            self.fo_assert_select('Sercurity paper type', sercurity_paper_type)
        if collateral_rate:
            self.fo_assert_value_group('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.fo_assert_value('Risk allocation rate', risk_allocation_rate)
        if collateral_asset_value:
            self.fo_assert_value('Collateral asset value', collateral_asset_value)
        if market_value:
            self.fo_assert_value('Market value', market_value)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if cc_contract:
            self.fo_assert_text('CC contract', cc_contract)
        if cc_amount:
            self.fo_assert_value('CC amount', cc_amount)
        if seq_number:
            self.fo_assert_value('Seq number', seq_number)
        if reference_number:
            self.fo_assert_text('Reference number', reference_number)
        if name_of_title:
            self.fo_click_collap('Other address')
            self.fo_assert_text_multi('Other address', 'Name of title', name_of_title)
        if house_no:
            self.fo_click_collap('Other address')
            self.fo_assert_text_multi('Other address', 'House no', house_no)
        if plot_no:
            self.fo_click_collap('Other address')
            self.fo_assert_text_multi('Other address', 'Plot no', plot_no)
        if holding_no:
            self.fo_click_collap('Other address')
            self.fo_assert_text_multi('Other address', 'Holding no', holding_no)
        if ward_no:
            self.fo_click_collap('Other address')
            self.fo_assert_text_multi('Other address', 'Ward no', ward_no)
        if block_no:
            self.fo_click_collap('Other address')
            self.fo_assert_text_multi('Other address', 'Block no', block_no)
        if area_acre:
            self.fo_click_collap('Other address')
            self.fo_assert_text_multi('Other address', 'Area (acre)', area_acre)
        if street:
            self.fo_click_collap('Other address')
            self.fo_assert_text_multi('Other address', 'Street', street)
        if township:
            self.fo_click_collap('Other address')
            self.fo_assert_text_multi('Other address', 'Township', township)
        if division_city:
            self.fo_click_collap('Other address')
            self.fo_assert_text_multi('Other address', 'Division, city', division_city)
        if location:
            self.fo_assert_select('Location', location)
        if legal_address:
            self.fo_assert_text('Legal address', legal_address)
        if legal_local_address:
            self.fo_assert_text('Legal local address', legal_local_address)
        if expiry_date:
            self.fo_assert_date('Expiry date', expiry_date)
        if policy_amount:
            self.fo_assert_value('Policy Amount', policy_amount)
        if company_issues_policy:
            self.fo_assert_text('Company issues policy', company_issues_policy)
        if policy_number:
            self.fo_assert_text('Policy Number', policy_number)
        if evaluate_by:
            self.fo_assert_text('Evaluate by', evaluate_by)
        if evaluate_method:
            self.fo_assert_select('Evaluate method', evaluate_method)
        if evaluate_date:
            self.fo_assert_date('Evaluate date', evaluate_date)
        if new_evaluate_date:
            self.fo_assert_date('New Evaluate date', new_evaluate_date)
        if insurance_name:
            self.fo_assert_text('Insurance Name', insurance_name)
        if insurance_expiry_date:
            self.fo_assert_text('Insurance Expiry Date', insurance_expiry_date)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.fo_assert_select('Currency code', currency_code)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_OPN: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # MTG_APR: 4450: Approve collateral account
    def mtg_apr(self, account_number=None, customer_code=None, customer_name=None, customer_address=None, home=None, office=None, description=None, account_holder_name=None, forced_sale_value=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_APR', '4450')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4450: Approve collateral account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if customer_code:
            self.fo_write('Customer code', str(customer_code).replace('-', ''))
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
            self.fo_write_text_group('Description', description)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
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
            print(f'Transaction references MTG_APR: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def mtg_apr_view(self, transaction_references, account_number=None, customer_code=None, customer_name=None, customer_address=None, home=None, office=None, description=None, account_holder_name=None, forced_sale_value=None, expected_posting=None):
        self.transaction_view(transaction_references, '4450: Approve collateral account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
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
            self.fo_assert_text_group('Description', description)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_APR: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # MTG_BLK: 4484: Block account
    def mtg_blk(self, account_number=None, account_holder_name=None, customer_name=None, customer_address=None, description=None, customer_description=None, forced_sale_value=None, customer_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_BLK', '4484')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4484: Block account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if account_holder_name:
            self.fo_write_text('Account holder name', account_holder_name)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
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
            print(f'Transaction references MTG_BLK: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def mtg_blk_view(self, transaction_references, account_number=None, account_holder_name=None, customer_name=None, customer_address=None, description=None, customer_description=None, forced_sale_value=None, customer_code=None, expected_posting=None):
        self.transaction_view(transaction_references, '4484: Block account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_BLK: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # MTG_BRL: 4481: Release block account
    def mtg_brl(self, account_number=None, account_holder_name=None, customer_name=None, customer_address=None, description=None, customer_description=None, forced_sale_value=None, customer_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_BRL', '4481')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4481: Release block account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if account_holder_name:
            self.fo_write_text('Account holder name', account_holder_name)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
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
            print(f'Transaction references MTG_BRL: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def mtg_brl_view(self, transaction_references, account_number=None, account_holder_name=None, customer_name=None, customer_address=None, description=None, customer_description=None, forced_sale_value=None, customer_code=None, expected_posting=None):
        self.transaction_view(transaction_references, '4481: Release block account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_BRL: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # MTG_INR: 4451: Increasing asset value
    def mtg_inr(self, account_number=None, increasing_value=None, increasing_booking_value=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, account_holder_name=None, asset_value=None, asset_booking_value=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_INR', '4451:')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4451: Increasing asset value')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if increasing_value:
            self.fo_write_number('Increasing value', increasing_value)
        if increasing_booking_value:
            self.fo_write_number('Increasing booking value', increasing_booking_value)
        if customer_code:
            self.fo_write('Customer code', customer_code)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if asset_value:
            self.fo_assert_value('Asset value', asset_value)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
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
            print(f'Transaction references MTG_INR: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def mtg_inr_view(self, transaction_references, account_number=None, increasing_value=None, increasing_booking_value=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, account_holder_name=None, asset_value=None, asset_booking_value=None, expected_posting=None):
        self.transaction_view(transaction_references, '4451: Increasing asset value')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if increasing_value:
            self.fo_assert_value('Increasing value', increasing_value)
        if increasing_booking_value:
            self.fo_assert_value('Increasing booking value', increasing_booking_value)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if asset_value:
            self.fo_assert_value('Asset value', asset_value)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_INR: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # MTG_DCR: 4452: Decreasing asset value
    def mtg_dcr(self, account_number=None, decreasing_value=None, decreasing_booking_value=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, account_holder_name=None, asset_value=None, asset_booking_value=None, secured_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_DCR', '4452')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4452: Decreasing asset value')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if decreasing_value:
            self.fo_write_number('Decreasing value', decreasing_value)
        if decreasing_booking_value:
            self.fo_write_number('Decreasing booking value', decreasing_booking_value)
        if customer_code:
            self.fo_write('Customer code', customer_code)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if asset_value:
            self.fo_assert_value('Asset value', asset_value)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
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
            print(f'Transaction references MTG_DCR: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def mtg_dcr_view(self, transaction_references, account_number=None, decreasing_value=None, decreasing_booking_value=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, account_holder_name=None, asset_value=None, asset_booking_value=None, secured_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '4452: Decreasing asset value')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if decreasing_value:
            self.fo_assert_value('Decreasing value', decreasing_value)
        if decreasing_booking_value:
            self.fo_assert_value('Decreasing booking value', decreasing_booking_value)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if asset_value:
            self.fo_assert_value('Asset value', asset_value)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_DCR: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # MTG_HDT: MTG-4460: History Inquiry Detail
    def mtg_hdt(self, account_number=None, from_date=None, to_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_HDT', '4460')
        self.wait_for_button_available('Accept')
        self.assert_form_title('MTG-4460: History Inquiry Detail')
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
            print(f'Transaction references MTG_HDT: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    # MTG_RTN: 4431: Return collateral asset to customer
    def mtg_rtn(self, account_number=None, return_amount=None, return_amount_in_asset_currency=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, asset_booking_value=None, secured_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_RTN', '4431')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4431: Return collateral asset to customer')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if return_amount:
            self.fo_write_number('Return amount', return_amount)
        if return_amount_in_asset_currency:
            self.fo_write_number('Return amount in asset currency', return_amount_in_asset_currency)
        if customer_code:
            self.fo_write('Customer code', customer_code)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
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
            print(f'Transaction references MTG_RTN: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def mtg_rtn_view(self, transaction_references, account_number=None, return_amount=None, return_amount_in_asset_currency=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, asset_booking_value=None, secured_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '4431: Return collateral asset to customer')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if return_amount:
            self.fo_assert_value('Return amount', return_amount)
        if return_amount_in_asset_currency:
            self.fo_assert_value('Return amount in asset currency', return_amount_in_asset_currency)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_RTN: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # MTG_CLS: 4490: Close account
    def mtg_cls(self, account_number=None, account_holder_name=None, customer_name=None, customer_address=None, description=None, customer_description=None, forced_sale_value=None, customer_code=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_CLS', '4490')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4490: Close account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if account_holder_name:
            self.fo_write_text('Account holder name', account_holder_name)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
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
            print(f'Transaction references MTG_CLS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def mtg_cls_view(self, transaction_references, account_number=None, account_holder_name=None, customer_name=None, customer_address=None, description=None, customer_description=None, forced_sale_value=None, customer_code=None, expected_posting=None):
        self.transaction_view(transaction_references, '4490: Close account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if account_holder_name:
            self.fo_assert_text('Account holder name', account_holder_name)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_CLS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # MTG_RLS: 4410: Release asset from credit account
    def mtg_rls(self, account_number=None, credit_account=None, release_amount_in_collateral_currency=None, release_amount_in_credit_currency=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, forced_sale_value=None, collateral_account_currency=None, credit_account_currency=None, secured_amount=None, exchange_rate=None, base_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_RLS', '4410')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4410: Release asset from credit account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        if release_amount_in_collateral_currency:
            self.fo_write_number('Release amount in collateral currency', release_amount_in_collateral_currency)
        if release_amount_in_credit_currency:
            self.fo_write_number('Release amount in credit currency', release_amount_in_credit_currency)
        if customer_code:
            self.fo_write('Customer code', str(customer_code).replace('-', ''))
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if collateral_account_currency:
            self.fo_assert_select('Collateral account currency', collateral_account_currency)
        if credit_account_currency:
            self.fo_assert_select('credit account currency', credit_account_currency)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if exchange_rate:
            self.fo_assert_text('Exchange rate', exchange_rate)
        if base_amount:
            self.fo_assert_value('base amount', base_amount)
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
            print(f'Transaction references MTG_RLS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            return transaction_references, account_number_out, credit_account_out

    def mtg_rls_view(self, transaction_references, account_number=None, credit_account=None, release_amount_in_collateral_currency=None, release_amount_in_credit_currency=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, forced_sale_value=None, collateral_account_currency=None, credit_account_currency=None, secured_amount=None, exchange_rate=None, base_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '4410: Release asset from credit account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if credit_account:
            self.fo_assert_value_group('Credit account', self.deposit_account_number_mask(credit_account))
        if release_amount_in_collateral_currency:
            self.fo_assert_value('Release amount in collateral currency', release_amount_in_collateral_currency)
        if release_amount_in_credit_currency:
            self.fo_assert_value('Release amount in credit currency', release_amount_in_credit_currency)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if collateral_account_currency:
            self.fo_assert_select('Collateral account currency', collateral_account_currency)
        if credit_account_currency:
            self.fo_assert_select('credit account currency', credit_account_currency)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if exchange_rate:
            self.fo_assert_text('Exchange rate', exchange_rate)
        if base_amount:
            self.fo_assert_value('base amount', base_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_RLS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        return transaction_references, account_number_out, credit_account_out

    # MTG_RLS_OD: Release asset from overdraft contract
    def mtg_rls_od(self, account_number=None, contract_number=None, release_amount_in_collateral_currency=None, release_amount_in_overdraft_contract_currency=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, forced_sale_value=None, collateral_account_currency=None, overdraft_contract_currency=None, secured_amount=None, exchange_rate=None, base_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_RLS_OD', 'OD contract')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Release asset from overdraft contract')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if contract_number:
            self.fo_write_group('Contract number', str(contract_number).replace('-', ''))
            self.wait_loading()
        if release_amount_in_collateral_currency:
            self.fo_write_number('Release amount in collateral currency', release_amount_in_collateral_currency)
        if release_amount_in_overdraft_contract_currency:
            self.fo_write_number('Release amount in overdraft contract currency', release_amount_in_overdraft_contract_currency)
        if customer_code:
            self.fo_write('Customer code', customer_code)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if collateral_account_currency:
            self.fo_assert_select('Collateral account currency', collateral_account_currency)
        if overdraft_contract_currency:
            self.fo_assert_select('Overdraft contract currency', overdraft_contract_currency)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if exchange_rate:
            self.fo_assert_text('Exchange rate', exchange_rate)
        if base_amount:
            self.fo_assert_value('base amount', base_amount)
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
            print(f'Transaction references MTG_RLS_OD: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            contract_number_out=self.fo_get_value_group('Contract number')
            print(f'Contract number: {contract_number_out}')
            return transaction_references, account_number_out, contract_number_out

    def mtg_rls_od_view(self, transaction_references, account_number=None, contract_number=None, release_amount_in_collateral_currency=None, release_amount_in_overdraft_contract_currency=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, forced_sale_value=None, collateral_account_currency=None, overdraft_contract_currency=None, secured_amount=None, exchange_rate=None, base_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Release asset from overdraft contract')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if contract_number:
            self.fo_assert_value_group('Contract number', self.deposit_account_number_mask(contract_number))
        if release_amount_in_collateral_currency:
            self.fo_assert_value('Release amount in collateral currency', release_amount_in_collateral_currency)
        if release_amount_in_overdraft_contract_currency:
            self.fo_assert_value('Release amount in overdraft contract currency', release_amount_in_overdraft_contract_currency)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if collateral_account_currency:
            self.fo_assert_select('Collateral account currency', collateral_account_currency)
        if overdraft_contract_currency:
            self.fo_assert_select('Overdraft contract currency', overdraft_contract_currency)
        if secured_amount:
            self.fo_assert_value('Secured amount', secured_amount)
        if exchange_rate:
            self.fo_assert_text('Exchange rate', exchange_rate)
        if base_amount:
            self.fo_assert_value('base amount', base_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_RLS_OD: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        contract_number_out=self.fo_get_value_group('Contract number')
        print(f'F8: Contract number: {contract_number_out}')
        return transaction_references, account_number_out, contract_number_out

    # MTG_SCR: 4420: Secure asset for credit account
    def mtg_scr(self, account_number=None, credit_account=None, amount_secure_from_this_asset=None, amount_secured_for_credit_account=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, collateral_account_currency=None, forced_sale_value=None, secured_amount_01=None, credit_account_currency=None, credit_limit=None, secured_amount_02=None, total_secured_amount=None, exchange_rate=None, base_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_SCR', '4420')
        self.wait_for_button_available('Accept')
        self.assert_form_title('4420: Secure asset for credit account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if credit_account:
            self.fo_write_group('Credit account', str(credit_account).replace('-', ''))
            self.wait_loading()
        if amount_secure_from_this_asset:
            self.fo_write_number('Amount secure from this asset', amount_secure_from_this_asset)
        if amount_secured_for_credit_account:
            self.fo_write_number('Amount secured for credit account', amount_secured_for_credit_account)
        if customer_code:
            self.fo_write('Customer code', customer_code)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if collateral_account_currency:
            self.fo_assert_select('Collateral account currency', collateral_account_currency)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if secured_amount_01:
            self.fo_assert_value('Secured amount', secured_amount_01)
        if credit_account_currency:
            self.fo_assert_select('credit account currency', credit_account_currency)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if secured_amount_02:
            self.fo_assert_value('Secured amount', secured_amount_02)
        if total_secured_amount:
            self.fo_assert_value('Total secured amount', total_secured_amount)
        if exchange_rate:
            self.fo_assert_text('Exchange rate', exchange_rate)
        if base_amount:
            self.fo_assert_value('base amount', base_amount)
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
            print(f'Transaction references MTG_SCR: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            credit_account_out=self.fo_get_value_group('Credit account')
            print(f'Credit account: {credit_account_out}')
            return transaction_references, account_number_out, credit_account_out

    def mtg_scr_view(self, transaction_references, account_number=None, credit_account=None, amount_secure_from_this_asset=None, amount_secured_for_credit_account=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, collateral_account_currency=None, forced_sale_value=None, secured_amount_01=None, credit_account_currency=None, credit_limit=None, secured_amount_02=None, total_secured_amount=None, exchange_rate=None, base_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, '4420: Secure asset for credit account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if credit_account:
            self.fo_assert_value_group('Credit account', self.credit_account_number_mask(credit_account))
        if amount_secure_from_this_asset:
            self.fo_assert_value('Amount secure from this asset', amount_secure_from_this_asset)
        if amount_secured_for_credit_account:
            self.fo_assert_value('Amount secured for credit account', amount_secured_for_credit_account)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if collateral_account_currency:
            self.fo_assert_select('Collateral account currency', collateral_account_currency)
        if forced_sale_value:
            self.fo_assert_value('Forced sale value', forced_sale_value)
        if secured_amount_01:
            self.fo_assert_value('Secured amount', secured_amount_01)
        if credit_account_currency:
            self.fo_assert_select('credit account currency', credit_account_currency)
        if credit_limit:
            self.fo_assert_value('Credit limit', credit_limit)
        if secured_amount_02:
            self.fo_assert_value('Secured amount', secured_amount_02)
        if total_secured_amount:
            self.fo_assert_value('Total secured amount', total_secured_amount)
        if exchange_rate:
            self.fo_assert_text('Exchange rate', exchange_rate)
        if base_amount:
            self.fo_assert_value('base amount', base_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_SCR: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        credit_account_out=self.fo_get_value_group('Credit account')
        print(f'F8: Credit account: {credit_account_out}')
        return transaction_references, account_number_out, credit_account_out

    # MTG_SCR_OD: Secure asset for overdraft contract
    def mtg_scr_od(self, account_number=None, overdraft_contract_number=None, amount_secure_from_this_asset=None, amount_secured_for_overdraft_contract=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, collateral_account_currency=None, asset_booking_value=None, secured_amount_01=None, overdraft_contract_currency=None, overdraft_limit=None, secured_amount_02=None, total_secured_amount=None, exchange_rate=None, base_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('MTG_SCR_OD', 'OD contract')
        self.wait_for_button_available('Accept')
        self.assert_form_title('Secure asset for overdraft contract')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if overdraft_contract_number:
            self.fo_write('Overdraft contract number', str(overdraft_contract_number).replace('-', ''))
            self.wait_loading()
        if amount_secure_from_this_asset:
            self.fo_write_number('Amount secure from this asset', amount_secure_from_this_asset)
        if amount_secured_for_overdraft_contract:
            self.fo_write_number('Amount secured for overdraft contract', amount_secured_for_overdraft_contract)
        if customer_code:
            self.fo_write('Customer code', customer_code)
        if customer_name:
            self.fo_write_text('Customer name', customer_name)
        if customer_address:
            self.fo_write_text('Customer address', customer_address)
        if customer_description:
            self.fo_write_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if collateral_account_currency:
            self.fo_assert_select('Collateral account currency', collateral_account_currency)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if secured_amount_01:
            self.fo_assert_value('Secured amount', secured_amount_01)
        if overdraft_contract_currency:
            self.fo_assert_select('Overdraft contract currency', overdraft_contract_currency)
        if overdraft_limit:
            self.fo_assert_value('Overdraft limit', overdraft_limit)
        if secured_amount_02:
            self.fo_assert_value('Secured amount', secured_amount_02)
        if total_secured_amount:
            self.fo_assert_value('Total secured amount', total_secured_amount)
        if exchange_rate:
            self.fo_assert_text('Exchange rate', exchange_rate)
        if base_amount:
            self.fo_assert_value('base amount', base_amount)
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
            print(f'Transaction references MTG_SCR_OD: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            overdraft_contract_number_out=self.fo_get_value('Overdraft contract number')
            print(f'Overdraft contract number: {overdraft_contract_number_out}')
            return transaction_references, account_number_out, overdraft_contract_number_out

    def mtg_scr_od_view(self, transaction_references, account_number=None, overdraft_contract_number=None, amount_secure_from_this_asset=None, amount_secured_for_overdraft_contract=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, description=None, collateral_account_currency=None, asset_booking_value=None, secured_amount_01=None, overdraft_contract_currency=None, overdraft_limit=None, secured_amount_02=None, total_secured_amount=None, exchange_rate=None, base_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'Secure asset for overdraft contract')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.mortgage_account_number_mask(account_number))
        if overdraft_contract_number:
            self.fo_assert_value('Overdraft contract number', self.deposit_account_number_mask(overdraft_contract_number))
        if amount_secure_from_this_asset:
            self.fo_assert_value('Amount secure from this asset', amount_secure_from_this_asset)
        if amount_secured_for_overdraft_contract:
            self.fo_assert_value('Amount secured for overdraft contract', amount_secured_for_overdraft_contract)
        if customer_code:
            self.fo_assert_value('Customer code', self.customer_code_mask(customer_code))
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if collateral_account_currency:
            self.fo_assert_select('Collateral account currency', collateral_account_currency)
        if asset_booking_value:
            self.fo_assert_value('Asset booking value', asset_booking_value)
        if secured_amount_01:
            self.fo_assert_value('Secured amount', secured_amount_01)
        if overdraft_contract_currency:
            self.fo_assert_select('Overdraft contract currency', overdraft_contract_currency)
        if overdraft_limit:
            self.fo_assert_value('Overdraft limit', overdraft_limit)
        if secured_amount_02:
            self.fo_assert_value('Secured amount', secured_amount_02)
        if total_secured_amount:
            self.fo_assert_value('Total secured amount', total_secured_amount)
        if exchange_rate:
            self.fo_assert_text('Exchange rate', exchange_rate)
        if base_amount:
            self.fo_assert_value('base amount', base_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        self.fo_assert_checkbox('Caution!  There is no doubt that banks may be used as a means of Money Laundering/ Terrorist Financing/ Proliferation of Weapons of Mass Destruction.', True)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references MTG_SCR_OD: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        overdraft_contract_number_out=self.fo_get_value('Overdraft contract number')
        print(f'F8: Overdraft contract number: {overdraft_contract_number_out}')
        return transaction_references, account_number_out, overdraft_contract_number_out

# -------------------------- handle BO - MORTGAGE --------------------------
    # MTG-Catalogue Definition
    def mortgage_catalogue_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Collateral', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('MTG-Catalogue Definition-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def mortgage_catalogue_definition_advanced_search(self, catalogue_code=None, catalogue_name=None, currency=None, collateral_asset_type=None, classification=None, collateral_rate_from=None, collateral_rate_to=None, status=None):
        self.close_all_form()
        self.click_menu('Collateral', 'Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('MTG-Catalogue Definition-Search')
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.adv_search_text('Catalogue name', catalogue_name)
        if currency:
            self.adv_search_text('Currency', currency)
        self.key_escape()
        if collateral_asset_type:
            self.adv_search_select('Collateral asset type', collateral_asset_type)
        self.key_escape()
        if classification:
            self.adv_search_select('Classification', classification)
        if collateral_rate_from:
            self.adv_search_group('Collateral rate from', collateral_rate_from)
        if collateral_rate_to:
            self.adv_search_group('Collateral rate to', collateral_rate_to)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        self.click_button_search_advanced()
        self.wait_loading()

    def mortgage_catalogue_definition_add(self, catalogue_code=None, catalogue_name=None, currency_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_rate=None, risk_allocation_rate=None, book_scope=None, depreciation_option=None, catalogue_status=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Collateral', 'Catalogue Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('MTG-Catalogue Definition-Add')
        # enter value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_write('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_write_text('Catalogue name', catalogue_name)
        self.key_escape()
        if currency_code:
            self.bo_select('Currency code', currency_code)
        self.key_escape()
        if collateral_asset_type:
            self.bo_select('Collateral asset type', collateral_asset_type)
        self.key_escape()
        if collateral_asset_classification:
            self.bo_select('Collateral asset classification', collateral_asset_classification)
        if collateral_rate:
            self.bo_write_number('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.bo_write_number('Risk allocation rate', risk_allocation_rate)
        self.key_escape()
        if book_scope:
            self.bo_select('Book scope', book_scope)
        self.key_escape()
        if depreciation_option:
            self.bo_select('Depreciation option', depreciation_option)
        self.key_escape()
        if catalogue_status:
            self.bo_select('Catalogue status', catalogue_status)
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
            catalogue_code_out=self.bo_get_value('Catalogue Code')
            print(f'Catalogue Code: {catalogue_code_out}')
            return catalogue_code_out

    def mortgage_catalogue_definition_view(self, catalogue_code=None, catalogue_name=None, currency_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_rate=None, risk_allocation_rate=None, book_scope=None, depreciation_option=None, catalogue_status=None, created_by=None, approved_by=None):
        # search
        self.mortgage_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('MTG-Catalogue Definition-View')
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if collateral_asset_type:
            self.bo_assert_select('Collateral asset type', collateral_asset_type)
        if collateral_asset_classification:
            self.bo_assert_select('Collateral asset classification', collateral_asset_classification)
        if collateral_rate:
            self.bo_assert_value('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.bo_assert_value('Risk allocation rate', risk_allocation_rate)
        if book_scope:
            self.bo_assert_select('Book scope', book_scope)
        if depreciation_option:
            self.bo_assert_select('Depreciation option', depreciation_option)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)

    def mortgage_catalogue_definition_update(self, catalogue_code=None, catalogue_name=None, currency_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_rate=None, risk_allocation_rate=None, book_scope=None, depreciation_option=None, catalogue_status=None, created_by=None, approved_by=None, list_error_message=None):
        # view
        self.mortgage_catalogue_definition_view(catalogue_code=catalogue_code)
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
        if collateral_asset_type:
            self.bo_select('Collateral asset type', collateral_asset_type)
        self.key_escape()
        if collateral_asset_classification:
            self.bo_select('Collateral asset classification', collateral_asset_classification)
        if collateral_rate:
            self.bo_write_number('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.bo_write_number('Risk allocation rate', risk_allocation_rate)
        self.key_escape()
        if book_scope:
            self.bo_select('Book scope', book_scope)
        self.key_escape()
        if depreciation_option:
            self.bo_select('Depreciation option', depreciation_option)
        self.key_escape()
        if catalogue_status:
            self.bo_select('Catalogue status', catalogue_status)
        # assert value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
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
            catalogue_code_out=self.bo_get_value('Catalogue Code')
            print(f'Catalogue Code: {catalogue_code_out}')
            return catalogue_code_out

    def mortgage_catalogue_definition_delete(self, catalogue_code, list_error_message=None, expected_message=None):
        # search
        self.mortgage_catalogue_definition_simple_search(catalogue_code)
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

    # MTG-Account Information
    def mortgage_account_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Collateral', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('MTG-Account Information-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def mortgage_account_advanced_search(self, account_number=None, account_name=None, currency=None, customer_code=None, catalogue_code=None, collateral_type=None, classification=None, status=None, old_a_c_no=None):
        self.close_all_form()
        self.click_menu('Collateral', 'Account Information')
        self.wait_for_button_available('Search')
        self.assert_form_title('MTG-Account Information-Search')
        if account_number:
            self.adv_search_text('Account number', str(account_number).replace('-', ''))
        if account_name:
            self.adv_search_text('Account name', account_name)
        if currency:
            self.adv_search_text('Currency', currency)
        if customer_code:
            self.adv_search('Customer code', str(customer_code).replace('-', ''))
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        self.key_escape()
        if collateral_type:
            self.adv_search_select('Collateral type', collateral_type)
        self.key_escape()
        if classification:
            self.adv_search_select('Classification', classification)
        self.key_escape()
        if status:
            self.adv_search_select('Status', status)
        if old_a_c_no:
            self.adv_search_text('Old a/c no', old_a_c_no)
        self.click_button_search_advanced()
        self.wait_loading()

    def mortgage_account_view(self, account_number, account_name=None, cc_contract=None, currency_code=None, book_currency_code=None, account_holder_type=None, customer_code=None, branch_code=None, collateral_account_status=None, catalogue_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_rate=None, risk_allocation_rate=None, book_scope=None, depreciation_option=None, was_register_at_collateral_center=None, security_paper_type=None, reference_number=None, name_of_title=None, house_no=None, plot_no=None, holding_no=None, ward_no=None, block_no=None, area_acre=None, street=None, township=None, division_city=None, location=None, legal_local_address=None, local_address=None, evaluate_by=None, evaluate_method=None, evaluate_date=None, new_evaluate_date=None, insurance_name=None, open_date=None, insurance_expiry_date=None, close_date=None, last_transaction_date=None, created_by=None, approved_by=None, account_manager_staff_id=None, other_paper_type=None, other_paper_no=None, collateral_asset_value=None, market_value=None, forced_sale_value=None, current_secure_amount=None, cc_amount=None, loan_to_fsv=None, released_collateral_amount=None, keeping_amount=None, keeping_release_amount=None, other_counter_party_collateral_amount=None, other_counter_party_collateral_released=None, sum_insurance_amount=None, premium_amount=None, original_amount_price=None, accumulate_of_depreciation_amount=None, net_book_value_after_depreciation=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quarter_debit=None, quarter_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, remark=None, reference_id=None, owner=None, user_define_1=None, user_define_2=None, user_define_3=None, user_define_4=None, user_define_5=None, policy_number=None, expiry_date=None, policy_amount=None, company_issues_policy=None):
        # search mortgage account
        self.mortgage_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, str(account_number).replace('-', ''))
        if account_name:
            self.assert_table_data('Account name', 1, account_name)
        if currency_code:
            self.assert_table_data('Currency', 1, currency_code)
        if collateral_account_status:
            self.assert_table_data('Status', 1, collateral_account_status)
        if catalogue_code:
            self.assert_table_data('Catalogue code', 1, catalogue_code)
        if customer_code:
            self.assert_table_data('Customer code', 1, self.customer_code_mask(customer_code))
        if collateral_asset_type:
            self.assert_table_data('Collateral type', 1, collateral_asset_type)
        if collateral_asset_classification:
            self.assert_table_data('Classification', 1, collateral_asset_classification)
        # view mortgage account
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('MTG-Account Information-View')
        # verify value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_text('Account code', self.no_mask(account_number))
        if account_name:
            self.bo_assert_text('Account name', account_name)
        if cc_contract:
            self.bo_assert_text('CC contract', cc_contract)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if book_currency_code:
            self.bo_assert_select('Book currency code', book_currency_code)
        if account_holder_type:
            self.bo_assert_select('Account holder type', account_holder_type)
        if customer_code:
            self.bo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if branch_code:
            self.bo_assert_text('Branch code', branch_code)
        if collateral_account_status:
            self.bo_assert_select('Collateral account status', collateral_account_status)
        if catalogue_code:
            self.bo_assert_text_group('Catalogue code', catalogue_code)
        if collateral_asset_type:
            self.bo_assert_select('Collateral asset type', collateral_asset_type)
        if collateral_asset_classification:
            self.bo_assert_select('Collateral asset classification', collateral_asset_classification)
        if collateral_rate:
            self.bo_assert_value('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.bo_assert_value('Risk allocation rate', risk_allocation_rate)
        if book_scope:
            self.bo_assert_select('Book scope', book_scope)
        if depreciation_option:
            self.bo_assert_select('Depreciation option', depreciation_option)
        if was_register_at_collateral_center:
            self.bo_assert_select('Was register at collateral center', was_register_at_collateral_center)
        if security_paper_type:
            self.bo_assert_select('Security paper type', security_paper_type)
        if reference_number:
            self.bo_assert_text('Reference number', reference_number)
        if name_of_title:
            self.bo_click_collap('Other address')
            self.bo_assert_text_multi('Other address', 'Name of title', name_of_title)
        if house_no:
            self.bo_click_collap('Other address')
            self.bo_assert_text_multi('Other address', 'House no', house_no)
        if plot_no:
            self.bo_click_collap('Other address')
            self.bo_assert_text_multi('Other address', 'Plot no', plot_no)
        if holding_no:
            self.bo_click_collap('Other address')
            self.bo_assert_text_multi('Other address', 'Holding no', holding_no)
        if ward_no:
            self.bo_click_collap('Other address')
            self.bo_assert_text_multi('Other address', 'Ward no', ward_no)
        if block_no:
            self.bo_click_collap('Other address')
            self.bo_assert_text_multi('Other address', 'Block no', block_no)
        if area_acre:
            self.bo_click_collap('Other address')
            self.bo_assert_text_multi('Other address', 'Area (acre)', area_acre)
        if street:
            self.bo_click_collap('Other address')
            self.bo_assert_text_multi('Other address', 'Street', street)
        if township:
            self.bo_click_collap('Other address')
            self.bo_assert_text_multi('Other address', 'Township', township)
        if division_city:
            self.bo_click_collap('Other address')
            self.bo_assert_text_multi('Other address', 'Division, city', division_city)
        if location:
            self.bo_assert_select('Location', location)
        if legal_local_address:
            self.bo_assert_text('Legal local address', legal_local_address)
        if local_address:
            self.bo_assert_text('Local address', local_address)
        if evaluate_by:
            self.bo_assert_text('Evaluate by', evaluate_by)
        if evaluate_method:
            self.bo_assert_select('Evaluate method', evaluate_method)
        if evaluate_date:
            self.bo_assert_date('Evaluate date', evaluate_date)
        if new_evaluate_date:
            self.bo_assert_date('New evaluate date', new_evaluate_date)
        if insurance_name:
            self.bo_assert_text('Insurance Name', insurance_name)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if insurance_expiry_date:
            self.bo_assert_text('Insurance Expiry Date', insurance_expiry_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if account_manager_staff_id:
            self.bo_assert_text_group('Account manager staff id', account_manager_staff_id)
        self.bo_click_tab('Other paper information')
        if other_paper_type:
            self.bo_assert_select('Other paper type', other_paper_type)
        if other_paper_no:
            self.bo_assert_text('Other paper no', other_paper_no)
        self.bo_click_tab('Outstanding information')
        if collateral_asset_value:
            self.bo_assert_value('Collateral asset value', collateral_asset_value)
        if market_value:
            self.bo_assert_value('Market value', market_value)
        if forced_sale_value:
            self.bo_assert_value('Forced sale value', forced_sale_value)
        if current_secure_amount:
            self.bo_assert_value('Current secure amount', current_secure_amount)
        if cc_amount:
            self.bo_assert_value('CC amount', cc_amount)
        if loan_to_fsv:
            self.bo_assert_value('Loan to FSV (%)', loan_to_fsv)
        if released_collateral_amount:
            self.bo_assert_value('Released collateral amount', released_collateral_amount)
        if keeping_amount:
            self.bo_assert_value('Keeping amount', keeping_amount)
        if keeping_release_amount:
            self.bo_assert_value('Keeping release amount', keeping_release_amount)
        if other_counter_party_collateral_amount:
            self.bo_assert_value('Other counter party collateral amount', other_counter_party_collateral_amount)
        if other_counter_party_collateral_released:
            self.bo_assert_value('Other counter party collateral released', other_counter_party_collateral_released)
        if sum_insurance_amount:
            self.bo_assert_value('Sum insurance amount', sum_insurance_amount)
        if premium_amount:
            self.bo_assert_value('Premium amount', premium_amount)
        if original_amount_price:
            self.bo_assert_value('Original amount/price', original_amount_price)
        if accumulate_of_depreciation_amount:
            self.bo_assert_value('Accumulate of depreciation amount', accumulate_of_depreciation_amount)
        if net_book_value_after_depreciation:
            self.bo_assert_value('Net book value after depreciation', net_book_value_after_depreciation)
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
        self.bo_click_tab('Addition information')
        if remark:
            self.bo_assert_text('Remark', remark)
        if reference_id:
            self.bo_assert_text('Reference id', reference_id)
        if owner:
            self.bo_assert_text('Owner', owner)
        if user_define_1:
            self.bo_assert_text('User define 1', user_define_1)
        if user_define_2:
            self.bo_assert_text('User define 2', user_define_2)
        if user_define_3:
            self.bo_assert_text('User define 3', user_define_3)
        if user_define_4:
            self.bo_assert_text('User define 4', user_define_4)
        if user_define_5:
            self.bo_assert_text('User define 5', user_define_5)
        if policy_number:
            self.bo_assert_text('Policy number', policy_number)
        if expiry_date:
            self.bo_assert_date('Expiry date', expiry_date)
        if policy_amount:
            self.bo_assert_value('Policy Amount', policy_amount)
        if company_issues_policy:
            self.bo_assert_text('Company issues policy', company_issues_policy)

    def mortgage_account_update(self, account_number=None, account_name=None, cc_contract=None, currency_code=None, book_currency_code=None, account_holder_type=None, customer_code=None, branch_code=None, collateral_account_status=None, catalogue_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_rate=None, risk_allocation_rate=None, book_scope=None, depreciation_option=None, was_register_at_collateral_center=None, security_paper_type=None, reference_number=None, name_of_title=None, house_no=None, plot_no=None, holding_no=None, ward_no=None, block_no=None, area_acre=None, street=None, township=None, division_city=None, location=None, legal_local_address=None, local_address=None, evaluate_by=None, evaluate_method=None, evaluate_date=None, new_evaluate_date=None, insurance_name=None, open_date=None, insurance_expiry_date=None, close_date=None, last_transaction_date=None, created_by=None, approved_by=None, account_manager_staff_id=None, other_paper_type=None, other_paper_no=None, collateral_asset_value=None, market_value=None, forced_sale_value=None, current_secure_amount=None, cc_amount=None, loan_to_fsv=None, released_collateral_amount=None, keeping_amount=None, keeping_release_amount=None, other_counter_party_collateral_amount=None, other_counter_party_collateral_released=None, sum_insurance_amount=None, premium_amount=None, original_amount_price=None, accumulate_of_depreciation_amount=None, net_book_value_after_depreciation=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quarter_debit=None, quarter_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, remark=None, reference_id=None, owner=None, user_define_1=None, user_define_2=None, user_define_3=None, user_define_4=None, user_define_5=None, policy_number=None, expiry_date=None, policy_amount=None, company_issues_policy=None, list_error_message=None):
        # view
        self.mortgage_account_view(account_number=account_number)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if account_name:
            self.bo_write_text('Account name', account_name)
        if cc_contract:
            self.bo_write_text('CC contract', cc_contract)
        if collateral_rate:
            self.bo_write_number('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.bo_write_number('Risk allocation rate', risk_allocation_rate)
        self.key_escape()
        if was_register_at_collateral_center:
            self.bo_select('Was register at collateral center', was_register_at_collateral_center)
        self.key_escape()
        if security_paper_type:
            self.bo_select('Security paper type', security_paper_type)
        if reference_number:
            self.bo_write_text('Reference number', reference_number)
        if name_of_title:
            self.bo_click_collap('Other address')
            self.bo_write_text_multi('Other address', 'Name of title', name_of_title)
        if house_no:
            self.bo_click_collap('Other address')
            self.bo_write_text_multi('Other address', 'House no', house_no)
        if plot_no:
            self.bo_click_collap('Other address')
            self.bo_write_text_multi('Other address', 'Plot no', plot_no)
        if holding_no:
            self.bo_click_collap('Other address')
            self.bo_write_text_multi('Other address', 'Holding no', holding_no)
        if ward_no:
            self.bo_click_collap('Other address')
            self.bo_write_text_multi('Other address', 'Ward no', ward_no)
        if block_no:
            self.bo_click_collap('Other address')
            self.bo_write_text_multi('Other address', 'Block no', block_no)
        if area_acre:
            self.bo_click_collap('Other address')
            self.bo_write_text_multi('Other address', 'Area (acre)', area_acre)
        if street:
            self.bo_click_collap('Other address')
            self.bo_write_text_multi('Other address', 'Street', street)
        if township:
            self.bo_click_collap('Other address')
            self.bo_write_text_multi('Other address', 'Township', township)
        if division_city:
            self.bo_click_collap('Other address')
            self.bo_write_text_multi('Other address', 'Division, city', division_city)
        self.key_escape()
        if location:
            self.bo_select('Location', location)
        if legal_local_address:
            self.bo_write_text('Legal local address', legal_local_address)
        if local_address:
            self.bo_write_text('Local address', local_address)
        if evaluate_by:
            self.bo_write_text('Evaluate by', evaluate_by)
        self.key_escape()
        if evaluate_method:
            self.bo_select('Evaluate method', evaluate_method)
        if evaluate_date:
            self.bo_write_date('Evaluate date', evaluate_date)
        if new_evaluate_date:
            self.bo_write_date('New evaluate date', new_evaluate_date)
        if insurance_name:
            self.bo_write_text('Insurance Name', insurance_name)
        if insurance_expiry_date:
            self.bo_write_text('Insurance Expiry Date', insurance_expiry_date)
        self.bo_click_tab('Other paper information')
        self.key_escape()
        if other_paper_type:
            self.bo_select('Other paper type', other_paper_type)
        if other_paper_no:
            self.bo_write_text('Other paper no', other_paper_no)
        self.bo_click_tab('Outstanding information')
        if market_value:
            self.bo_write_number('Market value', market_value)
        if cc_amount:
            self.bo_write_number('CC amount', cc_amount)
        if other_counter_party_collateral_amount:
            self.bo_write_number('Other counter party collateral amount', other_counter_party_collateral_amount)
        if other_counter_party_collateral_released:
            self.bo_write_number('Other counter party collateral released', other_counter_party_collateral_released)
        if sum_insurance_amount:
            self.bo_write_number('Sum insurance amount', sum_insurance_amount)
        if premium_amount:
            self.bo_write_number('Premium amount', premium_amount)
        if original_amount_price:
            self.bo_write_number('Original amount/price', original_amount_price)
        self.bo_click_tab('Addition information')
        if remark:
            self.bo_write_text('Remark', remark)
        if reference_id:
            self.bo_write_text('Reference id', reference_id)
        if owner:
            self.bo_write_text('Owner', owner)
        if user_define_1:
            self.bo_write_text('User define 1', user_define_1)
        if user_define_2:
            self.bo_write_text('User define 2', user_define_2)
        if user_define_3:
            self.bo_write_text('User define 3', user_define_3)
        if user_define_4:
            self.bo_write_text('User define 4', user_define_4)
        if user_define_5:
            self.bo_write_text('User define 5', user_define_5)
        if policy_number:
            self.bo_write_text('Policy number', policy_number)
        if expiry_date:
            self.bo_write_date('Expiry date', expiry_date)
        if policy_amount:
            self.bo_write_number('Policy Amount', policy_amount)
        if company_issues_policy:
            self.bo_write_text('Company issues policy', company_issues_policy)
        # assert value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_text('Account code', self.no_mask(account_number))
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if book_currency_code:
            self.bo_assert_select('Book currency code', book_currency_code)
        if account_holder_type:
            self.bo_assert_select('Account holder type', account_holder_type)
        if customer_code:
            self.bo_assert_value_group('Customer code', self.customer_code_mask(customer_code))
        if branch_code:
            self.bo_assert_text('Branch code', branch_code)
        if collateral_account_status:
            self.bo_assert_select('Collateral account status', collateral_account_status)
        if catalogue_code:
            self.bo_assert_text_group('Catalogue code', catalogue_code)
        if collateral_asset_type:
            self.bo_assert_select('Collateral asset type', collateral_asset_type)
        if collateral_asset_classification:
            self.bo_assert_select('Collateral asset classification', collateral_asset_classification)
        if book_scope:
            self.bo_assert_select('Book scope', book_scope)
        if depreciation_option:
            self.bo_assert_select('Depreciation option', depreciation_option)
        if open_date:
            self.bo_assert_date('Open date', open_date)
        if close_date:
            self.bo_assert_date('Close date', close_date)
        if last_transaction_date:
            self.bo_assert_date('Last transaction date', last_transaction_date)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if account_manager_staff_id:
            self.bo_assert_text_group('Account manager staff id', account_manager_staff_id)
        self.bo_click_tab('Outstanding information')
        if collateral_asset_value:
            self.bo_assert_value('Collateral asset value', collateral_asset_value)
        if forced_sale_value:
            self.bo_assert_value('Forced sale value', forced_sale_value)
        if current_secure_amount:
            self.bo_assert_value('Current secure amount', current_secure_amount)
        if loan_to_fsv:
            self.bo_assert_value('Loan to FSV (%)', loan_to_fsv)
        if released_collateral_amount:
            self.bo_assert_value('Released collateral amount', released_collateral_amount)
        if keeping_amount:
            self.bo_assert_value('Keeping amount', keeping_amount)
        if keeping_release_amount:
            self.bo_assert_value('Keeping release amount', keeping_release_amount)
        if accumulate_of_depreciation_amount:
            self.bo_assert_value('Accumulate of depreciation amount', accumulate_of_depreciation_amount)
        if net_book_value_after_depreciation:
            self.bo_assert_value('Net book value after depreciation', net_book_value_after_depreciation)
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
            account_number_out=self.bo_get_text('Account code')
            print(f'Account code: {account_number_out}')
            return account_number_out

    def mortgage_account_delete(self, account_number, list_error_message=None):
        # search
        self.mortgage_account_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, str(account_number).replace('-', ''))
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
            self.mortgage_account_simple_search(str(account_number).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {account_number}')
            return account_number

# -------------------------- handle BO approval - MORTGAGE --------------------------
    # MTG-Catalogue Definition - Data Verification
    def mortgage_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_rate=None, risk_allocation_rate=None, book_scope=None, depreciation_option=None, catalogue_status=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='MTG-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if collateral_asset_type:
            self.bo_assert_select('Collateral asset type', collateral_asset_type)
        if collateral_asset_classification:
            self.bo_assert_select('Collateral asset classification', collateral_asset_classification)
        if collateral_rate:
            self.bo_assert_value('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.bo_assert_value('Risk allocation rate', risk_allocation_rate)
        if book_scope:
            self.bo_assert_select('Book scope', book_scope)
        if depreciation_option:
            self.bo_assert_select('Depreciation option', depreciation_option)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)

    def mortgage_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_rate=None, risk_allocation_rate=None, book_scope=None, depreciation_option=None, catalogue_status=None, created_by=None, approved_by=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='MTG-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if collateral_asset_type:
            self.bo_assert_select('Collateral asset type', collateral_asset_type)
        if collateral_asset_classification:
            self.bo_assert_select('Collateral asset classification', collateral_asset_classification)
        if collateral_rate:
            self.bo_assert_value('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.bo_assert_value('Risk allocation rate', risk_allocation_rate)
        if book_scope:
            self.bo_assert_select('Book scope', book_scope)
        if depreciation_option:
            self.bo_assert_select('Depreciation option', depreciation_option)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)

    def mortgage_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, currency=None, collateral_asset_type=None, classification=None, collateral_rate=None, status=None):
        # search and verify
        self.mortgage_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue name', 1, catalogue_name)
        if currency:
            self.assert_table_data('Currency', 1, currency)
        if collateral_asset_type:
            self.assert_table_data('Collateral asset type', 1, collateral_asset_type)
        if classification:
            self.assert_table_data('Classification', 1, classification)
        if collateral_rate:
            self.assert_table_data('Collateral rate', 1, collateral_rate)
        if status:
            self.assert_table_data('Status', 1, status)

