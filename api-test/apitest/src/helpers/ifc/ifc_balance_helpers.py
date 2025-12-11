from ...utilities.requestUtility import RequestUtility

class IFCBalanceHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_ifc_balance(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCBalance/View', payload)

    def simple_search_ifc_balance(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCBalance/SimpleSearch', payload)

    def add_ifc_balance(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCBalance/Create', payload)

    def update_ifc_balance(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCBalance/Update', payload)

    def delete_ifc_balance(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCBalance/Delete', payload)