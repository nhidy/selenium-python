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
stock_prefix='SB'
stock_type='P'
assigned_staff_code=user_service['username']
currency_code='MMK'
# data test invalid
gl_account_level_07='5010101000101'
gl_account_level_08='501010100010101'
gl_account_posting_side_debit='003110070100000101'
gl_account_usd='003101010666666602'
gl_account_cash='003101030100010101'
gl_account_direct_posting_no='003110060100000001'
gl_account_not_same_branch='001110060100000001'
# # data test trên 104
# step_code_cash='CSH_UPDATE_CASH'
# account_number_fixed_deposit_normal='430030589898'
# account_number_prepaid_fixed_deposit_normal='460030177172'
# account_number_current_normal='110031370833'
# account_number_saving_closed='340034919619'
# account_number_saving_block='310033187741'
# account_number_saving_pending='310030475906'
# account_number_saving_new='210032347511'
# account_number_current_new='110038698206'
# account_number_current_closed='110031738819'
# account_number_current_block='110037723297'
# account_number_current_dormant='110037212072'
# account_number_current_usd='120032453573'
# data test trên 198
step_code_cash='CSH_UPDATE_CASH_SP'
account_number_fixed_deposit_normal='430036727166'
account_number_prepaid_fixed_deposit_normal='460034232309'
account_number_current_normal='110031573739'
account_number_saving_closed='330038150764'
account_number_saving_block='330038310139'
account_number_saving_pending='330038808568'
account_number_saving_new='310031442402'
account_number_current_new='110033365907'
account_number_current_closed='110033046060'
account_number_current_block='110036552201'
account_number_current_dormant='110036763005'
account_number_current_usd='120033442107'

@pytest.fixture(scope='session')
def user():
    req = RU(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_SBI
class Test_SP_DPT_SBI(object):

    def test_09_sp_dpt_sbi_001_success_saving_account_status_new_no_passbook(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        method='CSH'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_exists(expected_key['data_dpt_sbi'], data_actual['data'])
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_SBI', value_data_sub_code)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_description)
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_step_cash_description)
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
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"&&\",\"type\":\"boolean\",\"paras\":[{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}]}}", value_list_cash_condition)
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

    def test_09_sp_dpt_sbi_002_success_saving_account_status_normal_no_passbook(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='BSMMK0000'
        catalog_name='Bonus savings account  in MMK'
        deposit_type='Savings'
        deposit_sub_type='S2'
        minimum_deposit_amount=50000
        amount_deposit=200000.45
        method='CSH'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_exists(expected_key['data_dpt_sbi'], data_actual['data'])
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_SBI', value_data_sub_code)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_description)
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_step_cash_description)
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
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"&&\",\"type\":\"boolean\",\"paras\":[{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}]}}", value_list_cash_condition)
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

    def test_09_sp_dpt_sbi_003_success_saving_account_status_dormant_no_passbook(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='PSMMK0000'
        catalog_name='Premier savings deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S3'
        minimum_deposit_amount=50000
        amount_deposit=200000.45
        method='CSH'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-07: change status from 'Normal' to 'Dormant' of saving account
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_exists(expected_key['data_dpt_sbi'], data_actual['data'])
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_SBI', value_data_sub_code)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_description)
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_step_cash_description)
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
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"&&\",\"type\":\"boolean\",\"paras\":[{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}]}}", value_list_cash_condition)
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

    def test_09_sp_dpt_sbi_004_success_saving_account_status_new_has_passbook(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        method='CSH'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        cn_status='D'
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
        # STEP 02-02: Change passbook status to 'Damage'
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
        # STEP 03: Deposit savings book issue second time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_exists(expected_key['data_dpt_sbi'], data_actual['data'])
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_SBI', value_data_sub_code)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_description)
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_step_cash_description)
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
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"&&\",\"type\":\"boolean\",\"paras\":[{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}]}}", value_list_cash_condition)
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

    def test_09_sp_dpt_sbi_005_success_saving_account_status_normal_has_passbook(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='PCMMK0000'
        catalog_name='Premium call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S5'
        minimum_deposit_amount=100000
        amount_deposit=200000.45
        method='CSH'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        cn_status='L'
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
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
        # STEP 03: Deposit savings book issue second time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_exists(expected_key['data_dpt_sbi'], data_actual['data'])
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_SBI', value_data_sub_code)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_description)
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_step_cash_description)
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
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"&&\",\"type\":\"boolean\",\"paras\":[{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}]}}", value_list_cash_condition)
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

    def test_09_sp_dpt_sbi_006_success_saving_account_status_dormant_has_passbook(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SCMMK0000'
        catalog_name='SHWE cash call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S6'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        method='CSH'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        cn_status='C'
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
        # STEP 02-02: Change passbook status to 'Closed'
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
        # STEP 02-06: change status from 'Normal' to 'Dormant' of saving account
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
        # STEP 03: Deposit savings book issue second time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_exists(expected_key['data_dpt_sbi'], data_actual['data'])
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_SBI', value_data_sub_code)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_description)
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_step_cash_description)
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
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"&&\",\"type\":\"boolean\",\"paras\":[{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}]}}", value_list_cash_condition)
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

    def test_09_sp_dpt_sbi_007_success_saving_account_status_new_no_passbook_add_fee_cash(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        method='CSH'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='CSH'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_exists(expected_key['data_dpt_sbi'], data_actual['data'])
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
        AU.assert_equals('total_fee', total_fee, value_data_total_fee)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_SBI', value_data_sub_code)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_description)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_step_cash_description)
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
        AU.assert_equals('amount_cash_change', total_fee, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_code, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"&&\",\"type\":\"boolean\",\"paras\":[{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}]}}", value_list_cash_condition)
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
        AU.assert_equals('SysAccountName', 'IFCC', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_ifcc_02, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', ifc_amount_02, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
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
        AU.assert_equals('TransTableName', 'CashList', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'CASH', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_cash, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', total_fee, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)

    def test_09_sp_dpt_sbi_008_success_saving_account_status_normal_no_passbook_add_fee_deposit_current(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        method='DPT'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 01-06: Deposit money
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
        # STEP 01-07: Open current account
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
        gl_account_ifcc_02='003303030100010101'
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount_current=1000
        amount_deposit_current=ifc_amount_01+ifc_amount_02+minimum_deposit_amount_current
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
        # STEP 01-08: Approve current account
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
        # STEP 01-09: Deposit money to current account
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
        # STEP 02: Deposit savings book issue
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_current
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_exists(expected_key['data_dpt_sbi'], data_actual['data'])
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
        AU.assert_equals('account_number_for_fee', account_number_current, value_data_account_number_for_fee)
        AU.assert_equals('currency_code', currency_code, value_data_currency_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('total_fee', total_fee, value_data_total_fee)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_SBI', value_data_sub_code)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_description)
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
        AU.assert_equals('GLAccount', gl_account_deposit_current, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', total_fee, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_step_cash_description)
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
        AU.assert_equals('amount_cash_change', total_fee, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_code, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"&&\",\"type\":\"boolean\",\"paras\":[{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}]}}", value_list_cash_condition)
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
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', total_fee, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)

    def test_09_sp_dpt_sbi_009_success_saving_account_status_normal_has_passbook_add_fee_deposit_saving(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='PCMMK0000'
        catalog_name='Premium call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S5'
        minimum_deposit_amount=100000
        amount_deposit=200000.45
        method='DPT'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 01-06: Deposit money
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
        # STEP 01-07: Open saving account
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
        gl_account_ifcc_02='003303030100010101'
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount_saving=1000
        amount_deposit_saving=ifc_amount_01+ifc_amount_02+minimum_deposit_amount_saving
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
        # STEP 01-08: Approve saving account
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
        # STEP 01-09: Deposit money to current account
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method='CSH'
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
        # STEP 02-02: Change passbook status to 'Closed'
        cn_status='C'
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
        # STEP 03: Deposit savings book issue second time
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_saving
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_exists(expected_key['data_dpt_sbi'], data_actual['data'])
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
        AU.assert_equals('account_number_for_fee', account_number_saving, value_data_account_number_for_fee)
        AU.assert_equals('currency_code', currency_code, value_data_currency_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('total_fee', total_fee, value_data_total_fee)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_SBI', value_data_sub_code)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_description)
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
        AU.assert_equals('GLAccount', gl_account_deposit_saving, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', total_fee, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_step_cash_description)
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
        AU.assert_equals('amount_cash_change', total_fee, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_code, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"&&\",\"type\":\"boolean\",\"paras\":[{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}]}}", value_list_cash_condition)
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
        AU.assert_equals('GLAccount', gl_account_deposit_saving, value_GLAccount)
        AU.assert_equals('DorC', 'D', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', total_fee, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)

    def test_09_sp_dpt_sbi_010_success_saving_account_status_dormant_has_passbook_add_fee_accounting(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SCMMK0000'
        catalog_name='SHWE cash call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S6'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        method='ACT'
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 01-06: Cash deposit
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method='CSH'
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
        # STEP 02-02: Change passbook status to 'Closed'
        cn_status='C'
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
        # STEP 02-06: change status from 'Normal' to 'Dormant' of saving account
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
        # STEP 03: Deposit savings book issue second time
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='ACT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='ACT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=debit_accounting_valid
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_exists(expected_key['data_dpt_sbi'], data_actual['data'])
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
        AU.assert_equals('account_number_for_fee', debit_accounting_valid, value_data_account_number_for_fee)
        AU.assert_equals('currency_code', currency_code, value_data_currency_code)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('total_fee', total_fee, value_data_total_fee)
        AU.assert_not_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_SBI', value_data_sub_code)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_description)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
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
        AU.assert_equals('transaction_code', 'DPT_SBI', value_data_step_cash_transaction_code)
        AU.assert_equals('transaction_number', value_data_transaction_number, value_data_step_cash_transaction_number)
        AU.assert_equals('transaction_type', 'SBI', value_data_step_cash_transaction_type)
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
        AU.assert_equals('description', '11802: Deposit savings book issue', value_data_step_cash_description)
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
        AU.assert_equals('amount_cash_change', total_fee, value_list_cash_amount_cash_change)
        AU.assert_equals('base_amount', 0, value_list_cash_base_amount)
        AU.assert_equals('debit_or_credit', 'D', value_list_cash_debit_or_credit)
        AU.assert_equals('currency_code', currency_code, value_list_cash_currency_code)
        AU.assert_equals('condition', "{\"expression\":{\"func\":\"&&\",\"type\":\"boolean\",\"paras\":[{\"func\":\"IsStringEqual\",\"type\":\"boolean\",\"paras\":[\"$.execution.input.fields.method\",\"CSH\"]}]}}", value_list_cash_condition)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
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
        AU.assert_equals('CurrencyCode', currency_code, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 2, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)

    def test_09_sp_dpt_sbi_011_error_current_account(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Stock registration
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
        # STEP 01-02: Stock assigned to teller
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
        # STEP 01-03: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_current_normal,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', f'Invalid deposit type [Current] of account [{account_number_current_normal}]- en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_012_error_fixed_deposit_account(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Stock registration
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
        # STEP 01-02: Stock assigned to teller
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
        # STEP 01-03: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_fixed_deposit_normal,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', f'Invalid deposit type [Fixed Deposit] of account [{account_number_fixed_deposit_normal}]- en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_013_error_prepaid_fixed_deposit_account(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Stock registration
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
        # STEP 01-02: Stock assigned to teller
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
        # STEP 01-03: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_prepaid_fixed_deposit_normal,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', f'Invalid deposit type [Fixed Deposit] of account [{account_number_prepaid_fixed_deposit_normal}]- en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_014_error_saving_account_status_closed(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Stock registration
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
        # STEP 01-02: Stock assigned to teller
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
        # STEP 01-03: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_closed,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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

    def test_09_sp_dpt_sbi_015_error_saving_account_status_block(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Stock registration
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
        # STEP 01-02: Stock assigned to teller
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
        # STEP 01-03: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_block,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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

    def test_09_sp_dpt_sbi_016_error_saving_account_status_pending(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Stock registration
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
        # STEP 01-02: Stock assigned to teller
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
        # STEP 01-03: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_pending,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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

    def test_09_sp_dpt_sbi_017_error_saving_account_has_passbook_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='CDMMK0000'
        catalog_name='Call deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S4'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        cn_status='D'
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
        # STEP 02-02: Stock registration second time
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
        # STEP 02-03: Stock assigned to teller
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
        # STEP 02-04: Stock confirm received
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
        # STEP 03: Deposit savings book issue second time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', f'This account aldready have stock with normal status\nThis account [{account_number}] already have a passbook number - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_018_error_saving_account_has_passbook_stop_payment(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='PSMMK0000'
        catalog_name='Premier savings deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S3'
        minimum_deposit_amount=50000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        cn_status='O'
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
        # STEP 02-02: Change passbook status to 'Stop payment'
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
        # STEP 03: Deposit savings book issue second time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', f'This account [{account_number}] already have a passbook number - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_019_error_saving_account_add_fee_fixed_deposit(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='DPT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_fixed_deposit_normal
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', f'Invalid deposit type [Fixed Deposit] of account [{account_number_fixed_deposit_normal}]- en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_020_error_saving_account_add_fee_prepaid_fixed_deposit(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='DPT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_prepaid_fixed_deposit_normal
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', f'Invalid deposit type [Fixed Deposit] of account [{account_number_prepaid_fixed_deposit_normal}]- en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_021_error_saving_account_add_fee_deposit_status_closed(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='DPT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_current_closed
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', 'Invalid amount [1500]\nInvalid account status [Closed]', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_022_error_saving_account_add_fee_deposit_status_block(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='DPT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_current_block
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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

    def test_09_sp_dpt_sbi_023_error_saving_account_add_fee_deposit_status_pending(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='DPT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_saving_pending
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', 'Invalid amount [1500]\nInvalid account status [Pending to approve]', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_024_error_saving_account_add_fee_deposit_status_new(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='DPT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_current_new
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', 'Invalid amount [1500]\nInvalid account status [New]', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_025_error_saving_account_add_fee_deposit_status_dormant(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='DPT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_current_dormant
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', 'Invalid account status [Dormant]', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_026_error_saving_account_add_fee_deposit_bigger_available_balance(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 01-06: Deposit money
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
        # STEP 01-07: Open current account
        method='DPT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
        gl_account_ifcc_02='003303030100010101'
        catalog_code='CAMMK0000'
        catalog_name='Current account in MMK'
        deposit_type='Current'
        deposit_sub_type='C1'
        minimum_deposit_amount_current=1000
        amount_deposit_current=ifc_amount_01+ifc_amount_02+minimum_deposit_amount_current-0.01
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
        # STEP 01-08: Approve current account
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
        # STEP 01-09: Deposit money to current account
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
        # STEP 02: Deposit savings book issue
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_current
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', f'Invalid amount [{total_fee}]', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_027_error_saving_account_add_fee_deposit_not_same_currency(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='DPT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='DPT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='DPT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=account_number_current_usd
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', 'Deposit.InvalidCcr', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_028_error_saving_account_add_fee_accounting_not_same_currency(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='ACT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='ACT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='ACT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=gl_account_usd
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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

    def test_09_sp_dpt_sbi_029_error_saving_account_add_fee_accounting_level_not_9(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='ACT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='ACT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='ACT'
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
        # Case 1: fee collect by GL level 7
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=gl_account_level_07
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', 'Accounting account is invalid - en\nDebit and credit currency must be the same', value_error_message)
        AU.assert_null('data', value_data)
        # Case 2: fee collect by GL level 8   
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=gl_account_level_08
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', 'Accounting account is invalid - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_030_error_saving_account_add_fee_accounting_not_same_branch(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='SAMMK0000'
        catalog_name='Savings account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S1'
        minimum_deposit_amount=1000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        method='ACT'
        total_fee=1500
        share_fee_01=0
        ifc_name_01='Passbook Replacement Fee (MMK)'
        value_type_01='F'
        ifc_code_01=311
        payrate_01=100
        ifc_value_01=1000
        ifc_amount_01=1000
        currency_account_code_01='MMK'
        floor_value_01=0
        ceiling_value_01=0
        share_rate_01=0
        share_amount_01=0
        round_rate_01=0
        round_amount_01=0
        currency_fee_code_01='MMK'
        pay_source_01='ACT'
        gl_account_ifcc_01='003303090100030301'
        share_fee_02=0
        ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
        value_type_02='F'
        ifc_code_02=340
        payrate_02=100
        ifc_value_02=500
        ifc_amount_02=500
        currency_account_code_02='MMK'
        floor_value_02=0
        ceiling_value_02=0
        share_rate_02=0
        share_amount_02=0
        round_rate_02=0
        round_amount_02=0
        currency_fee_code_02='MMK'
        pay_source_02='ACT'
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
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code,
            method=method,
            fee_data=fee_data,
            account_number_for_fee=gl_account_not_same_branch
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', 'Accounting account is invalid - en', value_error_message)
        AU.assert_null('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY VI LAM LECH MASTER-DATAIL CUA CASH
#     def test_09_sp_dpt_sbi_031_error_saving_account_add_fee_accounting_group_is_cash(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         catalog_code='SAMMK0000'
#         catalog_name='Savings account in MMK'
#         deposit_type='Savings'
#         deposit_sub_type='S1'
#         minimum_deposit_amount=1000
#         amount_deposit=200000.45
#         generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
#         print('generated_numbers: ', generated_numbers)
#         from_serial = to_serial = serial_no = generated_numbers
#         # STEP 01-01: Open saving account
#         fields_data_opn = sp_payload.DPT_OPN(
#             customer_code=customer_code_individual,
#             catalog_code=catalog_code,
#             catalog_name=catalog_name,
#             deposit_type=deposit_type,
#             account_name=account_name_individual,
#             deposit_sub_type=deposit_sub_type
#         )
#         rs = sp_helper.DPT_OPN(fields_data_opn)
#         step_code = 'DPT_OPN'
#         # 'response' - get data actual
#         data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_dpt_opn['status'])
#         # 'response' - get value 'account_number' under 'data'
#         AU.assert_exists('account_number', data_dpt_opn['data'])
#         AU.assert_exists('account_chart_number', data_dpt_opn['data'])
#         account_number = data_dpt_opn['data']['account_number']
#         gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
#         # STEP 01-02: Approve saving account
#         fields_data_apr = sp_payload.DPT_APR(
#             account_number=account_number,
#             branch_name=branch_name,
#             account_holder_name=account_name_individual,
#             catalog_code=catalog_code,
#             deposit_sub_type=deposit_sub_type,
#             deposit_type='S',
#             catalogue_name=catalog_name,
#             created_by=user_service['username']
#         )
#         rs = sp_helper.DPT_APR(fields_data_apr)
#         step_code = 'DPT_APR'
#         # 'response' - get data actual
#         data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_dpt_apr['status'])
#         # 'response' - verify value under 'data'
#         AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
#         # STEP 01-03: Stock registration
#         fields_data = sp_payload.DPT_SRG(
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix,
#             stock_type=stock_type
#         )
#         rs = sp_helper.DPT_SRG(fields_data)
#         step_code = 'DPT_SRG'
#         # 'response' - get data actual
#         data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_dpt_srg['status'])
#         # 'response' - get value 'account_number' under 'data'
#         AU.assert_exists('from_serial', data_dpt_srg['data'])
#         AU.assert_exists('to_serial', data_dpt_srg['data'])
#         AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
#         AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
#         # STEP 01-04: Stock assigned to teller
#         fields_data = sp_payload.DPT_SAT(
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix,
#             assigned_staff_code=assigned_staff_code,
#             stock_type=stock_type
#         )
#         rs = sp_helper.DPT_SAT(fields_data)
#         step_code = 'DPT_SAT'
#         # 'response' - get data actual
#         data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_dpt_sat['status'])
#         # 'response' - verify value under 'data'
#         AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
#         # STEP 01-05: Stock confirm received
#         fields_data = sp_payload.DPT_CCR(
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix,
#             stock_type=stock_type
#         )
#         rs = sp_helper.DPT_CCR(fields_data)
#         step_code = 'DPT_CCR'
#         # 'response' - get data actual
#         data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_dpt_ccr['status'])
#         # 'response' - verify value under 'data'
#         AU.assert_exists('from_serial', data_dpt_ccr['data'])
#         AU.assert_exists('to_serial', data_dpt_ccr['data'])
#         AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
#         AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
#         # STEP 02: Deposit savings book issue
#         method='ACT'
#         total_fee=1500
#         share_fee_01=0
#         ifc_name_01='Passbook Replacement Fee (MMK)'
#         value_type_01='F'
#         ifc_code_01=311
#         payrate_01=100
#         ifc_value_01=1000
#         ifc_amount_01=1000
#         currency_account_code_01='MMK'
#         floor_value_01=0
#         ceiling_value_01=0
#         share_rate_01=0
#         share_amount_01=0
#         round_rate_01=0
#         round_amount_01=0
#         currency_fee_code_01='MMK'
#         pay_source_01='ACT'
#         gl_account_ifcc_01='003303090100030301'
#         share_fee_02=0
#         ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
#         value_type_02='F'
#         ifc_code_02=340
#         payrate_02=100
#         ifc_value_02=500
#         ifc_amount_02=500
#         currency_account_code_02='MMK'
#         floor_value_02=0
#         ceiling_value_02=0
#         share_rate_02=0
#         share_amount_02=0
#         round_rate_02=0
#         round_amount_02=0
#         currency_fee_code_02='MMK'
#         pay_source_02='ACT'
#         fee_data = [
#             {
#                 "share_fee": share_fee_01,
#                 "ifc_name": ifc_name_01,
#                 "value_type": value_type_01,
#                 "ifc_code": ifc_code_01,
#                 "payrate": payrate_01,
#                 "ifc_value": ifc_value_01,
#                 "ifc_amount": ifc_amount_01,
#                 "currency_account_code": currency_account_code_01,
#                 "floor_value": floor_value_01,
#                 "ceiling_value": ceiling_value_01,
#                 "share_rate": share_rate_01,
#                 "share_amount": share_amount_01,
#                 "round_rate": round_rate_01,
#                 "round_amount": round_amount_01,
#                 "currency_fee_code": currency_fee_code_01,
#                 "pay_source": pay_source_01
#             },
#             {
#                 "share_fee": share_fee_02,
#                 "ifc_name": ifc_name_02,
#                 "value_type": value_type_02,
#                 "ifc_code": ifc_code_02,
#                 "payrate": payrate_02,
#                 "ifc_value": ifc_value_02,
#                 "ifc_amount": ifc_amount_02,
#                 "currency_account_code": currency_account_code_02,
#                 "floor_value": floor_value_02,
#                 "ceiling_value": ceiling_value_02,
#                 "share_rate": share_rate_02,
#                 "share_amount": share_amount_02,
#                 "round_rate": round_rate_02,
#                 "round_amount": round_amount_02,
#                 "currency_fee_code": currency_fee_code_02,
#                 "pay_source": pay_source_02
#             }
#         ]
#         fields_data = sp_payload.DPT_SBI(
#             account_number=account_number,
#             branch_name=branch_name,
#             serial_no=serial_no,
#             stock_prefix=stock_prefix,
#             currency_code=currency_code,
#             method=method,
#             fee_data=fee_data,
#             account_number_for_fee=gl_account_cash
#         )
#         rs = sp_helper.DPT_SBI(fields_data)
#         step_code = 'DPT_SBI'
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
#         AU.assert_equals('error_code', 'InvalidDepositStatus', value_error_code)
#         AU.assert_equals('error_message', 'Invalid deposit status [Pending to approve]', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)

# # CASE NAY TREN PRODUCTION KHONG VALIDATE, KHONG TEST CASE NAY
#     def test_09_sp_dpt_sbi_032_error_saving_account_add_fee_accounting_direct_posting_is_no(self, user):
#         sp_helper = StoredProcedureHelper(user)
#         catalog_code='SAMMK0000'
#         catalog_name='Savings account in MMK'
#         deposit_type='Savings'
#         deposit_sub_type='S1'
#         minimum_deposit_amount=1000
#         amount_deposit=200000.45
#         generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
#         print('generated_numbers: ', generated_numbers)
#         from_serial = to_serial = serial_no = generated_numbers
#         # STEP 01-01: Open saving account
#         fields_data_opn = sp_payload.DPT_OPN(
#             customer_code=customer_code_individual,
#             catalog_code=catalog_code,
#             catalog_name=catalog_name,
#             deposit_type=deposit_type,
#             account_name=account_name_individual,
#             deposit_sub_type=deposit_sub_type
#         )
#         rs = sp_helper.DPT_OPN(fields_data_opn)
#         step_code = 'DPT_OPN'
#         # 'response' - get data actual
#         data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_dpt_opn['status'])
#         # 'response' - get value 'account_number' under 'data'
#         AU.assert_exists('account_number', data_dpt_opn['data'])
#         AU.assert_exists('account_chart_number', data_dpt_opn['data'])
#         account_number = data_dpt_opn['data']['account_number']
#         gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
#         # STEP 01-02: Approve saving account
#         fields_data_apr = sp_payload.DPT_APR(
#             account_number=account_number,
#             branch_name=branch_name,
#             account_holder_name=account_name_individual,
#             catalog_code=catalog_code,
#             deposit_sub_type=deposit_sub_type,
#             deposit_type='S',
#             catalogue_name=catalog_name,
#             created_by=user_service['username']
#         )
#         rs = sp_helper.DPT_APR(fields_data_apr)
#         step_code = 'DPT_APR'
#         # 'response' - get data actual
#         data_dpt_apr = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_dpt_apr, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_dpt_apr['status'])
#         # 'response' - verify value under 'data'
#         AU.assert_equals('account_number', account_number, data_dpt_apr['data']['account_number'])
#         # STEP 01-03: Stock registration
#         fields_data = sp_payload.DPT_SRG(
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix,
#             stock_type=stock_type
#         )
#         rs = sp_helper.DPT_SRG(fields_data)
#         step_code = 'DPT_SRG'
#         # 'response' - get data actual
#         data_dpt_srg = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_dpt_srg, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_dpt_srg['status'])
#         # 'response' - get value 'account_number' under 'data'
#         AU.assert_exists('from_serial', data_dpt_srg['data'])
#         AU.assert_exists('to_serial', data_dpt_srg['data'])
#         AU.assert_equals('from_serial', from_serial, data_dpt_srg['data']['from_serial'])
#         AU.assert_equals('to_serial', to_serial, data_dpt_srg['data']['to_serial'])
#         # STEP 01-04: Stock assigned to teller
#         fields_data = sp_payload.DPT_SAT(
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix,
#             assigned_staff_code=assigned_staff_code,
#             stock_type=stock_type
#         )
#         rs = sp_helper.DPT_SAT(fields_data)
#         step_code = 'DPT_SAT'
#         # 'response' - get data actual
#         data_dpt_sat = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_dpt_sat, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_dpt_sat['status'])
#         # 'response' - verify value under 'data'
#         AU.assert_equals('assigned_staff_code', assigned_staff_code, data_dpt_sat['data']['assigned_staff_code'])
#         # STEP 01-05: Stock confirm received
#         fields_data = sp_payload.DPT_CCR(
#             from_serial=from_serial,
#             to_serial=to_serial,
#             stock_prefix=stock_prefix,
#             stock_type=stock_type
#         )
#         rs = sp_helper.DPT_CCR(fields_data)
#         step_code = 'DPT_CCR'
#         # 'response' - get data actual
#         data_dpt_ccr = RU.get_p2_content_response_by_step_code(rs, step_code)
#         print(json.dumps(data_dpt_ccr, indent=4, sort_keys=False))
#         # 'response' - verify value level 1
#         AU.assert_equals('status', 0, data_dpt_ccr['status'])
#         # 'response' - verify value under 'data'
#         AU.assert_exists('from_serial', data_dpt_ccr['data'])
#         AU.assert_exists('to_serial', data_dpt_ccr['data'])
#         AU.assert_equals('from_serial', from_serial, data_dpt_ccr['data']['from_serial'])
#         AU.assert_equals('to_serial', to_serial, data_dpt_ccr['data']['to_serial'])
#         # STEP 02: Deposit savings book issue
#         method='ACT'
#         total_fee=1500
#         share_fee_01=0
#         ifc_name_01='Passbook Replacement Fee (MMK)'
#         value_type_01='F'
#         ifc_code_01=311
#         payrate_01=100
#         ifc_value_01=1000
#         ifc_amount_01=1000
#         currency_account_code_01='MMK'
#         floor_value_01=0
#         ceiling_value_01=0
#         share_rate_01=0
#         share_amount_01=0
#         round_rate_01=0
#         round_amount_01=0
#         currency_fee_code_01='MMK'
#         pay_source_01='ACT'
#         gl_account_ifcc_01='003303090100030301'
#         share_fee_02=0
#         ifc_name_02='Deposit (MMK) For Same Region  (By Cash/Tr)'
#         value_type_02='F'
#         ifc_code_02=340
#         payrate_02=100
#         ifc_value_02=500
#         ifc_amount_02=500
#         currency_account_code_02='MMK'
#         floor_value_02=0
#         ceiling_value_02=0
#         share_rate_02=0
#         share_amount_02=0
#         round_rate_02=0
#         round_amount_02=0
#         currency_fee_code_02='MMK'
#         pay_source_02='ACT'
#         fee_data = [
#             {
#                 "share_fee": share_fee_01,
#                 "ifc_name": ifc_name_01,
#                 "value_type": value_type_01,
#                 "ifc_code": ifc_code_01,
#                 "payrate": payrate_01,
#                 "ifc_value": ifc_value_01,
#                 "ifc_amount": ifc_amount_01,
#                 "currency_account_code": currency_account_code_01,
#                 "floor_value": floor_value_01,
#                 "ceiling_value": ceiling_value_01,
#                 "share_rate": share_rate_01,
#                 "share_amount": share_amount_01,
#                 "round_rate": round_rate_01,
#                 "round_amount": round_amount_01,
#                 "currency_fee_code": currency_fee_code_01,
#                 "pay_source": pay_source_01
#             },
#             {
#                 "share_fee": share_fee_02,
#                 "ifc_name": ifc_name_02,
#                 "value_type": value_type_02,
#                 "ifc_code": ifc_code_02,
#                 "payrate": payrate_02,
#                 "ifc_value": ifc_value_02,
#                 "ifc_amount": ifc_amount_02,
#                 "currency_account_code": currency_account_code_02,
#                 "floor_value": floor_value_02,
#                 "ceiling_value": ceiling_value_02,
#                 "share_rate": share_rate_02,
#                 "share_amount": share_amount_02,
#                 "round_rate": round_rate_02,
#                 "round_amount": round_amount_02,
#                 "currency_fee_code": currency_fee_code_02,
#                 "pay_source": pay_source_02
#             }
#         ]
#         fields_data = sp_payload.DPT_SBI(
#             account_number=account_number,
#             branch_name=branch_name,
#             serial_no=serial_no,
#             stock_prefix=stock_prefix,
#             currency_code=currency_code,
#             method=method,
#             fee_data=fee_data,
#             account_number_for_fee=gl_account_direct_posting_no
#         )
#         rs = sp_helper.DPT_SBI(fields_data)
#         step_code = 'DPT_SBI'
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
#         AU.assert_equals('error_code', 'InvalidDepositStatus', value_error_code)
#         AU.assert_equals('error_message', 'Invalid deposit status [Pending to approve]', value_error_message)
#         AU.assert_not_null('data', value_data)
#         AU.assert_not_empty('data', value_data)

    def test_09_sp_dpt_sbi_033_error_account_number_is_empty(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number='',
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', 'FieldRequireValidator\n', value_error_code)
        AU.assert_equals('error_message', 'Account Number is required\nInvalid account number []', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_034_error_account_number_is_null(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=None,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', 'FieldRequireValidator\n', value_error_code)
        AU.assert_equals('error_message', 'Account Number is required\nInvalid account number []', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_035_error_account_number_not_exist(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number='111111111111',
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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

    def test_09_sp_dpt_sbi_036_error_serial_no_is_empty(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_new,
            branch_name=branch_name,
            serial_no='',
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', 'Serial No is required', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_037_error_serial_no_is_null(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_new,
            branch_name=branch_name,
            serial_no=None,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', 'Serial No is required', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_038_error_serial_no_not_exist(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_new,
            branch_name=branch_name,
            serial_no='SB000000',
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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

    def test_09_sp_dpt_sbi_039_error_serial_no_is_cheque(self, user):
        sp_helper = StoredProcedureHelper(user)
        stk_prefix='CQ'
        stk_type='C'
        generated_numbers = self.gen_serial_number(user, prefix=stk_prefix, s_type=stk_type) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-03: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stk_prefix,
            stock_type=stk_type
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
            stock_prefix=stk_prefix,
            assigned_staff_code=assigned_staff_code,
            stock_type=stk_type
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
            stock_prefix=stk_prefix,
            stock_type=stk_type
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_new,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stk_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', '\n\n', value_error_code)
        AU.assert_equals('error_message', f'Invalid serial number [{serial_no}]\nInvalid passbook status [{serial_no}] - en\nINVALID LEAF STATUS [{serial_no}] - EN', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_040_error_serial_no_is_receipt(self, user):
        sp_helper = StoredProcedureHelper(user)
        stk_prefix='RC'
        stk_type='R'
        generated_numbers = self.gen_serial_number(user, prefix=stk_prefix, s_type=stk_type) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-03: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stk_prefix,
            stock_type=stk_type
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
            stock_prefix=stk_prefix,
            assigned_staff_code=assigned_staff_code,
            stock_type=stk_type
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
            stock_prefix=stk_prefix,
            stock_type=stk_type
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_new,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stk_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', '\n\n', value_error_code)
        AU.assert_equals('error_message', f'Invalid serial number [{serial_no}]\nInvalid passbook status [{serial_no}] - en\nINVALID LEAF STATUS [{serial_no}] - EN', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_041_error_serial_no_is_passbook_for_fixed_deposit(self, user):
        sp_helper = StoredProcedureHelper(user)
        stk_prefix='FB'
        stk_type='F'
        generated_numbers = self.gen_serial_number(user, prefix=stk_prefix, s_type=stk_type) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-03: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stk_prefix,
            stock_type=stk_type
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
            stock_prefix=stk_prefix,
            assigned_staff_code=assigned_staff_code,
            stock_type=stk_type
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
            stock_prefix=stk_prefix,
            stock_type=stk_type
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_new,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stk_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', '\n\n', value_error_code)
        AU.assert_equals('error_message', f'Invalid serial number [{serial_no}]\nInvalid passbook status [{serial_no}] - en\nINVALID LEAF STATUS [{serial_no}] - EN', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_042_error_serial_no_is_payment_order(self, user):
        sp_helper = StoredProcedureHelper(user)
        stk_prefix='PO'
        stk_type='O'
        generated_numbers = self.gen_serial_number(user, prefix=stk_prefix, s_type=stk_type) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-03: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stk_prefix,
            stock_type=stk_type
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
            stock_prefix=stk_prefix,
            assigned_staff_code=assigned_staff_code,
            stock_type=stk_type
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
            stock_prefix=stk_prefix,
            stock_type=stk_type
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_new,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stk_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', '\n\n', value_error_code)
        AU.assert_equals('error_message', f'Invalid serial number [{serial_no}]\nInvalid passbook status [{serial_no}] - en\nINVALID LEAF STATUS [{serial_no}] - EN', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_043_error_serial_no_is_gift_cheque(self, user):
        sp_helper = StoredProcedureHelper(user)
        stk_prefix='GC'
        stk_type='G'
        generated_numbers = self.gen_serial_number(user, prefix=stk_prefix, s_type=stk_type) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-03: Stock registration
        fields_data = sp_payload.DPT_SRG(
            from_serial=from_serial,
            to_serial=to_serial,
            stock_prefix=stk_prefix,
            stock_type=stk_type
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
            stock_prefix=stk_prefix,
            assigned_staff_code=assigned_staff_code,
            stock_type=stk_type
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
            stock_prefix=stk_prefix,
            stock_type=stk_type
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_new,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stk_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', '\n\n', value_error_code)
        AU.assert_equals('error_message', f'Invalid serial number [{serial_no}]\nInvalid passbook status [{serial_no}] - en\nINVALID LEAF STATUS [{serial_no}] - EN', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_044_error_passbook_at_branch(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-03: Stock registration
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_new,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', f'Invalid passbook status [{serial_no}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_045_error_passbook_at_teller_not_confirm(self, user):
        sp_helper = StoredProcedureHelper(user)
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 02: Deposit savings book issue
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number_saving_new,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_message', f'Invalid confirm status [{serial_no}] - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_046_error_passbook_status_lost(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='PSMMK0000'
        catalog_name='Premier savings deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S3'
        minimum_deposit_amount=50000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
        # STEP 02-02: Change passbook status to 'Lost'
        cn_status='L'
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
        # STEP 03: Deposit savings book issue second time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', '\n\n', value_error_code)
        AU.assert_equals('error_message', f'Invalid passbook status [{serial_no}] - en\nINVALID LEAF STATUS [{serial_no}] - EN\nPassbook already in use - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_047_error_passbook_status_damage(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='PSMMK0000'
        catalog_name='Premier savings deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S3'
        minimum_deposit_amount=50000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
        # STEP 02-02: Change passbook status to 'Damage'
        cn_status='D'
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
        # STEP 03: Deposit savings book issue second time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', '\n\n', value_error_code)
        AU.assert_equals('error_message', f'Invalid passbook status [{serial_no}] - en\nINVALID LEAF STATUS [{serial_no}] - EN\nPassbook already in use - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_048_error_passbook_status_stop_payment(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='PSMMK0000'
        catalog_name='Premier savings deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S3'
        minimum_deposit_amount=50000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
        # STEP 02-02: Change passbook status to 'Stop payment'
        cn_status='O'
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
        # STEP 03: Deposit savings book issue second time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', '\n\n\n', value_error_code)
        AU.assert_equals('error_message', f'Invalid passbook status [{serial_no}] - en\nThis account [{account_number}] already have a passbook number - en\nINVALID LEAF STATUS [{serial_no}] - EN\nPassbook already in use - en', value_error_message)
        AU.assert_null('data', value_data)

    def test_09_sp_dpt_sbi_049_error_passbook_status_closed(self, user):
        sp_helper = StoredProcedureHelper(user)
        catalog_code='PSMMK0000'
        catalog_name='Premier savings deposit account in MMK'
        deposit_type='Savings'
        deposit_sub_type='S3'
        minimum_deposit_amount=50000
        amount_deposit=200000.45
        generated_numbers = self.gen_serial_number(user) # Ensure 5 digits padded with 0
        print('generated_numbers: ', generated_numbers)
        from_serial = to_serial = serial_no = generated_numbers
        # STEP 01-01: Open saving account
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
        # STEP 01-02: Approve saving account
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
        # STEP 01-03: Stock registration
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
        # STEP 01-04: Stock assigned to teller
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
        # STEP 01-05: Stock confirm received
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
        # STEP 02-01: Deposit savings book issue first time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
        # 'response' - get data actual
        data_dpt_sbi = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_sbi, indent=4, sort_keys=False))
        # 'response' - verify value level 1
        AU.assert_equals('status', 0, data_dpt_sbi['status'])
        # 'response' - verify value under 'data'
        AU.assert_exists('account_number', data_dpt_sbi['data'])
        AU.assert_equals('account_number', account_number, data_dpt_sbi['data']['account_number'])
        AU.assert_exists('serial_no', data_dpt_sbi['data'])
        AU.assert_equals('serial_no', serial_no, data_dpt_sbi['data']['serial_no'])
        # STEP 02-02: Change passbook status to 'Closed'
        cn_status='C'
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
        # STEP 03: Deposit savings book issue second time
        fields_data = sp_payload.DPT_SBI(
            account_number=account_number,
            branch_name=branch_name,
            serial_no=serial_no,
            stock_prefix=stock_prefix,
            currency_code=currency_code
        )
        rs = sp_helper.DPT_SBI(fields_data)
        step_code = 'DPT_SBI'
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
        AU.assert_equals('error_code', '\n\n', value_error_code)
        AU.assert_equals('error_message', f'Invalid passbook status [{serial_no}] - en\nINVALID LEAF STATUS [{serial_no}] - EN\nPassbook already in use - en', value_error_message)
        AU.assert_null('data', value_data)

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
