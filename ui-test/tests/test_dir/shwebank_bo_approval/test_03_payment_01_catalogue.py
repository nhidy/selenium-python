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

action_add ='PMT-Catalogue Definition-Add'
action_update ='PMT-Catalogue Definition-Update'
catalogue_code_in_use = '55010101'
# list_error_message_in_use = [f'Payment Product code [{catalogue_code_in_use}] have been used, can not delete !!!']
list_error_message_in_use = ['ERROR: An unexpected system error has occurred. Please contact support or check the system logs for more information.']
tran_name_delete = 'PMT_DELETE_PMTCAT'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_catalogue_code = 'AUTO0001'
value_output_format = 'DOMESTIC'
value_direction = 'Outward'
value_instrument = 'Telegraphic tranfer'
value_purpose = 'Others service'
value_holding_days = '0'
value_status = 'Normal'
value_created_by = USERNAME_LOGIN
value_approved_by = USERNAME_APPROVE
value_message_type = 'MT103'
value_export_swift = 'No'
value_send_by_email = 'No'
value_group_code = '103-MT103'

# value_ifc_codes = ['371', '372', '373']
# value_expected_ifc_list_codes =  ['371', '372', '373']
# value_expected_ifc_names = ['CHL1 - Consumer Home Loan - Main Interest', 'CHL1 - Consumer Home Loan - Penalty Principle', 'CHL1 - Consumer Home Loan - Penalty Interest']
# value_expected_ifc_values = ['10.00000', '14.50000', '14.50000']
# value_expected_ifc_types = ['Interest', 'Fee', 'Fee']
# value_expected_ifc_tenors = ['1', '1', '1']
# value_expected_ifc_tenor_units = ['Year(s)', 'Year(s)', 'Year(s)']
# value_expected_ifc_statuses = ['Normal', 'Normal', 'Normal']
# value_expected_gls_account_aliass = ['###{REF}**', '###{REF}**', '###{REF}**', '###{REF}**', '###{REF}**']
# value_expected_gls_sys_account_names = ['CREDIT0', 'CREDIT1', 'CREDIT2', 'CREDIT3', 'CREDIT4']
# value_expected_extension_sys_account_names = ['CREDIT0', 'CREDIT1', 'CREDIT2', 'CREDIT3', 'CREDIT4', 'CREDIT0', 'CREDIT1', 'CREDIT2', 'CREDIT3', 'CREDIT4']
# value_expected_extension_replace_bys = ['1030102020101', '1030103020202', '1030103020202', '1030103020202', '1030103020202', '1030102020101', '1030102020101', '1030102020101', '1030102020101', '1030102020101']
# value_business_lines = ['Personal', 'Personal', 'Personal', 'Personal', 'Personal', 'Corporate', 'Corporate', 'Corporate', 'Corporate', 'Corporate']
# value_expected_extension_conditions_add = ['{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C1","subproduct":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}',
#     '{"sector":"-","resident_status":"-","categories":"C3","subproduct":"-"}']

# value_expected_extension_conditions_view = ['{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C1","subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}',
#     '{"sector":null,"resident_status":null,"categories":"C3","subproduct":null}']

# data test add
catalogue_code_test_add = value_catalogue_code
catalogue_name_test_add = f'AUTO TEST add {date_time}'
output_format_test_add = value_output_format
direction_test_add = value_direction
instrument_test_add = value_instrument
purpose_test_add = value_purpose
holding_days_test_add = value_holding_days
status_test_add = value_status
message_type_test_add = value_message_type
export_swift_test_add = value_export_swift
send_by_email_test_add = value_send_by_email
group_code_test_add = value_group_code
list_error_message_test_add = None

# data test add verify
catalogue_code_test_add_verify = value_catalogue_code
catalogue_name_test_add_verify = catalogue_name_test_add
output_format_test_add_verify = value_output_format
direction_test_add_verify = value_direction
instrument_test_add_verify = value_instrument
purpose_test_add_verify = value_purpose
holding_days_test_add_verify = value_holding_days
status_test_add_verify = value_status
message_type_test_add_verify = value_message_type
export_swift_test_add_verify = value_export_swift
send_by_email_test_add_verify = value_send_by_email
group_code_test_add_verify = value_group_code

# data test view add
catalogue_code_test_view_add = value_catalogue_code
catalogue_name_test_view_add = catalogue_name_test_add
output_format_test_view_add = value_output_format
direction_test_view_add = value_direction
instrument_test_view_add = value_instrument
purpose_test_view_add = value_purpose
holding_days_test_view_add = value_holding_days
status_test_view_add = value_status
created_by_test_view_add = value_created_by
approved_by_test_view_add = value_approved_by
message_type_test_view_add = value_message_type
export_swift_test_view_add = value_export_swift
send_by_email_test_view_add = value_send_by_email
group_code_test_view_add = value_group_code

# data test update
catalogue_code_test_update = value_catalogue_code
catalogue_name_test_update = f'AUTO TEST update {date_time}'
output_format_test_update = value_output_format
direction_test_update = value_direction
instrument_test_update = value_instrument
purpose_test_update = value_purpose
holding_days_test_update = value_holding_days
status_test_update = value_status
created_by_test_update = value_created_by
approved_by_test_update = value_approved_by
message_type_test_update = value_message_type
export_swift_test_update = value_export_swift
send_by_email_test_update = value_send_by_email
group_code_test_update = value_group_code
list_error_message_test_update = None

# data test update verify
catalogue_code_test_update_verify = value_catalogue_code
catalogue_name_test_update_verify = catalogue_name_test_update
output_format_test_update_verify = value_output_format
direction_test_update_verify = value_direction
instrument_test_update_verify = value_instrument
purpose_test_update_verify = value_purpose
holding_days_test_update_verify = value_holding_days
status_test_update_verify = value_status
created_by_test_update_verify = value_created_by
approved_by_test_update_verify = value_approved_by
message_type_test_update_verify = value_message_type
export_swift_test_update_verify = value_export_swift
send_by_email_test_update_verify = value_send_by_email
group_code_test_update_verify = value_group_code

# data test view update
catalogue_code_test_view_update = value_catalogue_code
catalogue_name_test_view_update = catalogue_name_test_update
output_format_test_view_update = value_output_format
direction_test_view_update = value_direction
instrument_test_view_update = value_instrument
purpose_test_view_update = value_purpose
holding_days_test_view_update = value_holding_days
status_test_view_update = value_status
created_by_test_view_update = value_created_by
approved_by_test_view_update = value_approved_by
message_type_test_view_update = value_message_type
export_swift_test_view_update = value_export_swift
send_by_email_test_view_update = value_send_by_email
group_code_test_view_update = value_group_code

class PaymentCatalogueTest(FormAction):
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

# PMT-Catalogue Definition
    def test_001_pmt_cat_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.payment_catalogue_definition_add(
            catalogue_code=catalogue_code_test_add,
            catalogue_name=catalogue_name_test_add,
            output_format=output_format_test_add,
            direction=direction_test_add,
            instrument=instrument_test_add,
            purpose=purpose_test_add,
            holding_days=holding_days_test_add,
            status=status_test_add,
            message_type=message_type_test_add,
            export_swift=export_swift_test_add,
            send_by_email=send_by_email_test_add,
            group_code=group_code_test_add,
            list_error_message=list_error_message_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.payment_catalogue_definition_simple_search(catalogue_code_test_add)
        self.assert_search_not_found()

    def test_002_pmt_cat_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.payment_catalogue_definition_add_verify(
            transaction_number=transaction_number_add,
            catalogue_code=catalogue_code_test_add_verify,
            catalogue_name=catalogue_name_test_add_verify,
            output_format=output_format_test_add_verify,
            direction=direction_test_add_verify,
            instrument=instrument_test_add_verify,
            purpose=purpose_test_add_verify,
            holding_days=holding_days_test_add_verify,
            status=status_test_add_verify,
            message_type=message_type_test_add_verify,
            export_swift=export_swift_test_add_verify,
            send_by_email=send_by_email_test_add_verify,
            group_code=group_code_test_add_verify,
        )

    def test_003_pmt_cat_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # search and verify master
        self.payment_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_add,
        )

    def test_004_pmt_cat_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_add,
            catalogue_name=catalogue_name_test_view_add,
            output_format=output_format_test_view_add,
            direction=direction_test_view_add,
            instrument=instrument_test_view_add,
            purpose=purpose_test_view_add,
            holding_days=holding_days_test_view_add,
            status=status_test_view_add,
            created_by=created_by_test_view_add,
            approved_by=approved_by_test_view_add,
            message_type=message_type_test_view_add,
            export_swift=export_swift_test_view_add,
            send_by_email=send_by_email_test_view_add,
            group_code=group_code_test_view_add,
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

    def test_006_pmt_cat_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.payment_catalogue_definition_update(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
            output_format=output_format_test_update,
            direction=direction_test_update,
            instrument=instrument_test_update,
            purpose=purpose_test_update,
            holding_days=holding_days_test_update,
            status=status_test_update,
            created_by=created_by_test_update,
            approved_by=approved_by_test_update,
            message_type=message_type_test_update,
            export_swift=export_swift_test_update,
            send_by_email=send_by_email_test_update,
            group_code=group_code_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.payment_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_view_add,
        )

    def test_007_pmt_cat_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.payment_catalogue_definition_update_verify(
            transaction_number=transaction_number_update,
            catalogue_code=catalogue_code_test_update_verify,
            catalogue_name=catalogue_name_test_update_verify,
            output_format=output_format_test_update_verify,
            direction=direction_test_update_verify,
            instrument=instrument_test_update_verify,
            purpose=purpose_test_update_verify,
            holding_days=holding_days_test_update_verify,
            status=status_test_update_verify,
            created_by=created_by_test_update_verify,
            approved_by=approved_by_test_update_verify,
            message_type=message_type_test_update_verify,
            export_swift=export_swift_test_update_verify,
            send_by_email=send_by_email_test_update_verify,
            group_code=group_code_test_update_verify,
        )

    def test_008_pmt_cat_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.payment_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_test_update,
            catalogue_name=catalogue_name_test_update,
        )

    def test_009_pmt_cat_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_catalogue_definition_view(
            catalogue_code=catalogue_code_test_view_update,
            catalogue_name=catalogue_name_test_view_update,
            output_format=output_format_test_view_update,
            direction=direction_test_view_update,
            instrument=instrument_test_view_update,
            purpose=purpose_test_view_update,
            holding_days=holding_days_test_view_update,
            status=status_test_view_update,
            created_by=created_by_test_view_update,
            approved_by=approved_by_test_view_update,
            message_type=message_type_test_view_update,
            export_swift=export_swift_test_view_update,
            send_by_email=send_by_email_test_view_update,
            group_code=group_code_test_view_update,
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

    def test_010_pmt_cat_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_catalogue_definition_delete(
            catalogue_code=value_catalogue_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.payment_catalogue_definition_search_verify(
            catalogue_code=value_catalogue_code,
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_catalogue_code,
            tran_name=tran_name_delete,
        )

    def test_011_pmt_cat_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_catalogue_definition_simple_search(value_catalogue_code)
        self.assert_search_not_found()

    def test_012_pmt_cat_delete_item_in_use_01_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.payment_catalogue_definition_delete(
            catalogue_code= catalogue_code_in_use,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.payment_catalogue_definition_search_verify(
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

    def test_012_pmt_cat_delete_item_in_use_02_reject(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # reject delete
        self.bo_approval_reject(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=catalogue_code_in_use,
            tran_name=tran_name_delete,
        )
        # search master
        self.payment_catalogue_definition_search_verify(
            catalogue_code=catalogue_code_in_use,
        )

if __name__ == '__main__': 
    webui_test.main()