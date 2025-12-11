from ...utilities.requestUtility import RequestUtility

class MortgageFOHelper(object):
    def __init__(self, user):
        self.requests_utility = user

# ====================================== Workflow id ======================================
# Mortgage - FO
    def MTG_OPN(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'MTG_OPN', fields_data)

    # def MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG', fields_data)

    # def MTG_VIEW_MORTGAGE_CATALOG(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'MTG_VIEW_MORTGAGE_CATALOG', fields_data)

    # def MTG_INSERT_MORTGAGE_CATALOG(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'MTG_INSERT_MORTGAGE_CATALOG', fields_data)

    # def MTG_UPDATE_MORTGAGE_CATALOG(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'MTG_UPDATE_MORTGAGE_CATALOG', fields_data)

    # def MTG_DELETE_MORTGAGE_CATALOG(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'MTG_DELETE_MORTGAGE_CATALOG', fields_data)