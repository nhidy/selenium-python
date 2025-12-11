from ...utilities.requestUtility import RequestUtility

class CashTransactionHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_cash_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/CashTransaction/View', payload)

    def simple_search_cash_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/CashTransaction/SimpleSearch', payload)

    def advanced_search_cash_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/CashTransaction/AdvanceSearch', payload)

    def add_cash_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/CashTransaction/Create', payload)

    def update_cash_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/CashTransaction/Update', payload)

    def delete_cash_transaction(self, payload):
        return self.requests_utility.post_cash(f'api/CashTransaction/Delete', payload)