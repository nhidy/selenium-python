from datetime import datetime

class AccountGroupPayload(object):
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

    def advanced_search(self, group_id=None, module=None, account_group_def=None, page_size=None, page_index=None):
        if not group_id:
            group_id = None
        if not module:
            module = ''
        if not account_group_def:
            account_group_def = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "group_id": group_id,
            "module": module,
            "account_group_def": account_group_def,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def add(self, group_id=None, module=None, account_group_def=None):
        if not group_id:
            group_id = 0
        if not module:
            module = ''
        if not account_group_def:
            account_group_def = ''
        payload = {
            "group_id": group_id,
            "module": module,
            "account_group_def": account_group_def
        }
        return payload

    def update(self, id=None, module=None, account_group_def=None):
        if not id:
            id = 0
        if not module:
            module = ''
        if not account_group_def:
            account_group_def = ''
        payload = {
            "id": id,
            "module": module,
            "account_group_def": account_group_def
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload