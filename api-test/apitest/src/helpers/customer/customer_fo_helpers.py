from ...utilities.requestUtility import RequestUtility

class CustomerFOHelper(object):
    def __init__(self, user):
        self.requests_utility = user

# ====================================== Workflow id ======================================
# Customer - FO
    def CTM_APR(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CTM_APR', fields_data)