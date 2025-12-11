from ...utilities.requestUtility import RequestUtility

class AccountMappingHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_account_mapping(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMapping/View', payload)

    def simple_search_account_mapping(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMapping/SimpleSearch', payload)

    def advanced_search_account_mapping(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMapping/AdvanceSearch', payload)

    def add_account_mapping(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMapping/Create', payload)

    def update_account_mapping(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMapping/Update', payload)

    def delete_account_mapping(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMapping/Delete', payload)

# ====================================== Workflow id ======================================
# Accounting - Account Mapping
    def ACT_ACMAP_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACMAP_SER_SIMPLE', fields_data)

    def ACT_ACMAP_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACMAP_SER_ADVANCE', fields_data)

    def ACT_ACMAP_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACMAP_VIEW', fields_data)

    def ACT_ACMAP_INS(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACMAP_INS', fields_data)

    def ACT_ACMAP_UPD(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACMAP_UPD', fields_data)

    def ACT_ACMAP_DEL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACMAP_DEL', fields_data)