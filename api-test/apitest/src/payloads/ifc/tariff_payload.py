from datetime import datetime

class TariffPayload(object):
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

    def advanced_search(self, tariff_code=None, tariff_code_from=None, tariff_code_to=None, tariff_name=None, tariff_condition=None, tariff_status=None, page_index=None, page_size=None):
        if not tariff_code:
            tariff_code = None
        if not tariff_code_from:
            tariff_code_from = None
        if not tariff_code_to:
            tariff_code_to = None
        if not tariff_name:
            tariff_name = ''
        if not tariff_condition:
            tariff_condition = ''
        if not tariff_status:
            tariff_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "tariff_code": tariff_code,
            "tariff_code_from": tariff_code_from,
            "tariff_code_to": tariff_code_to,
            "tariff_name": tariff_name,
            "tariff_condition": tariff_condition,
            "tariff_status": tariff_status,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, id=None, tariff_code=None, tariff_name=None, tariff_condition=None, tariff_description=None, tariff_status=None, ifc_list=None):
        if not id:
            id = 0
        if not tariff_code:
            tariff_code = 0
        if not tariff_name:
            tariff_name = ''
        if not tariff_condition:
            tariff_condition = ''
        if not tariff_description:
            tariff_description = ''
        if not tariff_status:
            tariff_status = ''
        if not ifc_list:
            ifc_list = 0
        payload = {
            "id": id,
            "tariff_code": tariff_code,
            "tariff_name": tariff_name,
            "tariff_condition": tariff_condition,
            "tariff_description": tariff_description,
            "tariff_status": tariff_status,
            "ifc_list": ifc_list
        }
        return payload

    def update(self, id=None, tariff_code=None, tariff_name=None, tariff_condition=None, tariff_description=None, tariff_status=None, ifc_list=None):
        if not id:
            id = 0
        if not tariff_code:
            tariff_code = 0
        if not tariff_name:
            tariff_name = ''
        if not tariff_condition:
            tariff_condition = ''
        if not tariff_description:
            tariff_description = ''
        if not tariff_status:
            tariff_status = ''
        if not ifc_list:
            ifc_list = None
        payload = {
            "id": id,
            "tariff_code": tariff_code,
            "tariff_name": tariff_name,
            "tariff_condition": tariff_condition,
            "tariff_description": tariff_description,
            "tariff_status": tariff_status,
            "ifc_list": ifc_list
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload