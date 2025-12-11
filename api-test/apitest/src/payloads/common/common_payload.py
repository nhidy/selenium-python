from datetime import datetime

class CommonPayload(object):
    def adm_lookup_user_account_by_branchid(self, branch_code=None, page_index=None, page_size=None):
        if not branch_code:
            branch_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "branch_code": branch_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def adm_lookup_user_account_cashier(self, branch_code=None, page_index=None, page_size=None):
        if not branch_code:
            branch_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "branch_code": branch_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def adm_lookup_user_account_cashier_other_branch(self, branch_code=None, page_index=None, page_size=None):
        if not branch_code:
            branch_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "branch_code": branch_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def crd_ifc_lookup_by_currency_and_transcode(self, currency_code=None, tran_code=None, page_index=None, page_size=None):
        if not currency_code:
            currency_code=''
        if not tran_code:
            tran_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "currency_code": currency_code,
            "tran_code": tran_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def crd_ifc_lookup_ifctype_c(self, currency_code=None, page_index=None, page_size=None):
        if not currency_code:
            currency_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "currency_code": currency_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def crd_ifc_lookup_ifctype_co(self, page_index=None, page_size=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def crd_ifc_lookup_ifctype_co_by_currency(self, currency_code=None, page_index=None, page_size=None):
        if not currency_code:
            currency_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "currency_code": currency_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def pmt_ifc_lookup_ifctype_co_by_currency(self, currency_code=None, page_index=None, page_size=None):
        if not currency_code:
            currency_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "currency_code": currency_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def crd_ifc_lookup_ifctype_i_by_crdacno(self, account_number=None, page_index=None, page_size=None):
        if not account_number:
            account_number=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "account_number": account_number,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def crd_ifc_lookup_ifctype_not_c(self, page_index=None, page_size=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "page_index": page_index,
            "page_size": page_size
        }
        return payload


    def crd_ifc_lookup_ifctype_pp_pi_by_crdacno(self, account_number=None, page_index=None, page_size=None):
        if not account_number:
            account_number=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "account_number": account_number,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def crd_lookup_crdcat_by_spl(self, sub_product_limit_code=None, page_index=None, page_size=None):
        if not sub_product_limit_code:
            sub_product_limit_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "sub_product_limit_code": sub_product_limit_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def crd_lookup_crdpl_by_ctm(self, customer_code=None, customer_type=None, page_index=None, page_size=None):
        if not customer_code:
            customer_code=''
        if not customer_type:
            customer_type=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "customer_code": customer_code,
            "customer_type": customer_type,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def crd_lookup_crdspl_by_ctm(self, customer_code=None, customer_type=None, page_index=None, page_size=None):
        if not customer_code:
            customer_code=''
        if not customer_type:
            customer_type=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "customer_code": customer_code,
            "customer_type": customer_type,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def crd_lookup_crdspl_od_by_ctm(self, customer_code=None, customer_type=None, page_index=None, page_size=None):
        if not customer_code:
            customer_code=''
        if not customer_type:
            customer_type=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "customer_code": customer_code,
            "customer_type": customer_type,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def ctm_lookup_ctm_by_ctmtype(self, customer_type=None, page_index=None, page_size=None):
        if not customer_type:
            customer_type=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "customer_type": customer_type,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_erl_lkp_data_ref(self, account_number=None, deposit_reference=None, page_index=None, page_size=None):
        if not account_number:
            account_number=''
        if not deposit_reference:
            deposit_reference=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "account_number": account_number,
            "deposit_reference": deposit_reference,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_ifc_lookup_by_currency_and_transcode(self, currency_code=None, tran_code=None, page_index=None, page_size=None):
        if not currency_code:
            currency_code=''
        if not tran_code:
            tran_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "currency_code": currency_code,
            "tran_code": tran_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_ifc_lookup_ifctype_c(self, currency_code=None, page_index=None, page_size=None):
        if not currency_code:
            currency_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "currency_code": currency_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_ifc_lookup_ifctype_co(self, page_index=None, page_size=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_ifc_lookup_ifctype_it_by_dptacno(self, account_number=None, page_index=None, page_size=None):
        if not account_number:
            account_number=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "account_number": account_number,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_ifc_lookup_ifctype_not_c(self, page_index=None, page_size=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_lkp_data_pdmacc(self, branch_code=None, page_index=None, page_size=None):
        if not branch_code:
            branch_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "branch_code": branch_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_lkp_data_pdoacc(self, account_number=None, branch_id=None, page_index=None, page_size=None):
        if not account_number:
            account_number=''
        if not branch_id:
            branch_id=0
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0        
        payload = {
            "account_number": account_number,
            "branch_id": branch_id,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_lookup_deposit_by_macno(self, master_fd_account_number=None, page_index=None, page_size=None):
        if not master_fd_account_number:
            master_fd_account_number=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "master_fd_account_number": master_fd_account_number,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_get_list_dptcat_api(self, page_index=None, page_size=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def dpt_opn_lkp_data_cncat(self, page_index=None, page_size=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def pmt_ifc_lookup_by_currency_and_transcode(self, currency_code=None, tran_code=None, page_index=None, page_size=None):
        if not currency_code:
            currency_code=''
        if not tran_code:
            tran_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "currency_code": currency_code,
            "tran_code": tran_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def pmt_ifc_lookup_ifctype_c(self, currency_code=None, page_index=None, page_size=None):
        if not currency_code:
            currency_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "currency_code": currency_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def pmt_ifc_lookup_ifctype_co(self, page_index=None, page_size=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def pmt_kitt_lookup_agentbank(self, catalog_code=None, page_index=None, page_size=None):
        if not catalog_code:
            catalog_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "catalog_code": catalog_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def pmt_lookup_agentbank(self, page_index=None, page_size=None):
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def pmt_lookup_message_inward_internal(self, branch_code=None, page_index=None, page_size=None):
        if not branch_code:
            branch_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "branch_code": branch_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def pmt_lookup_message_inward_international(self, branch_code=None, page_index=None, page_size=None):
        if not branch_code:
            branch_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "branch_code": branch_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def pmt_lookup_payment_catalog(self, output_format=None, direction=None, page_index=None, page_size=None):
        if not output_format:
            output_format=''
        if not direction:
            direction=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "output_format": output_format,
            "direction": direction,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def act_acchrt_lookup(self, account_number=None, currency_code=None, account_level_from=None, account_level_to=None, balance_side=None, account_name=None, account_classification=None, account_group=None, refresh_cache=None, page_index=None, page_size=None):
        if not account_number:
            account_number=''
        if not currency_code:
            currency_code=''
        if not account_level_from:
            account_level_from=''
        if not account_level_to:
            account_level_to=''
        if not balance_side:
            balance_side=''
        if not account_name:
            account_name=''
        if not account_classification:
            account_classification=''
        if not account_group:
            account_group=''
        if not refresh_cache:
            refresh_cache=True
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "account_number": account_number,
            "currency_code": currency_code,
            "account_level_from": account_level_from,
            "account_level_to": account_level_to,
            "balance_side": balance_side,
            "account_name": account_name,
            "account_classification": account_classification,
            "account_group": account_group,
            "refresh_cache": refresh_cache,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def act_acchrt_lookup_by_branchid(self, account_branch_code=None, page_index=None, page_size=None):
        if not account_branch_code:
            account_branch_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "account_branch_code": account_branch_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def act_acchrt_lookup_by_branchid_currency(self, account_branch_code=None, currency_code=None, page_index=None, page_size=None):
        if not account_branch_code:
            account_branch_code=''
        if not currency_code:
            currency_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "account_branch_code": account_branch_code,
            "currency_code": currency_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def act_acchrt_lookup_by_branchid_dptacc(self, account_branch_code=None, account_number=None, page_index=None, page_size=None):
        if not account_branch_code:
            account_branch_code=''
        if not account_number:
            account_number=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "account_branch_code": account_branch_code,
            "account_number": account_number,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def act_acchrt_lookup_by_currency(self, currency_code=None, page_index=None, page_size=None):
        if not currency_code:
            currency_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "currency_code": currency_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload

    def sql_lookup_listnot_ctm(self, customer_code=None, page_index=None, page_size=None):
        if not customer_code:
            customer_code=''
        if not page_index:
            page_index=0
        if not page_size:
            page_size=0
        payload = {
            "customer_code": customer_code,
            "page_index": page_index,
            "page_size": page_size
        }
        return payload