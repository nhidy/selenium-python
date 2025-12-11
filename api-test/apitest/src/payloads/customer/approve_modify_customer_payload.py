from datetime import datetime

class ApproveModifyCustomerPayload(object):
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

    def view_user_modify_customer(self, customer_code=None):
        if not customer_code:
            customer_code = ''
        payload = {
            "customer_code": customer_code
        }
        return payload

    def view_info_modify_customer(self, transaction_id=None, customer_code=None):
        if not transaction_id:
            transaction_id = ''
        if not customer_code:
            customer_code = ''
        payload = {
            "transaction_id": transaction_id,
            "customer_code": customer_code
        }
        return payload

    def approve_info_modify_customer(self, transaction_id=None, customer_code=None):
        if not transaction_id:
            transaction_id = ''
        if not customer_code:
            customer_code = ''
        payload = {
            "transaction_id": transaction_id,
            "customer_code": customer_code
        }
        return payload

    def reject_info_modify_customer(self, transaction_id=None, customer_code=None):
        if not transaction_id:
            transaction_id = ''
        if not customer_code:
            customer_code = ''
        payload = {
            "transaction_id": transaction_id,
            "customer_code": customer_code
        }
        return payload