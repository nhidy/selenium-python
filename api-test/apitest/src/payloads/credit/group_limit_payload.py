from datetime import datetime

class GroupLimitPayload(object):
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

    def advanced_search(self, group_limit_code=None, group_limit_name=None, currency_code=None, credit_limit=None, page_index=None, page_size=None):
        if not group_limit_code:
            group_limit_code = ''
        if not group_limit_name:
            group_limit_name = ''
        if not currency_code:
            currency_code = ''
        if not credit_limit:
            credit_limit = None
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "group_limit_code": group_limit_code,
            "group_limit_name": group_limit_name,
            "currency_code": currency_code,
            "credit_limit": credit_limit,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, group_limit_name=None, currency_code=None, credit_limit=None):
        if not group_limit_name:
            group_limit_name = ''
        if not currency_code:
            currency_code = ''
        if not credit_limit:
            credit_limit = 0
        payload = {
            "group_limit_name": group_limit_name,
            "currency_code": currency_code,
            "credit_limit": credit_limit
        }
        return payload

    def update(self, id=None, group_limit_code=None, group_limit_name=None, currency_code=None, credit_limit=None):
        if not id:
            id = 0
        if not group_limit_code:
            group_limit_code = ''
        if not group_limit_name:
            group_limit_name = ''
        if not currency_code:
            currency_code = ''
        if not credit_limit:
            credit_limit = 0
        payload = {
            "id": id,
            "group_limit_code": group_limit_code,
            "group_limit_name": group_limit_name,
            "currency_code": currency_code,
            "credit_limit": credit_limit
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def get_list_customer_use_group_limit(self, group_limit_code=None, page_size=None, page_index=None):
        if not group_limit_code:
            group_limit_code = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "group_limit_code": group_limit_code,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload