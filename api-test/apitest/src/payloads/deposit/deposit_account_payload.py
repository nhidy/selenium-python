from datetime import datetime
from pickle import TRUE

class DepositAccountPayload(object):
    def view_by_id(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def view_by_account_number(self, account_number=None):
        if not account_number:
            account_number = ''
        payload = {
            "account_number": account_number
        }
        return payload

    def simple_search(self, search_text=None, page_size=None, page_index=None):
        if not search_text:
            search_text = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "search_text": search_text,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def advanced_search(self, account_number_def=None, account_number=None, account_name=None, currency_code=None, customer_code=None, customer_type_caption=None, catalog_code=None, deposit_status=None, deposit_type=None, reference_id=None, page_index=None, page_size=None):
        if not account_number_def:
            account_number_def = ''
        if not account_number:
            account_number = ''
        if not account_name:
            account_name = ''
        if not currency_code:
            currency_code = ''
        if not customer_code:
            customer_code = ''
        if not customer_type_caption:
            customer_type_caption = ''
        if not catalog_code:
            catalog_code = ''
        if not deposit_status:
            deposit_status = ''
        if not deposit_type:
            deposit_type = ''
        if not reference_id:
            reference_id = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "account_number_def": account_number_def,
            "account_number": account_number,
            "account_name": account_name,
            "currency_code": currency_code,
            "customer_code": customer_code,
            "customer_type_caption": customer_type_caption,
            "catalog_code": catalog_code,
            "deposit_status": deposit_status,
            "deposit_type": deposit_type,
            "reference_id": reference_id,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def update(self, id=None, account_name=None, business_purpose_code=None, minimum_deposit_amount=None, initial_deposit_amount=None, interest_tenor=None, interest_tenor_unit=None, minimum_tenor=None, minimum_tenor_unit=None, multiple_deposit_allow=None, multiple_withdrawal_allow=None, early_withdrawal=None, minimum_tenor_allow_early_withdrawal=None, minimum_tenor_allow_early_withdrawal_unit=None, credit_interest=None, credit_interest_tenor=None, credit_interest_tenor_unit=None, crediting_interest=None, dormant_period=None, dormant_period_unit=None, rollover=None, rollover_to_catalog=None, interest_due_on_holiday=None, principal_due_on_holiday=None, statement_tenor=None, statement_tenor_unit=None, statement_format=None, account_number_def=None, module_code=None, list_ifc_balance=None, approve_modify=None):
        if not id:
            id = 0
        if not account_name:
            account_name = ''
        if not business_purpose_code:
            business_purpose_code = ''
        if not minimum_deposit_amount:
            minimum_deposit_amount = 0
        if not initial_deposit_amount:
            initial_deposit_amount = 0
        if not interest_tenor:
            interest_tenor = 0
        if not interest_tenor_unit:
            interest_tenor_unit = ''
        if not minimum_tenor:
            minimum_tenor = 0
        if not minimum_tenor_unit:
            minimum_tenor_unit = ''
        if not multiple_deposit_allow:
            multiple_deposit_allow = ''
        if not multiple_withdrawal_allow:
            multiple_withdrawal_allow = ''
        if not early_withdrawal:
            early_withdrawal = ''
        if not minimum_tenor_allow_early_withdrawal:
            minimum_tenor_allow_early_withdrawal = 0
        if not minimum_tenor_allow_early_withdrawal_unit:
            minimum_tenor_allow_early_withdrawal_unit = ''
        if not credit_interest:
            credit_interest = ''
        if not credit_interest_tenor:
            credit_interest_tenor = 0
        if not credit_interest_tenor_unit:
            credit_interest_tenor_unit
        if not crediting_interest:
            crediting_interest = 0
        if not dormant_period:
            dormant_period = 0
        if not dormant_period_unit:
            dormant_period_unit = ''
        if not rollover:
            rollover = ''
        if not rollover_to_catalog:
            rollover_to_catalog = None
        if not interest_due_on_holiday:
            interest_due_on_holiday = 0
        if not principal_due_on_holiday:
            principal_due_on_holiday = 0
        if not statement_tenor:
            statement_tenor = 0
        if not statement_tenor_unit:
            statement_tenor_unit = ''
        if not statement_format:
            statement_format = ''
        if not account_number_def:
            account_number_def = ''
        if not module_code:
            module_code = ''
        if not list_ifc_balance:
            list_ifc_balance = ''
        if not approve_modify:
            approve_modify = True
        payload = {
            "id": id,
            "account_name": account_name,
            "business_purpose_code": business_purpose_code,
            "minimum_deposit_amount": minimum_deposit_amount,
            "initial_deposit_amount": initial_deposit_amount,
            "interest_tenor": interest_tenor,
            "interest_tenor_unit": interest_tenor_unit,
            "minimum_tenor": minimum_tenor,
            "minimum_tenor_unit": minimum_tenor_unit,
            "multiple_deposit_allow": multiple_deposit_allow,
            "multiple_withdrawal_allow": multiple_withdrawal_allow,
            "early_withdrawal": early_withdrawal,
            "minimum_tenor_allow_early_withdrawal": minimum_tenor_allow_early_withdrawal,
            "minimum_tenor_allow_early_withdrawal_unit": minimum_tenor_allow_early_withdrawal_unit,
            "credit_interest": credit_interest,
            "credit_interest_tenor": credit_interest_tenor,
            "credit_interest_tenor_unit": credit_interest_tenor_unit,
            "crediting_interest": crediting_interest,
            "dormant_period": dormant_period,
            "dormant_period_unit": dormant_period_unit,
            "rollover": rollover,
            "rollover_to_catalog": rollover_to_catalog,
            "interest_due_on_holiday": interest_due_on_holiday,
            "principal_due_on_holiday": principal_due_on_holiday,
            "statement_tenor": statement_tenor,
            "statement_tenor_unit": statement_tenor_unit,
            "statement_format": statement_format,
            "account_number_def": account_number_def,
            "module_code": module_code,
            "list_ifc_balance": list_ifc_balance,
            "approve_modify": approve_modify
        }
        return payload

    def delete_by_id(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def delete_by_defacno(self, account_number_def=None):
        if not account_number_def:
            account_number_def = ''
        payload = {
            "account_number_def": account_number_def
        }
        return payload