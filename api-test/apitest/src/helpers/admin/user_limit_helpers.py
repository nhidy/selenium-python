from ...utilities.requestUtility import RequestUtility

class UserLimitHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_user_limit(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/UserLimit/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_user_limit(self, payload):
        return self.requests_utility.post_admin(f'api/UserLimit/GetListUserLimit', payload)

    def add_user_limit(self, payload):
        return self.requests_utility.post_admin(f'api/UserLimit/Create', payload)

    def view_user_limit(self, id):
        return self.requests_utility.get_admin(f'api/UserLimit/View/{id}')

    def update_user_limit(self, payload):
        return self.requests_utility.put_admin(f'api/UserLimit/Update', payload)

    def delete_user_limit(self, payload):
        return self.requests_utility.delete_admin(f'api/UserLimit/Delete', payload)