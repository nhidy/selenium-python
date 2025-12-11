from datetime import datetime

class StockStatusPayload(object):
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

    def add(self, id=None, txcode=None, rules=None, stktype=None):
        if not id:
            id = 0
        if not txcode:
            txcode = ''
        if not rules:
            rules = ''
        if not stktype:
            stktype = ''
        payload = {
            "id": id,
            "txcode": txcode,
            "rules": rules,
            "stktype": stktype
        }
        return payload

    def update(self, id=None, txcode=None, rules=None, stktype=None):
        if not id:
            id = 0
        if not txcode:
            txcode = ''
        if not rules:
            rules = ''
        if not stktype:
            stktype = ''
        payload = {
            "id": id,
            "txcode": txcode,
            "rules": rules,
            "stktype": stktype
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload