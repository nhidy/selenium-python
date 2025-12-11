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
debit_accounting_valid='003101010333333301'
deposit_currency='MMK'
accounting_currency='MMK'
accounting_currency1='MMK'
address='27, Nguyen huu tho, Tan Hung, Q7'
values_date=user_service['working_date']
branch_code=user_service['branch_code']
gl_account_cash='003101030100010101'
cash_currency='MMK'
id_issue_date=user_service['working_date']
value_date=user_service['working_date']
currency_of_deposit_account='MMK'

# data test valid
branch_name='003 - Bayint Naung Branch'
stock_prefix='FB'
stock_type='F'
assigned_staff_code=user_service['username']
currency_code='MMK'

# data test invalid

# data test trên 104
step_code_cash='CSH_UPDATE_CASH'

# # data test trên 198
# step_code_cash='CSH_UPDATE_CASH_SP'

@pytest.fixture(scope='session')
def user():
    req = RU(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_FBI
class Test_SP_DPT_FBI(object):

    # def test_sp_dpt_fbi_001_success(self, user):
    #     sp_helper = StoredProcedureHelper(user)
    #     fee_data = [
    #         {
    #             "share_fee": 0.0,
    #             "ifc_name": "Deposit (MMK) For Different Region (By Cash/Tr)(Postage & Fax Charges)",
    #             "ifc_code": 344,
    #             "payrate": 100,
    #             "ifc_value": 500.0,
    #             "ifc_amount": 500.0,
    #             "currency_account_code": "MMK",
    #             "floor_value": 0.0,
    #             "ceiling_value": 0.0,
    #             "value_type": "F",
    #             "share_rate": 0.0,
    #             "share_amount": 0.0,
    #             "round_rate": 0.0,
    #             "round_amount": 0.0,
    #             "currency_fee_code": "MMK",
    #             "pay_source": "DPT"
    #         },
    #         {
    #             "share_fee": 0.0,
    #             "ifc_name": "Deposit (MMK) For Same Region  (By Cash/Tr)",
    #             "ifc_code": 340,
    #             "payrate": 100,
    #             "ifc_value": 350.45,
    #             "ifc_amount": 350.45,
    #             "currency_account_code": "MMK",
    #             "floor_value": 0.0,
    #             "ceiling_value": 0.0,
    #             "value_type": "F",
    #             "share_rate": 0.0,
    #             "share_amount": 0.0,
    #             "round_rate": 0.0,
    #             "round_amount": 0.0,
    #             "currency_fee_code": "MMK",
    #             "pay_source": "DPT"
    #         }
    #     ]
    #     fields_data = sp_payload.DPT_FBI(
    #         branch_name=branch_name,
    #         account_number=account_number,
    #         serial_no=serial_no,
    #         description=description,
    #         currency_code=currency_code,
    #         stock_prefix=stock_prefix,
    #         fee_data=fee_data,
    #         account_number_for_fee=account_number_for_fee,
    #         method=method
    #     )
    #     rs = sp_helper.DPT_FBI(fields_data)
    #     step_code = 'DPT_FBI'
    #     data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual, indent=4, sort_keys=False))
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_001_success_fixed_deposit_account_status_new_no_passbook(self, user):
    #     sp_helper = StoredProcedureHelper(user)
    #     catalog_code='FD06PIMMK'
    #     catalog_name='Fixed deposit 6 months (Principal plus interest rollover) in MMK'
    #     deposit_type='Fixed Deposit'
    #     deposit_sub_type='T3'
    #     deposit_purpose='S'
    #     rollover='A'
    #     auto_transfer_option='N'
    #     minimum_deposit_amount=0
    #     amount_deposit=200000.45
    #     method='CSH'
    #     generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
    #     print('generated_numbers: ', generated_numbers)
    #     from_serial = to_serial = serial_no = generated_numbers
    #     # STEP 01-01: Open fixed deposit account
    #     fields_data_opn = sp_payload.DPT_OPN(
    #         customer_code=customer_code_individual,
    #         catalog_code=catalog_code,
    #         catalog_name=catalog_name,
    #         deposit_type=deposit_type,
    #         account_name=account_name_individual,
    #         deposit_sub_type=deposit_sub_type,
    #         deposit_purpose=deposit_purpose,
    #         rollover=rollover,
    #         auto_transfer_option=auto_transfer_option
    #     )
    #     rs = sp_helper.DPT_OPN(fields_data_opn)
    #     step_code = 'DPT_OPN'
    #     # 'response' - get data actual
    #     data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_opn['status'])
    #     # 'response' - get value 'account_number' under 'data'
    #     AU.assert_exists('account_number', data_dpt_opn['data'])
    #     AU.assert_exists('account_chart_number', data_dpt_opn['data'])
    #     account_number = data_dpt_opn['data']['account_number']
    #     gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
    #     # STEP 01-02: Approve fixed deposit account
    #     fields_data_apr = sp_payload.DPT_APR(
    #         account_number=account_number,
    #         branch_name=branch_name,
    #         account_holder_name=account_name_individual,
    #         catalog_code=catalog_code,
    #         deposit_sub_type=deposit_sub_type,
    #         deposit_type='T',
    #         catalogue_name=catalog_name,
    #         created_by=user_service['username']
    #     )
    #     rs = sp_helper.DPT_APR(fields_data_apr)
    #     step_code = 'DPT_APR'
    #     # 'response' - get data actual
    #     data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_apr['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
    #     # STEP 01-03: Stock registration
    #     fields_data = sp_payload.DPT_SRG(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_SRG(fields_data)
    #     step_code = 'DPT_SRG'
    #     # 'response' - get data actual
    #     data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_srg['status'])
    #     # 'response' - get value 'account_number' under 'data'
    #     AU.assert_exists('from_serial', data_dpt_srg['data'])
    #     AU.assert_exists('to_serial', data_dpt_srg['data'])
    #     AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
    #     AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
    #     # STEP 01-04: Stock assigned to teller
    #     fields_data = sp_payload.DPT_SAT(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         assigned_staff_code=assigned_staff_code,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_SAT(fields_data)
    #     step_code = 'DPT_SAT'
    #     # 'response' - get data actual
    #     data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_sat['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
    #     # STEP 01-05: Stock confirm received
    #     fields_data = sp_payload.DPT_CCR(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_CCR(fields_data)
    #     step_code = 'DPT_CCR'
    #     # 'response' - get data actual
    #     data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_ccr['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_exists('from_serial', data_dpt_ccr['data'])
    #     AU.assert_exists('to_serial', data_dpt_ccr['data'])
    #     AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
    #     AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
    #     # STEP 02: Fixed deposit book issue
    #     fields_data = sp_payload.DPT_FBI(
    #         account_number=account_number,
    #         branch_name=branch_name,
    #         serial_no=serial_no,
    #         stock_prefix=stock_prefix,
    #         currency_code=currency_code,
    #         method=method
    #     )
    #     rs = sp_helper.DPT_FBI(fields_data)
    #     step_code = 'DPT_FBI'
    #     # 'response' - get data actual
    #     data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual, indent=4, sort_keys=False))
    #     # 'response' - verify key response level 1
    #     AU.assert_exists(expected_key['level_01'], data_actual)
    #     # 'response' - get value level 1
    #     value_status = data_actual['status']
    #     value_error_message = data_actual['error_message']
    #     value_error_code = data_actual['error_code']
    #     value_data = data_actual['data']
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, value_status)
    #     AU.assert_empty('error_message', value_error_message)
    #     AU.assert_empty('error_code', value_error_code)
    #     AU.assert_not_null('data', value_data)
    #     # 'response' - verify key response under 'data'
    #     AU.assert_exists(expected_key['data_dpt_fbi'], data_actual['data'])
    #     # 'response' - get value under 'data'
    #     value_data_stock_type = data_actual['data']['stock_type']
    #     value_data_account_number = data_actual['data']['account_number']
    #     value_data_serial_no = data_actual['data']['serial_no']
    #     value_data_stock_prefix = data_actual['data']['stock_prefix']
    #     value_data_method = data_actual['data']['method']
    #     value_data_account_number_for_fee = data_actual['data']['account_number_for_fee']
    #     value_data_currency_code = data_actual['data']['currency_code']
    #     value_data_branch_name = data_actual['data']['branch_name']
    #     value_data_total_fee = data_actual['data']['total_fee']
    #     value_data_fee_data = data_actual['data']['fee_data']
    #     value_data_transaction_code = data_actual['data']['transaction_code']
    #     value_data_transaction_number = data_actual['data']['transaction_number']
    #     value_data_transaction_type = data_actual['data']['transaction_type']
    #     value_data_sub_code = data_actual['data']['sub_code']
    #     value_data_transaction_date = data_actual['data']['transaction_date']
    #     value_data_service_sys_date = data_actual['data']['service_sys_date']
    #     value_data_reference_id = data_actual['data']['reference_id']
    #     value_data_ref_id = data_actual['data']['ref_id']
    #     value_data_reference_code = data_actual['data']['reference_code']
    #     value_data_business_code = data_actual['data']['business_code']
    #     value_data_value_date = data_actual['data']['value_date']
    #     value_data_current_user_code = data_actual['data']['current_user_code']
    #     value_data_current_branch_code = data_actual['data']['current_branch_code']
    #     value_data_current_username = data_actual['data']['current_username']
    #     value_data_current_loginname = data_actual['data']['current_loginname']
    #     value_data_user_approve = data_actual['data']['user_approve']
    #     value_data_status = data_actual['data']['status']
    #     value_data_is_reverse = data_actual['data']['is_reverse']
    #     value_data_amount1 = data_actual['data']['amount1']
    #     value_data_description = data_actual['data']['description']
    #     value_data_token = data_actual['data']['token']
    #     value_data_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
    #     value_data_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('stock_type', stock_type, value_data_stock_type)
    #     AU.assert_equals('account_number', account_number, value_data_account_number)
    #     AU.assert_equals('serial_no', serial_no, value_data_serial_no)
    #     AU.assert_equals('stock_prefix', stock_prefix, value_data_stock_prefix)
    #     AU.assert_equals('method', method, value_data_method)
    #     AU.assert_equals('account_number_for_fee', '', value_data_account_number_for_fee)
    #     AU.assert_equals('currency_code', currency_code, value_data_currency_code)
    #     AU.assert_equals('branch_name', branch_name, value_data_branch_name)
    #     AU.assert_equals('total_fee', 0, value_data_total_fee)
    #     AU.assert_equals('fee_data', [], value_data_fee_data)
    #     AU.assert_equals('transaction_code', 'DPT_FBI', value_data_transaction_code)
    #     AU.assert_not_null('transaction_number', value_data_transaction_number)
    #     AU.assert_not_empty('transaction_number', value_data_transaction_number)
    #     AU.assert_equals('transaction_type', 'FBI', value_data_transaction_type)
    #     AU.assert_equals('sub_code', 'DPT_FBI', value_data_sub_code)
    #     AU.assert_not_null('transaction_date', value_data_transaction_date)
    #     AU.assert_not_empty('transaction_date', value_data_transaction_date)
    #     AU.assert_not_null('service_sys_date', value_data_service_sys_date)
    #     AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
    #     AU.assert_not_null('reference_id', value_data_reference_id)
    #     AU.assert_not_empty('reference_id', value_data_reference_id)
    #     AU.assert_not_null('ref_id', value_data_ref_id)
    #     AU.assert_not_empty('ref_id', value_data_ref_id)
    #     AU.assert_empty('reference_code', value_data_reference_code)
    #     AU.assert_empty('business_code', value_data_business_code)
    #     AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
    #     AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
    #     AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
    #     AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
    #     AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
    #     AU.assert_empty('user_approve', value_data_user_approve)
    #     AU.assert_equals('status', 'N', value_data_status)
    #     AU.assert_equals('is_reverse',  False, value_data_is_reverse)
    #     AU.assert_equals('amount1', 0, value_data_amount1)
    #     AU.assert_equals('description', '11804: Fixed deposit book issue', value_data_description)
    #     AU.assert_equals('token', '*', value_data_token)
    #     AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
    #     AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
    #     # 'postings' - get data actual
    #     data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
    #     # verify step CASH
    #     step_code = step_code_cash
    #     # 'response' - get data actual - step CASH
    #     data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual, indent=4, sort_keys=False))
    #     # 'response' - verify key response level 1
    #     AU.assert_exists(expected_key['level_01'], data_actual)
    #     # 'response' - get value level 1
    #     value_status = data_actual['status']
    #     value_error_message = data_actual['error_message']
    #     value_error_code = data_actual['error_code']
    #     value_data = data_actual['data']
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, value_status)
    #     AU.assert_empty('error_message', value_error_message)
    #     AU.assert_empty('error_code', value_error_code)
    #     AU.assert_not_null('data', value_data)
    #     # 'response' - verify key response under 'data'
    #     AU.assert_exists(expected_key['data_step_cash'], data_actual['data'])
    #     # 'response' - get value under 'data'
    #     value_data_step_cash_list_cash = data_actual['data']['list_cash']
    #     value_data_step_cash_list_cash_from_response = data_actual['data']['list_cash_from_response']
    #     value_data_step_cash_transaction_code = data_actual['data']['transaction_code']
    #     value_data_step_cash_transaction_number = data_actual['data']['transaction_number']
    #     value_data_step_cash_transaction_type = data_actual['data']['transaction_type']
    #     value_data_step_cash_sub_code = data_actual['data']['sub_code']
    #     value_data_step_cash_transaction_date = data_actual['data']['transaction_date']
    #     value_data_step_cash_service_sys_date = data_actual['data']['service_sys_date']
    #     value_data_step_cash_reference_id = data_actual['data']['reference_id']
    #     value_data_step_cash_ref_id = data_actual['data']['ref_id']
    #     value_data_step_cash_reference_code = data_actual['data']['reference_code']
    #     value_data_step_cash_business_code = data_actual['data']['business_code']
    #     value_data_step_cash_value_date = data_actual['data']['value_date']
    #     value_data_step_cash_current_user_code = data_actual['data']['current_user_code']
    #     value_data_step_cash_current_branch_code = data_actual['data']['current_branch_code']
    #     value_data_step_cash_current_username = data_actual['data']['current_username']
    #     value_data_step_cash_current_loginname = data_actual['data']['current_loginname']
    #     value_data_step_cash_user_approve = data_actual['data']['user_approve']
    #     value_data_step_cash_status = data_actual['data']['status']
    #     value_data_step_cash_is_reverse = data_actual['data']['is_reverse']
    #     value_data_step_cash_amount1 = data_actual['data']['amount1']
    #     value_data_step_cash_description = data_actual['data']['description']
    #     value_data_step_cash_token = data_actual['data']['token']
    #     value_data_step_cash_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
    #     value_data_step_cash_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
    #     # 'response' - verify value under 'data'
    #     AU.assert_not_equals('list_cash', [], value_data_step_cash_list_cash)
    #     AU.assert_not_empty('list_cash', [], value_data_step_cash_list_cash)
    #     AU.assert_equals('list_cash_from_response', [], value_data_step_cash_list_cash_from_response)
    #     AU.assert_equals('transaction_code', 'DPT_FBI', value_data_step_cash_transaction_code)
    #     AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
    #     AU.assert_equals('transaction_type', 'FBI', value_data_step_cash_transaction_type)
    #     AU.assert_equals('sub_code', step_code_cash, value_data_step_cash_sub_code)
    #     AU.assert_not_null('transaction_date', value_data_step_cash_transaction_date)
    #     AU.assert_not_empty('transaction_date', value_data_step_cash_transaction_date)
    #     AU.assert_not_null('service_sys_date', value_data_step_cash_service_sys_date)
    #     AU.assert_not_empty('service_sys_date', value_data_step_cash_service_sys_date)
    #     AU.assert_not_null('reference_id', value_data_step_cash_reference_id)
    #     AU.assert_not_empty('reference_id', value_data_step_cash_reference_id)
    #     AU.assert_not_null('ref_id', value_data_step_cash_ref_id)
    #     AU.assert_not_empty('ref_id', value_data_step_cash_ref_id)
    #     AU.assert_empty('reference_code', value_data_step_cash_reference_code)
    #     AU.assert_empty('business_code', value_data_step_cash_business_code)
    #     AU.assert_equals('value_date', user_service['working_date'], value_data_step_cash_value_date)
    #     AU.assert_equals('current_user_code', user_service['username'], value_data_step_cash_current_user_code)
    #     AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_step_cash_current_branch_code)
    #     AU.assert_equals('current_username', user_service['fullname'], value_data_step_cash_current_username)
    #     AU.assert_equals('current_loginname', user_service['username'], value_data_step_cash_current_loginname)
    #     AU.assert_empty('user_approve', value_data_step_cash_user_approve)
    #     AU.assert_equals('status', 'N', value_data_step_cash_status)
    #     AU.assert_equals('is_reverse',  False, value_data_step_cash_is_reverse)
    #     AU.assert_equals('amount1', 0, value_data_step_cash_amount1)
    #     AU.assert_equals('description', '11804: Fixed deposit book issue', value_data_step_cash_description)
    #     AU.assert_equals('token', '*', value_data_step_cash_token)
    #     AU.assert_equals('is_transaction_reverse',  False, value_data_step_cash_is_transaction_reverse)
    #     AU.assert_equals('is_transaction_compensated',  False, value_data_step_cash_is_transaction_compensated)
    #     # 'response' - verify item under 'data' and 'list_cash'
    #     AU.assert_equals('Number item in list_cash', 1, len(data_actual['data']['list_cash']))
    #     # 'response' - verify key response under 'data' and 'list_cash', item 1
    #     AU.assert_exists(expected_key['data_list_cash'], data_actual['data']['list_cash'][0])
    #     # 'response' - get value under 'data' and 'list_cash', item 1
    #     value_list_cash_amount_cash_change = data_actual['data']['list_cash'][0]['amount_cash_change']
    #     value_list_cash_base_amount = data_actual['data']['list_cash'][0]['base_amount']
    #     value_list_cash_debit_or_credit = data_actual['data']['list_cash'][0]['debit_or_credit']
    #     value_list_cash_currency_code = data_actual['data']['list_cash'][0]['currency_code']
    #     value_list_cash_condition = data_actual['data']['list_cash'][0]['condition']
    #     value_list_cash_posting = data_actual['data']['list_cash'][0]['posting']
    #     value_list_cash_accounting_group = data_actual['data']['list_cash'][0]['accounting_group']
    #     value_list_cash_transaction_code = data_actual['data']['list_cash'][0]['transaction_code']
    #     value_list_cash_transaction_number = data_actual['data']['list_cash'][0]['transaction_number']
    #     value_list_cash_transaction_type = data_actual['data']['list_cash'][0]['transaction_type']
    #     value_list_cash_sub_code = data_actual['data']['list_cash'][0]['sub_code']
    #     value_list_cash_transaction_date = data_actual['data']['list_cash'][0]['transaction_date']
    #     value_list_cash_service_sys_date = data_actual['data']['list_cash'][0]['service_sys_date']
    #     value_list_cash_reference_id = data_actual['data']['list_cash'][0]['reference_id']
    #     value_list_cash_ref_id = data_actual['data']['list_cash'][0]['ref_id']
    #     value_list_cash_reference_code = data_actual['data']['list_cash'][0]['reference_code']
    #     value_list_cash_business_code = data_actual['data']['list_cash'][0]['business_code']
    #     value_list_cash_value_date = data_actual['data']['list_cash'][0]['value_date']
    #     value_list_cash_current_user_code = data_actual['data']['list_cash'][0]['current_user_code']
    #     value_list_cash_current_branch_code = data_actual['data']['list_cash'][0]['current_branch_code']
    #     value_list_cash_current_username = data_actual['data']['list_cash'][0]['current_username']
    #     value_list_cash_current_loginname = data_actual['data']['list_cash'][0]['current_loginname']
    #     value_list_cash_user_approve = data_actual['data']['list_cash'][0]['user_approve']
    #     value_list_cash_status = data_actual['data']['list_cash'][0]['status']
    #     value_list_cash_is_reverse = data_actual['data']['list_cash'][0]['is_reverse']
    #     value_list_cash_amount1 = data_actual['data']['list_cash'][0]['amount1']
    #     value_list_cash_description = data_actual['data']['list_cash'][0]['description']
    #     value_list_cash_token = data_actual['data']['list_cash'][0]['token']
    #     value_list_cash_is_transaction_reverse = data_actual['data']['list_cash'][0]['is_transaction_reverse']
    #     value_list_cash_is_transaction_compensated = data_actual['data']['list_cash'][0]['is_transaction_compensated']
    #     # 'response' - verify value under 'data' and 'list_cash', item 1
    #     AU.assert_equals('amount_cash_change', 0, value_list_cash_amount_cash_change)
    #     AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
    #     AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
    #     AU.assert_equals('currency_code', currency_code, value_list_cash_currency_code)
    #     AU.assert_equals('condition', "{\"expression\":{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}}", value_list_cash_condition)
    #     AU.assert_equals('posting', False, value_list_cash_posting)
    #     AU.assert_equals('accounting_group', 2, value_list_cash_accounting_group)
    #     AU.assert_null('transaction_code', value_list_cash_transaction_code)
    #     AU.assert_null('transaction_number', value_list_cash_transaction_number)
    #     AU.assert_null('transaction_type', value_list_cash_transaction_type)
    #     AU.assert_null('sub_code', value_list_cash_sub_code)
    #     AU.assert_equals('transaction_date', '0001-01-01T00:00:00', value_list_cash_transaction_date)
    #     AU.assert_equals('service_sys_date', '0001-01-01T00:00:00', value_list_cash_service_sys_date)
    #     AU.assert_null('reference_id', value_list_cash_reference_id)
    #     AU.assert_null('ref_id', value_list_cash_ref_id)
    #     AU.assert_null('reference_code', value_list_cash_reference_code)
    #     AU.assert_null('business_code', value_list_cash_business_code)
    #     AU.assert_equals('value_date', '0001-01-01T00:00:00', value_list_cash_value_date)
    #     AU.assert_null('current_user_code', value_list_cash_current_user_code)
    #     AU.assert_null('current_branch_code', value_list_cash_current_branch_code)
    #     AU.assert_null('current_username', value_list_cash_current_username)
    #     AU.assert_null('current_loginname', value_list_cash_current_loginname)
    #     AU.assert_null('user_approve', value_list_cash_user_approve)
    #     AU.assert_null('status', value_list_cash_status)
    #     AU.assert_equals('is_reverse', False, value_list_cash_is_reverse)
    #     AU.assert_equals('amount1', 0, value_list_cash_amount1)
    #     AU.assert_null('description', value_list_cash_description)
    #     AU.assert_null('token', value_list_cash_token)
    #     AU.assert_equals('is_transaction_reverse', False, value_list_cash_is_transaction_reverse)
    #     AU.assert_equals('is_transaction_compensated', False, value_list_cash_is_transaction_compensated)
    #     # 'postings' - get data actual - step CASH
    #     data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual_posting, indent=4, sort_keys=False))

    # def test_11_sp_dpt_fbi_002_success_fixed_deposit_account_status_normal_no_passbook(self, user):
    #     sp_helper = StoredProcedureHelper(user)
    #     catalog_code='FD06PIMMK'
    #     catalog_name='Fixed deposit 6 months (Principal plus interest rollover) in MMK'
    #     deposit_type='Fixed Deposit'
    #     deposit_sub_type='T3'
    #     deposit_purpose='S'
    #     rollover='A'
    #     auto_transfer_option='N'
    #     minimum_deposit_amount=0
    #     amount_deposit=200000.45
    #     method='CSH'
    #     generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
    #     print('generated_numbers: ', generated_numbers)
    #     from_serial = to_serial = serial_no = generated_numbers
    #     # STEP 01-01: Open fixed deposit account
    #     fields_data_opn = sp_payload.DPT_OPN(
    #         customer_code=customer_code_individual,
    #         catalog_code=catalog_code,
    #         catalog_name=catalog_name,
    #         deposit_type=deposit_type,
    #         account_name=account_name_individual,
    #         deposit_sub_type=deposit_sub_type,
    #         deposit_purpose=deposit_purpose,
    #         rollover=rollover,
    #         auto_transfer_option=auto_transfer_option
    #     )
    #     rs = sp_helper.DPT_OPN(fields_data_opn)
    #     step_code = 'DPT_OPN'
    #     # 'response' - get data actual
    #     data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_opn['status'])
    #     # 'response' - get value 'account_number' under 'data'
    #     AU.assert_exists('account_number', data_dpt_opn['data'])
    #     AU.assert_exists('account_chart_number', data_dpt_opn['data'])
    #     account_number = data_dpt_opn['data']['account_number']
    #     gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
    #     # STEP 01-02: Approve fixed deposit account
    #     fields_data_apr = sp_payload.DPT_APR(
    #         account_number=account_number,
    #         branch_name=branch_name,
    #         account_holder_name=account_name_individual,
    #         catalog_code=catalog_code,
    #         deposit_sub_type=deposit_sub_type,
    #         deposit_type='T',
    #         catalogue_name=catalog_name,
    #         created_by=user_service['username']
    #     )
    #     rs = sp_helper.DPT_APR(fields_data_apr)
    #     step_code = 'DPT_APR'
    #     # 'response' - get data actual
    #     data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_apr['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
    #     # STEP 01-03: Deposit money
    #     fields_data_mdp = sp_payload.DPT_MDP(
    #         account_number=account_number,
    #         amount_deposit=amount_deposit,
    #         debit_accounting=debit_accounting_valid,
    #         branch_name=branch_name,
    #         accounting_currency=accounting_currency,
    #         depositor_name=account_name_individual,
    #         depositor_code=customer_code_individual,
    #         depositor_address=address,
    #         values_date=values_date,
    #         deposit_currency=deposit_currency,
    #         accounting_currency1=accounting_currency1
    #     )
    #     rs = sp_helper.DPT_MDP(fields_data_mdp)
    #     step_code = 'DPT_MDP'
    #     # 'response' - get data actual
    #     data_dpt_mdp = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_mdp, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_mdp['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('account_number', account_number, data_dpt_mdp['data']['account_number'])
    #     # STEP 01-04: Stock registration
    #     fields_data = sp_payload.DPT_SRG(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_SRG(fields_data)
    #     step_code = 'DPT_SRG'
    #     # 'response' - get data actual
    #     data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_srg['status'])
    #     # 'response' - get value 'account_number' under 'data'
    #     AU.assert_exists('from_serial', data_dpt_srg['data'])
    #     AU.assert_exists('to_serial', data_dpt_srg['data'])
    #     AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
    #     AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
    #     # STEP 01-05: Stock assigned to teller
    #     fields_data = sp_payload.DPT_SAT(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         assigned_staff_code=assigned_staff_code,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_SAT(fields_data)
    #     step_code = 'DPT_SAT'
    #     # 'response' - get data actual
    #     data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_sat['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
    #     # STEP 01-06: Stock confirm received
    #     fields_data = sp_payload.DPT_CCR(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_CCR(fields_data)
    #     step_code = 'DPT_CCR'
    #     # 'response' - get data actual
    #     data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_ccr['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_exists('from_serial', data_dpt_ccr['data'])
    #     AU.assert_exists('to_serial', data_dpt_ccr['data'])
    #     AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
    #     AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
    #     # STEP 02: Fixed deposit book issue
    #     fields_data = sp_payload.DPT_FBI(
    #         account_number=account_number,
    #         branch_name=branch_name,
    #         serial_no=serial_no,
    #         stock_prefix=stock_prefix,
    #         currency_code=currency_code,
    #         method=method
    #     )
    #     rs = sp_helper.DPT_FBI(fields_data)
    #     step_code = 'DPT_FBI'
    #     # 'response' - get data actual
    #     data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual, indent=4, sort_keys=False))
    #     # 'response' - verify key response level 1
    #     AU.assert_exists(expected_key['level_01'], data_actual)
    #     # 'response' - get value level 1
    #     value_status = data_actual['status']
    #     value_error_message = data_actual['error_message']
    #     value_error_code = data_actual['error_code']
    #     value_data = data_actual['data']
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, value_status)
    #     AU.assert_empty('error_message', value_error_message)
    #     AU.assert_empty('error_code', value_error_code)
    #     AU.assert_not_null('data', value_data)
    #     # 'response' - verify key response under 'data'
    #     AU.assert_exists(expected_key['data_dpt_fbi'], data_actual['data'])
    #     # 'response' - get value under 'data'
    #     value_data_stock_type = data_actual['data']['stock_type']
    #     value_data_account_number = data_actual['data']['account_number']
    #     value_data_serial_no = data_actual['data']['serial_no']
    #     value_data_stock_prefix = data_actual['data']['stock_prefix']
    #     value_data_method = data_actual['data']['method']
    #     value_data_account_number_for_fee = data_actual['data']['account_number_for_fee']
    #     value_data_currency_code = data_actual['data']['currency_code']
    #     value_data_branch_name = data_actual['data']['branch_name']
    #     value_data_total_fee = data_actual['data']['total_fee']
    #     value_data_fee_data = data_actual['data']['fee_data']
    #     value_data_transaction_code = data_actual['data']['transaction_code']
    #     value_data_transaction_number = data_actual['data']['transaction_number']
    #     value_data_transaction_type = data_actual['data']['transaction_type']
    #     value_data_sub_code = data_actual['data']['sub_code']
    #     value_data_transaction_date = data_actual['data']['transaction_date']
    #     value_data_service_sys_date = data_actual['data']['service_sys_date']
    #     value_data_reference_id = data_actual['data']['reference_id']
    #     value_data_ref_id = data_actual['data']['ref_id']
    #     value_data_reference_code = data_actual['data']['reference_code']
    #     value_data_business_code = data_actual['data']['business_code']
    #     value_data_value_date = data_actual['data']['value_date']
    #     value_data_current_user_code = data_actual['data']['current_user_code']
    #     value_data_current_branch_code = data_actual['data']['current_branch_code']
    #     value_data_current_username = data_actual['data']['current_username']
    #     value_data_current_loginname = data_actual['data']['current_loginname']
    #     value_data_user_approve = data_actual['data']['user_approve']
    #     value_data_status = data_actual['data']['status']
    #     value_data_is_reverse = data_actual['data']['is_reverse']
    #     value_data_amount1 = data_actual['data']['amount1']
    #     value_data_description = data_actual['data']['description']
    #     value_data_token = data_actual['data']['token']
    #     value_data_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
    #     value_data_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('stock_type', stock_type, value_data_stock_type)
    #     AU.assert_equals('account_number', account_number, value_data_account_number)
    #     AU.assert_equals('serial_no', serial_no, value_data_serial_no)
    #     AU.assert_equals('stock_prefix', stock_prefix, value_data_stock_prefix)
    #     AU.assert_equals('method', method, value_data_method)
    #     AU.assert_equals('account_number_for_fee', '', value_data_account_number_for_fee)
    #     AU.assert_equals('currency_code', currency_code, value_data_currency_code)
    #     AU.assert_equals('branch_name', branch_name, value_data_branch_name)
    #     AU.assert_equals('total_fee', 0, value_data_total_fee)
    #     AU.assert_equals('fee_data', [], value_data_fee_data)
    #     AU.assert_equals('transaction_code', 'DPT_FBI', value_data_transaction_code)
    #     AU.assert_not_null('transaction_number', value_data_transaction_number)
    #     AU.assert_not_empty('transaction_number', value_data_transaction_number)
    #     AU.assert_equals('transaction_type', 'FBI', value_data_transaction_type)
    #     AU.assert_equals('sub_code', 'DPT_FBI', value_data_sub_code)
    #     AU.assert_not_null('transaction_date', value_data_transaction_date)
    #     AU.assert_not_empty('transaction_date', value_data_transaction_date)
    #     AU.assert_not_null('service_sys_date', value_data_service_sys_date)
    #     AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
    #     AU.assert_not_null('reference_id', value_data_reference_id)
    #     AU.assert_not_empty('reference_id', value_data_reference_id)
    #     AU.assert_not_null('ref_id', value_data_ref_id)
    #     AU.assert_not_empty('ref_id', value_data_ref_id)
    #     AU.assert_empty('reference_code', value_data_reference_code)
    #     AU.assert_empty('business_code', value_data_business_code)
    #     AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
    #     AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
    #     AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
    #     AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
    #     AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
    #     AU.assert_empty('user_approve', value_data_user_approve)
    #     AU.assert_equals('status', 'N', value_data_status)
    #     AU.assert_equals('is_reverse',  False, value_data_is_reverse)
    #     AU.assert_equals('amount1', 0, value_data_amount1)
    #     AU.assert_equals('description', '11804: Fixed deposit book issue', value_data_description)
    #     AU.assert_equals('token', '*', value_data_token)
    #     AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
    #     AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
    #     # 'postings' - get data actual
    #     data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
    #     # verify step CASH
    #     step_code = step_code_cash
    #     # 'response' - get data actual - step CASH
    #     data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual, indent=4, sort_keys=False))
    #     # 'response' - verify key response level 1
    #     AU.assert_exists(expected_key['level_01'], data_actual)
    #     # 'response' - get value level 1
    #     value_status = data_actual['status']
    #     value_error_message = data_actual['error_message']
    #     value_error_code = data_actual['error_code']
    #     value_data = data_actual['data']
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, value_status)
    #     AU.assert_empty('error_message', value_error_message)
    #     AU.assert_empty('error_code', value_error_code)
    #     AU.assert_not_null('data', value_data)
    #     # 'response' - verify key response under 'data'
    #     AU.assert_exists(expected_key['data_step_cash'], data_actual['data'])
    #     # 'response' - get value under 'data'
    #     value_data_step_cash_list_cash = data_actual['data']['list_cash']
    #     value_data_step_cash_list_cash_from_response = data_actual['data']['list_cash_from_response']
    #     value_data_step_cash_transaction_code = data_actual['data']['transaction_code']
    #     value_data_step_cash_transaction_number = data_actual['data']['transaction_number']
    #     value_data_step_cash_transaction_type = data_actual['data']['transaction_type']
    #     value_data_step_cash_sub_code = data_actual['data']['sub_code']
    #     value_data_step_cash_transaction_date = data_actual['data']['transaction_date']
    #     value_data_step_cash_service_sys_date = data_actual['data']['service_sys_date']
    #     value_data_step_cash_reference_id = data_actual['data']['reference_id']
    #     value_data_step_cash_ref_id = data_actual['data']['ref_id']
    #     value_data_step_cash_reference_code = data_actual['data']['reference_code']
    #     value_data_step_cash_business_code = data_actual['data']['business_code']
    #     value_data_step_cash_value_date = data_actual['data']['value_date']
    #     value_data_step_cash_current_user_code = data_actual['data']['current_user_code']
    #     value_data_step_cash_current_branch_code = data_actual['data']['current_branch_code']
    #     value_data_step_cash_current_username = data_actual['data']['current_username']
    #     value_data_step_cash_current_loginname = data_actual['data']['current_loginname']
    #     value_data_step_cash_user_approve = data_actual['data']['user_approve']
    #     value_data_step_cash_status = data_actual['data']['status']
    #     value_data_step_cash_is_reverse = data_actual['data']['is_reverse']
    #     value_data_step_cash_amount1 = data_actual['data']['amount1']
    #     value_data_step_cash_description = data_actual['data']['description']
    #     value_data_step_cash_token = data_actual['data']['token']
    #     value_data_step_cash_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
    #     value_data_step_cash_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
    #     # 'response' - verify value under 'data'
    #     AU.assert_not_equals('list_cash', [], value_data_step_cash_list_cash)
    #     AU.assert_not_empty('list_cash', [], value_data_step_cash_list_cash)
    #     AU.assert_equals('list_cash_from_response', [], value_data_step_cash_list_cash_from_response)
    #     AU.assert_equals('transaction_code', 'DPT_FBI', value_data_step_cash_transaction_code)
    #     AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
    #     AU.assert_equals('transaction_type', 'FBI', value_data_step_cash_transaction_type)
    #     AU.assert_equals('sub_code', step_code_cash, value_data_step_cash_sub_code)
    #     AU.assert_not_null('transaction_date', value_data_step_cash_transaction_date)
    #     AU.assert_not_empty('transaction_date', value_data_step_cash_transaction_date)
    #     AU.assert_not_null('service_sys_date', value_data_step_cash_service_sys_date)
    #     AU.assert_not_empty('service_sys_date', value_data_step_cash_service_sys_date)
    #     AU.assert_not_null('reference_id', value_data_step_cash_reference_id)
    #     AU.assert_not_empty('reference_id', value_data_step_cash_reference_id)
    #     AU.assert_not_null('ref_id', value_data_step_cash_ref_id)
    #     AU.assert_not_empty('ref_id', value_data_step_cash_ref_id)
    #     AU.assert_empty('reference_code', value_data_step_cash_reference_code)
    #     AU.assert_empty('business_code', value_data_step_cash_business_code)
    #     AU.assert_equals('value_date', user_service['working_date'], value_data_step_cash_value_date)
    #     AU.assert_equals('current_user_code', user_service['username'], value_data_step_cash_current_user_code)
    #     AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_step_cash_current_branch_code)
    #     AU.assert_equals('current_username', user_service['fullname'], value_data_step_cash_current_username)
    #     AU.assert_equals('current_loginname', user_service['username'], value_data_step_cash_current_loginname)
    #     AU.assert_empty('user_approve', value_data_step_cash_user_approve)
    #     AU.assert_equals('status', 'N', value_data_step_cash_status)
    #     AU.assert_equals('is_reverse',  False, value_data_step_cash_is_reverse)
    #     AU.assert_equals('amount1', 0, value_data_step_cash_amount1)
    #     AU.assert_equals('description', '11804: Fixed deposit book issue', value_data_step_cash_description)
    #     AU.assert_equals('token', '*', value_data_step_cash_token)
    #     AU.assert_equals('is_transaction_reverse',  False, value_data_step_cash_is_transaction_reverse)
    #     AU.assert_equals('is_transaction_compensated',  False, value_data_step_cash_is_transaction_compensated)
    #     # 'response' - verify item under 'data' and 'list_cash'
    #     AU.assert_equals('Number item in list_cash', 1, len(data_actual['data']['list_cash']))
    #     # 'response' - verify key response under 'data' and 'list_cash', item 1
    #     AU.assert_exists(expected_key['data_list_cash'], data_actual['data']['list_cash'][0])
    #     # 'response' - get value under 'data' and 'list_cash', item 1
    #     value_list_cash_amount_cash_change = data_actual['data']['list_cash'][0]['amount_cash_change']
    #     value_list_cash_base_amount = data_actual['data']['list_cash'][0]['base_amount']
    #     value_list_cash_debit_or_credit = data_actual['data']['list_cash'][0]['debit_or_credit']
    #     value_list_cash_currency_code = data_actual['data']['list_cash'][0]['currency_code']
    #     value_list_cash_condition = data_actual['data']['list_cash'][0]['condition']
    #     value_list_cash_posting = data_actual['data']['list_cash'][0]['posting']
    #     value_list_cash_accounting_group = data_actual['data']['list_cash'][0]['accounting_group']
    #     value_list_cash_transaction_code = data_actual['data']['list_cash'][0]['transaction_code']
    #     value_list_cash_transaction_number = data_actual['data']['list_cash'][0]['transaction_number']
    #     value_list_cash_transaction_type = data_actual['data']['list_cash'][0]['transaction_type']
    #     value_list_cash_sub_code = data_actual['data']['list_cash'][0]['sub_code']
    #     value_list_cash_transaction_date = data_actual['data']['list_cash'][0]['transaction_date']
    #     value_list_cash_service_sys_date = data_actual['data']['list_cash'][0]['service_sys_date']
    #     value_list_cash_reference_id = data_actual['data']['list_cash'][0]['reference_id']
    #     value_list_cash_ref_id = data_actual['data']['list_cash'][0]['ref_id']
    #     value_list_cash_reference_code = data_actual['data']['list_cash'][0]['reference_code']
    #     value_list_cash_business_code = data_actual['data']['list_cash'][0]['business_code']
    #     value_list_cash_value_date = data_actual['data']['list_cash'][0]['value_date']
    #     value_list_cash_current_user_code = data_actual['data']['list_cash'][0]['current_user_code']
    #     value_list_cash_current_branch_code = data_actual['data']['list_cash'][0]['current_branch_code']
    #     value_list_cash_current_username = data_actual['data']['list_cash'][0]['current_username']
    #     value_list_cash_current_loginname = data_actual['data']['list_cash'][0]['current_loginname']
    #     value_list_cash_user_approve = data_actual['data']['list_cash'][0]['user_approve']
    #     value_list_cash_status = data_actual['data']['list_cash'][0]['status']
    #     value_list_cash_is_reverse = data_actual['data']['list_cash'][0]['is_reverse']
    #     value_list_cash_amount1 = data_actual['data']['list_cash'][0]['amount1']
    #     value_list_cash_description = data_actual['data']['list_cash'][0]['description']
    #     value_list_cash_token = data_actual['data']['list_cash'][0]['token']
    #     value_list_cash_is_transaction_reverse = data_actual['data']['list_cash'][0]['is_transaction_reverse']
    #     value_list_cash_is_transaction_compensated = data_actual['data']['list_cash'][0]['is_transaction_compensated']
    #     # 'response' - verify value under 'data' and 'list_cash', item 1
    #     AU.assert_equals('amount_cash_change', 0, value_list_cash_amount_cash_change)
    #     AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
    #     AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
    #     AU.assert_equals('currency_code', currency_code, value_list_cash_currency_code)
    #     AU.assert_equals('condition', "{\"expression\":{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}}", value_list_cash_condition)
    #     AU.assert_equals('posting', False, value_list_cash_posting)
    #     AU.assert_equals('accounting_group', 2, value_list_cash_accounting_group)
    #     AU.assert_null('transaction_code', value_list_cash_transaction_code)
    #     AU.assert_null('transaction_number', value_list_cash_transaction_number)
    #     AU.assert_null('transaction_type', value_list_cash_transaction_type)
    #     AU.assert_null('sub_code', value_list_cash_sub_code)
    #     AU.assert_equals('transaction_date', '0001-01-01T00:00:00', value_list_cash_transaction_date)
    #     AU.assert_equals('service_sys_date', '0001-01-01T00:00:00', value_list_cash_service_sys_date)
    #     AU.assert_null('reference_id', value_list_cash_reference_id)
    #     AU.assert_null('ref_id', value_list_cash_ref_id)
    #     AU.assert_null('reference_code', value_list_cash_reference_code)
    #     AU.assert_null('business_code', value_list_cash_business_code)
    #     AU.assert_equals('value_date', '0001-01-01T00:00:00', value_list_cash_value_date)
    #     AU.assert_null('current_user_code', value_list_cash_current_user_code)
    #     AU.assert_null('current_branch_code', value_list_cash_current_branch_code)
    #     AU.assert_null('current_username', value_list_cash_current_username)
    #     AU.assert_null('current_loginname', value_list_cash_current_loginname)
    #     AU.assert_null('user_approve', value_list_cash_user_approve)
    #     AU.assert_null('status', value_list_cash_status)
    #     AU.assert_equals('is_reverse', False, value_list_cash_is_reverse)
    #     AU.assert_equals('amount1', 0, value_list_cash_amount1)
    #     AU.assert_null('description', value_list_cash_description)
    #     AU.assert_null('token', value_list_cash_token)
    #     AU.assert_equals('is_transaction_reverse', False, value_list_cash_is_transaction_reverse)
    #     AU.assert_equals('is_transaction_compensated', False, value_list_cash_is_transaction_compensated)
    #     # 'postings' - get data actual - step CASH
    #     data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual_posting, indent=4, sort_keys=False))

# CASE NAY TEST MANUAL
    # def test_11_sp_dpt_fbi_003_success_fixed_deposit_account_status_maturity_no_passbook(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_004_success_fixed_deposit_account_status_new_has_passbook(self, user):
    #     sp_helper = StoredProcedureHelper(user)
    #     catalog_code='FD06PIMMK'
    #     catalog_name='Fixed deposit 6 months (Principal plus interest rollover) in MMK'
    #     deposit_type='Fixed Deposit'
    #     deposit_sub_type='T3'
    #     deposit_purpose='S'
    #     rollover='A'
    #     auto_transfer_option='N'
    #     minimum_deposit_amount=0
    #     amount_deposit=200000.45
    #     method='CSH'
    #     generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
    #     print('generated_numbers: ', generated_numbers)
    #     from_serial = to_serial = serial_no = generated_numbers
    #     cn_status='D'
    #     # STEP 01-01: Open fixed deposit account
    #     fields_data_opn = sp_payload.DPT_OPN(
    #         customer_code=customer_code_individual,
    #         catalog_code=catalog_code,
    #         catalog_name=catalog_name,
    #         deposit_type=deposit_type,
    #         account_name=account_name_individual,
    #         deposit_sub_type=deposit_sub_type,
    #         deposit_purpose=deposit_purpose,
    #         rollover=rollover,
    #         auto_transfer_option=auto_transfer_option
    #     )
    #     rs = sp_helper.DPT_OPN(fields_data_opn)
    #     step_code = 'DPT_OPN'
    #     # 'response' - get data actual
    #     data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_opn['status'])
    #     # 'response' - get value 'account_number' under 'data'
    #     AU.assert_exists('account_number', data_dpt_opn['data'])
    #     AU.assert_exists('account_chart_number', data_dpt_opn['data'])
    #     account_number = data_dpt_opn['data']['account_number']
    #     gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
    #     # STEP 01-02: Approve fixed deposit account
    #     fields_data_apr = sp_payload.DPT_APR(
    #         account_number=account_number,
    #         branch_name=branch_name,
    #         account_holder_name=account_name_individual,
    #         catalog_code=catalog_code,
    #         deposit_sub_type=deposit_sub_type,
    #         deposit_type='T',
    #         catalogue_name=catalog_name,
    #         created_by=user_service['username']
    #     )
    #     rs = sp_helper.DPT_APR(fields_data_apr)
    #     step_code = 'DPT_APR'
    #     # 'response' - get data actual
    #     data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_apr['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
    #     # STEP 01-03: Stock registration
    #     fields_data = sp_payload.DPT_SRG(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_SRG(fields_data)
    #     step_code = 'DPT_SRG'
    #     # 'response' - get data actual
    #     data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_srg['status'])
    #     # 'response' - get value 'account_number' under 'data'
    #     AU.assert_exists('from_serial', data_dpt_srg['data'])
    #     AU.assert_exists('to_serial', data_dpt_srg['data'])
    #     AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
    #     AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
    #     # STEP 01-04: Stock assigned to teller
    #     fields_data = sp_payload.DPT_SAT(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         assigned_staff_code=assigned_staff_code,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_SAT(fields_data)
    #     step_code = 'DPT_SAT'
    #     # 'response' - get data actual
    #     data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_sat['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
    #     # STEP 01-05: Stock confirm received
    #     fields_data = sp_payload.DPT_CCR(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_CCR(fields_data)
    #     step_code = 'DPT_CCR'
    #     # 'response' - get data actual
    #     data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_ccr['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_exists('from_serial', data_dpt_ccr['data'])
    #     AU.assert_exists('to_serial', data_dpt_ccr['data'])
    #     AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
    #     AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
    #     # STEP 02-01: Fixed deposit book issue first time
    #     fields_data = sp_payload.DPT_FBI(
    #         account_number=account_number,
    #         branch_name=branch_name,
    #         serial_no=serial_no,
    #         stock_prefix=stock_prefix,
    #         currency_code=currency_code,
    #         method=method
    #     )
    #     rs = sp_helper.DPT_FBI(fields_data)
    #     step_code = 'DPT_FBI'
    #     # 'response' - get data actual
    #     data_dpt_fbi = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_fbi, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_fbi['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_exists('account_number', data_dpt_fbi['data'])
    #     AU.assert_equals('account_number', account_number, data_dpt_fbi['data']['account_number'])
    #     AU.assert_exists('serial_no', data_dpt_fbi['data'])
    #     AU.assert_equals('serial_no', serial_no, data_dpt_fbi['data']['serial_no'])
    #     # STEP 02-02: Change passbook status to 'Damage'
    #     fields_data_cts = sp_payload.DPT_CTS(
    #         account_number=account_number,
    #         branch_name=branch_name,
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         cn_status=cn_status,
    #         stock_prefix=stock_prefix,
    #         currency_code=deposit_currency,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_CTS(fields_data_cts)
    #     step_code = 'DPT_CTS'
    #     # 'response' - get data actual
    #     data_dpt_cts = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_cts, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_cts['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('account_number', account_number, data_dpt_cts['data']['account_number'])
    #     # STEP 02-03: Stock registration second time
    #     generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
    #     print('generated_numbers second time: ', generated_numbers)
    #     from_serial = to_serial = serial_no = generated_numbers
    #     fields_data = sp_payload.DPT_SRG(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_SRG(fields_data)
    #     step_code = 'DPT_SRG'
    #     # 'response' - get data actual
    #     data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_srg['status'])
    #     # 'response' - get value 'account_number' under 'data'
    #     AU.assert_exists('from_serial', data_dpt_srg['data'])
    #     AU.assert_exists('to_serial', data_dpt_srg['data'])
    #     AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
    #     AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
    #     # STEP 02-04: Stock assigned to teller
    #     fields_data = sp_payload.DPT_SAT(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         assigned_staff_code=assigned_staff_code,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_SAT(fields_data)
    #     step_code = 'DPT_SAT'
    #     # 'response' - get data actual
    #     data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_sat['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
    #     # STEP 02-05: Stock confirm received
    #     fields_data = sp_payload.DPT_CCR(
    #         from_serial=from_serial,
    #         to_serial=to_serial,
    #         stock_prefix=stock_prefix,
    #         stock_type=stock_type
    #     )
    #     rs = sp_helper.DPT_CCR(fields_data)
    #     step_code = 'DPT_CCR'
    #     # 'response' - get data actual
    #     data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, data_dpt_ccr['status'])
    #     # 'response' - verify value under 'data'
    #     AU.assert_exists('from_serial', data_dpt_ccr['data'])
    #     AU.assert_exists('to_serial', data_dpt_ccr['data'])
    #     AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
    #     AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
    #     # STEP 03: Fixed deposit book issue second time
    #     fields_data = sp_payload.DPT_FBI(
    #         account_number=account_number,
    #         branch_name=branch_name,
    #         serial_no=serial_no,
    #         stock_prefix=stock_prefix,
    #         currency_code=currency_code,
    #         method=method
    #     )
    #     rs = sp_helper.DPT_FBI(fields_data)
    #     step_code = 'DPT_FBI'
    #     # 'response' - get data actual
    #     data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual, indent=4, sort_keys=False))
    #     # 'response' - verify key response level 1
    #     AU.assert_exists(expected_key['level_01'], data_actual)
    #     # 'response' - get value level 1
    #     value_status = data_actual['status']
    #     value_error_message = data_actual['error_message']
    #     value_error_code = data_actual['error_code']
    #     value_data = data_actual['data']
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, value_status)
    #     AU.assert_empty('error_message', value_error_message)
    #     AU.assert_empty('error_code', value_error_code)
    #     AU.assert_not_null('data', value_data)
    #     # 'response' - verify key response under 'data'
    #     AU.assert_exists(expected_key['data_dpt_fbi'], data_actual['data'])
    #     # 'response' - get value under 'data'
    #     value_data_stock_type = data_actual['data']['stock_type']
    #     value_data_account_number = data_actual['data']['account_number']
    #     value_data_serial_no = data_actual['data']['serial_no']
    #     value_data_stock_prefix = data_actual['data']['stock_prefix']
    #     value_data_method = data_actual['data']['method']
    #     value_data_account_number_for_fee = data_actual['data']['account_number_for_fee']
    #     value_data_currency_code = data_actual['data']['currency_code']
    #     value_data_branch_name = data_actual['data']['branch_name']
    #     value_data_total_fee = data_actual['data']['total_fee']
    #     value_data_fee_data = data_actual['data']['fee_data']
    #     value_data_transaction_code = data_actual['data']['transaction_code']
    #     value_data_transaction_number = data_actual['data']['transaction_number']
    #     value_data_transaction_type = data_actual['data']['transaction_type']
    #     value_data_sub_code = data_actual['data']['sub_code']
    #     value_data_transaction_date = data_actual['data']['transaction_date']
    #     value_data_service_sys_date = data_actual['data']['service_sys_date']
    #     value_data_reference_id = data_actual['data']['reference_id']
    #     value_data_ref_id = data_actual['data']['ref_id']
    #     value_data_reference_code = data_actual['data']['reference_code']
    #     value_data_business_code = data_actual['data']['business_code']
    #     value_data_value_date = data_actual['data']['value_date']
    #     value_data_current_user_code = data_actual['data']['current_user_code']
    #     value_data_current_branch_code = data_actual['data']['current_branch_code']
    #     value_data_current_username = data_actual['data']['current_username']
    #     value_data_current_loginname = data_actual['data']['current_loginname']
    #     value_data_user_approve = data_actual['data']['user_approve']
    #     value_data_status = data_actual['data']['status']
    #     value_data_is_reverse = data_actual['data']['is_reverse']
    #     value_data_amount1 = data_actual['data']['amount1']
    #     value_data_description = data_actual['data']['description']
    #     value_data_token = data_actual['data']['token']
    #     value_data_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
    #     value_data_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
    #     # 'response' - verify value under 'data'
    #     AU.assert_equals('stock_type', stock_type, value_data_stock_type)
    #     AU.assert_equals('account_number', account_number, value_data_account_number)
    #     AU.assert_equals('serial_no', serial_no, value_data_serial_no)
    #     AU.assert_equals('stock_prefix', stock_prefix, value_data_stock_prefix)
    #     AU.assert_equals('method', method, value_data_method)
    #     AU.assert_equals('account_number_for_fee', '', value_data_account_number_for_fee)
    #     AU.assert_equals('currency_code', currency_code, value_data_currency_code)
    #     AU.assert_equals('branch_name', branch_name, value_data_branch_name)
    #     AU.assert_equals('total_fee', 0, value_data_total_fee)
    #     AU.assert_equals('fee_data', [], value_data_fee_data)
    #     AU.assert_equals('transaction_code', 'DPT_FBI', value_data_transaction_code)
    #     AU.assert_not_null('transaction_number', value_data_transaction_number)
    #     AU.assert_not_empty('transaction_number', value_data_transaction_number)
    #     AU.assert_equals('transaction_type', 'FBI', value_data_transaction_type)
    #     AU.assert_equals('sub_code', 'DPT_FBI', value_data_sub_code)
    #     AU.assert_not_null('transaction_date', value_data_transaction_date)
    #     AU.assert_not_empty('transaction_date', value_data_transaction_date)
    #     AU.assert_not_null('service_sys_date', value_data_service_sys_date)
    #     AU.assert_not_empty('service_sys_date', value_data_service_sys_date)
    #     AU.assert_not_null('reference_id', value_data_reference_id)
    #     AU.assert_not_empty('reference_id', value_data_reference_id)
    #     AU.assert_not_null('ref_id', value_data_ref_id)
    #     AU.assert_not_empty('ref_id', value_data_ref_id)
    #     AU.assert_empty('reference_code', value_data_reference_code)
    #     AU.assert_empty('business_code', value_data_business_code)
    #     AU.assert_equals('value_date', user_service['working_date'], value_data_value_date)
    #     AU.assert_equals('current_user_code', user_service['username'], value_data_current_user_code)
    #     AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_current_branch_code)
    #     AU.assert_equals('current_username', user_service['fullname'], value_data_current_username)
    #     AU.assert_equals('current_loginname', user_service['username'], value_data_current_loginname)
    #     AU.assert_empty('user_approve', value_data_user_approve)
    #     AU.assert_equals('status', 'N', value_data_status)
    #     AU.assert_equals('is_reverse',  False, value_data_is_reverse)
    #     AU.assert_equals('amount1', 0, value_data_amount1)
    #     AU.assert_equals('description', '11804: Fixed deposit book issue', value_data_description)
    #     AU.assert_equals('token', '*', value_data_token)
    #     AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
    #     AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
    #     # 'postings' - get data actual
    #     data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
    #     # verify step CASH
    #     step_code = step_code_cash
    #     # 'response' - get data actual - step CASH
    #     data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual, indent=4, sort_keys=False))
    #     # 'response' - verify key response level 1
    #     AU.assert_exists(expected_key['level_01'], data_actual)
    #     # 'response' - get value level 1
    #     value_status = data_actual['status']
    #     value_error_message = data_actual['error_message']
    #     value_error_code = data_actual['error_code']
    #     value_data = data_actual['data']
    #     # 'response' - verify value level 1
    #     AU.assert_equals('status', 0, value_status)
    #     AU.assert_empty('error_message', value_error_message)
    #     AU.assert_empty('error_code', value_error_code)
    #     AU.assert_not_null('data', value_data)
    #     # 'response' - verify key response under 'data'
    #     AU.assert_exists(expected_key['data_step_cash'], data_actual['data'])
    #     # 'response' - get value under 'data'
    #     value_data_step_cash_list_cash = data_actual['data']['list_cash']
    #     value_data_step_cash_list_cash_from_response = data_actual['data']['list_cash_from_response']
    #     value_data_step_cash_transaction_code = data_actual['data']['transaction_code']
    #     value_data_step_cash_transaction_number = data_actual['data']['transaction_number']
    #     value_data_step_cash_transaction_type = data_actual['data']['transaction_type']
    #     value_data_step_cash_sub_code = data_actual['data']['sub_code']
    #     value_data_step_cash_transaction_date = data_actual['data']['transaction_date']
    #     value_data_step_cash_service_sys_date = data_actual['data']['service_sys_date']
    #     value_data_step_cash_reference_id = data_actual['data']['reference_id']
    #     value_data_step_cash_ref_id = data_actual['data']['ref_id']
    #     value_data_step_cash_reference_code = data_actual['data']['reference_code']
    #     value_data_step_cash_business_code = data_actual['data']['business_code']
    #     value_data_step_cash_value_date = data_actual['data']['value_date']
    #     value_data_step_cash_current_user_code = data_actual['data']['current_user_code']
    #     value_data_step_cash_current_branch_code = data_actual['data']['current_branch_code']
    #     value_data_step_cash_current_username = data_actual['data']['current_username']
    #     value_data_step_cash_current_loginname = data_actual['data']['current_loginname']
    #     value_data_step_cash_user_approve = data_actual['data']['user_approve']
    #     value_data_step_cash_status = data_actual['data']['status']
    #     value_data_step_cash_is_reverse = data_actual['data']['is_reverse']
    #     value_data_step_cash_amount1 = data_actual['data']['amount1']
    #     value_data_step_cash_description = data_actual['data']['description']
    #     value_data_step_cash_token = data_actual['data']['token']
    #     value_data_step_cash_is_transaction_reverse = data_actual['data']['is_transaction_reverse']
    #     value_data_step_cash_is_transaction_compensated = data_actual['data']['is_transaction_compensated']
    #     # 'response' - verify value under 'data'
    #     AU.assert_not_equals('list_cash', [], value_data_step_cash_list_cash)
    #     AU.assert_not_empty('list_cash', [], value_data_step_cash_list_cash)
    #     AU.assert_equals('list_cash_from_response', [], value_data_step_cash_list_cash_from_response)
    #     AU.assert_equals('transaction_code', 'DPT_FBI', value_data_step_cash_transaction_code)
    #     AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
    #     AU.assert_equals('transaction_type', 'FBI', value_data_step_cash_transaction_type)
    #     AU.assert_equals('sub_code', step_code_cash, value_data_step_cash_sub_code)
    #     AU.assert_not_null('transaction_date', value_data_step_cash_transaction_date)
    #     AU.assert_not_empty('transaction_date', value_data_step_cash_transaction_date)
    #     AU.assert_not_null('service_sys_date', value_data_step_cash_service_sys_date)
    #     AU.assert_not_empty('service_sys_date', value_data_step_cash_service_sys_date)
    #     AU.assert_not_null('reference_id', value_data_step_cash_reference_id)
    #     AU.assert_not_empty('reference_id', value_data_step_cash_reference_id)
    #     AU.assert_not_null('ref_id', value_data_step_cash_ref_id)
    #     AU.assert_not_empty('ref_id', value_data_step_cash_ref_id)
    #     AU.assert_empty('reference_code', value_data_step_cash_reference_code)
    #     AU.assert_empty('business_code', value_data_step_cash_business_code)
    #     AU.assert_equals('value_date', user_service['working_date'], value_data_step_cash_value_date)
    #     AU.assert_equals('current_user_code', user_service['username'], value_data_step_cash_current_user_code)
    #     AU.assert_equals('current_branch_code', user_service['branch_code'], value_data_step_cash_current_branch_code)
    #     AU.assert_equals('current_username', user_service['fullname'], value_data_step_cash_current_username)
    #     AU.assert_equals('current_loginname', user_service['username'], value_data_step_cash_current_loginname)
    #     AU.assert_empty('user_approve', value_data_step_cash_user_approve)
    #     AU.assert_equals('status', 'N', value_data_step_cash_status)
    #     AU.assert_equals('is_reverse',  False, value_data_step_cash_is_reverse)
    #     AU.assert_equals('amount1', 0, value_data_step_cash_amount1)
    #     AU.assert_equals('description', '11804: Fixed deposit book issue', value_data_step_cash_description)
    #     AU.assert_equals('token', '*', value_data_step_cash_token)
    #     AU.assert_equals('is_transaction_reverse',  False, value_data_step_cash_is_transaction_reverse)
    #     AU.assert_equals('is_transaction_compensated',  False, value_data_step_cash_is_transaction_compensated)
    #     # 'response' - verify item under 'data' and 'list_cash'
    #     AU.assert_equals('Number item in list_cash', 1, len(data_actual['data']['list_cash']))
    #     # 'response' - verify key response under 'data' and 'list_cash', item 1
    #     AU.assert_exists(expected_key['data_list_cash'], data_actual['data']['list_cash'][0])
    #     # 'response' - get value under 'data' and 'list_cash', item 1
    #     value_list_cash_amount_cash_change = data_actual['data']['list_cash'][0]['amount_cash_change']
    #     value_list_cash_base_amount = data_actual['data']['list_cash'][0]['base_amount']
    #     value_list_cash_debit_or_credit = data_actual['data']['list_cash'][0]['debit_or_credit']
    #     value_list_cash_currency_code = data_actual['data']['list_cash'][0]['currency_code']
    #     value_list_cash_condition = data_actual['data']['list_cash'][0]['condition']
    #     value_list_cash_posting = data_actual['data']['list_cash'][0]['posting']
    #     value_list_cash_accounting_group = data_actual['data']['list_cash'][0]['accounting_group']
    #     value_list_cash_transaction_code = data_actual['data']['list_cash'][0]['transaction_code']
    #     value_list_cash_transaction_number = data_actual['data']['list_cash'][0]['transaction_number']
    #     value_list_cash_transaction_type = data_actual['data']['list_cash'][0]['transaction_type']
    #     value_list_cash_sub_code = data_actual['data']['list_cash'][0]['sub_code']
    #     value_list_cash_transaction_date = data_actual['data']['list_cash'][0]['transaction_date']
    #     value_list_cash_service_sys_date = data_actual['data']['list_cash'][0]['service_sys_date']
    #     value_list_cash_reference_id = data_actual['data']['list_cash'][0]['reference_id']
    #     value_list_cash_ref_id = data_actual['data']['list_cash'][0]['ref_id']
    #     value_list_cash_reference_code = data_actual['data']['list_cash'][0]['reference_code']
    #     value_list_cash_business_code = data_actual['data']['list_cash'][0]['business_code']
    #     value_list_cash_value_date = data_actual['data']['list_cash'][0]['value_date']
    #     value_list_cash_current_user_code = data_actual['data']['list_cash'][0]['current_user_code']
    #     value_list_cash_current_branch_code = data_actual['data']['list_cash'][0]['current_branch_code']
    #     value_list_cash_current_username = data_actual['data']['list_cash'][0]['current_username']
    #     value_list_cash_current_loginname = data_actual['data']['list_cash'][0]['current_loginname']
    #     value_list_cash_user_approve = data_actual['data']['list_cash'][0]['user_approve']
    #     value_list_cash_status = data_actual['data']['list_cash'][0]['status']
    #     value_list_cash_is_reverse = data_actual['data']['list_cash'][0]['is_reverse']
    #     value_list_cash_amount1 = data_actual['data']['list_cash'][0]['amount1']
    #     value_list_cash_description = data_actual['data']['list_cash'][0]['description']
    #     value_list_cash_token = data_actual['data']['list_cash'][0]['token']
    #     value_list_cash_is_transaction_reverse = data_actual['data']['list_cash'][0]['is_transaction_reverse']
    #     value_list_cash_is_transaction_compensated = data_actual['data']['list_cash'][0]['is_transaction_compensated']
    #     # 'response' - verify value under 'data' and 'list_cash', item 1
    #     AU.assert_equals('amount_cash_change', 0, value_list_cash_amount_cash_change)
    #     AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
    #     AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
    #     AU.assert_equals('currency_code', currency_code, value_list_cash_currency_code)
    #     AU.assert_equals('condition', "{\"expression\":{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}}", value_list_cash_condition)
    #     AU.assert_equals('posting', False, value_list_cash_posting)
    #     AU.assert_equals('accounting_group', 2, value_list_cash_accounting_group)
    #     AU.assert_null('transaction_code', value_list_cash_transaction_code)
    #     AU.assert_null('transaction_number', value_list_cash_transaction_number)
    #     AU.assert_null('transaction_type', value_list_cash_transaction_type)
    #     AU.assert_null('sub_code', value_list_cash_sub_code)
    #     AU.assert_equals('transaction_date', '0001-01-01T00:00:00', value_list_cash_transaction_date)
    #     AU.assert_equals('service_sys_date', '0001-01-01T00:00:00', value_list_cash_service_sys_date)
    #     AU.assert_null('reference_id', value_list_cash_reference_id)
    #     AU.assert_null('ref_id', value_list_cash_ref_id)
    #     AU.assert_null('reference_code', value_list_cash_reference_code)
    #     AU.assert_null('business_code', value_list_cash_business_code)
    #     AU.assert_equals('value_date', '0001-01-01T00:00:00', value_list_cash_value_date)
    #     AU.assert_null('current_user_code', value_list_cash_current_user_code)
    #     AU.assert_null('current_branch_code', value_list_cash_current_branch_code)
    #     AU.assert_null('current_username', value_list_cash_current_username)
    #     AU.assert_null('current_loginname', value_list_cash_current_loginname)
    #     AU.assert_null('user_approve', value_list_cash_user_approve)
    #     AU.assert_null('status', value_list_cash_status)
    #     AU.assert_equals('is_reverse', False, value_list_cash_is_reverse)
    #     AU.assert_equals('amount1', 0, value_list_cash_amount1)
    #     AU.assert_null('description', value_list_cash_description)
    #     AU.assert_null('token', value_list_cash_token)
    #     AU.assert_equals('is_transaction_reverse', False, value_list_cash_is_transaction_reverse)
    #     AU.assert_equals('is_transaction_compensated', False, value_list_cash_is_transaction_compensated)
    #     # 'postings' - get data actual - step CASH
    #     data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual_posting, indent=4, sort_keys=False))

    def test_11_sp_dpt_fbi_005_success_fixed_deposit_account_status_normal_has_passbook(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='FD06PIMMK'
        catalog_name='Fixed deposit 6 months (Principal plus interest rollover) in MMK'
        deposit_type='Fixed Deposit'
        deposit_sub_type='T3'
        deposit_purpose='S'
        rollover='A'
        auto_transfer_option='N'
        minimum_deposit_amount=0
        amount_deposit=200000.45
        method='CSH'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        cn_status='L'
        # STEP 01-01: Open fixed deposit account
        fields_data_opn = sp_payload.DPT_OPN(
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
        # STEP 01-02: Approve fixed deposit account
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
        # 'response' - verify value under 'data'
        AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
        # STEP 01-03: Deposit money
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
        # STEP 01-04: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            stock_type=stock_type
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
            assigned_staff_code=assigned_staff_code,
            stock_type=stock_type
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
            stock_prefix=stock_prefix,
            stock_type=stock_type
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
        # STEP 02-01: Fixed deposit book issue first time
        fields_data = sp_payload.DPT_FBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_FBI(fields_data)
        step_code = 'DPT_FBI'
        # 'response' - get data actual
        data_dpt_fbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_fbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_fbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_fbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_fbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_fbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_fbi['data']['serial_no'])
        # STEP 02-02: Change passbook status to 'Lost'
        fields_data_cts = sp_payload.DPT_CTS(
            account_number=account_number,
            branch_name=branch_name,
            from_serial=from_serial,
            to_serial=to_serial,
            cn_status=cn_status,
            stock_prefix=stock_prefix,
            currency_code=deposit_currency,
            stock_type=stock_type
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
        # STEP 02-03: Stock registration second time
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers second time: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            stock_type=stock_type
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
        # STEP 02-04: Stock assigned to teller
        fields_data = sp_payload.DPT_SAT(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            assigned_staff_code=assigned_staff_code,
            stock_type=stock_type
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
        # STEP 02-05: Stock confirm received
        fields_data = sp_payload.DPT_CCR(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stock_prefix,
            stock_type=stock_type
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
        # STEP 03: Fixed deposit book issue second time
        fields_data = sp_payload.DPT_FBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_FBI(fields_data)
        step_code = 'DPT_FBI'
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
        AU.assert_exists(expected_key['data_dpt_fbi'], data_actual['data'])
        # 'response' - get value under 'data'
        value_data_stock_type = data_actual['data']['stock_type']
        value_data_account_number = data_actual['data']['account_number']
        value_data_serial_no = data_actual['data']['serial_no']
        value_data_stock_prefix = data_actual['data']['stock_prefix']
        value_data_method = data_actual['data']['method']
        value_data_account_number_for_fee = data_actual['data']['account_number_for_fee']
        value_data_currency_code = data_actual['data']['currency_code']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_total_fee = data_actual['data']['total_fee']
        value_data_fee_data = data_actual['data']['fee_data']
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
        AU.assert_equals('stock_type', stock_type, value_data_stock_type)
        AU.assert_equals('account_number', account_number, value_data_account_number)
        AU.assert_equals('serial_no', serial_no, value_data_serial_no)
        AU.assert_equals('stock_prefix', stock_prefix, value_data_stock_prefix)
        AU.assert_equals('method', method, value_data_method)
        AU.assert_equals('account_number_for_fee', '', value_data_account_number_for_fee)
        AU.assert_equals('currency_code', currency_code, value_data_currency_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('total_fee', 0, value_data_total_fee)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('transaction_code', 'DPT_FBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'FBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_FBI', value_data_sub_code)
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
        AU.assert_equals('description', '11804: Fixed deposit book issue', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs, step_code)
        print(json.dumps(data_actual_posting, indent=4, sort_keys=False))
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
        AU.assert_equals('transaction_code', 'DPT_FBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'FBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11804: Fixed deposit book issue', value_data_step_cash_description)
        AU.assert_equals('token', '*', value_data_step_cash_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_step_cash_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_step_cash_is_transaction_compensated)
        # 'response' - verify item under 'data' and 'list_cash'
        AU.assert_equals('Number item in list_cash', 1, len(data_actual['data']['list_cash']))
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
        AU.assert_equals('amount_cash_change', 0, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_code, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}}", value_list_cash_condition)
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

# CASE NAY TEST MANUAL
    # def test_11_sp_dpt_fbi_006_success_fixed_deposit_account_status_maturity_has_passbook(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_007_success_fixed_deposit_account_status_new_no_passbook_add_fee_cash(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_008_success_fixed_deposit_account_status_normal_no_passbook_add_fee_deposit_current(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_009_success_fixed_deposit_account_status_normal_has_passbook_add_fee_deposit_fixed deposit(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_010_success_fixed_deposit_account_status_new_has_passbook_add_fee_accounting(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_011_error_current_account(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_012_error_fixed deposit_account(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_013_error_prepaid_fixed_deposit_account(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_014_error_fixed_deposit_account_status_closed(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_015_error_fixed_deposit_account_status_block(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_016_error_fixed_deposit_account_status_pending(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_017_error_fixed_deposit_account_has_passbook_normal(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_018_error_fixed_deposit_account_has_passbook_stop_payment(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_019_error_fixed_deposit_account_add_fee_fixed_deposit(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_020_error_fixed_deposit_account_add_fee_prepaid_fixed_deposit(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_021_error_fixed_deposit_account_add_fee_deposit_status_closed(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_022_error_fixed_deposit_account_add_fee_deposit_status_block(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_023_error_fixed_deposit_account_add_fee_deposit_status_pending(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_024_error_fixed_deposit_account_add_fee_deposit_status_new(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_025_error_fixed_deposit_account_add_fee_deposit_status_dormant(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_026_error_fixed_deposit_account_add_fee_deposit_bigger_available_balance(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_027_error_fixed_deposit_account_add_fee_deposit_not_same_currency(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_028_error_fixed_deposit_account_add_fee_accounting_posting_side_is_credit(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_029_error_fixed_deposit_account_add_fee_accounting_level_not_9(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_030_error_fixed_deposit_account_add_fee_accounting_not_same_currency(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_031_error_fixed_deposit_account_add_fee_accounting_not_same_branch(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_032_error_fixed_deposit_account_add_fee_accounting_group_is_cash(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_033_error_fixed_deposit_account_add_fee_accounting_direct_posting_is_no(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_034_error_account_number_is_empty(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_035_error_account_number_is_null(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_036_error_account_number_not_exist(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_037_error_serial_no_is_empty(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_038_error_serial_no_is_null(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_039_error_serial_no_not_exist(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_040_error_serial_no_is_cheque(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_041_error_serial_no_is_receipt(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_042_error_serial_no_is_passbook_for_fixed deposit(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_043_error_serial_no_is_payment_order(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_044_error_serial_no_is_gift_cheque(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_045_error_passbook_at_branch(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_046_error_passbook_at_teller_not_confirm(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_047_error_passbook_status_lost(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_048_error_passbook_status_damage(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_049_error_passbook_status_stop_payment(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_050_error_passbook_status_closed(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"

    # def test_11_sp_dpt_fbi_051_error_passbook_not_belong_to_teller(self, user):
    #     assert '', f"Expected: ..., Actual: response Json:"


    def check_serial_number_not_exist(self, user, generated_number, prefix=None, s_type=None):
        sp_helper = StoredProcedureHelper(user)
        if prefix == None:
            prefix = stock_prefix
        else:
            prefix = prefix
        if s_type == None:
            s_type = stock_type
        else:
            s_type = s_type
        # search serial_number
        fields_data_search = sp_payload.DPT_ADSEARCH_STOCKINVENTORY(
            stock_prefix=prefix,
            from_serial_from=generated_number,
            from_serial_to=generated_number,
            stock_type=s_type
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

    def gen_serial_number(self, user, prefix=None, s_type=None):
        if prefix == None:
            prefix = stock_prefix
        else:
            prefix = prefix
        if s_type == None:
            s_type = stock_type
        else:
            s_type = s_type
        while True:
            # Generate a random number with the desired format
            generated_number = f"8{random.randint(0, 99999):05}"
            # Check if the generated number exists; if not, break the loop
            if self.check_serial_number_not_exist(user, generated_number, prefix=prefix, s_type=s_type):
                break
        generated_number = f"{prefix}{generated_number}"
        return generated_number
