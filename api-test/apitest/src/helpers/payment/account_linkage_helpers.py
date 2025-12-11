from ...utilities.requestUtility import RequestUtility

class AccountLinkageHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_account_linkage(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_payment(f'api/AccountLinkage/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_account_linkage(self, payload):
        return self.requests_utility.post_payment(f'api/AccountLinkage/Search', payload)

    def add_account_linkage(self, payload):
        return self.requests_utility.post_payment(f'api/AccountLinkage/Create', payload)

    def view_account_linkage(self, id):
        return self.requests_utility.get_payment(f'api/AccountLinkage/View/{id}')

    def update_account_linkage(self, payload):
        return self.requests_utility.put_payment(f'api/AccountLinkage/Update', payload)

    def delete_account_linkage(self, id=None):
        if not id:
            id = 0
        return self.requests_utility.delete_payment(f'api/AccountLinkage/Delete?id={id}')

    def list_ifc(self, payload):
        return self.requests_utility.post_payment(f'', payload)
        # payment/AccountLinkage/ListIFC

# ====================================== Workflow id ======================================
# Payment - Account Linkage
    def PMT_SEARCH_SP_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_SEARCH_SP_ACLINKAGE', fields_data)

    def PMT_SEARCH_ADV_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_SEARCH_ADV_ACLINKAGE', fields_data)

    def PMT_VIEW_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_VIEW_ACLINKAGE', fields_data)

    def PMT_INSERT_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_INSERT_ACLINKAGE', fields_data)

    def PMT_UPDATE_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_UPDATE_ACLINKAGE', fields_data)

    def PMT_DELETE_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_DELETE_ACLINKAGE', fields_data)