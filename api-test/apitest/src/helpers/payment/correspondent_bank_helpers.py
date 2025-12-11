from ...utilities.requestUtility import RequestUtility

class CorrespondentBankHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_correspondent_bank(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_payment(f'api/CorrespondentBank/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_correspondent_bank(self, payload):
        return self.requests_utility.post_payment(f'api/CorrespondentBank/Search', payload)

    def add_correspondent_bank(self, payload):
        return self.requests_utility.post_payment(f'api/CorrespondentBank/Create', payload)

    def view_correspondent_bank(self, id):
        return self.requests_utility.get_payment(f'api/CorrespondentBank/View/{id}')

    def update_correspondent_bank(self, payload):
        return self.requests_utility.put_payment(f'api/CorrespondentBank/Update', payload)

    def delete_correspondent_bank(self, id=None):
        if not id:
            id = 0
        return self.requests_utility.delete_payment(f'api/CorrespondentBank/Delete?id={id}')

# ====================================== Workflow id ======================================
# Payment - Correspondent Bank
    def PMT_SEARCH_SP_AGENTBANK(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_SEARCH_SP_AGENTBANK', fields_data)

    def PMT_SEARCH_ADV_AGENTBANK(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_SEARCH_ADV_AGENTBANK', fields_data)

    def PMT_VIEW_AGENTBANK(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_VIEW_AGENTBANK', fields_data)

    def PMT_INSERT_AGENTBANK(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_INSERT_AGENTBANK', fields_data)

    def PMT_UPDATE_AGENTBANK(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_UPDATE_AGENTBANK', fields_data)

    def PMT_DELETE_AGENTBANK(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_DELETE_AGENTBANK', fields_data)