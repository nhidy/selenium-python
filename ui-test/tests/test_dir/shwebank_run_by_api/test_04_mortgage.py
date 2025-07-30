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

# data test secure mortgage
catalogue_code_mortgage = '00000003'
collateral_asset_value_test = '4,500,000.00'
reference_number_test = 'Ref AUTO TEST'
evaluate_by_test = 'By AUTO TEST'
name_of_title_test = 'name_of_title test'
house_no_test = 'house_no test'
plot_no_test = 'plot_no test'
holding_no_test = 'holding_no test'
ward_no_test = 'ward_no test'
block_no_test = 'block_no test'
area_acre_test = 'area_acre test'
street_test = 'street test'
township_test = 'township test'
division_city_test = 'division_city test'
home_test = 'home test'
office_test = 'office test'

class RegressionMortgageTest(FormAction):
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
    def test_000_check_test_data_must_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=gl_account_number
        )
        if self.check_customer_profile_not_exist(customer_code_personal):
            self.stop()
            self.fail()

    def test_001_mtg_opn_open_mortgage_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global mortgage_account_number_mask
        account_name = None
        customer_type = None
        customer_code = customer_code_personal
        catalogue_code = catalogue_code_mortgage
        collateral_asset_type = None
        collateral_asset_class = None
        sercurity_paper_type = None
        collateral_rate = None
        risk_allocation_rate = None
        collateral_asset_value = collateral_asset_value_test
        market_value = None
        forced_sale_value = None
        cc_contract = None
        cc_amount = None
        seq_number = None
        reference_number = reference_number_test
        name_of_title = name_of_title_test
        house_no = house_no_test
        plot_no = plot_no_test
        holding_no = holding_no_test
        ward_no = ward_no_test
        block_no = block_no_test
        area_acre = area_acre_test
        street = street_test
        township = township_test
        division_city = division_city_test
        location = None
        legal_address = None
        legal_local_address = None
        expiry_date = None
        policy_amount = None
        company_issues_policy = None
        policy_number = None
        evaluate_by = evaluate_by_test
        evaluate_method = None
        evaluate_date = None
        new_evaluate_date = None
        insurance_name = None
        insurance_expiry_date = None
        description = None
        catalogue_name = None
        currency_code = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_on_form = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        mtg_opn_result = self.mtg_opn(
            account_name=account_name,
            customer_type=customer_type,
            customer_code=customer_code,
            catalogue_code=catalogue_code,
            collateral_asset_type=collateral_asset_type,
            collateral_asset_class=collateral_asset_class,
            sercurity_paper_type=sercurity_paper_type,
            collateral_rate=collateral_rate,
            risk_allocation_rate=risk_allocation_rate,
            collateral_asset_value=collateral_asset_value,
            market_value=market_value,
            forced_sale_value=forced_sale_value,
            cc_contract=cc_contract,
            cc_amount=cc_amount,
            seq_number=seq_number,
            reference_number=reference_number,
            name_of_title=name_of_title,
            house_no=house_no,
            plot_no=plot_no,
            holding_no=holding_no,
            ward_no=ward_no,
            block_no=block_no,
            area_acre=area_acre,
            street=street,
            township=township,
            division_city=division_city,
            location=location,
            legal_address=legal_address,
            legal_local_address=legal_local_address,
            expiry_date=expiry_date,
            policy_amount=policy_amount,
            company_issues_policy=company_issues_policy,
            policy_number=policy_number,
            evaluate_by=evaluate_by,
            evaluate_method=evaluate_method,
            evaluate_date=evaluate_date,
            new_evaluate_date=new_evaluate_date,
            insurance_name=insurance_name,
            insurance_expiry_date=insurance_expiry_date,
            description=description,
            catalogue_name=catalogue_name,
            currency_code=currency_code,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
            approve_on_form=approve_on_form,
            username=username,
            password=password,
            reason=reason
        )
        transaction_references=mtg_opn_result[0]
        mortgage_account_number_mask=mtg_opn_result[1]
        self.mtg_opn_view(
            transaction_references=transaction_references,
            account_name=account_name,
            customer_type=customer_type,
            customer_code=customer_code,
            catalogue_code=catalogue_code,
            collateral_asset_type=collateral_asset_type,
            collateral_asset_class=collateral_asset_class,
            sercurity_paper_type=sercurity_paper_type,
            collateral_rate=collateral_rate,
            risk_allocation_rate=risk_allocation_rate,
            collateral_asset_value=collateral_asset_value,
            market_value=market_value,
            forced_sale_value=forced_sale_value,
            cc_contract=cc_contract,
            cc_amount=cc_amount,
            seq_number=seq_number,
            reference_number=reference_number,
            name_of_title=name_of_title,
            house_no=house_no,
            plot_no=plot_no,
            holding_no=holding_no,
            ward_no=ward_no,
            block_no=block_no,
            area_acre=area_acre,
            street=street,
            township=township,
            division_city=division_city,
            location=location,
            legal_address=legal_address,
            legal_local_address=legal_local_address,
            expiry_date=expiry_date,
            policy_amount=policy_amount,
            company_issues_policy=company_issues_policy,
            policy_number=policy_number,
            evaluate_by=evaluate_by,
            evaluate_method=evaluate_method,
            evaluate_date=evaluate_date,
            new_evaluate_date=new_evaluate_date,
            insurance_name=insurance_name,
            insurance_expiry_date=insurance_expiry_date,
            description=description,
            account_number=mortgage_account_number_mask,
            catalogue_name=catalogue_name,
            currency_code=currency_code,
            expected_posting=expected_posting,
        )

    def test_002_mtg_apr_approve_mortgage_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        customer_code = customer_code_personal
        customer_name = None
        customer_address = None
        home = home_test
        office = office_test
        description = None
        account_holder_name = None
        forced_sale_value = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        mtg_apr_result = self.mtg_apr(
            account_number=account_number,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            home=home,
            office=office,
            description=description,
            account_holder_name=account_holder_name,
            forced_sale_value=forced_sale_value,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=mtg_apr_result[0]
        account_number_out=mtg_apr_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.mtg_apr_view(
            transaction_references=transaction_references,
            account_number=account_number,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            home=home,
            office=office,
            description=description,
            account_holder_name=account_holder_name,
            forced_sale_value=forced_sale_value,
            expected_posting=expected_posting,
        )

    def test_003_mtg_blk_block_mortgage_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        account_holder_name = None
        customer_name = None
        customer_address = None
        description = None
        customer_description = None
        forced_sale_value = None
        customer_code = customer_code_personal
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        mtg_blk_result = self.mtg_blk(
            account_number=account_number,
            account_holder_name=account_holder_name,
            customer_name=customer_name,
            customer_address=customer_address,
            description=description,
            customer_description=customer_description,
            forced_sale_value=forced_sale_value,
            customer_code=customer_code,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=mtg_blk_result[0]
        account_number_out=mtg_blk_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.mtg_blk_view(
            transaction_references=transaction_references,
            account_number=account_number,
            account_holder_name=account_holder_name,
            customer_name=customer_name,
            customer_address=customer_address,
            description=description,
            customer_description=customer_description,
            forced_sale_value=forced_sale_value,
            customer_code=customer_code,
            expected_posting=expected_posting,
        )

    def test_004_mtg_brl_release_block_mortgage_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        account_holder_name = None
        customer_name = None
        customer_address = None
        description = None
        customer_description = None
        forced_sale_value = None
        customer_code = customer_code_personal
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        mtg_brl_result = self.mtg_brl(
            account_number=account_number,
            account_holder_name=account_holder_name,
            customer_name=customer_name,
            customer_address=customer_address,
            description=description,
            customer_description=customer_description,
            forced_sale_value=forced_sale_value,
            customer_code=customer_code,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=mtg_brl_result[0]
        account_number_out=mtg_brl_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.mtg_brl_view(
            transaction_references=transaction_references,
            account_number=account_number,
            account_holder_name=account_holder_name,
            customer_name=customer_name,
            customer_address=customer_address,
            description=description,
            customer_description=customer_description,
            forced_sale_value=forced_sale_value,
            customer_code=customer_code,
            expected_posting=expected_posting,
        )

    def test_005_mtg_inr_increasing_asset_value_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        increasing_value = '1,000,000.59'
        increasing_booking_value = '1,000,000.59'
        customer_code = customer_code_personal
        customer_name = None
        customer_address = None
        customer_description = None
        description = None
        account_holder_name = None
        asset_value = None
        asset_booking_value = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        mtg_inr_result = self.mtg_inr(
            account_number=account_number,
            increasing_value=increasing_value,
            increasing_booking_value=increasing_booking_value,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            description=description,
            account_holder_name=account_holder_name,
            asset_value=asset_value,
            asset_booking_value=asset_booking_value,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=mtg_inr_result[0]
        account_number_out=mtg_inr_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.mtg_inr_view(
            transaction_references=transaction_references,
            account_number=account_number,
            increasing_value=increasing_value,
            increasing_booking_value=increasing_booking_value,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            description=description,
            account_holder_name=account_holder_name,
            asset_value=asset_value,
            asset_booking_value=asset_booking_value,
            expected_posting=expected_posting,
        )

    def test_006_mtg_dcr_decreasing_asset_value_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        decreasing_value = '1,000,000.59'
        decreasing_booking_value = '1,000,000.59'
        customer_code = customer_code_personal
        customer_name = None
        customer_address = None
        customer_description = None
        description = None
        account_holder_name = None
        asset_value = None
        asset_booking_value = None
        secured_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        mtg_dcr_result = self.mtg_dcr(
            account_number=account_number,
            decreasing_value=decreasing_value,
            decreasing_booking_value=decreasing_booking_value,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            description=description,
            account_holder_name=account_holder_name,
            asset_value=asset_value,
            asset_booking_value=asset_booking_value,
            secured_amount=secured_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=mtg_dcr_result[0]
        account_number_out=mtg_dcr_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.mtg_dcr_view(
            transaction_references=transaction_references,
            account_number=account_number,
            decreasing_value=decreasing_value,
            decreasing_booking_value=decreasing_booking_value,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            description=description,
            account_holder_name=account_holder_name,
            asset_value=asset_value,
            asset_booking_value=asset_booking_value,
            secured_amount=secured_amount,
            expected_posting=expected_posting,
        )

    def test_007_mtg_rtn_return_collateral_asset_to_customer_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        return_amount = None
        return_amount_in_asset_currency = collateral_asset_value_test
        customer_code = customer_code_personal
        customer_name = None
        customer_address = None
        customer_description = None
        description = None
        asset_booking_value = None
        secured_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        mtg_rtn_result = self.mtg_rtn(
            account_number=account_number,
            return_amount=return_amount,
            return_amount_in_asset_currency=return_amount_in_asset_currency,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            description=description,
            asset_booking_value=asset_booking_value,
            secured_amount=secured_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=mtg_rtn_result[0]
        account_number_out=mtg_rtn_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.mtg_rtn_view(
            transaction_references=transaction_references,
            account_number=account_number,
            return_amount=return_amount,
            return_amount_in_asset_currency=return_amount_in_asset_currency,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            description=description,
            asset_booking_value=asset_booking_value,
            secured_amount=secured_amount,
            expected_posting=expected_posting,
        )

    def test_008_mtg_cls_close_mortgage_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        account_holder_name = None
        customer_name = None
        customer_address = None
        description = None
        customer_description = None
        forced_sale_value = None
        customer_code = customer_code_personal
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None

        mtg_cls_result = self.mtg_cls(
            account_number=account_number,
            account_holder_name=account_holder_name,
            customer_name=customer_name,
            customer_address=customer_address,
            description=description,
            customer_description=customer_description,
            forced_sale_value=forced_sale_value,
            customer_code=customer_code,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
        )
        transaction_references=mtg_cls_result[0]
        account_number_out=mtg_cls_result[1]
        self.mtg_cls_view(
            transaction_references=transaction_references,
            account_number=account_number,
            account_holder_name=account_holder_name,
            customer_name=customer_name,
            customer_address=customer_address,
            description=description,
            customer_description=customer_description,
            forced_sale_value=forced_sale_value,
            customer_code=customer_code,
            expected_posting=expected_posting,
        )

if __name__ == '__main__': 
    webui_test.main()