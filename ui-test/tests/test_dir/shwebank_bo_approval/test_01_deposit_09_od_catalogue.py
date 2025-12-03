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

action_add ='DPT-OD Catalogue Definition-Add'
action_update ='DPT-OD Catalogue Definition-Update'
catalogue_code_in_use = 'OD3MMMK001'
list_error_message_in_use = [f'ERROR: Catalog [{catalogue_code_in_use}] is used']
tran_name_delete = 'DPT_DELETE_ODCAT'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_catalogue_code = 'AUTO000001'
value_currency_code = 'MMK'
value_secure_type = 'Partial secured'
value_secure_rate = '80.00'
value_secured_by_currency = value_currency_code
value_credit_type = 'Blanket'
value_credit_sub_type = 'Overdraft'
value_tenor_type = 'Long term'
value_credit_purpose = 'INDUSTRY'
value_credit_classification = 'Auto Loan'
value_credit_facility = 'Over Draft'
value_disbursement_mode = 'Revolving'
value_is_provision = 'Yes'
value_classification_option = 'NPL auto'
value_status = 'Normal'
value_created_by = USERNAME_LOGIN
value_approved_by = USERNAME_APPROVE
value_principal_collection_tenor = '1'
value_principal_collection_tenor_unit = 'Month(s)'
value_principal_grace_period = '0'
value_principal_due_on_holiday = '0'
value_interest_collection_tenor = '1'
value_interest_collection_tenor_unit = 'Month(s)'
value_interest_grace_period = '0'
value_interest_due_on_holiday = '0'
value_fine_collection_tenor = '1'
value_fine_collection_tenor_unit = 'Month(s)'
value_fine_grace_period = '0'
value_fine_due_on_holiday = '0'
value_standard = '0.00'
value_watch = '5.00'
value_substandard = '25.00'
value_doubtful = '50.00'
value_loss = '100.00'
value_email = False
value_push_notification = True
value_sms = False
value_list_error_message = None

value_ifc_codes = ['201', '202']
value_expected_ifc_list_codes =  ['201', '202']
value_expected_ifc_names = ['OD3M - Overdraft - Main Interest', 'OD3M - Overdraft - Commitment Fee']
value_expected_ifc_values = ['9.00000', '1.00000']
value_expected_ifc_types = ['Interest', 'Fee']
value_expected_ifc_tenors = ['1', '1']
value_expected_ifc_tenor_units = ['Year(s)', 'Year(s)']
value_expected_ifc_statuses = ['Normal', 'Normal']
value_expected_gls_account_aliass = ['###{REF}**', '###{REF}**', '###{REF}**', '###{REF}**', '###{REF}**']
value_expected_gls_sys_account_names = ['CREDIT0', 'CREDIT1', 'CREDIT2', 'CREDIT3', 'CREDIT4']
value_expected_extension_sys_account_names = ['CREDIT0', 'CREDIT1', 'CREDIT2', 'CREDIT3', 'CREDIT4', 'CREDIT0', 'CREDIT1', 'CREDIT2', 'CREDIT3', 'CREDIT4']
value_expected_extension_replace_bys = ['1030102020101', '1030103020202', '1030103020202', '1030103020202', '1030103020202', '1030102020101', '1030102020101', '1030102020101', '1030102020101', '1030102020101']
value_business_lines = ['Personal', 'Personal', 'Personal', 'Personal', 'Personal', 'Corporate', 'Corporate', 'Corporate', 'Corporate', 'Corporate']
value_expected_extension_conditions_add = ['{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}',
    '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}']

value_expected_extension_conditions_view = ['{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}',
    '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}']

# data test add
catalogue_code_test_add = value_catalogue_code
catalogue_name_test_add = f'AUTO TEST add {date_time}'
currency_code_test_add = value_currency_code
secure_type_test_add = value_secure_type
secure_rate_test_add = value_secure_rate
secured_by_currency_test_add = value_secured_by_currency
credit_type_test_add = value_credit_type
credit_sub_type_test_add = value_credit_sub_type
tenor_type_test_add = value_tenor_type
credit_purpose_test_add = value_credit_purpose
credit_classification_test_add = value_credit_classification
credit_facility_test_add = value_credit_facility
disbursement_mode_test_add = value_disbursement_mode
is_provision_test_add = value_is_provision
classification_option_test_add = value_classification_option
status_test_add = value_status
principal_collection_tenor_test_add = value_principal_collection_tenor
principal_collection_tenor_unit_test_add = value_principal_collection_tenor_unit
principal_grace_period_test_add = value_principal_grace_period
principal_due_on_holiday_test_add = value_principal_due_on_holiday
interest_collection_tenor_test_add = value_interest_collection_tenor
interest_collection_tenor_unit_test_add = value_interest_collection_tenor_unit
interest_grace_period_test_add = value_interest_grace_period
interest_due_on_holiday_test_add = value_interest_due_on_holiday
fine_collection_tenor_test_add = value_fine_collection_tenor
fine_collection_tenor_unit_test_add = value_fine_collection_tenor_unit
fine_grace_period_test_add = value_fine_grace_period
fine_due_on_holiday_test_add = value_fine_due_on_holiday
standard_test_add = value_standard
watch_test_add = value_watch
substandard_test_add = value_substandard
doubtful_test_add = value_doubtful
loss_test_add = value_loss
ifc_codes_test_add = value_ifc_codes
sys_account_names_test_add = value_expected_gls_sys_account_names
account_aliass_test_add = value_expected_gls_account_aliass
coa_accounts_test_add = None
replace_bys_test_add = value_expected_extension_replace_bys
system_account_names_test_add = value_expected_extension_sys_account_names
business_lines_test_add = value_business_lines
customer_sectors_test_add = None
customer_resident_statuss_test_add = None
sub_products_test_add = None
bank_identifications_test_add = None
replace_code_test_add = None
email_test_add = value_email
push_notification_test_add = value_push_notification
sms_test_add = value_sms
list_error_message_test_add = value_list_error_message

# data test add verify
catalogue_code_test_add_verify = value_catalogue_code
catalogue_name_test_add_verify = catalogue_name_test_add
currency_code_test_add_verify = value_currency_code
secure_type_test_add_verify = value_secure_type
secure_rate_test_add_verify = value_secure_rate
secured_by_currency_test_add_verify = value_secured_by_currency
credit_type_test_add_verify = value_credit_type
credit_sub_type_test_add_verify = value_credit_sub_type
tenor_type_test_add_verify = value_tenor_type
credit_purpose_test_add_verify = value_credit_purpose
credit_classification_test_add_verify = value_credit_classification
credit_facility_test_add_verify = value_credit_facility
disbursement_mode_test_add_verify = value_disbursement_mode
is_provision_test_add_verify = value_is_provision
classification_option_test_add_verify = value_classification_option
status_test_add_verify = value_status
principal_collection_tenor_test_add_verify = value_principal_collection_tenor
principal_collection_tenor_unit_test_add_verify = value_principal_collection_tenor_unit
principal_grace_period_test_add_verify = value_principal_grace_period
principal_due_on_holiday_test_add_verify = value_principal_due_on_holiday
interest_collection_tenor_test_add_verify = value_interest_collection_tenor
interest_collection_tenor_unit_test_add_verify = value_interest_collection_tenor_unit
interest_grace_period_test_add_verify = value_interest_grace_period
interest_due_on_holiday_test_add_verify = value_interest_due_on_holiday
fine_collection_tenor_test_add_verify = value_fine_collection_tenor
fine_collection_tenor_unit_test_add_verify = value_fine_collection_tenor_unit
fine_grace_period_test_add_verify = value_fine_grace_period
fine_due_on_holiday_test_add_verify = value_fine_due_on_holiday
standard_test_add_verify = value_standard
watch_test_add_verify = value_watch
substandard_test_add_verify = value_substandard
doubtful_test_add_verify = value_doubtful
loss_test_add_verify = value_loss
expected_ifc_list_codes_test_add_verify = value_expected_ifc_list_codes
expected_ifc_names_test_add_verify = value_expected_ifc_names
expected_ifc_values_test_add_verify = value_expected_ifc_values
expected_ifc_types_test_add_verify = value_expected_ifc_types
expected_ifc_tenors_test_add_verify = value_expected_ifc_tenors
expected_ifc_tenor_units_test_add_verify = value_expected_ifc_tenor_units
expected_ifc_statuss_test_add_verify = value_expected_ifc_statuses
expected_gls_account_aliass_test_add_verify = value_expected_gls_account_aliass
expected_gls_sys_account_names_test_add_verify = value_expected_gls_sys_account_names
expected_extension_sys_account_names_test_add_verify = value_expected_extension_sys_account_names
expected_extension_conditions_test_add_verify = value_expected_extension_conditions_add
expected_extension_replace_bys_test_add_verify = value_expected_extension_replace_bys
email_test_add_verify = value_email
push_notification_test_add_verify = value_push_notification
sms_test_add_verify = value_sms

# data test view add
catalogue_code_test_view_add = value_catalogue_code
catalogue_name_test_view_add = catalogue_name_test_add
currency_code_test_view_add = value_currency_code
secure_type_test_view_add = value_secure_type
secure_rate_test_view_add = value_secure_rate
secured_by_currency_test_view_add = value_secured_by_currency
credit_type_test_view_add = value_credit_type
credit_sub_type_test_view_add = value_credit_sub_type
tenor_type_test_view_add = value_tenor_type
credit_purpose_test_view_add = value_credit_purpose
credit_classification_test_view_add = value_credit_classification
credit_facility_test_view_add = value_credit_facility
disbursement_mode_test_view_add = value_disbursement_mode
is_provision_test_view_add = value_is_provision
classification_option_test_view_add = value_classification_option
status_test_view_add = value_status
created_by_test_view_add = value_created_by
approved_by_test_view_add = value_approved_by
principal_collection_tenor_test_view_add = value_principal_collection_tenor
principal_collection_tenor_unit_test_view_add = value_principal_collection_tenor_unit
principal_grace_period_test_view_add = value_principal_grace_period
principal_due_on_holiday_test_view_add = value_principal_due_on_holiday
interest_collection_tenor_test_view_add = value_interest_collection_tenor
interest_collection_tenor_unit_test_view_add = value_interest_collection_tenor_unit
interest_grace_period_test_view_add = value_interest_grace_period
interest_due_on_holiday_test_view_add = value_interest_due_on_holiday
fine_collection_tenor_test_view_add = value_fine_collection_tenor
fine_collection_tenor_unit_test_view_add = value_fine_collection_tenor_unit
fine_grace_period_test_view_add = value_fine_grace_period
fine_due_on_holiday_test_view_add = value_fine_due_on_holiday
standard_test_view_add = value_standard
watch_test_view_add = value_watch
substandard_test_view_add = value_substandard
doubtful_test_view_add = value_doubtful
loss_test_view_add = value_loss
expected_ifc_list_codes_test_view_add = value_expected_ifc_list_codes
expected_ifc_names_test_view_add = value_expected_ifc_names
expected_ifc_values_test_view_add = value_expected_ifc_values
expected_ifc_types_test_view_add = value_expected_ifc_types
expected_ifc_tenors_test_view_add = value_expected_ifc_tenors
expected_ifc_tenor_units_test_view_add = value_expected_ifc_tenor_units
expected_ifc_statuss_test_view_add = value_expected_ifc_statuses
expected_gls_account_aliass_test_view_add = value_expected_gls_account_aliass
expected_gls_sys_account_names_test_view_add = value_expected_gls_sys_account_names
expected_extension_sys_account_names_test_view_add = value_expected_extension_sys_account_names
expected_extension_conditions_test_view_add = value_expected_extension_conditions_view
expected_extension_replace_bys_test_view_add = value_expected_extension_replace_bys
email_test_view_add = value_email
push_notification_test_view_add = value_push_notification
sms_test_view_add = value_sms

# data test update
catalogue_code_test_update = value_catalogue_code
catalogue_name_test_update = f'AUTO TEST update {date_time}'
currency_code_test_update = value_currency_code
secure_type_test_update = 'Full secured'
secure_rate_test_update = '100.00'
secured_by_currency_test_update = value_secured_by_currency
credit_type_test_update = value_credit_type
credit_sub_type_test_update = 'Agent Hub OD'
tenor_type_test_update = 'Short term'
credit_purpose_test_update = 'AGRICULTURAL'
credit_classification_test_update = 'CONSTRUCTION'
credit_facility_test_update = 'Over Draft'
disbursement_mode_test_update = value_disbursement_mode
is_provision_test_update = 'No'
classification_option_test_update = 'NPL manual'
status_test_update = 'Close'
created_by_test_update = value_created_by
approved_by_test_update = value_approved_by
principal_collection_tenor_test_update = '5'
principal_collection_tenor_unit_test_update = 'Year(s)'
principal_grace_period_test_update = '1'
principal_due_on_holiday_test_update = '2'
interest_collection_tenor_test_update = '3'
interest_collection_tenor_unit_test_update = 'Year(s)'
interest_grace_period_test_update = '4'
interest_due_on_holiday_test_update = '8'
fine_collection_tenor_test_update = '7'
fine_collection_tenor_unit_test_update = 'Year(s)'
fine_grace_period_test_update = '6'
fine_due_on_holiday_test_update = '9'
standard_test_update = '0.50'
watch_test_update = '6.00'
substandard_test_update = '26.00'
doubtful_test_update = '51.00'
loss_test_update = '99.99'
email_test_update = True
push_notification_test_update = False
sms_test_update = True
list_error_message_test_update = value_list_error_message

# data test update verify
catalogue_code_test_update_verify = value_catalogue_code
catalogue_name_test_update_verify = catalogue_name_test_update
currency_code_test_update_verify = value_currency_code
secure_type_test_update_verify = secure_type_test_update
secure_rate_test_update_verify = secure_rate_test_update
secured_by_currency_test_update_verify = value_secured_by_currency
credit_type_test_update_verify = value_credit_type
credit_sub_type_test_update_verify = credit_sub_type_test_update
tenor_type_test_update_verify = tenor_type_test_update
credit_purpose_test_update_verify = credit_purpose_test_update
credit_classification_test_update_verify = credit_classification_test_update
credit_facility_test_update_verify = credit_facility_test_update
disbursement_mode_test_update_verify = value_disbursement_mode
is_provision_test_update_verify = is_provision_test_update
classification_option_test_update_verify = classification_option_test_update
status_test_update_verify = status_test_update
created_by_test_update_verify = value_created_by
approved_by_test_update_verify = value_approved_by
principal_collection_tenor_test_update_verify = principal_collection_tenor_test_update
principal_collection_tenor_unit_test_update_verify = principal_collection_tenor_unit_test_update
principal_grace_period_test_update_verify = principal_grace_period_test_update
principal_due_on_holiday_test_update_verify = principal_due_on_holiday_test_update
interest_collection_tenor_test_update_verify = interest_collection_tenor_test_update
interest_collection_tenor_unit_test_update_verify = interest_collection_tenor_unit_test_update
interest_grace_period_test_update_verify = interest_grace_period_test_update
interest_due_on_holiday_test_update_verify = interest_due_on_holiday_test_update
fine_collection_tenor_test_update_verify = fine_collection_tenor_test_update
fine_collection_tenor_unit_test_update_verify = fine_collection_tenor_unit_test_update
fine_grace_period_test_update_verify = fine_grace_period_test_update
fine_due_on_holiday_test_update_verify = fine_due_on_holiday_test_update
standard_test_update_verify = standard_test_update
watch_test_update_verify = watch_test_update
substandard_test_update_verify = substandard_test_update
doubtful_test_update_verify = doubtful_test_update
loss_test_update_verify = loss_test_update
expected_ifc_list_codes_test_update_verify = value_expected_ifc_list_codes
expected_ifc_names_test_update_verify = value_expected_ifc_names
expected_ifc_values_test_update_verify = value_expected_ifc_values
expected_ifc_types_test_update_verify = value_expected_ifc_types
expected_ifc_tenors_test_update_verify = value_expected_ifc_tenors
expected_ifc_tenor_units_test_update_verify = value_expected_ifc_tenor_units
expected_ifc_statuss_test_update_verify = value_expected_ifc_statuses
expected_gls_account_aliass_test_update_verify = value_expected_gls_account_aliass
expected_gls_sys_account_names_test_update_verify = value_expected_gls_sys_account_names
expected_extension_sys_account_names_test_update_verify = value_expected_extension_sys_account_names
expected_extension_conditions_test_update_verify = value_expected_extension_conditions_view
expected_extension_replace_bys_test_update_verify = value_expected_extension_replace_bys
email_test_update_verify = email_test_update
push_notification_test_update_verify = push_notification_test_update
sms_test_update_verify = sms_test_update


# data test view update
catalogue_code_test_view_update = value_catalogue_code
catalogue_name_test_view_update = catalogue_name_test_update
currency_code_test_view_update = value_currency_code
secure_type_test_view_update = secure_type_test_update
secure_rate_test_view_update = secure_rate_test_update
secured_by_currency_test_view_update = value_secured_by_currency
credit_type_test_view_update = value_credit_type
credit_sub_type_test_view_update = credit_sub_type_test_update
tenor_type_test_view_update = tenor_type_test_update
credit_purpose_test_view_update = credit_purpose_test_update
credit_classification_test_view_update = credit_classification_test_update
credit_facility_test_view_update = credit_facility_test_update
disbursement_mode_test_view_update = value_disbursement_mode
is_provision_test_view_update = is_provision_test_update
classification_option_test_view_update = classification_option_test_update
status_test_view_update = status_test_update
created_by_test_view_update = value_created_by
approved_by_test_view_update = value_approved_by
principal_collection_tenor_test_view_update = principal_collection_tenor_test_update
principal_collection_tenor_unit_test_view_update = principal_collection_tenor_unit_test_update
principal_grace_period_test_view_update = principal_grace_period_test_update
principal_due_on_holiday_test_view_update = principal_due_on_holiday_test_update
interest_collection_tenor_test_view_update = interest_collection_tenor_test_update
interest_collection_tenor_unit_test_view_update = interest_collection_tenor_unit_test_update
interest_grace_period_test_view_update = interest_grace_period_test_update
interest_due_on_holiday_test_view_update = interest_due_on_holiday_test_update
fine_collection_tenor_test_view_update = fine_collection_tenor_test_update
fine_collection_tenor_unit_test_view_update = fine_collection_tenor_unit_test_update
fine_grace_period_test_view_update = fine_grace_period_test_update
fine_due_on_holiday_test_view_update = fine_due_on_holiday_test_update
standard_test_view_update = standard_test_update
watch_test_view_update = watch_test_update
substandard_test_view_update = substandard_test_update
doubtful_test_view_update = doubtful_test_update
loss_test_view_update = loss_test_update
expected_ifc_list_codes_test_view_update = value_expected_ifc_list_codes
expected_ifc_names_test_view_update = value_expected_ifc_names
expected_ifc_values_test_view_update = value_expected_ifc_values
expected_ifc_types_test_view_update = value_expected_ifc_types
expected_ifc_tenors_test_view_update = value_expected_ifc_tenors
expected_ifc_tenor_units_test_view_update = value_expected_ifc_tenor_units
expected_ifc_statuss_test_view_update = value_expected_ifc_statuses
expected_gls_account_aliass_test_view_update = value_expected_gls_account_aliass
expected_gls_sys_account_names_test_view_update = value_expected_gls_sys_account_names
expected_extension_sys_account_names_test_view_update = value_expected_extension_sys_account_names
expected_extension_conditions_test_view_update = value_expected_extension_conditions_view
expected_extension_replace_bys_test_view_update = value_expected_extension_replace_bys
email_test_view_update = email_test_update
push_notification_test_view_update = push_notification_test_update
sms_test_view_update = sms_test_update

class OverdraftCatalogueTest(FormAction):
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

# DPT-OD Catalogue Definition
    def test_001_od_cat_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.overdraft_catalogue_definition_add(
            catalogue_code=catalogue_code_test_add,
            catalogue_name=catalogue_name_test_add,
            currency_code=currency_code_test_add,
            secure_type=secure_type_test_add,
            secure_rate=secure_rate_test_add,
            secured_by_currency=secured_by_currency_test_add,
            credit_type=credit_type_test_add,
            credit_sub_type=credit_sub_type_test_add,
            tenor_type=tenor_type_test_add,
            credit_purpose=credit_purpose_test_add,
            credit_classification=credit_classification_test_add,
            credit_facility=credit_facility_test_add,
            disbursement_mode=disbursement_mode_test_add,
            is_provision=is_provision_test_add,
            classification_option=classification_option_test_add,
            status=status_test_add,
            principal_collection_tenor=principal_collection_tenor_test_add,
            principal_collection_tenor_unit=principal_collection_tenor_unit_test_add,
            principal_grace_period=principal_grace_period_test_add,
            principal_due_on_holiday=principal_due_on_holiday_test_add,
            interest_collection_tenor=interest_collection_tenor_test_add,
            interest_collection_tenor_unit=interest_collection_tenor_unit_test_add,
            interest_grace_period=interest_grace_period_test_add,
            interest_due_on_holiday=interest_due_on_holiday_test_add,
            fine_collection_tenor=fine_collection_tenor_test_add,
            fine_collection_tenor_unit=fine_collection_tenor_unit_test_add,
            fine_grace_period=fine_grace_period_test_add,
            fine_due_on_holiday=fine_due_on_holiday_test_add,
            standard=standard_test_add,
            watch=watch_test_add,
            substandard=substandard_test_add,
            doubtful=doubtful_test_add,
            loss=loss_test_add,
            ifc_codes=ifc_codes_test_add,
            sys_account_names=sys_account_names_test_add,
            account_aliass=account_aliass_test_add,
            coa_accounts=coa_accounts_test_add,
            replace_bys=replace_bys_test_add,
            system_account_names=system_account_names_test_add,
            business_lines=business_lines_test_add,
            customer_sectors=customer_sectors_test_add,
            customer_resident_statuss=customer_resident_statuss_test_add,
            sub_products=sub_products_test_add,
            bank_identifications=bank_identifications_test_add,
            replace_code=replace_code_test_add,
            email=email_test_add,
            push_notification=push_notification_test_add,
            sms=sms_test_add,
            list_error_message=list_error_message_test_add,

        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.overdraft_catalogue_definition_simple_search(catalogue_code_test_add)
        self.assert_search_not_found()

    def test_002_od_cat_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.overdraft_catalogue_definition_add_verify(
            transaction_number=transaction_number_add,
            catalogue_code=catalogue_code_test_add_verify,
            catalogue_name=catalogue_name_test_add_verify,
            currency_code=currency_code_test_add_verify,
            secure_type=secure_type_test_add_verify,
            secure_rate=secure_rate_test_add_verify,
            secured_by_currency=secured_by_currency_test_add_verify,
            credit_type=credit_type_test_add_verify,
            credit_sub_type=credit_sub_type_test_add_verify,
            tenor_type=tenor_type_test_add_verify,
            credit_purpose=credit_purpose_test_add_verify,
            credit_classification=credit_classification_test_add_verify,
            credit_facility=credit_facility_test_add_verify,
            disbursement_mode=disbursement_mode_test_add_verify,
            is_provision=is_provision_test_add_verify,
            classification_option=classification_option_test_add_verify,
            status=status_test_add_verify,
            principal_collection_tenor=principal_collection_tenor_test_add_verify,
            principal_collection_tenor_unit=principal_collection_tenor_unit_test_add_verify,
            principal_grace_period=principal_grace_period_test_add_verify,
            principal_due_on_holiday=principal_due_on_holiday_test_add_verify,
            interest_collection_tenor=interest_collection_tenor_test_add_verify,
            interest_collection_tenor_unit=interest_collection_tenor_unit_test_add_verify,
            interest_grace_period=interest_grace_period_test_add_verify,
            interest_due_on_holiday=interest_due_on_holiday_test_add_verify,
            fine_collection_tenor=fine_collection_tenor_test_add_verify,
            fine_collection_tenor_unit=fine_collection_tenor_unit_test_add_verify,
            fine_grace_period=fine_grace_period_test_add_verify,
            fine_due_on_holiday=fine_due_on_holiday_test_add_verify,
            standard=standard_test_add_verify,
            watch=watch_test_add_verify,
            substandard=substandard_test_add_verify,
            doubtful=doubtful_test_add_verify,
            loss=loss_test_add_verify,
            expected_ifc_list_codes=expected_ifc_list_codes_test_add_verify,
            expected_ifc_names=expected_ifc_names_test_add_verify,
            expected_ifc_values=expected_ifc_values_test_add_verify,
            expected_ifc_types=expected_ifc_types_test_add_verify,
            expected_ifc_tenors=expected_ifc_tenors_test_add_verify,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_add_verify,
            expected_ifc_statuss=expected_ifc_statuss_test_add_verify,
            expected_gls_account_aliass=expected_gls_account_aliass_test_add_verify,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_add_verify,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_add_verify,
            expected_extension_conditions=expected_extension_conditions_test_add_verify,
            expected_extension_replace_bys=expected_extension_replace_bys_test_add_verify,
            email=email_test_add_verify,
            push_notification=push_notification_test_add_verify,
            sms=sms_test_add_verify,
        )

    def test_003_od_cat_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.overdraft_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_add,
        )

    def test_004_od_cat_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.overdraft_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_add,
            catalogue_name=catalogue_name_test_view_add,
            currency_code=currency_code_test_view_add,
            secure_type=secure_type_test_view_add,
            secure_rate=secure_rate_test_view_add,
            secured_by_currency=secured_by_currency_test_view_add,
            credit_type=credit_type_test_view_add,
            credit_sub_type=credit_sub_type_test_view_add,
            tenor_type=tenor_type_test_view_add,
            credit_purpose=credit_purpose_test_view_add,
            credit_classification=credit_classification_test_view_add,
            credit_facility=credit_facility_test_view_add,
            disbursement_mode=disbursement_mode_test_view_add,
            is_provision=is_provision_test_view_add,
            classification_option=classification_option_test_view_add,
            status=status_test_view_add,
            created_by=created_by_test_view_add,
            approved_by=approved_by_test_view_add,
            principal_collection_tenor=principal_collection_tenor_test_view_add,
            principal_collection_tenor_unit=principal_collection_tenor_unit_test_view_add,
            principal_grace_period=principal_grace_period_test_view_add,
            principal_due_on_holiday=principal_due_on_holiday_test_view_add,
            interest_collection_tenor=interest_collection_tenor_test_view_add,
            interest_collection_tenor_unit=interest_collection_tenor_unit_test_view_add,
            interest_grace_period=interest_grace_period_test_view_add,
            interest_due_on_holiday=interest_due_on_holiday_test_view_add,
            fine_collection_tenor=fine_collection_tenor_test_view_add,
            fine_collection_tenor_unit=fine_collection_tenor_unit_test_view_add,
            fine_grace_period=fine_grace_period_test_view_add,
            fine_due_on_holiday=fine_due_on_holiday_test_view_add,
            standard=standard_test_view_add,
            watch=watch_test_view_add,
            substandard=substandard_test_view_add,
            doubtful=doubtful_test_view_add,
            loss=loss_test_view_add,
            expected_ifc_list_codes=expected_ifc_list_codes_test_view_add,
            expected_ifc_names=expected_ifc_names_test_view_add,
            expected_ifc_values=expected_ifc_values_test_view_add,
            expected_ifc_types=expected_ifc_types_test_view_add,
            expected_ifc_tenors=expected_ifc_tenors_test_view_add,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_view_add,
            expected_ifc_statuss=expected_ifc_statuss_test_view_add,
            expected_gls_account_aliass=expected_gls_account_aliass_test_view_add,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_view_add,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_view_add,
            expected_extension_conditions=expected_extension_conditions_test_view_add,
            expected_extension_replace_bys=expected_extension_replace_bys_test_view_add,
            email=email_test_view_add,
            push_notification=push_notification_test_view_add,
            sms=sms_test_view_add,
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

    def test_006_od_cat_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.overdraft_catalogue_definition_update(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
            currency_code=currency_code_test_update,
            secure_type=secure_type_test_update,
            secure_rate=secure_rate_test_update,
            secured_by_currency=secured_by_currency_test_update,
            credit_type=credit_type_test_update,
            credit_sub_type=credit_sub_type_test_update,
            tenor_type=tenor_type_test_update,
            credit_purpose=credit_purpose_test_update,
            credit_classification=credit_classification_test_update,
            credit_facility=credit_facility_test_update,
            disbursement_mode=disbursement_mode_test_update,
            is_provision=is_provision_test_update,
            classification_option=classification_option_test_update,
            status=status_test_update,
            created_by=created_by_test_update,
            approved_by=approved_by_test_update,
            principal_collection_tenor=principal_collection_tenor_test_update,
            principal_collection_tenor_unit=principal_collection_tenor_unit_test_update,
            principal_grace_period=principal_grace_period_test_update,
            principal_due_on_holiday=principal_due_on_holiday_test_update,
            interest_collection_tenor=interest_collection_tenor_test_update,
            interest_collection_tenor_unit=interest_collection_tenor_unit_test_update,
            interest_grace_period=interest_grace_period_test_update,
            interest_due_on_holiday=interest_due_on_holiday_test_update,
            fine_collection_tenor=fine_collection_tenor_test_update,
            fine_collection_tenor_unit=fine_collection_tenor_unit_test_update,
            fine_grace_period=fine_grace_period_test_update,
            fine_due_on_holiday=fine_due_on_holiday_test_update,
            standard=standard_test_update,
            watch=watch_test_update,
            substandard=substandard_test_update,
            doubtful=doubtful_test_update,
            loss=loss_test_update,
            email=email_test_update,
            push_notification=push_notification_test_update,
            sms=sms_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.overdraft_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_view_add,
        )

    def test_007_od_cat_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.overdraft_catalogue_definition_update_verify(
            transaction_number=transaction_number_update,
            catalogue_code=catalogue_code_test_update_verify,
            catalogue_name=catalogue_name_test_update_verify,
            currency_code=currency_code_test_update_verify,
            secure_type=secure_type_test_update_verify,
            secure_rate=secure_rate_test_update_verify,
            secured_by_currency=secured_by_currency_test_update_verify,
            credit_type=credit_type_test_update_verify,
            credit_sub_type=credit_sub_type_test_update_verify,
            tenor_type=tenor_type_test_update_verify,
            credit_purpose=credit_purpose_test_update_verify,
            credit_classification=credit_classification_test_update_verify,
            credit_facility=credit_facility_test_update_verify,
            disbursement_mode=disbursement_mode_test_update_verify,
            is_provision=is_provision_test_update_verify,
            classification_option=classification_option_test_update_verify,
            status=status_test_update_verify,
            created_by=created_by_test_update_verify,
            approved_by=approved_by_test_update_verify,
            principal_collection_tenor=principal_collection_tenor_test_update_verify,
            principal_collection_tenor_unit=principal_collection_tenor_unit_test_update_verify,
            principal_grace_period=principal_grace_period_test_update_verify,
            principal_due_on_holiday=principal_due_on_holiday_test_update_verify,
            interest_collection_tenor=interest_collection_tenor_test_update_verify,
            interest_collection_tenor_unit=interest_collection_tenor_unit_test_update_verify,
            interest_grace_period=interest_grace_period_test_update_verify,
            interest_due_on_holiday=interest_due_on_holiday_test_update_verify,
            fine_collection_tenor=fine_collection_tenor_test_update_verify,
            fine_collection_tenor_unit=fine_collection_tenor_unit_test_update_verify,
            fine_grace_period=fine_grace_period_test_update_verify,
            fine_due_on_holiday=fine_due_on_holiday_test_update_verify,
            standard=standard_test_update_verify,
            watch=watch_test_update_verify,
            substandard=substandard_test_update_verify,
            doubtful=doubtful_test_update_verify,
            loss=loss_test_update_verify,
            expected_ifc_list_codes=expected_ifc_list_codes_test_update_verify,
            expected_ifc_names=expected_ifc_names_test_update_verify,
            expected_ifc_values=expected_ifc_values_test_update_verify,
            expected_ifc_types=expected_ifc_types_test_update_verify,
            expected_ifc_tenors=expected_ifc_tenors_test_update_verify,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_update_verify,
            expected_ifc_statuss=expected_ifc_statuss_test_update_verify,
            expected_gls_account_aliass=expected_gls_account_aliass_test_update_verify,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_update_verify,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_update_verify,
            expected_extension_conditions=expected_extension_conditions_test_update_verify,
            expected_extension_replace_bys=expected_extension_replace_bys_test_update_verify,
            email=email_test_update_verify,
            push_notification=push_notification_test_update_verify,
            sms=sms_test_update_verify,
        )

    def test_008_od_cat_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.overdraft_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
        )

    def test_009_od_cat_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.overdraft_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_update,
            catalogue_name=catalogue_name_test_view_update,
            currency_code=currency_code_test_view_update,
            secure_type=secure_type_test_view_update,
            secure_rate=secure_rate_test_view_update,
            secured_by_currency=secured_by_currency_test_view_update,
            credit_type=credit_type_test_view_update,
            credit_sub_type=credit_sub_type_test_view_update,
            tenor_type=tenor_type_test_view_update,
            credit_purpose=credit_purpose_test_view_update,
            credit_classification=credit_classification_test_view_update,
            credit_facility=credit_facility_test_view_update,
            disbursement_mode=disbursement_mode_test_view_update,
            is_provision=is_provision_test_view_update,
            classification_option=classification_option_test_view_update,
            status=status_test_view_update,
            created_by=created_by_test_view_update,
            approved_by=approved_by_test_view_update,
            principal_collection_tenor=principal_collection_tenor_test_view_update,
            principal_collection_tenor_unit=principal_collection_tenor_unit_test_view_update,
            principal_grace_period=principal_grace_period_test_view_update,
            principal_due_on_holiday=principal_due_on_holiday_test_view_update,
            interest_collection_tenor=interest_collection_tenor_test_view_update,
            interest_collection_tenor_unit=interest_collection_tenor_unit_test_view_update,
            interest_grace_period=interest_grace_period_test_view_update,
            interest_due_on_holiday=interest_due_on_holiday_test_view_update,
            fine_collection_tenor=fine_collection_tenor_test_view_update,
            fine_collection_tenor_unit=fine_collection_tenor_unit_test_view_update,
            fine_grace_period=fine_grace_period_test_view_update,
            fine_due_on_holiday=fine_due_on_holiday_test_view_update,
            standard=standard_test_view_update,
            watch=watch_test_view_update,
            substandard=substandard_test_view_update,
            doubtful=doubtful_test_view_update,
            loss=loss_test_view_update,
            expected_ifc_list_codes=expected_ifc_list_codes_test_view_update,
            expected_ifc_names=expected_ifc_names_test_view_update,
            expected_ifc_values=expected_ifc_values_test_view_update,
            expected_ifc_types=expected_ifc_types_test_view_update,
            expected_ifc_tenors=expected_ifc_tenors_test_view_update,
            expected_ifc_tenor_units=expected_ifc_tenor_units_test_view_update,
            expected_ifc_statuss=expected_ifc_statuss_test_view_update,
            expected_gls_account_aliass=expected_gls_account_aliass_test_view_update,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_view_update,
            expected_extension_sys_account_names=expected_extension_sys_account_names_test_view_update,
            expected_extension_conditions=expected_extension_conditions_test_view_update,
            expected_extension_replace_bys=expected_extension_replace_bys_test_view_update,
            email=email_test_view_update,
            push_notification=push_notification_test_view_update,
            sms=sms_test_view_update,
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

    def test_010_od_cat_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.overdraft_catalogue_definition_delete(
            catalogue_code=value_catalogue_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.overdraft_catalogue_definition_search_verify(
            catalogue_code=value_catalogue_code,
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_catalogue_code,
            tran_name=tran_name_delete,
        )

    def test_011_od_cat_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.overdraft_catalogue_definition_simple_search(value_catalogue_code)
        self.assert_search_not_found()

    def test_012_od_cat_delete_item_in_use_01_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.overdraft_catalogue_definition_delete(
            catalogue_code= catalogue_code_in_use,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.overdraft_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_in_use,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=catalogue_code_in_use,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=catalogue_code_in_use,
            tran_name=tran_name_delete,
            list_error_message=list_error_message_in_use,
        )

    def test_012_od_cat_delete_item_in_use_02_reject(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # reject delete
        self.bo_approval_reject(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=catalogue_code_in_use,
            tran_name=tran_name_delete,
        )
        # search master
        self.overdraft_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_in_use,
        )

if __name__ == '__main__': 
    webui_test.main()