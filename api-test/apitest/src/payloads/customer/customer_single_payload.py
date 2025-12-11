from datetime import datetime

class CustomerSinglePayload(object):
    def view(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload

    def view_by_customer_code(self, customer_code=None):
        if not customer_code:
            customer_code = ''
        payload = {
            "customer_code": customer_code
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
            "page_index": page_index,
        }
        return payload

    def get_list_relation_customer(self, group_code=None, page_size=None, page_index=None):
        if not group_code:
            group_code = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "group_code": group_code,
            "page_size": page_size,
            "page_index": page_index,
        }
        return payload

    def get_list_deposit_by_customer_id(self, customer_id=None, page_size=None, page_index=None):
        if not customer_id:
            customer_id = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "customer_id": customer_id,
            "page_size": page_size,
            "page_index": page_index,
        }
        return payload

    def get_list_credit_by_customer_id(self, customer_id=None, page_size=None, page_index=None):
        if not customer_id:
            customer_id = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "customer_id": customer_id,
            "page_size": page_size,
            "page_index": page_index,
        }
        return payload

    def get_list_detail_customer_code(self, customer_code=None, page_size=None, page_index=None):
        if not customer_code:
            customer_code = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "customer_code": customer_code,
            "page_size": page_size,
            "page_index": page_index,
        }
        return payload

    def lookup_customer_single(self, customer_code=None, fullname=None, shortname=None, paper_number=None, dob_from=None, dob_to=None, gender=None, customer_status=None, nation=None, resident=None, address=None, old_id_of_customer=None, group_id=None, page_index=None, page_size=None):
        if not customer_code:
            customer_code = ''
        if not fullname:
            fullname = ''
        if not shortname:
            shortname = ''
        if not paper_number:
            paper_number = ''
        if not dob_from:
            dob_from = None
        if not dob_to:
            dob_to = None
        if not gender:
            gender = ''
        if not customer_status:
            customer_status = ''
        if not nation:
            nation = ''
        if not resident:
            resident = ''
        if not address:
            address = ''
        if not old_id_of_customer:
            old_id_of_customer = ''
        if not group_id:
            group_id = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "customer_code": customer_code,
            "fullname": fullname,
            "shortname": shortname,
            "paper_number": paper_number,
            "dob_from": dob_from,
            "dob_to": dob_to,
            "gender": gender,
            "customer_status": customer_status,
            "nation": nation,
            "resident": resident,
            "address": address,
            "old_id_of_customer": old_id_of_customer,
            "group_id": group_id,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def advanced_search(self, customer_code=None, fullname=None, shortname=None, paper_number=None, dob_from=None, dob_to=None, gender=None, customer_status=None, nation=None, resident=None, address=None, old_id_of_customer=None, group_id=None, page_index=None, page_size=None):
        if not customer_code:
            customer_code = ''
        if not fullname:
            fullname = ''
        if not shortname:
            shortname = ''
        if not paper_number:
            paper_number = ''
        if not dob_from:
            dob_from = None
        if not dob_to:
            dob_to = None
        if not gender:
            gender = ''
        if not customer_status:
            customer_status = ''
        if not nation:
            nation = ''
        if not resident:
            resident = ''
        if not address:
            address = ''
        if not old_id_of_customer:
            old_id_of_customer = ''
        if not group_id:
            group_id = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "customer_code": customer_code,
            "fullname": fullname,
            "shortname": shortname,
            "paper_number": paper_number,
            "dob_from": dob_from,
            "dob_to": dob_to,
            "gender": gender,
            "customer_status": customer_status,
            "nation": nation,
            "resident": resident,
            "address": address,
            "old_id_of_customer": old_id_of_customer,
            "group_id": group_id,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def add(self, hocifcd=None, customer_private=None, title=None, title_of_organization=None, suffix=None, firstname=None, lastname=None, midname=None, fullname=None, firstname_local=None, lastname_local=None, midname_local=None, shortname=None, gender=None, date_of_birth=None, place_of_birth=None, nation=None, country=None, paper_type=None, paper_number=None, issue_date_of_paper=None, issue_place_of_paper=None, expire_date_of_paper=None, paper_type_sub=None, paper_number_sub=None, issue_date_of_sub_paper=None, issue_place_of_sub_paper=None, customer_group_type=None, customer_sub_group_type=None, categories=None, sector=None, subsector=None, resident=None, line1=None, line2=None, line3=None, line4=None, line5=None, phone_home=None, phone_mobile=None, email=None, education=None, marital_status=None, profession=None, business_type=None, financial=None, isic_code=None, managing_branch_code=None, customer_status=None, classify=None, polists=None, repolists=None, country_of_income=None, fatca_status=None, government_id=None, international_id=None, oversea_juristic_id=None, gfmis_code=None, branch_code=None, group_code=None, customer_credit_line=None, currency_code=None, customer_type=None, primary_cif=None, mdm_amount_status=None, mdm_request_status=None, mdm_list_sub_type_code=None, mdm_list_sub_type_desc=None, mdm_matching_by=None, mdm_final_kyc_status=None, mdm_kyc_comment_code=None, mdm_kyc_comment_desc=None, kyc_level=None, kyc_update_date=None, customer_size=None, name_1=None, account_no_1=None, name_2=None, account_no_2=None, customer_sub_type=None, father_name=None):
        payload = {
            "hocifcd": hocifcd,
            "customer_private": customer_private,
            "title": title,
            "title_of_organization": title_of_organization,
            "suffix": suffix,
            "firstname": firstname,
            "lastname": lastname,
            "midname": midname,
            "fullname": fullname,
            "firstname_local": firstname_local,
            "lastname_local": lastname_local,
            "midname_local": midname_local,
            "shortname": shortname,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "place_of_birth": place_of_birth,
            "nation": nation,
            "country": country,
            "paper_type": paper_type,
            "paper_number": paper_number,
            "issue_date_of_paper": issue_date_of_paper,
            "issue_place_of_paper": issue_place_of_paper,
            "expire_date_of_paper": expire_date_of_paper,
            "paper_type_sub": paper_type_sub,
            "paper_number_sub": paper_number_sub,
            "issue_date_of_sub_paper": issue_date_of_sub_paper,
            "issue_place_of_sub_paper": issue_place_of_sub_paper,
            "customer_group_type": customer_group_type,
            "customer_sub_group_type": customer_sub_group_type,
            "categories": categories,
            "sector": sector,
            "subsector": subsector,
            "resident": resident,
            "legal_local_address": {},
            "contact_local_address": {
                "line1": line1,
                "line2": line2,
                "line3": line3,
                "line4": line4,
                "line5": line5
            },
            "normal_local_address": {},
            "phone_home": phone_home,
            "phone_mobile": phone_mobile,
            "email": email,
            "education": education,
            "marital_status": marital_status,
            "profession": profession,
            "business_type": business_type,
            "financial": financial,
            "isic_code": isic_code,
            "managing_branch_code": managing_branch_code,
            "customer_status": customer_status,
            "classify": classify,
            "polists": polists,
            "repolists": repolists,
            "country_of_income": country_of_income,
            "fatca_status": fatca_status,
            "government_id": government_id,
            "international_id": international_id,
            "oversea_juristic_id": oversea_juristic_id,
            "gfmis_code": gfmis_code,
            "branch_code": branch_code,
            "group_code": group_code,
            "customer_credit_line": customer_credit_line,
            "currency_code": currency_code,
            "customer_type": customer_type,
            "primary_cif": primary_cif,
            "mdm_amount_status": mdm_amount_status,
            "mdm_request_status": mdm_request_status,
            "mdm_list_sub_type_code": mdm_list_sub_type_code,
            "mdm_list_sub_type_desc": mdm_list_sub_type_desc,
            "mdm_matching_by": mdm_matching_by,
            "mdm_final_kyc_status": mdm_final_kyc_status,
            "mdm_kyc_comment_code": mdm_kyc_comment_code,
            "mdm_kyc_comment_desc": mdm_kyc_comment_desc,
            "kyc_level": kyc_level,
            "kyc_update_date": kyc_update_date,
            "relation_customer_code1": "",
            "relation_customer_code2": "",
            "relation_customer_code3": "",
            "relation_customer_code4": "",
            "relation_customer_code5": "",
            "customer_size": "S",
            "staff_code": "00923",
            "introducer_1": {
                "name": name_1,
                "account_no": account_no_1
            },
            "introducer_2": {
                "name": name_2,
                "account_no": account_no_2
            },
            "customer_sub_type": customer_sub_type,
            "father_name": father_name
        }
        return payload

    def update(self, id=None, hocifcd=None, title=None, title_of_organization=None, suffix=None, firstname=None, lastname=None, midname=None, fullname=None, firstname_local=None, lastname_local=None, midname_local=None, shortname=None, gender=None, date_of_birth=None, place_of_birth=None, nation=None, country=None, paper_type=None, paper_number=None, issue_date_of_paper=None, issue_place_of_paper=None, expire_date_of_paper=None, paper_type_sub=None, paper_number_sub=None, issue_date_of_sub_paper=None, issue_place_of_sub_paper=None, customer_group_type=None, customer_sub_group_type=None, sector=None, subsector=None, resident=None, address_local_legal=None, province_legal=None, village_legal=None, sub_district_legal=None, district_legal=None, address_legal=None, zipcode_legal=None, address_local_contact=None, province_contact=None, village_contact=None, sub_district_contact=None, district_contact=None, address_contact=None, zipcode_contact=None, address_local_normal=None, province_normal=None, village_normal=None, sub_district_normal=None, district_normal=None, address_normal=None, zipcode_normal=None, phone_home=None, phone_mobile=None, email=None, education=None, marital_status=None, profession=None, business_type=None, financial=None, isic_code=None, managing_branch_code=None, classify=None, polists=None, repolists=None, country_of_income=None, fatca_status=None, government_id=None, international_id=None, oversea_juristic_id=None, gfmis_code=None, last_update_date=None, group_id=None, customer_credit_line=None, currency_code=None, customer_type=None, primary_cif=None, mdm_amount_status=None, mdm_request_status=None, mdm_list_sub_type_code=None, mdm_list_sub_type_desc=None, mdm_matching_by=None, mdm_final_kyc_status=None, mdm_kyc_comment_code=None, mdm_kyc_comment_desc=None, kyc_level=None, kyc_update_date=None, kyc_override=None, kyc_override_descr=None, customer_size=None, name_1=None, account_no_1=None, name_2=None, account_no_2=None):
        payload = {
            "id": id,
            "hocifcd": hocifcd,
            "title": title,
            "title_of_organization": title_of_organization,
            "suffix": suffix,
            "firstname": firstname,
            "lastname": lastname,
            "midname": midname,
            "fullname": fullname,
            "firstname_local": firstname_local,
            "lastname_local": lastname_local,
            "midname_local": midname_local,
            "shortname": shortname,
            "gender": gender,
            "date_of_birth": date_of_birth,
            "place_of_birth": place_of_birth,
            "nation": nation,
            "country": country,
            "paper_type": paper_type,
            "paper_number": paper_number,
            "issue_date_of_paper": issue_date_of_paper,
            "issue_place_of_paper": issue_place_of_paper,
            "expire_date_of_paper": expire_date_of_paper,
            "paper_type_sub": paper_type_sub,
            "paper_number_sub": paper_number_sub,
            "issue_date_of_sub_paper": issue_date_of_sub_paper,
            "issue_place_of_sub_paper": issue_place_of_sub_paper,
            "customer_group_type": customer_group_type,
            "customer_sub_group_type": customer_sub_group_type,
            "sector": sector,
            "subsector": subsector,
            "resident": resident,
            "legal_local_address": {
                "address_local": address_local_legal,
                "province": province_legal,
                "village": village_legal,
                "sub_district": sub_district_legal,
                "district": district_legal,
                "address": address_legal,
                "zipcode": zipcode_legal
            },
            "contact_local_address": {
                "address_local": address_local_contact,
                "province": province_contact,
                "village": village_contact,
                "sub_district": sub_district_contact,
                "district": district_contact,
                "address": address_contact,
                "zipcode": zipcode_contact
            },
            "normal_local_address": {
                "address_local": address_local_normal,
                "province": province_normal,
                "village": village_normal,
                "sub_district": sub_district_normal,
                "district": district_normal,
                "address": address_normal,
                "zipcode": zipcode_normal
            },
            "phone_home": phone_home,
            "phone_mobile": phone_mobile,
            "email": email,
            "education": education,
            "marital_status": marital_status,
            "profession": profession,
            "business_type": business_type,
            "financial": financial,
            "isic_code": isic_code,
            "managing_branch_code": managing_branch_code,
            "classify": classify,
            "polists": polists,
            "repolists": repolists,
            "country_of_income": country_of_income,
            "fatca_status": fatca_status,
            "government_id": government_id,
            "international_id": international_id,
            "oversea_juristic_id": oversea_juristic_id,
            "gfmis_code": gfmis_code,
            "last_update_date": last_update_date,
            "group_id": group_id,
            "customer_credit_line": customer_credit_line,
            "currency_code": currency_code,
            "customer_type": customer_type,
            "primary_cif": primary_cif,
            "mdm_amount_status": mdm_amount_status,
            "mdm_request_status": mdm_request_status,
            "mdm_list_sub_type_code": mdm_list_sub_type_code,
            "mdm_list_sub_type_desc": mdm_list_sub_type_desc,
            "mdm_matching_by": mdm_matching_by,
            "mdm_final_kyc_status": mdm_final_kyc_status,
            "mdm_kyc_comment_code": mdm_kyc_comment_code,
            "mdm_kyc_comment_desc": mdm_kyc_comment_desc,
            "kyc_level": kyc_level,
            "kyc_update_date": kyc_update_date,
            "kyc_override": kyc_override,
            "kyc_override_descr": kyc_override_descr,
            "customer_size": "M",
            "introducer_1": {
                "name": name_1,
                "account_no": account_no_1
            },
            "introducer_2": {
                "name": name_2,
                "account_no": account_no_2
            }
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = 0
        payload = {
            "id": id
        }
        return payload