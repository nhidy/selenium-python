from ...utilities.requestUtility import RequestUtility

class AccountCommonHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_account_common(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountCommon/View', payload)

    def simple_search_account_common(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountCommon/SimpleSearch', payload)

    def advanced_search_account_common(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountCommon/AdvanceSearch', payload)

    def add_account_common(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountCommon/Create', payload)

    def update_account_common(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountCommon/Update', payload)

    def delete_account_common(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountCommon/Delete', payload)

# ====================================== Workflow id ======================================
# Accounting - Common Account
    def ACT_ACCOM_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCOM_SER_SIMPLE', fields_data)

    def ACT_ACCOM_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCOM_SER_ADVANCE', fields_data)

    def ACT_ACCOM_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCOM_VIEW', fields_data)

    def ACT_ACCOM_INS(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCOM_INS', fields_data)

    def ACT_ACCOM_UPD(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCOM_UPD', fields_data)

    def ACT_ACCOM_DEL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCOM_DEL', fields_data)