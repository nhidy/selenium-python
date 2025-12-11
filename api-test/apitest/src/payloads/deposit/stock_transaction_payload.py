from datetime import datetime

class StockTransactionPayload(object):
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

    def add(self, id=None, defacno=None, txdt=None, txrefid=None, amt=None, stkfr=None, stkto=None, leafno=None, mtxcode=None, transts=None):
        if not id:
            id = 0
        if not defacno:
            defacno = ''
        if not txdt:
            txdt = ''
        if not txrefid:
            txrefid = ''
        if not amt:
            amt = 0
        if not stkfr:
            stkfr = ''
        if not stkto:
            stkto = ''
        if not leafno:
            leafno = 0
        if not mtxcode:
            mtxcode = ''
        if not transts:
            transts = ''
        payload = {
            "id": id,
            "defacno": defacno,
            "txdt": txdt,
            "txrefid": txrefid,
            "amt": amt,
            "stkfr": stkfr,
            "stkto": stkto,
            "leafno": leafno,
            "mtxcode": mtxcode,
            "transts": transts
        }
        return payload

    def update(self, id=None, defacno=None, txdt=None, txrefid=None, amt=None, stkfr=None, stkto=None, leafno=None, mtxcode=None, transts=None):
        if not id:
            id = 0
        if not defacno:
            defacno = ''
        if not txdt:
            txdt = ''
        if not txrefid:
            txrefid = ''
        if not amt:
            amt = 0
        if not stkfr:
            stkfr = ''
        if not stkto:
            stkto = ''
        if not leafno:
            leafno = 0
        if not mtxcode:
            mtxcode = ''
        if not transts:
            transts = ''
        payload = {
            "id": id,
            "defacno": defacno,
            "txdt": txdt,
            "txrefid": txrefid,
            "amt": amt,
            "stkfr": stkfr,
            "stkto": stkto,
            "leafno": leafno,
            "mtxcode": mtxcode,
            "transts": transts
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload