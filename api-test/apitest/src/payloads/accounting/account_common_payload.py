from datetime import datetime

class AccountCommonPayload(object):
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

    def advanced_search(self, account_number=None, account_name=None, ref_account_number=None, ref_account_number2=None, page_size=None, page_index=None):
        if not account_number:
            account_number = ''
        if not account_name:
            account_name = ''
        if not ref_account_number:
            ref_account_number = ''
        if not ref_account_number2:
            ref_account_number2 = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "account_number": account_number,
            "account_name": account_name,
            "ref_account_number": ref_account_number,
            "ref_account_number2": ref_account_number2,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def add(self, account_number=None, account_name=None, ref_account_number=None, ref_account_number2=None):
        if not account_number:
            account_number = ''
        if not account_name:
            account_name = ''
        if not ref_account_number:
            ref_account_number = ''
        if not ref_account_number2:
            ref_account_number2 = ''
        payload = {
            "account_number": account_number,
            "account_name": account_name,
            "ref_account_number": ref_account_number,
            "ref_account_number2": ref_account_number2
        }
        return payload

    def update(self, id=None, account_number=None, account_name=None, ref_account_number=None, ref_account_number2=None):
        if not id:
            id = 0
        if not account_number:
            account_number = ''
        if not account_name:
            account_name = ''
        if not ref_account_number:
            ref_account_number = ''
        if not ref_account_number2:
            ref_account_number2 = ''
        payload = {
            "id": id,
            "account_number": account_number,
            "account_name": account_name,
            "ref_account_number": ref_account_number,
            "ref_account_number2": ref_account_number2
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload