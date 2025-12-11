from ...utilities.requestUtility import RequestUtility

class CreditFOHelper(object):
    def __init__(self, user):
        self.requests_utility = user

# ====================================== Workflow id ======================================
# Credit - FO
    def CRD_PLO(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_PLO', fields_data)

    def CRD_PLA(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_PLA', fields_data)

    def CRD_SPLO(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SPLO', fields_data)

    def CRD_SPLA(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_SPLA', fields_data)

    def CRD_OPN(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_OPN', fields_data)

    def CRD_APR(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_APR', fields_data)

    def CRD_TDR(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_TDR', fields_data)