from ...utilities.requestUtility import RequestUtility

class ProductLimitHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_product_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditProductLimit/View', payload)

    def simple_search_product_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditProductLimit/SimpleSearch', payload)

    def advanced_search_product_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditProductLimit/AdvanceSearch', payload)

    def add_product_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditProductLimit/Create', payload)

    def update_product_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditProductLimit/Update', payload)

# ====================================== Workflow id ======================================
# Credit - Product Limit
    def CRD_UPDATE_CRDPL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_UPDATE_CRDPL', fields_data)

    def CRD_SEARCH_SP_CRDPL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SEARCH_SP_CRDPL', fields_data)

    def CRD_SEARCH_ADV_CRDPL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SEARCH_ADV_CRDPL', fields_data)

    def CRD_VIEW_CRDPL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_VIEW_CRDPL', fields_data)