from ...utilities.requestUtility import RequestUtility

class FixedAssetCatalogHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_fixed_asset_catalog(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetCatalog/View', payload)

    def simple_search_fixed_asset_catalog(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetCatalog/SimpleSearch', payload)

    def advanced_search_fixed_asset_catalog(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetCatalog/AdvanceSearch', payload)

    def add_fixed_asset_catalog(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetCatalog/Create', payload)

    def update_fixed_asset_catalog(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetCatalog/Update', payload)

    def delete_fixed_asset_catalog(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetCatalog/Delete', payload)

    def list_fixed_asset_catalog(self, page):
        return self.requests_utility.get_fixed_asset(f'{page}')
        # fixed_asset/catalogue/?page=

# ====================================== Workflow id ======================================
# Fixed Asset - Catalogue Definition
    def SQL_SEARCH_FACCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_SEARCH_FACCAT', fields_data)

    def SQL_ADSEARCH_FACCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_ADSEARCH_FACCAT', fields_data)

    def SQL_VIEW_FACCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_VIEW_FACCAT', fields_data)

    def SQL_INSERT_FACCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_INSERT_FACCAT', fields_data)

    def SQL_UPDATE_FACCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_UPDATE_FACCAT', fields_data)

    def SQL_DELETE_FACCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_DELETE_FACCAT', fields_data)