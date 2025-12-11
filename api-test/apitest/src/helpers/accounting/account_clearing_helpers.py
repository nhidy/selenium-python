from ...utilities.requestUtility import RequestUtility

class AccountClearingHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_account_clearing(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountClearing/View', payload)

    def simple_search_account_clearing(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountClearing/SimpleSearch', payload)

    def advanced_search_account_clearing(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountClearing/AdvanceSearch', payload)

    def add_account_clearing(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountClearing/Create', payload)

    def update_account_clearing(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountClearing/Update', payload)

    def delete_account_clearing(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountClearing/Delete', payload)

# ====================================== Workflow id ======================================
# Accounting - Clearing Account
    def ACT_ACCLR_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCLR_SER_SIMPLE', fields_data)

    def ACT_ACCLR_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCLR_SER_ADVANCE', fields_data)

    def ACT_ACCLR_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCLR_VIEW', fields_data)

    def ACT_ACCLR_INS(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCLR_INS', fields_data)

    def ACT_ACCLR_UPD(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCLR_UPD', fields_data)

    def ACT_ACCLR_DEL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCLR_DEL', fields_data)