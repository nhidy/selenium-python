from datetime import datetime

class MortgageTransactionPayload(object):
    def add(self, def_account_number=None, amount=None, dir_amount=None, transaction_date=None, reference_id=None, transaction_code=None):
        if not def_account_number: 
            def_account_number= ''
        if not amount: 
            amount= 0
        if not dir_amount: 
            dir_amount= 0
        if not transaction_date: 
            transaction_date= ''
        if not reference_id: 
            reference_id= ''
        if not transaction_code: 
            transaction_code= ''
        payload = {
            "def_account_number": def_account_number,
            "amount": amount,
            "dir_amount": dir_amount,
            "transaction_date": transaction_date,
            "reference_id": reference_id,
            "transaction_code": transaction_code
        }
        return payload

    def update(self, id=None, def_account_number=None, amount=None, dir_amount=None, transaction_date=None, reference_id=None, transaction_code=None):
        if not id:
            id = 0
        if not def_account_number: 
            def_account_number= ''
        if not amount: 
            amount= 0
        if not dir_amount: 
            dir_amount= 0
        if not transaction_date: 
            transaction_date= ''
        if not reference_id: 
            reference_id= ''
        if not transaction_code: 
            transaction_code= ''
        payload = {
            "id": id,
            "def_account_number": def_account_number,
            "amount": amount,
            "dir_amount": dir_amount,
            "transaction_date": transaction_date,
            "reference_id": reference_id,
            "transaction_code": transaction_code
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