from ...utilities.requestUtility import RequestUtility

class CurrencyHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_currency(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_admin(f'api/Currency/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_currency(self, payload):
        return self.requests_utility.post_admin(f'api/Currency/Search', payload)

    def add_currency(self, payload):
        return self.requests_utility.post_admin('api/Currency/Create', payload)

    def view_currency(self, id):
        return self.requests_utility.get_admin(f'api/Currency/View/{id}')

    def update_currency(self, payload):
        return self.requests_utility.put_admin(f'api/Currency/Update', payload)

    def delete_currency(self, payload):
        return self.requests_utility.delete_admin(f'api/Currency/Delete', payload)

# ====================================== Workflow id ======================================
# Admin - Currency
    def ADM_SIMPLE_SEARCH_CURRENCY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_SIMPLE_SEARCH_CURRENCY', fields_data)

    def ADM_ADVANCED_SEARCH_CURRENCY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_ADVANCED_SEARCH_CURRENCY', fields_data)

    def ADM_VIEW_CURRENCY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_VIEW_CURRENCY', fields_data)

    def ADM_INSERT_CURRENCY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_INSERT_CURRENCY', fields_data)

    def ADM_UPDATE_CURRENCY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_UPDATE_CURRENCY', fields_data)

    def ADM_DELETE_CURRENCY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_DELETE_CURRENCY', fields_data)