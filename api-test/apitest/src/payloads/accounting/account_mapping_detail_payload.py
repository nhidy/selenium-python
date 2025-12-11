from datetime import datetime

class AccountMappingDetailPayload(object):
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

    def add(self, mapping_id=None, sys_account_number=None, bank_account_number=None):
        if not mapping_id:
            mapping_id = ''
        if not sys_account_number:
            sys_account_number = ''
        if not bank_account_number:
            bank_account_number = ''
        payload = {
            "mapping_id": mapping_id,
            "sys_account_number": sys_account_number,
            "bank_account_number": bank_account_number
        }
        return payload

    def update(self, id=None, mapping_id=None, sys_account_number=None, bank_account_number=None):
        if not id:
            id = 0
        if not mapping_id:
            mapping_id = ''
        if not sys_account_number:
            sys_account_number = ''
        if not bank_account_number:
            bank_account_number = ''
        payload = {
            "id": id,
            "mapping_id": mapping_id,
            "sys_account_number": sys_account_number,
            "bank_account_number": bank_account_number
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload