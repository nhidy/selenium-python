from datetime import datetime

class IFCDefinitionPayload(object):
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

    def advanced_search(self, ifc_code=None, ifc_code_from=None, ifc_code_to=None, ifc_name=None, value_type=None, ifc_type=None, ifc_value=None, ifc_value_from=None, ifc_value_to=None, ifc_tenor=None, ifc_tenor_from=None, ifc_tenor_to=None, ifc_tenor_unit=None, ifc_condition=None, ifc_status=None, page_index=None, page_size=None):
        if not ifc_code:
            ifc_code = None
        if not ifc_code_from:
            ifc_code_from = None
        if not ifc_code_to:
            ifc_code_to = None
        if not ifc_name:
            ifc_name = ''
        if not value_type:
            value_type = ''
        if not ifc_type:
            ifc_type = ''
        if not ifc_value:
            ifc_value = None
        if not ifc_value_from:
            ifc_value_from = None
        if not ifc_value_to:
            ifc_value_to = None
        if not ifc_tenor:
            ifc_tenor = None
        if not ifc_tenor_from:
            ifc_tenor_from = None
        if not ifc_tenor_to:
            ifc_tenor_to = None
        if not ifc_tenor_unit:
            ifc_tenor_unit = ''
        if not ifc_condition:
            ifc_condition = ''
        if not ifc_status:
            ifc_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "ifc_code": ifc_code,
            "ifc_code_from": ifc_code_from,
            "ifc_code_to": ifc_code_to,
            "ifc_name": ifc_name,
            "value_type": value_type,
            "ifc_type": ifc_type,
            "ifc_value": ifc_value,
            "ifc_value_from": ifc_value_from,
            "ifc_value_to": ifc_value_to,
            "ifc_tenor": ifc_tenor,
            "ifc_tenor_from": ifc_tenor_from,
            "ifc_tenor_to": ifc_tenor_to,
            "ifc_tenor_unit": ifc_tenor_unit,
            "ifc_condition": ifc_condition,
            "ifc_status": ifc_status,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, id=None, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, value_base=None, is_linked=None, ifc_value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basic=None, ifc_tenor=None, ifc_tenor_unit=None, ifc_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, user_created=None, user_approved=None, effect_value_date=None, effect_value=None, group_id=None):
        if not id:
            id = 0
        if not ifc_code:
            ifc_code = 0
        if not ifc_name:
            ifc_name = ''
        if not ifc_type:
            ifc_type = ''
        if not ifc_sub_type:
            ifc_sub_type = ''
        if not value_base:
            value_base = ''
        if not is_linked:
            is_linked = ''
        if not ifc_value:
            ifc_value = 0
        if not ifc_linkage:
            ifc_linkage = 0
        if not ifc_operator:
            ifc_operator = ''
        if not margin_value:
            margin_value = 0
        if not value_type:
            value_type = ''
        if not currency_code:
            currency_code = ''
        if not floor_value:
            floor_value = 0
        if not ceiling_value:
            ceiling_value = 0
        if not value_basic:
            value_basic = ''
        if not ifc_tenor:
            ifc_tenor = 0
        if not ifc_tenor_unit:
            ifc_tenor_unit = ''
        if not ifc_condition:
            ifc_condition = ''
        if not rounding_rule:
            rounding_rule = ''
        if not rounding_basis:
            rounding_basis = ''
        if not rounding_num:
            rounding_num = 0
        if not share_fee:
            share_fee = 0
        if not ifc_status:
            ifc_status = ''
        if not user_created:
            user_created = 0
        if not user_approved:
            user_approved = 0
        if not effect_value_date:
            effect_value_date = ''
        if not effect_value:
            effect_value = 0
        if not group_id:
            group_id = 0
        payload = {
            "id": id,
            "ifc_code": ifc_code,
            "ifc_name": ifc_name,
            "ifc_type": ifc_type,
            "ifc_sub_type": ifc_sub_type,
            "value_base": value_base,
            "is_linked": is_linked,
            "ifc_value": ifc_value,
            "ifc_linkage": ifc_linkage,
            "ifc_operator": ifc_operator,
            "margin_value": margin_value,
            "value_type": value_type,
            "currency_code": currency_code,
            "floor_value": floor_value,
            "ceiling_value": ceiling_value,
            "value_basic": value_basic,
            "ifc_tenor": ifc_tenor,
            "ifc_tenor_unit": ifc_tenor_unit,
            "ifc_condition": ifc_condition,
            "rounding_rule": rounding_rule,
            "rounding_basis": rounding_basis,
            "rounding_num": rounding_num,
            "share_fee": share_fee,
            "ifc_status": ifc_status,
            "user_created": user_created,
            "user_approved": user_approved,
            "effect_value_date": effect_value_date,
            "effect_value": effect_value,
            "group_id": group_id
        }
        return payload

    def update(self, id=None, ifc_code=None, ifc_name=None, ifc_sub_type=None, value_base=None, is_linked=None, ifc_value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, currency_code=None, floor_value=None, ceiling_value=None, value_basic=None, ifc_tenor=None, ifc_tenor_unit=None, ifc_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_value_date=None, effect_value=None, group_id=None):
        if not id:
            id = 0
        if not ifc_code:
            ifc_code = 0
        if not ifc_name:
            ifc_name = ''
        if not ifc_sub_type:
            ifc_sub_type = ''
        if not value_base:
            value_base = ''
        if not is_linked:
            is_linked = ''
        if not ifc_value:
            ifc_value = 0
        if not ifc_linkage:
            ifc_linkage = 0
        if not ifc_operator:
            ifc_operator = ''
        if not margin_value:
            margin_value = 0
        if not currency_code:
            currency_code = ''
        if not floor_value:
            floor_value = 0
        if not ceiling_value:
            ceiling_value = 0
        if not value_basic:
            value_basic = ''
        if not ifc_tenor:
            ifc_tenor = 0
        if not ifc_tenor_unit:
            ifc_tenor_unit = ''
        if not ifc_condition:
            ifc_condition = ''
        if not rounding_rule:
            rounding_rule = ''
        if not rounding_basis:
            rounding_basis = ''
        if not rounding_num:
            rounding_num = 0
        if not share_fee:
            share_fee = 0
        if not ifc_status:
            ifc_status = ''
        if not effect_value_date:
            effect_value_date = None
        if not effect_value:
            effect_value = 0
        if not group_id:
            group_id = 0
        payload = {
            "id": id,
            "ifc_code": ifc_code,
            "ifc_name": ifc_name,
            "ifc_sub_type": ifc_sub_type,
            "value_base": value_base,
            "is_linked": is_linked,
            "ifc_value": ifc_value,
            "ifc_linkage": ifc_linkage,
            "ifc_operator": ifc_operator,
            "margin_value": margin_value,
            "currency_code": currency_code,
            "floor_value": floor_value,
            "ceiling_value": ceiling_value,
            "value_basic": value_basic,
            "ifc_tenor": ifc_tenor,
            "ifc_tenor_unit": ifc_tenor_unit,
            "ifc_condition": ifc_condition,
            "rounding_rule": rounding_rule,
            "rounding_basis": rounding_basis,
            "rounding_num": rounding_num,
            "share_fee": share_fee,
            "ifc_status": ifc_status,
            "effect_value_date": effect_value_date,
            "effect_value": effect_value,
            "group_id": group_id
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload