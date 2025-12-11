from ...utilities.requestUtility import RequestUtility

class CountryHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_country(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/Country/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_country(self, payload):
        return self.requests_utility.post_admin(f'api/Country/Search', payload)

    def add_country(self, payload):
        return self.requests_utility.post_admin(f'api/Country/Create', payload)

    def view_country(self, id):
        return self.requests_utility.get_admin(f'api/Country/View/{id}')

    def update_country(self, payload):
        return self.requests_utility.put_admin(f'api/Country/Update', payload)

    def delete_country(self, payload):
        return self.requests_utility.delete_admin(f'api/Country/Delete', payload)

# ====================================== Workflow id ======================================
# Admin - Country
    def ADM_SIMPLE_SEARCH_COUNTRY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_SIMPLE_SEARCH_COUNTRY', fields_data)

    def ADM_ADVANCED_SEARCH_COUNTRY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_ADVANCED_SEARCH_COUNTRY', fields_data)

    def ADM_VIEW_COUNTRY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_VIEW_COUNTRY', fields_data)

    def ADM_INSERT_COUNTRY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_INSERT_COUNTRY', fields_data)

    def ADM_UPDATE_COUNTRY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_UPDATE_COUNTRY', fields_data)

    def ADM_DELETE_COUNTRY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_DELETE_COUNTRY', fields_data)