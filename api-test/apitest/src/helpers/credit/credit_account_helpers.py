from ...utilities.requestUtility import RequestUtility

class CreditAccountHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def view_credit_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditAccount/View', payload)

    def simple_search_credit_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditAccount/SimpleSearch', payload)

    def advanced_search_credit_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditAccount/AdvanceSearch', payload)

    def add_credit_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditAccount/Create', payload)

    def update_credit_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditAccount/Update', payload)

    def delete_credit_account(self, payload):
        return self.requests_utility.post_credit(f'api/CreditAccount/Delete', payload)

    def list_ifc(self, payload):
        return self.requests_utility.post_credit(f'', payload)
        # credit/Account/ListIFC

    def list_disbursement(self, payload):
        return self.requests_utility.post_credit(f'', payload)
        # credit/Account/ListDebursement

    def list_principal(self, payload):
        return self.requests_utility.post_credit(f'', payload)
        # credit/Account/ListPrincipal

    def list_interest(self, payload):
        return self.requests_utility.post_credit(f'', payload)
        # credit/Account/ListInterest

    def list_payment(self, payload):
        return self.requests_utility.post_credit(f'', payload)
        # credit/Account/ListPayment

    def list_media(self, payload):
        return self.requests_utility.post_credit(f'', payload)
        # credit/Account/GetSignatureExecute

# ====================================== Workflow id ======================================
# Credit - Credit Account Infomation
    def CRD_SEARCH_SP_CREDIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SEARCH_SP_CREDIT', fields_data)

    def CRD_SEARCH_ADV_CREDIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SEARCH_ADV_CREDIT', fields_data)

    def CRD_VIEW_CREDIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_VIEW_CREDIT', fields_data)

    def CRD_UPDATE_CREDIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_UPDATE_CREDIT', fields_data)

    def CRD_DELETE_CREDIT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_DELETE_CREDIT', fields_data)

    def CRD_GEN_SCHD_PRIN_INT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_GEN_SCHD_PRIN_INT', fields_data)

    def CRD_GEN_SCHD_PRIN(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_GEN_SCHD_PRIN', fields_data)

    def CRD_GEN_SCHD_INT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_GEN_SCHD_INT', fields_data)