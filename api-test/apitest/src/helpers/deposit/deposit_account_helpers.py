from ...utilities.requestUtility import RequestUtility

class DepositAccountHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_deposit_account_by_account_number(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositAccount/GetByAccountNumber', payload)

    def view_deposit_account_by_id(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositAccount/View', payload)

    def simple_search_deposit_account(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositAccount/SimpleSearch', payload)

    def advanced_search_deposit_account(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositAccount/AdvanceSearch', payload)

    def add_deposit_account(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositAccount/Create', payload)

    def update_deposit_account(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositAccount/Update', payload)

    def delete_deposit_account_by_id(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositAccount/Delete', payload)

    def delete_deposit_account_by_defacno(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositAccount/DeleteByDefacno', payload)

    def list_ifc(self, payload):
        return self.requests_utility.post_deposit(f'', payload)
        # deposit/account/ListIFC

    def list_media(self, payload):
        return self.requests_utility.post_deposit(f'', payload)
        # deposit/account/GetSignatureExecute

    def refresh_print(self, payload):
        return self.requests_utility.post_deposit(f'', payload)
        # deposit/Account/refreshprint

# ====================================== Workflow id ======================================
# Deposit - Deposit Account
    def DPT_SEARCH_DEPOSIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_SEARCH_DEPOSIT', fields_data)

    def DPT_ADSEARCH_DEPOSIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_ADSEARCH_DEPOSIT', fields_data)

    def DPT_VIEW_DEPOSIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_VIEW_DEPOSIT', fields_data)

    def DPT_UPDATE_DEPOSIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_UPDATE_DEPOSIT', fields_data)

    def DPT_DELETE_DEPOSIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_DELETE_DEPOSIT', fields_data)

    def DPT_LIST_FDACC_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_LIST_FDACC_VIEW', fields_data)

    def DPT_UPDATE_LFA_MFA(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_UPDATE_LFA_MFA', fields_data)

    def DPT_UPDATE_STATUS_DPT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_UPDATE_STATUS_DPT', fields_data)