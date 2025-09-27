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

    def bo_approval_search_advanced_status(self, transaction_number=None, master_code=None, tran_name=None):
        self.close_all_form()
        self.open_bo_approval()
        self.assert_form_title('FOF-Back Office Approval')
        if transaction_number:
            self.advanced_search_f8('Tran number', transaction_number, field_type='A')
        if master_code:
            self.advanced_search_f8('Master Code', master_code, field_type='A')
        if tran_name:
            self.advanced_search_f8('Tran name', tran_name, field_type='A')
        self.click_button_search_advanced_f8()
        self.wait_loading()

    def bo_approval_search_advanced_normal(self, transaction_number=None, master_code=None, tran_name=None):
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

    def bo_approval_mode_advanced(self, transaction_number=None, master_code=None, tran_name=None, mode=None):
        if mode is None:
            mode = F8Config.view_mode
        if mode=='S':
            self.bo_approval_search_advanced_status(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name)
        if mode=='N':
            self.bo_approval_search_advanced_normal(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name)

    def bo_approval_view(self, transaction_number, form_title=None, mode=None):
        self.bo_approval_mode_simple(transaction_number=transaction_number, mode=mode)
        self.click_table_menu('View', 1)
        self.wait_loading()
        self.check_notification('Get info successfully')
        if form_title:
            self.assert_form_title(form_title)
        self.fo_assert_text('Transaction number', transaction_number)

    def bo_approval_approve(self, username, password, reason=None, list_error_message=None, mode=None, transaction_number=None, master_code=None, tran_name=None):
        self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode)
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
            self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode)
            self.assert_status_table_data('Status', 1, 'Pending to approve')
        else:
            self.check_notification('Approve successfully')
            # search and compare status
            self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode)
            self.assert_status_table_data('Status', 1, 'Completed')

    def bo_approval_reject(self, username, password, reason=None, mode=None, transaction_number=None, master_code=None, tran_name=None):
        self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode)
        self.click_table_menu('Reject', 1)
        self.approve_in_popup(
            username=username,
            password=password,
            reason=reason
        )
        self.wait_loading()
        self.check_notification('Reject successfully')
        # search and compare status
        self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode)
        self.assert_status_table_data('Status', 1, 'Rejected')
        print(f'Transaction number has been rejected: {transaction_number}')

    def check_bo_approval(self, transaction_number=None, master_code=None, tran_name=None, transaction_status=None, mode=None):
        self.bo_approval_mode_advanced(transaction_number=transaction_number, master_code=master_code, tran_name=tran_name, mode=mode)
        if transaction_status:
            transaction_status_actual = self.get_status_table_data('Status', 1)
            if transaction_status==transaction_status_actual:
                return True
            else:
                return False

    def bo_approval_search_verify(self, transaction_number=None, master_code=None, tran_name=None):
        if transaction_number:
            self.assert_table_data('Tran Number', 1, transaction_number)
        if master_code:
            self.assert_table_data('Master Code', 1, master_code)
        if tran_name:
            self.assert_table_data('Tran Name', 1, tran_name)

    def get_transaction_number(self):
        transaction_number = self.bo_get_text_single('Transaction number')
        print(f'Transaction number: {transaction_number}')
        return transaction_number

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
        if debit_accounting:
            self.bo_click_collap('Debit With')
            self.bo_assert_checkbox_multi('Debit With', 'Accounting', debit_accounting)
        if debit_cash:
            self.bo_click_collap('Debit With')
            self.bo_assert_checkbox_multi('Debit With', 'Cash', debit_cash)
        if debit_deposit:
            self.bo_click_collap('Debit With')
            self.bo_assert_checkbox_multi('Debit With', 'Deposit', debit_deposit)
        if credit_accounting:
            self.bo_click_collap('Credit With')
            self.bo_assert_checkbox_multi('Credit With', 'Accounting', credit_accounting)
        if credit_cash:
            self.bo_click_collap('Credit With')
            self.bo_assert_checkbox_multi('Credit With', 'Cash', credit_cash)
        if credit_deposit:
            self.bo_click_collap('Credit With')
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
        if debit_accounting:
            self.bo_click_collap('Debit with ')
            self.bo_assert_checkbox_multi('Debit with ', 'Accounting', debit_accounting)
        if debit_cash:
            self.bo_click_collap('Debit with ')
            self.bo_assert_checkbox_multi('Debit with ', 'Cash', debit_cash)
        if debit_deposit:
            self.bo_click_collap('Debit with ')
            self.bo_assert_checkbox_multi('Debit with ', 'Deposit', debit_deposit)
        if credit_accounting:
            self.bo_click_collap('Credit with')
            self.bo_assert_checkbox_multi('Credit with', 'Accounting', credit_accounting)
        if credit_cash:
            self.bo_click_collap('Credit with')
            self.bo_assert_checkbox_multi('Credit with', 'Cash', credit_cash)
        if credit_deposit:
            self.bo_click_collap('Credit with')
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
            self.bo_assert_value_group('Dormant period', dormant_period)
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
