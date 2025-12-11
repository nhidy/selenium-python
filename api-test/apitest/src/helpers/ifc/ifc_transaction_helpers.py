from ...utilities.requestUtility import RequestUtility

class IFCTransactionHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_ifc_transaction(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTransaction/View', payload)

    def simple_search_ifc_transaction(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTransaction/SimpleSearch', payload)

    def advanced_search_ifc_transaction(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTransaction/AdvanceSearch', payload)

    def add_ifc_transaction(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTransaction/Create', payload)

    def update_ifc_transaction(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTransaction/Update', payload)

    def delete_ifc_transaction(self, payload):
        return self.requests_utility.post_ifc(f'api/IFCTransaction/Delete', payload)