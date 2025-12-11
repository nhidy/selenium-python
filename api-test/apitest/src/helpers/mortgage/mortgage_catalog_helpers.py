from ...utilities.requestUtility import RequestUtility

class MortgageCatalogHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_mortgage_catalog(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_mortgage(f'api/MortgageCatalog/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_mortgage_catalog(self, payload):
        return self.requests_utility.post_mortgage(f'api/MortgageCatalog/Search', payload)

    def add_mortgage_catalog(self, payload):
        return self.requests_utility.post_mortgage('api/MortgageCatalog/Create', payload)

    def view_mortgage_catalog(self, id):
        return self.requests_utility.get_mortgage(f'api/MortgageCatalog/View/{id}')

    def update_mortgage_catalog(self, payload):
        return self.requests_utility.put_mortgage(f'api/MortgageCatalog/Update', payload)

    def delete_mortgage_catalog(self, payload):
        return self.requests_utility.delete_mortgage(f'api/MortgageCatalog/Delete', payload)

# ====================================== Workflow id ======================================
# Mortgage - Catalogue Definition
    def MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG', fields_data)

    def MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG', fields_data)

    def MTG_VIEW_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'MTG_VIEW_MORTGAGE_CATALOG', fields_data)

    def MTG_INSERT_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'MTG_INSERT_MORTGAGE_CATALOG', fields_data)

    def MTG_UPDATE_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'MTG_UPDATE_MORTGAGE_CATALOG', fields_data)

    def MTG_DELETE_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'MTG_DELETE_MORTGAGE_CATALOG', fields_data)