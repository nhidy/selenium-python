from ...utilities.requestUtility import RequestUtility

class CreditCatalogHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_credit_catalog(self, payload):
        return self.requests_utility.post_credit(f'api/CreditCatalog/View', payload)

    def simple_search_credit_catalog(self, payload):
        return self.requests_utility.post_credit(f'api/CreditCatalog/SimpleSearch', payload)

    def advanced_search_credit_catalog(self, payload):
        return self.requests_utility.post_credit(f'api/CreditCatalog/AdvanceSearch', payload)

    def add_credit_catalog(self, payload):
        return self.requests_utility.post_credit(f'api/CreditCatalog/Create', payload)

    def update_credit_catalog(self, payload):
        return self.requests_utility.post_credit(f'api/CreditCatalog/Update', payload)

    def delete_credit_catalog(self, payload):
        return self.requests_utility.post_credit(f'api/CreditCatalog/Delete', payload)

    def list_group_id(self, payload):
        return self.requests_utility.post_credit(f'', payload)

    def list_tariff(self, payload):
        return self.requests_utility.post_credit(f'', payload)

# ====================================== Workflow id ======================================
# Credit - Catalogue Definition
    def CRD_SEARCH_SP_CRDCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SEARCH_SP_CRDCAT', fields_data)

    def CRD_SEARCH_ADV_CRDCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SEARCH_ADV_CRDCAT', fields_data)

    def CRD_VIEW_CRDCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_VIEW_CRDCAT', fields_data)

    def CRD_INSERT_CRDCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_INSERT_CRDCAT', fields_data)

    def CRD_UPDATE_CRDCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_UPDATE_CRDCAT', fields_data)

    def CRD_DELETE_CRDCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_DELETE_CRDCAT', fields_data)