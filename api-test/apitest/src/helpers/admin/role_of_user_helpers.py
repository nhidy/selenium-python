from ...utilities.requestUtility import RequestUtility

class RoleOfUserHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_role_of_user(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/RoleOfUser/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_role_of_user(self, payload):
        return self.requests_utility.post_admin(f'api/RoleOfUser/Search', payload)

    def add_role_of_user(self, payload):
        return self.requests_utility.post_admin(f'api/RoleOfUser/Create', payload)

    def view_role_of_user(self, id):
        return self.requests_utility.get_admin(f'api/RoleOfUser/View/{id}')

    def update_role_of_user(self, payload):
        return self.requests_utility.put_admin(f'api/RoleOfUser/Update', payload)

    def delete_role_of_user(self, payload):
        return self.requests_utility.delete_admin(f'api/RoleOfUser/Delete', payload)