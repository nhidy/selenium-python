from datetime import datetime

class CreditAccountPayload(object):
    def view(self, id=None):
        if not id:
            id = ''
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

    def advanced_search(self, def_account_number=None, account_number=None, account_name=None, currency_code=None, customer_code=None, catalog_code=None, credit_type=None, tenor_type=None, credit_status=None, reference_number=None, sub_product_limit_code=None, page_index=None, page_size=None):
        if not def_account_number:
            def_account_number = ''
        if not account_number:
            account_number = ''
        if not account_name:
            account_name = ''
        if not currency_code:
            currency_code = ''
        if not customer_code:
            customer_code = ''
        if not catalog_code:
            catalog_code = ''
        if not credit_type:
            credit_type = ''
        if not tenor_type:
            tenor_type = ''
        if not credit_status:
            credit_status = None
        if not reference_number:
            reference_number = ''
        if not sub_product_limit_code:
            sub_product_limit_code = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "def_account_number": def_account_number,
            "account_number": account_number,
            "account_name": account_name,
            "currency_code": currency_code,
            "customer_code": customer_code,
            "catalog_code": catalog_code,
            "credit_type": credit_type,
            "tenor_type": tenor_type,
            "credit_status": credit_status,
            "reference_number": reference_number,
            "sub_product_limit_code": sub_product_limit_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, account_number=None, dpt_account_number=None, ctmtype=None, customerid=None, splcd=None, branchid=None, catalogue_code=None, catalogue_name=None, credit_facility=None, sub_product=None, crdcls=None, seqnumber=None, ccrcd=None, acname=None, maximumlimit=None, crlimit=None, margin=None, frdt=None, todt=None, pfstdt=None, intfstdt=None, amount=None, exchangerate=None, desc=None, prtnun=None, isiccd=None, apuser=None, pod=None):
        if not account_number:
            account_number = ''
        if not dpt_account_number:
            dpt_account_number = ''
        if not ctmtype:
            ctmtype = ''
        if not customerid:
            customerid = 0
        if not splcd:
            splcd = ''
        if not branchid:
            branchid = ''
        if not catalogue_code:
            catalogue_code = ''
        if not catalogue_name:
            catalogue_name = ''
        if not credit_facility:
            credit_facility = ''
        if not sub_product:
            sub_product = ''
        if not crdcls:
            crdcls = ''
        if not seqnumber:
            seqnumber = ''
        if not ccrcd:
            ccrcd = ''
        if not acname:
            acname = ''
        if not maximumlimit:
            maximumlimit = 0
        if not crlimit:
            crlimit = 0
        if not margin:
            margin = 0
        if not frdt:
            frdt = ''
        if not todt:
            todt = ''
        if not pfstdt:
            pfstdt = ''
        if not intfstdt:
            intfstdt = ''
        if not amount:
            amount = 0
        if not exchangerate:
            exchangerate = 0
        if not desc:
            desc = ''
        if not prtnun:
            prtnun = ''
        if not isiccd:
            isiccd = ''
        if not apuser:
            apuser = 0
        if not pod:
            pod = ''
        payload = {
            "account_number": account_number,
            "dpt_account_number": dpt_account_number,
            "ctmtype": ctmtype,
            "customerid": customerid,
            "splcd": splcd,
            "branchid": branchid,
            "catalogue_code": catalogue_code,
            "catalogue_name": catalogue_name,
            "credit_facility": credit_facility,
            "sub_product": sub_product,
            "crdcls": crdcls,
            "seqnumber": seqnumber,
            "ccrcd": ccrcd,
            "acname": acname,
            "maximumlimit": maximumlimit,
            "crlimit": crlimit,
            "margin": margin,
            "frdt": frdt,
            "todt": todt,
            "pfstdt": pfstdt,
            "intfstdt": intfstdt,
            "amount": amount,
            "exchangerate": exchangerate,
            "desc": desc,
            "prtnun": prtnun,
            "isiccd": isiccd,
            "apuser": apuser,
            "pod": pod
        }
        return payload

    def update(self, id=None, account_name=None, secure_type=None, secure_rate=None, principal_tenor=None, principal_tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, credit_purpose=None, disbursement_mode=None, is_provision=None, provision_tenor=None, provision_tenor_unit=None, restruct=None, limit_from_third_party=None, operative_limit_from_third_party=None, interest_first_date=None, from_date=None, to_date=None, ranking_status=None, staff_id=None, remark=None, reference_number=None, is_restructured=None, principal_provision_rate_0=None, principal_provision_rate_1=None, principal_provision_rate_2=None, principal_provision_rate_3=None, principal_provision_rate_4=None, interest_provision_rate_0=None, interest_provision_rate_1=None, interest_provision_rate_2=None, interest_provision_rate_3=None, interest_provision_rate_4=None, business_purpose_code=None, provision_of_other=None, fine_tenor=None, fine_tenor_unit=None, principal_grace_period=None, holiday_principal_due_on=None, interest_grace_period=None, holiday_interest_tenor=None, fine_grace_period=None, holiday_fine_tenor=None, discount_rate=None, re_discount_rate=None, approve_modify=None, account_number_def=None, module_code=None, list_ifc_balance=None, payment_list=None, principal_list=None):
        if not id:
            id = 0
        if not account_name:
            account_name = ''
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
        if not credit_purpose:
            credit_purpose = ''
        if not disbursement_mode:
            disbursement_mode = ''
        if not is_provision:
            is_provision = ''
        if not provision_tenor:
            provision_tenor = None
        if not provision_tenor_unit:
            provision_tenor_unit = None
        if not restruct:
            restruct = ''
        if not limit_from_third_party:
            limit_from_third_party = 0
        if not operative_limit_from_third_party:
            operative_limit_from_third_party = 0
        if not interest_first_date:
            interest_first_date = ''
        if not from_date:
            from_date = ''
        if not to_date:
            to_date = ''
        if not ranking_status:
            ranking_status = ''
        if not staff_id:
            staff_id = 0
        if not remark:
            remark = ''
        if not reference_number:
            reference_number = ''
        if not is_restructured:
            is_restructured = ''
        if not principal_provision_rate_0:
            principal_provision_rate_0 = 0
        if not principal_provision_rate_1:
            principal_provision_rate_1 = 0
        if not principal_provision_rate_2:
            principal_provision_rate_2 = 0
        if not principal_provision_rate_3:
            principal_provision_rate_3 = 0
        if not principal_provision_rate_4:
            principal_provision_rate_4 = 0
        if not interest_provision_rate_0:
            interest_provision_rate_0 = 0
        if not interest_provision_rate_1:
            interest_provision_rate_1 = 0
        if not interest_provision_rate_2:
            interest_provision_rate_2 = 0
        if not interest_provision_rate_3:
            interest_provision_rate_3 = 0
        if not interest_provision_rate_4:
            interest_provision_rate_4 = 0
        if not business_purpose_code:
            business_purpose_code = ''
        if not provision_of_other:
            provision_of_other = None
        if not fine_tenor:
            fine_tenor = 0
        if not fine_tenor_unit:
            fine_tenor_unit = ''
        if not principal_grace_period:
            principal_grace_period = 0
        if not holiday_principal_due_on:
            holiday_principal_due_on = 0
        if not interest_grace_period:
            interest_grace_period = 0
        if not holiday_interest_tenor:
            holiday_interest_tenor = 0
        if not fine_grace_period:
            fine_grace_period = 0
        if not holiday_fine_tenor:
            holiday_fine_tenor = 0
        if not discount_rate:
            discount_rate = 0
        if not re_discount_rate:
            re_discount_rate = 0
        if not approve_modify:
            approve_modify = True
        if not account_number_def:
            account_number_def = ''
        if not module_code:
            module_code = ''
        if not list_ifc_balance:
            list_ifc_balance = ''
        if not payment_list:
            payment_list = ''
        if not principal_list:
            principal_list = ''
        payload = {
            "id": id,
            "account_name": account_name,
            "secure_type": secure_type,
            "secure_rate": secure_rate,
            "principal_tenor": principal_tenor,
            "principal_tenor_unit": principal_tenor_unit,
            "interest_tenor": interest_tenor,
            "interest_tenor_unit": interest_tenor_unit,
            "credit_purpose": credit_purpose,
            "disbursement_mode": disbursement_mode,
            "is_provision": is_provision,
            "provision_tenor": provision_tenor,
            "provision_tenor_unit": provision_tenor_unit,
            "restruct": restruct,
            "limit_from_third_party": limit_from_third_party,
            "operative_limit_from_third_party": operative_limit_from_third_party,
            "interest_first_date": interest_first_date,
            "from_date": from_date,
            "to_date": to_date,
            "ranking_status": ranking_status,
            "staff_id": staff_id,
            "remark": remark,
            "reference_number": reference_number,
            "is_restructured": is_restructured,
            "principal_provision_rate_0": principal_provision_rate_0,
            "principal_provision_rate_1": principal_provision_rate_1,
            "principal_provision_rate_2": principal_provision_rate_2,
            "principal_provision_rate_3": principal_provision_rate_3,
            "principal_provision_rate_4": principal_provision_rate_4,
            "interest_provision_rate_0": interest_provision_rate_0,
            "interest_provision_rate_1": interest_provision_rate_1,
            "interest_provision_rate_2": interest_provision_rate_2,
            "interest_provision_rate_3": interest_provision_rate_3,
            "interest_provision_rate_4": interest_provision_rate_4,
            "business_purpose_code": business_purpose_code,
            "provision_of_other": provision_of_other,
            "fine_tenor": fine_tenor,
            "fine_tenor_unit": fine_tenor_unit,
            "principal_grace_period": principal_grace_period,
            "holiday_principal_due_on": holiday_principal_due_on,
            "interest_grace_period": interest_grace_period,
            "holiday_interest_tenor": holiday_interest_tenor,
            "fine_grace_period": fine_grace_period,
            "holiday_fine_tenor": holiday_fine_tenor,
            "discount_rate": discount_rate,
            "re_discount_rate": re_discount_rate,
            "approve_modify": approve_modify,
            "account_number_def": account_number_def,
            "module_code": module_code,
            "list_ifc_balance": list_ifc_balance,
            "payment_list": payment_list,
            "principal_list": principal_list
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload