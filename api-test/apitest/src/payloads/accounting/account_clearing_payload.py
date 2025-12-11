from datetime import datetime

class AccountClearingPayload(object):
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

    def advanced_search(self, branch_name=None, currency_id=None, clearing_branch_name=None, clearing_type=None, account_number=None, page_size=None, page_index=None):
        if not branch_name:
            branch_name = ''
        if not currency_id:
            currency_id = ''
        if not clearing_branch_name:
            clearing_branch_name = ''
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
            "currency_id": currency_id,
            "clearing_branch_name": clearing_branch_name,
            "clearing_type": clearing_type,
            "account_number": account_number,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def add(self, branch_code=None, currency_id=None, clearing_branch_code=None, clearing_type=None, account_number=None):
        if not branch_code:
            branch_code = ''
        if not currency_id:
            currency_id = ''
        if not clearing_branch_code:
            clearing_branch_code = ''
        if not clearing_type:
            clearing_type = ''
        if not account_number:
            account_number = ''
        payload = {
            "branch_code": branch_code,
            "currency_id": currency_id,
            "clearing_branch_code": clearing_branch_code,
            "clearing_type": clearing_type,
            "account_number": account_number
        }
        return payload

    def update(self, id=None, branch_code=None, currency_id=None, clearing_branch_code=None, clearing_type=None, account_number=None):
        if not id:
            id = 0
        if not branch_code:
            branch_code = ''
        if not currency_id:
            currency_id = ''
        if not clearing_branch_code:
            clearing_branch_code = ''
        if not clearing_type:
            clearing_type = ''
        if not account_number:
            account_number = ''
        payload = {
            "id": id,
            "branch_code": branch_code,
            "currency_id": currency_id,
            "clearing_branch_code": clearing_branch_code,
            "clearing_type": clearing_type,
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