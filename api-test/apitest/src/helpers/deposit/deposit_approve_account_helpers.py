from ...utilities.requestUtility import RequestUtility

class DepositApproveAccountHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def simple_search_deposit_approve_account(self, payload):
        return self.requests_utility.post_deposit(f'api/ApproveDepositAccount/Search', payload)

    def advanced_search_deposit_approve_account(self, payload):
        return self.requests_utility.post_deposit(f'api/ApproveDepositAccount/AdvanceSearch', payload)

    def add_deposit_approve_account(self, payload):
        return self.requests_utility.post_deposit('api/ApproveDepositAccount/Create', payload)

    def view_deposit_approve_account_by_id(self, payload):
        return self.requests_utility.post_deposit(f'api/ApproveDepositAccount/View', payload)

    def update_deposit_approve_account(self, payload):
        return self.requests_utility.post_deposit(f'api/ApproveDepositAccount/Update', payload)

    def delete_deposit_approve_account(self, payload):
        return self.requests_utility.post_deposit(f'api/ApproveDepositAccount/Delete', payload)

    def get_deposit_approve_account_not_approve(self, payload):
        return self.requests_utility.post_deposit(f'', payload)
        # deposit/ApproveAccountModification/GetNotApproveTxRefId

    def view_modify_info_deposit_approve_account(self, payload): 
        return self.requests_utility.post_deposit(f'', payload)
        # deposit/ApproveAccountModification/GetInfoModify

    def approve_deposit_approve_account(self, payload): 
        return self.requests_utility.post_deposit(f'', payload)
        # deposit/ApproveAccountModification/ApproveModification

    def reject_deposit_approve_account(self, payload): 
        return self.requests_utility.get_deposit(f'',payload)
        # deposit/deposit/ApproveAccountModification/RejectModification