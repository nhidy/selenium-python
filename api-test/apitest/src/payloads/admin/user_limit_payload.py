from datetime import datetime

class UserLimitPayload(object):
    def add(self, roleid=None, cmdid=None, ccrid=None, ulimit=None, cvtable=None, limittype=None, margin=None):
        if not roleid:
            roleid = 0
        if not cmdid:
            cmdid = ''
        if not ccrid:
            ccrid = ''
        if not ulimit:
            ulimit = 0
        if not cvtable:
            cvtable = ''
        if not limittype:
            limittype = ''
        if not margin:
            margin = 0
        payload = {
            "roleid": roleid,
            "cmdid": cmdid,
            "ccrid": ccrid,
            "ulimit": ulimit,
            "cvtable": cvtable,
            "limittype": limittype,
            "margin": margin
        }
        return payload

    def update(self, id=None, roleid=None, cmdid=None, ccrid=None, ulimit=None, cvtable=None, limittype=None, margin=None):
        if not id:
            id = 0
        if not roleid:
            roleid = 0
        if not cmdid:
            cmdid = ''
        if not ccrid:
            ccrid = ''
        if not ulimit:
            ulimit = 0
        if not cvtable:
            cvtable = ''
        if not limittype:
            limittype = ''
        if not margin:
            margin = 0
        payload = {
            "id": id,
            "roleid": roleid,
            "cmdid": cmdid,
            "ccrid": ccrid,
            "ulimit": ulimit,
            "cvtable": cvtable,
            "limittype": limittype,
            "margin": margin
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