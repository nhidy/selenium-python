from ...utilities.requestUtility import RequestUtility

class UserRoleHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_user_role(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/UserRole/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_user_role(self, payload):
        return self.requests_utility.post_admin(f'api/UserRole/Search', payload)

    def add_user_role(self, payload):
        return self.requests_utility.post_admin(f'api/UserRole/Create', payload)

    def view_user_role(self, id):
        return self.requests_utility.get_admin(f'api/UserRole/View/{id}')

    def update_user_role(self, payload):
        return self.requests_utility.put_admin(f'api/UserRole/Update', payload)

    def delete_user_role(self, payload):
        return self.requests_utility.delete_admin(f'api/UserRole/Delete', payload)

    def list_member_user_role(self, payload):
        return self.requests_utility.post_admin(f'', payload)
        # userrole/ListMembers

# ====================================== Workflow id ======================================
# Admin - Role Profiles - Add - Remove - API [UserRole]
    def ADM_VIEW_USER_ROLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_VIEW_USER_ROLE', fields_data)

    def ADM_INSERT_USER_ROLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_INSERT_USER_ROLE', fields_data)

    def ADM_DELETE_USER_ROLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_DELETE_USER_ROLE', fields_data)