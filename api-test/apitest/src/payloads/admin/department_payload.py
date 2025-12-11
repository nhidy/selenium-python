from datetime import datetime

class DepartmentPayload(object):
    def add(self, branch_id=None, department_name=None):
        if not branch_id:
            branch_id = 0
        if not department_name:
            department_name = ''
        payload = {
            "branch_id": branch_id,
            "department_name": department_name
        }
        return payload

    def update(self, id=None, department_code=None, branch_id=None, department_name=None):
        if not id:
            id = 0
        if not department_code:
            department_code = ''
        if not branch_id:
            branch_id = 0
        if not department_name:
            department_name = ''
        payload = {
            "id": id,
            "department_code": department_code,
            "branch_id": branch_id,
            "department_name": department_name
        }
        return payload

    def view(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def advanced_search(self, department_code=None, department_name=None, branch_name=None, page_index=None, page_size=None):
        if not department_code:
            department_code = ''
        if not department_name:
            department_name = ''
        if not branch_name:
            branch_name = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "department_code": department_code,
            "department_name": department_name,
            "branch_name": branch_name,
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

    def get_list_user(self, department_id=None, page_size=None, page_index=None):
        if not department_id:
            department_id = None
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "department_id": department_id,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload