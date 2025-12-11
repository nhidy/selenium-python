from datetime import datetime

class IFCBalancePayload(object):
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

    def add(self, id=None, mdlcode=None, defacno=None, ifccd=None, valbase=None, ifcval=None, marval=None, amt=None, paid=None, lamt=None, ifc_status=None, lastdt=None, amtpbl=None, wdays=None, odays=None, nextdt=None):
        if not id:
            id = 0
        if not mdlcode:
            mdlcode = ''
        if not defacno:
            defacno = ''
        if not ifccd:
            ifccd = 0
        if not valbase:
            valbase = ''
        if not ifcval:
            ifcval = 0
        if not marval:
            marval = 0
        if not amt:
            amt = 0
        if not paid:
            paid = 0
        if not lamt:
            lamt = 0
        if not ifc_status:
            ifc_status = ''
        if not lastdt:
            lastdt = ''
        if not amtpbl:
            amtpbl = 0
        if not wdays:
            wdays = 0
        if not odays:
            odays = 0
        if not nextdt:
            nextdt = ''
        payload = {
            "id": id,
            "mdlcode": mdlcode,
            "defacno": defacno,
            "ifccd": ifccd,
            "valbase": valbase,
            "ifcval": ifcval,
            "marval": marval,
            "amt": amt,
            "paid": paid,
            "lamt": lamt,
            "ifc_status": ifc_status,
            "lastdt": lastdt,
            "amtpbl": amtpbl,
            "wdays": wdays,
            "odays": odays,
            "nextdt": nextdt
        }
        return payload

    def update(self, id=None, mdlcode=None, defacno=None, ifccd=None, valbase=None, ifcval=None, marval=None, amt=None, paid=None, lamt=None, ifc_status=None, lastdt=None, amtpbl=None, wdays=None, odays=None, nextdt=None, acction=None, balance=None, frdt=None, todt=None):
        if not id:
            id = 0
        if not mdlcode:
            mdlcode = ''
        if not defacno:
            defacno = ''
        if not ifccd:
            ifccd = 0
        if not valbase:
            valbase = ''
        if not ifcval:
            ifcval = 0
        if not marval:
            marval = 0
        if not amt:
            amt = 0
        if not paid:
            paid = 0
        if not lamt:
            lamt = 0
        if not ifc_status:
            ifc_status = ''
        if not lastdt:
            lastdt = ''
        if not amtpbl:
            amtpbl = 0
        if not wdays:
            wdays = 0
        if not odays:
            odays = 0
        if not nextdt:
            nextdt = ''
        if not acction:
            acction = ''
        if not balance:
            balance = 0
        if not frdt:
            frdt = ''
        if not todt:
            todt = ''
        payload = {
            "id": id,
            "mdlcode": mdlcode,
            "defacno": defacno,
            "ifccd": ifccd,
            "valbase": valbase,
            "ifcval": ifcval,
            "marval": marval,
            "amt": amt,
            "paid": paid,
            "lamt": lamt,
            "ifc_status": ifc_status,
            "lastdt": lastdt,
            "amtpbl": amtpbl,
            "wdays": wdays,
            "odays": odays,
            "nextdt": nextdt,
            "acction": acction,
            "balance": balance,
            "frdt": frdt,
            "todt": todt
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload