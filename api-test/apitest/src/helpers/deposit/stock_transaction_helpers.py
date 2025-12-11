from ...utilities.requestUtility import RequestUtility

class StockTransactionHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_stock_transaction(self, payload):
        return self.requests_utility.post_deposit(f'api/StockTransaction/View', payload)

    def simple_search_stock_transaction(self, payload):
        return self.requests_utility.post_deposit(f'api/StockTransaction/SimpleSearch', payload)

    def add_stock_transaction(self, payload):
        return self.requests_utility.post_deposit(f'api/StockTransaction/Create', payload)

    def update_stock_transaction(self, payload):
        return self.requests_utility.post_deposit(f'api/StockTransaction/Update', payload)

    def delete_stock_transaction(self, payload):
        return self.requests_utility.post_deposit(f'api/StockTransaction/Delete', payload)