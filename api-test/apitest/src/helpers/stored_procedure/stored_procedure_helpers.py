from ...utilities.requestUtility import RequestUtility

class StoredProcedureHelper(object):
    def __init__(self, user):
        self.requests_utility = user

# ====================================== Workflow id FO ======================================
    def DPT_CDP(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_CDP', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_CWR(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_CWR', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ACT_DPT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ACT_DPT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_OPN(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_OPN', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_APR(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_APR', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def CSH_MOV(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'CSH_MOV', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def CTM_APR(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'CTM_APR', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def CTM_CAS(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'CTM_CAS', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ACT_CSH(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ACT_CSH', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ACT_MAN(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ACT_MAN', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_TRF(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_TRF', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_SBI(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_SBI', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_DLS(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_DLS', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def CSH_DNM(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'CSH_DNM', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_CER(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_CER', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_ACT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_ACT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_CWC(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_CWC', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_HIS(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_HIS', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ACT_ACT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ACT_ACT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_MWR(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_MWR', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_FBI(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_FBI', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def CSH_ACT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'CSH_ACT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def CRD_EXT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'CRD_EXT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_MDP(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_MDP', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_DPT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_DPT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

# CAC FO CHUA CHUYEN STORED PROCEDURE, KHOI TAO DE TAO DU LIEU TEST
    def DPT_CAS(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_CAS', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_OPAL(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_OPAL', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_CLS(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_CLS', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_BLK(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_BLK', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_SRG(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_SRG', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_SAT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_SAT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_CCR(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_CCR', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_CIS(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_CIS', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_CTS(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_CTS', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_ADSEARCH_STOCKINVENTORY(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_ADSEARCH_STOCKINVENTORY', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

# ====================================== Workflow id BO ======================================
    def SQL_INSERT_MEDIA(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'SQL_INSERT_MEDIA', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def SQL_APPROVE_MEDIA(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'SQL_APPROVE_MEDIA', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def SQL_UPDATE_CTM(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'SQL_UPDATE_CTM', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def PRINT_CUSTOMER_INFO(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'PRINT_CUSTOMER_INFO', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def SQL_CTM_APR(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'SQL_CTM_APR', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ADM_REFRESH_BRANCH(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ADM_REFRESH_BRANCH', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def SQL_INSERT_CTM(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'SQL_INSERT_CTM', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ADM_REFRESH_BRANCH_BY_USER(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ADM_REFRESH_BRANCH_BY_USER', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ACT_ACCHRT_SER_SIMPLE(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ACT_ACCHRT_SER_SIMPLE', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_DELETE_ACCOUNTLINKAGE(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_DELETE_ACCOUNTLINKAGE', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ACT_ACCHRT_INS(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ACT_ACCHRT_INS', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ADM_CLOSE_BRANCH(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ADM_CLOSE_BRANCH', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ADM_OPEN_BRANCH(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ADM_OPEN_BRANCH', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def CRD_SEARCH_SP_CREDIT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'CRD_SEARCH_SP_CREDIT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_UPDATE_DEPOSIT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_UPDATE_DEPOSIT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def PMT_SEARCH_SP_QUEUE_INWAR(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'PMT_SEARCH_SP_QUEUE_INWAR', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ADM_ADVANCED_SEARCH_ROLE_OF_USER(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ADM_ADVANCED_SEARCH_ROLE_OF_USER', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def FX_FXRATE_GETFXRATE(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'FX_FXRATE_GETFXRATE', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ADM_SIMPLE_SEARCH_USER_ACCOUNT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ADM_SIMPLE_SEARCH_USER_ACCOUNT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def TRS_SEARCH_ACCOUNT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'TRS_SEARCH_ACCOUNT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def CRD_VIEW_CREDIT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'CRD_VIEW_CREDIT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_VIEW_MODIFY_EXT_FIELD(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_VIEW_MODIFY_EXT_FIELD', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def DPT_APPROVE_MODIFY(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'DPT_APPROVE_MODIFY', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def TRS_VIEW_ACCOUNT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'TRS_VIEW_ACCOUNT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)

    def ADM_UPDATE_LIST_USER_RIGHT(self, fields_data, reversal_execution_id=None, approved_execution_id=None):
        return self.requests_utility.get_response_data(f'ADM_UPDATE_LIST_USER_RIGHT', fields_data, reversal_execution_id=reversal_execution_id, approved_execution_id=approved_execution_id)