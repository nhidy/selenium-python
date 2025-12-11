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
amount_deposit=10000000.45
debit_accounting_valid='003101010333333301'
deposit_currency='MMK'
accounting_currency1='MMK'
gl_account_ifcc='003303030100010101'

# data test valid
credit_accounting_valid='003110080100000001'
accounting_currency='MMK'
branch_name='003 - Bayint Naung Branch'
address='Home, Street, Ward, Township'
values_date=user_service['working_date']
branch_code=user_service['branch_code']
# data test invalid
gl_account_level_07='5010101000101'
gl_account_level_08='501010100010101'
gl_account_posting_side_debit='003110070100000101'
gl_account_usd='003101010666666602'
gl_account_cash='003101030100010101'
gl_account_direct_posting_no='003110060100000001'
gl_account_not_same_branch='001110060100000001'
# # data test trên 104
# account_number_closed='340034919619'
# account_number_block='310033187741'
# account_number_pending='310030475906'
# account_number_new='310030730191'
# account_number_fixed_deposit_normal='430030589898'
# account_number_prepaid_fixed_deposit_normal='460030177172'
# account_number_current_normal='110031370833'
# data test trên 198
account_number_closed='110031400004'
account_number_block='110036552201'
account_number_pending='310036280263'
account_number_new='110033365907'
account_number_fixed_deposit_normal='430030879304'
account_number_prepaid_fixed_deposit_normal='460031072430'
account_number_current_normal='110030077368'

@pytest.fixture(scope='session')
def user():
    req = RU(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_MWR
class Test_SP_DPT_MWR(object):

    def test_06_sp_dpt_mwr_001_success_current_account_status_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_mdp['data']['account_number'])
        # STEP 04: miscellaneous withdrawal
        withdraw_amount=amount_deposit-minimum_deposit_amount
        accounting_amount=withdraw_amount
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mwr'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_mwr_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_interest_earlywdr = data_actual['data']['interest_earlywdr']
        value_data_withdraw_amount = data_actual['data']['withdraw_amount']
        value_data_credit_accounting = data_actual['data']['credit_accounting']
        value_data_accounting_currency = data_actual['data']['accounting_currency']
        value_data_cross_rate = data_actual['data']['cross_rate']
        value_data_accounting_amount = data_actual['data']['accounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual['data']['exchange_rate_of_accounting_bcy']
        value_data_amount_equivalent_in_bcy = data_actual['data']['amount_equivalent_in_bcy']
        value_data_withdrawer_name = data_actual['data']['withdrawer_name']
        value_data_withdrawer_code = data_actual['data']['withdrawer_code']
        value_data_withdrawer_address = data_actual['data']['withdrawer_address']
        value_data_values_date = data_actual['data']['values_date']
        value_data_currency_of_deposit_account = data_actual['data']['currency_of_deposit_account']
        value_data_exchange_rate_debit_account_bcy = data_actual['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual['data']['amount_debit_account_bcy']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_code = data_actual['data']['branch_code']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_accounting = data_actual['data']['total_ifc_fee_accounting']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
        value_data_total_ifc_fee = data_actual['data']['total_ifc_fee']
        value_data_passbook_number = data_actual['data']['passbook_number']
        # value_data_account_balances = data_actual['data']['account_balances']
        value_data_auto_fund_trasfer = data_actual['data']['auto_fund_trasfer']
        value_data_transaction_code = data_actual['data']['transaction_code']
        value_data_transaction_number = data_actual['data']['transaction_number']
        value_data_transaction_type = data_actual['data']['transaction_type']
        value_data_sub_code = data_actual['data']['sub_code']
        value_data_transaction_date = data_actual['data']['transaction_date']
        value_data_service_sys_date = data_actual['data']['service_sys_date']
        value_data_reference_id = data_actual['data']['reference_id']
        value_data_ref_id = data_actual['data']['ref_id']
        value_data_reference_code = data_actual['data']['reference_code']
        value_data_business_code = data_actual['data']['business_code']
        value_data_value_date = data_actual['data']['value_date']
        value_data_current_user_code = data_actual['data']['current_user_code']
        value_data_current_branch_code = data_actual['data']['current_branch_code']
        value_data_current_username = data_actual['data']['current_username']
        value_data_current_loginname = data_actual['data']['current_loginname']
        value_data_user_approve = data_actual['data']['user_approve']
        value_data_status = data_actual['data']['status']
        value_data_is_reverse = data_actual['data']['is_reverse']
        value_data_amount1 = data_actual['data']['amount1']
        value_data_description = data_actual['data']['description']
        value_data_token = data_actual['data']['token']
        value_data_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
        value_data_home = data_actual['data']['withdrawer_description']['home']
        value_data_office = data_actual['data']['withdrawer_description']['office']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('interest_earlywdr', 0, value_data_interest_earlywdr)
        AU.assert_equals('withdraw_amount', withdraw_amount, value_data_withdraw_amount)
        AU.assert_equals('credit_accounting', credit_accounting_valid, value_data_credit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('accounting_amount', withdraw_amount, value_data_accounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('amount_equivalent_in_bcy', 0, value_data_amount_equivalent_in_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_code', customer_code_individual, value_data_withdrawer_code)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('currency_of_deposit_account', deposit_currency, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('account_linkage', '', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_code', branch_code, value_data_branch_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_accounting', 0, value_data_total_ifc_fee_accounting)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        AU.assert_equals('total_ifc_fee', 0, value_data_total_ifc_fee)
        AU.assert_empty('passbook_number', value_data_passbook_number)
        # AU.assert_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_MWR', value_data_transaction_code)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MWR', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MWR', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
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
        AU.assert_equals('is_reverse',  False, value_data_is_reverse)
        AU.assert_equals('amount1', 0, value_data_amount1)
        AU.assert_equals('description', '1122: Miscellaneous withdrawal', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 1, len(data_actual_posting))
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array
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
        # 'postings' - verify value under array
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
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
        # 'account_balances' - get data actual
        data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # 'account_balances' - verify number items
        AU.assert_equals('Number item in account_balances', 1, len(data_account_balances))
        # 'account_balances' - verify key response under array item 1
        AU.assert_exists(expected_key['account_balances'], data_account_balances[0])
        # 'account_balances' - get value under array item 1
        value_account_balances_account_number = data_account_balances[0]['account_number']
        value_account_balances_amount = data_account_balances[0]['amount']
        value_account_balances_debit_or_credit = data_account_balances[0]['debit_or_credit']
        value_account_balances_currency = data_account_balances[0]['currency']
        value_account_balances_available_balance = data_account_balances[0]['available_balance']
        value_account_balances_transaction_number = data_account_balances[0]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[0]['transaction_date']
        value_account_balances_description = data_account_balances[0]['description']
        # 'account_balances' - verify value under array item 1
        AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', deposit_currency, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)) - Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_06_sp_dpt_mwr_002_success_current_account_status_normal_add_fee(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_mdp['data']['account_number'])
        # STEP 04: miscellaneous withdrawal
        withdraw_amount=amount_deposit-minimum_deposit_amount
        accounting_amount=withdraw_amount
        total_ifc_fee=450
        share_fee_01=0.0
        ifc_name_01='Withdrawal (MMK) For Same Region  (By Cash)'
        value_type_01='F'
        ifc_code_01=308
        payrate_01=100
        ifc_value_01=100.0
        ifc_amount_01=100.0
        currency_account_code_01='MMK'
        floor_value_01=0.0
        ceiling_value_01=0.0
        share_rate_01=0.0
        share_amount_01=0.0
        round_rate_01=0.0
        round_amount_01=0.0
        currency_fee_code_01='MMK'
        pay_source_01='CSH'
        share_fee_02=0
        ifc_name_02='Account To Account Transfer (MMK) For Same Region'
        value_type_02='F'
        ifc_code_02=309
        payrate_02=100
        ifc_value_02=350
        ifc_amount_02=350
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='CSH'
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
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name,
            fee_data=fee_data
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mwr'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_mwr_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_interest_earlywdr = data_actual['data']['interest_earlywdr']
        value_data_withdraw_amount = data_actual['data']['withdraw_amount']
        value_data_credit_accounting = data_actual['data']['credit_accounting']
        value_data_accounting_currency = data_actual['data']['accounting_currency']
        value_data_cross_rate = data_actual['data']['cross_rate']
        value_data_accounting_amount = data_actual['data']['accounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual['data']['exchange_rate_of_accounting_bcy']
        value_data_amount_equivalent_in_bcy = data_actual['data']['amount_equivalent_in_bcy']
        value_data_withdrawer_name = data_actual['data']['withdrawer_name']
        value_data_withdrawer_code = data_actual['data']['withdrawer_code']
        value_data_withdrawer_address = data_actual['data']['withdrawer_address']
        value_data_values_date = data_actual['data']['values_date']
        value_data_currency_of_deposit_account = data_actual['data']['currency_of_deposit_account']
        value_data_exchange_rate_debit_account_bcy = data_actual['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual['data']['amount_debit_account_bcy']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_code = data_actual['data']['branch_code']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_accounting = data_actual['data']['total_ifc_fee_accounting']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
        value_data_total_ifc_fee = data_actual['data']['total_ifc_fee']
        value_data_passbook_number = data_actual['data']['passbook_number']
        # value_data_account_balances = data_actual['data']['account_balances']
        value_data_auto_fund_trasfer = data_actual['data']['auto_fund_trasfer']
        value_data_transaction_code = data_actual['data']['transaction_code']
        value_data_transaction_number = data_actual['data']['transaction_number']
        value_data_transaction_type = data_actual['data']['transaction_type']
        value_data_sub_code = data_actual['data']['sub_code']
        value_data_transaction_date = data_actual['data']['transaction_date']
        value_data_service_sys_date = data_actual['data']['service_sys_date']
        value_data_reference_id = data_actual['data']['reference_id']
        value_data_ref_id = data_actual['data']['ref_id']
        value_data_reference_code = data_actual['data']['reference_code']
        value_data_business_code = data_actual['data']['business_code']
        value_data_value_date = data_actual['data']['value_date']
        value_data_current_user_code = data_actual['data']['current_user_code']
        value_data_current_branch_code = data_actual['data']['current_branch_code']
        value_data_current_username = data_actual['data']['current_username']
        value_data_current_loginname = data_actual['data']['current_loginname']
        value_data_user_approve = data_actual['data']['user_approve']
        value_data_status = data_actual['data']['status']
        value_data_is_reverse = data_actual['data']['is_reverse']
        value_data_amount1 = data_actual['data']['amount1']
        value_data_description = data_actual['data']['description']
        value_data_token = data_actual['data']['token']
        value_data_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
        value_data_home = data_actual['data']['withdrawer_description']['home']
        value_data_office = data_actual['data']['withdrawer_description']['office']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('interest_earlywdr', 0, value_data_interest_earlywdr)
        AU.assert_equals('withdraw_amount', withdraw_amount, value_data_withdraw_amount)
        AU.assert_equals('credit_accounting', credit_accounting_valid, value_data_credit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('accounting_amount', withdraw_amount, value_data_accounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('amount_equivalent_in_bcy', 0, value_data_amount_equivalent_in_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_code', customer_code_individual, value_data_withdrawer_code)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('currency_of_deposit_account', deposit_currency, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('account_linkage', '', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_code', branch_code, value_data_branch_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_accounting', 0, value_data_total_ifc_fee_accounting)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        AU.assert_equals('total_ifc_fee', total_ifc_fee, value_data_total_ifc_fee)
        AU.assert_empty('passbook_number', value_data_passbook_number)
        # AU.assert_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_MWR', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MWR', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MWR', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
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
        AU.assert_equals('is_reverse',  False, value_data_is_reverse)
        AU.assert_equals('amount1', 0, value_data_amount1)
        AU.assert_equals('description', '1122: Miscellaneous withdrawal', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'fee_data', item 1
        AU.assert_exists(expected_key['fee_data'], data_actual['data']['fee_data'][0])
        # 'response' - get value under 'data' and 'fee_data', item 1
        value_fee_data_ifc_name = data_actual['data']['fee_data'][0]['ifc_name']
        value_fee_data_share_fee = data_actual['data']['fee_data'][0]['share_fee']
        value_fee_data_ifc_code = data_actual['data']['fee_data'][0]['ifc_code']
        value_fee_data_payrate = data_actual['data']['fee_data'][0]['payrate']
        value_fee_data_ifc_value = data_actual['data']['fee_data'][0]['ifc_value']
        value_fee_data_ifc_amount = data_actual['data']['fee_data'][0]['ifc_amount']
        value_fee_data_currency_account_code = data_actual['data']['fee_data'][0]['currency_account_code']
        value_fee_data_floor_value = data_actual['data']['fee_data'][0]['floor_value']
        value_fee_data_ceiling_value = data_actual['data']['fee_data'][0]['ceiling_value']
        value_fee_data_share_rate = data_actual['data']['fee_data'][0]['share_rate']
        value_fee_data_share_amount = data_actual['data']['fee_data'][0]['share_amount']
        value_fee_data_round_rate = data_actual['data']['fee_data'][0]['round_rate']
        value_fee_data_round_amount = data_actual['data']['fee_data'][0]['round_amount']
        value_fee_data_currency_fee_code = data_actual['data']['fee_data'][0]['currency_fee_code']
        value_fee_data_pay_source = data_actual['data']['fee_data'][0]['pay_source']
        # value_fee_data_value_typect = data_actual['data']['fee_data'][0]['value_typect']
        value_fee_data_value_type = data_actual['data']['fee_data'][0]['value_type']
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
        AU.assert_exists(expected_key['fee_data'], data_actual['data']['fee_data'][1])
        # 'response' - get value under 'data' and 'fee_data', item 2
        value_fee_data_ifc_name = data_actual['data']['fee_data'][1]['ifc_name']
        value_fee_data_share_fee = data_actual['data']['fee_data'][1]['share_fee']
        value_fee_data_ifc_code = data_actual['data']['fee_data'][1]['ifc_code']
        value_fee_data_payrate = data_actual['data']['fee_data'][1]['payrate']
        value_fee_data_ifc_value = data_actual['data']['fee_data'][1]['ifc_value']
        value_fee_data_ifc_amount = data_actual['data']['fee_data'][1]['ifc_amount']
        value_fee_data_currency_account_code = data_actual['data']['fee_data'][1]['currency_account_code']
        value_fee_data_floor_value = data_actual['data']['fee_data'][1]['floor_value']
        value_fee_data_ceiling_value = data_actual['data']['fee_data'][1]['ceiling_value']
        value_fee_data_share_rate = data_actual['data']['fee_data'][1]['share_rate']
        value_fee_data_share_amount = data_actual['data']['fee_data'][1]['share_amount']
        value_fee_data_round_rate = data_actual['data']['fee_data'][1]['round_rate']
        value_fee_data_round_amount = data_actual['data']['fee_data'][1]['round_amount']
        value_fee_data_currency_fee_code = data_actual['data']['fee_data'][1]['currency_fee_code']
        value_fee_data_pay_source = data_actual['data']['fee_data'][1]['pay_source']
        # value_fee_data_value_typect = data_actual['data']['fee_data'][1]['value_typect']
        value_fee_data_value_type = data_actual['data']['fee_data'][1]['value_type']
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
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 3, len(data_actual_posting))
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array item 1
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
        # 'postings' - verify value under array item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
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
        # 'postings' - get value under array item 2
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
        # 'postings' - verify value under array item 2
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc, value_GLAccount)
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
        # 'postings' - get value under array item 3
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
        # 'postings' - verify value under array item 3
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc, value_GLAccount)
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
        # 'account_balances' - get data actual
        data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # 'account_balances' - verify number items
        AU.assert_equals('Number item in account_balances', 1, len(data_account_balances))
        # 'account_balances' - verify key response under array item 1
        AU.assert_exists(expected_key['account_balances'], data_account_balances[0])
        # 'account_balances' - get value under array item 1
        value_account_balances_account_number = data_account_balances[0]['account_number']
        value_account_balances_amount = data_account_balances[0]['amount']
        value_account_balances_debit_or_credit = data_account_balances[0]['debit_or_credit']
        value_account_balances_currency = data_account_balances[0]['currency']
        value_account_balances_available_balance = data_account_balances[0]['available_balance']
        value_account_balances_transaction_number = data_account_balances[0]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[0]['transaction_date']
        value_account_balances_description = data_account_balances[0]['description']
        # 'account_balances' - verify value under array item 1
        AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', deposit_currency, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)) - Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_06_sp_dpt_mwr_003_success_saving_account_status_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='BSMMK0000'
        catalog_name='Bonus savings account  in MMK'
        deposit_type='Savings'
        deposit_sub_type='S2'
        minimum_deposit_amount=50000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_mdp['data']['account_number'])
        # STEP 04: miscellaneous withdrawal
        withdraw_amount=amount_deposit-minimum_deposit_amount
        accounting_amount=withdraw_amount
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mwr'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_mwr_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_interest_earlywdr = data_actual['data']['interest_earlywdr']
        value_data_withdraw_amount = data_actual['data']['withdraw_amount']
        value_data_credit_accounting = data_actual['data']['credit_accounting']
        value_data_accounting_currency = data_actual['data']['accounting_currency']
        value_data_cross_rate = data_actual['data']['cross_rate']
        value_data_accounting_amount = data_actual['data']['accounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual['data']['exchange_rate_of_accounting_bcy']
        value_data_amount_equivalent_in_bcy = data_actual['data']['amount_equivalent_in_bcy']
        value_data_withdrawer_name = data_actual['data']['withdrawer_name']
        value_data_withdrawer_code = data_actual['data']['withdrawer_code']
        value_data_withdrawer_address = data_actual['data']['withdrawer_address']
        value_data_values_date = data_actual['data']['values_date']
        value_data_currency_of_deposit_account = data_actual['data']['currency_of_deposit_account']
        value_data_exchange_rate_debit_account_bcy = data_actual['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual['data']['amount_debit_account_bcy']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_code = data_actual['data']['branch_code']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_accounting = data_actual['data']['total_ifc_fee_accounting']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
        value_data_total_ifc_fee = data_actual['data']['total_ifc_fee']
        value_data_passbook_number = data_actual['data']['passbook_number']
        # value_data_account_balances = data_actual['data']['account_balances']
        value_data_auto_fund_trasfer = data_actual['data']['auto_fund_trasfer']
        value_data_transaction_code = data_actual['data']['transaction_code']
        value_data_transaction_number = data_actual['data']['transaction_number']
        value_data_transaction_type = data_actual['data']['transaction_type']
        value_data_sub_code = data_actual['data']['sub_code']
        value_data_transaction_date = data_actual['data']['transaction_date']
        value_data_service_sys_date = data_actual['data']['service_sys_date']
        value_data_reference_id = data_actual['data']['reference_id']
        value_data_ref_id = data_actual['data']['ref_id']
        value_data_reference_code = data_actual['data']['reference_code']
        value_data_business_code = data_actual['data']['business_code']
        value_data_value_date = data_actual['data']['value_date']
        value_data_current_user_code = data_actual['data']['current_user_code']
        value_data_current_branch_code = data_actual['data']['current_branch_code']
        value_data_current_username = data_actual['data']['current_username']
        value_data_current_loginname = data_actual['data']['current_loginname']
        value_data_user_approve = data_actual['data']['user_approve']
        value_data_status = data_actual['data']['status']
        value_data_is_reverse = data_actual['data']['is_reverse']
        value_data_amount1 = data_actual['data']['amount1']
        value_data_description = data_actual['data']['description']
        value_data_token = data_actual['data']['token']
        value_data_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
        value_data_home = data_actual['data']['withdrawer_description']['home']
        value_data_office = data_actual['data']['withdrawer_description']['office']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('interest_earlywdr', 0, value_data_interest_earlywdr)
        AU.assert_equals('withdraw_amount', withdraw_amount, value_data_withdraw_amount)
        AU.assert_equals('credit_accounting', credit_accounting_valid, value_data_credit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('accounting_amount', withdraw_amount, value_data_accounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('amount_equivalent_in_bcy', 0, value_data_amount_equivalent_in_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_code', customer_code_individual, value_data_withdrawer_code)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('currency_of_deposit_account', deposit_currency, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('account_linkage', '', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_code', branch_code, value_data_branch_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_accounting', 0, value_data_total_ifc_fee_accounting)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        AU.assert_equals('total_ifc_fee', 0, value_data_total_ifc_fee)
        AU.assert_empty('passbook_number', value_data_passbook_number)
        # AU.assert_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_MWR', value_data_transaction_code)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MWR', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MWR', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
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
        AU.assert_equals('is_reverse',  False, value_data_is_reverse)
        AU.assert_equals('amount1', 0, value_data_amount1)
        AU.assert_equals('description', '1122: Miscellaneous withdrawal', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 1, len(data_actual_posting))
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array
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
        # 'postings' - verify value under array
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
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
        # 'account_balances' - get data actual
        data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # 'account_balances' - verify number items
        AU.assert_equals('Number item in account_balances', 1, len(data_account_balances))
        # 'account_balances' - verify key response under array item 1
        AU.assert_exists(expected_key['account_balances'], data_account_balances[0])
        # 'account_balances' - get value under array item 1
        value_account_balances_account_number = data_account_balances[0]['account_number']
        value_account_balances_amount = data_account_balances[0]['amount']
        value_account_balances_debit_or_credit = data_account_balances[0]['debit_or_credit']
        value_account_balances_currency = data_account_balances[0]['currency']
        value_account_balances_available_balance = data_account_balances[0]['available_balance']
        value_account_balances_transaction_number = data_account_balances[0]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[0]['transaction_date']
        value_account_balances_description = data_account_balances[0]['description']
        # 'account_balances' - verify value under array item 1
        AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', deposit_currency, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)) - Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_06_sp_dpt_mwr_004_success_saving_account_status_normal_add_fee(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_mdp['data']['account_number'])
        # STEP 04: miscellaneous withdrawal
        withdraw_amount=amount_deposit-minimum_deposit_amount
        accounting_amount=withdraw_amount
        total_ifc_fee=450
        share_fee_01=0.0
        ifc_name_01='Withdrawal (MMK) For Same Region  (By Cash)'
        value_type_01='F'
        ifc_code_01=308
        payrate_01=100
        ifc_value_01=100.0
        ifc_amount_01=100.0
        currency_account_code_01='MMK'
        floor_value_01=0.0
        ceiling_value_01=0.0
        share_rate_01=0.0
        share_amount_01=0.0
        round_rate_01=0.0
        round_amount_01=0.0
        currency_fee_code_01='MMK'
        pay_source_01='CSH'
        share_fee_02=0
        ifc_name_02='Account To Account Transfer (MMK) For Same Region'
        value_type_02='F'
        ifc_code_02=309
        payrate_02=100
        ifc_value_02=350
        ifc_amount_02=350
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='CSH'
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
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name,
            fee_data=fee_data
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mwr'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_mwr_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_interest_earlywdr = data_actual['data']['interest_earlywdr']
        value_data_withdraw_amount = data_actual['data']['withdraw_amount']
        value_data_credit_accounting = data_actual['data']['credit_accounting']
        value_data_accounting_currency = data_actual['data']['accounting_currency']
        value_data_cross_rate = data_actual['data']['cross_rate']
        value_data_accounting_amount = data_actual['data']['accounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual['data']['exchange_rate_of_accounting_bcy']
        value_data_amount_equivalent_in_bcy = data_actual['data']['amount_equivalent_in_bcy']
        value_data_withdrawer_name = data_actual['data']['withdrawer_name']
        value_data_withdrawer_code = data_actual['data']['withdrawer_code']
        value_data_withdrawer_address = data_actual['data']['withdrawer_address']
        value_data_values_date = data_actual['data']['values_date']
        value_data_currency_of_deposit_account = data_actual['data']['currency_of_deposit_account']
        value_data_exchange_rate_debit_account_bcy = data_actual['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual['data']['amount_debit_account_bcy']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_code = data_actual['data']['branch_code']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_accounting = data_actual['data']['total_ifc_fee_accounting']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
        value_data_total_ifc_fee = data_actual['data']['total_ifc_fee']
        value_data_passbook_number = data_actual['data']['passbook_number']
        # value_data_account_balances = data_actual['data']['account_balances']
        value_data_auto_fund_trasfer = data_actual['data']['auto_fund_trasfer']
        value_data_transaction_code = data_actual['data']['transaction_code']
        value_data_transaction_number = data_actual['data']['transaction_number']
        value_data_transaction_type = data_actual['data']['transaction_type']
        value_data_sub_code = data_actual['data']['sub_code']
        value_data_transaction_date = data_actual['data']['transaction_date']
        value_data_service_sys_date = data_actual['data']['service_sys_date']
        value_data_reference_id = data_actual['data']['reference_id']
        value_data_ref_id = data_actual['data']['ref_id']
        value_data_reference_code = data_actual['data']['reference_code']
        value_data_business_code = data_actual['data']['business_code']
        value_data_value_date = data_actual['data']['value_date']
        value_data_current_user_code = data_actual['data']['current_user_code']
        value_data_current_branch_code = data_actual['data']['current_branch_code']
        value_data_current_username = data_actual['data']['current_username']
        value_data_current_loginname = data_actual['data']['current_loginname']
        value_data_user_approve = data_actual['data']['user_approve']
        value_data_status = data_actual['data']['status']
        value_data_is_reverse = data_actual['data']['is_reverse']
        value_data_amount1 = data_actual['data']['amount1']
        value_data_description = data_actual['data']['description']
        value_data_token = data_actual['data']['token']
        value_data_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
        value_data_home = data_actual['data']['withdrawer_description']['home']
        value_data_office = data_actual['data']['withdrawer_description']['office']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('interest_earlywdr', 0, value_data_interest_earlywdr)
        AU.assert_equals('withdraw_amount', withdraw_amount, value_data_withdraw_amount)
        AU.assert_equals('credit_accounting', credit_accounting_valid, value_data_credit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('accounting_amount', withdraw_amount, value_data_accounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('amount_equivalent_in_bcy', 0, value_data_amount_equivalent_in_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_code', customer_code_individual, value_data_withdrawer_code)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('currency_of_deposit_account', deposit_currency, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('account_linkage', '', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_code', branch_code, value_data_branch_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_accounting', 0, value_data_total_ifc_fee_accounting)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        AU.assert_equals('total_ifc_fee', total_ifc_fee, value_data_total_ifc_fee)
        AU.assert_empty('passbook_number', value_data_passbook_number)
        # AU.assert_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_MWR', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MWR', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MWR', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
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
        AU.assert_equals('is_reverse',  False, value_data_is_reverse)
        AU.assert_equals('amount1', 0, value_data_amount1)
        AU.assert_equals('description', '1122: Miscellaneous withdrawal', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'fee_data', item 1
        AU.assert_exists(expected_key['fee_data'], data_actual['data']['fee_data'][0])
        # 'response' - get value under 'data' and 'fee_data', item 1
        value_fee_data_ifc_name = data_actual['data']['fee_data'][0]['ifc_name']
        value_fee_data_share_fee = data_actual['data']['fee_data'][0]['share_fee']
        value_fee_data_ifc_code = data_actual['data']['fee_data'][0]['ifc_code']
        value_fee_data_payrate = data_actual['data']['fee_data'][0]['payrate']
        value_fee_data_ifc_value = data_actual['data']['fee_data'][0]['ifc_value']
        value_fee_data_ifc_amount = data_actual['data']['fee_data'][0]['ifc_amount']
        value_fee_data_currency_account_code = data_actual['data']['fee_data'][0]['currency_account_code']
        value_fee_data_floor_value = data_actual['data']['fee_data'][0]['floor_value']
        value_fee_data_ceiling_value = data_actual['data']['fee_data'][0]['ceiling_value']
        value_fee_data_share_rate = data_actual['data']['fee_data'][0]['share_rate']
        value_fee_data_share_amount = data_actual['data']['fee_data'][0]['share_amount']
        value_fee_data_round_rate = data_actual['data']['fee_data'][0]['round_rate']
        value_fee_data_round_amount = data_actual['data']['fee_data'][0]['round_amount']
        value_fee_data_currency_fee_code = data_actual['data']['fee_data'][0]['currency_fee_code']
        value_fee_data_pay_source = data_actual['data']['fee_data'][0]['pay_source']
        # value_fee_data_value_typect = data_actual['data']['fee_data'][0]['value_typect']
        value_fee_data_value_type = data_actual['data']['fee_data'][0]['value_type']
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
        AU.assert_exists(expected_key['fee_data'], data_actual['data']['fee_data'][1])
        # 'response' - get value under 'data' and 'fee_data', item 2
        value_fee_data_ifc_name = data_actual['data']['fee_data'][1]['ifc_name']
        value_fee_data_share_fee = data_actual['data']['fee_data'][1]['share_fee']
        value_fee_data_ifc_code = data_actual['data']['fee_data'][1]['ifc_code']
        value_fee_data_payrate = data_actual['data']['fee_data'][1]['payrate']
        value_fee_data_ifc_value = data_actual['data']['fee_data'][1]['ifc_value']
        value_fee_data_ifc_amount = data_actual['data']['fee_data'][1]['ifc_amount']
        value_fee_data_currency_account_code = data_actual['data']['fee_data'][1]['currency_account_code']
        value_fee_data_floor_value = data_actual['data']['fee_data'][1]['floor_value']
        value_fee_data_ceiling_value = data_actual['data']['fee_data'][1]['ceiling_value']
        value_fee_data_share_rate = data_actual['data']['fee_data'][1]['share_rate']
        value_fee_data_share_amount = data_actual['data']['fee_data'][1]['share_amount']
        value_fee_data_round_rate = data_actual['data']['fee_data'][1]['round_rate']
        value_fee_data_round_amount = data_actual['data']['fee_data'][1]['round_amount']
        value_fee_data_currency_fee_code = data_actual['data']['fee_data'][1]['currency_fee_code']
        value_fee_data_pay_source = data_actual['data']['fee_data'][1]['pay_source']
        # value_fee_data_value_typect = data_actual['data']['fee_data'][1]['value_typect']
        value_fee_data_value_type = data_actual['data']['fee_data'][1]['value_type']
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
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 3, len(data_actual_posting))
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array item 1
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
        # 'postings' - verify value under array item 1
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
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
        # 'postings' - get value under array item 2
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
        # 'postings' - verify value under array item 2
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc, value_GLAccount)
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
        # 'postings' - get value under array item 3
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
        # 'postings' - verify value under array item 3
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc, value_GLAccount)
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
        # 'account_balances' - get data actual
        data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # 'account_balances' - verify number items
        AU.assert_equals('Number item in account_balances', 1, len(data_account_balances))
        # 'account_balances' - verify key response under array item 1
        AU.assert_exists(expected_key['account_balances'], data_account_balances[0])
        # 'account_balances' - get value under array item 1
        value_account_balances_account_number = data_account_balances[0]['account_number']
        value_account_balances_amount = data_account_balances[0]['amount']
        value_account_balances_debit_or_credit = data_account_balances[0]['debit_or_credit']
        value_account_balances_currency = data_account_balances[0]['currency']
        value_account_balances_available_balance = data_account_balances[0]['available_balance']
        value_account_balances_transaction_number = data_account_balances[0]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[0]['transaction_date']
        value_account_balances_description = data_account_balances[0]['description']
        # 'account_balances' - verify value under array item 1
        AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', deposit_currency, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)) - Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_06_sp_dpt_mwr_005_success_current_account_status_dormant(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000.00
        # minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_mdp['data']['account_number'])
        # STEP 04: change status from 'Normal' to 'Dormant'
        fields_data_cas = sp_payload.DPT_CAS(
            account_number=account_number,
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
        # STEP 05: miscellaneous withdrawal from deposit status 'Dormant'
        withdraw_amount=amount_deposit-minimum_deposit_amount
        accounting_amount=withdraw_amount
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'ApprovalRequired', value_error_code)
        AU.assert_equals('error_message', 'ApprovalRequired', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_006_success_saving_account_status_dormant(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_mdp['data']['account_number'])
        # STEP 04: change status from 'Normal' to 'Dormant'
        fields_data_cas = sp_payload.DPT_CAS(
            account_number=account_number,
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
        # STEP 05: miscellaneous withdrawal from deposit status 'Dormant'
        withdraw_amount=amount_deposit-minimum_deposit_amount
        accounting_amount=withdraw_amount
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'ApprovalRequired', value_error_code)
        AU.assert_equals('error_message', 'ApprovalRequired', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_007_success_current_account_fund_transfer(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve and deposit money to current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount_current=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_mdp['data']['account_number'])
        # STEP 02-01: open, approve and deposit money to saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount_saving=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_mdp['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mwr'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_mwr_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_interest_earlywdr = data_actual['data']['interest_earlywdr']
        value_data_withdraw_amount = data_actual['data']['withdraw_amount']
        value_data_credit_accounting = data_actual['data']['credit_accounting']
        value_data_accounting_currency = data_actual['data']['accounting_currency']
        value_data_cross_rate = data_actual['data']['cross_rate']
        value_data_accounting_amount = data_actual['data']['accounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual['data']['exchange_rate_of_accounting_bcy']
        value_data_amount_equivalent_in_bcy = data_actual['data']['amount_equivalent_in_bcy']
        value_data_withdrawer_name = data_actual['data']['withdrawer_name']
        value_data_withdrawer_code = data_actual['data']['withdrawer_code']
        value_data_withdrawer_address = data_actual['data']['withdrawer_address']
        value_data_values_date = data_actual['data']['values_date']
        value_data_currency_of_deposit_account = data_actual['data']['currency_of_deposit_account']
        value_data_exchange_rate_debit_account_bcy = data_actual['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual['data']['amount_debit_account_bcy']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_code = data_actual['data']['branch_code']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_accounting = data_actual['data']['total_ifc_fee_accounting']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
        value_data_total_ifc_fee = data_actual['data']['total_ifc_fee']
        value_data_passbook_number = data_actual['data']['passbook_number']
        # value_data_account_balances = data_actual['data']['account_balances']
        value_data_auto_fund_trasfer = data_actual['data']['auto_fund_trasfer']
        value_data_transaction_code = data_actual['data']['transaction_code']
        value_data_transaction_number = data_actual['data']['transaction_number']
        value_data_transaction_type = data_actual['data']['transaction_type']
        value_data_sub_code = data_actual['data']['sub_code']
        value_data_transaction_date = data_actual['data']['transaction_date']
        value_data_service_sys_date = data_actual['data']['service_sys_date']
        value_data_reference_id = data_actual['data']['reference_id']
        value_data_ref_id = data_actual['data']['ref_id']
        value_data_reference_code = data_actual['data']['reference_code']
        value_data_business_code = data_actual['data']['business_code']
        value_data_value_date = data_actual['data']['value_date']
        value_data_current_user_code = data_actual['data']['current_user_code']
        value_data_current_branch_code = data_actual['data']['current_branch_code']
        value_data_current_username = data_actual['data']['current_username']
        value_data_current_loginname = data_actual['data']['current_loginname']
        value_data_user_approve = data_actual['data']['user_approve']
        value_data_status = data_actual['data']['status']
        value_data_is_reverse = data_actual['data']['is_reverse']
        value_data_amount1 = data_actual['data']['amount1']
        value_data_description = data_actual['data']['description']
        value_data_token = data_actual['data']['token']
        value_data_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
        value_data_home = data_actual['data']['withdrawer_description']['home']
        value_data_office = data_actual['data']['withdrawer_description']['office']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('interest_earlywdr', 0, value_data_interest_earlywdr)
        AU.assert_equals('withdraw_amount', withdraw_amount_fund, value_data_withdraw_amount)
        AU.assert_equals('credit_accounting', credit_accounting_valid, value_data_credit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('accounting_amount', withdraw_amount_fund, value_data_accounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('amount_equivalent_in_bcy', 0, value_data_amount_equivalent_in_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_code', customer_code_individual, value_data_withdrawer_code)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('currency_of_deposit_account', deposit_currency, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('account_linkage', '', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_code', branch_code, value_data_branch_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_accounting', 0, value_data_total_ifc_fee_accounting)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        AU.assert_equals('total_ifc_fee', 0, value_data_total_ifc_fee)
        AU.assert_empty('passbook_number', value_data_passbook_number)
        # AU.assert_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_MWR', value_data_transaction_code)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MWR', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MWR', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
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
        AU.assert_equals('is_reverse',  False, value_data_is_reverse)
        AU.assert_equals('amount1', 0, value_data_amount1)
        AU.assert_equals('description', '1122: Miscellaneous withdrawal', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
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
        AU.assert_equals('GLAccount', gl_account_deposit_current, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', Decimal(str(withdraw_amount_fund))-(Decimal(str(amount_deposit_current))-Decimal(str(minimum_deposit_amount_current))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 0, value_AccountingGroup)
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
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit_current, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount_fund, value_Amount)
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
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit_saving, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', Decimal(str(withdraw_amount_fund))-(Decimal(str(amount_deposit_current))-Decimal(str(minimum_deposit_amount_current))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 0, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'account_balances' - get data actual
        data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # 'account_balances' - verify number items
        AU.assert_equals('Number item in account_balances', 1, len(data_account_balances))
        # 'account_balances' - verify key response under array item 1
        AU.assert_exists(expected_key['account_balances'], data_account_balances[0])
        # 'account_balances' - get value under array item 1
        value_account_balances_account_number = data_account_balances[0]['account_number']
        value_account_balances_amount = data_account_balances[0]['amount']
        value_account_balances_debit_or_credit = data_account_balances[0]['debit_or_credit']
        value_account_balances_currency = data_account_balances[0]['currency']
        value_account_balances_available_balance = data_account_balances[0]['available_balance']
        value_account_balances_transaction_number = data_account_balances[0]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[0]['transaction_date']
        value_account_balances_description = data_account_balances[0]['description']
        # 'account_balances' - verify value under array item 1  - (Decimal(str(amount_deposit_current)) - Decimal(str(minimum_deposit_amount_current)))
        AU.assert_equals('account_number', account_number_current, value_account_balances_account_number)
        AU.assert_equals('amount', Decimal(str(withdraw_amount_fund)), value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', deposit_currency, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(0)), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_06_sp_dpt_mwr_008_success_current_account_fund_transfer_add_fee(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve and deposit money to current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount_current=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_mdp['data']['account_number'])
        # STEP 02-01: open, approve and deposit money to saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount_saving=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_mdp['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        total_ifc_fee=450
        share_fee_01=0.0
        ifc_name_01='Withdrawal (MMK) For Same Region  (By Cash)'
        value_type_01='F'
        ifc_code_01=308
        payrate_01=100
        ifc_value_01=100.0
        ifc_amount_01=100.0
        currency_account_code_01='MMK'
        floor_value_01=0.0
        ceiling_value_01=0.0
        share_rate_01=0.0
        share_amount_01=0.0
        round_rate_01=0.0
        round_amount_01=0.0
        currency_fee_code_01='MMK'
        pay_source_01='CSH'
        share_fee_02=0
        ifc_name_02='Account To Account Transfer (MMK) For Same Region'
        value_type_02='F'
        ifc_code_02=309
        payrate_02=100
        ifc_value_02=350
        ifc_amount_02=350
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='CSH'
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
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name,
            fee_data=fee_data
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mwr'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_mwr_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_interest_earlywdr = data_actual['data']['interest_earlywdr']
        value_data_withdraw_amount = data_actual['data']['withdraw_amount']
        value_data_credit_accounting = data_actual['data']['credit_accounting']
        value_data_accounting_currency = data_actual['data']['accounting_currency']
        value_data_cross_rate = data_actual['data']['cross_rate']
        value_data_accounting_amount = data_actual['data']['accounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual['data']['exchange_rate_of_accounting_bcy']
        value_data_amount_equivalent_in_bcy = data_actual['data']['amount_equivalent_in_bcy']
        value_data_withdrawer_name = data_actual['data']['withdrawer_name']
        value_data_withdrawer_code = data_actual['data']['withdrawer_code']
        value_data_withdrawer_address = data_actual['data']['withdrawer_address']
        value_data_values_date = data_actual['data']['values_date']
        value_data_currency_of_deposit_account = data_actual['data']['currency_of_deposit_account']
        value_data_exchange_rate_debit_account_bcy = data_actual['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual['data']['amount_debit_account_bcy']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_code = data_actual['data']['branch_code']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_accounting = data_actual['data']['total_ifc_fee_accounting']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
        value_data_total_ifc_fee = data_actual['data']['total_ifc_fee']
        value_data_passbook_number = data_actual['data']['passbook_number']
        # value_data_account_balances = data_actual['data']['account_balances']
        value_data_auto_fund_trasfer = data_actual['data']['auto_fund_trasfer']
        value_data_transaction_code = data_actual['data']['transaction_code']
        value_data_transaction_number = data_actual['data']['transaction_number']
        value_data_transaction_type = data_actual['data']['transaction_type']
        value_data_sub_code = data_actual['data']['sub_code']
        value_data_transaction_date = data_actual['data']['transaction_date']
        value_data_service_sys_date = data_actual['data']['service_sys_date']
        value_data_reference_id = data_actual['data']['reference_id']
        value_data_ref_id = data_actual['data']['ref_id']
        value_data_reference_code = data_actual['data']['reference_code']
        value_data_business_code = data_actual['data']['business_code']
        value_data_value_date = data_actual['data']['value_date']
        value_data_current_user_code = data_actual['data']['current_user_code']
        value_data_current_branch_code = data_actual['data']['current_branch_code']
        value_data_current_username = data_actual['data']['current_username']
        value_data_current_loginname = data_actual['data']['current_loginname']
        value_data_user_approve = data_actual['data']['user_approve']
        value_data_status = data_actual['data']['status']
        value_data_is_reverse = data_actual['data']['is_reverse']
        value_data_amount1 = data_actual['data']['amount1']
        value_data_description = data_actual['data']['description']
        value_data_token = data_actual['data']['token']
        value_data_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
        value_data_home = data_actual['data']['withdrawer_description']['home']
        value_data_office = data_actual['data']['withdrawer_description']['office']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('interest_earlywdr', 0, value_data_interest_earlywdr)
        AU.assert_equals('withdraw_amount', withdraw_amount_fund, value_data_withdraw_amount)
        AU.assert_equals('credit_accounting', credit_accounting_valid, value_data_credit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('accounting_amount', withdraw_amount_fund, value_data_accounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('amount_equivalent_in_bcy', 0, value_data_amount_equivalent_in_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_code', customer_code_individual, value_data_withdrawer_code)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('currency_of_deposit_account', deposit_currency, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('account_linkage', '', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_code', branch_code, value_data_branch_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_accounting', 0, value_data_total_ifc_fee_accounting)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        AU.assert_equals('total_ifc_fee', total_ifc_fee, value_data_total_ifc_fee)
        AU.assert_empty('passbook_number', value_data_passbook_number)
        # AU.assert_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_MWR', value_data_transaction_code)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MWR', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MWR', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
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
        AU.assert_equals('is_reverse',  False, value_data_is_reverse)
        AU.assert_equals('amount1', 0, value_data_amount1)
        AU.assert_equals('description', '1122: Miscellaneous withdrawal', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'fee_data', item 1
        AU.assert_exists(expected_key['fee_data'], data_actual['data']['fee_data'][0])
        # 'response' - get value under 'data' and 'fee_data', item 1
        value_fee_data_ifc_name = data_actual['data']['fee_data'][0]['ifc_name']
        value_fee_data_share_fee = data_actual['data']['fee_data'][0]['share_fee']
        value_fee_data_ifc_code = data_actual['data']['fee_data'][0]['ifc_code']
        value_fee_data_payrate = data_actual['data']['fee_data'][0]['payrate']
        value_fee_data_ifc_value = data_actual['data']['fee_data'][0]['ifc_value']
        value_fee_data_ifc_amount = data_actual['data']['fee_data'][0]['ifc_amount']
        value_fee_data_currency_account_code = data_actual['data']['fee_data'][0]['currency_account_code']
        value_fee_data_floor_value = data_actual['data']['fee_data'][0]['floor_value']
        value_fee_data_ceiling_value = data_actual['data']['fee_data'][0]['ceiling_value']
        value_fee_data_share_rate = data_actual['data']['fee_data'][0]['share_rate']
        value_fee_data_share_amount = data_actual['data']['fee_data'][0]['share_amount']
        value_fee_data_round_rate = data_actual['data']['fee_data'][0]['round_rate']
        value_fee_data_round_amount = data_actual['data']['fee_data'][0]['round_amount']
        value_fee_data_currency_fee_code = data_actual['data']['fee_data'][0]['currency_fee_code']
        value_fee_data_pay_source = data_actual['data']['fee_data'][0]['pay_source']
        # value_fee_data_value_typect = data_actual['data']['fee_data'][0]['value_typect']
        value_fee_data_value_type = data_actual['data']['fee_data'][0]['value_type']
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
        AU.assert_exists(expected_key['fee_data'], data_actual['data']['fee_data'][1])
        # 'response' - get value under 'data' and 'fee_data', item 2
        value_fee_data_ifc_name = data_actual['data']['fee_data'][1]['ifc_name']
        value_fee_data_share_fee = data_actual['data']['fee_data'][1]['share_fee']
        value_fee_data_ifc_code = data_actual['data']['fee_data'][1]['ifc_code']
        value_fee_data_payrate = data_actual['data']['fee_data'][1]['payrate']
        value_fee_data_ifc_value = data_actual['data']['fee_data'][1]['ifc_value']
        value_fee_data_ifc_amount = data_actual['data']['fee_data'][1]['ifc_amount']
        value_fee_data_currency_account_code = data_actual['data']['fee_data'][1]['currency_account_code']
        value_fee_data_floor_value = data_actual['data']['fee_data'][1]['floor_value']
        value_fee_data_ceiling_value = data_actual['data']['fee_data'][1]['ceiling_value']
        value_fee_data_share_rate = data_actual['data']['fee_data'][1]['share_rate']
        value_fee_data_share_amount = data_actual['data']['fee_data'][1]['share_amount']
        value_fee_data_round_rate = data_actual['data']['fee_data'][1]['round_rate']
        value_fee_data_round_amount = data_actual['data']['fee_data'][1]['round_amount']
        value_fee_data_currency_fee_code = data_actual['data']['fee_data'][1]['currency_fee_code']
        value_fee_data_pay_source = data_actual['data']['fee_data'][1]['pay_source']
        # value_fee_data_value_typect = data_actual['data']['fee_data'][1]['value_typect']
        value_fee_data_value_type = data_actual['data']['fee_data'][1]['value_type']
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
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        AU.assert_equals('Number item in posting', 5, len(data_actual_posting))
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
        AU.assert_equals('GLAccount', gl_account_deposit_current, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', Decimal(str(withdraw_amount_fund))-(Decimal(str(amount_deposit_current))-Decimal(str(minimum_deposit_amount_current))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 0, value_AccountingGroup)
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
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit_current, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount_fund, value_Amount)
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
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit_saving, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', Decimal(str(withdraw_amount_fund))-(Decimal(str(amount_deposit_current))-Decimal(str(minimum_deposit_amount_current))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', deposit_currency, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 0, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # 'postings' - verify key response, item 4
        AU.assert_exists(expected_key['postings'], data_actual_posting[3])
        # 'postings' - get value under array, item 4
        value_TransactionNumber = data_actual_posting[3]['TransactionNumber']
        value_TransTableName = data_actual_posting[3]['TransTableName']
        value_TransId = data_actual_posting[3]['TransId']
        value_SysAccountName = data_actual_posting[3]['SysAccountName']
        value_GLAccount = data_actual_posting[3]['GLAccount']
        value_DorC = data_actual_posting[3]['DorC']
        value_TransactionStatus = data_actual_posting[3]['TransactionStatus']
        value_Amount = data_actual_posting[3]['Amount']
        value_BranchCode = data_actual_posting[3]['BranchCode']
        value_CurrencyCode = data_actual_posting[3]['CurrencyCode']
        value_ValueDate = data_actual_posting[3]['ValueDate']
        value_Posted = data_actual_posting[3]['Posted']
        value_AccountingGroup = data_actual_posting[3]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[3]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[3]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[3]['BaseCurrencyAmount']
        value_Id = data_actual_posting[3]['Id']
        # 'postings' - verify value under array, item 4
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc, value_GLAccount)
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
        # 'postings' - verify key response, item 5
        AU.assert_exists(expected_key['postings'], data_actual_posting[4])
        # 'postings' - get value under array, item 5
        value_TransactionNumber = data_actual_posting[4]['TransactionNumber']
        value_TransTableName = data_actual_posting[4]['TransTableName']
        value_TransId = data_actual_posting[4]['TransId']
        value_SysAccountName = data_actual_posting[4]['SysAccountName']
        value_GLAccount = data_actual_posting[4]['GLAccount']
        value_DorC = data_actual_posting[4]['DorC']
        value_TransactionStatus = data_actual_posting[4]['TransactionStatus']
        value_Amount = data_actual_posting[4]['Amount']
        value_BranchCode = data_actual_posting[4]['BranchCode']
        value_CurrencyCode = data_actual_posting[4]['CurrencyCode']
        value_ValueDate = data_actual_posting[4]['ValueDate']
        value_Posted = data_actual_posting[4]['Posted']
        value_AccountingGroup = data_actual_posting[4]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[4]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[4]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[4]['BaseCurrencyAmount']
        value_Id = data_actual_posting[4]['Id']
        # 'postings' - verify value under array, item 5
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc, value_GLAccount)
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
        # 'account_balances' - get data actual
        data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # 'account_balances' - verify number items
        AU.assert_equals('Number item in account_balances', 1, len(data_account_balances))
        # 'account_balances' - verify key response under array item 1
        AU.assert_exists(expected_key['account_balances'], data_account_balances[0])
        # 'account_balances' - get value under array item 1
        value_account_balances_account_number = data_account_balances[0]['account_number']
        value_account_balances_amount = data_account_balances[0]['amount']
        value_account_balances_debit_or_credit = data_account_balances[0]['debit_or_credit']
        value_account_balances_currency = data_account_balances[0]['currency']
        value_account_balances_available_balance = data_account_balances[0]['available_balance']
        value_account_balances_transaction_number = data_account_balances[0]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[0]['transaction_date']
        value_account_balances_description = data_account_balances[0]['description']
        # 'account_balances' - verify value under array item 1  - (Decimal(str(amount_deposit_current)) - Decimal(str(minimum_deposit_amount_current)))
        AU.assert_equals('account_number', account_number_current, value_account_balances_account_number)
        AU.assert_equals('amount', Decimal(str(withdraw_amount_fund)), value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', deposit_currency, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(0)), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_06_sp_dpt_mwr_009_success_credit_accounting_not_same_branch(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='BSMMK0000'
        catalog_name='Bonus savings account  in MMK'
        deposit_type='Savings'
        deposit_sub_type='S2'
        minimum_deposit_amount=50000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_mdp['data']['account_number'])
        # STEP 04: miscellaneous withdrawal
        withdraw_amount=amount_deposit-minimum_deposit_amount
        accounting_amount=withdraw_amount
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number,
            withdraw_amount=withdraw_amount,
            credit_accounting=gl_account_not_same_branch,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # 'response' - verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_mwr'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_mwr_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_interest_earlywdr = data_actual['data']['interest_earlywdr']
        value_data_withdraw_amount = data_actual['data']['withdraw_amount']
        value_data_credit_accounting = data_actual['data']['credit_accounting']
        value_data_accounting_currency = data_actual['data']['accounting_currency']
        value_data_cross_rate = data_actual['data']['cross_rate']
        value_data_accounting_amount = data_actual['data']['accounting_amount']
        value_data_exchange_rate_of_accounting_bcy = data_actual['data']['exchange_rate_of_accounting_bcy']
        value_data_amount_equivalent_in_bcy = data_actual['data']['amount_equivalent_in_bcy']
        value_data_withdrawer_name = data_actual['data']['withdrawer_name']
        value_data_withdrawer_code = data_actual['data']['withdrawer_code']
        value_data_withdrawer_address = data_actual['data']['withdrawer_address']
        value_data_values_date = data_actual['data']['values_date']
        value_data_currency_of_deposit_account = data_actual['data']['currency_of_deposit_account']
        value_data_exchange_rate_debit_account_bcy = data_actual['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual['data']['amount_debit_account_bcy']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_code = data_actual['data']['branch_code']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_accounting = data_actual['data']['total_ifc_fee_accounting']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
        value_data_total_ifc_fee = data_actual['data']['total_ifc_fee']
        value_data_passbook_number = data_actual['data']['passbook_number']
        # value_data_account_balances = data_actual['data']['account_balances']
        value_data_auto_fund_trasfer = data_actual['data']['auto_fund_trasfer']
        value_data_transaction_code = data_actual['data']['transaction_code']
        value_data_transaction_number = data_actual['data']['transaction_number']
        value_data_transaction_type = data_actual['data']['transaction_type']
        value_data_sub_code = data_actual['data']['sub_code']
        value_data_transaction_date = data_actual['data']['transaction_date']
        value_data_service_sys_date = data_actual['data']['service_sys_date']
        value_data_reference_id = data_actual['data']['reference_id']
        value_data_ref_id = data_actual['data']['ref_id']
        value_data_reference_code = data_actual['data']['reference_code']
        value_data_business_code = data_actual['data']['business_code']
        value_data_value_date = data_actual['data']['value_date']
        value_data_current_user_code = data_actual['data']['current_user_code']
        value_data_current_branch_code = data_actual['data']['current_branch_code']
        value_data_current_username = data_actual['data']['current_username']
        value_data_current_loginname = data_actual['data']['current_loginname']
        value_data_user_approve = data_actual['data']['user_approve']
        value_data_status = data_actual['data']['status']
        value_data_is_reverse = data_actual['data']['is_reverse']
        value_data_amount1 = data_actual['data']['amount1']
        value_data_description = data_actual['data']['description']
        value_data_token = data_actual['data']['token']
        value_data_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
        value_data_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
        value_data_home = data_actual['data']['withdrawer_description']['home']
        value_data_office = data_actual['data']['withdrawer_description']['office']
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('interest_earlywdr', 0, value_data_interest_earlywdr)
        AU.assert_equals('withdraw_amount', withdraw_amount, value_data_withdraw_amount)
        AU.assert_equals('credit_accounting', gl_account_not_same_branch, value_data_credit_accounting)
        AU.assert_equals('accounting_currency', accounting_currency, value_data_accounting_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('accounting_amount', withdraw_amount, value_data_accounting_amount)
        AU.assert_equals('exchange_rate_of_accounting_bcy', 1, value_data_exchange_rate_of_accounting_bcy)
        AU.assert_equals('amount_equivalent_in_bcy', 0, value_data_amount_equivalent_in_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_code', customer_code_individual, value_data_withdrawer_code)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('currency_of_deposit_account', deposit_currency, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('account_linkage', '', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_code', branch_code, value_data_branch_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_accounting', 0, value_data_total_ifc_fee_accounting)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        AU.assert_equals('total_ifc_fee', 0, value_data_total_ifc_fee)
        AU.assert_empty('passbook_number', value_data_passbook_number)
        # AU.assert_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_MWR', value_data_transaction_code)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'MWR', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_MWR', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
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
        AU.assert_equals('is_reverse',  False, value_data_is_reverse)
        AU.assert_equals('amount1', 0, value_data_amount1)
        AU.assert_equals('description', '1122: Miscellaneous withdrawal', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        # 'postings' - verify key response
        AU.assert_equals('Number item in posting', 1, len(data_actual_posting))
        AU.assert_exists(expected_key['postings'], data_actual_posting[0])
        # 'postings' - get value under array
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
        # 'postings' - verify value under array
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
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
        # 'account_balances' - get data actual
        data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # 'account_balances' - verify number items
        AU.assert_equals('Number item in account_balances', 1, len(data_account_balances))
        # 'account_balances' - verify key response under array item 1
        AU.assert_exists(expected_key['account_balances'], data_account_balances[0])
        # 'account_balances' - get value under array item 1
        value_account_balances_account_number = data_account_balances[0]['account_number']
        value_account_balances_amount = data_account_balances[0]['amount']
        value_account_balances_debit_or_credit = data_account_balances[0]['debit_or_credit']
        value_account_balances_currency = data_account_balances[0]['currency']
        value_account_balances_available_balance = data_account_balances[0]['available_balance']
        value_account_balances_transaction_number = data_account_balances[0]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[0]['transaction_date']
        value_account_balances_description = data_account_balances[0]['description']
        # 'account_balances' - verify value under array item 1
        AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', deposit_currency, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)) - Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_06_sp_dpt_mwr_010_error_account_number_is_empty(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number='',
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'NotEmptyValidator\n', value_error_code)
        AU.assert_equals('error_message', 'Account number is required\nInvalid account number []', value_error_message)
        AU.assert_null('data', value_data)

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_06_sp_dpt_mwr_011_error_account_number_is_null(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number=None,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [account_number] violates IS_NULL rule.;', rs['description'])

    def test_06_sp_dpt_mwr_012_error_account_number_not_exist(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number='111111111111',
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_empty('error_code', value_error_code)
        AU.assert_equals('error_message', 'Invalid account number [111111111111]', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_013_error_account_status_closed(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_closed,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_empty('error_code', value_error_code)
        AU.assert_equals('error_message', 'Invalid account status [Closed]', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_014_error_account_status_block(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_block,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_empty('error_code', value_error_code)
        AU.assert_equals('error_message', 'Invalid account status [Block]', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_015_error_account_status_pending(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_pending,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_empty('error_code', value_error_code)
        AU.assert_equals('error_message', 'Invalid account status [Pending to approve]', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_016_error_account_status_new(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_new,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_empty('error_code', value_error_code)
        AU.assert_equals('error_message', 'Invalid account status [New]', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_017_error_fixed_deposit_account_status_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_fixed_deposit_normal,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'InvalidDpttype', value_error_code)
        AU.assert_equals('error_message', f'Invalid deposit type of account [{account_number_fixed_deposit_normal}]- en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_018_error_pepaid_fixed_deposit_account_status_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_prepaid_fixed_deposit_normal,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'InvalidDpttype', value_error_code)
        AU.assert_equals('error_message', f'Invalid deposit type of account [{account_number_prepaid_fixed_deposit_normal}]- en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_06_sp_dpt_mwr_019_error_withdrawal_amount_is_minus(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_normal,
            withdraw_amount=-withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=-accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [accounting_amount] violates Minimum rule: Minimum value is 0.00;Field [withdraw_amount] violates Minimum rule: Minimum value is 0.01;', rs['description'])

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_06_sp_dpt_mwr_020_error_withdrawal_amount_is_empty(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_normal,
            withdraw_amount='',
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount='',
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', "Input is invalid.Validate field [withdraw_amount]: value=[], datatype=[Number] with exception: [The input string '' was not in a correct format.].;", rs['description'])

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_06_sp_dpt_mwr_021_error_withdrawal_amount_is_zero(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_normal,
            withdraw_amount=0,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=0,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [withdraw_amount] violates Minimum rule: Minimum value is 0.01;', rs['description'])

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_06_sp_dpt_mwr_022_error_withdrawal_amount_is_null(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_normal,
            withdraw_amount=None,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=None,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [withdraw_amount] violates IS_NULL rule.;', rs['description'])

    def test_06_sp_dpt_mwr_023_error_withdrawal_amount_bigger_available_balance(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=9000000000
        accounting_amount=9000000000
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_normal,
            withdraw_amount=withdraw_amount,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'InvalidAvailableAmt', value_error_code)
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_current_normal}] of account. Available balance must be more than [9000000000] - en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_024_error_credit_accounting_is_empty(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_normal,
            withdraw_amount=withdraw_amount,
            credit_accounting='',
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'NotEmptyValidator', value_error_code)
        AU.assert_equals('error_message', 'Credit accounting is required', value_error_message)
        AU.assert_null('data', value_data)

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_06_sp_dpt_mwr_025_error_credit_accounting_is_null(self, user):
        sp_helper = StoredProcedureHelper(user)
        withdraw_amount=1000000.54
        accounting_amount=1000000.54
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_normal,
            withdraw_amount=withdraw_amount,
            credit_accounting=None,
            accounting_currency=accounting_currency,
            accounting_amount=accounting_amount,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [credit_accounting] violates IS_NULL rule.;', rs['description'])

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY
#     def test_06_sp_dpt_mwr_026_error_credit_accounting_not_exist(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MWR(
#             account_number=account_number_current_normal,
#             withdraw_amount=100,
#             credit_accounting='111111111111111111',
#             accounting_currency=accounting_currency,
#             accounting_amount=100,
#             withdrawer_name=account_name_individual,
#             withdrawer_code=customer_code_individual,
#             withdrawer_address=address,
#             values_date=values_date,
#             currency_of_deposit_account=deposit_currency,
#             branch_code=branch_code,
#             branch_name=branch_name
#         )
#         rs = sp_helper.DPT_MWR(fields_data)
#         step_code = 'DPT_MWR'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_actual['status'])
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
#     def test_06_sp_dpt_mwr_027_error_credit_accounting_posting_side_is_debit(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MWR(
#             account_number=account_number_current_normal,
#             withdraw_amount=100,
#             credit_accounting=gl_account_posting_side_debit,
#             accounting_currency=accounting_currency,
#             accounting_amount=100,
#             withdrawer_name=account_name_individual,
#             withdrawer_code=customer_code_individual,
#             withdrawer_address=address,
#             values_date=values_date,
#             currency_of_deposit_account=deposit_currency,
#             branch_code=branch_code,
#             branch_name=branch_name
#         )
#         rs = sp_helper.DPT_MWR(fields_data)
#         step_code = 'DPT_MWR'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_actual['status'])
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
#         AU.assert_equals('error_code', 'AccountNotAlowCreditBalance', value_error_code)
#         AU.assert_equals('error_message', f'Account [{gl_account_posting_side_debit}] is not allowed posting credit', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_028_error_credit_accounting_level_not_9(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_normal,
            withdraw_amount=100,
            credit_accounting=gl_account_level_07,
            accounting_currency=accounting_currency,
            accounting_amount=100,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
        # 'response' - get data actual
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_actual['status'])
        step_code = 'ACT_EXECUTE_POSTING'
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
        AU.assert_equals('error_code', 'record_not_found', value_error_code)
        AU.assert_equals('error_message', 'Foreign Exchange Account Definition [001 - AAA - MMK - I] doest not exist', value_error_message)
        AU.assert_null('data', value_data)
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_normal,
            withdraw_amount=100,
            credit_accounting=gl_account_level_08,
            accounting_currency=accounting_currency,
            accounting_amount=100,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
        # 'response' - get data actual
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_actual['status'])
        step_code = 'ACT_EXECUTE_POSTING'
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
        AU.assert_equals('error_code', 'ERROR', value_error_code)
        AU.assert_equals('error_message', 'An unexpected system error has occurred. Please contact support or check the system logs for more information.', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_029_error_credit_accounting_not_same_currency(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_normal,
            withdraw_amount=100,
            credit_accounting=gl_account_usd,
            accounting_currency='USD',
            accounting_amount=100,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', '', value_error_code)
        AU.assert_equals('error_message', 'Debit and credit currency must be the same', value_error_message)
        AU.assert_null('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY VI LAM LECH MASTER-DATAIL CUA CASH
#     def test_06_sp_dpt_mwr_030_error_credit_accounting_group_is_cash(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MWR(
#             account_number=account_number_current_normal,
#             withdraw_amount=100,
#             credit_accounting=gl_account_cash,
#             accounting_currency=accounting_currency,
#             accounting_amount=100,
#             withdrawer_name=account_name_individual,
#             withdrawer_code=customer_code_individual,
#             withdrawer_address=address,
#             values_date=values_date,
#             currency_of_deposit_account=deposit_currency,
#             branch_code=branch_code,
#             branch_name=branch_name
#         )
#         rs = sp_helper.DPT_MWR(fields_data)
#         step_code = 'DPT_MWR'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_actual['status'])
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
#         AU.assert_equals('error_message', f'GL [{gl_account_cash}] not allowed [Cash in Hand (MMK)] GL account number(Account group = [Cash])', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY
#     def test_06_sp_dpt_mwr_031_error_credit_accounting_direct_posting_is_no(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         fields_data = sp_payload.DPT_MWR(
#             account_number=account_number_current_normal,
#             withdraw_amount=100,
#             credit_accounting=gl_account_direct_posting_no,
#             accounting_currency=accounting_currency,
#             accounting_amount=100,
#             withdrawer_name=account_name_individual,
#             withdrawer_code=customer_code_individual,
#             withdrawer_address=address,
#             values_date=values_date,
#             currency_of_deposit_account=deposit_currency,
#             branch_code=branch_code,
#             branch_name=branch_name
#         )
#         rs = sp_helper.DPT_MWR(fields_data)
#         step_code = 'DPT_MWR'
#         # 'response' - get data actual
#         data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_actual, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_actual['status'])
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
#         AU.assert_equals('error_code', 'MasterNotAllowed', value_error_code)
#         AU.assert_equals('error_message', 'Accounting master is not allowed - en', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_032_error_saving_account_fund_transfer(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_saving_master=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve and deposit money to saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving_master = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving_master = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving_master,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving_master, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving_master,
            amount_deposit=amount_deposit_saving_master+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving_master, data_dpt_mdp['data']['account_number'])
        # STEP 02-01: open, approve and deposit money to saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_mdp['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" saving_master account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_saving_master,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_saving_master, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from saving_master account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_saving_master,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'InvalidAvailableAmt', value_error_code)
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_saving_master}] of account. Available balance must be more than [{withdraw_amount_fund}] - en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_033_error_current_account_fund_transfer_master_account_status_closed(self, user):
        sp_helper = StoredProcedureHelper(user)
        # amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open and close current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: close deposit account
        fields_data_cls = sp_payload.DPT_CLS(
            account_number=account_number_current,
            branch_name=branch_name,
            depositor_name=account_name_individual,
            depositor_id=customer_code_individual,
            depositor_address=address
        )
        rs = sp_helper.DPT_CLS(fields_data_cls)
        step_code = 'DPT_CLS'
        # 'response' - get data actual
        data_dpt_cls = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cls, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cls['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_cls['data']['account_number'])
        # STEP 02-01: open, approve and deposit money to saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_mdp['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', '', value_error_code)
        AU.assert_equals('error_message', 'Invalid account status [Closed]', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_034_error_current_account_fund_transfer_master_account_status_block(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve, deposit money and block current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_mdp['data']['account_number'])
        # STEP 01-04: block current account
        fields_data_blk = sp_payload.DPT_BLK(
            account_number=account_number_current,
            branch_name=branch_name,
            depositor_name=account_name_individual,
            depositor_id=customer_code_individual,
            depositor_address=address,
            depositor_currency=deposit_currency,
            value_date=user_service['working_date']
        )
        rs = sp_helper.DPT_BLK(fields_data_blk)
        step_code = 'DPT_BLK'
        # 'response' - get data actual
        data_dpt_blk = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_blk, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_blk['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_blk['data']['account_number'])
        # STEP 02-01: open, approve and deposit money to saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_mdp['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', '', value_error_code)
        AU.assert_equals('error_message', 'Invalid account status [Block]', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_035_error_current_account_fund_transfer_master_account_status_pending(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01: open current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02-01: open, approve and deposit money to saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_mdp['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', '', value_error_code)
        AU.assert_equals('error_message', 'Invalid account status [Pending to approve]', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_036_error_current_account_fund_transfer_master_account_status_new(self, user):
        sp_helper = StoredProcedureHelper(user)
        # amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=10000
        # STEP 01-01: open and approve current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 02-01: open, approve and deposit money to saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_mdp['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', '', value_error_code)
        AU.assert_equals('error_message', 'Invalid account status [New]', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_037_error_current_account_fund_transfer_master_account_status_dormant(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve, deposit money and change status current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_mdp['data']['account_number'])
        # STEP 01-04: change status from 'Normal' to 'Dormant' of current account
        fields_data_cas = sp_payload.DPT_CAS(
            account_number=account_number_current,
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
        AU.assert_equals('account_number', account_number_current, data_dpt_cas['data']['account_number'])
        # STEP 02-01: open, approve and deposit money to saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_mdp['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'ApprovalRequired', value_error_code)
        AU.assert_equals('error_message', 'ApprovalRequired', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_038_error_current_account_fund_transfer_link_account_is_current(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current_master=100000
        amount_deposit_current=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve and deposit money to current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current_master = data_dpt_opn['data']['account_number']
        gl_account_deposit_current_master = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current_master,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current_master, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current_master,
            amount_deposit=amount_deposit_current_master+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current_master, data_dpt_mdp['data']['account_number'])
        # STEP 02-01: open, approve and deposit money to current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_mdp['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current_master account and current account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current_master,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_current,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current_master, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_current, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current_master account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current_master,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name,
            account_linkage=account_number_current
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'InvalidAvailableAmt', value_error_code)
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_current_master}] of account. Available balance must be more than [{withdraw_amount_fund}] - en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_039_error_current_account_fund_transfer_link_account_status_closed(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve and deposit money to current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_mdp['data']['account_number'])
        # STEP 02-01: open and close saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02-02: close deposit account
        fields_data_cls = sp_payload.DPT_CLS(
            account_number=account_number_saving,
            branch_name=branch_name,
            depositor_name=account_name_individual,
            depositor_id=customer_code_individual,
            depositor_address=address
        )
        rs = sp_helper.DPT_CLS(fields_data_cls)
        step_code = 'DPT_CLS'
        # 'response' - get data actual
        data_dpt_cls = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cls, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cls['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_cls['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', '', value_error_code)
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_current}] of account. Available balance must be more than [{withdraw_amount_fund}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_040_error_current_account_fund_transfer_link_account_status_block(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve and deposit money to current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_mdp['data']['account_number'])
        # STEP 02-01: open, approve and deposit money to saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 02-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_mdp['data']['account_number'])
        # STEP 02-04: block saving account
        fields_data_blk = sp_payload.DPT_BLK(
            account_number=account_number_saving,
            branch_name=branch_name,
            depositor_name=account_name_individual,
            depositor_id=customer_code_individual,
            depositor_address=address,
            depositor_currency=deposit_currency,
            value_date=user_service['working_date']
        )
        rs = sp_helper.DPT_BLK(fields_data_blk)
        step_code = 'DPT_BLK'
        # 'response' - get data actual
        data_dpt_blk = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_blk, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_blk['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_blk['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'InvalidAvailableAmt', value_error_code)
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_current}] of account. Available balance must be more than [{withdraw_amount_fund}] - en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_06_sp_dpt_mwr_041_error_current_account_fund_transfer_link_account_status_pending(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve and deposit money to current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_mdp['data']['account_number'])
        # STEP 02: open saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', '', value_error_code)
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_current}] of account. Available balance must be more than [{withdraw_amount_fund}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_042_error_current_account_fund_transfer_link_account_status_new(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve and deposit money to current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_mdp['data']['account_number'])
        # STEP 02-01: open and approve saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', '', value_error_code)
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_current}] of account. Available balance must be more than [{withdraw_amount_fund}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_06_sp_dpt_mwr_043_error_current_account_fund_transfer_link_account_status_dormant(self, user):
        sp_helper = StoredProcedureHelper(user)
        amount_deposit_current=100000
        amount_deposit_saving=100000
        withdraw_amount_fund=150000
        # STEP 01-01: open, approve and deposit money to current account
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_current = data_dpt_opn['data']['account_number']
        gl_account_deposit_current = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 01-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 01-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_mdp['data']['account_number'])
        # STEP 02-01: open, approve, deposit money and change status of saving account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        fields_data_opn = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            deposit_sub_type=deposit_sub_type
        )
        rs = sp_helper.DPT_OPN(fields_data_opn)
        step_code = 'DPT_OPN'
        # 'response' - get data actual
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number_saving = data_dpt_opn['data']['account_number']
        gl_account_deposit_saving = data_dpt_opn['data']['account_chart_number'][0]
        # STEP 02-02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_saving,
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_apr['data']['account_number'])
        # STEP 02-03: miscellaneous deposit to deposit status 'New'
        fields_data_mdp = sp_payload.DPT_MDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving+minimum_deposit_amount,
            debit_accounting=debit_accounting_valid,
            branch_name=branch_name,
            accounting_currency=accounting_currency,
            depositor_name=account_name_individual,
            depositor_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            deposit_currency=deposit_currency,
            accounting_currency1=accounting_currency1
        )
        rs = sp_helper.DPT_MDP(fields_data_mdp)
        step_code = 'DPT_MDP'
        # 'response' - get data actual
        data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_mdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_mdp['data']['account_number'])
        # STEP 02-04: change status 'Normal' to 'Dormant' of saving account
        fields_data_cas = sp_payload.DPT_CAS(
            account_number=account_number_saving,
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
        AU.assert_equals('account_number', account_number_saving, data_dpt_cas['data']['account_number'])
        # STEP 03: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number_current,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=branch_code
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number_current, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 04: miscellaneous withdrawal from current account
        fields_data = sp_payload.DPT_MWR(
            account_number=account_number_current,
            withdraw_amount=withdraw_amount_fund,
            credit_accounting=credit_accounting_valid,
            accounting_currency=accounting_currency,
            accounting_amount=withdraw_amount_fund,
            withdrawer_name=account_name_individual,
            withdrawer_code=customer_code_individual,
            withdrawer_address=address,
            values_date=values_date,
            currency_of_deposit_account=deposit_currency,
            branch_code=branch_code,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_MWR(fields_data)
        step_code = 'DPT_MWR'
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
        AU.assert_equals('error_code', 'InvalidAvailableAmt', value_error_code)
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_current}] of account. Available balance must be more than [{withdraw_amount_fund}] - en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)
