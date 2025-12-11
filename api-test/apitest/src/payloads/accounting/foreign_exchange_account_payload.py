from datetime import datetime

class ForeignExchangeAccountPayload(object):
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

    def advanced_search(self, branch_name=None, account_currency=None, clearing_currency=None, clearing_type=None, account_number=None, page_size=None, page_index=None):
        if not branch_name:
            branch_name = ''
        if not account_currency:
            account_currency = ''
        if not clearing_currency:
            clearing_currency = ''
        if not clearing_type:
            clearing_type = ''
        if not account_number:
            account_number = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "branch_name": branch_name,
            "account_currency": account_currency,
            "clearing_currency": clearing_currency,
            "clearing_type": clearing_type,
            "account_number": account_number,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def add(self, branch_code=None, account_currency=None, clearing_currency=None, clearing_type=None, account_number=None):
        if not branch_code:
            branch_code = ''
        if not account_currency:
            account_currency = ''
        if not clearing_currency:
            clearing_currency = ''
        if not clearing_type:
            clearing_type = ''
        if not account_number:
            account_number = ''
        payload = {
            "branch_code": branch_code,
            "account_currency": account_currency,
            "clearing_currency": clearing_currency,
            "clearing_type": clearing_type,
            "account_number": account_number
        }
        return payload

    def update(self, id=None, account_number=None):
        if not id:
            id = 0
        if not account_number:
            account_number = ''
        payload = {
            "id": id,
            "account_number": account_number
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload