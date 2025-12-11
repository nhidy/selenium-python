from datetime import datetime

class DepositCatalogPayload(object):
    def view(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
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

    def advanced_search(self, catalog_id=None, catalog_code=None, catalog_name=None, currency_code=None, deposit_type_caption=None, passbook_or_statement_or_receipt_caption=None, tenor=None, tenor_from=None, tenor_to=None, tenor_unit_caption=None, catalog_status_caption=None, page_index=None, page_size=None):
        if not catalog_id:
            catalog_id = None
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not currency_code:
            currency_code = ''
        if not deposit_type_caption:
            deposit_type_caption = ''
        if not passbook_or_statement_or_receipt_caption:
            passbook_or_statement_or_receipt_caption = ''
        if not tenor:
            tenor = None
        if not tenor_from:
            tenor_from = None
        if not tenor_to:
            tenor_to = None
        if not tenor_unit_caption:
            tenor_unit_caption = ''
        if not catalog_status_caption:
            catalog_status_caption = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "catalog_id": catalog_id,
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "currency_code": currency_code,
            "deposit_type_caption": deposit_type_caption,
            "passbook_or_statement_or_receipt_caption": passbook_or_statement_or_receipt_caption,
            "tenor": tenor,
            "tenor_from": tenor_from,
            "tenor_to": tenor_to,
            "tenor_unit_caption": tenor_unit_caption,
            "catalog_status_caption": catalog_status_caption,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, catalog_code=None, catalog_name=None, currency_code=None, secure_currency=None, deposit_type=None, deposit_purpose=None, deposit_classification=None, passbook_or_statement_or_receipt=None, minimum_deposit_amount=None, catalog_status=None, user_created=None, user_approved=None, tenor=None, tenor_unit=None, tenor2=None, tenor_unit2=None, deposit_tenor=None, deposit_tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, minimum_tenor=None, minimum_tenor_unit=None, multi_deposit=None, multi_withdraw=None, early_withdraw=None, minimum_tenor_allow_early_withdrawal=None, minimum_tenor_allow_early_withdrawal_unit=None, credit_interest=None, credit_interest_tenor=None, credit_interest_tenor_unit=None, crediting_interest=None, minimum_dormant_amount=None, dormant_period=None, dormant_period_unit=None, rollover=None, rollover_to_catalog=None, interest_due_on_holiday=None, principal_due_on_holiday=None, statement_format=None, statement_tenor=None, statement_tenor_unit=None, inital_depost_amount=None, periodic_deposit_amount=None, periodic_deposit_tenor=None, periodic_deposit_tenor_unit=None, tariff_code=None, group_id=None):
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not currency_code:
            currency_code = ''
        if not secure_currency:
            secure_currency = ''
        if not deposit_type:
            deposit_type = ''
        if not deposit_purpose:
            deposit_purpose = ''
        if not deposit_classification:
            deposit_classification = ''
        if not passbook_or_statement_or_receipt:
            passbook_or_statement_or_receipt = ''
        if not minimum_deposit_amount:
            minimum_deposit_amount = 0
        if not catalog_status:
            catalog_status = ''
        if not user_created:
            user_created = 0
        if not user_approved:
            user_approved = 0
        if not tenor:
            tenor = 0
        if not tenor_unit:
            tenor_unit = ''
        if not tenor2:
            tenor2 = 0
        if not tenor_unit2:
            tenor_unit2 = ''
        if not deposit_tenor:
            deposit_tenor = 0
        if not deposit_tenor_unit:
            deposit_tenor_unit = ''
        if not interest_tenor:
            interest_tenor = 0
        if not interest_tenor_unit:
            interest_tenor_unit = ''
        if not minimum_tenor:
            minimum_tenor = 0
        if not minimum_tenor_unit:
            minimum_tenor_unit = ''
        if not multi_deposit:
            multi_deposit = ''
        if not multi_withdraw:
            multi_withdraw = ''
        if not early_withdraw:
            early_withdraw = ''
        if not minimum_tenor_allow_early_withdrawal:
            minimum_tenor_allow_early_withdrawal = 0
        if not minimum_tenor_allow_early_withdrawal_unit:
            minimum_tenor_allow_early_withdrawal_unit = ''
        if not credit_interest:
            credit_interest = ''
        if not credit_interest_tenor:
            credit_interest_tenor = 0
        if not credit_interest_tenor_unit:
            credit_interest_tenor_unit = ''
        if not crediting_interest:
            crediting_interest = 0
        if not minimum_dormant_amount:
            minimum_dormant_amount = 0
        if not dormant_period:
            dormant_period = 0
        if not dormant_period_unit:
            dormant_period_unit = ''
        if not rollover:
            rollover = ''
        if not rollover_to_catalog:
            rollover_to_catalog = 0
        if not interest_due_on_holiday:
            interest_due_on_holiday = 0
        if not principal_due_on_holiday:
            principal_due_on_holiday = 0
        if not statement_format:
            statement_format = ''
        if not statement_tenor:
            statement_tenor = 0
        if not statement_tenor_unit:
            statement_tenor_unit = ''
        if not inital_depost_amount:
            inital_depost_amount = 0
        if not periodic_deposit_amount:
            periodic_deposit_amount = 0
        if not periodic_deposit_tenor:
            periodic_deposit_tenor = 0
        if not periodic_deposit_tenor_unit:
            periodic_deposit_tenor_unit = ''
        if not tariff_code:
            tariff_code = 0
        if not group_id:
            group_id = 0
        payload = {
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "currency_code": currency_code,
            "secure_currency": secure_currency,
            "deposit_type": deposit_type,
            "deposit_purpose": deposit_purpose,
            "deposit_classification": deposit_classification,
            "passbook_or_statement_or_receipt": passbook_or_statement_or_receipt,
            "minimum_deposit_amount": minimum_deposit_amount,
            "catalog_status": catalog_status,
            "user_created": user_created,
            "user_approved": user_approved,
            "tenor": tenor,
            "tenor_unit": tenor_unit,
            "tenor2": tenor2,
            "tenor_unit2": tenor_unit2,
            "deposit_tenor": deposit_tenor,
            "deposit_tenor_unit": deposit_tenor_unit,
            "interest_tenor": interest_tenor,
            "interest_tenor_unit": interest_tenor_unit,
            "minimum_tenor": minimum_tenor,
            "minimum_tenor_unit": minimum_tenor_unit,
            "multi_deposit": multi_deposit,
            "multi_withdraw": multi_withdraw,
            "early_withdraw": early_withdraw,
            "minimum_tenor_allow_early_withdrawal": minimum_tenor_allow_early_withdrawal,
            "minimum_tenor_allow_early_withdrawal_unit": minimum_tenor_allow_early_withdrawal_unit,
            "credit_interest": credit_interest,
            "credit_interest_tenor": credit_interest_tenor,
            "credit_interest_tenor_unit": credit_interest_tenor_unit,
            "crediting_interest": crediting_interest,
            "minimum_dormant_amount": minimum_dormant_amount,
            "dormant_period": dormant_period,
            "dormant_period_unit": dormant_period_unit,
            "rollover": rollover,
            "rollover_to_catalog": rollover_to_catalog,
            "interest_due_on_holiday": interest_due_on_holiday,
            "principal_due_on_holiday": principal_due_on_holiday,
            "statement_format": statement_format,
            "statement_tenor": statement_tenor,
            "statement_tenor_unit": statement_tenor_unit,
            "inital_depost_amount": inital_depost_amount,
            "periodic_deposit_amount": periodic_deposit_amount,
            "periodic_deposit_tenor": periodic_deposit_tenor,
            "periodic_deposit_tenor_unit": periodic_deposit_tenor_unit,
            "tariff_code": tariff_code,
            "group_id": group_id
        }
        return payload

    def update(self, id=None, catalog_code=None, catalog_name=None, currency_code=None, secure_currency=None, deposit_type=None, deposit_purpose=None, deposit_classification=None, passbook_or_statement_or_receipt=None, minimum_deposit_amount=None, catalog_status=None, multi_deposit=None, multi_withdraw=None, credit_interest=None, credit_interest_tenor=None, credit_interest_tenor_unit=None, crediting_interest=None, minimum_dormant_amount=None, dormant_period=None, dormant_period_unit=None, statement_format=None, statement_tenor=None, statement_tenor_unit=None, inital_depost_amount=None, tariff_code=None, group_id=None):
        if not id:
            id = 0
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not currency_code:
            currency_code = ''
        if not secure_currency:
            secure_currency = ''
        if not deposit_type:
            deposit_type = ''
        if not deposit_purpose:
            deposit_purpose = ''
        if not deposit_classification:
            deposit_classification = ''
        if not passbook_or_statement_or_receipt:
            passbook_or_statement_or_receipt = ''
        if not minimum_deposit_amount:
            minimum_deposit_amount = 0
        if not catalog_status:
            catalog_status = ''
        if not multi_deposit:
            multi_deposit = ''
        if not multi_withdraw:
            multi_withdraw = ''
        if not credit_interest:
            credit_interest = ''
        if not credit_interest_tenor:
            credit_interest_tenor = 0
        if not credit_interest_tenor_unit:
            credit_interest_tenor_unit = ''
        if not crediting_interest:
            crediting_interest = 0
        if not minimum_dormant_amount:
            minimum_dormant_amount = 0
        if not dormant_period:
            dormant_period = 0
        if not dormant_period_unit:
            dormant_period_unit = ''
        if not statement_format:
            statement_format = ''
        if not statement_tenor:
            statement_tenor = 0
        if not statement_tenor_unit:
            statement_tenor_unit = ''
        if not inital_depost_amount:
            inital_depost_amount = 0
        if not tariff_code:
            tariff_code = 0
        if not group_id:
            group_id = 0
        payload = {
            "id": id,
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "currency_code": currency_code,
            "secure_currency": secure_currency,
            "deposit_type": deposit_type,
            "deposit_purpose": deposit_purpose,
            "deposit_classification": deposit_classification,
            "passbook_or_statement_or_receipt": passbook_or_statement_or_receipt,
            "minimum_deposit_amount": minimum_deposit_amount,
            "catalog_status": catalog_status,
            "multi_deposit": multi_deposit,
            "multi_withdraw": multi_withdraw,
            "credit_interest": credit_interest,
            "credit_interest_tenor": credit_interest_tenor,
            "credit_interest_tenor_unit": credit_interest_tenor_unit,
            "crediting_interest": crediting_interest,
            "minimum_dormant_amount": minimum_dormant_amount,
            "dormant_period": dormant_period,
            "dormant_period_unit": dormant_period_unit,
            "statement_format": statement_format,
            "statement_tenor": statement_tenor,
            "statement_tenor_unit": statement_tenor_unit,
            "inital_depost_amount": inital_depost_amount,
            "tariff_code": tariff_code,
            "group_id": group_id
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload