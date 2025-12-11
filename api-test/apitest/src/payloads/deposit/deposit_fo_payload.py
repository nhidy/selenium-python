from datetime import datetime

class DepositFOPayload(object):
    # def dpt_opn(self, account_number=None, customer_type=None, customer_code=None, catalog_code=None, catalog_name=None, deposit_type=None, master_fd_account=None, deposit_purpose=None, account_type=None, seq_number=None, account_name=None, business_purpose_code=None, rollover=None, auto_transfer_option=None, to_account_number=None, description=None, deposit_sub_type=None, reason_of_account_opening=None, is_restricted=None, im_banking=None, mpu_card=None, pc_book=None, wallet=None):
    #     if not account_number:
    #         account_number=''
    #     if not customer_type:
    #         customer_type=''
    #     if not customer_code:
    #         customer_code=''
    #     if not catalog_code:
    #         catalog_code=''
    #     if not catalog_name:
    #         catalog_name=''
    #     if not deposit_type:
    #         deposit_type=''
    #     if not master_fd_account:
    #         master_fd_account=''
    #     if not deposit_purpose:
    #         deposit_purpose=''
    #     if not account_type:
    #         account_type=''
    #     if not seq_number:
    #         seq_number=None
    #     if not account_name:
    #         account_name=''
    #     if not business_purpose_code:
    #         business_purpose_code=''
    #     if not rollover:
    #         rollover=''
    #     if not auto_transfer_option:
    #         auto_transfer_option=''
    #     if not to_account_number:
    #         to_account_number=''
    #     if not description:
    #         description=''
    #     if not reason_of_account_opening:
    #         reason_of_account_opening=''
    #     if not is_restricted:
    #         is_restricted=''
    #     if not im_banking:
    #         im_banking=''
    #     if not mpu_card:
    #         mpu_card=''
    #     if not pc_book:
    #         pc_book=''
    #     if not wallet:
    #         wallet=''
    #     payload = {
    #         "account_number": account_number,
    #         "customer_type": customer_type,
    #         "customer_code": customer_code,
    #         "catalog_code": catalog_code,
    #         "catalog_name": catalog_name,
    #         "deposit_type": deposit_type,
    #         "master_fd_account": master_fd_account,
    #         "deposit_purpose": deposit_purpose,
    #         "account_type": account_type,
    #         "seq_number": seq_number,
    #         "account_name": account_name,
    #         "business_purpose_code": business_purpose_code,
    #         "rollover": rollover,
    #         "auto_transfer_option": auto_transfer_option,
    #         "to_account_number": to_account_number,
    #         "description": description,
    #         "agent_hub_referral": "",
    #         "relation_customers": [],
    #         "user_approve": None,
    #         "deposit_sub_type": deposit_sub_type,
    #         "fee_data": None,
    #         "reason_of_account_opening": reason_of_account_opening,
    #         "is_restricted": is_restricted,
    #         "im_banking": im_banking,
    #         "mpu_card": mpu_card,
    #         "pc_book": pc_book,
    #         "wallet": wallet,
    #     }
    #     return payload

    def dpt_opn(self, customer_code, catalog_code, catalog_name, deposit_sub_type, amount=None, account_number=None, customer_type=None, customer_type_caption=None, employer_organization_name=None, deposit_type=None, agent_hub_referral=None, relation_customers=None, master_fd_account=None, deposit_purpose=None, account_type=None, account_type_caption=None, seq_number=None, account_name=None, business_purpose_code=None, rollover=None, auto_transfer_option=None, to_account_number=None, description=None, user_approve=None, fee_data=None, is_restricted=None, im_banking=None, mpu_card=None, pc_book=None, wallet=None, reason_of_account_opening=None, relationship_manager=None):
        if not amount:
            amount=1
        if not account_number:
            account_number=''
        if not customer_type:
            customer_type=''
        if not customer_type_caption:
            customer_type_caption=''
        if not employer_organization_name:
            employer_organization_name=''
        if not deposit_type:
            deposit_type='' # Current
        if not agent_hub_referral:
            agent_hub_referral=''
        if not relation_customers:
            relation_customers=[]
        if not master_fd_account:
            master_fd_account=None
        if not deposit_purpose:
            deposit_purpose=''
        if not account_type:
            account_type=''
        if not account_type_caption:
            account_type_caption=''
        if not seq_number:
            seq_number=None
        if not account_name:
            account_name=''
        if not business_purpose_code:
            business_purpose_code=''
        if not rollover:
            rollover=''
        if not auto_transfer_option:
            auto_transfer_option=''
        if not to_account_number:
            to_account_number=None
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        if not is_restricted:
            is_restricted=''
        if not im_banking:
            im_banking=False
        if not mpu_card:
            mpu_card=False
        if not pc_book:
            pc_book=False
        if not wallet:
            wallet=False
        if not reason_of_account_opening:
            reason_of_account_opening='Reason of Account Opening'
        if not relationship_manager:
            relationship_manager=''
        payload = {
            "amount": amount,
            "account_number": account_number,
            "customer_type": customer_type,
            "customer_type_caption": customer_type_caption,
            "customer_code": customer_code,
            "employer_organization_name": employer_organization_name,
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "deposit_type": deposit_type,
            "agent_hub_referral": agent_hub_referral,
            "relation_customers": relation_customers,
            "master_fd_account": master_fd_account,
            "deposit_purpose": deposit_purpose,
            "account_type": account_type,
            "account_type_caption": account_type_caption,
            "seq_number": seq_number,
            "account_name": account_name,
            "business_purpose_code": business_purpose_code,
            "rollover": rollover,
            "auto_transfer_option": auto_transfer_option,
            "to_account_number": to_account_number,
            "description": description,
            "user_approve": user_approve,
            "deposit_sub_type": deposit_sub_type,
            "fee_data": fee_data,
            "is_restricted": is_restricted,
            "im_banking": im_banking,
            "mpu_card": mpu_card,
            "pc_book": pc_book,
            "wallet": wallet,
            "extension_fields": {
                "reason_of_account_opening": reason_of_account_opening,
                "relationship_manager": relationship_manager
            }
        }
        return payload

    # def dpt_apr(self, account_number=None, account_holder_name=None, description=None):
    #     if not account_number:
    #         account_number = ''
    #     if not account_holder_name:
    #         account_holder_name = ''
    #     if not description:
    #         description = ''
    #     payload = {
    #         "account_number": account_number,
    #         "account_holder_name": account_holder_name,
    #         "description": description
    #     }
    #     return payload

    def dpt_apr(self, account_number, branch_name=None, account_holder_name=None, description=None, user_approve=None, account_type=None, catalog_code=None, deposit_sub_type=None, deposit_type=None, catalogue_name=None, created_by=None):
        if not branch_name:
            branch_name=''
        if not account_holder_name:
            account_holder_name=''
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not account_type:
            account_type=''
        if not catalog_code:
            catalog_code=''
        if not deposit_sub_type:
            deposit_sub_type=''
        if not deposit_type:
            deposit_type=''
        if not catalogue_name:
            catalogue_name=''
        if not created_by:
            created_by=''
        payload = {
            "account_number": account_number,
            "branch_name": branch_name,
            "account_holder_name": account_holder_name,
            "description": description,
            "user_approve": user_approve,
            "account_type": account_type,
            "catalog_code": catalog_code,
            "deposit_sub_type": deposit_sub_type,
            "deposit_type": deposit_type,
            "catalogue_name": catalogue_name,
            "created_by": created_by
        }
        return payload

    # def dpt_cdp(self, account_number=None, amount_deposit=None, amount=None, home=None, office=None, inclusive=None, depositor_address=None, identification_number=None, currency_deposit=None, values_date=None, customer_code=None, cash_amount_bcy=None, id_place=None, cash_exchange_rate=None, cash_amount=None, cash_currency=None, prepaid_interest=None, account_name=None, exchange_rate=None, cross_rate=None, deposit_type=None, interest_tenor_unit=None, commission=None, id_issue_date=None, description=None, fee_data=None):
    #     if not account_number:
    #         account_number = ''
    #     if not amount_deposit:
    #         amount_deposit=0
    #     if not amount:
    #         amount=0
    #     if not home:
    #         home = ''
    #     if not office:
    #         office = ''
    #     if not inclusive:
    #         inclusive = ''
    #     if not depositor_address:
    #         depositor_address = ''
    #     if not identification_number:
    #         identification_number = ''
    #     if not currency_deposit:
    #         currency_deposit = ''
    #     if not values_date:
    #         values_date = ''
    #     if not customer_code:
    #         customer_code = ''
    #     if not cash_amount_bcy:
    #         cash_amount_bcy=0
    #     if not id_place:
    #         id_place = ''
    #     if not cash_exchange_rate:
    #         cash_exchange_rate=0
    #     if not cash_amount:
    #         cash_amount=0
    #     if not cash_currency:
    #         cash_currency = ''
    #     if not prepaid_interest:
    #         prepaid_interest=0
    #     if not account_name:
    #         account_name = ''
    #     if not exchange_rate:
    #         exchange_rate=0
    #     if not cross_rate:
    #         cross_rate=0
    #     if not deposit_type:
    #         deposit_type = ''
    #     if not interest_tenor_unit:
    #         interest_tenor_unit = ''
    #     if not commission:
    #         commission=0
    #     if not id_issue_date:
    #         id_issue_date = ''
    #     if not description:
    #         description = ''
    #     if not fee_data:
    #         fee_data=None
    #     payload = {
    #         "account_number": account_number,
    #         "amount_deposit": amount_deposit,
    #         "amount": amount,
    #         "depositor_description": {
    #             "home": home,
    #             "office": office
    #         },
    #         "inclusive": inclusive,
    #         "depositor_address": depositor_address,
    #         "identification_number": identification_number,
    #         "currency_deposit": currency_deposit,
    #         "values_date": values_date,
    #         "customer_code": customer_code,
    #         "cash_amount_bcy": cash_amount_bcy,
    #         "id_place": id_place,
    #         "cash_exchange_rate": cash_exchange_rate,
    #         "cash_amount": cash_amount,
    #         "cash_currency": cash_currency,
    #         "prepaid_interest": prepaid_interest,
    #         "account_name": account_name,
    #         "exchange_rate": exchange_rate,
    #         "cross_rate": cross_rate,
    #         "deposit_type": deposit_type,
    #         "interest_tenor_unit": interest_tenor_unit,
    #         "commission": commission,
    #         "id_issue_date": id_issue_date,
    #         "description": description,
    #         "fee_data":[]
    #     }
    #     return payload

    def dpt_cdp(self, account_number, amount_deposit, cash_currency=None, branch_name=None, cross_rate=None, cash_amount=None, cash_exchange_rate=None, cash_amount_bcy=None, account_name=None, customer_code=None, depositor_address=None, home=None, office=None, description=None, values_date=None, identification_number=None, id_issue_date=None, id_place=None, deposit_type=None, currency_deposit=None, exchange_rate=None, amount=None, prepaid_interest=None, interest_tenor_unit=None, inclusive=None, commission=None, fee_data=None, user_approve=None):
        if not cash_currency:
            cash_currency=''
        if not branch_name:
            branch_name=''
        if not cross_rate:
            cross_rate=1
        if not cash_amount:
            cash_amount=0
        if not cash_exchange_rate:
            cash_exchange_rate=1
        if not cash_amount_bcy:
            cash_amount_bcy=0
        if not account_name:
            account_name=''
        if not customer_code:
            customer_code=''
        if not depositor_address:
            depositor_address=''
        if not home:
            home=''
        if not office:
            office=''
        if not description:
            description=''
        if not values_date:
            values_date=''
        if not identification_number:
            identification_number=''
        if not id_issue_date:
            id_issue_date=''
        if not id_place:
            id_place=''
        if not deposit_type:
            deposit_type=''
        if not currency_deposit:
            currency_deposit=''
        if not exchange_rate:
            exchange_rate=1
        if not amount:
            amount=0
        if not prepaid_interest:
            prepaid_interest=0
        if not interest_tenor_unit:
            interest_tenor_unit=''
        if not inclusive:
            inclusive=''
        if not commission:
            commission=0
        if not fee_data:
            fee_data=[]
        if not user_approve:
            user_approve=None
        payload = {
            "account_number": account_number,
            "amount_deposit": amount_deposit,
            "cash_currency": cash_currency,
            "branch_name": branch_name,
            "cross_rate": cross_rate,
            "cash_amount": cash_amount,
            "cash_exchange_rate": cash_exchange_rate,
            "cash_amount_bcy": cash_amount_bcy,
            "account_name": account_name,
            "customer_code": customer_code,
            "depositor_address": depositor_address,
            "depositor_description": {
                "home": home,
                "office": office
            },
            "description": description,
            "values_date": values_date,
            "identification_number": identification_number,
            "id_issue_date": id_issue_date,
            "id_place": id_place,
            "deposit_type": deposit_type,
            "currency_deposit": currency_deposit,
            "exchange_rate": exchange_rate,
            "amount": amount,
            "prepaid_interest": prepaid_interest,
            "interest_tenor_unit": interest_tenor_unit,
            "inclusive": inclusive,
            "commission": commission,
            "fee_data": fee_data,
            "user_approve": user_approve
        }
        return payload

    # def dpt_blk(self, account_number=None, depositor_name=None, depositor_id=None, depositor_address=None, home=None, office=None, depositor_balance=None, depositor_currency=None, block_reason=None, value_date=None, description=None):
    #     if not account_number: 	
    #         account_number = ''
    #     if not depositor_name: 	
    #         depositor_name = ''
    #     if not depositor_id: 	
    #         depositor_id = ''
    #     if not depositor_address: 	
    #         depositor_address = ''
    #     if not home:
    #         home = ''
    #     if not office:
    #         office = ''
    #     if not depositor_balance: 	
    #         depositor_balance = 0
    #     if not depositor_currency: 	
    #         depositor_currency = ''
    #     if not block_reason: 	
    #         block_reason = ''
    #     if not value_date: 	
    #         value_date = ''
    #     if not description: 	
    #         description = ''
    #     payload = {
    #         "account_number": account_number,
    #         "depositor_name": depositor_name,
    #         "depositor_id": depositor_id,
    #         "depositor_address": depositor_address,
    #         "depositor_description": {
    #             "home": home,
    #             "office": office
    #         },
    #         "depositor_balance": depositor_balance,
    #         "depositor_currency": depositor_currency,
    #         "block_reason": block_reason,
    #         "value_date": value_date,
    #         "description": description
    #     }
    #     return payload

    def dpt_blk(self, account_number=None, branch_name=None, depositor_name=None, depositor_id=None, depositor_address=None, home=None, office=None, depositor_balance=None, depositor_currency=None, description=None, block_reason=None, value_date=None, user_approve=None, amount=None):
        if not account_number:
            account_number=''
        if not branch_name:
            branch_name=''
        if not depositor_name:
            depositor_name=''
        if not depositor_id:
            depositor_id=''
        if not depositor_address:
            depositor_address=''
        if not home:
            home=''
        if not office:
            office=''
        if not depositor_balance:
            depositor_balance=0
        if not depositor_currency:
            depositor_currency='MMK'
        if not description:
            description=''
        if not block_reason:
            block_reason=''
        if not value_date:
            value_date=''
        if not user_approve:
            user_approve=None
        if not amount:
            amount=1
        payload = {
            "account_number": account_number,
            "branch_name": branch_name,
            "depositor_name": depositor_name,
            "depositor_id": depositor_id,
            "depositor_address": depositor_address,
            "depositor_description": {
                "home": home,
                "office": office
            },
            "depositor_balance": depositor_balance,
            "depositor_currency": depositor_currency,
            "description": description,
            "block_reason": block_reason,
            "value_date": value_date,
            "user_approve": user_approve,
            "amount": amount
        }
        return payload

    def dpt_trf(self, debit_account=None, balance_debit_account=None, available_balance_debit_account=None, account_linkage=None, amount_linkage=None, amount=None, t_exchange_rate_debit_account_bcy=None, amount_equivalent_in_bcy=None, credit_account=None, currency_of_debit_account=None, currency_of_credit_account=None, cross_rate=None, credit_amount=None, exchange_rate_credit_ac_bcy=None, amount_to_credit_bcy=None, debit_account_name=None, customer_code=None, customer_address=None, home=None, office=None, value_date=None, total_fee_credit_account=None, paper_number_of_debit=None, issue_date_of_debit=None, total_amount_payable=None, issue_place_of_debit=None, paper_number_of_credit=None, issue_date_of_credit=None, total_fee=None, issue_place_of_credit=None, credit_account_name=None, b_exchange_rate_debit_account_bcy=None, amount_debit_account_bcy=None, fee_data=None, description=None):
        if not debit_account:	
            debit_account = ''
        if not balance_debit_account:	
            balance_debit_account = 0
        if not available_balance_debit_account:	
            available_balance_debit_account = 0
        if not account_linkage:	
            account_linkage = ''
        if not amount_linkage:	
            amount_linkage = 0
        if not amount:	
            amount = 0
        if not t_exchange_rate_debit_account_bcy:	
            t_exchange_rate_debit_account_bcy = 0
        if not amount_equivalent_in_bcy:	
            amount_equivalent_in_bcy = 0
        if not credit_account:	
            credit_account = ''
        if not currency_of_debit_account:	
            currency_of_debit_account = ''
        if not currency_of_credit_account:	
            currency_of_credit_account = ''
        if not cross_rate:	
            cross_rate = 0
        if not credit_amount:	
            credit_amount = 0
        if not exchange_rate_credit_ac_bcy:	
            exchange_rate_credit_ac_bcy = 0
        if not amount_to_credit_bcy:	
            amount_to_credit_bcy = 0
        if not debit_account_name:	
            debit_account_name = ''
        if not customer_code:	
            customer_code = ''
        if not customer_address:	
            customer_address = ''
        if not home:	    
            home = ''
        if not office:	    
            office = ''
        if not value_date:	
            value_date = ''
        if not total_fee_credit_account:	
            total_fee_credit_account = 0
        if not paper_number_of_debit:	
            paper_number_of_debit = ''
        if not issue_date_of_debit:	
            issue_date_of_debit = ''
        if not total_amount_payable:	
            total_amount_payable = 0
        if not issue_place_of_debit:	
            issue_place_of_debit = ''
        if not paper_number_of_credit:	
            paper_number_of_credit = ''
        if not issue_date_of_credit:	
            issue_date_of_credit = ''
        if not total_fee:	total_fee = 0
        if not issue_place_of_credit:	
            issue_place_of_credit = ''
        if not credit_account_name:	
            credit_account_name = ''
        if not b_exchange_rate_debit_account_bcy:	
            b_exchange_rate_debit_account_bcy = 0
        if not amount_debit_account_bcy:	
            amount_debit_account_bcy = 0
        if not fee_data:	
            fee_data = None
        if not description:	
            description = ''
        payload = {
            "debit_account": debit_account,
            "balance_debit_account": balance_debit_account,
            "available_balance_debit_account": available_balance_debit_account,
            "account_linkage": account_linkage,
            "amount_linkage": amount_linkage,
            "amount": amount,
            "t_exchange_rate_debit_account_bcy": t_exchange_rate_debit_account_bcy,
            "amount_equivalent_in_bcy": amount_equivalent_in_bcy,
            "credit_account": credit_account,
            "currency_of_debit_account": currency_of_debit_account,
            "currency_of_credit_account": currency_of_credit_account,
            "cross_rate": cross_rate,
            "credit_amount": credit_amount,
            "exchange_rate_credit_ac_bcy": exchange_rate_credit_ac_bcy,
            "amount_to_credit_bcy": amount_to_credit_bcy,
            "debit_account_name": debit_account_name,
            "customer_code": customer_code,
            "customer_address": customer_address,
            "customer_description":	{
                "home": home,
                "office": office
            },
            "value_date": value_date,
            "total_fee_credit_account": total_fee_credit_account,
            "paper_number_of_debit": paper_number_of_debit,
            "issue_date_of_debit": issue_date_of_debit,
            "total_amount_payable": total_amount_payable,
            "issue_place_of_debit": issue_place_of_debit,
            "paper_number_of_credit": paper_number_of_credit,
            "issue_date_of_credit": issue_date_of_credit,
            "total_fee": total_fee,
            "issue_place_of_credit": issue_place_of_credit,
            "credit_account_name": credit_account_name,
            "b_exchange_rate_debit_account_bcy": b_exchange_rate_debit_account_bcy,
            "amount_debit_account_bcy": amount_debit_account_bcy,
            "fee_data": [],
            "description": description
        }
        return payload