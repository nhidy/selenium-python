from ...utilities.requestUtility import RequestUtility

class ExtensionAccountHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_extension_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ExtensionAccountOfGroupDefinition/View', payload)

    def simple_search_extension_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ExtensionAccountOfGroupDefinition/SimpleSearch', payload)

    def advanced_search_extension_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ExtensionAccountOfGroupDefinition/AdvanceSearch', payload)

    def add_extension_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ExtensionAccountOfGroupDefinition/Create', payload)

    def update_extension_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ExtensionAccountOfGroupDefinition/Update', payload)

    def delete_extension_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ExtensionAccountOfGroupDefinition/Delete', payload)

# ====================================== Workflow id ======================================
# Accounting - Extension Account
    def ACT_ACGLDEF_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGLDEF_SER_SIMPLE', fields_data)

    def ACT_ACGLDEF_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGLDEF_SER_ADVANCE', fields_data)

    def ACT_ACGLDEF_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGLDEF_VIEW', fields_data)

    def ACT_ACGLDEF_INS(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGLDEF_INS', fields_data)

    def ACT_ACGLDEF_UPD(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGLDEF_UPD', fields_data)

    def ACT_ACGLDEF_DEL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACGLDEF_DEL', fields_data)