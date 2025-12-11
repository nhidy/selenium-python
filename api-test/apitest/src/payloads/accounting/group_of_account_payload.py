from datetime import datetime

class GroupOfAccountPayload(object):
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

    def advanced_search(self, group_id=None, account_group_def=None, account_number=None, account_name=None, desc=None, page_size=None, page_index=None):
        if not group_id:
            group_id = None
        if not account_group_def:
            account_group_def = ''
        if not account_number:
            account_number = ''
        if not account_name:
            account_name = ''
        if not desc:
            desc = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "group_id": group_id,
            "account_group_def": account_group_def,
            "account_number": account_number,
            "account_name": account_name,
            "desc": desc,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def add(self, group_id=None, account_number=None, account_name=None, ref_account_number=None, ref_account_number2=None):
        if not group_id:
            group_id = 0
        if not account_number:
            account_number = ''
        if not account_name:
            account_name = ''
        if not ref_account_number:
            ref_account_number = ''
        if not ref_account_number2:
            ref_account_number2 = ''
        payload = {
            "group_id": group_id,
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