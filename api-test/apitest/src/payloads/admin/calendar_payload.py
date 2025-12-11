from datetime import datetime

class CalendarPayload(object):
    def add(self, sqndt=None, isnow=None, isholiday=None, iseow=None, iseom=None, iseoq=None, iseoh=None, iseoy=None, isbow=None, isbom=None, isboq=None, isboh=None, isboy=None, isfeow=None, isfeom=None, isfeoq=None, isfeoh=None, isfeoy=None, isfbow=None, isfbom=None, isfboq=None, isfboh=None, isfboy=None, descs=None, ccrid=None):
        if not sqndt:
            sqndt = ''
        if not isnow:
            isnow = 0
        if not isholiday:
            isholiday = 0
        if not iseow:
            iseow = 0
        if not iseom:
            iseom = 0
        if not iseoq:
            iseoq = 0
        if not iseoh:
            iseoh = 0
        if not iseoy:
            iseoy = 0
        if not isbow:
            isbow = 0
        if not isbom:
            isbom = 0
        if not isboq:
            isboq = 0
        if not isboh:
            isboh = 0
        if not isboy:
            isboy = 0
        if not isfeow:
            isfeow = 0
        if not isfeom:
            isfeom = 0
        if not isfeoq:
            isfeoq = 0
        if not isfeoh:
            isfeoh = 0
        if not isfeoy:
            isfeoy = 0
        if not isfbow:
            isfbow = 0
        if not isfbom:
            isfbom = 0
        if not isfboq:
            isfboq = 0
        if not isfboh:
            isfboh = 0
        if not isfboy:
            isfboy = 0
        if not descs:
            descs = ''
        if not ccrid:
            ccrid = ''
        payload = {
            "sqndt": sqndt,
            "isnow": isnow,
            "isholiday": isholiday,
            "iseow": iseow,
            "iseom": iseom,
            "iseoq": iseoq,
            "iseoh": iseoh,
            "iseoy": iseoy,
            "isbow": isbow,
            "isbom": isbom,
            "isboq": isboq,
            "isboh": isboh,
            "isboy": isboy,
            "isfeow": isfeow,
            "isfeom": isfeom,
            "isfeoq": isfeoq,
            "isfeoh": isfeoh,
            "isfeoy": isfeoy,
            "isfbow": isfbow,
            "isfbom": isfbom,
            "isfboq": isfboq,
            "isfboh": isfboh,
            "isfboy": isfboy,
            "descs": descs,
            "ccrid": ccrid
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def update(seft, id=None, sqndt=None, isnow=None, isholiday=None, iseow=None, iseom=None, iseoq=None, iseoh=None, iseoy=None, isbow=None, isbom=None, isboq=None, isboh=None, isboy=None, isfeow=None, isfeom=None, isfeoq=None, isfeoh=None, isfeoy=None, isfbow=None, isfbom=None, isfboq=None, isfboh=None, isfboy=None, descs=None, ccrid=None):
        if not id:
            id = 0
        if not sqndt:
            sqndt = ''
        if not isnow:
            isnow = 0
        if not isholiday:
            isholiday = 0
        if not iseow:
            iseow = 0
        if not iseom:
            iseom = 0
        if not iseoq:
            iseoq = 0
        if not iseoh:
            iseoh = 0
        if not iseoy:
            iseoy = 0
        if not isbow:
            isbow = 0
        if not isbom:
            isbom = 0
        if not isboq:
            isboq = 0
        if not isboh:
            isboh = 0
        if not isboy:
            isboy = 0
        if not isfeow:
            isfeow = 0
        if not isfeom:
            isfeom = 0
        if not isfeoq:
            isfeoq = 0
        if not isfeoh:
            isfeoh = 0
        if not isfeoy:
            isfeoy = 0
        if not isfbow:
            isfbow = 0
        if not isfbom:
            isfbom = 0
        if not isfboq:
            isfboq = 0
        if not isfboh:
            isfboh = 0
        if not isfboy:
            isfboy = 0
        if not descs:
            descs = ''
        if not ccrid:
            ccrid = ''
        payload = {
            "id": id,
            "sqndt": sqndt,
            "isnow": isnow,
            "isholiday": isholiday,
            "iseow": iseow,
            "iseom": iseom,
            "iseoq": iseoq,
            "iseoh": iseoh,
            "iseoy": iseoy,
            "isbow": isbow,
            "isbom": isbom,
            "isboq": isboq,
            "isboh": isboh,
            "isboy": isboy,
            "isfeow": isfeow,
            "isfeom": isfeom,
            "isfeoq": isfeoq,
            "isfeoh": isfeoh,
            "isfeoy": isfeoy,
            "isfbow": isfbow,
            "isfbom": isfbom,
            "isfboq": isfboq,
            "isfboh": isfboh,
            "isfboy": isfboy,
            "descs": descs,
            "ccrid": ccrid
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