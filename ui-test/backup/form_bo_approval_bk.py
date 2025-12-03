import random

from webui_test.running.config import F8Config
from webui_test.form_action import *

class FormBoApproval(FormAction):

# -------------------------- handle BO - BACK OFFICE APPROVAL --------------------------
    # FOF-Back Office Approval
    def bo_approval_search(self, text):
        self.close_all_form()
        self.open_bo_approval()
        self.wait_for_button_available('Search')
        self.assert_form_title('FOF-Back Office Approval')
        self.simple_search_f8(text)
        self.wait_loading()

    def bo_approval_search_advanced_status(self, transaction_number=None, master_code=None, tran_name=None, status=None, user_name=None):
        self.close_all_form()
        self.open_bo_approval()
        self.assert_form_title('FOF-Back Office Approval')
        if transaction_number:
            self.advanced_search_f8('Tran number', transaction_number, field_type='A')
        if master_code:
            self.advanced_search_f8('Master Code', master_code, field_type='A')
        if tran_name:
            self.advanced_search_f8('Tran name', tran_name, field_type='A')
        self.key_escape()
        if status:
            self.advanced_search_f8('Status', status, field_type='S')
        if user_name:
            self.advanced_search_f8('User name', user_name, field_type='A')
        self.click_button_search_advanced_f8()
        self.wait_loading()

    def bo_approval_search_advanced_normal(self, transaction_number=None, master_code=None, tran_name=None, status=None, user_name=None):
        self.close_all_form()
        self.open_bo_approval()
        self.assert_form_title('FOF-Back Office Approval')
        self.bo_click_collap('Advanced search')
        if transaction_number:
            self.advanced_search('Tran number', transaction_number, field_type='A')
        if master_code:
            self.advanced_search('Master code', master_code, field_type='A')
        if tran_name:
            self.advanced_search('Tran name', tran_name, field_type='A')
        self.key_escape()
        if status:
            self.advanced_search('Status', status, field_type='S')
        if user_name:
            self.advanced_search('User name', user_name, field_type='A')
        self.click_button_search_advanced()
        self.wait_loading()
        self.bo_click_uncollap('Advanced search')

    def bo_approval_mode_simple(self, transaction_number, mode=None):
        if mode is None:
            mode = F8Config.view_mode
        if mode=='S':
            self.bo_approval_search_advanced_status(transaction_number=transaction_number)
        if mode=='N':
            self.bo_approval_search(transaction_number)

    def bo_approval_mode_advanced(self, transaction_number=None, master_code=None, tran_name=None, mode=None, status=None, user_name=None):
        if mode is None:
            mode = F8Config.view_mode
        if mode=='S':
            self.bo_approval_search_advanced_status(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, status=status, user_name=user_name)
        if mode=='N':
            self.bo_approval_search_advanced_normal(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, status=status, user_name=user_name)

    def bo_approval_view(self, transaction_number, form_title=None, mode=None):
        self.bo_approval_mode_simple(transaction_number=transaction_number, mode=mode)
        self.click_table_menu('View', 1)
        self.wait_loading()
        self.check_notification('Get info successfully')
        self.wait_for_label_available('This change requires approval to be affected.')
        if form_title:
            self.assert_form_title(form_title)
        self.fo_assert_text('Transaction number', transaction_number)

    def bo_approval_approve(self, username, password, reason=None, list_error_message=None, mode=None, transaction_number=None, master_code=None, tran_name=None, status=None, user_name=None):
        self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode, status=status, user_name=user_name)
        self.click_table_menu('Approve', 1)
        self.approve_in_popup(
            username=username,
            password=password,
            reason=reason
        )
        self.wait_loading()
        # approve transaction not allow
        if list_error_message:
            self.assert_notification('Approve error')
            self.assert_error_message()
            self.assert_list_error_message(list_error_message)
            # search and compare status
            self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode, status=None, user_name=user_name)
            self.assert_status_table_data('Status', 1, 'Pending to approve')
        else:
            # self.check_notification('Approve successfully')
            self.assert_notification('Approve successfully')
            # search and compare status
            self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode, status=None, user_name=user_name)
            self.assert_status_table_data('Status', 1, 'Completed')

    def bo_approval_reject(self, username, password, reason=None, mode=None, transaction_number=None, master_code=None, tran_name=None, status=None, user_name=None):
        self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode, status=status, user_name=user_name)
        self.click_table_menu('Reject', 1)
        self.approve_in_popup(
            username=username,
            password=password,
            reason=reason
        )
        self.wait_loading()
        # self.check_notification('Reject successfully')
        self.assert_notification('Reject successfully')
        # search and compare status
        self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode, status=None, user_name=user_name)
        self.assert_status_table_data('Status', 1, 'Rejected')
        print(f'Transaction number has been rejected: {transaction_number}')

    def check_bo_approval(self, transaction_number=None, master_code=None, tran_name=None, transaction_status=None, mode=None, status=None, user_name=None):
        self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode, status=status, user_name=user_name)
        if transaction_status:
            transaction_status_actual = self.get_status_table_data('Status', 1)
            if transaction_status==transaction_status_actual:
                return True
            else:
                return False

    def bo_approval_search_verify(self, transaction_number=None, master_code=None, tran_name=None, status=None, user_name=None):
        if transaction_number:
            self.assert_table_data('Tran Number', 1, transaction_number)
        if master_code:
            self.assert_table_data('Master Code', 1, master_code)
        if tran_name:
            self.assert_table_data('Tran Name', 1, tran_name)
        if status:
            self.assert_status_table_data('Status', 1, status)
        if user_name:
            self.assert_table_data('Tran Name', 1, user_name)

    def get_transaction_number(self):
        transaction_number = self.bo_get_text_single('Transaction number')
        print(f'Transaction number: {transaction_number}')
        return transaction_number

    def bo_approval_verify_actions(self, mode=None, transaction_number=None, master_code=None, tran_name=None, expected_actions=None, row=None, status=None, user_name=None):
        self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode, status=status, user_name=user_name)
        self.assert_actions(expected_actions=expected_actions, row=row)

# -------------------------- handle BO - DEPOSIT --------------------------
    # DPT-Catalogue Definition - Data Verification
    def deposit_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, deposit_classification=None, passbook_or_statement_or_receipt=None, minimum_deposit_amount=None, catalogue_status=None, interest_payment_restrictions=None, debit_accounting=None, debit_cash=None, debit_deposit=None, credit_accounting=None, credit_cash=None, credit_deposit=None, tenor_1=None, tenor_unit_1=None, tenor_2=None, tenor_unit_2=None, deposit_tenor=None, deposit_tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, minimum_tenor=None, minimum_tenor_unit=None, multiple_deposit_allow=None, multiple_withdrawal_allow=None, early_withdrawal=None, minimum_tenor_allow_early_withdrawal=None, minimum_tenor_allow_early_withdrawal_unit=None, credit_interest_y_n=None, credit_interest_tenor=None, credit_interest_tenor_unit=None, the_day_of_tenor_for_crediting_interest=None, minimum_dormant_amount=None, dormant_period=None, type_of_dormant_period=None, rollover_option=None, rollover_to_catalogue=None, initial_deposit_amount=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if deposit_type:
            self.bo_assert_select('Deposit type', deposit_type)
        if deposit_sub_type:
            self.bo_assert_select('Deposit sub type', deposit_sub_type)
        if deposit_purpose:
            self.bo_assert_select('Deposit purpose', deposit_purpose)
        if deposit_classification:
            self.bo_assert_select('Deposit classification', deposit_classification)
        if passbook_or_statement_or_receipt:
            self.bo_assert_select('Passbook or statement or receipt', passbook_or_statement_or_receipt)
        if minimum_deposit_amount:
            self.bo_assert_value('Minimum deposit amount', minimum_deposit_amount)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if interest_payment_restrictions:
            self.bo_assert_select_multi('Interest payment restriction', interest_payment_restrictions)
        self.bo_click_collap('Debit With')
        if debit_accounting is not None:
            self.bo_assert_checkbox_multi('Debit With', 'Accounting', debit_accounting)
        if debit_cash is not None:
            self.bo_assert_checkbox_multi('Debit With', 'Cash', debit_cash)
        if debit_deposit is not None:
            self.bo_assert_checkbox_multi('Debit With', 'Deposit', debit_deposit)
        self.bo_click_collap('Credit With')
        if credit_accounting is not None:
            self.bo_assert_checkbox_multi('Credit With', 'Accounting', credit_accounting)
        if credit_cash is not None:
            self.bo_assert_checkbox_multi('Credit With', 'Cash', credit_cash)
        if credit_deposit is not None:
            self.bo_assert_checkbox_multi('Credit With', 'Deposit', credit_deposit)
        self.bo_click_tab('Tenor and relative information')
        if tenor_1:
            self.bo_assert_value_group('Tenor 1', tenor_1)
        if tenor_unit_1:
            self.bo_assert_select_group('Tenor unit 1', tenor_unit_1)
        if tenor_2:
            self.bo_assert_value_group('Tenor 2', tenor_2)
        if tenor_unit_2:
            self.bo_assert_select_group('Tenor unit 2', tenor_unit_2)
        if deposit_tenor:
            self.bo_assert_value_group('Deposit tenor', deposit_tenor)
        if deposit_tenor_unit:
            self.bo_assert_select_group('Deposit tenor unit', deposit_tenor_unit)
        if interest_tenor:
            self.bo_assert_value('Interest tenor', interest_tenor)
        if interest_tenor_unit:
            self.bo_assert_select('Interest tenor unit', interest_tenor_unit)
        if minimum_tenor:
            self.bo_assert_value_group('Minimum tenor', minimum_tenor)
        if minimum_tenor_unit:
            self.bo_assert_select_group('Minimum tenor unit', minimum_tenor_unit)
        if multiple_deposit_allow:
            self.bo_assert_select('Multiple deposit allow', multiple_deposit_allow)
        if multiple_withdrawal_allow:
            self.bo_assert_select('Multiple withdrawal allow', multiple_withdrawal_allow)
        if early_withdrawal:
            self.bo_assert_select('Early withdrawal', early_withdrawal)
        if minimum_tenor_allow_early_withdrawal:
            self.bo_assert_value_group('Minimum tenor allow early withdrawal', minimum_tenor_allow_early_withdrawal)
        if minimum_tenor_allow_early_withdrawal_unit:
            self.bo_assert_select_group('Minimum tenor allow early withdrawal unit', minimum_tenor_allow_early_withdrawal_unit)
        if credit_interest_y_n:
            self.bo_assert_select('Credit interest (Y/N)', credit_interest_y_n)
        if credit_interest_tenor:
            self.bo_assert_value_group('Credit interest tenor', credit_interest_tenor)
        if credit_interest_tenor_unit:
            self.bo_assert_select_group('Credit interest tenor unit', credit_interest_tenor_unit)
        if the_day_of_tenor_for_crediting_interest:
            self.bo_assert_value('The day of tenor for crediting interest', the_day_of_tenor_for_crediting_interest)
        if minimum_dormant_amount:
            self.bo_assert_value('Minimum Dormant amount', minimum_dormant_amount)
        if dormant_period:
            self.bo_assert_value_group('Dormant period', dormant_period)
        if type_of_dormant_period:
            self.bo_assert_select_group('Type of dormant period', type_of_dormant_period)
        if rollover_option:
            self.bo_assert_select('Rollover option', rollover_option)
        if rollover_to_catalogue:
            self.bo_assert_value_group('Rollover to catalogue', rollover_to_catalogue)
        if initial_deposit_amount:
            self.bo_assert_value('Initial deposit amount', initial_deposit_amount)
        self.bo_click_tab('IFC information ')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs information ')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')

    def deposit_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, deposit_type=None, deposit_sub_type=None, deposit_purpose=None, deposit_classification=None, passbook_or_statement_or_receipt=None, minimum_deposit_amount=None, catalogue_status=None, interest_payment_restrictions=None, created_by=None, approved_by=None, debit_accounting=None, debit_cash=None, debit_deposit=None, credit_accounting=None, credit_cash=None, credit_deposit=None, tenor_1=None, tenor_unit_1=None, tenor_2=None, tenor_unit_2=None, deposit_tenor=None, deposit_tenor_unit=None, interest_tenor_unit=None, interest_tenor=None, minimum_tenor=None, minimum_tenor_unit=None, multiple_deposit_allow=None, multiple_withdrawal_allow=None, early_withdrawal=None, minimum_tenor_allow_early_withdrawal=None, minimum_tenor_allow_early_withdrawal_unit=None, credit_interest_y_n=None, credit_interest_tenor=None, credit_interest_tenor_unit=None, the_day_of_tenor_for_crediting_interest=None, minimum_dormant_amount=None, dormant_period=None, type_of_dormant_period=None, rollover_option=None, rollover_to_catalogue=None, initial_deposit_amount=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if deposit_type:
            self.bo_assert_select('Deposit type', deposit_type)
        if deposit_sub_type:
            self.bo_assert_select('Deposit sub type', deposit_sub_type)
        if deposit_purpose:
            self.bo_assert_select('Deposit purpose', deposit_purpose)
        if deposit_classification:
            self.bo_assert_select('Deposit classification', deposit_classification)
        if passbook_or_statement_or_receipt:
            self.bo_assert_select('Passbook or statement or receipt', passbook_or_statement_or_receipt)
        if minimum_deposit_amount:
            self.bo_assert_value('Minimum deposit amount', minimum_deposit_amount)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if interest_payment_restrictions:
            self.bo_assert_select_multi('Interest payment restriction', interest_payment_restrictions)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.bo_click_collap('Debit with ')
        if debit_accounting is not None:
            self.bo_assert_checkbox_multi('Debit with ', 'Accounting', debit_accounting)
        if debit_cash is not None:
            self.bo_assert_checkbox_multi('Debit with ', 'Cash', debit_cash)
        if debit_deposit is not None:
            self.bo_assert_checkbox_multi('Debit with ', 'Deposit', debit_deposit)
        self.bo_click_collap('Credit with')
        if credit_accounting is not None:
            self.bo_assert_checkbox_multi('Credit with', 'Accounting', credit_accounting)
        if credit_cash is not None:
            self.bo_assert_checkbox_multi('Credit with', 'Cash', credit_cash)
        if credit_deposit is not None:
            self.bo_assert_checkbox_multi('Credit with', 'Deposit', credit_deposit)
        self.bo_click_tab('Tenor and relative information')
        if tenor_1:
            self.bo_assert_value_group('Tenor 1', tenor_1)
        if tenor_unit_1:
            self.bo_assert_select_group('Tenor unit 1', tenor_unit_1)
        if tenor_2:
            self.bo_assert_value_group('Tenor 2', tenor_2)
        if tenor_unit_2:
            self.bo_assert_select_group('Tenor unit 2', tenor_unit_2)
        if deposit_tenor:
            self.bo_assert_value_group('Deposit tenor', deposit_tenor)
        if deposit_tenor_unit:
            self.bo_assert_select_group('Deposit tenor unit', deposit_tenor_unit)
        if interest_tenor_unit:
            self.bo_assert_select('Interest tenor unit', interest_tenor_unit)
        if interest_tenor:
            self.bo_assert_value('Interest tenor', interest_tenor)
        if minimum_tenor:
            self.bo_assert_value_group('Minimum tenor', minimum_tenor)
        if minimum_tenor_unit:
            self.bo_assert_select_group('Minimum tenor unit', minimum_tenor_unit)
        if multiple_deposit_allow:
            self.bo_assert_select('Multiple deposit allow', multiple_deposit_allow)
        if multiple_withdrawal_allow:
            self.bo_assert_select('Multiple withdrawal allow', multiple_withdrawal_allow)
        if early_withdrawal:
            self.bo_assert_select('Early withdrawal', early_withdrawal)
        if minimum_tenor_allow_early_withdrawal:
            self.bo_assert_value_group('Minimum tenor allow early withdrawal', minimum_tenor_allow_early_withdrawal)
        if minimum_tenor_allow_early_withdrawal_unit:
            self.bo_assert_select_group('Minimum tenor allow early withdrawal unit', minimum_tenor_allow_early_withdrawal_unit)
        if credit_interest_y_n:
            self.bo_assert_select('Credit interest (Y/N)', credit_interest_y_n)
        if credit_interest_tenor:
            self.bo_assert_value_group('Credit interest tenor', credit_interest_tenor)
        if credit_interest_tenor_unit:
            self.bo_assert_select_group('Credit interest tenor unit', credit_interest_tenor_unit)
        if the_day_of_tenor_for_crediting_interest:
            self.bo_assert_value('The day of tenor for crediting interest', the_day_of_tenor_for_crediting_interest)
        if minimum_dormant_amount:
            self.bo_assert_value('Minimum Dormant amount', minimum_dormant_amount)
        if dormant_period:
            self.bo_assert_value_group('Dormant period', self.no_thousands_separator(dormant_period))
        if type_of_dormant_period:
            self.bo_assert_select_group('Type of dormant period', type_of_dormant_period)
        if rollover_option:
            self.bo_assert_select('Rollover option', rollover_option)
        if rollover_to_catalogue:
            self.bo_assert_value_group('Rollover to catalogue', rollover_to_catalogue)
        if initial_deposit_amount:
            self.bo_assert_value('Initial deposit amount', initial_deposit_amount)
        self.bo_click_tab('IFC Information ')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')

    def deposit_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, currency_code=None, deposit_type=None, passbook_or_statement_or_receipt=None, tenor=None, tenor_unit=None, catalogue_status=None):
        # search and verify
        self.deposit_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue name', 1, catalogue_name)
        if currency_code:
            self.assert_table_data('Currency code', 1, currency_code)
        if deposit_type:
            self.assert_table_data('Deposit type', 1, deposit_type)
        if passbook_or_statement_or_receipt:
            self.assert_table_data('Passbook or statement', 1, passbook_or_statement_or_receipt)
        if tenor:
            self.assert_table_data('Tenor', 1, tenor)
        if tenor_unit:
            self.assert_table_data('Tenor unit', 1, tenor_unit)
        if catalogue_status:
            self.assert_table_data('Status', 1, catalogue_status)

    # DPT-IFC Item Definition - Data Verification
    def deposit_ifc_item_definition_add_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-IFC Item Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor unit', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def deposit_ifc_item_definition_update_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-IFC Item Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def deposit_ifc_item_definition_search_verify(self, ifc_code, ifc_name=None, value_type=None, ifc_type=None, value=None, tenor=None, tenor_unit=None, active_condition=None, status=None):
        # search and verify
        self.deposit_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        # verify value
        self.assert_table_data('IFC code', 1, ifc_code)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)
        if value_type:
            self.assert_table_data('Value type', 1, value_type)
        if ifc_type:
            self.assert_table_data('IFC type', 1, ifc_type)
        if value:
            self.assert_table_data('Value', 1, value)
        if tenor:
            self.assert_table_data('Tenor', 1, tenor)
        if tenor_unit:
            self.assert_table_data('Tenor unit', 1, tenor_unit)
        if active_condition:
            self.assert_table_data('Active condition', 1, active_condition)
        if status:
            self.assert_table_data('Status', 1, status)

    def deposit_get_ifc_code(self, ifc_name):
        self.deposit_ifc_item_definition_simple_search(ifc_name)
        self.assert_table_data('IFC name', 1, ifc_name)
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('DPT-IFC Item Definition-View')
        self.bo_click_tab('General information')
        ifc_code_out=self.bo_get_value('IFC code')
        print(f'IFC code: {ifc_code_out}')
        return ifc_code_out

    # DPT-IFC Auto Fee - Data Verification
    def deposit_ifc_auto_fee_add_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None, list_error_message=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-IFC Auto Fee-Add'
        )
        # verify value
        if transaction_code:
            self.bo_assert_value_group_single('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group_single('IFC code', ifc_code)
        if condition:
            self.bo_assert_text_single('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def deposit_ifc_auto_fee_update_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-IFC Auto Fee-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if transaction_code:
            self.bo_assert_value_group('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group('IFC code', ifc_code)
        if condition:
            self.bo_assert_text('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def deposit_ifc_auto_fee_search_verify(self, transaction_code, ifc_code, transaction_name=None, ifc_name=None):
        # search
        self.deposit_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        # verify value
        self.assert_table_data('Transaction code', 1, transaction_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        if transaction_name:
            self.assert_table_data('Transaction name', 1, transaction_name)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)

# -------------------------- handle BO - CREDIT --------------------------
    # CRD-Catalogue Definition - Data Verification
    def credit_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, interest_computation_mode=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, reminder_profile_code=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_account_aliass=None, expected_gls_sys_account_names=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None, email=None, push_notification=None, sms=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if secured_by_currency:
            self.bo_assert_select('Secured by currency', secured_by_currency)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if interest_computation_mode:
            self.bo_assert_select('Interest computation mode', interest_computation_mode)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if status:
            self.bo_assert_select('Status', status)
        if reminder_profile_code:
            self.bo_assert_value('Reminder Profile code', reminder_profile_code)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_assert_value('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_assert_value('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_assert_value('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_assert_value('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_assert_value_group('Fine collection tenor', fine_collection_tenor)
        if fine_collection_tenor_unit:
            self.bo_assert_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_assert_value('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_assert_value('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('IFC information')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def credit_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, interest_computation_mode=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, reminder_profile_code=None, created_by=None, approved_by=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_account_aliass=None, expected_gls_sys_account_names=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None, email=None, push_notification=None, sms=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if secured_by_currency:
            self.bo_assert_select('Secured by currency', secured_by_currency)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if interest_computation_mode:
            self.bo_assert_select('Interest computation mode', interest_computation_mode)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if status:
            self.bo_assert_select('Status', status)
        if reminder_profile_code:
            self.bo_assert_value('Reminder Profile code', reminder_profile_code)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_assert_value('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_assert_value('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_assert_value('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_assert_value('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_assert_value_group('Fine collection tenor', fine_collection_tenor)
        if fine_collection_tenor_unit:
            self.bo_assert_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_assert_value('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_assert_value('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('IFC Information')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def credit_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, currency=None, credit_type=None, credit_facility=None, tenor_type=None, status=None):
        # search and verify
        self.credit_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue name', 1, catalogue_name)
        if currency:
            self.assert_table_data('Currency', 1, currency)
        if credit_type:
            self.assert_table_data('Credit type', 1, credit_type)
        if credit_facility:
            self.assert_table_data('Credit facility', 1, credit_facility)
        if tenor_type:
            self.assert_table_data('Tenor type', 1, tenor_type)
        if status:
            self.assert_table_data('Status', 1, status)

    # CRD-IFC Item Definition - Data Verification
    def credit_ifc_item_definition_add_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-IFC Item Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor unit', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def credit_ifc_item_definition_update_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-IFC Item Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def credit_ifc_item_definition_search_verify(self, ifc_code, ifc_name=None, value_type=None, ifc_type=None, value=None, tenor=None, tenor_unit=None, active_condition=None, status=None):
        # search and verify
        self.credit_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        # verify value
        self.assert_table_data('IFC code', 1, ifc_code)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)
        if value_type:
            self.assert_table_data('Value type', 1, value_type)
        if ifc_type:
            self.assert_table_data('IFC type', 1, ifc_type)
        if value:
            self.assert_table_data('Value', 1, value)
        if tenor:
            self.assert_table_data('Tenor', 1, tenor)
        if tenor_unit:
            self.assert_table_data('Tenor unit', 1, tenor_unit)
        if active_condition:
            self.assert_table_data('Active condition', 1, active_condition)
        if status:
            self.assert_table_data('Status', 1, status)

    def credit_get_ifc_code(self, ifc_name):
        self.credit_ifc_item_definition_simple_search(ifc_name)
        self.assert_table_data('IFC name', 1, ifc_name)
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('CRD-IFC Item Definition-View')
        self.bo_click_tab('General information')
        ifc_code_out=self.bo_get_value('IFC code')
        print(f'IFC code: {ifc_code_out}')
        return ifc_code_out

    # CRD-IFC Auto Fee - Data Verification
    def credit_ifc_auto_fee_add_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-IFC Auto Fee-Add'
        )
        # verify value
        if transaction_code:
            self.bo_assert_value_group_single('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group_single('IFC code', ifc_code)
        if condition:
            self.bo_assert_text_single('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def credit_ifc_auto_fee_update_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-IFC Auto Fee-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if transaction_code:
            self.bo_assert_value_group('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group('IFC code', ifc_code)
        if condition:
            self.bo_assert_text('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def credit_ifc_auto_fee_search_verify(self, transaction_code, ifc_code, transaction_name=None, ifc_name=None):
        # search
        self.credit_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        # verify value
        self.assert_table_data('Transaction code', 1, transaction_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        if transaction_name:
            self.assert_table_data('Transaction name', 1, transaction_name)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)

    # CRD-Collection Reminder - Data Verification
    def collection_reminder_add_verify(self, transaction_number, reminder_code=None, reminder_name=None, description=None, reminder_basis=None, remind_officer=None, number_of_days=None, remind_customer=None, use_sms=None, sms_template=None, use_email=None, email_template_id=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Collection Reminder-Add'
        )
        # verify value
        if reminder_code:
            self.bo_assert_text('Reminder code', reminder_code)
        if reminder_name:
            self.bo_assert_text('Reminder name', reminder_name)
        if description is None or description == '':
            description = 'AUTO TEST'
        if description:
            self.bo_assert_text('Description', description)
        if reminder_basis:
            self.bo_assert_select('Reminder basis', reminder_basis)
        if remind_officer is not None:
            self.bo_assert_checkbox('Remind officer', remind_officer)
        if number_of_days:
            self.bo_assert_value('Number of days', number_of_days)
        if remind_customer is not None:
            self.bo_assert_checkbox('Remind customer', remind_customer)
        if use_sms is not None:
            self.bo_assert_checkbox('Use SMS', use_sms)
        if sms_template:
            self.bo_assert_text_multi_line('Sms template', sms_template)
        if use_email is not None:
            self.bo_assert_checkbox('Use Email', use_email)
        if email_template_id:
            self.bo_assert_select('Email template id', email_template_id)

    def collection_reminder_update_verify(self, transaction_number, reminder_code=None, reminder_name=None, description=None, reminder_basis=None, remind_officer=None, number_of_days=None, remind_customer=None, use_sms=None, sms_template=None, use_email=None, email_template_id=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Collection Reminder-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if reminder_code:
            self.bo_assert_text('Reminder code', reminder_code)
        if reminder_name:
            self.bo_assert_text('Reminder name', reminder_name)
        if description:
            self.bo_assert_text('Description', description)
        if reminder_basis:
            self.bo_assert_select('Reminder basis', reminder_basis)
        if remind_officer is not None:
            self.bo_assert_checkbox('Remind officer', remind_officer)
        if number_of_days:
            self.bo_assert_value('Number of days', number_of_days)
        if remind_customer is not None:
            self.bo_assert_checkbox('Remind customer', remind_customer)
        if use_sms is not None:
            self.bo_assert_checkbox('Use SMS', use_sms)
        if sms_template:
            self.bo_assert_text_multi_line('Sms template', sms_template)
        if use_email is not None:
            self.bo_assert_checkbox('Use Email', use_email)
        if email_template_id:
            self.bo_assert_select('Email template id', email_template_id)

    def collection_reminder_search_verify(self, reminder_code=None, reminder_name=None, number_of_days=None, remind_officer=None, remind_customer=None, use_email=None):
        # search
        self.collection_reminder_simple_search(reminder_code)
        # verify value
        if reminder_code:
            self.assert_table_data('Reminder code', 1, reminder_code)
        if reminder_name:
            self.assert_table_data('Reminder name', 1, reminder_name)
        if number_of_days:
            self.assert_table_data('Number of days', 1, number_of_days)
        if remind_officer:
            self.assert_table_data('Remind officer', 1, remind_officer)
        if remind_customer:
            self.assert_table_data('Remind customer', 1, remind_customer)
        if use_email:
            self.assert_table_data('Use Email', 1, use_email)

    # CRD-Collection Reminder Profile - Data Verification
    def collection_reminder_profile_add_verify(self, transaction_number, profile_code=None, profile_name=None, reminder_codes=None, reminder_names=None, orders=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Collection Reminder Profile-Add'
        )
        # verify value
        if profile_code:
            self.bo_assert_text('Profile code', profile_code)
        if profile_name:
            self.bo_assert_text('Profile name', profile_name)
        if reminder_names:
            for reminder_code, reminder_name in zip(reminder_codes, reminder_names):
                self.bo_assert_text_table('Reminder code', reminder_code, 'Reminder name', reminder_name)
        if orders:
            for reminder_code, order in zip(reminder_codes, orders):
                self.bo_assert_text_table('Reminder code', reminder_code, 'Order', order)

    def collection_reminder_profile_update_verify(self, transaction_number, profile_code=None, profile_name=None, reminder_codes=None, reminder_names=None, orders=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-Collection Reminder Profile-View'
        )
        # verify value
        if profile_code:
            self.bo_assert_text('Profile code', profile_code)
        if profile_name:
            self.bo_assert_text('Profile name', profile_name)
        if reminder_names:
            for reminder_code, reminder_name in zip(reminder_codes, reminder_names):
                self.bo_assert_text_table('Reminder code', reminder_code, 'Reminder name', reminder_name)
        if orders:
            for reminder_code, order in zip(reminder_codes, orders):
                self.bo_assert_text_table('Reminder code', reminder_code, 'Order', order)

    def collection_reminder_profile_search_verify(self, profile_code, profile_name=None):
        # search
        self.collection_reminder_profile_advanced_search(profile_code=profile_code)
        # verify value
        self.assert_table_data('Profile code', 1, profile_code)
        if profile_name:
            self.assert_table_data('Profile name', 1, profile_name)

# -------------------------- handle BO - PAYMENT --------------------------
    # PMT-Catalogue Definition - Data Verification
    def payment_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, output_format=None, direction=None, instrument=None, purpose=None, holding_days=None, status=None, message_type=None, export_swift=None, send_by_email=None, group_code=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if output_format:
            self.bo_assert_select('Output format', output_format)
        if direction:
            self.bo_assert_select('Direction', direction)
        if instrument:
            self.bo_assert_select('Instrument', instrument)
        if purpose:
            self.bo_assert_select('Purpose', purpose)
        if holding_days:
            self.bo_assert_value('Holding days', holding_days)
        if status:
            self.bo_assert_select('Status', status)
        if message_type:
            self.bo_assert_select('Message type', message_type)
        if export_swift:
            self.bo_assert_select('Export swift', export_swift)
        if send_by_email:
            self.bo_assert_select('Send by email', send_by_email)
        self.bo_click_tab('Payment instruction group information')
        if group_code:
            self.bo_assert_select('Group code', group_code)

    def payment_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, output_format=None, direction=None, instrument=None, purpose=None, holding_days=None, status=None, created_by=None, approved_by=None, message_type=None, export_swift=None, send_by_email=None, group_code=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if output_format:
            self.bo_assert_select('Output format', output_format)
        if direction:
            self.bo_assert_select('Direction', direction)
        if instrument:
            self.bo_assert_select('Instrument', instrument)
        if purpose:
            self.bo_assert_select('Purpose', purpose)
        if holding_days:
            self.bo_assert_value('Holding days', holding_days)
        if status:
            self.bo_assert_select('Status', status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if message_type:
            self.bo_assert_select('Message type', message_type)
        if export_swift:
            self.bo_assert_select('Export swift', export_swift)
        if send_by_email:
            self.bo_assert_select('Send by email', send_by_email)
        self.bo_click_tab('Payment instruction group information')
        if group_code:
            self.bo_assert_select('Group code', group_code)

    def payment_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, output_format=None, direction=None, instrument=None, status=None, export_swift_file=None, send_email=None, message_type=None):
        # search and verify
        self.payment_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue name', 1, catalogue_name)
        if output_format:
            self.assert_table_data('Output format', 1, output_format)
        if direction:
            self.assert_table_data('Direction', 1, direction)
        if instrument:
            self.assert_table_data('Instrument', 1, instrument)
        if status:
            self.assert_table_data('Status', 1, status)
        if export_swift_file:
            self.assert_table_data('Export Swift File', 1, export_swift_file)
        if send_email:
            self.assert_table_data('Send email', 1, send_email)
        if message_type:
            self.assert_table_data('Message type', 1, message_type)

    # PMT-IFC Item Definition - Data Verification
    def payment_ifc_item_definition_add_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-IFC Item Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor unit', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def payment_ifc_item_definition_update_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-IFC Item Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def payment_ifc_item_definition_search_verify(self, ifc_code, ifc_name=None, value_type=None, ifc_type=None, value=None, tenor=None, tenor_unit=None, active_condition=None, status=None):
        # search and verify
        self.payment_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        # verify value
        self.assert_table_data('IFC code', 1, ifc_code)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)
        if value_type:
            self.assert_table_data('Value type', 1, value_type)
        if ifc_type:
            self.assert_table_data('IFC type', 1, ifc_type)
        if value:
            self.assert_table_data('Value', 1, value)
        if tenor:
            self.assert_table_data('Tenor', 1, tenor)
        if tenor_unit:
            self.assert_table_data('Tenor unit', 1, tenor_unit)
        if active_condition:
            self.assert_table_data('Active condition', 1, active_condition)
        if status:
            self.assert_table_data('Status', 1, status)

    def payment_get_ifc_code(self, ifc_name):
        self.payment_ifc_item_definition_simple_search(ifc_name)
        self.assert_table_data('IFC name', 1, ifc_name)
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('PMT-IFC Item Definition-View')
        self.bo_click_tab('General information')
        ifc_code_out=self.bo_get_value('IFC code')
        print(f'IFC code: {ifc_code_out}')
        return ifc_code_out

    # PMT-IFC Auto Fee - Data Verification
    def payment_ifc_auto_fee_add_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-IFC Auto Fee-Add'
        )
        # verify value
        if transaction_code:
            self.bo_assert_value_group_single('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group_single('IFC code', ifc_code)
        if condition:
            self.bo_assert_text_single('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def payment_ifc_auto_fee_update_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-IFC Auto Fee-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if transaction_code:
            self.bo_assert_value_group('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group('IFC code', ifc_code)
        if condition:
            self.bo_assert_text('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def payment_ifc_auto_fee_search_verify(self, transaction_code, ifc_code, transaction_name=None, ifc_name=None):
        # search
        self.payment_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        # verify value
        self.assert_table_data('Transaction code', 1, transaction_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        if transaction_name:
            self.assert_table_data('Transaction name', 1, transaction_name)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)

# -------------------------- handle BO - TREASURY --------------------------
    # TRS-Catalogue Definition - Data Verification
    def treasury_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, trade_group=None, details_category=None, trade_type=None, margin_trading=None, market=None, catalogue_status=None, settle_tenor=None, settle_tenor_unit=None, tenor=None, tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, rollover_option=None, revaluation=None, user_create=None, approve_by=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if trade_group:
            self.bo_assert_select('Trade Group', trade_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if trade_type:
            self.bo_assert_select('Trade Type', trade_type)
        if margin_trading:
            self.bo_assert_select('Margin Trading', margin_trading)
        if market:
            self.bo_assert_select('Market', market)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if settle_tenor:
            self.bo_assert_value('Settle Tenor', settle_tenor)
        if settle_tenor_unit:
            self.bo_assert_select('Settle Tenor Unit', settle_tenor_unit)
        if tenor:
            self.bo_assert_value('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select('Tenor Unit', tenor_unit)
        if interest_tenor:
            self.bo_assert_value('Interest Tenor', interest_tenor)
        if interest_tenor_unit:
            self.bo_assert_select('Interest Tenor Unit', interest_tenor_unit)
        if rollover_option:
            self.bo_assert_select('Rollover Option', rollover_option)
        if revaluation:
            self.bo_assert_select('Revaluation', revaluation)
        if user_create:
            self.bo_assert_text('User create', user_create)
        if approve_by:
            self.bo_assert_text('Approve by', approve_by)
        self.bo_click_tab('IFC information ')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs information ')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')

    def treasury_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, trade_group=None, details_category=None, trade_type=None, margin_trading=None, market=None, catalogue_status=None, settle_tenor=None, settle_tenor_unit=None, tenor=None, tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, rollover_option=None, revaluation=None, user_create=None, approve_by=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_text('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if trade_group:
            self.bo_assert_select('Trade Group', trade_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if trade_type:
            self.bo_assert_select('Trade Type', trade_type)
        if margin_trading:
            self.bo_assert_select('Margin Trading', margin_trading)
        if market:
            self.bo_assert_select('Market', market)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if settle_tenor:
            self.bo_assert_value('Settle Tenor', settle_tenor)
        if settle_tenor_unit:
            self.bo_assert_select('Settle Tenor Unit', settle_tenor_unit)
        if tenor:
            self.bo_assert_value('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select('Tenor Unit', tenor_unit)
        if interest_tenor:
            self.bo_assert_value('Interest Tenor', interest_tenor)
        if interest_tenor_unit:
            self.bo_assert_select('Interest Tenor Unit', interest_tenor_unit)
        if rollover_option:
            self.bo_assert_select('Rollover Option', rollover_option)
        if revaluation:
            self.bo_assert_select('Revaluation', revaluation)
        if user_create:
            self.bo_assert_text_group('User create', user_create)
        if approve_by:
            self.bo_assert_text_group('Approve by', approve_by)
        self.bo_click_tab('IFC information ')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs information ')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')

    def treasury_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, trade_group=None, details_category=None, trade_type=None, margin_trading=None, market=None, status=None, settle_tenor=None, settle_tenor_unit=None, tenor=None, tenor_unit=None, interest_tenor=None, interest_tenor_unit=None, rollover_option=None, revaluation=None, creator=None, approve_by=None):
        # search and verify
        self.treasury_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalog Code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalog name', 1, catalogue_name)
        if trade_group:
            self.assert_table_data('Trade Group', 1, trade_group)
        if details_category:
            self.assert_table_data('Details category', 1, details_category)
        if trade_type:
            self.assert_table_data('Trade Type', 1, trade_type)
        if margin_trading:
            self.assert_table_data('Margin Trading', 1, margin_trading)
        if market:
            self.assert_table_data('Market', 1, market)
        if status:
            self.assert_table_data('Status', 1, status)
        if settle_tenor:
            self.assert_table_data('Settle Tenor', 1, settle_tenor)
        if settle_tenor_unit:
            self.assert_table_data('Settle Tenor Unit', 1, settle_tenor_unit)
        if tenor:
            self.assert_table_data('Tenor', 1, tenor)
        if tenor_unit:
            self.assert_table_data('Tenor Unit', 1, tenor_unit)
        if interest_tenor:
            self.assert_table_data('Interest Tenor', 1, interest_tenor)
        if interest_tenor_unit:
            self.assert_table_data('Interest Tenor Unit', 1, interest_tenor_unit)
        if rollover_option:
            self.assert_table_data('Rollover Option', 1, rollover_option)
        if revaluation:
            self.assert_table_data('Revaluation', 1, revaluation)
        if creator:
            self.assert_table_data('Creator', 1, creator)
        if approve_by:
            self.assert_table_data('Approve by', 1, approve_by)

    # TRS-IFC Item Definition - Data Verification
    def treasury_ifc_item_definition_add_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-IFC Item Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor unit', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def treasury_ifc_item_definition_update_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-IFC Item Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def treasury_ifc_item_definition_search_verify(self, ifc_code, ifc_name=None, value_type=None, ifc_type=None, value=None, tenor=None, tenor_unit=None, active_condition=None, status=None):
        # search and verify
        self.treasury_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        # verify value
        self.assert_table_data('IFC code', 1, ifc_code)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)
        if value_type:
            self.assert_table_data('Value type', 1, value_type)
        if ifc_type:
            self.assert_table_data('IFC type', 1, ifc_type)
        if value:
            self.assert_table_data('Value', 1, value)
        if tenor:
            self.assert_table_data('Tenor', 1, tenor)
        if tenor_unit:
            self.assert_table_data('Tenor unit', 1, tenor_unit)
        if active_condition:
            self.assert_table_data('Active condition', 1, active_condition)
        if status:
            self.assert_table_data('Status', 1, status)

    def treasury_get_ifc_code(self, ifc_name):
        self.treasury_ifc_item_definition_simple_search(ifc_name)
        self.assert_table_data('IFC name', 1, ifc_name)
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRS-IFC Item Definition-View')
        self.bo_click_tab('General information')
        ifc_code_out=self.bo_get_value('IFC code')
        print(f'IFC code: {ifc_code_out}')
        return ifc_code_out

    # TRS-IFC Auto Fee - Data Verification
    def treasury_ifc_auto_fee_add_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-IFC Auto Fee-Add'
        )
        # verify value
        if transaction_code:
            self.bo_assert_value_group_single('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group_single('IFC code', ifc_code)
        if condition:
            self.bo_assert_text_single('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def treasury_ifc_auto_fee_update_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-IFC Auto Fee-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if transaction_code:
            self.bo_assert_value_group('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group('IFC code', ifc_code)
        if condition:
            self.bo_assert_text('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def treasury_ifc_auto_fee_search_verify(self, transaction_code, ifc_code, transaction_name=None, ifc_name=None):
        # search
        self.treasury_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        # verify value
        self.assert_table_data('Transaction code', 1, transaction_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        if transaction_name:
            self.assert_table_data('Transaction name', 1, transaction_name)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)

# -------------------------- handle BO - TRADE --------------------------
    # TRD-Catalogue Definition - Data Verification
    def trade_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, business_group=None, details_category=None, term_and_condition=None, tenor=None, customer_type=None, catalogue_status=None, user_create=None, approve_by=None, obs_percentage_rate=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if business_group:
            self.bo_assert_select('Business group', business_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if term_and_condition:
            self.bo_assert_select('Term and condition', term_and_condition)
        if tenor:
            self.bo_assert_select('Tenor', tenor)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if user_create:
            self.bo_assert_text('User create', user_create)
        if approve_by:
            self.bo_assert_text('Approve by', approve_by)
        if obs_percentage_rate:
            self.bo_assert_value('OBS percentage/rate', obs_percentage_rate)
        self.bo_click_tab('IFC information ')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs information ')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')

    def trade_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, business_group=None, details_category=None, term_and_condition=None, tenor=None, customer_type=None, catalogue_status=None, user_create=None, approve_by=None, obs_percentage_rate=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if business_group:
            self.bo_assert_select('Business group', business_group)
        if details_category:
            self.bo_assert_select('Details category', details_category)
        if term_and_condition:
            self.bo_assert_select('Term and condition', term_and_condition)
        if tenor:
            self.bo_assert_select('Tenor', tenor)
        if customer_type:
            self.bo_assert_select('Customer type', customer_type)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if user_create:
            self.bo_assert_text_group('User create', user_create)
        if approve_by:
            self.bo_assert_text_group('Approve by', approve_by)
        if obs_percentage_rate:
            self.bo_assert_value('OBS percentage/rate', obs_percentage_rate)
        self.bo_click_tab('IFC information ')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs information ')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')

    def trade_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, business_group=None, category=None, term=None, customer_type=None, creator=None, status=None, obs_percentage_rate=None):
        # search and verify
        self.trade_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalog Code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalog name', 1, catalogue_name)
        if business_group:
            self.assert_table_data('Business group', 1, business_group)
        if category:
            self.assert_table_data('Category', 1, category)
        if term:
            self.assert_table_data('Term', 1, term)
        if customer_type:
            self.assert_table_data('Customer type', 1, customer_type)
        if creator:
            self.assert_table_data('Creator', 1, creator)
        if status:
            self.assert_table_data('Status', 1, status)
        if obs_percentage_rate:
            self.assert_table_data('OBS percentage/rate', 1, obs_percentage_rate)

    # TRD-IFC Item Definition - Data Verification
    def trade_ifc_item_definition_add_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-IFC Item Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor unit', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def trade_ifc_item_definition_update_verify(self, transaction_number, ifc_code=None, ifc_name=None, ifc_type=None, ifc_sub_type=None, val_base=None, is_linked=None, value=None, ifc_linkage=None, ifc_operator=None, margin_value=None, value_type=None, currency_code=None, floor_value=None, ceiling_value=None, value_basis=None, tenor=None, tenor_unit=None, active_condition=None, rounding_rule=None, rounding_basis=None, rounding_num=None, share_fee=None, ifc_status=None, created_by=None, approved_by=None, effect_date=None, effect_value=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None, list_transaction=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-IFC Item Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if ifc_code:
            self.bo_assert_value('IFC code', ifc_code)
        if ifc_name:
            self.bo_assert_text('IFC name', ifc_name)
        if ifc_type:
            self.bo_assert_select('IFC type', ifc_type)
        if ifc_sub_type:
            self.bo_assert_select('IFC sub type', ifc_sub_type)
        if val_base:
            self.bo_assert_select('Val base', val_base)
        if is_linked:
            self.bo_assert_select('Is Linked', is_linked)
        if value:
            self.bo_assert_value('Value', value)
        if ifc_linkage:
            self.bo_assert_text_group('IFC linkage', ifc_linkage)
        if ifc_operator:
            self.bo_assert_select('IFC Operator', ifc_operator)
        if margin_value:
            self.bo_assert_value('Margin value', margin_value)
        if value_type:
            self.bo_assert_select('Value type', value_type)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if floor_value:
            self.bo_assert_value('Floor value', floor_value)
        if ceiling_value:
            self.bo_assert_value('Ceiling value', ceiling_value)
        if value_basis:
            self.bo_assert_text('Value basis', value_basis)
        if tenor:
            self.bo_assert_value_group('Tenor', tenor)
        if tenor_unit:
            self.bo_assert_select_group('Tenor', tenor_unit)
        if active_condition:
            self.bo_assert_text('Active condition', active_condition)
        if rounding_rule:
            self.bo_assert_select('Rounding rule', rounding_rule)
        if rounding_basis:
            self.bo_assert_select('Rounding basis', rounding_basis)
        if rounding_num:
            self.bo_assert_value('Rounding num', rounding_num)
        if share_fee:
            self.bo_assert_select('Share fee', share_fee)
        if ifc_status:
            self.bo_assert_select('IFC status', ifc_status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        if effect_date:
            self.bo_assert_date('Effect Date', effect_date)
        if effect_value:
            self.bo_assert_value('Effect Value', effect_value)
        self.bo_click_tab('GLs information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('List Transaction')
        if list_transaction:
            self.bo_assert_select_multi('List transaction', list_transaction)

    def trade_ifc_item_definition_search_verify(self, ifc_code, ifc_name=None, value_type=None, ifc_type=None, value=None, tenor=None, tenor_unit=None, active_condition=None, status=None):
        # search and verify
        self.trade_ifc_item_definition_advanced_search(ifc_code_from=ifc_code, ifc_code_to=ifc_code)
        # verify value
        self.assert_table_data('IFC code', 1, ifc_code)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)
        if value_type:
            self.assert_table_data('Value type', 1, value_type)
        if ifc_type:
            self.assert_table_data('IFC type', 1, ifc_type)
        if value:
            self.assert_table_data('Value', 1, value)
        if tenor:
            self.assert_table_data('Tenor', 1, tenor)
        if tenor_unit:
            self.assert_table_data('Tenor unit', 1, tenor_unit)
        if active_condition:
            self.assert_table_data('Active condition', 1, active_condition)
        if status:
            self.assert_table_data('Status', 1, status)

    def trade_get_ifc_code(self, ifc_name):
        self.trade_ifc_item_definition_simple_search(ifc_name)
        self.assert_table_data('IFC name', 1, ifc_name)
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('TRD-IFC Item Definition-View')
        self.bo_click_tab('General information')
        ifc_code_out=self.bo_get_value('IFC code')
        print(f'IFC code: {ifc_code_out}')
        return ifc_code_out

    # TRD-IFC Auto Fee - Data Verification
    def trade_ifc_auto_fee_add_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-IFC Auto Fee-Add'
        )
        # verify value
        if transaction_code:
            self.bo_assert_value_group_single('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group_single('IFC code', ifc_code)
        if condition:
            self.bo_assert_text_single('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def trade_ifc_auto_fee_update_verify(self, transaction_number, transaction_code=None, ifc_code=None, condition=None, active=None, exchange=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-IFC Auto Fee-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if transaction_code:
            self.bo_assert_value_group('Transaction code', transaction_code)
        if ifc_code:
            self.bo_assert_text_group('IFC code', ifc_code)
        if condition:
            self.bo_assert_text('Condition', condition)
        if active is not None:
            self.bo_assert_checkbox('Active', active)
        if exchange is not None:
            self.bo_assert_checkbox('Exchange', exchange)

    def trade_ifc_auto_fee_search_verify(self, transaction_code, ifc_code, transaction_name=None, ifc_name=None):
        # search
        self.trade_ifc_auto_fee_advanced_search(transaction_code=transaction_code, ifc_code=ifc_code)
        # verify value
        self.assert_table_data('Transaction code', 1, transaction_code)
        self.assert_table_data('IFC code', 1, ifc_code)
        if transaction_name:
            self.assert_table_data('Transaction name', 1, transaction_name)
        if ifc_name:
            self.assert_table_data('IFC name', 1, ifc_name)

# -------------------------- handle BO - OVERDRAFT --------------------------
    # DPT-OD Catalogue Definition - Data Verification
    def overdraft_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_account_aliass=None, expected_gls_sys_account_names=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None, email=None, push_notification=None, sms=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-OD Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if secured_by_currency:
            self.bo_assert_select('Secured by currency', secured_by_currency)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if status:
            self.bo_assert_select('Status', status)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_assert_value('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_assert_value('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_assert_value('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_assert_value('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_assert_value_group('Fine collection tenor', fine_collection_tenor)
        if fine_collection_tenor_unit:
            self.bo_assert_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_assert_value('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_assert_value('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('IFC information')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def overdraft_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, secure_type=None, secure_rate=None, secured_by_currency=None, credit_type=None, credit_sub_type=None, tenor_type=None, credit_purpose=None, credit_classification=None, credit_facility=None, disbursement_mode=None, is_provision=None, classification_option=None, status=None, created_by=None, approved_by=None, principal_collection_tenor=None, principal_collection_tenor_unit=None, principal_grace_period=None, principal_due_on_holiday=None, interest_collection_tenor=None, interest_collection_tenor_unit=None, interest_grace_period=None, interest_due_on_holiday=None, fine_collection_tenor=None, fine_collection_tenor_unit=None, fine_grace_period=None, fine_due_on_holiday=None, standard=None, watch=None, substandard=None, doubtful=None, loss=None, expected_ifc_list_codes=None, expected_ifc_names=None, expected_ifc_values=None, expected_ifc_types=None, expected_ifc_tenors=None, expected_ifc_tenor_units=None, expected_ifc_statuss=None, expected_gls_account_aliass=None, expected_gls_sys_account_names=None, expected_extension_sys_account_names=None, expected_extension_conditions=None, expected_extension_replace_bys=None, email=None, push_notification=None, sms=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-OD Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if secure_type:
            self.bo_assert_select('Secure type', secure_type)
        if secure_rate:
            self.bo_assert_value('Secure rate', secure_rate)
        if secured_by_currency:
            self.bo_assert_select('Secured by currency', secured_by_currency)
        if credit_type:
            self.bo_assert_select('Credit type', credit_type)
        if credit_sub_type:
            self.bo_assert_select('Credit sub type', credit_sub_type)
        if tenor_type:
            self.bo_assert_select('Tenor type', tenor_type)
        if credit_purpose:
            self.bo_assert_select('Credit purpose', credit_purpose)
        if credit_classification:
            self.bo_assert_select('Credit classification', credit_classification)
        if credit_facility:
            self.bo_assert_select('Credit facility', credit_facility)
        if disbursement_mode:
            self.bo_assert_select('Disbursement mode', disbursement_mode)
        if is_provision:
            self.bo_assert_select('Is provision?', is_provision)
        if classification_option:
            self.bo_assert_select('Classification option', classification_option)
        if status:
            self.bo_assert_select('Status', status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)
        self.bo_click_tab('Term and condition')
        if principal_collection_tenor:
            self.bo_assert_value_group('Principal collection tenor', principal_collection_tenor)
        if principal_collection_tenor_unit:
            self.bo_assert_select_group('Principal collection tenor', principal_collection_tenor_unit)
        if principal_grace_period:
            self.bo_assert_value('Principal grace period', principal_grace_period)
        if principal_due_on_holiday:
            self.bo_assert_value('Principal due on holiday', principal_due_on_holiday)
        if interest_collection_tenor:
            self.bo_assert_value_group('Interest collection tenor', interest_collection_tenor)
        if interest_collection_tenor_unit:
            self.bo_assert_select_group('Interest collection tenor', interest_collection_tenor_unit)
        if interest_grace_period:
            self.bo_assert_value('Interest grace period', interest_grace_period)
        if interest_due_on_holiday:
            self.bo_assert_value('Interest due on holiday', interest_due_on_holiday)
        if fine_collection_tenor:
            self.bo_assert_value_group('Fine collection tenor', fine_collection_tenor)
        if fine_collection_tenor_unit:
            self.bo_assert_select_group('Fine collection tenor', fine_collection_tenor_unit)
        if fine_grace_period:
            self.bo_assert_value('Fine grace period', fine_grace_period)
        if fine_due_on_holiday:
            self.bo_assert_value('Fine due on holiday', fine_due_on_holiday)
        self.bo_click_tab('Provision rate of principal')
        if standard:
            self.bo_assert_value('Standard', standard)
        if watch:
            self.bo_assert_value('Watch', watch)
        if substandard:
            self.bo_assert_value('Substandard', substandard)
        if doubtful:
            self.bo_assert_value('Doubtful', doubtful)
        if loss:
            self.bo_assert_value('Loss', loss)
        self.bo_click_tab('IFC information')
        if expected_ifc_names:
            for ifc_code, ifc_name in zip(expected_ifc_list_codes, expected_ifc_names):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC name', value_colunm_expected=ifc_name)
        if expected_ifc_values:
            for ifc_code, ifc_value in zip(expected_ifc_list_codes, expected_ifc_values):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC value', value_colunm_expected=ifc_value)
        if expected_ifc_types:
            for ifc_code, ifc_type in zip(expected_ifc_list_codes, expected_ifc_types):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='IFC type', value_colunm_expected=ifc_type)
        if expected_ifc_tenors:
            for ifc_code, ifc_tenor in zip(expected_ifc_list_codes, expected_ifc_tenors):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor', value_colunm_expected=ifc_tenor)
        if expected_ifc_tenor_units:
            for ifc_code, ifc_tenor_unit in zip(expected_ifc_list_codes, expected_ifc_tenor_units):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Tenor unit', value_colunm_expected=ifc_tenor_unit)
        if expected_ifc_statuss:
            for ifc_code, ifc_status in zip(expected_ifc_list_codes, expected_ifc_statuss):
                self.bo_assert_text_table(colunm_01='IFC code', value_colunm_01=ifc_code, colunm_expected='Status', value_colunm_expected=ifc_status)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)
        self.bo_click_tab('Extension Group of Account Information')
        if expected_extension_replace_bys:
            for sys_account_name, condition, replace_by in zip(expected_extension_sys_account_names, expected_extension_conditions, expected_extension_replace_bys):
                self.bo_assert_text_table(colunm_01='System account name', value_colunm_01=sys_account_name, colunm_02='Customer Condition', value_colunm_02=condition, colunm_expected='Replace by', value_colunm_expected=replace_by, xpath_type='preceding')
        self.bo_click_tab('Notification channel')
        self.bo_click_collap('Notification type')
        if email is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Email', email)
        if push_notification is not None:
            self.bo_assert_checkbox_multi('Notification type', 'Push Notification', push_notification)
        if sms is not None:
            self.bo_assert_checkbox_multi('Notification type', 'SMS', sms)

    def overdraft_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, currency=None, credit_type=None, credit_facility=None, tenor_type=None, status=None):
        # search and verify
        self.overdraft_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue name', 1, catalogue_name)
        if currency:
            self.assert_table_data('Currency', 1, currency)
        if credit_type:
            self.assert_table_data('Credit type', 1, credit_type)
        if credit_facility:
            self.assert_table_data('Credit facility', 1, credit_facility)
        if tenor_type:
            self.assert_table_data('Tenor type', 1, tenor_type)
        if status:
            self.assert_table_data('Status', 1, status)

# -------------------------- handle BO - MORTGAGE --------------------------
    # MTG-Catalogue Definition - Data Verification
    def mortgage_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_rate=None, risk_allocation_rate=None, book_scope=None, depreciation_option=None, catalogue_status=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='MTG-Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if collateral_asset_type:
            self.bo_assert_select('Collateral asset type', collateral_asset_type)
        if collateral_asset_classification:
            self.bo_assert_select('Collateral asset classification', collateral_asset_classification)
        if collateral_rate:
            self.bo_assert_value('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.bo_assert_value('Risk allocation rate', risk_allocation_rate)
        if book_scope:
            self.bo_assert_select('Book scope', book_scope)
        if depreciation_option:
            self.bo_assert_select('Depreciation option', depreciation_option)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)

    def mortgage_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, currency_code=None, collateral_asset_type=None, collateral_asset_classification=None, collateral_rate=None, risk_allocation_rate=None, book_scope=None, depreciation_option=None, catalogue_status=None, created_by=None, approved_by=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='MTG-Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue name', catalogue_name)
        if currency_code:
            self.bo_assert_select('Currency code', currency_code)
        if collateral_asset_type:
            self.bo_assert_select('Collateral asset type', collateral_asset_type)
        if collateral_asset_classification:
            self.bo_assert_select('Collateral asset classification', collateral_asset_classification)
        if collateral_rate:
            self.bo_assert_value('Collateral rate', collateral_rate)
        if risk_allocation_rate:
            self.bo_assert_value('Risk allocation rate', risk_allocation_rate)
        if book_scope:
            self.bo_assert_select('Book scope', book_scope)
        if depreciation_option:
            self.bo_assert_select('Depreciation option', depreciation_option)
        if catalogue_status:
            self.bo_assert_select('Catalogue status', catalogue_status)
        if created_by:
            self.bo_assert_text_group('Created by', created_by)
        if approved_by:
            self.bo_assert_text_group('Approved by', approved_by)

    def mortgage_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, currency=None, collateral_asset_type=None, classification=None, collateral_rate=None, status=None):
        # search and verify
        self.mortgage_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue name', 1, catalogue_name)
        if currency:
            self.assert_table_data('Currency', 1, currency)
        if collateral_asset_type:
            self.assert_table_data('Collateral asset type', 1, collateral_asset_type)
        if classification:
            self.assert_table_data('Classification', 1, classification)
        if collateral_rate:
            self.assert_table_data('Collateral rate', 1, collateral_rate)
        if status:
            self.assert_table_data('Status', 1, status)

# -------------------------- handle BO - FIXED ASSET --------------------------
    # FAC-Fixed Asset Catalogue Definition - Data Verification
    def fixed_asset_catalogue_definition_add_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalogue_status=None, fixed_asset_life_time=None, life_time_unit=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FAC-Fixed Asset Catalogue Definition-Add'
        )
        # verify value
        self.bo_click_tab('General Information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue Name', catalogue_name)
        if fixed_asset_type:
            self.bo_assert_select('Fixed Asset Type', fixed_asset_type)
        if fixed_asset_classification:
            self.bo_assert_select('Fixed Asset Classification', fixed_asset_classification)
        if depreciation_method:
            self.bo_assert_select('Depreciation Method', depreciation_method)
        if catalogue_status:
            self.bo_assert_select('Catalogue Status', catalogue_status)
        if fixed_asset_life_time:
            self.bo_assert_value('Fixed asset life time', fixed_asset_life_time)
        if life_time_unit:
            self.bo_assert_select('Life time unit', life_time_unit)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)

    def fixed_asset_catalogue_definition_update_verify(self, transaction_number, catalogue_code=None, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalogue_status=None, fixed_asset_life_time=None, life_time_unit=None, created_by=None, approve_by=None, expected_gls_sys_account_names=None, expected_gls_account_aliass=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FAC-Fixed Asset Catalogue Definition-View'
        )
        # verify value
        self.bo_click_tab('General Information')
        if catalogue_code:
            self.bo_assert_value('Catalogue Code', catalogue_code)
        if catalogue_name:
            self.bo_assert_text('Catalogue Name', catalogue_name)
        if fixed_asset_type:
            self.bo_assert_select('Fixed Asset Type', fixed_asset_type)
        if fixed_asset_classification:
            self.bo_assert_select('Fixed Asset Classification', fixed_asset_classification)
        if depreciation_method:
            self.bo_assert_select('Depreciation Method', depreciation_method)
        if catalogue_status:
            self.bo_assert_select('Catalogue Status', catalogue_status)
        if fixed_asset_life_time:
            self.bo_assert_value('Fixed asset life time', fixed_asset_life_time)
        if life_time_unit:
            self.bo_assert_select('Life time unit', life_time_unit)
        if created_by:
            self.bo_assert_text_group('Created By', created_by)
        if approve_by:
            self.bo_assert_text_group('Approve By', approve_by)
        self.bo_click_tab('GLs Information')
        if expected_gls_account_aliass:
            for sys_account_name, account_alias in zip(expected_gls_sys_account_names, expected_gls_account_aliass):
                self.bo_assert_text_table(colunm_01='Sys Account Name', value_colunm_01=sys_account_name, colunm_expected='Account Alias', value_colunm_expected=account_alias)

    def fixed_asset_catalogue_definition_search_verify(self, catalogue_code, catalogue_name=None, fixed_asset_type=None, fixed_asset_classification=None, depreciation_method=None, catalogue_status=None):
        # search and verify
        self.fixed_asset_catalogue_definition_simple_search(catalogue_code)
        self.assert_table_data('Catalogue Code', 1, catalogue_code)
        if catalogue_name:
            self.assert_table_data('Catalogue Name', 1, catalogue_name)
        if fixed_asset_type:
            self.assert_table_data('Fixed Asset Type', 1, fixed_asset_type)
        if fixed_asset_classification:
            self.assert_table_data('Fixed Asset Classification', 1, fixed_asset_classification)
        if depreciation_method:
            self.assert_table_data('Depreciation Method', 1, depreciation_method)
        if catalogue_status:
            self.assert_table_data('Catalogue Status', 1, catalogue_status)

# -------------------------- handle BO - SYSTEM CODE TABLE --------------------------
    # ACT-System Code Table - Data Verification
    def accounting_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ACT-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def accounting_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ACT-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def accounting_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.accounting_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # ADM-System Code Table - Data Verification
    def admin_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def admin_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def admin_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.admin_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # BCH-System Code Table - Data Verification
    def batch_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='BCH-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def batch_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='BCH-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def batch_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.batch_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # CAR-System Code Table - Data Verification
    def card_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CAR-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def card_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CAR-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def card_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.card_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # CSH-System Code Table - Data Verification
    def cash_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CSH-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def cash_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CSH-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def cash_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.cash_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # CRD-System Code Table - Data Verification
    def credit_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def credit_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CRD-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def credit_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.credit_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # CTM-System Code Table - Data Verification
    def customer_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CTM-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def customer_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CTM-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def customer_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.customer_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # DPT-System Code Table - Data Verification
    def deposit_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def deposit_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='DPT-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def deposit_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.deposit_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # FX-System Code Table - Data Verification
    def fx_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FX-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def fx_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FX-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def fx_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.fx_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # FAC-System Code Table - Data Verification
    def fixed_asset_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FAC-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def fixed_asset_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='FAC-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def fixed_asset_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.fixed_asset_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # MTG-System Code Table - Data Verification
    def mortgage_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='MTG-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def mortgage_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='MTG-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def mortgage_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.mortgage_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # PMT-System Code Table - Data Verification
    def payment_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def payment_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='PMT-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def payment_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.payment_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # TRS-System Code Table - Data Verification
    def treasury_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def treasury_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRS-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def treasury_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.treasury_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # VCH-System Code Table - Data Verification
    def voucher_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='VCH-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def voucher_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='VCH-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def voucher_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.voucher_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # TRD-System Code Table - Data Verification
    def trade_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def trade_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='TRD-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)

    def trade_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None):
        # search and verify
        self.trade_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)

    # CMS-System Code Table - Data Verification
    def cms_system_code_table_add_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CMS-System Code Table-Add'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)
        if application_code:
            self.bo_assert_select_single('Application Code', application_code)

    def cms_system_code_table_update_verify(self, transaction_number, code_id=None, code_name=None, caption_of_code=None, english=None, vietnamese=None, laothian=None, khmer=None, myanmar=None, code_of_group=None, code_index=None, code_value=None, field_link=None, is_visible=None, application_code=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='CMS-System Code Table-View'
        )
        # verify value
        if code_id:
            self.bo_assert_text_single('Code Id', code_id)
        if code_name:
            self.bo_assert_text_single('Code Name', code_name)
        if caption_of_code:
            self.bo_assert_text_single('Caption Of Code', caption_of_code)
        self.bo_click_collap('Multi Caption Of Code')
        if english:
            self.bo_assert_text_multi('Multi Caption Of Code', 'English', english)
        if vietnamese:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Vietnamese', vietnamese)
        if laothian:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Laothian', laothian)
        if khmer:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Khmer', khmer)
        if myanmar:
            self.bo_assert_text_multi('Multi Caption Of Code', 'Myanmar', myanmar)
        if code_of_group:
            self.bo_assert_select_single('Code Of Group', code_of_group)
        if code_index:
            self.bo_assert_value_single('Code Index', code_index)
        if code_value:
            self.bo_assert_text_single('Code Value', code_value)
        if field_link:
            self.bo_assert_text_single('Field Link', field_link)
        if is_visible is not None:
            self.bo_assert_checkbox('Is Visible?', is_visible)
        if application_code:
            self.bo_assert_select_single('Application Code', application_code)

    def cms_system_code_table_search_verify(self, code_id, code_name=None, caption=None, index=None, field_link=None, application_code=None):
        # search and verify
        self.cms_system_code_table_simple_search(code_id)
        self.assert_table_data('Code Id', 1, code_id)
        if code_name:
            self.assert_table_data('Code Name', 1, code_name)
        if caption:
            self.assert_table_data('Caption', 1, caption)
        if index:
            self.assert_table_data('Index', 1, index)
        if field_link:
            self.assert_table_data('Field Link', 1, field_link)
        if application_code:
            self.assert_table_data('Application Code', 1, application_code)

# -------------------------- handle BO - ADMINISTRATION --------------------------
    # ADM-Branch Profile - Data Verification
    def branch_profile_add_verify(self, transaction_number, branch_code=None, old_branch_id=None, branch_name=None, branch_address=None, branch_type=None, branch_phone=None, home=None, office=None, cell=None, facsimile=None, telex=None, tax_code=None, base_currency_code=None, local_currency_code=None, region=None, bic=None, domestic_bank_code=None, internal_code=None, country=None, main_language=None, time_zone_of_branch=None, thousand_separate_character=None, decimal_separate_character=None, date_format_for_short=None, long_date_format=None, time_format=None, online=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-Branch Profile-Add'
        )
        # verify value
        self.bo_click_tab('General information')
        if branch_code:
            self.bo_assert_value('Branch code', branch_code)
        if old_branch_id:
            self.bo_assert_text('Old branch ID', old_branch_id)
        if branch_name:
            self.bo_assert_text('Branch name', branch_name)
        if branch_address:
            self.bo_assert_text('Branch address', branch_address)
        if branch_type:
            self.bo_assert_select('Branch type', branch_type)
        if branch_phone:
            self.bo_assert_text('Branch phone', branch_phone)
        self.bo_click_collap('Phone number')
        if home:
            self.bo_assert_text_multi('Phone number', 'Home', home)
        if office:
            self.bo_assert_text_multi('Phone number', 'Office', office)
        if cell:
            self.bo_assert_text_multi('Phone number', 'Cell', cell)
        if facsimile:
            self.bo_assert_text_multi('Phone number', 'Facsimile', facsimile)
        if telex:
            self.bo_assert_text_multi('Phone number', 'Telex', telex)
        if tax_code:
            self.bo_assert_text('Tax code', tax_code)
        if base_currency_code:
            self.bo_assert_select('Base currency code', base_currency_code)
        if local_currency_code:
            self.bo_assert_select('Local currency code', local_currency_code)
        if region:
            self.bo_assert_select('Region', region)
        self.bo_click_collap('Reference code')
        if bic:
            self.bo_assert_text_multi('Reference code', 'Bic', bic)
        if domestic_bank_code:
            self.bo_assert_text_multi('Reference code', 'Domestic bank code', domestic_bank_code)
        if internal_code:
            self.bo_assert_text_multi('Reference code', 'Internal code', internal_code)
        if country:
            self.bo_assert_select('Country', country)
        if main_language:
            self.bo_assert_select('Main language', main_language)
        if time_zone_of_branch:
            self.bo_assert_select('Time zone of branch', time_zone_of_branch)
        if thousand_separate_character:
            self.bo_assert_select('Thousand separate character', thousand_separate_character)
        if decimal_separate_character:
            self.bo_assert_select('Decimal separate character', decimal_separate_character)
        if date_format_for_short:
            self.bo_assert_select('Date format for short', date_format_for_short)
        if long_date_format:
            self.bo_assert_select('Long date format', long_date_format)
        if time_format:
            self.bo_assert_select('Time format', time_format)
        if online:
            self.bo_assert_select('Online', online)

    def branch_profile_update_verify(self, transaction_number, branch_code=None, old_branch_id=None, branch_name=None, branch_address=None, branch_phone=None, branch_type=None, home=None, office=None, cell=None, facsimile=None, telex=None, tax_code=None, base_currency_code=None, local_currency_code=None, region=None, bic=None, domestic_bank_code=None, internal_code=None, country=None, main_language=None, time_zone_of_branch=None, thousand_separate_character=None, decimal_separate_character=None, date_format_for_short=None, long_date_format=None, time_format=None, online=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-Branch Profile-View'
        )
        # verify value
        self.bo_click_tab('General information')
        if branch_code:
            self.bo_assert_text('Branch code', branch_code)
        if old_branch_id:
            self.bo_assert_text('Old branch ID', old_branch_id)
        if branch_name:
            self.bo_assert_text('Branch name', branch_name)
        if branch_address:
            self.bo_assert_text('Branch address', branch_address)
        if branch_phone:
            self.bo_assert_text('Branch phone', branch_phone)
        if branch_type:
            self.bo_assert_select('Branch type', branch_type)
        self.bo_click_collap('Phone number')
        if home:
            self.bo_assert_text_multi('Phone number', 'Home', home)
        if office:
            self.bo_assert_text_multi('Phone number', 'Office', office)
        if cell:
            self.bo_assert_text_multi('Phone number', 'Cell', cell)
        if facsimile:
            self.bo_assert_text_multi('Phone number', 'Facsimile', facsimile)
        if telex:
            self.bo_assert_text_multi('Phone number', 'Telex', telex)
        if tax_code:
            self.bo_assert_text('Tax code', tax_code)
        if base_currency_code:
            self.bo_assert_select('Base currency code', base_currency_code)
        if local_currency_code:
            self.bo_assert_select('Local currency code', local_currency_code)
        if region:
            self.bo_assert_select('Region', region)
        self.bo_click_collap('Reference code')
        if bic:
            self.bo_assert_text_multi('Reference code', 'Bic', bic)
        if domestic_bank_code:
            self.bo_assert_text_multi('Reference code', 'Domestic bank code', domestic_bank_code)
        if internal_code:
            self.bo_assert_text_multi('Reference code', 'Internal code', internal_code)
        if country:
            self.bo_assert_select('Country', country)
        if main_language:
            self.bo_assert_select('Main language', main_language)
        if time_zone_of_branch:
            self.bo_assert_select('Time zone of branch', time_zone_of_branch)
        if thousand_separate_character:
            self.bo_assert_select('Thousand separate character', thousand_separate_character)
        if decimal_separate_character:
            self.bo_assert_select('Decimal separate character', decimal_separate_character)
        if date_format_for_short:
            self.bo_assert_select('Date format for short', date_format_for_short)
        if long_date_format:
            self.bo_assert_select('Long date format', long_date_format)
        if time_format:
            self.bo_assert_select('Time format', time_format)
        if online:
            self.bo_assert_select('Online', online)

    def branch_profile_search_verify(self, branch_code=None, branch_name=None, address=None, base_currency_code=None, online_status=None, branch_type=None):
        # search and verify
        self.branch_profile_simple_search(branch_code)
        self.assert_table_data('Branch code', 1, branch_code)
        if branch_name:
            self.assert_table_data('Branch name', 1, branch_name)
        if address:
            self.assert_table_data('Address', 1, address)
        if base_currency_code:
            self.assert_table_data('Base currency code', 1, base_currency_code)
        if online_status:
            self.assert_table_data('Online status', 1, online_status)
        if branch_type:
            self.assert_table_data('Branch type', 1, branch_type)

    # ADM-Department Profile - Data Verification
    def department_profile_add_verify(self, transaction_number, department_code=None, department_name=None, branch_code=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-Department Profile-Add'
        )
        # verify value
        if department_code:
            self.bo_assert_value_single('Department Code', department_code)
        if department_name:
            self.bo_assert_text_single('Department Name', department_name)
        if branch_code:
            self.bo_assert_select_single('Branch Code', branch_code)

    def department_profile_update_verify(self, transaction_number, department_code=None, department_name=None, branch_code=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-Department Profile-View'
        )
        # verify value
        self.bo_click_tab('General')
        if department_code:
            self.bo_assert_text('Department Code', department_code)
        if department_name:
            self.bo_assert_text('Department Name', department_name)
        if branch_code:
            self.bo_assert_select('Branch Code', branch_code)

    def department_profile_search_verify(self, department_code=None, department_name=None, branch_name=None):
        # search and verify
        self.department_profile_simple_search(department_code)
        self.assert_table_data('Department Code', 1, department_code)
        if department_name:
            self.assert_table_data('Department Name', 1, department_name)
        if branch_name:
            self.assert_table_data('Branch name', 1, branch_name)

    # ADM-Branch Linkage - Data Verification
    def branch_linkage_add_verify(self, transaction_number, master_branch=None, linkage_branch=None, linkage_type=None, description=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-Branch Linkage-Add'
        )
        # verify value
        if master_branch:
            self.bo_assert_select_single('Master branch', master_branch)
        if linkage_branch:
            self.bo_assert_select_single('Linkage branch', linkage_branch)
        if linkage_type:
            self.bo_assert_select_single('Linkage type', linkage_type)
        if description:
            self.bo_assert_text_single('Description', description)

    def branch_linkage_update_verify(self, transaction_number, master_branch=None, linkage_branch=None, linkage_type=None, description=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-Branch Linkage-View'
        )
        # verify value
        if master_branch:
            self.bo_assert_select_single('Master branch', master_branch)
        if linkage_branch:
            self.bo_assert_select_single('Linkage branch', linkage_branch)
        if linkage_type:
            self.bo_assert_select_single('Linkage type', linkage_type)
        if description:
            self.bo_assert_text_single('Description', description)

    def branch_linkage_search_verify(self, master_branch_code=None, linkage_branch_code=None, linkage_type=None, linkage_description=None):
        # search and verify
        self.branch_linkage_simple_search(linkage_description)
        self.assert_table_data('Linkage description', 1, linkage_description)
        if master_branch_code:
            self.assert_table_data('Master branch code', 1, master_branch_code)
        if linkage_branch_code:
            self.assert_table_data('Linkage branch code', 1, linkage_branch_code)
        if linkage_type:
            self.assert_table_data('Linkage type', 1, linkage_type)

    # ADM-System Policy - Data Verification
    def system_policy_add_verify(self, transaction_number, policy_id=None, description_of_policy=None, effective_from=None, effective_to=None, enforce_password_history=None, maximum_password_age=None, minimum_password_length=None, password_must_meet_complexity_requirements=None, at_least_one_lower_case_letter=None, at_least_one_upper_case_letter=None, at_least_symbol_character=None, at_least_one_number=None, can_login_from=None, can_login_to=None, the_number_of_failed_logon_attempts=None, session_mode=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-System Policy-Add'
        )
        # verify value
        if policy_id:
            self.bo_assert_text_single('Policy ID', policy_id)
        if description_of_policy:
            self.bo_assert_text_single('Description Of Policy', description_of_policy)
        if effective_from:
            self.bo_assert_date_single('Effective From', effective_from)
        if effective_to:
            self.bo_assert_date_single('Effective To', effective_to)
        if enforce_password_history:
            self.bo_assert_value_single('Enforce Password History', enforce_password_history)
        if maximum_password_age:
            self.bo_assert_value_single('Maximum Password age (0=unlimit)', maximum_password_age)
        if minimum_password_length:
            self.bo_assert_value_single('Minimum Password Length', minimum_password_length)
        if password_must_meet_complexity_requirements:
            self.bo_assert_select_single('Password Must Meet Complexity Requirements', password_must_meet_complexity_requirements)
        if at_least_one_lower_case_letter:
            self.bo_assert_select_single('At Least One Lower Case Letter', at_least_one_lower_case_letter)
        if at_least_one_upper_case_letter:
            self.bo_assert_select_single('At Least One Upper Case Letter', at_least_one_upper_case_letter)
        if at_least_symbol_character:
            self.bo_assert_select_single("At Least Symbol Character (`~!@#$%^&*()-_=+[]{}|;:'\",<.>/?)", at_least_symbol_character)
        if at_least_one_number:
            self.bo_assert_select_single('At Least One Number', at_least_one_number)
        if can_login_from:
            self.bo_assert_value_single('Can Login From', can_login_from)
        if can_login_to:
            self.bo_assert_value_single('Can Login To', can_login_to)
        if the_number_of_failed_logon_attempts:
            self.bo_assert_value_single('The Number Of Failed Logon Attempts (0=unlimit)', the_number_of_failed_logon_attempts)
        if session_mode:
            self.bo_assert_select_single('Session Mode', session_mode)

    def system_policy_update_verify(self, transaction_number, policy_id=None, description_of_policy=None, effective_from=None, effective_to=None, enforce_password_history=None, maximum_password_age=None, minimum_password_length=None, password_must_meet_complexity_requirements=None, at_least_symbol_character=None, at_least_one_upper_case_letter=None, at_least_one_lower_case_letter=None, at_least_one_number=None, can_login_from=None, can_login_to=None, the_number_of_failed_logon_attempts=None, session_mode=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-System Policy-View'
        )
        # verify value
        self.bo_click_tab('Group Name')
        if policy_id:
            self.bo_assert_value('Policy ID', policy_id)
        if description_of_policy:
            self.bo_assert_text('Description Of Policy', description_of_policy)
        if effective_from:
            self.bo_assert_date('Effective From', effective_from)
        if effective_to:
            self.bo_assert_date('Effective To', effective_to)
        if enforce_password_history:
            self.bo_assert_value('Enforce Password History', enforce_password_history)
        if maximum_password_age:
            self.bo_assert_value('Maximum Password age (0=unlimit)', maximum_password_age)
        if minimum_password_length:
            self.bo_assert_value('Minimum Password Length', minimum_password_length)
        if password_must_meet_complexity_requirements:
            self.bo_assert_select('Password Must Meet Complexity Requirements', password_must_meet_complexity_requirements)
        if at_least_symbol_character:
            self.bo_assert_select("At Least Symbol Character (`~!@#$%^&*()-_=+[]{}|;:'\",<.>/?)", at_least_symbol_character)
        if at_least_one_upper_case_letter:
            self.bo_assert_select('At Least One Upper Case Letter', at_least_one_upper_case_letter)
        if at_least_one_lower_case_letter:
            self.bo_assert_select('At Least One Lower Case Letter', at_least_one_lower_case_letter)
        if at_least_one_number:
            self.bo_assert_select('At Least One Number', at_least_one_number)
        if can_login_from:
            self.bo_assert_value('Can Login From', can_login_from)
        if can_login_to:
            self.bo_assert_value('Can Login To', can_login_to)
        if the_number_of_failed_logon_attempts:
            self.bo_assert_value('The Number Of Failed Logon Attempts (0=unlimit)', the_number_of_failed_logon_attempts)
        if session_mode:
            self.bo_assert_select('Session Mode', session_mode)

    def system_policy_search_verify(self, policy_id=None, description_of_policy=None, effective_from=None, effective_to=None):
        # search and verify
        self.system_policy_advanced_search(policy_id=policy_id)
        self.assert_table_data('Policy ID', 1, policy_id)
        if description_of_policy:
            self.assert_table_data('Description Of Policy', 1, description_of_policy)
        if effective_from:
            self.assert_table_data('Effective From', 1, effective_from)
        if effective_to:
            self.assert_table_data('Effective To', 1, effective_to)

    def system_policy_get_policy_id(self, description_of_policy):
        self.system_policy_simple_search(description_of_policy)
        self.assert_table_data('Description Of Policy', 1, description_of_policy)
        # view
        self.click_table_menu('View', 1)
        self.wait_for_button_available('Modify')
        self.assert_form_title('ADM-System Policy-View')
        self.bo_click_tab('Group Name')
        policy_id_out=self.bo_get_value('Policy ID')
        print(f'Policy ID: {policy_id_out}')
        return policy_id_out

    # ADM-User Profile
    def user_profile_add_verify(self, transaction_number, user_code=None, old_user_id=None, user_name=None, login_name=None, branch_code=None, department_name=None, cashier=None, officer=None, chief_cashier=None, operation_staff=None, dealer=None, inter_branch_user=None, branch_manager_authorized=None, hr=None, email=None, remark=None, status_of_this_record=None, password=None, main_language=None, user_phone=None, home=None, office=None, cell=None, facsimile=None, telex=None, time_zone_of_user=None, thousand_separate_character_in_amount_field=None, decimal_separate_character_in_amount_field=None, date_format_for_short=None, long_date_format=None, time_format=None, expire_date_of_this_user=None, id_of_policy_apply_for_this_user=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-User Profile-Add'
        )
        # verify value
        self.bo_click_tab('General Information')
        if user_code:
            self.bo_assert_text('User Code', user_code)
        if old_user_id:
            self.bo_assert_text('Old User ID', old_user_id)
        if user_name:
            self.bo_assert_text('User Name', user_name)
        if login_name:
            self.bo_assert_text('Login Name', login_name)
        if branch_code:
            self.bo_assert_select('Branch Code', branch_code)
        if department_name:
            self.bo_assert_select('Department Name', department_name)
        self.bo_click_collap('Position')
        if cashier is not None:
            self.bo_assert_checkbox_multi('Position', 'Cashier', cashier)
        if officer is not None:
            self.bo_assert_checkbox_multi('Position', 'Officer', officer)
        if chief_cashier is not None:
            self.bo_assert_checkbox_multi('Position', 'Chief Cashier', chief_cashier)
        if operation_staff is not None:
            self.bo_assert_checkbox_multi('Position', 'Operation Staff', operation_staff)
        if dealer is not None:
            self.bo_assert_checkbox_multi('Position', 'Dealer', dealer)
        if inter_branch_user is not None:
            self.bo_assert_checkbox_multi('Position', 'Inter-branch user', inter_branch_user)
        if branch_manager_authorized is not None:
            self.bo_assert_checkbox_multi('Position', 'Branch Manager/Authorized', branch_manager_authorized)
        if hr is not None:
            self.bo_assert_checkbox_multi('Position', 'HR', hr)
        if email:
            self.bo_assert_value('Email', email)
        if remark:
            self.bo_assert_text('Remark', remark)
        if status_of_this_record:
            self.bo_assert_select('Status Of This Record', status_of_this_record)
        if password:
            self.bo_assert_text('Password', password)
        self.bo_click_tab('Other Information')
        if main_language:
            self.bo_assert_select('Main Language', main_language)
        if user_phone:
            self.bo_assert_text('User Phone', user_phone)
        self.bo_click_collap('Phone Number')
        if home:
            self.bo_assert_text_multi('Phone Number', 'Home', home)
        if office:
            self.bo_assert_text_multi('Phone Number', 'Office', office)
        if cell:
            self.bo_assert_text_multi('Phone Number', 'Cell', cell)
        if facsimile:
            self.bo_assert_text_multi('Phone Number', 'Facsimile', facsimile)
        if telex:
            self.bo_assert_text_multi('Phone Number', 'Telex', telex)
        if time_zone_of_user:
            self.bo_assert_select('Time Zone Of User', time_zone_of_user)
        if thousand_separate_character_in_amount_field:
            self.bo_assert_select('Thousand Separate Character In Amount Field', thousand_separate_character_in_amount_field)
        if decimal_separate_character_in_amount_field:
            self.bo_assert_select('Decimal Separate Character In Amount Field', decimal_separate_character_in_amount_field)
        if date_format_for_short:
            self.bo_assert_select('Date Format For Short', date_format_for_short)
        if long_date_format:
            self.bo_assert_select('Long Date Format', long_date_format)
        if time_format:
            self.bo_assert_select('Time Format', time_format)
        if expire_date_of_this_user:
            self.bo_assert_date('Expire Date Of This User', expire_date_of_this_user)
        if id_of_policy_apply_for_this_user:
            self.bo_assert_select('ID Of Policy Apply For This User', id_of_policy_apply_for_this_user)

    def user_profile_update_verify(self, transaction_number, user_code=None, old_user_id=None, user_name=None, login_name=None, branch_code=None, department_name=None, cashier=None, officer=None, chief_cashier=None, operation_staff=None, dealer=None, inter_branch_user=None, branch_manager_authorized=None, hr=None, email=None, remark=None, status_of_this_record=None, password=None, main_language=None, user_phone=None, home=None, office=None, cell=None, facsimile=None, telex=None, time_zone_of_user=None, thousand_separate_character_in_amount_field=None, decimal_separate_character_in_amount_field=None, date_format_for_short=None, long_date_format=None, time_format=None, expire_date_of_this_user=None, id_of_policy_apply_for_this_user=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='ADM-User Profile-View'
        )
        # verify value
        self.bo_click_tab('General Information')
        if user_code:
            self.bo_assert_text('User Code', user_code)
        if old_user_id:
            self.bo_assert_text('Old User ID', old_user_id)
        if user_name:
            self.bo_assert_text('User Name', user_name)
        if login_name:
            self.bo_assert_text('Login Name', login_name)
        if branch_code:
            self.bo_assert_select('Branch Code', branch_code)
        if department_name:
            self.bo_assert_select('Department Name', department_name)
        self.bo_click_collap('Position')
        if cashier is not None:
            self.bo_assert_checkbox_multi('Position', 'Cashier', cashier)
        if officer is not None:
            self.bo_assert_checkbox_multi('Position', 'Officer', officer)
        if chief_cashier is not None:
            self.bo_assert_checkbox_multi('Position', 'Chief Cashier', chief_cashier)
        if operation_staff is not None:
            self.bo_assert_checkbox_multi('Position', 'Operation Staff', operation_staff)
        if dealer is not None:
            self.bo_assert_checkbox_multi('Position', 'Dealer', dealer)
        if inter_branch_user is not None:
            self.bo_assert_checkbox_multi('Position', 'Inter-branch user', inter_branch_user)
        if branch_manager_authorized is not None:
            self.bo_assert_checkbox_multi('Position', 'Branch Manager/Authorized', branch_manager_authorized)
        if hr is not None:
            self.bo_assert_checkbox_multi('Position', 'HR', hr)
        if email:
            self.bo_assert_value('Email', email)
        if remark:
            self.bo_assert_text('Remark', remark)
        if status_of_this_record:
            self.bo_assert_select('Status Of This Record', status_of_this_record)
        if password:
            self.bo_assert_text('Password', password)
        self.bo_click_tab('Other Information')
        if main_language:
            self.bo_assert_select('Main Language', main_language)
        if user_phone:
            self.bo_assert_text('User Phone', user_phone)
        self.bo_click_collap('Phone Number')
        if home:
            self.bo_assert_text_multi('Phone Number', 'Home', home)
        if office:
            self.bo_assert_text_multi('Phone Number', 'Office', office)
        if cell:
            self.bo_assert_text_multi('Phone Number', 'Cell', cell)
        if facsimile:
            self.bo_assert_text_multi('Phone Number', 'Facsimile', facsimile)
        if telex:
            self.bo_assert_text_multi('Phone Number', 'Telex', telex)
        if time_zone_of_user:
            self.bo_assert_select('Time Zone Of User', time_zone_of_user)
        if thousand_separate_character_in_amount_field:
            self.bo_assert_select('Thousand Separate Character In Amount Field', thousand_separate_character_in_amount_field)
        if decimal_separate_character_in_amount_field:
            self.bo_assert_select('Decimal Separate Character In Amount Field', decimal_separate_character_in_amount_field)
        if date_format_for_short:
            self.bo_assert_select('Date Format For Short', date_format_for_short)
        if long_date_format:
            self.bo_assert_select('Long Date Format', long_date_format)
        if time_format:
            self.bo_assert_select('Time Format', time_format)
        if expire_date_of_this_user:
            self.bo_assert_date('Expire Date Of This User', expire_date_of_this_user)
        if id_of_policy_apply_for_this_user:
            self.bo_assert_select('ID Of Policy Apply For This User', id_of_policy_apply_for_this_user)

    def user_profile_search_verify(self, user_code=None, user_name=None, login_name=None, branch_name=None, department_name=None, status=None, is_online=None, email=None):
        # search and verify
        self.user_profile_simple_search(user_code)
        self.assert_table_data('User Code', 1, user_code)
        if user_name:
            self.assert_table_data('User Name', 1, user_name)
        if login_name:
            self.assert_table_data('Login Name', 1, login_name)
        if branch_name:
            self.assert_table_data('Branch Name', 1, branch_name)
        if department_name:
            self.assert_table_data('Department Name', 1, department_name)
        if status:
            self.assert_table_data('Status', 1, status)
        if is_online:
            self.assert_table_data('Is Online', 1, is_online)
        if email:
            self.assert_table_data('Email', 1, email)

# -------------------------- handle BO - CARDZONE --------------------------
    # Terminal Management - Data Verification
    def terminal_management_add_verify(self, transaction_number, channel=None, terminal_id=None, branch=None, account_number_or_gl=None, terminal_address=None, intelligent_deposit=None, merchant_id=None, status=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Terminal management-Add'
        )
        # verify value
        if channel:
            self.bo_assert_select_single('Channel', channel)
        if terminal_id:
            self.bo_assert_text_single('Terminal ID', terminal_id)
        if branch:
            self.bo_assert_select_single('Branch', branch)
        if account_number_or_gl:
            self.bo_assert_text_single('Account number or GL', account_number_or_gl)
        if terminal_address:
            self.bo_assert_text_single('Terminal address', terminal_address)
        if intelligent_deposit:
            self.bo_assert_select_single('Intelligent deposit', intelligent_deposit)
        if merchant_id:
            self.bo_assert_text_single('Merchant ID', merchant_id)
        if status:
            self.bo_assert_select_single('Status', status)

    def terminal_management_update_verify(self, transaction_number, channel=None, terminal_id=None, branch=None, account_number_or_gl=None, terminal_address=None, intelligent_deposit=None, merchant_id=None, status=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Terminal management-View'
        )
        # verify value
        if channel:
            self.bo_assert_select_single('Channel', channel)
        if terminal_id:
            self.bo_assert_text_single('Terminal ID', terminal_id)
        if branch:
            self.bo_assert_select_single('Branch', branch)
        if account_number_or_gl:
            self.bo_assert_text_single('Account number or GL', account_number_or_gl)
        if terminal_address:
            self.bo_assert_text_single('Terminal address', terminal_address)
        if intelligent_deposit:
            self.bo_assert_select_single('Intelligent deposit', intelligent_deposit)
        if merchant_id:
            self.bo_assert_text_single('Merchant ID', merchant_id)
        if status:
            self.bo_assert_select_single('Status', status)

    def terminal_management_search_verify(self, channel=None, terminal_id=None, branch=None, account_number_or_gl=None, terminal_address=None, intelligent_deposit=None, merchant_id=None, status=None):
        # search and verify
        self.terminal_management_simple_search(terminal_id)
        self.assert_table_data('Terminal ID', 1, terminal_id)
        if channel:
            self.assert_table_data('Channel', 1, channel)
        if branch:
            self.assert_table_data('Branch', 1, branch)
        if account_number_or_gl:
            self.assert_table_data('Account number or GL', 1, account_number_or_gl)
        if terminal_address:
            self.assert_table_data('Terminal address', 1, terminal_address)
        if intelligent_deposit:
            self.assert_table_data('Intelligent deposit', 1, intelligent_deposit)
        if merchant_id:
            self.assert_table_data('Merchant ID', 1, merchant_id)
        if status:
            self.assert_table_data('Status', 1, status)

    # Merchant management - Data Verification
    def merchant_management_add_verify(self, transaction_number, merchant_id=None, merchant_account=None, branch=None, status=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Merchant management-Add'
        )
        # verify value
        if merchant_id:
            self.bo_assert_text_single('Merchant ID', merchant_id)
        if merchant_account:
            self.bo_assert_text_single('Merchant account', merchant_account)
        if branch:
            self.bo_assert_select_single('Branch', branch)
        if status:
            self.bo_assert_select_single('Status', status)

    def merchant_management_update_verify(self, transaction_number, merchant_id=None, merchant_account=None, branch=None, status=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Merchant management-View'
        )
        # verify value
        if merchant_id:
            self.bo_assert_text_single('Merchant ID', merchant_id)
        if merchant_account:
            self.bo_assert_text_single('Merchant account', merchant_account)
        if branch:
            self.bo_assert_select_single('Branch', branch)
        if status:
            self.bo_assert_select_single('Status', status)

    def merchant_management_search_verify(self, merchant_id=None, merchant_account=None, branch=None, status=None):
        # search and verify
        self.merchant_management_simple_search(merchant_id)
        self.assert_table_data('Merchant ID', 1, merchant_id)
        if merchant_account:
            self.assert_table_data('Merchant account', 1, merchant_account)
        if branch:
            self.assert_table_data('Branch', 1, branch)
        if status:
            self.assert_table_data('Status', 1, status)

    # Card Bin Management - Data Verification
    def card_bin_management_add_verify(self, transaction_number, institution_name=None, institution_id=None, bin_name=None, bin_value=None, bin_type=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Card Bin Management-Add'
        )
        # verify value
        if institution_name:
            self.bo_assert_text_single('Institution Name', institution_name)
        if institution_id:
            self.bo_assert_text_single('Institution ID', institution_id)
        if bin_name:
            self.bo_assert_text_single('BIN Name', bin_name)
        if bin_value:
            self.bo_assert_text_single('BIN', bin_value)
        if bin_type:
            self.bo_assert_text_single('Type', bin_type)

    def card_bin_management_update_verify(self, transaction_number, institution_name=None, institution_id=None, bin_name=None, bin_value=None, bin_type=None):
        # open form
        self.bo_approval_view(
            transaction_number=transaction_number,
            form_title='Card Bin Management-View'
        )
        # verify value
        if institution_name:
            self.bo_assert_text_single('Institution Name', institution_name)
        if institution_id:
            self.bo_assert_text_single('Institution ID', institution_id)
        if bin_name:
            self.bo_assert_text_single('BIN Name', bin_name)
        if bin_value:
            self.bo_assert_text_single('BIN', bin_value)
        if bin_type:
            self.bo_assert_text_single('Type', bin_type)

    def card_bin_management_search_verify(self, institution_name=None, institution_id=None, bin_name=None, bin_value=None, bin_type=None):
        # search and verify
        self.card_bin_management_simple_search(institution_id)
        self.assert_table_data('Institution ID', 1, institution_id)
        if institution_name:
            self.assert_table_data('Institution Name', 1, institution_name)
        if bin_name:
            self.assert_table_data('BIN Name', 1, bin_name)
        if bin_value:
            self.assert_table_data('BIN', 1, bin_value)
        if bin_type:
            self.assert_table_data('Type', 1, bin_type)



