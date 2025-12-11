from datetime import datetime

class ExtensionAccountPayload(object):
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

    def advanced_search(self, id=None, accounting_group_id=None, group_name=None, replace_by_code=None, account_name=None, desc=None, sector=None, resident_status=None, categories=None, account_resident_status=None, page_size=None, page_index=None):
        if not id:
            id = None
        if not accounting_group_id:
            accounting_group_id = None
        if not group_name:
            group_name = ''
        if not replace_by_code:
            replace_by_code = ''
        if not account_name:
            account_name = ''
        if not desc:
            desc = ''
        if not sector:
            sector = ''
        if not resident_status:
            resident_status = ''
        if not categories:
            categories = ''
        if not account_resident_status:
            account_resident_status = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "id": id,
            "accounting_group_id": accounting_group_id,
            "group_name": group_name,
            "replace_by_code": replace_by_code,
            "account_name": account_name,
            "desc": desc,
            "sector": sector,
            "resident_status": resident_status,
            "categories": categories,
            "account_resident_status": account_resident_status,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def add(self, accounting_group_id=None, replace_by_code=None, replace_by=None, account_name=None, sector=None, resident_status=None, categories=None, account_resident=None, subproduct=None):
        if not accounting_group_id:
            accounting_group_id = 0
        if not replace_by_code:
            replace_by_code = ''
        if not replace_by:
            replace_by = ''
        if not account_name:
            account_name = ''
        if not sector:
            sector = ''
        if not resident_status:
            resident_status = ''
        if not categories:
            categories = ''
        if not account_resident:
            account_resident = ''
        if not subproduct:
            subproduct = ''
        payload = {
            "accounting_group_id": accounting_group_id,
            "replace_by_code": replace_by_code,
            "replace_by": replace_by,
            "account_name": account_name,
            "condition": {
                "sector": sector,
                "resident_status": resident_status,
                "categories": categories,
                "account_resident": account_resident,
                "subproduct": subproduct
            }
        }
        return payload

    def update(self, id=None, accounting_group_id=None, replace_by_code=None, replace_by=None, account_name=None, sector=None, resident_status=None, categories=None, account_resident=None, subproduct=None):
        if not id:
            id = 0
        if not accounting_group_id:
            accounting_group_id = 0
        if not replace_by_code:
            replace_by_code = ''
        if not replace_by:
            replace_by = ''
        if not account_name:
            account_name = ''
        if not sector:
            sector = ''
        if not resident_status:
            resident_status = ''
        if not categories:
            categories = ''
        if not account_resident:
            account_resident = ''
        if not subproduct:
            subproduct = ''
        payload = {
            "id": id,
            "accounting_group_id": accounting_group_id,
            "replace_by_code": replace_by_code,
            "replace_by": replace_by,
            "account_name": account_name,
            "condition": {
                "sector": sector,
                "resident_status": resident_status,
                "categories": categories,
                "account_resident": account_resident,
                "subproduct": subproduct
            }
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload