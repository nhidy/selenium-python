from ...utilities.requestUtility import RequestUtility

class CustomerGroupHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_customer_group(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerGroup/View', payload)

    def simple_search_customer_group(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerGroup/SimpleSearch', payload)

    def advanced_search_customer_group(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerGroup/AdvanceSearch', payload)

    def add_customer_group(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerGroup/Create', payload)

    def update_customer_group(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerGroup/Update', payload)

    def delete_customer_group(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerGroup/Delete', payload)

    def list_media(self, id): 
        return self.requests_utility.get_customer(f'')
        # customer/customergroup/{id}/media

    def list_member_in_group(self, id):
        return self.requests_utility.get_customer(f'')
        # customer/customergroup/{id}/members/CTM/in

    def list_member_not_in_group(self, term):
        return self.requests_utility.get_customer(f'')
        # customer/customergroup/members/CTM/notin/{term}

# ====================================== Workflow id ======================================
# Customer - Customer Group
    def SQL_SEARCH_CTMGRP(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_SEARCH_CTMGRP', fields_data)

    def SQL_ADSEARCH_CTMGRP(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_ADSEARCH_CTMGRP', fields_data)

    def SQL_VIEW_CTMGRP(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_VIEW_CTMGRP', fields_data)

    def SQL_INSERT_CTMGRP(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_INSERT_CTMGRP', fields_data)

    def SQL_UPDATE_CTMGRP(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_UPDATE_CTMGRP', fields_data)

    def SQL_DELETE_CTMGRP(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_DELETE_CTMGRP', fields_data)

    def CTM_GROUP_LIMIT_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CTM_GROUP_LIMIT_VIEW', fields_data)