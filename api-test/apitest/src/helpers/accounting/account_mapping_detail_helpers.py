from ...utilities.requestUtility import RequestUtility

class AccountMappingDetailHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_account_mapping_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMappingDetail/View', payload)

    def simple_search_account_mapping_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMappingDetail/SimpleSearch', payload)

    def add_account_mapping_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMappingDetail/Create', payload)

    def update_account_mapping_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMappingDetail/Update', payload)

    def delete_account_mapping_detail(self, payload):
        return self.requests_utility.post_accounting(f'api/AccountMappingDetail/Delete', payload)