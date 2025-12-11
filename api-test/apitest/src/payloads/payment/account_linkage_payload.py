from datetime import datetime

class AccountLinkagePayload(object):
    def add(self, master_account_no=None, master_module_code=None, linked_account_no=None, linked_module_code=None, linkage_pmt_desc=None, linkage_type=None, linkage_classification=None):
        if not master_account_no:
            master_account_no = ''
        if not master_module_code:
            master_module_code = ''
        if not linked_account_no:
            linked_account_no = ''
        if not linked_module_code:
            linked_module_code = ''
        if not linkage_pmt_desc:
            linkage_pmt_desc = ''
        if not linkage_type:
            linkage_type = ''
        if not linkage_classification:
            linkage_classification = ''
        payload = {
            "master_account_no": master_account_no,
            "master_module_code": master_module_code,
            "linked_account_no": linked_account_no,
            "linked_module_code": linked_module_code,
            "linkage_pmt_desc": linkage_pmt_desc,
            "linkage_type": linkage_type,
            "linkage_classification": linkage_classification
        }
        return payload

    def update(self, id=None, linked_account_no=None, linked_account_name=None, linked_module_code=None, linkage_pmt_desc=None, linkage_type=None, linkage_classification=None):
        if not id:
            id = 0
        if not linked_account_no:
            linked_account_no = ''
        if not linked_account_name:
            linked_account_name = ''
        if not linked_module_code:
            linked_module_code = ''
        if not linkage_pmt_desc:
            linkage_pmt_desc = ''
        if not linkage_type:
            linkage_type = ''
        if not linkage_classification:
            linkage_classification = ''
        payload = {
            "id": id,
            "linked_account_no": linked_account_no,
            "linked_account_name": linked_account_name,
            "linked_module_code": linked_module_code,
            "linkage_pmt_desc": linkage_pmt_desc,
            "linkage_type": linkage_type,
            "linkage_classification": linkage_classification
        }
        return payload

    def advanced_search(self, master_account_no=None, master_module_code=None, account_name=None, page_index=None, page_size=None):
        if not master_account_no:
            master_account_no = ''
        if not master_module_code:
            master_module_code = ''
        if not account_name:
            account_name = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "master_account_no": master_account_no,
            "master_module_code": master_module_code,
            "account_name": account_name,
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