from datetime import datetime

class DenominationTransactionPayload(object):
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

    def add(self, currency_id=None, face_value=None, face_type=None, quantity=None, amount=None, trans_ref_id=None, trans_date=None, in_or_out=None, cashier_id=None):
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
        if not trans_ref_id:
            trans_ref_id = ''
        if not trans_date:
            trans_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        if not in_or_out:
            in_or_out = ''
        if not cashier_id:
            cashier_id = 0
        payload = {
            "currency_id": currency_id,
            "face_value": face_value,
            "face_type": face_type,
            "quantity": quantity,
            "amount": amount,
            "trans_ref_id": trans_ref_id,
            "trans_date": trans_date,
            "in_or_out": in_or_out,
            "cashier_id": cashier_id,
        }
        return payload

    def update(self, id=None, currency_id=None, face_value=None, face_type=None, quantity=None, amount=None, trans_ref_id=None, trans_date=None, in_or_out=None, cashier_id=None):
        if not id:
            id = 0
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
        if not trans_ref_id:
            trans_ref_id = ''
        if not trans_date:
            trans_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        if not in_or_out:
            in_or_out = ''
        if not cashier_id:
            cashier_id = 0
        payload = {
            "id": id,
            "currency_id": currency_id,
            "face_value": face_value,
            "face_type": face_type,
            "quantity": quantity,
            "amount": amount,
            "trans_ref_id": trans_ref_id,
            "trans_date": trans_date,
            "in_or_out": in_or_out,
            "cashier_id": cashier_id
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload