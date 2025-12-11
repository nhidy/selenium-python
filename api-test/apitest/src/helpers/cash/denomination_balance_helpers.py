from ...utilities.requestUtility import RequestUtility

class DenominationBalanceHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_denomination_balance(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationBalance/View', payload)

    def simple_search_denomination_balance(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationBalance/SimpleSearch', payload)

    def advanced_search_denomination_balance(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationBalance/AdvanceSearch', payload)

    def add_denomination_balance(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationBalance/Create', payload)

    def update_denomination_balance(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationBalance/Update', payload)

    def delete_denomination_balance(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationBalance/Delete', payload)