from datetime import datetime

class RoleOfUserPayload(object):
    def add(self, roleid=None, usrid=None):
        if not roleid:
            roleid = 0
        if not usrid:
            usrid = 0
        payload = {
            "roleid": roleid,
            "usrid": usrid
        }
        return payload

    def update(self, id=None, roleid=None, usrid=None):
        if not id:
            id = 0
        if not roleid:
            roleid = 0
        if not usrid:
            usrid = 0
        payload = {
            "id": id,
            "roleid": roleid,
            "usrid": usrid
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def advanced_search(self, id=None, roleid=None, usrid=None, page_index=None, page_size=None):
        if not id:
            id = ''
        if not roleid:
            roleid = None
        if not usrid:
            usrid = None
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "id": id,
            "roleid": roleid,
            "usrid": usrid,
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
