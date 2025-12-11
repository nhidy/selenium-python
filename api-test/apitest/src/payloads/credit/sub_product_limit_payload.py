from datetime import datetime

class SubProductLimitPayload(object):
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

    def advanced_search(self, sub_product_limit_code=None, sub_product_limit_name=None, product_name=None, product_limit_code=None, customer_type=None, customer_code=None, customer_name=None, currency_code=None, limit_amount_from=None, limit_amount_to=None, sub_product_status=None, page_index=None, page_size=None):
        if not sub_product_limit_code:
            sub_product_limit_code = ''
        if not sub_product_limit_name:
            sub_product_limit_name = ''
        if not product_name:
            product_name = ''
        if not product_limit_code:
            product_limit_code = ''
        if not customer_type:
            customer_type = ''
        if not customer_code:
            customer_code = ''
        if not customer_name:
            customer_name = ''
        if not currency_code:
            currency_code = ''
        if not limit_amount_from:
            limit_amount_from = None
        if not limit_amount_to:
            limit_amount_to = None
        if not sub_product_status:
            sub_product_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "sub_product_limit_code": sub_product_limit_code,
            "sub_product_limit_name": sub_product_limit_name,
            "product_name": product_name,
            "product_limit_code": product_limit_code,
            "customer_type": customer_type,
            "customer_code": customer_code,
            "customer_name": customer_name,
            "currency_code": currency_code,
            "limit_amount_from": limit_amount_from,
            "limit_amount_to": limit_amount_to,
            "sub_product_status": sub_product_status,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, sub_product_limit_name=None, product_limit_code=None, customer_type=None, customer_id=None, reference_id=None, currency_code=None, limit_amount=None, credit_facility=None):
        if not sub_product_limit_name:
            sub_product_limit_name = ''
        if not product_limit_code:
            product_limit_code = ''
        if not customer_type:
            customer_type = ''
        if not customer_id:
            customer_id = 0
        if not reference_id:
            reference_id = ''
        if not currency_code:
            currency_code = ''
        if not limit_amount:
            limit_amount = 0
        if not credit_facility:
            credit_facility = ''
        payload = {
            "sub_product_limit_name": sub_product_limit_name,
            "product_limit_code": product_limit_code,
            "customer_type": customer_type,
            "customer_id": customer_id,
            "reference_id": reference_id,
            "currency_code": currency_code,
            "limit_amount": limit_amount,
            "credit_facility": credit_facility
        }
        return payload

    def update(self, id=None, sub_product_limit_code=None, sub_product_limit_name=None, reference_id=None, currency_code=None, limit_amount=None, credit_facility=None):
        if not id:
            id = 0
        if not sub_product_limit_code:
            sub_product_limit_code = ''
        if not sub_product_limit_name:
            sub_product_limit_name = ''
        if not reference_id:
            reference_id = ''
        if not currency_code:
            currency_code = ''
        if not limit_amount:
            limit_amount = 0
        if not credit_facility:
            credit_facility = ''
        payload = {
            "id": id,
            "sub_product_limit_code": sub_product_limit_code,
            "sub_product_limit_name": sub_product_limit_name,
            "reference_id": reference_id,
            "currency_code": currency_code,
            "limit_amount": limit_amount,
            "credit_facility": credit_facility
        }
        return payload