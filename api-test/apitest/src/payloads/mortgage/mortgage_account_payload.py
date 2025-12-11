class MortgageAccountPayload(object):
    def update(self, id=None, account_name=None, cc_contract=None, collateral_rate=None, risk_allocation_rate=None, was_register_at_collateral_center=None, security_paper_type=None, security_paper_number=None, name_of_title=None, house_no=None, plot_no=None, holding_no=None, ward_no=None, block_no=None, area=None, street=None, town_ship=None, division_city=None, location=None, province_legal=None, district_legal=None, sub_district_legal=None, village_legal=None, address_in_combodia_legal=None, address_legal=None, zip_code_legal=None, province_local=None, district_local=None, sub_district_local=None, village_local=None, address_in_combodia_local=None, address_local=None, zip_code_local=None, evaluate_by=None, evaluate_method=None, evaluate_date=None, new_evaluate_date=None, insurance=None, paper_type=None, paper_number=None, market_value=None, cc_amount=None, other_counter_party_collateral_amount=None, other_counter_party_collateral_released=None, sum_insurance_amount=None, premium_amount=None, original_amount=None, remark=None, reference_number=None, owner=None, user_define1=None, user_define2=None, user_define3=None, user_define4=None, user_define5=None, policy_number=None, expiry_date=None, policy_amount=None, company_issues_policy=None):
        if not id:
            id = ''
        if not account_name:
            account_name = ''
        if not cc_contract:
            cc_contract = ''
        if not collateral_rate:
            collateral_rate = None
        if not risk_allocation_rate:
            risk_allocation_rate = 0
        if not was_register_at_collateral_center:
            was_register_at_collateral_center = ''
        if not security_paper_type:
            security_paper_type = ''
        if not security_paper_number:
            security_paper_number = ''
        if not name_of_title:
            name_of_title = ''
        if not house_no:
            house_no = ''
        if not plot_no:
            plot_no = ''
        if not holding_no:
            holding_no = ''
        if not ward_no:
            ward_no = ''
        if not block_no:
            block_no = ''
        if not area:
            area = ''
        if not street:
            street = ''
        if not town_ship:
            town_ship = ''
        if not division_city:
            division_city = ''
        if not location:
            location = ''
        if not province_legal:
            province_legal = ''
        if not district_legal:
            district_legal = ''
        if not sub_district_legal:
            sub_district_legal = ''
        if not village_legal:
            village_legal = ''
        if not address_in_combodia_legal:
            address_in_combodia_legal = ''
        if not address_legal:
            address_legal = ''
        if not zip_code_legal:
            zip_code_legal = ''
        if not province_local:
            province_local = ''
        if not district_local:
            district_local = ''
        if not sub_district_local:
            sub_district_local = ''
        if not village_local:
            village_local = ''
        if not address_in_combodia_local:
            address_in_combodia_local = ''
        if not address_local:
            address_local = ''
        if not zip_code_local:
            zip_code_local = ''
        if not evaluate_by:
            evaluate_by = ''
        if not evaluate_method:
            evaluate_method = ''
        if not evaluate_date:
            evaluate_date = ''
        if not new_evaluate_date:
            new_evaluate_date = ''
        if not insurance:
            insurance = ''
        if not paper_type:
            paper_type = ''
        if not paper_number:
            paper_number = ''
        if not market_value:
            market_value = None
        if not cc_amount:
            cc_amount = None
        if not other_counter_party_collateral_amount:
            other_counter_party_collateral_amount = 0
        if not other_counter_party_collateral_released:
            other_counter_party_collateral_released = 0
        if not sum_insurance_amount:
            sum_insurance_amount = 0
        if not premium_amount:
            premium_amount = 0
        if not original_amount:
            original_amount = 0
        if not remark:
            remark = ''
        if not reference_number:
            reference_number = ''
        if not owner:
            owner = ''
        if not user_define1:
            user_define1 = ''
        if not user_define2:
            user_define2 = ''
        if not user_define3:
            user_define3 = ''
        if not user_define4:
            user_define4 = ''
        if not user_define5:
            user_define5 = ''
        if not policy_number:
            policy_number = ''
        if not expiry_date:
            expiry_date = ''
        if not policy_amount:
            policy_amount = None
        if not company_issues_policy:
            company_issues_policy = ''

        payload = {
            "id": id,
            "account_name": account_name,
            "cc_contract": cc_contract,
            "collateral_rate": collateral_rate,
            "risk_allocation_rate": risk_allocation_rate,
            "was_register_at_collateral_center": was_register_at_collateral_center,
            "security_paper_type": security_paper_type,
            "security_paper_number": security_paper_number,
            "other_address": {
                "name_of_title": name_of_title,
                "house_no": house_no,
                "plot_no": plot_no,
                "holding_no": holding_no,
                "ward_no": ward_no,
                "block_no": block_no,
                "area": area,
                "street": street,
                "town_ship": town_ship,
                "division_city": division_city
            },
            "location": location,
            "legal_local_address": {
                "province": province_legal,
                "district": district_legal,
                "sub_district": sub_district_legal,
                "village": village_legal,
                "address_in_combodia": address_in_combodia_legal,
                "address": address_legal,
                "zip_code": zip_code_legal
            },
            "local_address": {
                "province": province_local,
                "district": district_local,
                "sub_district": sub_district_local,
                "village": village_local,
                "address_in_combodia": address_in_combodia_local,
                "address": address_local,
                "zip_code": zip_code_local
            },
            "evaluate_by": evaluate_by,
            "evaluate_method": evaluate_method,
            "evaluate_date": evaluate_date,
            "new_evaluate_date": new_evaluate_date,
            "insurance": insurance,
            "other_paper_data": {
                "paper_type": paper_type,
                "paper_number": paper_number
            },
            "market_value": market_value,
            "cc_amount": cc_amount,
            "other_counter_party_collateral_amount": other_counter_party_collateral_amount,
            "other_counter_party_collateral_released": other_counter_party_collateral_released,
            "sum_insurance_amount": sum_insurance_amount,
            "premium_amount": premium_amount,
            "original_amount": original_amount,
            "remark": remark,
            "reference_number": reference_number,
            "owner": owner,
            "user_define1": user_define1,
            "user_define2": user_define2,
            "user_define3": user_define3,
            "user_define4": user_define4,
            "user_define5": user_define5,
            "policy_number": policy_number,
            "expiry_date": expiry_date,
            "policy_amount": policy_amount,
            "company_issues_policy": company_issues_policy
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

    def advanced_search(self, account_number=None, account_name=None, currency_code=None, customer_code=None, catalog_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_account_status=None, reference_number=None, page_index=None, page_size=None):
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
        if not collateral_asset_type:
            collateral_asset_type = ''
        if not collateral_asset_classification:
            collateral_asset_classification = ''
        if not collateral_account_status:
            collateral_account_status = ''
        if not reference_number:
            reference_number = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "account_number": account_number,
            "account_name": account_name,
            "currency_code": currency_code,
            "customer_code": customer_code,
            "catalog_code": catalog_code,
            "collateral_asset_type": collateral_asset_type,
            "collateral_asset_classification": collateral_asset_classification,
            "collateral_account_status": collateral_account_status,
            "reference_number": reference_number,
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