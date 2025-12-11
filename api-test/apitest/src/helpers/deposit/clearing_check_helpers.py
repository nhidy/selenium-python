from ...utilities.requestUtility import RequestUtility

class ClearingCheckHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_clearing_check(self, payload):
        return self.requests_utility.post_deposit(f'api/ClearingCheck/View', payload)

    def simple_search_clearing_check(self, payload):
        return self.requests_utility.post_deposit(f'api/ClearingCheck/SimpleSearch', payload)

    def add_clearing_check(self, payload):
        return self.requests_utility.post_deposit(f'api/ClearingCheck/Create', payload)

    def update_clearing_check(self, payload):
        return self.requests_utility.post_deposit(f'api/ClearingCheck/Update', payload)

    def delete_clearing_check(self, payload):
        return self.requests_utility.post_deposit(f'api/ClearingCheck/Delete', payload)

    def list_clearing_check(self, payload):
        return self.requests_utility.post_deposit(f'', payload)
        # deposit/ClearingCheck

    def reject_clearing_check(self, payload):
        return self.requests_utility.post_deposit(f'', payload)
        # deposit/ClearingCheck/reject

    def process_clearing_check(self, payload):
        return self.requests_utility.post_deposit('', payload)
        # deposit/ClearingCheck/process