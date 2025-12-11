from ...utilities.requestUtility import RequestUtility

class FixedAssetAccountHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_fixed_asset_account(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetAccount/View', payload)

    def simple_search_fixed_asset_account(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetAccount/SimpleSearch', payload)

    def advanced_search_fixed_asset_account(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetAccount/AdvanceSearch', payload)

    def add_fixed_asset_account(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetAccount/Create', payload)

    def update_fixed_asset_account(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetAccount/Update', payload)

    def delete_fixed_asset_account(self, payload):
        return self.requests_utility.post_fixed_asset(f'api/FixedAssetAccount/Delete', payload)

# ====================================== Workflow id ======================================
# Fixed Asset - Fixed Asset And Tool
    def SQL_SEARCH_FACACT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_SEARCH_FACACT', fields_data)

    def SQL_ADSEARCH_FACACT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_ADSEARCH_FACACT', fields_data)

    def SQL_VIEW_FACACT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_VIEW_FACACT', fields_data)

    def SQL_UPDATE_FACACT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_UPDATE_FACACT', fields_data)

    def SQL_DELETE_FACACT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_DELETE_FACACT', fields_data)