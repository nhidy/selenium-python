from datetime import datetime

class AccountChartPayload(object):
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

    def advanced_search(self, bank_account_number=None, currency_code=None, account_level_from=None, account_level_to=None, balance_side=None, account_name=None, account_classification=None, account_group=None, page_size=None, page_index=None):
        if not bank_account_number:
            bank_account_number = ''
        if not currency_code:
            currency_code = ''
        if not account_level_from:
            account_level_from = None
        if not account_level_to:
            account_level_to = None
        if not balance_side:
            balance_side = ''
        if not account_name:
            account_name = ''
        if not account_classification:
            account_classification = ''
        if not account_group:
            account_group = ''
        if not page_size:
            page_size = 0
        if not page_index:
            page_index = 0
        payload = {
            "bank_account_number": bank_account_number,
            "currency_code": currency_code,
            "account_level_from": account_level_from,
            "account_level_to": account_level_to,
            "balance_side": balance_side,
            "account_name": account_name,
            "account_classification": account_classification,
            "account_group": account_group,
            "page_size": page_size,
            "page_index": page_index
        }
        return payload

    def add(self, bank_account_number=None, currency_code=None, branch_code=None, account_level=None, balance_side=None, reverse_balance=None, posting_side=None, account_name=None, short_account_name=None, laos_name=None, thai_name=None, khmer_name=None, vietnamese_name=None, account_classification=None, account_categories=None, account_group=None, direct_posting=None, is_visible=None, is_multi_currency=None, job_process_option=None, ref_account_number=None, references_number=None):
        if not bank_account_number:
            bank_account_number = ''
        if not currency_code:
            currency_code = ''
        if not branch_code:
            branch_code = ''
        if not account_level:
            account_level = 0
        if not balance_side:
            balance_side = ''
        if not reverse_balance:
            reverse_balance = ''
        if not posting_side:
            posting_side = ''
        if not account_name:
            account_name = ''
        if not short_account_name:
            short_account_name = ''
        if not laos_name:
            laos_name = ''
        if not thai_name:
            thai_name = ''
        if not khmer_name:
            khmer_name = ''
        if not vietnamese_name:
            vietnamese_name = ''
        if not account_classification:
            account_classification = ''
        if not account_categories:
            account_categories = ''
        if not account_group:
            account_group = ''
        if not direct_posting:
            direct_posting = ''
        if not is_visible:
            is_visible = ''
        if not is_multi_currency:
            is_multi_currency = ''
        if not job_process_option:
            job_process_option = ''
        if not ref_account_number:
            ref_account_number = ''
        if not references_number:
            references_number = ''
        payload = {
            "bank_account_number": bank_account_number,
            "currency_code": currency_code,
            "branch_code": branch_code,
            "account_level": account_level,
            "balance_side": balance_side,
            "reverse_balance": reverse_balance,
            "posting_side": posting_side,
            "account_name": account_name,
            "short_account_name": short_account_name,
            "multi_value_name": {
                "laos_name": laos_name,
                "thai_name": thai_name,
                "khmer_name": khmer_name,
                "vietnamese_name": vietnamese_name
            },
            "account_classification": account_classification,
            "account_categories": account_categories,
            "account_group": account_group,
            "direct_posting": direct_posting,
            "is_visible": is_visible,
            "is_multi_currency": is_multi_currency,
            "job_process_option": job_process_option,
            "ref_account_number": ref_account_number,
            "references_number": references_number
        }
        return payload

    def update(self, id=None, bank_account_number=None, account_name=None, short_account_name=None, laos_name=None, thai_name=None, khmer_name=None, vietnamese_name=None, balance_side=None, reverse_balance=None, posting_side=None, account_classification=None, account_categories=None, account_group=None, direct_posting=None, is_visible=None, job_process_option=None, ref_account_number=None, references_number=None):
        if not id:
            id = 0
        if not bank_account_number:
            bank_account_number = ''
        if not account_name:
            account_name = ''
        if not short_account_name:
            short_account_name = ''
        if not laos_name:
            laos_name = ''
        if not thai_name:
            thai_name = ''
        if not khmer_name:
            khmer_name = ''
        if not vietnamese_name:
            vietnamese_name = ''
        if not balance_side:
            balance_side = ''
        if not reverse_balance:
            reverse_balance = ''
        if not posting_side:
            posting_side = ''
        if not account_classification:
            account_classification = ''
        if not account_categories:
            account_categories = ''
        if not account_group:
            account_group = ''
        if not direct_posting:
            direct_posting = ''
        if not is_visible:
            is_visible = ''
        if not job_process_option:
            job_process_option = ''
        if not ref_account_number:
            ref_account_number = ''
        if not references_number:
            references_number = ''
        payload = {
            "id": id,
            "bank_account_number": bank_account_number,
            "account_name": account_name,
            "short_account_name": short_account_name,
            "multi_value_name": {
                "laos_name": laos_name,
                "thai_name": thai_name,
                "khmer_name": khmer_name,
                "vietnamese_name": vietnamese_name
            },
            "balance_side": balance_side,
            "reverse_balance": reverse_balance,
            "posting_side": posting_side,
            "account_classification": account_classification,
            "account_categories": account_categories,
            "account_group": account_group,
            "direct_posting": direct_posting,
            "is_visible": is_visible,
            "job_process_option": job_process_option,
            "ref_account_number": ref_account_number,
            "references_number": references_number
        }
        return payload

    def delete(self, id=None):
        if not id:
            id = ''
        payload = {
            "id": id
        }
        return payload

    def open_account(self, account_number=None):
        if not account_number:
            account_number = ''
        payload = {
            "account_number": account_number
        }
        return payload