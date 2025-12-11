from datetime import datetime

class ProductLimitPayload(object):
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

    def advanced_search(self, product_limit_code=None, product_limit_name=None, customer_type=None, limit_type=None, currency_code=None, customer_code=None, customer_name=None, limit_amount_from=None, limit_amount_to=None, product_status=None, page_index=None, page_size=None):
        if not product_limit_code:
            product_limit_code = ''
        if not product_limit_name:
            product_limit_name = ''
        if not customer_type:
            customer_type = ''
        if not limit_type:
            limit_type = ''
        if not currency_code:
            currency_code = ''
        if not customer_code:
            customer_code = ''
        if not customer_name:
            customer_name = ''
        if not limit_amount_from:
            limit_amount_from = None
        if not limit_amount_to:
            limit_amount_to = None
        if not product_status:
            product_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "product_limit_code": product_limit_code,
            "product_limit_name": product_limit_name,
            "customer_type": customer_type,
            "limit_type": limit_type,
            "currency_code": currency_code,
            "customer_code": customer_code,
            "customer_name": customer_name,
            "limit_amount_from": limit_amount_from,
            "limit_amount_to": limit_amount_to,
            "product_status": product_status,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, product_limit_name=None, customer_type=None, customer_id=None, limit_type=None, reference_id=None, currency_code=None, limit_amount=None, available_amount=None, product_status=None, accounting_group=None, exchange_rate=None, user_created=None, secure_type=None, secure_rate=None):
        if not product_limit_name:
            product_limit_name = ''
        if not customer_type:
            customer_type = ''
        if not customer_id:
            customer_id = 0
        if not reference_id:
            reference_id = ''
        if not limit_type:
            limit_type = ''
        if not currency_code:
            currency_code = ''
        if not limit_amount:
            limit_amount = 0
        if not available_amount:
            available_amount = 0
        if not product_status:
            product_status = ''
        if not accounting_group:
            accounting_group = 0
        if not exchange_rate:
            exchange_rate = 0
        if not user_created:
            user_created = 0
        if not secure_type:
            secure_type = ''
        if not secure_rate:
            secure_rate = 0
        payload = {
            "product_limit_name": product_limit_name,
            "customer_type": customer_type,
            "customer_id": customer_id,
            "limit_type": limit_type,
            "reference_id": reference_id,
            "currency_code": currency_code,
            "limit_amount": limit_amount,
            "available_amount": available_amount,
            "product_status": product_status,
            "accounting_group": accounting_group,
            "exchange_rate": exchange_rate,
            "user_created": user_created,
            "secure_type": secure_type,
            "secure_rate": secure_rate
        }
        return payload

    def update(self, id=None, product_limit_code=None, product_limit_name=None, customer_type=None, customer_id=None, limit_type=None, reference_id=None, currency_code=None, limit_amount=None, product_status=None, accounting_group=None, exchange_rate=None, secure_type=None, secure_rate=None):
        if not id:
            id = 0
        if not product_limit_code:
            product_limit_code = ''
        if not product_limit_name:
            product_limit_name = ''
        if not customer_type:
            customer_type = ''
        if not customer_id:
            customer_id = 0
        if not limit_type:
            limit_type = ''
        if not currency_code:
            currency_code = ''
        if not limit_amount:
            limit_amount = 0
        if not product_status:
            product_status = ''
        if not accounting_group:
            accounting_group = 0
        if not exchange_rate:
            exchange_rate = 0
        if not secure_type:
            secure_type = ''
        if not secure_rate:
            secure_rate = 0
        payload = {
            "id": id,
            "product_limit_code": product_limit_code,
            "product_limit_name": product_limit_name,
            "customer_type": customer_type,
            "customer_id": customer_id,
            "limit_type": limit_type,
            "reference_id": reference_id,
            "currency_code": currency_code,
            "limit_amount": limit_amount,
            "product_status": product_status,
            "accounting_group": accounting_group,
            "exchange_rate": exchange_rate,
            "secure_type": secure_type,
            "secure_rate": secure_rate
        }
        return payload