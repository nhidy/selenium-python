from ...utilities.requestUtility import RequestUtility

class DepositFOHelper(object):
    def __init__(self, user):
        self.requests_utility = user

# ====================================== Workflow id ======================================
# Deposit - FO
    # def DPT_OPN(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'DPT_OPN', fields_data)
    
    def DPT_OPN(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_OPN', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    # def DPT_APR(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'DPT_APR', fields_data)

    def DPT_APR(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_APR', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    # def DPT_CDP(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'DPT_CDP', fields_data)

    def DPT_CDP(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_CDP', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)
    
    # def DPT_BLK(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'DPT_BLK', fields_data)

    def DPT_BLK(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_BLK', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_TRF(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_TRF', fields_data)

    # def DPT_ADSEARCH_CATALOG(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'DPT_ADSEARCH_CATALOG', fields_data)

    # def DPT_VIEW_CATALOG(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'DPT_VIEW_CATALOG', fields_data)

    # def DPT_INSERT_CATALOG(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'DPT_INSERT_CATALOG', fields_data)

    # def DPT_UPDATE_CATALOG(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'DPT_UPDATE_CATALOG', fields_data)

    # def DPT_DELETE_CATALOG(self, fields_data):
    #     return self.requests_utility.get_p2_content_response_data(f'DPT_DELETE_CATALOG', fields_data)