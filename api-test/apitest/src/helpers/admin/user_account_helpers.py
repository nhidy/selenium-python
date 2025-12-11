from ...utilities.requestUtility import RequestUtility

class UserAccountHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_user_account(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/UserAccount/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_user_account(self, payload):
        return self.requests_utility.post_admin(f'api/UserAccount/Search', payload)

    def add_user_account(self, payload):
        return self.requests_utility.post_admin(f'api/UserAccount/Create', payload)

    def view_user_account(self, id):
        return self.requests_utility.get_admin(f'api/UserAccount/View/{id}')

    def update_user_account(self, payload):
        return self.requests_utility.put_admin(f'api/UserAccount/Update', payload)

    def delete_user_account(self, payload):
        return self.requests_utility.delete_admin(f'api/UserAccount/Delete', payload)

    def logout_user_account(self, payload):
        return self.requests_utility.post_admin(f'', payload)
        # user/logout

    def approve_user_account(self, payload):
        return self.requests_utility.post_admin(f'', payload )
        # user/approve

    def send_email_password(self, payload):
        return self.requests_utility.post_admin(f'',payload)
        # user/sendemailpwd

    def change_password(self, payload):
        return self.requests_utility.post_admin(f'', payload)
        # user/changepwd

    def user_preference(self, payload):
        return self.requests_utility.post_admin(f'', payload)
        # user/preference

# ====================================== Workflow id ======================================
# Admin - User Account
    def ADM_SIMPLE_SEARCH_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_SIMPLE_SEARCH_USER_ACCOUNT', fields_data)

    def ADM_ADVANCED_SEARCH_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_ADVANCED_SEARCH_USER_ACCOUNT', fields_data)

    def ADM_VIEW_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_VIEW_USER_ACCOUNT', fields_data)

    def ADM_INSERT_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_INSERT_USER_ACCOUNT', fields_data)

    def ADM_UPDATE_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_UPDATE_USER_ACCOUNT', fields_data)

    def ADM_DELETE_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_DELETE_USER_ACCOUNT', fields_data)