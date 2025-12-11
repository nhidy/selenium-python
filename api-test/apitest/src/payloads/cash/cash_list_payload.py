from datetime import datetime

class CashListPayload(object):
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

    def add(self, cashier_id=None, currency_code=None, current_balance=None):
        if not cashier_id:
            cashier_id = 0
        if not currency_code:
            currency_code = ''
        if not current_balance:
            current_balance = 0
        payload = {
            "cashier_id": cashier_id,
            "currency_code": currency_code,
            "current_balance": current_balance
        }
        return payload

    def update(self, id=None, current_balance=None):
        if not id:
            id = 0
        if not current_balance:
            current_balance = 0
        payload = {
            "id": id,
            "current_balance": current_balance
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def get_cash_account(self, id=None):
        if not id:
            id = ''
        payload = {
            "id": id
        }
        return payload