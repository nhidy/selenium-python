import random
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

random_num = f"{random.randint(0, 99999):06}"
date_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

action_add ='DPT-Catalogue Definition-Add'
action_update ='DPT-Catalogue Definition-Update'
tran_name_delete = 'DPT_DELETE_CATALOG'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_catalogue_code = 'AUTO00003'
value_currency_code = 'MMK'
value_deposit_type = 'Fixed Deposit'
value_deposit_sub_type = 'Fixed Deposit Account - 9 M'
value_deposit_purpose = 'Savings'
value_deposit_classification = 'Normal Deposit'
value_passbook_or_statement_or_receipt = 'Passbook'
value_created_by = USERNAME_LOGIN
value_approved_by = USERNAME_APPROVE
value_debit_accounting = True
value_debit_cash = True
value_debit_deposit = True
value_credit_accounting = True
value_credit_cash = True
value_credit_deposit = True
value_tenor_1 = '9'
value_tenor_unit_1 = 'Month(s)'
value_tenor_2 = '0'
value_tenor_unit_2 = 'Day(s)'
value_deposit_tenor = '0'
value_deposit_tenor_unit = 'Month(s)'
value_interest_tenor_unit = 'Lump Sum'
value_interest_tenor = '0'
value_minimum_tenor = '0'
value_minimum_tenor_unit = 'Day(s)'
value_multiple_deposit_allow = 'No'
value_multiple_withdrawal_allow = 'No'
value_early_withdrawal = 'Rate for Early termination'
value_minimum_tenor_allow_early_withdrawal = '1'
value_minimum_tenor_allow_early_withdrawal_unit = 'Month(s)'
value_credit_interest_y_n = None
value_credit_interest_tenor = None
value_credit_interest_tenor_unit = None
value_the_day_of_tenor_for_crediting_interest = None
value_minimum_dormant_amount = '0.00'
value_dormant_period = '1,095'
value_type_of_dormant_period = 'Day(s)'
value_rollover_option = 'Principal rollover only'
value_rollover_to_catalogue = ''
value_initial_deposit_amount = '50,000.00'
value_ifc_codes = ['Fixed deposit 9 months in MMK', 'Early withdrawal interest 1 months', 'Early withdrawal interest 3 months', 'Early withdrawal interest 6 months']
value_expected_ifc_list_codes = ['117', '124', '125', '126']
value_expected_ifc_names = value_ifc_codes
value_expected_ifc_values = ['9.60000', '7.00000', '7.00000', '7.00000']
value_expected_ifc_types = ['Interest', 'Interest', 'Interest', 'Interest']
value_expected_ifc_tenors = ['1', '1', '1', '1']
value_expected_ifc_tenor_units = ['Year(s)', 'Year(s)', 'Year(s)', 'Year(s)']
value_expected_ifc_statuses = ['Normal', 'Normal', 'Normal', 'Normal']
value_expected_gls_sys_account_names = ['DEPOSIT']
value_expected_gls_account_aliass = ['###{REF}**']
value_expected_extension_sys_account_names = ['DEPOSIT', 'DEPOSIT', 'DEPOSIT', 'DEPOSIT']
value_expected_extension_replace_bys = ['2020302031111', '2020202031111', '2020202031111', '2020102020505']
value_business_lines = ['Personal', 'SME', 'Corporate', 'Institutional']

# value_expected_extension_conditions_add = ['{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-","bank_identification":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C2","subproduct":"-","bank_identification":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-","bank_identification":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C4","subproduct":"-","bank_identification":"-"}']
# Update after fixed
value_expected_extension_conditions_add = ['{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C2","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C4","subproduct":"-"}']

# value_expected_extension_conditions_view = ['{"sector":null,"resident_status":null,"categories":"C1","account_resident":null,"subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C2","account_resident":null,"subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C3","account_resident":null,"subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C4","account_resident":null,"subproduct":null}']
# Update after fixed
value_expected_extension_conditions_view = ['{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C2","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C4","subproduct":null}']

# data test add
catalogue_code_test_add = value_catalogue_code
catalogue_name_test_add = f'AUTO TEST add {date_time}'
currency_code_test_add = value_currency_code
deposit_type_test_add = value_deposit_type
deposit_sub_type_test_add = value_deposit_sub_type
deposit_purpose_test_add = value_deposit_purpose
deposit_classification_test_add = value_deposit_classification
passbook_or_statement_or_receipt_test_add = value_passbook_or_statement_or_receipt
minimum_deposit_amount_test_add = '1,000.00'
catalogue_status_test_add = 'Normal'
interest_payment_restrictions_test_add = ['Pending to approve', 'Dormant', 'Maturity', 'Block']
debit_accounting_test_add = value_debit_accounting
debit_cash_test_add = value_debit_cash
debit_deposit_test_add = value_debit_deposit
credit_accounting_test_add =  value_credit_accounting
credit_cash_test_add = value_credit_cash
credit_deposit_test_add = value_credit_deposit
tenor_1_test_add = value_tenor_1
tenor_unit_1_test_add = value_tenor_unit_1
tenor_2_test_add = value_tenor_2
tenor_unit_2_test_add = value_tenor_unit_2
deposit_tenor_test_add = value_deposit_tenor
deposit_tenor_unit_test_add = value_deposit_tenor_unit
interest_tenor_test_add = value_interest_tenor
interest_tenor_unit_test_add = value_interest_tenor_unit
minimum_tenor_test_add = value_minimum_tenor
minimum_tenor_unit_test_add = value_minimum_tenor_unit
multiple_deposit_allow_test_add = value_multiple_deposit_allow
multiple_withdrawal_allow_test_add = value_multiple_withdrawal_allow
early_withdrawal_test_add = value_early_withdrawal
minimum_tenor_allow_early_withdrawal_test_add = value_minimum_tenor_allow_early_withdrawal
minimum_tenor_allow_early_withdrawal_unit_test_add = value_minimum_tenor_allow_early_withdrawal_unit
credit_interest_y_n_test_add = value_credit_interest_y_n
credit_interest_tenor_test_add = value_credit_interest_tenor
credit_interest_tenor_unit_test_add = value_credit_interest_tenor_unit
the_day_of_tenor_for_crediting_interest_test_add = value_the_day_of_tenor_for_crediting_interest
minimum_dormant_amount_test_add = value_minimum_dormant_amount
dormant_period_test_add = value_dormant_period
type_of_dormant_period_test_add = value_type_of_dormant_period
rollover_option_test_add = value_rollover_option
rollover_to_catalogue_test_add = value_rollover_to_catalogue
initial_deposit_amount_test_add = value_initial_deposit_amount
ifc_codes_test_add = value_ifc_codes
sys_account_names_test_add = value_expected_gls_sys_account_names
coa_accounts_test_add = None
account_aliass_test_add = value_expected_gls_account_aliass
replace_code_test_add = None
replace_bys_test_add = value_expected_extension_replace_bys
system_account_names_test_add = value_expected_extension_sys_account_names
customer_sectors_test_add = None
customer_resident_statuss_test_add = None
business_lines_test_add = value_business_lines
sub_products_test_add = None
bank_identifications_test_add = None
list_error_message_test_add = None

# data test add verify
catalogue_code_test_add_verify = value_catalogue_code
catalogue_name_test_add_verify = catalogue_name_test_add
currency_code_test_add_verify = value_currency_code
deposit_type_test_add_verify = value_deposit_type
deposit_sub_type_test_add_verify = value_deposit_sub_type
deposit_purpose_test_add_verify = value_deposit_purpose
deposit_classification_test_add_verify = value_deposit_classification
passbook_or_statement_or_receipt_test_add_verify = value_passbook_or_statement_or_receipt
minimum_deposit_amount_test_add_verify = minimum_deposit_amount_test_add
catalogue_status_test_add_verify = catalogue_status_test_add
interest_payment_restrictions_test_add_verify = interest_payment_restrictions_test_add
debit_accounting_test_add_verify = value_debit_accounting
debit_cash_test_add_verify = value_debit_cash
debit_deposit_test_add_verify = value_debit_deposit
credit_accounting_test_add_verify = value_credit_accounting
credit_cash_test_add_verify = value_credit_cash
credit_deposit_test_add_verify = value_credit_deposit
tenor_1_test_add_verify = value_tenor_1
tenor_unit_1_test_add_verify = value_tenor_unit_1
tenor_2_test_add_verify = value_tenor_2
tenor_unit_2_test_add_verify = value_tenor_unit_2
deposit_tenor_test_add_verify = value_deposit_tenor
deposit_tenor_unit_test_add_verify = value_deposit_tenor_unit
interest_tenor_test_add_verify = value_interest_tenor
interest_tenor_unit_test_add_verify = value_interest_tenor_unit
minimum_tenor_test_add_verify = value_minimum_tenor
minimum_tenor_unit_test_add_verify = value_minimum_tenor_unit
multiple_deposit_allow_test_add_verify = value_multiple_deposit_allow
multiple_withdrawal_allow_test_add_verify = value_multiple_withdrawal_allow
early_withdrawal_test_add_verify = value_early_withdrawal
minimum_tenor_allow_early_withdrawal_test_add_verify = value_minimum_tenor_allow_early_withdrawal
minimum_tenor_allow_early_withdrawal_unit_test_add_verify = value_minimum_tenor_allow_early_withdrawal_unit
credit_interest_y_n_test_add_verify = value_credit_interest_y_n
credit_interest_tenor_test_add_verify = value_credit_interest_tenor
credit_interest_tenor_unit_test_add_verify = value_credit_interest_tenor_unit
the_day_of_tenor_for_crediting_interest_test_add_verify = value_the_day_of_tenor_for_crediting_interest
minimum_dormant_amount_test_add_verify = value_minimum_dormant_amount
dormant_period_test_add_verify = value_dormant_period
type_of_dormant_period_test_add_verify = value_type_of_dormant_period
rollover_option_test_add_verify = value_rollover_option
rollover_to_catalogue_test_add_verify = value_rollover_to_catalogue
initial_deposit_amount_test_add_verify = value_initial_deposit_amount
expected_ifc_list_codes_test_add_verify = value_expected_ifc_list_codes
expected_ifc_names_test_add_verify = value_expected_ifc_names
expected_ifc_values_test_add_verify = value_expected_ifc_values
expected_ifc_types_test_add_verify = value_expected_ifc_types
expected_ifc_tenors_test_add_verify = value_expected_ifc_tenors
expected_ifc_tenor_units_test_add_verify = value_expected_ifc_tenor_units
expected_ifc_statuss_test_add_verify = value_expected_ifc_statuses
expected_gls_sys_account_names_test_add_verify = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_add_verify = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_add_verify = value_expected_extension_sys_account_names
expected_extension_conditions_test_add_verify = value_expected_extension_conditions_add
expected_extension_replace_bys_test_add_verify = value_expected_extension_replace_bys

# data test view add
catalogue_code_test_view_add = value_catalogue_code
catalogue_name_test_view_add = catalogue_name_test_add
currency_code_test_view_add = value_currency_code
deposit_type_test_view_add = value_deposit_type
deposit_sub_type_test_view_add = value_deposit_sub_type
deposit_purpose_test_view_add = value_deposit_purpose
deposit_classification_test_view_add = value_deposit_classification
passbook_or_statement_or_receipt_test_view_add = value_passbook_or_statement_or_receipt
minimum_deposit_amount_test_view_add = minimum_deposit_amount_test_add
catalogue_status_test_view_add = catalogue_status_test_add
interest_payment_restrictions_test_view_add = interest_payment_restrictions_test_add
created_by_test_view_add = value_created_by
approved_by_test_view_add = value_approved_by
debit_accounting_test_view_add = value_debit_accounting
debit_cash_test_view_add = value_debit_cash
debit_deposit_test_view_add = value_debit_deposit
credit_accounting_test_view_add = value_credit_accounting
credit_cash_test_view_add = value_credit_cash
credit_deposit_test_view_add = value_credit_deposit
tenor_1_test_view_add = value_tenor_1
tenor_unit_1_test_view_add = value_tenor_unit_1
tenor_2_test_view_add = value_tenor_2
tenor_unit_2_test_view_add = value_tenor_unit_2
deposit_tenor_test_view_add = value_deposit_tenor
deposit_tenor_unit_test_view_add = value_deposit_tenor_unit
interest_tenor_unit_test_view_add = value_interest_tenor_unit
interest_tenor_test_view_add = value_interest_tenor
minimum_tenor_test_view_add = value_minimum_tenor
minimum_tenor_unit_test_view_add = value_minimum_tenor_unit
multiple_deposit_allow_test_view_add = value_multiple_deposit_allow
multiple_withdrawal_allow_test_view_add = value_multiple_withdrawal_allow
early_withdrawal_test_view_add = value_early_withdrawal
minimum_tenor_allow_early_withdrawal_test_view_add = value_minimum_tenor_allow_early_withdrawal
minimum_tenor_allow_early_withdrawal_unit_test_view_add = value_minimum_tenor_allow_early_withdrawal_unit
credit_interest_y_n_test_view_add = value_credit_interest_y_n
credit_interest_tenor_test_view_add = value_credit_interest_tenor
credit_interest_tenor_unit_test_view_add = value_credit_interest_tenor_unit
the_day_of_tenor_for_crediting_interest_test_view_add = value_the_day_of_tenor_for_crediting_interest
minimum_dormant_amount_test_view_add = value_minimum_dormant_amount
dormant_period_test_view_add = value_dormant_period
type_of_dormant_period_test_view_add = value_type_of_dormant_period
rollover_option_test_view_add = value_rollover_option
rollover_to_catalogue_test_view_add = value_rollover_to_catalogue
initial_deposit_amount_test_view_add = value_initial_deposit_amount
expected_ifc_list_codes_test_view_add = value_expected_ifc_list_codes
expected_ifc_names_test_view_add = value_expected_ifc_names
expected_ifc_values_test_view_add = value_expected_ifc_values
expected_ifc_types_test_view_add = value_expected_ifc_types
expected_ifc_tenors_test_view_add = value_expected_ifc_tenors
expected_ifc_tenor_units_test_view_add = value_expected_ifc_tenor_units
expected_ifc_statuss_test_view_add = value_expected_ifc_statuses
expected_gls_sys_account_names_test_view_add = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_view_add = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_view_add = value_expected_extension_sys_account_names
expected_extension_conditions_test_view_add = value_expected_extension_conditions_view
expected_extension_replace_bys_test_view_add = value_expected_extension_replace_bys

# data test update
catalogue_code_test_update = value_catalogue_code
catalogue_name_test_update = f'AUTO TEST update {date_time}'
currency_code_test_update = value_currency_code
deposit_type_test_update = value_deposit_type
deposit_sub_type_test_update = value_deposit_sub_type
deposit_purpose_test_update = value_deposit_purpose
deposit_classification_test_update = value_deposit_classification
passbook_or_statement_or_receipt_test_update = value_passbook_or_statement_or_receipt
minimum_deposit_amount_test_update = '20,000.00'
catalogue_status_test_update = 'Closed'
interest_payment_restrictions_test_update = ['Pending to approve', 'Dormant', 'Maturity', 'Block', 'Normal']
debit_accounting_test_update = value_debit_accounting
debit_cash_test_update = value_debit_cash
debit_deposit_test_update = value_debit_deposit
credit_accounting_test_update = value_credit_accounting
credit_cash_test_update = value_credit_cash
credit_deposit_test_update = value_credit_deposit
minimum_tenor_unit_test_update = value_minimum_tenor_unit
multiple_deposit_allow_test_update = value_multiple_deposit_allow
multiple_withdrawal_allow_test_update = value_multiple_withdrawal_allow
credit_interest_y_n_test_update = None
credit_interest_tenor_test_update = None
credit_interest_tenor_unit_test_update = None
the_day_of_tenor_for_crediting_interest_test_update = None
minimum_dormant_amount_test_update = value_minimum_dormant_amount
dormant_period_test_update = value_dormant_period
type_of_dormant_period_test_update = value_type_of_dormant_period
initial_deposit_amount_test_update = value_initial_deposit_amount
list_error_message_test_update = None

# data test update verify
catalogue_code_test_update_verify = value_catalogue_code
catalogue_name_test_update_verify = catalogue_name_test_update
currency_code_test_update_verify = value_currency_code
deposit_type_test_update_verify = value_deposit_type
deposit_sub_type_test_update_verify = value_deposit_sub_type
deposit_purpose_test_update_verify = value_deposit_purpose
deposit_classification_test_update_verify = value_deposit_classification
passbook_or_statement_or_receipt_test_update_verify = value_passbook_or_statement_or_receipt
minimum_deposit_amount_test_update_verify = minimum_deposit_amount_test_update
catalogue_status_test_update_verify = catalogue_status_test_update
interest_payment_restrictions_test_update_verify = interest_payment_restrictions_test_update
created_by_test_update_verify = value_created_by
approved_by_test_update_verify = value_approved_by
debit_accounting_test_update_verify = value_debit_accounting
debit_cash_test_update_verify = value_debit_cash
debit_deposit_test_update_verify = value_debit_deposit
credit_accounting_test_update_verify = value_credit_accounting
credit_cash_test_update_verify = value_credit_cash
credit_deposit_test_update_verify = value_credit_deposit
tenor_1_test_update_verify = value_tenor_1
tenor_unit_1_test_update_verify = value_tenor_unit_1
tenor_2_test_update_verify = value_tenor_2
tenor_unit_2_test_update_verify = value_tenor_unit_2
deposit_tenor_test_update_verify = value_deposit_tenor
deposit_tenor_unit_test_update_verify = value_deposit_tenor_unit
interest_tenor_unit_test_update_verify = value_interest_tenor_unit
interest_tenor_test_update_verify = value_interest_tenor
minimum_tenor_test_update_verify = value_minimum_tenor
minimum_tenor_unit_test_update_verify = value_minimum_tenor_unit
multiple_deposit_allow_test_update_verify = value_multiple_deposit_allow
multiple_withdrawal_allow_test_update_verify = value_multiple_withdrawal_allow
early_withdrawal_test_update_verify = value_early_withdrawal
minimum_tenor_allow_early_withdrawal_test_update_verify = value_minimum_tenor_allow_early_withdrawal
minimum_tenor_allow_early_withdrawal_unit_test_update_verify = value_minimum_tenor_allow_early_withdrawal_unit
credit_interest_y_n_test_update_verify = value_credit_interest_y_n
credit_interest_tenor_test_update_verify = value_credit_interest_tenor
credit_interest_tenor_unit_test_update_verify = value_credit_interest_tenor_unit
the_day_of_tenor_for_crediting_interest_test_update_verify = value_the_day_of_tenor_for_crediting_interest
minimum_dormant_amount_test_update_verify = value_minimum_dormant_amount
dormant_period_test_update_verify = value_dormant_period
type_of_dormant_period_test_update_verify = value_type_of_dormant_period
rollover_option_test_update_verify = value_rollover_option
rollover_to_catalogue_test_update_verify = value_rollover_to_catalogue
initial_deposit_amount_test_update_verify = value_initial_deposit_amount
expected_ifc_list_codes_test_update_verify = value_expected_ifc_list_codes
expected_ifc_names_test_update_verify = value_expected_ifc_names
expected_ifc_values_test_update_verify = value_expected_ifc_values
expected_ifc_types_test_update_verify = value_expected_ifc_types
expected_ifc_tenors_test_update_verify = value_expected_ifc_tenors
expected_ifc_tenor_units_test_update_verify = value_expected_ifc_tenor_units
expected_ifc_statuss_test_update_verify = value_expected_ifc_statuses
expected_gls_sys_account_names_test_update_verify = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_update_verify = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_update_verify = value_expected_extension_sys_account_names
expected_extension_conditions_test_update_verify = value_expected_extension_conditions_view
expected_extension_replace_bys_test_update_verify = value_expected_extension_replace_bys

# data test view update
catalogue_code_test_view_update = value_catalogue_code
catalogue_name_test_view_update = catalogue_name_test_update
currency_code_test_view_update = value_currency_code
deposit_type_test_view_update = value_deposit_type
deposit_sub_type_test_view_update = value_deposit_sub_type
deposit_purpose_test_view_update = value_deposit_purpose
deposit_classification_test_view_update = value_deposit_classification
passbook_or_statement_or_receipt_test_view_update = value_passbook_or_statement_or_receipt
minimum_deposit_amount_test_view_update = minimum_deposit_amount_test_update
catalogue_status_test_view_update = catalogue_status_test_update
interest_payment_restrictions_test_view_update = interest_payment_restrictions_test_update
created_by_test_view_update = value_created_by
approved_by_test_view_update = value_approved_by
debit_accounting_test_view_update = value_debit_accounting
debit_cash_test_view_update = value_debit_cash
debit_deposit_test_view_update = value_debit_deposit
credit_accounting_test_view_update = value_credit_accounting
credit_cash_test_view_update = value_credit_cash
credit_deposit_test_view_update = value_credit_deposit
tenor_1_test_view_update = value_tenor_1
tenor_unit_1_test_view_update = value_tenor_unit_1
tenor_2_test_view_update = value_tenor_2
tenor_unit_2_test_view_update = value_tenor_unit_2
deposit_tenor_test_view_update = value_deposit_tenor
deposit_tenor_unit_test_view_update = value_deposit_tenor_unit
interest_tenor_unit_test_view_update = value_interest_tenor_unit
interest_tenor_test_view_update = value_interest_tenor
minimum_tenor_test_view_update = value_minimum_tenor
minimum_tenor_unit_test_view_update = value_minimum_tenor_unit
multiple_deposit_allow_test_view_update = value_multiple_deposit_allow
multiple_withdrawal_allow_test_view_update = value_multiple_withdrawal_allow
early_withdrawal_test_view_update = value_early_withdrawal
minimum_tenor_allow_early_withdrawal_test_view_update = value_minimum_tenor_allow_early_withdrawal
minimum_tenor_allow_early_withdrawal_unit_test_view_update = value_minimum_tenor_allow_early_withdrawal_unit
credit_interest_y_n_test_view_update = value_credit_interest_y_n
credit_interest_tenor_test_view_update = value_credit_interest_tenor
credit_interest_tenor_unit_test_view_update = value_credit_interest_tenor_unit
the_day_of_tenor_for_crediting_interest_test_view_update = value_the_day_of_tenor_for_crediting_interest
minimum_dormant_amount_test_view_update = value_minimum_dormant_amount
dormant_period_test_view_update = value_dormant_period
type_of_dormant_period_test_view_update = value_type_of_dormant_period
rollover_option_test_view_update = value_rollover_option
rollover_to_catalogue_test_view_update = value_rollover_to_catalogue
initial_deposit_amount_test_view_update = value_initial_deposit_amount
expected_ifc_list_codes_test_view_update = value_expected_ifc_list_codes
expected_ifc_names_test_view_update = value_expected_ifc_names
expected_ifc_values_test_view_update = value_expected_ifc_values
expected_ifc_types_test_view_update = value_expected_ifc_types
expected_ifc_tenors_test_view_update = value_expected_ifc_tenors
expected_ifc_tenor_units_test_view_update = value_expected_ifc_tenor_units
expected_ifc_statuss_test_view_update = value_expected_ifc_statuses
expected_gls_sys_account_names_test_view_update = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_view_update = value_expected_gls_account_aliass
expected_extension_sys_account_names_test_view_update = value_expected_extension_sys_account_names
expected_extension_conditions_test_view_update = value_expected_extension_conditions_view
expected_extension_replace_bys_test_view_update = value_expected_extension_replace_bys

class DepositCatalogueFixedTest(FormAction):
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
        global working_date, branch_code, username_logged
        working_date = self.get_working_date()
        branch_code = self.get_logged_branch_code()
        username_logged = self.get_username()
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

# DPT-Catalogue Definition
    def test_001_dpt_cat_fixed_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.deposit_catalogue_definition_add(
            catalogue_code=catalogue_code_test_add,
            catalogue_name=catalogue_name_test_add,
            currency_code=currency_code_test_add,
            deposit_type=deposit_type_test_add,
            deposit_sub_type=deposit_sub_type_test_add,
            deposit_purpose=deposit_purpose_test_add,
            deposit_classification=deposit_classification_test_add,
            passbook_or_statement_or_receipt=passbook_or_statement_or_receipt_test_add,
            minimum_deposit_amount=minimum_deposit_amount_test_add,
            catalogue_status=catalogue_status_test_add,
            interest_payment_restrictions=interest_payment_restrictions_test_add,
            debit_accounting=debit_accounting_test_add,
            debit_cash=debit_cash_test_add,
            debit_deposit=debit_deposit_test_add,
            credit_accounting=credit_accounting_test_add,
            credit_cash=credit_cash_test_add,
            credit_deposit=credit_deposit_test_add,
            tenor_1=tenor_1_test_add,
            tenor_unit_1=tenor_unit_1_test_add,
            tenor_2=tenor_2_test_add,
            tenor_unit_2=tenor_unit_2_test_add,
            deposit_tenor=deposit_tenor_test_add,
            deposit_tenor_unit=deposit_tenor_unit_test_add,
            interest_tenor=interest_tenor_test_add,
            interest_tenor_unit=interest_tenor_unit_test_add,
            minimum_tenor=minimum_tenor_test_add,
            minimum_tenor_unit=minimum_tenor_unit_test_add,
            multiple_deposit_allow=multiple_deposit_allow_test_add,
            multiple_withdrawal_allow=multiple_withdrawal_allow_test_add,
            early_withdrawal=early_withdrawal_test_add,
            minimum_tenor_allow_early_withdrawal=minimum_tenor_allow_early_withdrawal_test_add,
            minimum_tenor_allow_early_withdrawal_unit=minimum_tenor_allow_early_withdrawal_unit_test_add,
            credit_interest_y_n=credit_interest_y_n_test_add,
            credit_interest_tenor=credit_interest_tenor_test_add,
            credit_interest_tenor_unit=credit_interest_tenor_unit_test_add,
            the_day_of_tenor_for_crediting_interest=the_day_of_tenor_for_crediting_interest_test_add,
            minimum_dormant_amount=minimum_dormant_amount_test_add,
            dormant_period=dormant_period_test_add,
            type_of_dormant_period=type_of_dormant_period_test_add,
            rollover_option=rollover_option_test_add,
            rollover_to_catalogue=rollover_to_catalogue_test_add,
            initial_deposit_amount=initial_deposit_amount_test_add,
            ifc_codes=ifc_codes_test_add,
            sys_account_names=sys_account_names_test_add,
            coa_accounts=coa_accounts_test_add,
            account_aliass=account_aliass_test_add,
            replace_code=replace_code_test_add,
            replace_bys=replace_bys_test_add,
            system_account_names=system_account_names_test_add,
            customer_sectors=customer_sectors_test_add,
            customer_resident_statuss=customer_resident_statuss_test_add,
            business_lines=business_lines_test_add,
            sub_products=sub_products_test_add,
            bank_identifications=bank_identifications_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.deposit_catalogue_definition_simple_search(catalogue_code_test_add)
        self.assert_search_not_found()

    def test_002_dpt_cat_fixed_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.deposit_catalogue_definition_add_verify(
            transaction_number=transaction_number_add,
            catalogue_code=catalogue_code_test_add_verify,
            catalogue_name=catalogue_name_test_add_verify,
            currency_code=currency_code_test_add_verify,
            deposit_type=deposit_type_test_add_verify,
            deposit_sub_type=deposit_sub_type_test_add_verify,
            deposit_purpose=deposit_purpose_test_add_verify,
            deposit_classification=deposit_classification_test_add_verify,
            passbook_or_statement_or_receipt=passbook_or_statement_or_receipt_test_add_verify,
            minimum_deposit_amount=minimum_deposit_amount_test_add_verify,
            catalogue_status=catalogue_status_test_add_verify,
            interest_payment_restrictions=interest_payment_restrictions_test_add_verify,
            debit_accounting=debit_accounting_test_add_verify,
            debit_cash=debit_cash_test_add_verify,
            debit_deposit=debit_deposit_test_add_verify,
            credit_accounting=credit_accounting_test_add_verify,
            credit_cash=credit_cash_test_add_verify,
            credit_deposit=credit_deposit_test_add_verify,
            tenor_1=tenor_1_test_add_verify,
            tenor_unit_1=tenor_unit_1_test_add_verify,
            tenor_2=tenor_2_test_add_verify,
            tenor_unit_2=tenor_unit_2_test_add_verify,
            deposit_tenor=deposit_tenor_test_add_verify,
            deposit_tenor_unit=deposit_tenor_unit_test_add_verify,
            interest_tenor=interest_tenor_test_add_verify,
            interest_tenor_unit=interest_tenor_unit_test_add_verify,
            minimum_tenor=minimum_tenor_test_add_verify,
            minimum_tenor_unit=minimum_tenor_unit_test_add_verify,
            multiple_deposit_allow=multiple_deposit_allow_test_add_verify,
            multiple_withdrawal_allow=multiple_withdrawal_allow_test_add_verify,
            early_withdrawal=early_withdrawal_test_add_verify,
            minimum_tenor_allow_early_withdrawal=minimum_tenor_allow_early_withdrawal_test_add_verify,
            minimum_tenor_allow_early_withdrawal_unit=minimum_tenor_allow_early_withdrawal_unit_test_add_verify,
            credit_interest_y_n=credit_interest_y_n_test_add_verify,
            credit_interest_tenor=credit_interest_tenor_test_add_verify,
            credit_interest_tenor_unit=credit_interest_tenor_unit_test_add_verify,
            the_day_of_tenor_for_crediting_interest=the_day_of_tenor_for_crediting_interest_test_add_verify,
            minimum_dormant_amount=minimum_dormant_amount_test_add_verify,
            dormant_period=dormant_period_test_add_verify,
            type_of_dormant_period=type_of_dormant_period_test_add_verify,
            rollover_option=rollover_option_test_add_verify,
            rollover_to_catalogue=rollover_to_catalogue_test_add_verify,
            initial_deposit_amount=initial_deposit_amount_test_add_verify,
            expected_ifc_list_codes=expected_ifc_list_codes_test_add_verify,
            expected_ifc_names=expected_ifc_names_test_add_verify,
            expected_ifc_values=expected_ifc_values_test_add_verify,
            expected_ifc_types=expected_ifc_types_test_add_verify,
            expected_ifc_tenors=expected_ifc_tenors_test_add_verify,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_add_verify,
            expected_ifc_statuss=expected_ifc_statuss_test_add_verify,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_add_verify,
            expected_gls_account_aliass=expected_gls_account_aliass_test_add_verify,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_add_verify,
            expected_extension_conditions=expected_extension_conditions_test_add_verify,
            expected_extension_replace_bys=expected_extension_replace_bys_test_add_verify,
        )

    def test_003_dpt_cat_fixed_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.deposit_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_add,
        )

    def test_004_dpt_cat_fixed_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_add,
            catalogue_name=catalogue_name_test_view_add,
            currency_code=currency_code_test_view_add,
            deposit_type=deposit_type_test_view_add,
            deposit_sub_type=deposit_sub_type_test_view_add,
            deposit_purpose=deposit_purpose_test_view_add,
            deposit_classification=deposit_classification_test_view_add,
            passbook_or_statement_or_receipt=passbook_or_statement_or_receipt_test_view_add,
            minimum_deposit_amount=minimum_deposit_amount_test_view_add,
            catalogue_status=catalogue_status_test_view_add,
            interest_payment_restrictions=interest_payment_restrictions_test_view_add,
            created_by=created_by_test_view_add,
            approved_by=approved_by_test_view_add,
            debit_accounting=debit_accounting_test_view_add,
            debit_cash=debit_cash_test_view_add,
            debit_deposit=debit_deposit_test_view_add,
            credit_accounting=credit_accounting_test_view_add,
            credit_cash=credit_cash_test_view_add,
            credit_deposit=credit_deposit_test_view_add,
            tenor_1=tenor_1_test_view_add,
            tenor_unit_1=tenor_unit_1_test_view_add,
            tenor_2=tenor_2_test_view_add,
            tenor_unit_2=tenor_unit_2_test_view_add,
            deposit_tenor=deposit_tenor_test_view_add,
            deposit_tenor_unit=deposit_tenor_unit_test_view_add,
            interest_tenor_unit=interest_tenor_unit_test_view_add,
            interest_tenor=interest_tenor_test_view_add,
            minimum_tenor=minimum_tenor_test_view_add,
            minimum_tenor_unit=minimum_tenor_unit_test_view_add,
            multiple_deposit_allow=multiple_deposit_allow_test_view_add,
            multiple_withdrawal_allow=multiple_withdrawal_allow_test_view_add,
            early_withdrawal=early_withdrawal_test_view_add,
            minimum_tenor_allow_early_withdrawal=minimum_tenor_allow_early_withdrawal_test_view_add,
            minimum_tenor_allow_early_withdrawal_unit=minimum_tenor_allow_early_withdrawal_unit_test_view_add,
            credit_interest_y_n=credit_interest_y_n_test_view_add,
            credit_interest_tenor=credit_interest_tenor_test_view_add,
            credit_interest_tenor_unit=credit_interest_tenor_unit_test_view_add,
            the_day_of_tenor_for_crediting_interest=the_day_of_tenor_for_crediting_interest_test_view_add,
            minimum_dormant_amount=minimum_dormant_amount_test_view_add,
            dormant_period=dormant_period_test_view_add,
            type_of_dormant_period=type_of_dormant_period_test_view_add,
            rollover_option=rollover_option_test_view_add,
            rollover_to_catalogue=rollover_to_catalogue_test_view_add,
            initial_deposit_amount=initial_deposit_amount_test_view_add,
            expected_ifc_list_codes=expected_ifc_list_codes_test_view_add,
            expected_ifc_names=expected_ifc_names_test_view_add,
            expected_ifc_values=expected_ifc_values_test_view_add,
            expected_ifc_types=expected_ifc_types_test_view_add,
            expected_ifc_tenors=expected_ifc_tenors_test_view_add,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_view_add,
            expected_ifc_statuss=expected_ifc_statuss_test_view_add,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_view_add,
            expected_gls_account_aliass=expected_gls_account_aliass_test_view_add,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_view_add,
            expected_extension_conditions=expected_extension_conditions_test_view_add,
            expected_extension_replace_bys=expected_extension_replace_bys_test_view_add,
        )
        self.assert_activity(
            transaction_number=transaction_number_add,
            maker=username_logged,
            action=action_add
        )

    def test_005_login_with_other_user(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        print(f'Username: {username_logged}')
        self.logout()
        self.login(username_other_branch, password_other_branch, one_app=ONE_APP)
        global other_username_logged
        other_username_logged = self.get_username()
        print(f'Other username: {other_username_logged}')

    def test_006_dpt_cat_fixed_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.deposit_catalogue_definition_update(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
            currency_code=currency_code_test_update,
            deposit_type=deposit_type_test_update,
            deposit_sub_type=deposit_sub_type_test_update,
            deposit_purpose=deposit_purpose_test_update,
            deposit_classification=deposit_classification_test_update,
            passbook_or_statement_or_receipt=passbook_or_statement_or_receipt_test_update,
            minimum_deposit_amount=minimum_deposit_amount_test_update,
            catalogue_status=catalogue_status_test_update,
            interest_payment_restrictions=interest_payment_restrictions_test_update,
            debit_accounting=debit_accounting_test_update,
            debit_cash=debit_cash_test_update,
            debit_deposit=debit_deposit_test_update,
            credit_accounting=credit_accounting_test_update,
            credit_cash=credit_cash_test_update,
            credit_deposit=credit_deposit_test_update,
            minimum_tenor_unit=minimum_tenor_unit_test_update,
            multiple_deposit_allow=multiple_deposit_allow_test_update,
            multiple_withdrawal_allow=multiple_withdrawal_allow_test_update,
            credit_interest_y_n=credit_interest_y_n_test_update,
            credit_interest_tenor=credit_interest_tenor_test_update,
            credit_interest_tenor_unit=credit_interest_tenor_unit_test_update,
            the_day_of_tenor_for_crediting_interest=the_day_of_tenor_for_crediting_interest_test_update,
            minimum_dormant_amount=minimum_dormant_amount_test_update,
            dormant_period=dormant_period_test_update,
            type_of_dormant_period=type_of_dormant_period_test_update,
            initial_deposit_amount=initial_deposit_amount_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.deposit_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_view_add,
        )

    def test_007_dpt_cat_fixed_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.deposit_catalogue_definition_update_verify(
            transaction_number=transaction_number_update,
            catalogue_code=catalogue_code_test_update_verify,
            catalogue_name=catalogue_name_test_update_verify,
            currency_code=currency_code_test_update_verify,
            deposit_type=deposit_type_test_update_verify,
            deposit_sub_type=deposit_sub_type_test_update_verify,
            deposit_purpose=deposit_purpose_test_update_verify,
            deposit_classification=deposit_classification_test_update_verify,
            passbook_or_statement_or_receipt=passbook_or_statement_or_receipt_test_update_verify,
            minimum_deposit_amount=minimum_deposit_amount_test_update_verify,
            catalogue_status=catalogue_status_test_update_verify,
            interest_payment_restrictions=interest_payment_restrictions_test_update_verify,
            created_by=created_by_test_update_verify,
            approved_by=approved_by_test_update_verify,
            debit_accounting=debit_accounting_test_update_verify,
            debit_cash=debit_cash_test_update_verify,
            debit_deposit=debit_deposit_test_update_verify,
            credit_accounting=credit_accounting_test_update_verify,
            credit_cash=credit_cash_test_update_verify,
            credit_deposit=credit_deposit_test_update_verify,
            tenor_1=tenor_1_test_update_verify,
            tenor_unit_1=tenor_unit_1_test_update_verify,
            tenor_2=tenor_2_test_update_verify,
            tenor_unit_2=tenor_unit_2_test_update_verify,
            deposit_tenor=deposit_tenor_test_update_verify,
            deposit_tenor_unit=deposit_tenor_unit_test_update_verify,
            interest_tenor_unit=interest_tenor_unit_test_update_verify,
            interest_tenor=interest_tenor_test_update_verify,
            minimum_tenor=minimum_tenor_test_update_verify,
            minimum_tenor_unit=minimum_tenor_unit_test_update_verify,
            multiple_deposit_allow=multiple_deposit_allow_test_update_verify,
            multiple_withdrawal_allow=multiple_withdrawal_allow_test_update_verify,
            early_withdrawal=early_withdrawal_test_update_verify,
            minimum_tenor_allow_early_withdrawal=minimum_tenor_allow_early_withdrawal_test_update_verify,
            minimum_tenor_allow_early_withdrawal_unit=minimum_tenor_allow_early_withdrawal_unit_test_update_verify,
            credit_interest_y_n=credit_interest_y_n_test_update_verify,
            credit_interest_tenor=credit_interest_tenor_test_update_verify,
            credit_interest_tenor_unit=credit_interest_tenor_unit_test_update_verify,
            the_day_of_tenor_for_crediting_interest=the_day_of_tenor_for_crediting_interest_test_update_verify,
            minimum_dormant_amount=minimum_dormant_amount_test_update_verify,
            dormant_period=dormant_period_test_update_verify,
            type_of_dormant_period=type_of_dormant_period_test_update_verify,
            rollover_option=rollover_option_test_update_verify,
            rollover_to_catalogue=rollover_to_catalogue_test_update_verify,
            initial_deposit_amount=initial_deposit_amount_test_update_verify,
            expected_ifc_list_codes=expected_ifc_list_codes_test_update_verify,
            expected_ifc_names=expected_ifc_names_test_update_verify,
            expected_ifc_values=expected_ifc_values_test_update_verify,
            expected_ifc_types=expected_ifc_types_test_update_verify,
            expected_ifc_tenors=expected_ifc_tenors_test_update_verify,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_update_verify,
            expected_ifc_statuss=expected_ifc_statuss_test_update_verify,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_update_verify,
            expected_gls_account_aliass=expected_gls_account_aliass_test_update_verify,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_update_verify,
            expected_extension_conditions=expected_extension_conditions_test_update_verify,
            expected_extension_replace_bys=expected_extension_replace_bys_test_update_verify,
        )

    def test_008_dpt_cat_fixed_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.deposit_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
        )

    def test_009_dpt_cat_fixed_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_update,
            catalogue_name=catalogue_name_test_view_update,
            currency_code=currency_code_test_view_update,
            deposit_type=deposit_type_test_view_update,
            deposit_sub_type=deposit_sub_type_test_view_update,
            deposit_purpose=deposit_purpose_test_view_update,
            deposit_classification=deposit_classification_test_view_update,
            passbook_or_statement_or_receipt=passbook_or_statement_or_receipt_test_view_update,
            minimum_deposit_amount=minimum_deposit_amount_test_view_update,
            catalogue_status=catalogue_status_test_view_update,
            interest_payment_restrictions=interest_payment_restrictions_test_view_update,
            created_by=created_by_test_view_update,
            approved_by=approved_by_test_view_update,
            debit_accounting=debit_accounting_test_view_update,
            debit_cash=debit_cash_test_view_update,
            debit_deposit=debit_deposit_test_view_update,
            credit_accounting=credit_accounting_test_view_update,
            credit_cash=credit_cash_test_view_update,
            credit_deposit=credit_deposit_test_view_update,
            tenor_1=tenor_1_test_view_update,
            tenor_unit_1=tenor_unit_1_test_view_update,
            tenor_2=tenor_2_test_view_update,
            tenor_unit_2=tenor_unit_2_test_view_update,
            deposit_tenor=deposit_tenor_test_view_update,
            deposit_tenor_unit=deposit_tenor_unit_test_view_update,
            interest_tenor_unit=interest_tenor_unit_test_view_update,
            interest_tenor=interest_tenor_test_view_update,
            minimum_tenor=minimum_tenor_test_view_update,
            minimum_tenor_unit=minimum_tenor_unit_test_view_update,
            multiple_deposit_allow=multiple_deposit_allow_test_view_update,
            multiple_withdrawal_allow=multiple_withdrawal_allow_test_view_update,
            early_withdrawal=early_withdrawal_test_view_update,
            minimum_tenor_allow_early_withdrawal=minimum_tenor_allow_early_withdrawal_test_view_update,
            minimum_tenor_allow_early_withdrawal_unit=minimum_tenor_allow_early_withdrawal_unit_test_view_update,
            credit_interest_y_n=credit_interest_y_n_test_view_update,
            credit_interest_tenor=credit_interest_tenor_test_view_update,
            credit_interest_tenor_unit=credit_interest_tenor_unit_test_view_update,
            the_day_of_tenor_for_crediting_interest=the_day_of_tenor_for_crediting_interest_test_view_update,
            minimum_dormant_amount=minimum_dormant_amount_test_view_update,
            dormant_period=dormant_period_test_view_update,
            type_of_dormant_period=type_of_dormant_period_test_view_update,
            rollover_option=rollover_option_test_view_update,
            rollover_to_catalogue=rollover_to_catalogue_test_view_update,
            initial_deposit_amount=initial_deposit_amount_test_view_update,
            expected_ifc_list_codes=expected_ifc_list_codes_test_view_update,
            expected_ifc_names=expected_ifc_names_test_view_update,
            expected_ifc_values=expected_ifc_values_test_view_update,
            expected_ifc_types=expected_ifc_types_test_view_update,
            expected_ifc_tenors=expected_ifc_tenors_test_view_update,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_view_update,
            expected_ifc_statuss=expected_ifc_statuss_test_view_update,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_view_update,
            expected_gls_account_aliass=expected_gls_account_aliass_test_view_update,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_view_update,
            expected_extension_conditions=expected_extension_conditions_test_view_update,
            expected_extension_replace_bys=expected_extension_replace_bys_test_view_update,
        )
        self.assert_activity(
            transaction_number=transaction_number_add,
            maker=username_logged,
            action=action_add
        )
        self.assert_activity(
            transaction_number=transaction_number_update,
            maker=other_username_logged,
            action=action_update
        )

    def test_010_dpt_cat_fixed_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_catalogue_definition_delete(
            catalogue_code=value_catalogue_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.deposit_catalogue_definition_search_verify(
            catalogue_code=value_catalogue_code,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_catalogue_code,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_catalogue_code,
            tran_name=tran_name_delete,
        )

    def test_011_dpt_cat_fixed_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_catalogue_definition_simple_search(value_catalogue_code)
        self.assert_search_not_found()

if __name__ == '__main__': 
    webui_test.main()