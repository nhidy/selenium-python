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

# data test credit
date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
product_limit_name_test = 'PL AUTO TEST ' + str(date_time)
currency_test = 'MMK'
limit_amount_test = '50,000,000.34'
limit_type_test = 'Non-shared' # or 'Shared'
sub_product_limit_name_test = 'SPL AUTO TEST ' + str(date_time)
credit_facility_test = 'Loan' # or 'Hire Purchase' or 'Over Draft' or 'Trust receipt' or 'Trade finance'
catalogue_code_test = 'CHL1MMK017'
account_holder_name_test = 'CRD AUTO TEST ' + str(date_time)
credit_limit_test = '5,000,000.65'
dealer_name_test = 'Dealer name test'
type_of_commodity_test = 'Type of commodity test'
purpose_of_loan_test = 'N2'
purpose_of_loan_name_test = 'Others'
disbursement_amount_test = '5,000,000.65'
# deposit_account_number_test = '11-003-097469-6'
interest_collect_test = '0.00'
principal_collect_test = '5,000,000.65'
new_status_test = 'Normal'
adjustment_amount_test_enter = '-100.23'
adjustment_amount_test_ui = '-1,000.23'

# data test mortgage
catalogue_code_mortgage = '00000003'
collateral_asset_value_test = '50,000,000.34'
reference_number_test = 'Ref AUTO TEST'
evaluate_by_test = 'By AUTO TEST'
amount_secure_from_this_asset_test = '5,000,000.65'
amount_secured_for_credit_account_test = '5,000,000.65'
release_amount_in_collateral_currency_test = '5,000,000.65'
release_amount_in_credit_currency_test = '5,000,000.65'
return_amount_test = collateral_asset_value_test
return_amount_in_asset_currency_test = collateral_asset_value_test

# INTMODE	F	Fixed
# INTMODE	B	Flat basic of installment
# INTMODE	C	Compound basic of installment
# INTMODE	U	Interest upfront
# INTMODE	O	Interest upfront based on OS
# sub_product_limit_code_mask = ''

class CreditCompoundTest(FormAction):
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
    def test_000_01_check_test_data_must_exist(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.add_gl_level_9_use_for_testing(
            branch_code=branch_code,
            currency_code='MMK',
            account_number=gl_account_number_test
        )
        if self.check_customer_profile_not_exist(customer_code_personal):
            self.stop()
            self.fail()

# Create other deposit account use for testing
    def test_000_02_create_deposit_account_use_for_testing(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global deposit_account_number_test
        dpt_opn_result = self.dpt_opn(
            customer_code=customer_code_personal,
            customer_type='Single customer',
            catalogue_code='CAMMK0000',
            reason_of_account_opening='Enter value reason of account opening'
        )
        deposit_account_number_test=dpt_opn_result[1]
        self.dpt_apr(
            account_number=deposit_account_number_test,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )
        self.dpt_cdp(
            account_number=deposit_account_number_test,
            amount_deposit='50,000,000.46',
            # debit_accounting=gl_account_number,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve
        )

    def test_001_crd_plo_open_product_limit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global product_limit_code_mask
        product_limit_name = product_limit_name_test
        customer_type = None
        customer_code = customer_code_personal
        reference_id = None
        currency = currency_test
        limit_amount = limit_amount_test
        limit_type = limit_type_test
        description = None
        product_limit_code = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_on_form = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_plo_result = self.crd_plo(
            product_limit_name=product_limit_name,
            customer_type=customer_type,
            customer_code=customer_code,
            reference_id=reference_id,
            currency=currency,
            limit_amount=limit_amount,
            limit_type=limit_type,
            description=description,
            product_limit_code=product_limit_code,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
            approve_on_form=approve_on_form,
            username=username,
            password=password,
            reason=reason
        )
        transaction_references=crd_plo_result[0]
        product_limit_code_mask=crd_plo_result[1]
        self.crd_plo_view(
            transaction_references=transaction_references,
            product_limit_name=product_limit_name,
            customer_type=customer_type,
            customer_code=customer_code,
            reference_id=reference_id,
            currency=currency,
            limit_amount=limit_amount,
            limit_type=limit_type,
            description=description,
            product_limit_code=product_limit_code,
            expected_posting=expected_posting,
        )

    def test_002_crd_pla_approve_product_limit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        product_limit_code = product_limit_code_mask
        description = None
        product_limit_name = product_limit_name_test
        customer_type = None
        customer_code = customer_code_personal
        reference_id = None
        currency = currency_test
        credit_limit = limit_amount_test
        limit_type = limit_type_test
        status = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_pla_result = self.crd_pla(
            product_limit_code=product_limit_code,
            description=description,
            product_limit_name=product_limit_name,
            customer_type=customer_type,
            customer_code=customer_code,
            reference_id=reference_id,
            currency=currency,
            credit_limit=credit_limit,
            limit_type=limit_type,
            status=status,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_pla_result[0]
        product_limit_code_out=crd_pla_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_pla_view(
            transaction_references=transaction_references,
            product_limit_code=product_limit_code,
            description=description,
            product_limit_name=product_limit_name,
            customer_type=customer_type,
            customer_code=customer_code,
            reference_id=reference_id,
            currency=currency,
            credit_limit=credit_limit,
            limit_type=limit_type,
            status=status,
            expected_posting=expected_posting,
        )

    def test_003_crd_splo_open_sub_product_limit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global sub_product_limit_code_mask
        sub_product_limit_name = sub_product_limit_name_test
        customer_type = None
        customer_code = customer_code_personal
        product_limit_code = product_limit_code_mask
        reference_id = None
        currency = currency_test
        credit_facility = credit_facility_test
        limit_amount = limit_amount_test
        description = None
        sub_product_limit_code = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_on_form = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_splo_result = self.crd_splo(
            sub_product_limit_name=sub_product_limit_name,
            customer_type=customer_type,
            customer_code=customer_code,
            product_limit_code=product_limit_code,
            reference_id=reference_id,
            currency=currency,
            credit_facility=credit_facility,
            limit_amount=limit_amount,
            description=description,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
            approve_on_form=approve_on_form,
            username=username,
            password=password,
            reason=reason
        )
        transaction_references=crd_splo_result[0]
        sub_product_limit_code_mask=crd_splo_result[1]
        self.crd_splo_view(
            transaction_references=transaction_references,
            sub_product_limit_name=sub_product_limit_name,
            customer_type=customer_type,
            customer_code=customer_code,
            product_limit_code=product_limit_code,
            reference_id=reference_id,
            currency=currency,
            credit_facility=credit_facility,
            limit_amount=limit_amount,
            description=description,
            sub_product_limit_code=sub_product_limit_code_mask,
            expected_posting=expected_posting,
        )

    def test_004_crd_spla_approve_sub_product_limit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        sub_product_limit_code = sub_product_limit_code_mask
        description = None
        sub_product_limit_name = sub_product_limit_name_test
        customer_type = None
        customer_code = customer_code_personal
        reference_id = None
        product_limit_code = product_limit_code_mask
        currency = currency_test
        credit_limit = limit_amount_test
        status = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_spla_result = self.crd_spla(
            sub_product_limit_code=sub_product_limit_code,
            description=description,
            sub_product_limit_name=sub_product_limit_name,
            customer_type=customer_type,
            customer_code=customer_code,
            reference_id=reference_id,
            product_limit_code=product_limit_code,
            currency=currency,
            credit_limit=credit_limit,
            status=status,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_spla_result[0]
        sub_product_limit_code_out=crd_spla_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_spla_view(
            transaction_references=transaction_references,
            sub_product_limit_code=sub_product_limit_code,
            description=description,
            sub_product_limit_name=sub_product_limit_name,
            customer_type=customer_type,
            customer_code=customer_code,
            reference_id=reference_id,
            product_limit_code=product_limit_code,
            currency=currency,
            credit_limit=credit_limit,
            status=status,
            expected_posting=expected_posting,
        )

    def test_005_crd_opn_open_new_credit_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global credit_account_number_mask
        customer_type = None
        customer_code = customer_code_personal
        sub_product_limit_code = sub_product_limit_code_mask
        catalogue_code = catalogue_code_test
        company_name = None
        sub_product = None
        credit_classification = None
        account_holder_name = account_holder_name_test
        sale_price = None
        down_payment = None
        down_payment_amount = None
        dealer_name = dealer_name_test
        type_of_commodity = type_of_commodity_test
        credit_limit = credit_limit_test
        margin = None
        from_date = None
        to_date = None
        first_prin_repayment_date = None
        first_int_repayment_date = None
        grace_period_for_principal = None
        branch_cd = None
        description = None
        purpose_of_loan = purpose_of_loan_test
        account_number = None
        catalogue_name = None
        credit_sub_type = None
        credit_facility = None
        currency_code = None
        maximum_limit = None
        interest_rate = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_on_form = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_opn_result = self.crd_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            sub_product_limit_code=sub_product_limit_code,
            catalogue_code=catalogue_code,
            company_name=company_name,
            sub_product=sub_product,
            credit_classification=credit_classification,
            account_holder_name=account_holder_name,
            sale_price=sale_price,
            down_payment=down_payment,
            down_payment_amount=down_payment_amount,
            dealer_name=dealer_name,
            type_of_commodity=type_of_commodity,
            credit_limit=credit_limit,
            margin=margin,
            from_date=from_date,
            to_date=to_date,
            first_prin_repayment_date=first_prin_repayment_date,
            first_int_repayment_date=first_int_repayment_date,
            grace_period_for_principal=grace_period_for_principal,
            branch_cd=branch_cd,
            description=description,
            purpose_of_loan=purpose_of_loan,
            account_number=account_number,
            catalogue_name=catalogue_name,
            credit_sub_type=credit_sub_type,
            credit_facility=credit_facility,
            currency_code=currency_code,
            maximum_limit=maximum_limit,
            interest_rate=interest_rate,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
            approve_on_form=approve_on_form,
            username=username,
            password=password,
            reason=reason
        )
        transaction_references=crd_opn_result[0]
        credit_account_number_mask=crd_opn_result[1]
        self.crd_opn_view(
            transaction_references=transaction_references,
            customer_type=customer_type,
            customer_code=customer_code,
            sub_product_limit_code=sub_product_limit_code,
            catalogue_code=catalogue_code,
            company_name=company_name,
            sub_product=sub_product,
            credit_classification=credit_classification,
            account_holder_name=account_holder_name,
            sale_price=sale_price,
            down_payment=down_payment,
            down_payment_amount=down_payment_amount,
            dealer_name=dealer_name,
            type_of_commodity=type_of_commodity,
            credit_limit=credit_limit,
            margin=margin,
            from_date=from_date,
            to_date=to_date,
            first_prin_repayment_date=first_prin_repayment_date,
            first_int_repayment_date=first_int_repayment_date,
            grace_period_for_principal=grace_period_for_principal,
            branch_cd=branch_cd,
            description=description,
            purpose_of_loan=purpose_of_loan,
            account_number=credit_account_number_mask,
            catalogue_name=catalogue_name,
            credit_sub_type=credit_sub_type,
            credit_facility=credit_facility,
            currency_code=currency_code,
            maximum_limit=maximum_limit,
            interest_rate=interest_rate,
            expected_posting=expected_posting,
        )

    def test_006_crd_rej_reject_credit_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_type = None
        customer_code = customer_code_personal
        sub_product_limit_code = sub_product_limit_code_mask
        catalogue_code = catalogue_code_test
        company_name = None
        sub_product = None
        credit_classification = None
        account_holder_name = account_holder_name_test
        sale_price = None
        down_payment = None
        down_payment_amount = None
        dealer_name = dealer_name_test
        type_of_commodity = type_of_commodity_test
        credit_limit = credit_limit_test
        margin = None
        from_date = None
        to_date = None
        first_prin_repayment_date = None
        first_int_repayment_date = None
        grace_period_for_principal = None
        branch_cd = None
        description = None
        purpose_of_loan = purpose_of_loan_test
        account_number = None
        catalogue_name = None
        credit_sub_type = None
        credit_facility = None
        currency_code = None
        maximum_limit = None
        interest_rate = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_on_form = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_opn_result = self.crd_opn(
            customer_type=customer_type,
            customer_code=customer_code,
            sub_product_limit_code=sub_product_limit_code,
            catalogue_code=catalogue_code,
            company_name=company_name,
            sub_product=sub_product,
            credit_classification=credit_classification,
            account_holder_name=account_holder_name,
            sale_price=sale_price,
            down_payment=down_payment,
            down_payment_amount=down_payment_amount,
            dealer_name=dealer_name,
            type_of_commodity=type_of_commodity,
            credit_limit=credit_limit,
            margin=margin,
            from_date=from_date,
            to_date=to_date,
            first_prin_repayment_date=first_prin_repayment_date,
            first_int_repayment_date=first_int_repayment_date,
            grace_period_for_principal=grace_period_for_principal,
            branch_cd=branch_cd,
            description=description,
            purpose_of_loan=purpose_of_loan,
            account_number=account_number,
            catalogue_name=catalogue_name,
            credit_sub_type=credit_sub_type,
            credit_facility=credit_facility,
            currency_code=currency_code,
            maximum_limit=maximum_limit,
            interest_rate=interest_rate,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
            approve_on_form=approve_on_form,
            username=username,
            password=password,
            reason=reason
        )
        credit_account_number_out=crd_opn_result[1]

        account_number = credit_account_number_out
        description = None
        current_status = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_rej_result = self.crd_rej(
            account_number=account_number,
            description=description,
            current_status=current_status,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
        )
        transaction_references=crd_rej_result[0]
        account_number_out=crd_rej_result[1]
        self.crd_rej_view(
            transaction_references=transaction_references,
            account_number=account_number,
            description=description,
            current_status=current_status,
            expected_posting=expected_posting,
        )

    def test_007_01_mtg_opn_open_mortgage_account_success(self):
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

    def test_007_02_mtg_apr_approve_mortgage_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        customer_code = customer_code_personal
        customer_name = None
        customer_address = None
        description = None
        account_holder_name = None
        forced_sale_value = None
        ifc_codes = None
        values = None
        total_fee = None
        username = username_approve
        password = password_approve
        reason = None

        mtg_apr_result = self.mtg_apr(
            account_number=account_number,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            description=description,
            account_holder_name=account_holder_name,
            forced_sale_value=forced_sale_value,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_on_form='Y',
            username=username,
            password=password,
            reason=reason,
        )

    def test_007_03_mtg_scr_secure_asset_for_credit_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        credit_account = credit_account_number_mask
        amount_secure_from_this_asset = amount_secure_from_this_asset_test
        amount_secured_for_credit_account = amount_secured_for_credit_account_test
        customer_code = customer_code_personal
        customer_name = None
        customer_address = None
        customer_description = None
        description = None
        collateral_account_currency = None
        forced_sale_value = None
        secured_amount_01 = None
        credit_account_currency = None
        credit_limit = None
        secured_amount_02 = None
        total_secured_amount = None
        exchange_rate = None
        base_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_on_form = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        mtg_scr_result = self.mtg_scr(
            account_number=account_number,
            credit_account=credit_account,
            amount_secure_from_this_asset=amount_secure_from_this_asset,
            amount_secured_for_credit_account=amount_secured_for_credit_account,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            description=description,
            collateral_account_currency=collateral_account_currency,
            forced_sale_value=forced_sale_value,
            secured_amount_01=secured_amount_01,
            credit_account_currency=credit_account_currency,
            credit_limit=credit_limit,
            secured_amount_02=secured_amount_02,
            total_secured_amount=total_secured_amount,
            exchange_rate=exchange_rate,
            base_amount=base_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
            approve_on_form=approve_on_form,
            username=username,
            password=password,
            reason=reason
        )

    def test_007_04_crd_apr_approve_credit_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = credit_account_number_mask
        deposit_account = None
        description = None
        customer_type = None
        account_holder_name = None
        catalogue_code = None
        catalogue_name = None
        currency_code = None
        credit_limit = None
        interest_rate = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_apr_result = self.crd_apr(
            account_number=account_number,
            deposit_account=deposit_account,
            description=description,
            customer_type=customer_type,
            account_holder_name=account_holder_name,
            catalogue_code=catalogue_code,
            catalogue_name=catalogue_name,
            currency_code=currency_code,
            credit_limit=credit_limit,
            interest_rate=interest_rate,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_apr_result[0]
        account_number_out=crd_apr_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_apr_view(
            transaction_references=transaction_references,
            account_number=account_number,
            deposit_account=deposit_account,
            description=description,
            customer_type=customer_type,
            account_holder_name=account_holder_name,
            catalogue_code=catalogue_code,
            catalogue_name=catalogue_name,
            currency_code=currency_code,
            credit_limit=credit_limit,
            interest_rate=interest_rate,
            expected_posting=expected_posting,
        )

    def test_008_crd_mdr_miscellaneous_disbursement_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        credit_account = credit_account_number_mask
        disbursement_amount = disbursement_amount_test
        accounting_account = gl_account_number_test
        receiver_name = None
        receiver_address = None
        home = None
        office = None
        description = None
        fee_collect_method = None
        schedule_template = None
        receiver_code = None
        remaining_provision_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_mdr_result = self.crd_mdr(
            credit_account=credit_account,
            disbursement_amount=disbursement_amount,
            accounting_account=accounting_account,
            receiver_name=receiver_name,
            receiver_address=receiver_address,
            home=home,
            office=office,
            description=description,
            fee_collect_method=fee_collect_method,
            schedule_template=schedule_template,
            receiver_code=receiver_code,
            remaining_provision_amount=remaining_provision_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_mdr_result[0]
        credit_account_out=crd_mdr_result[1]
        accounting_account_out=crd_mdr_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_mdr_view(
            transaction_references=transaction_references,
            credit_account=credit_account,
            disbursement_amount=disbursement_amount,
            accounting_account=accounting_account,
            receiver_name=receiver_name,
            receiver_address=receiver_address,
            home=home,
            office=office,
            description=description,
            fee_collect_method=fee_collect_method,
            schedule_template=schedule_template,
            receiver_code=receiver_code,
            remaining_provision_amount=remaining_provision_amount,
            expected_posting=expected_posting,
        )
        self.transaction_reverse(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )

    def test_009_crd_tdr_disbursement_by_transfer_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        credit_account = credit_account_number_mask
        disbursement_amount_deposit = disbursement_amount_test
        deposit_account = deposit_account_number_test
        deposit_account_name = None
        receiver_name = None
        receiver_address = None
        home = None
        office = None
        description = None
        fee_collect_method = None
        schedule_template = None
        receiver_code = None
        remaining_provision_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_tdr_result = self.crd_tdr(
            credit_account=credit_account,
            disbursement_amount_deposit=disbursement_amount_deposit,
            deposit_account=deposit_account,
            deposit_account_name=deposit_account_name,
            receiver_name=receiver_name,
            receiver_address=receiver_address,
            home=home,
            office=office,
            description=description,
            fee_collect_method=fee_collect_method,
            schedule_template=schedule_template,
            receiver_code=receiver_code,
            remaining_provision_amount=remaining_provision_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_tdr_result[0]
        credit_account_out=crd_tdr_result[1]
        deposit_account_out=crd_tdr_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_tdr_view(
            transaction_references=transaction_references,
            credit_account=credit_account,
            disbursement_amount_deposit=disbursement_amount_deposit,
            deposit_account=deposit_account,
            deposit_account_name=deposit_account_name,
            receiver_name=receiver_name,
            receiver_address=receiver_address,
            home=home,
            office=office,
            description=description,
            fee_collect_method=fee_collect_method,
            schedule_template=schedule_template,
            receiver_code=receiver_code,
            remaining_provision_amount=remaining_provision_amount,
            expected_posting=expected_posting,
        )

    def test_010_crd_blk_block_credit_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        credit_account = credit_account_number_mask
        customer_name = None
        customer_address = None
        home = None
        office = None
        description = None
        customer_code = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None

        crd_blk_result = self.crd_blk(
            credit_account=credit_account,
            customer_name=customer_name,
            customer_address=customer_address,
            home=home,
            office=office,
            description=description,
            customer_code=customer_code,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
        )
        transaction_references=crd_blk_result[0]
        credit_account_out=crd_blk_result[1]
        self.crd_blk_view(
            transaction_references=transaction_references,
            credit_account=credit_account,
            customer_name=customer_name,
            customer_address=customer_address,
            home=home,
            office=office,
            description=description,
            customer_code=customer_code,
            expected_posting=expected_posting,
        )

    def test_011_crd_cas_change_account_status_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = credit_account_number_mask
        new_status = new_status_test
        description = None
        current_status = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None

        crd_cas_result = self.crd_cas(
            account_number=account_number,
            new_status=new_status,
            description=description,
            current_status=current_status,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
        )
        transaction_references=crd_cas_result[0]
        account_number_out=crd_cas_result[1]
        self.crd_cas_view(
            transaction_references=transaction_references,
            account_number=account_number,
            new_status=new_status,
            description=description,
            current_status=current_status,
            expected_posting=expected_posting,
        )

    def test_012_crd_mipm_miscelaneous_interest_and_principal_collection_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        credit_account = credit_account_number_mask
        interest_collect = interest_collect_test
        penalty_interest_collect = None
        principal_collect = principal_collect_test
        penalty_principal_collect = None
        gl_account_number = gl_account_number_test
        payee_name = None
        payee_address = None
        home = None
        office = None
        description = None
        fee_collect_method = None
        interest_due_amount = None
        accrued_interest_amount = None
        interest_receivable_amount = None
        total_interest = None
        total_penalty_interest = None
        total_principal_amount = None
        principal_due_amount = None
        total_penalty_principal = None
        advance_repayment_principal_mode = None
        payee_code = None
        value_date = None
        remaining_provision_amount = None
        total_collect_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_mipm_result = self.crd_mipm(
            credit_account=credit_account,
            interest_collect=interest_collect,
            penalty_interest_collect=penalty_interest_collect,
            principal_collect=principal_collect,
            penalty_principal_collect=penalty_principal_collect,
            gl_account_number=gl_account_number,
            payee_name=payee_name,
            payee_address=payee_address,
            home=home,
            office=office,
            description=description,
            fee_collect_method=fee_collect_method,
            interest_due_amount=interest_due_amount,
            accrued_interest_amount=accrued_interest_amount,
            interest_receivable_amount=interest_receivable_amount,
            total_interest=total_interest,
            total_penalty_interest=total_penalty_interest,
            total_principal_amount=total_principal_amount,
            principal_due_amount=principal_due_amount,
            total_penalty_principal=total_penalty_principal,
            advance_repayment_principal_mode=advance_repayment_principal_mode,
            payee_code=payee_code,
            value_date=value_date,
            remaining_provision_amount=remaining_provision_amount,
            total_collect_amount=total_collect_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_mipm_result[0]
        credit_account_out=crd_mipm_result[1]
        gl_account_number_out=crd_mipm_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_mipm_view(
            transaction_references=transaction_references,
            credit_account=credit_account,
            interest_collect=interest_collect,
            penalty_interest_collect=penalty_interest_collect,
            principal_collect=principal_collect,
            penalty_principal_collect=penalty_principal_collect,
            gl_account_number=gl_account_number,
            payee_name=payee_name,
            payee_address=payee_address,
            home=home,
            office=office,
            description=description,
            fee_collect_method=fee_collect_method,
            interest_due_amount=interest_due_amount,
            accrued_interest_amount=accrued_interest_amount,
            interest_receivable_amount=interest_receivable_amount,
            total_interest=total_interest,
            total_penalty_interest=total_penalty_interest,
            total_principal_amount=total_principal_amount,
            principal_due_amount=principal_due_amount,
            total_penalty_principal=total_penalty_principal,
            advance_repayment_principal_mode=advance_repayment_principal_mode,
            payee_code=payee_code,
            value_date=value_date,
            remaining_provision_amount=remaining_provision_amount,
            total_collect_amount=total_collect_amount,
            expected_posting=expected_posting,
        )
        self.transaction_reverse(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )

    def test_013_crd_ipct_principal_and_interest_collection_by_transfer_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        credit_account = credit_account_number_mask
        interest_collect = interest_collect_test
        penalty_interest_collect = None
        principal_collect = principal_collect_test
        penalty_principal_collect = None
        deposit_account = deposit_account_number_test
        payee_name = None
        payee_address = None
        home = None
        office = None
        description = None
        fee_collect_method = None
        interest_due_amount = None
        accrued_interest_amount = None
        interest_receivable_amount = None
        total_interest = None
        total_penalty_interest = None
        total_principal_amount = None
        principal_due_amount = None
        total_penalty_principal = None
        advance_repayment_principal_mode = None
        payee_code = None
        value_date = None
        remaining_provision_amount = None
        total_collect_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_ipct_result = self.crd_ipct(
            credit_account=credit_account,
            interest_collect=interest_collect,
            penalty_interest_collect=penalty_interest_collect,
            principal_collect=principal_collect,
            penalty_principal_collect=penalty_principal_collect,
            deposit_account=deposit_account,
            payee_name=payee_name,
            payee_address=payee_address,
            home=home,
            office=office,
            description=description,
            fee_collect_method=fee_collect_method,
            interest_due_amount=interest_due_amount,
            accrued_interest_amount=accrued_interest_amount,
            interest_receivable_amount=interest_receivable_amount,
            total_interest=total_interest,
            total_penalty_interest=total_penalty_interest,
            total_principal_amount=total_principal_amount,
            principal_due_amount=principal_due_amount,
            total_penalty_principal=total_penalty_principal,
            advance_repayment_principal_mode=advance_repayment_principal_mode,
            payee_code=payee_code,
            value_date=value_date,
            remaining_provision_amount=remaining_provision_amount,
            total_collect_amount=total_collect_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_ipct_result[0]
        credit_account_out=crd_ipct_result[1]
        deposit_account_out=crd_ipct_result[2]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_ipct_view(
            transaction_references=transaction_references,
            credit_account=credit_account,
            interest_collect=interest_collect,
            penalty_interest_collect=penalty_interest_collect,
            principal_collect=principal_collect,
            penalty_principal_collect=penalty_principal_collect,
            deposit_account=deposit_account,
            payee_name=payee_name,
            payee_address=payee_address,
            home=home,
            office=office,
            description=description,
            fee_collect_method=fee_collect_method,
            interest_due_amount=interest_due_amount,
            accrued_interest_amount=accrued_interest_amount,
            interest_receivable_amount=interest_receivable_amount,
            total_interest=total_interest,
            total_penalty_interest=total_penalty_interest,
            total_principal_amount=total_principal_amount,
            principal_due_amount=principal_due_amount,
            total_penalty_principal=total_penalty_principal,
            advance_repayment_principal_mode=advance_repayment_principal_mode,
            payee_code=payee_code,
            value_date=value_date,
            remaining_provision_amount=remaining_provision_amount,
            total_collect_amount=total_collect_amount,
            expected_posting=expected_posting,
        )

    def test_014_01_mtg_rls_release_asset_from_credit_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        credit_account = credit_account_number_mask
        release_amount_in_collateral_currency = release_amount_in_collateral_currency_test
        release_amount_in_credit_currency = release_amount_in_credit_currency_test
        customer_code = customer_code_personal
        customer_name = None
        customer_address = None
        customer_description = None
        description = None
        forced_sale_value = None
        collateral_account_currency = None
        credit_account_currency = None
        secured_amount = None
        exchange_rate = None
        base_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_on_form = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        mtg_rls_result = self.mtg_rls(
            account_number=account_number,
            credit_account=credit_account,
            release_amount_in_collateral_currency=release_amount_in_collateral_currency,
            release_amount_in_credit_currency=release_amount_in_credit_currency,
            customer_code=customer_code,
            customer_name=customer_name,
            customer_address=customer_address,
            customer_description=customer_description,
            description=description,
            forced_sale_value=forced_sale_value,
            collateral_account_currency=collateral_account_currency,
            credit_account_currency=credit_account_currency,
            secured_amount=secured_amount,
            exchange_rate=exchange_rate,
            base_amount=base_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
            approve_on_form=approve_on_form,
            username=username,
            password=password,
            reason=reason
        )

    def test_014_02_mtg_rtn_return_collateral_asset_to_customer_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        return_amount = return_amount_test
        return_amount_in_asset_currency = return_amount_in_asset_currency_test
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
        approve_on_form = 'Y'
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
            expected_posting=expected_posting,
            approve_on_form=approve_on_form,
            username=username,
            password=password,
            reason=reason
        )

    def test_014_03_mtg_cls_close_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = mortgage_account_number_mask
        account_holder_name = None
        customer_name = None
        customer_address = None
        description = None
        customer_description = None
        forced_sale_value = None
        customer_code = None
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

    def test_014_04_crd_cls_close_account_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        credit_account = credit_account_number_mask
        home = None
        office = None
        description = None
        current_group = None
        creditor_name = None
        creditor_code = None
        creditor_address = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None

        crd_cls_result = self.crd_cls(
            credit_account=credit_account,
            home=home,
            office=office,
            description=description,
            current_group=current_group,
            creditor_name=creditor_name,
            creditor_code=creditor_code,
            creditor_address=creditor_address,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
        )
        transaction_references=crd_cls_result[0]
        credit_account_out=crd_cls_result[1]
        self.crd_cls_view(
            transaction_references=transaction_references,
            credit_account=credit_account,
            home=home,
            office=office,
            description=description,
            current_group=current_group,
            creditor_name=creditor_name,
            creditor_code=creditor_code,
            creditor_address=creditor_address,
            expected_posting=expected_posting,
        )

    def test_015_crd_his_history_inquiry_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        account_number = credit_account_number_mask
        from_date = None
        to_date = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None

        self.crd_his(
            account_number=account_number,
            from_date=from_date,
            to_date=to_date,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            expected_posting=expected_posting,
        )

    def test_016_crd_spad_adjust_sub_product_limit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        sub_product_limit_code = sub_product_limit_code_mask
        description = None
        current_limit = None
        avaiable_limit = None
        outstanding_balance = None
        new_limit_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_spad_result = self.crd_spad(
            sub_product_limit_code=sub_product_limit_code,
            adjustment_amount=adjustment_amount_test_enter,
            description=description,
            current_limit=current_limit,
            avaiable_limit=avaiable_limit,
            outstanding_balance=outstanding_balance,
            new_limit_amount=new_limit_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_spad_result[0]
        sub_product_limit_code_out=crd_spad_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_spad_view(
            transaction_references=transaction_references,
            sub_product_limit_code=sub_product_limit_code,
            adjustment_amount=adjustment_amount_test_ui,
            description=description,
            current_limit=current_limit,
            avaiable_limit=avaiable_limit,
            outstanding_balance=outstanding_balance,
            new_limit_amount=new_limit_amount,
            expected_posting=expected_posting,
        )

    def test_017_crd_plad_adjust_product_limit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        product_limit_code = product_limit_code_mask
        description = None
        current_limit = None
        avaiable_limit = None
        outstanding_balance = None
        new_limit_amount = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_plad_result = self.crd_plad(
            product_limit_code=product_limit_code,
            adjustment_amount=adjustment_amount_test_enter,
            description=description,
            current_limit=current_limit,
            avaiable_limit=avaiable_limit,
            outstanding_balance=outstanding_balance,
            new_limit_amount=new_limit_amount,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_plad_result[0]
        product_limit_code_out=crd_plad_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_plad_view(
            transaction_references=transaction_references,
            product_limit_code=product_limit_code,
            adjustment_amount=adjustment_amount_test_ui,
            description=description,
            current_limit=current_limit,
            avaiable_limit=avaiable_limit,
            outstanding_balance=outstanding_balance,
            new_limit_amount=new_limit_amount,
            expected_posting=expected_posting,
        )

    def test_018_crd_opn_open_new_credit_account_with_lookup_field_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        customer_type = None
        customer_code = customer_code_personal
        sub_product_limit_code = sub_product_limit_code_mask
        catalogue_code = catalogue_code_test
        company_name = None
        sub_product = None
        credit_classification = None
        account_holder_name = account_holder_name_test
        sale_price = None
        down_payment = None
        down_payment_amount = None
        dealer_name = dealer_name_test
        type_of_commodity = type_of_commodity_test
        credit_limit = credit_limit_test
        margin = None
        from_date = None
        to_date = None
        first_prin_repayment_date = None
        first_int_repayment_date = None
        grace_period_for_principal = None
        branch_cd = branch_code
        description = None
        purpose_of_loan = purpose_of_loan_test
        purpose_of_loan_name = purpose_of_loan_name_test
        account_number = None
        catalogue_name = None
        credit_sub_type = None
        credit_facility = None
        currency_code = None
        maximum_limit = None
        interest_rate = None
        approve_on_form = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_opn_result = self.crd_opn_lookup(
            customer_type=customer_type,
            customer_code=customer_code,
            sub_product_limit_code=sub_product_limit_code,
            catalogue_code=catalogue_code,
            company_name=company_name,
            sub_product=sub_product,
            credit_classification=credit_classification,
            account_holder_name=account_holder_name,
            sale_price=sale_price,
            down_payment=down_payment,
            down_payment_amount=down_payment_amount,
            dealer_name=dealer_name,
            type_of_commodity=type_of_commodity,
            credit_limit=credit_limit,
            margin=margin,
            from_date=from_date,
            to_date=to_date,
            first_prin_repayment_date=first_prin_repayment_date,
            first_int_repayment_date=first_int_repayment_date,
            grace_period_for_principal=grace_period_for_principal,
            branch_cd=branch_cd,
            description=description,
            purpose_of_loan_name=purpose_of_loan_name,
            account_number=account_number,
            catalogue_name=catalogue_name,
            credit_sub_type=credit_sub_type,
            credit_facility=credit_facility,
            currency_code=currency_code,
            maximum_limit=maximum_limit,
            interest_rate=interest_rate,
            approve_on_form=approve_on_form,
            username=username,
            password=password,
            reason=reason
        )
        transaction_references=crd_opn_result[0]
        credit_account_number=crd_opn_result[1]
        self.crd_opn_view(
            transaction_references=transaction_references,
            customer_type=customer_type,
            customer_code=customer_code,
            sub_product_limit_code=sub_product_limit_code,
            catalogue_code=catalogue_code,
            company_name=company_name,
            sub_product=sub_product,
            credit_classification=credit_classification,
            account_holder_name=account_holder_name,
            sale_price=sale_price,
            down_payment=down_payment,
            down_payment_amount=down_payment_amount,
            dealer_name=dealer_name,
            type_of_commodity=type_of_commodity,
            credit_limit=credit_limit,
            margin=margin,
            from_date=from_date,
            to_date=to_date,
            first_prin_repayment_date=first_prin_repayment_date,
            first_int_repayment_date=first_int_repayment_date,
            grace_period_for_principal=grace_period_for_principal,
            branch_cd=branch_cd,
            description=description,
            purpose_of_loan=purpose_of_loan,
            account_number=credit_account_number,
            catalogue_name=catalogue_name,
            credit_sub_type=credit_sub_type,
            credit_facility=credit_facility,
            currency_code=currency_code,
            maximum_limit=maximum_limit,
            interest_rate=interest_rate,
        )
        self.crd_rej(
            account_number=credit_account_number,
            approve_on_form='Y',
            username=username_approve,
            password=password_approve,
        )

    def test_019_crd_splc_close_sub_product_limit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        sub_product_limit_code = sub_product_limit_code_mask
        description = None
        currency = None
        sub_product_limit = None
        avaiable_limit = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_splc_result = self.crd_splc(
            sub_product_limit_code=sub_product_limit_code,
            description=description,
            currency=currency,
            sub_product_limit=sub_product_limit,
            avaiable_limit=avaiable_limit,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_splc_result[0]
        sub_product_limit_code_out=crd_splc_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_splc_view(
            transaction_references=transaction_references,
            sub_product_limit_code=sub_product_limit_code,
            description=description,
            currency=currency,
            sub_product_limit=sub_product_limit,
            avaiable_limit=avaiable_limit,
            expected_posting=expected_posting,
        )

    def test_020_crd_plc_close_product_limit_success(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        product_limit_code = product_limit_code_mask
        description = None
        currency = None
        product_limit = None
        avaiable_limit = None
        ifc_codes = None
        values = None
        total_fee = None
        expected_posting = None
        approve_later = 'Y'
        username = username_approve
        password = password_approve
        reason = None

        crd_plc_result = self.crd_plc(
            product_limit_code=product_limit_code,
            description=description,
            currency=currency,
            product_limit=product_limit,
            avaiable_limit=avaiable_limit,
            ifc_codes=ifc_codes,
            values=values,
            total_fee=total_fee,
            approve_later=approve_later,
        )
        transaction_references=crd_plc_result[0]
        product_limit_code_out=crd_plc_result[1]
        self.transaction_approve(
            transaction_references=transaction_references,
            username=username,
            password=password,
            reason=reason,
        )
        self.crd_plc_view(
            transaction_references=transaction_references,
            product_limit_code=product_limit_code,
            description=description,
            currency=currency,
            product_limit=product_limit,
            avaiable_limit=avaiable_limit,
            expected_posting=expected_posting,
        )

if __name__ == '__main__': 
    webui_test.main()