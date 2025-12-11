from datetime import datetime

class IFCAutoFeePayload(object):
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

    def advanced_search(self, trans_code=None, transaction_name=None, ifc_code=None, ifc_name=None, page_index=None, page_size=None):
        if not trans_code:
            trans_code = ''
        if not transaction_name:
            transaction_name = ''
        if not ifc_code:
            ifc_code = None
        if not ifc_name:
            ifc_name = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "trans_code": trans_code,
            "transaction_name": transaction_name,
            "ifc_code": ifc_code,
            "ifc_name": ifc_name,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, trans_code=None, ifc_code=None, exchange=None, inuse=None):
        if not trans_code:
            trans_code = ''
        if not ifc_code:
            ifc_code = 0
        if not exchange:
            exchange = 0
        if not inuse:
            inuse = 0
        payload = {
            "trans_code": trans_code,
            "ifc_code": ifc_code,
            "exchange": exchange,
            "inuse": inuse
        }
        return payload

    def update(self, id=None, exchange=None, inuse=None):
        if not id:
            id = 0
        if not exchange:
            exchange = 0
        if not inuse:
            inuse = 0
        payload = {
            "id": id,
            "exchange": exchange,
            "inuse": inuse
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload