from datetime import datetime

class DenominationStatementPayload(object):
    def view(self, id=None, transaction_code=None):
        if not id:
            id = 0
        payload = {
            "id": id,
            "transaction_code": transaction_code
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

    def advanced_search(self, trans_ref_id=None, cashier_id=None, page_index=None, page_size=None):
        if not trans_ref_id:
            trans_ref_id = ''
        if not cashier_id:
            cashier_id = None
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "trans_ref_id": trans_ref_id,
            "cashier_id": cashier_id,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, trans_ref_id=None, value_date=None, currency_id=None, face_value=None, face_type=None, quantity=None, amount=None, in_or_out=None, cashier_id=None, statement_status=None):
        if not trans_ref_id:
            trans_ref_id = ''
        if not value_date:
            value_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        if not currency_id:
            currency_id = ''
        if not face_value:
            face_value = 0
        if not face_type:
            face_type = ''
        if not quantity:
            quantity = 0
        if not amount:
            amount = 0
        if not in_or_out:
            in_or_out = ''
        if not cashier_id:
            cashier_id = 0
        if not statement_status:
            statement_status = ''
        payload = {
            "trans_ref_id": trans_ref_id,
            "value_date": value_date,
            "currency_id": currency_id,
            "face_value": face_value,
            "face_type": face_type,
            "quantity": quantity,
            "amount": amount,
            "in_or_out": in_or_out,
            "cashier_id": cashier_id,
            "statement_status": statement_status
        }
        return payload

    def update(self, id=None, trans_ref_id=None, value_date=None, currency_id=None, face_value=None, face_type=None, quantity=None, amount=None, in_or_out=None, cashier_id=None, statement_status=None):
        if not id:
           id = 0
        if not trans_ref_id:
            trans_ref_id = ''
        if not value_date:
            value_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        if not currency_id:
            currency_id = ''
        if not face_value:
            face_value = 0
        if not face_type:
            face_type = ''
        if not quantity:
            quantity = 0
        if not amount:
            amount = 0
        if not in_or_out:
            in_or_out = ''
        if not cashier_id:
            cashier_id = 0
        if not statement_status:
            statement_status = ''
        payload = {
            "id": id,
            "trans_ref_id": trans_ref_id,
            "value_date": value_date,
            "currency_id": currency_id,
            "face_value": face_value,
            "face_type": face_type,
            "quantity": quantity,
            "amount": amount,
            "in_or_out": in_or_out,
            "cashier_id": cashier_id,
            "statement_status": statement_status
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload