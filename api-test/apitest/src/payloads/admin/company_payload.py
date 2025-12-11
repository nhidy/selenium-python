from datetime import datetime

class CompanyPayload(object):
    def add(self, company_code=None, company_name=None, company_type=None, company_status=None, gatway_user_name=None, gatway_password=None, descr=None, message_type_field=None, processing_code_field=None, message_standard=None, message_format=None, message_transport_protocol=None, uri=None, user_name=None, password=None):
        if not company_code:
            company_code = ''
        if not company_name:
            company_name = ''
        if not company_type:
            company_type = ''
        if not company_status:
            company_status = ''
        if not gatway_user_name:
            gatway_user_name = ''
        if not gatway_password:
            gatway_password = ''
        if not descr:
            descr = ''
        if not message_type_field:
            message_type_field = ''
        if not processing_code_field:
            processing_code_field = ''
        if not message_standard:
            message_standard = ''
        if not message_format:
            message_format = ''
        if not message_transport_protocol:
            message_transport_protocol = ''
        if not uri:
            uri = ''
        if not user_name:
            user_name = ''
        if not password:
            password = ''
        payload = {
            "company_code": company_code,
            "company_name": company_name,
            "company_type": company_type,
            "company_status": company_status,
            "gatway_user_name": gatway_user_name,
            "gatway_password": gatway_password,
            "descr": descr,
            "message_type_field": message_type_field,
            "processing_code_field": processing_code_field,
            "message_standard": message_standard,
            "message_format": message_format,
            "message_transport_protocol": message_transport_protocol,
            "uri": uri,
            "user_name": user_name,
            "password": password
        }
        return payload

    def update(self, id=None, company_code=None, company_name=None, company_type=None, company_status=None, gatway_user_name=None, gatway_password=None, descr=None, message_type_field=None, processing_code_field=None, message_standard=None, message_format=None, message_transport_protocol=None, uri=None, user_name=None, password=None):
        if not id:
            id = 0
        if not company_code:
            company_code = ''
        if not company_name:
            company_name = ''
        if not company_type:
            company_type = ''
        if not company_status:
            company_status = ''
        if not gatway_user_name:
            gatway_user_name = ''
        if not gatway_password:
            gatway_password = ''
        if not descr:
            descr = ''
        if not message_type_field:
            message_type_field = ''
        if not processing_code_field:
            processing_code_field = ''
        if not message_standard:
            message_standard = ''
        if not message_format:
            message_format = ''
        if not message_transport_protocol:
            message_transport_protocol = ''
        if not uri:
            uri = ''
        if not user_name:
            user_name = ''
        if not password:
            password = ''
        payload = {
            "id": id,
            "company_code": company_code,
            "company_name": company_name,
            "company_type": company_type,
            "company_status": company_status,
            "gatway_user_name": gatway_user_name,
            "gatway_password": gatway_password,
            "descr": descr,
            "message_type_field": message_type_field,
            "processing_code_field": processing_code_field,
            "message_standard": message_standard,
            "message_format": message_format,
            "message_transport_protocol": message_transport_protocol,
            "uri": uri,
            "user_name": user_name,
            "password": password
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def view(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload
    def advanced_search(self, company_code=None, company_name=None, company_type=None, company_status=None, descr=None, page_index=None, page_size=None):
        if not company_code:
            company_code = ''
        if not company_name:
            company_name = ''
        if not company_type:
            company_type = ''
        if not company_status:
            company_status = ''
        if not descr:
            descr = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "company_code": company_code,
            "company_name": company_name,
            "company_type": company_type,
            "company_status": company_status,
            "descr": descr,
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
