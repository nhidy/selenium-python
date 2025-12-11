from ...utilities.requestUtility import RequestUtility

class AdminHelper(object):
    def __init__(self, user):
        self.requests_utility = user

# ====================================== Workflow id ======================================
# Login
    def UMG_LOGIN(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'UMG_LOGIN', fields_data)
    
# Admin - Branch
    def ADM_SIMPLE_SEARCH_BRANCH(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_SIMPLE_SEARCH_BRANCH', fields_data)

    def ADM_ADVANCED_SEARCH_BRANCH(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_ADVANCED_SEARCH_BRANCH', fields_data)