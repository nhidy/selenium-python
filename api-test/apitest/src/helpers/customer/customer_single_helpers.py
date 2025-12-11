from ...utilities.requestUtility import RequestUtility

class CustomerSingleHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_customer_single(self, payload):
        return self.requests_utility.post_customer(f'api/SingleCustomer/View', payload)

    def simple_search_customer_single(self, payload):
        return self.requests_utility.post_customer(f'api/SingleCustomer/SimpleSearch', payload)

    def advanced_search_customer_single(self, payload):
        return self.requests_utility.post_customer(f'api/SingleCustomer/AdvanceSearch', payload)

    def add_customer_single(self, payload):
        return self.requests_utility.post_customer(f'api/SingleCustomer/Create', payload)

    def update_customer_single(self, payload):
        return self.requests_utility.post_customer(f'api/SingleCustomer/Update', payload)

    def delete_customer_single(self, payload):
        return self.requests_utility.post_customer(f'api/SingleCustomer/Delete', payload)

    def list_sanction(self, payload): 
        return self.requests_utility.post_customer(f'', payload)
        # customer/customer/sanction

    def check_sanction(self, payload): 
        return self.requests_utility.post_customer(f'', payload)
        # customer/customer/checksanction

    def list_deposit(self, id): 
        return self.requests_utility.get_customer(f'')
        # customer/customer/{id}/deposit

    def list_credit(self, id): 
        return self.requests_utility.get_customer(f'')
        # customer/customer/{id}/credit

# ====================================== Workflow id ======================================
# Customer - Customer Information
    def SQL_SEARCH_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_SEARCH_CTM', fields_data)

    def SQL_ADSEARCH_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_ADSEARCH_CTM', fields_data)

    def SQL_VIEW_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_VIEW_CTM', fields_data)

    def SQL_INSERT_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_INSERT_CTM', fields_data)

    def SQL_UPDATE_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_UPDATE_CTM', fields_data)

    def SQL_DELETE_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_DELETE_CTM', fields_data)

    # Get list relation customer by customer code
    def SQL_RELATION_CTMGRP(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_RELATION_CTMGRP', fields_data)

    # Get list deposit by customer id
    def DPT_GETLISTDPTBYCUSTID(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_GETLISTDPTBYCUSTID', fields_data)

    # Get list credit by customer id
    def CRD_LIST_CREDIT_ACCOUNT_BY_CUSTOMER_ID(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_LIST_CREDIT_ACCOUNT_BY_CUSTOMER_ID', fields_data)

    # View by customer code
    def SQL_VIEWBYCODE_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_VIEWBYCODE_CTM', fields_data)

    # Get list detail customer code (lấy ra danh sách các customer, trừ customer code được gửi đi)
    def SQL_LOOKUP_LISTNOT_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_LOOKUP_LISTNOT_CTM', fields_data)

    # Get list customer
    def SQL_LOOKUP_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_LOOKUP_CTM', fields_data)