import json
import pytest

from datetime import datetime
from decimal import Decimal
from apitest.src.configs import USER_LOGIN, EXPECTED_KEY, EXPECTED_COL
from apitest.src.utilities.requestUtility import RequestUtility as RU
from apitest.src.utilities.assertUtility import AssertUtility as AU
from apitest.src.helpers.stored_procedure.stored_procedure_helpers import StoredProcedureHelper
from apitest.src.payloads.stored_procedure.stored_procedure_payload import StoredProcedurePayload

sp_payload = StoredProcedurePayload()
user_service = USER_LOGIN['user1']
expected_key = EXPECTED_KEY
expected_col = EXPECTED_COL

# data test common
customer_code_individual='11001706'
account_name_individual='CTM INDIVIDUAL TEST SP 01'
customer_code_enterprise='32000064'
account_name_enterprise='CTM ENTERPRISE TEST SP 01'
# data test valid
debit_accounting_valid='003101010333333301'
debit_accounting_usd='003101010666666602'
amount_deposit=10000000.45
accounting_currency='MMK'
accounting_currency1='MMK'
branch_name='003 - Bayint Naung Branch'
depositor_address='Home, Street, Ward, Township'
values_date=user_service['working_date']
deposit_currency='MMK'
# data test invalid
debit_accounting_invalid_posting_side_credit='003110070100000001'
debit_accounting_invalid_balance='003110080100000001'
# # data test trên 104
# to_account_number_saving_single_valid='310035109637'
# account_number_closed='110031738819'
# account_number_block='110037723297'
# account_number_pending='110031449759'
# data test trên 198
to_account_number_saving_single_valid='310034460838'
account_number_closed='110031400004'
account_number_block='110036552201'
account_number_pending='310036280263'

@pytest.fixture(scope='session')
def user():
    req = RU(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_MDP
class Test_SP_DPT_MDP(object):

    def test_04_sp_dpt_mdp_001_success_current_account_status_new_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_apr['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs_01 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_01 = RU.get_p2_content_response_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_01)
        # 'response' - get value level 1
        value_status = data_actual_01['status']
        value_error_message = data_actual_01['error_message']
        value_error_code = data_actual_01['error_code']
        value_data = data_actual_01['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mdp'], data_actual_01['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_mdp_depositor_description'], data_actual_01['data']['depositor_description'])
        # 'response' - get value in 'data'
        value_data_account_number = data_actual_01['data']['account_number']
        value_data_amount_deposit = data_actual_01['data']['amount_deposit']
        value_data_debit_accounting = data_actual_01['data']['debit_accounting']
        value_data_accounting_currency = data_actual_01['data']['accounting_currency']
        value_data_cross_rate = data_actual_01['data']['cross_rate']
        value_data_acounting_amount = data_actual_01['data']['acounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual_01['data']['exchange_rate_of_accounting_bcy']
        value_data_accounting_amount_bcy = data_actual_01['data']['accounting_amount_bcy']
        value_data_depositor_name = data_actual_01['data']['depositor_name']
        value_data_depositor_code = data_actual_01['data']['depositor_code']
        value_data_depositor_address = data_actual_01['data']['depositor_address']
        value_data_values_date = data_actual_01['data']['values_date']
        value_data_deposit_currency = data_actual_01['data']['deposit_currency']
        value_data_exchange_rate_debit_account_bcy = data_actual_01['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual_01['data']['amount_debit_account_bcy']
        value_data_prepaid_interest = data_actual_01['data']['prepaid_interest']
        value_data_accounting_currency1 = data_actual_01['data']['accounting_currency1']
        value_data_fee_data = data_actual_01['data']['fee_data']
        value_data_total_fee = data_actual_01['data']['total_fee']
        value_data_branch_name = data_actual_01['data']['branch_name']
        value_data_transaction_code = data_actual_01['data']['transaction_code']
        value_data_transaction_number = data_actual_01['data']['transaction_number']
        value_data_transaction_type = data_actual_01['data']['transaction_type']
        value_data_sub_code = data_actual_01['data']['sub_code']
        value_data_transaction_date = data_actual_01['data']['transaction_date']
        value_data_service_sys_date = data_actual_01['data']['service_sys_date']
        value_data_reference_id = data_actual_01['data']['reference_id']
        value_data_ref_id = data_actual_01['data']['ref_id']
        value_data_reference_code = data_actual_01['data']['reference_code']
        value_data_business_code = data_actual_01['data']['business_code']
        value_data_value_date = data_actual_01['data']['value_date']
        value_data_current_user_code = data_actual_01['data']['current_user_code']
        value_data_current_branch_code = data_actual_01['data']['current_branch_code']
        value_data_current_username = data_actual_01['data']['current_username']
        value_data_current_loginname = data_actual_01['data']['current_loginname']
        value_data_user_approve = data_actual_01['data']['user_approve']
        value_data_status = data_actual_01['data']['status']
        value_data_is_reverse = data_actual_01['data']['is_reverse']
        value_data_amount1 = data_actual_01['data']['amount1']
        value_data_description = data_actual_01['data']['description']
        value_data_token = data_actual_01['data']['token']
        value_data_is_transaction_reverse = data_actual_01['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual_01['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
        AU.assert_equals('debit_accounting', debit_accounting_valid, value_data_debit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('acounting_amount', 0.0, value_data_acounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1.0, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('accounting_amount_bcy', 0.0, value_data_accounting_amount_bcy)
        AU.assert_equals('depositor_name', account_name_individual, value_data_depositor_name)
        AU.assert_equals('depositor_code', customer_code_individual, value_data_depositor_code)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('deposit_currency', deposit_currency, value_data_deposit_currency)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('prepaid_interest', 0.0, value_data_prepaid_interest)
        AU.assert_equals('accounting_currency1', accounting_currency1, value_data_accounting_currency1)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_fee', 0.0, value_data_total_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('transaction_code', 'DPT_MDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_empty('reference_code', value_data_reference_code)
        AU.assert_empty('business_code', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_empty('user_approve', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_false('is_reverse', value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1112: Miscellaneous deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_false('is_transaction_reverse', value_data_is_transaction_reverse)
        AU.assert_false('is_transaction_compensated', value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 1, len(data_actual_posting))
        # 'postings' - verify key response, item 1
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array, item 1
        value_TransactionNumber = data_actual_posting[0]['TransactionNumber']
        value_TransTableName = data_actual_posting[0]['TransTableName']
        value_TransId = data_actual_posting[0]['TransId']
        value_SysAccountName = data_actual_posting[0]['SysAccountName']
        value_GLAccount = data_actual_posting[0]['GLAccount']
        value_DorC = data_actual_posting[0]['DorC']
        value_TransactionStatus = data_actual_posting[0]['TransactionStatus']
        value_Amount = data_actual_posting[0]['Amount']
        value_BranchCode = data_actual_posting[0]['BranchCode']
        value_CurrencyCode = data_actual_posting[0]['CurrencyCode']
        value_ValueDate = data_actual_posting[0]['ValueDate']
        value_Posted = data_actual_posting[0]['Posted']
        value_AccountingGroup = data_actual_posting[0]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[0]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[0]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[0]['BaseCurrencyAmount']
        value_Id = data_actual_posting[0]['Id']
        # 'postings' - verify value under array, item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', amount_deposit, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # STEP 04: miscellaneous deposit to deposit status 'Normal'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs_02 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_02 = RU.get_p2_content_response_by_step_code(rs_02, step_code)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_02)
        # 'response' - get value level 1
        value_status = data_actual_02['status']
        value_error_message = data_actual_02['error_message']
        value_error_code = data_actual_02['error_code']
        value_data = data_actual_02['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mdp'], data_actual_02['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_mdp_depositor_description'], data_actual_02['data']['depositor_description'])
        # 'response' - get value in 'data'
        value_data_account_number = data_actual_02['data']['account_number']
        value_data_amount_deposit = data_actual_02['data']['amount_deposit']
        value_data_debit_accounting = data_actual_02['data']['debit_accounting']
        value_data_accounting_currency = data_actual_02['data']['accounting_currency']
        value_data_cross_rate = data_actual_02['data']['cross_rate']
        value_data_acounting_amount = data_actual_02['data']['acounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual_02['data']['exchange_rate_of_accounting_bcy']
        value_data_accounting_amount_bcy = data_actual_02['data']['accounting_amount_bcy']
        value_data_depositor_name = data_actual_02['data']['depositor_name']
        value_data_depositor_code = data_actual_02['data']['depositor_code']
        value_data_depositor_address = data_actual_02['data']['depositor_address']
        value_data_values_date = data_actual_02['data']['values_date']
        value_data_deposit_currency = data_actual_02['data']['deposit_currency']
        value_data_exchange_rate_debit_account_bcy = data_actual_02['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual_02['data']['amount_debit_account_bcy']
        value_data_prepaid_interest = data_actual_02['data']['prepaid_interest']
        value_data_accounting_currency1 = data_actual_02['data']['accounting_currency1']
        value_data_fee_data = data_actual_02['data']['fee_data']
        value_data_total_fee = data_actual_02['data']['total_fee']
        value_data_branch_name = data_actual_02['data']['branch_name']
        value_data_transaction_code = data_actual_02['data']['transaction_code']
        value_data_transaction_number = data_actual_02['data']['transaction_number']
        value_data_transaction_type = data_actual_02['data']['transaction_type']
        value_data_sub_code = data_actual_02['data']['sub_code']
        value_data_transaction_date = data_actual_02['data']['transaction_date']
        value_data_service_sys_date = data_actual_02['data']['service_sys_date']
        value_data_reference_id = data_actual_02['data']['reference_id']
        value_data_ref_id = data_actual_02['data']['ref_id']
        value_data_reference_code = data_actual_02['data']['reference_code']
        value_data_business_code = data_actual_02['data']['business_code']
        value_data_value_date = data_actual_02['data']['value_date']
        value_data_current_user_code = data_actual_02['data']['current_user_code']
        value_data_current_branch_code = data_actual_02['data']['current_branch_code']
        value_data_current_username = data_actual_02['data']['current_username']
        value_data_current_loginname = data_actual_02['data']['current_loginname']
        value_data_user_approve = data_actual_02['data']['user_approve']
        value_data_status = data_actual_02['data']['status']
        value_data_is_reverse = data_actual_02['data']['is_reverse']
        value_data_amount1 = data_actual_02['data']['amount1']
        value_data_description = data_actual_02['data']['description']
        value_data_token = data_actual_02['data']['token']
        value_data_is_transaction_reverse = data_actual_02['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual_02['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
        AU.assert_equals('debit_accounting', debit_accounting_valid, value_data_debit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('acounting_amount', 0.0, value_data_acounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1.0, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('accounting_amount_bcy', 0.0, value_data_accounting_amount_bcy)
        AU.assert_equals('depositor_name', account_name_individual, value_data_depositor_name)
        AU.assert_equals('depositor_code', customer_code_individual, value_data_depositor_code)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('deposit_currency', deposit_currency, value_data_deposit_currency)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('prepaid_interest', 0.0, value_data_prepaid_interest)
        AU.assert_equals('accounting_currency1', accounting_currency1, value_data_accounting_currency1)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_fee', 0.0, value_data_total_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('transaction_code', 'DPT_MDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_empty('reference_code', value_data_reference_code)
        AU.assert_empty('business_code', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_empty('user_approve', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_false('is_reverse', value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1112: Miscellaneous deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_false('is_transaction_reverse', value_data_is_transaction_reverse)
        AU.assert_false('is_transaction_compensated', value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_02, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        AU.assert_equals('Number item in posting', 1, len(data_actual_posting))
        # 'postings' - verify key response, item 1
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array, item 1
        value_TransactionNumber = data_actual_posting[0]['TransactionNumber']
        value_TransTableName = data_actual_posting[0]['TransTableName']
        value_TransId_step_main = data_actual_posting[0]['TransId']
        value_SysAccountName = data_actual_posting[0]['SysAccountName']
        value_GLAccount = data_actual_posting[0]['GLAccount']
        value_DorC = data_actual_posting[0]['DorC']
        value_TransactionStatus = data_actual_posting[0]['TransactionStatus']
        value_Amount = data_actual_posting[0]['Amount']
        value_BranchCode = data_actual_posting[0]['BranchCode']
        value_CurrencyCode = data_actual_posting[0]['CurrencyCode']
        value_ValueDate = data_actual_posting[0]['ValueDate']
        value_Posted = data_actual_posting[0]['Posted']
        value_AccountingGroup_step_main = data_actual_posting[0]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[0]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[0]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[0]['BaseCurrencyAmount']
        value_Id = data_actual_posting[0]['Id']
        # 'postings' - verify value under array, item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId_step_main)
        AU.assert_not_null('TransId', value_TransId_step_main)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', amount_deposit, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup_step_main)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)

    def test_04_sp_dpt_mdp_002_success_current_account_status_new_normal_add_fee(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_apr['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 03: miscellaneous deposit to deposit status 'New'
        total_fee=3200.0
        share_fee_01=0.0
        ifc_name_01='Withdrawal (MMK) For Different Region  (By Cash)'
        value_type_01='P'
        ifc_code_01=302
        payrate_01=100
        ifc_value_01=0.025
        ifc_amount_01=200.0
        currency_account_code_01=deposit_currency
        floor_value_01=200.0
        ceiling_value_01=0.0
        share_rate_01=0.0
        share_amount_01=0.0
        round_rate_01=0.0
        round_amount_01=0.0
        currency_fee_code_01=deposit_currency
        pay_source_01='CSH'
        share_fee_02=0.0
        ifc_name_02='Account To Account Transfer (MMK) For Same Region'
        value_type_02='F'
        ifc_code_02=309
        payrate_02=100
        ifc_value_02=3000.0
        ifc_amount_02=3000.0
        currency_account_code_02=deposit_currency
        floor_value_02=0.0
        ceiling_value_02=0.0
        share_rate_02=0.0
        share_amount_02=0.0
        round_rate_02=0.0
        round_amount_02=0.0
        currency_fee_code_02=deposit_currency
        pay_source_02='CSH'
        gl_account_ifcc_01='003303030100010101'
        gl_account_ifcc_02='003303030100010101'
        fee_data = [
            {
                "share_fee": share_fee_01,
                "ifc_name": ifc_name_01,
                "value_type": value_type_01,
                "ifc_code": ifc_code_01,
                "payrate": payrate_01,
                "ifc_value": ifc_value_01,
                "ifc_amount": ifc_amount_01,
                "currency_account_code": currency_account_code_01,
                "floor_value": floor_value_01,
                "ceiling_value": ceiling_value_01,
                "share_rate": share_rate_01,
                "share_amount": share_amount_01,
                "round_rate": round_rate_01,
                "round_amount": round_amount_01,
                "currency_fee_code": currency_fee_code_01,
                "pay_source": pay_source_01
            },
            {
                "share_fee": share_fee_02,
                "ifc_name": ifc_name_02,
                "value_type": value_type_02,
                "ifc_code": ifc_code_02,
                "payrate": payrate_02,
                "ifc_value": ifc_value_02,
                "ifc_amount": ifc_amount_02,
                "currency_account_code": currency_account_code_02,
                "floor_value": floor_value_02,
                "ceiling_value": ceiling_value_02,
                "share_rate": share_rate_02,
                "share_amount": share_amount_02,
                "round_rate": round_rate_02,
                "round_amount": round_amount_02,
                "currency_fee_code": currency_fee_code_02,
                "pay_source": pay_source_02
            }
        ]
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1,
            fee_data=fee_data
        )
        rs_01 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_01 = RU.get_p2_content_response_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_01)
        # 'response' - get value level 1
        value_status = data_actual_01['status']
        value_error_message = data_actual_01['error_message']
        value_error_code = data_actual_01['error_code']
        value_data = data_actual_01['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mdp'], data_actual_01['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_mdp_depositor_description'], data_actual_01['data']['depositor_description'])
        # 'response' - get value in 'data'
        value_data_account_number = data_actual_01['data']['account_number']
        value_data_amount_deposit = data_actual_01['data']['amount_deposit']
        value_data_debit_accounting = data_actual_01['data']['debit_accounting']
        value_data_accounting_currency = data_actual_01['data']['accounting_currency']
        value_data_cross_rate = data_actual_01['data']['cross_rate']
        value_data_acounting_amount = data_actual_01['data']['acounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual_01['data']['exchange_rate_of_accounting_bcy']
        value_data_accounting_amount_bcy = data_actual_01['data']['accounting_amount_bcy']
        value_data_depositor_name = data_actual_01['data']['depositor_name']
        value_data_depositor_code = data_actual_01['data']['depositor_code']
        value_data_depositor_address = data_actual_01['data']['depositor_address']
        value_data_values_date = data_actual_01['data']['values_date']
        value_data_deposit_currency = data_actual_01['data']['deposit_currency']
        value_data_exchange_rate_debit_account_bcy = data_actual_01['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual_01['data']['amount_debit_account_bcy']
        value_data_prepaid_interest = data_actual_01['data']['prepaid_interest']
        value_data_accounting_currency1 = data_actual_01['data']['accounting_currency1']
        value_data_fee_data = data_actual_01['data']['fee_data']
        value_data_total_fee = data_actual_01['data']['total_fee']
        value_data_branch_name = data_actual_01['data']['branch_name']
        value_data_transaction_code = data_actual_01['data']['transaction_code']
        value_data_transaction_number = data_actual_01['data']['transaction_number']
        value_data_transaction_type = data_actual_01['data']['transaction_type']
        value_data_sub_code = data_actual_01['data']['sub_code']
        value_data_transaction_date = data_actual_01['data']['transaction_date']
        value_data_service_sys_date = data_actual_01['data']['service_sys_date']
        value_data_reference_id = data_actual_01['data']['reference_id']
        value_data_ref_id = data_actual_01['data']['ref_id']
        value_data_reference_code = data_actual_01['data']['reference_code']
        value_data_business_code = data_actual_01['data']['business_code']
        value_data_value_date = data_actual_01['data']['value_date']
        value_data_current_user_code = data_actual_01['data']['current_user_code']
        value_data_current_branch_code = data_actual_01['data']['current_branch_code']
        value_data_current_username = data_actual_01['data']['current_username']
        value_data_current_loginname = data_actual_01['data']['current_loginname']
        value_data_user_approve = data_actual_01['data']['user_approve']
        value_data_status = data_actual_01['data']['status']
        value_data_is_reverse = data_actual_01['data']['is_reverse']
        value_data_amount1 = data_actual_01['data']['amount1']
        value_data_description = data_actual_01['data']['description']
        value_data_token = data_actual_01['data']['token']
        value_data_is_transaction_reverse = data_actual_01['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual_01['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
        AU.assert_equals('debit_accounting', debit_accounting_valid, value_data_debit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('acounting_amount', 0.0, value_data_acounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1.0, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('accounting_amount_bcy', 0.0, value_data_accounting_amount_bcy)
        AU.assert_equals('depositor_name', account_name_individual, value_data_depositor_name)
        AU.assert_equals('depositor_code', customer_code_individual, value_data_depositor_code)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('deposit_currency', deposit_currency, value_data_deposit_currency)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('prepaid_interest', 0.0, value_data_prepaid_interest)
        AU.assert_equals('accounting_currency1', accounting_currency1, value_data_accounting_currency1)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_fee', total_fee, value_data_total_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('transaction_code', 'DPT_MDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_empty('reference_code', value_data_reference_code)
        AU.assert_empty('business_code', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_empty('user_approve', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_false('is_reverse', value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1112: Miscellaneous deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_false('is_transaction_reverse', value_data_is_transaction_reverse)
        AU.assert_false('is_transaction_compensated', value_data_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'fee_data', item 1
        AU.assert_exists(expected_key['fee_data'], data_actual_01['data']['fee_data'][0])
        # 'response' - get value under 'data' and 'fee_data', item 1
        value_fee_data_ifc_name = data_actual_01['data']['fee_data'][0]['ifc_name']
        value_fee_data_share_fee = data_actual_01['data']['fee_data'][0]['share_fee']
        value_fee_data_ifc_code = data_actual_01['data']['fee_data'][0]['ifc_code']
        value_fee_data_payrate = data_actual_01['data']['fee_data'][0]['payrate']
        value_fee_data_ifc_value = data_actual_01['data']['fee_data'][0]['ifc_value']
        value_fee_data_ifc_amount = data_actual_01['data']['fee_data'][0]['ifc_amount']
        value_fee_data_currency_account_code = data_actual_01['data']['fee_data'][0]['currency_account_code']
        value_fee_data_floor_value = data_actual_01['data']['fee_data'][0]['floor_value']
        value_fee_data_ceiling_value = data_actual_01['data']['fee_data'][0]['ceiling_value']
        value_fee_data_share_rate = data_actual_01['data']['fee_data'][0]['share_rate']
        value_fee_data_share_amount = data_actual_01['data']['fee_data'][0]['share_amount']
        value_fee_data_round_rate = data_actual_01['data']['fee_data'][0]['round_rate']
        value_fee_data_round_amount = data_actual_01['data']['fee_data'][0]['round_amount']
        value_fee_data_currency_fee_code = data_actual_01['data']['fee_data'][0]['currency_fee_code']
        value_fee_data_pay_source = data_actual_01['data']['fee_data'][0]['pay_source']
        # value_fee_data_value_typect = data_actual_01['data']['fee_data'][0]['value_typect']
        value_fee_data_value_type = data_actual_01['data']['fee_data'][0]['value_type']
        # 'response' - verify value under 'data' and 'fee_data', item 1
        AU.assert_equals('ifc_name', ifc_name_01, value_fee_data_ifc_name)
        AU.assert_equals('share_fee', share_fee_01, value_fee_data_share_fee)
        AU.assert_equals('ifc_code', ifc_code_01, value_fee_data_ifc_code)
        AU.assert_equals('payrate', payrate_01, value_fee_data_payrate)
        AU.assert_equals('ifc_value', ifc_value_01, value_fee_data_ifc_value)
        AU.assert_equals('ifc_amount', ifc_amount_01, value_fee_data_ifc_amount)
        AU.assert_equals('currency_account_code', currency_account_code_01, value_fee_data_currency_account_code)
        AU.assert_equals('floor_value', floor_value_01, value_fee_data_floor_value)
        AU.assert_equals('ceiling_value', ceiling_value_01, value_fee_data_ceiling_value)
        AU.assert_equals('share_rate', share_rate_01, value_fee_data_share_rate)
        AU.assert_equals('share_amount', share_amount_01, value_fee_data_share_amount)
        AU.assert_equals('round_rate', round_rate_01, value_fee_data_round_rate)
        AU.assert_equals('round_amount', round_amount_01, value_fee_data_round_amount)
        AU.assert_equals('currency_fee_code', currency_fee_code_01, value_fee_data_currency_fee_code)
        AU.assert_equals('pay_source', pay_source_01, value_fee_data_pay_source)
        # AU.assert_null('value_typect', value_fee_data_value_typect)
        AU.assert_equals('value_type', value_type_01, value_fee_data_value_type)
        # 'response' - verify key response under 'data' and 'fee_data', item 2
        AU.assert_exists(expected_key['fee_data'], data_actual_01['data']['fee_data'][1])
        # 'response' - get value under 'data' and 'fee_data', item 2
        value_fee_data_ifc_name = data_actual_01['data']['fee_data'][1]['ifc_name']
        value_fee_data_share_fee = data_actual_01['data']['fee_data'][1]['share_fee']
        value_fee_data_ifc_code = data_actual_01['data']['fee_data'][1]['ifc_code']
        value_fee_data_payrate = data_actual_01['data']['fee_data'][1]['payrate']
        value_fee_data_ifc_value = data_actual_01['data']['fee_data'][1]['ifc_value']
        value_fee_data_ifc_amount = data_actual_01['data']['fee_data'][1]['ifc_amount']
        value_fee_data_currency_account_code = data_actual_01['data']['fee_data'][1]['currency_account_code']
        value_fee_data_floor_value = data_actual_01['data']['fee_data'][1]['floor_value']
        value_fee_data_ceiling_value = data_actual_01['data']['fee_data'][1]['ceiling_value']
        value_fee_data_share_rate = data_actual_01['data']['fee_data'][1]['share_rate']
        value_fee_data_share_amount = data_actual_01['data']['fee_data'][1]['share_amount']
        value_fee_data_round_rate = data_actual_01['data']['fee_data'][1]['round_rate']
        value_fee_data_round_amount = data_actual_01['data']['fee_data'][1]['round_amount']
        value_fee_data_currency_fee_code = data_actual_01['data']['fee_data'][1]['currency_fee_code']
        value_fee_data_pay_source = data_actual_01['data']['fee_data'][1]['pay_source']
        # value_fee_data_value_typect = data_actual_01['data']['fee_data'][1]['value_typect']
        value_fee_data_value_type = data_actual_01['data']['fee_data'][1]['value_type']
        # 'response' - verify value under 'data' and 'fee_data', item 2
        AU.assert_equals('ifc_name', ifc_name_02, value_fee_data_ifc_name)
        AU.assert_equals('share_fee', share_fee_02, value_fee_data_share_fee)
        AU.assert_equals('ifc_code', ifc_code_02, value_fee_data_ifc_code)
        AU.assert_equals('payrate', payrate_02, value_fee_data_payrate)
        AU.assert_equals('ifc_value', ifc_value_02, value_fee_data_ifc_value)
        AU.assert_equals('ifc_amount', ifc_amount_02, value_fee_data_ifc_amount)
        AU.assert_equals('currency_account_code', currency_account_code_02, value_fee_data_currency_account_code)
        AU.assert_equals('floor_value', floor_value_02, value_fee_data_floor_value)
        AU.assert_equals('ceiling_value', ceiling_value_02, value_fee_data_ceiling_value)
        AU.assert_equals('share_rate', share_rate_02, value_fee_data_share_rate)
        AU.assert_equals('share_amount', share_amount_02, value_fee_data_share_amount)
        AU.assert_equals('round_rate', round_rate_02, value_fee_data_round_rate)
        AU.assert_equals('round_amount', round_amount_02, value_fee_data_round_amount)
        AU.assert_equals('currency_fee_code', currency_fee_code_02, value_fee_data_currency_fee_code)
        AU.assert_equals('pay_source', pay_source_02, value_fee_data_pay_source)
        # AU.assert_null('value_typect', value_fee_data_value_typect)
        AU.assert_equals('value_type', value_type_02, value_fee_data_value_type)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 3, len(data_actual_posting))
        # 'postings' - verify key response, item 1
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array, item 1
        value_TransactionNumber = data_actual_posting[0]['TransactionNumber']
        value_TransTableName = data_actual_posting[0]['TransTableName']
        value_TransId = data_actual_posting[0]['TransId']
        value_SysAccountName = data_actual_posting[0]['SysAccountName']
        value_GLAccount = data_actual_posting[0]['GLAccount']
        value_DorC = data_actual_posting[0]['DorC']
        value_TransactionStatus = data_actual_posting[0]['TransactionStatus']
        value_Amount = data_actual_posting[0]['Amount']
        value_BranchCode = data_actual_posting[0]['BranchCode']
        value_CurrencyCode = data_actual_posting[0]['CurrencyCode']
        value_ValueDate = data_actual_posting[0]['ValueDate']
        value_Posted = data_actual_posting[0]['Posted']
        value_AccountingGroup = data_actual_posting[0]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[0]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[0]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[0]['BaseCurrencyAmount']
        value_Id = data_actual_posting[0]['Id']
        # 'postings' - verify value under array, item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', Decimal(str(amount_deposit)) - (Decimal(str(ifc_amount_01)) + Decimal(str(ifc_amount_02))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 2
        AU.assert_exists(expected_key['postings'], data_actual_posting[1])
        # 'postings' - get value under array, item 2
        value_TransactionNumber = data_actual_posting[1]['TransactionNumber']
        value_TransTableName = data_actual_posting[1]['TransTableName']
        value_TransId = data_actual_posting[1]['TransId']
        value_SysAccountName = data_actual_posting[1]['SysAccountName']
        value_GLAccount = data_actual_posting[1]['GLAccount']
        value_DorC = data_actual_posting[1]['DorC']
        value_TransactionStatus = data_actual_posting[1]['TransactionStatus']
        value_Amount = data_actual_posting[1]['Amount']
        value_BranchCode = data_actual_posting[1]['BranchCode']
        value_CurrencyCode = data_actual_posting[1]['CurrencyCode']
        value_ValueDate = data_actual_posting[1]['ValueDate']
        value_Posted = data_actual_posting[1]['Posted']
        value_AccountingGroup = data_actual_posting[1]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[1]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[1]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[1]['BaseCurrencyAmount']
        value_Id = data_actual_posting[1]['Id']
        # 'postings' - verify value under array, item 2
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_01, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_01, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 3
        AU.assert_exists(expected_key['postings'], data_actual_posting[2])
        # 'postings' - get value under array, item 3
        value_TransactionNumber = data_actual_posting[2]['TransactionNumber']
        value_TransTableName = data_actual_posting[2]['TransTableName']
        value_TransId = data_actual_posting[2]['TransId']
        value_SysAccountName = data_actual_posting[2]['SysAccountName']
        value_GLAccount = data_actual_posting[2]['GLAccount']
        value_DorC = data_actual_posting[2]['DorC']
        value_TransactionStatus = data_actual_posting[2]['TransactionStatus']
        value_Amount = data_actual_posting[2]['Amount']
        value_BranchCode = data_actual_posting[2]['BranchCode']
        value_CurrencyCode = data_actual_posting[2]['CurrencyCode']
        value_ValueDate = data_actual_posting[2]['ValueDate']
        value_Posted = data_actual_posting[2]['Posted']
        value_AccountingGroup = data_actual_posting[2]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[2]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[2]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[2]['BaseCurrencyAmount']
        value_Id = data_actual_posting[2]['Id']
        # 'postings' - verify value under array, item 3
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_02, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_02, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # STEP 04: miscellaneous deposit to deposit status 'Normal'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1,
            fee_data=fee_data
        )
        rs_02 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_02 = RU.get_p2_content_response_by_step_code(rs_02, step_code)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_02)
        # 'response' - get value level 1
        value_status = data_actual_02['status']
        value_error_message = data_actual_02['error_message']
        value_error_code = data_actual_02['error_code']
        value_data = data_actual_02['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mdp'], data_actual_02['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_mdp_depositor_description'], data_actual_02['data']['depositor_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual_02['data']['account_number']
        value_data_amount_deposit = data_actual_02['data']['amount_deposit']
        value_data_debit_accounting = data_actual_02['data']['debit_accounting']
        value_data_accounting_currency = data_actual_02['data']['accounting_currency']
        value_data_cross_rate = data_actual_02['data']['cross_rate']
        value_data_acounting_amount = data_actual_02['data']['acounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual_02['data']['exchange_rate_of_accounting_bcy']
        value_data_accounting_amount_bcy = data_actual_02['data']['accounting_amount_bcy']
        value_data_depositor_name = data_actual_02['data']['depositor_name']
        value_data_depositor_code = data_actual_02['data']['depositor_code']
        value_data_depositor_address = data_actual_02['data']['depositor_address']
        value_data_values_date = data_actual_02['data']['values_date']
        value_data_deposit_currency = data_actual_02['data']['deposit_currency']
        value_data_exchange_rate_debit_account_bcy = data_actual_02['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual_02['data']['amount_debit_account_bcy']
        value_data_prepaid_interest = data_actual_02['data']['prepaid_interest']
        value_data_accounting_currency1 = data_actual_02['data']['accounting_currency1']
        value_data_fee_data = data_actual_02['data']['fee_data']
        value_data_total_fee = data_actual_02['data']['total_fee']
        value_data_branch_name = data_actual_02['data']['branch_name']
        value_data_transaction_code = data_actual_02['data']['transaction_code']
        value_data_transaction_number = data_actual_02['data']['transaction_number']
        value_data_transaction_type = data_actual_02['data']['transaction_type']
        value_data_sub_code = data_actual_02['data']['sub_code']
        value_data_transaction_date = data_actual_02['data']['transaction_date']
        value_data_service_sys_date = data_actual_02['data']['service_sys_date']
        value_data_reference_id = data_actual_02['data']['reference_id']
        value_data_ref_id = data_actual_02['data']['ref_id']
        value_data_reference_code = data_actual_02['data']['reference_code']
        value_data_business_code = data_actual_02['data']['business_code']
        value_data_value_date = data_actual_02['data']['value_date']
        value_data_current_user_code = data_actual_02['data']['current_user_code']
        value_data_current_branch_code = data_actual_02['data']['current_branch_code']
        value_data_current_username = data_actual_02['data']['current_username']
        value_data_current_loginname = data_actual_02['data']['current_loginname']
        value_data_user_approve = data_actual_02['data']['user_approve']
        value_data_status = data_actual_02['data']['status']
        value_data_is_reverse = data_actual_02['data']['is_reverse']
        value_data_amount1 = data_actual_02['data']['amount1']
        value_data_description = data_actual_02['data']['description']
        value_data_token = data_actual_02['data']['token']
        value_data_is_transaction_reverse = data_actual_02['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual_02['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
        AU.assert_equals('debit_accounting', debit_accounting_valid, value_data_debit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('acounting_amount', 0.0, value_data_acounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1.0, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('accounting_amount_bcy', 0.0, value_data_accounting_amount_bcy)
        AU.assert_equals('depositor_name', account_name_individual, value_data_depositor_name)
        AU.assert_equals('depositor_code', customer_code_individual, value_data_depositor_code)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('deposit_currency', deposit_currency, value_data_deposit_currency)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('prepaid_interest', 0.0, value_data_prepaid_interest)
        AU.assert_equals('accounting_currency1', accounting_currency1, value_data_accounting_currency1)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_fee', total_fee, value_data_total_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('transaction_code', 'DPT_MDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_empty('reference_code', value_data_reference_code)
        AU.assert_empty('business_code', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_empty('user_approve', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_false('is_reverse', value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1112: Miscellaneous deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_false('is_transaction_reverse', value_data_is_transaction_reverse)
        AU.assert_false('is_transaction_compensated', value_data_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'fee_data', item 1
        AU.assert_exists(expected_key['fee_data'], data_actual_02['data']['fee_data'][0])
        # 'response' - get value under 'data' and 'fee_data', item 1
        value_fee_data_ifc_name = data_actual_02['data']['fee_data'][0]['ifc_name']
        value_fee_data_share_fee = data_actual_02['data']['fee_data'][0]['share_fee']
        value_fee_data_ifc_code = data_actual_02['data']['fee_data'][0]['ifc_code']
        value_fee_data_payrate = data_actual_02['data']['fee_data'][0]['payrate']
        value_fee_data_ifc_value = data_actual_02['data']['fee_data'][0]['ifc_value']
        value_fee_data_ifc_amount = data_actual_02['data']['fee_data'][0]['ifc_amount']
        value_fee_data_currency_account_code = data_actual_02['data']['fee_data'][0]['currency_account_code']
        value_fee_data_floor_value = data_actual_02['data']['fee_data'][0]['floor_value']
        value_fee_data_ceiling_value = data_actual_02['data']['fee_data'][0]['ceiling_value']
        value_fee_data_share_rate = data_actual_02['data']['fee_data'][0]['share_rate']
        value_fee_data_share_amount = data_actual_02['data']['fee_data'][0]['share_amount']
        value_fee_data_round_rate = data_actual_02['data']['fee_data'][0]['round_rate']
        value_fee_data_round_amount = data_actual_02['data']['fee_data'][0]['round_amount']
        value_fee_data_currency_fee_code = data_actual_02['data']['fee_data'][0]['currency_fee_code']
        value_fee_data_pay_source = data_actual_02['data']['fee_data'][0]['pay_source']
        # value_fee_data_value_typect = data_actual_02['data']['fee_data'][0]['value_typect']
        value_fee_data_value_type = data_actual_02['data']['fee_data'][0]['value_type']
        # 'response' - verify value under 'data' and 'fee_data', item 1
        AU.assert_equals('ifc_name', ifc_name_01, value_fee_data_ifc_name)
        AU.assert_equals('share_fee', share_fee_01, value_fee_data_share_fee)
        AU.assert_equals('ifc_code', ifc_code_01, value_fee_data_ifc_code)
        AU.assert_equals('payrate', payrate_01, value_fee_data_payrate)
        AU.assert_equals('ifc_value', ifc_value_01, value_fee_data_ifc_value)
        AU.assert_equals('ifc_amount', ifc_amount_01, value_fee_data_ifc_amount)
        AU.assert_equals('currency_account_code', currency_account_code_01, value_fee_data_currency_account_code)
        AU.assert_equals('floor_value', floor_value_01, value_fee_data_floor_value)
        AU.assert_equals('ceiling_value', ceiling_value_01, value_fee_data_ceiling_value)
        AU.assert_equals('share_rate', share_rate_01, value_fee_data_share_rate)
        AU.assert_equals('share_amount', share_amount_01, value_fee_data_share_amount)
        AU.assert_equals('round_rate', round_rate_01, value_fee_data_round_rate)
        AU.assert_equals('round_amount', round_amount_01, value_fee_data_round_amount)
        AU.assert_equals('currency_fee_code', currency_fee_code_01, value_fee_data_currency_fee_code)
        AU.assert_equals('pay_source', pay_source_01, value_fee_data_pay_source)
        # AU.assert_null('value_typect', value_fee_data_value_typect)
        AU.assert_equals('value_type', value_type_01, value_fee_data_value_type)
        # 'response' - verify key response under 'data' and 'fee_data', item 2
        AU.assert_exists(expected_key['fee_data'], data_actual_02['data']['fee_data'][1])
        # 'response' - get value under 'data' and 'fee_data', item 2
        value_fee_data_ifc_name = data_actual_02['data']['fee_data'][1]['ifc_name']
        value_fee_data_share_fee = data_actual_02['data']['fee_data'][1]['share_fee']
        value_fee_data_ifc_code = data_actual_02['data']['fee_data'][1]['ifc_code']
        value_fee_data_payrate = data_actual_02['data']['fee_data'][1]['payrate']
        value_fee_data_ifc_value = data_actual_02['data']['fee_data'][1]['ifc_value']
        value_fee_data_ifc_amount = data_actual_02['data']['fee_data'][1]['ifc_amount']
        value_fee_data_currency_account_code = data_actual_02['data']['fee_data'][1]['currency_account_code']
        value_fee_data_floor_value = data_actual_02['data']['fee_data'][1]['floor_value']
        value_fee_data_ceiling_value = data_actual_02['data']['fee_data'][1]['ceiling_value']
        value_fee_data_share_rate = data_actual_02['data']['fee_data'][1]['share_rate']
        value_fee_data_share_amount = data_actual_02['data']['fee_data'][1]['share_amount']
        value_fee_data_round_rate = data_actual_02['data']['fee_data'][1]['round_rate']
        value_fee_data_round_amount = data_actual_02['data']['fee_data'][1]['round_amount']
        value_fee_data_currency_fee_code = data_actual_02['data']['fee_data'][1]['currency_fee_code']
        value_fee_data_pay_source = data_actual_02['data']['fee_data'][1]['pay_source']
        # value_fee_data_value_typect = data_actual_02['data']['fee_data'][1]['value_typect']
        value_fee_data_value_type = data_actual_02['data']['fee_data'][1]['value_type']
        # 'response' - verify value under 'data' and 'fee_data', item 2
        AU.assert_equals('ifc_name', ifc_name_02, value_fee_data_ifc_name)
        AU.assert_equals('share_fee', share_fee_02, value_fee_data_share_fee)
        AU.assert_equals('ifc_code', ifc_code_02, value_fee_data_ifc_code)
        AU.assert_equals('payrate', payrate_02, value_fee_data_payrate)
        AU.assert_equals('ifc_value', ifc_value_02, value_fee_data_ifc_value)
        AU.assert_equals('ifc_amount', ifc_amount_02, value_fee_data_ifc_amount)
        AU.assert_equals('currency_account_code', currency_account_code_02, value_fee_data_currency_account_code)
        AU.assert_equals('floor_value', floor_value_02, value_fee_data_floor_value)
        AU.assert_equals('ceiling_value', ceiling_value_02, value_fee_data_ceiling_value)
        AU.assert_equals('share_rate', share_rate_02, value_fee_data_share_rate)
        AU.assert_equals('share_amount', share_amount_02, value_fee_data_share_amount)
        AU.assert_equals('round_rate', round_rate_02, value_fee_data_round_rate)
        AU.assert_equals('round_amount', round_amount_02, value_fee_data_round_amount)
        AU.assert_equals('currency_fee_code', currency_fee_code_02, value_fee_data_currency_fee_code)
        AU.assert_equals('pay_source', pay_source_02, value_fee_data_pay_source)
        # AU.assert_null('value_typect', value_fee_data_value_typect)
        AU.assert_equals('value_type', value_type_02, value_fee_data_value_type)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_02, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 3, len(data_actual_posting))
        # 'postings' - verify key response, item 1
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array, item 1
        value_TransactionNumber = data_actual_posting[0]['TransactionNumber']
        value_TransTableName = data_actual_posting[0]['TransTableName']
        value_TransId = data_actual_posting[0]['TransId']
        value_SysAccountName = data_actual_posting[0]['SysAccountName']
        value_GLAccount = data_actual_posting[0]['GLAccount']
        value_DorC = data_actual_posting[0]['DorC']
        value_TransactionStatus = data_actual_posting[0]['TransactionStatus']
        value_Amount = data_actual_posting[0]['Amount']
        value_BranchCode = data_actual_posting[0]['BranchCode']
        value_CurrencyCode = data_actual_posting[0]['CurrencyCode']
        value_ValueDate = data_actual_posting[0]['ValueDate']
        value_Posted = data_actual_posting[0]['Posted']
        value_AccountingGroup = data_actual_posting[0]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[0]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[0]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[0]['BaseCurrencyAmount']
        value_Id = data_actual_posting[0]['Id']
        # 'postings' - verify value under array, item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', Decimal(str(amount_deposit)) - (Decimal(str(ifc_amount_01)) + Decimal(str(ifc_amount_02))), Decimal(str(value_Amount)), value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 2
        AU.assert_exists(expected_key['postings'], data_actual_posting[1])
        # 'postings' - get value under array, item 2
        value_TransactionNumber = data_actual_posting[1]['TransactionNumber']
        value_TransTableName = data_actual_posting[1]['TransTableName']
        value_TransId = data_actual_posting[1]['TransId']
        value_SysAccountName = data_actual_posting[1]['SysAccountName']
        value_GLAccount = data_actual_posting[1]['GLAccount']
        value_DorC = data_actual_posting[1]['DorC']
        value_TransactionStatus = data_actual_posting[1]['TransactionStatus']
        value_Amount = data_actual_posting[1]['Amount']
        value_BranchCode = data_actual_posting[1]['BranchCode']
        value_CurrencyCode = data_actual_posting[1]['CurrencyCode']
        value_ValueDate = data_actual_posting[1]['ValueDate']
        value_Posted = data_actual_posting[1]['Posted']
        value_AccountingGroup = data_actual_posting[1]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[1]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[1]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[1]['BaseCurrencyAmount']
        value_Id = data_actual_posting[1]['Id']
        # 'postings' - verify value under array, item 2
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_01, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_01, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 3
        AU.assert_exists(expected_key['postings'], data_actual_posting[2])
        # 'postings' - get value under array, item 3
        value_TransactionNumber = data_actual_posting[2]['TransactionNumber']
        value_TransTableName = data_actual_posting[2]['TransTableName']
        value_TransId = data_actual_posting[2]['TransId']
        value_SysAccountName = data_actual_posting[2]['SysAccountName']
        value_GLAccount = data_actual_posting[2]['GLAccount']
        value_DorC = data_actual_posting[2]['DorC']
        value_TransactionStatus = data_actual_posting[2]['TransactionStatus']
        value_Amount = data_actual_posting[2]['Amount']
        value_BranchCode = data_actual_posting[2]['BranchCode']
        value_CurrencyCode = data_actual_posting[2]['CurrencyCode']
        value_ValueDate = data_actual_posting[2]['ValueDate']
        value_Posted = data_actual_posting[2]['Posted']
        value_AccountingGroup = data_actual_posting[2]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[2]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[2]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[2]['BaseCurrencyAmount']
        value_Id = data_actual_posting[2]['Id']
        # 'postings' - verify value under array, item 3
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_02, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_02, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)

    def test_04_sp_dpt_mdp_003_success_saving_account_status_new_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='BSMMK0000'
        catalog_name='Bonus savings account  in MMK'
        deposit_type='Savings'
        deposit_sub_type='S2'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='S',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_apr['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs_01 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_01 = RU.get_p2_content_response_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_01)
        # 'response' - get value level 1
        value_status = data_actual_01['status']
        value_error_message = data_actual_01['error_message']
        value_error_code = data_actual_01['error_code']
        value_data = data_actual_01['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mdp'], data_actual_01['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_mdp_depositor_description'], data_actual_01['data']['depositor_description'])
        # 'response' - get value in 'data'
        value_data_account_number = data_actual_01['data']['account_number']
        value_data_amount_deposit = data_actual_01['data']['amount_deposit']
        value_data_debit_accounting = data_actual_01['data']['debit_accounting']
        value_data_accounting_currency = data_actual_01['data']['accounting_currency']
        value_data_cross_rate = data_actual_01['data']['cross_rate']
        value_data_acounting_amount = data_actual_01['data']['acounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual_01['data']['exchange_rate_of_accounting_bcy']
        value_data_accounting_amount_bcy = data_actual_01['data']['accounting_amount_bcy']
        value_data_depositor_name = data_actual_01['data']['depositor_name']
        value_data_depositor_code = data_actual_01['data']['depositor_code']
        value_data_depositor_address = data_actual_01['data']['depositor_address']
        value_data_values_date = data_actual_01['data']['values_date']
        value_data_deposit_currency = data_actual_01['data']['deposit_currency']
        value_data_exchange_rate_debit_account_bcy = data_actual_01['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual_01['data']['amount_debit_account_bcy']
        value_data_prepaid_interest = data_actual_01['data']['prepaid_interest']
        value_data_accounting_currency1 = data_actual_01['data']['accounting_currency1']
        value_data_fee_data = data_actual_01['data']['fee_data']
        value_data_total_fee = data_actual_01['data']['total_fee']
        value_data_branch_name = data_actual_01['data']['branch_name']
        value_data_transaction_code = data_actual_01['data']['transaction_code']
        value_data_transaction_number = data_actual_01['data']['transaction_number']
        value_data_transaction_type = data_actual_01['data']['transaction_type']
        value_data_sub_code = data_actual_01['data']['sub_code']
        value_data_transaction_date = data_actual_01['data']['transaction_date']
        value_data_service_sys_date = data_actual_01['data']['service_sys_date']
        value_data_reference_id = data_actual_01['data']['reference_id']
        value_data_ref_id = data_actual_01['data']['ref_id']
        value_data_reference_code = data_actual_01['data']['reference_code']
        value_data_business_code = data_actual_01['data']['business_code']
        value_data_value_date = data_actual_01['data']['value_date']
        value_data_current_user_code = data_actual_01['data']['current_user_code']
        value_data_current_branch_code = data_actual_01['data']['current_branch_code']
        value_data_current_username = data_actual_01['data']['current_username']
        value_data_current_loginname = data_actual_01['data']['current_loginname']
        value_data_user_approve = data_actual_01['data']['user_approve']
        value_data_status = data_actual_01['data']['status']
        value_data_is_reverse = data_actual_01['data']['is_reverse']
        value_data_amount1 = data_actual_01['data']['amount1']
        value_data_description = data_actual_01['data']['description']
        value_data_token = data_actual_01['data']['token']
        value_data_is_transaction_reverse = data_actual_01['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual_01['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
        AU.assert_equals('debit_accounting', debit_accounting_valid, value_data_debit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('acounting_amount', 0.0, value_data_acounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1.0, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('accounting_amount_bcy', 0.0, value_data_accounting_amount_bcy)
        AU.assert_equals('depositor_name', account_name_individual, value_data_depositor_name)
        AU.assert_equals('depositor_code', customer_code_individual, value_data_depositor_code)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('deposit_currency', deposit_currency, value_data_deposit_currency)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('prepaid_interest', 0.0, value_data_prepaid_interest)
        AU.assert_equals('accounting_currency1', accounting_currency1, value_data_accounting_currency1)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_fee', 0.0, value_data_total_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('transaction_code', 'DPT_MDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_empty('reference_code', value_data_reference_code)
        AU.assert_empty('business_code', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_empty('user_approve', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_false('is_reverse', value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1112: Miscellaneous deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_false('is_transaction_reverse', value_data_is_transaction_reverse)
        AU.assert_false('is_transaction_compensated', value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 1, len(data_actual_posting))
        # 'postings' - verify key response, item 1
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array, item 1
        value_TransactionNumber = data_actual_posting[0]['TransactionNumber']
        value_TransTableName = data_actual_posting[0]['TransTableName']
        value_TransId = data_actual_posting[0]['TransId']
        value_SysAccountName = data_actual_posting[0]['SysAccountName']
        value_GLAccount = data_actual_posting[0]['GLAccount']
        value_DorC = data_actual_posting[0]['DorC']
        value_TransactionStatus = data_actual_posting[0]['TransactionStatus']
        value_Amount = data_actual_posting[0]['Amount']
        value_BranchCode = data_actual_posting[0]['BranchCode']
        value_CurrencyCode = data_actual_posting[0]['CurrencyCode']
        value_ValueDate = data_actual_posting[0]['ValueDate']
        value_Posted = data_actual_posting[0]['Posted']
        value_AccountingGroup = data_actual_posting[0]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[0]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[0]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[0]['BaseCurrencyAmount']
        value_Id = data_actual_posting[0]['Id']
        # 'postings' - verify value under array, item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', amount_deposit, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # STEP 04: miscellaneous deposit to deposit status 'Normal'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs_02 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_02 = RU.get_p2_content_response_by_step_code(rs_02, step_code)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_02)
        # 'response' - get value level 1
        value_status = data_actual_02['status']
        value_error_message = data_actual_02['error_message']
        value_error_code = data_actual_02['error_code']
        value_data = data_actual_02['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mdp'], data_actual_02['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_mdp_depositor_description'], data_actual_02['data']['depositor_description'])
        # 'response' - get value in 'data'
        value_data_account_number = data_actual_02['data']['account_number']
        value_data_amount_deposit = data_actual_02['data']['amount_deposit']
        value_data_debit_accounting = data_actual_02['data']['debit_accounting']
        value_data_accounting_currency = data_actual_02['data']['accounting_currency']
        value_data_cross_rate = data_actual_02['data']['cross_rate']
        value_data_acounting_amount = data_actual_02['data']['acounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual_02['data']['exchange_rate_of_accounting_bcy']
        value_data_accounting_amount_bcy = data_actual_02['data']['accounting_amount_bcy']
        value_data_depositor_name = data_actual_02['data']['depositor_name']
        value_data_depositor_code = data_actual_02['data']['depositor_code']
        value_data_depositor_address = data_actual_02['data']['depositor_address']
        value_data_values_date = data_actual_02['data']['values_date']
        value_data_deposit_currency = data_actual_02['data']['deposit_currency']
        value_data_exchange_rate_debit_account_bcy = data_actual_02['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual_02['data']['amount_debit_account_bcy']
        value_data_prepaid_interest = data_actual_02['data']['prepaid_interest']
        value_data_accounting_currency1 = data_actual_02['data']['accounting_currency1']
        value_data_fee_data = data_actual_02['data']['fee_data']
        value_data_total_fee = data_actual_02['data']['total_fee']
        value_data_branch_name = data_actual_02['data']['branch_name']
        value_data_transaction_code = data_actual_02['data']['transaction_code']
        value_data_transaction_number = data_actual_02['data']['transaction_number']
        value_data_transaction_type = data_actual_02['data']['transaction_type']
        value_data_sub_code = data_actual_02['data']['sub_code']
        value_data_transaction_date = data_actual_02['data']['transaction_date']
        value_data_service_sys_date = data_actual_02['data']['service_sys_date']
        value_data_reference_id = data_actual_02['data']['reference_id']
        value_data_ref_id = data_actual_02['data']['ref_id']
        value_data_reference_code = data_actual_02['data']['reference_code']
        value_data_business_code = data_actual_02['data']['business_code']
        value_data_value_date = data_actual_02['data']['value_date']
        value_data_current_user_code = data_actual_02['data']['current_user_code']
        value_data_current_branch_code = data_actual_02['data']['current_branch_code']
        value_data_current_username = data_actual_02['data']['current_username']
        value_data_current_loginname = data_actual_02['data']['current_loginname']
        value_data_user_approve = data_actual_02['data']['user_approve']
        value_data_status = data_actual_02['data']['status']
        value_data_is_reverse = data_actual_02['data']['is_reverse']
        value_data_amount1 = data_actual_02['data']['amount1']
        value_data_description = data_actual_02['data']['description']
        value_data_token = data_actual_02['data']['token']
        value_data_is_transaction_reverse = data_actual_02['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual_02['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
        AU.assert_equals('debit_accounting', debit_accounting_valid, value_data_debit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('acounting_amount', 0.0, value_data_acounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1.0, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('accounting_amount_bcy', 0.0, value_data_accounting_amount_bcy)
        AU.assert_equals('depositor_name', account_name_individual, value_data_depositor_name)
        AU.assert_equals('depositor_code', customer_code_individual, value_data_depositor_code)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('deposit_currency', deposit_currency, value_data_deposit_currency)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('prepaid_interest', 0.0, value_data_prepaid_interest)
        AU.assert_equals('accounting_currency1', accounting_currency1, value_data_accounting_currency1)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_fee', 0.0, value_data_total_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('transaction_code', 'DPT_MDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_empty('reference_code', value_data_reference_code)
        AU.assert_empty('business_code', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_empty('user_approve', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_false('is_reverse', value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1112: Miscellaneous deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_false('is_transaction_reverse', value_data_is_transaction_reverse)
        AU.assert_false('is_transaction_compensated', value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_02, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        AU.assert_equals('Number item in posting', 1, len(data_actual_posting))
        # 'postings' - verify key response, item 1
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array, item 1
        value_TransactionNumber = data_actual_posting[0]['TransactionNumber']
        value_TransTableName = data_actual_posting[0]['TransTableName']
        value_TransId_step_main = data_actual_posting[0]['TransId']
        value_SysAccountName = data_actual_posting[0]['SysAccountName']
        value_GLAccount = data_actual_posting[0]['GLAccount']
        value_DorC = data_actual_posting[0]['DorC']
        value_TransactionStatus = data_actual_posting[0]['TransactionStatus']
        value_Amount = data_actual_posting[0]['Amount']
        value_BranchCode = data_actual_posting[0]['BranchCode']
        value_CurrencyCode = data_actual_posting[0]['CurrencyCode']
        value_ValueDate = data_actual_posting[0]['ValueDate']
        value_Posted = data_actual_posting[0]['Posted']
        value_AccountingGroup_step_main = data_actual_posting[0]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[0]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[0]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[0]['BaseCurrencyAmount']
        value_Id = data_actual_posting[0]['Id']
        # 'postings' - verify value under array, item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId_step_main)
        AU.assert_not_null('TransId', value_TransId_step_main)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', amount_deposit, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup_step_main)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)

    def test_04_sp_dpt_mdp_004_success_saving_account_status_new_normal_add_fee(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='BSMMK0000'
        catalog_name='Bonus savings account  in MMK'
        deposit_type='Savings'
        deposit_sub_type='S2'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='S',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_apr['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 03: miscellaneous deposit to deposit status 'New'
        total_fee=3200.0
        share_fee_01=0.0
        ifc_name_01='Withdrawal (MMK) For Different Region  (By Cash)'
        value_type_01='P'
        ifc_code_01=302
        payrate_01=100
        ifc_value_01=0.025
        ifc_amount_01=200.0
        currency_account_code_01=deposit_currency
        floor_value_01=200.0
        ceiling_value_01=0.0
        share_rate_01=0.0
        share_amount_01=0.0
        round_rate_01=0.0
        round_amount_01=0.0
        currency_fee_code_01=deposit_currency
        pay_source_01='CSH'
        share_fee_02=0.0
        ifc_name_02='Account To Account Transfer (MMK) For Same Region'
        value_type_02='F'
        ifc_code_02=309
        payrate_02=100
        ifc_value_02=3000.0
        ifc_amount_02=3000.0
        currency_account_code_02=deposit_currency
        floor_value_02=0.0
        ceiling_value_02=0.0
        share_rate_02=0.0
        share_amount_02=0.0
        round_rate_02=0.0
        round_amount_02=0.0
        currency_fee_code_02=deposit_currency
        pay_source_02='CSH'
        gl_account_ifcc_01='003303030100010101'
        gl_account_ifcc_02='003303030100010101'
        fee_data = [
            {
                "share_fee": share_fee_01,
                "ifc_name": ifc_name_01,
                "value_type": value_type_01,
                "ifc_code": ifc_code_01,
                "payrate": payrate_01,
                "ifc_value": ifc_value_01,
                "ifc_amount": ifc_amount_01,
                "currency_account_code": currency_account_code_01,
                "floor_value": floor_value_01,
                "ceiling_value": ceiling_value_01,
                "share_rate": share_rate_01,
                "share_amount": share_amount_01,
                "round_rate": round_rate_01,
                "round_amount": round_amount_01,
                "currency_fee_code": currency_fee_code_01,
                "pay_source": pay_source_01
            },
            {
                "share_fee": share_fee_02,
                "ifc_name": ifc_name_02,
                "value_type": value_type_02,
                "ifc_code": ifc_code_02,
                "payrate": payrate_02,
                "ifc_value": ifc_value_02,
                "ifc_amount": ifc_amount_02,
                "currency_account_code": currency_account_code_02,
                "floor_value": floor_value_02,
                "ceiling_value": ceiling_value_02,
                "share_rate": share_rate_02,
                "share_amount": share_amount_02,
                "round_rate": round_rate_02,
                "round_amount": round_amount_02,
                "currency_fee_code": currency_fee_code_02,
                "pay_source": pay_source_02
            }
        ]
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1,
            fee_data=fee_data
        )
        rs_01 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_01 = RU.get_p2_content_response_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_01)
        # 'response' - get value level 1
        value_status = data_actual_01['status']
        value_error_message = data_actual_01['error_message']
        value_error_code = data_actual_01['error_code']
        value_data = data_actual_01['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mdp'], data_actual_01['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_mdp_depositor_description'], data_actual_01['data']['depositor_description'])
        # 'response' - get value in 'data'
        value_data_account_number = data_actual_01['data']['account_number']
        value_data_amount_deposit = data_actual_01['data']['amount_deposit']
        value_data_debit_accounting = data_actual_01['data']['debit_accounting']
        value_data_accounting_currency = data_actual_01['data']['accounting_currency']
        value_data_cross_rate = data_actual_01['data']['cross_rate']
        value_data_acounting_amount = data_actual_01['data']['acounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual_01['data']['exchange_rate_of_accounting_bcy']
        value_data_accounting_amount_bcy = data_actual_01['data']['accounting_amount_bcy']
        value_data_depositor_name = data_actual_01['data']['depositor_name']
        value_data_depositor_code = data_actual_01['data']['depositor_code']
        value_data_depositor_address = data_actual_01['data']['depositor_address']
        value_data_values_date = data_actual_01['data']['values_date']
        value_data_deposit_currency = data_actual_01['data']['deposit_currency']
        value_data_exchange_rate_debit_account_bcy = data_actual_01['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual_01['data']['amount_debit_account_bcy']
        value_data_prepaid_interest = data_actual_01['data']['prepaid_interest']
        value_data_accounting_currency1 = data_actual_01['data']['accounting_currency1']
        value_data_fee_data = data_actual_01['data']['fee_data']
        value_data_total_fee = data_actual_01['data']['total_fee']
        value_data_branch_name = data_actual_01['data']['branch_name']
        value_data_transaction_code = data_actual_01['data']['transaction_code']
        value_data_transaction_number = data_actual_01['data']['transaction_number']
        value_data_transaction_type = data_actual_01['data']['transaction_type']
        value_data_sub_code = data_actual_01['data']['sub_code']
        value_data_transaction_date = data_actual_01['data']['transaction_date']
        value_data_service_sys_date = data_actual_01['data']['service_sys_date']
        value_data_reference_id = data_actual_01['data']['reference_id']
        value_data_ref_id = data_actual_01['data']['ref_id']
        value_data_reference_code = data_actual_01['data']['reference_code']
        value_data_business_code = data_actual_01['data']['business_code']
        value_data_value_date = data_actual_01['data']['value_date']
        value_data_current_user_code = data_actual_01['data']['current_user_code']
        value_data_current_branch_code = data_actual_01['data']['current_branch_code']
        value_data_current_username = data_actual_01['data']['current_username']
        value_data_current_loginname = data_actual_01['data']['current_loginname']
        value_data_user_approve = data_actual_01['data']['user_approve']
        value_data_status = data_actual_01['data']['status']
        value_data_is_reverse = data_actual_01['data']['is_reverse']
        value_data_amount1 = data_actual_01['data']['amount1']
        value_data_description = data_actual_01['data']['description']
        value_data_token = data_actual_01['data']['token']
        value_data_is_transaction_reverse = data_actual_01['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual_01['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
        AU.assert_equals('debit_accounting', debit_accounting_valid, value_data_debit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('acounting_amount', 0.0, value_data_acounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1.0, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('accounting_amount_bcy', 0.0, value_data_accounting_amount_bcy)
        AU.assert_equals('depositor_name', account_name_individual, value_data_depositor_name)
        AU.assert_equals('depositor_code', customer_code_individual, value_data_depositor_code)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('deposit_currency', deposit_currency, value_data_deposit_currency)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('prepaid_interest', 0.0, value_data_prepaid_interest)
        AU.assert_equals('accounting_currency1', accounting_currency1, value_data_accounting_currency1)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_fee', total_fee, value_data_total_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('transaction_code', 'DPT_MDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_empty('reference_code', value_data_reference_code)
        AU.assert_empty('business_code', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_empty('user_approve', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_false('is_reverse', value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1112: Miscellaneous deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_false('is_transaction_reverse', value_data_is_transaction_reverse)
        AU.assert_false('is_transaction_compensated', value_data_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'fee_data', item 1
        AU.assert_exists(expected_key['fee_data'], data_actual_01['data']['fee_data'][0])
        # 'response' - get value under 'data' and 'fee_data', item 1
        value_fee_data_ifc_name = data_actual_01['data']['fee_data'][0]['ifc_name']
        value_fee_data_share_fee = data_actual_01['data']['fee_data'][0]['share_fee']
        value_fee_data_ifc_code = data_actual_01['data']['fee_data'][0]['ifc_code']
        value_fee_data_payrate = data_actual_01['data']['fee_data'][0]['payrate']
        value_fee_data_ifc_value = data_actual_01['data']['fee_data'][0]['ifc_value']
        value_fee_data_ifc_amount = data_actual_01['data']['fee_data'][0]['ifc_amount']
        value_fee_data_currency_account_code = data_actual_01['data']['fee_data'][0]['currency_account_code']
        value_fee_data_floor_value = data_actual_01['data']['fee_data'][0]['floor_value']
        value_fee_data_ceiling_value = data_actual_01['data']['fee_data'][0]['ceiling_value']
        value_fee_data_share_rate = data_actual_01['data']['fee_data'][0]['share_rate']
        value_fee_data_share_amount = data_actual_01['data']['fee_data'][0]['share_amount']
        value_fee_data_round_rate = data_actual_01['data']['fee_data'][0]['round_rate']
        value_fee_data_round_amount = data_actual_01['data']['fee_data'][0]['round_amount']
        value_fee_data_currency_fee_code = data_actual_01['data']['fee_data'][0]['currency_fee_code']
        value_fee_data_pay_source = data_actual_01['data']['fee_data'][0]['pay_source']
        # value_fee_data_value_typect = data_actual_01['data']['fee_data'][0]['value_typect']
        value_fee_data_value_type = data_actual_01['data']['fee_data'][0]['value_type']
        # 'response' - verify value under 'data' and 'fee_data', item 1
        AU.assert_equals('ifc_name', ifc_name_01, value_fee_data_ifc_name)
        AU.assert_equals('share_fee', share_fee_01, value_fee_data_share_fee)
        AU.assert_equals('ifc_code', ifc_code_01, value_fee_data_ifc_code)
        AU.assert_equals('payrate', payrate_01, value_fee_data_payrate)
        AU.assert_equals('ifc_value', ifc_value_01, value_fee_data_ifc_value)
        AU.assert_equals('ifc_amount', ifc_amount_01, value_fee_data_ifc_amount)
        AU.assert_equals('currency_account_code', currency_account_code_01, value_fee_data_currency_account_code)
        AU.assert_equals('floor_value', floor_value_01, value_fee_data_floor_value)
        AU.assert_equals('ceiling_value', ceiling_value_01, value_fee_data_ceiling_value)
        AU.assert_equals('share_rate', share_rate_01, value_fee_data_share_rate)
        AU.assert_equals('share_amount', share_amount_01, value_fee_data_share_amount)
        AU.assert_equals('round_rate', round_rate_01, value_fee_data_round_rate)
        AU.assert_equals('round_amount', round_amount_01, value_fee_data_round_amount)
        AU.assert_equals('currency_fee_code', currency_fee_code_01, value_fee_data_currency_fee_code)
        AU.assert_equals('pay_source', pay_source_01, value_fee_data_pay_source)
        # AU.assert_null('value_typect', value_fee_data_value_typect)
        AU.assert_equals('value_type', value_type_01, value_fee_data_value_type)
        # 'response' - verify key response under 'data' and 'fee_data', item 2
        AU.assert_exists(expected_key['fee_data'], data_actual_01['data']['fee_data'][1])
        # 'response' - get value under 'data' and 'fee_data', item 2
        value_fee_data_ifc_name = data_actual_01['data']['fee_data'][1]['ifc_name']
        value_fee_data_share_fee = data_actual_01['data']['fee_data'][1]['share_fee']
        value_fee_data_ifc_code = data_actual_01['data']['fee_data'][1]['ifc_code']
        value_fee_data_payrate = data_actual_01['data']['fee_data'][1]['payrate']
        value_fee_data_ifc_value = data_actual_01['data']['fee_data'][1]['ifc_value']
        value_fee_data_ifc_amount = data_actual_01['data']['fee_data'][1]['ifc_amount']
        value_fee_data_currency_account_code = data_actual_01['data']['fee_data'][1]['currency_account_code']
        value_fee_data_floor_value = data_actual_01['data']['fee_data'][1]['floor_value']
        value_fee_data_ceiling_value = data_actual_01['data']['fee_data'][1]['ceiling_value']
        value_fee_data_share_rate = data_actual_01['data']['fee_data'][1]['share_rate']
        value_fee_data_share_amount = data_actual_01['data']['fee_data'][1]['share_amount']
        value_fee_data_round_rate = data_actual_01['data']['fee_data'][1]['round_rate']
        value_fee_data_round_amount = data_actual_01['data']['fee_data'][1]['round_amount']
        value_fee_data_currency_fee_code = data_actual_01['data']['fee_data'][1]['currency_fee_code']
        value_fee_data_pay_source = data_actual_01['data']['fee_data'][1]['pay_source']
        # value_fee_data_value_typect = data_actual_01['data']['fee_data'][1]['value_typect']
        value_fee_data_value_type = data_actual_01['data']['fee_data'][1]['value_type']
        # 'response' - verify value under 'data' and 'fee_data', item 2
        AU.assert_equals('ifc_name', ifc_name_02, value_fee_data_ifc_name)
        AU.assert_equals('share_fee', share_fee_02, value_fee_data_share_fee)
        AU.assert_equals('ifc_code', ifc_code_02, value_fee_data_ifc_code)
        AU.assert_equals('payrate', payrate_02, value_fee_data_payrate)
        AU.assert_equals('ifc_value', ifc_value_02, value_fee_data_ifc_value)
        AU.assert_equals('ifc_amount', ifc_amount_02, value_fee_data_ifc_amount)
        AU.assert_equals('currency_account_code', currency_account_code_02, value_fee_data_currency_account_code)
        AU.assert_equals('floor_value', floor_value_02, value_fee_data_floor_value)
        AU.assert_equals('ceiling_value', ceiling_value_02, value_fee_data_ceiling_value)
        AU.assert_equals('share_rate', share_rate_02, value_fee_data_share_rate)
        AU.assert_equals('share_amount', share_amount_02, value_fee_data_share_amount)
        AU.assert_equals('round_rate', round_rate_02, value_fee_data_round_rate)
        AU.assert_equals('round_amount', round_amount_02, value_fee_data_round_amount)
        AU.assert_equals('currency_fee_code', currency_fee_code_02, value_fee_data_currency_fee_code)
        AU.assert_equals('pay_source', pay_source_02, value_fee_data_pay_source)
        # AU.assert_null('value_typect', value_fee_data_value_typect)
        AU.assert_equals('value_type', value_type_02, value_fee_data_value_type)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 3, len(data_actual_posting))
        # 'postings' - verify key response, item 1
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array, item 1
        value_TransactionNumber = data_actual_posting[0]['TransactionNumber']
        value_TransTableName = data_actual_posting[0]['TransTableName']
        value_TransId = data_actual_posting[0]['TransId']
        value_SysAccountName = data_actual_posting[0]['SysAccountName']
        value_GLAccount = data_actual_posting[0]['GLAccount']
        value_DorC = data_actual_posting[0]['DorC']
        value_TransactionStatus = data_actual_posting[0]['TransactionStatus']
        value_Amount = data_actual_posting[0]['Amount']
        value_BranchCode = data_actual_posting[0]['BranchCode']
        value_CurrencyCode = data_actual_posting[0]['CurrencyCode']
        value_ValueDate = data_actual_posting[0]['ValueDate']
        value_Posted = data_actual_posting[0]['Posted']
        value_AccountingGroup = data_actual_posting[0]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[0]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[0]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[0]['BaseCurrencyAmount']
        value_Id = data_actual_posting[0]['Id']
        # 'postings' - verify value under array, item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', Decimal(str(amount_deposit)) - (Decimal(str(ifc_amount_01)) + Decimal(str(ifc_amount_02))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 2
        AU.assert_exists(expected_key['postings'], data_actual_posting[1])
        # 'postings' - get value under array, item 2
        value_TransactionNumber = data_actual_posting[1]['TransactionNumber']
        value_TransTableName = data_actual_posting[1]['TransTableName']
        value_TransId = data_actual_posting[1]['TransId']
        value_SysAccountName = data_actual_posting[1]['SysAccountName']
        value_GLAccount = data_actual_posting[1]['GLAccount']
        value_DorC = data_actual_posting[1]['DorC']
        value_TransactionStatus = data_actual_posting[1]['TransactionStatus']
        value_Amount = data_actual_posting[1]['Amount']
        value_BranchCode = data_actual_posting[1]['BranchCode']
        value_CurrencyCode = data_actual_posting[1]['CurrencyCode']
        value_ValueDate = data_actual_posting[1]['ValueDate']
        value_Posted = data_actual_posting[1]['Posted']
        value_AccountingGroup = data_actual_posting[1]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[1]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[1]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[1]['BaseCurrencyAmount']
        value_Id = data_actual_posting[1]['Id']
        # 'postings' - verify value under array, item 2
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_01, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_01, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 3
        AU.assert_exists(expected_key['postings'], data_actual_posting[2])
        # 'postings' - get value under array, item 3
        value_TransactionNumber = data_actual_posting[2]['TransactionNumber']
        value_TransTableName = data_actual_posting[2]['TransTableName']
        value_TransId = data_actual_posting[2]['TransId']
        value_SysAccountName = data_actual_posting[2]['SysAccountName']
        value_GLAccount = data_actual_posting[2]['GLAccount']
        value_DorC = data_actual_posting[2]['DorC']
        value_TransactionStatus = data_actual_posting[2]['TransactionStatus']
        value_Amount = data_actual_posting[2]['Amount']
        value_BranchCode = data_actual_posting[2]['BranchCode']
        value_CurrencyCode = data_actual_posting[2]['CurrencyCode']
        value_ValueDate = data_actual_posting[2]['ValueDate']
        value_Posted = data_actual_posting[2]['Posted']
        value_AccountingGroup = data_actual_posting[2]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[2]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[2]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[2]['BaseCurrencyAmount']
        value_Id = data_actual_posting[2]['Id']
        # 'postings' - verify value under array, item 3
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_02, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_02, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # STEP 04: miscellaneous deposit to deposit status 'Normal'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1,
            fee_data=fee_data
        )
        rs_02 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_02 = RU.get_p2_content_response_by_step_code(rs_02, step_code)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_02)
        # 'response' - get value level 1
        value_status = data_actual_02['status']
        value_error_message = data_actual_02['error_message']
        value_error_code = data_actual_02['error_code']
        value_data = data_actual_02['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mdp'], data_actual_02['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_mdp_depositor_description'], data_actual_02['data']['depositor_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual_02['data']['account_number']
        value_data_amount_deposit = data_actual_02['data']['amount_deposit']
        value_data_debit_accounting = data_actual_02['data']['debit_accounting']
        value_data_accounting_currency = data_actual_02['data']['accounting_currency']
        value_data_cross_rate = data_actual_02['data']['cross_rate']
        value_data_acounting_amount = data_actual_02['data']['acounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual_02['data']['exchange_rate_of_accounting_bcy']
        value_data_accounting_amount_bcy = data_actual_02['data']['accounting_amount_bcy']
        value_data_depositor_name = data_actual_02['data']['depositor_name']
        value_data_depositor_code = data_actual_02['data']['depositor_code']
        value_data_depositor_address = data_actual_02['data']['depositor_address']
        value_data_values_date = data_actual_02['data']['values_date']
        value_data_deposit_currency = data_actual_02['data']['deposit_currency']
        value_data_exchange_rate_debit_account_bcy = data_actual_02['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual_02['data']['amount_debit_account_bcy']
        value_data_prepaid_interest = data_actual_02['data']['prepaid_interest']
        value_data_accounting_currency1 = data_actual_02['data']['accounting_currency1']
        value_data_fee_data = data_actual_02['data']['fee_data']
        value_data_total_fee = data_actual_02['data']['total_fee']
        value_data_branch_name = data_actual_02['data']['branch_name']
        value_data_transaction_code = data_actual_02['data']['transaction_code']
        value_data_transaction_number = data_actual_02['data']['transaction_number']
        value_data_transaction_type = data_actual_02['data']['transaction_type']
        value_data_sub_code = data_actual_02['data']['sub_code']
        value_data_transaction_date = data_actual_02['data']['transaction_date']
        value_data_service_sys_date = data_actual_02['data']['service_sys_date']
        value_data_reference_id = data_actual_02['data']['reference_id']
        value_data_ref_id = data_actual_02['data']['ref_id']
        value_data_reference_code = data_actual_02['data']['reference_code']
        value_data_business_code = data_actual_02['data']['business_code']
        value_data_value_date = data_actual_02['data']['value_date']
        value_data_current_user_code = data_actual_02['data']['current_user_code']
        value_data_current_branch_code = data_actual_02['data']['current_branch_code']
        value_data_current_username = data_actual_02['data']['current_username']
        value_data_current_loginname = data_actual_02['data']['current_loginname']
        value_data_user_approve = data_actual_02['data']['user_approve']
        value_data_status = data_actual_02['data']['status']
        value_data_is_reverse = data_actual_02['data']['is_reverse']
        value_data_amount1 = data_actual_02['data']['amount1']
        value_data_description = data_actual_02['data']['description']
        value_data_token = data_actual_02['data']['token']
        value_data_is_transaction_reverse = data_actual_02['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual_02['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
        AU.assert_equals('debit_accounting', debit_accounting_valid, value_data_debit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('acounting_amount', 0.0, value_data_acounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1.0, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('accounting_amount_bcy', 0.0, value_data_accounting_amount_bcy)
        AU.assert_equals('depositor_name', account_name_individual, value_data_depositor_name)
        AU.assert_equals('depositor_code', customer_code_individual, value_data_depositor_code)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('deposit_currency', deposit_currency, value_data_deposit_currency)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('prepaid_interest', 0.0, value_data_prepaid_interest)
        AU.assert_equals('accounting_currency1', accounting_currency1, value_data_accounting_currency1)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_fee', total_fee, value_data_total_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('transaction_code', 'DPT_MDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_empty('reference_code', value_data_reference_code)
        AU.assert_empty('business_code', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_empty('user_approve', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_false('is_reverse', value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1112: Miscellaneous deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_false('is_transaction_reverse', value_data_is_transaction_reverse)
        AU.assert_false('is_transaction_compensated', value_data_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'fee_data', item 1
        AU.assert_exists(expected_key['fee_data'], data_actual_02['data']['fee_data'][0])
        # 'response' - get value under 'data' and 'fee_data', item 1
        value_fee_data_ifc_name = data_actual_02['data']['fee_data'][0]['ifc_name']
        value_fee_data_share_fee = data_actual_02['data']['fee_data'][0]['share_fee']
        value_fee_data_ifc_code = data_actual_02['data']['fee_data'][0]['ifc_code']
        value_fee_data_payrate = data_actual_02['data']['fee_data'][0]['payrate']
        value_fee_data_ifc_value = data_actual_02['data']['fee_data'][0]['ifc_value']
        value_fee_data_ifc_amount = data_actual_02['data']['fee_data'][0]['ifc_amount']
        value_fee_data_currency_account_code = data_actual_02['data']['fee_data'][0]['currency_account_code']
        value_fee_data_floor_value = data_actual_02['data']['fee_data'][0]['floor_value']
        value_fee_data_ceiling_value = data_actual_02['data']['fee_data'][0]['ceiling_value']
        value_fee_data_share_rate = data_actual_02['data']['fee_data'][0]['share_rate']
        value_fee_data_share_amount = data_actual_02['data']['fee_data'][0]['share_amount']
        value_fee_data_round_rate = data_actual_02['data']['fee_data'][0]['round_rate']
        value_fee_data_round_amount = data_actual_02['data']['fee_data'][0]['round_amount']
        value_fee_data_currency_fee_code = data_actual_02['data']['fee_data'][0]['currency_fee_code']
        value_fee_data_pay_source = data_actual_02['data']['fee_data'][0]['pay_source']
        # value_fee_data_value_typect = data_actual_02['data']['fee_data'][0]['value_typect']
        value_fee_data_value_type = data_actual_02['data']['fee_data'][0]['value_type']
        # 'response' - verify value under 'data' and 'fee_data', item 1
        AU.assert_equals('ifc_name', ifc_name_01, value_fee_data_ifc_name)
        AU.assert_equals('share_fee', share_fee_01, value_fee_data_share_fee)
        AU.assert_equals('ifc_code', ifc_code_01, value_fee_data_ifc_code)
        AU.assert_equals('payrate', payrate_01, value_fee_data_payrate)
        AU.assert_equals('ifc_value', ifc_value_01, value_fee_data_ifc_value)
        AU.assert_equals('ifc_amount', ifc_amount_01, value_fee_data_ifc_amount)
        AU.assert_equals('currency_account_code', currency_account_code_01, value_fee_data_currency_account_code)
        AU.assert_equals('floor_value', floor_value_01, value_fee_data_floor_value)
        AU.assert_equals('ceiling_value', ceiling_value_01, value_fee_data_ceiling_value)
        AU.assert_equals('share_rate', share_rate_01, value_fee_data_share_rate)
        AU.assert_equals('share_amount', share_amount_01, value_fee_data_share_amount)
        AU.assert_equals('round_rate', round_rate_01, value_fee_data_round_rate)
        AU.assert_equals('round_amount', round_amount_01, value_fee_data_round_amount)
        AU.assert_equals('currency_fee_code', currency_fee_code_01, value_fee_data_currency_fee_code)
        AU.assert_equals('pay_source', pay_source_01, value_fee_data_pay_source)
        # AU.assert_null('value_typect', value_fee_data_value_typect)
        AU.assert_equals('value_type', value_type_01, value_fee_data_value_type)
        # 'response' - verify key response under 'data' and 'fee_data', item 2
        AU.assert_exists(expected_key['fee_data'], data_actual_02['data']['fee_data'][1])
        # 'response' - get value under 'data' and 'fee_data', item 2
        value_fee_data_ifc_name = data_actual_02['data']['fee_data'][1]['ifc_name']
        value_fee_data_share_fee = data_actual_02['data']['fee_data'][1]['share_fee']
        value_fee_data_ifc_code = data_actual_02['data']['fee_data'][1]['ifc_code']
        value_fee_data_payrate = data_actual_02['data']['fee_data'][1]['payrate']
        value_fee_data_ifc_value = data_actual_02['data']['fee_data'][1]['ifc_value']
        value_fee_data_ifc_amount = data_actual_02['data']['fee_data'][1]['ifc_amount']
        value_fee_data_currency_account_code = data_actual_02['data']['fee_data'][1]['currency_account_code']
        value_fee_data_floor_value = data_actual_02['data']['fee_data'][1]['floor_value']
        value_fee_data_ceiling_value = data_actual_02['data']['fee_data'][1]['ceiling_value']
        value_fee_data_share_rate = data_actual_02['data']['fee_data'][1]['share_rate']
        value_fee_data_share_amount = data_actual_02['data']['fee_data'][1]['share_amount']
        value_fee_data_round_rate = data_actual_02['data']['fee_data'][1]['round_rate']
        value_fee_data_round_amount = data_actual_02['data']['fee_data'][1]['round_amount']
        value_fee_data_currency_fee_code = data_actual_02['data']['fee_data'][1]['currency_fee_code']
        value_fee_data_pay_source = data_actual_02['data']['fee_data'][1]['pay_source']
        # value_fee_data_value_typect = data_actual_02['data']['fee_data'][1]['value_typect']
        value_fee_data_value_type = data_actual_02['data']['fee_data'][1]['value_type']
        # 'response' - verify value under 'data' and 'fee_data', item 2
        AU.assert_equals('ifc_name', ifc_name_02, value_fee_data_ifc_name)
        AU.assert_equals('share_fee', share_fee_02, value_fee_data_share_fee)
        AU.assert_equals('ifc_code', ifc_code_02, value_fee_data_ifc_code)
        AU.assert_equals('payrate', payrate_02, value_fee_data_payrate)
        AU.assert_equals('ifc_value', ifc_value_02, value_fee_data_ifc_value)
        AU.assert_equals('ifc_amount', ifc_amount_02, value_fee_data_ifc_amount)
        AU.assert_equals('currency_account_code', currency_account_code_02, value_fee_data_currency_account_code)
        AU.assert_equals('floor_value', floor_value_02, value_fee_data_floor_value)
        AU.assert_equals('ceiling_value', ceiling_value_02, value_fee_data_ceiling_value)
        AU.assert_equals('share_rate', share_rate_02, value_fee_data_share_rate)
        AU.assert_equals('share_amount', share_amount_02, value_fee_data_share_amount)
        AU.assert_equals('round_rate', round_rate_02, value_fee_data_round_rate)
        AU.assert_equals('round_amount', round_amount_02, value_fee_data_round_amount)
        AU.assert_equals('currency_fee_code', currency_fee_code_02, value_fee_data_currency_fee_code)
        AU.assert_equals('pay_source', pay_source_02, value_fee_data_pay_source)
        # AU.assert_null('value_typect', value_fee_data_value_typect)
        AU.assert_equals('value_type', value_type_02, value_fee_data_value_type)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_02, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 3, len(data_actual_posting))
        # 'postings' - verify key response, item 1
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array, item 1
        value_TransactionNumber = data_actual_posting[0]['TransactionNumber']
        value_TransTableName = data_actual_posting[0]['TransTableName']
        value_TransId = data_actual_posting[0]['TransId']
        value_SysAccountName = data_actual_posting[0]['SysAccountName']
        value_GLAccount = data_actual_posting[0]['GLAccount']
        value_DorC = data_actual_posting[0]['DorC']
        value_TransactionStatus = data_actual_posting[0]['TransactionStatus']
        value_Amount = data_actual_posting[0]['Amount']
        value_BranchCode = data_actual_posting[0]['BranchCode']
        value_CurrencyCode = data_actual_posting[0]['CurrencyCode']
        value_ValueDate = data_actual_posting[0]['ValueDate']
        value_Posted = data_actual_posting[0]['Posted']
        value_AccountingGroup = data_actual_posting[0]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[0]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[0]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[0]['BaseCurrencyAmount']
        value_Id = data_actual_posting[0]['Id']
        # 'postings' - verify value under array, item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', Decimal(str(amount_deposit)) - (Decimal(str(ifc_amount_01)) + Decimal(str(ifc_amount_02))), Decimal(str(value_Amount)), value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 2
        AU.assert_exists(expected_key['postings'], data_actual_posting[1])
        # 'postings' - get value under array, item 2
        value_TransactionNumber = data_actual_posting[1]['TransactionNumber']
        value_TransTableName = data_actual_posting[1]['TransTableName']
        value_TransId = data_actual_posting[1]['TransId']
        value_SysAccountName = data_actual_posting[1]['SysAccountName']
        value_GLAccount = data_actual_posting[1]['GLAccount']
        value_DorC = data_actual_posting[1]['DorC']
        value_TransactionStatus = data_actual_posting[1]['TransactionStatus']
        value_Amount = data_actual_posting[1]['Amount']
        value_BranchCode = data_actual_posting[1]['BranchCode']
        value_CurrencyCode = data_actual_posting[1]['CurrencyCode']
        value_ValueDate = data_actual_posting[1]['ValueDate']
        value_Posted = data_actual_posting[1]['Posted']
        value_AccountingGroup = data_actual_posting[1]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[1]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[1]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[1]['BaseCurrencyAmount']
        value_Id = data_actual_posting[1]['Id']
        # 'postings' - verify value under array, item 2
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_01, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_01, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 3
        AU.assert_exists(expected_key['postings'], data_actual_posting[2])
        # 'postings' - get value under array, item 3
        value_TransactionNumber = data_actual_posting[2]['TransactionNumber']
        value_TransTableName = data_actual_posting[2]['TransTableName']
        value_TransId = data_actual_posting[2]['TransId']
        value_SysAccountName = data_actual_posting[2]['SysAccountName']
        value_GLAccount = data_actual_posting[2]['GLAccount']
        value_DorC = data_actual_posting[2]['DorC']
        value_TransactionStatus = data_actual_posting[2]['TransactionStatus']
        value_Amount = data_actual_posting[2]['Amount']
        value_BranchCode = data_actual_posting[2]['BranchCode']
        value_CurrencyCode = data_actual_posting[2]['CurrencyCode']
        value_ValueDate = data_actual_posting[2]['ValueDate']
        value_Posted = data_actual_posting[2]['Posted']
        value_AccountingGroup = data_actual_posting[2]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[2]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[2]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[2]['BaseCurrencyAmount']
        value_Id = data_actual_posting[2]['Id']
        # 'postings' - verify value under array, item 3
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_02, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_02, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)

    def test_04_sp_dpt_mdp_005_success_fixed_deposit_account_status_new_normal_multiple_deposit_no(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='FD06PIMMK'
        catalog_name='Fixed deposit 6 months (Principal plus interest rollover) in MMK'
        deposit_type='Fixed Deposit'
        deposit_sub_type='T3'
        deposit_purpose='S'
        rollover='A'
        auto_transfer_option='N'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type,
            deposit_purpose=deposit_purpose,
            rollover=rollover,
            auto_transfer_option=auto_transfer_option
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='T',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_apr['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs_01 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_01 = RU.get_p2_content_response_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_01)
        # 'response' - get value level 1
        value_status = data_actual_01['status']
        value_error_message = data_actual_01['error_message']
        value_error_code = data_actual_01['error_code']
        value_data = data_actual_01['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mdp'], data_actual_01['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_mdp_depositor_description'], data_actual_01['data']['depositor_description'])
        # 'response' - get value in 'data'
        value_data_account_number = data_actual_01['data']['account_number']
        value_data_amount_deposit = data_actual_01['data']['amount_deposit']
        value_data_debit_accounting = data_actual_01['data']['debit_accounting']
        value_data_accounting_currency = data_actual_01['data']['accounting_currency']
        value_data_cross_rate = data_actual_01['data']['cross_rate']
        value_data_acounting_amount = data_actual_01['data']['acounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual_01['data']['exchange_rate_of_accounting_bcy']
        value_data_accounting_amount_bcy = data_actual_01['data']['accounting_amount_bcy']
        value_data_depositor_name = data_actual_01['data']['depositor_name']
        value_data_depositor_code = data_actual_01['data']['depositor_code']
        value_data_depositor_address = data_actual_01['data']['depositor_address']
        value_data_values_date = data_actual_01['data']['values_date']
        value_data_deposit_currency = data_actual_01['data']['deposit_currency']
        value_data_exchange_rate_debit_account_bcy = data_actual_01['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual_01['data']['amount_debit_account_bcy']
        value_data_prepaid_interest = data_actual_01['data']['prepaid_interest']
        value_data_accounting_currency1 = data_actual_01['data']['accounting_currency1']
        value_data_fee_data = data_actual_01['data']['fee_data']
        value_data_total_fee = data_actual_01['data']['total_fee']
        value_data_branch_name = data_actual_01['data']['branch_name']
        value_data_transaction_code = data_actual_01['data']['transaction_code']
        value_data_transaction_number = data_actual_01['data']['transaction_number']
        value_data_transaction_type = data_actual_01['data']['transaction_type']
        value_data_sub_code = data_actual_01['data']['sub_code']
        value_data_transaction_date = data_actual_01['data']['transaction_date']
        value_data_service_sys_date = data_actual_01['data']['service_sys_date']
        value_data_reference_id = data_actual_01['data']['reference_id']
        value_data_ref_id = data_actual_01['data']['ref_id']
        value_data_reference_code = data_actual_01['data']['reference_code']
        value_data_business_code = data_actual_01['data']['business_code']
        value_data_value_date = data_actual_01['data']['value_date']
        value_data_current_user_code = data_actual_01['data']['current_user_code']
        value_data_current_branch_code = data_actual_01['data']['current_branch_code']
        value_data_current_username = data_actual_01['data']['current_username']
        value_data_current_loginname = data_actual_01['data']['current_loginname']
        value_data_user_approve = data_actual_01['data']['user_approve']
        value_data_status = data_actual_01['data']['status']
        value_data_is_reverse = data_actual_01['data']['is_reverse']
        value_data_amount1 = data_actual_01['data']['amount1']
        value_data_description = data_actual_01['data']['description']
        value_data_token = data_actual_01['data']['token']
        value_data_is_transaction_reverse = data_actual_01['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual_01['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
        AU.assert_equals('debit_accounting', debit_accounting_valid, value_data_debit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('acounting_amount', 0.0, value_data_acounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1.0, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('accounting_amount_bcy', 0.0, value_data_accounting_amount_bcy)
        AU.assert_equals('depositor_name', account_name_individual, value_data_depositor_name)
        AU.assert_equals('depositor_code', customer_code_individual, value_data_depositor_code)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('deposit_currency', deposit_currency, value_data_deposit_currency)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('prepaid_interest', 0.0, value_data_prepaid_interest)
        AU.assert_equals('accounting_currency1', accounting_currency1, value_data_accounting_currency1)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_fee', 0.0, value_data_total_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('transaction_code', 'DPT_MDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_empty('reference_code', value_data_reference_code)
        AU.assert_empty('business_code', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_empty('user_approve', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_false('is_reverse', value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1112: Miscellaneous deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_false('is_transaction_reverse', value_data_is_transaction_reverse)
        AU.assert_false('is_transaction_compensated', value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 1, len(data_actual_posting))
        # 'postings' - verify key response, item 1
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array, item 1
        value_TransactionNumber = data_actual_posting[0]['TransactionNumber']
        value_TransTableName = data_actual_posting[0]['TransTableName']
        value_TransId = data_actual_posting[0]['TransId']
        value_SysAccountName = data_actual_posting[0]['SysAccountName']
        value_GLAccount = data_actual_posting[0]['GLAccount']
        value_DorC = data_actual_posting[0]['DorC']
        value_TransactionStatus = data_actual_posting[0]['TransactionStatus']
        value_Amount = data_actual_posting[0]['Amount']
        value_BranchCode = data_actual_posting[0]['BranchCode']
        value_CurrencyCode = data_actual_posting[0]['CurrencyCode']
        value_ValueDate = data_actual_posting[0]['ValueDate']
        value_Posted = data_actual_posting[0]['Posted']
        value_AccountingGroup = data_actual_posting[0]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[0]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[0]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[0]['BaseCurrencyAmount']
        value_Id = data_actual_posting[0]['Id']
        # 'postings' - verify value under array, item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', amount_deposit, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # STEP 04: miscellaneous deposit to deposit status 'Normal'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs_02 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_02 = RU.get_p2_content_response_by_step_code(rs_02, step_code)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_02)
        # 'response' - get value level 1
        value_status = data_actual_02['status']
        value_error_message = data_actual_02['error_message']
        value_error_code = data_actual_02['error_code']
        value_data = data_actual_02['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'InvalidStatus', value_error_code)
        AU.assert_equals('error_message', 'Invalid account status [Normal]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_04_sp_dpt_mdp_006_success_fixed_deposit_account_status_new_normal_multiple_deposit_no_add_fee(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='FD06PIMMK'
        catalog_name='Fixed deposit 6 months (Principal plus interest rollover) in MMK'
        deposit_type='Fixed Deposit'
        deposit_sub_type='T3'
        deposit_purpose='S'
        rollover='A'
        auto_transfer_option='N'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type,
            deposit_purpose=deposit_purpose,
            rollover=rollover,
            auto_transfer_option=auto_transfer_option
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='T',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_apr['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 03: miscellaneous deposit to deposit status 'New'
        total_fee=3200.0
        share_fee_01=0.0
        ifc_name_01='Withdrawal (MMK) For Different Region  (By Cash)'
        value_type_01='P'
        ifc_code_01=302
        payrate_01=100
        ifc_value_01=0.025
        ifc_amount_01=200.0
        currency_account_code_01=deposit_currency
        floor_value_01=200.0
        ceiling_value_01=0.0
        share_rate_01=0.0
        share_amount_01=0.0
        round_rate_01=0.0
        round_amount_01=0.0
        currency_fee_code_01=deposit_currency
        pay_source_01='CSH'
        share_fee_02=0.0
        ifc_name_02='Account To Account Transfer (MMK) For Same Region'
        value_type_02='F'
        ifc_code_02=309
        payrate_02=100
        ifc_value_02=3000.0
        ifc_amount_02=3000.0
        currency_account_code_02=deposit_currency
        floor_value_02=0.0
        ceiling_value_02=0.0
        share_rate_02=0.0
        share_amount_02=0.0
        round_rate_02=0.0
        round_amount_02=0.0
        currency_fee_code_02=deposit_currency
        pay_source_02='CSH'
        gl_account_ifcc_01='003303030100010101'
        gl_account_ifcc_02='003303030100010101'
        fee_data = [
            {
                "share_fee": share_fee_01,
                "ifc_name": ifc_name_01,
                "value_type": value_type_01,
                "ifc_code": ifc_code_01,
                "payrate": payrate_01,
                "ifc_value": ifc_value_01,
                "ifc_amount": ifc_amount_01,
                "currency_account_code": currency_account_code_01,
                "floor_value": floor_value_01,
                "ceiling_value": ceiling_value_01,
                "share_rate": share_rate_01,
                "share_amount": share_amount_01,
                "round_rate": round_rate_01,
                "round_amount": round_amount_01,
                "currency_fee_code": currency_fee_code_01,
                "pay_source": pay_source_01
            },
            {
                "share_fee": share_fee_02,
                "ifc_name": ifc_name_02,
                "value_type": value_type_02,
                "ifc_code": ifc_code_02,
                "payrate": payrate_02,
                "ifc_value": ifc_value_02,
                "ifc_amount": ifc_amount_02,
                "currency_account_code": currency_account_code_02,
                "floor_value": floor_value_02,
                "ceiling_value": ceiling_value_02,
                "share_rate": share_rate_02,
                "share_amount": share_amount_02,
                "round_rate": round_rate_02,
                "round_amount": round_amount_02,
                "currency_fee_code": currency_fee_code_02,
                "pay_source": pay_source_02
            }
        ]
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1,
            fee_data=fee_data
        )
        rs_01 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_01 = RU.get_p2_content_response_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_01)
        # 'response' - get value level 1
        value_status = data_actual_01['status']
        value_error_message = data_actual_01['error_message']
        value_error_code = data_actual_01['error_code']
        value_data = data_actual_01['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mdp'], data_actual_01['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_mdp_depositor_description'], data_actual_01['data']['depositor_description'])
        # 'response' - get value in 'data'
        value_data_account_number = data_actual_01['data']['account_number']
        value_data_amount_deposit = data_actual_01['data']['amount_deposit']
        value_data_debit_accounting = data_actual_01['data']['debit_accounting']
        value_data_accounting_currency = data_actual_01['data']['accounting_currency']
        value_data_cross_rate = data_actual_01['data']['cross_rate']
        value_data_acounting_amount = data_actual_01['data']['acounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual_01['data']['exchange_rate_of_accounting_bcy']
        value_data_accounting_amount_bcy = data_actual_01['data']['accounting_amount_bcy']
        value_data_depositor_name = data_actual_01['data']['depositor_name']
        value_data_depositor_code = data_actual_01['data']['depositor_code']
        value_data_depositor_address = data_actual_01['data']['depositor_address']
        value_data_values_date = data_actual_01['data']['values_date']
        value_data_deposit_currency = data_actual_01['data']['deposit_currency']
        value_data_exchange_rate_debit_account_bcy = data_actual_01['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual_01['data']['amount_debit_account_bcy']
        value_data_prepaid_interest = data_actual_01['data']['prepaid_interest']
        value_data_accounting_currency1 = data_actual_01['data']['accounting_currency1']
        value_data_fee_data = data_actual_01['data']['fee_data']
        value_data_total_fee = data_actual_01['data']['total_fee']
        value_data_branch_name = data_actual_01['data']['branch_name']
        value_data_transaction_code = data_actual_01['data']['transaction_code']
        value_data_transaction_number = data_actual_01['data']['transaction_number']
        value_data_transaction_type = data_actual_01['data']['transaction_type']
        value_data_sub_code = data_actual_01['data']['sub_code']
        value_data_transaction_date = data_actual_01['data']['transaction_date']
        value_data_service_sys_date = data_actual_01['data']['service_sys_date']
        value_data_reference_id = data_actual_01['data']['reference_id']
        value_data_ref_id = data_actual_01['data']['ref_id']
        value_data_reference_code = data_actual_01['data']['reference_code']
        value_data_business_code = data_actual_01['data']['business_code']
        value_data_value_date = data_actual_01['data']['value_date']
        value_data_current_user_code = data_actual_01['data']['current_user_code']
        value_data_current_branch_code = data_actual_01['data']['current_branch_code']
        value_data_current_username = data_actual_01['data']['current_username']
        value_data_current_loginname = data_actual_01['data']['current_loginname']
        value_data_user_approve = data_actual_01['data']['user_approve']
        value_data_status = data_actual_01['data']['status']
        value_data_is_reverse = data_actual_01['data']['is_reverse']
        value_data_amount1 = data_actual_01['data']['amount1']
        value_data_description = data_actual_01['data']['description']
        value_data_token = data_actual_01['data']['token']
        value_data_is_transaction_reverse = data_actual_01['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual_01['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
        AU.assert_equals('debit_accounting', debit_accounting_valid, value_data_debit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('acounting_amount', 0.0, value_data_acounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1.0, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('accounting_amount_bcy', 0.0, value_data_accounting_amount_bcy)
        AU.assert_equals('depositor_name', account_name_individual, value_data_depositor_name)
        AU.assert_equals('depositor_code', customer_code_individual, value_data_depositor_code)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('deposit_currency', deposit_currency, value_data_deposit_currency)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('prepaid_interest', 0.0, value_data_prepaid_interest)
        AU.assert_equals('accounting_currency1', accounting_currency1, value_data_accounting_currency1)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_fee', total_fee, value_data_total_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('transaction_code', 'DPT_MDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_empty('reference_code', value_data_reference_code)
        AU.assert_empty('business_code', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_empty('user_approve', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_false('is_reverse', value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1112: Miscellaneous deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_false('is_transaction_reverse', value_data_is_transaction_reverse)
        AU.assert_false('is_transaction_compensated', value_data_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'fee_data', item 1
        AU.assert_exists(expected_key['fee_data'], data_actual_01['data']['fee_data'][0])
        # 'response' - get value under 'data' and 'fee_data', item 1
        value_fee_data_ifc_name = data_actual_01['data']['fee_data'][0]['ifc_name']
        value_fee_data_share_fee = data_actual_01['data']['fee_data'][0]['share_fee']
        value_fee_data_ifc_code = data_actual_01['data']['fee_data'][0]['ifc_code']
        value_fee_data_payrate = data_actual_01['data']['fee_data'][0]['payrate']
        value_fee_data_ifc_value = data_actual_01['data']['fee_data'][0]['ifc_value']
        value_fee_data_ifc_amount = data_actual_01['data']['fee_data'][0]['ifc_amount']
        value_fee_data_currency_account_code = data_actual_01['data']['fee_data'][0]['currency_account_code']
        value_fee_data_floor_value = data_actual_01['data']['fee_data'][0]['floor_value']
        value_fee_data_ceiling_value = data_actual_01['data']['fee_data'][0]['ceiling_value']
        value_fee_data_share_rate = data_actual_01['data']['fee_data'][0]['share_rate']
        value_fee_data_share_amount = data_actual_01['data']['fee_data'][0]['share_amount']
        value_fee_data_round_rate = data_actual_01['data']['fee_data'][0]['round_rate']
        value_fee_data_round_amount = data_actual_01['data']['fee_data'][0]['round_amount']
        value_fee_data_currency_fee_code = data_actual_01['data']['fee_data'][0]['currency_fee_code']
        value_fee_data_pay_source = data_actual_01['data']['fee_data'][0]['pay_source']
        # value_fee_data_value_typect = data_actual_01['data']['fee_data'][0]['value_typect']
        value_fee_data_value_type = data_actual_01['data']['fee_data'][0]['value_type']
        # 'response' - verify value under 'data' and 'fee_data', item 1
        AU.assert_equals('ifc_name', ifc_name_01, value_fee_data_ifc_name)
        AU.assert_equals('share_fee', share_fee_01, value_fee_data_share_fee)
        AU.assert_equals('ifc_code', ifc_code_01, value_fee_data_ifc_code)
        AU.assert_equals('payrate', payrate_01, value_fee_data_payrate)
        AU.assert_equals('ifc_value', ifc_value_01, value_fee_data_ifc_value)
        AU.assert_equals('ifc_amount', ifc_amount_01, value_fee_data_ifc_amount)
        AU.assert_equals('currency_account_code', currency_account_code_01, value_fee_data_currency_account_code)
        AU.assert_equals('floor_value', floor_value_01, value_fee_data_floor_value)
        AU.assert_equals('ceiling_value', ceiling_value_01, value_fee_data_ceiling_value)
        AU.assert_equals('share_rate', share_rate_01, value_fee_data_share_rate)
        AU.assert_equals('share_amount', share_amount_01, value_fee_data_share_amount)
        AU.assert_equals('round_rate', round_rate_01, value_fee_data_round_rate)
        AU.assert_equals('round_amount', round_amount_01, value_fee_data_round_amount)
        AU.assert_equals('currency_fee_code', currency_fee_code_01, value_fee_data_currency_fee_code)
        AU.assert_equals('pay_source', pay_source_01, value_fee_data_pay_source)
        # AU.assert_null('value_typect', value_fee_data_value_typect)
        AU.assert_equals('value_type', value_type_01, value_fee_data_value_type)
        # 'response' - verify key response under 'data' and 'fee_data', item 2
        AU.assert_exists(expected_key['fee_data'], data_actual_01['data']['fee_data'][1])
        # 'response' - get value under 'data' and 'fee_data', item 2
        value_fee_data_ifc_name = data_actual_01['data']['fee_data'][1]['ifc_name']
        value_fee_data_share_fee = data_actual_01['data']['fee_data'][1]['share_fee']
        value_fee_data_ifc_code = data_actual_01['data']['fee_data'][1]['ifc_code']
        value_fee_data_payrate = data_actual_01['data']['fee_data'][1]['payrate']
        value_fee_data_ifc_value = data_actual_01['data']['fee_data'][1]['ifc_value']
        value_fee_data_ifc_amount = data_actual_01['data']['fee_data'][1]['ifc_amount']
        value_fee_data_currency_account_code = data_actual_01['data']['fee_data'][1]['currency_account_code']
        value_fee_data_floor_value = data_actual_01['data']['fee_data'][1]['floor_value']
        value_fee_data_ceiling_value = data_actual_01['data']['fee_data'][1]['ceiling_value']
        value_fee_data_share_rate = data_actual_01['data']['fee_data'][1]['share_rate']
        value_fee_data_share_amount = data_actual_01['data']['fee_data'][1]['share_amount']
        value_fee_data_round_rate = data_actual_01['data']['fee_data'][1]['round_rate']
        value_fee_data_round_amount = data_actual_01['data']['fee_data'][1]['round_amount']
        value_fee_data_currency_fee_code = data_actual_01['data']['fee_data'][1]['currency_fee_code']
        value_fee_data_pay_source = data_actual_01['data']['fee_data'][1]['pay_source']
        # value_fee_data_value_typect = data_actual_01['data']['fee_data'][1]['value_typect']
        value_fee_data_value_type = data_actual_01['data']['fee_data'][1]['value_type']
        # 'response' - verify value under 'data' and 'fee_data', item 2
        AU.assert_equals('ifc_name', ifc_name_02, value_fee_data_ifc_name)
        AU.assert_equals('share_fee', share_fee_02, value_fee_data_share_fee)
        AU.assert_equals('ifc_code', ifc_code_02, value_fee_data_ifc_code)
        AU.assert_equals('payrate', payrate_02, value_fee_data_payrate)
        AU.assert_equals('ifc_value', ifc_value_02, value_fee_data_ifc_value)
        AU.assert_equals('ifc_amount', ifc_amount_02, value_fee_data_ifc_amount)
        AU.assert_equals('currency_account_code', currency_account_code_02, value_fee_data_currency_account_code)
        AU.assert_equals('floor_value', floor_value_02, value_fee_data_floor_value)
        AU.assert_equals('ceiling_value', ceiling_value_02, value_fee_data_ceiling_value)
        AU.assert_equals('share_rate', share_rate_02, value_fee_data_share_rate)
        AU.assert_equals('share_amount', share_amount_02, value_fee_data_share_amount)
        AU.assert_equals('round_rate', round_rate_02, value_fee_data_round_rate)
        AU.assert_equals('round_amount', round_amount_02, value_fee_data_round_amount)
        AU.assert_equals('currency_fee_code', currency_fee_code_02, value_fee_data_currency_fee_code)
        AU.assert_equals('pay_source', pay_source_02, value_fee_data_pay_source)
        # AU.assert_null('value_typect', value_fee_data_value_typect)
        AU.assert_equals('value_type', value_type_02, value_fee_data_value_type)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_01, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 3, len(data_actual_posting))
        # 'postings' - verify key response, item 1
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array, item 1
        value_TransactionNumber = data_actual_posting[0]['TransactionNumber']
        value_TransTableName = data_actual_posting[0]['TransTableName']
        value_TransId = data_actual_posting[0]['TransId']
        value_SysAccountName = data_actual_posting[0]['SysAccountName']
        value_GLAccount = data_actual_posting[0]['GLAccount']
        value_DorC = data_actual_posting[0]['DorC']
        value_TransactionStatus = data_actual_posting[0]['TransactionStatus']
        value_Amount = data_actual_posting[0]['Amount']
        value_BranchCode = data_actual_posting[0]['BranchCode']
        value_CurrencyCode = data_actual_posting[0]['CurrencyCode']
        value_ValueDate = data_actual_posting[0]['ValueDate']
        value_Posted = data_actual_posting[0]['Posted']
        value_AccountingGroup = data_actual_posting[0]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[0]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[0]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[0]['BaseCurrencyAmount']
        value_Id = data_actual_posting[0]['Id']
        # 'postings' - verify value under array, item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', Decimal(str(amount_deposit)) - (Decimal(str(ifc_amount_01)) + Decimal(str(ifc_amount_02))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 2
        AU.assert_exists(expected_key['postings'], data_actual_posting[1])
        # 'postings' - get value under array, item 2
        value_TransactionNumber = data_actual_posting[1]['TransactionNumber']
        value_TransTableName = data_actual_posting[1]['TransTableName']
        value_TransId = data_actual_posting[1]['TransId']
        value_SysAccountName = data_actual_posting[1]['SysAccountName']
        value_GLAccount = data_actual_posting[1]['GLAccount']
        value_DorC = data_actual_posting[1]['DorC']
        value_TransactionStatus = data_actual_posting[1]['TransactionStatus']
        value_Amount = data_actual_posting[1]['Amount']
        value_BranchCode = data_actual_posting[1]['BranchCode']
        value_CurrencyCode = data_actual_posting[1]['CurrencyCode']
        value_ValueDate = data_actual_posting[1]['ValueDate']
        value_Posted = data_actual_posting[1]['Posted']
        value_AccountingGroup = data_actual_posting[1]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[1]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[1]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[1]['BaseCurrencyAmount']
        value_Id = data_actual_posting[1]['Id']
        # 'postings' - verify value under array, item 2
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_01, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_01, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 3
        AU.assert_exists(expected_key['postings'], data_actual_posting[2])
        # 'postings' - get value under array, item 3
        value_TransactionNumber = data_actual_posting[2]['TransactionNumber']
        value_TransTableName = data_actual_posting[2]['TransTableName']
        value_TransId = data_actual_posting[2]['TransId']
        value_SysAccountName = data_actual_posting[2]['SysAccountName']
        value_GLAccount = data_actual_posting[2]['GLAccount']
        value_DorC = data_actual_posting[2]['DorC']
        value_TransactionStatus = data_actual_posting[2]['TransactionStatus']
        value_Amount = data_actual_posting[2]['Amount']
        value_BranchCode = data_actual_posting[2]['BranchCode']
        value_CurrencyCode = data_actual_posting[2]['CurrencyCode']
        value_ValueDate = data_actual_posting[2]['ValueDate']
        value_Posted = data_actual_posting[2]['Posted']
        value_AccountingGroup = data_actual_posting[2]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[2]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[2]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[2]['BaseCurrencyAmount']
        value_Id = data_actual_posting[2]['Id']
        # 'postings' - verify value under array, item 3
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_02, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_02, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # STEP 04: miscellaneous deposit to deposit status 'Normal'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1,
            fee_data=fee_data
        )
        rs_02 = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_02 = RU.get_p2_content_response_by_step_code(rs_02, step_code)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_02)
        # 'response' - get value level 1
        value_status = data_actual_02['status']
        value_error_message = data_actual_02['error_message']
        value_error_code = data_actual_02['error_code']
        value_data = data_actual_02['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'InvalidStatus', value_error_code)
        AU.assert_equals('error_message', 'Invalid account status [Normal]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_04_sp_dpt_mdp_007_error_current_account_status_dormant(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open deposit account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_apr['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_01 = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_actual_01['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_actual_01['data']['account_number'])
        # STEP 01-04: change status from 'Normal' to 'Dormant'
        fields_data_cas = sp_payload.DPT_CAS(
            account_number=account_number_approved,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CAS(fields_data_cas)
        step_code = 'DPT_CAS'
        # 'response' - get data actual
        data_dpt_cas = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cas, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cas['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cas['data']['account_number'])
        # STEP 02-01: miscellaneous deposit to deposit status 'Dormant'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_02 = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_02)
        # 'response' - get value level 1
        value_status = data_actual_02['status']
        value_error_message = data_actual_02['error_message']
        value_error_code = data_actual_02['error_code']
        value_data = data_actual_02['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'DormantNotAllowedCredit', value_error_code)
        AU.assert_equals('error_message', 'Not Allowed to do Credit Posting because this Account is Dormant', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_04_sp_dpt_mdp_008_error_saving_account_status_dormant(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: open deposit account
        catalog_code='BSMMK0000'
        catalog_name='Bonus savings account  in MMK'
        deposit_type='Savings'
        deposit_sub_type='S2'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='S',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_01 = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_actual_01['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_actual_01['data']['account_number'])
        # STEP 01-04: change status from 'Normal' to 'Dormant'
        fields_data_cas = sp_payload.DPT_CAS(
            account_number=account_number_approved,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CAS(fields_data_cas)
        step_code = 'DPT_CAS'
        # 'response' - get data actual
        data_dpt_cas = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cas, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cas['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cas['data']['account_number'])
        # STEP 02-01: miscellaneous deposit to deposit status 'Dormant'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_02 = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_02)
        # 'response' - get value level 1
        value_status = data_actual_02['status']
        value_error_message = data_actual_02['error_message']
        value_error_code = data_actual_02['error_code']
        value_data = data_actual_02['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'DormantNotAllowedCredit', value_error_code)
        AU.assert_equals('error_message', 'Not Allowed to do Credit Posting because this Account is Dormant', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_04_sp_dpt_mdp_009_error_saving_account_cash_call(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: open deposit account
        catalog_code='SCMMK0000'
        catalog_name='SHWE cash call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S6'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='S',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 02: miscellaneous deposit to deposit status 'New'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_02 = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_02)
        # 'response' - get value level 1
        value_status = data_actual_02['status']
        value_error_message = data_actual_02['error_message']
        value_error_code = data_actual_02['error_code']
        value_data = data_actual_02['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'Deposit.NotAllowedCredit', value_error_code)
        AU.assert_equals('error_message', f'Not Allowed to do Credit Posting because this is [CSH] Credit Only Account [{account_number_approved}]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_04_sp_dpt_mdp_010_error_prepaid_fixed_deposit_account(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: open deposit account
        catalog_code='PR120MMK0'
        catalog_name='SHWE prepaid fixed deposit account by cash in MMK'
        deposit_type='Fixed Deposit'
        deposit_sub_type='T6'
        deposit_purpose='S'
        auto_transfer_option='A'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type,
            deposit_purpose=deposit_purpose,
            auto_transfer_option=auto_transfer_option,
            to_account_number=to_account_number_saving_single_valid
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='T',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 02: miscellaneous deposit
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual_02 = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual_02, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_02)
        # 'response' - get value level 1
        value_status = data_actual_02['status']
        value_error_message = data_actual_02['error_message']
        value_error_code = data_actual_02['error_code']
        value_data = data_actual_02['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'Deposit.NotAllowedCredit', value_error_code)
        AU.assert_equals('error_message', f'Not Allowed to do Credit Posting because this is [CSH] Credit Only Account [{account_number_approved}]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_04_sp_dpt_mdp_011_error_account_status_closed(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_closed,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # 'response' - get value level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'InvalidDepositStatus', value_error_code)
        AU.assert_equals('error_message', 'Invalid deposit status [Closed]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_04_sp_dpt_mdp_012_error_account_status_block(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_block,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # 'response' - get value level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'InvalidDepositStatus', value_error_code)
        AU.assert_equals('error_message', 'Invalid deposit status [Block]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_04_sp_dpt_mdp_013_error_account_status_pending(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_pending,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # 'response' - get value level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'InvalidDepositStatus', value_error_code)
        AU.assert_equals('error_message', 'Invalid deposit status [Pending to approve]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_04_sp_dpt_mdp_014_error_account_number_is_empty(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MDP(
            account_number='',
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # 'response' - get value level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'FieldRequireValidator', value_error_code)
        AU.assert_equals('error_message', 'Account Number is required', value_error_message)
        AU.assert_null('data', value_data)

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_04_sp_dpt_mdp_015_error_account_number_is_null(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MDP(
            account_number=None,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [account_number] violates IS_NULL rule.;', rs['description'])

    def test_04_sp_dpt_mdp_016_error_account_number_not_exist(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MDP(
            account_number='111111111111',
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # 'response' - get value level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', '', value_error_code)
        AU.assert_equals('error_message', 'Account deposit [111111111111] does not exist', value_error_message)
        AU.assert_null('data', value_data)

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_04_sp_dpt_mdp_017_error_amount_deposit_is_minus(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MDP(
            account_number=to_account_number_saving_single_valid,
            amount_deposit=-10000.45,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [amount_deposit] violates Minimum rule: Minimum value is 0.01;', rs['description'])

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_04_sp_dpt_mdp_018_error_amount_deposit_is_empty(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MDP(
            account_number=to_account_number_saving_single_valid,
            amount_deposit='',
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', "Input is invalid.Validate field [amount_deposit]: value=[], datatype=[Number] with exception: [The input string '' was not in a correct format.].;", rs['description'])

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_04_sp_dpt_mdp_019_error_amount_deposit_is_zero(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MDP(
            account_number=to_account_number_saving_single_valid,
            amount_deposit=0.0,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [amount_deposit] violates Minimum rule: Minimum value is 0.01;', rs['description'])

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_04_sp_dpt_mdp_020_error_amount_deposit_is_null(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MDP(
            account_number=to_account_number_saving_single_valid,
            amount_deposit=None,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [amount_deposit] violates IS_NULL rule.;', rs['description'])

    def test_04_sp_dpt_mdp_021_error_amount_deposit_smaller_initial_deposit_amount(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: open deposit account 'Current'
        catalog_code='CAMMK0000' # Initial deposit amount = 1,000.00
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=999.99,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # 'response' - get value level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'Err0000004', value_error_code)
        AU.assert_equals('error_message', 'Invalid initial deposit amount', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)
        # STEP 02-01: open deposit account 'Savings'
        catalog_code='BSMMK0000' # Initial deposit amount = 100,000.00
        catalog_name='Bonus savings account  in MMK'
        deposit_type='Savings'
        deposit_sub_type='S2'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        # STEP 02-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='S',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 02-03: miscellaneous deposit to deposit status 'New'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=99999.99,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # 'response' - get value level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'Err0000004', value_error_code)
        AU.assert_equals('error_message', 'Invalid initial deposit amount', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)
        # STEP 03-01: open deposit account 'Fixed Deposit'
        catalog_code='FD06PIMMK' # Initial deposit amount = 50,000.00
        catalog_name='Fixed deposit 6 months (Principal plus interest rollover) in MMK'
        deposit_type='Fixed Deposit'
        deposit_sub_type='T3'
        deposit_purpose='S'
        rollover='A'
        auto_transfer_option='N'
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type,
            deposit_purpose=deposit_purpose,
            rollover=rollover,
            auto_transfer_option=auto_transfer_option
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        # STEP 03-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='T',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        # 'response' - get data actual
        data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_apr['status'])
        # get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number_approved = data_dpt_apr['data']['account_number']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, account_number_approved)
        # STEP 03-03: miscellaneous deposit to deposit status 'New'
        fields_data = sp_payload.DPT_MDP(
            account_number=account_number_approved,
            amount_deposit=49999.99,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # 'response' - verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # 'response' - get value level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # 'response' - verify value level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'Err0000004', value_error_code)
        AU.assert_equals('error_message', 'Invalid initial deposit amount', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY
#     def test_04_sp_dpt_mdp_022_error_debit_accounting_is_empty(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MDP(
#             account_number=to_account_number_saving_single_valid,
#             amount_deposit=amount_deposit,
#             debit_accounting='',
#             branch_name=branch_name,
#             accounting_currency=accounting_currency,
#             depositor_name=account_name_individual,
#             depositor_code=customer_code_individual,
#             depositor_address=depositor_address,
#             values_date=values_date,
#             deposit_currency=deposit_currency,
#             accounting_currency1=accounting_currency1
#         )
#         rs = sp_helper.DPT_MDP(fields_data)
#         step_code = 'DPT_MDP'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify key response level 1
#         AU.assert_exists(expected_key['level_01'], data_actual)
#         # 'response' - get value level 1
#         value_status = data_actual['status']
#         value_error_message = data_actual['error_message']
#         value_error_code = data_actual['error_code']
#         value_data = data_actual['data']
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 1, value_status)
#         AU.assert_equals('error_code', 'FieldRequireValidator', value_error_code)
#         AU.assert_equals('error_message', 'Debit Accounting is required', value_error_message)
#         AU.assert_null('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY
#     def test_04_sp_dpt_mdp_023_error_debit_accounting_not_exist(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MDP(
#             account_number=to_account_number_saving_single_valid,
#             amount_deposit=amount_deposit,
#             debit_accounting='111111111111111111',
#             branch_name=branch_name,
#             accounting_currency=accounting_currency,
#             depositor_name=account_name_individual,
#             depositor_code=customer_code_individual,
#             depositor_address=depositor_address,
#             values_date=values_date,
#             deposit_currency=deposit_currency,
#             accounting_currency1=accounting_currency1
#         )
#         rs = sp_helper.DPT_MDP(fields_data)
#         step_code = 'ACT_EXECUTE_POSTING'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify key response level 1
#         AU.assert_exists(expected_key['level_01'], data_actual)
#         # 'response' - get value level 1
#         value_status = data_actual['status']
#         value_error_message = data_actual['error_message']
#         value_error_code = data_actual['error_code']
#         value_data = data_actual['data']
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 1, value_status)
#         AU.assert_equals('error_code', 'AccountNotExist', value_error_code)
#         AU.assert_equals('error_message', 'Account [111111111111111111] has not been existing', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY
#     def test_04_sp_dpt_mdp_024_error_debit_accounting_invalid_posting_side_credit(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MDP(
#             account_number=to_account_number_saving_single_valid,
#             amount_deposit=amount_deposit,
#             debit_accounting=debit_accounting_invalid_posting_side_credit,
#             branch_name=branch_name,
#             accounting_currency=accounting_currency,
#             depositor_name=account_name_individual,
#             depositor_code=customer_code_individual,
#             depositor_address=depositor_address,
#             values_date=values_date,
#             deposit_currency=deposit_currency,
#             accounting_currency1=accounting_currency1
#         )
#         rs = sp_helper.DPT_MDP(fields_data)
#         step_code = 'ACT_EXECUTE_POSTING'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify key response level 1
#         AU.assert_exists(expected_key['level_01'], data_actual)
#         # 'response' - get value level 1
#         value_status = data_actual['status']
#         value_error_message = data_actual['error_message']
#         value_error_code = data_actual['error_code']
#         value_data = data_actual['data']
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 1, value_status)
#         AU.assert_equals('error_code', 'AccountNotAlowDebitBalance', value_error_code)
#         AU.assert_equals('error_message', f'Account [{debit_accounting_invalid_posting_side_credit}] is not allowed posting debit', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY
#     def test_04_sp_dpt_mdp_025_error_debit_accounting_invalid_balance(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MDP(
#             account_number=to_account_number_saving_single_valid,
#             amount_deposit=amount_deposit,
#             debit_accounting=debit_accounting_invalid_balance,
#             branch_name=branch_name,
#             accounting_currency=accounting_currency,
#             depositor_name=account_name_individual,
#             depositor_code=customer_code_individual,
#             depositor_address=depositor_address,
#             values_date=values_date,
#             deposit_currency=deposit_currency,
#             accounting_currency1=accounting_currency1
#         )
#         rs = sp_helper.DPT_MDP(fields_data)
#         step_code = 'ACT_EXECUTE_POSTING'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify key response level 1
#         AU.assert_exists(expected_key['level_01'], data_actual)
#         # 'response' - get value level 1
#         value_status = data_actual['status']
#         value_error_message = data_actual['error_message']
#         value_error_code = data_actual['error_code']
#         value_data = data_actual['data']
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 1, value_status)
#         AU.assert_equals('error_code', 'ACT_NOT_ALLOW_DEBIT_BAL', value_error_code)
#         AU.assert_equals('error_message', f'Account [{debit_accounting_invalid_balance}] is not allowed to be debit balance', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY
#     def test_04_sp_dpt_mdp_026_error_debit_accounting_invalid_level_9(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MDP(
#             account_number=to_account_number_saving_single_valid,
#             amount_deposit=amount_deposit,
#             debit_accounting='1010701000101',
#             branch_name=branch_name,
#             accounting_currency=accounting_currency,
#             depositor_name=account_name_individual,
#             depositor_code=customer_code_individual,
#             depositor_address=depositor_address,
#             values_date=values_date,
#             deposit_currency=deposit_currency,
#             accounting_currency1=accounting_currency1
#         )
#         rs = sp_helper.DPT_MDP(fields_data)
#         step_code = 'ACT_EXECUTE_POSTING'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify key response level 1
#         AU.assert_exists(expected_key['level_01'], data_actual)
#         # 'response' - get value level 1
#         value_status = data_actual['status']
#         value_error_message = data_actual['error_message']
#         value_error_code = data_actual['error_code']
#         value_data = data_actual['data']
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 1, value_status)
#         AU.assert_equals('error_code', 'InvalidCurrency', value_error_code)
#         AU.assert_equals('error_message', 'Invalid currency code [AAA-MMK]', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY
#     def test_04_sp_dpt_mdp_027_error_debit_accounting_invalid_currency(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MDP(
#             account_number=to_account_number_saving_single_valid,
#             amount_deposit=amount_deposit,
#             debit_accounting=debit_accounting_usd,
#             branch_name=branch_name,
#             accounting_currency='USD',
#             depositor_name=account_name_individual,
#             depositor_code=customer_code_individual,
#             depositor_address=depositor_address,
#             values_date=values_date,
#             deposit_currency=deposit_currency,
#             accounting_currency1='USD'
#         )
#         rs = sp_helper.DPT_MDP(fields_data)
#         step_code = 'ACT_EXECUTE_POSTING'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify key response level 1
#         AU.assert_exists(expected_key['level_01'], data_actual)
#         # 'response' - get value level 1
#         value_status = data_actual['status']
#         value_error_message = data_actual['error_message']
#         value_error_code = data_actual['error_code']
#         value_data = data_actual['data']
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 1, value_status)
#         AU.assert_equals('error_code', 'InvalidCurrency', value_error_code)
#         AU.assert_equals('error_message', 'Invalid currency code [USD-MMK]', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY VI LAM LECH MASTER-DATAIL CUA CASH
#     def test_04_sp_dpt_mdp_028_error_debit_accounting_invalid_gl_cash(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MDP(
#             account_number=to_account_number_saving_single_valid,
#             amount_deposit=amount_deposit,
#             debit_accounting='003101030100010101',
#             branch_name=branch_name,
#             accounting_currency=accounting_currency,
#             depositor_name=account_name_individual,
#             depositor_code=customer_code_individual,
#             depositor_address=depositor_address,
#             values_date=values_date,
#             deposit_currency=deposit_currency,
#             accounting_currency1=accounting_currency1
#         )
#         rs = sp_helper.DPT_MDP(fields_data)
#         step_code = 'ACT_EXECUTE_POSTING'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify key response level 1
#         AU.assert_exists(expected_key['level_01'], data_actual)
#         # 'response' - get value level 1
#         value_status = data_actual['status']
#         value_error_message = data_actual['error_message']
#         value_error_code = data_actual['error_code']
#         value_data = data_actual['data']
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 1, value_status)
#         AU.assert_equals('error_code', 'NotAllow', value_error_code)
#         AU.assert_equals('error_message', 'GL [003101030100010101] not allowed [Cash in Hand (MMK)] GL account number(Account group = [Cash])', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)
