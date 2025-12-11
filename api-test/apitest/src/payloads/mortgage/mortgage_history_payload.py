from datetime import datetime

class MortgageHistoryPayload(object):
    def add(self, mortgage_account_number=None, set_date=None, value_date=None, amount=None, dorc=None):
        if not mortgage_account_number: 
            mortgage_account_number = ''
        if not set_date: 
            set_date = ''
        if not value_date: 
            value_date = ''
        if not amount: 
            amount = 0
        if not dorc: 
            dorc= ''
        payload = {
            "mortgage_account_number": mortgage_account_number,
            "set_date": set_date,
            "value_date": value_date,
            "amount": amount,
            "dorc": dorc
        }
        return payload

    def update(self, id=None, def_account_number=None, set_date=None, value_date=None, amount=None, dorc=None):
        if not id:
            id = 0
        if not def_account_number: 
            def_account_number = ''
        if not set_date: 
            set_date = ''
        if not value_date: 
            value_date = ''
        if not amount: 
            amount = 0
        if not dorc: 
            dorc = ''
        payload = {
            "id": id,
            "def_account_number": def_account_number,
            "set_date": set_date,
            "value_date": value_date,
            "amount": amount,
            "dorc": dorc
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