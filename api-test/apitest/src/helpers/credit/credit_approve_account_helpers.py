from ...utilities.requestUtility import RequestUtility

class CreditApproveAccountHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_credit_approve_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditApproveAccount/View', payload)

    def simple_search_credit_approve_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditApproveAccount/SimpleSearch', payload)

    def advance_search_credit_approve_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditApproveAccount/AdvanceSearch', payload)

    def add_credit_approve_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditApproveAccount/Create', payload)

    def update_credit_approve_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditApproveAccount/Update', payload)

    def approve_credit_approve_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditApproveAccount/Approve', payload)

    def reject_credit_approve_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditApproveAccount/Reject', payload)

    def get_credit_approve_account_not_approve(self, payload):
        return self.requests_utility.post_credit(f'', payload)
        # credit/ApproveAccountModification/GetNotApproveTxRefId

    def view_modify_info_credit_approve_account(self, payload): 
        return self.requests_utility.post_credit(f'', payload)
        # credit/ApproveAccountModification/GetInfoModify