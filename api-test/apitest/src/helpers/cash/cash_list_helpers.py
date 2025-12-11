from ...utilities.requestUtility import RequestUtility

class CashListHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_cash_list(self, payload):
        return self.requests_utility.post_cash(f'api/CashList/View', payload)

    def get_cash_account(self, payload):
        return self.requests_utility.post_cash(f'api/CashList/GetCashAccount', payload)

    def simple_search_cash_list(self, payload):
        return self.requests_utility.post_cash(f'api/CashList/SimpleSearch', payload)

    def advanced_search_cash_list(self, payload):
        return self.requests_utility.post_cash(f'api/CashList/AdvanceSearch', payload)

    def add_cash_list(self, payload):
        return self.requests_utility.post_cash(f'api/CashList/Create', payload)

    def update_cash_list(self, payload):
        return self.requests_utility.post_cash(f'api/CashList/Update', payload)

    def delete_cash_list(self, payload):
        return self.requests_utility.post_cash(f'api/CashList/Delete', payload)