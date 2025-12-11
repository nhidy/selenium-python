from datetime import datetime

class StoredProcedurePayload(object):
# ====================================== Workflow id FO ======================================
    def DPT_OPN(self, customer_code, catalog_code, catalog_name, deposit_sub_type, amount=None, account_number=None, customer_type=None, customer_type_caption=None, employer_organization_name=None, deposit_type=None, agent_hub_referral=None, relation_customers=None, master_fd_account=None, deposit_purpose=None, account_type=None, account_type_caption=None, seq_number=None, account_name=None, business_purpose_code=None, rollover=None, auto_transfer_option=None, to_account_number=None, description=None, user_approve=None, fee_data=None, is_restricted=None, im_banking=None, mpu_card=None, pc_book=None, wallet=None, reason_of_account_opening=None, relationship_manager=None):
        if not amount:
            amount=1
        if not account_number:
            account_number=''
        if not customer_type:
            customer_type='C'
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
            deposit_purpose='P'
        if not account_type:
            account_type='1'
        if not account_type_caption:
            account_type_caption=''
        if not seq_number:
            seq_number=None
        if not account_name:
            account_name=''
        if not business_purpose_code:
            business_purpose_code=''
        if not rollover:
            rollover='N'
        if not auto_transfer_option:
            auto_transfer_option='N'
        if not to_account_number:
            to_account_number=None
        if not description:
            description='1100: Open new deposit account'
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        if not is_restricted:
            is_restricted='N'
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

    def DPT_APR(self, account_number, branch_name=None, account_holder_name=None, description=None, user_approve=None, account_type=None, catalog_code=None, deposit_sub_type=None, deposit_type=None, catalogue_name=None, created_by=None):
        if not branch_name:
            branch_name=''
        if not account_holder_name:
            account_holder_name=''
        if not description:
            description='Approve deposit account'
        if not user_approve:
            user_approve=None
        if not account_type:
            account_type='Individual'
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

    def DPT_CDP(self, account_number, amount_deposit, cash_currency=None, branch_name=None, cross_rate=None, cash_amount=None, cash_exchange_rate=None, cash_amount_bcy=None, account_name=None, customer_code=None, depositor_address=None, home=None, office=None, description=None, values_date=None, identification_number=None, id_issue_date=None, id_place=None, deposit_type=None, currency_deposit=None, exchange_rate=None, amount=None, prepaid_interest=None, interest_tenor_unit=None, inclusive=None, commission=None, fee_data=None, user_approve=None):
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
            description='1110: Cash deposit'
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

    def DPT_MDP(self, account_number, amount_deposit, debit_accounting=None, branch_name=None, accounting_currency=None, cross_rate=None, acounting_amount=None, exchange_rate_of_accounting_bcy=None, accounting_amount_bcy=None, depositor_name=None, depositor_code=None, depositor_address=None, home=None, office=None, description=None, values_date=None, deposit_currency=None, exchange_rate_debit_account_bcy=None, amount_debit_account_bcy=None, accounting_currency1=None, user_approve=None, fee_data=None):
        if not debit_accounting:
            debit_accounting=''
        if not branch_name:
            branch_name=''
        if not accounting_currency:
            accounting_currency=''
        if not cross_rate:
            cross_rate=1
        if not acounting_amount:
            acounting_amount=0
        if not exchange_rate_of_accounting_bcy:
            exchange_rate_of_accounting_bcy=1
        if not accounting_amount_bcy:
            accounting_amount_bcy=0
        if not depositor_name:
            depositor_name=''
        if not depositor_code:
            depositor_code=''
        if not depositor_address:
            depositor_address=''
        if not home:
            home=''
        if not office:
            office=''
        if not description:
            description='1112: Miscellaneous deposit'
        if not values_date:
            values_date=''
        if not deposit_currency:
            deposit_currency=''
        if not exchange_rate_debit_account_bcy:
            exchange_rate_debit_account_bcy=1
        if not amount_debit_account_bcy:
            amount_debit_account_bcy=0
        if not accounting_currency1:
            accounting_currency1=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        payload = {
            "account_number": account_number,
            "amount_deposit": amount_deposit,
            "debit_accounting": debit_accounting,
            "branch_name": branch_name,
            "accounting_currency": accounting_currency,
            "cross_rate": cross_rate,
            "acounting_amount": acounting_amount,
            "exchange_rate_of_accounting_bcy": exchange_rate_of_accounting_bcy,
            "accounting_amount_bcy": accounting_amount_bcy,
            "depositor_name": depositor_name,
            "depositor_code": depositor_code,
            "depositor_address": depositor_address,
            "depositor_description": {
                "home": home,
                "office": office
            },
            "description": description,
            "values_date": values_date,
            "deposit_currency": deposit_currency,
            "exchange_rate_debit_account_bcy": exchange_rate_debit_account_bcy,
            "amount_debit_account_bcy": amount_debit_account_bcy,
            "accounting_currency1": accounting_currency1,
            "user_approve": user_approve,
            "fee_data": fee_data
        }
        return payload

    def DPT_SBI(self, account_number, serial_no, branch_name=None, description=None, stock_type=None, stock_prefix=None, currency_code=None, user_approve=None, fee_data=None, account_number_for_fee=None, method=None):
        if not account_number:
            account_number=''
        if not branch_name:
            branch_name=''
        if not serial_no:
            serial_no=''
        if not description:
            description='11802: Deposit savings book issue'
        if not stock_type:
            stock_type='P'
        if not stock_prefix:
            stock_prefix=''
        if not currency_code:
            currency_code=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        if not account_number_for_fee:
            account_number_for_fee=''
        if not method:
            method='CSH'
        payload = {
            "account_number": account_number,
            "branch_name": branch_name,
            "serial_no": serial_no,
            "description": description,
            "stock_type": stock_type,
            "stock_prefix": stock_prefix,
            "currency_code": currency_code,
            "user_approve": user_approve,
            "fee_data": fee_data,
            "account_number_for_fee": account_number_for_fee,
            "method": method
        }
        return payload

    def DPT_CWR(self, account_number, withdraw_amount, account_linkage=None, amount_linkage=None, current_balance=None, available_balance=None, cash_currency=None, cross_rate=None, cash_amount=None, exchange_rate=None, cash_amount_bcy=None, withdrawer_name=None, withdrawer_id=None, withdrawer_address=None, home=None, office=None, description=None, id_issue_date=None, passbook_number=None, id_place=None, identification_number=None, value_date=None, currency_of_deposit_account=None, exchange_rate_debit_account_bcy=None, amount_debit_account_bcy=None, interest_from_earlywdr=None, commission=None, due_date=None, interest_prepaid=None, total_vat_for_cash=None, fee_data=None, user_approve=None, branch_name=None):
        if not current_balance:
            current_balance=None
        if not available_balance:
            available_balance=None
        if not cash_currency:
            cash_currency=''
        if not cross_rate:
            cross_rate=1
        if not cash_amount:
            cash_amount=0
        if not exchange_rate:
            exchange_rate=1
        if not cash_amount_bcy:
            cash_amount_bcy=0
        if not withdrawer_name:
            withdrawer_name=''
        if not withdrawer_id:
            withdrawer_id=''
        if not withdrawer_address:
            withdrawer_address=''
        if not home:
            home=''
        if not office:
            office=''
        if not description:
            description='1120: Cash withdrawal'
        if not id_issue_date:
            id_issue_date=''
        if not passbook_number:
            passbook_number=''
        if not id_place:
            id_place=''
        if not identification_number:
            identification_number=''
        if not value_date:
            value_date=''
        if not currency_of_deposit_account:
            currency_of_deposit_account=''
        if not exchange_rate_debit_account_bcy:
            exchange_rate_debit_account_bcy=1
        if not amount_debit_account_bcy:
            amount_debit_account_bcy=0
        if not interest_from_earlywdr:
            interest_from_earlywdr=0
        if not commission:
            commission=0
        if not due_date:
            due_date=''
        if not interest_prepaid:
            interest_prepaid=0
        if not total_vat_for_cash:
            total_vat_for_cash='0'
        if not account_linkage:
            account_linkage=''
        if not amount_linkage:
            amount_linkage=0
        if not fee_data:
            fee_data=[]
        if not user_approve:
            user_approve=None
        if not branch_name:
            branch_name=''
        payload = {
            "account_number": account_number,
            "current_balance": current_balance,
            "available_balance": available_balance,
            "withdraw_amount": withdraw_amount,
            "cash_currency": cash_currency,
            "cross_rate": cross_rate,
            "cash_amount": cash_amount,
            "exchange_rate": exchange_rate,
            "cash_amount_bcy": cash_amount_bcy,
            "withdrawer_name": withdrawer_name,
            "withdrawer_id": withdrawer_id,
            "withdrawer_address": withdrawer_address,
            "withdrawer_description": {
                "home": home,
                "office": office
            },
            "description": description,
            "id_issue_date": id_issue_date,
            "passbook_number": passbook_number,
            "id_place": id_place,
            "identification_number": identification_number,
            "value_date": value_date,
            "currency_of_deposit_account": currency_of_deposit_account,
            "exchange_rate_debit_account_bcy": exchange_rate_debit_account_bcy,
            "amount_debit_account_bcy": amount_debit_account_bcy,
            "interest_from_earlywdr": interest_from_earlywdr,
            "commission": commission,
            "due_date": due_date,
            "interest_prepaid": interest_prepaid,
            "total_vat_for_cash": total_vat_for_cash,
            "account_linkage": account_linkage,
            "amount_linkage": amount_linkage,
            "fee_data": fee_data,
            "user_approve": user_approve,
            "branch_name": branch_name
        }
        return payload

    def DPT_MWR(self, account_number, withdraw_amount, credit_accounting, account_linkage=None, amount_linkage=None, current_balance=None, available_balance=None, interest_prepaid=None, interest_earlywdr=None, accounting_currency=None, passbook_number=None, cross_rate=None, accounting_amount=None, exchange_rate_of_accounting_bcy=None, amount_equivalent_in_bcy=None, withdrawer_name=None, withdrawer_code=None, withdrawer_address=None, home=None, office=None, description=None, values_date=None, currency_of_deposit_account=None, exchange_rate_debit_account_bcy=None, amount_debit_account_bcy=None, branch_code=None, fee_data=None, user_approve=None, branch_name=None):
        if not current_balance:
            current_balance=None
        if not available_balance:
            available_balance=None
        if not interest_prepaid:
            interest_prepaid=0
        if not interest_earlywdr:
            interest_earlywdr=0
        if not accounting_currency:
            accounting_currency=''
        if not passbook_number:
            passbook_number=''
        if not cross_rate:
            cross_rate=1
        if not accounting_amount:
            accounting_amount=0
        if not exchange_rate_of_accounting_bcy:
            exchange_rate_of_accounting_bcy=1
        if not amount_equivalent_in_bcy:
            amount_equivalent_in_bcy=0
        if not withdrawer_name:
            withdrawer_name=''
        if not withdrawer_code:
            withdrawer_code=''
        if not withdrawer_address:
            withdrawer_address=''
        if not home:
            home=''
        if not office:
            office=''
        if not description:
            description='1122: Miscellaneous withdrawal'
        if not values_date:
            values_date=''
        if not currency_of_deposit_account:
            currency_of_deposit_account=''
        if not exchange_rate_debit_account_bcy:
            exchange_rate_debit_account_bcy=1
        if not amount_debit_account_bcy:
            amount_debit_account_bcy=0
        if not account_linkage:
            account_linkage=''
        if not amount_linkage:
            amount_linkage=0
        if not branch_code:
            branch_code=''
        if not fee_data:
            fee_data=[]
        if not user_approve:
            user_approve=None
        if not branch_name:
            branch_name=''
        payload = {
            "account_number": account_number,
            "current_balance": current_balance,
            "available_balance": available_balance,
            "interest_prepaid": interest_prepaid,
            "interest_earlywdr": interest_earlywdr,
            "withdraw_amount": withdraw_amount,
            "credit_accounting": credit_accounting,
            "accounting_currency": accounting_currency,
            "passbook_number": passbook_number,
            "cross_rate": cross_rate,
            "accounting_amount": accounting_amount,
            "exchange_rate_of_accounting_bcy": exchange_rate_of_accounting_bcy,
            "amount_equivalent_in_bcy": amount_equivalent_in_bcy,
            "withdrawer_name": withdrawer_name,
            "withdrawer_code": withdrawer_code,
            "withdrawer_address": withdrawer_address,
            "withdrawer_description": {
                "home": home,
                "office": office
            },
            "description": description,
            "values_date": values_date,
            "currency_of_deposit_account": currency_of_deposit_account,
            "exchange_rate_debit_account_bcy": exchange_rate_debit_account_bcy,
            "amount_debit_account_bcy": amount_debit_account_bcy,
            "account_linkage": account_linkage,
            "amount_linkage": amount_linkage,
            "branch_code": branch_code,
            "fee_data": fee_data,
            "user_approve": user_approve,
            "branch_name": branch_name
        }
        return payload

    def DPT_TRF(self, debit_account, amount, credit_account, account_linkage=None, amount_linkage=None, balance_debit_account=None, available_balance_debit_account=None, passbook_number=None, t_exchange_rate_debit_account_bcy=None, amount_equivalent_in_bcy=None, currency_of_debit_account=None, currency_of_credit_account=None, cross_rate=None, credit_amount=None, exchange_rate_credit_ac_bcy=None, amount_to_credit_bcy=None, debit_account_name=None, customer_code=None, customer_address=None, home=None, office=None, description=None, value_date=None, total_fee_credit_account=None, paper_number_of_debit=None, issue_date_of_debit=None, total_amount_payable=None, issue_place_of_debit=None, paper_number_of_credit=None, issue_date_of_credit=None, total_fee=None, issue_place_of_credit=None, credit_account_name=None, b_exchange_rate_debit_account_bcy=None, amount_debit_account_bcy=None, fee_data=None, user_approve=None, branch_name=None):
        if not balance_debit_account:
            balance_debit_account=None
        if not available_balance_debit_account:
            available_balance_debit_account=None
        if not passbook_number:
            passbook_number=''
        if not t_exchange_rate_debit_account_bcy:
            t_exchange_rate_debit_account_bcy=1
        if not amount_equivalent_in_bcy:
            amount_equivalent_in_bcy=0
        if not currency_of_debit_account:
            currency_of_debit_account=''
        if not currency_of_credit_account:
            currency_of_credit_account=''
        if not cross_rate:
            cross_rate=1
        if not credit_amount:
            credit_amount=0
        if not exchange_rate_credit_ac_bcy:
            exchange_rate_credit_ac_bcy=1
        if not amount_to_credit_bcy:
            amount_to_credit_bcy=0
        if not debit_account_name:
            debit_account_name=''
        if not customer_code:
            customer_code=''
        if not customer_address:
            customer_address=''
        if not home:
            home=''
        if not office:
            office=''
        if not description:
            description='1130: Transfer from deposit account to deposit account'
        if not value_date:
            value_date=''
        if not total_fee_credit_account:
            total_fee_credit_account=0
        if not paper_number_of_debit:
            paper_number_of_debit=''
        if not issue_date_of_debit:
            issue_date_of_debit=''
        if not total_amount_payable:
            total_amount_payable=0
        if not issue_place_of_debit:
            issue_place_of_debit=''
        if not paper_number_of_credit:
            paper_number_of_credit=''
        if not issue_date_of_credit:
            issue_date_of_credit=''
        if not total_fee:
            total_fee=0
        if not issue_place_of_credit:
            issue_place_of_credit=''
        if not credit_account_name:
            credit_account_name=''
        if not b_exchange_rate_debit_account_bcy:
            b_exchange_rate_debit_account_bcy=1
        if not amount_debit_account_bcy:
            amount_debit_account_bcy=0
        if not account_linkage:
            account_linkage=''
        if not amount_linkage:
            amount_linkage=0
        if not fee_data:
            fee_data=[]
        if not user_approve:
            user_approve=None
        if not branch_name:
            branch_name=''
        payload = {
            "debit_account": debit_account,
            "balance_debit_account": balance_debit_account,
            "available_balance_debit_account": available_balance_debit_account,
            "account_linkage": account_linkage,
            "passbook_number": passbook_number,
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
            "customer_description": {
                "home": home,
                "office": office
            },
            "description": description,
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
            "fee_data": fee_data,
            "user_approve": user_approve,
            "branch_name": branch_name
        }
        return payload

    def DPT_CER(self, account_number, cerfiticate_serial, stock_prefix=None, description=None, user_approve=None, fee_data=None, branch_name=None, account_number_for_fee=None, currency_code=None, method=None):
        if not stock_prefix:
            stock_prefix=''
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        if not branch_name:
            branch_name=''
        if not account_number_for_fee:
            account_number_for_fee=''
        if not currency_code:
            currency_code=''
        if not method:
            method=''
        payload = {
            "account_number": account_number,
            "cerfiticate_serial": cerfiticate_serial,
            "stock_prefix": stock_prefix,
            "description": description,
            "user_approve": user_approve,
            "fee_data": fee_data,
            "branch_name": branch_name,
            "account_number_for_fee": account_number_for_fee,
            "currency_code": currency_code,
            "method": method
        }
        return payload

    def DPT_CWC(self, cheque_no, account_number, cheque_amount, account_linkage=None, amount_linkage=None, stock_prefix=None, current_balance=None, available_balance=None, cash_currency=None, cross_rate=None, cash_amount=None, exchange_rate=None, cash_amount_bcy=None, withdrawer_name=None, withdrawer_id=None, withdrawer_address=None, home=None, office=None, description=None, id_issue_date=None, id_place=None, identification_number=None, value_date=None, currency_of_deposit_account=None, exchange_rate_debit_account_bcy=None, amount_debit_account_bcy=None, commission=None, interest_from_earlywdr=None, due_date=None, interest_prepaid=None, total_vat_for_cash=None, fee_data=None, user_approve=None, branch_name=None):
        if not stock_prefix:
            stock_prefix=''
        if not current_balance:
            current_balance=None
        if not available_balance:
            available_balance=None
        if not cash_currency:
            cash_currency=''
        if not cross_rate:
            cross_rate=1
        if not cash_amount:
            cash_amount=0
        if not exchange_rate:
            exchange_rate=1
        if not cash_amount_bcy:
            cash_amount_bcy=0
        if not withdrawer_name:
            withdrawer_name=''
        if not withdrawer_id:
            withdrawer_id=''
        if not withdrawer_address:
            withdrawer_address=''
        if not home:
            home=''
        if not office:
            office=''
        if not description:
            description='1121: Cash withdrawal by cheque'
        if not id_issue_date:
            id_issue_date=''
        if not id_place:
            id_place=''
        if not identification_number:
            identification_number=''
        if not value_date:
            value_date=''
        if not currency_of_deposit_account:
            currency_of_deposit_account=''
        if not exchange_rate_debit_account_bcy:
            exchange_rate_debit_account_bcy=1
        if not amount_debit_account_bcy:
            amount_debit_account_bcy=0
        if not commission:
            commission=0
        if not interest_from_earlywdr:
            interest_from_earlywdr=0
        if not due_date:
            due_date=''
        if not interest_prepaid:
            interest_prepaid=0
        if not total_vat_for_cash:
            total_vat_for_cash='0'
        if not account_linkage:
            account_linkage=''
        if not amount_linkage:
            amount_linkage=0
        if not fee_data:
            fee_data=[]
        if not user_approve:
            user_approve=None
        if not branch_name:
            branch_name=''
        payload = {
            "stock_prefix": stock_prefix,
            "cheque_no": cheque_no,
            "account_number": account_number,
            "current_balance": current_balance,
            "available_balance": available_balance,
            "cheque_amount": cheque_amount,
            "cash_currency": cash_currency,
            "cross_rate": cross_rate,
            "cash_amount": cash_amount,
            "exchange_rate": exchange_rate,
            "cash_amount_bcy": cash_amount_bcy,
            "withdrawer_name": withdrawer_name,
            "withdrawer_id": withdrawer_id,
            "withdrawer_address": withdrawer_address,
            "withdrawer_description": {
                "home": home,
                "office": office
            },
            "description": description,
            "id_issue_date": id_issue_date,
            "id_place": id_place,
            "identification_number": identification_number,
            "value_date": value_date,
            "currency_of_deposit_account": currency_of_deposit_account,
            "exchange_rate_debit_account_bcy": exchange_rate_debit_account_bcy,
            "amount_debit_account_bcy": amount_debit_account_bcy,
            "commission": commission,
            "interest_from_earlywdr": interest_from_earlywdr,
            "due_date": due_date,
            "interest_prepaid": interest_prepaid,
            "total_vat_for_cash": total_vat_for_cash,
            "account_linkage": account_linkage,
            "amount_linkage": amount_linkage,
            "fee_data": fee_data,
            "user_approve": user_approve,
            "branch_name": branch_name
        }
        return payload

    def DPT_FBI(self, account_number, serial_no, branch_name=None, description=None, stock_type=None, currency_code=None, stock_prefix=None, user_approve=None, fee_data=None, account_number_for_fee=None, method=None):
        if not branch_name:
            branch_name=''
        if not description:
            description='11804: Fixed deposit book issue'
        if not stock_type:
            stock_type='F'
        if not currency_code:
            currency_code=''
        if not stock_prefix:
            stock_prefix=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        if not account_number_for_fee:
            account_number_for_fee=''
        if not method:
            method=''
        payload = {
            "branch_name": branch_name,
            "account_number": account_number,
            "serial_no": serial_no,
            "description": description,
            "stock_type": stock_type,
            "currency_code": currency_code,
            "stock_prefix": stock_prefix,
            "user_approve": user_approve,
            "fee_data": fee_data,
            "account_number_for_fee": account_number_for_fee,
            "method": method
        }
        return payload

    def DPT_DLS(self, account_number, another_deposit_account, sum_amount, balance_received, passbook_number=None, balance=None, interest_accrual=None, withholding_tax_accrual_actural=None, withholding_tax_accrual=None, interest_payable_receivable=None, interest_due=None, gross_interest_paid_out=None, interest_pre_calculate=None, withholding_tax_rate=None, withholding_tax_amount=None, penalty_fee=None, total_amount=None, depositor_name=None, depositor_id=None, depositor_address=None, home=None, office=None, description=None, currency_code=None, ifc_code=None, receive_currency=None, accrual_interest_amount=None, user_approve=None, branch_name=None):
        if not passbook_number:
            passbook_number=''
        if not balance:
            balance=0
        if not interest_accrual:
            interest_accrual=0
        if not withholding_tax_accrual_actural:
            withholding_tax_accrual_actural=0
        if not withholding_tax_accrual:
            withholding_tax_accrual=0
        if not interest_payable_receivable:
            interest_payable_receivable=0
        if not interest_due:
            interest_due=0
        if not gross_interest_paid_out:
            gross_interest_paid_out=0
        if not interest_pre_calculate:
            interest_pre_calculate=0
        if not withholding_tax_rate:
            withholding_tax_rate=0
        if not withholding_tax_amount:
            withholding_tax_amount=0
        if not penalty_fee:
            penalty_fee=0
        if not total_amount:
            total_amount=0
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
        if not description:
            description=''
        if not currency_code:
            currency_code=''
        if not ifc_code:
            ifc_code=0
        if not receive_currency:
            receive_currency=''
        if not accrual_interest_amount:
            accrual_interest_amount=0
        if not user_approve:
            user_approve=None
        if not branch_name:
            branch_name=''
        payload = {
            "account_number": account_number,
            "passbook_number": passbook_number,
            "balance": balance,
            "interest_accrual": interest_accrual,
            "withholding_tax_accrual_actural": withholding_tax_accrual_actural,
            "withholding_tax_accrual": withholding_tax_accrual,
            "interest_payable_receivable": interest_payable_receivable,
            "interest_due": interest_due,
            "gross_interest_paid_out": gross_interest_paid_out,
            "interest_pre_calculate": interest_pre_calculate,
            "withholding_tax_rate": withholding_tax_rate,
            "withholding_tax_amount": withholding_tax_amount,
            "penalty_fee": penalty_fee,
            "total_amount": total_amount,
            "another_deposit_account": another_deposit_account,
            "depositor_name": depositor_name,
            "depositor_id": depositor_id,
            "depositor_address": depositor_address,
            "depositor_description": {
                "home": home,
                "office": office
            },
            "description": description,
            "currency_code": currency_code,
            "ifc_code": ifc_code,
            "sum_amount": sum_amount,
            "receive_currency": receive_currency,
            "accrual_interest_amount": accrual_interest_amount,
            "balance_received": balance_received,
            "user_approve": user_approve,
            "branch_name": branch_name
        }
        return payload

    def DPT_ACT(self, debit_account_number, credit_account_number, debit_amount, credit_amount, base_amount, fee_amount, receive_amount, customer_type=None, account_name_debit=None, account_name_credit=None, custommer_code=None, phone_mobile=None, nationality=None, paper_type=None, debit_accounting_type=None, credit_accounting_type=None, debit_currency_code=None, debit_type=None, credit_currency_code=None, credit_type=None, debit_rate=None, cross_rate=None, original_cross_rate=None, reverse_rate=None, credit_rate=None, full_name=None, paper_number=None, address=None, description=None, user_approve=None, fee_data=None):
        if not customer_type:
            customer_type='C'
        if not account_name_debit:
            account_name_debit=''
        if not account_name_credit:
            account_name_credit=''
        if not custommer_code:
            custommer_code=''
        if not phone_mobile:
            phone_mobile=''
        if not nationality:
            nationality=''
        if not paper_type:
            paper_type='-'
        if not debit_accounting_type:
            debit_accounting_type='DPT'
        if not credit_accounting_type:
            credit_accounting_type='ACT'
        if not debit_currency_code:
            debit_currency_code=''
        if not debit_type:
            debit_type=0
        if not credit_currency_code:
            credit_currency_code=''
        if not credit_type:
            credit_type=0
        if not debit_rate:
            debit_rate=0
        if not cross_rate:
            cross_rate=0
        if not original_cross_rate:
            original_cross_rate=0
        if not reverse_rate:
            reverse_rate=0
        if not credit_rate:
            credit_rate=0
        if not full_name:
            full_name=''
        if not paper_number:
            paper_number=''
        if not address:
            address=''
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        payload = {
            "customer_type": customer_type,
            "account_name_debit": account_name_debit,
            "account_name_credit": account_name_credit,
            "custommer_code": custommer_code,
            "phone_mobile": phone_mobile,
            "nationality": nationality,
            "paper_type": paper_type,
            "debit_accounting_type": debit_accounting_type,
            "credit_accounting_type": credit_accounting_type,
            "debit_account_number": debit_account_number,
            "debit_currency_code": debit_currency_code,
            "debit_type": debit_type,
            "credit_currency_code": credit_currency_code,
            "credit_type": credit_type,
            "debit_rate": debit_rate,
            "cross_rate": cross_rate,
            "original_cross_rate": original_cross_rate,
            "reverse_rate": reverse_rate,
            "credit_rate": credit_rate,
            "debit_amount": debit_amount,
            "credit_amount": credit_amount,
            "base_amount": base_amount,
            "full_name": full_name,
            "paper_number": paper_number,
            "address": address,
            "description": description,
            "credit_account_number": credit_account_number,
            "user_approve": user_approve,
            "fee_amount": fee_amount,
            "receive_amount": receive_amount,
            "fee_data": fee_data
        }
        return payload

    def DPT_DPT(self, debit_account_number, credit_account_number, debit_amount, credit_amount, base_amount, fee_amount, receive_amount, customer_type=None, custommer_code=None, phone_mobile=None, nationality=None, paper_type=None, account_name_debit=None, account_name_credit=None, debit_accounting_type=None, credit_accounting_type=None, debit_currency_code=None, debit_type=None, credit_currency_code=None, credit_type=None, debit_rate=None, cross_rate=None, original_cross_rate=None, reverse_rate=None, credit_rate=None, full_name=None, paper_number=None, address=None, description=None, user_approve=None, fee_data=None):
        if not customer_type:
            customer_type='C'
        if not custommer_code:
            custommer_code=''
        if not phone_mobile:
            phone_mobile=''
        if not nationality:
            nationality=''
        if not paper_type:
            paper_type='-'
        if not account_name_debit:
            account_name_debit=''
        if not account_name_credit:
            account_name_credit=''
        if not debit_accounting_type:
            debit_accounting_type='DPT'
        if not credit_accounting_type:
            credit_accounting_type='DPT'
        if not debit_currency_code:
            debit_currency_code=''
        if not debit_type:
            debit_type=0
        if not credit_currency_code:
            credit_currency_code=''
        if not credit_type:
            credit_type=0
        if not debit_rate:
            debit_rate=0
        if not cross_rate:
            cross_rate=0
        if not original_cross_rate:
            original_cross_rate=0
        if not reverse_rate:
            reverse_rate=0
        if not credit_rate:
            credit_rate=0
        if not full_name:
            full_name=''
        if not paper_number:
            paper_number=''
        if not address:
            address=''
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        payload = {
            "customer_type": customer_type,
            "custommer_code": custommer_code,
            "phone_mobile": phone_mobile,
            "nationality": nationality,
            "paper_type": paper_type,
            "account_name_debit": account_name_debit,
            "account_name_credit": account_name_credit,
            "debit_accounting_type": debit_accounting_type,
            "credit_accounting_type": credit_accounting_type,
            "debit_account_number": debit_account_number,
            "debit_currency_code": debit_currency_code,
            "debit_type": debit_type,
            "credit_currency_code": credit_currency_code,
            "credit_type": credit_type,
            "debit_rate": debit_rate,
            "cross_rate": cross_rate,
            "original_cross_rate": original_cross_rate,
            "reverse_rate": reverse_rate,
            "credit_rate": credit_rate,
            "debit_amount": debit_amount,
            "credit_amount": credit_amount,
            "base_amount": base_amount,
            "full_name": full_name,
            "paper_number": paper_number,
            "address": address,
            "description": description,
            "credit_account_number": credit_account_number,
            "user_approve": user_approve,
            "fee_amount": fee_amount,
            "receive_amount": receive_amount,
            "fee_data": fee_data
        }
        return payload

    def ACT_DPT(self, debit_account_number, credit_account_number, debit_amount, credit_amount, base_amount, fee_amount, receive_amount, customer_type=None, account_name_debit=None, account_name_credit=None, custommer_code=None, phone_mobile=None, nationality=None, paper_type=None, debit_accounting_type=None, credit_accounting_type=None, debit_currency_code=None, debit_type=None, credit_currency_code=None, credit_type=None, debit_rate=None, cross_rate=None, original_cross_rate=None, reverse_rate=None, credit_rate=None, full_name=None, paper_number=None, address=None, description=None, user_approve=None, fee_data=None):
        if not customer_type:
            customer_type='C'
        if not account_name_debit:
            account_name_debit=''
        if not account_name_credit:
            account_name_credit=''
        if not custommer_code:
            custommer_code=''
        if not phone_mobile:
            phone_mobile=''
        if not nationality:
            nationality=''
        if not paper_type:
            paper_type='-'
        if not debit_accounting_type:
            debit_accounting_type='ACT'
        if not credit_accounting_type:
            credit_accounting_type='DPT'
        if not debit_currency_code:
            debit_currency_code=''
        if not debit_type:
            debit_type=0
        if not credit_currency_code:
            credit_currency_code=''
        if not credit_type:
            credit_type=0
        if not debit_rate:
            debit_rate=0
        if not cross_rate:
            cross_rate=0
        if not original_cross_rate:
            original_cross_rate=0
        if not reverse_rate:
            reverse_rate=0
        if not credit_rate:
            credit_rate=0
        if not full_name:
            full_name=''
        if not paper_number:
            paper_number=''
        if not address:
            address=''
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        payload = {
            "customer_type": customer_type,
            "account_name_debit": account_name_debit,
            "account_name_credit": account_name_credit,
            "custommer_code": custommer_code,
            "phone_mobile": phone_mobile,
            "nationality": nationality,
            "paper_type": paper_type,
            "debit_accounting_type": debit_accounting_type,
            "credit_accounting_type": credit_accounting_type,
            "debit_account_number": debit_account_number,
            "debit_currency_code": debit_currency_code,
            "debit_type": debit_type,
            "credit_currency_code": credit_currency_code,
            "credit_type": credit_type,
            "debit_rate": debit_rate,
            "cross_rate": cross_rate,
            "original_cross_rate": original_cross_rate,
            "reverse_rate": reverse_rate,
            "credit_rate": credit_rate,
            "debit_amount": debit_amount,
            "credit_amount": credit_amount,
            "base_amount": base_amount,
            "full_name": full_name,
            "paper_number": paper_number,
            "address": address,
            "description": description,
            "credit_account_number": credit_account_number,
            "user_approve": user_approve,
            "fee_amount": fee_amount,
            "receive_amount": receive_amount,
            "fee_data": fee_data
        }
        return payload

    def ACT_ACT(self, debit_account_number, credit_account_number, debit_amount, credit_amount, base_amount, fee_amount, receive_amount, customer_type=None, account_name_debit=None, account_name_credit=None, custommer_code=None, phone_mobile=None, nationality=None, paper_type=None, debit_accounting_type=None, credit_accounting_type=None, debit_currency_code=None, debit_type=None, credit_currency_code=None, credit_type=None, debit_rate=None, cross_rate=None, reverse_rate=None, original_cross_rate=None, credit_rate=None, full_name=None, paper_number=None, address=None, description=None, user_approve=None, fee_data=None):
        if not customer_type:
            customer_type='C'
        if not account_name_debit:
            account_name_debit=''
        if not account_name_credit:
            account_name_credit=''
        if not custommer_code:
            custommer_code=''
        if not phone_mobile:
            phone_mobile=''
        if not nationality:
            nationality=''
        if not paper_type:
            paper_type='-'
        if not debit_accounting_type:
            debit_accounting_type='ACT'
        if not credit_accounting_type:
            credit_accounting_type='ACT'
        if not debit_currency_code:
            debit_currency_code=''
        if not debit_type:
            debit_type=0
        if not credit_currency_code:
            credit_currency_code=''
        if not credit_type:
            credit_type=0
        if not debit_rate:
            debit_rate=0
        if not cross_rate:
            cross_rate=0
        if not reverse_rate:
            reverse_rate=0
        if not original_cross_rate:
            original_cross_rate=0
        if not credit_rate:
            credit_rate=0
        if not full_name:
            full_name=''
        if not paper_number:
            paper_number=''
        if not address:
            address=''
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        payload = {
            "customer_type": customer_type,
            "account_name_debit": account_name_debit,
            "account_name_credit": account_name_credit,
            "custommer_code": custommer_code,
            "phone_mobile": phone_mobile,
            "nationality": nationality,
            "paper_type": paper_type,
            "debit_accounting_type": debit_accounting_type,
            "credit_accounting_type": credit_accounting_type,
            "debit_account_number": debit_account_number,
            "credit_account_number": credit_account_number,
            "debit_currency_code": debit_currency_code,
            "debit_type": debit_type,
            "credit_currency_code": credit_currency_code,
            "credit_type": credit_type,
            "debit_rate": debit_rate,
            "cross_rate": cross_rate,
            "reverse_rate": reverse_rate,
            "original_cross_rate": original_cross_rate,
            "credit_rate": credit_rate,
            "debit_amount": debit_amount,
            "credit_amount": credit_amount,
            "base_amount": base_amount,
            "full_name": full_name,
            "paper_number": paper_number,
            "address": address,
            "description": description,
            "user_approve": user_approve,
            "fee_amount": fee_amount,
            "receive_amount": receive_amount,
            "fee_data": fee_data
        }
        return payload

    def ACT_CSH(self, debit_account_number, debit_amount, credit_amount, base_amount, fee_amount, receive_amount, customer_type=None, account_name_debit=None, account_name_credit=None, custommer_code=None, phone_mobile=None, nationality=None, paper_type=None, debit_accounting_type=None, credit_accounting_type=None, debit_currency_code=None, debit_type=None, credit_currency_code=None, credit_type=None, debit_rate=None, cross_rate=None, reverse_rate=None, original_cross_rate=None, credit_rate=None, full_name=None, paper_number=None, address=None, description=None, user_approve=None, fee_data=None):
        if not customer_type:
            customer_type='C'
        if not account_name_debit:
            account_name_debit=''
        if not account_name_credit:
            account_name_credit=''
        if not custommer_code:
            custommer_code=''
        if not phone_mobile:
            phone_mobile=''
        if not nationality:
            nationality=''
        if not paper_type:
            paper_type='-'
        if not debit_accounting_type:
            debit_accounting_type='ACT'
        if not credit_accounting_type:
            credit_accounting_type='CSH'
        if not debit_currency_code:
            debit_currency_code=''
        if not debit_type:
            debit_type=0
        if not credit_currency_code:
            credit_currency_code=''
        if not credit_type:
            credit_type=0
        if not debit_rate:
            debit_rate=0
        if not cross_rate:
            cross_rate=0
        if not reverse_rate:
            reverse_rate=0
        if not original_cross_rate:
            original_cross_rate=0
        if not credit_rate:
            credit_rate=0
        if not full_name:
            full_name=''
        if not paper_number:
            paper_number=''
        if not address:
            address=''
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        payload = {
            "customer_type": customer_type,
            "account_name_debit": account_name_debit,
            "account_name_credit": account_name_credit,
            "custommer_code": custommer_code,
            "phone_mobile": phone_mobile,
            "nationality": nationality,
            "paper_type": paper_type,
            "debit_accounting_type": debit_accounting_type,
            "credit_accounting_type": credit_accounting_type,
            "debit_account_number": debit_account_number,
            "debit_currency_code": debit_currency_code,
            "debit_type": debit_type,
            "credit_currency_code": credit_currency_code,
            "credit_type": credit_type,
            "debit_rate": debit_rate,
            "cross_rate": cross_rate,
            "reverse_rate": reverse_rate,
            "original_cross_rate": original_cross_rate,
            "credit_rate": credit_rate,
            "debit_amount": debit_amount,
            "credit_amount": credit_amount,
            "base_amount": base_amount,
            "full_name": full_name,
            "paper_number": paper_number,
            "address": address,
            "description": description,
            "user_approve": user_approve,
            "fee_amount": fee_amount,
            "receive_amount": receive_amount,
            "fee_data": fee_data
        }
        return payload

    def CSH_ACT(self, credit_account_number, debit_amount, credit_amount, base_amount, fee_amount, receive_amount, customer_type=None, account_name_debit=None, account_name_credit=None, custommer_code=None, phone_mobile=None, nationality=None, paper_type=None, debit_type_of_cash=None, debit_accounting_type=None, credit_accounting_type=None, debit_currency_code=None, debit_type=None, credit_currency_code=None, credit_type=None, debit_rate=None, cross_rate=None, original_cross_rate=None, reverse_rate=None, credit_rate=None, full_name=None, paper_number=None, address=None, description=None, user_approve=None, fee_data=None):
        if not customer_type:
            customer_type='C'
        if not account_name_debit:
            account_name_debit=''
        if not account_name_credit:
            account_name_credit=''
        if not custommer_code:
            custommer_code=''
        if not phone_mobile:
            phone_mobile=''
        if not nationality:
            nationality=''
        if not paper_type:
            paper_type='-'
        if not debit_type_of_cash:
            debit_type_of_cash='B'
        if not debit_accounting_type:
            debit_accounting_type='CSH'
        if not credit_accounting_type:
            credit_accounting_type='ACT'
        if not debit_currency_code:
            debit_currency_code=''
        if not debit_type:
            debit_type=0
        if not credit_currency_code:
            credit_currency_code=''
        if not credit_type:
            credit_type=0
        if not debit_rate:
            debit_rate=0
        if not cross_rate:
            cross_rate=0
        if not original_cross_rate:
            original_cross_rate=0
        if not reverse_rate:
            reverse_rate=0
        if not credit_rate:
            credit_rate=0
        if not full_name:
            full_name=''
        if not paper_number:
            paper_number=''
        if not address:
            address=''
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not fee_data:
            fee_data=[]
        payload = {
            "customer_type": customer_type,
            "account_name_debit": account_name_debit,
            "account_name_credit": account_name_credit,
            "custommer_code": custommer_code,
            "phone_mobile": phone_mobile,
            "nationality": nationality,
            "paper_type": paper_type,
            "debit_type_of_cash": debit_type_of_cash,
            "debit_accounting_type": debit_accounting_type,
            "credit_accounting_type": credit_accounting_type,
            "credit_account_number": credit_account_number,
            "debit_currency_code": debit_currency_code,
            "debit_type": debit_type,
            "credit_currency_code": credit_currency_code,
            "credit_type": credit_type,
            "debit_rate": debit_rate,
            "cross_rate": cross_rate,
            "original_cross_rate": original_cross_rate,
            "reverse_rate": reverse_rate,
            "credit_rate": credit_rate,
            "debit_amount": debit_amount,
            "credit_amount": credit_amount,
            "base_amount": base_amount,
            "full_name": full_name,
            "paper_number": paper_number,
            "address": address,
            "description": description,
            "user_approve": user_approve,
            "fee_amount": fee_amount,
            "receive_amount": receive_amount,
            "fee_data": fee_data
        }
        return payload

    def DPT_HIS(self, account_number, from_date=None, to_date=None, description=None, user_approve=None, branch_name=None):
        if not from_date:
            from_date=''
        if not to_date:
            to_date=''
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not branch_name:
            branch_name=''
        payload = {
            "account_number": account_number,
            "from_date": from_date,
            "to_date": to_date,
            "description": description,
            "user_approve": user_approve,
            "branch_name": branch_name
        }
        return payload

    def ACT_MAN(self, posting_data=None, description=None, reference_document_no=None, value_date=None, customer_id=None, customer_account_id=None, user_defined4=None, user_defined5=None, user_approve=None, amount=None, total_amount=None):
        if not posting_data:
            posting_data=[]
        if not description:
            description=''
        if not reference_document_no:
            reference_document_no=''
        if not value_date:
            value_date=''
        if not customer_id:
            customer_id=''
        if not customer_account_id:
            customer_account_id=''
        if not user_defined4:
            user_defined4=''
        if not user_defined5:
            user_defined5=''
        if not user_approve:
            user_approve=None
        if not amount:
            amount=1
        if not total_amount:
            total_amount=0
        payload = {
            "posting_data": posting_data,
            "description": description,
            "reference_document_no": reference_document_no,
            "value_date": value_date,
            "customer_id": customer_id,
            "customer_account_id": customer_account_id,
            "user_defined4": user_defined4,
            "user_defined5": user_defined5,
            "user_approve": user_approve,
            "amount": amount,
            "total_amount": total_amount
        }
        return payload

    def CSH_MOV(self, from_teller_code, to_teller_code, amount, currency, user_approve, to_teller_name=None, description=None):
        if not to_teller_name:
            to_teller_name=''
        if not description:
            description=''
        payload = {
            "from_teller_code": from_teller_code,
            "to_teller_code": to_teller_code,
            "to_teller_name": to_teller_name,
            "amount": amount,
            "currency": currency,
            "description": description,
            "user_approve": user_approve
        }
        return payload

    def CSH_DNM(self, description=None, user_approve=None, remaining_cash_balance=None, closing_cash_balance=None, denom_cash_balance=None, last_total_amount=None, currency_code=None, total_amount=None, cash_denom_list=None):
        if not description:
            description=''
        if not user_approve:
            user_approve=None
        if not remaining_cash_balance:
            remaining_cash_balance=0
        if not closing_cash_balance:
            closing_cash_balance=0
        if not denom_cash_balance:
            denom_cash_balance=0
        if not last_total_amount:
            last_total_amount=0
        if not currency_code:
            currency_code=''
        if not total_amount:
            total_amount=0
        if not cash_denom_list:
            cash_denom_list=[]
        payload = {
            "description": description,
            "user_approve": user_approve,
            "remaining_cash_balance": remaining_cash_balance,
            "closing_cash_balance": closing_cash_balance,
            "denom_cash_balance": denom_cash_balance,
            "last_total_amount": last_total_amount,
            "currency_code": currency_code,
            "total_amount": total_amount,
            "cash_denom_list": cash_denom_list
        }
        return payload

    def CTM_APR(self, customer_code, customer_name=None, description=None, customer_status=None, user_approve=None, customer_type=None, created_by=None):
        if not customer_name:
            customer_name=''
        if not description:
            description=''
        if not customer_status:
            customer_status=''
        if not user_approve:
            user_approve=None
        if not customer_type:
            customer_type='C'
        if not created_by:
            created_by=''
        payload = {
            "customer_code": customer_code,
            "customer_name": customer_name,
            "description": description,
            "customer_status": customer_status,
            "user_approve": user_approve,
            "customer_type": customer_type,
            "created_by": created_by
        }
        return payload

    def CTM_CAS(self, customer_code, current_status=None, new_status=None, description=None, limit_amount=None, limit_currency=None, user_approve=None):
        if not current_status:
            current_status=''
        if not new_status:
            new_status=''
        if not description:
            description=''
        if not limit_amount:
            limit_amount=1
        if not limit_currency:
            limit_currency='MMK'
        if not user_approve:
            user_approve=None
        payload = {
            "customer_code": customer_code,
            "current_status": current_status,
            "new_status": new_status,
            "description": description,
            "limit_amount": limit_amount,
            "limit_currency": limit_currency,
            "user_approve": user_approve
        }
        return payload

    def CRD_EXT(self, credit_account, new_expire_date, credit_limit=None, oustanding_balance=None, old_expire_date=None, creditor_name=None, creditor_code=None, creditor_address=None, description=None, home=None, office=None, user_approve=None):
        if not credit_limit:
            credit_limit=0
        if not oustanding_balance:
            oustanding_balance=0
        if not old_expire_date:
            old_expire_date=''
        if not creditor_name:
            creditor_name=''
        if not creditor_code:
            creditor_code=''
        if not creditor_address:
            creditor_address=''
        if not description:
            description=''
        if not home:
            home=''
        if not office:
            office=''
        if not user_approve:
            user_approve=None
        payload = {
            "credit_account": credit_account,
            "credit_limit": credit_limit,
            "oustanding_balance": oustanding_balance,
            "old_expire_date": old_expire_date,
            "new_expire_date": new_expire_date,
            "creditor_name": creditor_name,
            "creditor_code": creditor_code,
            "creditor_address": creditor_address,
            "description": description,
            "creditor_description": {
                "home": home,
                "office": office
            },
            "user_approve": user_approve
        }
        return payload

# CAC FO CHUA CHUYEN STORED PROCEDURE, KHOI TAO DE TAO DU LIEU TEST
    def DPT_CAS(self, account_number, amount=None, current_status=None, new_status=None, description=None, user_approve=None, branch_name=None):
        if not amount:
            amount=1
        if not current_status:
            current_status='Normal'
        if not new_status:
            new_status='D'
        if not description:
            description='11841: Change account status'
        if not user_approve:
            user_approve=None
        if not branch_name:
            branch_name=''
        payload = {
            "amount": amount,
            "account_number": account_number,
            "current_status": current_status,
            "new_status": new_status,
            "description": description,
            "user_approve": user_approve,
            "branch_name": branch_name
        }
        return payload

    def DPT_OPAL(self, master_account_number, linkage_account_number, branch_code, master_account_name=None, master_module_code=None, linkage_account_name=None, linkage_module_code=None, linkage_description=None, linkage_type=None, linkage_class=None, linkage_module_name=None, fee_data=None, account_for_fee=None, fee_collection_method=None, amount_for_fee_calculation=None, currency=None, description=None, amount=None):
        if not master_account_number:
            master_account_number=''
        if not master_account_name:
            master_account_name=''
        if not master_module_code:
            master_module_code='DPT'
        if not linkage_account_number:
            linkage_account_number=''
        if not linkage_account_name:
            linkage_account_name=''
        if not linkage_module_code:
            linkage_module_code='DPT'
        if not linkage_description:
            linkage_description=None
        if not linkage_type:
            linkage_type='D'
        if not linkage_class:
            linkage_class='F'
        if not linkage_module_name:
            linkage_module_name='DEPOSIT'
        if not fee_data:
            fee_data=[]
        if not account_for_fee:
            account_for_fee=''
        if not fee_collection_method:
            fee_collection_method='CSH'
        if not branch_code:
            branch_code=''
        if not amount_for_fee_calculation:
            amount_for_fee_calculation=0
        if not currency:
            currency='MMK'
        if not description:
            description='DPT-Account Linkage-Add'
        if not amount:
            amount=1
        payload = {
            "master_account_number": master_account_number,
            "master_account_name": master_account_name,
            "master_module_code": master_module_code,
            "list_account_linkage": [
                {
                    "linkage_account_number": linkage_account_number,
                    "linkage_account_name": linkage_account_name,
                    "linkage_module_code": linkage_module_code,
                    "linkage_description": linkage_description,
                    "linkage_type": linkage_type,
                    "linkage_class": linkage_class,
                    "linkage_module_name": linkage_module_name
                }
            ],
            "fee_data": fee_data,
            "account_for_fee": account_for_fee,
            "fee_collection_method": fee_collection_method,
            "branch_code": branch_code,
            "amount_for_fee_calculation": amount_for_fee_calculation,
            "currency": currency,
            "description": description,
            "amount": amount
        }
        return payload

    def DPT_CLS(self, account_number, passbook_number=None, branch_name=None, balance=None, interest_accrual=None, withholding_tax_accrual=None, withholding_tax_accrual_actural=None, interest_payable_receivable=None, interest_due=None, gross_paid_interest_amount=None, withholding_tax_rate=None, withholding_tax_amount=None, penalty_fee=None, fee_amount=None, ifc_code=None, depositor_name=None, depositor_id=None, depositor_address=None, home=None, office=None, description=None, currency_code=None, sum_amount=None, interest_pre_calculate=None, balance_received=None, accrual_interest_amount_decimal_adjust=None, fee_data=None, user_approve=None):
        if not account_number:
            account_number=None
        if not passbook_number:
            passbook_number=''
        if not branch_name:
            branch_name=''
        if not balance:
            balance=0
        if not interest_accrual:
            interest_accrual=0
        if not withholding_tax_accrual:
            withholding_tax_accrual=0
        if not withholding_tax_accrual_actural:
            withholding_tax_accrual_actural=0
        if not interest_payable_receivable:
            interest_payable_receivable=0
        if not interest_due:
            interest_due=0
        if not gross_paid_interest_amount:
            gross_paid_interest_amount=0
        if not withholding_tax_rate:
            withholding_tax_rate=0
        if not withholding_tax_amount:
            withholding_tax_amount=0
        if not penalty_fee:
            penalty_fee=0
        if not fee_amount:
            fee_amount=0
        if not ifc_code:
            ifc_code=0
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
        if not description:
            description='1193: Close deposit account'
        if not currency_code:
            currency_code='MMK'
        if not sum_amount:
            sum_amount=0
        if not interest_pre_calculate:
            interest_pre_calculate=0
        if not balance_received:
            balance_received=0
        if not accrual_interest_amount_decimal_adjust:
            accrual_interest_amount_decimal_adjust=0
        if not fee_data:
            fee_data=[]
        if not user_approve:
            user_approve=None
        payload = {
            "account_number": account_number,
            "passbook_number": passbook_number,
            "branch_name": branch_name,
            "balance": balance,
            "interest_accrual": interest_accrual,
            "withholding_tax_accrual": withholding_tax_accrual,
            "withholding_tax_accrual_actural": withholding_tax_accrual_actural,
            "interest_payable_receivable": interest_payable_receivable,
            "interest_due": interest_due,
            "gross_paid_interest_amount": gross_paid_interest_amount,
            "withholding_tax_rate": withholding_tax_rate,
            "withholding_tax_amount": withholding_tax_amount,
            "penalty_fee": penalty_fee,
            "fee_amount": fee_amount,
            "ifc_code": ifc_code,
            "depositor_name": depositor_name,
            "depositor_id": depositor_id,
            "depositor_address": depositor_address,
            "depositor_description": {
                "home": home,
                "office": office
            },
            "description": description,
            "currency_code": currency_code,
            "sum_amount": sum_amount,
            "interest_pre_calculate": interest_pre_calculate,
            "balance_received": balance_received,
            "accrual_interest_amount_decimal_adjust": accrual_interest_amount_decimal_adjust,
            "fee_data": fee_data,
            "user_approve": user_approve
        }
        return payload

    def DPT_BLK(self, account_number=None, branch_name=None, depositor_name=None, depositor_id=None, depositor_address=None, home=None, office=None, depositor_balance=None, depositor_currency=None, description=None, block_reason=None, value_date=None, user_approve=None, amount=None):
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
            description='11840: Block account'
        if not block_reason:
            block_reason='R1'
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

    def DPT_SRG(self, from_serial, to_serial, module=None, stock_type=None, stock_prefix=None, no_of_leaves=None, no_of_books=None, description=None, amount=None):
        if not module:
            module='DPT'
        if not stock_type:
            stock_type='C'
        if not stock_prefix:
            stock_prefix=''
        if not no_of_leaves:
            no_of_leaves=1
        if not no_of_books:
            no_of_books=1
        if not description:
            description='11830: Stock registration'
        if not amount:
            amount=1
        payload = {
            "module": module,
            "stock_type": stock_type,
            "from_serial": from_serial,
            "to_serial": to_serial,
            "stock_prefix": stock_prefix,
            "no_of_leaves": no_of_leaves,
            "no_of_books": no_of_books,
            "description": description,
            "amount": amount
        }
        return payload

    def DPT_SAT(self, from_serial, to_serial, assigned_staff_code, stock_type=None, stock_prefix=None, description=None, user_approve=None):
        if not stock_type:
            stock_type='C'
        if not stock_prefix:
            stock_prefix=''
        if not description:
            description='11832: Stock assign to Staff'
        if not user_approve:
            user_approve=None
        payload = {
            "stock_type": stock_type,
            "from_serial": from_serial,
            "to_serial": to_serial,
            "assigned_staff_code": assigned_staff_code,
            "stock_prefix": stock_prefix,
            "description": description,
            "user_approve": user_approve
        }
        return payload

    def DPT_CCR(self, from_serial, to_serial, stock_type=None, stock_prefix=None, description=None, user_approve=None, amount=None):
        if not stock_type:
            stock_type='C'
        if not stock_prefix:
            stock_prefix=''
        if not description:
            description='11834: Stock confirm received'
        if not user_approve:
            user_approve=None
        if not amount:
            amount=1
        payload = {
            "stock_type": stock_type,
            "from_serial": from_serial,
            "to_serial": to_serial,
            "stock_prefix": stock_prefix,
            "description": description,
            "user_approve": user_approve,
            "amount": amount
        }
        return payload

    def DPT_CIS(self, account_number, from_serial, to_serial, stock_number=None, stock_type=None, number_of_leaves=None, total_fee_for_cash=None, total_vat_for_cash=None, fee_amount=None, fee_vat=None, stock_prefix=None, currency_code=None, description=None, fee_data=None, user_approve=None, branch_name=None, account_for_fee=None, fee_collected_method=None):
        if not stock_number:
            stock_number=''
        if not stock_type:
            stock_type='C'
        if not number_of_leaves:
            number_of_leaves=1
        if not total_fee_for_cash:
            total_fee_for_cash=0
        if not total_vat_for_cash:
            total_vat_for_cash=0
        if not fee_amount:
            fee_amount=0
        if not fee_vat:
            fee_vat=0
        if not stock_prefix:
            stock_prefix=''
        if not currency_code:
            currency_code='MMK'
        if not description:
            description='11834: Stock confirm received'
        if not fee_data:
            fee_data=[]
        if not user_approve:
            user_approve=None
        if not branch_name:
            branch_name=''
        if not account_for_fee:
            account_for_fee=''
        if not fee_collected_method:
            fee_collected_method='CSH'
        payload = {
            "account_number": account_number,
            "stock_number": stock_number,
            "stock_type": stock_type,
            "from_serial": from_serial,
            "to_serial": to_serial,
            "number_of_leaves": number_of_leaves,
            "total_fee_for_cash": total_fee_for_cash,
            "total_vat_for_cash": total_vat_for_cash,
            "fee_amount": fee_amount,
            "fee_vat": fee_vat,
            "stock_prefix": stock_prefix,
            "currency_code": currency_code,
            "description": description,
            "fee_data": fee_data,
            "user_approve": user_approve,
            "branch_name": branch_name,
            "account_for_fee": account_for_fee,
            "fee_collected_method": fee_collected_method
        }
        return payload

    def DPT_CTS(self, account_number, from_serial, to_serial, branch_name=None, stock_type=None, cn_status=None, fee_amount=None, stock_prefix=None, currency_code=None, description=None, fee_data=None, user_approve=None, amount=None):
        if not branch_name:
            branch_name=''
        if not stock_type:
            stock_type='C'
        if not cn_status:
            cn_status=''
        if not fee_amount:
            fee_amount=0
        if not stock_prefix:
            stock_prefix=''
        if not currency_code:
            currency_code=''
        if not description:
            description='11837: Change status of stock'
        if not fee_data:
            fee_data=[]
        if not user_approve:
            user_approve=None
        if not amount:
            amount=1
        payload = {
            "account_number": account_number,
            "branch_name": branch_name,
            "stock_type": stock_type,
            "from_serial": from_serial,
            "to_serial": to_serial,
            "cn_status": cn_status,
            "fee_amount": fee_amount,
            "stock_prefix": stock_prefix,
            "currency_code": currency_code,
            "description": description,
            "fee_data": fee_data,
            "user_approve": user_approve,
            "amount": amount
        }
        return payload

    def DPT_ADSEARCH_STOCKINVENTORY(self, stock_no=None, stock_prefix=None, from_serial_from=None, from_serial_to=None, to_serial_from=None, to_serial_to=None, book_status=None, confirm_status=None, branch_name=None, user_name=None, stock_leaves_status=None, stock_type=None, amount=None, stock_balance=None, currency=None, ref_account_no=None, user_approved=None, assigned_teller_code=None, page_index=None, page_size=None):
        if not stock_no:
            stock_no=''
        if not stock_prefix:
            stock_prefix=''
        if not from_serial_from:
            from_serial_from=''
        if not from_serial_to:
            from_serial_to=''
        if not to_serial_from:
            to_serial_from=''
        if not to_serial_to:
            to_serial_to=''
        if not book_status:
            book_status=''
        if not confirm_status:
            confirm_status=''
        if not branch_name:
            branch_name=''
        if not user_name:
            user_name=''
        if not stock_leaves_status:
            stock_leaves_status=''
        if not stock_type:
            stock_type=''
        if not amount:
            amount=None
        if not stock_balance:
            stock_balance=None
        if not currency:
            currency=''
        if not ref_account_no:
            ref_account_no=''
        if not user_approved:
            user_approved=''
        if not assigned_teller_code:
            assigned_teller_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=5
        payload = {
            "stock_no": stock_no,
            "stock_prefix": stock_prefix,
            "from_serial_from": from_serial_from,
            "from_serial_to": from_serial_to,
            "to_serial_from": to_serial_from,
            "to_serial_to": to_serial_to,
            "book_status": book_status,
            "confirm_status": confirm_status,
            "branch_name": branch_name,
            "user_name": user_name,
            "stock_leaves_status": stock_leaves_status,
            "stock_type": stock_type,
            "amount": amount,
            "stock_balance": stock_balance,
            "currency": currency,
            "ref_account_no": ref_account_no,
            "user_approved": user_approved,
            "assigned_teller_code": assigned_teller_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

# ====================================== Workflow id BO ======================================
    def SQL_INSERT_CTM(self, currency_code_foreign_exchange_rate=None, currency_code_monetary_market=None, customer_credit_line2=None, customer_credit_line3=None, hocifcd=None, customer_private=None, title=None, title_of_organization=None, suffix=None, firstname=None, lastname=None, midname=None, fullname=None, firstname_local=None, lastname_local=None, midname_local=None, shortname=None, gender=None, date_of_birth=None, place_of_birth=None, nation=None, country=None, paper_type=None, paper_number=None, issue_date_of_paper=None, issue_place_of_paper=None, expire_date_of_paper=None, paper_type_sub=None, paper_number_sub=None, issue_date_of_sub_paper=None, issue_place_of_sub_paper=None, customer_group_type=None, customer_sub_group_type=None, categories=None, sector=None, subsector=None, resident=None, bank_identification=None, legal_local_address_line1=None, legal_local_address_line2=None, legal_local_address_line3=None, legal_local_address_line4=None, legal_local_address_line5=None, contact_local_address_line1=None, contact_local_address_line2=None, contact_local_address_line3=None, contact_local_address_line4=None, contact_local_address_line5=None, introducer_1_name=None, introducer_1_account_no=None, introducer_2_name=None, introducer_2_account_no=None, phone_home=None, phone_mobile=None, email=None, education=None, marital_status=None, profession=None, business_type=None, financial=None, isic_code=None, managing_branch_code=None, customer_status=None, classify=None, polists=None, repolists=None, country_of_income=None, fatca_status=None, government_id=None, international_id=None, oversea_juristic_id=None, gfmis_code=None, branch_code=None, group_code=None, customer_credit_line=None, currency_code=None, customer_type=None, primary_cif=None, mdm_amount_status=None, mdm_request_status=None, mdm_list_sub_type_code=None, mdm_list_sub_type_desc=None, mdm_matching_by=None, mdm_final_kyc_status=None, mdm_kyc_comment_code=None, mdm_kyc_comment_desc=None, kyc_level=None, kyc_update_date=None, relation_customer_code1=None, relation_customer_code2=None, relation_customer_code3=None, relation_customer_code4=None, relation_customer_code5=None, customer_size=None, staff_code=None, customer_sub_type=None, father_name=None, is_restricted=None, extension_fields_reason_for_other_economic_sector=None, extension_fields_reason_for_other_business_type=None, extension_fields_referral_field=None, extension_fields_reason_for_other_sub_economic_sector=None, extension_fields_reason_for_other_occupation=None, extension_fields_reason_for_other_paper_type=None, extension_fields_income=None, extension_fields_introducer=None, extension_fields_position=None, extension_fields_remark_field_to_add=None, extension_fields_employer_name=None, extension_fields_fdi_info=None, extension_fields_tin_number=None):
        if not currency_code_foreign_exchange_rate:
            currency_code_foreign_exchange_rate='MMK'
        if not currency_code_monetary_market:
            currency_code_monetary_market='MMK'
        if not customer_credit_line2:
            customer_credit_line2=0
        if not customer_credit_line3:
            customer_credit_line3=0
        if not hocifcd:
            hocifcd=''
        if not customer_private:
            customer_private=''
        if not title:
            title=''
        if not title_of_organization:
            title_of_organization=None
        if not suffix:
            suffix=None
        if not firstname:
            firstname=''
        if not lastname:
            lastname=''
        if not midname:
            midname=''
        if not fullname:
            fullname=''
        if not firstname_local:
            firstname_local=''
        if not lastname_local:
            lastname_local=''
        if not midname_local:
            midname_local=''
        if not shortname:
            shortname=''
        if not gender:
            gender=''
        if not date_of_birth:
            date_of_birth=''
        if not place_of_birth:
            place_of_birth=None
        if not nation:
            nation='MM'
        if not country:
            country=None
        if not paper_type:
            paper_type=''
        if not paper_number:
            paper_number=''
        if not issue_date_of_paper:
            issue_date_of_paper=None
        if not issue_place_of_paper:
            issue_place_of_paper=''
        if not expire_date_of_paper:
            expire_date_of_paper=None
        if not paper_type_sub:
            paper_type_sub='N'
        if not paper_number_sub:
            paper_number_sub=''
        if not issue_date_of_sub_paper:
            issue_date_of_sub_paper=None
        if not issue_place_of_sub_paper:
            issue_place_of_sub_paper=''
        if not customer_group_type:
            customer_group_type=None
        if not customer_sub_group_type:
            customer_sub_group_type=None
        if not categories:
            categories=''
        if not sector:
            sector=None
        if not subsector:
            subsector=None
        if not resident:
            resident='R'
        if not bank_identification:
            bank_identification='-'
        if not legal_local_address_line1:
            legal_local_address_line1=''
        if not legal_local_address_line2:
            legal_local_address_line2=''
        if not legal_local_address_line3:
            legal_local_address_line3=''
        if not legal_local_address_line4:
            legal_local_address_line4=''
        if not legal_local_address_line5:
            legal_local_address_line5=''
        if not contact_local_address_line1:
            contact_local_address_line1=''
        if not contact_local_address_line2:
            contact_local_address_line2=''
        if not contact_local_address_line3:
            contact_local_address_line3=''
        if not contact_local_address_line4:
            contact_local_address_line4=''
        if not contact_local_address_line5:
            contact_local_address_line5=''
        if not introducer_1_name:
            introducer_1_name=''
        if not introducer_1_account_no:
            introducer_1_account_no=''
        if not introducer_2_name:
            introducer_2_name=''
        if not introducer_2_account_no:
            introducer_2_account_no=''
        if not phone_home:
            phone_home=''
        if not phone_mobile:
            phone_mobile=''
        if not email:
            email=''
        if not education:
            education='-'
        if not marital_status:
            marital_status='-'
        if not profession:
            profession=''
        if not business_type:
            business_type=''
        if not financial:
            financial=None
        if not isic_code:
            isic_code=None
        if not managing_branch_code:
            managing_branch_code=''
        if not customer_status:
            customer_status='P'
        if not classify:
            classify='N'
        if not polists:
            polists=''
        if not repolists:
            repolists=''
        if not country_of_income:
            country_of_income='MM'
        if not fatca_status:
            fatca_status='-'
        if not government_id:
            government_id=None
        if not international_id:
            international_id=None
        if not oversea_juristic_id:
            oversea_juristic_id=None
        if not gfmis_code:
            gfmis_code=None
        if not branch_code:
            branch_code=''
        if not group_code:
            group_code=''
        if not customer_credit_line:
            customer_credit_line=0
        if not currency_code:
            currency_code='MMK'
        if not customer_type:
            customer_type=''
        if not primary_cif:
            primary_cif='-'
        if not mdm_amount_status:
            mdm_amount_status='1'
        if not mdm_request_status:
            mdm_request_status='SUCCESS'
        if not mdm_list_sub_type_code:
            mdm_list_sub_type_code='PEPFR'
        if not mdm_list_sub_type_desc:
            mdm_list_sub_type_desc=''
        if not mdm_matching_by:
            mdm_matching_by='IWLLA'
        if not mdm_final_kyc_status:
            mdm_final_kyc_status=''
        if not mdm_kyc_comment_code:
            mdm_kyc_comment_code=''
        if not mdm_kyc_comment_desc:
            mdm_kyc_comment_desc=''
        if not kyc_level:
            kyc_level='3'
        if not kyc_update_date:
            kyc_update_date='2022-03-21T03:03:42.518Z'
        if not relation_customer_code1:
            relation_customer_code1=''
        if not relation_customer_code2:
            relation_customer_code2=''
        if not relation_customer_code3:
            relation_customer_code3=''
        if not relation_customer_code4:
            relation_customer_code4=''
        if not relation_customer_code5:
            relation_customer_code5=''
        if not customer_size:
            customer_size='S'
        if not staff_code:
            staff_code=''
        if not customer_sub_type:
            customer_sub_type=''
        if not father_name:
            father_name=''
        if not is_restricted:
            is_restricted='N'
        if not extension_fields_reason_for_other_economic_sector:
            extension_fields_reason_for_other_economic_sector=None
        if not extension_fields_reason_for_other_business_type:
            extension_fields_reason_for_other_business_type=None
        if not extension_fields_referral_field:
            extension_fields_referral_field=None
        if not extension_fields_reason_for_other_sub_economic_sector:
            extension_fields_reason_for_other_sub_economic_sector=None
        if not extension_fields_reason_for_other_occupation:
            extension_fields_reason_for_other_occupation=None
        if not extension_fields_reason_for_other_paper_type:
            extension_fields_reason_for_other_paper_type=None
        if not extension_fields_income:
            extension_fields_income=None
        if not extension_fields_introducer:
            extension_fields_introducer=None
        if not extension_fields_position:
            extension_fields_position=None
        if not extension_fields_remark_field_to_add:
            extension_fields_remark_field_to_add=None
        if not extension_fields_employer_name:
            extension_fields_employer_name=None
        if not extension_fields_fdi_info:
            extension_fields_fdi_info=None
        if not extension_fields_tin_number:
            extension_fields_tin_number=None
        payload = {
            "currency_code_foreign_exchange_rate": currency_code_foreign_exchange_rate,
            "currency_code_monetary_market": currency_code_monetary_market,
            "customer_credit_line2": customer_credit_line2,
            "customer_credit_line3": customer_credit_line3,
            "hocifcd": hocifcd,
            "customer_private": customer_private,
            "title": title,
            "title_of_organization": title_of_organization,
            "suffix": suffix,
            "firstname": firstname,
            "lastname": lastname,
            "midname": midname,
            "fullname": fullname,
            "firstname_local": firstname_local,
            "lastname_local": lastname_local,
            "midname_local": midname_local,
            "shortname": shortname,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "place_of_birth": place_of_birth,
            "nation": nation,
            "country": country,
            "paper_type": paper_type,
            "paper_number": paper_number,
            "issue_date_of_paper": issue_date_of_paper,
            "issue_place_of_paper": issue_place_of_paper,
            "expire_date_of_paper": expire_date_of_paper,
            "paper_type_sub": paper_type_sub,
            "paper_number_sub": paper_number_sub,
            "issue_date_of_sub_paper": issue_date_of_sub_paper,
            "issue_place_of_sub_paper": issue_place_of_sub_paper,
            "customer_group_type": customer_group_type,
            "customer_sub_group_type": customer_sub_group_type,
            "categories": categories,
            "sector": sector,
            "subsector": subsector,
            "resident": resident,
            "bank_identification": bank_identification,
                "legal_local_address": {
                "legal_local_address_line1": legal_local_address_line1,
                "legal_local_address_line2": legal_local_address_line2,
                "legal_local_address_line3": legal_local_address_line3,
                "legal_local_address_line4": legal_local_address_line4,
                "legal_local_address_line5": legal_local_address_line5
            },
            "contact_local_address": {
                "contact_local_address_line1": contact_local_address_line1,
                "contact_local_address_line2": contact_local_address_line2,
                "contact_local_address_line3": contact_local_address_line3,
                "contact_local_address_line4": contact_local_address_line4,
                "contact_local_address_line5": contact_local_address_line5
            },
            "normal_local_address": {},
            "introducer_1": {
                "introducer_1_name": introducer_1_name,
                "introducer_1_account_no": introducer_1_account_no
            },
            "introducer_2": {
                "introducer_2_name": introducer_2_name,
                "introducer_2_account_no": introducer_2_account_no
            },
            "phone_home": phone_home,
            "phone_mobile": phone_mobile,
            "email": email,
            "education": education,
            "marital_status": marital_status,
            "profession": profession,
            "business_type": business_type,
            "financial": financial,
            "isic_code": isic_code,
            "managing_branch_code": managing_branch_code,
            "customer_status": customer_status,
            "classify": classify,
            "polists": polists,
            "repolists": repolists,
            "country_of_income": country_of_income,
            "fatca_status": fatca_status,
            "government_id": government_id,
            "international_id": international_id,
            "oversea_juristic_id": oversea_juristic_id,
            "gfmis_code": gfmis_code,
            "branch_code": branch_code,
            "group_code": group_code,
            "customer_credit_line": customer_credit_line,
            "currency_code": currency_code,
            "customer_type": customer_type,
            "primary_cif": primary_cif,
            "mdm_amount_status": mdm_amount_status,
            "mdm_request_status": mdm_request_status,
            "mdm_list_sub_type_code": mdm_list_sub_type_code,
            "mdm_list_sub_type_desc": mdm_list_sub_type_desc,
            "mdm_matching_by": mdm_matching_by,
            "mdm_final_kyc_status": mdm_final_kyc_status,
            "mdm_kyc_comment_code": mdm_kyc_comment_code,
            "mdm_kyc_comment_desc": mdm_kyc_comment_desc,
            "kyc_level": kyc_level,
            "kyc_update_date": kyc_update_date,
            "relation_customer_code1": relation_customer_code1,
            "relation_customer_code2": relation_customer_code2,
            "relation_customer_code3": relation_customer_code3,
            "relation_customer_code4": relation_customer_code4,
            "relation_customer_code5": relation_customer_code5,
            "customer_size": customer_size,
            "staff_code": staff_code,
            "customer_sub_type": customer_sub_type,
            "father_name": father_name,
            "is_restricted": is_restricted,
            "extension_fields": {
                "extension_fields_reason_for_other_economic_sector": extension_fields_reason_for_other_economic_sector,
                "extension_fields_reason_for_other_business_type": extension_fields_reason_for_other_business_type,
                "extension_fields_referral_field": extension_fields_referral_field,
                "extension_fields_reason_for_other_sub_economic_sector": extension_fields_reason_for_other_sub_economic_sector,
                "extension_fields_reason_for_other_occupation": extension_fields_reason_for_other_occupation,
                "extension_fields_reason_for_other_paper_type": extension_fields_reason_for_other_paper_type,
                "extension_fields_income": extension_fields_income,
                "extension_fields_introducer": extension_fields_introducer,
                "extension_fields_position": extension_fields_position,
                "extension_fields_remark_field_to_add": extension_fields_remark_field_to_add,
                "extension_fields_employer_name": extension_fields_employer_name,
                "extension_fields_fdi_info": extension_fields_fdi_info,
                "extension_fields_tin_number": extension_fields_tin_number
            }
        }
        return payload

    def SQL_UPDATE_CTM(self, id, customer_code, hocifcd=None, title=None, title_of_organization=None, currency_code_foreign_exchange_rate=None, currency_code_monetary_market=None, customer_credit_line2=None, customer_credit_line3=None, suffix=None, firstname=None, lastname=None, midname=None, fullname=None, firstname_local=None, lastname_local=None, midname_local=None, shortname=None, gender=None, date_of_birth=None, place_of_birth=None, nation=None, country=None, paper_type=None, paper_number=None, issue_date_of_paper=None, issue_place_of_paper=None, expire_date_of_paper=None, paper_type_sub=None, paper_number_sub=None, issue_date_of_sub_paper=None, issue_place_of_sub_paper=None, customer_group_type=None, customer_sub_group_type=None, sector=None, subsector=None, resident=None, legal_local_address_line1=None, legal_local_address_line2=None, legal_local_address_line3=None, legal_local_address_line4=None, legal_local_address_line5=None, contact_local_address_line1=None, contact_local_address_line2=None, contact_local_address_line3=None, contact_local_address_line4=None, contact_local_address_line5=None, normal_local_address_address_local=None, normal_local_address_province=None, normal_local_address_province_name=None, normal_local_address_village=None, normal_local_address_village_name=None, normal_local_address_sub_district=None, normal_local_address_sub_district_name=None, normal_local_address_district=None, normal_local_address_district_name=None, normal_local_address_address=None, normal_local_address_zipcode=None, introducer_1_name=None, introducer_1_account_no=None, introducer_2_name=None, introducer_2_account_no=None, phone_home=None, phone_mobile=None, email=None, education=None, marital_status=None, profession=None, business_type=None, financial=None, isic_code=None, managing_branch_code=None, classify=None, polists=None, repolists=None, country_of_income=None, fatca_status=None, government_id=None, international_id=None, oversea_juristic_id=None, gfmis_code=None, last_update_date=None, customer_size=None, group_id=None, customer_credit_line=None, currency_code=None, customer_type=None, primary_cif=None, mdm_amount_status=None, mdm_request_status=None, mdm_list_sub_type_code=None, mdm_list_sub_type_desc=None, mdm_matching_by=None, mdm_final_kyc_status=None, mdm_kyc_comment_code=None, mdm_kyc_comment_desc=None, kyc_level=None, kyc_update_date=None, kyc_override=None, kyc_override_descr=None, customer_sub_type=None, approve_modify=None, father_name=None, is_restricted=None, bank_identification=None, extension_fields_reason_for_other_economic_sector=None, extension_fields_reason_for_other_business_type=None, extension_fields_referral_field=None, extension_fields_reason_for_other_sub_economic_sector=None, extension_fields_reason_for_other_occupation=None, extension_fields_reason_for_other_paper_type=None, extension_fields_income=None, extension_fields_introducer=None, extension_fields_position=None, extension_fields_remark_field_to_add=None, extension_fields_employer_name=None, extension_fields_fdi_info=None, extension_fields_tin_number=None):
        if not hocifcd:
            hocifcd=''
        if not title:
            title=''
        if not title_of_organization:
            title_of_organization=None
        if not currency_code_foreign_exchange_rate:
            currency_code_foreign_exchange_rate='MMK'
        if not currency_code_monetary_market:
            currency_code_monetary_market='MMK'
        if not customer_credit_line2:
            customer_credit_line2=0
        if not customer_credit_line3:
            customer_credit_line3=0
        if not suffix:
            suffix=None
        if not firstname:
            firstname=''
        if not lastname:
            lastname=''
        if not midname:
            midname=''
        if not fullname:
            fullname=''
        if not firstname_local:
            firstname_local=''
        if not lastname_local:
            lastname_local=''
        if not midname_local:
            midname_local=''
        if not shortname:
            shortname=''
        if not gender:
            gender=''
        if not date_of_birth:
            date_of_birth=''
        if not place_of_birth:
            place_of_birth=None
        if not nation:
            nation='MM'
        if not country:
            country=None
        if not paper_type:
            paper_type=''
        if not paper_number:
            paper_number=''
        if not issue_date_of_paper:
            issue_date_of_paper=None
        if not issue_place_of_paper:
            issue_place_of_paper=''
        if not expire_date_of_paper:
            expire_date_of_paper=None
        if not paper_type_sub:
            paper_type_sub='N'
        if not paper_number_sub:
            paper_number_sub=''
        if not issue_date_of_sub_paper:
            issue_date_of_sub_paper=None
        if not issue_place_of_sub_paper:
            issue_place_of_sub_paper=''
        if not customer_group_type:
            customer_group_type=None
        if not customer_sub_group_type:
            customer_sub_group_type=None
        if not sector:
            sector=None
        if not subsector:
            subsector=None
        if not resident:
            resident='R'
        if not legal_local_address_line1:
            legal_local_address_line1=''
        if not legal_local_address_line2:
            legal_local_address_line2=''
        if not legal_local_address_line3:
            legal_local_address_line3=''
        if not legal_local_address_line4:
            legal_local_address_line4=''
        if not legal_local_address_line5:
            legal_local_address_line5=''
        if not contact_local_address_line1:
            contact_local_address_line1=''
        if not contact_local_address_line2:
            contact_local_address_line2=''
        if not contact_local_address_line3:
            contact_local_address_line3=''
        if not contact_local_address_line4:
            contact_local_address_line4=''
        if not contact_local_address_line5:
            contact_local_address_line5=''
        if not normal_local_address_address_local:
            normal_local_address_address_local=''
        if not normal_local_address_province:
            normal_local_address_province=''
        if not normal_local_address_province_name:
            normal_local_address_province_name=''
        if not normal_local_address_village:
            normal_local_address_village=''
        if not normal_local_address_village_name:
            normal_local_address_village_name=''
        if not normal_local_address_sub_district:
            normal_local_address_sub_district=''
        if not normal_local_address_sub_district_name:
            normal_local_address_sub_district_name=''
        if not normal_local_address_district:
            normal_local_address_district=''
        if not normal_local_address_district_name:
            normal_local_address_district_name=''
        if not normal_local_address_address:
            normal_local_address_address=''
        if not normal_local_address_zipcode:
            normal_local_address_zipcode=''
        if not introducer_1_name:
            introducer_1_name=''
        if not introducer_1_account_no:
            introducer_1_account_no=''
        if not introducer_2_name:
            introducer_2_name=''
        if not introducer_2_account_no:
            introducer_2_account_no=''
        if not phone_home:
            phone_home=''
        if not phone_mobile:
            phone_mobile=''
        if not email:
            email=''
        if not education:
            education=''
        if not marital_status:
            marital_status=''
        if not profession:
            profession=''
        if not business_type:
            business_type=''
        if not financial:
            financial=None
        if not isic_code:
            isic_code=None
        if not managing_branch_code:
            managing_branch_code=''
        if not classify:
            classify='N'
        if not polists:
            polists='-'
        if not repolists:
            repolists='-'
        if not country_of_income:
            country_of_income='MM'
        if not fatca_status:
            fatca_status='-'
        if not government_id:
            government_id=None
        if not international_id:
            international_id=None
        if not oversea_juristic_id:
            oversea_juristic_id=None
        if not gfmis_code:
            gfmis_code=None
        if not last_update_date:
            last_update_date=None
        if not customer_size:
            customer_size='S'
        if not group_id:
            group_id=''
        if not customer_credit_line:
            customer_credit_line=0
        if not currency_code:
            currency_code='MMK'
        if not customer_type:
            customer_type=''
        if not primary_cif:
            primary_cif='-'
        if not mdm_amount_status:
            mdm_amount_status=''
        if not mdm_request_status:
            mdm_request_status=''
        if not mdm_list_sub_type_code:
            mdm_list_sub_type_code=''
        if not mdm_list_sub_type_desc:
            mdm_list_sub_type_desc=''
        if not mdm_matching_by:
            mdm_matching_by=''
        if not mdm_final_kyc_status:
            mdm_final_kyc_status=''
        if not mdm_kyc_comment_code:
            mdm_kyc_comment_code=''
        if not mdm_kyc_comment_desc:
            mdm_kyc_comment_desc=''
        if not kyc_level:
            kyc_level='3'
        if not kyc_update_date:
            kyc_update_date='2022-02-25T05:51:26.127Z'
        if not kyc_override:
            kyc_override=''
        if not kyc_override_descr:
            kyc_override_descr=''
        if not customer_sub_type:
            customer_sub_type=''
        if not approve_modify:
            approve_modify=True
        if not father_name:
            father_name=''
        if not is_restricted:
            is_restricted='N'
        if not bank_identification:
            bank_identification='-'
        if not extension_fields_reason_for_other_economic_sector:
            extension_fields_reason_for_other_economic_sector=None
        if not extension_fields_reason_for_other_business_type:
            extension_fields_reason_for_other_business_type=None
        if not extension_fields_referral_field:
            extension_fields_referral_field=None
        if not extension_fields_reason_for_other_sub_economic_sector:
            extension_fields_reason_for_other_sub_economic_sector=None
        if not extension_fields_reason_for_other_occupation:
            extension_fields_reason_for_other_occupation=None
        if not extension_fields_reason_for_other_paper_type:
            extension_fields_reason_for_other_paper_type=None
        if not extension_fields_income:
            extension_fields_income=None
        if not extension_fields_introducer:
            extension_fields_introducer=None
        if not extension_fields_position:
            extension_fields_position=None
        if not extension_fields_remark_field_to_add:
            extension_fields_remark_field_to_add=None
        if not extension_fields_employer_name:
            extension_fields_employer_name=None
        if not extension_fields_fdi_info:
            extension_fields_fdi_info=None
        if not extension_fields_tin_number:
            extension_fields_tin_number=None
        payload = {
            "id": id,
            "hocifcd": hocifcd,
            "title": title,
            "title_of_organization": title_of_organization,
            "currency_code_foreign_exchange_rate": currency_code_foreign_exchange_rate,
            "currency_code_monetary_market": currency_code_monetary_market,
            "customer_credit_line2": customer_credit_line2,
            "customer_credit_line3": customer_credit_line3,
            "suffix": suffix,
            "firstname": firstname,
            "lastname": lastname,
            "midname": midname,
            "fullname": fullname,
            "firstname_local": firstname_local,
            "lastname_local": lastname_local,
            "midname_local": midname_local,
            "shortname": shortname,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "place_of_birth": place_of_birth,
            "nation": nation,
            "country": country,
            "paper_type": paper_type,
            "paper_number": paper_number,
            "issue_date_of_paper": issue_date_of_paper,
            "issue_place_of_paper": issue_place_of_paper,
            "expire_date_of_paper": expire_date_of_paper,
            "paper_type_sub": paper_type_sub,
            "paper_number_sub": paper_number_sub,
            "issue_date_of_sub_paper": issue_date_of_sub_paper,
            "issue_place_of_sub_paper": issue_place_of_sub_paper,
            "customer_group_type": customer_group_type,
            "customer_sub_group_type": customer_sub_group_type,
            "sector": sector,
            "subsector": subsector,
            "resident": resident,
            "legal_local_address": {
                "legal_local_address_line1": legal_local_address_line1,
                "legal_local_address_line2": legal_local_address_line2,
                "legal_local_address_line3": legal_local_address_line3,
                "legal_local_address_line4": legal_local_address_line4,
                "legal_local_address_line5": legal_local_address_line5
            },
            "contact_local_address": {
                "contact_local_address_line1": contact_local_address_line1,
                "contact_local_address_line2": contact_local_address_line2,
                "contact_local_address_line3": contact_local_address_line3,
                "contact_local_address_line4": contact_local_address_line4,
                "contact_local_address_line5": contact_local_address_line5
            },
            "normal_local_address": {
                "normal_local_address_address_local": normal_local_address_address_local,
                "normal_local_address_province": normal_local_address_province,
                "normal_local_address_province_name": normal_local_address_province_name,
                "normal_local_address_village": normal_local_address_village,
                "normal_local_address_village_name": normal_local_address_village_name,
                "normal_local_address_sub_district": normal_local_address_sub_district,
                "normal_local_address_sub_district_name": normal_local_address_sub_district_name,
                "normal_local_address_district": normal_local_address_district,
                "normal_local_address_district_name": normal_local_address_district_name,
                "normal_local_address_address": normal_local_address_address,
                "normal_local_address_zipcode": normal_local_address_zipcode
            },
            "introducer_1": {
                "introducer_1_name": introducer_1_name,
                "introducer_1_account_no": introducer_1_account_no
            },
            "introducer_2": {
                "introducer_2_name": introducer_2_name,
                "introducer_2_account_no": introducer_2_account_no
            },
            "phone_home": phone_home,
            "phone_mobile": phone_mobile,
            "email": email,
            "education": education,
            "marital_status": marital_status,
            "profession": profession,
            "business_type": business_type,
            "financial": financial,
            "isic_code": isic_code,
            "managing_branch_code": managing_branch_code,
            "classify": classify,
            "polists": polists,
            "repolists": repolists,
            "country_of_income": country_of_income,
            "fatca_status": fatca_status,
            "government_id": government_id,
            "international_id": international_id,
            "oversea_juristic_id": oversea_juristic_id,
            "gfmis_code": gfmis_code,
            "last_update_date": last_update_date,
            "customer_size": customer_size,
            "group_id": group_id,
            "customer_credit_line": customer_credit_line,
            "currency_code": currency_code,
            "customer_type": customer_type,
            "primary_cif": primary_cif,
            "mdm_amount_status": mdm_amount_status,
            "mdm_request_status": mdm_request_status,
            "mdm_list_sub_type_code": mdm_list_sub_type_code,
            "mdm_list_sub_type_desc": mdm_list_sub_type_desc,
            "mdm_matching_by": mdm_matching_by,
            "mdm_final_kyc_status": mdm_final_kyc_status,
            "mdm_kyc_comment_code": mdm_kyc_comment_code,
            "mdm_kyc_comment_desc": mdm_kyc_comment_desc,
            "kyc_level": kyc_level,
            "kyc_update_date": kyc_update_date,
            "kyc_override": kyc_override,
            "kyc_override_descr": kyc_override_descr,
            "customer_sub_type": customer_sub_type,
            "approve_modify": approve_modify,
            "father_name": father_name,
            "customer_code": customer_code,
            "is_restricted": is_restricted,
            "bank_identification": bank_identification,
            "extension_fields": {
                "extension_fields_reason_for_other_economic_sector": extension_fields_reason_for_other_economic_sector,
                "extension_fields_reason_for_other_business_type": extension_fields_reason_for_other_business_type,
                "extension_fields_referral_field": extension_fields_referral_field,
                "extension_fields_reason_for_other_sub_economic_sector": extension_fields_reason_for_other_sub_economic_sector,
                "extension_fields_reason_for_other_occupation": extension_fields_reason_for_other_occupation,
                "extension_fields_reason_for_other_paper_type": extension_fields_reason_for_other_paper_type,
                "extension_fields_income": extension_fields_income,
                "extension_fields_introducer": extension_fields_introducer,
                "extension_fields_position": extension_fields_position,
                "extension_fields_remark_field_to_add": extension_fields_remark_field_to_add,
                "extension_fields_employer_name": extension_fields_employer_name,
                "extension_fields_fdi_info": extension_fields_fdi_info,
                "extension_fields_tin_number": extension_fields_tin_number
            }
        }
        return payload

    def SQL_CTM_APR(self, transaction_id, customer_code, is_restricted=None):
        if not is_restricted:
            is_restricted=''
        payload = {
            "transaction_id": transaction_id,
            "customer_code": customer_code,
            "is_restricted": is_restricted
        }
        return payload

    def PRINT_CUSTOMER_INFO(self, customer_code, customer_type=None):
        if not customer_type:
            customer_type='C'
        payload = {
            "customer_code": customer_code,
            "customer_type": customer_type
        }
        return payload

    def SQL_INSERT_MEDIA(self, file_upload_id, media_name=None, customer_code=None, reference_type=None, expire_date=None, other=None, media_status=None, media_type=None, open_date=None, last_update_date=None, infor1=None, infor2=None):
        if not media_name:
            media_name=''
        if not customer_code:
            customer_code=''
        if not reference_type:
            reference_type=''
        if not expire_date:
            expire_date=None
        if not other:
            other=''
        if not media_status:
            media_status=''
        if not media_type:
            media_type=''
        if not open_date:
            open_date=None
        if not last_update_date:
            last_update_date=None
        if not infor1:
            infor1=''
        if not infor2:
            infor2=''
        payload = {
            "file_upload_id": file_upload_id,
            "media_name": media_name,
            "customer_code": customer_code,
            "reference_type": reference_type,
            "expire_date": expire_date,
            "other": other,
            "media_status": media_status,
            "media_type": media_type,
            "open_date": open_date,
            "last_update_date": last_update_date,
            "infor1": infor1,
            "infor2": infor2
        }
        return payload

    def SQL_APPROVE_MEDIA(self, id):
        payload = {
            "id": id
        }
        return payload

    def DPT_UPDATE_DEPOSIT(self, id, account_number, account_name=None, agent_hub_referral=None, approve_modify=None, business_purpose_code=None, contract_number=None, credit_interest=None, credit_interest_tenor=None, credit_interest_tenor_unit=None, crediting_interest=None, dormant_period=None, dormant_period_unit=None, early_withdrawal=None, initial_deposit_amount=None, interest_due_on_holiday=None, interest_tenor=None, interest_tenor_unit=None, list_ifc_balance=None, list_od_ifc_balance=None, minimum_deposit_amount=None, minimum_tenor=None, minimum_tenor_allow_early_withdrawal=None, minimum_tenor_allow_early_withdrawal_unit=None, minimum_tenor_unit=None, module_code=None, multiple_deposit_allow=None, multiple_withdrawal_allow=None, principal_due_on_holiday=None, relation_customers=None, restruct=None, rollover=None, rollover_to_catalog=None, secure_rate=None, secure_type=None, statement_format=None, statement_tenor=None, statement_tenor_unit=None, sweeping_status=None, surplus_amount=None, deficit_amount=None, limit_amount=None, sweeping_mode=None, sweeping_type=None, surplus_account=None, surplus_account_name=None, deficit_account_name=None, deficit_account=None, sweeping_from_date=None, sweeping_to_date=None, is_restricted=None, extension_fields_reason_of_account_opening=None, extension_fields_relationship_manager=None, od_extension_fields_credit_classification=None, od_extension_fields_notification_type=None):
        if not account_name:
            account_name=''
        if not agent_hub_referral:
            agent_hub_referral=''
        if not approve_modify:
            approve_modify=True
        if not business_purpose_code:
            business_purpose_code=''
        if not contract_number:
            contract_number=''
        if not credit_interest:
            credit_interest='Y'
        if not credit_interest_tenor:
            credit_interest_tenor=1
        if not credit_interest_tenor_unit:
            credit_interest_tenor_unit='D'
        if not crediting_interest:
            crediting_interest=0
        if not dormant_period:
            dormant_period=1095
        if not dormant_period_unit:
            dormant_period_unit='D'
        if not early_withdrawal:
            early_withdrawal='R'
        if not initial_deposit_amount:
            initial_deposit_amount=0
        if not interest_due_on_holiday:
            interest_due_on_holiday=0
        if not interest_tenor:
            interest_tenor=0
        if not interest_tenor_unit:
            interest_tenor_unit='L'
        if not list_ifc_balance:
            list_ifc_balance=[]
        if not list_od_ifc_balance:
            list_od_ifc_balance=[]
        if not minimum_deposit_amount:
            minimum_deposit_amount=0
        if not minimum_tenor:
            minimum_tenor=0
        if not minimum_tenor_allow_early_withdrawal:
            minimum_tenor_allow_early_withdrawal=1
        if not minimum_tenor_allow_early_withdrawal_unit:
            minimum_tenor_allow_early_withdrawal_unit='M'
        if not minimum_tenor_unit:
            minimum_tenor_unit='L'
        if not module_code:
            module_code='DPT'
        if not multiple_deposit_allow:
            multiple_deposit_allow='N'
        if not multiple_withdrawal_allow:
            multiple_withdrawal_allow='N'
        if not principal_due_on_holiday:
            principal_due_on_holiday=0
        if not relation_customers:
            relation_customers=[]
        if not restruct:
            restruct=''
        if not rollover:
            rollover='P'
        if not rollover_to_catalog:
            rollover_to_catalog=''
        if not secure_rate:
            secure_rate=0
        if not secure_type:
            secure_type=''
        if not statement_format:
            statement_format='E'
        if not statement_tenor:
            statement_tenor=1
        if not statement_tenor_unit:
            statement_tenor_unit='M'
        if not sweeping_status:
            sweeping_status=False
        if not surplus_amount:
            surplus_amount=0
        if not deficit_amount:
            deficit_amount=0
        if not limit_amount:
            limit_amount=0
        if not sweeping_mode:
            sweeping_mode=None
        if not sweeping_type:
            sweeping_type=None
        if not surplus_account:
            surplus_account=''
        if not surplus_account_name:
            surplus_account_name=''
        if not deficit_account_name:
            deficit_account_name=''
        if not deficit_account:
            deficit_account=''
        if not sweeping_from_date:
            sweeping_from_date=None
        if not sweeping_to_date:
            sweeping_to_date=None
        if not is_restricted:
            is_restricted='N'
        if not extension_fields_reason_of_account_opening:
            extension_fields_reason_of_account_opening=None
        if not extension_fields_relationship_manager:
            extension_fields_relationship_manager=None
        if not od_extension_fields_credit_classification:
            od_extension_fields_credit_classification='-'
        if not od_extension_fields_notification_type:
            od_extension_fields_notification_type=[]
        payload = {
            "account_name": account_name,
            "account_number": account_number,
            "agent_hub_referral": agent_hub_referral,
            "approve_modify": approve_modify,
            "business_purpose_code": business_purpose_code,
            "contract_number": contract_number,
            "credit_interest": credit_interest,
            "credit_interest_tenor": credit_interest_tenor,
            "credit_interest_tenor_unit": credit_interest_tenor_unit,
            "crediting_interest": crediting_interest,
            "dormant_period": dormant_period,
            "dormant_period_unit": dormant_period_unit,
            "early_withdrawal": early_withdrawal,
            "id": id,
            "initial_deposit_amount": initial_deposit_amount,
            "interest_due_on_holiday": interest_due_on_holiday,
            "interest_tenor": interest_tenor,
            "interest_tenor_unit": interest_tenor_unit,
            "list_ifc_balance": list_ifc_balance,
            "list_od_ifc_balance": list_od_ifc_balance,
            "minimum_deposit_amount": minimum_deposit_amount,
            "minimum_tenor": minimum_tenor,
            "minimum_tenor_allow_early_withdrawal": minimum_tenor_allow_early_withdrawal,
            "minimum_tenor_allow_early_withdrawal_unit": minimum_tenor_allow_early_withdrawal_unit,
            "minimum_tenor_unit": minimum_tenor_unit,
            "module_code": module_code,
            "multiple_deposit_allow": multiple_deposit_allow,
            "multiple_withdrawal_allow": multiple_withdrawal_allow,
            "principal_due_on_holiday": principal_due_on_holiday,
            "relation_customers": relation_customers,
            "restruct": restruct,
            "rollover": rollover,
            "rollover_to_catalog": rollover_to_catalog,
            "secure_rate": secure_rate,
            "secure_type": secure_type,
            "statement_format": statement_format,
            "statement_tenor": statement_tenor,
            "statement_tenor_unit": statement_tenor_unit,
            "sweeping_status": sweeping_status,
            "surplus_amount": surplus_amount,
            "deficit_amount": deficit_amount,
            "limit_amount": limit_amount,
            "sweeping_mode": sweeping_mode,
            "sweeping_type": sweeping_type,
            "surplus_account": surplus_account,
            "surplus_account_name": surplus_account_name,
            "deficit_account_name": deficit_account_name,
            "deficit_account": deficit_account,
            "sweeping_from_date": sweeping_from_date,
            "sweeping_to_date": sweeping_to_date,
            "is_restricted": is_restricted,
            "extension_fields": {
                "extension_fields_reason_of_account_opening": extension_fields_reason_of_account_opening,
                "extension_fields_relationship_manager": extension_fields_relationship_manager
            },
            "od_extension_fields": {
                "od_extension_fields_credit_classification": od_extension_fields_credit_classification,
                "od_extension_fields_notification_type": od_extension_fields_notification_type
            }
        }
        return payload

    def DPT_VIEW_MODIFY_EXT_FIELD(self, account_number, tx_reference_id, module_code=None):
        if not module_code:
            module_code='DPT'
        payload = {
            "account_number": account_number,
            "module_code": module_code,
            "tx_reference_id": tx_reference_id
        }
        return payload

    def DPT_APPROVE_MODIFY(self, account_number, tx_reference_id, module_code=None):
        if not module_code:
            module_code='DPT'
        payload = {
            "account_number": account_number,
            "module_code": module_code,
            "tx_reference_id": tx_reference_id
        }
        return payload

    def DPT_DELETE_ACCOUNTLINKAGE(self, master_account_number):
        payload = {
            "master_account_number": master_account_number
        }
        return payload

    def ADM_REFRESH_BRANCH(self, page_index=None, page_size=None, search_text=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        if not search_text:
            search_text=''
        payload = {
            "page_index": page_index,
            "page_size": page_size,
            "search_text": search_text
        }
        return payload

    def ADM_REFRESH_BRANCH_BY_USER(self, page_index=None, page_size=None, search_text=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        if not search_text:
            search_text=''
        payload = {
            "page_index": page_index,
            "page_size": page_size,
            "search_text": search_text
        }
        return payload

    def ADM_CLOSE_BRANCH(self, id, branch_code):
        payload = {
            "id": id,
            "branch_code": branch_code
        }
        return payload

    def ADM_OPEN_BRANCH(self, id):
        payload = {
            "id": id
        }
        return payload

    def ADM_ADVANCED_SEARCH_ROLE_OF_USER(self, role_id, user_code=None, page_size=None, page_index=None):
        if not page_size:
            page_size=0
        if not page_index:
            page_index=0
        if not user_code:
            user_code=None
        payload = {
            "page_size": page_size,
            "page_index": page_index,
            "role_id": role_id,
            "user_code": user_code
        }
        return payload

    def ADM_SIMPLE_SEARCH_USER_ACCOUNT(self, page_index=None, page_size=None, search_text=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        if not search_text:
            search_text=''
        payload = {
            "page_index": page_index,
            "page_size": page_size,
            "search_text": search_text
        }
        return payload

    def ADM_UPDATE_LIST_USER_RIGHT(self, list_user_right=None):
        if not list_user_right:
            list_user_right=[]
        payload = {
            "list_user_right": list_user_right
        }
        return payload

    def ACT_ACCHRT_SER_SIMPLE(self, page_index=None, page_size=None, search_text=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        if not search_text:
            search_text=''
        payload = {
            "page_index": page_index,
            "page_size": page_size,
            "search_text": search_text
        }
        return payload

    def ACT_ACCHRT_INS(self, account_level, currency_code, account_number, is_multi_currency=None, account_name=None, short_account_name=None, laos_name=None, thai_name=None, khmer_name=None, vietnamese_name=None, account_classification=None, reverse_balance=None, balance_side=None, posting_side=None, account_group=None, account_categories=None, direct_posting=None, is_visible=None, job_process_option=None, branch_code=None, ref_account_number=None, references_number=None):
        if not account_level:
            account_level=1
        if not is_multi_currency:
            is_multi_currency='Y'
        if not currency_code:
            currency_code=''
        if not account_number:
            account_number=''
        if not account_name:
            account_name=''
        if not short_account_name:
            short_account_name=''
        if not laos_name:
            laos_name=''
        if not thai_name:
            thai_name=''
        if not khmer_name:
            khmer_name=''
        if not vietnamese_name:
            vietnamese_name=''
        if not account_classification:
            account_classification='A'
        if not reverse_balance:
            reverse_balance='N'
        if not balance_side:
            balance_side='B'
        if not posting_side:
            posting_side='A'
        if not account_group:
            account_group='N'
        if not account_categories:
            account_categories='N'
        if not direct_posting:
            direct_posting='N'
        if not is_visible:
            is_visible='N'
        if not job_process_option:
            job_process_option='N'
        if not branch_code:
            branch_code=''
        if not ref_account_number:
            ref_account_number=None
        if not references_number:
            references_number=None
        payload = {
            "account_level": account_level,
            "is_multi_currency": is_multi_currency,
            "currency_code": currency_code,
            "account_number": account_number,
            "account_name": account_name,
            "short_account_name": short_account_name,
            "multi_value_name": {
                "laos_name": laos_name,
                "thai_name": thai_name,
                "khmer_name": khmer_name,
                "vietnamese_name": vietnamese_name
            },
            "account_classification": account_classification,
            "reverse_balance": reverse_balance,
            "balance_side": balance_side,
            "posting_side": posting_side,
            "account_group": account_group,
            "account_categories": account_categories,
            "direct_posting": direct_posting,
            "is_visible": is_visible,
            "job_process_option": job_process_option,
            "branch_code": branch_code,
            "ref_account_number": ref_account_number,
            "references_number": references_number
        }
        return payload

    def CRD_SEARCH_SP_CREDIT(self, page_index=None, page_size=None, search_text=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        if not search_text:
            search_text=''
        payload = {
            "page_index": page_index,
            "page_size": page_size,
            "search_text": search_text
        }
        return payload

    def CRD_VIEW_CREDIT(self, id):
        payload = {
            "id": id
        }
        return payload

    def PMT_SEARCH_SP_QUEUE_INWAR(self, page_index=None, page_size=None, search_text=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        if not search_text:
            search_text=''
        payload = {
            "page_index": page_index,
            "page_size": page_size,
            "search_text": search_text
        }
        return payload

    def FX_FXRATE_GETFXRATE(self, branch_code_fx):
        payload = {
            "branch_code_fx": branch_code_fx
        }
        return payload

    def TRS_SEARCH_ACCOUNT(self, page_index=None, page_size=None, search_text=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        if not search_text:
            search_text=''
        payload = {
            "page_index": page_index,
            "page_size": page_size,
            "search_text": search_text
        }
        return payload

    def TRS_VIEW_ACCOUNT(self, id):
        payload = {
            "id": id
        }
        return payload

