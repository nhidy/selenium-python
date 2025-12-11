from ...utilities.requestUtility import RequestUtility

class DenominationTransactionHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_denomination_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationTransaction/View', payload)

    def simple_search_denomination_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationTransaction/SimpleSearch', payload)

    def advanced_search_denomination_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationTransaction/AdvanceSearch', payload)

    def add_denomination_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationTransaction/Create', payload)

    def update_denomination_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationTransaction/Update', payload)

    def delete_denomination_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationTransaction/Delete', payload)