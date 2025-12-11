from ...utilities.requestUtility import RequestUtility

class DenominationHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_denomination(self, payload):
        return self.requests_utility.post_cash(f'api/Denomination/View', payload)

    def simple_search_denomination(self, payload):
        return self.requests_utility.post_cash(f'api/Denomination/SimpleSearch', payload)

    def advanced_search_denomination(self, payload):
        return self.requests_utility.post_cash(f'api/Denomination/AdvanceSearch', payload)

    def add_denomination(self, payload):
        return self.requests_utility.post_cash(f'api/Denomination/Create', payload)

    def update_denomination(self, payload):
        return self.requests_utility.post_cash(f'api/Denomination/Update', payload)

    def delete_denomination(self, payload):
        return self.requests_utility.post_cash(f'api/Denomination/Delete', payload)

# ====================================== Workflow id ======================================
# Cash - Denomination
    def CSH_DENOM_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CSH_DENOM_SER_SIMPLE', fields_data)

    def CSH_DENOM_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CSH_DENOM_SER_ADVANCE', fields_data)

    def CSH_DENOM_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CSH_DENOM_VIEW', fields_data)

    def CSH_DENOM_INS(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CSH_DENOM_INS', fields_data)

    def CSH_DENOM_UPD(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CSH_DENOM_UPD', fields_data)

    def CSH_DENOM_DEL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CSH_DENOM_DEL', fields_data)