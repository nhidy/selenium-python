from ...utilities.requestUtility import RequestUtility

class ForeignExchangeAccountHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_foreign_exchange_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ForeignExchangeAccountDefinition/View', payload)

    def simple_search_foreign_exchange_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ForeignExchangeAccountDefinition/SimpleSearch', payload)

    def advanced_search_foreign_exchange_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ForeignExchangeAccountDefinition/AdvanceSearch', payload)

    def add_foreign_exchange_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ForeignExchangeAccountDefinition/Create', payload)

    def update_foreign_exchange_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ForeignExchangeAccountDefinition/Update', payload)

    def delete_foreign_exchange_account(self, payload):
        return self.requests_utility.post_accounting(f'api/ForeignExchangeAccountDefinition/Delete', payload)

# ====================================== Workflow id ======================================
# Accounting - Foreign Exchange Account
    def ACT_FXCLR_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_FXCLR_SER_SIMPLE', fields_data)

    def ACT_FXCLR_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_FXCLR_SER_ADVANCE', fields_data)

    def ACT_FXCLR_VIEW(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_FXCLR_VIEW', fields_data)

    def ACT_FXCLR_INS(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_FXCLR_INS', fields_data)

    def ACT_FXCLR_UPD(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_FXCLR_UPD', fields_data)

    def ACT_FXCLR_DEL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_FXCLR_DEL', fields_data)