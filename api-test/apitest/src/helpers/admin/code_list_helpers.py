from ...utilities.requestUtility import RequestUtility

class CodeListHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def advanced_search_code_list(self, payload):
        return self.requests_utility.post_admin(f'api/CodeList/Search', payload)

    def simple_search_code_list(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/CodeList/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def add_code_list(self, payload):
        return self.requests_utility.post_admin(f'api/CodeList/Create', payload)

    def view_code_list(self, id):
        return self.requests_utility.get_admin(f'api/CodeList/View/{id}')

    def update_code_list(self, payload):
        return self.requests_utility.put_admin(f'api/CodeList/Update', payload)

    def delete_code_list(self, payload):
        return self.requests_utility.delete_admin(f'api/CodeList/Delete', payload)

    def sync_code_list(self):
        return self.requests_utility.post_admin(f'')
        # code/cdlistforsync

# ====================================== Workflow id ======================================
# Admin - Code List
    def ADM_SIMPLE_SEARCH_CODE_LIST(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_SIMPLE_SEARCH_CODE_LIST', fields_data)

    def ADM_ADVANCED_SEARCH_CODE_LIST(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_ADVANCED_SEARCH_CODE_LIST', fields_data)

    def ADM_VIEW_CODE_LIST(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_VIEW_CODE_LIST', fields_data)

    def ADM_INSERT_CODE_LIST(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_INSERT_CODE_LIST', fields_data)

    def ADM_UPDATE_CODE_LIST(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_UPDATE_CODE_LIST', fields_data)

    def ADM_DELETE_CODE_LIST(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_DELETE_CODE_LIST', fields_data)