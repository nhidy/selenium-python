from ...utilities.requestUtility import RequestUtility

class StockStatusHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_stock_status(self, payload):
        return self.requests_utility.post_deposit(f'api/StockStatus/View', payload)

    def simple_search_stock_status(self, payload):
        return self.requests_utility.post_deposit(f'api/StockStatus/SimpleSearch', payload)

    def add_stock_status(self, payload):
        return self.requests_utility.post_deposit(f'api/StockStatus/Create', payload)

    def update_stock_status(self, payload):
        return self.requests_utility.post_deposit(f'api/StockStatus/Update', payload)

    def delete_stock_status(self, payload):
        return self.requests_utility.post_deposit(f'api/StockStatus/Delete', payload)