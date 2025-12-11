from ...utilities.requestUtility import RequestUtility

class MomoneyHelper(object):
    def __init__(self, user):
        self.requests_utility = user

# ====================================== Workflow id deposit ======================================
    def DPT_MDP_MOMONEY(self, fields_data):
        return self.requests_utility.openapi_get_response_data_mo(f'DPT_MDP_MOMONEY', fields_data)

# ====================================== Workflow id withdrawal ======================================
    def DPT_MWR_MOMONEY(self, fields_data):
        return self.requests_utility.openapi_get_response_data_mo(f'DPT_MWR_MOMONEY', fields_data)

# ====================================== Workflow id transfer ======================================
    def DPT_TRF_MOMONEY(self, fields_data):
        return self.requests_utility.openapi_get_response_data_mo(f'DPT_TRF_MOMONEY', fields_data)

    def DPT_TRF_FEE_MOMONEY(self, fields_data):
        return self.requests_utility.openapi_get_response_data_mo(f'DPT_TRF_FEE_MOMONEY', fields_data)

# ====================================== reverse by execution id ======================================
    def openapi_reverse_by_execution_id(self, execution_id, transaction_date):
        return self.requests_utility.openapi_reverse_by_execution_id_mo(execution_id, transaction_date)

# ====================================== reverse by reference id ======================================
    def openapi_reverse_by_reference_id(self, reference_id):
        return self.requests_utility.openapi_reverse_by_reference_id_mo(reference_id)