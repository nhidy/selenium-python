from datetime import datetime

class CashTransactionPayload(object):
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

    def advanced_search(self, cashier_id=None, currency_code=None, page_index=None, page_size=None):
        if not cashier_id:
            cashier_id = None
        if not currency_code:
            currency_code = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "cashier_id": cashier_id,
            "currency_code": currency_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, cashier_id=None, currency_code=None, cash_amount=None, cash_type=None, trans_ref_id=None, trans_date=None, trans_status=None):
        if not cashier_id:
            cashier_id = 0
        if not currency_code:
            currency_code = ''
        if not cash_amount:
            cash_amount = 0
        if not cash_type:
            cash_type = ''
        if not trans_ref_id:
            trans_ref_id = ''
        if not trans_date:
            trans_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        if not trans_status:
            trans_status = ''
        payload = {
            "cashier_id": cashier_id,
            "currency_code": currency_code,
            "cash_amount": cash_amount,
            "cash_type": cash_type,
            "trans_ref_id": trans_ref_id,
            "trans_date": trans_date,
            "trans_status": trans_status
        }
        return payload

    def update(self, id=None, cashier_id=None, currency_code=None, cash_amount=None, cash_type=None, trans_ref_id=None, trans_date=None, trans_status=None):
        if not id:
            id = 0
        if not cashier_id:
            cashier_id = 0
        if not currency_code:
            currency_code = ''
        if not cash_amount:
            cash_amount = 0
        if not cash_type:
            cash_type = ''
        if not trans_ref_id:
            trans_ref_id = ''
        if not trans_date:
            trans_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        if not trans_status:
            trans_status = ''
        payload = {
            "id": id,
            "cashier_id": cashier_id,
            "currency_code": currency_code,
            "cash_amount": cash_amount,
            "cash_type": cash_type,
            "trans_ref_id": trans_ref_id,
            "trans_date": trans_date,
            "trans_status": trans_status
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload