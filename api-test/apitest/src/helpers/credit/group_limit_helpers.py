from ...utilities.requestUtility import RequestUtility

class GroupLimitHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_group_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditGroupLimit/View', payload)

    def simple_search_group_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditGroupLimit/SimpleSearch', payload)

    def advanced_search_group_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditGroupLimit/AdvanceSearch', payload)

    def add_group_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditGroupLimit/Create', payload)

    def update_group_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditGroupLimit/Update', payload)

    def delete_group_limit(self, payload):
        return self.requests_utility.post_credit(f'api/CreditGroupLimit/Delete', payload)

# ====================================== Workflow id ======================================
# Credit - Group Limit
    def CRD_SEARCH_SP_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SEARCH_SP_CRDGRPLM', fields_data)

    def CRD_SEARCH_ADV_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SEARCH_ADV_CRDGRPLM', fields_data)

    def CRD_VIEW_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_VIEW_CRDGRPLM', fields_data)

    def CRD_INSERT_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_INSERT_CRDGRPLM', fields_data)

    def CRD_UPDATE_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_UPDATE_CRDGRPLM', fields_data)

    def CRD_DELETE_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_DELETE_CRDGRPLM', fields_data)

    # get list customer use group limit
    def CTM_VIEW_GRP_LIMIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CTM_VIEW_GRP_LIMIT', fields_data)