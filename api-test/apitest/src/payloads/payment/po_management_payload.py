from datetime import datetime

class PoManagementPayload(object):
    def add(self, pmt_transaction_number=None, transaction_date_pmt=None, transaction_ref_id=None, transaction_code_pmt=None, catalog_code=None, reference_number=None, issue_date=None, effective_date=None, expire_date=None, cheque_number=None, bill_number=None, debit_currency=None, credit_currency=None, debit_amount=None, credit_amount=None, base_amount=None, exchange_rate=None, account_number1=None, account_number2=None, priority=None, purpose=None, sub_purpose=None, country=None, more_description=None, receiver_license=None, receiver_name=None, receiver_address=None, receiver_phone=None, receiver_type=None, sender_license=None, sender_name=None, sender_address=None, sender_phone=None, sender_type=None, send_bank=None, send_bank_branch=None, beneficary_bank=None, beneficary_bank_branch=None, is_inform_bank=None, collecting_bank=None, group_pmt_inst=None, good_type=None, good_list=None, message_direction=None, message_description=None, value_paper_status=None, message_status_history=None, paid_amount=None, fee_amount=None, fee_paid=None, pmt_order_type=None, pmt_order_status=None):
        if not pmt_transaction_number:
            pmt_transaction_number = ''
        if not transaction_date_pmt:
            transaction_date_pmt = ''
        if not transaction_ref_id:
            transaction_ref_id = ''
        if not transaction_code_pmt:
            transaction_code_pmt = ''
        if not catalog_code:
            catalog_code = ''
        if not reference_number:
            reference_number = ''
        if not issue_date:
            issue_date = ''
        if not effective_date:
            effective_date = ''
        if not expire_date:
            expire_date = ''
        if not cheque_number:
            cheque_number = ''
        if not bill_number:
            bill_number = ''
        if not debit_currency:
            debit_currency = ''
        if not credit_currency:
            credit_currency = ''
        if not debit_amount:
            debit_amount = 0
        if not credit_amount:
            credit_amount = 0
        if not base_amount:
            base_amount = 0
        if not exchange_rate:
            exchange_rate = 0
        if not account_number1:
            account_number1 = ''
        if not account_number2:
            account_number2 = ''
        if not priority:
            priority = ''
        if not purpose:
            purpose = ''
        if not sub_purpose:
            sub_purpose = ''
        if not country:
            country = ''
        if not more_description:
            more_description = ''
        if not receiver_license:
            receiver_license = ''
        if not receiver_name:
            receiver_name = ''
        if not receiver_address:
            receiver_address = ''
        if not receiver_phone:
            receiver_phone = ''
        if not receiver_type:
            receiver_type = ''
        if not sender_license:
            sender_license = ''
        if not sender_name:
            sender_name = ''
        if not sender_address:
            sender_address = ''
        if not sender_phone:
            sender_phone = ''
        if not sender_type:
            sender_type = ''
        if not send_bank:
            send_bank = ''
        if not send_bank_branch:
            send_bank_branch = ''
        if not beneficary_bank:
            beneficary_bank = ''
        if not beneficary_bank_branch:
            beneficary_bank_branch = ''
        if not is_inform_bank:
            is_inform_bank = ''
        if not collecting_bank:
            collecting_bank = ''
        if not group_pmt_inst:
            group_pmt_inst = ''
        if not good_type:
            good_type = ''
        if not good_list:
            good_list = ''
        if not message_direction:
            message_direction = ''
        if not message_description:
            message_description = ''
        if not value_paper_status:
            value_paper_status = ''
        if not message_status_history:
            message_status_history = ''
        if not paid_amount:
            paid_amount = 0
        if not fee_amount:
            fee_amount = 0
        if not fee_paid:
            fee_paid = 0
        if not pmt_order_type:
            pmt_order_type = ''
        if not pmt_order_status:
            pmt_order_status = ''
        payload = {
            "pmt_transaction_number": pmt_transaction_number,
            "transaction_date_pmt": transaction_date_pmt,
            "transaction_ref_id": transaction_ref_id,
            "transaction_code_pmt": transaction_code_pmt,
            "catalog_code": catalog_code,
            "reference_number": reference_number,
            "issue_date": issue_date,
            "effective_date": effective_date,
            "expire_date": expire_date,
            "cheque_number": cheque_number,
            "bill_number": bill_number,
            "debit_currency": debit_currency,
            "credit_currency": credit_currency,
            "debit_amount": debit_amount,
            "credit_amount": credit_amount,
            "base_amount": base_amount,
            "exchange_rate": exchange_rate,
            "account_number1": account_number1,
            "account_number2": account_number2,
            "priority": priority,
            "purpose": purpose,
            "sub_purpose": sub_purpose,
            "country": country,
            "more_description": more_description,
            "receiver_license": receiver_license,
            "receiver_name": receiver_name,
            "receiver_address": receiver_address,
            "receiver_phone": receiver_phone,
            "receiver_type": receiver_type,
            "sender_license": sender_license,
            "sender_name": sender_name,
            "sender_address": sender_address,
            "sender_phone": sender_phone,
            "sender_type": sender_type,
            "send_bank": send_bank,
            "send_bank_branch": send_bank_branch,
            "beneficary_bank": beneficary_bank,
            "beneficary_bank_branch": beneficary_bank_branch,
            "is_inform_bank": is_inform_bank,
            "collecting_bank": collecting_bank,
            "group_pmt_inst": group_pmt_inst,
            "good_type": good_type,
            "good_list": good_list,
            "message_direction": message_direction,
            "message_description": message_description,
            "value_paper_status": value_paper_status,
            "message_status_history": message_status_history,
            "paid_amount": paid_amount,
            "fee_amount": fee_amount,
            "fee_paid": fee_paid,
            "pmt_order_type": pmt_order_type,
            "pmt_order_status": pmt_order_status
        }
        return payload

    def update(self, id=None, pmt_transaction_number=None, transaction_date_pmt=None, transaction_ref_id=None, transaction_code_pmt=None, catalog_code=None, reference_number=None, issue_date=None, effective_date=None, expire_date=None, cheque_number=None, bill_number=None, debit_currency=None, credit_currency=None, debit_amount=None, credit_amount=None, base_amount=None, exchange_rate=None, account_number1=None, account_number2=None, priority=None, purpose=None, sub_purpose=None, country=None, more_description=None, receiver_license=None, receiver_name=None, receiver_address=None, receiver_phone=None, receiver_type=None, sender_license=None, sender_name=None, sender_address=None, sender_phone=None, sender_type=None, send_bank=None, send_bank_branch=None, beneficary_bank=None, beneficary_bank_branch=None, is_inform_bank=None, collecting_bank=None, group_pmt_inst=None, good_type=None, good_list=None, message_direction=None, message_description=None, value_paper_status=None, message_status_history=None, paid_amount=None, fee_amount=None, fee_paid=None, pmt_order_type=None, pmt_order_status=None):
        if not id:
            id = 0
        if not pmt_transaction_number:
            pmt_transaction_number = ''
        if not transaction_date_pmt:
            transaction_date_pmt = ''
        if not transaction_ref_id:
            transaction_ref_id = ''
        if not transaction_code_pmt:
            transaction_code_pmt = ''
        if not catalog_code:
            catalog_code = ''
        if not reference_number:
            reference_number = ''
        if not issue_date:
            issue_date = ''
        if not effective_date:
            effective_date = ''
        if not expire_date:
            expire_date = ''
        if not cheque_number:
            cheque_number = ''
        if not bill_number:
            bill_number = ''
        if not debit_currency:
            debit_currency = ''
        if not credit_currency:
            credit_currency = ''
        if not debit_amount:
            debit_amount = 0
        if not credit_amount:
            credit_amount = 0
        if not base_amount:
            base_amount = 0
        if not exchange_rate:
            exchange_rate = 0
        if not account_number1:
            account_number1 = ''
        if not account_number2:
            account_number2 = ''
        if not priority:
            priority = ''
        if not purpose:
            purpose = ''
        if not sub_purpose:
            sub_purpose = ''
        if not country:
            country = ''
        if not more_description:
            more_description = ''
        if not receiver_license:
            receiver_license = ''
        if not receiver_name:
            receiver_name = ''
        if not receiver_address:
            receiver_address = ''
        if not receiver_phone:
            receiver_phone = ''
        if not receiver_type:
            receiver_type = ''
        if not sender_license:
            sender_license = ''
        if not sender_name:
            sender_name = ''
        if not sender_address:
            sender_address = ''
        if not sender_phone:
            sender_phone = ''
        if not sender_type:
            sender_type = ''
        if not send_bank:
            send_bank = ''
        if not send_bank_branch:
            send_bank_branch = ''
        if not beneficary_bank:
            beneficary_bank = ''
        if not beneficary_bank_branch:
            beneficary_bank_branch = ''
        if not is_inform_bank:
            is_inform_bank = ''
        if not collecting_bank:
            collecting_bank = ''
        if not group_pmt_inst:
            group_pmt_inst = ''
        if not good_type:
            good_type = ''
        if not good_list:
            good_list = ''
        if not message_direction:
            message_direction = ''
        if not message_description:
            message_description = ''
        if not value_paper_status:
            value_paper_status = ''
        if not message_status_history:
            message_status_history = ''
        if not paid_amount:
            paid_amount = 0
        if not fee_amount:
            fee_amount = 0
        if not fee_paid:
            fee_paid = 0
        if not pmt_order_type:
            pmt_order_type = ''
        if not pmt_order_status:
            pmt_order_status = ''
        payload = {
            "id": id,
            "pmt_transaction_number": pmt_transaction_number,
            "transaction_date_pmt": transaction_date_pmt,
            "transaction_ref_id": transaction_ref_id,
            "transaction_code_pmt": transaction_code_pmt,
            "catalog_code": catalog_code,
            "reference_number": reference_number,
            "issue_date": issue_date,
            "effective_date": effective_date,
            "expire_date": expire_date,
            "cheque_number": cheque_number,
            "bill_number": bill_number,
            "debit_currency": debit_currency,
            "credit_currency": credit_currency,
            "debit_amount": debit_amount,
            "credit_amount": credit_amount,
            "base_amount": base_amount,
            "exchange_rate": exchange_rate,
            "account_number1": account_number1,
            "account_number2": account_number2,
            "priority": priority,
            "purpose": purpose,
            "sub_purpose": sub_purpose,
            "country": country,
            "more_description": more_description,
            "receiver_license": receiver_license,
            "receiver_name": receiver_name,
            "receiver_address": receiver_address,
            "receiver_phone": receiver_phone,
            "receiver_type": receiver_type,
            "sender_license": sender_license,
            "sender_name": sender_name,
            "sender_address": sender_address,
            "sender_phone": sender_phone,
            "sender_type": sender_type,
            "send_bank": send_bank,
            "send_bank_branch": send_bank_branch,
            "beneficary_bank": beneficary_bank,
            "beneficary_bank_branch": beneficary_bank_branch,
            "is_inform_bank": is_inform_bank,
            "collecting_bank": collecting_bank,
            "group_pmt_inst": group_pmt_inst,
            "good_type": good_type,
            "good_list": good_list,
            "message_direction": message_direction,
            "message_description": message_description,
            "value_paper_status": value_paper_status,
            "message_status_history": message_status_history,
            "paid_amount": paid_amount,
            "fee_amount": fee_amount,
            "fee_paid": fee_paid,
            "pmt_order_type": pmt_order_type,
            "pmt_order_status": pmt_order_status
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