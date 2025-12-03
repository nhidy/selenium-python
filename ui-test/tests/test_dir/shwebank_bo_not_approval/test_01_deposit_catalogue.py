import webui_test
import os
from datetime import datetime
from webui_test.logging import log

from webui_test.form_action import FormAction

# Get value from environment variable
RUN_ON_URL = os.getenv("TEST_CONFIG_RUN_ON_URL", "")
USERNAME_LOGIN = os.getenv("TEST_CONFIG_USERNAME_LOGIN", "")
PASSWORD_LOGIN = os.getenv("TEST_CONFIG_PASSWORD_LOGIN", "")
ONE_APP = os.getenv("TEST_CONFIG_ONE_APP", "")
CUSTOMER_CODE = os.getenv("TEST_CONFIG_CUSTOMER_CODE", "")
USERNAME_APPROVE = os.getenv("TEST_CONFIG_USERNAME_APPROVE", "")
PASSWORD_APPROVE = os.getenv("TEST_CONFIG_PASSWORD_APPROVE", "")
USERNAME_REVERSE = os.getenv("TEST_CONFIG_USERNAME_REVERSE", "")
PASSWORD_REVERSE = os.getenv("TEST_CONFIG_PASSWORD_REVERSE", "")
USERNAME_LOGIN_OTHER_BRANCH = os.getenv("TEST_CONFIG_USERNAME_LOGIN_OTHER_BRANCH", "")
PASSWORD_LOGIN_OTHER_BRANCH = os.getenv("TEST_CONFIG_PASSWORD_LOGIN_OTHER_BRANCH", "")
USERNAME_APPROVE_OTHER_BRANCH = os.getenv("TEST_CONFIG_USERNAME_APPROVE_OTHER_BRANCH", "")
PASSWORD_APPROVE_OTHER_BRANCH = os.getenv("TEST_CONFIG_PASSWORD_APPROVE_OTHER_BRANCH", "")
USERNAME_REVERSE_OTHER_BRANCH = os.getenv("TEST_CONFIG_USERNAME_REVERSE_OTHER_BRANCH", "")
PASSWORD_REVERSE_OTHER_BRANCH = os.getenv("TEST_CONFIG_PASSWORD_REVERSE_OTHER_BRANCH", "")

customer_code_personal = CUSTOMER_CODE

# data test
catalogue_code = 'DPTCAT001'
catalogue_name = 'TEST AUTO ADD DPTCAT 01'
currency_code = 'MMK'
deposit_type = 'Fixed Deposit'
passbook_or_statement_or_receipt = 'Passbook'
tenor_1 = '9'
tenor_unit_1 = 'Month(s)'
catalogue_status = 'Normal'
catalogue_name_add_fail = 'TEST AUTO DPTCAT 02'
catalogue_name_update = 'TEST AUTO UPDATE DPTCAT 01'
catalogue_delete_fail = 'CAMMK0000'

class DepositCatalogueTest(FormAction):
    def get_url(self):
        return RUN_ON_URL

    def data_begin(self):
        # get username_reverse and password_reverse
        global username_approve, password_approve, username_reverse, password_reverse, username_login, password_login, username_approve_other_branch, password_approve_other_branch, username_reverse_other_branch, password_reverse_other_branch, username_other_branch, password_other_branch
        username_approve = USERNAME_APPROVE
        password_approve = PASSWORD_APPROVE
        username_reverse = USERNAME_REVERSE
        password_reverse = PASSWORD_REVERSE
        username_login = USERNAME_LOGIN
        password_login = PASSWORD_LOGIN
        username_approve_other_branch = USERNAME_APPROVE_OTHER_BRANCH
        password_approve_other_branch = PASSWORD_APPROVE_OTHER_BRANCH
        username_reverse_other_branch = USERNAME_REVERSE_OTHER_BRANCH
        password_reverse_other_branch = PASSWORD_REVERSE_OTHER_BRANCH
        username_other_branch = USERNAME_LOGIN_OTHER_BRANCH
        password_other_branch = PASSWORD_LOGIN_OTHER_BRANCH
        self.login(username_login, password_login, one_app=ONE_APP)
        global working_date, branch_code
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()
        global gl_account_number
        gl_account_number = f'{branch_code}-1100601000000-01'

    def start_class(self):
        self.data_begin()

    def end_class(self):
        self.logout()

    def reset_browser(self):
        self.logout()
        self.restart_browser()
        self.data_begin()

    def test_01_deposit_catalogue_definition_bo_add_successfully(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_catalogue_definition_add(
            catalogue_code=catalogue_code,
            catalogue_name=catalogue_name,
            currency_code=currency_code,
            deposit_type=deposit_type,
            deposit_sub_type='Fixed Deposit Account - 9 M',
            deposit_purpose='Payment',
            deposit_classification='Normal Deposit',
            passbook_or_statement_or_receipt=passbook_or_statement_or_receipt,
            minimum_deposit_amount='1,000.00',
            catalogue_status=catalogue_status,
            interest_payment_restrictions=['Pending to approve', 'Dormant', 'Maturity', 'Block'],
            debit_accounting=False,
            debit_cash=True,
            debit_deposit=False,
            credit_accounting=True,
            credit_cash=False,
            credit_deposit=False,
            tenor_1=tenor_1,
            tenor_unit_1=tenor_unit_1,
            tenor_2='1',
            tenor_unit_2='Month(s)',
            deposit_tenor='1',
            deposit_tenor_unit='Month(s)',
            interest_tenor='1',
            interest_tenor_unit='Month(s)',
            minimum_tenor='1',
            minimum_tenor_unit='Month(s)',
            multiple_deposit_allow='No',
            multiple_withdrawal_allow='No',
            early_withdrawal='Rate for Early termination',
            minimum_tenor_allow_early_withdrawal='5',
            minimum_tenor_allow_early_withdrawal_unit='Quarter(s)',
            credit_interest_y_n='Yes',
            credit_interest_tenor='14',
            credit_interest_tenor_unit='Week(s)',
            the_day_of_tenor_for_crediting_interest='1',
            minimum_dormant_amount='100,000.56',
            dormant_period='5,689',
            type_of_dormant_period='Day(s)',
            rollover_option='Principal plus interest rollover',
            rollover_to_catalogue='FD09PIMMK',
            initial_deposit_amount='1,000,000.57',
            ifc_codes=['Fixed deposit 9 months in MMK', 'Early withdrawal interest 1 months', 'Early withdrawal interest 3 months', 'Early withdrawal interest 6 months'],
            sys_account_names=['DEPOSIT'],
            account_aliass=['###{REF}**'],
            replace_bys=['2020302031111', '2020202031111', '2020202031111', '2020102020505'],
            system_account_names=['DEPOSIT', 'DEPOSIT', 'DEPOSIT', 'DEPOSIT'],
            business_lines=['Personal', 'SME', 'Corporate', 'Institutional']
        )

    def test_02_deposit_catalogue_definition_bo_add_invalid(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = ['ERROR: An unexpected system error has occurred. Please contact support or check the system logs for more information.']
        self.deposit_catalogue_definition_add(
            catalogue_code=catalogue_code,
            catalogue_name=catalogue_name_add_fail,
            currency_code='MMK',
            deposit_type='Fixed Deposit',
            deposit_sub_type='Fixed Deposit Account - 9 M',
            deposit_purpose='Payment',
            deposit_classification='Normal Deposit',
            passbook_or_statement_or_receipt='Passbook',
            minimum_deposit_amount='1,000.00',
            catalogue_status=catalogue_status,
            interest_payment_restrictions=['Pending to approve', 'Dormant', 'Maturity', 'Block'],
            tenor_1='9',
            tenor_unit_1='Month(s)',
            tenor_2='1',
            tenor_unit_2='Month(s)',
            deposit_tenor='1',
            deposit_tenor_unit='Month(s)',
            interest_tenor='1',
            interest_tenor_unit='Month(s)',
            minimum_tenor='1',
            minimum_tenor_unit='Month(s)',
            multiple_deposit_allow='No',
            multiple_withdrawal_allow='No',
            early_withdrawal='Rate for Early termination',
            minimum_tenor_allow_early_withdrawal='5',
            minimum_tenor_allow_early_withdrawal_unit='Quarter(s)',
            credit_interest_y_n='Yes',
            credit_interest_tenor='14',
            credit_interest_tenor_unit='Week(s)',
            the_day_of_tenor_for_crediting_interest='1',
            minimum_dormant_amount='100,000.56',
            dormant_period='5,689',
            type_of_dormant_period='Day(s)',
            rollover_option='Principal plus interest rollover',
            rollover_to_catalogue='FD09PIMMK',
            initial_deposit_amount='1,000,000.57',
            list_error_message=list_error_message
        )

    def test_03_deposit_catalogue_definition_search_nothing(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_catalogue_definition_simple_search(catalogue_name_add_fail)
        self.assert_search_not_found()

    def test_04_deposit_catalogue_definition_search(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        self.assert_table_data('Catalogue name', 1, catalogue_name)
        self.assert_table_data('Currency code', 1, currency_code)
        self.assert_table_data('Deposit type', 1, deposit_type)
        self.assert_table_data('Passbook or statement', 1, passbook_or_statement_or_receipt)
        self.assert_table_data('Tenor', 1, tenor_1)
        self.assert_table_data('Tenor unit', 1, tenor_unit_1)
        self.assert_table_data('Status', 1, catalogue_status)

    def test_05_deposit_catalogue_definition_view(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_catalogue_definition_view(
            catalogue_code=catalogue_code,
            catalogue_name=catalogue_name,
            interest_payment_restrictions=['Pending to approve', 'Dormant', 'Maturity', 'Block'],
            expected_ifc_list_codes=['117', '124', '125', '126'],
            expected_ifc_names=['Fixed deposit 9 months in MMK', 'Early withdrawal interest 1 months', 'Early withdrawal interest 3 months', 'Early withdrawal interest 6 months'],
            expected_ifc_values=['9.60000', '7.00000', '7.00000', '7.00000'],
            expected_ifc_types=['Interest', 'Interest', 'Interest', 'Interest'],
            expected_ifc_tenors=['1', '1', '1', '1'],
            expected_ifc_tenor_units=['Year(s)', 'Year(s)', 'Year(s)', 'Year(s)'],
            expected_ifc_statuss=['Normal', 'Normal', 'Normal', 'Normal'],
            expected_gls_sys_account_names=['DEPOSIT'],
            expected_gls_account_aliass=['###{REF}**'],
            expected_extension_sys_account_names=['DEPOSIT', 'DEPOSIT', 'DEPOSIT', 'DEPOSIT'],
            expected_extension_conditions=['{"sector":null,"resident_status":null,"categories":"C1","account_resident":null,"subproduct":null}',
                '{"sector":null,"resident_status":null,"categories":"C2","account_resident":null,"subproduct":null}',
                '{"sector":null,"resident_status":null,"categories":"C3","account_resident":null,"subproduct":null}',
                '{"sector":null,"resident_status":null,"categories":"C4","account_resident":null,"subproduct":null}'],
            expected_extension_replace_bys=['2020302031111', '2020202031111', '2020202031111', '2020102020505']
        )

    def test_06_deposit_catalogue_definition_update_successfully(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_catalogue_definition_update(
            catalogue_code=catalogue_code,
            catalogue_name=catalogue_name_update
        )
        self.deposit_catalogue_definition_view(
            catalogue_code=catalogue_code,
            catalogue_name=catalogue_name_update
        )

    def test_07_deposit_catalogue_definition_update_invalid(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = ['Name: Can not be blank']
        self.deposit_catalogue_definition_update(
            catalogue_code=catalogue_code,
            catalogue_name='',
            list_error_message=list_error_message
        )

    def test_08_deposit_catalogue_definition_delete_successfully(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_catalogue_definition_delete(
            catalogue_code=catalogue_code,
            expected_message='Deleted successfully',
        )
        self.deposit_catalogue_definition_simple_search(catalogue_code)
        self.assert_search_not_found()

    def test_09_deposit_catalogue_definition_delete_invalid(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        list_error_message = ['ERROR: Catid is [1] used by other deposit account- en']
        self.deposit_catalogue_definition_delete(
            catalogue_code='CAMMK0000',
            list_error_message=list_error_message
        )

if __name__ == '__main__': 
    webui_test.main()