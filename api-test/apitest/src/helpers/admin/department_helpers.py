from ...utilities.requestUtility import RequestUtility

class DepartmentHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_department(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/Department/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_department(self, payload):
        return self.requests_utility.post_admin(f'api/Department/Search', payload)

    def add_department(self, payload):
        return self.requests_utility.post_admin(f'api/Department/Create', payload)

    def view_department(self, id):
        return self.requests_utility.get_admin(f'api/Department/View/{id}')

    def update_department(self, payload):
        return self.requests_utility.put_admin(f'api/Department/Update', payload)

    def delete_department(self, payload):
        return self.requests_utility.delete_admin(f'api/Department/Delete', payload)

# ====================================== Workflow id ======================================
# Admin - Department
    def ADM_SIMPLE_SEARCH_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_SIMPLE_SEARCH_DEPARTMENT', fields_data)

    def ADM_ADVANCED_SEARCH_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_ADVANCED_SEARCH_DEPARTMENT', fields_data)

    def ADM_VIEW_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_VIEW_DEPARTMENT', fields_data)

    def ADM_INSERT_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_INSERT_DEPARTMENT', fields_data)

    def ADM_UPDATE_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_UPDATE_DEPARTMENT', fields_data)

    def ADM_DELETE_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_DELETE_DEPARTMENT', fields_data)