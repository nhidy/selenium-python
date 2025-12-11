from datetime import datetime

class PaymentCatalogPayload(object):
    def add(self, catalog_code=None, catalog_name=None, output_format=None, direction=None, instrument=None, purpose=None, holding_days=None, catalog_status=None, payment_classification=None, approve_user_account=None, message_type=None, export_file=None, send_mail=None, group_pmt_ins_code=None, tariff_code=None, accounting_group_id=None, message_status=None):
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not output_format:
            output_format = ''
        if not direction:
            direction = ''
        if not instrument:
            instrument = ''
        if not purpose:
            purpose = ''
        if not holding_days:
            holding_days = 0
        if not catalog_status:
            catalog_status = ''
        if not payment_classification:
            payment_classification = ''
        if not approve_user_account:
            approve_user_account = 0
        if not message_type:
            message_type = ''
        if not export_file:
            export_file = ''
        if not send_mail:
            send_mail = ''
        if not group_pmt_ins_code:
            group_pmt_ins_code = ''
        if not tariff_code:
            tariff_code = 0
        if not accounting_group_id:
            accounting_group_id = 0
        if not message_status:
            message_status = ''
        payload = {
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "output_format": output_format,
            "direction": direction,
            "instrument": instrument,
            "purpose": purpose,
            "holding_days": holding_days,
            "catalog_status": catalog_status,
            "payment_classification": payment_classification,
            "approve_user_account": approve_user_account,
            "message_type": message_type,
            "export_file": export_file,
            "send_mail": send_mail,
            "group_pmt_ins_code": group_pmt_ins_code,
            "tariff_code": tariff_code,
            "accounting_group_id": accounting_group_id,
            "message_status": message_status
        }
        return payload

    def update(self, id=None, catalog_name=None, output_format=None, direction=None, instrument=None, purpose=None, holding_days=None, catalog_status=None, message_type=None, export_file=None, send_mail=None, group_pmt_ins_code=None, tariff_code=None, accounting_group_id=None, payment_classification=None):
        if not id:
            id = 0
        if not catalog_name:
            catalog_name = ''
        if not output_format:
            output_format = ''
        if not direction:
            direction = ''
        if not instrument:
            instrument = ''
        if not purpose:
            purpose = ''
        if not holding_days:
            holding_days = 0
        if not catalog_status:
            catalog_status = ''
        if not message_type:
            message_type = ''
        if not export_file:
            export_file = ''
        if not send_mail:
            send_mail = ''
        if not group_pmt_ins_code:
            group_pmt_ins_code = ''
        if not tariff_code:
            tariff_code = 0
        if not accounting_group_id:
            accounting_group_id = 0
        if not payment_classification:
            payment_classification = ''
        payload = {
            "id": id,
            "catalog_name": catalog_name,
            "output_format": output_format,
            "direction": direction,
            "instrument": instrument,
            "purpose": purpose,
            "holding_days": holding_days,
            "catalog_status": catalog_status,
            "message_type": message_type,
            "export_file": export_file,
            "payment_classification": payment_classification,
            "send_mail": send_mail,
            "group_pmt_ins_code": group_pmt_ins_code,
            "tariff_code": tariff_code,
            "accounting_group_id": accounting_group_id
        }
        return payload

    def advanced_search(self, catalog_code=None, catalog_name=None, output_format=None, direction=None, instrument=None, catalog_status=None, export_file=None, send_mail=None, message_type=None, page_index=None, page_size=None):
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not output_format:
            output_format = ''
        if not direction:
            direction = ''
        if not instrument:
            instrument = ''
        if not catalog_status:
            catalog_status = ''
        if not export_file:
            export_file = ''
        if not send_mail:
            send_mail = ''
        if not message_type:
            message_type = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "output_format": output_format,
            "direction": direction,
            "instrument": instrument,
            "catalog_status": catalog_status,
            "export_file": export_file,
            "send_mail": send_mail,
            "message_type": message_type,
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

    def view(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload