from ...utilities.requestUtility import RequestUtility

class DenominationStatementHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_denomination_statement(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationStatement/View', payload)

    def simple_search_denomination_statement(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationStatement/SimpleSearch', payload)

    def advanced_search_denomination_statement(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationStatement/AdvanceSearch', payload)

    def add_denomination_statement(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationStatement/Create', payload)

    def update_denomination_statement(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationStatement/Update', payload)

    def delete_denomination_statement(self, payload):
        return self.requests_utility.post_cash(f'api/DenominationStatement/Delete', payload)