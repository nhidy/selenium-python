from datetime import datetime

class MortgageBalancePayload(object):
    def add(self, def_account_number=None, mortgage_reference=None, module_code=None, amount=None, clear_amount=None, set_date=None, clear_date=None, module_amount=None, module_clear_amount=None):
        if not def_account_number:
            def_account_number = ''
        if not mortgage_reference:
            mortgage_reference = ''
        if not module_code:
            module_code = ''
        if not amount:
            amount = 0
        if not clear_amount:
            clear_amount = 0
        if not set_date:
            set_date = ''
        if not clear_date:
            clear_date = ''
        if not module_amount:
            module_amount = 0
        if not module_clear_amount:
            module_clear_amount = 0
        payload = {
            "def_account_number": def_account_number,
            "mortgage_reference": mortgage_reference,
            "module_code": module_code,
            "amount": amount,
            "clear_amount": clear_amount,
            "set_date": set_date,
            "clear_date": clear_date,
            "module_amount": module_amount,
            "module_clear_amount": module_clear_amount
        }
        return payload

    def update(self, id=None, def_account_number=None, mortgage_reference=None, module_code=None, amount=None, clear_amount=None, set_date=None, clear_date=None, module_amount=None, module_clear_amount=None):
        if not id:
            id = 0
        if not def_account_number:
            def_account_number = ''
        if not mortgage_reference:
            mortgage_reference = ''
        if not module_code:
            module_code = ''
        if not amount:
            amount = 0
        if not clear_amount:
            clear_amount = 0
        if not set_date:
            set_date = ''
        if not clear_date:
            clear_date = ''
        if not module_amount:
            module_amount = 0
        if not module_clear_amount:
            module_clear_amount = 0
        payload = {
            "id": id,
            "def_account_number": def_account_number,
            "mortgage_reference": mortgage_reference,
            "module_code": module_code,
            "amount": amount,
            "clear_amount": clear_amount,
            "set_date": set_date,
            "clear_date": clear_date,
            "module_amount": module_amount,
            "module_clear_amount": module_clear_amount
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def advanced_search(self, page_index=None, page_size=None):
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
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