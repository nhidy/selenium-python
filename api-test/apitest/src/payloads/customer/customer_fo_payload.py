from datetime import datetime

class CustomerFOPayload(object):
    def ctm_apr(self, customer_code=None, customer_name=None, customer_status=None, description=None):
        if not customer_code:
            customer_code = ''
        if not customer_name:
            customer_name = ''
        if not customer_status:
            customer_status = ''
        if not description:
            description = ''
        payload = {
            "customer_code": customer_code,
            "customer_name": customer_name,
            "customer_status": customer_status,
            "description": description,
            "customer_type": "C"
        }
        return payload