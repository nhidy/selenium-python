from datetime import datetime

class BranchPayload(object):
    def add(self, old_branch_id=None, branch_name=None, branch_address=None, branch_phone=None, home=None, office=None, cell=None, facsimile=None, telex=None, tax_code=None, base_currency_code=None, base_currency_name=None, local_currency_code=None, local_currency_name=None, bic=None, domestic_bank_code=None, internal_code=None, country=None, main_language=None, time_zone_of_branch=None, thousand_separate_character=None, decimal_separate_character=None, date_format_for_short=None, long_date_format=None, time_format=None, online=None, ud_field1=None, long_branch_name=None):
        if not old_branch_id:
            old_branch_id = ''
        if not branch_name:
            branch_name = ''
        if not branch_address:
            branch_address = ''
        if not branch_phone:
            branch_phone = ''
        if not home:
            home = ''
        if not office:
            office = ''
        if not cell:
            cell = ''
        if not facsimile:
            facsimile = ''
        if not telex:
            telex = ''
        if not tax_code:
            tax_code = ''
        if not base_currency_code:
            base_currency_code = ''
        if not base_currency_name:
            base_currency_name = ''
        if not local_currency_code:
            local_currency_code = ''
        if not local_currency_name:
            local_currency_name = ''
        if not bic:
            bic = ''
        if not domestic_bank_code:
            domestic_bank_code = ''
        if not internal_code:
            internal_code = ''
        if not country:
            country = ''
        if not main_language:
            main_language = ''
        if not time_zone_of_branch:
            time_zone_of_branch = 0
        if not thousand_separate_character:
            thousand_separate_character = ','
        if not decimal_separate_character:
            decimal_separate_character = '.'
        if not date_format_for_short:
            date_format_for_short = ''
        if not long_date_format:
            long_date_format = ''
        if not time_format:
            time_format = ''
        if not online:
            online = ''
        if not ud_field1:
            ud_field1 = ''
        if not long_branch_name:
            long_branch_name = ''
        payload = {
            "old_branch_id": old_branch_id,
            "branch_name": branch_name,
            "branch_address": branch_address,
            "branch_phone": branch_phone,
            "phone_number": {
                "home": home,
                "office": office,
                "cell": cell,
                "facsimile": facsimile,
                "telex": telex
            },
            "tax_code": tax_code,
            "base_currency_code": base_currency_code,
            "base_currency_name": base_currency_name,
            "local_currency_code": local_currency_code,
            "local_currency_name": local_currency_name,
            "reference_code": {
                "bic": bic,
                "domestic_bank_code": domestic_bank_code,
                "internal_code": internal_code
            },
            "country": country,
            "main_language": main_language,
            "time_zone_of_branch": time_zone_of_branch,
            "thousand_separate_character": thousand_separate_character,
            "decimal_separate_character": decimal_separate_character,
            "date_format_for_short": date_format_for_short,
            "long_date_format": long_date_format,
            "time_format": time_format,
            "online": online,
            "ud_field1": ud_field1,
            "long_branch_name": long_branch_name
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

    def update(seft, id=None, old_branch_id=None, branch_name=None, branch_address=None, branch_phone=None, home=None, office=None, cell=None, facsimile=None, telex=None, tax_code=None, base_currency_code=None, base_currency_name=None, local_currency_code=None, local_currency_name=None, bic=None, domestic_bank_code=None, internal_code=None, country=None, main_language=None, time_zone_of_branch=None, thousand_separate_character=None, decimal_separate_character=None, date_format_for_short=None, long_date_format=None, time_format=None, online=None, ud_field1=None, long_branch_name=None):
        if not id:
            id = 0
        if not old_branch_id:
            old_branch_id = ''
        if not branch_name:
            branch_name = ''
        if not branch_address:
            branch_address = ''
        if not branch_phone:
            branch_phone = ''
        if not home:
            home = ''
        if not office:
            office = ''
        if not cell:
            cell = ''
        if not facsimile:
            facsimile = ''
        if not telex:
            telex = ''
        if not tax_code:
            tax_code = ''
        if not base_currency_code:
            base_currency_code = ''
        if not base_currency_name:
            base_currency_name = ''
        if not local_currency_code:
            local_currency_code = ''
        if not local_currency_name:
            local_currency_name = ''
        if not bic:
            bic = ''
        if not domestic_bank_code:
            domestic_bank_code = ''
        if not internal_code:
            internal_code = ''
        if not country:
            country = ''
        if not main_language:
            main_language = ''
        if not time_zone_of_branch:
            time_zone_of_branch = 0
        if not thousand_separate_character:
            thousand_separate_character = ''
        if not decimal_separate_character:
            decimal_separate_character = ''
        if not date_format_for_short:
            date_format_for_short = ''
        if not long_date_format:
            long_date_format = ''
        if not time_format:
            time_format = ''
        if not online:
            online = ''
        if not ud_field1:
            ud_field1 = ''
        if not long_branch_name:
            long_branch_name = ''
        payload = {
            "id": id,
            "old_branch_id": old_branch_id,
            "branch_name": branch_name,
            "branch_address": branch_address,
            "branch_phone": branch_phone,
            "phone_number": {
                "home": home,
                "office": office,
                "cell": cell,
                "facsimile": facsimile,
                "telex": telex
            },
            "tax_code": tax_code,
            "base_currency_code": base_currency_code,
            "base_currency_name": base_currency_name,
            "local_currency_code": local_currency_code,
            "local_currency_name": local_currency_name,
            "reference_code": {
                "bic": bic,
                "domestic_bank_code": domestic_bank_code,
                "internal_code": internal_code
            },
            "country": country,
            "main_language": main_language,
            "time_zone_of_branch": time_zone_of_branch,
            "thousand_separate_character": thousand_separate_character,
            "decimal_separate_character": decimal_separate_character,
            "date_format_for_short": date_format_for_short,
            "long_date_format": long_date_format,
            "time_format": time_format,
            "online": online,
            "ud_field1": ud_field1,
            "long_branch_name": long_branch_name
        }
        return payload

    def advanced_search(self, branch_code=None, branch_name=None, branch_address=None, base_currency_code=None, online=None, page_index=None, page_size=None):
        if not branch_code:
            branch_code = ''
        if not branch_name:
            branch_name = ''
        if not branch_address:
            branch_address = ''
        if not base_currency_code:
            base_currency_code = ''
        if not online:
            online = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "branch_code": branch_code,
            "branch_name": branch_name,
            "branch_address": branch_address,
            "base_currency_code": base_currency_code,
            "online": online,
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