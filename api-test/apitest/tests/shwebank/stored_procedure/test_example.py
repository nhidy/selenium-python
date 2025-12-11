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
# data test valid
amount_deposit=10000000.45
cash_currency='MMK'
branch_name='003 - Bayint Naung Branch'
depositor_address='Home, Street, Ward, Township'
values_date=user_service['working_date']
id_issue_date=user_service['working_date']
currency_deposit='MMK'
to_account_number_saving_single_valid='310035109637'
gl_account_cash='003101030100010101'

@pytest.fixture(scope='session')
def user():
    req = RU(user_service)
    req.login_neptune()
    req.login_service()
    return req

@pytest.mark.Example
class TestExample(object):

    # def test_001_DPT_CDP_001_success(self, user):
    #     # data test
    #     account_number='110030974696'
    #     amount_deposit=10000.45
    #     cash_currency='MMK'
    #     branch_name='003 - Bayint Naung Branch'
    #     account_name='TEST AUTO ADD PERSONAL'
    #     customer_code='11001572'
    #     depositor_address='Home, Street, Ward, Township'
    #     description='1110: Cash deposit'
    #     values_date='2023-08-23T00:00:00Z'
    #     id_issue_date='2023-08-23T00:00:00Z'
    #     currency_deposit='MMK'
    #     fee_data = [
    #         {
    #             "share_fee": 0.0,
    #             "ifc_name": "Deposit (MMK) For Same Region  (By Cash/Tr)",
    #             "value_type": "F",
    #             "ifc_code": 340,
    #             "payrate": 100,
    #             "ifc_value": 100.0,
    #             "ifc_amount": 100.0,
    #             "currency_account_code": "MMK",
    #             "floor_value": 0.0,
    #             "ceiling_value": 0.0,
    #             "share_rate": 0.0,
    #             "share_amount": 0.0,
    #             "round_rate": 0.0,
    #             "round_amount": 0.0,
    #             "currency_fee_code": "MMK",
    #             "pay_source": "CSH"
    #         }
    #     ]

    #     sp_helper = StoredProcedureHelper(user)
    #     fields_data = sp_payload.DPT_CDP(
    #         account_number=account_number,
    #         amount_deposit=amount_deposit,
    #         cash_currency=cash_currency,
    #         branch_name=branch_name,
    #         account_name=account_name,
    #         customer_code=customer_code,
    #         depositor_address=depositor_address,
    #         description=description,
    #         values_date=values_date,
    #         id_issue_date=id_issue_date,
    #         currency_deposit=currency_deposit,
    #         fee_data=fee_data
    #     )
    #     rs = sp_helper.DPT_CDP(fields_data)
    #     step_code = 'DPT_CDP'
    #     data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     print(json.dumps(data_actual, indent=4, sort_keys=False))
    #     # verify key response
    #     assert 'transaction_number' in data_actual['data'], f"Expected: 'transaction_number' exists, Actual: response Json: {json.dumps(data_actual, indent=4, sort_keys=False)}"
    #     transaction_number = data_actual['data']['transaction_number']
    #     print('transaction_number: ', transaction_number)
    #     # verify value of key response
    #     assert transaction_number is not None, f"Expected: value of 'transaction_number' is NOT NULL, Actual: response Json: {json.dumps(data_actual, indent=4, sort_keys=False)}"
        
    #     account_number='110030974696'
    #     customer_code='11001572'
    #     dormant_period=1095
    #     current_balance=8730016.37
    #     open_date=datetime.strptime('2023-08-23', '%Y-%m-%d')
    #     updated_on_utc=datetime.strptime('2024-11-15 09:22:50.535367', '%Y-%m-%d %H:%M:%S.%f')

    #     # print('type account_number: ', type(account_number))
    #     # print('type customer_code: ', type(customer_code))
    #     # print('type dormant_period: ', type(dormant_period))
    #     # print('type current_balance: ', type(current_balance))
    #     # print('type open_date: ', type(open_date))

    #     sql_query = f"SELECT * FROM [o9deposit].[dbo].[DepositAccount] WHERE AccountNumber='{account_number}'"
    #     # sql_query = 'SELECT TOP 50 * FROM [o9admin].[dbo].[Branch]'
    #     data_after = RU.query_db(sql_query)
    #     # print(data)
    #     db_RolloverToCatalog = data_after['RolloverToCatalog'][0]
    #     db_PassbookOrReceiptNumber = data_after['PassbookOrReceiptNumber'][0]
    #     db_CustomerCode = data_after['CustomerCode'][0]
    #     db_DormantPeriod = data_after['DormantPeriod'][0]
    #     db_CurrentBalance = data_after['CurrentBalance'][0]
    #     db_OpenDate = data_after['OpenDate'][0]
    #     db_CreatedOnUtc = data_after['CreatedOnUtc'][0]
    #     db_UpdatedOnUtc = data_after['UpdatedOnUtc'][0]
        
    #     # print('db_RolloverToCatalog: ', db_RolloverToCatalog, '| type: ', type(db_RolloverToCatalog))
    #     # print('db_PassbookOrReceiptNumber: ', db_PassbookOrReceiptNumber, '| type: ', type(db_PassbookOrReceiptNumber))
    #     # print('db_CustomerCode: ', db_CustomerCode, '| type: ', type(db_CustomerCode))
    #     # print('db_DormantPeriod: ', db_DormantPeriod, '| type: ', type(db_DormantPeriod))
    #     # print('db_CurrentBalance: ', db_CurrentBalance, '| type: ', type(db_CurrentBalance))
    #     # print('db_OpenDate: ', db_OpenDate, '| type: ', type(db_OpenDate))

    #     assert db_RolloverToCatalog == '', f"Expected: value is empty."
    #     assert db_PassbookOrReceiptNumber is None, f"Expected: value is NULL."
    #     assert db_CustomerCode == customer_code, f"Expected: value is '{customer_code}'."
    #     assert db_DormantPeriod == dormant_period, f"Expected: value is NULL."
    #     assert db_CurrentBalance == current_balance, f"Expected: value is NULL."
    #     assert db_OpenDate == open_date, f"Expected: value is NULL."
    #     assert db_UpdatedOnUtc == updated_on_utc, f"Expected: value is NULL."
    #     assert db_CreatedOnUtc != updated_on_utc, f"Expected: value is NULL."

    # def test_001_DPT_CDP_001_success(self, user):
    #     # data test
    #     account_number='110030974696'
    #     amount_deposit=10000.45
    #     cash_currency='MMK'
    #     branch_name='003 - Bayint Naung Branch'
    #     account_name='TEST AUTO ADD PERSONAL'
    #     customer_code='11001572'
    #     depositor_address='Home, Street, Ward, Township'
    #     description='1110: Cash deposit'
    #     values_date='2023-08-23T00:00:00Z'
    #     id_issue_date='2023-08-23T00:00:00Z'
    #     currency_deposit='MMK'
    #     sql_query_DepositAccount = f"SELECT * FROM [o9deposit].[dbo].[DepositAccount] WHERE AccountNumber='{account_number}'"
    #     sql_update_DepositAccount = f"UPDATE [o9deposit].[dbo].[DepositAccount] SET [LastTransactionDate] = DATEADD(day,-1,LastTransactionDate) WHERE AccountNumber='{account_number}'"
    #     RU.update_db(sql_update_DepositAccount)
    #     data_before_DepositAccount = RU.query_db(sql_query_DepositAccount)
    #     # sql_query = 'SELECT TOP 50 * FROM [o9admin].[dbo].[Branch]'
    #     sp_helper = StoredProcedureHelper(user)
    #     fields_data = sp_payload.DPT_CDP(
    #         account_number=account_number,
    #         amount_deposit=amount_deposit,
    #         cash_currency=cash_currency,
    #         branch_name=branch_name,
    #         account_name=account_name,
    #         customer_code=customer_code,
    #         depositor_address=depositor_address,
    #         description=description,
    #         values_date=values_date,
    #         id_issue_date=id_issue_date,
    #         currency_deposit=currency_deposit
    #     )
    #     rs = sp_helper.DPT_CDP(fields_data)
    #     step_code = 'DPT_CDP'
    #     data_actual = RU.get_p2_content_response_by_step_code(rs, step_code)
    #     # verify key response under 'data'
    #     expected_key = [
    #         'account_number',
    #         'transaction_number',
    #         'amount_deposit',
    #         'amount',
    #         'depositor_description',
    #         'inclusive',
    #         'depositor_address',
    #         'identification_number',
    #         'currency_deposit',
    #         'values_date',
    #         'customer_code',
    #         'cash_amount_bcy',
    #     ]
    #     AU.assert_exists(expected_key, data_actual['data'])
    #     # get value in 'data'
    #     value_data_account_number = data_actual['data']['account_number']
    #     value_data_amount_deposit = data_actual['data']['amount_deposit']
    #     value_data_amount = data_actual['data']['amount']
    #     # verify value of key response in 'data'
    #     AU.assert_equals('account_number', account_number, value_data_account_number)
    #     AU.assert_equals('amount_deposit', amount_deposit, value_data_amount_deposit)
    #     AU.assert_equals('amount', 0.00, value_data_amount)
    #     # verify database
    #     data_after_DepositAccount = RU.query_db(sql_query_DepositAccount)
    #     diff_columns_DepositAccount = AU.db_compare_results('[o9deposit].[dbo].[DepositAccount]', data_before_DepositAccount, data_after_DepositAccount)

    #     data_before_DepositAccount_CurrentBalance = data_before_DepositAccount['CurrentBalance'][0]
    #     data_after_DepositAccount_CurrentBalance =data_after_DepositAccount['CurrentBalance'][0]
    #     AU.equals_decimal('CurrentBalance', amount_deposit, data_before_DepositAccount_CurrentBalance, data_after_DepositAccount_CurrentBalance)

    #     data_before_DepositAccount_DepositAmount = data_before_DepositAccount['DepositAmount'][0]
    #     data_after_DepositAccount_DepositAmount = data_after_DepositAccount['DepositAmount'][0]
    #     AU.equals_decimal('DepositAmount', amount_deposit, data_before_DepositAccount_DepositAmount, data_after_DepositAccount_DepositAmount)

    #     expected_columns_DepositAccount = [
    #         'DepositAmount',
    #         'CurrentBalance',
    #         'Psts',
    #         'WeekCredit',
    #         'MonthCredit',
    #         'QuarterCredit',
    #         'SemiAnnualCredit',
    #         'YearCredit',
    #         'UpdatedOnUtc',
    #         'LastTransactionDate'
    #     ]
    #     AU.db_compare_columns(expected_columns_DepositAccount, diff_columns_DepositAccount)

    def test_03_sp_dpt_cdp_001_success_current_account_status_new_normal(self, user):
        sp_helper = StoredProcedureHelper(user)
        # STEP 01: open deposit account
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
        AU.assert_exists('account_chart_number', data_dpt_opn['data'])
        account_number = data_dpt_opn['data']['account_number']
        gl_account_deposit = data_dpt_opn['data']['account_chart_number'][0]
        # database - query for next step
        sql_query_DepositAccount = f"SELECT * FROM [o9deposit].[dbo].[DepositAccount] WHERE AccountNumber='{account_number}'"
        sql_update_DepositAccount = f"UPDATE [o9deposit].[dbo].[DepositAccount] SET [LastTransactionDate] = DATEADD(day,-1,LastTransactionDate) WHERE AccountNumber='{account_number}'"
        RU.update_db(sql_update_DepositAccount)
        data_dpt_opn_DepositAccount = RU.query_db(sql_query_DepositAccount)
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
        # database - verify columns update
        data_dpt_apr_DepositAccount = RU.query_db(sql_query_DepositAccount)
        diff_columns_DepositAccount = AU.db_compare_results('[o9deposit].[dbo].[DepositAccount]', data_dpt_opn_DepositAccount, data_dpt_apr_DepositAccount)
        AU.db_compare_columns(expected_col['DepositAccount_approve'], diff_columns_DepositAccount)
        # database - verify value update
        AU.assert_equals('DepositStatus', 'W', data_dpt_apr_DepositAccount['DepositStatus'][0])
        AU.assert_equals('UserApproved', user_service['username'], data_dpt_apr_DepositAccount['UserApproved'][0])
        # database - query for next step - deposit
        RU.update_db(sql_update_DepositAccount)
        data_dpt_apr_DepositAccount = RU.query_db(sql_query_DepositAccount)
        # database - query for next step - cash - CashList
        sql_query_CashList = f"SELECT * FROM [o9cash].[dbo].[CashList] WHERE CashierCode='{user_service['username']}' AND CurrencyCode='{currency_deposit}'"
        data_dpt_apr_CashList = RU.query_db(sql_query_CashList)
        # database - query for next step - cash - CashStatement
        sql_query_CashStatement = f"SELECT * FROM [o9cash].[dbo].[CashStatement] WHERE CashierCode='{user_service['username']}' AND CurrencyCode='{currency_deposit}' AND CashType='D' AND ValueDate='{user_service['working_date']}'"
        data_dpt_apr_CashStatement = RU.query_db(sql_query_CashStatement)
        # database - query for next step - accounting
        sql_query_AccountBalance_DEPOSIT = f"SELECT * FROM [o9accounting].[dbo].[AccountBalance] WHERE AccountNumber='{gl_account_deposit}'"
        sql_query_AccountBalance_CASH = f"SELECT * FROM [o9accounting].[dbo].[AccountBalance] WHERE AccountNumber='{gl_account_cash}'"
        data_dpt_apr_AccountBalance_DEPOSIT = RU.query_db(sql_query_AccountBalance_DEPOSIT)
        data_dpt_apr_AccountBalance_CASH = RU.query_db(sql_query_AccountBalance_CASH)
        # STEP 03: cash deposit for deposit status 'New'
        fields_data_01 = sp_payload.DPT_CDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_deposit
        )
        rs_01 = sp_helper.DPT_CDP(fields_data_01)
        step_code = 'DPT_CDP'
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_01, step_code)
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
        AU.assert_not_empty('TransactionNumber', value_TransactionNumber)
        AU.assert_not_null('TransactionNumber', value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', amount_deposit, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_deposit, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
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
        AU.assert_exists(expected_key['data_dpt_cdp'], data_actual_01['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_cdp_depositor_description'], data_actual_01['data']['depositor_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual_01['data']['account_number']
        value_data_amount_deposit = data_actual_01['data']['amount_deposit']
        value_data_amount = data_actual_01['data']['amount']
        value_data_home = data_actual_01['data']['depositor_description']['home']
        value_data_office = data_actual_01['data']['depositor_description']['office']
        value_data_inclusive = data_actual_01['data']['inclusive']
        value_data_depositor_address = data_actual_01['data']['depositor_address']
        value_data_identification_number = data_actual_01['data']['identification_number']
        value_data_currency_deposit = data_actual_01['data']['currency_deposit']
        value_data_values_date = data_actual_01['data']['values_date']
        value_data_customer_code = data_actual_01['data']['customer_code']
        value_data_cash_amount_bcy = data_actual_01['data']['cash_amount_bcy']
        value_data_id_place = data_actual_01['data']['id_place']
        value_data_cash_exchange_rate = data_actual_01['data']['cash_exchange_rate']
        value_data_cash_amount = data_actual_01['data']['cash_amount']
        value_data_cash_currency = data_actual_01['data']['cash_currency']
        value_data_prepaid_interest = data_actual_01['data']['prepaid_interest']
        value_data_account_name = data_actual_01['data']['account_name']
        value_data_exchange_rate = data_actual_01['data']['exchange_rate']
        value_data_cross_rate = data_actual_01['data']['cross_rate']
        value_data_deposit_type = data_actual_01['data']['deposit_type']
        value_data_interest_tenor_unit = data_actual_01['data']['interest_tenor_unit']
        value_data_commission = data_actual_01['data']['commission']
        value_data_id_issue_date = data_actual_01['data']['id_issue_date']
        value_data_base_amount = data_actual_01['data']['base_amount']
        value_data_total_ifc_fee = data_actual_01['data']['total_ifc_fee']
        value_data_fee_currency_code = data_actual_01['data']['fee_currency_code']
        value_data_round_total_ifc_fee = data_actual_01['data']['round_total_ifc_fee']
        value_data_branch_name = data_actual_01['data']['branch_name']
        value_data_fee_data = data_actual_01['data']['fee_data']
        value_data_account_balances = data_actual_01['data']['account_balances']
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
        AU.assert_equals('amount', 0, value_data_amount)
        AU.assert_empty('home', value_data_home)
        AU.assert_empty('office', value_data_office)
        AU.assert_empty('inclusive', value_data_inclusive)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_empty('identification_number', value_data_identification_number)
        AU.assert_equals('currency_deposit', currency_deposit, value_data_currency_deposit)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('customer_code', customer_code_individual, value_data_customer_code)
        AU.assert_equals('cash_amount_bcy', 0, value_data_cash_amount_bcy)
        AU.assert_empty('id_place', value_data_id_place)
        AU.assert_equals('cash_exchange_rate', 1, value_data_cash_exchange_rate)
        AU.assert_equals('cash_amount', 0, value_data_cash_amount)
        AU.assert_equals('cash_currency', cash_currency, value_data_cash_currency)
        AU.assert_equals('prepaid_interest', 0, value_data_prepaid_interest)
        AU.assert_equals('account_name', account_name_individual, value_data_account_name)
        AU.assert_equals('exchange_rate', 1, value_data_exchange_rate)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_empty('deposit_type', value_data_deposit_type)
        AU.assert_empty('interest_tenor_unit', value_data_interest_tenor_unit)
        AU.assert_equals('commission', 0, value_data_commission)
        AU.assert_equals('id_issue_date', id_issue_date, value_data_id_issue_date)
        AU.assert_equals('base_amount', 0, value_data_base_amount)
        AU.assert_equals('total_ifc_fee', 0, value_data_total_ifc_fee)
        AU.assert_null('fee_currency_code', value_data_fee_currency_code)
        AU.assert_equals('round_total_ifc_fee', 0, value_data_round_total_ifc_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('transaction_code', 'DPT_CDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_number', value_TransactionNumber, value_data_transaction_number)
        AU.assert_equals('transaction_type', 'CDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_CDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
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
        AU.assert_equals('is_reverse',  False, value_data_is_reverse)
        AU.assert_equals('amount1', 0, value_data_amount1)
        AU.assert_equals('description', '1110: Cash deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)

        # database - verify columns update - o9deposit - DepositAccount
        data_dpt_cdp_01_DepositAccount = RU.query_db(sql_query_DepositAccount)
        diff_columns_DepositAccount = AU.db_compare_results('[o9deposit].[dbo].[DepositAccount]', data_dpt_apr_DepositAccount, data_dpt_cdp_01_DepositAccount)
        AU.db_compare_columns(expected_col['DepositAccount_deposit_new'], diff_columns_DepositAccount)
        # database - verify value update - o9deposit - DepositAccount
        data_dpt_apr_DepositAccount_CurrentBalance = data_dpt_apr_DepositAccount['CurrentBalance'][0]
        data_dpt_cdp_01_DepositAccount_CurrentBalance =data_dpt_cdp_01_DepositAccount['CurrentBalance'][0]
        AU.equals_decimal('CurrentBalance', amount_deposit, data_dpt_apr_DepositAccount_CurrentBalance, data_dpt_cdp_01_DepositAccount_CurrentBalance)
        data_dpt_apr_DepositAccount_DepositAmount = data_dpt_apr_DepositAccount['DepositAmount'][0]
        data_dpt_cdp_01_DepositAccount_DepositAmount = data_dpt_cdp_01_DepositAccount['DepositAmount'][0]
        AU.equals_decimal('DepositAmount', amount_deposit, data_dpt_apr_DepositAccount_DepositAmount, data_dpt_cdp_01_DepositAccount_DepositAmount)

        # database - verify value insert - o9deposit - DepositHistory
        sql_query_DepositHistory = f"SELECT * FROM [o9deposit].[dbo].[DepositHistory] WHERE AccountNumber='{account_number}'"
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[DepositHistory]', 3, len(RU.query_db(sql_query_DepositHistory)))
        # verify data in row of transaction
        sql_query_DepositHistory = f"SELECT * FROM [o9deposit].[dbo].[DepositHistory] WHERE AccountNumber='{account_number}' AND RefId='{value_data_ref_id}'"
        data_DepositHistory = RU.query_db(sql_query_DepositHistory)
        AU.assert_not_empty('Id', data_DepositHistory['Id'][0])
        AU.assert_not_null('Id', data_DepositHistory['Id'][0])
        AU.assert_equals('AccountNumber', account_number, data_DepositHistory['AccountNumber'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_DepositHistory['ValueDate'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_DepositHistory['RefId'][0])
        AU.assert_not_empty('TransactionDate', data_DepositHistory['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_DepositHistory['TransactionDate'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_DepositHistory['TransactionCode'][0])
        AU.assert_equals('Amount', amount_deposit, data_DepositHistory['Amount'][0])
        AU.assert_equals('Dorc', 'C', data_DepositHistory['Dorc'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_DepositHistory['Description'][0])
        AU.assert_equals('UsrCode', user_service['username'], data_DepositHistory['UsrCode'][0])
        AU.assert_equals('Oder', 1, data_DepositHistory['Oder'][0])
        AU.assert_equals('DepositHistoryStatus', 'N', data_DepositHistory['DepositHistoryStatus'][0])
        AU.assert_equals('Stcode', 'CDP', data_DepositHistory['Stcode'][0])
        AU.assert_equals('Usrid', 0, data_DepositHistory['Usrid'][0])
        AU.assert_not_empty('CreatedOnUtc', data_DepositHistory['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_DepositHistory['CreatedOnUtc'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_DepositHistory['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_DepositHistory['UpdatedOnUtc'][0])
        AU.assert_equals('ChannelId', 'C', data_DepositHistory['ChannelId'][0])

        # database - verify value insert - o9deposit - DepositStatement
        sql_query_DepositStatement = f"SELECT * FROM [o9deposit].[dbo].[DepositStatement] WHERE AccountNumber='{account_number}'"
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[DepositStatement]', 1, len(RU.query_db(sql_query_DepositStatement)))
        # verify data in row of transaction
        sql_query_DepositStatement = f"SELECT * FROM [o9deposit].[dbo].[DepositStatement] WHERE AccountNumber='{account_number}' AND TransactionNumber='{value_data_transaction_number}'"
        data_DepositStatement = RU.query_db(sql_query_DepositStatement)
        AU.assert_not_empty('Id', data_DepositStatement['Id'][0])
        AU.assert_not_null('Id', data_DepositStatement['Id'][0])
        AU.assert_equals('AccountNumber', account_number, data_DepositStatement['AccountNumber'][0])
        AU.assert_not_empty('StatementDate', data_DepositStatement['StatementDate'][0])
        AU.assert_not_null('StatementDate', data_DepositStatement['StatementDate'][0])
        AU.assert_equals('ReferenceId', value_data_ref_id, data_DepositStatement['ReferenceId'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_DepositStatement['ValueDate'][0])
        AU.assert_equals('Amount', amount_deposit, data_DepositStatement['Amount'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_DepositStatement['CurrencyCode'][0])
        AU.assert_equals('ConvertAmount', 0, data_DepositStatement['ConvertAmount'][0])
        AU.assert_equals('StatementCode', 'DEP', data_DepositStatement['StatementCode'][0])
        AU.assert_equals('StatementStatus', 'N', data_DepositStatement['StatementStatus'][0])
        AU.assert_equals('RefNumber', '0', data_DepositStatement['RefNumber'][0])
        AU.assert_equals('TransCode', 'DPT_CREDIT_BALANCE', data_DepositStatement['TransCode'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_DepositStatement['Description'][0])
        AU.assert_not_empty('CreatedOnUtc', data_DepositStatement['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_DepositStatement['CreatedOnUtc'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_DepositStatement['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_DepositStatement['UpdatedOnUtc'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_DepositStatement['TransactionNumber'][0])

        # database - verify value insert - o9deposit - DepositAccountTrans
        sql_query_DepositAccountTrans = f"SELECT * FROM [o9deposit].[dbo].[DepositAccountTrans] WHERE DepositAccount='{account_number}'"
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[DepositAccountTrans]', 1, len(RU.query_db(sql_query_DepositAccountTrans)))
        # verify data in row of transaction
        sql_query_DepositAccountTrans = f"SELECT * FROM [o9deposit].[dbo].[DepositAccountTrans] WHERE DepositAccount='{account_number}' AND TransactionNumber='{value_data_transaction_number}'"
        data_DepositAccountTrans = RU.query_db(sql_query_DepositAccountTrans)
        AU.assert_not_empty('Id', data_DepositAccountTrans['Id'][0])
        AU.assert_not_null('Id', data_DepositAccountTrans['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_DepositAccountTrans['TransactionNumber'][0])
        AU.assert_equals('DepositAccount', account_number, data_DepositAccountTrans['DepositAccount'][0])
        AU.assert_equals('TransCode', 'DPT_CREDIT_BALANCE', data_DepositAccountTrans['TransCode'][0])
        AU.assert_equals('TransactionStatus', 'N', data_DepositAccountTrans['TransactionStatus'][0])
        AU.assert_equals('Amount', amount_deposit, data_DepositAccountTrans['Amount'][0])
        AU.assert_equals('GLPopulated', True, data_DepositAccountTrans['GLPopulated'][0])
        AU.assert_empty('CrossBranchCode', data_DepositAccountTrans['CrossBranchCode'][0])
        AU.assert_empty('CrossCurrencyCode', data_DepositAccountTrans['CrossCurrencyCode'][0])
        AU.assert_null('DebitSysAccountName', data_DepositAccountTrans['DebitSysAccountName'][0])
        AU.assert_null('CreditSysAccountName', data_DepositAccountTrans['CreditSysAccountName'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_DepositAccountTrans['BaseCurrencyAmount'][0])
        AU.assert_equals('TransId', value_TransId, data_DepositAccountTrans['TransId'][0])
        AU.assert_equals('GLGroup', value_AccountingGroup, data_DepositAccountTrans['GLGroup'][0])

        # database - verify value insert - o9deposit - GLEntries
        sql_query_GLEntries = f"SELECT * FROM [o9deposit].[dbo].[GLEntries] WHERE GLAccount='{gl_account_deposit}' AND TransactionNumber='{value_data_transaction_number}'"
        data_GLEntries = RU.query_db(sql_query_GLEntries)
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[GLEntries]', 1, len(data_GLEntries))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_GLEntries['Id'][0])
        AU.assert_not_null('Id', data_GLEntries['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_GLEntries['TransactionNumber'][0])
        AU.assert_equals('TransTableName', 'DepositAccountTrans', data_GLEntries['TransTableName'][0])
        AU.assert_equals('TransId', value_TransId, data_GLEntries['TransId'][0])
        AU.assert_equals('SysAccountName', 'DEPOSIT', data_GLEntries['SysAccountName'][0])
        AU.assert_equals('GLAccount', gl_account_deposit, data_GLEntries['GLAccount'][0])
        AU.assert_equals('DorC', 'C', data_GLEntries['DorC'][0])
        AU.assert_equals('TransactionStatus', 'N', data_GLEntries['TransactionStatus'][0])
        AU.assert_equals('Amount', amount_deposit, data_GLEntries['Amount'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_GLEntries['BranchCode'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_GLEntries['CurrencyCode'][0])
        AU.assert_empty('CrossBranchCode', data_GLEntries['CrossBranchCode'][0])
        AU.assert_empty('CrossCurrencyCode', data_GLEntries['CrossCurrencyCode'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_GLEntries['BaseCurrencyAmount'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_GLEntries['ValueDate'][0])
        AU.assert_equals('Posted', 1, data_GLEntries['Posted'][0])
        AU.assert_equals('AccountingGroup', value_AccountingGroup, data_GLEntries['AccountingGroup'][0])

        # database - verify value insert - o9deposit - Transaction
        sql_query_Transaction = f"SELECT * FROM [o9deposit].[dbo].[Transaction] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_Transaction = RU.query_db(sql_query_Transaction)
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[Transaction]', 1, len(data_Transaction))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_Transaction['Id'][0])
        AU.assert_not_null('Id', data_Transaction['Id'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_Transaction['TransactionCode'][0])
        AU.assert_equals('SubCode', 'DPT_CDP', data_Transaction['SubCode'][0])
        AU.assert_not_empty('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_Transaction['ValueDate'][0])
        AU.assert_not_empty('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_not_null('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_equals('ReferenceId', value_data_reference_id, data_Transaction['ReferenceId'][0])
        AU.assert_empty('ReferenceCode', data_Transaction['ReferenceCode'][0])
        AU.assert_empty('BusinessCode', data_Transaction['BusinessCode'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_Transaction['TransactionNumber'][0])
        AU.assert_null('TransId', data_Transaction['TransId'][0])
        AU.assert_equals('ChannelId', 'C', data_Transaction['ChannelId'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_Transaction['RefId'][0])
        AU.assert_equals('Status', 'C', data_Transaction['Status'][0])
        AU.assert_equals('IsReverse', False, data_Transaction['IsReverse'][0])
        AU.assert_equals('Amount1', 0, data_Transaction['Amount1'][0])
        AU.assert_not_empty('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_null('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_equals('RequestBody', '{}', data_Transaction['RequestBody'][0])
        AU.assert_not_empty('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_null('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_equals('ResponseBody', '{}', data_Transaction['ResponseBody'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_Transaction['Description'][0])
        AU.assert_not_empty('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_null('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_equals('StartTime', 0, data_Transaction['StartTime'][0])
        AU.assert_not_empty('Duration', data_Transaction['Duration'][0])
        AU.assert_not_null('Duration', data_Transaction['Duration'][0])
        AU.assert_not_equals('Duration', 0, data_Transaction['Duration'][0])
        AU.assert_equals('UserCode', user_service['username'], data_Transaction['UserCode'][0])
        AU.assert_equals('UserName', user_service['fullname'], data_Transaction['UserName'][0])
        AU.assert_equals('LoginName', user_service['username'], data_Transaction['LoginName'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_Transaction['BranchCode'][0])

        # database - verify value insert - o9deposit - TransactionDetails
        sql_query_TransactionDetails = f"SELECT * FROM [o9deposit].[dbo].[TransactionDetails] WHERE RefId='{value_data_ref_id}' ORDER BY Id"
        data_TransactionDetails = RU.query_db(sql_query_TransactionDetails)
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[TransactionDetails]', 11, len(data_TransactionDetails))
        # verify data in row 1 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][0])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][0])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][0])
        AU.assert_equals('FieldName', 'CurrentBalance', data_TransactionDetails['FieldName'][0])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][0])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][0])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][0])
        AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][0])
        AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][0])
        AU.assert_empty('Description', data_TransactionDetails['Description'][0])
        # verify data in row 2 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][1])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][1])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][1])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][1])
        AU.assert_equals('FieldName', 'DepositAmount', data_TransactionDetails['FieldName'][1])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][1])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][1])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][1])
        AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][1])
        AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][1])
        AU.assert_empty('Description', data_TransactionDetails['Description'][1])
        # verify data in row 3 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][2])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][2])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][2])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][2])
        AU.assert_equals('FieldName', 'MonthCredit', data_TransactionDetails['FieldName'][2])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][2])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][2])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][2])
        AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][2])
        AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][2])
        AU.assert_empty('Description', data_TransactionDetails['Description'][2])
        # verify data in row 4 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][3])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][3])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][3])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][3])
        AU.assert_equals('FieldName', 'QuarterCredit', data_TransactionDetails['FieldName'][3])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][3])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][3])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][3])
        AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][3])
        AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][3])
        AU.assert_empty('Description', data_TransactionDetails['Description'][3])
        # verify data in row 5 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][4])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][4])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][4])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][4])
        AU.assert_equals('FieldName', 'SemiAnnualCredit', data_TransactionDetails['FieldName'][4])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][4])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][4])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][4])
        AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][4])
        AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][4])
        AU.assert_empty('Description', data_TransactionDetails['Description'][4])
        # verify data in row 6 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][5])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][5])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][5])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][5])
        AU.assert_equals('FieldName', 'WeekCredit', data_TransactionDetails['FieldName'][5])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][5])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][5])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][5])
        AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][5])
        AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][5])
        AU.assert_empty('Description', data_TransactionDetails['Description'][5])
        # verify data in row 7 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][6])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][6])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][6])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][6])
        AU.assert_equals('FieldName', 'YearCredit', data_TransactionDetails['FieldName'][6])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][6])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][6])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][6])
        AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][6])
        AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][6])
        AU.assert_empty('Description', data_TransactionDetails['Description'][6])
        # verify data in row 8 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][7])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][7])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][7])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][7])
        AU.assert_equals('FieldName', 'DepositStatus', data_TransactionDetails['FieldName'][7])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][7])
        AU.assert_equals('UpdateType', 'A', data_TransactionDetails['UpdateType'][7])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][7])
        AU.assert_equals('OldValue', 'W', data_TransactionDetails['OldValue'][7])
        AU.assert_equals('NewValue', 'N', data_TransactionDetails['NewValue'][7])
        AU.assert_empty('Description', data_TransactionDetails['Description'][7])
        # verify data in row 9 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][8])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][8])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][8])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][8])
        AU.assert_equals('FieldName', 'DepositStatus', data_TransactionDetails['FieldName'][8])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][8])
        AU.assert_equals('UpdateType', 'A', data_TransactionDetails['UpdateType'][8])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][8])
        AU.assert_equals('OldValue', 'W', data_TransactionDetails['OldValue'][8])
        AU.assert_equals('NewValue', 'N', data_TransactionDetails['NewValue'][8])
        AU.assert_empty('Description', data_TransactionDetails['Description'][8])
        # verify data in row 10 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][9])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][9])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][9])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][9])
        AU.assert_equals('FieldName', 'LastTransactionDate', data_TransactionDetails['FieldName'][9])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][9])
        AU.assert_equals('UpdateType', 'A', data_TransactionDetails['UpdateType'][9])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][9])
        AU.assert_equals('OldValue', '2023-09-12', data_TransactionDetails['OldValue'][9])
        AU.assert_equals('NewValue', '2023-09-13', data_TransactionDetails['NewValue'][9])
        AU.assert_empty('Description', data_TransactionDetails['Description'][9])
        # verify data in row 11 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][10])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][10])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][10])
        AU.assert_equals('Entity', 'DepositAccount', data_TransactionDetails['Entity'][10])
        AU.assert_equals('FieldName', 'Psts', data_TransactionDetails['FieldName'][10])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][10])
        AU.assert_equals('UpdateType', 'A', data_TransactionDetails['UpdateType'][10])
        AU.assert_equals('EntityId', data_dpt_cdp_01_DepositAccount['Id'][0], data_TransactionDetails['EntityId'][10])
        AU.assert_equals('OldValue', 'P', data_TransactionDetails['OldValue'][10])
        AU.assert_equals('NewValue', 'P|W', data_TransactionDetails['NewValue'][10])
        AU.assert_empty('Description', data_TransactionDetails['Description'][10])

        # database - verify value insert or update - o9cash - CashList
        if len(data_dpt_apr_CashList) == 0: # insert
            data_CashList = RU.query_db(sql_query_CashList)
            # verify total row
            AU.assert_equals('Total row in table [o9cash].[dbo].[CashList]', 1, len(data_CashList))
            # verify data in row of transaction
            AU.assert_not_empty('Id', data_CashList['Id'][0])
            AU.assert_not_null('Id', data_CashList['Id'][0])
            AU.assert_equals('CashierCode', user_service['username'], data_CashList['CashierCode'][0])
            AU.assert_equals('CurrencyCode', currency_deposit, data_CashList['CurrencyCode'][0])
            AU.assert_equals('CurrentBalance', amount_deposit, data_CashList['CurrentBalance'][0])
            AU.assert_not_empty('CreatedOnUtc', data_CashList['CreatedOnUtc'][0])
            AU.assert_not_null('CreatedOnUtc', data_CashList['CreatedOnUtc'][0])
            AU.assert_not_empty('UpdatedOnUtc', data_CashList['UpdatedOnUtc'][0])
            AU.assert_not_null('UpdatedOnUtc', data_CashList['UpdatedOnUtc'][0])
        else: # update
            # verify columns update
            data_dpt_cdp_01_CashList = RU.query_db(sql_query_CashList)
            diff_columns_CashList = AU.db_compare_results('[o9cash].[dbo].[CashList]', data_dpt_apr_CashList, data_dpt_cdp_01_CashList)
            AU.db_compare_columns(expected_col['CashList'], diff_columns_CashList)
            # verify value update
            data_dpt_apr_CashList_CurrentBalance = data_dpt_apr_CashList['CurrentBalance'][0]
            data_dpt_cdp_01_CashList_CurrentBalance =data_dpt_cdp_01_CashList['CurrentBalance'][0]
            AU.equals_decimal('CurrentBalance', amount_deposit, data_dpt_apr_CashList_CurrentBalance, data_dpt_cdp_01_CashList_CurrentBalance)

        # database - verify value insert or update - o9cash - CashStatement
        if len(data_dpt_apr_CashStatement) == 0: # insert
            data_CashStatement = RU.query_db(sql_query_CashStatement)
            # verify total row
            AU.assert_equals('Total row in table [o9cash].[dbo].[CashStatement]', 1, len(data_CashStatement))
            # verify data in row of transaction
            AU.assert_not_empty('Id', data_CashStatement['Id'][0])
            AU.assert_not_null('Id', data_CashStatement['Id'][0])
            AU.assert_equals('CashierCode', user_service['username'], data_CashStatement['CashierCode'][0])
            AU.assert_equals('CurrencyCode', currency_deposit, data_CashStatement['CurrencyCode'][0])
            AU.assert_equals('CashAmount', amount_deposit, data_CashStatement['CashAmount'][0])
            AU.assert_equals('CashType', 'D', data_CashStatement['CashType'][0])
            AU.assert_not_empty('CreatedOnUtc', data_CashStatement['CreatedOnUtc'][0])
            AU.assert_not_null('CreatedOnUtc', data_CashStatement['CreatedOnUtc'][0])
            AU.assert_not_empty('UpdatedOnUtc', data_CashStatement['UpdatedOnUtc'][0])
            AU.assert_not_null('UpdatedOnUtc', data_CashStatement['UpdatedOnUtc'][0])
            AU.assert_not_empty('StatementDate', data_CashStatement['StatementDate'][0])
            AU.assert_not_null('StatementDate', data_CashStatement['StatementDate'][0])
            AU.assert_equals('ValueDate', user_service['working_date_db'], data_CashStatement['ValueDate'][0])
        else: # update
            # verify columns update
            data_dpt_cdp_01_CashStatement = RU.query_db(sql_query_CashStatement)
            diff_columns_CashStatement = AU.db_compare_results('[o9cash].[dbo].[CashStatement]', data_dpt_apr_CashStatement, data_dpt_cdp_01_CashStatement)
            AU.db_compare_columns(expected_col['CashStatement'], diff_columns_CashStatement)
            # verify value update
            data_dpt_apr_CashStatement_CashAmount = data_dpt_apr_CashStatement['CashAmount'][0]
            data_dpt_cdp_01_CashStatement_CashAmount =data_dpt_cdp_01_CashStatement['CashAmount'][0]
            AU.equals_decimal('CashAmount', amount_deposit, data_dpt_apr_CashStatement_CashAmount, data_dpt_cdp_01_CashStatement_CashAmount)

        # database - verify value insert - o9cash - CashTransaction
        sql_query_CashTransaction = f"SELECT * FROM [o9cash].[dbo].[CashTransaction] WHERE CashierCode='{user_service['username']}' AND CurrencyCode='{currency_deposit}' AND TransactionNumber='{value_data_transaction_number}'"
        data_CashTransaction = RU.query_db(sql_query_CashTransaction)
        # verify total row
        AU.assert_equals('Total row in table [o9cash].[dbo].[CashTransaction]', 1, len(data_CashTransaction))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_CashTransaction['Id'][0])
        AU.assert_not_null('Id', data_CashTransaction['Id'][0])
        AU.assert_equals('CashierCode', user_service['username'], data_CashTransaction['CashierCode'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_CashTransaction['CurrencyCode'][0])
        AU.assert_equals('Amount', amount_deposit, data_CashTransaction['Amount'][0])
        AU.assert_equals('TransCode', 'CSH_DEBIT_BALANCE', data_CashTransaction['TransCode'][0])
        AU.assert_not_empty('TransId', data_CashTransaction['TransId'][0])
        AU.assert_not_null('TransId', data_CashTransaction['TransId'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_CashTransaction['TransactionNumber'][0])
        AU.assert_equals('GLPopulated', True, data_CashTransaction['GLPopulated'][0])
        AU.assert_equals('TransactionStatus', 'N', data_CashTransaction['TransactionStatus'][0])
        AU.assert_not_empty('CreatedOnUtc', data_CashTransaction['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_CashTransaction['CreatedOnUtc'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_CashTransaction['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_CashTransaction['UpdatedOnUtc'][0])
        AU.assert_empty('CrossBranchCode', data_CashTransaction['CrossBranchCode'][0])
        AU.assert_empty('CrossCurrencyCode', data_CashTransaction['CrossCurrencyCode'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_CashTransaction['BaseCurrencyAmount'][0])
        AU.assert_equals('GLGroup', 1, data_CashTransaction['GLGroup'][0])

        # database - verify value insert - o9cash - GLEntries
        sql_query_GLEntries = f"SELECT * FROM [o9cash].[dbo].[GLEntries] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_GLEntries = RU.query_db(sql_query_GLEntries)
        # verify total row
        AU.assert_equals('Total row in table [o9cash].[dbo].[GLEntries]', 1, len(data_GLEntries))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_GLEntries['Id'][0])
        AU.assert_not_null('Id', data_GLEntries['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_GLEntries['TransactionNumber'][0])
        AU.assert_equals('TransTableName', 'CashList', data_GLEntries['TransTableName'][0])
        AU.assert_equals('TransId', data_CashTransaction['TransId'][0], data_GLEntries['TransId'][0])
        AU.assert_equals('SysAccountName', 'CASH', data_GLEntries['SysAccountName'][0])
        AU.assert_equals('GLAccount', gl_account_cash, data_GLEntries['GLAccount'][0])
        AU.assert_equals('DorC', 'D', data_GLEntries['DorC'][0])
        AU.assert_equals('TransactionStatus', 'N', data_GLEntries['TransactionStatus'][0])
        AU.assert_equals('Amount', amount_deposit, data_GLEntries['Amount'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_GLEntries['BranchCode'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_GLEntries['CurrencyCode'][0])
        AU.assert_empty('CrossBranchCode', data_GLEntries['CrossBranchCode'][0])
        AU.assert_empty('CrossCurrencyCode', data_GLEntries['CrossCurrencyCode'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_GLEntries['BaseCurrencyAmount'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_GLEntries['ValueDate'][0])
        AU.assert_equals('Posted', True, data_GLEntries['Posted'][0])
        AU.assert_equals('AccountingGroup', 1, data_GLEntries['AccountingGroup'][0])

        # database - verify value insert - o9cash - Transaction
        sql_query_Transaction = f"SELECT * FROM [o9cash].[dbo].[Transaction] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_Transaction = RU.query_db(sql_query_Transaction)
        # verify total row
        AU.assert_equals('Total row in table [o9cash].[dbo].[Transaction]', 1, len(data_Transaction))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_Transaction['Id'][0])
        AU.assert_not_null('Id', data_Transaction['Id'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_Transaction['TransactionCode'][0])
        AU.assert_equals('SubCode', 'CSH_UPDATE_CASH', data_Transaction['SubCode'][0])
        AU.assert_not_empty('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_Transaction['ValueDate'][0])
        AU.assert_not_empty('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_not_null('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_equals('ReferenceId', value_data_reference_id, data_Transaction['ReferenceId'][0])
        AU.assert_empty('ReferenceCode', data_Transaction['ReferenceCode'][0])
        AU.assert_empty('BusinessCode', data_Transaction['BusinessCode'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_Transaction['TransactionNumber'][0])
        AU.assert_null('TransId', data_Transaction['TransId'][0])
        AU.assert_equals('ChannelId', 'C', data_Transaction['ChannelId'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_Transaction['RefId'][0])
        AU.assert_equals('UserCode', user_service['username'], data_Transaction['UserCode'][0])
        AU.assert_equals('LoginName', user_service['username'], data_Transaction['LoginName'][0])
        AU.assert_equals('UserName', user_service['fullname'], data_Transaction['UserName'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_Transaction['BranchCode'][0])
        AU.assert_equals('Status', 'C', data_Transaction['Status'][0])
        AU.assert_equals('IsReverse', False, data_Transaction['IsReverse'][0])
        AU.assert_equals('Amount1', 0, data_Transaction['Amount1'][0])
        AU.assert_not_empty('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_null('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_equals('RequestBody', '{}', data_Transaction['RequestBody'][0])
        AU.assert_not_empty('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_null('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_equals('ResponseBody', '{}', data_Transaction['ResponseBody'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_Transaction['Description'][0])
        AU.assert_not_empty('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_null('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_equals('StartTime', 0, data_Transaction['StartTime'][0])
        AU.assert_not_empty('Duration', data_Transaction['Duration'][0])
        AU.assert_not_null('Duration', data_Transaction['Duration'][0])
        AU.assert_not_equals('Duration', 0, data_Transaction['Duration'][0])

        # database - verify value insert - o9cash - TransactionDetails
        sql_query_TransactionDetails = f"SELECT * FROM [o9cash].[dbo].[TransactionDetails] WHERE RefId='{value_data_ref_id}' ORDER BY Id"
        data_TransactionDetails = RU.query_db(sql_query_TransactionDetails)
        # verify total row
        AU.assert_equals('Total row in table [o9cash].[dbo].[TransactionDetails]', 2, len(data_TransactionDetails))
        # verify data in row 1 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][0])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][0])
        AU.assert_equals('Entity', 'CashList', data_TransactionDetails['Entity'][0])
        AU.assert_equals('FieldName', 'CurrentBalance', data_TransactionDetails['FieldName'][0])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][0])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][0])
        AU.assert_equals('EntityId', data_dpt_cdp_01_CashList['Id'][0], data_TransactionDetails['EntityId'][0])
        # AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][0])
        # AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][0])
        AU.assert_empty('Description', data_TransactionDetails['Description'][0])
        # verify data in row 2 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][1])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][1])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][1])
        AU.assert_equals('Entity', 'CashStatement', data_TransactionDetails['Entity'][1])
        AU.assert_equals('FieldName', 'CashAmount', data_TransactionDetails['FieldName'][1])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][1])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][1])
        AU.assert_equals('EntityId', data_dpt_cdp_01_CashStatement['Id'][0], data_TransactionDetails['EntityId'][1])
        # AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][1])
        # AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][1])
        AU.assert_empty('Description', data_TransactionDetails['Description'][1])

        # database - verify columns update - o9accounting - AccountBalance
        data_dpt_cdp_01_AccountBalance_DEPOSIT = RU.query_db(sql_query_AccountBalance_DEPOSIT)
        diff_columns_AccountBalance_DEPOSIT = AU.db_compare_results('[o9accounting].[dbo].[AccountBalance]: DEPOSIT', data_dpt_apr_AccountBalance_DEPOSIT, data_dpt_cdp_01_AccountBalance_DEPOSIT)
        data_dpt_cdp_01_AccountBalance_CASH = RU.query_db(sql_query_AccountBalance_CASH)
        diff_columns_AccountBalance_CASH = AU.db_compare_results('[o9accounting].[dbo].[AccountBalance]: CASH', data_dpt_apr_AccountBalance_CASH, data_dpt_cdp_01_AccountBalance_CASH)
        AU.db_compare_columns(expected_col['AccountBalance_credit'], diff_columns_AccountBalance_DEPOSIT)
        AU.db_compare_columns(expected_col['AccountBalance_debit'], diff_columns_AccountBalance_CASH)
        # database - verify value update - o9accounting - AccountBalance
        data_dpt_apr_AccountBalance_DEPOSIT = data_dpt_apr_AccountBalance_DEPOSIT['Balance'][0]
        data_dpt_cdp_01_AccountBalance_DEPOSIT =data_dpt_cdp_01_AccountBalance_DEPOSIT['Balance'][0]
        AU.equals_decimal('Balance', amount_deposit, data_dpt_apr_AccountBalance_DEPOSIT, data_dpt_cdp_01_AccountBalance_DEPOSIT)
        data_dpt_apr_AccountBalance_CASH = data_dpt_apr_AccountBalance_CASH['Balance'][0]
        data_dpt_cdp_01_AccountBalance_CASH =data_dpt_cdp_01_AccountBalance_CASH['Balance'][0]
        AU.equals_decimal('Balance', amount_deposit, -data_dpt_apr_AccountBalance_CASH, -data_dpt_cdp_01_AccountBalance_CASH)

        # database - verify value insert - o9accounting - GLEntries - DEPOSIT
        sql_query_GLEntries = f"SELECT * FROM [o9accounting].[dbo].[GLEntries] WHERE GLAccount='{gl_account_deposit}' AND TransactionNumber='{value_data_transaction_number}'"
        data_GLEntries = RU.query_db(sql_query_GLEntries)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[GLEntries]', 1, len(data_GLEntries))
        # verify data in row of transaction - DEPOSIT
        AU.assert_not_empty('Id', data_GLEntries['Id'][0])
        AU.assert_not_null('Id', data_GLEntries['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_GLEntries['TransactionNumber'][0])
        AU.assert_equals('TransTableName', 'DepositAccountTrans', data_GLEntries['TransTableName'][0])
        AU.assert_equals('TransId', data_DepositAccountTrans['TransId'][0], data_GLEntries['TransId'][0])
        AU.assert_equals('SysAccountName', 'DEPOSIT', data_GLEntries['SysAccountName'][0])
        AU.assert_equals('GLAccount', gl_account_deposit, data_GLEntries['GLAccount'][0])
        AU.assert_equals('DorC', 'C', data_GLEntries['DorC'][0])
        AU.assert_equals('TransactionStatus', 'N', data_GLEntries['TransactionStatus'][0])
        AU.assert_equals('Amount', amount_deposit, data_GLEntries['Amount'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_GLEntries['BranchCode'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_GLEntries['CurrencyCode'][0])
        AU.assert_null('CrossBranchCode', data_GLEntries['CrossBranchCode'][0])
        AU.assert_null('CrossCurrencyCode', data_GLEntries['CrossCurrencyCode'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_GLEntries['BaseCurrencyAmount'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_GLEntries['ValueDate'][0])
        AU.assert_equals('Posted', True, data_GLEntries['Posted'][0])
        AU.assert_equals('AccountingGroup', 1, data_GLEntries['AccountingGroup'][0])

        # database - verify value insert - o9accounting - GLEntries - CASH
        sql_query_GLEntries = f"SELECT * FROM [o9accounting].[dbo].[GLEntries] WHERE GLAccount='{gl_account_cash}' AND TransactionNumber='{value_data_transaction_number}'"
        data_GLEntries = RU.query_db(sql_query_GLEntries)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[GLEntries]', 1, len(data_GLEntries))
        # verify data in row of transaction - CASH
        AU.assert_not_empty('Id', data_GLEntries['Id'][0])
        AU.assert_not_null('Id', data_GLEntries['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_GLEntries['TransactionNumber'][0])
        AU.assert_equals('TransTableName', 'CashList', data_GLEntries['TransTableName'][0])
        AU.assert_equals('TransId', data_CashTransaction['TransId'][0], data_GLEntries['TransId'][0])
        AU.assert_equals('SysAccountName', 'CASH', data_GLEntries['SysAccountName'][0])
        AU.assert_equals('GLAccount', gl_account_cash, data_GLEntries['GLAccount'][0])
        AU.assert_equals('DorC', 'D', data_GLEntries['DorC'][0])
        AU.assert_equals('TransactionStatus', 'N', data_GLEntries['TransactionStatus'][0])
        AU.assert_equals('Amount', amount_deposit, data_GLEntries['Amount'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_GLEntries['BranchCode'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_GLEntries['CurrencyCode'][0])
        AU.assert_null('CrossBranchCode', data_GLEntries['CrossBranchCode'][0])
        AU.assert_null('CrossCurrencyCode', data_GLEntries['CrossCurrencyCode'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_GLEntries['BaseCurrencyAmount'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_GLEntries['ValueDate'][0])
        AU.assert_equals('Posted', True, data_GLEntries['Posted'][0])
        AU.assert_equals('AccountingGroup', 1, data_GLEntries['AccountingGroup'][0])

        # database - verify value insert - o9accounting - AccountStatement - DEPOSIT
        sql_query_AccountStatement = f"SELECT * FROM [o9accounting].[dbo].[AccountStatement] WHERE AccountNumber='{gl_account_deposit}' AND TransactionNumber='{value_data_transaction_number}'"
        data_AccountStatement = RU.query_db(sql_query_AccountStatement)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[AccountStatement]', 1, len(data_AccountStatement))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_AccountStatement['Id'][0])
        AU.assert_not_null('Id', data_AccountStatement['Id'][0])
        AU.assert_equals('AccountNumber', gl_account_deposit, data_AccountStatement['AccountNumber'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_AccountStatement['CurrencyCode'][0])
        AU.assert_equals('ConvertAmount', 0, data_AccountStatement['ConvertAmount'][0])
        AU.assert_equals('Amount', amount_deposit, data_AccountStatement['Amount'][0])
        AU.assert_equals('ReferenceId', value_data_ref_id, data_AccountStatement['ReferenceId'][0])
        AU.assert_equals('StatementStatus', 'N', data_AccountStatement['StatementStatus'][0])
        AU.assert_not_empty('StatementDate', data_AccountStatement['StatementDate'][0])
        AU.assert_not_null('StatementDate', data_AccountStatement['StatementDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_AccountStatement['ValueDate'][0])
        AU.assert_equals('StatementCode', 'DEP', data_AccountStatement['StatementCode'][0])
        AU.assert_empty('RefNumber', data_AccountStatement['RefNumber'][0])
        AU.assert_equals('TransCode', 'C', data_AccountStatement['TransCode'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_AccountStatement['Description'][0])
        AU.assert_not_empty('CreatedOnUtc', data_AccountStatement['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_AccountStatement['CreatedOnUtc'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_AccountStatement['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_AccountStatement['UpdatedOnUtc'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_AccountStatement['TransactionNumber'][0])

        # database - verify value insert - o9accounting - AccountStatement - CASH
        sql_query_AccountStatement = f"SELECT * FROM [o9accounting].[dbo].[AccountStatement] WHERE AccountNumber='{gl_account_cash}' AND TransactionNumber='{value_data_transaction_number}'"
        data_AccountStatement = RU.query_db(sql_query_AccountStatement)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[AccountStatement]', 1, len(data_AccountStatement))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_AccountStatement['Id'][0])
        AU.assert_not_null('Id', data_AccountStatement['Id'][0])
        AU.assert_equals('AccountNumber', gl_account_cash, data_AccountStatement['AccountNumber'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_AccountStatement['CurrencyCode'][0])
        AU.assert_equals('ConvertAmount', 0, data_AccountStatement['ConvertAmount'][0])
        AU.assert_equals('Amount', amount_deposit, data_AccountStatement['Amount'][0])
        AU.assert_equals('ReferenceId', value_data_ref_id, data_AccountStatement['ReferenceId'][0])
        AU.assert_equals('StatementStatus', 'N', data_AccountStatement['StatementStatus'][0])
        AU.assert_not_empty('StatementDate', data_AccountStatement['StatementDate'][0])
        AU.assert_not_null('StatementDate', data_AccountStatement['StatementDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_AccountStatement['ValueDate'][0])
        AU.assert_equals('StatementCode', 'WDR', data_AccountStatement['StatementCode'][0])
        AU.assert_empty('RefNumber', data_AccountStatement['RefNumber'][0])
        AU.assert_equals('TransCode', 'D', data_AccountStatement['TransCode'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_AccountStatement['Description'][0])
        AU.assert_not_empty('CreatedOnUtc', data_AccountStatement['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_AccountStatement['CreatedOnUtc'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_AccountStatement['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_AccountStatement['UpdatedOnUtc'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_AccountStatement['TransactionNumber'][0])

        # database - verify value insert - o9accounting - Transaction
        sql_query_Transaction = f"SELECT * FROM [o9accounting].[dbo].[Transaction] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_Transaction = RU.query_db(sql_query_Transaction)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[Transaction]', 1, len(data_Transaction))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_Transaction['Id'][0])
        AU.assert_not_null('Id', data_Transaction['Id'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_Transaction['TransactionCode'][0])
        AU.assert_equals('SubCode', 'ACT_EXECUTE_POSTING', data_Transaction['SubCode'][0])
        AU.assert_not_empty('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_Transaction['ValueDate'][0])
        AU.assert_not_empty('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_not_null('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_equals('ReferenceId', value_data_reference_id, data_Transaction['ReferenceId'][0])
        AU.assert_empty('ReferenceCode', data_Transaction['ReferenceCode'][0])
        AU.assert_empty('BusinessCode', data_Transaction['BusinessCode'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_Transaction['TransactionNumber'][0])
        AU.assert_null('TransId', data_Transaction['TransId'][0])
        AU.assert_equals('ChannelId', 'C', data_Transaction['ChannelId'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_Transaction['RefId'][0])
        AU.assert_equals('UserCode', user_service['username'], data_Transaction['UserCode'][0])
        AU.assert_equals('LoginName', user_service['username'], data_Transaction['LoginName'][0])
        AU.assert_equals('UserName', user_service['fullname'], data_Transaction['UserName'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_Transaction['BranchCode'][0])
        AU.assert_equals('Status', 'C', data_Transaction['Status'][0])
        AU.assert_equals('IsReverse', False, data_Transaction['IsReverse'][0])
        AU.assert_equals('Amount1', 0, data_Transaction['Amount1'][0])
        AU.assert_not_empty('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_null('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_equals('RequestBody', '{}', data_Transaction['RequestBody'][0])
        AU.assert_not_empty('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_null('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_equals('ResponseBody', '{}', data_Transaction['ResponseBody'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_Transaction['Description'][0])
        AU.assert_not_empty('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_null('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_equals('StartTime', 0, data_Transaction['StartTime'][0])
        AU.assert_not_empty('Duration', data_Transaction['Duration'][0])
        AU.assert_not_null('Duration', data_Transaction['Duration'][0])
        AU.assert_not_equals('Duration', 0, data_Transaction['Duration'][0])

        # database - verify value NOT insert - o9accounting - TransactionDetails
        sql_query_TransactionDetails = f"SELECT * FROM [o9accounting].[dbo].[TransactionDetails] WHERE RefId='{value_data_ref_id}' ORDER BY Id"
        data_TransactionDetails = RU.query_db(sql_query_TransactionDetails)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[TransactionDetails]', 0, len(data_TransactionDetails))

        # database - verify value insert - o9admin - TransactionJournalDone
        sql_query_TransactionJournalDone = f"SELECT * FROM [o9admin].[dbo].[TransactionJournalDone] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_TransactionJournalDone = RU.query_db(sql_query_TransactionJournalDone)
        # verify total row
        AU.assert_equals('Total row in table [o9admin].[dbo].[TransactionJournalDone]', 1, len(data_TransactionJournalDone))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_TransactionJournalDone['Id'][0])
        AU.assert_not_null('Id', data_TransactionJournalDone['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_TransactionJournalDone['TransactionNumber'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_TransactionJournalDone['TransactionCode'][0])
        AU.assert_not_empty('TransactionDate', data_TransactionJournalDone['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_TransactionJournalDone['TransactionDate'][0])
        AU.assert_equals('ReferenceId', value_data_reference_id, data_TransactionJournalDone['ReferenceId'][0])
        AU.assert_equals('UserCreated', user_service['username'], data_TransactionJournalDone['UserCreated'][0])
        AU.assert_equals('Status', 'C', data_TransactionJournalDone['Status'][0])
        AU.assert_equals('IsReverse', False, data_TransactionJournalDone['IsReverse'][0])
        AU.assert_equals('HasPosting', True, data_TransactionJournalDone['HasPosting'][0])
        AU.assert_equals('Amount1', amount_deposit, data_TransactionJournalDone['Amount1'][0])
        AU.assert_equals('Channel', 'C', data_TransactionJournalDone['Channel'][0])
        AU.assert_null('UserApprove', data_TransactionJournalDone['UserApprove'][0])
        AU.assert_null('UserReject', data_TransactionJournalDone['UserReject'][0])
        AU.assert_equals('String1', account_number, data_TransactionJournalDone['String1'][0])
        AU.assert_not_empty('TransactionBody', data_TransactionJournalDone['TransactionBody'][0])
        AU.assert_not_null('TransactionBody', data_TransactionJournalDone['TransactionBody'][0])
        AU.assert_not_equals('TransactionBody', '{}', data_TransactionJournalDone['TransactionBody'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_TransactionJournalDone['Description'][0])
        AU.assert_equals('CashAmount', amount_deposit, data_TransactionJournalDone['CashAmount'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_TransactionJournalDone['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_TransactionJournalDone['UpdatedOnUtc'][0])
        AU.assert_not_empty('CreatedOnUtc', data_TransactionJournalDone['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_TransactionJournalDone['CreatedOnUtc'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionJournalDone['RefId'][0])
        AU.assert_null('ApproveStatus', data_TransactionJournalDone['ApproveStatus'][0])
        AU.assert_null('ApproveReason', data_TransactionJournalDone['ApproveReason'][0])
        AU.assert_null('ApproveDate', data_TransactionJournalDone['ApproveDate'][0])
        AU.assert_null('RejectReason', data_TransactionJournalDone['RejectReason'][0])
        AU.assert_null('RejectDate', data_TransactionJournalDone['RejectDate'][0])
        AU.assert_null('ReverseReason', data_TransactionJournalDone['ReverseReason'][0])
        AU.assert_null('ReverseDate', data_TransactionJournalDone['ReverseDate'][0])
        AU.assert_null('UserReverse', data_TransactionJournalDone['UserReverse'][0])
        AU.assert_equals('ApproveLimit', 0, data_TransactionJournalDone['ApproveLimit'][0])

        # database - verify value insert - o9admin - Transaction
        sql_query_Transaction = f"SELECT * FROM [o9admin].[dbo].[Transaction] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_Transaction = RU.query_db(sql_query_Transaction)
        # verify total row
        AU.assert_equals('Total row in table [o9admin].[dbo].[Transaction]', 1, len(data_Transaction))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_Transaction['Id'][0])
        AU.assert_not_null('Id', data_Transaction['Id'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_Transaction['TransactionCode'][0])
        AU.assert_equals('SubCode', 'SQL_CAN_USER_INVOKE_COMMAND', data_Transaction['SubCode'][0])
        AU.assert_not_empty('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_Transaction['ValueDate'][0])
        AU.assert_not_empty('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_not_null('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_equals('ReferenceId', value_data_reference_id, data_Transaction['ReferenceId'][0])
        AU.assert_null('ReferenceCode', data_Transaction['ReferenceCode'][0])
        AU.assert_null('BusinessCode', data_Transaction['BusinessCode'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_Transaction['TransactionNumber'][0])
        AU.assert_null('TransId', data_Transaction['TransId'][0])
        AU.assert_equals('ChannelId', 'C', data_Transaction['ChannelId'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_Transaction['RefId'][0])
        AU.assert_equals('UserCode', user_service['username'], data_Transaction['UserCode'][0])
        AU.assert_equals('LoginName', user_service['username'], data_Transaction['LoginName'][0])
        AU.assert_equals('UserName', user_service['fullname'], data_Transaction['UserName'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_Transaction['BranchCode'][0])
        AU.assert_equals('Status', 'C', data_Transaction['Status'][0])
        AU.assert_equals('IsReverse', False, data_Transaction['IsReverse'][0])
        AU.assert_equals('Amount1', 0, data_Transaction['Amount1'][0])
        AU.assert_not_empty('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_null('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_equals('RequestBody', '{}', data_Transaction['RequestBody'][0])
        AU.assert_not_empty('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_null('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_equals('ResponseBody', '{}', data_Transaction['ResponseBody'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_Transaction['Description'][0])
        AU.assert_not_empty('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_null('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_equals('StartTime', 0, data_Transaction['StartTime'][0])
        AU.assert_not_empty('Duration', data_Transaction['Duration'][0])
        AU.assert_not_null('Duration', data_Transaction['Duration'][0])
        AU.assert_not_equals('Duration', 0, data_Transaction['Duration'][0])

        # database - verify value NOT insert - o9admin - TransactionDetails
        sql_query_TransactionDetails = f"SELECT * FROM [o9admin].[dbo].[TransactionDetails] WHERE RefId='{value_data_ref_id}' ORDER BY Id"
        data_TransactionDetails = RU.query_db(sql_query_TransactionDetails)
        # verify total row
        AU.assert_equals('Total row in table [o9admin].[dbo].[TransactionDetails]', 0, len(data_TransactionDetails))

        # database - query for next step - deposit
        RU.update_db(sql_update_DepositAccount)
        data_dpt_cdp_01_DepositAccount = RU.query_db(sql_query_DepositAccount)
        # database - query for next step - cash - CashList
        sql_query_CashList = f"SELECT * FROM [o9cash].[dbo].[CashList] WHERE CashierCode='{user_service['username']}' AND CurrencyCode='{currency_deposit}'"
        data_dpt_cdp_01_CashList = RU.query_db(sql_query_CashList)
        # database - query for next step - cash - CashStatement
        sql_query_CashStatement = f"SELECT * FROM [o9cash].[dbo].[CashStatement] WHERE CashierCode='{user_service['username']}' AND CurrencyCode='{currency_deposit}' AND CashType='D' AND ValueDate='{user_service['working_date']}'"
        data_dpt_cdp_01_CashStatement = RU.query_db(sql_query_CashStatement)
        # database - query for next step - accounting
        sql_query_AccountBalance_DEPOSIT = f"SELECT * FROM [o9accounting].[dbo].[AccountBalance] WHERE AccountNumber='{gl_account_deposit}'"
        sql_query_AccountBalance_CASH = f"SELECT * FROM [o9accounting].[dbo].[AccountBalance] WHERE AccountNumber='{gl_account_cash}'"
        data_dpt_cdp_01_AccountBalance_DEPOSIT = RU.query_db(sql_query_AccountBalance_DEPOSIT)
        data_dpt_cdp_01_AccountBalance_CASH = RU.query_db(sql_query_AccountBalance_CASH)

        # STEP 04: cash deposit for deposit status 'Normal'
        fields_data_02 = sp_payload.DPT_CDP(
            account_number=account_number_approved,
            amount_deposit=amount_deposit,
            cash_currency=cash_currency,
            branch_name=branch_name,
            account_name=account_name_individual,
            customer_code=customer_code_individual,
            depositor_address=depositor_address,
            values_date=values_date,
            id_issue_date=id_issue_date,
            currency_deposit=currency_deposit
        )
        rs_02 = sp_helper.DPT_CDP(fields_data_02)
        step_code = 'DPT_CDP'
        # 'postings' - get data actual
        data_actual_posting = RU.get_p2_content_postings_by_step_code(rs_02, step_code)
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
        AU.assert_not_empty('TransactionNumber', value_TransactionNumber)
        AU.assert_not_null('TransactionNumber', value_TransactionNumber)
        AU.assert_equals('TransTableName', 'DepositAccountTrans', value_TransTableName)
        AU.assert_not_empty('TransId', value_TransId)
        AU.assert_not_null('TransId', value_TransId)
        AU.assert_equals('SysAccountName', 'DEPOSIT', value_SysAccountName)
        AU.assert_equals('GLAccount', gl_account_deposit, value_GLAccount)
        AU.assert_equals('DorC', 'C', value_DorC)
        AU.assert_equals('TransactionStatus', 'N', value_TransactionStatus)
        AU.assert_equals('Amount', amount_deposit, value_Amount)
        AU.assert_equals('BranchCode', user_service['branch_code'], value_BranchCode)
        AU.assert_equals('CurrencyCode', currency_deposit, value_CurrencyCode)
        AU.assert_equals('ValueDate', user_service['working_date'], value_ValueDate)
        AU.assert_true('Posted', value_Posted)
        AU.assert_equals('AccountingGroup', 1, value_AccountingGroup)
        AU.assert_empty('CrossBranchCode', value_CrossBranchCode)
        AU.assert_empty('CrossCurrencyCode', value_CrossCurrencyCode)
        AU.assert_equals('BaseCurrencyAmount', 0, value_BaseCurrencyAmount)
        AU.assert_not_empty('Id', value_Id)
        AU.assert_not_null('Id', value_Id)
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
        AU.assert_exists(expected_key['data_dpt_cdp'], data_actual_02['data'])
        # 'response' - verify key response under 'data' and 'depositor_description'
        AU.assert_exists(expected_key['data_dpt_cdp_depositor_description'], data_actual_02['data']['depositor_description'])
        # 'response' - get value under 'data'
        value_data_account_number = data_actual_02['data']['account_number']
        value_data_amount_deposit = data_actual_02['data']['amount_deposit']
        value_data_amount = data_actual_02['data']['amount']
        value_data_home = data_actual_02['data']['depositor_description']['home']
        value_data_office = data_actual_02['data']['depositor_description']['office']
        value_data_inclusive = data_actual_02['data']['inclusive']
        value_data_depositor_address = data_actual_02['data']['depositor_address']
        value_data_identification_number = data_actual_02['data']['identification_number']
        value_data_currency_deposit = data_actual_02['data']['currency_deposit']
        value_data_values_date = data_actual_02['data']['values_date']
        value_data_customer_code = data_actual_02['data']['customer_code']
        value_data_cash_amount_bcy = data_actual_02['data']['cash_amount_bcy']
        value_data_id_place = data_actual_02['data']['id_place']
        value_data_cash_exchange_rate = data_actual_02['data']['cash_exchange_rate']
        value_data_cash_amount = data_actual_02['data']['cash_amount']
        value_data_cash_currency = data_actual_02['data']['cash_currency']
        value_data_prepaid_interest = data_actual_02['data']['prepaid_interest']
        value_data_account_name = data_actual_02['data']['account_name']
        value_data_exchange_rate = data_actual_02['data']['exchange_rate']
        value_data_cross_rate = data_actual_02['data']['cross_rate']
        value_data_deposit_type = data_actual_02['data']['deposit_type']
        value_data_interest_tenor_unit = data_actual_02['data']['interest_tenor_unit']
        value_data_commission = data_actual_02['data']['commission']
        value_data_id_issue_date = data_actual_02['data']['id_issue_date']
        value_data_base_amount = data_actual_02['data']['base_amount']
        value_data_total_ifc_fee = data_actual_02['data']['total_ifc_fee']
        value_data_fee_currency_code = data_actual_02['data']['fee_currency_code']
        value_data_round_total_ifc_fee = data_actual_02['data']['round_total_ifc_fee']
        value_data_branch_name = data_actual_02['data']['branch_name']
        value_data_fee_data = data_actual_02['data']['fee_data']
        value_data_account_balances = data_actual_02['data']['account_balances']
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
        AU.assert_equals('amount', 0, value_data_amount)
        AU.assert_empty('home', value_data_home)
        AU.assert_empty('office', value_data_office)
        AU.assert_empty('inclusive', value_data_inclusive)
        AU.assert_equals('depositor_address', depositor_address, value_data_depositor_address)
        AU.assert_empty('identification_number', value_data_identification_number)
        AU.assert_equals('currency_deposit', currency_deposit, value_data_currency_deposit)
        AU.assert_equals('values_date', values_date, value_data_values_date)
        AU.assert_equals('customer_code', customer_code_individual, value_data_customer_code)
        AU.assert_equals('cash_amount_bcy', 0, value_data_cash_amount_bcy)
        AU.assert_empty('id_place', value_data_id_place)
        AU.assert_equals('cash_exchange_rate', 1, value_data_cash_exchange_rate)
        AU.assert_equals('cash_amount', 0, value_data_cash_amount)
        AU.assert_equals('cash_currency', cash_currency, value_data_cash_currency)
        AU.assert_equals('prepaid_interest', 0, value_data_prepaid_interest)
        AU.assert_equals('account_name', account_name_individual, value_data_account_name)
        AU.assert_equals('exchange_rate', 1, value_data_exchange_rate)
        AU.assert_equals('cross_rate', 1, value_data_cross_rate)
        AU.assert_empty('deposit_type', value_data_deposit_type)
        AU.assert_empty('interest_tenor_unit', value_data_interest_tenor_unit)
        AU.assert_equals('commission', 0, value_data_commission)
        AU.assert_equals('id_issue_date', id_issue_date, value_data_id_issue_date)
        AU.assert_equals('base_amount', 0, value_data_base_amount)
        AU.assert_equals('total_ifc_fee', 0, value_data_total_ifc_fee)
        AU.assert_null('fee_currency_code', value_data_fee_currency_code)
        AU.assert_equals('round_total_ifc_fee', 0, value_data_round_total_ifc_fee)
        AU.assert_equals('branch_name', branch_name, value_data_branch_name)
        AU.assert_equals('fee_data', [], value_data_fee_data)
        AU.assert_equals('account_balances', [], value_data_account_balances)
        AU.assert_equals('transaction_code', 'DPT_CDP', value_data_transaction_code)
        AU.assert_not_null('transaction_number', value_data_transaction_number)
        AU.assert_not_empty('transaction_number', value_data_transaction_number)
        AU.assert_equals('transaction_number', value_TransactionNumber, value_data_transaction_number)
        AU.assert_equals('transaction_type', 'CDP', value_data_transaction_type)
        AU.assert_equals('sub_code', 'DPT_CDP', value_data_sub_code)
        AU.assert_not_null('transaction_date', value_data_transaction_date)
        AU.assert_not_null('service_sys_date', value_data_service_sys_date)
        AU.assert_not_null('reference_id', value_data_reference_id)
        AU.assert_not_null('ref_id', value_data_ref_id)
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
        AU.assert_equals('is_reverse',  False, value_data_is_reverse)
        AU.assert_equals('amount1', 0, value_data_amount1)
        AU.assert_equals('description', '1110: Cash deposit', value_data_description)
        AU.assert_equals('token', '*', value_data_token)
        AU.assert_equals('is_transaction_reverse',  False, value_data_is_transaction_reverse)
        AU.assert_equals('is_transaction_compensated',  False, value_data_is_transaction_compensated)

        # database - verify columns update - o9deposit - DepositAccount
        data_dpt_cdp_02_DepositAccount = RU.query_db(sql_query_DepositAccount)
        diff_columns_DepositAccount = AU.db_compare_results('[o9deposit].[dbo].[DepositAccount]', data_dpt_cdp_01_DepositAccount, data_dpt_cdp_02_DepositAccount)
        AU.db_compare_columns(expected_col['DepositAccount_deposit_normal'], diff_columns_DepositAccount)
        # database - verify value update - o9deposit - DepositAccount
        data_dpt_cdp_01_DepositAccount_CurrentBalance = data_dpt_cdp_01_DepositAccount['CurrentBalance'][0]
        data_dpt_cdp_02_DepositAccount_CurrentBalance = data_dpt_cdp_02_DepositAccount['CurrentBalance'][0]
        AU.equals_decimal('CurrentBalance', amount_deposit, data_dpt_cdp_01_DepositAccount_CurrentBalance, data_dpt_cdp_02_DepositAccount_CurrentBalance)
        data_dpt_cdp_01_DepositAccount_DepositAmount = data_dpt_cdp_01_DepositAccount['DepositAmount'][0]
        data_dpt_cdp_02_DepositAccount_DepositAmount = data_dpt_cdp_02_DepositAccount['DepositAmount'][0]
        AU.equals_decimal('DepositAmount', amount_deposit, data_dpt_cdp_01_DepositAccount_DepositAmount, data_dpt_cdp_02_DepositAccount_DepositAmount)

        # database - verify value insert - o9deposit - DepositHistory
        sql_query_DepositHistory = f"SELECT * FROM [o9deposit].[dbo].[DepositHistory] WHERE AccountNumber='{account_number}'"
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[DepositHistory]', 4, len(RU.query_db(sql_query_DepositHistory)))
        # verify data in row of transaction
        sql_query_DepositHistory = f"SELECT * FROM [o9deposit].[dbo].[DepositHistory] WHERE AccountNumber='{account_number}' AND RefId='{value_data_ref_id}'"
        data_DepositHistory = RU.query_db(sql_query_DepositHistory)
        AU.assert_not_empty('Id', data_DepositHistory['Id'][0])
        AU.assert_not_null('Id', data_DepositHistory['Id'][0])
        AU.assert_equals('AccountNumber', account_number, data_DepositHistory['AccountNumber'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_DepositHistory['ValueDate'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_DepositHistory['RefId'][0])
        AU.assert_not_empty('TransactionDate', data_DepositHistory['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_DepositHistory['TransactionDate'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_DepositHistory['TransactionCode'][0])
        AU.assert_equals('Amount', amount_deposit, data_DepositHistory['Amount'][0])
        AU.assert_equals('Dorc', 'C', data_DepositHistory['Dorc'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_DepositHistory['Description'][0])
        AU.assert_equals('UsrCode', user_service['username'], data_DepositHistory['UsrCode'][0])
        AU.assert_equals('Oder', 1, data_DepositHistory['Oder'][0])
        AU.assert_equals('DepositHistoryStatus', 'N', data_DepositHistory['DepositHistoryStatus'][0])
        AU.assert_equals('Stcode', 'CDP', data_DepositHistory['Stcode'][0])
        AU.assert_equals('Usrid', 0, data_DepositHistory['Usrid'][0])
        AU.assert_not_empty('CreatedOnUtc', data_DepositHistory['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_DepositHistory['CreatedOnUtc'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_DepositHistory['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_DepositHistory['UpdatedOnUtc'][0])
        AU.assert_equals('ChannelId', 'C', data_DepositHistory['ChannelId'][0])

        # database - verify value insert - o9deposit - DepositStatement
        sql_query_DepositStatement = f"SELECT * FROM [o9deposit].[dbo].[DepositStatement] WHERE AccountNumber='{account_number}'"
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[DepositStatement]', 2, len(RU.query_db(sql_query_DepositStatement)))
        # verify data in row of transaction
        sql_query_DepositStatement = f"SELECT * FROM [o9deposit].[dbo].[DepositStatement] WHERE AccountNumber='{account_number}' AND TransactionNumber='{value_data_transaction_number}'"
        data_DepositStatement = RU.query_db(sql_query_DepositStatement)
        AU.assert_not_empty('Id', data_DepositStatement['Id'][0])
        AU.assert_not_null('Id', data_DepositStatement['Id'][0])
        AU.assert_equals('AccountNumber', account_number, data_DepositStatement['AccountNumber'][0])
        AU.assert_not_empty('StatementDate', data_DepositStatement['StatementDate'][0])
        AU.assert_not_null('StatementDate', data_DepositStatement['StatementDate'][0])
        AU.assert_equals('ReferenceId', value_data_ref_id, data_DepositStatement['ReferenceId'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_DepositStatement['ValueDate'][0])
        AU.assert_equals('Amount', amount_deposit, data_DepositStatement['Amount'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_DepositStatement['CurrencyCode'][0])
        AU.assert_equals('ConvertAmount', 0, data_DepositStatement['ConvertAmount'][0])
        AU.assert_equals('StatementCode', 'DEP', data_DepositStatement['StatementCode'][0])
        AU.assert_equals('StatementStatus', 'N', data_DepositStatement['StatementStatus'][0])
        AU.assert_equals('RefNumber', '0', data_DepositStatement['RefNumber'][0])
        AU.assert_equals('TransCode', 'DPT_CREDIT_BALANCE', data_DepositStatement['TransCode'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_DepositStatement['Description'][0])
        AU.assert_not_empty('CreatedOnUtc', data_DepositStatement['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_DepositStatement['CreatedOnUtc'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_DepositStatement['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_DepositStatement['UpdatedOnUtc'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_DepositStatement['TransactionNumber'][0])

        # database - verify value insert - o9deposit - DepositAccountTrans
        sql_query_DepositAccountTrans = f"SELECT * FROM [o9deposit].[dbo].[DepositAccountTrans] WHERE DepositAccount='{account_number}'"
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[DepositAccountTrans]', 2, len(RU.query_db(sql_query_DepositAccountTrans)))
        # verify data in row of transaction
        sql_query_DepositAccountTrans = f"SELECT * FROM [o9deposit].[dbo].[DepositAccountTrans] WHERE DepositAccount='{account_number}' AND TransactionNumber='{value_data_transaction_number}'"
        data_DepositAccountTrans = RU.query_db(sql_query_DepositAccountTrans)
        AU.assert_not_empty('Id', data_DepositAccountTrans['Id'][0])
        AU.assert_not_null('Id', data_DepositAccountTrans['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_DepositAccountTrans['TransactionNumber'][0])
        AU.assert_equals('DepositAccount', account_number, data_DepositAccountTrans['DepositAccount'][0])
        AU.assert_equals('TransCode', 'DPT_CREDIT_BALANCE', data_DepositAccountTrans['TransCode'][0])
        AU.assert_equals('TransactionStatus', 'N', data_DepositAccountTrans['TransactionStatus'][0])
        AU.assert_equals('Amount', amount_deposit, data_DepositAccountTrans['Amount'][0])
        AU.assert_equals('GLPopulated', True, data_DepositAccountTrans['GLPopulated'][0])
        AU.assert_empty('CrossBranchCode', data_DepositAccountTrans['CrossBranchCode'][0])
        AU.assert_empty('CrossCurrencyCode', data_DepositAccountTrans['CrossCurrencyCode'][0])
        AU.assert_null('DebitSysAccountName', data_DepositAccountTrans['DebitSysAccountName'][0])
        AU.assert_null('CreditSysAccountName', data_DepositAccountTrans['CreditSysAccountName'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_DepositAccountTrans['BaseCurrencyAmount'][0])
        AU.assert_equals('TransId', value_TransId, data_DepositAccountTrans['TransId'][0])
        AU.assert_equals('GLGroup', value_AccountingGroup, data_DepositAccountTrans['GLGroup'][0])

        # database - verify value insert - o9deposit - GLEntries
        sql_query_GLEntries = f"SELECT * FROM [o9deposit].[dbo].[GLEntries] WHERE GLAccount='{gl_account_deposit}' AND TransactionNumber='{value_data_transaction_number}'"
        data_GLEntries = RU.query_db(sql_query_GLEntries)
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[GLEntries]', 1, len(data_GLEntries))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_GLEntries['Id'][0])
        AU.assert_not_null('Id', data_GLEntries['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_GLEntries['TransactionNumber'][0])
        AU.assert_equals('TransTableName', 'DepositAccountTrans', data_GLEntries['TransTableName'][0])
        AU.assert_equals('TransId', value_TransId, data_GLEntries['TransId'][0])
        AU.assert_equals('SysAccountName', 'DEPOSIT', data_GLEntries['SysAccountName'][0])
        AU.assert_equals('GLAccount', gl_account_deposit, data_GLEntries['GLAccount'][0])
        AU.assert_equals('DorC', 'C', data_GLEntries['DorC'][0])
        AU.assert_equals('TransactionStatus', 'N', data_GLEntries['TransactionStatus'][0])
        AU.assert_equals('Amount', amount_deposit, data_GLEntries['Amount'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_GLEntries['BranchCode'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_GLEntries['CurrencyCode'][0])
        AU.assert_empty('CrossBranchCode', data_GLEntries['CrossBranchCode'][0])
        AU.assert_empty('CrossCurrencyCode', data_GLEntries['CrossCurrencyCode'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_GLEntries['BaseCurrencyAmount'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_GLEntries['ValueDate'][0])
        AU.assert_equals('Posted', 1, data_GLEntries['Posted'][0])
        AU.assert_equals('AccountingGroup', value_AccountingGroup, data_GLEntries['AccountingGroup'][0])

        # database - verify value insert - o9deposit - Transaction
        sql_query_Transaction = f"SELECT * FROM [o9deposit].[dbo].[Transaction] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_Transaction = RU.query_db(sql_query_Transaction)
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[Transaction]', 1, len(data_Transaction))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_Transaction['Id'][0])
        AU.assert_not_null('Id', data_Transaction['Id'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_Transaction['TransactionCode'][0])
        AU.assert_equals('SubCode', 'DPT_CDP', data_Transaction['SubCode'][0])
        AU.assert_not_empty('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_Transaction['ValueDate'][0])
        AU.assert_not_empty('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_not_null('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_equals('ReferenceId', value_data_reference_id, data_Transaction['ReferenceId'][0])
        AU.assert_empty('ReferenceCode', data_Transaction['ReferenceCode'][0])
        AU.assert_empty('BusinessCode', data_Transaction['BusinessCode'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_Transaction['TransactionNumber'][0])
        AU.assert_null('TransId', data_Transaction['TransId'][0])
        AU.assert_equals('ChannelId', 'C', data_Transaction['ChannelId'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_Transaction['RefId'][0])
        AU.assert_equals('Status', 'C', data_Transaction['Status'][0])
        AU.assert_equals('IsReverse', False, data_Transaction['IsReverse'][0])
        AU.assert_equals('Amount1', 0, data_Transaction['Amount1'][0])
        AU.assert_not_empty('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_null('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_equals('RequestBody', '{}', data_Transaction['RequestBody'][0])
        AU.assert_not_empty('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_null('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_equals('ResponseBody', '{}', data_Transaction['ResponseBody'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_Transaction['Description'][0])
        AU.assert_not_empty('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_null('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_equals('StartTime', 0, data_Transaction['StartTime'][0])
        AU.assert_not_empty('Duration', data_Transaction['Duration'][0])
        AU.assert_not_null('Duration', data_Transaction['Duration'][0])
        AU.assert_not_equals('Duration', 0, data_Transaction['Duration'][0])
        AU.assert_equals('UserCode', user_service['username'], data_Transaction['UserCode'][0])
        AU.assert_equals('UserName', user_service['fullname'], data_Transaction['UserName'][0])
        AU.assert_equals('LoginName', user_service['username'], data_Transaction['LoginName'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_Transaction['BranchCode'][0])

        # database - verify value insert - o9deposit - TransactionDetails
        sql_query_TransactionDetails = f"SELECT * FROM [o9deposit].[dbo].[TransactionDetails] WHERE RefId='{value_data_ref_id}' ORDER BY Id"
        data_TransactionDetails = RU.query_db(sql_query_TransactionDetails)
        # verify total row
        AU.assert_equals('Total row in table [o9deposit].[dbo].[TransactionDetails]', 9, len(data_TransactionDetails))
        # # verify data in row of transaction

        # database - verify value insert or update - o9cash - CashList
        if len(data_dpt_cdp_01_CashList) == 0: # insert
            data_CashList = RU.query_db(sql_query_CashList)
            # verify total row
            AU.assert_equals('Total row in table [o9cash].[dbo].[CashList]', 1, len(data_CashList))
            # verify data in row of transaction
            AU.assert_not_empty('Id', data_CashList['Id'][0])
            AU.assert_not_null('Id', data_CashList['Id'][0])
            AU.assert_equals('CashierCode', user_service['username'], data_CashList['CashierCode'][0])
            AU.assert_equals('CurrencyCode', currency_deposit, data_CashList['CurrencyCode'][0])
            AU.assert_equals('CurrentBalance', amount_deposit, data_CashList['CurrentBalance'][0])
            AU.assert_not_empty('CreatedOnUtc', data_CashList['CreatedOnUtc'][0])
            AU.assert_not_null('CreatedOnUtc', data_CashList['CreatedOnUtc'][0])
            AU.assert_not_empty('UpdatedOnUtc', data_CashList['UpdatedOnUtc'][0])
            AU.assert_not_null('UpdatedOnUtc', data_CashList['UpdatedOnUtc'][0])
        else: # update
            # verify columns update
            data_dpt_cdp_02_CashList = RU.query_db(sql_query_CashList)
            diff_columns_CashList = AU.db_compare_results('[o9cash].[dbo].[CashList]', data_dpt_cdp_01_CashList, data_dpt_cdp_02_CashList)
            AU.db_compare_columns(expected_col['CashList'], diff_columns_CashList)
            # verify value update
            data_dpt_cdp_01_CashList_CurrentBalance = data_dpt_cdp_01_CashList['CurrentBalance'][0]
            data_dpt_cdp_02_CashList_CurrentBalance = data_dpt_cdp_02_CashList['CurrentBalance'][0]
            AU.equals_decimal('CurrentBalance', amount_deposit, data_dpt_cdp_01_CashList_CurrentBalance, data_dpt_cdp_02_CashList_CurrentBalance)

        # database - verify value insert or update - o9cash - CashStatement
        if len(data_dpt_cdp_01_CashStatement) == 0: # insert
            data_CashStatement = RU.query_db(sql_query_CashStatement)
            # verify total row
            AU.assert_equals('Total row in table [o9cash].[dbo].[CashStatement]', 1, len(data_CashStatement))
            # verify data in row of transaction
            AU.assert_not_empty('Id', data_CashStatement['Id'][0])
            AU.assert_not_null('Id', data_CashStatement['Id'][0])
            AU.assert_equals('CashierCode', user_service['username'], data_CashStatement['CashierCode'][0])
            AU.assert_equals('CurrencyCode', currency_deposit, data_CashStatement['CurrencyCode'][0])
            AU.assert_equals('CashAmount', amount_deposit, data_CashStatement['CashAmount'][0])
            AU.assert_equals('CashType', 'D', data_CashStatement['CashType'][0])
            AU.assert_not_empty('CreatedOnUtc', data_CashStatement['CreatedOnUtc'][0])
            AU.assert_not_null('CreatedOnUtc', data_CashStatement['CreatedOnUtc'][0])
            AU.assert_not_empty('UpdatedOnUtc', data_CashStatement['UpdatedOnUtc'][0])
            AU.assert_not_null('UpdatedOnUtc', data_CashStatement['UpdatedOnUtc'][0])
            AU.assert_not_empty('StatementDate', data_CashStatement['StatementDate'][0])
            AU.assert_not_null('StatementDate', data_CashStatement['StatementDate'][0])
            AU.assert_equals('ValueDate', user_service['working_date_db'], data_CashStatement['ValueDate'][0])
        else: # update
            # verify columns update
            data_dpt_cdp_02_CashStatement = RU.query_db(sql_query_CashStatement)
            diff_columns_CashStatement = AU.db_compare_results('[o9cash].[dbo].[CashStatement]', data_dpt_cdp_01_CashStatement, data_dpt_cdp_02_CashStatement)
            AU.db_compare_columns(expected_col['CashStatement'], diff_columns_CashStatement)
            # verify value update
            data_dpt_cdp_01_CashStatement_CashAmount = data_dpt_cdp_01_CashStatement['CashAmount'][0]
            data_dpt_cdp_02_CashStatement_CashAmount = data_dpt_cdp_02_CashStatement['CashAmount'][0]
            AU.equals_decimal('CashAmount', amount_deposit, data_dpt_cdp_01_CashStatement_CashAmount, data_dpt_cdp_02_CashStatement_CashAmount)

        # database - verify value insert - o9cash - CashTransaction
        sql_query_CashTransaction = f"SELECT * FROM [o9cash].[dbo].[CashTransaction] WHERE CashierCode='{user_service['username']}' AND CurrencyCode='{currency_deposit}' AND TransactionNumber='{value_data_transaction_number}'"
        data_CashTransaction = RU.query_db(sql_query_CashTransaction)
        # verify total row
        AU.assert_equals('Total row in table [o9cash].[dbo].[CashTransaction]', 1, len(data_CashTransaction))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_CashTransaction['Id'][0])
        AU.assert_not_null('Id', data_CashTransaction['Id'][0])
        AU.assert_equals('CashierCode', user_service['username'], data_CashTransaction['CashierCode'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_CashTransaction['CurrencyCode'][0])
        AU.assert_equals('Amount', amount_deposit, data_CashTransaction['Amount'][0])
        AU.assert_equals('TransCode', 'CSH_DEBIT_BALANCE', data_CashTransaction['TransCode'][0])
        AU.assert_not_empty('TransId', data_CashTransaction['TransId'][0])
        AU.assert_not_null('TransId', data_CashTransaction['TransId'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_CashTransaction['TransactionNumber'][0])
        AU.assert_equals('GLPopulated', True, data_CashTransaction['GLPopulated'][0])
        AU.assert_equals('TransactionStatus', 'N', data_CashTransaction['TransactionStatus'][0])
        AU.assert_not_empty('CreatedOnUtc', data_CashTransaction['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_CashTransaction['CreatedOnUtc'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_CashTransaction['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_CashTransaction['UpdatedOnUtc'][0])
        AU.assert_empty('CrossBranchCode', data_CashTransaction['CrossBranchCode'][0])
        AU.assert_empty('CrossCurrencyCode', data_CashTransaction['CrossCurrencyCode'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_CashTransaction['BaseCurrencyAmount'][0])
        AU.assert_equals('GLGroup', 1, data_CashTransaction['GLGroup'][0])

        # database - verify value insert - o9cash - GLEntries
        sql_query_GLEntries = f"SELECT * FROM [o9cash].[dbo].[GLEntries] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_GLEntries = RU.query_db(sql_query_GLEntries)
        # verify total row
        AU.assert_equals('Total row in table [o9cash].[dbo].[GLEntries]', 1, len(data_GLEntries))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_GLEntries['Id'][0])
        AU.assert_not_null('Id', data_GLEntries['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_GLEntries['TransactionNumber'][0])
        AU.assert_equals('TransTableName', 'CashList', data_GLEntries['TransTableName'][0])
        AU.assert_equals('TransId', data_CashTransaction['TransId'][0], data_GLEntries['TransId'][0])
        AU.assert_equals('SysAccountName', 'CASH', data_GLEntries['SysAccountName'][0])
        AU.assert_equals('GLAccount', gl_account_cash, data_GLEntries['GLAccount'][0])
        AU.assert_equals('DorC', 'D', data_GLEntries['DorC'][0])
        AU.assert_equals('TransactionStatus', 'N', data_GLEntries['TransactionStatus'][0])
        AU.assert_equals('Amount', amount_deposit, data_GLEntries['Amount'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_GLEntries['BranchCode'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_GLEntries['CurrencyCode'][0])
        AU.assert_empty('CrossBranchCode', data_GLEntries['CrossBranchCode'][0])
        AU.assert_empty('CrossCurrencyCode', data_GLEntries['CrossCurrencyCode'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_GLEntries['BaseCurrencyAmount'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_GLEntries['ValueDate'][0])
        AU.assert_equals('Posted', True, data_GLEntries['Posted'][0])
        AU.assert_equals('AccountingGroup', 1, data_GLEntries['AccountingGroup'][0])

        # database - verify value insert - o9cash - Transaction
        sql_query_Transaction = f"SELECT * FROM [o9cash].[dbo].[Transaction] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_Transaction = RU.query_db(sql_query_Transaction)
        # verify total row
        AU.assert_equals('Total row in table [o9cash].[dbo].[Transaction]', 1, len(data_Transaction))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_Transaction['Id'][0])
        AU.assert_not_null('Id', data_Transaction['Id'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_Transaction['TransactionCode'][0])
        AU.assert_equals('SubCode', 'CSH_UPDATE_CASH', data_Transaction['SubCode'][0])
        AU.assert_not_empty('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_Transaction['ValueDate'][0])
        AU.assert_equals('ServiceSysDate', data_Transaction['TransactionDate'][0], data_Transaction['ServiceSysDate'][0])
        AU.assert_equals('ReferenceId', value_data_reference_id, data_Transaction['ReferenceId'][0])
        AU.assert_empty('ReferenceCode', data_Transaction['ReferenceCode'][0])
        AU.assert_empty('BusinessCode', data_Transaction['BusinessCode'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_Transaction['TransactionNumber'][0])
        AU.assert_null('TransId', data_Transaction['TransId'][0])
        AU.assert_equals('ChannelId', 'C', data_Transaction['ChannelId'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_Transaction['RefId'][0])
        AU.assert_equals('UserCode', user_service['username'], data_Transaction['UserCode'][0])
        AU.assert_equals('LoginName', user_service['username'], data_Transaction['LoginName'][0])
        AU.assert_equals('UserName', user_service['fullname'], data_Transaction['UserName'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_Transaction['BranchCode'][0])
        AU.assert_equals('Status', 'C', data_Transaction['Status'][0])
        AU.assert_equals('IsReverse', False, data_Transaction['IsReverse'][0])
        AU.assert_equals('Amount1', 0, data_Transaction['Amount1'][0])
        AU.assert_not_empty('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_null('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_equals('RequestBody', '{}', data_Transaction['RequestBody'][0])
        AU.assert_not_empty('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_null('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_equals('ResponseBody', '{}', data_Transaction['ResponseBody'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_Transaction['Description'][0])
        AU.assert_not_empty('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_null('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_equals('StartTime', 0, data_Transaction['StartTime'][0])
        AU.assert_not_empty('Duration', data_Transaction['Duration'][0])
        AU.assert_not_null('Duration', data_Transaction['Duration'][0])
        AU.assert_not_equals('Duration', 0, data_Transaction['Duration'][0])

        # database - verify value insert - o9cash - TransactionDetails
        sql_query_TransactionDetails = f"SELECT * FROM [o9cash].[dbo].[TransactionDetails] WHERE RefId='{value_data_ref_id}' ORDER BY Id"
        data_TransactionDetails = RU.query_db(sql_query_TransactionDetails)
        # verify total row
        AU.assert_equals('Total row in table [o9cash].[dbo].[TransactionDetails]', 2, len(data_TransactionDetails))
        # verify data in row 1 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][0])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][0])
        AU.assert_equals('Entity', 'CashList', data_TransactionDetails['Entity'][0])
        AU.assert_equals('FieldName', 'CurrentBalance', data_TransactionDetails['FieldName'][0])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][0])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][0])
        AU.assert_equals('EntityId', data_dpt_cdp_02_CashList['Id'][0], data_TransactionDetails['EntityId'][0])
        # AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][0])
        # AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][0])
        AU.assert_empty('Description', data_TransactionDetails['Description'][0])
        # verify data in row 2 of transaction
        AU.assert_not_empty('Id', data_TransactionDetails['Id'][1])
        AU.assert_not_null('Id', data_TransactionDetails['Id'][1])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionDetails['RefId'][1])
        AU.assert_equals('Entity', 'CashStatement', data_TransactionDetails['Entity'][1])
        AU.assert_equals('FieldName', 'CashAmount', data_TransactionDetails['FieldName'][1])
        AU.assert_equals('Status', 'N', data_TransactionDetails['Status'][1])
        AU.assert_equals('UpdateType', 'C', data_TransactionDetails['UpdateType'][1])
        AU.assert_equals('EntityId', data_dpt_cdp_02_CashStatement['Id'][0], data_TransactionDetails['EntityId'][1])
        # AU.assert_equals('OldValue', '0.000', data_TransactionDetails['OldValue'][1])
        # AU.assert_equals('NewValue', '10000000.450', data_TransactionDetails['NewValue'][1])
        AU.assert_empty('Description', data_TransactionDetails['Description'][1])

        # database - verify columns update - o9accounting - AccountBalance
        data_dpt_cdp_02_AccountBalance_DEPOSIT = RU.query_db(sql_query_AccountBalance_DEPOSIT)
        diff_columns_AccountBalance_DEPOSIT = AU.db_compare_results('[o9accounting].[dbo].[AccountBalance]: DEPOSIT', data_dpt_cdp_01_AccountBalance_DEPOSIT, data_dpt_cdp_02_AccountBalance_DEPOSIT)
        data_dpt_cdp_02_AccountBalance_CASH = RU.query_db(sql_query_AccountBalance_CASH)
        diff_columns_AccountBalance_CASH = AU.db_compare_results('[o9accounting].[dbo].[AccountBalance]: CASH', data_dpt_cdp_01_AccountBalance_CASH, data_dpt_cdp_02_AccountBalance_CASH)
        AU.db_compare_columns(expected_col['AccountBalance_credit'], diff_columns_AccountBalance_DEPOSIT)
        AU.db_compare_columns(expected_col['AccountBalance_debit'], diff_columns_AccountBalance_CASH)
        # database - verify value update - o9accounting - AccountBalance
        data_dpt_cdp_01_AccountBalance_DEPOSIT = data_dpt_cdp_01_AccountBalance_DEPOSIT['Balance'][0]
        data_dpt_cdp_02_AccountBalance_DEPOSIT = data_dpt_cdp_02_AccountBalance_DEPOSIT['Balance'][0]
        AU.equals_decimal('Balance', amount_deposit, data_dpt_cdp_01_AccountBalance_DEPOSIT, data_dpt_cdp_02_AccountBalance_DEPOSIT)
        data_dpt_cdp_01_AccountBalance_CASH = data_dpt_cdp_01_AccountBalance_CASH['Balance'][0]
        data_dpt_cdp_02_AccountBalance_CASH = data_dpt_cdp_02_AccountBalance_CASH['Balance'][0]
        AU.equals_decimal('Balance', amount_deposit, -data_dpt_cdp_01_AccountBalance_CASH, -data_dpt_cdp_02_AccountBalance_CASH)

        # database - verify value insert - o9accounting - GLEntries - DEPOSIT
        sql_query_GLEntries = f"SELECT * FROM [o9accounting].[dbo].[GLEntries] WHERE GLAccount='{gl_account_deposit}' AND TransactionNumber='{value_data_transaction_number}'"
        data_GLEntries = RU.query_db(sql_query_GLEntries)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[GLEntries]', 1, len(data_GLEntries))
        # verify data in row of transaction - DEPOSIT
        AU.assert_not_empty('Id', data_GLEntries['Id'][0])
        AU.assert_not_null('Id', data_GLEntries['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_GLEntries['TransactionNumber'][0])
        AU.assert_equals('TransTableName', 'DepositAccountTrans', data_GLEntries['TransTableName'][0])
        AU.assert_equals('TransId', data_DepositAccountTrans['TransId'][0], data_GLEntries['TransId'][0])
        AU.assert_equals('SysAccountName', 'DEPOSIT', data_GLEntries['SysAccountName'][0])
        AU.assert_equals('GLAccount', gl_account_deposit, data_GLEntries['GLAccount'][0])
        AU.assert_equals('DorC', 'C', data_GLEntries['DorC'][0])
        AU.assert_equals('TransactionStatus', 'N', data_GLEntries['TransactionStatus'][0])
        AU.assert_equals('Amount', amount_deposit, data_GLEntries['Amount'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_GLEntries['BranchCode'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_GLEntries['CurrencyCode'][0])
        AU.assert_null('CrossBranchCode', data_GLEntries['CrossBranchCode'][0])
        AU.assert_null('CrossCurrencyCode', data_GLEntries['CrossCurrencyCode'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_GLEntries['BaseCurrencyAmount'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_GLEntries['ValueDate'][0])
        AU.assert_equals('Posted', True, data_GLEntries['Posted'][0])
        AU.assert_equals('AccountingGroup', 1, data_GLEntries['AccountingGroup'][0])

        # database - verify value insert - o9accounting - GLEntries - CASH
        sql_query_GLEntries = f"SELECT * FROM [o9accounting].[dbo].[GLEntries] WHERE GLAccount='{gl_account_cash}' AND TransactionNumber='{value_data_transaction_number}'"
        data_GLEntries = RU.query_db(sql_query_GLEntries)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[GLEntries]', 1, len(data_GLEntries))
        # verify data in row of transaction - CASH
        AU.assert_not_empty('Id', data_GLEntries['Id'][0])
        AU.assert_not_null('Id', data_GLEntries['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_GLEntries['TransactionNumber'][0])
        AU.assert_equals('TransTableName', 'CashList', data_GLEntries['TransTableName'][0])
        AU.assert_equals('TransId', data_CashTransaction['TransId'][0], data_GLEntries['TransId'][0])
        AU.assert_equals('SysAccountName', 'CASH', data_GLEntries['SysAccountName'][0])
        AU.assert_equals('GLAccount', gl_account_cash, data_GLEntries['GLAccount'][0])
        AU.assert_equals('DorC', 'D', data_GLEntries['DorC'][0])
        AU.assert_equals('TransactionStatus', 'N', data_GLEntries['TransactionStatus'][0])
        AU.assert_equals('Amount', amount_deposit, data_GLEntries['Amount'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_GLEntries['BranchCode'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_GLEntries['CurrencyCode'][0])
        AU.assert_null('CrossBranchCode', data_GLEntries['CrossBranchCode'][0])
        AU.assert_null('CrossCurrencyCode', data_GLEntries['CrossCurrencyCode'][0])
        AU.assert_equals('BaseCurrencyAmount', 0, data_GLEntries['BaseCurrencyAmount'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_GLEntries['ValueDate'][0])
        AU.assert_equals('Posted', True, data_GLEntries['Posted'][0])
        AU.assert_equals('AccountingGroup', 1, data_GLEntries['AccountingGroup'][0])

        # database - verify value insert - o9accounting - AccountStatement - DEPOSIT
        sql_query_AccountStatement = f"SELECT * FROM [o9accounting].[dbo].[AccountStatement] WHERE AccountNumber='{gl_account_deposit}' AND TransactionNumber='{value_data_transaction_number}'"
        data_AccountStatement = RU.query_db(sql_query_AccountStatement)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[AccountStatement]', 1, len(data_AccountStatement))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_AccountStatement['Id'][0])
        AU.assert_not_null('Id', data_AccountStatement['Id'][0])
        AU.assert_equals('AccountNumber', gl_account_deposit, data_AccountStatement['AccountNumber'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_AccountStatement['CurrencyCode'][0])
        AU.assert_equals('ConvertAmount', 0, data_AccountStatement['ConvertAmount'][0])
        AU.assert_equals('Amount', amount_deposit, data_AccountStatement['Amount'][0])
        AU.assert_equals('ReferenceId', value_data_ref_id, data_AccountStatement['ReferenceId'][0])
        AU.assert_equals('StatementStatus', 'N', data_AccountStatement['StatementStatus'][0])
        AU.assert_not_empty('StatementDate', data_AccountStatement['StatementDate'][0])
        AU.assert_not_null('StatementDate', data_AccountStatement['StatementDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_AccountStatement['ValueDate'][0])
        AU.assert_equals('StatementCode', 'DEP', data_AccountStatement['StatementCode'][0])
        AU.assert_empty('RefNumber', data_AccountStatement['RefNumber'][0])
        AU.assert_equals('TransCode', 'C', data_AccountStatement['TransCode'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_AccountStatement['Description'][0])
        AU.assert_not_empty('CreatedOnUtc', data_AccountStatement['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_AccountStatement['CreatedOnUtc'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_AccountStatement['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_AccountStatement['UpdatedOnUtc'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_AccountStatement['TransactionNumber'][0])

        # database - verify value insert - o9accounting - AccountStatement - CASH
        sql_query_AccountStatement = f"SELECT * FROM [o9accounting].[dbo].[AccountStatement] WHERE AccountNumber='{gl_account_cash}' AND TransactionNumber='{value_data_transaction_number}'"
        data_AccountStatement = RU.query_db(sql_query_AccountStatement)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[AccountStatement]', 1, len(data_AccountStatement))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_AccountStatement['Id'][0])
        AU.assert_not_null('Id', data_AccountStatement['Id'][0])
        AU.assert_equals('AccountNumber', gl_account_cash, data_AccountStatement['AccountNumber'][0])
        AU.assert_equals('CurrencyCode', currency_deposit, data_AccountStatement['CurrencyCode'][0])
        AU.assert_equals('ConvertAmount', 0, data_AccountStatement['ConvertAmount'][0])
        AU.assert_equals('Amount', amount_deposit, data_AccountStatement['Amount'][0])
        AU.assert_equals('ReferenceId', value_data_ref_id, data_AccountStatement['ReferenceId'][0])
        AU.assert_equals('StatementStatus', 'N', data_AccountStatement['StatementStatus'][0])
        AU.assert_not_empty('StatementDate', data_AccountStatement['StatementDate'][0])
        AU.assert_not_null('StatementDate', data_AccountStatement['StatementDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_AccountStatement['ValueDate'][0])
        AU.assert_equals('StatementCode', 'WDR', data_AccountStatement['StatementCode'][0])
        AU.assert_empty('RefNumber', data_AccountStatement['RefNumber'][0])
        AU.assert_equals('TransCode', 'D', data_AccountStatement['TransCode'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_AccountStatement['Description'][0])
        AU.assert_not_empty('CreatedOnUtc', data_AccountStatement['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_AccountStatement['CreatedOnUtc'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_AccountStatement['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_AccountStatement['UpdatedOnUtc'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_AccountStatement['TransactionNumber'][0])

        # database - verify value insert - o9accounting - Transaction
        sql_query_Transaction = f"SELECT * FROM [o9accounting].[dbo].[Transaction] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_Transaction = RU.query_db(sql_query_Transaction)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[Transaction]', 1, len(data_Transaction))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_Transaction['Id'][0])
        AU.assert_not_null('Id', data_Transaction['Id'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_Transaction['TransactionCode'][0])
        AU.assert_equals('SubCode', 'ACT_EXECUTE_POSTING', data_Transaction['SubCode'][0])
        AU.assert_not_empty('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_Transaction['ValueDate'][0])
        AU.assert_equals('ServiceSysDate', data_Transaction['TransactionDate'][0], data_Transaction['ServiceSysDate'][0])
        AU.assert_equals('ReferenceId', value_data_reference_id, data_Transaction['ReferenceId'][0])
        AU.assert_empty('ReferenceCode', data_Transaction['ReferenceCode'][0])
        AU.assert_empty('BusinessCode', data_Transaction['BusinessCode'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_Transaction['TransactionNumber'][0])
        AU.assert_null('TransId', data_Transaction['TransId'][0])
        AU.assert_equals('ChannelId', 'C', data_Transaction['ChannelId'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_Transaction['RefId'][0])
        AU.assert_equals('UserCode', user_service['username'], data_Transaction['UserCode'][0])
        AU.assert_equals('LoginName', user_service['username'], data_Transaction['LoginName'][0])
        AU.assert_equals('UserName', user_service['fullname'], data_Transaction['UserName'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_Transaction['BranchCode'][0])
        AU.assert_equals('Status', 'C', data_Transaction['Status'][0])
        AU.assert_equals('IsReverse', False, data_Transaction['IsReverse'][0])
        AU.assert_equals('Amount1', 0, data_Transaction['Amount1'][0])
        AU.assert_not_empty('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_null('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_equals('RequestBody', '{}', data_Transaction['RequestBody'][0])
        AU.assert_not_empty('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_null('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_equals('ResponseBody', '{}', data_Transaction['ResponseBody'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_Transaction['Description'][0])
        AU.assert_not_empty('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_null('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_equals('StartTime', 0, data_Transaction['StartTime'][0])
        AU.assert_not_empty('Duration', data_Transaction['Duration'][0])
        AU.assert_not_null('Duration', data_Transaction['Duration'][0])
        AU.assert_not_equals('Duration', 0, data_Transaction['Duration'][0])

        # database - verify value NOT insert - o9accounting - TransactionDetails
        sql_query_TransactionDetails = f"SELECT * FROM [o9accounting].[dbo].[TransactionDetails] WHERE RefId='{value_data_ref_id}' ORDER BY Id"
        data_TransactionDetails = RU.query_db(sql_query_TransactionDetails)
        # verify total row
        AU.assert_equals('Total row in table [o9accounting].[dbo].[TransactionDetails]', 0, len(data_TransactionDetails))

        # database - verify value insert - o9admin - TransactionJournalDone
        sql_query_TransactionJournalDone = f"SELECT * FROM [o9admin].[dbo].[TransactionJournalDone] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_TransactionJournalDone = RU.query_db(sql_query_TransactionJournalDone)
        # verify total row
        AU.assert_equals('Total row in table [o9admin].[dbo].[TransactionJournalDone]', 1, len(data_TransactionJournalDone))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_TransactionJournalDone['Id'][0])
        AU.assert_not_null('Id', data_TransactionJournalDone['Id'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_TransactionJournalDone['TransactionNumber'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_TransactionJournalDone['TransactionCode'][0])
        AU.assert_not_empty('TransactionDate', data_TransactionJournalDone['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_TransactionJournalDone['TransactionDate'][0])
        AU.assert_equals('ReferenceId', value_data_reference_id, data_TransactionJournalDone['ReferenceId'][0])
        AU.assert_equals('UserCreated', user_service['username'], data_TransactionJournalDone['UserCreated'][0])
        AU.assert_equals('Status', 'C', data_TransactionJournalDone['Status'][0])
        AU.assert_equals('IsReverse', False, data_TransactionJournalDone['IsReverse'][0])
        AU.assert_equals('HasPosting', True, data_TransactionJournalDone['HasPosting'][0])
        AU.assert_equals('Amount1', amount_deposit, data_TransactionJournalDone['Amount1'][0])
        AU.assert_equals('Channel', 'C', data_TransactionJournalDone['Channel'][0])
        AU.assert_null('UserApprove', data_TransactionJournalDone['UserApprove'][0])
        AU.assert_null('UserReject', data_TransactionJournalDone['UserReject'][0])
        AU.assert_equals('String1', account_number, data_TransactionJournalDone['String1'][0])
        AU.assert_not_empty('TransactionBody', data_TransactionJournalDone['TransactionBody'][0])
        AU.assert_not_null('TransactionBody', data_TransactionJournalDone['TransactionBody'][0])
        AU.assert_not_equals('TransactionBody', '{}', data_TransactionJournalDone['TransactionBody'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_TransactionJournalDone['Description'][0])
        AU.assert_equals('CashAmount', amount_deposit, data_TransactionJournalDone['CashAmount'][0])
        AU.assert_not_empty('UpdatedOnUtc', data_TransactionJournalDone['UpdatedOnUtc'][0])
        AU.assert_not_null('UpdatedOnUtc', data_TransactionJournalDone['UpdatedOnUtc'][0])
        AU.assert_not_empty('CreatedOnUtc', data_TransactionJournalDone['CreatedOnUtc'][0])
        AU.assert_not_null('CreatedOnUtc', data_TransactionJournalDone['CreatedOnUtc'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_TransactionJournalDone['RefId'][0])
        AU.assert_null('ApproveStatus', data_TransactionJournalDone['ApproveStatus'][0])
        AU.assert_null('ApproveReason', data_TransactionJournalDone['ApproveReason'][0])
        AU.assert_null('ApproveDate', data_TransactionJournalDone['ApproveDate'][0])
        AU.assert_null('RejectReason', data_TransactionJournalDone['RejectReason'][0])
        AU.assert_null('RejectDate', data_TransactionJournalDone['RejectDate'][0])
        AU.assert_null('ReverseReason', data_TransactionJournalDone['ReverseReason'][0])
        AU.assert_null('ReverseDate', data_TransactionJournalDone['ReverseDate'][0])
        AU.assert_null('UserReverse', data_TransactionJournalDone['UserReverse'][0])
        AU.assert_equals('ApproveLimit', 0, data_TransactionJournalDone['ApproveLimit'][0])

        # database - verify value insert - o9admin - Transaction
        sql_query_Transaction = f"SELECT * FROM [o9admin].[dbo].[Transaction] WHERE TransactionNumber='{value_data_transaction_number}'"
        data_Transaction = RU.query_db(sql_query_Transaction)
        # verify total row
        AU.assert_equals('Total row in table [o9admin].[dbo].[Transaction]', 1, len(data_Transaction))
        # verify data in row of transaction
        AU.assert_not_empty('Id', data_Transaction['Id'][0])
        AU.assert_not_null('Id', data_Transaction['Id'][0])
        AU.assert_equals('TransactionCode', 'DPT_CDP', data_Transaction['TransactionCode'][0])
        AU.assert_equals('SubCode', 'SQL_CAN_USER_INVOKE_COMMAND', data_Transaction['SubCode'][0])
        AU.assert_not_empty('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_not_null('TransactionDate', data_Transaction['TransactionDate'][0])
        AU.assert_equals('ValueDate', user_service['working_date_db'], data_Transaction['ValueDate'][0])
        AU.assert_not_empty('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_not_null('ServiceSysDate', data_Transaction['ServiceSysDate'][0])
        AU.assert_equals('ReferenceId', value_data_reference_id, data_Transaction['ReferenceId'][0])
        AU.assert_null('ReferenceCode', data_Transaction['ReferenceCode'][0])
        AU.assert_null('BusinessCode', data_Transaction['BusinessCode'][0])
        AU.assert_equals('TransactionNumber', value_data_transaction_number, data_Transaction['TransactionNumber'][0])
        AU.assert_null('TransId', data_Transaction['TransId'][0])
        AU.assert_equals('ChannelId', 'C', data_Transaction['ChannelId'][0])
        AU.assert_equals('RefId', value_data_ref_id, data_Transaction['RefId'][0])
        AU.assert_equals('UserCode', user_service['username'], data_Transaction['UserCode'][0])
        AU.assert_equals('LoginName', user_service['username'], data_Transaction['LoginName'][0])
        AU.assert_equals('UserName', user_service['fullname'], data_Transaction['UserName'][0])
        AU.assert_equals('BranchCode', user_service['branch_code'], data_Transaction['BranchCode'][0])
        AU.assert_equals('Status', 'C', data_Transaction['Status'][0])
        AU.assert_equals('IsReverse', False, data_Transaction['IsReverse'][0])
        AU.assert_equals('Amount1', 0, data_Transaction['Amount1'][0])
        AU.assert_not_empty('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_null('RequestBody', data_Transaction['RequestBody'][0])
        AU.assert_not_equals('RequestBody', '{}', data_Transaction['RequestBody'][0])
        AU.assert_not_empty('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_null('ResponseBody', data_Transaction['ResponseBody'][0])
        AU.assert_not_equals('ResponseBody', '{}', data_Transaction['ResponseBody'][0])
        AU.assert_equals('Description', '1110: Cash deposit', data_Transaction['Description'][0])
        AU.assert_not_empty('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_null('StartTime', data_Transaction['StartTime'][0])
        AU.assert_not_equals('StartTime', 0, data_Transaction['StartTime'][0])
        AU.assert_not_empty('Duration', data_Transaction['Duration'][0])
        AU.assert_not_null('Duration', data_Transaction['Duration'][0])
        AU.assert_not_equals('Duration', 0, data_Transaction['Duration'][0])

        # database - verify value NOT insert - o9admin - TransactionDetails
        sql_query_TransactionDetails = f"SELECT * FROM [o9admin].[dbo].[TransactionDetails] WHERE RefId='{value_data_ref_id}' ORDER BY Id"
        data_TransactionDetails = RU.query_db(sql_query_TransactionDetails)
        # verify total row
        AU.assert_equals('Total row in table [o9admin].[dbo].[TransactionDetails]', 0, len(data_TransactionDetails))
