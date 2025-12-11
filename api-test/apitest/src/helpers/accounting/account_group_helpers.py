from ...utilities.requestUtility import RequestUtility

class AccountGroupHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_account_group(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinition/View', payload)

    def simple_search_account_group(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinition/SimpleSearch', payload)

    def advanced_search_account_group(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinition/AdvanceSearch', payload)

    def add_account_group(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinition/Create', payload)

    def update_account_group(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinition/Update', payload)

    def delete_account_group(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountGroupDefinition/Delete', payload)

# ====================================== Workflow id ======================================
# Accounting - Account Group
    def ACT_ACGRPDEF_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEF_SER_SIMPLE', fields_data)

    def ACT_ACGRPDEF_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEF_SER_ADVANCE', fields_data)

    def ACT_ACGRPDEF_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEF_VIEW', fields_data)

    def ACT_ACGRPDEF_INS(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEF_INS', fields_data)

    def ACT_ACGRPDEF_UPD(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEF_UPD', fields_data)

    def ACT_ACGRPDEF_DEL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGRPDEF_DEL', fields_data)