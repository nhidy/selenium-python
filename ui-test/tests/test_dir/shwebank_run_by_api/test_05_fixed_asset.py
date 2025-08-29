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

# data test
date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
catalogue_code_test = '00000102'
fixed_asset_name_test = 'FAC NAME AUTO TEST ' + str(date_time)
fixed_asset_group_test = 'FAC group TEST'
provider_name_test = 'Provider name TEST'
original_price_test = '5,000,000.46'
booking_value_test = '5,000,000.46'
salvage_value_of_the_asset_test = '4,000,000.52'
branch_name_test = '003 - Bayint Naung Branch'
department_name_test = '003 - BYN'
selling_amount_test = '5,000,000.46'
adjust_accumulate_amount_test = '1,000.45'
new_branch_test = '005'
new_department_test = '005 - YZD'

class FixedAssetTest(FormAction):
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
    def test_000_01_check_test_data_must_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=gl_account_number
        )

# Create other deposit account use for testing
    def test_000_02_create_deposit_account_use_for_testing(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_account_number
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code='CAMMK0000',
            reason_of_account_opening='Enter value reason of account opening'
        )
        deposit_account_number=dpt_opn_result[1]
        self.dpt_apr(
            account_number=deposit_account_number,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cdp(
            account_number=deposit_account_number,
            amount_deposit='50,000,000.46',
            # debit_accounting=gl_account_number,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )

    def test_001_fac_opn_open_new_fixed_asset_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global fixed_asset_account_number_mask
        catalogue_code = catalogue_code_test
        sequence_number = None
        fixed_asset_name = fixed_asset_name_test
        fixed_asset_group = fixed_asset_group_test
        provider_name = provider_name_test
        original_currency = None
        original_price = original_price_test
        booking_value = booking_value_test
        salvage_value_of_the_asset = salvage_value_of_the_asset_test
        branch_name = branch_name_test
        department_name = department_name_test
        description = None
        account_number = None
        owner_of_this_fixed_asset = None
        catalogue_name = None
        fixed_asset_type = None
        fixed_asset_classification = None
        depreciation_method = None
        fixed_asset_life_time = None
        life_time_unit = None
        depreciation_rate = None
        booking_currency = None
        cross_rate = None
        value_date = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        fac_opn_result = self.fac_opn(
            catalogue_code=catalogue_code,
            sequence_number=sequence_number,
            fixed_asset_name=fixed_asset_name,
            fixed_asset_group=fixed_asset_group,
            provider_name=provider_name,
            original_currency=original_currency,
            original_price=original_price,
            booking_value=booking_value,
            salvage_value_of_the_asset=salvage_value_of_the_asset,
            branch_name=branch_name,
            department_name=department_name,
            description=description,
            account_number=account_number,
            owner_of_this_fixed_asset=owner_of_this_fixed_asset,
            catalogue_name=catalogue_name,
            fixed_asset_type=fixed_asset_type,
            fixed_asset_classification=fixed_asset_classification,
            depreciation_method=depreciation_method,
            fixed_asset_life_time=fixed_asset_life_time,
            life_time_unit=life_time_unit,
            depreciation_rate=depreciation_rate,
            booking_currency=booking_currency,
            cross_rate=cross_rate,
            value_date=value_date,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
        )
        transaction_references=fac_opn_result[0]
        fixed_asset_account_number_mask=fac_opn_result[1]
        self.fac_opn_view(
            transaction_references=transaction_references,
            catalogue_code=catalogue_code,
            sequence_number=sequence_number,
            fixed_asset_name=fixed_asset_name,
            fixed_asset_group=fixed_asset_group,
            provider_name=provider_name,
            original_currency=original_currency,
            original_price=original_price,
            booking_value=booking_value,
            salvage_value_of_the_asset=salvage_value_of_the_asset,
            branch_name=branch_name,
            department_name=department_name,
            description=description,
            account_number=account_number,
            owner_of_this_fixed_asset=owner_of_this_fixed_asset,
            catalogue_name=catalogue_name,
            fixed_asset_type=fixed_asset_type,
            fixed_asset_classification=fixed_asset_classification,
            depreciation_method=depreciation_method,
            fixed_asset_life_time=fixed_asset_life_time,
            life_time_unit=life_time_unit,
            depreciation_rate=depreciation_rate,
            booking_currency=booking_currency,
            cross_rate=cross_rate,
            value_date=value_date,
            expected_posting=expected_posting,
        )

    def test_002_fac_pbc_purchase_fixed_asset_by_cash_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = fixed_asset_account_number_mask
        vendor_id = None
        vendor_name = None
        vendor_address = None
        vendor_description = None
        description = None
        fixed_asset_name = None
        original_currency = None
        original_amount = None
        cash_currency_book_cccy = None
        cross_rate_at_time_open_fa = None
        amount_in_cash = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        fac_pbc_result = self.fac_pbc(
            account_number=account_number,
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            vendor_address=vendor_address,
            vendor_description=vendor_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            original_currency=original_currency,
            original_amount=original_amount,
            cash_currency_book_cccy=cash_currency_book_cccy,
            cross_rate_at_time_open_fa=cross_rate_at_time_open_fa,
            amount_in_cash=amount_in_cash,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=fac_pbc_result[0]
        account_number_out=fac_pbc_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.fac_pbc_view(
            transaction_references=transaction_references,
            account_number=account_number,
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            vendor_address=vendor_address,
            vendor_description=vendor_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            original_currency=original_currency,
            original_amount=original_amount,
            cash_currency_book_cccy=cash_currency_book_cccy,
            cross_rate_at_time_open_fa=cross_rate_at_time_open_fa,
            amount_in_cash=amount_in_cash,
            expected_posting=expected_posting,
        )
        self.transaction_reverse(
            transaction_references=transaction_references,
            username=username,
            password=password,
        )

    def test_003_fac_pbd_purchase_fixed_asset_by_deposit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = fixed_asset_account_number_mask
        deposit_account = deposit_account_number
        vendor_id = None
        vendor_name = None
        vendor_address = None
        vendor_description = None
        description = None
        fixed_asset_name = None
        original_currency = None
        original_amount = None
        deposit_currency = None
        cross_rate = None
        book_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        fac_pbd_result = self.fac_pbd(
            account_number=account_number,
            deposit_account=deposit_account,
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            vendor_address=vendor_address,
            vendor_description=vendor_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            original_currency=original_currency,
            original_amount=original_amount,
            deposit_currency=deposit_currency,
            cross_rate=cross_rate,
            book_amount=book_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=fac_pbd_result[0]
        account_number_out=fac_pbd_result[1]
        deposit_account_out=fac_pbd_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.fac_pbd_view(
            transaction_references=transaction_references,
            account_number=account_number,
            deposit_account=deposit_account,
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            vendor_address=vendor_address,
            vendor_description=vendor_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            original_currency=original_currency,
            original_amount=original_amount,
            deposit_currency=deposit_currency,
            cross_rate=cross_rate,
            book_amount=book_amount,
            expected_posting=expected_posting,
        )
        self.transaction_reverse(
            transaction_references=transaction_references,
            username=username,
            password=password,
        )

    def test_004_fac_pbg_purchase_fixed_asset_by_accounting_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = fixed_asset_account_number_mask
        gl_account = gl_account_number
        vendor_id = None
        vendor_name = None
        vendor_address = None
        vendor_description = None
        description = None
        fixed_asset_name = None
        original_currency = None
        original_amount = None
        gl_currency = None
        cross_rate = None
        book_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        fac_pbg_result = self.fac_pbg(
            account_number=account_number,
            gl_account=gl_account,
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            vendor_address=vendor_address,
            vendor_description=vendor_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            original_currency=original_currency,
            original_amount=original_amount,
            gl_currency=gl_currency,
            cross_rate=cross_rate,
            book_amount=book_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=fac_pbg_result[0]
        account_number_out=fac_pbg_result[1]
        gl_account_out=fac_pbg_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.fac_pbg_view(
            transaction_references=transaction_references,
            account_number=account_number,
            gl_account=gl_account,
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            vendor_address=vendor_address,
            vendor_description=vendor_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            original_currency=original_currency,
            original_amount=original_amount,
            gl_currency=gl_currency,
            cross_rate=cross_rate,
            book_amount=book_amount,
            expected_posting=expected_posting,
        )

    def test_005_fac_sbc_selling_fixed_asset_by_cash_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = fixed_asset_account_number_mask
        selling_amount = selling_amount_test
        cross_rate = None
        amount_in_cash = selling_amount_test
        purchaser_id = None
        purchaser_name = None
        purchaser_address = None
        purchaser_description = None
        description = None
        fixed_asset_name = None
        net_book_value = None
        acummulate_not_posted = None
        acummulate_posted = None
        book_value = None
        book_currency = None
        cash_currency = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        fac_sbc_result = self.fac_sbc(
            account_number=account_number,
            selling_amount=selling_amount,
            cross_rate=cross_rate,
            amount_in_cash=amount_in_cash,
            purchaser_id=purchaser_id,
            purchaser_name=purchaser_name,
            purchaser_address=purchaser_address,
            purchaser_description=purchaser_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            net_book_value=net_book_value,
            acummulate_not_posted=acummulate_not_posted,
            acummulate_posted=acummulate_posted,
            book_value=book_value,
            book_currency=book_currency,
            cash_currency=cash_currency,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=fac_sbc_result[0]
        account_number_out=fac_sbc_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.fac_sbc_view(
            transaction_references=transaction_references,
            account_number=account_number,
            selling_amount=selling_amount,
            cross_rate=cross_rate,
            amount_in_cash=amount_in_cash,
            purchaser_id=purchaser_id,
            purchaser_name=purchaser_name,
            purchaser_address=purchaser_address,
            purchaser_description=purchaser_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            net_book_value=net_book_value,
            acummulate_not_posted=acummulate_not_posted,
            acummulate_posted=acummulate_posted,
            book_value=book_value,
            book_currency=book_currency,
            cash_currency=cash_currency,
            expected_posting=expected_posting,
        )
        self.transaction_reverse(
            transaction_references=transaction_references,
            username=username,
            password=password,
        )

    def test_006_fac_sbd_selling_fixed_asset_by_deposit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = fixed_asset_account_number_mask
        selling_amount = selling_amount_test
        debit_account = deposit_account_number
        purchaser_id = None
        purchaser_name = None
        purchaser_address = None
        purchaser_description = None
        description = None
        fixed_asset_name = None
        net_book_value = None
        acummulate_not_posted = None
        acummulate_posted = None
        book_value = None
        book_currency = None
        currency = None
        cross_rate = None
        debit_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        fac_sbd_result = self.fac_sbd(
            account_number=account_number,
            selling_amount=selling_amount,
            debit_account=debit_account,
            purchaser_id=purchaser_id,
            purchaser_name=purchaser_name,
            purchaser_address=purchaser_address,
            purchaser_description=purchaser_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            net_book_value=net_book_value,
            acummulate_not_posted=acummulate_not_posted,
            acummulate_posted=acummulate_posted,
            book_value=book_value,
            book_currency=book_currency,
            currency=currency,
            cross_rate=cross_rate,
            debit_amount=debit_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=fac_sbd_result[0]
        account_number_out=fac_sbd_result[1]
        debit_account_out=fac_sbd_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.fac_sbd_view(
            transaction_references=transaction_references,
            account_number=account_number,
            selling_amount=selling_amount,
            debit_account=debit_account,
            purchaser_id=purchaser_id,
            purchaser_name=purchaser_name,
            purchaser_address=purchaser_address,
            purchaser_description=purchaser_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            net_book_value=net_book_value,
            acummulate_not_posted=acummulate_not_posted,
            acummulate_posted=acummulate_posted,
            book_value=book_value,
            book_currency=book_currency,
            currency=currency,
            cross_rate=cross_rate,
            debit_amount=debit_amount,
            expected_posting=expected_posting,
        )
        self.transaction_reverse(
            transaction_references=transaction_references,
            username=username,
            password=password,
        )

    def test_007_fac_sbg_selling_fixed_asset_by_accounting_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = fixed_asset_account_number_mask
        selling_amount = selling_amount_test
        debit_account = gl_account_number
        purchaser_id = None
        purchaser_name = None
        purchaser_address = None
        purchaser_description = None
        description = None
        fixed_asset_name = None
        net_book_value = None
        acummulate_not_posted = None
        acummulate_posted = None
        book_value = None
        book_currency = None
        currency = None
        cross_rate = None
        debit_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        fac_sbg_result = self.fac_sbg(
            account_number=account_number,
            selling_amount=selling_amount,
            debit_account=debit_account,
            purchaser_id=purchaser_id,
            purchaser_name=purchaser_name,
            purchaser_address=purchaser_address,
            purchaser_description=purchaser_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            net_book_value=net_book_value,
            acummulate_not_posted=acummulate_not_posted,
            acummulate_posted=acummulate_posted,
            book_value=book_value,
            book_currency=book_currency,
            currency=currency,
            cross_rate=cross_rate,
            debit_amount=debit_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=fac_sbg_result[0]
        account_number_out=fac_sbg_result[1]
        debit_account_out=fac_sbg_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.fac_sbg_view(
            transaction_references=transaction_references,
            account_number=account_number,
            selling_amount=selling_amount,
            debit_account=debit_account,
            purchaser_id=purchaser_id,
            purchaser_name=purchaser_name,
            purchaser_address=purchaser_address,
            purchaser_description=purchaser_description,
            description=description,
            fixed_asset_name=fixed_asset_name,
            net_book_value=net_book_value,
            acummulate_not_posted=acummulate_not_posted,
            acummulate_posted=acummulate_posted,
            book_value=book_value,
            book_currency=book_currency,
            currency=currency,
            cross_rate=cross_rate,
            debit_amount=debit_amount,
            expected_posting=expected_posting,
        )
        self.transaction_reverse(
            transaction_references=transaction_references,
            username=username,
            password=password,
        )

    def test_008_fac_dep_adjust_fixed_asset_accumulate_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        fixasset_number = fixed_asset_account_number_mask
        adjust_accumulate_amount = adjust_accumulate_amount_test
        adjust_expense_amount = None
        description = None
        current_accumulate_amount = None
        current_expense_amount = None
        new_accumulate_amount = None
        new_expense_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        fac_dep_result = self.fac_dep(
            fixasset_number=fixasset_number,
            adjust_accumulate_amount=adjust_accumulate_amount,
            adjust_expense_amount=adjust_expense_amount,
            description=description,
            current_accumulate_amount=current_accumulate_amount,
            current_expense_amount=current_expense_amount,
            new_accumulate_amount=new_accumulate_amount,
            new_expense_amount=new_expense_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=fac_dep_result[0]
        fixasset_number_out=fac_dep_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.fac_dep_view(
            transaction_references=transaction_references,
            fixasset_number=fixasset_number,
            adjust_accumulate_amount=adjust_accumulate_amount,
            adjust_expense_amount=adjust_expense_amount,
            description=description,
            current_accumulate_amount=current_accumulate_amount,
            current_expense_amount=current_expense_amount,
            new_accumulate_amount=new_accumulate_amount,
            new_expense_amount=new_expense_amount,
            expected_posting=expected_posting,
        )
        self.transaction_reverse(
            transaction_references=transaction_references,
            username=username,
            password=password,
        )

    def test_009_fac_tfb_transfer_fixed_asset_to_another_branch_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = fixed_asset_account_number_mask
        new_branch = new_branch_test
        new_department = new_department_test
        description = None
        fixed_asset_name = None
        book_currency = None
        net_book_amount = None
        acummulate_not_posted = None
        book_amount = None
        new_account = None
        customer_code = None
        customer_name = None
        customer_address = None
        customer_description = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        fac_tfb_result = self.fac_tfb(
            account_number=account_number,
            new_branch=new_branch,
            new_department=new_department,
            description=description,
            fixed_asset_name=fixed_asset_name,
            book_currency=book_currency,
            net_book_amount=net_book_amount,
            acummulate_not_posted=acummulate_not_posted,
            book_amount=book_amount,
            new_account=new_account,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=fac_tfb_result[0]
        account_number_out=fac_tfb_result[1]
        new_account_out=fac_tfb_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.transaction_reverse(
            transaction_references=transaction_references,
            username=username,
            password=password,
        )
        self.fac_tfb_view(
            transaction_references=transaction_references,
            account_number=account_number,
            new_branch=new_branch,
            new_department=new_department,
            description=description,
            fixed_asset_name=fixed_asset_name,
            book_currency=book_currency,
            net_book_amount=net_book_amount,
            acummulate_not_posted=acummulate_not_posted,
            book_amount=book_amount,
            new_account=new_account,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            expected_posting=expected_posting,
        )

    def test_010_fac_cls_close_fixed_asset_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = fixed_asset_account_number_mask
        description = None
        fixed_asset_name = None
        net_book_value = None
        book_currency = None
        acummulate_posted = None
        book_value = None
        customer_id = None
        customer_name = None
        customer_address = None
        customer_description = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        fac_cls_result = self.fac_cls(
            account_number=account_number,
            description=description,
            fixed_asset_name=fixed_asset_name,
            net_book_value=net_book_value,
            book_currency=book_currency,
            acummulate_posted=acummulate_posted,
            book_value=book_value,
            customer_id=customer_id,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
        )
        transaction_references=fac_cls_result[0]
        account_number_out=fac_cls_result[1]
        self.fac_cls_view(
            transaction_references=transaction_references,
            account_number=account_number,
            description=description,
            fixed_asset_name=fixed_asset_name,
            net_book_value=net_book_value,
            book_currency=book_currency,
            acummulate_posted=acummulate_posted,
            book_value=book_value,
            customer_id=customer_id,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            expected_posting=expected_posting,
        )

if __name__ == '__main__': 
    webui_test.main()