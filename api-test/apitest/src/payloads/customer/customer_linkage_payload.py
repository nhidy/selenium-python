from datetime import datetime

class CustomerLinkagePayload(object):
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

    def lookup_customer_linkage(self, linkage_code=None, master_customer_code=None, master_customer_name=None, linkage_description=None, linkage_credit_line_from=None, linkage_credit_line_to=None, group_limit_code=None, page_index=None, page_size=None):
        if not linkage_code:
            linkage_code = ''
        if not master_customer_code:
            master_customer_code = ''
        if not master_customer_name:
            master_customer_name = ''
        if not linkage_description:
            linkage_description = ''
        if not linkage_credit_line_from:
            linkage_credit_line_from = None
        if not linkage_credit_line_to:
            linkage_credit_line_to = None
        if not group_limit_code:
            group_limit_code = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "linkage_code": linkage_code,
            "master_customer_code": master_customer_code,
            "master_customer_name": master_customer_name,
            "linkage_description": linkage_description,
            "linkage_credit_line_from": linkage_credit_line_from,
            "linkage_credit_line_to": linkage_credit_line_to,
            "group_limit_code": group_limit_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def advanced_search(self, linkage_code=None, master_customer_code=None, master_customer_name=None, linkage_description=None, linkage_credit_line_from=None, linkage_credit_line_to=None, group_limit_code=None, page_index=None, page_size=None):
        if not linkage_code:
            linkage_code = ''
        if not master_customer_code:
            master_customer_code = ''
        if not master_customer_name:
            master_customer_name = ''
        if not linkage_description:
            linkage_description = ''
        if not linkage_credit_line_from:
            linkage_credit_line_from = None
        if not linkage_credit_line_to:
            linkage_credit_line_to = None
        if not group_limit_code:
            group_limit_code = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "linkage_code": linkage_code,
            "master_customer_code": master_customer_code,
            "master_customer_name": master_customer_name,
            "linkage_description": linkage_description,
            "linkage_credit_line_from": linkage_credit_line_from,
            "linkage_credit_line_to": linkage_credit_line_to,
            "group_limit_code": group_limit_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, master_customer_id=None, linkage_description=None, detail_customer_id=None, linkage_type=None, linkage_status=None, group_limit_code=None, linkage_credit_line=None, currency_code=None):
        if not master_customer_id:
            master_customer_id = 0
        if not linkage_description:
            linkage_description = ''
        if not detail_customer_id:
            detail_customer_id = 0
        if not linkage_type:
            linkage_type = ''
        if not linkage_status:
            linkage_status = ''
        if not group_limit_code:
            group_limit_code = ''
        if not linkage_credit_line:
            linkage_credit_line = 0
        if not currency_code:
            currency_code = ''
        payload = {
            "master_customer_id": master_customer_id,
            "linkage_description": linkage_description,
            "detail_customer_id": detail_customer_id,
            "linkage_type": linkage_type,
            "linkage_status": linkage_status,
            "group_limit_code": group_limit_code,
            "linkage_credit_line": linkage_credit_line,
            "currency_code": currency_code
        }
        return payload

    def update(self, id=None, linkage_description=None, detail_customer_id=None, linkage_type=None, linkage_status=None, group_limit_code=None, linkage_credit_line=None, currency_code=None):
        if not id:
            id = 0
        if not linkage_description:
            linkage_description = ''
        if not detail_customer_id:
            detail_customer_id = ''
        if not linkage_type:
            linkage_type = ''
        if not linkage_status:
            linkage_status = ''
        if not group_limit_code:
            group_limit_code = ''
        if not linkage_credit_line:
            linkage_credit_line = 0
        if not currency_code:
            currency_code = ''
        payload = {
            "id": id,
            "linkage_description": linkage_description,
            "detail_customer_id": detail_customer_id,
            "linkage_type": linkage_type,
            "linkage_status": linkage_status,
            "group_limit_code": group_limit_code,
            "linkage_credit_line": linkage_credit_line,
            "currency_code": currency_code
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload