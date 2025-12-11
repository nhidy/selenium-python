from ...utilities.requestUtility import RequestUtility

class BranchHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def advanced_search_branch(self, payload):
        return self.requests_utility.post_admin(f'api/Branch/Search', payload)

    def simple_search_branch(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/Branch/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def add_branch(self, payload):
        return self.requests_utility.post_admin(f'api/Branch/Create', payload)

    def view_branch(self, id):
        return self.requests_utility.get_admin(f'api/Branch/View/{id}')

    def update_branch(self, payload):
        return self.requests_utility.put_admin(f'api/Branch/Update', payload)

    def delete_branch(self, payload):
        return self.requests_utility.delete_admin(f'api/Branch/Delete', payload)

# ====================================== Workflow id ======================================
# Admin - Branch
    def ADM_SIMPLE_SEARCH_BRANCH(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_SIMPLE_SEARCH_BRANCH', fields_data)

    def ADM_ADVANCED_SEARCH_BRANCH(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_ADVANCED_SEARCH_BRANCH', fields_data)

    def ADM_VIEW_BRANCH(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_VIEW_BRANCH', fields_data)

    def ADM_INSERT_BRANCH(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_INSERT_BRANCH', fields_data)

    def ADM_UPDATE_BRANCH(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_UPDATE_BRANCH', fields_data)

    def ADM_DELETE_BRANCH(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_DELETE_BRANCH', fields_data)