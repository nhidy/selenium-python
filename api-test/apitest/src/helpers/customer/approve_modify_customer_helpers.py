from ...utilities.requestUtility import RequestUtility

class ApproveModifyCustomerHelper(object):
    def __init__(self, user):
        self.requests_utility = user
    
    def simple_search_approve_modify_customer(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerApprove/SimpleSearch', payload)

    def advanced_search_approve_modify_customer(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerApprove/AdvanceSearch', payload)

    def view_by_customer_code(self, payload):
        return self.requests_utility.post_customer(f'api/SingleCustomer/ViewByCode', payload)

    def view_user_modify_customer(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerApprove/ViewUserModify', payload)

    def view_info_modify_customer(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerApprove/ViewModify', payload)

    def approve_info_modify_customer(self, payload):
        return self.requests_utility.post_customer(f'api/CustomerApprove/ApproveModify', payload)

    def reject_info_modify_customer(self, payload):
        return self.requests_utility.post_customer(f'/api/CustomerApprove/RejectModify', payload)

# ====================================== Workflow id ======================================
# Customer - Approve Modify Customer
    def SQL_SEARCH_APR(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_SEARCH_APR', fields_data)

    def SQL_ADSEARCH_APR(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_ADSEARCH_APR', fields_data)

    def SQL_VIEWBYCODE_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_VIEWBYCODE_CTM', fields_data)

    def CTM_GET_INFO_USER_MODIFY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CTM_GET_INFO_USER_MODIFY', fields_data)

    def SQL_VIEW_APR(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_VIEW_APR', fields_data)

    def SQL_CTM_APR(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_CTM_APR', fields_data)

    def SQL_CTM_REJ(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_CTM_REJ', fields_data)