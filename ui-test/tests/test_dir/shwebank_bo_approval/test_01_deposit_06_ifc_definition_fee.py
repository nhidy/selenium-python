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

action_add ='DPT-IFC Item Definition-Add'
action_update ='DPT-IFC Item Definition-Update'
tran_name_delete = 'DPT_IFC_DELETE_IFC'
expected_actions_delete = ['Reject', 'Approve', 'Copy execution_id']

# data not change
value_ifc_type = 'Fee'
value_ifc_sub_type = 'OD Commitment Fee'
value_val_base = 'Based on Account'
value_is_linked = 'No'
value_value = '1.00000'
value_ifc_linkage = ''
value_ifc_operator = '+'
value_margin_value = '0.00000'
value_value_type = 'Percentage'
value_currency_code = 'MMK'
value_floor_value = '100.00000'
value_ceiling_value = '200,000.00000'
value_value_basis = 'dbo.GetUnUseBalance(AccountNumber)'
value_tenor = '0'
value_tenor_unit = 'Day(s)'
value_active_condition = 'dbo.GetUnUseBalance(AccountNumber) > 0 AND (CAST(WorkingDate AS DATE) <= CAST(ToDate AS DATE))'
value_rounding_rule = 'Round'
value_rounding_basis = 'Private basis'
value_rounding_num = '5'
value_share_fee = 'No'
value_ifc_status = 'Normal'
value_created_by = USERNAME_LOGIN
value_approved_by = USERNAME_APPROVE
value_effect_date = '20/09/2020'
value_effect_value = ''
value_expected_gls_sys_account_names = ['COMMITMENT_FEE0', 'COMMITMENT_FEE1', 'PAID_COMMITMENT_FEE0', 'PAID_COMMITMENT_FEE_S']
value_expected_gls_account_aliass = ['###1100204010101**', '###1100204010101**', '###3030101000101**', '###3030101000101**']
value_list_transaction = None

# data test add
ifc_code_test_add = None
ifc_name_test_add = f'AUTO TEST add {date_time}'
ifc_type_test_add = value_ifc_type
ifc_sub_type_test_add = value_ifc_sub_type
val_base_test_add = value_val_base
is_linked_test_add = value_is_linked
value_test_add = value_value
ifc_linkage_test_add = None
ifc_operator_test_add = value_ifc_operator
margin_value_test_add = None
value_type_test_add = value_value_type
currency_code_test_add = value_currency_code
floor_value_test_add = value_floor_value
ceiling_value_test_add = value_ceiling_value
value_basis_test_add = value_value_basis
tenor_test_add = None
tenor_unit_test_add = None
active_condition_test_add = value_active_condition
rounding_rule_test_add = value_rounding_rule
rounding_basis_test_add = value_rounding_basis
rounding_num_test_add = value_rounding_num
share_fee_test_add = value_share_fee
ifc_status_test_add = value_ifc_status
effect_date_test_add = value_effect_date
effect_value_test_add = value_effect_value
expected_gls_sys_account_names_test_add = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_add = value_expected_gls_account_aliass
list_transaction_test_add = value_list_transaction

# data test add verify
ifc_code_test_add_verify = ifc_code_test_add
ifc_name_test_add_verify = ifc_name_test_add
ifc_type_test_add_verify = value_ifc_type
ifc_sub_type_test_add_verify = value_ifc_sub_type
val_base_test_add_verify = value_val_base
is_linked_test_add_verify = value_is_linked
value_test_add_verify = value_value
ifc_linkage_test_add_verify = value_ifc_linkage
ifc_operator_test_add_verify = value_ifc_operator
margin_value_test_add_verify = value_margin_value
value_type_test_add_verify = value_value_type
currency_code_test_add_verify = value_currency_code
floor_value_test_add_verify = value_floor_value
ceiling_value_test_add_verify = value_ceiling_value
value_basis_test_add_verify = value_value_basis
tenor_test_add_verify = value_tenor
tenor_unit_test_add_verify = value_tenor_unit
active_condition_test_add_verify = value_active_condition
rounding_rule_test_add_verify = value_rounding_rule
rounding_basis_test_add_verify = value_rounding_basis
rounding_num_test_add_verify = value_rounding_num
share_fee_test_add_verify = value_share_fee
ifc_status_test_add_verify = value_ifc_status
effect_date_test_add_verify = value_effect_date
effect_value_test_add_verify = value_effect_value
expected_gls_sys_account_names_test_add_verify = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_add_verify = value_expected_gls_account_aliass
list_transaction_test_add_verify = value_list_transaction

# data test view add
ifc_name_test_view_add = ifc_name_test_add
ifc_type_test_view_add = value_ifc_type
ifc_sub_type_test_view_add = value_ifc_sub_type
val_base_test_view_add = value_val_base
is_linked_test_view_add = value_is_linked
value_test_view_add = value_value
ifc_linkage_test_view_add = value_ifc_linkage
ifc_operator_test_view_add = value_ifc_operator
margin_value_test_view_add = value_margin_value
value_type_test_view_add = value_value_type
currency_code_test_view_add = value_currency_code
floor_value_test_view_add = value_floor_value
ceiling_value_test_view_add = value_ceiling_value
value_basis_test_view_add = value_value_basis
tenor_test_view_add = value_tenor
tenor_unit_test_view_add = value_tenor_unit
active_condition_test_view_add = value_active_condition
rounding_rule_test_view_add = value_rounding_rule
rounding_basis_test_view_add = value_rounding_basis
rounding_num_test_view_add = value_rounding_num
share_fee_test_view_add = value_share_fee
ifc_status_test_view_add = value_ifc_status
created_by_test_view_add = value_created_by
approved_by_test_view_add = value_approved_by
effect_date_test_view_add = value_effect_date
effect_value_test_view_add = value_effect_value
expected_gls_sys_account_names_test_view_add = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_view_add = value_expected_gls_account_aliass
list_transaction_test_view_add = value_list_transaction

# data test update
ifc_name_test_update = f'AUTO TEST update {date_time}'
ifc_type_test_update = None
ifc_sub_type_test_update = value_ifc_sub_type
val_base_test_update = 'Based on IFC Items'
is_linked_test_update = value_is_linked
value_test_update = '9.07000'
ifc_linkage_test_update = value_ifc_linkage
ifc_operator_test_update = value_ifc_operator
margin_value_test_update = None
value_type_test_update = None
currency_code_test_update = 'USD'
floor_value_test_update = '200.00000'
ceiling_value_test_update = '150,000.00000'
value_basis_test_update = value_value_basis
tenor_test_update = None
tenor_unit_test_update = None
active_condition_test_update = value_active_condition
rounding_rule_test_update = value_rounding_rule
rounding_basis_test_update = value_rounding_basis
rounding_num_test_update = value_rounding_num
share_fee_test_update = value_share_fee
ifc_status_test_update = 'Closed'
created_by_test_update = None
approved_by_test_update = None
effect_date_test_update = value_effect_date
effect_value_test_update = value_effect_value
list_transaction_test_update = value_list_transaction
list_error_message_test_update = None

# data test update verify
ifc_name_test_update_verify = ifc_name_test_update
ifc_type_test_update_verify = value_ifc_type
ifc_sub_type_test_update_verify = value_ifc_sub_type
val_base_test_update_verify = val_base_test_update
is_linked_test_update_verify = value_is_linked
value_test_update_verify = value_test_update
ifc_linkage_test_update_verify = value_ifc_linkage
ifc_operator_test_update_verify = value_ifc_operator
margin_value_test_update_verify = value_margin_value
value_type_test_update_verify = value_value_type
currency_code_test_update_verify = currency_code_test_update
floor_value_test_update_verify = floor_value_test_update
ceiling_value_test_update_verify = ceiling_value_test_update
value_basis_test_update_verify = value_value_basis
tenor_test_update_verify = value_tenor
tenor_unit_test_update_verify = value_tenor_unit
active_condition_test_update_verify = value_active_condition
rounding_rule_test_update_verify = value_rounding_rule
rounding_basis_test_update_verify = value_rounding_basis
rounding_num_test_update_verify = value_rounding_num
share_fee_test_update_verify = value_share_fee
ifc_status_test_update_verify = ifc_status_test_update
created_by_test_update_verify = value_created_by
approved_by_test_update_verify = value_approved_by
effect_date_test_update_verify = value_effect_date
effect_value_test_update_verify = value_effect_value
expected_gls_sys_account_names_test_update_verify = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_update_verify = value_expected_gls_account_aliass
list_transaction_test_update_verify = value_list_transaction

# data test view update
ifc_name_test_view_update = ifc_name_test_update
ifc_type_test_view_update = value_ifc_type
ifc_sub_type_test_view_update = value_ifc_sub_type
val_base_test_view_update = val_base_test_update
is_linked_test_view_update = value_is_linked
value_test_view_update = value_test_update
ifc_linkage_test_view_update = value_ifc_linkage
ifc_operator_test_view_update = value_ifc_operator
margin_value_test_view_update = value_margin_value
value_type_test_view_update = value_value_type
currency_code_test_view_update = currency_code_test_update
floor_value_test_view_update = floor_value_test_update
ceiling_value_test_view_update = ceiling_value_test_update
value_basis_test_view_update = value_value_basis
tenor_test_view_update = value_tenor
tenor_unit_test_view_update = value_tenor_unit
active_condition_test_view_update = value_active_condition
rounding_rule_test_view_update = value_rounding_rule
rounding_basis_test_view_update = value_rounding_basis
rounding_num_test_view_update = value_rounding_num
share_fee_test_view_update = value_share_fee
ifc_status_test_view_update = ifc_status_test_update
created_by_test_view_update = value_created_by
approved_by_test_view_update = value_approved_by
effect_date_test_view_update = value_effect_date
effect_value_test_view_update = value_effect_value
expected_gls_sys_account_names_test_view_update = value_expected_gls_sys_account_names
expected_gls_account_aliass_test_view_update = value_expected_gls_account_aliass
list_transaction_test_view_update = value_list_transaction

class DepositIFCItemDefinitionFeeTest(FormAction):
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

# DPT-IFC Item Definition
    def test_001_dpt_ifc_definition_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_add
        self.deposit_ifc_item_definition_add(
            ifc_code=ifc_code_test_add,
            ifc_name=ifc_name_test_add,
            ifc_type=ifc_type_test_add,
            ifc_sub_type=ifc_sub_type_test_add,
            val_base=val_base_test_add,
            is_linked=is_linked_test_add,
            value=value_test_add,
            ifc_linkage=ifc_linkage_test_add,
            ifc_operator=ifc_operator_test_add,
            margin_value=margin_value_test_add,
            value_type=value_type_test_add,
            currency_code=currency_code_test_add,
            floor_value=floor_value_test_add,
            ceiling_value=ceiling_value_test_add,
            value_basis=value_basis_test_add,
            tenor=tenor_test_add,
            tenor_unit=tenor_unit_test_add,
            active_condition=active_condition_test_add,
            rounding_rule=rounding_rule_test_add,
            rounding_basis=rounding_basis_test_add,
            rounding_num=rounding_num_test_add,
            share_fee=share_fee_test_add,
            ifc_status=ifc_status_test_add,
            effect_date=effect_date_test_add,
            effect_value=effect_value_test_add,
            sys_account_names=expected_gls_sys_account_names_test_add,
            account_aliass=expected_gls_account_aliass_test_add,
            list_transaction=list_transaction_test_add,
        )
        transaction_number_add=self.get_transaction_number()
        # search master
        self.deposit_ifc_item_definition_simple_search(ifc_name_test_add)
        self.assert_search_not_found()

    def test_002_dpt_ifc_definition_add_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data add
        self.deposit_ifc_item_definition_add_verify(
            transaction_number=transaction_number_add,
            ifc_code=ifc_code_test_add_verify,
            ifc_name=ifc_name_test_add_verify,
            ifc_type=ifc_type_test_add_verify,
            ifc_sub_type=ifc_sub_type_test_add_verify,
            val_base=val_base_test_add_verify,
            is_linked=is_linked_test_add_verify,
            value=value_test_add_verify,
            ifc_linkage=ifc_linkage_test_add_verify,
            ifc_operator=ifc_operator_test_add_verify,
            margin_value=margin_value_test_add_verify,
            value_type=value_type_test_add_verify,
            currency_code=currency_code_test_add_verify,
            floor_value=floor_value_test_add_verify,
            ceiling_value=ceiling_value_test_add_verify,
            value_basis=value_basis_test_add_verify,
            tenor=tenor_test_add_verify,
            tenor_unit=tenor_unit_test_add_verify,
            active_condition=active_condition_test_add_verify,
            rounding_rule=rounding_rule_test_add_verify,
            rounding_basis=rounding_basis_test_add_verify,
            rounding_num=rounding_num_test_add_verify,
            share_fee=share_fee_test_add_verify,
            ifc_status=ifc_status_test_add_verify,
            effect_date=effect_date_test_add_verify,
            effect_value=effect_value_test_add_verify,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_add_verify,
            expected_gls_account_aliass=expected_gls_account_aliass_test_add_verify,
            list_transaction=list_transaction_test_add_verify,
        )

    def test_003_dpt_ifc_definition_add_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global value_ifc_code
        # approve data add
        self.bo_approval_approve(
            transaction_number=transaction_number_add,
            username=username_approve,
            password=password_approve,
        )
        # get ifc code
        value_ifc_code = self.deposit_get_ifc_code(ifc_name_test_add)
        # search and verify master
        self.deposit_ifc_item_definition_search_verify(
            ifc_code=value_ifc_code,
            ifc_name=ifc_name_test_add,
        )

    def test_004_dpt_ifc_definition_view_after_add(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_ifc_item_definition_view(
            ifc_code=value_ifc_code,
            ifc_name=ifc_name_test_view_add,
            ifc_type=ifc_type_test_view_add,
            ifc_sub_type=ifc_sub_type_test_view_add,
            val_base=val_base_test_view_add,
            is_linked=is_linked_test_view_add,
            value=value_test_view_add,
            ifc_linkage=ifc_linkage_test_view_add,
            ifc_operator=ifc_operator_test_view_add,
            margin_value=margin_value_test_view_add,
            value_type=value_type_test_view_add,
            currency_code=currency_code_test_view_add,
            floor_value=floor_value_test_view_add,
            ceiling_value=ceiling_value_test_view_add,
            value_basis=value_basis_test_view_add,
            tenor=tenor_test_view_add,
            tenor_unit=tenor_unit_test_view_add,
            active_condition=active_condition_test_view_add,
            rounding_rule=rounding_rule_test_view_add,
            rounding_basis=rounding_basis_test_view_add,
            rounding_num=rounding_num_test_view_add,
            share_fee=share_fee_test_view_add,
            ifc_status=ifc_status_test_view_add,
            created_by=created_by_test_view_add,
            approved_by=approved_by_test_view_add,
            effect_date=effect_date_test_view_add,
            effect_value=effect_value_test_view_add,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_view_add,
            expected_gls_account_aliass=expected_gls_account_aliass_test_view_add,
            list_transaction=list_transaction_test_view_add,
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

    def test_006_dpt_ifc_definition_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        global transaction_number_update
        self.deposit_ifc_item_definition_update(
            ifc_code=value_ifc_code,
            ifc_name=ifc_name_test_update,
            ifc_type=ifc_type_test_update,
            ifc_sub_type=ifc_sub_type_test_update,
            val_base=val_base_test_update,
            is_linked=is_linked_test_update,
            value=value_test_update,
            ifc_linkage=ifc_linkage_test_update,
            ifc_operator=ifc_operator_test_update,
            margin_value=margin_value_test_update,
            value_type=value_type_test_update,
            currency_code=currency_code_test_update,
            floor_value=floor_value_test_update,
            ceiling_value=ceiling_value_test_update,
            value_basis=value_basis_test_update,
            tenor=tenor_test_update,
            tenor_unit=tenor_unit_test_update,
            active_condition=active_condition_test_update,
            rounding_rule=rounding_rule_test_update,
            rounding_basis=rounding_basis_test_update,
            rounding_num=rounding_num_test_update,
            share_fee=share_fee_test_update,
            ifc_status=ifc_status_test_update,
            created_by=created_by_test_update,
            approved_by=approved_by_test_update,
            effect_date=effect_date_test_update,
            effect_value=effect_value_test_update,
            list_transaction=list_transaction_test_update,
            list_error_message=list_error_message_test_update,
        )
        transaction_number_update=self.get_transaction_number()
        # search master
        self.deposit_ifc_item_definition_search_verify(
            ifc_code=value_ifc_code,
            ifc_name=ifc_name_test_view_add,
        )

    def test_007_dpt_ifc_definition_update_verify(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # verify data update
        self.deposit_ifc_item_definition_update_verify(
            transaction_number=transaction_number_update,
            ifc_code=value_ifc_code,
            ifc_name=ifc_name_test_update_verify,
            ifc_type=ifc_type_test_update_verify,
            ifc_sub_type=ifc_sub_type_test_update_verify,
            val_base=val_base_test_update_verify,
            is_linked=is_linked_test_update_verify,
            value=value_test_update_verify,
            ifc_linkage=ifc_linkage_test_update_verify,
            ifc_operator=ifc_operator_test_update_verify,
            margin_value=margin_value_test_update_verify,
            value_type=value_type_test_update_verify,
            currency_code=currency_code_test_update_verify,
            floor_value=floor_value_test_update_verify,
            ceiling_value=ceiling_value_test_update_verify,
            value_basis=value_basis_test_update_verify,
            tenor=tenor_test_update_verify,
            tenor_unit=tenor_unit_test_update_verify,
            active_condition=active_condition_test_update_verify,
            rounding_rule=rounding_rule_test_update_verify,
            rounding_basis=rounding_basis_test_update_verify,
            rounding_num=rounding_num_test_update_verify,
            share_fee=share_fee_test_update_verify,
            ifc_status=ifc_status_test_update_verify,
            created_by=created_by_test_update_verify,
            approved_by=approved_by_test_update_verify,
            effect_date=effect_date_test_update_verify,
            effect_value=effect_value_test_update_verify,
            list_transaction=list_transaction_test_update_verify,
        )

    def test_008_dpt_ifc_definition_update_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        # approve data update
        self.bo_approval_approve(
            transaction_number=transaction_number_update,
            username=username_approve_other_branch,
            password=password_approve_other_branch,
        )
        # search master
        self.deposit_ifc_item_definition_search_verify(
            ifc_code=value_ifc_code,
            ifc_name=ifc_name_test_update,
        )

    def test_009_dpt_ifc_definition_view_after_update(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_ifc_item_definition_view(
            ifc_code=value_ifc_code,
            ifc_name=ifc_name_test_view_update,
            ifc_type=ifc_type_test_view_update,
            ifc_sub_type=ifc_sub_type_test_view_update,
            val_base=val_base_test_view_update,
            is_linked=is_linked_test_view_update,
            value=value_test_view_update,
            ifc_linkage=ifc_linkage_test_view_update,
            ifc_operator=ifc_operator_test_view_update,
            margin_value=margin_value_test_view_update,
            value_type=value_type_test_view_update,
            currency_code=currency_code_test_view_update,
            floor_value=floor_value_test_view_update,
            ceiling_value=ceiling_value_test_view_update,
            value_basis=value_basis_test_view_update,
            tenor=tenor_test_view_update,
            tenor_unit=tenor_unit_test_view_update,
            active_condition=active_condition_test_view_update,
            rounding_rule=rounding_rule_test_view_update,
            rounding_basis=rounding_basis_test_view_update,
            rounding_num=rounding_num_test_view_update,
            share_fee=share_fee_test_view_update,
            ifc_status=ifc_status_test_view_update,
            created_by=created_by_test_view_update,
            approved_by=approved_by_test_view_update,
            effect_date=effect_date_test_view_update,
            effect_value=effect_value_test_view_update,
            expected_gls_sys_account_names=expected_gls_sys_account_names_test_view_update,
            expected_gls_account_aliass=expected_gls_account_aliass_test_view_update,
            list_transaction=list_transaction_test_view_update,
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

    def test_010_dpt_ifc_definition_delete_approve(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_ifc_item_definition_delete(
            ifc_code=value_ifc_code,
            expected_message='This change requires approval to be affected.',
        )
        # search master
        self.deposit_ifc_item_definition_search_verify(
            ifc_code=value_ifc_code,
        )
        # verify actions
        self.bo_approval_verify_actions(
            master_code=value_ifc_code,
            tran_name=tran_name_delete,
            expected_actions=expected_actions_delete
        )
        # approve delete
        self.bo_approval_approve(
            username=username_approve_other_branch,
            password=password_approve_other_branch,
            master_code=value_ifc_code,
            tran_name=tran_name_delete,
        )

    def test_011_dpt_ifc_definition_after_delete(self):
        print('Start: ' + datetime.now().strftime('%d/%m/%Y %H:%M:%S'))
        self.deposit_ifc_item_definition_advanced_search(ifc_code_from=value_ifc_code, ifc_code_to=value_ifc_code)
        self.assert_search_not_found()

if __name__ == '__main__': 
    webui_test.main()