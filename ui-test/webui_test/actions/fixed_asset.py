from webui_test.case import *

class FixedAssetActions(TestCase):

# -------------------------- handle FO - FIXED ASSET --------------------------
    # FAC_OPN: FAC-Open New Fixed Asset
    def fac_opn(self, catalogue_code=None, sequence_number=None, fixed_asset_name=None, fixed_asset_group=None, provider_name=None, original_currency=None, original_price=None, booking_value=None, salvage_value_of_the_asset=None, branch_name=None, department_name=None, description=None, account_number=None, owner_of_this_fixed_asset=None, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, fixed_asset_life_time=None, life_time_unit=None, depreciation_rate=None, booking_currency=None, cross_rate=None, value_date=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('FAC_OPN', 'Open new fixed asset')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FAC-Open New Fixed Asset')
        # enter value
        if catalogue_code:
            self.fo_write('Catalogue code', catalogue_code)
        if fixed_asset_name:
            self.fo_write_text('Fixed asset name', fixed_asset_name)
        if fixed_asset_group:
            self.fo_write_text('Fixed asset group', fixed_asset_group)
        if provider_name:
            self.fo_write_text('Provider name', provider_name)
        self.key_escape()
        if original_currency:
            self.fo_select('Original Currency', original_currency)
        if original_price:
            self.fo_write_number('Original price', original_price)
        if booking_value:
            self.fo_write_number('Booking value', booking_value)
        self.key_escape()
        if branch_name:
            self.fo_select('Branch Name', branch_name)
        self.key_escape()
        if department_name:
            self.fo_select('Department Name', department_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if account_number:
            self.fo_assert_value_group('Account number', self.fixed_asset_account_number_mask(account_number))
        if owner_of_this_fixed_asset:
            self.fo_assert_select('Owner of this fixed asset', owner_of_this_fixed_asset)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if sequence_number:
            self.fo_assert_value('Sequence number', sequence_number)
        if fixed_asset_type:
            self.fo_assert_select('Fixed asset type', fixed_asset_type)
        if fixed_asset_classification:
            self.fo_assert_select('Fixed asset classification', fixed_asset_classification)
        if depreciation_method:
            self.fo_assert_select('Depreciation method', depreciation_method)
        if fixed_asset_life_time:
            self.fo_assert_value('Fixed asset life time', fixed_asset_life_time)
        if life_time_unit:
            self.fo_assert_select('Life time unit', life_time_unit)
        if depreciation_rate:
            self.fo_assert_value_group('Depreciation rate', depreciation_rate)
        if booking_currency:
            self.fo_assert_select('Booking currency', booking_currency)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if salvage_value_of_the_asset:
            self.fo_assert_value('Salvage value of the asset', salvage_value_of_the_asset)
        if value_date:
            self.fo_assert_date('Value date', value_date)
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
            print(f'Transaction references FAC_OPN: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def fac_opn_view(self, transaction_references, catalogue_code=None, sequence_number=None, fixed_asset_name=None, fixed_asset_group=None, provider_name=None, original_currency=None, original_price=None, booking_value=None, salvage_value_of_the_asset=None, branch_name=None, department_name=None, description=None, account_number=None, owner_of_this_fixed_asset=None, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, fixed_asset_life_time=None, life_time_unit=None, depreciation_rate=None, booking_currency=None, cross_rate=None, value_date=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FAC-Open New Fixed Asset')
        # compare value
        if catalogue_code:
            self.fo_assert_value('Catalogue code', catalogue_code)
        if sequence_number:
            self.fo_assert_value('Sequence number', sequence_number)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if fixed_asset_group:
            self.fo_assert_text('Fixed asset group', fixed_asset_group)
        if provider_name:
            self.fo_assert_text('Provider name', provider_name)
        if original_currency:
            self.fo_assert_select('Original Currency', original_currency)
        if original_price:
            self.fo_assert_value('Original price', original_price)
        if booking_value:
            self.fo_assert_value('Booking value', booking_value)
        if salvage_value_of_the_asset:
            self.fo_assert_value('Salvage value of the asset', salvage_value_of_the_asset)
        if branch_name:
            self.fo_assert_select('Branch Name', branch_name)
        if department_name:
            self.fo_assert_select('Department Name', department_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if account_number:
            self.fo_assert_value_group('Account number', self.fixed_asset_account_number_mask(account_number))
        if owner_of_this_fixed_asset:
            self.fo_assert_select('Owner of this fixed asset', owner_of_this_fixed_asset)
        if catalogue_name:
            self.fo_assert_text('Catalogue name', catalogue_name)
        if fixed_asset_type:
            self.fo_assert_select('Fixed asset type', fixed_asset_type)
        if fixed_asset_classification:
            self.fo_assert_select('Fixed asset classification', fixed_asset_classification)
        if depreciation_method:
            self.fo_assert_select('Depreciation method', depreciation_method)
        if fixed_asset_life_time:
            self.fo_assert_value('Fixed asset life time', fixed_asset_life_time)
        if life_time_unit:
            self.fo_assert_select('Life time unit', life_time_unit)
        if depreciation_rate:
            self.fo_assert_value_group('Depreciation rate', depreciation_rate)
        if booking_currency:
            self.fo_assert_select('Booking currency', booking_currency)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if value_date:
            self.fo_assert_date('Value date', value_date)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references FAC_OPN: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    def fac_opn_fields(self, check_disabled='Y'):
         # open form
        self.close_all_form()
        self.open_fo('FAC_OPN', 'Open new fixed asset')
        self.wait_for_button_available('Accept')
        field_names_disabled = [
            'Sequence number',
            'Salvage value of the asset',
            'Account number',
            'Owner of this fixed asset',
            'Catalogue name',
            'Fixed asset type',
            'Fixed asset classification',
            'Depreciation method',
            'Fixed asset life time',
            'Life time unit',
            'Booking currency',
            'Cross rate',
            'Value date',
        ]
        field_names_enabled = [
            'Catalogue code',
            'Fixed asset name',
            'Fixed asset group',
            'Depreciation rate',
            'Provider name',
            'Original Currency',
            'Original price',
            'Booking value',
            'Branch Name',
            'Department Name',
            'Description',
        ]
        if check_disabled == 'Y':
            self.verify_disabled_fields(field_names_disabled)
        if check_disabled == 'N':
            self.verify_enabled_fields(field_names_enabled)

    # FAC_PBC: FAC-Purchase Fixed Asset By Cash
    def fac_pbc(self, account_number=None, vendor_id=None, vendor_name=None, vendor_address=None, vendor_description=None, description=None, fixed_asset_name=None, original_currency=None, original_amount=None, cash_currency_book_cccy=None, cross_rate_at_time_open_fa=None, amount_in_cash=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('FAC_PBC', 'Purchase fixed asset by cash')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FAC-Purchase Fixed Asset By Cash')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if vendor_id:
            self.fo_write('Vendor id', str(vendor_id).replace('-', ''))
            self.wait_loading()
        if vendor_name:
            self.fo_write_text('Vendor name', vendor_name)
        if vendor_address:
            self.fo_write_text('Vendor address', vendor_address)
        if vendor_description:
            self.fo_write_text('Vendor description', vendor_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if original_currency:
            self.fo_assert_select('Original currency', original_currency)
        if original_amount:
            self.fo_assert_value('Original amount', original_amount)
        if cash_currency_book_cccy:
            self.fo_assert_select('Cash currency (book cccy)', cash_currency_book_cccy)
        if cross_rate_at_time_open_fa:
            self.fo_assert_value_group('Cross rate (At time open FA)', cross_rate_at_time_open_fa)
        if amount_in_cash:
            self.fo_assert_value('Amount in cash', amount_in_cash)
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
            print(f'Transaction references FAC_PBC: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def fac_pbc_view(self, transaction_references, account_number=None, vendor_id=None, vendor_name=None, vendor_address=None, vendor_description=None, description=None, fixed_asset_name=None, original_currency=None, original_amount=None, cash_currency_book_cccy=None, cross_rate_at_time_open_fa=None, amount_in_cash=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FAC-Purchase Fixed Asset By Cash')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.fixed_asset_account_number_mask(account_number))
        if vendor_id:
            self.fo_assert_value('Vendor id', vendor_id)
        if vendor_name:
            self.fo_assert_text('Vendor name', vendor_name)
        if vendor_address:
            self.fo_assert_text('Vendor address', vendor_address)
        if vendor_description:
            self.fo_assert_text('Vendor description', vendor_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if original_currency:
            self.fo_assert_select('Original currency', original_currency)
        if original_amount:
            self.fo_assert_value('Original amount', original_amount)
        if cash_currency_book_cccy:
            self.fo_assert_select('Cash currency (book cccy)', cash_currency_book_cccy)
        if cross_rate_at_time_open_fa:
            self.fo_assert_value_group('Cross rate (At time open FA)', cross_rate_at_time_open_fa)
        if amount_in_cash:
            self.fo_assert_value('Amount in cash', amount_in_cash)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references FAC_PBC: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # FAC_PBD: FAC-Purchase Fixed Asset By Deposit
    def fac_pbd(self, account_number=None, deposit_account=None, vendor_id=None, vendor_name=None, vendor_address=None, vendor_description=None, description=None, fixed_asset_name=None, original_currency=None, original_amount=None, deposit_currency=None, cross_rate=None, book_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('FAC_PBD', 'Purchase fixed asset by deposit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FAC-Purchase Fixed Asset By Deposit')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if deposit_account:
            self.fo_write_group('Deposit account', str(deposit_account).replace('-', ''))
            self.wait_loading()
        if vendor_id:
            self.fo_write('Vendor id', str(vendor_id).replace('-', ''))
        if vendor_name:
            self.fo_write_text('Vendor name', vendor_name)
        if vendor_address:
            self.fo_write_text('Vendor address', vendor_address)
        if vendor_description:
            self.fo_write_text('Vendor description', vendor_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if original_currency:
            self.fo_assert_select('Original currency', original_currency)
        if original_amount:
            self.fo_assert_value('Original amount', original_amount)
        if deposit_currency:
            self.fo_assert_select('Deposit currency', deposit_currency)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if book_amount:
            self.fo_assert_value('Book amount', book_amount)
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
            print(f'Transaction references FAC_PBD: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            deposit_account_out=self.fo_get_value_group('Deposit account')
            print(f'Deposit account: {deposit_account_out}')
            return transaction_references, account_number_out, deposit_account_out

    def fac_pbd_view(self, transaction_references, account_number=None, deposit_account=None, vendor_id=None, vendor_name=None, vendor_address=None, vendor_description=None, description=None, fixed_asset_name=None, original_currency=None, original_amount=None, deposit_currency=None, cross_rate=None, book_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FAC-Purchase Fixed Asset By Deposit')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.fixed_asset_account_number_mask(account_number))
        if deposit_account:
            self.fo_assert_value_group('Deposit account', self.deposit_account_number_mask(deposit_account))
        if vendor_id:
            self.fo_assert_value('Vendor id', vendor_id)
        if vendor_name:
            self.fo_assert_text('Vendor name', vendor_name)
        if vendor_address:
            self.fo_assert_text('Vendor address', vendor_address)
        if vendor_description:
            self.fo_assert_text('Vendor description', vendor_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if original_currency:
            self.fo_assert_select('Original currency', original_currency)
        if original_amount:
            self.fo_assert_value('Original amount', original_amount)
        if deposit_currency:
            self.fo_assert_select('Deposit currency', deposit_currency)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if book_amount:
            self.fo_assert_value('Book amount', book_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references FAC_PBD: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        deposit_account_out=self.fo_get_value_group('Deposit account')
        print(f'F8: Deposit account: {deposit_account_out}')
        return transaction_references, account_number_out, deposit_account_out

    # FAC_PBG: FAC-Purchase Fixed Asset By Accounting
    def fac_pbg(self, account_number=None, gl_account=None, vendor_id=None, vendor_name=None, vendor_address=None, vendor_description=None, description=None, fixed_asset_name=None, original_currency=None, original_amount=None, gl_currency=None, cross_rate=None, book_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('FAC_PBG', 'Purchase fixed asset by accounting')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FAC-Purchase Fixed Asset By Accounting')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if gl_account:
            self.fo_write_group('GL account', str(gl_account).replace('-', ''))
            self.wait_loading()
        if vendor_id:
            self.fo_write('Vendor id', str(vendor_id).replace('-', ''))
        if vendor_name:
            self.fo_write_text('Vendor name', vendor_name)
        if vendor_address:
            self.fo_write_text('Vendor address', vendor_address)
        if vendor_description:
            self.fo_write_text('Vendor description', vendor_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if original_currency:
            self.fo_assert_select('Original currency', original_currency)
        if original_amount:
            self.fo_assert_value('Original amount', original_amount)
        if gl_currency:
            self.fo_assert_select('GL Currency', gl_currency)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if book_amount:
            self.fo_assert_value('Book amount', book_amount)
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
            print(f'Transaction references FAC_PBG: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            gl_account_out=self.fo_get_value_group('GL account')
            print(f'GL account: {gl_account_out}')
            return transaction_references, account_number_out, gl_account_out

    def fac_pbg_view(self, transaction_references, account_number=None, gl_account=None, vendor_id=None, vendor_name=None, vendor_address=None, vendor_description=None, description=None, fixed_asset_name=None, original_currency=None, original_amount=None, gl_currency=None, cross_rate=None, book_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FAC-Purchase Fixed Asset By Accounting')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.fixed_asset_account_number_mask(account_number))
        if gl_account:
            self.fo_assert_value_group('GL account', self.gl_account_number_mask(gl_account))
        if vendor_id:
            self.fo_assert_value('Vendor id', vendor_id)
        if vendor_name:
            self.fo_assert_text('Vendor name', vendor_name)
        if vendor_address:
            self.fo_assert_text('Vendor address', vendor_address)
        if vendor_description:
            self.fo_assert_text('Vendor description', vendor_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if original_currency:
            self.fo_assert_select('Original currency', original_currency)
        if original_amount:
            self.fo_assert_value('Original amount', original_amount)
        if gl_currency:
            self.fo_assert_select('GL Currency', gl_currency)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if book_amount:
            self.fo_assert_value('Book amount', book_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references FAC_PBG: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        gl_account_out=self.fo_get_value_group('GL account')
        print(f'F8: GL account: {gl_account_out}')
        return transaction_references, account_number_out, gl_account_out

    # FAC_SBC: FAC-Selling Fixed Asset By Cash
    def fac_sbc(self, account_number=None, selling_amount=None, cross_rate=None, amount_in_cash=None, purchaser_id=None, purchaser_name=None, purchaser_address=None, purchaser_description=None, description=None, fixed_asset_name=None, net_book_value=None, acummulate_not_posted=None, acummulate_posted=None, book_value=None, book_currency=None, cash_currency=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('FAC_SBC', 'Selling fixed asset by cash')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FAC-Selling Fixed Asset By Cash')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if selling_amount:
            self.fo_write_number('Selling amount', selling_amount)
        if cross_rate:
            self.fo_write_number_group('Cross rate', cross_rate)
        if amount_in_cash:
            self.fo_write_number('Amount in cash', amount_in_cash)
        if purchaser_id:
            self.fo_write('Purchaser id', purchaser_id)
        if purchaser_name:
            self.fo_write_text('Purchaser name', purchaser_name)
        if purchaser_address:
            self.fo_write_text('Purchaser address', purchaser_address)
        if purchaser_description:
            self.fo_write_text('Purchaser description', purchaser_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if net_book_value:
            self.fo_assert_value('Net book value', net_book_value)
        if acummulate_not_posted:
            self.fo_assert_value('Acummulate not posted', acummulate_not_posted)
        if acummulate_posted:
            self.fo_assert_value('Acummulate posted', acummulate_posted)
        if book_value:
            self.fo_assert_value('Book value', book_value)
        if book_currency:
            self.fo_assert_select('Book currency', book_currency)
        if cash_currency:
            self.fo_assert_select('Cash currency', cash_currency)
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
            print(f'Transaction references FAC_SBC: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def fac_sbc_view(self, transaction_references, account_number=None, selling_amount=None, cross_rate=None, amount_in_cash=None, purchaser_id=None, purchaser_name=None, purchaser_address=None, purchaser_description=None, description=None, fixed_asset_name=None, net_book_value=None, acummulate_not_posted=None, acummulate_posted=None, book_value=None, book_currency=None, cash_currency=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FAC-Selling Fixed Asset By Cash')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.fixed_asset_account_number_mask(account_number))
        if selling_amount:
            self.fo_assert_value('Selling amount', selling_amount)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if amount_in_cash:
            self.fo_assert_value('Amount in cash', amount_in_cash)
        if purchaser_id:
            self.fo_assert_value('Purchaser id', purchaser_id)
        if purchaser_name:
            self.fo_assert_text('Purchaser name', purchaser_name)
        if purchaser_address:
            self.fo_assert_text('Purchaser address', purchaser_address)
        if purchaser_description:
            self.fo_assert_text('Purchaser description', purchaser_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if net_book_value:
            self.fo_assert_value('Net book value', net_book_value)
        if acummulate_not_posted:
            self.fo_assert_value('Acummulate not posted', acummulate_not_posted)
        if acummulate_posted:
            self.fo_assert_value('Acummulate posted', acummulate_posted)
        if book_value:
            self.fo_assert_value('Book value', book_value)
        if book_currency:
            self.fo_assert_select('Book currency', book_currency)
        if cash_currency:
            self.fo_assert_select('Cash currency', cash_currency)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references FAC_SBC: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

    # FAC_SBD: FAC-Selling Fixed Asset By Deposit
    def fac_sbd(self, account_number=None, selling_amount=None, debit_account=None, purchaser_id=None, purchaser_name=None, purchaser_address=None, purchaser_description=None, description=None, fixed_asset_name=None, net_book_value=None, acummulate_not_posted=None, acummulate_posted=None, book_value=None, book_currency=None, currency=None, cross_rate=None, debit_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('FAC_SBD', 'Selling fixed asset by deposit')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FAC-Selling Fixed Asset By Deposit')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if selling_amount:
            self.fo_write_number('Selling amount', selling_amount)
        if debit_account:
            self.fo_write_group('Debit account', str(debit_account).replace('-', ''))
            self.wait_loading()
        if purchaser_id:
            self.fo_write('Purchaser id', purchaser_id)
        if purchaser_name:
            self.fo_write_text('Purchaser name', purchaser_name)
        if purchaser_address:
            self.fo_write_text('Purchaser address', purchaser_address)
        if purchaser_description:
            self.fo_write_text('Purchaser description', purchaser_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if net_book_value:
            self.fo_assert_value('Net book value', net_book_value)
        if acummulate_not_posted:
            self.fo_assert_value('Acummulate not posted', acummulate_not_posted)
        if acummulate_posted:
            self.fo_assert_value('Acummulate posted', acummulate_posted)
        if book_value:
            self.fo_assert_value('Book value', book_value)
        if book_currency:
            self.fo_assert_select('Book currency', book_currency)
        if currency:
            self.fo_assert_select('Currency', currency)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if debit_amount:
            self.fo_assert_value('Debit amount', debit_amount)
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
            print(f'Transaction references FAC_SBD: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            debit_account_out=self.fo_get_value_group('Debit account')
            print(f'Debit account: {debit_account_out}')
            return transaction_references, account_number_out, debit_account_out

    def fac_sbd_view(self, transaction_references, account_number=None, selling_amount=None, debit_account=None, purchaser_id=None, purchaser_name=None, purchaser_address=None, purchaser_description=None, description=None, fixed_asset_name=None, net_book_value=None, acummulate_not_posted=None, acummulate_posted=None, book_value=None, book_currency=None, currency=None, cross_rate=None, debit_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FAC-Selling Fixed Asset By Deposit')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.fixed_asset_account_number_mask(account_number))
        if selling_amount:
            self.fo_assert_value('Selling amount', selling_amount)
        if debit_account:
            self.fo_assert_value_group('Debit account', self.deposit_account_number_mask(debit_account))
        if purchaser_id:
            self.fo_assert_value('Purchaser id', purchaser_id)
        if purchaser_name:
            self.fo_assert_text('Purchaser name', purchaser_name)
        if purchaser_address:
            self.fo_assert_text('Purchaser address', purchaser_address)
        if purchaser_description:
            self.fo_assert_text('Purchaser description', purchaser_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if net_book_value:
            self.fo_assert_value('Net book value', net_book_value)
        if acummulate_not_posted:
            self.fo_assert_value('Acummulate not posted', acummulate_not_posted)
        if acummulate_posted:
            self.fo_assert_value('Acummulate posted', acummulate_posted)
        if book_value:
            self.fo_assert_value('Book value', book_value)
        if book_currency:
            self.fo_assert_select('Book currency', book_currency)
        if currency:
            self.fo_assert_select('Currency', currency)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if debit_amount:
            self.fo_assert_value('Debit amount', debit_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references FAC_SBD: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        debit_account_out=self.fo_get_value_group('Debit account')
        print(f'F8: Debit account: {debit_account_out}')
        return transaction_references, account_number_out, debit_account_out

    # FAC_SBG: FAC-Selling Fixed Asset By Accounting
    def fac_sbg(self, account_number=None, selling_amount=None, debit_account=None, purchaser_id=None, purchaser_name=None, purchaser_address=None, purchaser_description=None, description=None, fixed_asset_name=None, net_book_value=None, acummulate_not_posted=None, acummulate_posted=None, book_value=None, book_currency=None, currency=None, cross_rate=None, debit_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('FAC_SBG', 'Selling fixed asset by accounting')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FAC-Selling Fixed Asset By Accounting')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if selling_amount:
            self.fo_write_number('Selling amount', selling_amount)
        if debit_account:
            self.fo_write_group('Debit account', str(debit_account).replace('-', ''))
            self.wait_loading()
        if purchaser_id:
            self.fo_write('Purchaser id', purchaser_id)
        if purchaser_name:
            self.fo_write_text('Purchaser name', purchaser_name)
        if purchaser_address:
            self.fo_write_text('Purchaser address', purchaser_address)
        if purchaser_description:
            self.fo_write_text('Purchaser description', purchaser_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if net_book_value:
            self.fo_assert_value('Net book value', net_book_value)
        if acummulate_not_posted:
            self.fo_assert_value('Acummulate not posted', acummulate_not_posted)
        if acummulate_posted:
            self.fo_assert_value('Acummulate posted', acummulate_posted)
        if book_value:
            self.fo_assert_value('Book value', book_value)
        if book_currency:
            self.fo_assert_select('Book currency', book_currency)
        if currency:
            self.fo_assert_select('Currency', currency)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if debit_amount:
            self.fo_assert_value('Debit amount', debit_amount)
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
            print(f'Transaction references FAC_SBG: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            debit_account_out=self.fo_get_value_group('Debit account')
            print(f'Debit account: {debit_account_out}')
            return transaction_references, account_number_out, debit_account_out

    def fac_sbg_view(self, transaction_references, account_number=None, selling_amount=None, debit_account=None, purchaser_id=None, purchaser_name=None, purchaser_address=None, purchaser_description=None, description=None, fixed_asset_name=None, net_book_value=None, acummulate_not_posted=None, acummulate_posted=None, book_value=None, book_currency=None, currency=None, cross_rate=None, debit_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FAC-Selling Fixed Asset By Accounting')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.fixed_asset_account_number_mask(account_number))
        if selling_amount:
            self.fo_assert_value('Selling amount', selling_amount)
        if debit_account:
            self.fo_assert_value_group('Debit account', self.gl_account_number_mask(debit_account))
        if purchaser_id:
            self.fo_assert_value('Purchaser id', purchaser_id)
        if purchaser_name:
            self.fo_assert_text('Purchaser name', purchaser_name)
        if purchaser_address:
            self.fo_assert_text('Purchaser address', purchaser_address)
        if purchaser_description:
            self.fo_assert_text('Purchaser description', purchaser_description)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if net_book_value:
            self.fo_assert_value('Net book value', net_book_value)
        if acummulate_not_posted:
            self.fo_assert_value('Acummulate not posted', acummulate_not_posted)
        if acummulate_posted:
            self.fo_assert_value('Acummulate posted', acummulate_posted)
        if book_value:
            self.fo_assert_value('Book value', book_value)
        if book_currency:
            self.fo_assert_select('Book currency', book_currency)
        if currency:
            self.fo_assert_select('Currency', currency)
        if cross_rate:
            self.fo_assert_value_group('Cross rate', cross_rate)
        if debit_amount:
            self.fo_assert_value('Debit amount', debit_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references FAC_SBG: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        debit_account_out=self.fo_get_value_group('Debit account')
        print(f'F8: Debit account: {debit_account_out}')
        return transaction_references, account_number_out, debit_account_out

    # FAC_TFB: FAC-Transfer Fixed Asset To Another Branch
    def fac_tfb(self, account_number=None, new_branch=None, new_department=None, description=None, fixed_asset_name=None, book_currency=None, net_book_amount=None, acummulate_not_posted=None, book_amount=None, new_account=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('FAC_TFB', 'Transfer fixed asset to another branch')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FAC-Transfer Fixed Asset To Another Branch')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if new_branch:
            self.fo_write_text('New branch', new_branch)
        self.key_escape()
        if new_department:
            self.fo_select('New department', new_department)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if book_currency:
            self.fo_assert_select('Book currency', book_currency)
        if net_book_amount:
            self.fo_assert_value('Net book amount', net_book_amount)
        if acummulate_not_posted:
            self.fo_assert_value('Acummulate not posted', acummulate_not_posted)
        if book_amount:
            self.fo_assert_value('Book amount', book_amount)
        if new_account:
            self.fo_assert_value_group('New account', self.fixed_asset_account_number_mask(new_account))
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
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
            print(f'Transaction references FAC_TFB: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            new_account_out=self.fo_get_value_group('New account')
            print(f'New account: {new_account_out}')
            return transaction_references, account_number_out, new_account_out

    def fac_tfb_view(self, transaction_references, account_number=None, new_branch=None, new_department=None, description=None, fixed_asset_name=None, book_currency=None, net_book_amount=None, acummulate_not_posted=None, book_amount=None, new_account=None, customer_code=None, customer_name=None, customer_address=None, customer_description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FAC-Transfer Fixed Asset To Another Branch')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.fixed_asset_account_number_mask(account_number))
        if new_branch:
            self.fo_assert_text('New branch', new_branch)
        if new_department:
            self.fo_assert_select('New department', new_department)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if book_currency:
            self.fo_assert_select('Book currency', book_currency)
        if net_book_amount:
            self.fo_assert_value('Net book amount', net_book_amount)
        if acummulate_not_posted:
            self.fo_assert_value('Acummulate not posted', acummulate_not_posted)
        if book_amount:
            self.fo_assert_value('Book amount', book_amount)
        if new_account:
            self.fo_assert_value_group('New account', self.fixed_asset_account_number_mask(new_account))
        if customer_code:
            self.fo_assert_value('Customer code', customer_code)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references FAC_TFB: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        new_account_out=self.fo_get_value_group('New account')
        print(f'F8: New account: {new_account_out}')
        return transaction_references, account_number_out, new_account_out

    # FAC_DEP: FAC-Adjust Fixed Asset Accumulate
    def fac_dep(self, fixasset_number=None, adjust_accumulate_amount=None, adjust_expense_amount=None, description=None, current_accumulate_amount=None, current_expense_amount=None, new_accumulate_amount=None, new_expense_amount=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('FAC_DEP', 'Adjust Fixed Asset Accumulate')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FAC-Adjust Fixed Asset Accumulate')
        # enter value
        if fixasset_number:
            self.fo_write_group('Fixasset number', str(fixasset_number).replace('-', ''))
            self.wait_loading()
        if adjust_accumulate_amount:
            self.fo_write_number('Adjust accumulate amount', adjust_accumulate_amount)
        if adjust_expense_amount:
            self.fo_write_number('Adjust expense amount', adjust_expense_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if current_accumulate_amount:
            self.fo_assert_value('Current accumulate amount ', current_accumulate_amount)
        if current_expense_amount:
            self.fo_assert_value('Current expense amount', current_expense_amount)
        if new_accumulate_amount:
            self.fo_assert_value('New accumulate amount', new_accumulate_amount)
        if new_expense_amount:
            self.fo_assert_value('New expense amount', new_expense_amount)
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
            print(f'Transaction references FAC_DEP: {transaction_references}')
            fixasset_number_out=self.fo_get_value_group('Fixasset number')
            print(f'Fixasset number: {fixasset_number_out}')
            return transaction_references, fixasset_number_out

    def fac_dep_view(self, transaction_references, fixasset_number=None, adjust_accumulate_amount=None, adjust_expense_amount=None, description=None, current_accumulate_amount=None, current_expense_amount=None, new_accumulate_amount=None, new_expense_amount=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FAC-Adjust Fixed Asset Accumulate')
        # compare value
        if fixasset_number:
            self.fo_assert_value_group('Fixasset number', self.fixed_asset_account_number_mask(fixasset_number))
        if adjust_accumulate_amount:
            self.fo_assert_value('Adjust accumulate amount', adjust_accumulate_amount)
        if adjust_expense_amount:
            self.fo_assert_value('Adjust expense amount', adjust_expense_amount)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if current_accumulate_amount:
            self.fo_assert_value('Current accumulate amount ', current_accumulate_amount)
        if current_expense_amount:
            self.fo_assert_value('Current expense amount', current_expense_amount)
        if new_accumulate_amount:
            self.fo_assert_value('New accumulate amount', new_accumulate_amount)
        if new_expense_amount:
            self.fo_assert_value('New expense amount', new_expense_amount)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references FAC_DEP: {transaction_references}')
        fixasset_number_out=self.fo_get_value_group('Fixasset number')
        print(f'F8: Fixasset number: {fixasset_number_out}')
        return transaction_references, fixasset_number_out

    # FAC_CLS: FAC-Close Fixedasset Account
    def fac_cls(self, account_number=None, description=None, fixed_asset_name=None, net_book_value=None, book_currency=None, acummulate_posted=None, book_value=None, customer_id=None, customer_name=None, customer_address=None, customer_description=None, ifc_codes=None, values=None, total_fee=None, approve_later=None, approve_on_form=None, username=None, password=None, reason=None, list_error_message=None, expected_posting=None):
        # open form
        self.close_all_form()
        self.open_fo('FAC_CLS', 'Close fixedasset account')
        self.wait_for_button_available('Accept')
        self.assert_form_title('FAC-Close Fixedasset Account')
        # enter value
        if account_number:
            self.fo_write_group('Account number', str(account_number).replace('-', ''))
            self.wait_loading()
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_write_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if net_book_value:
            self.fo_assert_value('Net book value', net_book_value)
        if book_currency:
            self.fo_assert_select('Book currency', book_currency)
        if acummulate_posted:
            self.fo_assert_value('Acummulate posted', acummulate_posted)
        if book_value:
            self.fo_assert_value('Book value', book_value)
        if customer_id:
            self.fo_assert_value('Customer id', customer_id)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
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
            print(f'Transaction references FAC_CLS: {transaction_references}')
            account_number_out=self.fo_get_value_group('Account number')
            print(f'Account number: {account_number_out}')
            return transaction_references, account_number_out

    def fac_cls_view(self, transaction_references, account_number=None, description=None, fixed_asset_name=None, net_book_value=None, book_currency=None, acummulate_posted=None, book_value=None, customer_id=None, customer_name=None, customer_address=None, customer_description=None, expected_posting=None):
        self.transaction_view(transaction_references, 'FAC-Close Fixedasset Account')
        # compare value
        if account_number:
            self.fo_assert_value_group('Account number', self.fixed_asset_account_number_mask(account_number))
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.fo_assert_text('Description', description)
        if fixed_asset_name:
            self.fo_assert_text('Fixed asset name', fixed_asset_name)
        if net_book_value:
            self.fo_assert_value('Net book value', net_book_value)
        if book_currency:
            self.fo_assert_select('Book currency', book_currency)
        if acummulate_posted:
            self.fo_assert_value('Acummulate posted', acummulate_posted)
        if book_value:
            self.fo_assert_value('Book value', book_value)
        if customer_id:
            self.fo_assert_value('Customer id', customer_id)
        if customer_name:
            self.fo_assert_text('Customer name', customer_name)
        if customer_address:
            self.fo_assert_text('Customer address', customer_address)
        if customer_description:
            self.fo_assert_text('Customer description', customer_description)
        if expected_posting:
            self.assert_posting_data(**expected_posting)
        transaction_references=self.assert_transaction_number_not_null()
        print(f'F8: Transaction references FAC_CLS: {transaction_references}')
        account_number_out=self.fo_get_value_group('Account number')
        print(f'F8: Account number: {account_number_out}')
        return transaction_references, account_number_out

# -------------------------- handle BO - FIXED ASSET --------------------------
    # FAC-Fixed Asset Catalogue Definition
    def fixed_asset_catalogue_definition_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Accounting', 'Utilities', 'Fixed Asset Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('FAC-Fixed Asset Catalogue Definition-Search')
        self.simple_search(text=text, placeholder='Search Text')
        self.wait_loading()

    def fixed_asset_catalogue_definition_advanced_search(self, catalogue_code=None, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalogue_status=None):
        self.close_all_form()
        self.click_menu('Accounting', 'Utilities', 'Fixed Asset Catalogue Definition')
        self.wait_for_button_available('Search')
        self.assert_form_title('FAC-Fixed Asset Catalogue Definition-Search')
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.adv_search_text('Catalogue name', catalogue_name)
        self.key_escape()
        if fixed_asset_type:
            self.adv_search_select('Fixed asset type', fixed_asset_type)
        self.key_escape()
        if fixed_asset_classification:
            self.adv_search_select('Fixed asset classification', fixed_asset_classification)
        self.key_escape()
        if depreciation_method:
            self.adv_search_select('Depreciation method', depreciation_method)
        self.key_escape()
        if catalogue_status:
            self.adv_search_select('Catalogue status', catalogue_status)
        self.click_button_search_advanced()
        self.wait_loading()

    def fixed_asset_catalogue_definition_add(self, catalogue_code=None, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalogue_status=None, fixed_asset_life_time=None, life_time_unit=None, sys_account_names=None, coa_accounts=None, account_aliass=None, list_error_message=None):
        # open form
        self.close_all_form()
        self.click_menu('Accounting', 'Utilities', 'Fixed Asset Catalogue Definition')
        self.wait_for_button_available('Add')
        self.click_button('Add')
        self.wait_for_button_available('Save')
        self.assert_form_title('FAC-Fixed Asset Catalogue Definition-Add')
        # enter value
        self.bo_click_tab('General Information')
        if catalogue_code:
            self.bo_write('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_write_text('Catalogue Name', catalogue_name)
        self.key_escape()
        if fixed_asset_type:
            self.bo_select('Fixed Asset Type', fixed_asset_type)
        self.key_escape()
        if fixed_asset_classification:
            self.bo_select('Fixed Asset Classification', fixed_asset_classification)
        self.key_escape()
        if depreciation_method:
            self.bo_select('Depreciation Method', depreciation_method)
        self.key_escape()
        if catalogue_status:
            self.bo_select('Catalogue Status', catalogue_status)
        if fixed_asset_life_time:
            self.bo_write('Fixed asset life time', fixed_asset_life_time)
        if life_time_unit:
            self.bo_select('Life time unit', life_time_unit)
        # assert value
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
            self.bo_click_tab('General Information')
            catalogue_code_out=self.bo_get_value('Catalogue Code')
            print(f'Catalogue Code: {catalogue_code_out}')
            return catalogue_code_out

    def fixed_asset_catalogue_definition_view(self, catalogue_code=None, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalogue_status=None, fixed_asset_life_time=None, life_time_unit=None, created_by=None, approve_by=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None):
        # search
        self.fixed_asset_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue Code', 1, catalogue_code)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('FAC-Fixed Asset Catalogue Definition-View')
        # verify value
        self.bo_click_tab('General Information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue Name', catalogue_name)
        if fixed_asset_type:
            self.bo_assert_select('Fixed Asset Type', fixed_asset_type)
        if fixed_asset_classification:
            self.bo_assert_select('Fixed Asset Classification', fixed_asset_classification)
        if depreciation_method:
            self.bo_assert_select('Depreciation Method', depreciation_method)
        if catalogue_status:
            self.bo_assert_select('Catalogue Status', catalogue_status)
        if fixed_asset_life_time:
            self.bo_assert_value('Fixed asset life time', fixed_asset_life_time)
        if life_time_unit:
            self.bo_assert_select('Life time unit', life_time_unit)
        if created_by:
            self.bo_assert_text_group('Created By', created_by)
        if approve_by:
            self.bo_assert_text_group('Approve By', approve_by)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)

    def fixed_asset_catalogue_definition_update(self, catalogue_code=None, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalogue_status=None, fixed_asset_life_time=None, life_time_unit=None, created_by=None, approve_by=None, sys_account_names=None, coa_accounts=None, account_aliass=None, list_error_message=None):
        # view
        self.fixed_asset_catalogue_definition_view(catalogue_code=catalogue_code)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General Information')
        if catalogue_name:
            self.bo_write_text('Catalogue Name', catalogue_name)
        self.key_escape()
        if fixed_asset_type:
            self.bo_select('Fixed Asset Type', fixed_asset_type)
        self.key_escape()
        if fixed_asset_classification:
            self.bo_select('Fixed Asset Classification', fixed_asset_classification)
        self.key_escape()
        if depreciation_method:
            self.bo_select('Depreciation Method', depreciation_method)
        self.key_escape()
        if catalogue_status:
            self.bo_select('Catalogue Status', catalogue_status)
        if fixed_asset_life_time:
            self.bo_write_number('Fixed asset life time', fixed_asset_life_time)
        self.key_escape()
        if life_time_unit:
            self.bo_select('Life time unit', life_time_unit)
        # assert value
        self.bo_click_tab('General Information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if created_by:
            self.bo_assert_text_group('Created By', created_by)
        if approve_by:
            self.bo_assert_text_group('Approve By', approve_by)
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
            self.bo_click_tab('General Information')
            catalogue_code_out=self.bo_get_value('Catalogue Code')
            print(f'Catalogue Code: {catalogue_code_out}')
            return catalogue_code_out

    def fixed_asset_catalogue_definition_delete(self, catalogue_code, list_error_message=None, expected_message=None):
        # search
        self.fixed_asset_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue Code', 1, catalogue_code)
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

    # FAC-Fixed Asset And Tool
    def fixed_asset_and_tool_simple_search(self, text):
        self.close_all_form()
        self.click_menu('Accounting', 'Utilities', 'Fixed Asset And Tool')
        self.wait_for_button_available('Search')
        self.assert_form_title('FAC-Fixed Asset And Tool-Search')
        self.simple_search(text=text, placeholder='Search text')
        self.wait_loading()

    def fixed_asset_and_tool_advanced_search(self, account_number=None, account_name=None, book_currency=None, catalogue_code=None, fixed_asset_type=None, fixed_asset_status=None, branch_name=None, department_name=None, original_price_from=None, original_price_to=None):
        self.close_all_form()
        self.click_menu('Accounting', 'Utilities', 'Fixed Asset And Tool')
        self.wait_for_button_available('Search')
        self.assert_form_title('FAC-Fixed Asset And Tool-Search')
        if account_number:
            self.adv_search_text('Account number', str(account_number).replace('-', ''))
        if account_name:
            self.adv_search_text('Account name', account_name)
        if book_currency:
            self.adv_search_text('Book currency', book_currency)
        if catalogue_code:
            self.adv_search_text('Catalogue code', catalogue_code)
        self.key_escape()
        if fixed_asset_type:
            self.adv_search_select('Fixed asset type', fixed_asset_type)
        self.key_escape()
        if fixed_asset_status:
            self.adv_search_select('Fixed asset status', fixed_asset_status)
        self.key_escape()
        if branch_name:
            self.adv_search_select('Branch Name', branch_name)
        self.key_escape()
        if department_name:
            self.adv_search_select('Department Name', department_name)
        if original_price_from:
            self.adv_search('Original price from', original_price_from)
        if original_price_to:
            self.adv_search('Original price to', original_price_to)
        self.click_button_search_advanced()
        self.wait_loading()

    def fixed_asset_and_tool_view(self, account_number=None, fixed_asset_name=None, booking_currency_code=None, branch_name=None, reference_number=None, department_name=None, catalogue_code=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, life_time_unit=None, fixed_asset_life_time=None, provider_name=None, owner_fixed_asset=None, currency_code=None, status=None, created_by=None, approved_by=None, date_available_use=None, depreciation_rate=None, original_price=None, book_amount=None, net_book_value=None, accummulate_amount=None, expense_amount=None, insurrance_value=None, insurrance_fee_value=None, salvage_value_of_the_asset=None, income_amount_for_this_asset=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quater_debit=None, quater_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, expected_account_gl_names=None, expected_account_gl_numbers=None):
        # search
        self.fixed_asset_and_tool_simple_search(str(account_number).replace('-', ''))
        self.assert_table_data('Account number', 1, str(account_number).replace('-', ''))
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('FAC-Fixed Asset And Tool-View')
        # verify value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_text('Account number', str(account_number).replace('-', ''))
        if fixed_asset_name:
            self.bo_assert_text('Fixed asset name', fixed_asset_name)
        if booking_currency_code:
            self.bo_assert_select('Booking currency code', booking_currency_code)
        if branch_name:
            self.bo_assert_select('Branch name', branch_name)
        if reference_number:
            self.bo_assert_text('Reference number', reference_number)
        if department_name:
            self.bo_assert_select('Department name', department_name)
        if catalogue_code:
            self.bo_assert_text_group('Catalogue code', catalogue_code)
        if fixed_asset_type:
            self.bo_assert_select('Fixed asset type', fixed_asset_type)
        if fixed_asset_classification:
            self.bo_assert_select('Fixed asset classification', fixed_asset_classification)
        if depreciation_method:
            self.bo_assert_select('Depreciation method', depreciation_method)
        if life_time_unit:
            self.bo_assert_select('Life time unit', life_time_unit)
        if fixed_asset_life_time:
            self.bo_assert_value('Fixed asset life time', fixed_asset_life_time)
        if provider_name:
            self.bo_assert_text('Provider name', provider_name)
        if owner_fixed_asset:
            self.bo_assert_select('Owner fixed asset', owner_fixed_asset)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if status:
            self.bo_assert_select('Status', status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if date_available_use:
            self.bo_assert_date('Date available use', date_available_use)
        self.bo_click_tab('Outstanding information')
        if depreciation_rate:
            self.bo_assert_value('Depreciation rate', depreciation_rate)
        if original_price:
            self.bo_assert_value('Original price', original_price)
        if book_amount:
            self.bo_assert_value('Book amount', book_amount)
        if net_book_value:
            self.bo_assert_value('Net book value', net_book_value)
        if accummulate_amount:
            self.bo_assert_value('Accummulate amount', accummulate_amount)
        if expense_amount:
            self.bo_assert_value('Expense amount', expense_amount)
        if insurrance_value:
            self.bo_assert_value('Insurrance value', insurrance_value)
        if insurrance_fee_value:
            self.bo_assert_value('Insurrance fee value', insurrance_fee_value)
        if salvage_value_of_the_asset:
            self.bo_assert_value('Salvage value of the asset', salvage_value_of_the_asset)
        if income_amount_for_this_asset:
            self.bo_assert_value('Income amount for this asset', income_amount_for_this_asset)
        if week_debit:
            self.bo_assert_value('Week debit', week_debit)
        if week_credit:
            self.bo_assert_value('Week credit', week_credit)
        if month_debit:
            self.bo_assert_value('Month debit', month_debit)
        if month_credit:
            self.bo_assert_value('Month credit', month_credit)
        if quater_debit:
            self.bo_assert_value('Quater debit', quater_debit)
        if quater_credit:
            self.bo_assert_value('Quater credit', quater_credit)
        if semi_annual_debit:
            self.bo_assert_value('Semi-annual debit', semi_annual_debit)
        if semi_annual_credit:
            self.bo_assert_value('Semi-annual credit', semi_annual_credit)
        if year_debit:
            self.bo_assert_value('Year debit', year_debit)
        if year_credit:
            self.bo_assert_value('Year credit', year_credit)
        self.bo_click_tab('Account GLs Information')
        if expected_account_gl_names:
            for account_gl_name, account_gl_number in zip(expected_account_gl_names, expected_account_gl_numbers):
                self.bo_assert_text_table_account_gls(account_gl_name, str(account_gl_number).replace('-',''))

    def fixed_asset_and_tool_update(self, account_number=None, fixed_asset_name=None, booking_currency_code=None, branch_name=None, reference_number=None, department_name=None, catalogue_code=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, life_time_unit=None, fixed_asset_life_time=None, provider_name=None, owner_fixed_asset=None, currency_code=None, status=None, created_by=None, approved_by=None, date_available_use=None, depreciation_rate=None, original_price=None, book_amount=None, net_book_value=None, accummulate_amount=None, expense_amount=None, insurrance_value=None, insurrance_fee_value=None, salvage_value_of_the_asset=None, income_amount_for_this_asset=None, week_debit=None, week_credit=None, month_debit=None, month_credit=None, quater_debit=None, quater_credit=None, semi_annual_debit=None, semi_annual_credit=None, year_debit=None, year_credit=None, list_error_message=None):
        # view
        self.fixed_asset_and_tool_view(account_number=account_number)
        self.click_button('Modify')
        self.wait_loading()
        # update value
        self.bo_click_tab('General information')
        if fixed_asset_name:
            self.bo_write_text('Fixed asset name', fixed_asset_name)
        if reference_number:
            self.bo_write_text('Reference number', reference_number)
        if provider_name:
            self.bo_write_text('Provider name', provider_name)
        self.key_escape()
        if owner_fixed_asset:
            self.bo_select('Owner fixed asset', owner_fixed_asset)
        # assert value
        self.bo_click_tab('General information')
        if account_number:
            self.bo_assert_text('Account number', str(account_number).replace('-', ''))
        if booking_currency_code:
            self.bo_assert_select('Booking currency code', booking_currency_code)
        if branch_name:
            self.bo_assert_select('Branch name', branch_name)
        if department_name:
            self.bo_assert_select('Department name', department_name)
        if catalogue_code:
            self.bo_assert_text_group('Catalogue code', catalogue_code)
        if fixed_asset_type:
            self.bo_assert_select('Fixed asset type', fixed_asset_type)
        if fixed_asset_classification:
            self.bo_assert_select('Fixed asset classification', fixed_asset_classification)
        if depreciation_method:
            self.bo_assert_select('Depreciation method', depreciation_method)
        if life_time_unit:
            self.bo_assert_select('Life time unit', life_time_unit)
        if fixed_asset_life_time:
            self.bo_assert_value('Fixed asset life time', fixed_asset_life_time)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if status:
            self.bo_assert_select('Status', status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if date_available_use:
            self.bo_assert_date('Date available use', date_available_use)
        self.bo_click_tab('Outstanding information')
        if depreciation_rate:
            self.bo_assert_value('Depreciation rate', depreciation_rate)
        if original_price:
            self.bo_assert_value('Original price', original_price)
        if book_amount:
            self.bo_assert_value('Book amount', book_amount)
        if net_book_value:
            self.bo_assert_value('Net book value', net_book_value)
        if accummulate_amount:
            self.bo_assert_value('Accummulate amount', accummulate_amount)
        if expense_amount:
            self.bo_assert_value('Expense amount', expense_amount)
        if insurrance_value:
            self.bo_assert_value('Insurrance value', insurrance_value)
        if insurrance_fee_value:
            self.bo_assert_value('Insurrance fee value', insurrance_fee_value)
        if salvage_value_of_the_asset:
            self.bo_assert_value('Salvage value of the asset', salvage_value_of_the_asset)
        if income_amount_for_this_asset:
            self.bo_assert_value('Income amount for this asset', income_amount_for_this_asset)
        if week_debit:
            self.bo_assert_value('Week debit', week_debit)
        if week_credit:
            self.bo_assert_value('Week credit', week_credit)
        if month_debit:
            self.bo_assert_value('Month debit', month_debit)
        if month_credit:
            self.bo_assert_value('Month credit', month_credit)
        if quater_debit:
            self.bo_assert_value('Quater debit', quater_debit)
        if quater_credit:
            self.bo_assert_value('Quater credit', quater_credit)
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
            account_number_out=self.bo_get_text('Account number')
            print(f'Account number: {account_number_out}')
            return account_number_out

    def fixed_asset_and_tool_delete(self, account_number, list_error_message=None):
        # search
        self.fixed_asset_and_tool_simple_search(str(account_number).replace('-', ''))
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
            self.fixed_asset_and_tool_simple_search(str(account_number).replace('-', ''))
            self.assert_search_not_found()
            print(f'Deleted: {account_number}')
            return account_number

# -------------------------- handle BO approval - FIXED ASSET --------------------------
    # FAC-Fixed Asset Catalogue Definition - Data Verification
    def fixed_asset_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalogue_status=None, fixed_asset_life_time=None, life_time_unit=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FAC-Fixed Asset Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General Information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue Name', catalogue_name)
        if fixed_asset_type:
            self.bo_assert_select('Fixed Asset Type', fixed_asset_type)
        if fixed_asset_classification:
            self.bo_assert_select('Fixed Asset Classification', fixed_asset_classification)
        if depreciation_method:
            self.bo_assert_select('Depreciation Method', depreciation_method)
        if catalogue_status:
            self.bo_assert_select('Catalogue Status', catalogue_status)
        if fixed_asset_life_time:
            self.bo_assert_value('Fixed asset life time', fixed_asset_life_time)
        if life_time_unit:
            self.bo_assert_select('Life time unit', life_time_unit)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)

    def fixed_asset_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalogue_status=None, fixed_asset_life_time=None, life_time_unit=None, created_by=None, approve_by=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FAC-Fixed Asset Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General Information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue Name', catalogue_name)
        if fixed_asset_type:
            self.bo_assert_select('Fixed Asset Type', fixed_asset_type)
        if fixed_asset_classification:
            self.bo_assert_select('Fixed Asset Classification', fixed_asset_classification)
        if depreciation_method:
            self.bo_assert_select('Depreciation Method', depreciation_method)
        if catalogue_status:
            self.bo_assert_select('Catalogue Status', catalogue_status)
        if fixed_asset_life_time:
            self.bo_assert_value('Fixed asset life time', fixed_asset_life_time)
        if life_time_unit:
            self.bo_assert_select('Life time unit', life_time_unit)
        if created_by:
            self.bo_assert_text_group('Created By', created_by)
        if approve_by:
            self.bo_assert_text_group('Approve By', approve_by)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)

    def fixed_asset_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalogue_status=None):
        # search and verify
        self.fixed_asset_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue Code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue Name', 1, catalogue_name)
        if fixed_asset_type:
            self.assert_table_data('Fixed Asset Type', 1, fixed_asset_type)
        if fixed_asset_classification:
            self.assert_table_data('Fixed Asset Classification', 1, fixed_asset_classification)
        if depreciation_method:
            self.assert_table_data('Depreciation Method', 1, depreciation_method)
        if catalogue_status:
            self.assert_table_data('Catalogue Status', 1, catalogue_status)

