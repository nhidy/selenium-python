from ...utilities.requestUtility import RequestUtility

class UserRightHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_user_right(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/UserRight/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_user_right(self, payload):
        return self.requests_utility.post_admin(f'api/UserRight/Search', payload)

    def add_user_right(self, payload):
        return self.requests_utility.post_admin(f'api/UserRight/Create', payload)

    def view_user_right(self, id):
        return self.requests_utility.get_admin(f'api/UserRight/View/{id}')

    def update_user_right(self, payload):
        return self.requests_utility.put_admin(f'api/UserRight/Update', payload)

    def delete_user_right(self, payload):
        return self.requests_utility.delete_admin(f'api/UserRight/Delete', payload)