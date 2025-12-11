from ...utilities.requestUtility import RequestUtility

class CashStatementHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_cash_statement(self, payload):
        return self.requests_utility.post_cash(f'api/CashStatement/View', payload)

    def simple_search_cash_statement(self, payload):
        return self.requests_utility.post_cash(f'api/CashStatement/SimpleSearch', payload)

    def advanced_search_cash_statement(self, payload):
        return self.requests_utility.post_cash(f'api/CashStatement/AdvanceSearch', payload)

    def add_cash_statement(self, payload):
        return self.requests_utility.post_cash(f'api/CashStatement/Create', payload)

    def update_cash_statement(self, payload):
        return self.requests_utility.post_cash(f'api/CashStatement/Update', payload)

    def delete_cash_statement(self, payload):
        return self.requests_utility.post_cash(f'api/CashStatement/Delete', payload)