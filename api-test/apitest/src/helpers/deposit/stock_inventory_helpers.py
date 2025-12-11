from ...utilities.requestUtility import RequestUtility

class StockInventoryHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_stock_inventory(self, payload):
        return self.requests_utility.post_deposit(f'api/StockInventory/View', payload)

    def simple_search_stock_inventory(self, payload):
        return self.requests_utility.post_deposit(f'api/StockInventory/SimpleSearch', payload)

    def advanced_search_stock_inventory(self, payload):
        return self.requests_utility.post_deposit(f'api/StockInventory/AdvanceSearch', payload)

    def add_stock_inventory(self, payload):
        return self.requests_utility.post_deposit(f'api/StockInventory/Create', payload)

    def update_stock_inventory(self, payload):
        return self.requests_utility.post_deposit(f'api/StockInventory/Update', payload)

    def delete_stock_inventory(self, payload):
        return self.requests_utility.post_deposit(f'api/StockInventory/Delete', payload)

# ====================================== Workflow id ======================================
# Deposit - Stock Inventory
    def DPT_SEARCH_STOCKINVENTORY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_SEARCH_STOCKINVENTORY', fields_data)

    def DPT_ADSEARCH_STOCKINVENTORY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_ADSEARCH_STOCKINVENTORY', fields_data)

    def DPT_VIEW_STOCKINVENTORY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_VIEW_STOCKINVENTORY', fields_data)

    def DPT_DELETE_STOCKINVENTORY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_DELETE_STOCKINVENTORY', fields_data)