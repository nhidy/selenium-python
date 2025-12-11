from datetime import datetime

class FundTransferViaFastPayload(object):
    def add(self, message_code=None, message_id=None, payment_infor_id=None, instruction_id=None, transaction_ref_id=None, transaction_date_pmt=None, system_status=None, cncat=None, message_direction=None, send_bank=None, send_bank_name=None, send_bank_street=None, sbbdmb=None, sbpcode=None, send_bank_town=None, receiver_bank=None, receiver_bank_name=None, receiver_bank_steet=None, rbbdmb=None, rbpcode=None, receiver_bank_town=None, sender_name=None, sender_street=None, sdbdmb=None, sdpcode=None, sender_town=None, sender_coutry=None, sender_currency=None, sender_account_no=None, receiver_name=None, receiver_street=None, rcbdmb=None, rcpcode=None, receiver_town=None, receiver_country=None, receiver_currency=None, receiver_account_no=None, pmtmtd=None, remitting_currency=None, send_amount=None, remitting_amount=None, receive_amount=None, chrgbr=None, fee_amount=None, f_payment_by=None, info_payment=None, purpose=None, nostro=None, message_status=None, fast_status=None, refund_code=None, refnb=None, reason_refund=None, reason_message_code=None, brid=None, exchange_rate=None, end_to_end_status=None, coregateway_status=None, detail_charges=None):
        if not message_code:
            message_code = ''
        if not message_id:
            message_id = ''
        if not payment_infor_id:
            payment_infor_id = ''
        if not instruction_id:
            instruction_id = ''
        if not transaction_ref_id:
            transaction_ref_id = ''
        if not transaction_date_pmt:
            transaction_date_pmt = ''
        if not system_status:
            system_status = ''
        if not cncat:
            cncat = ''
        if not message_direction:
            message_direction = ''
        if not send_bank:
            send_bank = ''
        if not send_bank_name:
            send_bank_name = ''
        if not send_bank_street:
            send_bank_street = ''
        if not sbbdmb:
            sbbdmb = ''
        if not sbpcode:
            sbpcode = ''
        if not send_bank_town:
            send_bank_town = ''
        if not receiver_bank:
            receiver_bank = ''
        if not receiver_bank_name:
            receiver_bank_name = ''
        if not receiver_bank_steet:
            receiver_bank_steet = ''
        if not rbbdmb:
            rbbdmb = ''
        if not rbpcode:
            rbpcode = ''
        if not receiver_bank_town:
            receiver_bank_town = ''
        if not sender_name:
            sender_name = ''
        if not sender_street:
            sender_street = ''
        if not sdbdmb:
            sdbdmb = ''
        if not sdpcode:
            sdpcode = ''
        if not sender_town:
            sender_town = ''
        if not sender_coutry:
            sender_coutry = ''
        if not sender_currency:
            sender_currency = ''
        if not sender_account_no:
            sender_account_no = ''
        if not receiver_name:
            receiver_name = ''
        if not receiver_street:
            receiver_street = ''
        if not rcbdmb:
            rcbdmb = ''
        if not rcpcode:
            rcpcode = ''
        if not receiver_town:
            receiver_town = ''
        if not receiver_country:
            receiver_country = ''
        if not receiver_currency:
            receiver_currency = ''
        if not receiver_account_no:
            receiver_account_no = ''
        if not pmtmtd:
            pmtmtd = ''
        if not remitting_currency:
            remitting_currency = ''
        if not send_amount:
            send_amount = 0
        if not remitting_amount:
            remitting_amount = 0
        if not receive_amount:
            receive_amount = 0
        if not chrgbr:
            chrgbr = ''
        if not fee_amount:
            fee_amount = 0
        if not f_payment_by:
            f_payment_by = ''
        if not info_payment:
            info_payment = ''
        if not purpose:
            purpose = ''
        if not nostro:
            nostro = ''
        if not message_status:
            message_status = ''
        if not fast_status:
            fast_status = ''
        if not refund_code:
            refund_code = ''
        if not refnb:
            refnb = ''
        if not reason_refund:
            reason_refund = ''
        if not reason_message_code:
            reason_message_code = ''
        if not brid:
            brid = 0
        if not exchange_rate:
            exchange_rate = 0
        if not end_to_end_status:
            end_to_end_status = ''
        if not coregateway_status:
            coregateway_status = ''
        if not detail_charges:
            detail_charges = ''
        payload = {
            "message_code": message_code,
            "message_id": message_id,
            "payment_infor_id": payment_infor_id,
            "instruction_id": instruction_id,
            "transaction_ref_id": transaction_ref_id,
            "transaction_date_pmt": transaction_date_pmt,
            "system_status": system_status,
            "cncat": cncat,
            "message_direction": message_direction,
            "send_bank": send_bank,
            "send_bank_name": send_bank_name,
            "send_bank_street": send_bank_street,
            "sbbdmb": sbbdmb,
            "sbpcode": sbpcode,
            "send_bank_town": send_bank_town,
            "receiver_bank": receiver_bank,
            "receiver_bank_name": receiver_bank_name,
            "receiver_bank_steet": receiver_bank_steet,
            "rbbdmb": rbbdmb,
            "rbpcode": rbpcode,
            "receiver_bank_town": receiver_bank_town,
            "sender_name": sender_name,
            "sender_street": sender_street,
            "sdbdmb": sdbdmb,
            "sdpcode": sdpcode,
            "sender_town": sender_town,
            "sender_coutry": sender_coutry,
            "sender_currency": sender_currency,
            "sender_account_no": sender_account_no,
            "receiver_name": receiver_name,
            "receiver_street": receiver_street,
            "rcbdmb": rcbdmb,
            "rcpcode": rcpcode,
            "receiver_town": receiver_town,
            "receiver_country": receiver_country,
            "receiver_currency": receiver_currency,
            "receiver_account_no": receiver_account_no,
            "pmtmtd": pmtmtd,
            "remitting_currency": remitting_currency,
            "send_amount": send_amount,
            "remitting_amount": remitting_amount,
            "receive_amount": receive_amount,
            "chrgbr": chrgbr,
            "fee_amount": fee_amount,
            "f_payment_by": f_payment_by,
            "info_payment": info_payment,
            "purpose": purpose,
            "nostro": nostro,
            "message_status": message_status,
            "fast_status": fast_status,
            "refund_code": refund_code,
            "refnb": refnb,
            "reason_refund": reason_refund,
            "reason_message_code": reason_message_code,
            "brid": brid,
            "exchange_rate": exchange_rate,
            "end_to_end_status": end_to_end_status,
            "coregateway_status": coregateway_status,
            "detail_charges": detail_charges
        }
        return payload

    def advanced_search(self, transaction_ref_id=None, message_code=None, transaction_date_pmt=None, payment_infor_id=None, message_direction=None, end_to_end_status=None, send_bank=None, receiver_bank=None, send_bank_name=None, receiver_bank_name=None, sender_name=None, receiver_name=None, receiver_account_no=None, remitting_amount=None, remitting_currency=None, message_status=None, reason_refund=None, purpose=None, fast_status=None, info_payment=None, reason_message_code=None, coregateway_status=None, page_index=None, page_size=None):
        if not transaction_ref_id:
            transaction_ref_id = ''
        if not message_code:
            message_code = ''
        if not transaction_date_pmt:
            transaction_date_pmt = ''
        if not payment_infor_id:
            payment_infor_id = ''
        if not message_direction:
            message_direction = ''
        if not end_to_end_status:
            end_to_end_status = ''
        if not send_bank:
            send_bank = ''
        if not receiver_bank:
            receiver_bank = ''
        if not send_bank_name:
            send_bank_name = ''
        if not receiver_bank_name:
            receiver_bank_name = ''
        if not sender_name:
            sender_name = ''
        if not receiver_name:
            receiver_name = ''
        if not receiver_account_no:
            receiver_account_no = ''
        if not remitting_amount:
            remitting_amount = None
        if not remitting_currency:
            remitting_currency = ''
        if not message_status:
            message_status = ''
        if not reason_refund:
            reason_refund = ''
        if not purpose:
            purpose = ''
        if not fast_status:
            fast_status = ''
        if not info_payment:
            info_payment = ''
        if not reason_message_code:
            reason_message_code = ''
        if not coregateway_status:
            coregateway_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "transaction_ref_id": transaction_ref_id,
            "message_code": message_code,
            "transaction_date_pmt": transaction_date_pmt,
            "payment_infor_id": payment_infor_id,
            "message_direction": message_direction,
            "end_to_end_status": end_to_end_status,
            "send_bank": send_bank,
            "receiver_bank": receiver_bank,
            "send_bank_name": send_bank_name,
            "receiver_bank_name": receiver_bank_name,
            "sender_name": sender_name,
            "receiver_name": receiver_name,
            "receiver_account_no": receiver_account_no,
            "remitting_amount": remitting_amount,
            "remitting_currency": remitting_currency,
            "message_status": message_status,
            "reason_refund": reason_refund,
            "purpose": purpose,
            "fast_status": fast_status,
            "info_payment": info_payment,
            "reason_message_code": reason_message_code,
            "coregateway_status": coregateway_status,
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