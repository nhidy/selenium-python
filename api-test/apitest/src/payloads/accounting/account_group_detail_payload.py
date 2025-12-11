from datetime import datetime

class AccountGroupDetailPayload(object):
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

    def advanced_search(self, module=None, system_account_name=None, bank_define_account_name=None, page_size=None, page_index=None):
        if not module:
            module = ''
        if not system_account_name:
            system_account_name = ''
        if not bank_define_account_name:
            bank_define_account_name = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "module": module,
            "system_account_name": system_account_name,
            "bank_define_account_name": bank_define_account_name,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def add(self, module=None, system_account_name=None, bank_define_account_name=None):
        if not module:
            module = ''
        if not system_account_name:
            system_account_name = ''
        if not bank_define_account_name:
            bank_define_account_name = ''
        payload = {
            "module": module,
            "system_account_name": system_account_name,
            "bank_define_account_name": bank_define_account_name
        }
        return payload

    def update(self, id=None, bank_define_account_name=None):
        if not id:
            id = 0
        if not bank_define_account_name:
            bank_define_account_name = ''
        payload = {
            "id": id,
            "bank_define_account_name": bank_define_account_name
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload