from ...utilities.requestUtility import RequestUtility

class CustomerLinkageHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_customer_linkage(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerLinkage/View', payload)

    def simple_search_customer_linkage(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerLinkage/SimpleSearch', payload)

    def advanced_search_customer_linkage(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerLinkage/AdvanceSearch', payload)

    def add_customer_linkage(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerLinkage/Create', payload)

    def update_customer_linkage(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerLinkage/Update', payload)

    def delete_customer_linkage(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerLinkage/Delete', payload)

    def list_media(self, id): 
        return self.requests_utility.post_customer(f'')
        # customer/customerlinkage/{id}/media

    def list_member(self, id):
        return self.requests_utility.post_customer(f'')
        # customer/customerlinkage/{id}/members

# ====================================== Workflow id ======================================
# Customer - Customer Linkage
    def SQL_SEARCH_CTMLKG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_SEARCH_CTMLKG', fields_data)

    def SQL_ADSEARCH_CTMLKG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_ADSEARCH_CTMLKG', fields_data)

    def SQL_VIEW_CTMLKG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_VIEW_CTMLKG', fields_data)

    def SQL_INSERT_CTMLKG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_INSERT_CTMLKG', fields_data)

    def SQL_UPDATE_CTMLKG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_UPDATE_CTMLKG', fields_data)

    def SQL_DELETE_CTMLKG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_DELETE_CTMLKG', fields_data)