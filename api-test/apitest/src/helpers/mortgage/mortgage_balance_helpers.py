from ...utilities.requestUtility import RequestUtility

class MortgageBalanceHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_mortgage_balance(self, search_text=None, page_index=None, page_size=None):
        if not search_text:
            search_text = ''
        if not page_index:
            page_index = 0
        if not page_size:
            page_size = 2147483647
        return self.requests_utility.get_mortgage(f'api/MortgageBalance/Search?SearchText={search_text}&PageIndex={page_index}&PageSize={page_size}')

    def advanced_search_mortgage_balance(self, payload):
        return self.requests_utility.post_mortgage(f'api/MortgageBalance/Search', payload)

    def add_mortgage_balance(self, payload):
        return self.requests_utility.post_mortgage('api/MortgageBalance/Create', payload)

    def view_mortgage_balance(self, id):
        return self.requests_utility.get_mortgage(f'api/MortgageBalance/View/{id}')

    def update_mortgage_balance(self, payload):
        return self.requests_utility.put_mortgage(f'api/MortgageBalance/Update', payload)

    def delete_mortgage_balance(self, payload):
        return self.requests_utility.delete_mortgage(f'api/MortgageBalance/Delete', payload)