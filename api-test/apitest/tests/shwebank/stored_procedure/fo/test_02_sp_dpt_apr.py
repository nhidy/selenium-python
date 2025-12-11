import json
import pytest

from datetime import datetime
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
account_type='Individual'
catalog_code='CAMMK0000'
catalog_name='Current account in MMK'
deposit_type='Current'
deposit_sub_type='C1'
description='Approve deposit account'
branch_name='003 - Bayint Naung Branch'
# data test invalid
# # data test trên 104
# account_number_not_same_branch='110020157511'
# account_number_normal='110039615086'
# account_number_new='110038698206'
# account_number_closed='110031738819'
# account_number_block='110037723297'
# account_number_dormant='110037212072'
# data test trên 198
account_number_not_same_branch='110017639963'
account_number_normal='110030017306'
account_number_new='110033365907'
account_number_closed='330036004809'
account_number_block='330032348105'
account_number_dormant='350033694102'

@pytest.fixture(scope='session')
def user():
    req = RU(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.SP_DPT_APR
class Test_SP_DPT_APR(object):

    def test_02_sp_dpt_apr_001_success(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
        fields_data = sp_payload.DPT_OPN(
            customer_code=customer_code_individual,
            catalog_code=catalog_code,
            catalog_name=catalog_name,
            deposit_type=deposit_type,
            account_name=account_name_individual,
            description='1100: Open new deposit account',
            deposit_sub_type=deposit_sub_type,
            reason_of_account_opening='Reason of Account Opening'
        )
        rs = sp_helper.DPT_OPN(fields_data)
        step_code = 'DPT_OPN'
        data_dpt_opn = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_dpt_opn, indent=4, sort_keys=False))
        # verify value response level 1
        AU.assert_equals('status', 0, data_dpt_opn['status'])
        # get value 'account_number' under 'data'
        AU.assert_exists('account_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        # query database
        sql_query_DepositAccount = f"SELECT * FROM [o9deposit].[dbo].[DepositAccount] WHERE AccountNumber='{account_number}'"
        sql_update_DepositAccount = f"UPDATE [o9deposit].[dbo].[DepositAccount] SET [LastTransactionDate] = DATEADD(day,-1,LastTransactionDate) WHERE AccountNumber='{account_number}'"
        RU.update_db(sql_update_DepositAccount)
        data_dpt_opn_DepositAccount = RU.query_db(sql_query_DepositAccount)
        # verify in database
        AU.assert_equals('DepositStatus', 'P', data_dpt_opn_DepositAccount['DepositStatus'][0])
        # AU.assert_null('UserApproved', data_dpt_opn_DepositAccount['UserApproved'][0])
        # STEP 02: approve deposit account
        fields_data_apr = sp_payload.DPT_APR(
            account_number=account_number,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            description=description,
            account_type=account_type,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_apr)
        step_code = 'DPT_APR'
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # get value in level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # verify value of key response in level 1
        AU.assert_equals('status', 0, value_status)
        AU.assert_empty('error_message', value_error_message)
        AU.assert_empty('error_code', value_error_code)
        AU.assert_not_null('data', value_data)
        # verify key response under 'data'
        AU.assert_exists(expected_key['data_dpt_apr'], data_actual['data'])
        # get value in 'data'
        value_data_account_number = data_actual['data']['account_number']
        value_data_account_holder_name = data_actual['data']['account_holder_name']
        value_data_branch_name = data_actual['data']['branch_name']
        value_data_catalog_code = data_actual['data']['catalog_code']
        value_data_account_type = data_actual['data']['account_type']
        value_data_catalogue_name = data_actual['data']['catalogue_name']
        value_data_deposit_type = data_actual['data']['deposit_type']
        value_data_deposit_sub_type = data_actual['data']['deposit_sub_type']
        value_data_created_by = data_actual['data']['created_by']
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
        assert value_data_account_number == account_number, "Expected: value of 'account_number' is NOT NULL."
        assert value_data_account_holder_name == account_name_individual, "Expected: value of 'account_holder_name' is NOT NULL."
        assert value_data_branch_name == branch_name, "Expected: value of 'branch_name' is NOT NULL."
        assert value_data_catalog_code == catalog_code, "Expected: value of 'catalog_code' is NOT NULL."
        assert value_data_account_type == account_type, "Expected: value of 'account_type' is NOT NULL."
        assert value_data_catalogue_name == catalog_name, "Expected: value of 'catalogue_name' is NOT NULL."
        assert value_data_deposit_type == 'C', "Expected: value of 'deposit_type' is NOT NULL."
        assert value_data_deposit_sub_type == deposit_sub_type, "Expected: value of 'deposit_sub_type' is NOT NULL."
        assert value_data_created_by == user_service['username'], "Expected: value of 'created_by' is NOT NULL."
        assert value_data_transaction_code == 'DPT_APR', "Expected: value of 'transaction_code' is NOT NULL."
        assert value_data_transaction_number is not None, "Expected: value of 'transaction_number' is NOT NULL."
        assert value_data_transaction_number != '', "Expected: value of 'transaction_number' is NOT EMPTY."
        assert value_data_transaction_type == 'APR', "Expected: value of 'transaction_type' is NOT NULL."
        assert value_data_sub_code == 'DPT_APR', "Expected: value of 'sub_code' is NOT NULL."
        assert value_data_transaction_date is not None, "Expected: value of 'transaction_date' is NOT NULL."
        assert value_data_service_sys_date is not None, "Expected: value of 'service_sys_date' is NOT NULL."
        assert value_data_reference_id is not None, "Expected: value of 'reference_id' is NOT NULL."
        assert value_data_ref_id is not None, "Expected: value of 'ref_id' is NOT NULL."
        assert value_data_transaction_date != '', "Expected: value of 'transaction_date' is NOT EMPTY."
        assert value_data_service_sys_date != '', "Expected: value of 'service_sys_date' is NOT EMPTY."
        assert value_data_reference_id != '', "Expected: value of 'reference_id' is NOT EMPTY."
        assert value_data_ref_id != '', "Expected: value of 'ref_id' is NOT EMPTY."
        assert value_data_reference_code == '', "Expected: value of 'reference_code' is NOT NULL."
        assert value_data_business_code == '', "Expected: value of 'business_code' is NOT NULL."
        assert value_data_value_date is not None, "Expected: value of 'value_date' is NOT NULL."
        assert value_data_value_date != '', "Expected: value of 'value_date' is NOT EMPTY."
        assert value_data_current_user_code == user_service['username'], "Expected: value of 'current_user_code' is NOT NULL."
        assert value_data_current_branch_code == user_service['branch_code'], "Expected: value of 'current_branch_code' is NOT NULL."
        assert value_data_current_username == user_service['fullname'], "Expected: value of 'current_username' is NOT NULL."
        assert value_data_current_loginname == user_service['username'], "Expected: value of 'current_loginname' is NOT NULL."
        assert value_data_user_approve == '', "Expected: value of 'user_approve' is NOT NULL."
        assert value_data_status == 'N', "Expected: value of 'status' is NOT NULL."
        assert value_data_is_reverse is False, "Expected: value of 'is_reverse' is NOT NULL."
        assert value_data_amount1 == 0, "Expected: value of 'amount1' is NOT NULL."
        assert value_data_description == description, "Expected: value of 'description' is NOT NULL."
        assert value_data_token == '*', "Expected: value of 'token' is NOT NULL."
        assert value_data_is_transaction_reverse is False, "Expected: value of 'is_transaction_reverse' is NOT NULL."
        assert value_data_is_transaction_compensated is False, "Expected: value of 'is_transaction_compensated' is NOT NULL."
        # verify in database - columns updated
        data_dpt_apr_DepositAccount = RU.query_db(sql_query_DepositAccount)
        diff_columns_DepositAccount = AU.db_compare_results('[o9deposit].[dbo].[DepositAccount]', data_dpt_opn_DepositAccount, data_dpt_apr_DepositAccount)
        AU.db_compare_columns(expected_col['DepositAccount_approve'], diff_columns_DepositAccount)
        # verify in database - value updated
        AU.assert_equals('DepositStatus', 'W', data_dpt_apr_DepositAccount['DepositStatus'][0])
        AU.assert_equals('UserApproved', user_service['username'], data_dpt_apr_DepositAccount['UserApproved'][0])

    def test_02_sp_dpt_apr_002_error_deposit_account_not_same_branch(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_APR(
            account_number=account_number_not_same_branch,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            description=description,
            account_type=account_type,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data)
        step_code = 'DPT_APR'
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # get value in level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # verify value of key response in level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'BranchNotAllow', value_error_code)
        AU.assert_equals('error_message', 'Only the branch holding the deposit account can be made', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_02_sp_dpt_apr_003_error_deposit_account_empty(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data_01 = sp_payload.DPT_APR(
            account_number='',
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            description=description,
            account_type=account_type,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data_01)
        step_code = 'DPT_APR'
        data_actual_01 = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual_01, indent=4, sort_keys=False))
        # verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual_01)
        # get value in level 1
        value_status = data_actual_01['status']
        value_error_message = data_actual_01['error_message']
        value_error_code = data_actual_01['error_code']
        value_data = data_actual_01['data']
        # verify value of key response in level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'NotEmptyValidator', value_error_code)
        AU.assert_equals('error_message', 'Account number is required', value_error_message)
        AU.assert_null('data', value_data)

    def test_02_sp_dpt_apr_004_error_deposit_account_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_APR(
            account_number=account_number_normal,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            description=description,
            account_type=account_type,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data)
        step_code = 'DPT_APR'
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # get value in level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # verify value of key response in level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'InvalidDepositStatus', value_error_code)
        AU.assert_equals('error_message', 'Invalid deposit status [Normal]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_02_sp_dpt_apr_005_error_deposit_account_new(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_APR(
            account_number=account_number_new,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            description=description,
            account_type=account_type,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data)
        step_code = 'DPT_APR'
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # get value in level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # verify value of key response in level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'InvalidDepositStatus', value_error_code)
        AU.assert_equals('error_message', 'Invalid deposit status [New]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_02_sp_dpt_apr_006_error_deposit_account_closed(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_APR(
            account_number=account_number_closed,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            description=description,
            account_type=account_type,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data)
        step_code = 'DPT_APR'
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # get value in level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # verify value of key response in level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'InvalidDepositStatus', value_error_code)
        AU.assert_equals('error_message', 'Invalid deposit status [Closed]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_02_sp_dpt_apr_007_error_deposit_account_block(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_APR(
            account_number=account_number_block,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            description=description,
            account_type=account_type,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data)
        step_code = 'DPT_APR'
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # get value in level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # verify value of key response in level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'InvalidDepositStatus', value_error_code)
        AU.assert_equals('error_message', 'Invalid deposit status [Block]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)

    def test_02_sp_dpt_apr_008_error_deposit_account_dormant(self, user):
        sp_helper = StoredProcedureHelper(user)
        fields_data = sp_payload.DPT_APR(
            account_number=account_number_dormant,
            branch_name=branch_name,
            account_holder_name=account_name_individual,
            description=description,
            account_type=account_type,
            catalog_code=catalog_code,
            deposit_sub_type=deposit_sub_type,
            deposit_type='C',
            catalogue_name=catalog_name,
            created_by=user_service['username']
        )
        rs = sp_helper.DPT_APR(fields_data)
        step_code = 'DPT_APR'
        data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
        print(json.dumps(data_actual, indent=4, sort_keys=False))
        # verify key response level 1
        AU.assert_exists(expected_key['level_01'], data_actual)
        # get value in level 1
        value_status = data_actual['status']
        value_error_message = data_actual['error_message']
        value_error_code = data_actual['error_code']
        value_data = data_actual['data']
        # verify value of key response in level 1
        AU.assert_equals('status', 1, value_status)
        AU.assert_equals('error_code', 'InvalidDepositStatus', value_error_code)
        AU.assert_equals('error_message', 'Invalid deposit status [Dormant]', value_error_message)
        AU.assert_not_null('data', value_data)
        AU.assert_not_empty('data', value_data)