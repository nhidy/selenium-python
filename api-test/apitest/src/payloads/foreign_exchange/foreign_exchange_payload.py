from datetime import datetime

class ForeignExchangePayload(object):
    def add(self, currency_code=None, rate_type=None, base_currency_rate=None, local_currency_rate=None, rate_margin=None, value_date=None, user_id_fx=None, original_source=None, rate_sequence=None, is_listed=None, branch_id_fx=None):
        if not currency_code:
            currency_code = ''
        if not rate_type:
            rate_type = ''
        if not base_currency_rate:
            base_currency_rate = 0
        if not local_currency_rate:
            local_currency_rate = 0
        if not rate_margin:
            rate_margin = 0
        if not value_date:
            value_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        if not user_id_fx:
            user_id_fx = 0
        if not original_source:
            original_source = ''
        if not rate_sequence:
            rate_sequence = 0
        if not is_listed:
            is_listed = ''
        if not branch_id_fx:
            branch_id_fx = 0
        payload = {
            "currency_code": currency_code,
            "rate_type": rate_type,
            "base_currency_rate": base_currency_rate,
            "local_currency_rate": local_currency_rate,
            "rate_margin": rate_margin,
            "value_date": value_date,
            "user_id_fx": user_id_fx,
            "original_source": original_source,
            "rate_sequence": rate_sequence,
            "is_listed": is_listed,
            "branch_id_fx": branch_id_fx
        }
        return payload

    def update(seft,id=None, currency_code=None, rate_type=None, base_currency_rate=None, local_currency_rate=None, rate_margin=None, value_date=None, user_id_fx=None, original_source=None, rate_sequence=None, is_listed=None, branch_id_fx=None):
        if not id:
            id = 0
        if not currency_code:
            currency_code = ''
        if not rate_type:
            rate_type = ''
        if not base_currency_rate:
            base_currency_rate = 0
        if not local_currency_rate:
            local_currency_rate = 0
        if not rate_margin:
            rate_margin = 0
        if not value_date:
            value_date = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        if not user_id_fx:
            user_id_fx = 0
        if not original_source:
            original_source = ''
        if not rate_sequence:
            rate_sequence = 0
        if not is_listed:
            is_listed = ''
        if not branch_id_fx:
            branch_id_fx = 0
        payload = {
            "id": id,
            "currency_code": currency_code,
            "rate_type": rate_type,
            "base_currency_rate": base_currency_rate,
            "local_currency_rate": local_currency_rate,
            "rate_margin": rate_margin,
            "value_date": value_date,
            "user_id_fx": user_id_fx,
            "original_source": original_source,
            "rate_sequence": rate_sequence,
            "is_listed": is_listed,
            "branch_id_fx": branch_id_fx
        }
        return payload

    def advanced_search(self, branch_id_fx=None, working_date=None, page=None, limit=None):
        if not branch_id_fx:
            branch_id_fx = None
        if not working_date:
            working_date = ''
        if not page:
            page = 0
        if not limit:
            limit = 0
        payload = {
            "branch_id_fx": branch_id_fx,
            "working_date": working_date,
            "page": page,
            "limit": limit
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

    def view(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload