from datetime import datetime

class DenominationPayload(object):
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

    def advanced_search(self, currency_id=None, face_value=None, face_type=None, face_description=None, order=None, page_index=None, page_size=None):
        if not currency_id:
            currency_id = ''
        if not face_value:
            face_value = None
        if not face_type:
            face_type = ''
        if not face_description:
            face_description = ''
        if not order:
            order = None
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "currency_id": currency_id,
            "face_value": face_value,
            "face_type": face_type,
            "face_description": face_description,
            "order": order,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, currency_id=None, face_value=None, face_type=None, face_description=None, order=None):
        if not currency_id:
            currency_id = ''
        if not face_value:
            face_value = 0
        if not face_type:
            face_type = ''
        if not face_description:
            face_description = ''
        if not order:
            order = 0
        payload = {
            "currency_id": currency_id,
            "face_value": face_value,
            "face_type": face_type,
            "face_description": face_description,
            "order": order
        }
        return payload

    def update(self, id=None, currency_id=None, face_value=None, face_type=None, face_description=None, order=None):
        if not id:
            id = 0
        if not currency_id:
            currency_id = ''
        if not face_value:
            face_value = 0
        if not face_type:
            face_type = ''
        if not face_description:
            face_description = ''
        if not order:
            order = 0
        payload = {
            "id": id,
            "currency_id": currency_id,
            "face_value": face_value,
            "face_type": face_type,
            "face_description": face_description,
            "order": order
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload