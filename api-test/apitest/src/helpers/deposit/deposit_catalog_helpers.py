from ...utilities.requestUtility import RequestUtility

class DepositCatalogHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_deposit_catalog(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositCatalog/View', payload)

    def simple_search_deposit_catalog(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositCatalog/SimpleSearch', payload)

    def advanced_search_deposit_catalog(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositCatalog/AdvanceSearch', payload)

    def add_deposit_catalog(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositCatalog/Create', payload)

    def update_deposit_catalog(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositCatalog/Update', payload)

    def delete_deposit_catalog(self, payload):
        return self.requests_utility.post_deposit(f'api/DepositCatalog/Delete', payload)

    def list_group_id(self, payload):
        return self.requests_utility.post_deposit(f'', payload)
        # deposit/catalogue/GetGroupIdCdList
    
    def list_tariff(self, payload):
        return self.requests_utility.post_deposit(f'', payload)

# ====================================== Workflow id ======================================
# Deposit - Deposit Catalogue
    def DPT_SEARCH_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_SEARCH_CATALOG', fields_data)

    def DPT_ADSEARCH_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_ADSEARCH_CATALOG', fields_data)

    def DPT_VIEW_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_VIEW_CATALOG', fields_data)

    def DPT_INSERT_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_INSERT_CATALOG', fields_data)

    def DPT_UPDATE_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_UPDATE_CATALOG', fields_data)

    def DPT_DELETE_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_DELETE_CATALOG', fields_data)