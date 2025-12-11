from datetime import datetime

class IFCTransactionPayload(object):
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

    def advanced_search(self, ifccd=None, ifcname=None, paysrcct=None, valbas=None, refname=None, ifccond=None, valtypect=None, ifctypect=None, ifcval=None, payrate=None, txcode=None, paysrc=None, valtype=None, ifctype=None, page_index=None, page_size=None):
        if not ifccd:
            ifccd = None
        if not ifcname:
            ifcname = ''
        if not paysrcct:
            paysrcct = ''
        if not valbas:
            valbas = ''
        if not refname:
            refname = ''
        if not ifccond:
            ifccond = ''
        if not valtypect:
            valtypect = ''
        if not ifctypect:
            ifctypect = ''
        if not ifcval:
            ifcval = None
        if not payrate:
            payrate = None
        if not txcode:
            txcode = ''
        if not paysrc:
            paysrc = ''
        if not valtype:
            valtype = ''
        if not ifctype:
            ifctype = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "ifccd": ifccd,
            "ifcname": ifcname,
            "paysrcct": paysrcct,
            "valbas": valbas,
            "refname": refname,
            "ifccond": ifccond,
            "valtypect": valtypect,
            "ifctypect": ifctypect,
            "ifcval": ifcval,
            "payrate": payrate,
            "txcode": txcode,
            "paysrc": paysrc,
            "valtype": valtype,
            "ifctype": ifctype,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, id=None, ifccd=None, txcode=None, paysrc=None, valbas=None, refname=None, ifccond=None, ccrbas=None):
        if not id:
            id = 0
        if not ifccd:
            ifccd = 0
        if not txcode:
            txcode = ''
        if not paysrc:
            paysrc = ''
        if not valbas:
            valbas = ''
        if not refname:
            refname = ''
        if not ifccond:
            ifccond = ''
        if not ccrbas:
            ccrbas = ''

        payload = {
            "id": id,
            "ifccd": ifccd,
            "txcode": txcode,
            "paysrc": paysrc,
            "valbas": valbas,
            "refname": refname,
            "ifccond": ifccond,
            "ccrbas": ccrbas
        }
        return payload

    def update(self, id=None, ifccd=None, txcode=None, paysrc=None, valbas=None, refname=None, ifccond=None, ccrbas=None):
        if not id:
            id = 0
        if not ifccd:
            ifccd = 0
        if not txcode:
            txcode = ''
        if not paysrc:
            paysrc = ''
        if not valbas:
            valbas = ''
        if not refname:
            refname = ''
        if not ifccond:
            ifccond = ''
        if not ccrbas:
            ccrbas = ''

        payload = {
            "id": id,
            "ifccd": ifccd,
            "txcode": txcode,
            "paysrc": paysrc,
            "valbas": valbas,
            "refname": refname,
            "ifccond": ifccond,
            "ccrbas": ccrbas
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload