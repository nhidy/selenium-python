from datetime import datetime

class MortgageFOPayload(object):
    def mtg_opn(self, account_number=None, account_name=None, customer_type=None, customer_code=None, catalog_name=None, catalog_code=None, collateral_asset_type=None, collateral_asset_class=None, security_paper_type=None, currency_code=None, collateral_rate=None, risk_allocation_rate=None, collateral_asset_value=None, market_value=None, book_value=None, cc_contract=None, cc_amount=None, seq_number=None, reference_number=None, location=None, legal_local_address=None, legal_address=None, expiry_date=None, policy_amount=None, company_issues_policy=None, policy_number=None, evaluate_by=None, evaluate_method=None, evaluate_date=None, new_evaluate_date=None, insurance=None, description=None, book_currency_code=None, value_date=None):
        if not account_number:
            account_number  =  ''
        if not account_name:
            account_name  =  ''
        if not customer_type:
            customer_type  =  ''
        if not customer_code:
            customer_code  =  ''
        if not catalog_name:
            catalog_name  =  ''
        if not catalog_code:
            catalog_code  =  ''
        if not collateral_asset_type:
            collateral_asset_type  =  ''
        if not collateral_asset_class:
            collateral_asset_class  =  ''
        if not security_paper_type:
            security_paper_type  =  ''
        if not currency_code:
            currency_code  =  ''
        if not collateral_rate:
            collateral_rate =  0
        if not risk_allocation_rate:
            risk_allocation_rate =  0
        if not collateral_asset_value:
            collateral_asset_value =  0
        if not market_value:
            market_value =  0
        if not book_value:
            book_value =  0
        if not cc_contract:
            cc_contract  =  ''
        if not cc_amount:
            cc_amount =  0
        if not seq_number:
            seq_number =  None
        if not reference_number:
            reference_number  =  ''
        if not location:
            location  =  ''
        if not legal_local_address:
            legal_local_address  =  ''
        if not legal_address:
            legal_address  =  ''
        if not expiry_date:
            expiry_date  =  ''
        if not policy_amount:
            policy_amount =  0
        if not company_issues_policy:
            company_issues_policy  =  ''
        if not policy_number:
            policy_number  =  ''
        if not evaluate_by:
            evaluate_by  =  ''
        if not evaluate_method:
            evaluate_method  =  ''
        if not evaluate_date:
            evaluate_date  =  ''
        if not new_evaluate_date:
            new_evaluate_date  =  ''
        if not insurance:
            insurance  =  ''
        if not description:
            description  =  ''
        if not book_currency_code:
            book_currency_code  =  ''
        if not value_date:
            value_date  =  ''
        payload = {
            "account_number": account_number,
            "account_name": account_name,
            "customer_type": customer_type,
            "customer_code": customer_code,
            "catalog_name": catalog_name,
            "catalog_code": catalog_code,
            "collateral_asset_type": collateral_asset_type,
            "collateral_asset_class": collateral_asset_class,
            "security_paper_type": security_paper_type,
            "currency_code": currency_code,
            "collateral_rate": collateral_rate,
            "risk_allocation_rate": risk_allocation_rate,
            "collateral_asset_value": collateral_asset_value,
            "market_value": market_value,
            "book_value": book_value,
            "cc_contract": cc_contract,
            "cc_amount": cc_amount,
            "seq_number": seq_number,
            "reference_number": reference_number,
            "location": location,
            "legal_local_address": legal_local_address,
            "legal_address": legal_address,
            "expiry_date": expiry_date,
            "policy_amount": policy_amount,
            "company_issues_policy": company_issues_policy,
            "policy_number": policy_number,
            "evaluate_by": evaluate_by,
            "evaluate_method": evaluate_method,
            "evaluate_date": evaluate_date,
            "new_evaluate_date": new_evaluate_date,
            "insurance": insurance,
            "description": description,
            "book_currency_code": book_currency_code,
            "value_date": value_date
        }
        return payload