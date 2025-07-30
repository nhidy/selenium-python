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

if __name__ == '__main__': 
    webui_test.main()