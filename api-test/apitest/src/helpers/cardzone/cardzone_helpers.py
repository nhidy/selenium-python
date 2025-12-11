from ...utilities.requestUtility import RequestUtility

class CardzoneHelper(object):
    def __init__(self, user):
        self.requests_utility = user

# ====================================== Workflow id deposit ======================================
    def DPT_MDP_ATM_DPT_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MDP_ATM_DPT_CZ', fields_data)

    def DPT_MDP_ATM_IBFT2_BNB_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MDP_ATM_IBFT2_BNB_CZ', fields_data)

    def DPT_MDP_POS_VOID_ONUS_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MDP_POS_VOID_ONUS_CZ', fields_data)

    def DPT_MDP_POS_VOID_OFF_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MDP_POS_VOID_OFF_CZ', fields_data)

    def DPT_MDP_MINI_WDR_OFF_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MDP_MINI_WDR_OFF_CZ', fields_data)

    def DPT_MDP_MINI_CLS_WDR_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MDP_MINI_CLS_WDR_CZ', fields_data)

    def DPT_MWR_ECOM_VOID_ONUS_CZ(self, fields_data): # code is "MWR" but business is "MDP"
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MWR_ECOM_VOID_ONUS_CZ', fields_data)

# ====================================== Workflow id withdrawal ======================================
    def DPT_MWR_ATM_WDR_ONUS_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MWR_ATM_WDR_ONUS_CZ', fields_data)

    def DPT_MWR_ATM_WDR_OFF_ISS_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MWR_ATM_WDR_OFF_ISS_CZ', fields_data)

    def DPT_MWR_ATM_IBFT2_ISS_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MWR_ATM_IBFT2_ISS_CZ', fields_data)

    def DPT_MWR_ATM_TOPUP_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MWR_ATM_TOPUP_CZ', fields_data)

    def DPT_MWR_POS_SALE_ONUS_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MWR_POS_SALE_ONUS_CZ', fields_data)

    def DPT_MWR_POS_SALE_OFF_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MWR_POS_SALE_OFF_CZ', fields_data)

    def DPT_MWR_POS_CAV_ONUS_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MWR_POS_CAV_ONUS_CZ', fields_data)

    def DPT_MWR_ECOM_SALE_ONUS_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MWR_ECOM_SALE_ONUS_CZ', fields_data)

    def DPT_MWR_MINI_CLS_RES_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_MWR_MINI_CLS_RES_CZ', fields_data)

# ====================================== Workflow id transfer ======================================
    def DPT_TRF_MINI_WDR_ONUS_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_TRF_MINI_WDR_ONUS_CZ', fields_data)

    def DPT_TRF_ATM_IBFT_ONUS_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_TRF_ATM_IBFT_ONUS_CZ', fields_data)

    def DPT_TRF_ATM_IBFT1_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_TRF_ATM_IBFT1_CZ', fields_data)

    def DPT_TRF_MINI_DPT_CZ(self, fields_data):
        return self.requests_utility.openapi_get_response_data_cz(f'DPT_TRF_MINI_DPT_CZ', fields_data)

# ====================================== reverse by execution id ======================================
    def openapi_reverse_by_execution_id(self, execution_id, transaction_date):
        return self.requests_utility.openapi_reverse_by_execution_id_cz(execution_id, transaction_date)

# ====================================== reverse by reference id ======================================
    def openapi_reverse_by_reference_id(self, reference_id):
        return self.requests_utility.openapi_reverse_by_reference_id_cz(reference_id)