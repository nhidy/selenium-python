from ...utilities.requestUtility import RequestUtility

class SubProductLimitHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_sub_product_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditSubProductLimit/View', payload)

    def simple_search_sub_product_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditSubProductLimit/SimpleSearch', payload)

    def advanced_search_sub_product_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditSubProductLimit/AdvanceSearch', payload)

    def add_sub_product_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditSubProductLimit/Create', payload)

    def update_sub_product_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditSubProductLimit/Update', payload)

# ====================================== Workflow id ======================================
# Credit - Sub Product Limit
    def CRD_UPDATE_CRDSPL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_UPDATE_CRDSPL', fields_data)

    def CRD_SEARCH_SP_CRDSPL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SEARCH_SP_CRDSPL', fields_data)

    def CRD_SEARCH_ADV_CRDSPL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SEARCH_ADV_CRDSPL', fields_data)

    def CRD_VIEW_CRDSPL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_VIEW_CRDSPL', fields_data)