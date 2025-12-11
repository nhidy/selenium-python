from datetime import datetime

class PaymentQueueForOutwardPayload(object):
    def add(self, message_code=None, transaction_date_pmt=None, transaction_ref_id=None, message_direction=None, payment_type=None, sender_name=None, receiver_name=None, amount=None, paid_amount=None, fee_amount=None, fee_paid=None, message_status=None, send_bank=None, receiver_bank=None, group_pmt_inst=None, print_status=None, user_create=None, approver=None, sending_branch=None, receiving_branch=None, payment_by=None, location=None, apr_status_pmt_center=None, process_status_pmt_center=None, approve_user_pmt_center=None, process_user_pmt_center=None, reject_user_pmt_center=None, approve_status_branch=None, process_status_branch=None, approve_user_branch=None, process_user_branch=None, reject_user_branch=None, api_status=None, api_error=None, api_last_update_status=None, api_expected_effective_date=None, detail_charges=None):
        if not message_code:
            message_code = ''
        if not transaction_date_pmt:
            transaction_date_pmt = ''
        if not transaction_ref_id:
            transaction_ref_id = ''
        if not message_direction:
            message_direction = ''
        if not payment_type:
            payment_type = ''
        if not sender_name:
            sender_name = ''
        if not receiver_name:
            receiver_name = ''
        if not amount:
            amount = 0
        if not paid_amount:
            paid_amount = 0
        if not fee_amount:
            fee_amount = 0
        if not fee_paid:
            fee_paid = 0
        if not message_status:
            message_status = ''
        if not send_bank:
            send_bank = ''
        if not receiver_bank:
            receiver_bank = ''
        if not group_pmt_inst:
            group_pmt_inst = ''
        if not print_status:
            print_status = ''
        if not user_create:
            user_create = ''
        if not approver:
            approver = ''
        if not sending_branch:
            sending_branch = ''
        if not receiving_branch:
            receiving_branch = ''
        if not payment_by:
            payment_by = ''
        if not location:
            location = ''
        if not apr_status_pmt_center:
            apr_status_pmt_center = ''
        if not process_status_pmt_center:
            process_status_pmt_center = ''
        if not approve_user_pmt_center:
            approve_user_pmt_center = 0
        if not process_user_pmt_center:
            process_user_pmt_center = 0
        if not reject_user_pmt_center:
            reject_user_pmt_center = 0
        if not approve_status_branch:
            approve_status_branch = ''
        if not process_status_branch:
            process_status_branch = ''
        if not approve_user_branch:
            approve_user_branch = 0
        if not process_user_branch:
            process_user_branch = 0
        if not reject_user_branch:
            reject_user_branch = 0
        if not api_status:
            api_status = ''
        if not api_error:
            api_error = ''
        if not api_last_update_status:
            api_last_update_status = ''
        if not api_expected_effective_date:
            api_expected_effective_date = ''
        if not detail_charges:
            detail_charges = ''
        payload = {
            "message_code": message_code,
            "transaction_date_pmt": transaction_date_pmt,
            "transaction_ref_id": transaction_ref_id,
            "message_direction": message_direction,
            "payment_type": payment_type,
            "sender_name": sender_name,
            "receiver_name": receiver_name,
            "amount": amount,
            "paid_amount": paid_amount,
            "fee_amount": fee_amount,
            "fee_paid": fee_paid,
            "message_status": message_status,
            "send_bank": send_bank,
            "receiver_bank": receiver_bank,
            "group_pmt_inst": group_pmt_inst,
            "print_status": print_status,
            "user_create": user_create,
            "approver": approver,
            "sending_branch": sending_branch,
            "receiving_branch": receiving_branch,
            "payment_by": payment_by,
            "location": location,
            "apr_status_pmt_center": apr_status_pmt_center,
            "process_status_pmt_center": process_status_pmt_center,
            "approve_user_pmt_center": approve_user_pmt_center,
            "process_user_pmt_center": process_user_pmt_center,
            "reject_user_pmt_center": reject_user_pmt_center,
            "approve_status_branch": approve_status_branch,
            "process_status_branch": process_status_branch,
            "approve_user_branch": approve_user_branch,
            "process_user_branch": process_user_branch,
            "reject_user_branch": reject_user_branch,
            "api_status": api_status,
            "api_error": api_error,
            "api_last_update_status": api_last_update_status,
            "api_expected_effective_date": api_expected_effective_date,
            "detail_charges": detail_charges
        }
        return payload

    def advanced_search(self, message_code=None, reference_number=None, transaction_ref_id=None, transaction_date_pmt=None, message_direction=None, payment_typect=None, payment_type=None, message_status=None, debit_currency=None, amount=None, receiver_bank=None, send_bank=None, receiving_branch=None, sending_branch=None, location=None, apr_status_pmt_center=None, ordering=None, process_status_pmt_center=None, approve_status_branch=None, process_status_branch=None, ordinstitution=None, api_status=None, page_index=None, page_size=None):
        if not message_code:
            message_code = ''
        if not reference_number:
            reference_number = ''
        if not transaction_ref_id:
            transaction_ref_id = ''
        if not transaction_date_pmt:
            transaction_date_pmt = ''
        if not message_direction:
            message_direction = ''
        if not payment_typect:
            payment_typect = ''
        if not payment_type:
            payment_type = ''
        if not message_status:
            message_status = ''
        if not debit_currency:
            debit_currency = ''
        if not amount:
            amount = None
        if not receiver_bank:
            receiver_bank = ''
        if not send_bank:
            send_bank = ''
        if not receiving_branch:
            receiving_branch = ''
        if not sending_branch:
            sending_branch = ''
        if not location:
            location = ''
        if not apr_status_pmt_center:
            apr_status_pmt_center = ''
        if not ordering:
            ordering = ''
        if not process_status_pmt_center:
            process_status_pmt_center = ''
        if not approve_status_branch:
            approve_status_branch = ''
        if not process_status_branch:
            process_status_branch = ''
        if not ordinstitution:
            ordinstitution = ''
        if not api_status:
            api_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "message_code": message_code,
            "reference_number": reference_number,
            "transaction_ref_id": transaction_ref_id,
            "transaction_date_pmt": transaction_date_pmt,
            "message_direction": message_direction,
            "payment_typect": payment_typect,
            "payment_type": payment_type,
            "message_status": message_status,
            "debit_currency": debit_currency,
            "amount": amount,
            "receiver_bank": receiver_bank,
            "send_bank": send_bank,
            "receiving_branch": receiving_branch,
            "sending_branch": sending_branch,
            "location": location,
            "apr_status_pmt_center": apr_status_pmt_center,
            "ordering": ordering,
            "process_status_pmt_center": process_status_pmt_center,
            "approve_status_branch": approve_status_branch,
            "process_status_branch": process_status_branch,
            "ordinstitution": ordinstitution,
            "api_status": api_status,
            "page_index": page_index,
            "page_size": page_size
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