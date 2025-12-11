from datetime import datetime

class CreditCatalogPayload(object):
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

    def advanced_search(self, catalog_code=None, catalog_name=None, currency_code=None, credit_type=None, tenor_type=None, credit_facility=None, catalog_status=None, page_index=None, page_size=None):
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not currency_code:
            currency_code = ''
        if not credit_type:
            credit_type = ''
        if not tenor_type:
            tenor_type = ''
        if not credit_facility:
            credit_facility = ''
        if not catalog_status:
            catalog_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "currency_code": currency_code,
            "credit_type": credit_type,
            "tenor_type": tenor_type,
            "credit_facility": credit_facility,
            "catalog_status": catalog_status,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, catalog_code=None, catalog_name=None, currency_code=None, secure_currency_code=None, credit_type=None, tenor_type=None, is_syndicated=None, interest_computation_mode=None, secure_type=None, secure_rate=None, principal_tenor=None, principal_tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, fine_tenor=None, fine_tenor_unit=None, credit_purpose=None, credit_classification=None, credit_facility=None, discount_rate=None, re_discount_rate=None, disbursement_mode=None, principal_grace_period=None, interest_grace_period=None, fine_grace_period=None, is_provision=None, provision_tenor=None, provision_tenor_unit=None, rollover_option=None, restruct=None, holiday_interest_tenor=None, holiday_principal_due_on=None, holiday_fine_tenor=None, tariff_code=None, principal_decimal_rounding=None, interest_decimal_rounding=None, group_id=None, catalog_status=None, principal_provision_rate0=None, principal_provision_rate1=None, principal_provision_rate2=None, principal_provision_rate3=None, principal_provision_rate4=None, interest_provision_rate0=None, interest_provision_rate1=None, interest_provision_rate2=None, interest_provision_rate3=None, interest_provision_rate4=None, subproduct=None):
        if not catalog_code:
            catalog_code = ''
        if not catalog_name:
            catalog_name = ''
        if not currency_code:
            currency_code = ''
        if not secure_currency_code:
            secure_currency_code = ''
        if not credit_type:
            credit_type = ''
        if not tenor_type:
            tenor_type = ''
        if not is_syndicated:
            is_syndicated = ''
        if not interest_computation_mode:
            interest_computation_mode = ''
        if not secure_type:
            secure_type = ''
        if not secure_rate:
            secure_rate = 0
        if not principal_tenor:
            principal_tenor = 0
        if not principal_tenor_unit:
            principal_tenor_unit = ''
        if not interest_tenor:
            interest_tenor = 0
        if not interest_tenor_unit:
            interest_tenor_unit = ''
        if not fine_tenor:
            fine_tenor = 0
        if not fine_tenor_unit:
            fine_tenor_unit = ''
        if not credit_purpose:
            credit_purpose = ''
        if not credit_classification:
            credit_classification = ''
        if not credit_facility:
            credit_facility = ''
        if not discount_rate:
            discount_rate = 0
        if not re_discount_rate:
            re_discount_rate = 0
        if not disbursement_mode:
            disbursement_mode = ''
        if not principal_grace_period:
            principal_grace_period = 0
        if not interest_grace_period:
            interest_grace_period = 0
        if not fine_grace_period:
            fine_grace_period = 0
        if not is_provision:
            is_provision = ''
        if not provision_tenor:
            provision_tenor = 0
        if not provision_tenor_unit:
            provision_tenor_unit = ''
        if not rollover_option:
            rollover_option = ''
        if not restruct:
            restruct = ''
        if not holiday_interest_tenor:
            holiday_interest_tenor = 0
        if not holiday_principal_due_on:
            holiday_principal_due_on = 0
        if not holiday_fine_tenor:
            holiday_fine_tenor = 0
        if not tariff_code:
            tariff_code = 0
        if not principal_decimal_rounding:
            principal_decimal_rounding = 0
        if not interest_decimal_rounding:
            interest_decimal_rounding = 0
        if not group_id:
            group_id = 0
        if not catalog_status:
            catalog_status = ''
        if not principal_provision_rate0:
            principal_provision_rate0 = 0
        if not principal_provision_rate1:
            principal_provision_rate1 = 0
        if not principal_provision_rate2:
            principal_provision_rate2 = 0
        if not principal_provision_rate3:
            principal_provision_rate3 = 0
        if not principal_provision_rate4:
            principal_provision_rate4 = 0
        if not interest_provision_rate0:
            interest_provision_rate0 = 0
        if not interest_provision_rate1:
            interest_provision_rate1 = 0
        if not interest_provision_rate2:
            interest_provision_rate2 = 0
        if not interest_provision_rate3:
            interest_provision_rate3 = 0
        if not interest_provision_rate4:
            interest_provision_rate4 = 0
        if not subproduct:
            subproduct = ''
        payload = {
            "catalog_code": catalog_code,
            "catalog_name": catalog_name,
            "currency_code": currency_code,
            "secure_currency_code": secure_currency_code,
            "credit_type": credit_type,
            "tenor_type": tenor_type,
            "is_syndicated": is_syndicated,
            "interest_computation_mode": interest_computation_mode,
            "secure_type": secure_type,
            "secure_rate": secure_rate,
            "principal_tenor": principal_tenor,
            "principal_tenor_unit": principal_tenor_unit,
            "interest_tenor": interest_tenor,
            "interest_tenor_unit": interest_tenor_unit,
            "fine_tenor": fine_tenor,
            "fine_tenor_unit": fine_tenor_unit,
            "credit_purpose": credit_purpose,
            "credit_classification": credit_classification,
            "credit_facility": credit_facility,
            "discount_rate": discount_rate,
            "re_discount_rate": re_discount_rate,
            "disbursement_mode": disbursement_mode,
            "principal_grace_period": principal_grace_period,
            "interest_grace_period": interest_grace_period,
            "fine_grace_period": fine_grace_period,
            "is_provision": is_provision,
            "provision_tenor": provision_tenor,
            "provision_tenor_unit": provision_tenor_unit,
            "rollover_option": rollover_option,
            "restruct": restruct,
            "holiday_interest_tenor": holiday_interest_tenor,
            "holiday_principal_due_on": holiday_principal_due_on,
            "holiday_fine_tenor": holiday_fine_tenor,
            "tariff_code": tariff_code,
            "principal_decimal_rounding": principal_decimal_rounding,
            "interest_decimal_rounding": interest_decimal_rounding,
            "group_id": group_id,
            "catalog_status": catalog_status,
            "principal_provision_rate0": principal_provision_rate0,
            "principal_provision_rate1": principal_provision_rate1,
            "principal_provision_rate2": principal_provision_rate2,
            "principal_provision_rate3": principal_provision_rate3,
            "principal_provision_rate4": principal_provision_rate4,
            "interest_provision_rate0": interest_provision_rate0,
            "interest_provision_rate1": interest_provision_rate1,
            "interest_provision_rate2": interest_provision_rate2,
            "interest_provision_rate3": interest_provision_rate3,
            "interest_provision_rate4": interest_provision_rate4,
            "subproduct": subproduct
        }
        return payload

    def update(self, id=None, catalog_name=None, currency_code=None, secure_currency_code=None, credit_type=None, tenor_type=None, is_syndicated=None, interest_computation_mode=None, secure_type=None, secure_rate=None, principal_tenor=None, principal_tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, fine_tenor=None, fine_tenor_unit=None, credit_purpose=None, credit_classification=None, credit_facility=None, discount_rate=None, re_discount_rate=None, disbursement_mode=None, principal_grace_period=None, interest_grace_period=None, fine_grace_period=None, is_provision=None, provision_tenor=None, provision_tenor_unit=None, rollover_option=None, restruct=None, holiday_interest_tenor=None, holiday_principal_due_on=None, holiday_fine_tenor=None, tariff_code=None, principal_decimal_rounding=None, interest_decimal_rounding=None, group_id=None, catalog_status=None, principal_provision_rate0=None, principal_provision_rate1=None, principal_provision_rate2=None, principal_provision_rate3=None, principal_provision_rate4=None, interest_provision_rate0=None, interest_provision_rate1=None, interest_provision_rate2=None, interest_provision_rate3=None, interest_provision_rate4=None, subproduct=None):
        if not id:
            id = 0
        if not catalog_name:
            catalog_name = ''
        if not currency_code:
            currency_code = ''
        if not secure_currency_code:
            secure_currency_code = ''
        if not credit_type:
            credit_type = ''
        if not tenor_type:
            tenor_type = ''
        if not is_syndicated:
            is_syndicated = ''
        if not interest_computation_mode:
            interest_computation_mode = ''
        if not secure_type:
            secure_type = ''
        if not secure_rate:
            secure_rate = 0
        if not principal_tenor:
            principal_tenor = 0
        if not principal_tenor_unit:
            principal_tenor_unit = ''
        if not interest_tenor:
            interest_tenor = 0
        if not interest_tenor_unit:
            interest_tenor_unit = ''
        if not fine_tenor:
            fine_tenor = 0
        if not fine_tenor_unit:
            fine_tenor_unit = ''
        if not credit_purpose:
            credit_purpose = ''
        if not credit_classification:
            credit_classification = ''
        if not credit_facility:
            credit_facility = ''
        if not discount_rate:
            discount_rate = 0
        if not re_discount_rate:
            re_discount_rate = 0
        if not disbursement_mode:
            disbursement_mode = ''
        if not principal_grace_period:
            principal_grace_period = 0
        if not interest_grace_period:
            interest_grace_period = 0
        if not fine_grace_period:
            fine_grace_period = 0
        if not is_provision:
            is_provision = ''
        if not provision_tenor:
            provision_tenor = 0
        if not provision_tenor_unit:
            provision_tenor_unit = ''
        if not rollover_option:
            rollover_option = ''
        if not restruct:
            restruct = ''
        if not holiday_interest_tenor:
            holiday_interest_tenor = 0
        if not holiday_principal_due_on:
            holiday_principal_due_on = 0
        if not holiday_fine_tenor:
            holiday_fine_tenor = 0
        if not tariff_code:
            tariff_code = 0
        if not principal_decimal_rounding:
            principal_decimal_rounding = 0
        if not interest_decimal_rounding:
            interest_decimal_rounding = 0
        if not group_id:
            group_id = 0
        if not catalog_status:
            catalog_status = ''
        if not principal_provision_rate0:
            principal_provision_rate0 = 0
        if not principal_provision_rate1:
            principal_provision_rate1 = 0
        if not principal_provision_rate2:
            principal_provision_rate2 = 0
        if not principal_provision_rate3:
            principal_provision_rate3 = 0
        if not principal_provision_rate4:
            principal_provision_rate4 = 0
        if not interest_provision_rate0:
            interest_provision_rate0 = 0
        if not interest_provision_rate1:
            interest_provision_rate1 = 0
        if not interest_provision_rate2:
            interest_provision_rate2 = 0
        if not interest_provision_rate3:
            interest_provision_rate3 = 0
        if not interest_provision_rate4:
            interest_provision_rate4 = 0
        if not subproduct:
            subproduct = ''
        payload = {
            "id": id,
            "catalog_name": catalog_name,
            "currency_code": currency_code,
            "secure_currency_code": secure_currency_code,
            "credit_type": credit_type,
            "tenor_type": tenor_type,
            "is_syndicated": is_syndicated,
            "interest_computation_mode": interest_computation_mode,
            "secure_type": secure_type,
            "secure_rate": secure_rate,
            "principal_tenor": principal_tenor,
            "principal_tenor_unit": principal_tenor_unit,
            "interest_tenor": interest_tenor,
            "interest_tenor_unit": interest_tenor_unit,
            "fine_tenor": fine_tenor,
            "fine_tenor_unit": fine_tenor_unit,
            "credit_purpose": credit_purpose,
            "credit_classification": credit_classification,
            "credit_facility": credit_facility,
            "discount_rate": discount_rate,
            "re_discount_rate": re_discount_rate,
            "disbursement_mode": disbursement_mode,
            "principal_grace_period": principal_grace_period,
            "interest_grace_period": interest_grace_period,
            "fine_grace_period": fine_grace_period,
            "is_provision": is_provision,
            "provision_tenor": provision_tenor,
            "provision_tenor_unit": provision_tenor_unit,
            "rollover_option": rollover_option,
            "restruct": restruct,
            "holiday_interest_tenor": holiday_interest_tenor,
            "holiday_principal_due_on": holiday_principal_due_on,
            "holiday_fine_tenor": holiday_fine_tenor,
            "tariff_code": tariff_code,
            "principal_decimal_rounding": principal_decimal_rounding,
            "interest_decimal_rounding": interest_decimal_rounding,
            "group_id": group_id,
            "catalog_status": catalog_status,
            "principal_provision_rate0": principal_provision_rate0,
            "principal_provision_rate1": principal_provision_rate1,
            "principal_provision_rate2": principal_provision_rate2,
            "principal_provision_rate3": principal_provision_rate3,
            "principal_provision_rate4": principal_provision_rate4,
            "interest_provision_rate0": interest_provision_rate0,
            "interest_provision_rate1": interest_provision_rate1,
            "interest_provision_rate2": interest_provision_rate2,
            "interest_provision_rate3": interest_provision_rate3,
            "interest_provision_rate4": interest_provision_rate4,
            "subproduct": subproduct
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload