from datetime import datetime

class CreditFOPayload(object):
    def crd_plo(self, product_limit_code=None, product_limit_name=None, customer_type=None, customer_code=None, reference_number=None, limit_type=None, currency_code=None, limit_amount=None, accounting_group=None, secure_type=None, secure_rate=None, description=None, exchange_rate=None, amount=None):
        if not product_limit_code:
            product_limit_code = ''
        if not product_limit_name:
            product_limit_name = ''
        if not customer_type:
            customer_type = ''
        if not customer_code:
            customer_code = ''
        if not reference_number:
            reference_number = ''
        if not limit_type:
            limit_type = ''
        if not currency_code:
            currency_code = ''
        if not limit_amount:
            limit_amount = 0
        if not accounting_group:
            accounting_group = 0
        if not secure_type:
            secure_type = ''
        if not secure_rate:
            secure_rate = 0
        if not description:
            description = ''
        if not exchange_rate:
            exchange_rate = 0
        if not amount:
            amount = 0
        payload = {
            "product_limit_code": product_limit_code,
            "product_limit_name": product_limit_name,
            "customer_type": customer_type,
            "customer_code": customer_code,
            "reference_number": reference_number,
            "limit_type": limit_type,
            "currency_code": currency_code,
            "limit_amount": limit_amount,
            "accounting_group": accounting_group,
            "secure_type": secure_type,
            "secure_rate": secure_rate,
            "description": description,
            "exchange_rate": exchange_rate,
            "amount": amount
        }
        return payload

    def crd_pla(self, product_limit_code=None, product_limit_name=None, customer_type=None, customer_code=None, reference_number=None, currency_code=None, credit_limit=None, limit_type=None, product_status=None, description=None, customer_name=None, amount=None, exchange_rate=None):
        if not product_limit_code:
            product_limit_code = ''
        if not product_limit_name:
            product_limit_name = ''
        if not customer_type:
            customer_type = ''
        if not customer_code:
            customer_code = ''
        if not reference_number:
            reference_number = ''
        if not currency_code:
            currency_code = ''
        if not credit_limit:
            credit_limit = 0
        if not limit_type:
            limit_type = ''
        if not product_status:
            product_status = ''
        if not description:
            description = ''
        if not customer_name:
            customer_name = ''
        if not amount:
            amount = 0
        if not exchange_rate:
            exchange_rate = 0
        payload = {
            "product_limit_code": product_limit_code,
            "product_limit_name": product_limit_name,
            "customer_type": customer_type,
            "customer_code": customer_code,
            "reference_number": reference_number,
            "currency_code": currency_code,
            "credit_limit": credit_limit,
            "limit_type": limit_type,
            "product_status": product_status,
            "description": description,
            "customer_name": customer_name,
            "amount": amount,
            "exchange_rate": exchange_rate
        }
        return payload

    def crd_splo(self, sub_product_limit_code=None, product_limit_code=None, sub_product_limit_name=None, customer_type=None, currency_code=None, reference_number=None, customer_code=None, limit_amount=None, credit_facility=None, description=None, exchange_rate=None, amount=None):
        if not sub_product_limit_code:
            sub_product_limit_code = ''
        if not product_limit_code:
            product_limit_code = ''
        if not sub_product_limit_name:
            sub_product_limit_name = ''
        if not customer_type:
            customer_type = ''
        if not currency_code:
            currency_code = ''
        if not reference_number:
            reference_number = ''
        if not customer_code:
            customer_code = ''
        if not limit_amount:
            limit_amount = 0
        if not credit_facility:
            credit_facility = ''
        if not description:
            description = ''
        if not exchange_rate:
            exchange_rate = 0
        if not amount:
            amount = 0
        payload = {
            "sub_product_limit_code": sub_product_limit_code,
            "product_limit_code": product_limit_code,
            "sub_product_limit_name": sub_product_limit_name,
            "customer_type": customer_type,
            "currency_code": currency_code,
            "reference_number": reference_number,
            "customer_code": customer_code,
            "limit_amount": limit_amount,
            "credit_facility": credit_facility,
            "description": description,
            "exchange_rate": exchange_rate,
            "amount": amount
        }
        return payload

    def crd_spla(self, sub_product_limit_code=None, sub_product_limit_name=None, customer_type=None, reference_number=None, customer_code=None, product_limit_code=None, currency_code=None, credit_limit=None, product_limit_status=None, description=None, amount=None, exchange_rate=None):
        if not sub_product_limit_code:
            sub_product_limit_code = ''
        if not sub_product_limit_name:
            sub_product_limit_name = ''
        if not customer_type:
            customer_type = ''
        if not reference_number:
            reference_number = ''
        if not customer_code:
            customer_code = ''
        if not product_limit_code:
            product_limit_code = ''
        if not currency_code:
            currency_code = ''
        if not credit_limit:
            credit_limit = 0
        if not product_limit_status:
            product_limit_status = ''
        if not description:
            description = ''
        if not amount:
            amount = 0
        if not exchange_rate:
            exchange_rate = 0
        payload = {
            "sub_product_limit_code": sub_product_limit_code,
            "sub_product_limit_name": sub_product_limit_name,
            "customer_type": customer_type,
            "reference_number": reference_number,
            "customer_code": customer_code,
            "product_limit_code": product_limit_code,
            "currency_code": currency_code,
            "credit_limit": credit_limit,
            "product_limit_status": product_limit_status,
            "description": description,
            "amount": amount,
            "exchange_rate": exchange_rate
        }
        return payload

    def crd_opn(self, account_number=None, customer_type=None, customer_code=None, sub_product_limit_code=None, catalog_code=None, catalog_name=None, credit_facility=None, sub_product=None, credit_classification=None, seq_number=None, currency_code=None, account_holder_name=None, maximum_limit=None, credit_limit=None, margin=None, from_date=None, to_date=None, principal_first_date=None, int_first_date=None, amount=None, exchange_rate=None, branch_code=None, product_tenor_type=None, business_purpose_code=None, description=None):
        if not account_number:
            account_number = ''
        if not customer_type:
            customer_type = ''
        if not customer_code:
            customer_code = ''
        if not sub_product_limit_code:
            sub_product_limit_code = ''
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not credit_facility:
            credit_facility = ''
        if not sub_product:
            sub_product = ''
        if not credit_classification:
            credit_classification = ''
        if not seq_number:
            seq_number = None
        if not currency_code:
            currency_code = ''
        if not account_holder_name:
            account_holder_name = ''
        if not maximum_limit:
            maximum_limit = 0
        if not credit_limit:
            credit_limit = 0
        if not margin:
            margin = 0
        if not from_date:
            from_date = ''
        if not to_date:
            to_date = ''
        if not principal_first_date:
            principal_first_date = ''
        if not int_first_date:
            int_first_date = ''
        if not amount:
            amount = 0
        if not exchange_rate:
            exchange_rate = 0
        if not branch_code:
            branch_code = ''
        if not product_tenor_type:
            product_tenor_type = ''
        if not business_purpose_code:
            business_purpose_code = ''
        if not description:
            description = ''
        payload = {
            "account_number": account_number,
            "customer_type": customer_type,
            "customer_code": customer_code,
            "sub_product_limit_code": sub_product_limit_code,
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "credit_facility": credit_facility,
            "sub_product": sub_product,
            "credit_classification": credit_classification,
            "seq_number": seq_number,
            "currency_code": currency_code,
            "account_holder_name": account_holder_name,
            "maximum_limit": maximum_limit,
            "credit_limit": credit_limit,
            "margin": margin,
            "from_date": from_date,
            "to_date": to_date,
            "principal_first_date": principal_first_date,
            "int_first_date": int_first_date,
            "amount": amount,
            "exchange_rate": exchange_rate,
            "branch_code": branch_code,
            "product_tenor_type": product_tenor_type,
            "business_purpose_code": business_purpose_code,
            "description": description
        }
        return payload

    def crd_apr(self, account_number=None, customer_type=None, account_holder_name=None, catalog_code=None, catalog_name=None, seq_number=None, currency_code=None, credit_limit=None, deposit_account=None, currency_of_credit_account=None, amount=None, exchange_rate=None, sub_product_limit_code=None, description=None, fee_data=None):
        if not account_number:
            account_number = ''
        if not customer_type:
            customer_type = ''
        if not account_holder_name:
            account_holder_name = ''
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not seq_number:
            seq_number = 0
        if not currency_code:
            currency_code = ''
        if not credit_limit:
            credit_limit = 0
        if not deposit_account:
            deposit_account = None
        if not currency_of_credit_account:
            currency_of_credit_account = None
        if not amount:
            amount = 0
        if not exchange_rate:
            exchange_rate = 0
        if not sub_product_limit_code:
            sub_product_limit_code = ''
        if not description:
            description = ''
        if not fee_data:
            fee_data = None
        payload = {
            "account_number": account_number,
            "customer_type": customer_type,
            "account_holder_name": account_holder_name,
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "seq_number": seq_number,
            "currency_code": currency_code,
            "credit_limit": credit_limit,
            "deposit_account": deposit_account,
            "currency_of_credit_account": currency_of_credit_account,
            "amount": amount,
            "exchange_rate": exchange_rate,
            "sub_product_limit_code": sub_product_limit_code,
            "description": description,
            "fee_data": []
        }
        return payload

    def crd_tdr(self, credit_account=None, disbursement_amount_deposit=None, deposit_account=None, deposit_account_name=None, currency_code=None, cross_rate=None, deposit_amount=None, exchange_rate=None, disbursement_amount_equivalent_in_bcy=None, receiver_name=None, receiver_code=None, receiver_address=None, home=None, office=None, values_date=None, currency_of_credit_account=None, amount=None, exchange_rate_debit=None, repidtype=None, remaining_provision_amount=None, total_principal_amount=None, description=None):
        if not credit_account:
            credit_account = ''
        if not disbursement_amount_deposit:
            disbursement_amount_deposit = 0
        if not deposit_account:
            deposit_account = ''
        if not deposit_account_name:
            deposit_account_name = ''
        if not currency_code:
            currency_code = ''
        if not cross_rate:
            cross_rate = 0
        if not deposit_amount:
            deposit_amount = 0
        if not exchange_rate:
            exchange_rate = 0
        if not disbursement_amount_equivalent_in_bcy:
            disbursement_amount_equivalent_in_bcy = 0
        if not receiver_name:
            receiver_name = ''
        if not receiver_code:
            receiver_code = ''
        if not receiver_address:
            receiver_address = ''
        if not home:
            home = ''
        if not office:
            office = ''
        if not values_date:
            values_date = ''
        if not currency_of_credit_account:
            currency_of_credit_account = ''
        if not amount:
            amount = 0
        if not exchange_rate_debit:
            exchange_rate_debit = 0
        if not repidtype:
            repidtype = ''
        if not remaining_provision_amount:
            remaining_provision_amount = 0
        if not total_principal_amount:
            total_principal_amount = 0
        if not description:
            description = ''
        payload = {
            "credit_account": credit_account,
            "disbursement_amount_deposit": disbursement_amount_deposit,
            "deposit_account": deposit_account,
            "deposit_account_name": deposit_account_name,
            "currency_code": currency_code,
            "cross_rate": cross_rate,
            "deposit_amount": deposit_amount,
            "exchange_rate": exchange_rate,
            "disbursement_amount_equivalent_in_bcy": disbursement_amount_equivalent_in_bcy,
            "receiver_name": receiver_name,
            "receiver_code": receiver_code,
            "receiver_address": receiver_address,
            "receiver_description": {
                "home": home,
                "office": office
            },
            "values_date": values_date,
            "currency_of_credit_account": currency_of_credit_account,
            "amount": amount,
            "exchange_rate_debit": exchange_rate_debit,
            "repidtype": repidtype,
            "remaining_provision_amount": remaining_provision_amount,
            "total_principal_amount": total_principal_amount,
            "description": description
        }
        return payload