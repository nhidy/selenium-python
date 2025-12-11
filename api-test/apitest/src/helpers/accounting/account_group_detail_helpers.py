from ...utilities.requestUtility import RequestUtility

class AccountGroupDetailHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_account_group_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinitionDetail/View', payload)

    def simple_search_account_group_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinitionDetail/SimpleSearch', payload)

    def advanced_search_account_group_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinitionDetail/AdvanceSearch', payload)

    def add_account_group_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinitionDetail/Create', payload)

    def update_account_group_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinitionDetail/Update', payload)

    def delete_account_group_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinitionDetail/Delete', payload)

# ====================================== Workflow id ======================================
# Accounting - Account Group Detail
    def ACT_ACGRPDEFDTL_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEFDTL_SER_SIMPLE', fields_data)

    def ACT_ACGRPDEFDTL_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEFDTL_SER_ADVANCE', fields_data)

    def ACT_ACGRPDEFDTL_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEFDTL_VIEW', fields_data)

    def ACT_ACGRPDEFDTL_INS(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEFDTL_INS', fields_data)

    def ACT_ACGRPDEFDTL_UPD(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEFDTL_UPD', fields_data)

    def ACT_ACGRPDEFDTL_DEL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEFDTL_DEL', fields_data)