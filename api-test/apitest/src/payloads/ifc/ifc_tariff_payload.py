from datetime import datetime

class IFCTariffPayload(object):
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

    def advanced_search(self, ifc_code=None, ifc_name=None, ifc_value=None, ifc_type_caption=None, ifc_tenor=None, ifc_tenor_unit_caption=None, ifc_condition=None, ifc_statusct=None, tariff_code=None, ifctype=None, ifc_tenorun=None, ifc_status=None, page_index=None, page_size=None):
        if not ifc_code:
            ifc_code = None
        if not ifc_name:
            ifc_name = ''
        if not ifc_value:
            ifc_value = None
        if not ifc_type_caption:
            ifc_type_caption = ''
        if not ifc_tenor:
            ifc_tenor = None
        if not ifc_tenor_unit_caption:
            ifc_tenor_unit_caption = ''
        if not ifc_condition:
            ifc_condition = ''
        if not ifc_statusct:
            ifc_statusct = ''
        if not tariff_code:
            tariff_code = None
        if not ifctype:
            ifctype = ''
        if not ifc_tenorun:
            ifc_tenorun = ''
        if not ifc_status:
            ifc_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "ifc_code": ifc_code,
            "ifc_name": ifc_name,
            "ifc_value": ifc_value,
            "ifc_type_caption": ifc_type_caption,
            "ifc_tenor": ifc_tenor,
            "ifc_tenor_unit_caption": ifc_tenor_unit_caption,
            "ifc_condition": ifc_condition,
            "ifc_statusct": ifc_statusct,
            "tariff_code": tariff_code,
            "ifctype": ifctype,
            "ifc_tenorun": ifc_tenorun,
            "ifc_status": ifc_status,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, id=None, tariff_code=None, ifc_code=None, tariff_status=None, last_datime=None):
        if not id:
            id = 0
        if not tariff_code:
            tariff_code = 0
        if not ifc_code:
            ifc_code = 0
        if not tariff_status:
            tariff_status = ''
        if not last_datime:
            last_datime = ''
        payload = {
            "id": id,
            "tariff_code": tariff_code,
            "ifc_code": ifc_code,
            "tariff_status": tariff_status,
            "last_datime": last_datime
        }
        return payload

    def update(self, id=None, tariff_code=None, ifc_code=None, tariff_status=None, last_datime=None):
        if not id:
            id = 0
        if not tariff_code:
            tariff_code = 0
        if not ifc_code:
            ifc_code = 0
        if not tariff_status:
            tariff_status = ''
        if not last_datime:
            last_datime = ''
        payload = {
            "id": id,
            "tariff_code": tariff_code,
            "ifc_code": ifc_code,
            "tariff_status": tariff_status,
            "last_datime": last_datime
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def get_list_ifc_by_tariff_code(self, tariff_code=None):
        if not tariff_code:
            tariff_code = 0
        payload = {
            "tariff_code": tariff_code
        }
        return payload