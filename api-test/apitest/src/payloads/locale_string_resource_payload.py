from datetime import datetime

class LocaleStringResourcePayload(object):
    # locale string resource (lsr)
    def add_lsr(self, id=None, language=None, resource_name=None, resource_value=None):
        if not id:
            id = 0
        if not language:
            language = ''
        if not resource_name:
            resource_name = ''
        if not resource_value:
            resource_value = ''

        payload = {
            "id": id,
            "language": language,
            "resource_name": resource_name,
            "resource_value": resource_value
        }
        return payload

    def update_lsr(self, id=None, language=None, resource_name=None, resource_value=None):
        if not id:
            id = 0
        if not language:
            language = ''
        if not resource_name:
            resource_name = ''
        if not resource_value:
            resource_value = ''

        payload = {
            "id": id,
            "language": language,
            "resource_name": resource_name,
            "resource_value": resource_value
        }
        return payload