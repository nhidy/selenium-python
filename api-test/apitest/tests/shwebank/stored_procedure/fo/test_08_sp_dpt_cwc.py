import json
import pytest
import random

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
stock_prefix='CQ'
assigned_staff_code=user_service['username']
cash_currency='MMK'
address='27, Nguyen huu tho, Tan Hung, Q7'
id_issue_date=user_service['working_date']
value_date=user_service['working_date']
currency_of_deposit_account='MMK'
branch_name='003 - Bayint Naung Branch'
gl_account_cash='003101030100010101'
# data test invalid
# # data test trên 104
# step_code_cash='CSH_UPDATE_CASH'
# data test trên 198
step_code_cash='CSH_UPDATE_CASH_SP'

@pytest.fixture(scope='session')
def user():
    req = RU(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_CWC
class Test_SP_DPT_CWC(object):

    def test_08_sp_dpt_cwc_001_success_current_account_status_normal(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_exists(expected_key['data_dpt_cwc'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_cwc_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_stock_prefix = data_actual['data']['stock_prefix']
        value_data_cheque_no = data_actual['data']['cheque_no']
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_cheque_amount = data_actual['data']['cheque_amount']
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
        value_data_commission = data_actual['data']['commission']
        value_data_interest_from_earlywdr = data_actual['data']['interest_from_earlywdr']
        value_data_due_date = data_actual['data']['due_date']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_total_vat_for_cash = data_actual['data']['total_vat_for_cash']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_cash = data_actual['data']['total_ifc_fee_cash']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
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
        # 'response' - verify value under 'data'
        AU.assert_equals('stock_prefix', 'CQ', value_data_stock_prefix)
        AU.assert_equals('cheque_no', cheque_no, value_data_cheque_no)
        AU.assert_equals('account_number', account_number, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('cheque_amount', cheque_amount, value_data_cheque_amount)
        AU.assert_equals('cash_currency', cash_currency, value_data_cash_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('cash_amount', 0, value_data_cash_amount)
        AU.assert_equals('exchange_rate', 1, value_data_exchange_rate)
        AU.assert_equals('cash_amount_bcy', 0, value_data_cash_amount_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_id', customer_code_individual, value_data_withdrawer_id)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('id_issue_date', id_issue_date, value_data_id_issue_date)
        AU.assert_empty('id_place', value_data_id_place)
        AU.assert_empty('identification_number', value_data_identification_number)
        AU.assert_equals('currency_of_deposit_account', currency_of_deposit_account, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('commission', 0, value_data_commission)
        AU.assert_equals('interest_from_earlywdr', 0, value_data_interest_from_earlywdr)
        AU.assert_empty('due_date', value_data_due_date)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('total_vat_for_cash', 0, value_data_total_vat_for_cash)
        AU.assert_empty('account_linkage', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_cash', 0, value_data_total_ifc_fee_cash)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        # AU.assert_not_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_CWC', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'CWC', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_CWC', value_data_sub_code)
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
        AU.assert_equals('description', '1121: Cash withdrawal by cheque', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
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
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        AU.assert_equals('amount', cheque_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', 0, value_account_balances_available_balance)
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
        AU.assert_equals('transaction_code', 'DPT_CWC', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'CWC', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '1121: Cash withdrawal by cheque', value_data_step_cash_description)
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
        AU.assert_equals('amount_cash_change', cheque_amount, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'C', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\">\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.cheque_amount\",0]}}", value_list_cash_condition)
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
        AU.assert_equals('condition', "{\"expression\":{\"func\":\">\",\"type\":\"boolean\",\"paras\":[\"$.execution_steps.[1].p2_content.response.data.total_ifc_fee_cash\",0]}}", value_list_cash_condition)
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
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        AU.assert_equals('amount', cheque_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', 0, value_account_balances_available_balance)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_08_sp_dpt_cwc_002_success_current_account_status_normal_add_fee(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        commission=300
        share_fee_01=0
        ifc_name_01='Deposit (MMK) For Same Region  (By Cash/Tr)'
        ifc_code_01=340
        payrate_01=100
        ifc_value_01=250
        value_type_01='F'
        ifc_amount_01=250
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='CSH'
        gl_account_ifcc_01='003303030100010101'
        share_fee_02=0
        ifc_name_02='Withdrawal (MMK) For Different Region  (By Cash)(Postage & Fax Charges)'
        ifc_code_02=345
        payrate_02=100
        ifc_value_02=50
        value_type_02='F'
        ifc_amount_02=50
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='CSH'
        gl_account_ifcc_02='003207050100010101'
        fee_data = [
            {
                "share_fee": share_fee_01,
                "ifc_name": ifc_name_01,
                "ifc_code": ifc_code_01,
                "payrate": payrate_01,
                "ifc_value": ifc_value_01,
                "value_type": value_type_01,
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
                "ifc_code": ifc_code_02,
                "payrate": payrate_02,
                "ifc_value": ifc_value_02,
                "value_type": value_type_02,
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
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            fee_data=fee_data,
            commission=commission
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_exists(expected_key['data_dpt_cwc'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_cwc_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_stock_prefix = data_actual['data']['stock_prefix']
        value_data_cheque_no = data_actual['data']['cheque_no']
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_cheque_amount = data_actual['data']['cheque_amount']
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
        value_data_commission = data_actual['data']['commission']
        value_data_interest_from_earlywdr = data_actual['data']['interest_from_earlywdr']
        value_data_due_date = data_actual['data']['due_date']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_total_vat_for_cash = data_actual['data']['total_vat_for_cash']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_cash = data_actual['data']['total_ifc_fee_cash']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
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
        # 'response' - verify value under 'data'
        AU.assert_equals('stock_prefix', 'CQ', value_data_stock_prefix)
        AU.assert_equals('cheque_no', cheque_no, value_data_cheque_no)
        AU.assert_equals('account_number', account_number, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('cheque_amount', cheque_amount, value_data_cheque_amount)
        AU.assert_equals('cash_currency', cash_currency, value_data_cash_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('cash_amount', 0, value_data_cash_amount)
        AU.assert_equals('exchange_rate', 1, value_data_exchange_rate)
        AU.assert_equals('cash_amount_bcy', 0, value_data_cash_amount_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_id', customer_code_individual, value_data_withdrawer_id)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('id_issue_date', id_issue_date, value_data_id_issue_date)
        AU.assert_empty('id_place', value_data_id_place)
        AU.assert_empty('identification_number', value_data_identification_number)
        AU.assert_equals('currency_of_deposit_account', currency_of_deposit_account, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('commission', commission, value_data_commission)
        AU.assert_equals('interest_from_earlywdr', 0, value_data_interest_from_earlywdr)
        AU.assert_empty('due_date', value_data_due_date)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('total_vat_for_cash', 0, value_data_total_vat_for_cash)
        AU.assert_empty('account_linkage', value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_cash', commission, value_data_total_ifc_fee_cash)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        # AU.assert_not_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_CWC', value_data_transaction_code)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'CWC', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_CWC', value_data_sub_code)
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
        AU.assert_equals('description', '1121: Cash withdrawal by cheque', value_data_description)
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
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        AU.assert_equals('amount', cheque_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', 0, value_account_balances_available_balance)
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
        AU.assert_equals('transaction_code', 'DPT_CWC', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'CWC', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '1121: Cash withdrawal by cheque', value_data_step_cash_description)
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
        AU.assert_equals('amount_cash_change', cheque_amount, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'C', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\">\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.cheque_amount\",0]}}", value_list_cash_condition)
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
        AU.assert_equals('amount_cash_change', commission, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\">\",\"type\":\"boolean\",\"paras\":[\"$.execution_steps.[1].p2_content.response.data.total_ifc_fee_cash\",0]}}", value_list_cash_condition)
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
        AU.assert_equals('Number item in posting CASH', 5, len(data_actual_posting))
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
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        AU.assert_equals('Amount', commission, value_Amount)
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
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        AU.assert_equals('amount', cheque_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', 0, value_account_balances_available_balance)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_08_sp_dpt_cwc_003_error_cheque_no_is_empty(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no='',
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', 'Cheque No is required', value_error_message)
        AU.assert_null('data', value_data)

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_08_sp_dpt_cwc_004_error_cheque_no_is_null(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=None,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [cheque_no] violates IS_NULL rule.;', rs['description'])

    def test_08_sp_dpt_cwc_005_error_cheque_no_not_exist(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no='CQ000000',
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_code', '\n', value_error_code)
        AU.assert_equals('error_message', 'Invalid cheque no [CQ000000] - en\nInvalid cheque no [CQ000000] - en', value_error_message)
        AU.assert_null('data', value_data)

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_08_sp_dpt_cwc_006_error_cheque_amount_is_minus(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=-cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [cheque_amount] violates Minimum rule: Minimum value is 0.01;', rs['description'])

# CASE NAY CHECK DATA_FIELDS CUA NEPTUNE PORTAL
    def test_08_sp_dpt_cwc_007_error_cheque_amount_is_zero(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=0,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        print(json.dumps(rs, indent=4, sort_keys=False))
        # 'response' - verify value
        AU.assert_equals('status', 'ERROR', rs['status'])
        AU.assert_equals('description', 'Input is invalid.Field [cheque_amount] violates Minimum rule: Minimum value is 0.01;', rs['description'])

    def test_08_sp_dpt_cwc_008_error_cheque_no_status_paid(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        remaining_balance=200000
        cheque_amount=amount_deposit-minimum_deposit_amount-remaining_balance
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque status 'Unpaid'
        fields_data_cwc = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data_cwc)
        step_code = 'DPT_CWC'
        # 'response' - get data actual
        data_dpt_cwc = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cwc, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cwc['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cwc['data']['account_number'])
        # STEP 03: Cash withdrawal by cheque status 'Paid'
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=remaining_balance,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid cheque no [{cheque_no}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_08_sp_dpt_cwc_009_error_cheque_no_status_damage(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cn_status='D'
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: Change cheque status to 'Damage'
        fields_data_cts = sp_payload.DPT_CTS(
            account_number=account_number,
            branch_name=branch_name,
            from_serial=from_serial,
            to_serial=to_serial,
            cn_status=cn_status,
            stock_prefix=stock_prefix,
            currency_code=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CTS(fields_data_cts)
        step_code = 'DPT_CTS'
        # 'response' - get data actual
        data_dpt_cts = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cts, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cts['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cts['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque status 'Damage'
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid stock status [{cheque_no}]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_010_error_cheque_no_status_stop(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cn_status='S'
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: Change cheque status to 'Stop'
        fields_data_cts = sp_payload.DPT_CTS(
            account_number=account_number,
            branch_name=branch_name,
            from_serial=from_serial,
            to_serial=to_serial,
            cn_status=cn_status,
            stock_prefix=stock_prefix,
            currency_code=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CTS(fields_data_cts)
        step_code = 'DPT_CTS'
        # 'response' - get data actual
        data_dpt_cts = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cts, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cts['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cts['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque status 'Stop'
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        # AU.assert_equals('error_message', f'Invalid stock status [{cheque_no}]', value_error_message)
        # AU.assert_equals('error_code', 'ERROR', value_error_code)
        AU.assert_equals('error_code', 'Invalid stock status [{0}]', value_error_code)
        AU.assert_equals('error_message', f'{cheque_no}', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_011_error_cheque_no_status_canceled(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cn_status='A'
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: Change cheque status to 'Canceled'
        fields_data_cts = sp_payload.DPT_CTS(
            account_number=account_number,
            branch_name=branch_name,
            from_serial=from_serial,
            to_serial=to_serial,
            cn_status=cn_status,
            stock_prefix=stock_prefix,
            currency_code=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CTS(fields_data_cts)
        step_code = 'DPT_CTS'
        # 'response' - get data actual
        data_dpt_cts = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cts, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cts['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cts['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque status 'Canceled'
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid cheque no [{cheque_no}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_08_sp_dpt_cwc_012_error_cheque_no_status_lost(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cn_status='L'
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: Change cheque status to 'Lost'
        fields_data_cts = sp_payload.DPT_CTS(
            account_number=account_number,
            branch_name=branch_name,
            from_serial=from_serial,
            to_serial=to_serial,
            cn_status=cn_status,
            stock_prefix=stock_prefix,
            currency_code=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CTS(fields_data_cts)
        step_code = 'DPT_CTS'
        # 'response' - get data actual
        data_dpt_cts = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cts, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cts['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cts['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque status 'Lost'
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid stock status [{cheque_no}]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_013_error_current_account_status_closed(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # STEP 01-03: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-04: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-05: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-06: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-07: Close deposit account
        fields_data_cls = sp_payload.DPT_CLS(
            account_number=account_number,
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
        AU.assert_equals('account_number', account_number, data_dpt_cls['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque with account status 'Closed'
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number}] of account. Available balance must be more than [{cheque_amount}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_08_sp_dpt_cwc_014_error_current_account_status_block(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: block deposit account
        fields_data_blk = sp_payload.DPT_BLK(
            account_number=account_number,
            branch_name=branch_name,
            depositor_name=account_name_individual,
            depositor_id=customer_code_individual,
            depositor_address=address,
            depositor_currency=currency_of_deposit_account,
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
        AU.assert_equals('account_number', account_number, data_dpt_blk['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque with account status 'Block'
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid deposit status [Block]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_015_error_current_account_status_new(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cn_status='D'
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # STEP 01-03: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-04: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-05: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-06: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque with account status 'New'
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number}] of account. Available balance must be more than [{cheque_amount}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_08_sp_dpt_cwc_016_error_current_account_status_dormant(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cn_status='D'
        cheque_amount=amount_deposit-minimum_deposit_amount
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: change status from 'Normal' to 'Dormant' of current account
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
        # STEP 02: Cash withdrawal by cheque with account status 'Dormant'
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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

    def test_08_sp_dpt_cwc_017_error_withdrawal_amount_bigger_available_balance(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        cheque_amount=amount_deposit-minimum_deposit_amount+0.01
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number}] of account. Available balance must be more than [{cheque_amount}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_08_sp_dpt_cwc_018_success_current_account_status_normal_fund_transfer(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open saving account
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
        # STEP 01-09: approve saving account
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
        # STEP 01-10: cash deposit to saving status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_cdp['data']['account_number'])
        # STEP 01-11: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_exists(expected_key['data_dpt_cwc'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_cwc_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_stock_prefix = data_actual['data']['stock_prefix']
        value_data_cheque_no = data_actual['data']['cheque_no']
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_cheque_amount = data_actual['data']['cheque_amount']
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
        value_data_commission = data_actual['data']['commission']
        value_data_interest_from_earlywdr = data_actual['data']['interest_from_earlywdr']
        value_data_due_date = data_actual['data']['due_date']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_total_vat_for_cash = data_actual['data']['total_vat_for_cash']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_cash = data_actual['data']['total_ifc_fee_cash']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
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
        # 'response' - verify value under 'data'
        AU.assert_equals('stock_prefix', 'CQ', value_data_stock_prefix)
        AU.assert_equals('cheque_no', cheque_no, value_data_cheque_no)
        AU.assert_equals('account_number', account_number, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('cheque_amount', cheque_amount, value_data_cheque_amount)
        AU.assert_equals('cash_currency', cash_currency, value_data_cash_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('cash_amount', 0, value_data_cash_amount)
        AU.assert_equals('exchange_rate', 1, value_data_exchange_rate)
        AU.assert_equals('cash_amount_bcy', 0, value_data_cash_amount_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_id', customer_code_individual, value_data_withdrawer_id)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('id_issue_date', id_issue_date, value_data_id_issue_date)
        AU.assert_empty('id_place', value_data_id_place)
        AU.assert_empty('identification_number', value_data_identification_number)
        AU.assert_equals('currency_of_deposit_account', currency_of_deposit_account, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('commission', 0, value_data_commission)
        AU.assert_equals('interest_from_earlywdr', 0, value_data_interest_from_earlywdr)
        AU.assert_empty('due_date', value_data_due_date)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('total_vat_for_cash', 0, value_data_total_vat_for_cash)
        AU.assert_equals('account_linkage', account_number_saving, value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_cash', 0, value_data_total_ifc_fee_cash)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        # AU.assert_not_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_CWC', value_data_transaction_code)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'CWC', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_CWC', value_data_sub_code)
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
        AU.assert_equals('description', '1121: Cash withdrawal by cheque', value_data_description)
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
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount',  Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        AU.assert_equals('Amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('Number item in account_balances', 3, len(data_account_balances))
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
        AU.assert_equals('amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_account_balances_amount)))
        AU.assert_equals('debit_or_credit', 'C', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)) + (Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)))), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # 'account_balances' - verify key response under array item 2
        AU.assert_exists(expected_key['account_balances'], data_account_balances[1])
        # 'account_balances' - get value under array item 2
        value_account_balances_account_number = data_account_balances[1]['account_number']
        value_account_balances_amount = data_account_balances[1]['amount']
        value_account_balances_debit_or_credit = data_account_balances[1]['debit_or_credit']
        value_account_balances_currency = data_account_balances[1]['currency']
        value_account_balances_available_balance = data_account_balances[1]['available_balance']
        value_account_balances_transaction_number = data_account_balances[1]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[1]['transaction_date']
        value_account_balances_description = data_account_balances[1]['description']
        # 'account_balances' - verify value under array item 2
        AU.assert_equals('account_number', account_number_saving, value_account_balances_account_number)
        AU.assert_equals('amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_account_balances_amount)))
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', (Decimal(str(amount_deposit_saving)) - Decimal(str(minimum_deposit_amount_saving))) - (Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)))), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # 'account_balances' - verify key response under array item 3
        AU.assert_exists(expected_key['account_balances'], data_account_balances[2])
        # 'account_balances' - get value under array item 3
        value_account_balances_account_number = data_account_balances[2]['account_number']
        value_account_balances_amount = data_account_balances[2]['amount']
        value_account_balances_debit_or_credit = data_account_balances[2]['debit_or_credit']
        value_account_balances_currency = data_account_balances[2]['currency']
        value_account_balances_available_balance = data_account_balances[2]['available_balance']
        value_account_balances_transaction_number = data_account_balances[2]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[2]['transaction_date']
        value_account_balances_description = data_account_balances[2]['description']
        # 'account_balances' - verify value under array item 3
        AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        AU.assert_equals('amount', cheque_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', 0, value_account_balances_available_balance)
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
        AU.assert_equals('transaction_code', 'DPT_CWC', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'CWC', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '1121: Cash withdrawal by cheque', value_data_step_cash_description)
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
        AU.assert_equals('amount_cash_change', cheque_amount, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'C', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\">\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.cheque_amount\",0]}}", value_list_cash_condition)
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
        AU.assert_equals('condition', "{\"expression\":{\"func\":\">\",\"type\":\"boolean\",\"paras\":[\"$.execution_steps.[1].p2_content.response.data.total_ifc_fee_cash\",0]}}", value_list_cash_condition)
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
        AU.assert_equals('Number item in posting CASH', 4, len(data_actual_posting))
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
        AU.assert_equals('Amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        AU.assert_equals('Amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('TransTableName', 'CashList', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'CASH', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_cash, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # 'account_balances' - verify number items
        AU.assert_equals('Number item in account_balances', 3, len(data_account_balances))
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
        AU.assert_equals('amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_account_balances_amount)))
        AU.assert_equals('debit_or_credit', 'C', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)) + (Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)))), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # 'account_balances' - verify key response under array item 2
        AU.assert_exists(expected_key['account_balances'], data_account_balances[1])
        # 'account_balances' - get value under array item 2
        value_account_balances_account_number = data_account_balances[1]['account_number']
        value_account_balances_amount = data_account_balances[1]['amount']
        value_account_balances_debit_or_credit = data_account_balances[1]['debit_or_credit']
        value_account_balances_currency = data_account_balances[1]['currency']
        value_account_balances_available_balance = data_account_balances[1]['available_balance']
        value_account_balances_transaction_number = data_account_balances[1]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[1]['transaction_date']
        value_account_balances_description = data_account_balances[1]['description']
        # 'account_balances' - verify value under array item 2
        AU.assert_equals('account_number', account_number_saving, value_account_balances_account_number)
        AU.assert_equals('amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_account_balances_amount)))
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', (Decimal(str(amount_deposit_saving)) - Decimal(str(minimum_deposit_amount_saving))) - (Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)))), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # 'account_balances' - verify key response under array item 3
        AU.assert_exists(expected_key['account_balances'], data_account_balances[2])
        # 'account_balances' - get value under array item 3
        value_account_balances_account_number = data_account_balances[2]['account_number']
        value_account_balances_amount = data_account_balances[2]['amount']
        value_account_balances_debit_or_credit = data_account_balances[2]['debit_or_credit']
        value_account_balances_currency = data_account_balances[2]['currency']
        value_account_balances_available_balance = data_account_balances[2]['available_balance']
        value_account_balances_transaction_number = data_account_balances[2]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[2]['transaction_date']
        value_account_balances_description = data_account_balances[2]['description']
        # 'account_balances' - verify value under array item 3
        AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        AU.assert_equals('amount', cheque_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', 0, value_account_balances_available_balance)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_08_sp_dpt_cwc_019_success_current_account_status_normal_fund_transfer_add_fee(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        commission=300
        share_fee_01=0
        ifc_name_01='Deposit (MMK) For Same Region  (By Cash/Tr)'
        ifc_code_01=340
        payrate_01=100
        ifc_value_01=250
        value_type_01='F'
        ifc_amount_01=250
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='CSH'
        gl_account_ifcc_01='003303030100010101'
        share_fee_02=0
        ifc_name_02='Withdrawal (MMK) For Different Region  (By Cash)(Postage & Fax Charges)'
        ifc_code_02=345
        payrate_02=100
        ifc_value_02=50
        value_type_02='F'
        ifc_amount_02=50
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='CSH'
        gl_account_ifcc_02='003207050100010101'
        fee_data = [
            {
                "share_fee": share_fee_01,
                "ifc_name": ifc_name_01,
                "ifc_code": ifc_code_01,
                "payrate": payrate_01,
                "ifc_value": ifc_value_01,
                "value_type": value_type_01,
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
                "ifc_code": ifc_code_02,
                "payrate": payrate_02,
                "ifc_value": ifc_value_02,
                "value_type": value_type_02,
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
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open saving account
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
        # STEP 01-09: approve saving account
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
        # STEP 01-10: cash deposit to saving status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_cdp['data']['account_number'])
        # STEP 01-11: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            fee_data=fee_data,
            commission=commission,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_exists(expected_key['data_dpt_cwc'], data_actual['data'])
        # 'response' - verify key response under 'data' and 'withdrawer_description'
        AU.assert_exists(expected_key['data_dpt_cwc_withdrawer_description'], data_actual['data']['withdrawer_description'])
        # 'response' - get value under 'data'
        value_data_stock_prefix = data_actual['data']['stock_prefix']
        value_data_cheque_no = data_actual['data']['cheque_no']
        value_data_account_number = data_actual['data']['account_number']
        value_data_current_balance = data_actual['data']['current_balance']
        value_data_available_balance = data_actual['data']['available_balance']
        value_data_cheque_amount = data_actual['data']['cheque_amount']
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
        value_data_commission = data_actual['data']['commission']
        value_data_interest_from_earlywdr = data_actual['data']['interest_from_earlywdr']
        value_data_due_date = data_actual['data']['due_date']
        value_data_interest_prepaid = data_actual['data']['interest_prepaid']
        value_data_total_vat_for_cash = data_actual['data']['total_vat_for_cash']
        value_data_account_linkage = data_actual['data']['account_linkage']
        value_data_amount_linkage = data_actual['data']['amount_linkage']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_fee_data = data_actual['data']['fee_data']
        value_data_total_ifc_fee_cash = data_actual['data']['total_ifc_fee_cash']
        value_data_total_ifc_fee_deposit = data_actual['data']['total_ifc_fee_deposit']
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
        # 'response' - verify value under 'data'
        AU.assert_equals('stock_prefix', 'CQ', value_data_stock_prefix)
        AU.assert_equals('cheque_no', cheque_no, value_data_cheque_no)
        AU.assert_equals('account_number', account_number, value_data_account_number)
        AU.assert_null('current_balance', value_data_current_balance)
        AU.assert_null('available_balance', value_data_available_balance)
        AU.assert_equals('cheque_amount', cheque_amount, value_data_cheque_amount)
        AU.assert_equals('cash_currency', cash_currency, value_data_cash_currency)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_equals('cash_amount', 0, value_data_cash_amount)
        AU.assert_equals('exchange_rate', 1, value_data_exchange_rate)
        AU.assert_equals('cash_amount_bcy', 0, value_data_cash_amount_bcy)
        AU.assert_equals('withdrawer_name', account_name_individual, value_data_withdrawer_name)
        AU.assert_equals('withdrawer_id', customer_code_individual, value_data_withdrawer_id)
        AU.assert_equals('withdrawer_address', address, value_data_withdrawer_address)
        AU.assert_null('withdrawer_description_home', value_data_home)
        AU.assert_null('withdrawer_description_office', value_data_office)
        AU.assert_equals('id_issue_date', id_issue_date, value_data_id_issue_date)
        AU.assert_empty('id_place', value_data_id_place)
        AU.assert_empty('identification_number', value_data_identification_number)
        AU.assert_equals('currency_of_deposit_account', currency_of_deposit_account, value_data_currency_of_deposit_account)
        AU.assert_equals('exchange_rate_debit_account_bcy', 1, value_data_exchange_rate_debit_account_bcy)
        AU.assert_equals('amount_debit_account_bcy', 0, value_data_amount_debit_account_bcy)
        AU.assert_equals('commission', commission, value_data_commission)
        AU.assert_equals('interest_from_earlywdr', 0, value_data_interest_from_earlywdr)
        AU.assert_empty('due_date', value_data_due_date)
        AU.assert_equals('interest_prepaid', 0, value_data_interest_prepaid)
        AU.assert_equals('total_vat_for_cash', 0, value_data_total_vat_for_cash)
        AU.assert_equals('account_linkage', account_number_saving, value_data_account_linkage)
        AU.assert_equals('amount_linkage', 0, value_data_amount_linkage)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('total_ifc_fee_cash', commission, value_data_total_ifc_fee_cash)
        AU.assert_equals('total_ifc_fee_deposit', 0, value_data_total_ifc_fee_deposit)
        # AU.assert_not_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('auto_fund_trasfer', True, value_data_auto_fund_trasfer)
        AU.assert_equals('transaction_code', 'DPT_CWC', value_data_transaction_code)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'CWC', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_CWC', value_data_sub_code)
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
        AU.assert_equals('description', '1121: Cash withdrawal by cheque', value_data_description)
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
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        AU.assert_equals('Amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        # 'account_balances' - get data actual
        data_account_balances = RU.get_p2_content_account_balances_by_step_code(rs, step_code)
        print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # 'account_balances' - verify number items
        AU.assert_equals('Number item in account_balances', 3, len(data_account_balances))
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
        AU.assert_equals('amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_account_balances_amount)))
        AU.assert_equals('debit_or_credit', 'C', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)) + (Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)))), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # 'account_balances' - verify key response under array item 2
        AU.assert_exists(expected_key['account_balances'], data_account_balances[1])
        # 'account_balances' - get value under array item 2
        value_account_balances_account_number = data_account_balances[1]['account_number']
        value_account_balances_amount = data_account_balances[1]['amount']
        value_account_balances_debit_or_credit = data_account_balances[1]['debit_or_credit']
        value_account_balances_currency = data_account_balances[1]['currency']
        value_account_balances_available_balance = data_account_balances[1]['available_balance']
        value_account_balances_transaction_number = data_account_balances[1]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[1]['transaction_date']
        value_account_balances_description = data_account_balances[1]['description']
        # 'account_balances' - verify value under array item 2
        AU.assert_equals('account_number', account_number_saving, value_account_balances_account_number)
        AU.assert_equals('amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_account_balances_amount)))
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', (Decimal(str(amount_deposit_saving)) - Decimal(str(minimum_deposit_amount_saving))) - (Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)))), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # 'account_balances' - verify key response under array item 3
        AU.assert_exists(expected_key['account_balances'], data_account_balances[2])
        # 'account_balances' - get value under array item 3
        value_account_balances_account_number = data_account_balances[2]['account_number']
        value_account_balances_amount = data_account_balances[2]['amount']
        value_account_balances_debit_or_credit = data_account_balances[2]['debit_or_credit']
        value_account_balances_currency = data_account_balances[2]['currency']
        value_account_balances_available_balance = data_account_balances[2]['available_balance']
        value_account_balances_transaction_number = data_account_balances[2]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[2]['transaction_date']
        value_account_balances_description = data_account_balances[2]['description']
        # 'account_balances' - verify value under array item 3
        AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        AU.assert_equals('amount', cheque_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', 0, value_account_balances_available_balance)
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
        AU.assert_equals('transaction_code', 'DPT_CWC', value_data_step_cash_transaction_code)
        AU.assert_not_empty('transaction_number', value_data_step_cash_transaction_number)
        AU.assert_not_null('transaction_number', value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'CWC', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '1121: Cash withdrawal by cheque', value_data_step_cash_description)
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
        AU.assert_equals('amount_cash_change', cheque_amount, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'C', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\">\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.cheque_amount\",0]}}", value_list_cash_condition)
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
        AU.assert_equals('amount_cash_change', commission, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_of_deposit_account, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\">\",\"type\":\"boolean\",\"paras\":[\"$.execution_steps.[1].p2_content.response.data.total_ifc_fee_cash\",0]}}", value_list_cash_condition)
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
        AU.assert_equals('Number item in posting', 7, len(data_actual_posting))
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
        AU.assert_equals('Amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        AU.assert_equals('Amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_Amount)))
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_of_deposit_account, value_CurrencyCode)
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
        # 'postings' - verify key response, item 6
        AU.assert_exists(expected_key['postings'], data_actual_posting[5])
        # 'postings' - get value under array, item 6
        value_TransactionNumber = data_actual_posting[5]['TransactionNumber']
        value_TransTableName = data_actual_posting[5]['TransTableName']
        value_TransId = data_actual_posting[5]['TransId']
        value_SysAccountName = data_actual_posting[5]['SysAccountName']
        value_GLAccount = data_actual_posting[5]['GLAccount']
        value_DorC = data_actual_posting[5]['DorC']
        value_TransactionStatus = data_actual_posting[5]['TransactionStatus']
        value_Amount = data_actual_posting[5]['Amount']
        value_BranchCode = data_actual_posting[5]['BranchCode']
        value_CurrencyCode = data_actual_posting[5]['CurrencyCode']
        value_ValueDate = data_actual_posting[5]['ValueDate']
        value_Posted = data_actual_posting[5]['Posted']
        value_AccountingGroup = data_actual_posting[5]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[5]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[5]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[5]['BaseCurrencyAmount']
        value_Id = data_actual_posting[5]['Id']
        # 'postings' - verify value under array, item 6
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'CashList', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'CASH', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_cash, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', commission, value_Amount)
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
        # 'postings' - verify key response, item 7
        AU.assert_exists(expected_key['postings'], data_actual_posting[6])
        # 'postings' - get value under array, item 7
        value_TransactionNumber = data_actual_posting[6]['TransactionNumber']
        value_TransTableName = data_actual_posting[6]['TransTableName']
        value_TransId = data_actual_posting[6]['TransId']
        value_SysAccountName = data_actual_posting[6]['SysAccountName']
        value_GLAccount = data_actual_posting[6]['GLAccount']
        value_DorC = data_actual_posting[6]['DorC']
        value_TransactionStatus = data_actual_posting[6]['TransactionStatus']
        value_Amount = data_actual_posting[6]['Amount']
        value_BranchCode = data_actual_posting[6]['BranchCode']
        value_CurrencyCode = data_actual_posting[6]['CurrencyCode']
        value_ValueDate = data_actual_posting[6]['ValueDate']
        value_Posted = data_actual_posting[6]['Posted']
        value_AccountingGroup = data_actual_posting[6]['AccountingGroup']
        value_CrossBranchCode = data_actual_posting[6]['CrossBranchCode']
        value_CrossCurrencyCode = data_actual_posting[6]['CrossCurrencyCode']
        value_BaseCurrencyAmount = data_actual_posting[6]['BaseCurrencyAmount']
        value_Id = data_actual_posting[6]['Id']
        # 'postings' - verify value under array, item 7
        AU.assert_equals('TransactionNumber', value_data_transaction_number, value_TransactionNumber)
        AU.assert_equals('TransTableName', 'CashList', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'CASH', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_cash, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', cheque_amount, value_Amount)
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
        print(json.dumps(data_account_balances, indent=4, sort_keys=False))
        # 'account_balances' - verify number items
        AU.assert_equals('Number item in account_balances', 3, len(data_account_balances))
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
        AU.assert_equals('amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_account_balances_amount)))
        AU.assert_equals('debit_or_credit', 'C', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)) + (Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)))), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # 'account_balances' - verify key response under array item 2
        AU.assert_exists(expected_key['account_balances'], data_account_balances[1])
        # 'account_balances' - get value under array item 2
        value_account_balances_account_number = data_account_balances[1]['account_number']
        value_account_balances_amount = data_account_balances[1]['amount']
        value_account_balances_debit_or_credit = data_account_balances[1]['debit_or_credit']
        value_account_balances_currency = data_account_balances[1]['currency']
        value_account_balances_available_balance = data_account_balances[1]['available_balance']
        value_account_balances_transaction_number = data_account_balances[1]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[1]['transaction_date']
        value_account_balances_description = data_account_balances[1]['description']
        # 'account_balances' - verify value under array item 2
        AU.assert_equals('account_number', account_number_saving, value_account_balances_account_number)
        AU.assert_equals('amount', Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount))), Decimal(str(value_account_balances_amount)))
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', (Decimal(str(amount_deposit_saving)) - Decimal(str(minimum_deposit_amount_saving))) - (Decimal(str(cheque_amount))-(Decimal(str(amount_deposit)) - Decimal(str(minimum_deposit_amount)))), Decimal(str(value_account_balances_available_balance)))
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # 'account_balances' - verify key response under array item 3
        AU.assert_exists(expected_key['account_balances'], data_account_balances[2])
        # 'account_balances' - get value under array item 3
        value_account_balances_account_number = data_account_balances[2]['account_number']
        value_account_balances_amount = data_account_balances[2]['amount']
        value_account_balances_debit_or_credit = data_account_balances[2]['debit_or_credit']
        value_account_balances_currency = data_account_balances[2]['currency']
        value_account_balances_available_balance = data_account_balances[2]['available_balance']
        value_account_balances_transaction_number = data_account_balances[2]['transaction_number']
        value_account_balances_transaction_date = data_account_balances[2]['transaction_date']
        value_account_balances_description = data_account_balances[2]['description']
        # 'account_balances' - verify value under array item 3
        AU.assert_equals('account_number', account_number, value_account_balances_account_number)
        AU.assert_equals('amount', cheque_amount, value_account_balances_amount)
        AU.assert_equals('debit_or_credit', 'D', value_account_balances_debit_or_credit)
        AU.assert_equals('currency', currency_of_deposit_account, value_account_balances_currency)
        AU.assert_equals('available_balance', 0, value_account_balances_available_balance)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_account_balances_transaction_number)
        # AU.assert_equals('transaction_date', value_data_transaction_date, value_account_balances_transaction_date)
        AU.assert_equals('description', value_data_description, value_account_balances_description)
        # database - verify columns update - o9deposit - DepositAccount

    def test_08_sp_dpt_cwc_020_error_current_account_fund_transfer_master_account_status_closed(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # STEP 01-03: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-04: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-05: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-06: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-07: open saving account
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
        # STEP 01-08: approve saving account
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
        # STEP 01-09: cash deposit to saving status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_cdp['data']['account_number'])
        # STEP 01-10: close deposit account
        fields_data_cls = sp_payload.DPT_CLS(
            account_number=account_number,
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
        AU.assert_equals('account_number', account_number, data_dpt_cls['data']['account_number'])
        # STEP 01-11: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid deposit status [Closed]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_021_error_current_account_fund_transfer_master_account_status_block(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open saving account
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
        # STEP 01-09: approve saving account
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
        # STEP 01-10: cash deposit to saving status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_cdp['data']['account_number'])
        # STEP 01-11: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 01-12: block current account
        fields_data_blk = sp_payload.DPT_BLK(
            account_number=account_number,
            branch_name=branch_name,
            depositor_name=account_name_individual,
            depositor_id=customer_code_individual,
            depositor_address=address,
            depositor_currency=currency_of_deposit_account,
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
        AU.assert_equals('account_number', account_number, data_dpt_blk['data']['account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid deposit status [Block]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_022_error_current_account_fund_transfer_master_account_status_new(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open saving account
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
        # STEP 01-09: approve saving account
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
        # STEP 01-10: cash deposit to saving status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_cdp['data']['account_number'])
        # STEP 01-11: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number}] of account. Available balance must be more than [{cheque_amount}] - en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_023_error_current_account_fund_transfer_master_account_status_dormant(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open saving account
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
        # STEP 01-09: approve saving account
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
        # STEP 01-10: cash deposit to saving status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_cdp['data']['account_number'])
        # STEP 01-11: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 01-12: change status from 'Normal' to 'Dormant' of current account
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
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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

    def test_08_sp_dpt_cwc_024_error_current_account_fund_transfer_link_account_is_current(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_current=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open current account
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
        # STEP 01-09: approve current account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number_current,
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
        AU.assert_equals('account_number', account_number_current, data_dpt_apr['data']['account_number'])
        # STEP 01-10: cash deposit to current status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_current,
            amount_deposit=amount_deposit_current,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_current, data_dpt_cdp['data']['account_number'])
        # STEP 01-11: add linkage 'Auto fund transfer" current account and current account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_current,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_current, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_current
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number}] of account. Available balance must be more than [{cheque_amount}] - en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_025_error_current_account_fund_transfer_link_account_status_closed(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # STEP 01-03: cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open saving account
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
        # STEP 01-09: approve saving account
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
        # STEP 01-10: close deposit saving account
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
        # STEP 01-11: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid deposit status [Closed]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_026_error_current_account_fund_transfer_link_account_status_block(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open saving account
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
        # STEP 01-09: approve saving account
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
        # STEP 01-10: cash deposit to saving status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_cdp['data']['account_number'])
        # STEP 01-11: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 01-12: block saving account
        fields_data_blk = sp_payload.DPT_BLK(
            account_number=account_number_saving,
            branch_name=branch_name,
            depositor_name=account_name_individual,
            depositor_id=customer_code_individual,
            depositor_address=address,
            depositor_currency=currency_of_deposit_account,
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
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid deposit status [Block]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_027_error_current_account_fund_transfer_link_account_status_pending(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open saving account
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
        # STEP 01-09: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number}] of account. Available balance must be more than [{cheque_amount}] - en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_028_error_current_account_fund_transfer_link_account_status_new(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open saving account
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
        # STEP 01-09: approve saving account
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
        # STEP 01-10: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number}] of account. Available balance must be more than [{cheque_amount}] - en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_08_sp_dpt_cwc_029_error_current_account_fund_transfer_link_account_status_dormant(self, user):
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount=1000
        amount_deposit=1000000.45
        amount_deposit_saving=1003000.39
        cheque_amount=2000000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = cheque_no = generated_numbers
        sp_helper = StoredProcedureHelper(user)
        # STEP 01-01: Open current account
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
        # STEP 01-02: Approve current account
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
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-03: Cash deposit
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cdp['data']['account_number'])
        # database - query for next step - deposit
        # database - query for next step - accounting
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_SRG(fields_data)
        step_code = 'DPT_SRG'
        # 'response' - get data actual
        data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_srg['status'])
        # 'response' - get value 'account_number' under 'data'
        AU.assert_exists('from_serial', data_dpt_srg['data'])
        AU.assert_exists('to_serial', data_dpt_srg['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
        # STEP 01-05: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code
        )
        rs = sp_helper.DPT_SAT(fields_data)
        step_code = 'DPT_SAT'
        # 'response' - get data actual
        data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sat['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
        # STEP 01-06: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix
        )
        rs = sp_helper.DPT_CCR(fields_data)
        step_code = 'DPT_CCR'
        # 'response' - get data actual
        data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_ccr['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('from_serial', data_dpt_ccr['data'])
        AU.assert_exists('to_serial', data_dpt_ccr['data'])
        AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
        AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
        # STEP 01-07: Cheque book issued
        fields_data_cis = sp_payload.DPT_CIS(
            account_number=account_number,
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            branch_name=branch_name
        )
        rs = sp_helper.DPT_CIS(fields_data_cis)
        step_code = 'DPT_CIS'
        # 'response' - get data actual
        data_dpt_cis = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cis, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cis['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_cis['data']['account_number'])
        # STEP 01-08: open saving account
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
        # STEP 01-09: approve saving account
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
        # STEP 01-10: cash deposit to saving status 'New'
        fields_data_cdp = sp_payload.DPT_CDP(
            account_number=account_number_saving,
            amount_deposit=amount_deposit_saving,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=address,
            values_date=value_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_of_deposit_account
        )
        rs = sp_helper.DPT_CDP(fields_data_cdp)
        step_code = 'DPT_CDP'
        # 'response' - get data actual
        data_dpt_cdp = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_cdp, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_cdp['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number_saving, data_dpt_cdp['data']['account_number'])
        # STEP 01-11: add linkage 'Auto fund transfer" current account and saving account
        fields_data_opal = sp_payload.DPT_OPAL(
            master_account_number=account_number,
            master_account_name=account_name_individual,
            linkage_account_number=account_number_saving,
            linkage_account_name=account_name_individual,
            branch_code=user_service['branch_code']
        )
        rs = sp_helper.DPT_OPAL(fields_data_opal)
        step_code = 'DPT_OPAL'
        # 'response' - get data actual
        data_dpt_opal = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opal, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_opal['status'])
        # 'response' - verify value under 'data'
        AU.assert_equals('master_account_number', account_number, data_dpt_opal['data']['master_account_number'])
        AU.assert_equals('linkage_account_number', account_number_saving, data_dpt_opal['data']['list_account_linkage'][0]['linkage_account_number'])
        # STEP 01-12: change status from 'Normal' to 'Dormant' of saving account
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
        # STEP 02: Cash withdrawal by cheque
        fields_data = sp_payload.DPT_CWC(
            stock_prefix=stock_prefix,
            cheque_no=cheque_no,
            account_number=account_number,
            cheque_amount=cheque_amount,
            cash_currency=cash_currency,
            withdrawer_name=account_name_individual,
            withdrawer_id=customer_code_individual,
            withdrawer_address=address,
            id_issue_date=id_issue_date,
            value_date=value_date,
            currency_of_deposit_account=currency_of_deposit_account,
            branch_name=branch_name,
            account_linkage=account_number_saving
        )
        rs = sp_helper.DPT_CWC(fields_data)
        step_code = 'DPT_CWC'
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
        AU.assert_equals('error_message', f'Invalid available balance [{account_number}] of account. Available balance must be more than [{cheque_amount}] - en', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def check_serial_number_not_exist(self, user, generated_number):
        sp_helper = StoredProcedureHelper(user)
        # search serial_number
        fields_data_search = sp_payload.DPT_ADSEARCH_STOCKINVENTORY(
            stock_prefix=stock_prefix,
            from_serial_from=generated_number,
            from_serial_to=generated_number
        )
        rs = sp_helper.DPT_ADSEARCH_STOCKINVENTORY(fields_data_search)
        step_code = 'DPT_ADSEARCH_STOCKINVENTORY'
        # 'response' - get data actual
        data_stk_search = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_stk_search, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_stk_search['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('items', data_stk_search['data'])
        if len(data_stk_search['data']['items']) == 0:
            return True
        else:
            return False

    def gen_serial_number(self, user):
        while True:
            # Generate a random number with the desired format
            generated_number = f"8{random.randint(0, 99999):05}"
            # Check if the generated number exists; if not, break the loop
            if self.check_serial_number_not_exist(user, generated_number):
                break
        generated_number = f"{stock_prefix}{generated_number}"
        return generated_number
