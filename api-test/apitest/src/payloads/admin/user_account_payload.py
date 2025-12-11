from datetime import datetime

class UserAccountPayload(object):
    def add(self, user_code=None, old_user_id=None, user_name=None, login_name=None, branch_id=None, department_id=None, cashier=None, officer=None, operation_staff=None, dealer=None, inter_branch_user=None, branch_manager=None, main_language=None, home=None, office=None, cell=None, facsimile=None, telex=None, user_phone=None, remark=None, user_account_status=None, time_zone=None, thousand_separate_character=None, decimal_separate_character=None, date_format=None, long_date_format=None, time_format=None, policy_id=None, expire_date=None):
        if not user_code:
            user_code = ''
        if not old_user_id:
            old_user_id = ''
        if not user_name:
            user_name = ''
        if not login_name:
            login_name = ''
        if not branch_id:
            branch_id = 0
        if not department_id:
            department_id = 0
        if not cashier:
            cashier = 0
        if not officer:
            officer = 0
        if not operation_staff:
            operation_staff = 0
        if not dealer:
            dealer = 0
        if not inter_branch_user:
            inter_branch_user = 0
        if not branch_manager:
            branch_manager = 0
        if not main_language:
            main_language = ''
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
        if not user_phone:
            user_phone = ''
        if not remark:
            remark = ''
        if not user_account_status:
            user_account_status = ''
        if not time_zone:
            time_zone = 0
        if not thousand_separate_character:
            thousand_separate_character = ''
        if not decimal_separate_character:
            decimal_separate_character = ''
        if not date_format:
            date_format = ''
        if not long_date_format:
            long_date_format = ''
        if not time_format:
            time_format = ''
        if not policy_id:
            policy_id = 0
        if not expire_date:
            expire_date = None
        payload = {
            "user_code": user_code,
            "old_user_id": old_user_id,
            "user_name": user_name,
            "login_name": login_name,
            "branch_id": branch_id,
            "department_id": department_id,
            "position": {
                "cashier": cashier,
                "officer": officer,
                "operation_staff": operation_staff,
                "dealer": dealer,
                "inter_branch_user": inter_branch_user,
                "branch_manager": branch_manager
            },
            "main_language": main_language,
            "phone_number": {
                "home": home,
                "office": office,
                "cell": cell,
                "facsimile": facsimile,
                "telex": telex
            },
            "user_phone": user_phone,
            "remark": remark,
            "user_account_status": user_account_status,
            "time_zone": time_zone,
            "thousand_separate_character": thousand_separate_character,
            "decimal_separate_character": decimal_separate_character,
            "date_format": date_format,
            "long_date_format": long_date_format,
            "time_format": time_format,
            "policy_id": policy_id,
            "expire_date": expire_date
        }
        return payload

    def update(self, id=None, old_user_id=None, user_name=None, login_name=None, department_id=None, cashier=None, officer=None, operation_staff=None, dealer=None, inter_branch_user=None, branch_manager=None, main_language=None, home=None, office=None, cell=None, facsimile=None, telex=None, user_phone=None, remark=None, user_account_status=None, time_zone=None, thousand_separate_character=None, decimal_separate_character=None, date_format=None, long_date_format=None, time_format=None, policy_id=None, expire_date=None):
        if not id:
            id = 0
        if not old_user_id:
            old_user_id = ''
        if not user_name:
            user_name = ''
        if not login_name:
            login_name = ''
        if not department_id:
            department_id = 0
        if not cashier:
            cashier = 0
        if not officer:
            officer = 0
        if not operation_staff:
            operation_staff = 0
        if not dealer:
            dealer = 0
        if not inter_branch_user:
            inter_branch_user = 0
        if not branch_manager:
            branch_manager = 0
        if not main_language:
            main_language = ''
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
        if not user_phone:
            user_phone = ''
        if not remark:
            remark = ''
        if not user_account_status:
            user_account_status = ''
        if not time_zone:
            time_zone = 0
        if not thousand_separate_character:
            thousand_separate_character = ''
        if not decimal_separate_character:
            decimal_separate_character = ''
        if not date_format:
            date_format = ''
        if not long_date_format:
            long_date_format = ''
        if not time_format:
            time_format = ''
        if not policy_id:
            policy_id = 0
        if not expire_date:
            expire_date = None
        payload = {
            "id": id,
            "old_user_id": old_user_id,
            "user_name": user_name,
            "login_name": login_name,
            "department_id": department_id,
            "position": {
                "cashier": cashier,
                "officer": officer,
                "operation_staff": operation_staff,
                "dealer": dealer,
                "inter_branch_user": inter_branch_user,
                "branch_manager": branch_manager
            },
            "main_language": main_language,
            "phone_number": {
                "home": home,
                "office": office,
                "cell": cell,
                "facsimile": facsimile,
                "telex": telex
            },
            "user_phone": user_phone,
            "remark": remark,
            "user_account_status": user_account_status,
            "time_zone": time_zone,
            "thousand_separate_character": thousand_separate_character,
            "decimal_separate_character": decimal_separate_character,
            "date_format": date_format,
            "long_date_format": long_date_format,
            "time_format": time_format,
            "policy_id": policy_id,
            "expire_date": expire_date
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

    def advanced_search(self, user_code=None, user_name=None, login_name=None, branch_name=None, department_name=None, user_account_status=None, is_online=None, branch_id=None, department_id=None, page_index=None, page_size=None):
        if not user_code:
            user_code = ''
        if not user_name:
            user_name = ''
        if not login_name:
            login_name = ''
        if not branch_name:
            branch_name = ''
        if not department_name:
            department_name = ''
        if not user_account_status:
            user_account_status = ''
        if not is_online:
            is_online = ''
        if not branch_id:
            branch_id = None
        if not department_id:
            department_id = None
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "user_code": user_code,
            "user_name": user_name,
            "login_name": login_name,
            "branch_name": branch_name,
            "department_name": department_name,
            "user_account_status": user_account_status,
            "is_online": is_online,
            "branch_id": branch_id,
            "department_id": department_id,
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