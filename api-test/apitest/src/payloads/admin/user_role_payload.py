from datetime import datetime

class UserRolePayload(object):
    def add(self, rolename=None, userrolestatus=None, roletemplatedid=None):
        if not rolename:
            rolename = ''
        if not userrolestatus:
            userrolestatus = ''
        if not roletemplatedid:
            roletemplatedid = 0
        payload = {
            "rolename": rolename,
            "userrolestatus": userrolestatus,
            "roletemplatedid": roletemplatedid
        }
        return payload

    def update(self, id=None, rolename=None, userrolestatus=None):
        if not id:
            id = 0
        if not rolename:
            rolename = ''
        if not userrolestatus:
            userrolestatus = ''
        payload = {
            "id": id,
            "rolename": rolename,
            "userrolestatus": userrolestatus
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

    def advanced_search(self, page_index=None, page_size=None):
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
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