from datetime import datetime

class UserPolicyPayload(object):
    def add(self, descr=None, effective_from=None, effective_to=None, enforce_password_history=None, maximum_password_age=None, minimum_password_length=None, password_complexity_requirements=None, password_have_special_symbol=None, password_have_upper_case=None, password_have_symbol=None, password_have_number=None, can_login_from=None, can_login_to=None, lockout_tthrs=None):
        if not descr:
            descr = ''
        if not effective_from:
            effective_from = None
        if not effective_to:
            effective_to = None
        if not enforce_password_history:
            enforce_password_history = 0
        if not maximum_password_age:
            maximum_password_age = 0
        if not minimum_password_length:
            minimum_password_length = 0
        if not password_complexity_requirements:
            password_complexity_requirements = ''
        if not password_have_special_symbol:
            password_have_special_symbol = ''
        if not password_have_upper_case:
            password_have_upper_case = ''
        if not password_have_symbol:
            password_have_symbol = ''
        if not password_have_number:
            password_have_number = ''
        if not can_login_from:
            can_login_from = ''
        if not can_login_to:
            can_login_to = ''
        if not lockout_tthrs:
            lockout_tthrs = 0
        payload = {
            "descr": descr,
            "effective_from": effective_from,
            "effective_to": effective_to,
            "enforce_password_history": enforce_password_history,
            "maximum_password_age": maximum_password_age,
            "minimum_password_length": minimum_password_length,
            "password_complexity_requirements": password_complexity_requirements,
            "password_have_special_symbol": password_have_special_symbol,
            "password_have_upper_case": password_have_upper_case,
            "password_have_symbol": password_have_symbol,
            "password_have_number": password_have_number,
            "can_login_from": can_login_from,
            "can_login_to": can_login_to,
            "lockout_tthrs": lockout_tthrs
        }
        return payload

    def update(self, id=None, descr=None, effective_from=None, effective_to=None, enforce_password_history=None, maximum_password_age=None, minimum_password_length=None, password_complexity_requirements=None, password_have_special_symbol=None, password_have_upper_case=None, password_have_symbol=None, password_have_number=None, can_login_from=None, can_login_to=None, lockout_tthrs=None):
        if not id:
            id = 0
        if not descr:
            descr = ''
        if not effective_from:
            effective_from = None
        if not effective_to:
            effective_to = None
        if not enforce_password_history:
            enforce_password_history = 0
        if not maximum_password_age:
            maximum_password_age = 0
        if not minimum_password_length:
            minimum_password_length = 0
        if not password_complexity_requirements:
            password_complexity_requirements = ''
        if not password_have_special_symbol:
            password_have_special_symbol = ''
        if not password_have_upper_case:
            password_have_upper_case = ''
        if not password_have_symbol:
            password_have_symbol = ''
        if not password_have_number:
            password_have_number = ''
        if not can_login_from:
            can_login_from = ''
        if not can_login_to:
            can_login_to = ''
        if not lockout_tthrs:
            lockout_tthrs = 0
        payload = {
            "id": id,
            "descr": descr,
            "effective_from": effective_from,
            "effective_to": effective_to,
            "enforce_password_history": enforce_password_history,
            "maximum_password_age": maximum_password_age,
            "minimum_password_length": minimum_password_length,
            "password_complexity_requirements": password_complexity_requirements,
            "password_have_special_symbol": password_have_special_symbol,
            "password_have_upper_case": password_have_upper_case,
            "password_have_symbol": password_have_symbol,
            "password_have_number": password_have_number,
            "can_login_from": can_login_from,
            "can_login_to": can_login_to,
            "lockout_tthrs": lockout_tthrs
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

    def advanced_search(self, id=None, descr=None, effective_from=None, effective_to=None, page_index=None, page_size=None):
        if not id:
            id = None
        if not descr:
            descr = ''
        if not effective_from:
            effective_from = None
        if not effective_to:
            effective_to = None
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "id": id,
            "descr": descr,
            "effective_from": effective_from,
            "effective_to": effective_to,
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