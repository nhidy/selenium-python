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
amount_deposit=10000000.45
cash_currency='MMK'
branch_name='003 - Bayint Naung Branch'
address='Home, Street, Ward, Township'
values_date=user_service['working_date']
id_issue_date=user_service['working_date']
value_date=user_service['working_date']
currency_deposit='MMK'
# data test cash withdraw valid
withdraw_amount=100000.45
currency_of_deposit_account='MMK'
gl_account_cash='003101030100010101'

# # data test trên 104
# to_account_number_saving_single_valid='310035109637'
# # data test invalid
# account_number_closed='340034919619'
# account_number_block='310033187741'
# account_number_pending='310030475906'
# account_number_new='310030730191'
# account_number_current_normal='110031370833'
# account_number_fixed_deposit_normal='430030589898'
# account_number_prepaid_fixed_deposit_normal='460030177172'
# step_code_cash='CSH_UPDATE_CASH'

# data test trên 198
to_account_number_saving_single_valid='310034460838'
# data test invalid
account_number_closed='330038446405'
account_number_block='330038600106'
account_number_pending='310030394362'
account_number_new='310031442402'
account_number_current_normal='110030077368'
account_number_fixed_deposit_normal='430030879304'
account_number_prepaid_fixed_deposit_normal='460031072430'
step_code_cash='CSH_UPDATE_CASH_SP'

@pytest.fixture(scope='session')
def user():
    req = RU(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_CWR
class Test_SP_DPT_CWR(object):

    def test_05_sp_dpt_cwr_001_success_saving_account_status_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='BSMMK0000'
        catalog_name='Bonus savings account  in MMK'
        deposit_type='Savings'
        deposit_sub_type='S2'
        minimum_deposit_amount=50000
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
        # STEP 03: cash deposit for deposit status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_deposit
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, data_dpt_cdp['data']['account_number'])
        # STEP 04: cash withdrawal
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_approved,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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
        AU.assert_exists(expected_key['data_dpt_cwr'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_cwr_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_customer_code = data_actual['data']['customer_code']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_withdraw_amount = data_actual['data']['withdraw_amount']
        value_data_cash_currency = data_actual['data']['cash_currency']
        value_data_cross_rate = data_actual['data']['cross_rate']
        value_data_cash_amount = data_actual['data']['cash_amount']
        value_data_exchange_rate = data_actual['data']['exchange_rate']
        value_data_cash_amount_bcy = data_actual['data']['cash_amount_bcy']
        value_data_withdrawer_name = data_actual['data']['withdrawer_name']
        value_data_withdrawer_id = data_actual['data']['withdrawer_id']
        value_data_withdrawer_address = data_actual['data']['withdrawer_address']
        value_data_home = data_actual['data']['withdrawer_description']['home']
        value_data_office = data_actual['data']['withdrawer_description']['office']
        value_data_id_issue_date = data_actual['data']['id_issue_date']
        value_data_id_place = data_actual['data']['id_place']
        value_data_identification_number = data_actual['data']['identification_number']
        value_data_currency_of_deposit_account = data_actual['data']['currency_of_deposit_account']
        value_data_exchange_rate_debit_account_bcy = data_actual['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual['data']['amount_debit_account_bcy']
        value_data_interest_from_earlywdr = data_actual['data']['interest_from_earlywdr']
        value_data_due_date = data_actual['data']['due_date']
        value_data_commission = data_actual['data']['commission']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_total_vat_for_cash = data_actual['data']['total_vat_for_cash']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_total_ifc_fee_cash = data_actual['data']['total_ifc_fee_cash']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
        value_data_total_ifc_fee = data_actual['data']['total_ifc_fee']
        # value_data_fee_currency_code = data_actual['data']['fee_currency_code']
        value_data_passbook_number = data_actual['data']['passbook_number']
        value_data_fee_data = data_actual['data']['fee_data']
        # value_data_account_balances = data_actual['data']['account_balances']
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
        # verify value of key response in 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('customer_code', customer_code_individual, value_data_customer_code)
        AU.assert_equals('current_balance', None, value_data_current_balance)
        AU.assert_equals('available_balance', None, value_data_available_balance)
        AU.assert_equals('withdraw_amount', withdraw_amount, value_data_withdraw_amount)
        AU.assert_equals('cash_currency', cash_currency, value_data_cash_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('cash_amount', 0.0, value_data_cash_amount)
        AU.assert_equals('exchange_rate', 1.0, value_data_exchange_rate)
        AU.assert_equals('cash_amount_bcy', 0.0, value_data_cash_amount_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_id', customer_code_individual, value_data_withdrawer_id)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_equals('home', None, value_data_home)
        AU.assert_equals('office', None, value_data_office)
        AU.assert_equals('id_issue_date', id_issue_date, value_data_id_issue_date)
        AU.assert_equals('id_place', '', value_data_id_place)
        AU.assert_equals('identification_number', '', value_data_identification_number)
        AU.assert_equals('currency_of_deposit_account', currency_of_deposit_account, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('interest_from_earlywdr', 0.0, value_data_interest_from_earlywdr)
        AU.assert_equals('due_date', '', value_data_due_date)
        AU.assert_equals('commission', 0.0, value_data_commission)
        AU.assert_equals('interest_prepaid', 0.0, value_data_interest_prepaid)
        AU.assert_equals('total_vat_for_cash', 0.0, value_data_total_vat_for_cash)
        AU.assert_equals('account_linkage', '', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0.0, value_data_amount_linkage)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('total_ifc_fee_cash', 0.0, value_data_total_ifc_fee_cash)
        AU.assert_equals('total_ifc_fee_deposit', 0.0, value_data_total_ifc_fee_deposit)
        AU.assert_equals('total_ifc_fee', 0.0, value_data_total_ifc_fee)
        # AU.assert_equals('fee_currency_code', None, value_data_fee_currency_code)
        AU.assert_equals('passbook_number', '', value_data_passbook_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        # AU.assert_not_null('account_balances', value_data_account_balances)
        AU.assert_equals('transaction_code', 'DPT_CWR', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'CWR', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_CWR', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_equals('reference_code', '', value_data_reference_code)
        AU.assert_equals('business_code', '', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_equals('user_approve', '', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_equals('is_reverse', False, value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1120: Cash withdrawal', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse', False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated', False, value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
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
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        # data_account_balances = data_actual['data']['account_balances']
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
        AU.assert_equals('account_number', account_number_approved, value_account_balances_account_number)
        AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit))-Decimal(str(minimum_deposit_amount))-Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # verify step CASH
        step_code = step_code_cash
        # 'response' - get data actual - step CASH
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
        AU.assert_exists(expected_key['data_step_cash'], data_actual['data'])
        # 'response' - get value under 'data'
        value_data_step_cash_list_cash = data_actual['data']['list_cash']
        value_data_step_cash_list_cash_from_response = data_actual['data']['list_cash_from_response']
        value_data_step_cash_transaction_code = data_actual['data']['transaction_code']
        value_data_step_cash_transaction_number = data_actual['data']['transaction_number']
        value_data_step_cash_transaction_type = data_actual['data']['transaction_type']
        value_data_step_cash_sub_code = data_actual['data']['sub_code']
        value_data_step_cash_transaction_date = data_actual['data']['transaction_date']
        value_data_step_cash_service_sys_date = data_actual['data']['service_sys_date']
        value_data_step_cash_reference_id = data_actual['data']['reference_id']
        value_data_step_cash_ref_id = data_actual['data']['ref_id']
        value_data_step_cash_reference_code = data_actual['data']['reference_code']
        value_data_step_cash_business_code = data_actual['data']['business_code']
        value_data_step_cash_value_date = data_actual['data']['value_date']
        value_data_step_cash_current_user_code = data_actual['data']['current_user_code']
        value_data_step_cash_current_branch_code = data_actual['data']['current_branch_code']
        value_data_step_cash_current_username = data_actual['data']['current_username']
        value_data_step_cash_current_loginname = data_actual['data']['current_loginname']
        value_data_step_cash_user_approve = data_actual['data']['user_approve']
        value_data_step_cash_status = data_actual['data']['status']
        value_data_step_cash_is_reverse = data_actual['data']['is_reverse']
        value_data_step_cash_amount1 = data_actual['data']['amount1']
        value_data_step_cash_description = data_actual['data']['description']
        value_data_step_cash_token = data_actual['data']['token']
        value_data_step_cash_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
        value_data_step_cash_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_not_equals('list_cash', [], value_data_step_cash_list_cash)
        AU.assert_not_empty('list_cash', [], value_data_step_cash_list_cash)
        AU.assert_equals('list_cash_from_response', [], value_data_step_cash_list_cash_from_response)
        AU.assert_equals('transaction_code', 'DPT_CWR', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'CWR', value_data_step_cash_transaction_type)
        AU.assert_equals('sub_code', step_code_cash, value_data_step_cash_sub_code)
        AU.assert_not_null('transaction_date', value_data_step_cash_transaction_date)
        AU.assert_not_empty('transaction_date', value_data_step_cash_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_step_cash_service_sys_date)
        AU.assert_not_empty('service_sys_date', value_data_step_cash_service_sys_date)
        AU.assert_not_null('reference_id', value_data_step_cash_reference_id)
        AU.assert_not_empty('reference_id', value_data_step_cash_reference_id)
        AU.assert_not_null('ref_id', value_data_step_cash_ref_id)
        AU.assert_not_empty('ref_id', value_data_step_cash_ref_id)
        AU.assert_empty('reference_code', value_data_step_cash_reference_code)
        AU.assert_empty('business_code', value_data_step_cash_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_step_cash_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_step_cash_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_step_cash_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_step_cash_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_step_cash_current_loginname)
        AU.assert_empty('user_approve', value_data_step_cash_user_approve)
        AU.assert_equals('status', 'N', value_data_step_cash_status)
        AU.assert_equals('is_reverse',  False, value_data_step_cash_is_reverse)
        AU.assert_equals('amount1', 0, value_data_step_cash_amount1)
        AU.assert_equals('description', '1120: Cash withdrawal', value_data_step_cash_description)
        AU.assert_equals('token', '*', value_data_step_cash_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_step_cash_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_step_cash_is_transaction_compensated)
        # 'response' - verify item under 'data' and 'list_cash'
        AU.assert_equals('Number item in list_cash', 2, len(data_actual['data']['list_cash']))
        # 'response' - verify key response under 'data' and 'list_cash', item 1
        AU.assert_exists(expected_key['data_list_cash'], data_actual['data']['list_cash'][0])
        # 'response' - get value under 'data' and 'list_cash', item 1
        value_list_cash_amount_cash_change = data_actual['data']['list_cash'][0]['amount_cash_change']
        value_list_cash_base_amount = data_actual['data']['list_cash'][0]['base_amount']
        value_list_cash_debit_or_credit = data_actual['data']['list_cash'][0]['debit_or_credit']
        value_list_cash_currency_code = data_actual['data']['list_cash'][0]['currency_code']
        value_list_cash_condition = data_actual['data']['list_cash'][0]['condition']
        value_list_cash_posting = data_actual['data']['list_cash'][0]['posting']
        value_list_cash_accounting_group = data_actual['data']['list_cash'][0]['accounting_group']
        value_list_cash_transaction_code = data_actual['data']['list_cash'][0]['transaction_code']
        value_list_cash_transaction_number = data_actual['data']['list_cash'][0]['transaction_number']
        value_list_cash_transaction_type = data_actual['data']['list_cash'][0]['transaction_type']
        value_list_cash_sub_code = data_actual['data']['list_cash'][0]['sub_code']
        value_list_cash_transaction_date = data_actual['data']['list_cash'][0]['transaction_date']
        value_list_cash_service_sys_date = data_actual['data']['list_cash'][0]['service_sys_date']
        value_list_cash_reference_id = data_actual['data']['list_cash'][0]['reference_id']
        value_list_cash_ref_id = data_actual['data']['list_cash'][0]['ref_id']
        value_list_cash_reference_code = data_actual['data']['list_cash'][0]['reference_code']
        value_list_cash_business_code = data_actual['data']['list_cash'][0]['business_code']
        value_list_cash_value_date = data_actual['data']['list_cash'][0]['value_date']
        value_list_cash_current_user_code = data_actual['data']['list_cash'][0]['current_user_code']
        value_list_cash_current_branch_code = data_actual['data']['list_cash'][0]['current_branch_code']
        value_list_cash_current_username = data_actual['data']['list_cash'][0]['current_username']
        value_list_cash_current_loginname = data_actual['data']['list_cash'][0]['current_loginname']
        value_list_cash_user_approve = data_actual['data']['list_cash'][0]['user_approve']
        value_list_cash_status = data_actual['data']['list_cash'][0]['status']
        value_list_cash_is_reverse = data_actual['data']['list_cash'][0]['is_reverse']
        value_list_cash_amount1 = data_actual['data']['list_cash'][0]['amount1']
        value_list_cash_description = data_actual['data']['list_cash'][0]['description']
        value_list_cash_token = data_actual['data']['list_cash'][0]['token']
        value_list_cash_is_transaction_reverse = data_actual['data']['list_cash'][0]['is_transaction_reverse']
        value_list_cash_is_transaction_compensated = data_actual['data']['list_cash'][0]['is_transaction_compensated']
        # 'response' - verify value under 'data' and 'list_cash', item 1
        AU.assert_equals('amount_cash_change', withdraw_amount, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'C', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', None, value_list_cash_condition)
        AU.assert_equals('posting', False, value_list_cash_posting)
        AU.assert_equals('accounting_group', 1, value_list_cash_accounting_group)
        AU.assert_null('transaction_code', value_list_cash_transaction_code)
        AU.assert_null('transaction_number', value_list_cash_transaction_number)
        AU.assert_null('transaction_type', value_list_cash_transaction_type)
        AU.assert_null('sub_code', value_list_cash_sub_code)
        AU.assert_equals('transaction_date', '0001-01-01T00:00:00', value_list_cash_transaction_date)
        AU.assert_equals('service_sys_date', '0001-01-01T00:00:00', value_list_cash_service_sys_date)
        AU.assert_null('reference_id', value_list_cash_reference_id)
        AU.assert_null('ref_id', value_list_cash_ref_id)
        AU.assert_null('reference_code', value_list_cash_reference_code)
        AU.assert_null('business_code', value_list_cash_business_code)
        AU.assert_equals('value_date', '0001-01-01T00:00:00', value_list_cash_value_date)
        AU.assert_null('current_user_code', value_list_cash_current_user_code)
        AU.assert_null('current_branch_code', value_list_cash_current_branch_code)
        AU.assert_null('current_username', value_list_cash_current_username)
        AU.assert_null('current_loginname', value_list_cash_current_loginname)
        AU.assert_null('user_approve', value_list_cash_user_approve)
        AU.assert_null('status', value_list_cash_status)
        AU.assert_equals('is_reverse', False, value_list_cash_is_reverse)
        AU.assert_equals('amount1', 0, value_list_cash_amount1)
        AU.assert_null('description', value_list_cash_description)
        AU.assert_null('token', value_list_cash_token)
        AU.assert_equals('is_transaction_reverse', False, value_list_cash_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated', False, value_list_cash_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'list_cash', item 2
        AU.assert_exists(expected_key['data_list_cash'], data_actual['data']['list_cash'][1])
        # 'response' - get value under 'data' and 'list_cash', item 2
        value_list_cash_amount_cash_change = data_actual['data']['list_cash'][1]['amount_cash_change']
        value_list_cash_base_amount = data_actual['data']['list_cash'][1]['base_amount']
        value_list_cash_debit_or_credit = data_actual['data']['list_cash'][1]['debit_or_credit']
        value_list_cash_currency_code = data_actual['data']['list_cash'][1]['currency_code']
        value_list_cash_condition = data_actual['data']['list_cash'][1]['condition']
        value_list_cash_posting = data_actual['data']['list_cash'][1]['posting']
        value_list_cash_accounting_group = data_actual['data']['list_cash'][1]['accounting_group']
        value_list_cash_transaction_code = data_actual['data']['list_cash'][1]['transaction_code']
        value_list_cash_transaction_number = data_actual['data']['list_cash'][1]['transaction_number']
        value_list_cash_transaction_type = data_actual['data']['list_cash'][1]['transaction_type']
        value_list_cash_sub_code = data_actual['data']['list_cash'][1]['sub_code']
        value_list_cash_transaction_date = data_actual['data']['list_cash'][1]['transaction_date']
        value_list_cash_service_sys_date = data_actual['data']['list_cash'][1]['service_sys_date']
        value_list_cash_reference_id = data_actual['data']['list_cash'][1]['reference_id']
        value_list_cash_ref_id = data_actual['data']['list_cash'][1]['ref_id']
        value_list_cash_reference_code = data_actual['data']['list_cash'][1]['reference_code']
        value_list_cash_business_code = data_actual['data']['list_cash'][1]['business_code']
        value_list_cash_value_date = data_actual['data']['list_cash'][1]['value_date']
        value_list_cash_current_user_code = data_actual['data']['list_cash'][1]['current_user_code']
        value_list_cash_current_branch_code = data_actual['data']['list_cash'][1]['current_branch_code']
        value_list_cash_current_username = data_actual['data']['list_cash'][1]['current_username']
        value_list_cash_current_loginname = data_actual['data']['list_cash'][1]['current_loginname']
        value_list_cash_user_approve = data_actual['data']['list_cash'][1]['user_approve']
        value_list_cash_status = data_actual['data']['list_cash'][1]['status']
        value_list_cash_is_reverse = data_actual['data']['list_cash'][1]['is_reverse']
        value_list_cash_amount1 = data_actual['data']['list_cash'][1]['amount1']
        value_list_cash_description = data_actual['data']['list_cash'][1]['description']
        value_list_cash_token = data_actual['data']['list_cash'][1]['token']
        value_list_cash_is_transaction_reverse = data_actual['data']['list_cash'][1]['is_transaction_reverse']
        value_list_cash_is_transaction_compensated = data_actual['data']['list_cash'][1]['is_transaction_compensated']
        # 'response' - verify value under 'data' and 'list_cash', item 2
        AU.assert_equals('amount_cash_change', 0, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', None, value_list_cash_condition)
        AU.assert_equals('posting', False, value_list_cash_posting)
        AU.assert_equals('accounting_group', 2, value_list_cash_accounting_group)
        AU.assert_null('transaction_code', value_list_cash_transaction_code)
        AU.assert_null('transaction_number', value_list_cash_transaction_number)
        AU.assert_null('transaction_type', value_list_cash_transaction_type)
        AU.assert_null('sub_code', value_list_cash_sub_code)
        AU.assert_equals('transaction_date', '0001-01-01T00:00:00', value_list_cash_transaction_date)
        AU.assert_equals('service_sys_date', '0001-01-01T00:00:00', value_list_cash_service_sys_date)
        AU.assert_null('reference_id', value_list_cash_reference_id)
        AU.assert_null('ref_id', value_list_cash_ref_id)
        AU.assert_null('reference_code', value_list_cash_reference_code)
        AU.assert_null('business_code', value_list_cash_business_code)
        AU.assert_equals('value_date', '0001-01-01T00:00:00', value_list_cash_value_date)
        AU.assert_null('current_user_code', value_list_cash_current_user_code)
        AU.assert_null('current_branch_code', value_list_cash_current_branch_code)
        AU.assert_null('current_username', value_list_cash_current_username)
        AU.assert_null('current_loginname', value_list_cash_current_loginname)
        AU.assert_null('user_approve', value_list_cash_user_approve)
        AU.assert_null('status', value_list_cash_status)
        AU.assert_equals('is_reverse', False, value_list_cash_is_reverse)
        AU.assert_equals('amount1', 0, value_list_cash_amount1)
        AU.assert_null('description', value_list_cash_description)
        AU.assert_null('token', value_list_cash_token)
        AU.assert_equals('is_transaction_reverse', False, value_list_cash_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated', False, value_list_cash_is_transaction_compensated)
        # 'postings' - get data actual - step CASH
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        AU.assert_equals('Number item in posting', 2, len(data_actual_posting))
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
        AU.assert_not_empty('TransactionNumber', value_TransactionNumber)
        AU.assert_not_null('TransactionNumber', value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_not_empty('TransactionNumber', value_TransactionNumber)
        AU.assert_not_null('TransactionNumber', value_TransactionNumber)
        AU.assert_equals('TransTableName', 'CashList', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'CASH', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_cash, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # # 'account_balances' - get data actual - step CASH
        # data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        # print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # # 'account_balances' - verify number items
        # AU.assert_equals('Number item in account_balances', 1, len(data_account_balances))
        # # 'account_balances' - verify key response under array item 1
        # AU.assert_exists(expected_key['account_balances'], data_account_balances[0])
        # # 'account_balances' - get value under array item 1
        # value_account_balances_account_number = data_account_balances[0]['account_number']
        # value_account_balances_amount = data_account_balances[0]['amount']
        # value_account_balances_debit_or_credit = data_account_balances[0]['debit_or_credit']
        # value_account_balances_currency = data_account_balances[0]['currency']
        # value_account_balances_available_balance = data_account_balances[0]['available_balance']
        # value_account_balances_transaction_number = data_account_balances[0]['transaction_number']
        # value_account_balances_transaction_date = data_account_balances[0]['transaction_date']
        # value_account_balances_description = data_account_balances[0]['description']
        # # 'account_balances' - verify value under array item 1
        # AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        # AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        # AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        # AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        # AU.assert_equals('available_balance', Decimal(str(amount_deposit))-Decimal(str(minimum_deposit_amount))-Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        # AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        # AU.assert_equals('description', value_data_description, value_account_balances_description)

    def test_05_sp_dpt_cwr_002_success_saving_account_status_normal_add_fee(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='PSMMK0000'
        catalog_name='Premier savings deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S3'
        minimum_deposit_amount=50000
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
        # STEP 03: cash deposit for deposit status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_deposit
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, data_dpt_cdp['data']['account_number'])
        # STEP 04: cash withdrawal
        total_fee=600.0
        share_fee_01=0.0
        ifc_name_01='Withdrawal (MMK) For Same Region  (By Cash)'
        value_type_01='F'
        ifc_code_01=308
        payrate_01=100
        ifc_value_01=100.0
        ifc_amount_01=100.0
        currency_account_code_01=currency_of_deposit_account
        floor_value_01=0.0
        ceiling_value_01=0.0
        share_rate_01=0.0
        share_amount_01=0.0
        round_rate_01=0.0
        round_amount_01=0.0
        currency_fee_code_01=currency_of_deposit_account
        pay_source_01='CSH'
        gl_account_ifcc_01='003303030100010101'
        share_fee_02=0.0
        ifc_name_02='Withdrawal (MMK) For Same Region(By Cash)(Postage & Fax Charges)'
        value_type_02='F'
        ifc_code_02=342
        payrate_02=100
        ifc_value_02=500.0
        ifc_amount_02=500.0
        currency_account_code_02=currency_of_deposit_account
        floor_value_02=0.0
        ceiling_value_02=0.0
        share_rate_02=0.0
        share_amount_02=0.0
        round_rate_02=0.0
        round_amount_02=0.0
        currency_fee_code_02=currency_of_deposit_account
        pay_source_02='CSH'
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
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_approved,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            commission=total_fee,
            fee_data=fee_data
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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
        AU.assert_exists(expected_key['data_dpt_cwr'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_cwr_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_customer_code = data_actual['data']['customer_code']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_withdraw_amount = data_actual['data']['withdraw_amount']
        value_data_cash_currency = data_actual['data']['cash_currency']
        value_data_cross_rate = data_actual['data']['cross_rate']
        value_data_cash_amount = data_actual['data']['cash_amount']
        value_data_exchange_rate = data_actual['data']['exchange_rate']
        value_data_cash_amount_bcy = data_actual['data']['cash_amount_bcy']
        value_data_withdrawer_name = data_actual['data']['withdrawer_name']
        value_data_withdrawer_id = data_actual['data']['withdrawer_id']
        value_data_withdrawer_address = data_actual['data']['withdrawer_address']
        value_data_home = data_actual['data']['withdrawer_description']['home']
        value_data_office = data_actual['data']['withdrawer_description']['office']
        value_data_id_issue_date = data_actual['data']['id_issue_date']
        value_data_id_place = data_actual['data']['id_place']
        value_data_identification_number = data_actual['data']['identification_number']
        value_data_currency_of_deposit_account = data_actual['data']['currency_of_deposit_account']
        value_data_exchange_rate_debit_account_bcy = data_actual['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual['data']['amount_debit_account_bcy']
        value_data_interest_from_earlywdr = data_actual['data']['interest_from_earlywdr']
        value_data_due_date = data_actual['data']['due_date']
        value_data_commission = data_actual['data']['commission']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_total_vat_for_cash = data_actual['data']['total_vat_for_cash']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_total_ifc_fee_cash = data_actual['data']['total_ifc_fee_cash']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
        value_data_total_ifc_fee = data_actual['data']['total_ifc_fee']
        value_data_fee_currency_code = data_actual['data']['fee_currency_code']
        value_data_passbook_number = data_actual['data']['passbook_number']
        value_data_fee_data = data_actual['data']['fee_data']
        # value_data_account_balances = data_actual['data']['account_balances']
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
        # 'response' - verify value of key response in 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('customer_code', customer_code_individual, value_data_customer_code)
        AU.assert_equals('current_balance', None, value_data_current_balance)
        AU.assert_equals('available_balance', None, value_data_available_balance)
        AU.assert_equals('withdraw_amount', withdraw_amount, value_data_withdraw_amount)
        AU.assert_equals('cash_currency', cash_currency, value_data_cash_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('cash_amount', 0, value_data_cash_amount)
        AU.assert_equals('exchange_rate', 1, value_data_exchange_rate)
        AU.assert_equals('cash_amount_bcy', 0, value_data_cash_amount_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_id', customer_code_individual, value_data_withdrawer_id)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_equals('home', None, value_data_home)
        AU.assert_equals('office', None, value_data_office)
        AU.assert_equals('id_issue_date', id_issue_date, value_data_id_issue_date)
        AU.assert_equals('id_place', '', value_data_id_place)
        AU.assert_equals('identification_number', '', value_data_identification_number)
        AU.assert_equals('currency_of_deposit_account', currency_of_deposit_account, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('interest_from_earlywdr', 0, value_data_interest_from_earlywdr)
        AU.assert_equals('due_date', '', value_data_due_date)
        AU.assert_equals('commission', total_fee, value_data_commission)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('total_vat_for_cash', 0, value_data_total_vat_for_cash)
        AU.assert_equals('account_linkage', '', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('total_ifc_fee_cash', total_fee, value_data_total_ifc_fee_cash)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        AU.assert_equals('total_ifc_fee', total_fee, value_data_total_ifc_fee)
        AU.assert_equals('fee_currency_code', currency_of_deposit_account, value_data_fee_currency_code)
        AU.assert_equals('passbook_number', '', value_data_passbook_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_not_null('fee_data', value_data_fee_data)
        # AU.assert_not_null('account_balances', value_data_account_balances)
        AU.assert_equals('transaction_code', 'DPT_CWR', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'CWR', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_CWR', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date',  value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_equals('reference_code', '', value_data_reference_code)
        AU.assert_equals('business_code', '', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_equals('user_approve', '', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_equals('is_reverse', False, value_data_is_reverse)
        AU.assert_equals('amount1', 0, value_data_amount1)
        AU.assert_equals('description', '1120: Cash withdrawal', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse', False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated', False, value_data_is_transaction_compensated)
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
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        # data_account_balances = data_actual['data']['account_balances']
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
        AU.assert_equals('account_number', account_number_approved, value_account_balances_account_number)
        AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit))-Decimal(str(minimum_deposit_amount))-Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # verify step CASH
        step_code = step_code_cash
        # 'response' - get data actual - step CASH
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
        AU.assert_exists(expected_key['data_step_cash'], data_actual['data'])
        # 'response' - get value under 'data'
        value_data_step_cash_list_cash = data_actual['data']['list_cash']
        value_data_step_cash_list_cash_from_response = data_actual['data']['list_cash_from_response']
        value_data_step_cash_transaction_code = data_actual['data']['transaction_code']
        value_data_step_cash_transaction_number = data_actual['data']['transaction_number']
        value_data_step_cash_transaction_type = data_actual['data']['transaction_type']
        value_data_step_cash_sub_code = data_actual['data']['sub_code']
        value_data_step_cash_transaction_date = data_actual['data']['transaction_date']
        value_data_step_cash_service_sys_date = data_actual['data']['service_sys_date']
        value_data_step_cash_reference_id = data_actual['data']['reference_id']
        value_data_step_cash_ref_id = data_actual['data']['ref_id']
        value_data_step_cash_reference_code = data_actual['data']['reference_code']
        value_data_step_cash_business_code = data_actual['data']['business_code']
        value_data_step_cash_value_date = data_actual['data']['value_date']
        value_data_step_cash_current_user_code = data_actual['data']['current_user_code']
        value_data_step_cash_current_branch_code = data_actual['data']['current_branch_code']
        value_data_step_cash_current_username = data_actual['data']['current_username']
        value_data_step_cash_current_loginname = data_actual['data']['current_loginname']
        value_data_step_cash_user_approve = data_actual['data']['user_approve']
        value_data_step_cash_status = data_actual['data']['status']
        value_data_step_cash_is_reverse = data_actual['data']['is_reverse']
        value_data_step_cash_amount1 = data_actual['data']['amount1']
        value_data_step_cash_description = data_actual['data']['description']
        value_data_step_cash_token = data_actual['data']['token']
        value_data_step_cash_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
        value_data_step_cash_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_not_equals('list_cash', [], value_data_step_cash_list_cash)
        AU.assert_not_empty('list_cash', [], value_data_step_cash_list_cash)
        AU.assert_equals('list_cash_from_response', [], value_data_step_cash_list_cash_from_response)
        AU.assert_equals('transaction_code', 'DPT_CWR', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'CWR', value_data_step_cash_transaction_type)
        AU.assert_equals('sub_code', step_code_cash, value_data_step_cash_sub_code)
        AU.assert_not_null('transaction_date', value_data_step_cash_transaction_date)
        AU.assert_not_empty('transaction_date', value_data_step_cash_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_step_cash_service_sys_date)
        AU.assert_not_empty('service_sys_date', value_data_step_cash_service_sys_date)
        AU.assert_not_null('reference_id', value_data_step_cash_reference_id)
        AU.assert_not_empty('reference_id', value_data_step_cash_reference_id)
        AU.assert_not_null('ref_id', value_data_step_cash_ref_id)
        AU.assert_not_empty('ref_id', value_data_step_cash_ref_id)
        AU.assert_empty('reference_code', value_data_step_cash_reference_code)
        AU.assert_empty('business_code', value_data_step_cash_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_step_cash_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_step_cash_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_step_cash_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_step_cash_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_step_cash_current_loginname)
        AU.assert_empty('user_approve', value_data_step_cash_user_approve)
        AU.assert_equals('status', 'N', value_data_step_cash_status)
        AU.assert_equals('is_reverse',  False, value_data_step_cash_is_reverse)
        AU.assert_equals('amount1', 0, value_data_step_cash_amount1)
        AU.assert_equals('description', '1120: Cash withdrawal', value_data_step_cash_description)
        AU.assert_equals('token', '*', value_data_step_cash_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_step_cash_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_step_cash_is_transaction_compensated)
        # 'response' - verify item under 'data' and 'list_cash'
        AU.assert_equals('Number item in list_cash', 2, len(data_actual['data']['list_cash']))
        # 'response' - verify key response under 'data' and 'list_cash', item 1
        AU.assert_exists(expected_key['data_list_cash'], data_actual['data']['list_cash'][0])
        # 'response' - get value under 'data' and 'list_cash', item 1
        value_list_cash_amount_cash_change = data_actual['data']['list_cash'][0]['amount_cash_change']
        value_list_cash_base_amount = data_actual['data']['list_cash'][0]['base_amount']
        value_list_cash_debit_or_credit = data_actual['data']['list_cash'][0]['debit_or_credit']
        value_list_cash_currency_code = data_actual['data']['list_cash'][0]['currency_code']
        value_list_cash_condition = data_actual['data']['list_cash'][0]['condition']
        value_list_cash_posting = data_actual['data']['list_cash'][0]['posting']
        value_list_cash_accounting_group = data_actual['data']['list_cash'][0]['accounting_group']
        value_list_cash_transaction_code = data_actual['data']['list_cash'][0]['transaction_code']
        value_list_cash_transaction_number = data_actual['data']['list_cash'][0]['transaction_number']
        value_list_cash_transaction_type = data_actual['data']['list_cash'][0]['transaction_type']
        value_list_cash_sub_code = data_actual['data']['list_cash'][0]['sub_code']
        value_list_cash_transaction_date = data_actual['data']['list_cash'][0]['transaction_date']
        value_list_cash_service_sys_date = data_actual['data']['list_cash'][0]['service_sys_date']
        value_list_cash_reference_id = data_actual['data']['list_cash'][0]['reference_id']
        value_list_cash_ref_id = data_actual['data']['list_cash'][0]['ref_id']
        value_list_cash_reference_code = data_actual['data']['list_cash'][0]['reference_code']
        value_list_cash_business_code = data_actual['data']['list_cash'][0]['business_code']
        value_list_cash_value_date = data_actual['data']['list_cash'][0]['value_date']
        value_list_cash_current_user_code = data_actual['data']['list_cash'][0]['current_user_code']
        value_list_cash_current_branch_code = data_actual['data']['list_cash'][0]['current_branch_code']
        value_list_cash_current_username = data_actual['data']['list_cash'][0]['current_username']
        value_list_cash_current_loginname = data_actual['data']['list_cash'][0]['current_loginname']
        value_list_cash_user_approve = data_actual['data']['list_cash'][0]['user_approve']
        value_list_cash_status = data_actual['data']['list_cash'][0]['status']
        value_list_cash_is_reverse = data_actual['data']['list_cash'][0]['is_reverse']
        value_list_cash_amount1 = data_actual['data']['list_cash'][0]['amount1']
        value_list_cash_description = data_actual['data']['list_cash'][0]['description']
        value_list_cash_token = data_actual['data']['list_cash'][0]['token']
        value_list_cash_is_transaction_reverse = data_actual['data']['list_cash'][0]['is_transaction_reverse']
        value_list_cash_is_transaction_compensated = data_actual['data']['list_cash'][0]['is_transaction_compensated']
        # 'response' - verify value under 'data' and 'list_cash', item 1
        AU.assert_equals('amount_cash_change', withdraw_amount, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'C', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', None, value_list_cash_condition)
        AU.assert_equals('posting', False, value_list_cash_posting)
        AU.assert_equals('accounting_group', 1, value_list_cash_accounting_group)
        AU.assert_null('transaction_code', value_list_cash_transaction_code)
        AU.assert_null('transaction_number', value_list_cash_transaction_number)
        AU.assert_null('transaction_type', value_list_cash_transaction_type)
        AU.assert_null('sub_code', value_list_cash_sub_code)
        AU.assert_equals('transaction_date', '0001-01-01T00:00:00', value_list_cash_transaction_date)
        AU.assert_equals('service_sys_date', '0001-01-01T00:00:00', value_list_cash_service_sys_date)
        AU.assert_null('reference_id', value_list_cash_reference_id)
        AU.assert_null('ref_id', value_list_cash_ref_id)
        AU.assert_null('reference_code', value_list_cash_reference_code)
        AU.assert_null('business_code', value_list_cash_business_code)
        AU.assert_equals('value_date', '0001-01-01T00:00:00', value_list_cash_value_date)
        AU.assert_null('current_user_code', value_list_cash_current_user_code)
        AU.assert_null('current_branch_code', value_list_cash_current_branch_code)
        AU.assert_null('current_username', value_list_cash_current_username)
        AU.assert_null('current_loginname', value_list_cash_current_loginname)
        AU.assert_null('user_approve', value_list_cash_user_approve)
        AU.assert_null('status', value_list_cash_status)
        AU.assert_equals('is_reverse', False, value_list_cash_is_reverse)
        AU.assert_equals('amount1', 0, value_list_cash_amount1)
        AU.assert_null('description', value_list_cash_description)
        AU.assert_null('token', value_list_cash_token)
        AU.assert_equals('is_transaction_reverse', False, value_list_cash_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated', False, value_list_cash_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'list_cash', item 2
        AU.assert_exists(expected_key['data_list_cash'], data_actual['data']['list_cash'][1])
        # 'response' - get value under 'data' and 'list_cash', item 2
        value_list_cash_amount_cash_change = data_actual['data']['list_cash'][1]['amount_cash_change']
        value_list_cash_base_amount = data_actual['data']['list_cash'][1]['base_amount']
        value_list_cash_debit_or_credit = data_actual['data']['list_cash'][1]['debit_or_credit']
        value_list_cash_currency_code = data_actual['data']['list_cash'][1]['currency_code']
        value_list_cash_condition = data_actual['data']['list_cash'][1]['condition']
        value_list_cash_posting = data_actual['data']['list_cash'][1]['posting']
        value_list_cash_accounting_group = data_actual['data']['list_cash'][1]['accounting_group']
        value_list_cash_transaction_code = data_actual['data']['list_cash'][1]['transaction_code']
        value_list_cash_transaction_number = data_actual['data']['list_cash'][1]['transaction_number']
        value_list_cash_transaction_type = data_actual['data']['list_cash'][1]['transaction_type']
        value_list_cash_sub_code = data_actual['data']['list_cash'][1]['sub_code']
        value_list_cash_transaction_date = data_actual['data']['list_cash'][1]['transaction_date']
        value_list_cash_service_sys_date = data_actual['data']['list_cash'][1]['service_sys_date']
        value_list_cash_reference_id = data_actual['data']['list_cash'][1]['reference_id']
        value_list_cash_ref_id = data_actual['data']['list_cash'][1]['ref_id']
        value_list_cash_reference_code = data_actual['data']['list_cash'][1]['reference_code']
        value_list_cash_business_code = data_actual['data']['list_cash'][1]['business_code']
        value_list_cash_value_date = data_actual['data']['list_cash'][1]['value_date']
        value_list_cash_current_user_code = data_actual['data']['list_cash'][1]['current_user_code']
        value_list_cash_current_branch_code = data_actual['data']['list_cash'][1]['current_branch_code']
        value_list_cash_current_username = data_actual['data']['list_cash'][1]['current_username']
        value_list_cash_current_loginname = data_actual['data']['list_cash'][1]['current_loginname']
        value_list_cash_user_approve = data_actual['data']['list_cash'][1]['user_approve']
        value_list_cash_status = data_actual['data']['list_cash'][1]['status']
        value_list_cash_is_reverse = data_actual['data']['list_cash'][1]['is_reverse']
        value_list_cash_amount1 = data_actual['data']['list_cash'][1]['amount1']
        value_list_cash_description = data_actual['data']['list_cash'][1]['description']
        value_list_cash_token = data_actual['data']['list_cash'][1]['token']
        value_list_cash_is_transaction_reverse = data_actual['data']['list_cash'][1]['is_transaction_reverse']
        value_list_cash_is_transaction_compensated = data_actual['data']['list_cash'][1]['is_transaction_compensated']
        # 'response' - verify value under 'data' and 'list_cash', item 2
        AU.assert_equals('amount_cash_change', total_fee, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', None, value_list_cash_condition)
        AU.assert_equals('posting', False, value_list_cash_posting)
        AU.assert_equals('accounting_group', 2, value_list_cash_accounting_group)
        AU.assert_null('transaction_code', value_list_cash_transaction_code)
        AU.assert_null('transaction_number', value_list_cash_transaction_number)
        AU.assert_null('transaction_type', value_list_cash_transaction_type)
        AU.assert_null('sub_code', value_list_cash_sub_code)
        AU.assert_equals('transaction_date', '0001-01-01T00:00:00', value_list_cash_transaction_date)
        AU.assert_equals('service_sys_date', '0001-01-01T00:00:00', value_list_cash_service_sys_date)
        AU.assert_null('reference_id', value_list_cash_reference_id)
        AU.assert_null('ref_id', value_list_cash_ref_id)
        AU.assert_null('reference_code', value_list_cash_reference_code)
        AU.assert_null('business_code', value_list_cash_business_code)
        AU.assert_equals('value_date', '0001-01-01T00:00:00', value_list_cash_value_date)
        AU.assert_null('current_user_code', value_list_cash_current_user_code)
        AU.assert_null('current_branch_code', value_list_cash_current_branch_code)
        AU.assert_null('current_username', value_list_cash_current_username)
        AU.assert_null('current_loginname', value_list_cash_current_loginname)
        AU.assert_null('user_approve', value_list_cash_user_approve)
        AU.assert_null('status', value_list_cash_status)
        AU.assert_equals('is_reverse', False, value_list_cash_is_reverse)
        AU.assert_equals('amount1', 0, value_list_cash_amount1)
        AU.assert_null('description', value_list_cash_description)
        AU.assert_null('token', value_list_cash_token)
        AU.assert_equals('is_transaction_reverse', False, value_list_cash_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated', False, value_list_cash_is_transaction_compensated)
        # 'postings' - get data actual - step CASH
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
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
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
        AU.assert_equals('TransTableName', 'CashList', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'CASH', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_cash, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', total_fee, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('TransTableName', 'CashList', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'CASH', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_cash, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # # 'account_balances' - get data actual - step CASH
        # data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        # print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # # 'account_balances' - verify number items
        # AU.assert_equals('Number item in account_balances', 1, len(data_account_balances))
        # # 'account_balances' - verify key response under array item 1
        # AU.assert_exists(expected_key['account_balances'], data_account_balances[0])
        # # 'account_balances' - get value under array item 1
        # value_account_balances_account_number = data_account_balances[0]['account_number']
        # value_account_balances_amount = data_account_balances[0]['amount']
        # value_account_balances_debit_or_credit = data_account_balances[0]['debit_or_credit']
        # value_account_balances_currency = data_account_balances[0]['currency']
        # value_account_balances_available_balance = data_account_balances[0]['available_balance']
        # value_account_balances_transaction_number = data_account_balances[0]['transaction_number']
        # value_account_balances_transaction_date = data_account_balances[0]['transaction_date']
        # value_account_balances_description = data_account_balances[0]['description']
        # # 'account_balances' - verify value under array item 1
        # AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        # AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        # AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        # AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        # AU.assert_equals('available_balance', Decimal(str(amount_deposit))-Decimal(str(minimum_deposit_amount))-Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        # AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        # AU.assert_equals('description', value_data_description, value_account_balances_description)

    def test_05_sp_dpt_cwr_003_success_saving_account_status_dormant(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
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
        account_number = data_dpt_opn['data']['account_number']
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
        # STEP 03: cash deposit for deposit status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_deposit
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, data_dpt_cdp['data']['account_number'])
        # STEP 04: change status from 'Normal' to 'Dormant'
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
        AU.assert_equals('account_number', account_number_approved, data_dpt_cas['data']['account_number'])
        # STEP 05: cash withdrawal from deposit status 'Dormant'
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_approved,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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

    def test_05_sp_dpt_cwr_004_error_account_number_is_empty(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number='',
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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
    def test_05_sp_dpt_cwr_005_error_account_number_is_null(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=None,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [account_number] violates IS_NULL rule.;', rs['description'])

    def test_05_sp_dpt_cwr_006_error_account_number_not_exist(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number='111111111111',
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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
        AU.assert_equals('error_message', 'Invalid account number [111111111111]', value_error_message)
        AU.assert_null('data', value_data)

    def test_05_sp_dpt_cwr_007_error_account_status_closed(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_closed,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_closed}] of account. Available balance must be more than [{withdraw_amount}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_05_sp_dpt_cwr_008_error_account_status_block(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_block,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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

    def test_05_sp_dpt_cwr_009_error_account_status_pending(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_pending,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_pending}] of account. Available balance must be more than [{withdraw_amount}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_05_sp_dpt_cwr_010_error_account_status_new(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_new,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_new}] of account. Available balance must be more than [{withdraw_amount}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_05_sp_dpt_cwr_011_success_current_account_status_normal(self, user):
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
        # STEP 03: deposit for deposit status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_deposit
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, data_dpt_cdp['data']['account_number'])
        # STEP 04: cash withdrawal
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_approved,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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
        AU.assert_exists(expected_key['data_dpt_cwr'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_cwr_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_customer_code = data_actual['data']['customer_code']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_withdraw_amount = data_actual['data']['withdraw_amount']
        value_data_cash_currency = data_actual['data']['cash_currency']
        value_data_cross_rate = data_actual['data']['cross_rate']
        value_data_cash_amount = data_actual['data']['cash_amount']
        value_data_exchange_rate = data_actual['data']['exchange_rate']
        value_data_cash_amount_bcy = data_actual['data']['cash_amount_bcy']
        value_data_withdrawer_name = data_actual['data']['withdrawer_name']
        value_data_withdrawer_id = data_actual['data']['withdrawer_id']
        value_data_withdrawer_address = data_actual['data']['withdrawer_address']
        value_data_home = data_actual['data']['withdrawer_description']['home']
        value_data_office = data_actual['data']['withdrawer_description']['office']
        value_data_id_issue_date = data_actual['data']['id_issue_date']
        value_data_id_place = data_actual['data']['id_place']
        value_data_identification_number = data_actual['data']['identification_number']
        value_data_currency_of_deposit_account = data_actual['data']['currency_of_deposit_account']
        value_data_exchange_rate_debit_account_bcy = data_actual['data']['exchange_rate_debit_account_bcy']
        value_data_amount_debit_account_bcy = data_actual['data']['amount_debit_account_bcy']
        value_data_interest_from_earlywdr = data_actual['data']['interest_from_earlywdr']
        value_data_due_date = data_actual['data']['due_date']
        value_data_commission = data_actual['data']['commission']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_total_vat_for_cash = data_actual['data']['total_vat_for_cash']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_total_ifc_fee_cash = data_actual['data']['total_ifc_fee_cash']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
        value_data_total_ifc_fee = data_actual['data']['total_ifc_fee']
        # value_data_fee_currency_code = data_actual['data']['fee_currency_code']
        value_data_passbook_number = data_actual['data']['passbook_number']
        value_data_fee_data = data_actual['data']['fee_data']
        # value_data_account_balances = data_actual['data']['account_balances']
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
        # verify value of key response in 'data'
        AU.assert_equals('account_number', account_number_approved, value_data_account_number)
        AU.assert_equals('customer_code', customer_code_individual, value_data_customer_code)
        AU.assert_equals('current_balance', None, value_data_current_balance)
        AU.assert_equals('available_balance', None, value_data_available_balance)
        AU.assert_equals('withdraw_amount', withdraw_amount, value_data_withdraw_amount)
        AU.assert_equals('cash_currency', cash_currency, value_data_cash_currency)
        AU.assert_equals('cross_rate', 1.0, value_data_cross_rate)
        AU.assert_equals('cash_amount', 0.0, value_data_cash_amount)
        AU.assert_equals('exchange_rate', 1.0, value_data_exchange_rate)
        AU.assert_equals('cash_amount_bcy', 0.0, value_data_cash_amount_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_id', customer_code_individual, value_data_withdrawer_id)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_equals('home', None, value_data_home)
        AU.assert_equals('office', None, value_data_office)
        AU.assert_equals('id_issue_date', id_issue_date, value_data_id_issue_date)
        AU.assert_equals('id_place', '', value_data_id_place)
        AU.assert_equals('identification_number', '', value_data_identification_number)
        AU.assert_equals('currency_of_deposit_account', currency_of_deposit_account, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1.0, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0.0, value_data_amount_debit_account_bcy)
        AU.assert_equals('interest_from_earlywdr', 0.0, value_data_interest_from_earlywdr)
        AU.assert_equals('due_date', '', value_data_due_date)
        AU.assert_equals('commission', 0.0, value_data_commission)
        AU.assert_equals('interest_prepaid', 0.0, value_data_interest_prepaid)
        AU.assert_equals('total_vat_for_cash', 0.0, value_data_total_vat_for_cash)
        AU.assert_equals('account_linkage', '', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0.0, value_data_amount_linkage)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('total_ifc_fee_cash', 0.0, value_data_total_ifc_fee_cash)
        AU.assert_equals('total_ifc_fee_deposit', 0.0, value_data_total_ifc_fee_deposit)
        AU.assert_equals('total_ifc_fee', 0.0, value_data_total_ifc_fee)
        # AU.assert_equals('fee_currency_code', None, value_data_fee_currency_code)
        AU.assert_equals('passbook_number', '', value_data_passbook_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        # AU.assert_not_null('account_balances', value_data_account_balances)
        AU.assert_equals('transaction_code', 'DPT_CWR', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'CWR', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_CWR', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
        AU.assert_not_empty('transaction_date', value_data_transaction_date)
        AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
        AU.assert_not_empty('reference_id', value_data_reference_id)
        AU.assert_not_empty('ref_id', value_data_ref_id)
        AU.assert_equals('reference_code', '', value_data_reference_code)
        AU.assert_equals('business_code', '', value_data_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
        AU.assert_equals('user_approve', '', value_data_user_approve)
        AU.assert_equals('status', 'N', value_data_status)
        AU.assert_equals('is_reverse', False, value_data_is_reverse)
        AU.assert_equals('amount1', 0.0, value_data_amount1)
        AU.assert_equals('description', '1120: Cash withdrawal', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse', False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated', False, value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
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
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        # data_account_balances = data_actual['data']['account_balances']
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
        AU.assert_equals('account_number', account_number_approved, value_account_balances_account_number)
        AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit))-Decimal(str(minimum_deposit_amount))-Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # verify step CASH
        step_code = step_code_cash
        # 'response' - get data actual - step CASH
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
        AU.assert_exists(expected_key['data_step_cash'], data_actual['data'])
        # 'response' - get value under 'data'
        value_data_step_cash_list_cash = data_actual['data']['list_cash']
        value_data_step_cash_list_cash_from_response = data_actual['data']['list_cash_from_response']
        value_data_step_cash_transaction_code = data_actual['data']['transaction_code']
        value_data_step_cash_transaction_number = data_actual['data']['transaction_number']
        value_data_step_cash_transaction_type = data_actual['data']['transaction_type']
        value_data_step_cash_sub_code = data_actual['data']['sub_code']
        value_data_step_cash_transaction_date = data_actual['data']['transaction_date']
        value_data_step_cash_service_sys_date = data_actual['data']['service_sys_date']
        value_data_step_cash_reference_id = data_actual['data']['reference_id']
        value_data_step_cash_ref_id = data_actual['data']['ref_id']
        value_data_step_cash_reference_code = data_actual['data']['reference_code']
        value_data_step_cash_business_code = data_actual['data']['business_code']
        value_data_step_cash_value_date = data_actual['data']['value_date']
        value_data_step_cash_current_user_code = data_actual['data']['current_user_code']
        value_data_step_cash_current_branch_code = data_actual['data']['current_branch_code']
        value_data_step_cash_current_username = data_actual['data']['current_username']
        value_data_step_cash_current_loginname = data_actual['data']['current_loginname']
        value_data_step_cash_user_approve = data_actual['data']['user_approve']
        value_data_step_cash_status = data_actual['data']['status']
        value_data_step_cash_is_reverse = data_actual['data']['is_reverse']
        value_data_step_cash_amount1 = data_actual['data']['amount1']
        value_data_step_cash_description = data_actual['data']['description']
        value_data_step_cash_token = data_actual['data']['token']
        value_data_step_cash_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
        value_data_step_cash_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
        # 'response' - verify value under 'data'
        AU.assert_not_equals('list_cash', [], value_data_step_cash_list_cash)
        AU.assert_not_empty('list_cash', [], value_data_step_cash_list_cash)
        AU.assert_equals('list_cash_from_response', [], value_data_step_cash_list_cash_from_response)
        AU.assert_equals('transaction_code', 'DPT_CWR', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'CWR', value_data_step_cash_transaction_type)
        AU.assert_equals('sub_code', step_code_cash, value_data_step_cash_sub_code)
        AU.assert_not_null('transaction_date', value_data_step_cash_transaction_date)
        AU.assert_not_empty('transaction_date', value_data_step_cash_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_step_cash_service_sys_date)
        AU.assert_not_empty('service_sys_date', value_data_step_cash_service_sys_date)
        AU.assert_not_null('reference_id', value_data_step_cash_reference_id)
        AU.assert_not_empty('reference_id', value_data_step_cash_reference_id)
        AU.assert_not_null('ref_id', value_data_step_cash_ref_id)
        AU.assert_not_empty('ref_id', value_data_step_cash_ref_id)
        AU.assert_empty('reference_code', value_data_step_cash_reference_code)
        AU.assert_empty('business_code', value_data_step_cash_business_code)
        AU.assert_equals('value_date', user_service['working_date'], value_data_step_cash_value_date)
        AU.assert_equals('current_user_code', user_service['username'], value_data_step_cash_current_user_code)
        AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_step_cash_current_branch_code)
        AU.assert_equals('current_username', user_service['fullname'], value_data_step_cash_current_username)
        AU.assert_equals('current_loginname', user_service['username'], value_data_step_cash_current_loginname)
        AU.assert_empty('user_approve', value_data_step_cash_user_approve)
        AU.assert_equals('status', 'N', value_data_step_cash_status)
        AU.assert_equals('is_reverse',  False, value_data_step_cash_is_reverse)
        AU.assert_equals('amount1', 0, value_data_step_cash_amount1)
        AU.assert_equals('description', '1120: Cash withdrawal', value_data_step_cash_description)
        AU.assert_equals('token', '*', value_data_step_cash_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_step_cash_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_step_cash_is_transaction_compensated)
        # 'response' - verify item under 'data' and 'list_cash'
        AU.assert_equals('Number item in list_cash', 2, len(data_actual['data']['list_cash']))
        # 'response' - verify key response under 'data' and 'list_cash', item 1
        AU.assert_exists(expected_key['data_list_cash'], data_actual['data']['list_cash'][0])
        # 'response' - get value under 'data' and 'list_cash', item 1
        value_list_cash_amount_cash_change = data_actual['data']['list_cash'][0]['amount_cash_change']
        value_list_cash_base_amount = data_actual['data']['list_cash'][0]['base_amount']
        value_list_cash_debit_or_credit = data_actual['data']['list_cash'][0]['debit_or_credit']
        value_list_cash_currency_code = data_actual['data']['list_cash'][0]['currency_code']
        value_list_cash_condition = data_actual['data']['list_cash'][0]['condition']
        value_list_cash_posting = data_actual['data']['list_cash'][0]['posting']
        value_list_cash_accounting_group = data_actual['data']['list_cash'][0]['accounting_group']
        value_list_cash_transaction_code = data_actual['data']['list_cash'][0]['transaction_code']
        value_list_cash_transaction_number = data_actual['data']['list_cash'][0]['transaction_number']
        value_list_cash_transaction_type = data_actual['data']['list_cash'][0]['transaction_type']
        value_list_cash_sub_code = data_actual['data']['list_cash'][0]['sub_code']
        value_list_cash_transaction_date = data_actual['data']['list_cash'][0]['transaction_date']
        value_list_cash_service_sys_date = data_actual['data']['list_cash'][0]['service_sys_date']
        value_list_cash_reference_id = data_actual['data']['list_cash'][0]['reference_id']
        value_list_cash_ref_id = data_actual['data']['list_cash'][0]['ref_id']
        value_list_cash_reference_code = data_actual['data']['list_cash'][0]['reference_code']
        value_list_cash_business_code = data_actual['data']['list_cash'][0]['business_code']
        value_list_cash_value_date = data_actual['data']['list_cash'][0]['value_date']
        value_list_cash_current_user_code = data_actual['data']['list_cash'][0]['current_user_code']
        value_list_cash_current_branch_code = data_actual['data']['list_cash'][0]['current_branch_code']
        value_list_cash_current_username = data_actual['data']['list_cash'][0]['current_username']
        value_list_cash_current_loginname = data_actual['data']['list_cash'][0]['current_loginname']
        value_list_cash_user_approve = data_actual['data']['list_cash'][0]['user_approve']
        value_list_cash_status = data_actual['data']['list_cash'][0]['status']
        value_list_cash_is_reverse = data_actual['data']['list_cash'][0]['is_reverse']
        value_list_cash_amount1 = data_actual['data']['list_cash'][0]['amount1']
        value_list_cash_description = data_actual['data']['list_cash'][0]['description']
        value_list_cash_token = data_actual['data']['list_cash'][0]['token']
        value_list_cash_is_transaction_reverse = data_actual['data']['list_cash'][0]['is_transaction_reverse']
        value_list_cash_is_transaction_compensated = data_actual['data']['list_cash'][0]['is_transaction_compensated']
        # 'response' - verify value under 'data' and 'list_cash', item 1
        AU.assert_equals('amount_cash_change', withdraw_amount, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'C', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', None, value_list_cash_condition)
        AU.assert_equals('posting', False, value_list_cash_posting)
        AU.assert_equals('accounting_group', 1, value_list_cash_accounting_group)
        AU.assert_null('transaction_code', value_list_cash_transaction_code)
        AU.assert_null('transaction_number', value_list_cash_transaction_number)
        AU.assert_null('transaction_type', value_list_cash_transaction_type)
        AU.assert_null('sub_code', value_list_cash_sub_code)
        AU.assert_equals('transaction_date', '0001-01-01T00:00:00', value_list_cash_transaction_date)
        AU.assert_equals('service_sys_date', '0001-01-01T00:00:00', value_list_cash_service_sys_date)
        AU.assert_null('reference_id', value_list_cash_reference_id)
        AU.assert_null('ref_id', value_list_cash_ref_id)
        AU.assert_null('reference_code', value_list_cash_reference_code)
        AU.assert_null('business_code', value_list_cash_business_code)
        AU.assert_equals('value_date', '0001-01-01T00:00:00', value_list_cash_value_date)
        AU.assert_null('current_user_code', value_list_cash_current_user_code)
        AU.assert_null('current_branch_code', value_list_cash_current_branch_code)
        AU.assert_null('current_username', value_list_cash_current_username)
        AU.assert_null('current_loginname', value_list_cash_current_loginname)
        AU.assert_null('user_approve', value_list_cash_user_approve)
        AU.assert_null('status', value_list_cash_status)
        AU.assert_equals('is_reverse', False, value_list_cash_is_reverse)
        AU.assert_equals('amount1', 0, value_list_cash_amount1)
        AU.assert_null('description', value_list_cash_description)
        AU.assert_null('token', value_list_cash_token)
        AU.assert_equals('is_transaction_reverse', False, value_list_cash_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated', False, value_list_cash_is_transaction_compensated)
        # 'response' - verify key response under 'data' and 'list_cash', item 2
        AU.assert_exists(expected_key['data_list_cash'], data_actual['data']['list_cash'][1])
        # 'response' - get value under 'data' and 'list_cash', item 2
        value_list_cash_amount_cash_change = data_actual['data']['list_cash'][1]['amount_cash_change']
        value_list_cash_base_amount = data_actual['data']['list_cash'][1]['base_amount']
        value_list_cash_debit_or_credit = data_actual['data']['list_cash'][1]['debit_or_credit']
        value_list_cash_currency_code = data_actual['data']['list_cash'][1]['currency_code']
        value_list_cash_condition = data_actual['data']['list_cash'][1]['condition']
        value_list_cash_posting = data_actual['data']['list_cash'][1]['posting']
        value_list_cash_accounting_group = data_actual['data']['list_cash'][1]['accounting_group']
        value_list_cash_transaction_code = data_actual['data']['list_cash'][1]['transaction_code']
        value_list_cash_transaction_number = data_actual['data']['list_cash'][1]['transaction_number']
        value_list_cash_transaction_type = data_actual['data']['list_cash'][1]['transaction_type']
        value_list_cash_sub_code = data_actual['data']['list_cash'][1]['sub_code']
        value_list_cash_transaction_date = data_actual['data']['list_cash'][1]['transaction_date']
        value_list_cash_service_sys_date = data_actual['data']['list_cash'][1]['service_sys_date']
        value_list_cash_reference_id = data_actual['data']['list_cash'][1]['reference_id']
        value_list_cash_ref_id = data_actual['data']['list_cash'][1]['ref_id']
        value_list_cash_reference_code = data_actual['data']['list_cash'][1]['reference_code']
        value_list_cash_business_code = data_actual['data']['list_cash'][1]['business_code']
        value_list_cash_value_date = data_actual['data']['list_cash'][1]['value_date']
        value_list_cash_current_user_code = data_actual['data']['list_cash'][1]['current_user_code']
        value_list_cash_current_branch_code = data_actual['data']['list_cash'][1]['current_branch_code']
        value_list_cash_current_username = data_actual['data']['list_cash'][1]['current_username']
        value_list_cash_current_loginname = data_actual['data']['list_cash'][1]['current_loginname']
        value_list_cash_user_approve = data_actual['data']['list_cash'][1]['user_approve']
        value_list_cash_status = data_actual['data']['list_cash'][1]['status']
        value_list_cash_is_reverse = data_actual['data']['list_cash'][1]['is_reverse']
        value_list_cash_amount1 = data_actual['data']['list_cash'][1]['amount1']
        value_list_cash_description = data_actual['data']['list_cash'][1]['description']
        value_list_cash_token = data_actual['data']['list_cash'][1]['token']
        value_list_cash_is_transaction_reverse = data_actual['data']['list_cash'][1]['is_transaction_reverse']
        value_list_cash_is_transaction_compensated = data_actual['data']['list_cash'][1]['is_transaction_compensated']
        # 'response' - verify value under 'data' and 'list_cash', item 2
        AU.assert_equals('amount_cash_change', 0, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', None, value_list_cash_condition)
        AU.assert_equals('posting', False, value_list_cash_posting)
        AU.assert_equals('accounting_group', 2, value_list_cash_accounting_group)
        AU.assert_null('transaction_code', value_list_cash_transaction_code)
        AU.assert_null('transaction_number', value_list_cash_transaction_number)
        AU.assert_null('transaction_type', value_list_cash_transaction_type)
        AU.assert_null('sub_code', value_list_cash_sub_code)
        AU.assert_equals('transaction_date', '0001-01-01T00:00:00', value_list_cash_transaction_date)
        AU.assert_equals('service_sys_date', '0001-01-01T00:00:00', value_list_cash_service_sys_date)
        AU.assert_null('reference_id', value_list_cash_reference_id)
        AU.assert_null('ref_id', value_list_cash_ref_id)
        AU.assert_null('reference_code', value_list_cash_reference_code)
        AU.assert_null('business_code', value_list_cash_business_code)
        AU.assert_equals('value_date', '0001-01-01T00:00:00', value_list_cash_value_date)
        AU.assert_null('current_user_code', value_list_cash_current_user_code)
        AU.assert_null('current_branch_code', value_list_cash_current_branch_code)
        AU.assert_null('current_username', value_list_cash_current_username)
        AU.assert_null('current_loginname', value_list_cash_current_loginname)
        AU.assert_null('user_approve', value_list_cash_user_approve)
        AU.assert_null('status', value_list_cash_status)
        AU.assert_equals('is_reverse', False, value_list_cash_is_reverse)
        AU.assert_equals('amount1', 0, value_list_cash_amount1)
        AU.assert_null('description', value_list_cash_description)
        AU.assert_null('token', value_list_cash_token)
        AU.assert_equals('is_transaction_reverse', False, value_list_cash_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated', False, value_list_cash_is_transaction_compensated)
        # 'postings' - get data actual - step CASH
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
        AU.assert_equals('Number item in posting', 2, len(data_actual_posting))
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
        AU.assert_not_empty('TransactionNumber', value_TransactionNumber)
        AU.assert_not_null('TransactionNumber', value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_not_empty('TransactionNumber', value_TransactionNumber)
        AU.assert_not_null('TransactionNumber', value_TransactionNumber)
        AU.assert_equals('TransTableName', 'CashList', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'CASH', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_cash, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', withdraw_amount, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
        # # 'account_balances' - get data actual - step CASH
        # data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        # print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # # 'account_balances' - verify number items
        # AU.assert_equals('Number item in account_balances', 1, len(data_account_balances))
        # # 'account_balances' - verify key response under array item 1
        # AU.assert_exists(expected_key['account_balances'], data_account_balances[0])
        # # 'account_balances' - get value under array item 1
        # value_account_balances_account_number = data_account_balances[0]['account_number']
        # value_account_balances_amount = data_account_balances[0]['amount']
        # value_account_balances_debit_or_credit = data_account_balances[0]['debit_or_credit']
        # value_account_balances_currency = data_account_balances[0]['currency']
        # value_account_balances_available_balance = data_account_balances[0]['available_balance']
        # value_account_balances_transaction_number = data_account_balances[0]['transaction_number']
        # value_account_balances_transaction_date = data_account_balances[0]['transaction_date']
        # value_account_balances_description = data_account_balances[0]['description']
        # # 'account_balances' - verify value under array item 1
        # AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        # AU.assert_equals('amount', withdraw_amount, value_account_balances_amount)
        # AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        # AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        # AU.assert_equals('available_balance', Decimal(str(amount_deposit))-Decimal(str(minimum_deposit_amount))-Decimal(str(withdraw_amount)), Decimal(str(value_account_balances_available_balance)))
        # AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        # AU.assert_equals('description', value_data_description, value_account_balances_description)

    def test_05_sp_dpt_cwr_012_error_fixed_deposit_account_status_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_fixed_deposit_normal,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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

    def test_05_sp_dpt_cwr_013_error_pepaid_fixed_deposit_account_status_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_prepaid_fixed_deposit_normal,
            withdraw_amount=withdraw_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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
    def test_05_sp_dpt_cwr_014_error_withdrawal_amount_is_minus(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=to_account_number_saving_single_valid,
            withdraw_amount=-10000,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [withdraw_amount] violates Minimum rule: Minimum value is 0.01;', rs['description'])

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_05_sp_dpt_cwr_015_error_withdrawal_amount_is_empty(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=to_account_number_saving_single_valid,
            withdraw_amount='',
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', "Input is invalid.Validate field [withdraw_amount]: value=[], datatype=[Number] with exception: [The input string '' was not in a correct format.].;", rs['description'])

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_05_sp_dpt_cwr_016_error_withdrawal_amount_is_zero(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=to_account_number_saving_single_valid,
            withdraw_amount=0,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [withdraw_amount] violates Minimum rule: Minimum value is 0.01;', rs['description'])

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_05_sp_dpt_cwr_017_error_withdrawal_amount_is_null(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_CWR(
            account_number=to_account_number_saving_single_valid,
            withdraw_amount=None,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [withdraw_amount] violates IS_NULL rule.;', rs['description'])

    def test_05_sp_dpt_cwr_018_error_withdrawal_amount_bigger_available_balance(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        catalog_code='BSMMK0000'
        catalog_name='Bonus savings account  in MMK'
        deposit_type='Savings'
        deposit_sub_type='S2'
        minimum_deposit_amount=50000
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
        # STEP 03: cash deposit for deposit status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=values_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_deposit
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_approved, data_dpt_cdp['data']['account_number'])
        # STEP 04: cash withdrawal
        fields_data = sp_payload.DPT_CWR(
            account_number=account_number_approved,
            withdraw_amount=(amount_deposit-minimum_deposit_amount+0.01),
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWR(fields_data)
        step_code = 'DPT_CWR'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number_approved}] of account. Available balance must be more than [{amount_deposit-minimum_deposit_amount+0.01}] - en', value_error_message)
        AU.assert_null('data', value_data)
