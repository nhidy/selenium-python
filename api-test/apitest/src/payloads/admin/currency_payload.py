from datetime import datetime

class CurrencyPayload(object):
    def add(self, currency_id = None, short_currency_id = None, currency_name1 = None, currency_name2 = None, currency_name3 = None, currency_number = None, master_name1 = None, master_name2 = None, master_name3 = None, decimal_name1 = None, decimal_name2 = None, decimal_name3 = None, decimal_digits = None, rounding_digits = None, status_of_currency = None, order = None):
        if not currency_id: 
            currency_id = ''
        if not short_currency_id: 
            short_currency_id = ''
        if not currency_name1: 
            currency_name1 = ''
        if not currency_name2: 
            currency_name2 = ''
        if not currency_name3: 
            currency_name3 = ''
        if not currency_number: 
            currency_number = 0
        if not master_name1: 
            master_name1 = ''
        if not master_name2: 
            master_name2 = ''
        if not master_name3: 
            master_name3 = ''
        if not decimal_name1: 
            decimal_name1 = ''
        if not decimal_name2: 
            decimal_name2 = ''
        if not decimal_name3: 
            decimal_name3 = ''
        if not decimal_digits: 
            decimal_digits = 0
        if not rounding_digits: 
            rounding_digits = 0
        if not status_of_currency: 
            status_of_currency = ''
        if not order: 
            order = 0
        payload = {
            "currency_id": currency_id,
            "short_currency_id": short_currency_id,
            "currency_name": {
                "currency_name1": currency_name1,
                "currency_name2": currency_name2,
                "currency_name3": currency_name3,
            }, 
            "currency_number": currency_number,
            "master_name": {
                "master_name1": master_name1,
                "master_name2": master_name2,
                "master_name3": master_name3,
            }, 
            "decimal_name": {
                "decimal_name1": decimal_name1,
                "decimal_name2": decimal_name2,
                "decimal_name3": decimal_name3,
            }, 
            "decimal_digits": decimal_digits,
            "rounding_digits": rounding_digits,
            "status_of_currency": status_of_currency,
            "order": order,
        }
        return payload

    def update(self, id=None, currency_id = None, short_currency_id = None, currency_name1 = None, currency_name2 = None, currency_name3 = None, currency_number = None, master_name1 = None, master_name2 = None, master_name3 = None, decimal_name1 = None, decimal_name2 = None, decimal_name3 = None, decimal_digits = None, rounding_digits = None, status_of_currency = None, order = None):
        if not id:
            id = 0
        if not currency_id: 
            currency_id = ''
        if not short_currency_id: 
            short_currency_id = ''
        if not currency_name1: 
            currency_name1 = ''
        if not currency_name2: 
            currency_name2 = ''
        if not currency_name3: 
            currency_name3 = ''
        if not currency_number: 
            currency_number = 0
        if not master_name1: 
            master_name1 = ''
        if not master_name2: 
            master_name2 = ''
        if not master_name3: 
            master_name3 = ''
        if not decimal_name1: 
            decimal_name1 = ''
        if not decimal_name2: 
            decimal_name2 = ''
        if not decimal_name3: 
            decimal_name3 = ''
        if not decimal_digits: 
            decimal_digits = 0
        if not rounding_digits: 
            rounding_digits = 0
        if not status_of_currency: 
            status_of_currency = ''
        if not order: 
            order = 0
        payload = {
            "id": id,
            "currency_id": currency_id,
            "short_currency_id": short_currency_id,
            "currency_name": {
                "currency_name1": currency_name1,
                "currency_name2": currency_name2,
                "currency_name3": currency_name3,
            }, 
            "currency_number": currency_number,
            "master_name": {
                "master_name1": master_name1,
                "master_name2": master_name2,
                "master_name3": master_name3,
            }, 
            "decimal_name": {
                "decimal_name1": decimal_name1,
                "decimal_name2": decimal_name2,
                "decimal_name3": decimal_name3,
            }, 
            "decimal_digits": decimal_digits,
            "rounding_digits": rounding_digits,
            "status_of_currency": status_of_currency,
            "order": order,
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def advanced_search(self, currency_id=None, short_currency_id=None, currency_number=None, currency_number_from=None, currency_number_to=None, status_of_currency=None, order=None, order_from=None, order_to=None, page_index=None, page_size=None):
        if not currency_id:
            currency_id = ''
        if not short_currency_id:
            short_currency_id = ''
        if not currency_number:
            currency_number = None
        if not currency_number_from:
            currency_number_from = None
        if not currency_number_to:
            currency_number_to = None
        if not status_of_currency:
            status_of_currency = ''
        if not order:
            order = None
        if not order_from:
            order_from = None
        if not order_to:
            order_to = None
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "currency_id": currency_id,
            "short_currency_id": short_currency_id,
            "currency_number": currency_number,
            "currency_number_from": currency_number_from,
            "currency_number_to": currency_number_to,
            "status_of_currency": status_of_currency,
            "order": order,
            "order_from": order_from,
            "order_to": order_to,
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
