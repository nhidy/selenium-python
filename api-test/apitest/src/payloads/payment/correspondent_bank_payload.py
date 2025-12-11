from datetime import datetime

class CorrespondentBankPayload(object):
    def add(self, bic_code=None, bank_name=None, country=None, city_name=None, address=None, head_office_code=None, branch_code=None, bank_type=None, vostro_account_1=None, vostro_account_2=None, vostro_account_3=None, more_description=None, partner=None, bank_status=None, instruction_bank=None, nostro_account_1=None, nostro_account_2=None, nostro_account_3=None, sending_share_fee_rate=None, recieving_share_fee_rate=None):
        if not bic_code:
            bic_code = ''
        if not bank_name:
            bank_name = ''
        if not country:
            country = ''
        if not city_name:
            city_name = ''
        if not address:
            address = ''
        if not head_office_code:
            head_office_code = ''
        if not branch_code:
            branch_code = ''
        if not bank_type:
            bank_type = ''
        if not vostro_account_1:
            vostro_account_1 = ''
        if not vostro_account_2:
            vostro_account_2 = ''
        if not vostro_account_3:
            vostro_account_3 = ''
        if not more_description:
            more_description = ''
        if not partner:
            partner = ''
        if not bank_status:
            bank_status = ''
        if not instruction_bank:
            instruction_bank = ''
        if not nostro_account_1:
            nostro_account_1 = ''
        if not nostro_account_2:
            nostro_account_2 = ''
        if not nostro_account_3:
            nostro_account_3 = ''
        if not sending_share_fee_rate:
            sending_share_fee_rate = 0
        if not recieving_share_fee_rate:
            recieving_share_fee_rate = 0
        payload = {
            "bic_code": bic_code,
            "bank_name": bank_name,
            "country": country,
            "city_name": city_name,
            "address": address,
            "head_office_code": head_office_code,
            "branch_code": branch_code,
            "bank_type": bank_type,
            "vostro_account": {
                "vostro_account_1": vostro_account_1,
                "vostro_account_2": vostro_account_2,
                "vostro_account_3": vostro_account_3
            },
            "more_description": more_description,
            "partner": partner,
            "bank_status": bank_status,
            "instruction_bank": instruction_bank,
            "nostro_account": {
                "nostro_account_1": nostro_account_1,
                "nostro_account_2": nostro_account_2,
                "nostro_account_3": nostro_account_3
            },
            "sending_share_fee_rate": sending_share_fee_rate,
            "recieving_share_fee_rate": recieving_share_fee_rate
        }
        return payload

    def update(self, id=None, bic_code=None, bank_name=None, country=None, city_name=None, address=None, head_office_code=None, branch_code=None, bank_type=None, vostro_account_1=None, vostro_account_2=None, vostro_account_3=None, more_description=None, partner=None, bank_status=None, instruction_bank=None, nostro_account_1=None, nostro_account_2=None, nostro_account_3=None, sending_share_fee_rate=None, recieving_share_fee_rate=None):
        if not id:
            id = 0
        if not bic_code:
            bic_code = ''
        if not bank_name:
            bank_name = ''
        if not country:
            country = ''
        if not city_name:
            city_name = ''
        if not address:
            address = ''
        if not head_office_code:
            head_office_code = ''
        if not branch_code:
            branch_code = ''
        if not bank_type:
            bank_type = ''
        if not vostro_account_1:
            vostro_account_1 = ''
        if not vostro_account_2:
            vostro_account_2 = ''
        if not vostro_account_3:
            vostro_account_3 = ''
        if not more_description:
            more_description = ''
        if not partner:
            partner = ''
        if not bank_status:
            bank_status = ''
        if not instruction_bank:
            instruction_bank = ''
        if not nostro_account_1:
            nostro_account_1 = ''
        if not nostro_account_2:
            nostro_account_2 = ''
        if not nostro_account_3:
            nostro_account_3 = ''
        if not sending_share_fee_rate:
            sending_share_fee_rate = 0
        if not recieving_share_fee_rate:
            recieving_share_fee_rate = 0
        payload = {
            "id": id,
            "bic_code": bic_code,
            "bank_name": bank_name,
            "country": country,
            "city_name": city_name,
            "address": address,
            "head_office_code": head_office_code,
            "branch_code": branch_code,
            "bank_type": bank_type,
            "vostro_account": {
                "vostro_account_1": vostro_account_1,
                "vostro_account_2": vostro_account_2,
                "vostro_account_3": vostro_account_3
            },
            "more_description": more_description,
            "partner": partner,
            "bank_status": bank_status,
            "instruction_bank": instruction_bank,
            "nostro_account": {
                "nostro_account_1": nostro_account_1,
                "nostro_account_2": nostro_account_2,
                "nostro_account_3": nostro_account_3
            },
            "sending_share_fee_rate": sending_share_fee_rate,
            "recieving_share_fee_rate": recieving_share_fee_rate
        }
        return payload

    def advanced_search(self, bic_code=None, bank_name=None, country=None, bank_type=None, bank_status=None, page_index=None, page_size=None):
        if not bic_code:
            bic_code = ''
        if not bank_name:
            bank_name = ''
        if not country:
            country = ''
        if not bank_type:
            bank_type = ''
        if not bank_status:
            bank_status = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 0
        payload = {
            "bic_code": bic_code,
            "bank_name": bank_name,
            "country": country,
            "bank_type": bank_type,
            "bank_status": bank_status,
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