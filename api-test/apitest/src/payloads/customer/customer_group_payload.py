from datetime import datetime

class CustomerGroupPayload(object):
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

    def advanced_search(self, group_code=None, group_name=None, page_index=None, page_size=None):
        if not group_code:
            group_code = ''
        if not group_name:
            group_name = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "group_code": group_code,
            "group_name": group_name,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def update(self, id=None, list_members=None):
        if not id:
            id = 0
        if not list_members:
            list_members = None
        payload = {
            "id": id,
            "list_members": list_members
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload