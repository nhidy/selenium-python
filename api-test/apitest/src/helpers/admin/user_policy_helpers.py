from ...utilities.requestUtility import RequestUtility

class UserPolicyHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_user_policy(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/UserPolicy/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_user_policy(self, payload):
        return self.requests_utility.post_admin(f'api/UserPolicy/Search', payload)

    def add_user_policy(self, payload):
        return self.requests_utility.post_admin('api/UserPolicy/Create', payload)

    def view_user_policy(self, id):
        return self.requests_utility.get_admin(f'api/UserPolicy/View/{id}')

    def view_user_policy_by_policy_id(self, policy_id):
        return self.requests_utility.get_admin(f'api/UserPolicy/ViewByPolicyId/{policy_id}')

    def update_user_policy(self, payload):
        return self.requests_utility.put_admin(f'api/UserPolicy/Update', payload)

    def delete_user_policy(self, payload):
        return self.requests_utility.delete_admin(f'api/UserPolicy/Delete', payload)

# ====================================== Workflow id ======================================
# Admin - Policy
    def ADM_SIMPLE_SEARCH_USER_POLICY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_SIMPLE_SEARCH_USER_POLICY', fields_data)

    def ADM_ADVANCED_SEARCH_USER_POLICY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_ADVANCED_SEARCH_USER_POLICY', fields_data)

    def ADM_VIEW_USER_POLICY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_VIEW_USER_POLICY', fields_data)

    def ADM_INSERT_USER_POLICY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_INSERT_USER_POLICY', fields_data)

    def ADM_UPDATE_USER_POLICY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_UPDATE_USER_POLICY', fields_data)

    def ADM_DELETE_USER_POLICY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_DELETE_USER_POLICY', fields_data)