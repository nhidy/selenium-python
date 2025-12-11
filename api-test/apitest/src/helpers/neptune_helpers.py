from ..utilities.requestUtility import RequestUtility

class NeptuneHelper(object):
    def __init__(self, user):
        self.requests_utility = user

    def get_execution_info(self, execution_id):
        return self.requests_utility.get_neptune(f'api/workflow/get-execution-info/{execution_id}')

    def execute_workflow(self, payload):
        return self.requests_utility.post_neptune(f'api/workflow/execute', payload)

    def execute_workflow_status_code(self, payload, expected_status):
        return self.requests_utility.post_neptune(f'api/workflow/execute', payload, expected_status)

    def get_execution_info_res_body(self, workflow_id, fields_data):
        return self.requests_utility.get_execution_info_res_body(workflow_id, fields_data)

# ====================================== BO ======================================
# Authenticate - Login
    def UMG_LOGIN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'UMG_LOGIN', fields_data)

# Authenticate - Logout


# Accounting - Account Chart
    def ACT_ACCHRT_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCHRT_SER_SIMPLE', fields_data)

    def ACT_ACCHRT_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCHRT_SER_ADVANCE', fields_data)

    def ACT_ACCHRT_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCHRT_VIEW', fields_data)

    def ACT_ACCHRT_INS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCHRT_INS', fields_data)

    def ACT_ACCHRT_UPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCHRT_UPD', fields_data)

    def ACT_ACCHRT_DEL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCHRT_DEL', fields_data)

# Accounting - Account Group
    def ACT_ACGRPDEF_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEF_SER_SIMPLE', fields_data)

    def ACT_ACGRPDEF_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEF_SER_ADVANCE', fields_data)

    def ACT_ACGRPDEF_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEF_VIEW', fields_data)

    def ACT_ACGRPDEF_INS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEF_INS', fields_data)

    def ACT_ACGRPDEF_UPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEF_UPD', fields_data)

    def ACT_ACGRPDEF_DEL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEF_DEL', fields_data)

# Accounting - Account Group Detail
    def ACT_ACGRPDEFDTL_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEFDTL_SER_SIMPLE', fields_data)

    def ACT_ACGRPDEFDTL_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEFDTL_SER_ADVANCE', fields_data)

    def ACT_ACGRPDEFDTL_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEFDTL_VIEW', fields_data)

    def ACT_ACGRPDEFDTL_INS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEFDTL_INS', fields_data)

    def ACT_ACGRPDEFDTL_UPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEFDTL_UPD', fields_data)

    def ACT_ACGRPDEFDTL_DEL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRPDEFDTL_DEL', fields_data)

# Accounting - Group Of Account
    def ACT_ACGRP_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRP_SER_SIMPLE', fields_data)

    def ACT_ACGRP_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRP_SER_ADVANCE', fields_data)

    def ACT_ACGRP_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRP_VIEW', fields_data)

    def ACT_ACGRP_INS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRP_INS', fields_data)

    def ACT_ACGRP_UPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRP_UPD', fields_data)

    def ACT_ACGRP_DEL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGRP_DEL', fields_data)

# Accounting - Extension Account
    def ACT_ACGLDEF_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGLDEF_SER_SIMPLE', fields_data)

    def ACT_ACGLDEF_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGLDEF_SER_ADVANCE', fields_data)

    def ACT_ACGLDEF_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGLDEF_VIEW', fields_data)

    def ACT_ACGLDEF_INS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGLDEF_INS', fields_data)

    def ACT_ACGLDEF_UPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGLDEF_UPD', fields_data)

    def ACT_ACGLDEF_DEL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACGLDEF_DEL', fields_data)

# Accounting - Common Account
    def ACT_ACCOM_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCOM_SER_SIMPLE', fields_data)

    def ACT_ACCOM_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCOM_SER_ADVANCE', fields_data)

    def ACT_ACCOM_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCOM_VIEW', fields_data)

    def ACT_ACCOM_INS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCOM_INS', fields_data)

    def ACT_ACCOM_UPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCOM_UPD', fields_data)

    def ACT_ACCOM_DEL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCOM_DEL', fields_data)

# Accounting - Clearing Account
    def ACT_ACCLR_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCLR_SER_SIMPLE', fields_data)

    def ACT_ACCLR_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCLR_SER_ADVANCE', fields_data)

    def ACT_ACCLR_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCLR_VIEW', fields_data)

    def ACT_ACCLR_INS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCLR_INS', fields_data)

    def ACT_ACCLR_UPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCLR_UPD', fields_data)

    def ACT_ACCLR_DEL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACCLR_DEL', fields_data)

# Accounting - Foreign Exchange Account
    def ACT_FXCLR_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_FXCLR_SER_SIMPLE', fields_data)

    def ACT_FXCLR_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_FXCLR_SER_ADVANCE', fields_data)

    def ACT_FXCLR_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_FXCLR_VIEW', fields_data)

    def ACT_FXCLR_INS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_FXCLR_INS', fields_data)

    def ACT_FXCLR_UPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_FXCLR_UPD', fields_data)

    def ACT_FXCLR_DEL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_FXCLR_DEL', fields_data)

# Accounting - Account Mapping
    def ACT_ACMAP_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACMAP_SER_SIMPLE', fields_data)

    def ACT_ACMAP_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACMAP_SER_ADVANCE', fields_data)

    def ACT_ACMAP_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACMAP_VIEW', fields_data)

    def ACT_ACMAP_INS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACMAP_INS', fields_data)

    def ACT_ACMAP_UPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACMAP_UPD', fields_data)

    def ACT_ACMAP_DEL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACMAP_DEL', fields_data)

# Accounting - Account Chart Master
# Accounting - Account Map Detail
# Accounting - Account Linkage


# Admin - Code List
    def ADM_SIMPLE_SEARCH_CODE_LIST(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_SIMPLE_SEARCH_CODE_LIST', fields_data)

    def ADM_ADVANCED_SEARCH_CODE_LIST(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_ADVANCED_SEARCH_CODE_LIST', fields_data)

    def ADM_VIEW_CODE_LIST(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_VIEW_CODE_LIST', fields_data)

    def ADM_INSERT_CODE_LIST(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_INSERT_CODE_LIST', fields_data)

    def ADM_UPDATE_CODE_LIST(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_UPDATE_CODE_LIST', fields_data)

    def ADM_DELETE_CODE_LIST(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_DELETE_CODE_LIST', fields_data)

# Admin - Country
    def ADM_SIMPLE_SEARCH_COUNTRY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_SIMPLE_SEARCH_COUNTRY', fields_data)

    def ADM_ADVANCED_SEARCH_COUNTRY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_ADVANCED_SEARCH_COUNTRY', fields_data)

    def ADM_VIEW_COUNTRY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_VIEW_COUNTRY', fields_data)

    def ADM_INSERT_COUNTRY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_INSERT_COUNTRY', fields_data)

    def ADM_UPDATE_COUNTRY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_UPDATE_COUNTRY', fields_data)

    def ADM_DELETE_COUNTRY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_DELETE_COUNTRY', fields_data)
    
# Admin - Currency
    def ADM_SIMPLE_SEARCH_CURRENCY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_SIMPLE_SEARCH_CURRENCY', fields_data)

    def ADM_ADVANCED_SEARCH_CURRENCY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_ADVANCED_SEARCH_CURRENCY', fields_data)

    def ADM_VIEW_CURRENCY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_VIEW_CURRENCY', fields_data)

    def ADM_INSERT_CURRENCY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_INSERT_CURRENCY', fields_data)

    def ADM_UPDATE_CURRENCY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_UPDATE_CURRENCY', fields_data)

    def ADM_DELETE_CURRENCY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_DELETE_CURRENCY', fields_data)

# Admin - Branch
    def ADM_SIMPLE_SEARCH_BRANCH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_SIMPLE_SEARCH_BRANCH', fields_data)

    def ADM_ADVANCED_SEARCH_BRANCH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_ADVANCED_SEARCH_BRANCH', fields_data)

    def ADM_VIEW_BRANCH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_VIEW_BRANCH', fields_data)

    def ADM_INSERT_BRANCH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_INSERT_BRANCH', fields_data)

    def ADM_UPDATE_BRANCH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_UPDATE_BRANCH', fields_data)

    def ADM_DELETE_BRANCH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_DELETE_BRANCH', fields_data)

# Admin - Department
    def ADM_SIMPLE_SEARCH_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_SIMPLE_SEARCH_DEPARTMENT', fields_data)

    def ADM_ADVANCED_SEARCH_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_ADVANCED_SEARCH_DEPARTMENT', fields_data)

    def ADM_VIEW_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_VIEW_DEPARTMENT', fields_data)

    def ADM_INSERT_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_INSERT_DEPARTMENT', fields_data)

    def ADM_UPDATE_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_UPDATE_DEPARTMENT', fields_data)

    def ADM_DELETE_DEPARTMENT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_DELETE_DEPARTMENT', fields_data)

# Admin - User Account
    def ADM_SIMPLE_SEARCH_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_SIMPLE_SEARCH_USER_ACCOUNT', fields_data)

    def ADM_ADVANCED_SEARCH_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_ADVANCED_SEARCH_USER_ACCOUNT', fields_data)

    def ADM_VIEW_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_VIEW_USER_ACCOUNT', fields_data)

    def ADM_INSERT_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_INSERT_USER_ACCOUNT', fields_data)

    def ADM_UPDATE_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_UPDATE_USER_ACCOUNT', fields_data)

    def ADM_DELETE_USER_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_DELETE_USER_ACCOUNT', fields_data)

# Admin - Policy
    def ADM_SIMPLE_SEARCH_USER_POLICY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_SIMPLE_SEARCH_USER_POLICY', fields_data)

    def ADM_ADVANCED_SEARCH_USER_POLICY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_ADVANCED_SEARCH_USER_POLICY', fields_data)

    def ADM_VIEW_USER_POLICY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_VIEW_USER_POLICY', fields_data)

    def ADM_INSERT_USER_POLICY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_INSERT_USER_POLICY', fields_data)

    def ADM_UPDATE_USER_POLICY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_UPDATE_USER_POLICY', fields_data)

    def ADM_DELETE_USER_POLICY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_DELETE_USER_POLICY', fields_data)

# Admin - System Parameters
# Admin - Import Data Files
# Admin - Process Imported File
# Admin - Inter Company
    def ADM_SIMPLE_SEARCH_COMPANY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_SIMPLE_SEARCH_COMPANY', fields_data)

    def ADM_ADVANCED_SEARCH_COMPANY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_ADVANCED_SEARCH_COMPANY', fields_data)

    def ADM_VIEW_COMPANY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_VIEW_COMPANY', fields_data)

    def ADM_INSERT_COMPANY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_INSERT_COMPANY', fields_data)

    def ADM_UPDATE_COMPANY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_UPDATE_COMPANY', fields_data)

    def ADM_DELETE_COMPANY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_DELETE_COMPANY', fields_data)

# Admin - Cost Center
# Admin - Product Code

# Admin - Role Profiles - Invoke - Approve - API [UserRight]

# Admin - Role Profiles - Add - Remove - API [UserRole]
    def ADM_VIEW_USER_ROLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_VIEW_USER_ROLE', fields_data)

    def ADM_INSERT_USER_ROLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_INSERT_USER_ROLE', fields_data)

    def ADM_DELETE_USER_ROLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_DELETE_USER_ROLE', fields_data)

# Admin - Role Profiles - User - Assignment - API [RoleOfUser]
# Admin - Role Profiles - Invoke Limit - Approve Limit - API [UserLimit]

# Admin - User Profile
# Admin - Bank
# Admin - Branch Linkage
# Admin - Calendar
# Admin - Branch
# Admin - Branch Param


# Deposit - Deposit Catalogue
    def DPT_SEARCH_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SEARCH_CATALOG', fields_data)

    def DPT_ADSEARCH_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ADSEARCH_CATALOG', fields_data)

    def DPT_VIEW_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_VIEW_CATALOG', fields_data)

    def DPT_INSERT_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_INSERT_CATALOG', fields_data)

    def DPT_UPDATE_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_UPDATE_CATALOG', fields_data)

    def DPT_DELETE_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_DELETE_CATALOG', fields_data)

# Deposit - Deposit Account
    def DPT_SEARCH_DEPOSIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SEARCH_DEPOSIT', fields_data)

    def DPT_ADSEARCH_DEPOSIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ADSEARCH_DEPOSIT', fields_data)

    def DPT_VIEW_DEPOSIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_VIEW_DEPOSIT', fields_data)

    def DPT_UPDATE_DEPOSIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_UPDATE_DEPOSIT', fields_data)

    def DPT_DELETE_DEPOSIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_DELETE_DEPOSIT', fields_data)

    def DPT_LIST_FDACC_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_LIST_FDACC_VIEW', fields_data)

    def DPT_UPDATE_LFA_MFA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_UPDATE_LFA_MFA', fields_data)

    def DPT_UPDATE_STATUS_DPT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_UPDATE_STATUS_DPT', fields_data)

# Deposit - Clearing Check
# Deposit - Approve Modify Deposit Account

# Deposit - Stock Inventory
    def DPT_SEARCH_STOCKINVENTORY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SEARCH_STOCKINVENTORY', fields_data)

    def DPT_ADSEARCH_STOCKINVENTORY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ADSEARCH_STOCKINVENTORY', fields_data)

    def DPT_VIEW_STOCKINVENTORY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_VIEW_STOCKINVENTORY', fields_data)

    def DPT_DELETE_STOCKINVENTORY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_DELETE_STOCKINVENTORY', fields_data)


# IFC - IFC Definition
    def IFC_SEARCH_IFC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_SEARCH_IFC', fields_data)

    def IFC_ADSEARCH_IFC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_ADSEARCH_IFC', fields_data)

    def IFC_VIEW_IFC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_VIEW_IFC', fields_data)

    def IFC_INSERT_IFC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_INSERT_IFC', fields_data)

    def IFC_UPDATE_IFC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_UPDATE_IFC', fields_data)

    def IFC_DELETE_IFC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_DELETE_IFC', fields_data)

# IFC - Tariff
    def IFC_SEARCH_TARIFF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_SEARCH_TARIFF', fields_data)

    def IFC_ADSEARCH_TARIFF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_ADSEARCH_TARIFF', fields_data)

    def IFC_VIEW_TARIFF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_VIEW_TARIFF', fields_data)

    def IFC_INSERT_TARIFF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_INSERT_TARIFF', fields_data)

    def IFC_UPDATE_TARIFF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_UPDATE_TARIFF', fields_data)

    def IFC_DELETE_TARIFF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_DELETE_TARIFF', fields_data)

# IFC - IFC Auto Fee
    def IFC_SEARCH_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_SEARCH_IFCAUTOFEE', fields_data)

    def IFC_ADSEARCH_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_ADSEARCH_IFCAUTOFEE', fields_data)

    def IFC_VIEW_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_VIEW_IFCAUTOFEE', fields_data)

    def IFC_INSERT_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_INSERT_IFCAUTOFEE', fields_data)

    def IFC_UPDATE_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_UPDATE_IFCAUTOFEE', fields_data)

    def IFC_DELETE_IFCAUTOFEE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'IFC_DELETE_IFCAUTOFEE', fields_data)


# Payment - Catalogue Definition
    def PMT_SEARCH_SP_PMTCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_SEARCH_SP_PMTCAT', fields_data)

    def PMT_SEARCH_ADV_PMTCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_SEARCH_ADV_PMTCAT', fields_data)

    def PMT_VIEW_PMTCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_VIEW_PMTCAT', fields_data)

    def PMT_INSERT_PMTCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_INSERT_PMTCAT', fields_data)

    def PMT_UPDATE_PMTCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_UPDATE_PMTCAT', fields_data)

    def PMT_DELETE_PMTCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_DELETE_PMTCAT', fields_data)

# Payment - Account Linkage
    def PMT_SEARCH_SP_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_SEARCH_SP_ACLINKAGE', fields_data)

    def PMT_SEARCH_ADV_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_SEARCH_ADV_ACLINKAGE', fields_data)

    def PMT_VIEW_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_VIEW_ACLINKAGE', fields_data)

    def PMT_INSERT_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_INSERT_ACLINKAGE', fields_data)

    def PMT_UPDATE_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_UPDATE_ACLINKAGE', fields_data)

    def PMT_DELETE_ACLINKAGE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_DELETE_ACLINKAGE', fields_data)

# Payment - Correspondent Bank
    def PMT_SEARCH_SP_AGENTBANK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_SEARCH_SP_AGENTBANK', fields_data)

    def PMT_SEARCH_ADV_AGENTBANK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_SEARCH_ADV_AGENTBANK', fields_data)

    def PMT_VIEW_AGENTBANK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_VIEW_AGENTBANK', fields_data)

    def PMT_INSERT_AGENTBANK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_INSERT_AGENTBANK', fields_data)

    def PMT_UPDATE_AGENTBANK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_UPDATE_AGENTBANK', fields_data)

    def PMT_DELETE_AGENTBANK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_DELETE_AGENTBANK', fields_data)

# Payment - Payment Queue
# Payment - Payment Queue Center
# Payment - Fund Transfer Via Fast

# Payment - Transactions
    def PMT_DELETE_PMTTRAN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_DELETE_PMTTRAN', fields_data)

# Payment - TXGINV
    def PMT_UPDATE_TXGINV(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_UPDATE_TXGINV', fields_data)


# Customer - Customer Information
    def SQL_SEARCH_CTM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_SEARCH_CTM', fields_data)

    def SQL_ADSEARCH_CTM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_ADSEARCH_CTM', fields_data)

    def SQL_VIEW_CTM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_VIEW_CTM', fields_data)

    def SQL_INSERT_CTM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_INSERT_CTM', fields_data)

    def SQL_UPDATE_CTM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_UPDATE_CTM', fields_data)

    def SQL_DELETE_CTM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_DELETE_CTM', fields_data)

# Customer - Approve Modify Customer
# Customer - Customer Group
    def SQL_SEARCH_CTMGRP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_SEARCH_CTMGRP', fields_data)

    def SQL_ADSEARCH_CTMGRP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_ADSEARCH_CTMGRP', fields_data)

    def SQL_VIEW_CTMGRP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_VIEW_CTMGRP', fields_data)

    def SQL_INSERT_CTMGRP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_INSERT_CTMGRP', fields_data)

    def SQL_UPDATE_CTMGRP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_UPDATE_CTMGRP', fields_data)

    def SQL_DELETE_CTMGRP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_DELETE_CTMGRP', fields_data)

    def CTM_GROUP_LIMIT_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_GROUP_LIMIT_VIEW', fields_data)

# Customer - Customer Linkage
    def SQL_SEARCH_CTMLKG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_SEARCH_CTMLKG', fields_data)

    def SQL_ADSEARCH_CTMLKG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_ADSEARCH_CTMLKG', fields_data)

    def SQL_VIEW_CTMLKG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_VIEW_CTMLKG', fields_data)

    def SQL_INSERT_CTMLKG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_INSERT_CTMLKG', fields_data)

    def SQL_UPDATE_CTMLKG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_UPDATE_CTMLKG', fields_data)

    def SQL_DELETE_CTMLKG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_DELETE_CTMLKG', fields_data)

# Customer - Credit Line
    def CTM_INSERT_CRLINE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_INSERT_CRLINE', fields_data)

    def CTM_DELETE_CRLINE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_DELETE_CRLINE', fields_data)

# Customer - Customer Media File
    def CTM_DELETE_MEDIA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_DELETE_MEDIA', fields_data)

# Customer - Check Customer Sanction
    def CTM_DELETE_SNC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_DELETE_SNC', fields_data)

    def CTM_IMPORT_SANCTION(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_IMPORT_SANCTION', fields_data)

    def CTM_IMPORT_KEY_SANCTION(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_IMPORT_KEY_SANCTION', fields_data)

    def CTM_EXPORT_SANCTION(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_EXPORT_SANCTION', fields_data)


# Cash - Cash Limit Position
# Cash - Denomination
    def CSH_DENOM_SER_SIMPLE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_DENOM_SER_SIMPLE', fields_data)

    def CSH_DENOM_SER_ADVANCE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_DENOM_SER_ADVANCE', fields_data)

    def CSH_DENOM_VIEW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_DENOM_VIEW', fields_data)

    def CSH_DENOM_INS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_DENOM_INS', fields_data)

    def CSH_DENOM_UPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_DENOM_UPD', fields_data)

    def CSH_DENOM_DEL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_DENOM_DEL', fields_data)

# Cash - Denomination Balance
# Cash - Denomination Statement
# Cash - Denomination Transaction
# Cash - Cash List
# Cash - Cash Statement
# Cash - Cash Transaction
# Cash - Cash Flow
# Cash - Denom


# Credit - Catalogue Definition
    def CRD_SEARCH_SP_CRDCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SEARCH_SP_CRDCAT', fields_data)

    def CRD_SEARCH_ADV_CRDCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SEARCH_ADV_CRDCAT', fields_data)

    def CRD_VIEW_CRDCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_VIEW_CRDCAT', fields_data)

    def CRD_INSERT_CRDCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_INSERT_CRDCAT', fields_data)

    def CRD_UPDATE_CRDCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_UPDATE_CRDCAT', fields_data)

    def CRD_DELETE_CRDCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_DELETE_CRDCAT', fields_data)

# Credit - Credit Account Infomation
    def CRD_SEARCH_SP_CREDIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SEARCH_SP_CREDIT', fields_data)

    def CRD_SEARCH_ADV_CREDIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SEARCH_ADV_CREDIT', fields_data)

    def CRD_VIEW_CREDIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_VIEW_CREDIT', fields_data)

    def CRD_UPDATE_CREDIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_UPDATE_CREDIT', fields_data)

    def CRD_DELETE_CREDIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_DELETE_CREDIT', fields_data)

    def CRD_GEN_SCHD_PRIN_INT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_GEN_SCHD_PRIN_INT', fields_data)

    def CRD_GEN_SCHD_PRIN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_GEN_SCHD_PRIN', fields_data)

    def CRD_GEN_SCHD_INT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_GEN_SCHD_INT', fields_data)

# Credit - Group Limit
    def CRD_SEARCH_SP_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SEARCH_SP_CRDGRPLM', fields_data)

    def CRD_SEARCH_ADV_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SEARCH_ADV_CRDGRPLM', fields_data)

    def CRD_VIEW_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_VIEW_CRDGRPLM', fields_data)

    def CRD_INSERT_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_INSERT_CRDGRPLM', fields_data)

    def CRD_UPDATE_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_UPDATE_CRDGRPLM', fields_data)

    def CRD_DELETE_CRDGRPLM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_DELETE_CRDGRPLM', fields_data)

# Credit - Product Limit
    def CRD_UPDATE_CRDPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_UPDATE_CRDPL', fields_data)

    def CRD_SEARCH_SP_CRDPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SEARCH_SP_CRDPL', fields_data)

    def CRD_SEARCH_ADV_CRDPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SEARCH_ADV_CRDPL', fields_data)

    def CRD_VIEW_CRDPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_VIEW_CRDPL', fields_data)

# Credit - Sub Product Limit
    def CRD_UPDATE_CRDSPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_UPDATE_CRDSPL', fields_data)

    def CRD_SEARCH_SP_CRDSPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SEARCH_SP_CRDSPL', fields_data)

    def CRD_SEARCH_ADV_CRDSPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SEARCH_ADV_CRDSPL', fields_data)

    def CRD_VIEW_CRDSPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_VIEW_CRDSPL', fields_data)

# FX - Exchange Rate


# Fixed Asset - Catalogue Definition
    def SQL_SEARCH_FACCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_SEARCH_FACCAT', fields_data)

    def SQL_ADSEARCH_FACCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_ADSEARCH_FACCAT', fields_data)

    def SQL_VIEW_FACCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_VIEW_FACCAT', fields_data)

    def SQL_INSERT_FACCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_INSERT_FACCAT', fields_data)

    def SQL_UPDATE_FACCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_UPDATE_FACCAT', fields_data)

    def SQL_DELETE_FACCAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_DELETE_FACCAT', fields_data)

# Fixed Asset - Fixed Asset And Tool
    def SQL_SEARCH_FACACT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_SEARCH_FACACT', fields_data)

    def SQL_ADSEARCH_FACACT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_ADSEARCH_FACACT', fields_data)

    def SQL_VIEW_FACACT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_VIEW_FACACT', fields_data)

    def SQL_UPDATE_FACACT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_UPDATE_FACACT', fields_data)

    def SQL_DELETE_FACACT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'SQL_DELETE_FACACT', fields_data)

# Mortgage - Catalogue Definition
    def MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_SIMPLE_SEARCH_MORTGAGE_CATALOG', fields_data)

    def MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_ADVANCED_SEARCH_MORTGAGE_CATALOG', fields_data)

    def MTG_VIEW_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_VIEW_MORTGAGE_CATALOG', fields_data)

    def MTG_INSERT_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_INSERT_MORTGAGE_CATALOG', fields_data)

    def MTG_UPDATE_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_UPDATE_MORTGAGE_CATALOG', fields_data)

    def MTG_DELETE_MORTGAGE_CATALOG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_DELETE_MORTGAGE_CATALOG', fields_data)

# Mortgage - Mortgage Account Information
    def MTG_SIMPLE_SEARCH_MORTGAGE_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_SIMPLE_SEARCH_MORTGAGE_ACCOUNT', fields_data)

    def MTG_ADVANCED_SEARCH_MORTGAGE_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_ADVANCED_SEARCH_MORTGAGE_ACCOUNT', fields_data)

    def MTG_VIEW_MORTGAGE_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_VIEW_MORTGAGE_ACCOUNT', fields_data)

    def MTG_UPDATE_MORTGAGE_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_UPDATE_MORTGAGE_ACCOUNT', fields_data)

    def MTG_DELETE_MORTGAGE_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_DELETE_MORTGAGE_ACCOUNT', fields_data)

    def MTG_INSERT_MORTGAGE_ACCOUNT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_INSERT_MORTGAGE_ACCOUNT', fields_data)

# Front Office
# Job

# ====================================== FO (288 FO) ======================================
    def CTM_APR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_APR', fields_data)

    def CTM_CAC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_CAC', fields_data)

    def CTM_CAS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_CAS', fields_data)

    def CTM_SEC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_SEC', fields_data)

    def CTM_EKYC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_EKYC', fields_data)

    def CTM_IKKC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_IKKC', fields_data)

    def CTM_IKYC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CTM_IKYC', fields_data)

    def DPT_OPN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_OPN', fields_data)

    def DPT_ODO(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ODO', fields_data)

    def DPT_CDP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CDP', fields_data)

    def DPT_CDT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CDT', fields_data)

    def DPT_MDP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_MDP', fields_data)

    def DPT_CWR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CWR', fields_data)

    def DPT_CWC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CWC', fields_data)

    def DPT_MWR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_MWR', fields_data)

    def DPT_CWM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CWM', fields_data)

    def DPT_TRF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_TRF', fields_data)

    def DPT_CIP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CIP', fields_data)

    def DPT_DIP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_DIP', fields_data)

    def DPT_MIP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_MIP', fields_data)

    def DPT_CCD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CCD', fields_data)

    def DPT_OCC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_OCC', fields_data)

    def DPT_OCR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_OCR', fields_data)

    def DPT_HIS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_HIS', fields_data)

    def DPT_SLS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SLS', fields_data)

    def DPT_CIQ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CIQ', fields_data)

    def DPT_IFC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_IFC', fields_data)

    def DPT_EMK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_EMK', fields_data)

    def DPT_CIS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CIS', fields_data)

    def DPT_SBI(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SBI', fields_data)

    def DPT_CER(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CER', fields_data)

    def DPT_CSS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CSS', fields_data)

    def DPT_CSU(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CSU', fields_data)

    def DPT_CSC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CSC', fields_data)

    def DPT_CSD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CSD', fields_data)

    def DPT_CSL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CSL', fields_data)

    def DPT_CSN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CSN', fields_data)

    def DPT_CSO(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CSO', fields_data)

    def DPT_SRG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SRG', fields_data)

    def DPT_SAB(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SAB', fields_data)

    def DPT_SAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SAT', fields_data)

    def DPT_CRT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CRT', fields_data)

    def DPT_CCR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CCR', fields_data)

    def DPT_SRA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SRA', fields_data)

    def DPT_CSA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CSA', fields_data)

    def DPT_FOC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_FOC', fields_data)

    def DPT_BLK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_BLK', fields_data)

    def DPT_CAS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CAS', fields_data)

    def DPT_RLS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_RLS', fields_data)

    def DPT_FEE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_FEE', fields_data)

    def DPT_CEI(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CEI', fields_data)

    def DPT_ERL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ERL', fields_data)

    def DPT_REC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_REC', fields_data)

    def DPT_DLS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_DLS', fields_data)

    def DPT_MLS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_MLS', fields_data)

    def DPT_CLS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CLS', fields_data)

    def DPT_COD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_COD', fields_data)

    def DPT_COG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_COG', fields_data)

    def DPT_APR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_APR', fields_data)

    def DPT_AOPC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_AOPC', fields_data)

    def DPT_AOPM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_AOPM', fields_data)

    def DPT_AOPT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_AOPT', fields_data)

    def DPT_CWT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CWT', fields_data)

    def DPT_MWT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_MWT', fields_data)

    def DPT_OPC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_OPC', fields_data)

    def DPT_OPM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_OPM', fields_data)

    def DPT_OPT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_OPT', fields_data)

    def DPT_TRT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_TRT', fields_data)

    def DPT_LAS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_LAS', fields_data)

    def DPT_DMN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_DMN', fields_data)

    def DPT_SAL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SAL', fields_data)

    def DPT_IPE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_IPE', fields_data)

    def DPT_MDC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_MDC', fields_data)

    def DPT_WDM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_WDM', fields_data)

    def DPT_TID(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_TID', fields_data)

    def DPT_ICR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ICR', fields_data)

    def DPT_SIQ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_SIQ', fields_data)

    def DPT_PIA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_PIA', fields_data)

    def DPT_AIF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_AIF', fields_data)

    def DPT_CIF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CIF', fields_data)

    def DPT_TIF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_TIF', fields_data)

    def DPT_MIF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_MIF', fields_data)

    def DPT_CCI(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CCI', fields_data)

    def DPT_CCW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CCW', fields_data)

    def DPT_CTS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CTS', fields_data)

    def DPT_RDP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_RDP', fields_data)

    def DPT_PRE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_PRE', fields_data)

    def DPT_RAC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_RAC', fields_data)

    def DPT_IAJ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_IAJ', fields_data)

    def DPT_AIP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_AIP', fields_data)

    def DPT_CLSD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CLSD', fields_data)

    def DPT_ACI(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ACI', fields_data)

    def DPT_RNW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_RNW', fields_data)

    def DPT_ROV(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ROV', fields_data)

    def DPT_CCL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CCL', fields_data)

    def DPT_FCL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_FCL', fields_data)

    def DPT_DMF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_DMF', fields_data)

    def DPT_CMF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CMF', fields_data)

    def DPT_ATL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ATL', fields_data)

    def DPT_ANI(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ANI', fields_data)

    def DPT_DEPM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_DEPM', fields_data)

    def DPT_DEP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_DEP', fields_data)

    def DPT_ACT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ACT', fields_data)

    def DPT_ICLR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ICLR', fields_data)

    def DPT_IAC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_IAC', fields_data)

    def DPT_CRI(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CRI', fields_data)

    def DPT_TIP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_TIP', fields_data)

    def DPT_INP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_INP', fields_data)

    def DPT_ISP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ISP', fields_data)

    def DPT_IDU(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_IDU', fields_data)

    def DPT_EIP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_EIP', fields_data)

    def DPT_CWP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CWP', fields_data)

    def DPT_OPNF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_OPNF', fields_data)

    def DPT_PSP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_PSP', fields_data)

    def DPT_PRD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_PRD', fields_data)

    def DPT_PDU(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_PDU', fields_data)

    def DPT_PPB(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_PPB', fields_data)

    def DPT_RADR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_RADR', fields_data)

    def DPT_RIS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_RIS', fields_data)

    def DPT_MRN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_MRN', fields_data)

    def DPT_RID(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_RID', fields_data)

    def DPT_RVS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_RVS', fields_data)

    def DPT_CST(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CST', fields_data)

    def DPT_INQ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_INQ', fields_data)

    def DPT_TIO(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_TIO', fields_data)

    def DPT_WDRM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_WDRM', fields_data)

    def DPT_WDR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_WDR', fields_data)

    def DPT_COC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_COC', fields_data)

    def DPT_MNY(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_MNY', fields_data)

    def DPT_IPA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_IPA', fields_data)

    def DPT_ROLLOVER(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ROLLOVER', fields_data)

    def CRD_PLO(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_PLO', fields_data)

    def CRD_PLA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_PLA', fields_data)

    def CRD_SPLO(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SPLO', fields_data)

    def CRD_SPLA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SPLA', fields_data)

    def CRD_OPN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_OPN', fields_data)

    def CRD_APR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_APR', fields_data)

    def CRD_CDR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_CDR', fields_data)

    def CRD_MDR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_MDR', fields_data)

    def CRD_TDR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_TDR', fields_data)

    def CRD_MIPM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_MIPM', fields_data)

    def CRD_CIPM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_CIPM', fields_data)

    def CRD_IPCT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_IPCT', fields_data)

    def CRD_EXT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_EXT', fields_data)

    def CRD_REJ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_REJ', fields_data)

    def CRD_FOC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_FOC', fields_data)

    def CRD_FCD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_FCD', fields_data)

    def CRD_FCG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_FCG', fields_data)

    def CRD_RFC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_RFC', fields_data)

    def CRD_RFD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_RFD', fields_data)

    def CRD_FRG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_FRG', fields_data)

    def CRD_BLK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_BLK', fields_data)

    def CRD_CAS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_CAS', fields_data)

    def CRD_CLA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_CLA', fields_data)

    def CRD_CLS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_CLS', fields_data)

    def CRD_PIW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_PIW', fields_data)

    def CRD_IFC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_IFC', fields_data)

    def CRD_IHIS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_IHIS', fields_data)

    def CRD_RSCH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_RSCH', fields_data)

    def CRD_GSCH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_GSCH', fields_data)

    def CRD_HIS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_HIS', fields_data)

    def CRD_SCR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SCR', fields_data)

    def CRD_SPAD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SPAD', fields_data)

    def CRD_SPLC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SPLC', fields_data)

    def CRD_PLAD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_PLAD', fields_data)

    def CRD_PLC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_PLC', fields_data)

    def CRD_NPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_NPL', fields_data)

    def CRD_AIPV(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_AIPV', fields_data)

    def CRD_WOF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_WOF', fields_data)

    def CRD_AIF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_AIF', fields_data)

    def CRD_AIPB(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_AIPB', fields_data)

    def CRD_ANI(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_ANI', fields_data)

    def CRD_API(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_API', fields_data)

    def CRD_CCS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_CCS', fields_data)

    def CRD_CIF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_CIF', fields_data)

    def CRD_CPM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_CPM', fields_data)

    def CRD_DOD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_DOD', fields_data)

    def CRD_DRW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_DRW', fields_data)

    def CRD_DRWM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_DRWM', fields_data)

    def CRD_FCL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_FCL', fields_data)

    def CRD_FOD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_FOD', fields_data)

    def CRD_IAJ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_IAJ', fields_data)

    def CRD_INQ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_INQ', fields_data)

    def CRD_IOD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_IOD', fields_data)

    def CRD_MICBK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_MICBK', fields_data)

    def CRD_MIF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_MIF', fields_data)

    def CRD_OAJ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_OAJ', fields_data)

    def CRD_PCT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_PCT', fields_data)

    def CRD_PIA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_PIA', fields_data)

    def CRD_PMC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_PMC', fields_data)

    def CRD_POD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_POD', fields_data)

    def CRD_RAC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_RAC', fields_data)

    def CRD_RBD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_RBD', fields_data)

    def CRD_RID(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_RID', fields_data)

    def CRD_RLS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_RLS', fields_data)

    def CRD_RPD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_RPD', fields_data)

    def CRD_RVS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_RVS', fields_data)

    def CRD_SPLI(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_SPLI', fields_data)

    def CRD_TID(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_TID', fields_data)

    def CRD_TIF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_TIF', fields_data)

    def CRD_TLI(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_TLI', fields_data)

    def CRD_TLP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_TLP', fields_data)

    def CRD_TOD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_TOD', fields_data)

    def CRD_TODC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_TODC', fields_data)

    def CRD_TODO(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_TODO', fields_data)

    def CRD_PCM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_PCM', fields_data)

    def CRD_RVW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CRD_RVW', fields_data)

    def MTG_OPN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_OPN', fields_data)

    def MTG_APR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_APR', fields_data)

    def MTG_SCR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_SCR', fields_data)

    def MTG_RLS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_RLS', fields_data)

    def MTG_BLK(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_BLK', fields_data)

    def MTG_BRL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_BRL', fields_data)

    def MTG_DCR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_DCR', fields_data)

    def MTG_INR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_INR', fields_data)

    def MTG_RTN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_RTN', fields_data)

    def MTG_CLS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_CLS', fields_data)

    def MTG_REA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_REA', fields_data)

    def MTG_HDT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_HDT', fields_data)

    def MTG_HIS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_HIS', fields_data)

    def MTG_INQ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_INQ', fields_data)

    def MTG_KPT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_KPT', fields_data)

    def MTG_KRL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_KRL', fields_data)

    def MTG_RPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_RPL', fields_data)

    def MTG_SPL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_SPL', fields_data)

    def MTG_TRL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_TRL', fields_data)

    def MTG_TSC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'MTG_TSC', fields_data)

    def PMT_OIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_OIT', fields_data)

    def PMT_ODT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_ODT', fields_data)

    def PMT_OITT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_OITT', fields_data)

    def PMT_ODTF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_ODTF', fields_data)

    def PMT_IIT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_IIT', fields_data)

    def PMT_IDT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_IDT', fields_data)

    def PMT_IITT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_IITT', fields_data)

    def PMT_KITT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_KITT', fields_data)

    def PMT_OICT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_OICT', fields_data)

    def PMT_OITA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_OITA', fields_data)

    def PMT_ITTC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_ITTC', fields_data)

    def PMT_APOW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_APOW', fields_data)

    def PMT_APR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_APR', fields_data)

    def PMT_APRF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_APRF', fields_data)

    def PMT_APR1(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_APR1', fields_data)

    def PMT_REJ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_REJ', fields_data)

    def PMT_REJ1(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_REJ1', fields_data)

    def PMT_RJOW(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_RJOW', fields_data)

    def PMT_RJRF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_RJRF', fields_data)

    def PMT_INQ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_INQ', fields_data)

    def PMT_ADV(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_ADV', fields_data)

    def PMT_FCL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_FCL', fields_data)

    def PMT_GIL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_GIL', fields_data)

    def PMT_GOL(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_GOL', fields_data)

    def PMT_IDTF(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_IDTF', fields_data)

    def PMT_IDTR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_IDTR', fields_data)

    def PMT_KQCB(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_KQCB', fields_data)

    def PMT_KQCH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_KQCH', fields_data)

    def PMT_KQTB(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_KQTB', fields_data)

    def PMT_KQTH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_KQTH', fields_data)

    def PMT_MAT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_MAT', fields_data)

    def PMT_OFTA(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_OFTA', fields_data)

    def PMT_OTFR(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_OTFR', fields_data)

    def PMT_PRC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'PMT_PRC', fields_data)

    def CSH_MOV(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_MOV', fields_data)

    def CSH_DNM(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_DNM', fields_data)

    def CSH_ADJ(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_ADJ', fields_data)

    def FAC_OPN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_OPN', fields_data)

    def FAC_PBC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_PBC', fields_data)

    def FAC_PBD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_PBD', fields_data)

    def FAC_PBG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_PBG', fields_data)

    def FAC_SBC(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_SBC', fields_data)

    def FAC_SBD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_SBD', fields_data)

    def FAC_SBG(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_SBG', fields_data)

    def FAC_TFB(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_TFB', fields_data)

    def FAC_DEP(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_DEP', fields_data)

    def FAC_CLS(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_CLS', fields_data)

    def FAC_CED(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'FAC_CED', fields_data)

    def ACT_MAN(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_MAN', fields_data)

    def ACT_FEE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_FEE', fields_data)

    def ACT_GFEE(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_GFEE', fields_data)

    def CSH_CSH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_CSH', fields_data)

    def CSH_DPT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_DPT', fields_data)

    def CSH_ACT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'CSH_ACT', fields_data)

    def DPT_CSH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_CSH', fields_data)

    def DPT_DPT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_DPT', fields_data)

    def DPT_ACT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'DPT_ACT', fields_data)

    def ACT_CSH(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_CSH', fields_data)

    def ACT_DPT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_DPT', fields_data)

    def ACT_ACT(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ACT_ACT', fields_data)

    def ADM_FXD(self, fields_data):
        return self.requests_utility.get_execution_info_res_body(f'ADM_FXD', fields_data)