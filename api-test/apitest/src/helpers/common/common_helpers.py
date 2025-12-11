from ...utilities.requestUtility import RequestUtility

class CommonHelper(object):
    def __init__(self, user):
        self.requests_utility = user

# ====================================== Workflow id ======================================
# Lookup
    def ADM_LOOKUP_USER_ACCOUNT_BY_BRANCHID(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_LOOKUP_USER_ACCOUNT_BY_BRANCHID', fields_data)

    def ADM_LOOKUP_USER_ACCOUNT_CASHIER(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_LOOKUP_USER_ACCOUNT_CASHIER', fields_data)

    def ADM_LOOKUP_USER_ACCOUNT_CASHIER_OTHER_BRANCH(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ADM_LOOKUP_USER_ACCOUNT_CASHIER_OTHER_BRANCH', fields_data)

    def CRD_IFC_LOOKUP_BY_CURRENCY_AND_TRANSCODE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_IFC_LOOKUP_BY_CURRENCY_AND_TRANSCODE', fields_data)

    def CRD_IFC_LOOKUP_IFCTYPE_C(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_IFC_LOOKUP_IFCTYPE_C', fields_data)

    def CRD_IFC_LOOKUP_IFCTYPE_CO(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_IFC_LOOKUP_IFCTYPE_CO', fields_data)

    def CRD_IFC_LOOKUP_IFCTYPE_CO_BY_CURRENCY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_IFC_LOOKUP_IFCTYPE_CO_BY_CURRENCY', fields_data)

    def PMT_IFC_LOOKUP_IFCTYPE_CO_BY_CURRENCY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_IFC_LOOKUP_IFCTYPE_CO_BY_CURRENCY', fields_data)

    def CRD_IFC_LOOKUP_IFCTYPE_I_BY_CRDACNO(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_IFC_LOOKUP_IFCTYPE_I_BY_CRDACNO', fields_data)

    def CRD_IFC_LOOKUP_IFCTYPE_NOT_C(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_IFC_LOOKUP_IFCTYPE_NOT_C', fields_data)

    def CRD_IFC_LOOKUP_IFCTYPE_PP_PI_BY_CRDACNO(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_IFC_LOOKUP_IFCTYPE_PP_PI_BY_CRDACNO', fields_data)

    def CRD_LOOKUP_CRDCAT_BY_SPL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_LOOKUP_CRDCAT_BY_SPL', fields_data)

    def CRD_LOOKUP_CRDPL_BY_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_LOOKUP_CRDPL_BY_CTM', fields_data)

    def CRD_LOOKUP_CRDSPL_BY_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_LOOKUP_CRDSPL_BY_CTM', fields_data)

    def CRD_LOOKUP_CRDSPL_OD_BY_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CRD_LOOKUP_CRDSPL_OD_BY_CTM', fields_data)

    def CTM_LOOKUP_CTM_BY_CTMTYPE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'CTM_LOOKUP_CTM_BY_CTMTYPE', fields_data)

    def DPT_ERL_LKP_DATA_REF(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_ERL_LKP_DATA_REF', fields_data)

    def DPT_IFC_LOOKUP_BY_CURRENCY_AND_TRANSCODE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_IFC_LOOKUP_BY_CURRENCY_AND_TRANSCODE', fields_data)

    def DPT_IFC_LOOKUP_IFCTYPE_C(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_IFC_LOOKUP_IFCTYPE_C', fields_data)

    def DPT_IFC_LOOKUP_IFCTYPE_CO(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_IFC_LOOKUP_IFCTYPE_CO', fields_data)

    def DPT_IFC_LOOKUP_IFCTYPE_IT_BY_DPTACNO(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_IFC_LOOKUP_IFCTYPE_IT_BY_DPTACNO', fields_data)

    def DPT_IFC_LOOKUP_IFCTYPE_NOT_C(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_IFC_LOOKUP_IFCTYPE_NOT_C', fields_data)

    def DPT_LKP_DATA_PDMACC(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_LKP_DATA_PDMACC', fields_data)

    def DPT_LKP_DATA_PDOACC(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_LKP_DATA_PDOACC', fields_data)

    def DPT_LOOKUP_DEPOSIT_BY_MACNO(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_LOOKUP_DEPOSIT_BY_MACNO', fields_data)

    def DPT_GET_LIST_DPTCAT_API(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_GET_LIST_DPTCAT_API', fields_data)

    def DPT_OPN_LKP_DATA_CNCAT(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'DPT_OPN_LKP_DATA_CNCAT', fields_data)

    def PMT_IFC_LOOKUP_BY_CURRENCY_AND_TRANSCODE(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_IFC_LOOKUP_BY_CURRENCY_AND_TRANSCODE', fields_data)

    def PMT_IFC_LOOKUP_IFCTYPE_C(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_IFC_LOOKUP_IFCTYPE_C', fields_data)

    def PMT_IFC_LOOKUP_IFCTYPE_CO(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_IFC_LOOKUP_IFCTYPE_CO', fields_data)

    def PMT_KITT_LOOKUP_AGENTBANK(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_KITT_LOOKUP_AGENTBANK', fields_data)

    def PMT_LOOKUP_AGENTBANK(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_LOOKUP_AGENTBANK', fields_data)

    def PMT_LOOKUP_MESSAGE_INWARD_INTERNAL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_LOOKUP_MESSAGE_INWARD_INTERNAL', fields_data)

    def PMT_LOOKUP_MESSAGE_INWARD_INTERNATIONAL(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_LOOKUP_MESSAGE_INWARD_INTERNATIONAL', fields_data)

    def PMT_LOOKUP_PAYMENT_CATALOG(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'PMT_LOOKUP_PAYMENT_CATALOG', fields_data)

    def ACT_ACCHRT_LOOKUP(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_LOOKUP', fields_data)

    def ACT_ACCHRT_LOOKUP_BY_BRANCHID(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_LOOKUP_BY_BRANCHID', fields_data)

    def ACT_ACCHRT_LOOKUP_BY_BRANCHID_CURRENCY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_LOOKUP_BY_BRANCHID_CURRENCY', fields_data)

    def ACT_ACCHRT_LOOKUP_BY_BRANCHID_DPTACC(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_LOOKUP_BY_BRANCHID_DPTACC', fields_data)

    def ACT_ACCHRT_LOOKUP_BY_CURRENCY(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'ACT_ACCHRT_LOOKUP_BY_CURRENCY', fields_data)

    def SQL_LOOKUP_LISTNOT_CTM(self, fields_data):
        return self.requests_utility.get_p2_content_response_data(f'SQL_LOOKUP_LISTNOT_CTM', fields_data)
